#!/usr/bin/env python3
"""Stub generator for Java modules, based on mypy stubgenc
"""

import jpype
import jpype.imports
from jpype._pykeywords import pysafe
import importlib
import inspect
import os.path
import re
from typing import List, Optional, Mapping, Any, Set, NamedTuple, Dict
from types import ModuleType
import pathlib


class TypeStr:
    __slots__ = ('name', 'type_args')

    def __init__(self, name: str, type_args: Optional[List['TypeStr']] = None):
        self.name = name
        self.type_args = list(type_args or [])

    def __repr__(self) -> str:
        return "TypeStr(name={}, type_args={})".format(repr(self.name), repr(self.type_args))


TypeVarStr = NamedTuple('TypeVarStr', [
    ('java_name', str),
    ('python_name', str),
    ('bound', Optional[TypeStr])
])

ArgSig = NamedTuple('ArgSig', [
    ('name', str),
    ('type', Optional[TypeStr])
])

JavaFunctionSig = NamedTuple('JavaFunctionSig', [
    ('name', str),
    ('static', bool),
    ('args', List[ArgSig]),
    ('ret_type', TypeStr),
    ('type_vars', List[TypeVarStr])
])


def generate_java_stubs(pkg_prefixes: List[str], use_stub_suffix: bool = True, output_dir: str = '.') -> None:
    packages = {}  # type: Dict[str, List[str]]

    all_classes = find_all_classes()

    for prefix in pkg_prefixes:
        for cls_name in all_classes:
            if not cls_name.startswith(prefix + '.'):
                continue
            pkg_name = cls_name[:cls_name.rfind('.')]
            packages.setdefault(pkg_name, []).append(cls_name)

    for pkg, classes in packages.items():
        print('Generating stubs for %s (%d classes)' % (pkg, len(classes)))
        if '.' in pkg:
            pkg_domain = pkg[:pkg.find('.')]
            if pkg_domain not in jpype.imports._JDOMAINS.keys():
                jpype.imports.registerDomain(pkg_domain)
        importlib.import_module(pkg)
        for cls in classes:
            try:
                importlib.import_module(cls)
            except ImportError:
                print(">> skipping class %s" % cls)
                classes.remove(cls)
        path_parts = pkg.split(".")
        if use_stub_suffix:
            path_parts[0] += "-stubs"
        path = pathlib.Path(output_dir)
        for path_part in path_parts:
            path = path / pysafe(path_part)
            if not path.is_dir():
                os.makedirs(path)
            init_file = path / '__init__.pyi'
            if not init_file.exists():
                open(init_file, "w").close()

        generate_stubs_for_java_package(pkg, path / '__init__.pyi')


def find_all_classes() -> List[str]:
    from java.nio.file import Paths  # noqa
    from java.net import URI  # noqa
    from java.lang import ClassLoader  # noqa
    import zipfile
    class_loader = ClassLoader.getSystemClassLoader()
    jars = [str(Paths.get(u.toURI())) for u in class_loader.getURLs()]  # noqa
    jruntime = str(class_loader.getResource("java/lang/String.class").toURI())
    if jruntime:
        jruntime_uri = URI.create(str(jruntime[4:jruntime.index("!")]))
        jars.append(str(Paths.get(jruntime_uri)))
    classes = []
    for jar in jars:
        if not jar.endswith(".jar"):
            continue
        names = zipfile.ZipFile(jar).namelist()
        for name in names:
            if name.endswith('.class') and '$' not in name:
                classes.append(name[:-6].replace('/', '.'))
    return classes


def generate_stubs_for_java_package(package_name: str, output_file: str) -> None:
    module = importlib.import_module(package_name)
    subdir = os.path.dirname(output_file)
    if subdir and not os.path.isdir(subdir):
        os.makedirs(subdir)
    import_output = []  # type: List[str]
    class_output = []  # type: List[str]
    java_classes = [cls for name, cls in module.__dict__.items() if
                    not is_internal(name) and is_java_class(cls)]  # type: List[jpype.JClass]

    done = set()  # type: Set[str]
    while java_classes:
        java_classes_to_generate = [c for c in java_classes if dependencies_satisfied(module, c, done)]
        if not java_classes_to_generate:
            java_classes_to_generate = java_classes  # some inner class cases - will generate them with full names
        for cls in sorted(java_classes_to_generate, key=lambda c: c.__name__):
            generate_java_class_stub(module.__name__, cls, classes_done=done,
                                     output=class_output, imports_output=import_output)
            java_classes.remove(cls)

    output = []
    for line in sorted(set(import_output)):
        output.append(line)

    output.append('')
    for line in class_output:
        output.append(line)
    output = add_typing_import(output)
    with open(output_file, 'w') as file:
        for line in output:
            file.write('%s\n' % line)


def is_internal(name: str) -> bool:
    if name.startswith('__') and name.endswith('__'):
        return True  # python internal
    if '$' in name:
        return True  # inner class: will be generated recursively
    if '-' in name:
        return True  # package-info et al
    return False


def is_java_class(obj: type) -> bool:
    if not isinstance(obj, jpype.JClass) or not hasattr(obj, 'class_') or not inspect.isclass(obj):
        return False
    # noinspection
    if obj.class_.isAnonymousClass() or obj.class_.isLocalClass() or obj.class_.isSynthetic():  # noqa
        return False
    return True


def dependencies_satisfied(module: ModuleType, jclass: jpype.JClass, done: Set[str]):
    bases = [python_type(b) for b in java_super_types(jclass.class_)]
    for base in bases:
        base_name = base.name
        base_module = base_name[:base_name.rindex('.')]
        if base_module == module.__name__:
            base_local_name = base_name[len(base_module) + 1:]
            if base_local_name not in done:
                return False
    # check dependencies of nested classes
    obj_dict = getattr(jclass, '__dict__')  # type: Mapping[str, Any]  # noqa
    for member in obj_dict.values():
        if is_java_class(member):
            if not dependencies_satisfied(module, member, done):
                return False
    return True


def java_super_types(j_class: Any) -> List[Any]:
    super_types = [j_class.getGenericSuperclass()] + list(j_class.getGenericInterfaces())
    if super_types[0] is None or super_types[0].getTypeName() == 'java.lang.Object':
        del super_types[0]
    return super_types


def add_typing_import(output: List[str]) -> List[str]:
    names = []
    for name in ['Any', 'Union', 'List', 'TypeVar', 'Type', 'ClassVar', 'Generic', 'Set', 'Collection', 'Mapping']:
        if any(re.search(r'\b_py_%s\b' % name, line) for line in output):
            names.append(name)
    if names:
        return ['from typing import {ti} as _py_{ti}'.format(ti=ti_name) for ti_name in names] + output
    else:
        return output[:]


def convert_strings() -> bool:
    if convert_strings.jpype_flag is None:
        from java.lang import String  # noqa
        convert_strings.jpype_flag = isinstance(String().trim(), str)
    return convert_strings.jpype_flag


convert_strings.jpype_flag = None


def translate_type_name(typename: str, type_args: Optional[List[TypeStr]] = None) -> TypeStr:
    if typename == 'void':
        return TypeStr('None')
    if typename in ('byte', 'short', 'int', 'long', 'java.lang.Byte', 'java.lang.Short',
                    'java.lang.Integer', 'java.lang.Long'):
        return TypeStr('int')
    if typename in ('boolean', 'java.lang.Boolean'):
        return TypeStr('bool')
    if typename in ('double', 'float', 'java.lang.Double', 'java.lang.Float'):
        return TypeStr('float')
    if typename in ('char', 'java.lang.Character'):
        return TypeStr('str')  # 1-character string

    if typename == 'java.lang.String' and convert_strings():
        return TypeStr('str')
    if typename == 'java.lang.Class':
        return TypeStr('_py_Type', type_args)
    if typename == 'java.lang.Object':
        return TypeStr('_py_Any')
    return TypeStr(typename, type_args)


def python_type(j_type: Any, type_vars: Optional[List[TypeVarStr]] = None) -> TypeStr:
    from java.lang.reflect import GenericArrayType, ParameterizedType, TypeVariable, WildcardType  # noqa
    if j_type is None:
        return TypeStr('None')
    if type_vars is None:
        type_vars = []
    if isinstance(j_type, ParameterizedType):
        return translate_type_name(j_type.getRawType().getTypeName(),
                                   type_args=[python_type(arg, type_vars) for arg in j_type.getActualTypeArguments()])
    elif isinstance(j_type, TypeVariable):
        j_var_name = j_type.getName()
        matching_vars = [tv for tv in type_vars if tv.java_name == j_var_name]
        if len(matching_vars) == 1:
            return TypeStr(matching_vars[0].python_name)
        j_bound = j_type.getBounds()[0]
        if isinstance(j_bound, ParameterizedType):
            j_bound = j_bound.getRawType()
        return python_type(j_bound, type_vars)
    elif isinstance(j_type, WildcardType):
        j_bound = j_type.getUpperBounds()[0]
        if j_bound.getTypeName() == 'java.lang.Object':
            j_lower_bounds = j_type.getLowerBounds()
            if j_lower_bounds:
                j_bound = j_lower_bounds[0]
        return python_type(j_bound, type_vars)
    elif isinstance(j_type, GenericArrayType):
        return TypeStr('_py_List', [python_type(j_type.getGenericComponentType(), type_vars)])
    else:
        j_raw_type = j_type
        if j_raw_type.isArray():
            return TypeStr('_py_List', [python_type(j_raw_type.getComponentType(), type_vars)])
        return translate_type_name(j_raw_type.getName())


def python_type_var(j_type: Any, uniq_scope_id: str) -> TypeVarStr:
    from java.lang.reflect import TypeVariable, ParameterizedType  # noqa
    if not isinstance(j_type, TypeVariable):
        raise RuntimeError("FIXME: can not convert to type var " + str(j_type))
    j_bound = j_type.getBounds()[0]
    if isinstance(j_bound, ParameterizedType):
        j_bound = j_bound.getRawType()
    bound = python_type(j_bound)
    if bound.name == '_py_Any':
        bound = None  # unbounded
    java_name = j_type.getName()
    return TypeVarStr(java_name=java_name, python_name='_%s__%s' % (uniq_scope_id, java_name), bound=bound)


def infer_argname(j_type: Any, prev_args: List[ArgSig]) -> str:
    if j_type is None:
        return 'arg%d' % len(prev_args)

    typename = str(j_type.getTypeName())
    is_array = typename.endswith('[]')
    typename = typename.split('<')[0].split('$')[-1].split('.')[-1].replace('[]', '')
    typename = typename[:1].lower() + typename[1:]
    if is_array:
        typename += 'Array'
    prev_args_of_type = sum([bool(re.match(typename + '\\d*', prev.name)) for prev in prev_args])
    if prev_args_of_type == 0:
        return typename
    else:
        return typename + str(prev_args_of_type + 1)


def is_static(member: Any) -> bool:
    from java.lang.reflect import Modifier  # noqa
    return member.getModifiers() & Modifier.STATIC > 0


def is_public(member: Any) -> bool:
    from java.lang.reflect import Modifier  # noqa
    return member.getModifiers() & Modifier.PUBLIC > 0


def generate_java_method_stub(parent_name: str,
                              name: str,
                              j_overloads: List[Any],
                              types_done: Set[str],
                              class_type_vars: List[TypeVarStr],
                              output: List[str],
                              imports_output: List[str]) -> None:
    is_constructor = name == '__init__'
    is_overloaded = len(j_overloads) > 1
    signatures = []  # type: List[JavaFunctionSig]
    for i, j_overload in enumerate(j_overloads):
        j_return_type = None if is_constructor else j_overload.getGenericReturnType()
        j_args = j_overload.getParameters()
        static = False if is_constructor else is_static(j_overload)
        method_type_vars = [python_type_var(j_tp, uniq_scope_id='%s_%d' % (name, i) if is_overloaded else name)
                            for j_tp in j_overload.getTypeParameters()]
        usable_type_vars = method_type_vars + class_type_vars if not static else method_type_vars
        args = [ArgSig(name='cls' if static else 'self', type=None)]
        for j_arg in j_args:
            j_arg_type = j_arg.getParameterizedType()
            j_arg_name = j_arg.getName() if j_arg.isNamePresent() else infer_argname(j_arg_type, args)
            args.append(ArgSig(name=j_arg_name, type=python_type(j_arg_type, usable_type_vars)))

        signatures.append(JavaFunctionSig(name, args=args, ret_type=python_type(j_return_type, usable_type_vars),
                                          static=static, type_vars=method_type_vars))

    if is_overloaded:
        imports_output.append('from typing import overload')
    for signature in signatures:
        for type_var in signature.type_vars:
            output.append(to_type_var_declaration(type_var, parent_name, types_done, imports_output))
        if signature.static:
            output.append('@classmethod')
        sig = []
        for arg in signature.args:
            if arg.name in ('self', 'cls'):
                arg_def = arg.name
            else:
                arg_def = pysafe(arg.name)

                if arg.type:
                    arg_def += ": " + to_annotated_type(arg.type, parent_name, types_done, imports_output)

            sig.append(arg_def)

        if is_overloaded:
            output.append('@overload')
        if is_constructor:
            output.append('def __init__({args}): ...'.format(args=", ".join(sig)))
        else:
            output.append('def {function}({args}) -> {ret}: ...'.format(
                function=pysafe(signature.name),
                args=", ".join(sig),
                ret=to_annotated_type(signature.ret_type, parent_name, types_done, imports_output)
            ))


def generate_java_field_stub(parent_name: str,
                             j_field: Any,
                             types_done: Set[str],
                             class_type_vars: List[TypeVarStr],
                             output: List[str],
                             imports_output: List[str]) -> None:
    if not is_public(j_field):
        return
    static = is_static(j_field)
    field_name = j_field.getName()
    field_type = python_type(j_field.getType(), class_type_vars if not static else None)
    field_type_annotation = to_annotated_type(field_type, parent_name, types_done, imports_output,
                                              can_be_deferred=True)
    if static:
        field_type_annotation = '_py_ClassVar[%s]' % field_type_annotation
    output.append('%s: %s = ...' % (pysafe(field_name), field_type_annotation))


def to_annotated_type(type_name: TypeStr, parent_name: str, types_done: Set[str], imports: List[str],
                      can_be_deferred: bool = True, force_short: bool = False) -> str:
    atype = type_name.name
    is_java_type = '.' in atype
    if atype.startswith(parent_name + '$'):
        atype = atype[len(parent_name) + 1:]
    if '.' in atype:
        arg_module = atype[:atype.rindex('.')]
        if arg_module == 'builtins':
            atype = atype[len(arg_module) + 1:]
        elif arg_module == parent_name:
            short_type = atype[len(arg_module) + 1:]
            if short_type in types_done or force_short:
                atype = short_type
            elif can_be_deferred:
                atype = '\'%s\'' % short_type

        else:
            imports.append('import %s' % (arg_module,))
    atype = atype.replace('$', '.')
    if is_java_type:
        atype = ".".join([pysafe(p) for p in atype.split(".")])
    if type_name.type_args:
        return atype + "[" + ", ".join(
            [to_annotated_type(t, parent_name, types_done, imports) for t in type_name.type_args]) + "]"
    else:
        return atype


def to_type_var_declaration(type_var: TypeVarStr, parent_name: str, types_done: Set[str], imports: List[str]) -> str:
    if type_var.bound is not None:
        return '{pyname} = _py_TypeVar(\'{pyname}\', bound={bound})  # <{jname}>'.format(
            pyname=type_var.python_name,
            bound=to_annotated_type(type_var.bound, parent_name, types_done, imports),
            jname=type_var.java_name
        )
    else:
        return '{pyname} = _py_TypeVar(\'{pyname}\')  # <{jname}>'.format(
            pyname=type_var.python_name,
            jname=type_var.java_name
        )


def extra_super_types(class_name: str, class_type_vars: List[TypeVarStr]) -> List[str]:
    if class_name == 'java.util.Map':
        return ['_py_Mapping[%s, %s]' % (class_type_vars[0].python_name, class_type_vars[1].python_name)]
    elif class_name == 'java.util.Collection':
        return ['_py_Collection[%s]' % class_type_vars[0].python_name]
    elif class_name == 'java.util.Set':
        return ['_py_Set[%s]' % class_type_vars[0].python_name]
    elif class_name == 'java.util.List':
        return ['_py_List[%s]' % class_type_vars[0].python_name]
    return []


def generate_java_class_stub(package_name: str,
                             jclass: jpype.JClass,
                             classes_done: Set[str],
                             output: List[str],
                             imports_output: List[str],
                             type_var_output: List[str] = None,
                             parent_class: jpype.JClass = None,
                             parent_class_type_vars: List[TypeVarStr] = None) -> None:
    obj_dict = getattr(jclass, '__dict__')  # type: Mapping[str, Any]  # noqa
    items = sorted(obj_dict.items(), key=lambda x: x[0])

    write_type_vars_to_output = False
    if type_var_output is None:
        write_type_vars_to_output = True
        type_var_output = []  # type: List[str]

    class_uniq_prefix = jclass.class_.getName().replace(package_name + '.', '').replace('.', '_').replace('$', '__')
    class_type_vars = [python_type_var(j_tp, uniq_scope_id=class_uniq_prefix)
                       for j_tp in jclass.class_.getTypeParameters()]
    if parent_class_type_vars is None or is_static(jclass.class_):
        usable_type_vars = class_type_vars
    else:
        usable_type_vars = parent_class_type_vars + class_type_vars
    jclass.class_.getTypeParameters()
    nested_classes_output = []  # type: List[str]
    for attr, value in items:
        if is_java_class(value):
            generate_java_class_stub(package_name, value, classes_done, output=nested_classes_output,
                                     type_var_output=type_var_output, imports_output=imports_output,
                                     parent_class=jclass, parent_class_type_vars=usable_type_vars)

    constructors_output = []  # type: List[str]
    constructors = jclass.class_.getConstructors()
    generate_java_method_stub(package_name, '__init__', constructors, types_done=classes_done,
                              class_type_vars=usable_type_vars,
                              output=constructors_output, imports_output=imports_output)

    methods_output = []  # type: List[str]
    j_overloads = jclass.class_.getMethods()
    for attr, value in items:
        if isinstance(value, jpype.JMethod):
            matching_j_overloads = [j_ov for j_ov in j_overloads if j_ov.getName() == attr]
            generate_java_method_stub(package_name, attr, matching_j_overloads, types_done=classes_done,
                                      class_type_vars=usable_type_vars,
                                      output=methods_output, imports_output=imports_output)

    fields_output = []  # type: List[str]
    j_fields = jclass.class_.getDeclaredFields()
    for j_field in j_fields:
        generate_java_field_stub(package_name, j_field, types_done=classes_done,
                                 class_type_vars=usable_type_vars, output=fields_output, imports_output=imports_output)

    super_types = []
    for super in java_super_types(jclass.class_):
        super_types.append(to_annotated_type(
            python_type(super, usable_type_vars),
            package_name,
            classes_done,
            imports_output,
            can_be_deferred=False
        ))
    if class_type_vars:
        super_types.append('_py_Generic[%s]' % ', '.join([tv.python_name for tv in class_type_vars]))
    super_types = super_types + extra_super_types(jclass.class_.getName(), class_type_vars)
    for type_var in class_type_vars:
        type_var_output.append(to_type_var_declaration(type_var, package_name, classes_done, imports_output))

    bases_str = '(%s)' % ', '.join(super_types) if super_types else ''

    class_name = to_annotated_type(
        TypeStr(jclass.class_.getSimpleName()),  # do not use infer_typename to avoid mangling java.lang classes
        parent_class.class_.getName() if parent_class else package_name,
        classes_done,
        imports_output,
        force_short=True
    )

    if write_type_vars_to_output:
        output.append('')
        output += type_var_output

    if not constructors_output and not methods_output and not fields_output and not nested_classes_output:
        output.append('class %s%s: ...' % (class_name, bases_str))
    else:
        output.append('class %s%s:' % (class_name, bases_str))
        for line in fields_output:
            output.append('    %s' % line)
        for line in constructors_output:
            output.append('    %s' % line)
        for line in methods_output:
            output.append('    %s' % line)
        for line in nested_classes_output:
            output.append('    %s' % line)
    classes_done.add(class_name)
