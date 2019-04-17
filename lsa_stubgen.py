import inspect
import jpype
import pjlsa.domain as mod
from collections import namedtuple
from typing import *
from enum import Enum
import re

stub = open('pjlsa/domain.pyi', 'w')
print('# This stub has been generated by lsa-stubgen', file=stub)
print('# Any manual changes might get overwritten', file=stub)
print('\n', file=stub)
print('from enum import Enum', file=stub)
print('from typing import *', file=stub)
print('\n', file=stub)

TypeInfo = namedtuple('TypeInfo', 'name arguments')
MethodInfo = namedtuple('MethodInfo', 'name returntype paramtypes')
FieldInfo = namedtuple('FieldInfo', 'name type writable')
JClassInfo = namedtuple('JClassInfo', 'name superclass interfaces methods fields')
EnumInfo = namedtuple('EnumInfo', 'name superclass items')


def jtype(jt):
    if hasattr(jt, 'getRawType'):
        return TypeInfo(name=jt.getRawType().getName(),
                        arguments=[t.getName() if hasattr(t, 'getName') else None for t in jt.getActualTypeArguments()])
    else:
        return TypeInfo(name=jt.getName(), arguments=None)


jpype_classes = dict(inspect.getmembers(mod, lambda x: hasattr(x, 'class_')))

class_infos = []
for name, jc in jpype_classes.items():
    jsuper = jc.class_.getSuperclass()
    superclass = jsuper.getName() if jsuper else None
    interfaces = [t.getName() for t in jc.class_.getInterfaces()]
    methods = jpype.reflect.getMethods(jc)
    method_infos = []
    for method in methods:
        m_name = method.getName()
        m_returntype = jtype(method.getGenericReturnType())
        m_paramtypes = [jtype(t) for t in method.getGenericParameterTypes()]
        method_infos.append(MethodInfo(m_name, m_returntype, m_paramtypes))
    class_infos.append(JClassInfo(name, superclass, interfaces, method_infos, fields=[]))

builtins = {'java.lang.Boolean': bool, 'boolean': bool,
            'java.lang.Integer': int, 'java.lang.Long': int, 'int': int, 'long': int,
            'java.lang.Float': float, 'java.lang.Double': float, 'float': float, 'double': float,
            'java.lang.String': str, 'void': None}

class_aliases = {v.class_.getName(): v for k, v in jpype_classes.items()}

print(class_infos)


def resolve_type_info(tinfo: TypeInfo, extra_mappings={}, extra_mappings_generic={}) -> Type:
    if tinfo.arguments:
        if tinfo.name in extra_mappings_generic:
            return extra_mappings_generic.__getitem__(*tinfo.arguments)
    else:
        if tinfo.name in class_aliases:
            return class_aliases[tinfo.name]
        elif tinfo.name in builtins:
            return builtins[tinfo.name]
        elif tinfo.name in extra_mappings:
            return extra_mappings[tinfo.name]
        else:
            return Any


def post_process(ji: JClassInfo) -> JClassInfo:
    mapped_types_gen = {'java.util.List': List,
                        'java.util.Collection': List,
                        'java.util.Set': Set,
                        'java.util.Map': Mapping,
                        'java.util.Optional': Optional}
    getters = {re.sub('^(get|is)(.)(.*)', lambda g: g.group(2).lower() + g.group(3), m.name): m
               for m in ji.methods if m.name.startswith('get') or m.name.startswith('is')}
    setters = {re.sub('^(set)(.)(.*)', lambda g: g.group(2).lower() + g.group(3), m.name): m
               for m in ji.methods if m.name.startswith('set')}

    properties = []
    for fn, getter in getters.items():
        if getter.paramtypes:
            continue
        ji.methods.remove(getters[fn])
        ji.methods.append(getters[fn]._replace(name='_' + getters[fn].name))
        has_setter = False
        if fn in setters:
            has_setter = True
            ji.methods.remove(setters[fn])
            ji.methods.append(setters[fn]._replace(name='_' + getters[fn].name))
        fieldtype = resolve_type_info(getter.returntype, extra_mappings_generic=mapped_types_gen)
        properties.append(FieldInfo(name=fn, type=fieldtype, writable=has_setter))

    print(properties)


post_process(class_infos[0])

wrapped_enums = dict(inspect.getmembers(mod, lambda x: hasattr(x, '__members__')))

enum_infos = []
for name, enum in wrapped_enums.items():
    mro = inspect.getmro(enum)
    if mro[-2] is not Enum:
        continue
    superclass = None if mro[1] is Enum else mro[1].__name__
    items = list(enum.__members__.keys())
    enum_infos.append(EnumInfo(name, superclass, items))

print('###### Enum SuperClasses ######', file=stub)
for enum_superclass in set(e.superclass for e in enum_infos if e.superclass is not None):
    print('class {0}:'.format(enum_superclass), file=stub)
    print('    @classmethod', file=stub)
    print('    def of(cls, item: Union[{0}, str]) -> {0}: ...'.format(enum_superclass), file=stub)
    print('\n', file=stub)

print('###### Enums ######', file=stub)
for enum_info in enum_infos:
    sc = ['Enum']
    if enum_info.superclass is not None:
        sc.append(enum_info.superclass)
    print('class {0}({1}):'.format(enum_info.name, ', '.join(sc)), file=stub)
    for item in enum_info.items:
        print('    {0}: {1} = ...'.format(item, enum_info.name), file=stub)
    print('\n', file=stub)

print(enum_infos)
