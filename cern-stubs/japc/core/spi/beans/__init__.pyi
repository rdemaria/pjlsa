import cern.japc.value
import java.io
import typing



class ValueBean:
    """
    Java class 'cern.japc.core.spi.beans.ValueBean'
    
      Attributes:
        NON_MUTABLE_MESSAGE (java.lang.String): final static field
    
    """
    NON_MUTABLE_MESSAGE: typing.ClassVar[str] = ...
    def getParameterValue(self) -> cern.japc.value.ParameterValue: ...
    def isMutable(self) -> bool: ...
    def makeMutable(self) -> None: ...

class ValueBeanImpl(ValueBean, java.io.Serializable):
    """
    Java class 'cern.japc.core.spi.beans.ValueBeanImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.beans.ValueBean, java.io.Serializable
    
      Constructors:
        * ValueBeanImpl(cern.japc.value.ParameterValue)
    
    """
    def __init__(self, parameterValue: cern.japc.value.ParameterValue): ...
    def getParameterValue(self) -> cern.japc.value.ParameterValue: ...
    def isMutable(self) -> bool: ...
    def makeMutable(self) -> None: ...
    def toString(self) -> str: ...

class MapValueBean(ValueBeanImpl):
    """
    Java class 'cern.japc.core.spi.beans.MapValueBean'
    
        Extends:
            cern.japc.core.spi.beans.ValueBeanImpl
    
      Constructors:
        * MapValueBean()
        * MapValueBean(cern.japc.value.MapDescriptor)
        * MapValueBean(cern.japc.value.MapParameterValue)
        * MapValueBean(cern.japc.value.MapParameterValue, cern.japc.value.MapDescriptor)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, mapDescriptor: cern.japc.value.MapDescriptor): ...
    @typing.overload
    def __init__(self, mapParameterValue: cern.japc.value.MapParameterValue): ...
    @typing.overload
    def __init__(self, mapParameterValue: cern.japc.value.MapParameterValue, mapDescriptor: cern.japc.value.MapDescriptor): ...
    def setParameterValue(self, mapParameterValue: cern.japc.value.MapParameterValue) -> None: ...

class SimpleValueBean(ValueBeanImpl):
    """
    Java class 'cern.japc.core.spi.beans.SimpleValueBean'
    
        Extends:
            cern.japc.core.spi.beans.ValueBeanImpl
    
      Constructors:
        * SimpleValueBean()
        * SimpleValueBean(cern.japc.value.SimpleDescriptor)
        * SimpleValueBean(cern.japc.value.SimpleParameterValue)
        * SimpleValueBean(cern.japc.value.SimpleParameterValue, cern.japc.value.SimpleDescriptor)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, simpleDescriptor: cern.japc.value.SimpleDescriptor): ...
    @typing.overload
    def __init__(self, simpleParameterValue: cern.japc.value.SimpleParameterValue): ...
    @typing.overload
    def __init__(self, simpleParameterValue: cern.japc.value.SimpleParameterValue, simpleDescriptor: cern.japc.value.SimpleDescriptor): ...
    def setParameterValue(self, simpleParameterValue: cern.japc.value.SimpleParameterValue) -> None: ...
    @staticmethod
    def validateReader(simpleParameterValue: cern.japc.value.SimpleParameterValue, simpleDescriptor: cern.japc.value.SimpleDescriptor) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.beans")``.

    MapValueBean: typing.Type[MapValueBean]
    SimpleValueBean: typing.Type[SimpleValueBean]
    ValueBean: typing.Type[ValueBean]
    ValueBeanImpl: typing.Type[ValueBeanImpl]
