import inspect
import jpype
import pjlsa.domain as mod
from collections import namedtuple
from typing import *
from enum import Enum

JType = namedtuple('JType', 'name, arguments')
JMethodInfo = namedtuple('JMethodInfo', 'name, returntype, paramtypes')
JClassInfo = namedtuple('JClassInfo', 'name, superclass, interfaces, methods')
EnumInfo = namedtuple('EnumInfo', 'name, superclass, items')


def jtype(jt):
    if hasattr(jt, 'getRawType'):
        return JType(name=jt.getRawType().getName(),
                     arguments=[t.getName() if hasattr(t, 'getName') else None for t in jt.getActualTypeArguments()])
    else:
        return JType(name=jt.getName(), arguments=None)


jpype_classes = dict(inspect.getmembers(mod, lambda x: hasattr(x, 'class_')))

class_infos = []
for name, jc in jpype_classes.items():
    jsuper = jc.class_.getSuperclass()
    superclass = jsuper.getName() if jsuper else None
    interfaces = [t.getName() for t in mod.BeamProcessType.class_.getInterfaces()]
    methods = jpype.reflect.getMethods(jc)
    method_infos = []
    for method in methods:
        m_name = method.getName()
        m_returntype = jtype(method.getGenericReturnType())
        m_paramtypes = [jtype(t) for t in method.getGenericParameterTypes()]
        method_infos.append(JMethodInfo(m_name, m_returntype, m_paramtypes))
    class_infos.append(JClassInfo(name, superclass, interfaces, method_infos))

builtins = {'java.lang.Boolean': bool, 'boolean': bool,
            'java.lang.Integer': int, 'java.lang.Long': int, 'int': int, 'long': int,
            'java.lang.Float': float, 'java.lang.Double': float, 'float': float, 'double': float,
            'java.lang.String': str, 'void': None}

builtins_generic = {'java.util.List': List, 'java.util.Collection': Iterable, 'java.util.Set': Set,
                    'java.util.Map': Mapping}

class_aliases = {v.class_.getName(): k for k, v in jpype_classes.items()}

print(class_infos)

wrapped_enums = dict(inspect.getmembers(mod, lambda x: hasattr(x, '__members__')))

enum_infos = []
for name, enum in wrapped_enums.items():
    mro = inspect.getmro(enum)
    if mro[-2] is not Enum:
        continue
    superclass = None if mro[1] is Enum else mro[1].__name__
    items = list(enum.__members__.keys())
    enum_infos.append(EnumInfo(name, superclass, items))

print(enum_infos)
