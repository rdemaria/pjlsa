#!/usr/bin/env python3
"""Stub generator for Java modules, based on mypy stubgenc
"""

import jpype
import jpype.imports
import importlib
import inspect
import os.path
import re
from typing import List, Tuple, Optional, Mapping, Any, Set, NamedTuple, Dict
from types import ModuleType
import pathlib


class TypeStr:
    __slots__ = ('name', 'type_args')

    def __init__(self, name: str, type_args: Optional[List['TypeStr']] = None):
        self.name = name
        self.type_args = list(type_args or [])

    def __repr__(self) -> str:
        return "TypeStr(name={}, type_args={})".format(repr(self.name), repr(self.type_args))


ArgSig = NamedTuple('ArgSig', [
    ('name', str),
    ('type', Optional[TypeStr])
])

JavaFunctionSig = NamedTuple('JavaFunctionSig', [
    ('name', str),
    ('static', bool),
    ('args', List[ArgSig]),
    ('ret_type', TypeStr)
])


def generate_java_stubs(pkg_prefixes: List[str], output_dir_prefix: str = 'pyi') -> None:
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
        path = pathlib.Path(output_dir_prefix)
        for path_part in path_parts:
            path = path / path_part
            if not path.is_dir():
                os.makedirs(path)
            init_file = path / '__init__.pyi'
            if not init_file.exists():
                open(init_file, "w").close()

        generate_stubs_for_java_package(pkg, path / '__init__.pyi')


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
        if line.startswith('class') and output and output[-1]:
            output.append('')
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
    bases = [infer_typename(b.class_) for b in jclass.mro() if is_java_class(b)][1:]
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


def add_typing_import(output: List[str]) -> List[str]:
    names = []
    for name in ['Any', 'Union', 'Tuple', 'Optional', 'List', 'Dict', 'TypeVar', 'Type', 'ClassVar']:
        if any(re.search(r'\b%s\b' % name, line) for line in output):
            names.append(name)
    if names:
        return ['from typing import %s' % ', '.join(names), ''] + output
    else:
        return output[:]


def convert_strings() -> bool:
    if convert_strings.jpype_flag is None:
        from java.lang import String  # noqa
        convert_strings.jpype_flag = isinstance(String().trim(), str)
    return convert_strings.jpype_flag


convert_strings.jpype_flag = None


def infer_typename(jtype: Any) -> TypeStr:
    if jtype is None:
        return TypeStr('None')
    if jtype.isArray():
        return TypeStr('List', [infer_typename(jtype.getComponentType())])
    typename = jtype.getName()

    if jtype.isPrimitive():
        if typename == 'void':
            return TypeStr('None')
        if typename in ('byte', 'short', 'int', 'long'):
            return TypeStr('int')
        if typename == 'boolean':
            return TypeStr('bool')
        if typename in ('double', 'float'):
            return TypeStr('float')
        if typename == 'char':
            return TypeStr('str')  # 1-character string
    if typename == 'java.lang.String' and convert_strings():
        return TypeStr('str')
    if typename == 'java.lang.Class':
        return TypeStr('Type')
    return TypeStr(typename)


def infer_argname(jtype: Any, prev_args: List[ArgSig]) -> str:
    import keyword
    if jtype is None:
        return 'arg%d' % len(prev_args)
    typename = jtype.getSimpleName().split('$')[-1].replace('[]', 'Array')
    typename = typename[:1].lower() + typename[1:]
    if keyword.iskeyword(typename):
        typename = 'java' + typename.capitalize()
    prev_args_of_type = sum([bool(re.match(typename + '\\d*', prev.name)) for prev in prev_args])
    if prev_args_of_type == 0:
        return typename
    else:
        return typename + str(prev_args_of_type + 1)


def is_static(java_overload: Any) -> bool:
    from java.lang.reflect import Modifier  # noqa
    return java_overload.getModifiers() & Modifier.STATIC > 0


def is_public(member: Any) -> bool:
    from java.lang.reflect import Modifier  # noqa
    return member.getModifiers() & Modifier.PUBLIC > 0


def generate_java_method_stub(parent_name: str,
                              name: str,
                              overloads: List[Any],
                              types_done: Set[str],
                              output: List[str],
                              imports: List[str]) -> None:
    is_constructor = name == '__init__'
    signatures = []
    for overload in overloads:
        j_return_type = None if is_constructor else overload.getReturnType()
        j_args = overload.getParameterTypes()
        static = False if is_constructor else is_static(overload)
        args = [ArgSig(name='cls' if static else 'self', type=None)]
        for arg_num, j_arg in enumerate(j_args):
            args.append(ArgSig(name=infer_argname(j_arg, args), type=infer_typename(j_arg)))

        signatures.append(JavaFunctionSig(name, args=args, ret_type=infer_typename(j_return_type), static=static))

    is_overloaded = len(signatures) > 1 if signatures else False
    if is_overloaded:
        imports.append('from typing import overload')
    if signatures:
        for signature in signatures:
            if signature.static:
                output.append('@classmethod')
            sig = []
            for arg in signature.args:
                if arg.name in ('self', 'cls'):
                    arg_def = arg.name
                else:
                    arg_def = arg.name
                    if arg_def == 'None':
                        arg_def = '_none'  # None is not a valid argument name

                    if arg.type:
                        arg_def += ": " + to_annotated_type(arg.type, parent_name, types_done, imports)

                sig.append(arg_def)

            if is_overloaded:
                output.append('@overload')
            output.append('def {function}({args}) -> {ret}: ...'.format(
                function=name,
                args=", ".join(sig),
                ret=to_annotated_type(signature.ret_type, parent_name, types_done, imports)
            ))


def generate_java_field_stub(parent_name: str,
                             field: Any,
                             types_done: Set[str],
                             output: List[str],
                             imports: List[str]) -> None:
    if not is_public(field):
        return  # private field
    field_name = field.getName()
    field_type = infer_typename(field.getType())
    field_type_annotation = to_annotated_type(field_type, parent_name, types_done, imports, True)
    if is_static(field):
        field_type_annotation = 'ClassVar[%s]' % field_type_annotation
    output.append('%s: %s = ...' % (field_name, field_type_annotation))


def to_annotated_type(type_name: TypeStr, parent_name: str, types_done: Set[str], imports: List[str],
                      can_be_deferred: bool = True, force_short: bool = False) -> str:
    atype = type_name.name
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
    if type_name.type_args:
        return atype + "[" + ", ".join(
            [to_annotated_type(t, parent_name, types_done, imports) for t in type_name.type_args]) + "]"
    else:
        return atype


def generate_java_class_stub(package_name: str,
                             jclass: jpype.JClass,
                             classes_done: Set[str],
                             output: List[str],
                             imports_output: List[str],
                             parent_class: jpype.JClass = None) -> None:
    """Generate stub for a single class using runtime introspection.

    The result lines will be appended to 'output'. If necessary, any
    required names will be added to 'imports'.
    """
    obj_dict = getattr(jclass, '__dict__')  # type: Mapping[str, Any]  # noqa
    items = sorted(obj_dict.items(), key=lambda x: method_name_sort_key(x[0]))
    done = set()  # type: Set[str]
    nested_classes_output = []  # type: List[str]
    for attr, value in items:
        if is_java_class(value):
            done.add(attr)
            generate_java_class_stub(package_name, value, classes_done, output=nested_classes_output,
                                     imports_output=imports_output, parent_class=jclass)

    constructors_output = []  # type: List[str]
    constructors = jclass.class_.getConstructors()
    generate_java_method_stub(package_name, '__init__', constructors, types_done=classes_done,
                              output=constructors_output, imports=imports_output)
    done.add('__init__')

    methods_output = []  # type: List[str]
    overloads = jclass.class_.getMethods()
    for attr, value in items:
        if isinstance(value, jpype.JMethod):
            done.add(attr)
            matching_overloads = [ov for ov in overloads if ov.getName() == attr]
            generate_java_method_stub(package_name, attr, matching_overloads, types_done=classes_done,
                                      output=methods_output, imports=imports_output)

    fields_output = []
    fields = jclass.class_.getDeclaredFields()
    for field in fields:
        generate_java_field_stub(package_name, field, types_done=classes_done,
                                 output=fields_output, imports=imports_output)

    all_bases = list(jclass.mro())
    if all_bases[-1] is object:
        del all_bases[-1]
    if all_bases[-1].__module__ == '_jpype' and all_bases[-1].__name__ == '_JObject':
        del all_bases[-1]
    if 'java.lang.Object' in all_bases[-1].__name__:
        del all_bases[-1]
    # remove the class itself
    all_bases = all_bases[1:]
    # Remove base classes of other bases as redundant.
    bases = []  # type: List[jpype.JClass]
    for base in all_bases:
        if not any(issubclass(b, base) for b in bases) and is_java_class(base):
            bases.append(base)
    if bases:
        bases_str = '(%s)' % ', '.join(
            to_annotated_type(
                infer_typename(base.class_),
                package_name,
                classes_done,
                imports_output,
                can_be_deferred=False
            ) for base in bases
        )
    else:
        bases_str = ''
    class_name = to_annotated_type(
        infer_typename(jclass.class_),
        parent_class.class_.getName() if parent_class else package_name,
        classes_done,
        imports_output,
        force_short=True
    )
    if not constructors_output and not methods_output and not fields_output and not nested_classes_output:
        output.append('class %s%s: ...' % (class_name, bases_str))
    else:
        output.append('class %s%s:' % (class_name, bases_str))
        for line in constructors_output:
            output.append('    %s' % line)
        for line in fields_output:
            output.append('    %s' % line)
        for line in methods_output:
            output.append('    %s' % line)
        for line in nested_classes_output:
            output.append('    %s' % line)
    classes_done.add(class_name)


def method_name_sort_key(name: str) -> Tuple[int, str]:
    if name in ('__new__', '__init__'):
        return 0, name
    if name.startswith('__') and name.endswith('__'):
        return 2, name
    return 1, name


def is_skipped_member(attr: str) -> bool:
    return attr in ('__getattribute__',
                    '__str__',
                    '__repr__',
                    '__doc__',
                    '__dict__',
                    '__module__',
                    '__weakref__')  # For pickling


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
