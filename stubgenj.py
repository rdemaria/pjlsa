#!/usr/bin/env python3
"""Stub generator for Java modules, based on mypy stubgenc
"""

import jpype
import jpype.imports
import importlib
import inspect
import os.path
import re
from typing import List, Dict, Tuple, Optional, Mapping, Any, Set, NamedTuple, TypeVar
from types import ModuleType

from mypy.stubdoc import is_valid_type

_TypeStr = TypeVar('_TypeStr', bound='TypeStr')


class TypeStr:
    __slots__ = ('name', 'type_args')

    def __init__(self, name: str, type_args: Optional[List[_TypeStr]] = None):
        if name and not is_valid_type(name):
            raise ValueError("Invalid type: " + name)
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


def generate_stub_for_java_module(module_name: str, target: str) -> None:
    """Generate stub for a Java module/package.

    This combines simple runtime introspection (looking for docstrings and attributes
    with simple builtin types) and signatures inferred from .rst documentation (if given).

    If directory for target doesn't exist it will be created. Existing stub
    will be overwritten.
    """
    module = importlib.import_module(module_name)
    subdir = os.path.dirname(target)
    if subdir and not os.path.isdir(subdir):
        os.makedirs(subdir)
    imports = []  # type: List[str]
    done = set()  # type: Set[str]
    java_classes = {name: cls for name, cls in module.__dict__.items()
                    if not is_internal(name) and is_java_class(cls)}
    classes = []  # type: List[str]

    while java_classes:
        java_classes_to_generate = classes_with_satisfied_dependencies(module, java_classes, done)
        if not java_classes_to_generate:
            raise RuntimeError("Could not resolve inheritance dependencies for classes %s" % java_classes)
        for name, obj in sorted(java_classes_to_generate.items(), key=lambda x: x[0]):
            generate_java_class_stub(module, name, obj, classes_done=done, output=classes, imports=imports)
            done.add(name)
            del java_classes[name]

    output = []
    for line in sorted(set(imports)):
        output.append(line)

    output.append('')
    for line in classes:
        if line.startswith('class') and output and output[-1]:
            output.append('')
        output.append(line)
    output = add_typing_import(output)
    with open(target, 'w') as file:
        for line in output:
            file.write('%s\n' % line)


def is_internal(name: str) -> bool:
    return name.startswith('__') and name.endswith('__')


def classes_with_satisfied_dependencies(module: ModuleType, cls: Dict[str, type], done: Set[str]) -> Dict[str, type]:
    return {name: cls for name, cls in cls.items() if dependencies_satisfied(module, cls, done)}


def dependencies_satisfied(module: ModuleType, cls: type, done: Set[str]):
    bases = [type_to_typestr(b) for b in cls.mro()][1:]
    for base in bases:
        base_name = base.name
        base_module = base_name[:base_name.rindex('.')]
        if base_module == module.__name__:
            base_local_name = base_name[len(base_module) + 1:]
            if base_local_name not in done:
                return False
    return True


def add_typing_import(output: List[str]) -> List[str]:
    """Add typing imports for collections/types that occur in the generated stub."""
    names = []
    for name in ['Any', 'Union', 'Tuple', 'Optional', 'List', 'Dict', 'TypeVar']:
        if any(re.search(r'\b%s\b' % name, line) for line in output):
            names.append(name)
    if names:
        return ['from typing import %s' % ', '.join(names), ''] + output
    else:
        return output[:]


def is_java_class(obj: object) -> bool:
    return inspect.isclass(obj) and hasattr(obj, 'class_')


def is_java_method(obj: object) -> bool:
    return inspect.ismethoddescriptor(obj) or type(obj) in (type(str.index),
                                                            type(str.__add__),
                                                            type(str.__new__),
                                                            jpype.JMethod)


def is_java_static(java_overload: Any) -> bool:
    from java.lang.reflect import Modifier
    return java_overload.getModifiers() & Modifier.STATIC > 0


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
    if typename == 'java.lang.String':
        return TypeStr('str')
    return TypeStr(typename.replace('$', '__'))


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


def generate_java_method_stub(module: ModuleType,
                              name: str,
                              obj: object,
                              overloads: List[Any],
                              types_done: Set[str],
                              output: List[str],
                              imports: List[str]) -> None:
    """Generate stub for a single method.

    The result (always a single line) will be appended to 'output'.
    If necessary, any required names will be added to 'imports'.
    """

    signatures = []
    for overload in overloads:
        j_return_type = overload.getReturnType()
        j_args = overload.getParameterTypes()
        static = is_java_static(overload)
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
                        arg_def += ": " + to_annotated_type(arg.type, module, types_done, imports)

                sig.append(arg_def)

            if is_overloaded:
                output.append('@overload')
            output.append('def {function}({args}) -> {ret}: ...'.format(
                function=name,
                args=", ".join(sig),
                ret=to_annotated_type(signature.ret_type, module, types_done, imports)
            ))


def to_annotated_type(type_name: TypeStr, module: ModuleType, types_done: Set[str], imports: List[str],
                      can_be_deferred: bool = True) -> str:
    atype = type_name.name
    if '.' in atype:
        arg_module = atype[:atype.rindex('.')]
        if arg_module == 'builtins':
            atype = atype[len(arg_module) + 1:]
        elif arg_module == module.__name__:
            atype = atype[len(arg_module) + 1:]
            if can_be_deferred and atype not in types_done:
                atype = '\'%s\'' % atype

        else:
            imports.append('import %s' % (arg_module,))
    if type_name.type_args:
        return atype + "[" + ", ".join(
            [to_annotated_type(t, module, types_done, imports) for t in type_name.type_args]) + "]"
    else:
        return atype


def generate_java_class_stub(module: ModuleType,
                             class_name: str,
                             obj: type,
                             classes_done: Set[str],
                             output: List[str],
                             imports: List[str]) -> None:
    """Generate stub for a single class using runtime introspection.

    The result lines will be appended to 'output'. If necessary, any
    required names will be added to 'imports'.
    """
    obj_dict = getattr(obj, '__dict__')  # type: Mapping[str, Any]  # noqa
    items = sorted(obj_dict.items(), key=lambda x: method_name_sort_key(x[0]))
    methods = []  # type: List[str]
    properties = []  # type: List[str]
    done = set()  # type: Set[str]
    overloads = obj.class_.getMethods()
    for attr, value in items:
        if is_java_method(value):
            done.add(attr)
            if not is_skipped_attribute(attr):
                matching_overloads = [ov for ov in overloads if ov.getName() == attr]
                generate_java_method_stub(module, attr, value, matching_overloads, types_done=classes_done,
                                          output=methods, imports=imports)

    variables = []
    for attr, value in items:
        if is_skipped_attribute(attr):
            continue
        if attr not in done:
            variables.append('%s: Any = ...' % attr)
    all_bases = list(obj.mro())
    if all_bases[-1] is object:
        del all_bases[-1]
    if all_bases[-1].__module__ == '_jpype' and all_bases[-1].__name__ == '_JObject':
        del all_bases[-1]
    if 'java.lang.Object' in all_bases[-1].__name__:
        del all_bases[-1]
    # remove the class itself
    all_bases = all_bases[1:]
    # Remove base classes of other bases as redundant.
    bases = []  # type: List[type]
    for base in all_bases:
        if not any(issubclass(b, base) for b in bases):
            bases.append(base)
    if bases:
        bases_str = '(%s)' % ', '.join(
            to_annotated_type(
                type_to_typestr(base),
                module,
                classes_done,
                imports,
                can_be_deferred=False
            ) for base in bases
        )
    else:
        bases_str = ''
    if not methods and not variables and not properties:
        output.append('class %s%s: ...' % (class_name, bases_str))
    else:
        output.append('class %s%s:' % (class_name, bases_str))
        for variable in variables:
            output.append('    %s' % variable)
        for method in methods:
            output.append('    %s' % method)
        for prop in properties:
            output.append('    %s' % prop)


def type_to_typestr(typ: type) -> TypeStr:
    if typ.__module__ == 'jpype._jclass':
        return TypeStr(typ.__name__)
    return TypeStr('%s.%s' % (typ.__module__, typ.__name__))


def method_name_sort_key(name: str) -> Tuple[int, str]:
    """Sort methods in classes in a typical order.

    I.e.: constructor, normal methods, special methods.
    """
    if name in ('__new__', '__init__'):
        return 0, name
    if name.startswith('__') and name.endswith('__'):
        return 2, name
    return 1, name


def is_skipped_attribute(attr: str) -> bool:
    return attr in ('__getattribute__',
                    '__str__',
                    '__repr__',
                    '__doc__',
                    '__dict__',
                    '__module__',
                    '__weakref__')  # For pickling
