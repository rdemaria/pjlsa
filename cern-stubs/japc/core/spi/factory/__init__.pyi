import cern.japc.core
import cern.japc.core.factory
import cern.japc.core.spi
import cern.japc.core.spi.factory.impl
import cern.japc.core.transaction
import cern.japc.value
import java.io
import java.util
import typing



class InternalParameterCharacteristics(cern.japc.core.factory.ParameterCharacteristicsImpl, cern.japc.core.ParameterCharacteristics, java.io.Serializable):
    """
    Java class 'cern.japc.core.spi.factory.InternalParameterCharacteristics'
    
        Extends:
            cern.japc.core.factory.ParameterCharacteristicsImpl
    
        Interfaces:
            cern.japc.core.ParameterCharacteristics, java.io.Serializable
    
      Constructors:
        * InternalParameterCharacteristics(cern.japc.core.ParameterCharacteristics)
    
    """
    def __init__(self, parameterCharacteristics: cern.japc.core.ParameterCharacteristics): ...
    def decreaseCreatingCompositeParameter(self) -> None: ...
    def increaseCreatingCompositeParameter(self) -> None: ...
    def isCreatingCompositeParameter(self) -> bool: ...
    def toString(self) -> str: ...

class ParameterCreator:
    """
    Java class 'cern.japc.core.spi.factory.ParameterCreator'
    
      Attributes:
        SERVICE_NAME_PROPERTY (java.lang.String): final static field
        PROTOCOL_PROPERTY (java.lang.String): final static field
        CREATOR_CLASS_PROPERTY (java.lang.String): final static field
        DEFAULT_PROPERTY (java.lang.String): final static field
    
    """
    SERVICE_NAME_PROPERTY: typing.ClassVar[str] = ...
    PROTOCOL_PROPERTY: typing.ClassVar[str] = ...
    CREATOR_CLASS_PROPERTY: typing.ClassVar[str] = ...
    DEFAULT_PROPERTY: typing.ClassVar[str] = ...
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory) -> cern.japc.core.transaction.TransactionalParameter: ...

class ServiceConfigLookup:
    """
    Java class 'cern.japc.core.spi.factory.ServiceConfigLookup'
    
    """
    def getConfig(self, string: str) -> typing.List[java.util.Properties]: ...

class AdvancedParameterCreator(ParameterCreator):
    """
    Java class 'cern.japc.core.spi.factory.AdvancedParameterCreator'
    
        Interfaces:
            cern.japc.core.spi.factory.ParameterCreator
    
    """
    @typing.overload
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory, internalParameterCharacteristics: InternalParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory) -> cern.japc.core.transaction.TransactionalParameter: ...

class CompositeParameterCreator(AdvancedParameterCreator):
    """
    Java class 'cern.japc.core.spi.factory.CompositeParameterCreator'
    
        Interfaces:
            cern.japc.core.spi.factory.AdvancedParameterCreator
    
    """
    def isKnownCompositeParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.factory")``.

    AdvancedParameterCreator: typing.Type[AdvancedParameterCreator]
    CompositeParameterCreator: typing.Type[CompositeParameterCreator]
    InternalParameterCharacteristics: typing.Type[InternalParameterCharacteristics]
    ParameterCreator: typing.Type[ParameterCreator]
    ServiceConfigLookup: typing.Type[ServiceConfigLookup]
    impl: cern.japc.core.spi.factory.impl.__module_protocol__
