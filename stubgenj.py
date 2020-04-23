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
    forward_decls = [] # type: List[str]
    done = set() # type: Set[str]
    items = sorted(module.__dict__.items(), key=lambda x: x[0])
    classes = []  # type: List[str]
    for name, obj in items:
        if name.startswith('__') and name.endswith('__'):
            continue
        if is_java_class(obj):
            generate_java_class_stub(module, name, obj, done=done, output=classes, imports=imports, forward_decls=forward_decls)
            done.add(name)

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


def add_typing_import(output: List[str]) -> List[str]:
    """Add typing imports for collections/types that occur in the generated stub."""
    names = []
    for name in ['Any', 'Union', 'Tuple', 'Optional', 'List', 'Dict']:
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
                        arg_def += ": " + strip_or_import(arg.type, module, imports)

                sig.append(arg_def)

            if is_overloaded:
                output.append('@overload')
            output.append('def {function}({args}) -> {ret}: ...'.format(
                function=name,
                args=", ".join(sig),
                ret=strip_or_import(signature.ret_type, module, imports)
            ))


def strip_or_import(type_name: TypeStr, module: ModuleType, imports: List[str]) -> str:
    """Strips unnecessary module names from type_name.

    If typ represents a type that is inside module or is a type coming from builtins, remove
    module declaration from it. Return stripped name of the type.

    Arguments:
        type_name: name of the type
        module: in which this type is used
        imports: list of import statements (may be modified during the call)
    """
    stripped_type = type_name.name
    if '.' in stripped_type:
        arg_module = stripped_type[:stripped_type.rindex('.')]
        if arg_module in ('builtins', module.__name__):
            stripped_type = stripped_type[len(arg_module) + 1:]
        else:
            imports.append('import %s' % (arg_module,))
    if type_name.type_args:
        return stripped_type + "[" + ", ".join([strip_or_import(t, module, imports) for t in type_name.type_args]) + "]"
    else:
        return stripped_type


def generate_java_class_stub(module: ModuleType,
                             class_name: str,
                             obj: type,
                             done: Set[str],
                             output: List[str],
                             imports: List[str],
                             forward_decls: List[str]) -> None:
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
                generate_java_method_stub(module, attr, value, matching_overloads, output=methods, imports=imports)

    variables = []
    for attr, value in items:
        if is_skipped_attribute(attr):
            continue
        if attr not in done:
            variables.append('%s: Any = ...' % attr)
    all_bases = list(obj.mro())
    if all_bases[-1] is object:
        del all_bases[-1]
    # remove pybind11_object. All classes generated by pybind11 have pybind11_object in their MRO,
    # which only overrides a few functions in object type
    if all_bases and all_bases[-1].__name__ == 'pybind11_object':
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
            strip_or_import(
                type_to_typestr(base),
                module,
                imports
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
    if typ.__module__ == '_jpype' and typ.__name__ == '_JObject':
        return TypeStr('')
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
