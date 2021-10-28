import cern.accsoft.commons.util
import cern.accsoft.commons.util.value
import cern.japc.core.device
import cern.japc.core.directory
import cern.japc.core.factory
import cern.japc.core.group
import cern.japc.core.spi
import cern.japc.core.support
import cern.japc.core.transaction
import cern.japc.core.trigger
import cern.japc.core.util
import cern.japc.value
import java.lang
import java.util
import typing



class AcquiredParameterValue:
    """
    Java class 'cern.japc.core.AcquiredParameterValue'
    
    """
    def getAdditionalErrors(self) -> typing.List[str]: ...
    def getDescriptor(self) -> cern.japc.value.ValueDescriptor: ...
    def getHeader(self) -> 'ValueHeader': ...
    def getParameterName(self) -> str: ...
    def getStatus(self) -> cern.japc.value.ValueStatus: ...
    def getValue(self) -> cern.japc.value.ParameterValue: ...

class DeviceDescriptor:
    """
    Java class 'cern.japc.core.DeviceDescriptor'
    
      Attributes:
        IMPL_FESA (short): final static field
        IMPL_GM (short): final static field
        IMPL_SLEQP (short): final static field
        IMPL_BISCOTO (short): final static field
        IMPL_HARDWARE (short): final static field
        IMPL_VIRTUAL (short): final static field
        IMPL_FGC (short): final static field
        IMPL_UNKNOWN (short): final static field
    
    """
    IMPL_FESA: typing.ClassVar[int] = ...
    IMPL_GM: typing.ClassVar[int] = ...
    IMPL_SLEQP: typing.ClassVar[int] = ...
    IMPL_BISCOTO: typing.ClassVar[int] = ...
    IMPL_HARDWARE: typing.ClassVar[int] = ...
    IMPL_VIRTUAL: typing.ClassVar[int] = ...
    IMPL_FGC: typing.ClassVar[int] = ...
    IMPL_UNKNOWN: typing.ClassVar[int] = ...
    def getControlProperty(self) -> str: ...
    def getDescription(self) -> str: ...
    def getDeviceClassDescription(self) -> str: ...
    def getDeviceClassName(self) -> str: ...
    def getExtraCharacteristic(self, string: str) -> str: ...
    def getExtraCharacteristicNames(self) -> typing.List[str]: ...
    def getHostName(self) -> str: ...
    def getImplementation(self) -> int: ...
    def getLogicalLocation(self) -> str: ...
    def getName(self) -> str: ...
    def getResetProperty(self) -> str: ...
    def getStatusProperty(self) -> str: ...
    def getTgmName(self) -> str: ...
    def isCycleBound(self) -> bool: ...
    def isCycleDependent(self) -> bool: ...
    def isMultiplexed(self) -> bool: ...

class ImmutableParameter(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.japc.core.ImmutableParameter'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def createSubscription(self, selector: 'Selector', parameterValueListener: 'ParameterValueListener') -> 'SubscriptionHandle': ...
    def getDeviceName(self) -> str: ...
    def getName(self) -> str: ...
    def getParameterDescriptor(self) -> 'ParameterDescriptor': ...
    def getPropertyName(self) -> str: ...
    @typing.overload
    def getValue(self, selector: 'Selector') -> AcquiredParameterValue: ...
    @typing.overload
    def getValue(self, selector: 'Selector', parameterValueListener: 'ParameterValueListener') -> None: ...
    def getValueDescriptor(self) -> cern.japc.value.ValueDescriptor: ...

class ObjectDescriptor(cern.japc.value.ValueDescriptor):
    """
    Java class 'cern.japc.core.ObjectDescriptor'
    
        Interfaces:
            cern.japc.value.ValueDescriptor
    
    """
    def getDescription(self) -> str: ...

class ObjectParameterValue(cern.japc.value.ParameterValue):
    """
    Java class 'cern.japc.core.ObjectParameterValue'
    
        Interfaces:
            cern.japc.value.ParameterValue
    
    """
    def getValue(self) -> typing.Any: ...
    def makeMutable(self) -> 'ObjectParameterValue': ...
    def setValue(self, object: typing.Any) -> None: ...

class ParameterCharacteristics:
    """
    Java class 'cern.japc.core.ParameterCharacteristics'
    
      Attributes:
        PARAMETER_CHARACTERISTIC_ARRAY_CALL_ID (java.lang.String): final static field
    
    """
    PARAMETER_CHARACTERISTIC_ARRAY_CALL_ID: typing.ClassVar[str] = ...
    def getAdditionalInformation(self) -> java.util.Map[str, typing.Any]: ...
    def isWildcardSubscriptionParameter(self) -> bool: ...

class ParameterDescriptor:
    """
    Java class 'cern.japc.core.ParameterDescriptor'
    
    """
    def castAsMap(self) -> 'MapParameterDescriptor': ...
    def castAsSimple(self) -> 'SimpleParameterDescriptor': ...
    def getDescription(self) -> str: ...
    def getExtraCharacteristic(self, string: str) -> str: ...
    def getExtraCharacteristicNames(self) -> typing.List[str]: ...
    def getType(self) -> cern.japc.value.Type: ...
    def isCycleBound(self) -> bool: ...
    def isCycleDependent(self) -> bool: ...
    def isFilterable(self) -> bool: ...
    def isMonitorable(self) -> bool: ...
    def isMultiplexed(self) -> bool: ...
    def isReadable(self) -> bool: ...
    def isTransactional(self) -> bool: ...
    def isValueMutable(self) -> bool: ...
    def isWritable(self) -> bool: ...

class ParameterException(java.lang.Exception):
    """
    Java class 'cern.japc.core.ParameterException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ParameterException(java.lang.String, java.lang.Throwable, cern.japc.core.ValueHeader, int)
        * ParameterException()
        * ParameterException(java.lang.String, java.lang.Throwable, long, cern.japc.core.Selector)
        * ParameterException(java.lang.String, java.lang.Throwable, long, long, cern.japc.core.Selector)
        * ParameterException(java.lang.String, java.lang.Throwable, long, cern.japc.core.Selector, int)
        * ParameterException(java.lang.String)
        * ParameterException(java.lang.Throwable)
        * ParameterException(java.lang.String, java.lang.Throwable)
        * ParameterException(java.lang.String, java.lang.Throwable, int)
        * ParameterException(java.lang.String, java.lang.Throwable, cern.japc.core.ValueHeader)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: 'ValueHeader'): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: 'ValueHeader', int: int): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, int: int): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, long: int, selector: 'Selector'): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, long: int, selector: 'Selector', int: int): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, long: int, long2: int, selector: 'Selector'): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    def getCode(self) -> int: ...
    def getCycleStamp(self) -> int: ...
    def getHeader(self) -> 'ValueHeader': ...
    def getSelector(self) -> 'Selector': ...

class ParameterExplorer:
    """
    Java class 'cern.japc.core.ParameterExplorer'
    
    """
    def getAcceleratorNames(self, boolean: bool) -> typing.List[str]: ...
    def getDependentParameterNames(self, string: str) -> typing.List[str]: ...
    def getDeviceNamesForAccelerator(self, string: str, filter: 'ParameterExplorer.Filter') -> typing.List[str]: ...
    def getDeviceNamesForHost(self, string: str, filter: 'ParameterExplorer.Filter') -> typing.List[str]: ...
    def getFamilyNamesForAccelerator(self, string: str, filter: 'ParameterExplorer.Filter') -> typing.List[str]: ...
    def getFamilyNamesForHost(self, string: str, filter: 'ParameterExplorer.Filter') -> typing.List[str]: ...
    def getHostNamesForAccelerator(self, string: str, filter: 'ParameterExplorer.Filter') -> typing.List[str]: ...
    def getPropertyNameDescriptions(self, string: str) -> typing.List['ParameterExplorer.NameDescription']: ...
    def getRootParameterNames(self) -> typing.List[str]: ...
    def getSourceParameterNames(self, string: str) -> typing.List[str]: ...
    class Filter:
        """
        Java class 'cern.japc.core.ParameterExplorer$Filter'
        
        """
        def getFilteredValues(self) -> typing.List[str]: ...
    class NameDescription:
        """
        Java class 'cern.japc.core.ParameterExplorer$NameDescription'
        
        """
        def getDescription(self) -> str: ...
        def getName(self) -> str: ...

class ParameterRuntimeException(java.lang.RuntimeException):
    """
    Java class 'cern.japc.core.ParameterRuntimeException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * ParameterRuntimeException(java.lang.String, java.lang.Exception)
        * ParameterRuntimeException(java.lang.Exception)
        * ParameterRuntimeException(java.lang.String)
        * ParameterRuntimeException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ParameterValueListener:
    """
    Java class 'cern.japc.core.ParameterValueListener'
    
    """
    def exceptionOccured(self, string: str, string2: str, parameterException: ParameterException) -> None: ...
    def valueReceived(self, string: str, acquiredParameterValue: AcquiredParameterValue) -> None: ...

class Parameters:
    """
    Java class 'cern.japc.core.Parameters'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def appendFieldName(string: str, string2: str) -> str: ...
    @typing.overload
    @staticmethod
    def buildParameterName(string: str, string2: str) -> str: ...
    @typing.overload
    @staticmethod
    def buildParameterName(string: str, string2: str, string3: str) -> str: ...
    @staticmethod
    def extractDeviceAndProperty(string: str) -> str: ...
    @staticmethod
    def extractDeviceName(string: str) -> str: ...
    @staticmethod
    def extractDevicesAndProperties(stringArray: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def extractDistinctDevicesAndProperties(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[str]: ...
    @staticmethod
    def extractFieldName(string: str) -> str: ...
    @staticmethod
    def extractPropertyAndField(string: str) -> str: ...
    @staticmethod
    def extractPropertyName(string: str) -> str: ...
    @staticmethod
    def getDevicePropertyNameSeparator() -> str: ...
    @staticmethod
    def getMaxValue(string: str, selector: 'Selector') -> float: ...
    @staticmethod
    def getMinValue(string: str, selector: 'Selector') -> float: ...
    @staticmethod
    def getPropertyFieldSeparator() -> str: ...
    @staticmethod
    def getUnit(string: str, selector: 'Selector') -> str: ...
    @staticmethod
    def hasFieldName(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isParameterName(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isParameterName(string: str, boolean: bool) -> bool: ...

class Selector:
    """
    Java class 'cern.japc.core.Selector'
    
      Attributes:
        PERIODIC_PULLING (java.lang.String): final static field
        PERIODIC_2SEC (java.lang.String): final static field
        PERIODIC_4SEC (java.lang.String): final static field
        PERIODIC_16SEC (java.lang.String): final static field
        PERIODIC_64SEC (java.lang.String): final static field
        PERIODIC_256SEC (java.lang.String): final static field
    
    """
    PERIODIC_PULLING: typing.ClassVar[str] = ...
    PERIODIC_2SEC: typing.ClassVar[str] = ...
    PERIODIC_4SEC: typing.ClassVar[str] = ...
    PERIODIC_16SEC: typing.ClassVar[str] = ...
    PERIODIC_64SEC: typing.ClassVar[str] = ...
    PERIODIC_256SEC: typing.ClassVar[str] = ...
    def getDataFilter(self) -> cern.japc.value.ParameterValue: ...
    def getId(self) -> str: ...
    def getPeriod(self) -> int: ...
    def isPeriodic(self) -> bool: ...

class Selectors:
    """
    Java class 'cern.japc.core.Selectors'
    
        Extends:
            java.lang.Object
    
      Attributes:
        NO_SELECTOR (cern.japc.core.Selector): final static field
        NON_PPM_SELECTOR (cern.japc.core.Selector): final static field
        USER_ALL_SUFFIX (java.lang.String): final static field
    
    """
    NO_SELECTOR: typing.ClassVar[Selector] = ...
    NON_PPM_SELECTOR: typing.ClassVar[Selector] = ...
    USER_ALL_SUFFIX: typing.ClassVar[str] = ...
    @staticmethod
    def adapt(selector: Selector) -> 'Selectors.OngoingSelectorAdaptation': ...
    @staticmethod
    def adaptIfPossible(selector: Selector) -> 'Selectors.OngoingSelectorAdaptation': ...
    @staticmethod
    def assertSelectorIdValid(string: str) -> None: ...
    @staticmethod
    def assertSelectorValid(selector: Selector) -> None: ...
    @typing.overload
    @staticmethod
    def createUserAllSelector(string: str) -> Selector: ...
    @typing.overload
    @staticmethod
    def createUserAllSelector(string: str, parameterValue: cern.japc.value.ParameterValue) -> Selector: ...
    @staticmethod
    def createUserAllSelectorId(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def extractTimingDomain(selector: Selector) -> str: ...
    @typing.overload
    @staticmethod
    def extractTimingDomain(string: str) -> str: ...
    @staticmethod
    def isNoSelector(selector: Selector) -> bool: ...
    @staticmethod
    def isNoSelectorId(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isUserAllSelector(selector: Selector) -> bool: ...
    @typing.overload
    @staticmethod
    def isUserAllSelector(string: str) -> bool: ...
    @staticmethod
    def isUserAllSelectorId(string: str) -> bool: ...
    @staticmethod
    def isUserSelector(selector: Selector) -> bool: ...
    @staticmethod
    def isUserSelectorId(string: str) -> bool: ...
    class OngoingSelectorAdaptation:
        """
        Java class 'cern.japc.core.Selectors$OngoingSelectorAdaptation'
        
            Extends:
                java.lang.Object
        
        """
        def to(self, immutableParameter: ImmutableParameter) -> Selector: ...

class SubscriptionConfigurator:
    """
    Java class 'cern.japc.core.SubscriptionConfigurator'
    
      Attributes:
        PUSH_MODE (int): final static field
        PULL_MODE (int): final static field
    
    """
    PUSH_MODE: typing.ClassVar[int] = ...
    PULL_MODE: typing.ClassVar[int] = ...
    def getDataDeliveryMode(self) -> int: ...
    def getSelector(self) -> Selector: ...
    def setDataDeliveryMode(self, int: int) -> None: ...

class ValueHeader:
    """
    Java class 'cern.japc.core.ValueHeader'
    
    """
    def getAcqStamp(self) -> int: ...
    def getAcqStampMillis(self) -> int: ...
    def getCycleStamp(self) -> int: ...
    def getCycleStampMillis(self) -> int: ...
    def getSelector(self) -> Selector: ...
    def getSetStamp(self) -> int: ...
    def getSetStampMillis(self) -> int: ...
    def isFirstUpdate(self) -> bool: ...
    def isImmediateUpdate(self) -> bool: ...

class AuthorizationExpiredException(ParameterException):
    """
    Java class 'cern.japc.core.AuthorizationExpiredException'
    
        Extends:
            cern.japc.core.ParameterException
    
      Constructors:
        * AuthorizationExpiredException(java.lang.String)
        * AuthorizationExpiredException(java.lang.Throwable)
        * AuthorizationExpiredException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class FailSafeParameterValue(AcquiredParameterValue, cern.accsoft.commons.util.value.FailSafe[ParameterException, AcquiredParameterValue]):
    """
    Java class 'cern.japc.core.FailSafeParameterValue'
    
        Interfaces:
            cern.japc.core.AcquiredParameterValue,
            cern.accsoft.commons.util.value.FailSafe
    
    """
    def getException(self) -> ParameterException: ...
    def getString(self) -> str: ...

class MapParameterDescriptor(ParameterDescriptor):
    """
    Java class 'cern.japc.core.MapParameterDescriptor'
    
        Interfaces:
            cern.japc.core.ParameterDescriptor
    
    """
    def get(self, string: str) -> 'SimpleParameterDescriptor': ...
    def getNames(self) -> typing.List[str]: ...
    def size(self) -> int: ...

class NoDataAvailableException(ParameterException):
    """
    Java class 'cern.japc.core.NoDataAvailableException'
    
        Extends:
            cern.japc.core.ParameterException
    
      Constructors:
        * NoDataAvailableException(java.lang.String, java.lang.Throwable, cern.japc.core.Selector)
        * NoDataAvailableException(java.lang.String, cern.japc.core.Selector)
        * NoDataAvailableException(java.lang.String, java.lang.Throwable, cern.japc.core.ValueHeader)
        * NoDataAvailableException(java.lang.String)
        * NoDataAvailableException(java.lang.String, java.lang.Throwable)
        * NoDataAvailableException(java.lang.String, cern.japc.core.ValueHeader)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, selector: Selector): ...
    @typing.overload
    def __init__(self, string: str, valueHeader: ValueHeader): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, selector: Selector): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: ValueHeader): ...

class NoValueException(ParameterException):
    """
    Java class 'cern.japc.core.NoValueException'
    
        Extends:
            cern.japc.core.ParameterException
    
      Constructors:
        * NoValueException(java.lang.String, cern.japc.core.ValueHeader)
        * NoValueException(java.lang.String, java.lang.Throwable, cern.japc.core.ValueHeader)
        * NoValueException(java.lang.String, long)
        * NoValueException(java.lang.String, java.lang.Throwable, long, cern.japc.core.Selector)
        * NoValueException(java.lang.String)
        * NoValueException(java.lang.Throwable)
        * NoValueException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, valueHeader: ValueHeader): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: ValueHeader): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, long: int, selector: Selector): ...
    @typing.overload
    def __init__(self, string: str, long: int): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class Parameter(ImmutableParameter):
    """
    Java class 'cern.japc.core.Parameter'
    
        Interfaces:
            cern.japc.core.ImmutableParameter
    
    """
    @typing.overload
    def setValue(self, selector: Selector, parameterValue: cern.japc.value.ParameterValue) -> None: ...
    @typing.overload
    def setValue(self, selector: Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: ParameterValueListener) -> None: ...

class SubscriptionHandle(SubscriptionConfigurator):
    """
    Java class 'cern.japc.core.SubscriptionHandle'
    
        Interfaces:
            cern.japc.core.SubscriptionConfigurator
    
    """
    def getListener(self) -> ParameterValueListener: ...
    def getParameter(self) -> ImmutableParameter: ...
    def isMonitoring(self) -> bool: ...
    def peekValue(self, long: int) -> AcquiredParameterValue: ...
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None: ...

class SubscriptionProblemException(ParameterException):
    """
    Java class 'cern.japc.core.SubscriptionProblemException'
    
        Extends:
            cern.japc.core.ParameterException
    
      Constructors:
        * SubscriptionProblemException(java.lang.String)
        * SubscriptionProblemException(java.lang.String, java.lang.Throwable)
        * SubscriptionProblemException(java.lang.String, java.lang.Throwable, cern.japc.core.ValueHeader)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: ValueHeader): ...

class SubscriptionRecoveredException(ParameterException):
    """
    Java class 'cern.japc.core.SubscriptionRecoveredException'
    
        Extends:
            cern.japc.core.ParameterException
    
      Constructors:
        * SubscriptionRecoveredException(java.lang.String)
    
    """
    def __init__(self, string: str): ...

class WaitingForDataException(ParameterException):
    """
    Java class 'cern.japc.core.WaitingForDataException'
    
        Extends:
            cern.japc.core.ParameterException
    
      Constructors:
        * WaitingForDataException()
        * WaitingForDataException(java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class SimpleParameterDescriptor(MapParameterDescriptor): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core")``.

    AcquiredParameterValue: typing.Type[AcquiredParameterValue]
    AuthorizationExpiredException: typing.Type[AuthorizationExpiredException]
    DeviceDescriptor: typing.Type[DeviceDescriptor]
    FailSafeParameterValue: typing.Type[FailSafeParameterValue]
    ImmutableParameter: typing.Type[ImmutableParameter]
    MapParameterDescriptor: typing.Type[MapParameterDescriptor]
    NoDataAvailableException: typing.Type[NoDataAvailableException]
    NoValueException: typing.Type[NoValueException]
    ObjectDescriptor: typing.Type[ObjectDescriptor]
    ObjectParameterValue: typing.Type[ObjectParameterValue]
    Parameter: typing.Type[Parameter]
    ParameterCharacteristics: typing.Type[ParameterCharacteristics]
    ParameterDescriptor: typing.Type[ParameterDescriptor]
    ParameterException: typing.Type[ParameterException]
    ParameterExplorer: typing.Type[ParameterExplorer]
    ParameterRuntimeException: typing.Type[ParameterRuntimeException]
    ParameterValueListener: typing.Type[ParameterValueListener]
    Parameters: typing.Type[Parameters]
    Selector: typing.Type[Selector]
    Selectors: typing.Type[Selectors]
    SimpleParameterDescriptor: typing.Type[SimpleParameterDescriptor]
    SubscriptionConfigurator: typing.Type[SubscriptionConfigurator]
    SubscriptionHandle: typing.Type[SubscriptionHandle]
    SubscriptionProblemException: typing.Type[SubscriptionProblemException]
    SubscriptionRecoveredException: typing.Type[SubscriptionRecoveredException]
    ValueHeader: typing.Type[ValueHeader]
    WaitingForDataException: typing.Type[WaitingForDataException]
    device: cern.japc.core.device.__module_protocol__
    directory: cern.japc.core.directory.__module_protocol__
    factory: cern.japc.core.factory.__module_protocol__
    group: cern.japc.core.group.__module_protocol__
    spi: cern.japc.core.spi.__module_protocol__
    support: cern.japc.core.support.__module_protocol__
    transaction: cern.japc.core.transaction.__module_protocol__
    trigger: cern.japc.core.trigger.__module_protocol__
    util: cern.japc.core.util.__module_protocol__
