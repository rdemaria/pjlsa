import cern.japc.value
import java.io
import typing



class TypedObject(java.io.Serializable):
    """
    Java class 'cern.japc.value.spi.value.core.TypedObject'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
    """
    def getType(self) -> cern.japc.value.Type: ...

class AbstractValueDescriptor(TypedObject, cern.japc.value.ValueDescriptor, java.io.Serializable):
    """
    Java class 'cern.japc.value.spi.value.core.AbstractValueDescriptor'
    
        Extends:
            cern.japc.value.spi.value.core.TypedObject
    
        Interfaces:
            cern.japc.value.ValueDescriptor, java.io.Serializable
    
    """
    def getName(self) -> str: ...
    def isConstant(self) -> bool: ...
    def setConstant(self, boolean: bool) -> None: ...
    def setName(self, string: str) -> None: ...

class ParameterValueImpl(TypedObject, cern.japc.value.ParameterValue, java.io.Serializable):
    """
    Java class 'cern.japc.value.spi.value.core.ParameterValueImpl'
    
        Extends:
            cern.japc.value.spi.value.core.TypedObject
    
        Interfaces:
            cern.japc.value.ParameterValue, java.io.Serializable
    
      Constructors:
        * ParameterValueImpl(cern.japc.value.Type, cern.japc.value.ValueDescriptor)
        * ParameterValueImpl(cern.japc.value.Type)
    
    """
    @typing.overload
    def __init__(self, type: cern.japc.value.Type): ...
    @typing.overload
    def __init__(self, type: cern.japc.value.Type, valueDescriptor: cern.japc.value.ValueDescriptor): ...
    def clone(self) -> typing.Any: ...
    def getDescriptor(self) -> cern.japc.value.ValueDescriptor: ...
    def isMutable(self) -> bool: ...
    def makeImmutable(self) -> None: ...
    def makeMutable(self) -> cern.japc.value.ParameterValue: ...
    def setDescriptor(self, valueDescriptor: cern.japc.value.ValueDescriptor) -> None: ...
    def setMutable(self, boolean: bool) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.value.spi.value.core")``.

    AbstractValueDescriptor: typing.Type[AbstractValueDescriptor]
    ParameterValueImpl: typing.Type[ParameterValueImpl]
    TypedObject: typing.Type[TypedObject]
