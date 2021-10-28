import cern.japc.core
import cern.japc.core.spi
import cern.japc.core.spi.provider
import cern.japc.core.transaction
import cern.japc.value
import java.io
import java.lang
import java.util
import typing



class AcquiredParameterValueFactory:
    """
    Java class 'cern.japc.core.factory.AcquiredParameterValueFactory'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    @staticmethod
    def newAcquiredParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, valueHeader: cern.japc.core.ValueHeader) -> cern.japc.core.AcquiredParameterValue: ...
    @typing.overload
    @staticmethod
    def newAcquiredParameterValue(string: str, valueHeader: cern.japc.core.ValueHeader, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.AcquiredParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, valueHeader: cern.japc.core.ValueHeader) -> cern.japc.core.AcquiredParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(string: str, valueHeader: cern.japc.core.ValueHeader, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.AcquiredParameterValue: ...

class FactoryConfigurationError(java.lang.Error):
    """
    Java class 'cern.japc.core.factory.FactoryConfigurationError'
    
        Extends:
            java.lang.Error
    
      Constructors:
        * FactoryConfigurationError(java.lang.String, java.lang.Exception)
        * FactoryConfigurationError(java.lang.Exception)
        * FactoryConfigurationError(java.lang.String)
        * FactoryConfigurationError()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class FailSafeParameterValueFactory:
    """
    Java class 'cern.japc.core.factory.FailSafeParameterValueFactory'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    @staticmethod
    def newFailSafeParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> cern.japc.core.FailSafeParameterValue: ...
    @typing.overload
    @staticmethod
    def newFailSafeParameterValue(string: str, parameterException: cern.japc.core.ParameterException) -> cern.japc.core.FailSafeParameterValue: ...
    @typing.overload
    @staticmethod
    def newFailSafeParameterValue(string: str, valueHeader: cern.japc.core.ValueHeader, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.FailSafeParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(string: str, parameterException: cern.japc.core.ParameterException) -> cern.japc.core.FailSafeParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(string: str, valueHeader: cern.japc.core.ValueHeader, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.FailSafeParameterValue: ...

class IParameterFactory:
    """
    Java class 'cern.japc.core.factory.IParameterFactory'
    
    """
    @typing.overload
    def newParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterCharacteristics: cern.japc.core.ParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str, parameterCharacteristics: cern.japc.core.ParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str, string2: str) -> cern.japc.core.transaction.TransactionalParameter: ...

class MapParameterValueFactory:
    """
    Java class 'cern.japc.core.factory.MapParameterValueFactory'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    @staticmethod
    def newMapParameterValue() -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newMapParameterValue(immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newMapParameterValue(mapDescriptor: cern.japc.value.MapDescriptor) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newMapParameterValue(stringArray: typing.List[str], simpleParameterValueArray: typing.List[cern.japc.value.SimpleParameterValue]) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newMapParameterValue(map: typing.Union[java.util.Map[str, cern.japc.value.SimpleParameterValue], typing.Mapping[str, cern.japc.value.SimpleParameterValue]]) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue() -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(mapDescriptor: cern.japc.value.MapDescriptor) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(stringArray: typing.List[str], simpleParameterValueArray: typing.List[cern.japc.value.SimpleParameterValue]) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(map: typing.Union[java.util.Map[str, cern.japc.value.SimpleParameterValue], typing.Mapping[str, cern.japc.value.SimpleParameterValue]]) -> cern.japc.value.MapParameterValue: ...

class ObjectParameterValueFactory:
    """
    Java class 'cern.japc.core.factory.ObjectParameterValueFactory'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def newObjectParameterValue(object: typing.Any) -> cern.japc.core.ObjectParameterValue: ...
    @staticmethod
    def newValue(object: typing.Any) -> cern.japc.core.ObjectParameterValue: ...

class ParameterCharacteristicsFactory:
    """
    Java class 'cern.japc.core.factory.ParameterCharacteristicsFactory'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ParameterCharacteristicsFactory()
    
    """
    def __init__(self): ...
    @staticmethod
    def getNormalCharacteristics() -> cern.japc.core.ParameterCharacteristics: ...
    @staticmethod
    def getParameterCharacteristics(boolean: bool, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]) -> cern.japc.core.ParameterCharacteristics: ...
    @staticmethod
    def getWildcardCharacteristics() -> cern.japc.core.ParameterCharacteristics: ...

class ParameterCharacteristicsImpl(cern.japc.core.ParameterCharacteristics, java.io.Serializable):
    """
    Java class 'cern.japc.core.factory.ParameterCharacteristicsImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.ParameterCharacteristics, java.io.Serializable
    
      Attributes:
        CHARACHTERISTICS_N (cern.japc.core.ParameterCharacteristics): final static field
        CHARACHTERISTICS_W (cern.japc.core.ParameterCharacteristics): final static field
    
    """
    CHARACHTERISTICS_N: typing.ClassVar[cern.japc.core.ParameterCharacteristics] = ...
    CHARACHTERISTICS_W: typing.ClassVar[cern.japc.core.ParameterCharacteristics] = ...
    def getAdditionalInformation(self) -> java.util.Map[str, typing.Any]: ...
    def isWildcardSubscriptionParameter(self) -> bool: ...
    def toString(self) -> str: ...

class ParameterExceptionFactory:
    """
    Java class 'cern.japc.core.factory.ParameterExceptionFactory'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ParameterExceptionFactory()
    
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def newException(exception: java.lang.Exception, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> cern.japc.core.ParameterException: ...
    @typing.overload
    @staticmethod
    def newException(string: str, exception: java.lang.Exception, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> cern.japc.core.ParameterException: ...

class ParameterMetaFactoryConstants:
    """
    Java class 'cern.japc.core.factory.ParameterMetaFactoryConstants'
    
      Attributes:
        RDA_SERVICE_NAME (java.lang.String): final static field
        RDA3_SERVICE_NAME (java.lang.String): final static field
        TGM_SERVICE_NAME (java.lang.String): final static field
        SNMP_SERVICE_NAME (java.lang.String): final static field
        RMI_SERVICE_NAME (java.lang.String): final static field
        RDA_PROTOCOL (java.lang.String): final static field
        RDA3_PROTOCOL (java.lang.String): final static field
        TGM_PROTOCOL (java.lang.String): final static field
        SYSPROP_DEFAULT_SERVICE_NAME (java.lang.String): final static field
        SYSPROP_DEFAULT_PROTOCOL_NAME (java.lang.String): final static field
        DEFAULT_SERVICE_NAME (java.lang.String): final static field
        DEFAULT_PROTOCOL_NAME (java.lang.String): final static field
        SYSPROP_SERVICE_NAME_RESOLVERS (java.lang.String): final static field
        SYSPROP_SERVICE_CONFIG_LOOKUPS (java.lang.String): final static field
        SYSPROP_WILDCARD_SELECTOR_RESOLVER (java.lang.String): final static field
        SYSPROP_DEFAULT_WILDCARD_SUBSCRIPTION_ON (java.lang.String): final static field
    
    """
    RDA_SERVICE_NAME: typing.ClassVar[str] = ...
    RDA3_SERVICE_NAME: typing.ClassVar[str] = ...
    TGM_SERVICE_NAME: typing.ClassVar[str] = ...
    SNMP_SERVICE_NAME: typing.ClassVar[str] = ...
    RMI_SERVICE_NAME: typing.ClassVar[str] = ...
    RDA_PROTOCOL: typing.ClassVar[str] = ...
    RDA3_PROTOCOL: typing.ClassVar[str] = ...
    TGM_PROTOCOL: typing.ClassVar[str] = ...
    SYSPROP_DEFAULT_SERVICE_NAME: typing.ClassVar[str] = ...
    SYSPROP_DEFAULT_PROTOCOL_NAME: typing.ClassVar[str] = ...
    DEFAULT_SERVICE_NAME: typing.ClassVar[str] = ...
    DEFAULT_PROTOCOL_NAME: typing.ClassVar[str] = ...
    SYSPROP_SERVICE_NAME_RESOLVERS: typing.ClassVar[str] = ...
    SYSPROP_SERVICE_CONFIG_LOOKUPS: typing.ClassVar[str] = ...
    SYSPROP_WILDCARD_SELECTOR_RESOLVER: typing.ClassVar[str] = ...
    SYSPROP_DEFAULT_WILDCARD_SUBSCRIPTION_ON: typing.ClassVar[str] = ...

class SelectorFactory:
    """
    Java class 'cern.japc.core.factory.SelectorFactory'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    @staticmethod
    def newSelector(parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.Selector: ...
    @typing.overload
    @staticmethod
    def newSelector(string: str) -> cern.japc.core.Selector: ...
    @typing.overload
    @staticmethod
    def newSelector(string: str, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.Selector: ...

class ServiceNameResolver:
    """
    Java class 'cern.japc.core.factory.ServiceNameResolver'
    
    """
    def getServiceName(self, string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> str: ...

class SimpleParameterValueFactory:
    """
    Java class 'cern.japc.core.factory.SimpleParameterValueFactory'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    @staticmethod
    def newSimpleParameterValue() -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(boolean: bool) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(boolean: bool, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(booleanArray: typing.List[bool]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(booleanArray: typing.List[bool], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(booleanArray: typing.List[bool], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(booleanArray: typing.List[bool], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byte: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byte: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byteArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byteArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byteArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byteArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(discreteFunction: cern.japc.value.DiscreteFunction) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(discreteFunction: cern.japc.value.DiscreteFunction, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(discreteFunctionList: cern.japc.value.DiscreteFunctionList, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItem: cern.japc.value.EnumItem) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItem: cern.japc.value.EnumItem, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSet: cern.japc.value.EnumItemSet) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSet: cern.japc.value.EnumItemSet, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemArray: typing.List[cern.japc.value.EnumItem]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemArray: typing.List[cern.japc.value.EnumItem], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(simpleDescriptor: cern.japc.value.SimpleDescriptor) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(valueType: cern.japc.value.ValueType) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(valueType: cern.japc.value.ValueType, enumType: cern.japc.value.EnumType) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(double: float) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(double: float, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(doubleArray: typing.List[float]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(doubleArray: typing.List[float], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(doubleArray: typing.List[float], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(doubleArray: typing.List[float], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(float: float) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(float: float, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(floatArray: typing.List[float]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(floatArray: typing.List[float], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(floatArray: typing.List[float], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(floatArray: typing.List[float], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(int: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(int: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(intArray: typing.List[int], intArray2: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(intArray: typing.List[int], intArray2: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(object: typing.Any) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(object: typing.Any, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(object: typing.Any, intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(object: typing.Any, intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(string: str) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(string: str, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(stringArray: typing.List[str]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(stringArray: typing.List[str], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(stringArray: typing.List[str], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(stringArray: typing.List[str], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(long: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(long: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(longArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(longArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(longArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(longArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(short: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(short: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(shortArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(shortArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(shortArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(shortArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue() -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(boolean: bool) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(boolean: bool, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(booleanArray: typing.List[bool]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(booleanArray: typing.List[bool], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(booleanArray: typing.List[bool], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(booleanArray: typing.List[bool], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byte: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byte: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byteArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byteArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byteArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byteArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(discreteFunction: cern.japc.value.DiscreteFunction) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(discreteFunction: cern.japc.value.DiscreteFunction, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(discreteFunctionList: cern.japc.value.DiscreteFunctionList, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItem: cern.japc.value.EnumItem) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItem: cern.japc.value.EnumItem, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSet: cern.japc.value.EnumItemSet) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSet: cern.japc.value.EnumItemSet, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemArray: typing.List[cern.japc.value.EnumItem]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemArray: typing.List[cern.japc.value.EnumItem], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(simpleDescriptor: cern.japc.value.SimpleDescriptor) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(valueType: cern.japc.value.ValueType) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(valueType: cern.japc.value.ValueType, enumType: cern.japc.value.EnumType) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(double: float) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(double: float, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(doubleArray: typing.List[float]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(doubleArray: typing.List[float], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(doubleArray: typing.List[float], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(doubleArray: typing.List[float], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(float: float) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(float: float, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(floatArray: typing.List[float]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(floatArray: typing.List[float], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(floatArray: typing.List[float], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(floatArray: typing.List[float], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(int: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(int: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(intArray: typing.List[int], intArray2: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(intArray: typing.List[int], intArray2: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(object: typing.Any) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(object: typing.Any, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(object: typing.Any, intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(object: typing.Any, intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(string: str) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(string: str, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(stringArray: typing.List[str]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(stringArray: typing.List[str], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(stringArray: typing.List[str], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(stringArray: typing.List[str], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(long: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(long: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(longArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(longArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(longArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(longArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(short: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(short: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(shortArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(shortArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(shortArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(shortArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...

class TransactionFactory:
    """
    Java class 'cern.japc.core.factory.TransactionFactory'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def newCompositeTransaction() -> cern.japc.core.transaction.CompositeTransaction: ...

class ValueHeaderFactory:
    """
    Java class 'cern.japc.core.factory.ValueHeaderFactory'
    
        Extends:
            java.lang.Object
    
      Attributes:
        NO_CYCLE_STAMP (long): final static field
        NO_SET_STAMP (long): final static field
    
    """
    NO_CYCLE_STAMP: typing.ClassVar[int] = ...
    NO_SET_STAMP: typing.ClassVar[int] = ...
    @typing.overload
    @staticmethod
    def newAcquisitionFirstUpdateHeader(long: int, long2: int, selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newAcquisitionFirstUpdateHeader(long: int, long2: int, string: str) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newAcquisitionRegularUpdateHeader(long: int, long2: int, selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newAcquisitionRegularUpdateHeader(long: int, long2: int, string: str) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingFirstUpdateHeader(long: int, long2: int, selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingFirstUpdateHeader(long: int, long2: int, string: str) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingImmediateUpdateHeader(selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingImmediateUpdateHeader(string: str) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingImmediateUpdateHeader(long: int, long2: int, selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingImmediateUpdateHeader(long: int, long2: int, string: str) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingRegularUpdateHeader(long: int, long2: int, selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingRegularUpdateHeader(long: int, long2: int, string: str) -> cern.japc.core.ValueHeader: ...
    @staticmethod
    def toFirstUpdateHeader(valueHeader: cern.japc.core.ValueHeader) -> cern.japc.core.ValueHeader: ...
    @staticmethod
    def toImmediateUpdateHeader(valueHeader: cern.japc.core.ValueHeader) -> cern.japc.core.ValueHeader: ...
    @staticmethod
    def toRegularUpdateHeader(valueHeader: cern.japc.core.ValueHeader) -> cern.japc.core.ValueHeader: ...

class ParameterFactory(IParameterFactory):
    """
    Java class 'cern.japc.core.factory.ParameterFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.factory.IParameterFactory
    
      Attributes:
        FACTORY_ID (java.lang.String): final static field
        DESCRIPTOR_PROVIDER_ID (java.lang.String): final static field
        SYSPROP_JAPC_DIRSERVICE_PROVIDER_ENABLED (java.lang.String): final static field
        SYSPROP_JAPC_CCS_DESCRIPTORS_ENABLED (java.lang.String): final static field
        SYSPROP_JAPC_IGNORE_SET (java.lang.String): final static field
    
    """
    FACTORY_ID: typing.ClassVar[str] = ...
    DESCRIPTOR_PROVIDER_ID: typing.ClassVar[str] = ...
    SYSPROP_JAPC_DIRSERVICE_PROVIDER_ENABLED: typing.ClassVar[str] = ...
    SYSPROP_JAPC_CCS_DESCRIPTORS_ENABLED: typing.ClassVar[str] = ...
    SYSPROP_JAPC_IGNORE_SET: typing.ClassVar[str] = ...
    @staticmethod
    def addAllDescriptors(string: str, deviceDescriptor: cern.japc.core.DeviceDescriptor, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor) -> None: ...
    @staticmethod
    def addDeviceDescriptor(string: str, deviceDescriptor: cern.japc.core.DeviceDescriptor) -> None: ...
    @staticmethod
    def addParameterAndValueDescriptor(string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor) -> None: ...
    @staticmethod
    def addParameterDescriptor(string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> None: ...
    @staticmethod
    def addValueDescriptor(string: str, valueDescriptor: cern.japc.value.ValueDescriptor) -> None: ...
    def getDescriptorProvider(self) -> cern.japc.core.spi.provider.DescriptorProvider: ...
    def getDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor: ...
    def getDeviceDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    @typing.overload
    def getParameterDescriptor(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> cern.japc.core.ParameterDescriptor: ...
    @typing.overload
    def getParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def getParameterDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def getParameterDescriptorsFromUrls(self, collection: typing.Union[java.util.Collection[cern.japc.core.spi.ParameterUrl], typing.Sequence[cern.japc.core.spi.ParameterUrl]]) -> java.util.Map[cern.japc.core.spi.ParameterUrl, cern.japc.core.ParameterDescriptor]: ...
    @typing.overload
    def getValueDescriptor(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> cern.japc.value.ValueDescriptor: ...
    @typing.overload
    def getValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def getValueDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...
    def getValueDescriptorsFromUrls(self, collection: typing.Union[java.util.Collection[cern.japc.core.spi.ParameterUrl], typing.Sequence[cern.japc.core.spi.ParameterUrl]]) -> java.util.Map[cern.japc.core.spi.ParameterUrl, cern.japc.value.ValueDescriptor]: ...
    def isUnknownParameterSupported(self) -> bool: ...
    @typing.overload
    @staticmethod
    def newInstance() -> 'ParameterFactory': ...
    @typing.overload
    @staticmethod
    def newInstance(string: str) -> 'ParameterFactory': ...
    @typing.overload
    def newParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterCharacteristics: cern.japc.core.ParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str, parameterCharacteristics: cern.japc.core.ParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str, string2: str) -> cern.japc.core.transaction.TransactionalParameter: ...
    def newParameterExplorer(self) -> cern.japc.core.ParameterExplorer: ...
    def setUnknownParameterSupported(self, boolean: bool) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.factory")``.

    AcquiredParameterValueFactory: typing.Type[AcquiredParameterValueFactory]
    FactoryConfigurationError: typing.Type[FactoryConfigurationError]
    FailSafeParameterValueFactory: typing.Type[FailSafeParameterValueFactory]
    IParameterFactory: typing.Type[IParameterFactory]
    MapParameterValueFactory: typing.Type[MapParameterValueFactory]
    ObjectParameterValueFactory: typing.Type[ObjectParameterValueFactory]
    ParameterCharacteristicsFactory: typing.Type[ParameterCharacteristicsFactory]
    ParameterCharacteristicsImpl: typing.Type[ParameterCharacteristicsImpl]
    ParameterExceptionFactory: typing.Type[ParameterExceptionFactory]
    ParameterFactory: typing.Type[ParameterFactory]
    ParameterMetaFactoryConstants: typing.Type[ParameterMetaFactoryConstants]
    SelectorFactory: typing.Type[SelectorFactory]
    ServiceNameResolver: typing.Type[ServiceNameResolver]
    SimpleParameterValueFactory: typing.Type[SimpleParameterValueFactory]
    TransactionFactory: typing.Type[TransactionFactory]
    ValueHeaderFactory: typing.Type[ValueHeaderFactory]
