import cern.accsoft.commons.util
import cern.accsoft.commons.util.value
import cern.japc.value
import java.lang
import java.util
import typing


class AcquiredParameterValue:
    def getAdditionalErrors(self) -> typing.List[str]: ...
    def getDescriptor(self) -> cern.japc.value.ValueDescriptor: ...
    def getHeader(self) -> 'ValueHeader': ...
    def getParameterName(self) -> str: ...
    def getStatus(self) -> cern.japc.value.ValueStatus: ...
    def getValue(self) -> cern.japc.value.ParameterValue: ...

class DeviceDescriptor:
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
    def getDescription(self) -> str: ...

class ObjectParameterValue(cern.japc.value.ParameterValue):
    def getValue(self) -> typing.Any: ...
    def makeMutable(self) -> 'ObjectParameterValue': ...
    def setValue(self, object: typing.Any) -> None: ...

class ParameterCharacteristics:
    PARAMETER_CHARACTERISTIC_ARRAY_CALL_ID: typing.ClassVar[str] = ...
    def getAdditionalInformation(self) -> java.util.Map[str, typing.Any]: ...
    def isWildcardSubscriptionParameter(self) -> bool: ...

class ParameterDescriptor:
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
        def getFilteredValues(self) -> typing.List[str]: ...
    class NameDescription:
        def getDescription(self) -> str: ...
        def getName(self) -> str: ...

class ParameterRuntimeException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ParameterValueListener:
    def exceptionOccured(self, string: str, string2: str, parameterException: ParameterException) -> None: ...
    def valueReceived(self, string: str, acquiredParameterValue: AcquiredParameterValue) -> None: ...

class Parameters:
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
        def to(self, immutableParameter: ImmutableParameter) -> Selector: ...

class SubscriptionConfigurator:
    PUSH_MODE: typing.ClassVar[int] = ...
    PULL_MODE: typing.ClassVar[int] = ...
    def getDataDeliveryMode(self) -> int: ...
    def getSelector(self) -> Selector: ...
    def setDataDeliveryMode(self, int: int) -> None: ...

class ValueHeader:
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
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class FailSafeParameterValue(AcquiredParameterValue, cern.accsoft.commons.util.value.FailSafe[ParameterException, AcquiredParameterValue]):
    def getException(self) -> ParameterException: ...
    def getString(self) -> str: ...

class MapParameterDescriptor(ParameterDescriptor):
    def get(self, string: str) -> 'SimpleParameterDescriptor': ...
    def getNames(self) -> typing.List[str]: ...
    def size(self) -> int: ...

class NoDataAvailableException(ParameterException):
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
    @typing.overload
    def setValue(self, selector: Selector, parameterValue: cern.japc.value.ParameterValue) -> None: ...
    @typing.overload
    def setValue(self, selector: Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: ParameterValueListener) -> None: ...

class SubscriptionHandle(SubscriptionConfigurator):
    def getListener(self) -> ParameterValueListener: ...
    def getParameter(self) -> ImmutableParameter: ...
    def isMonitoring(self) -> bool: ...
    def peekValue(self, long: int) -> AcquiredParameterValue: ...
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None: ...

class SubscriptionProblemException(ParameterException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: ValueHeader): ...

class SubscriptionRecoveredException(ParameterException):
    def __init__(self, string: str): ...

class WaitingForDataException(ParameterException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class SimpleParameterDescriptor(MapParameterDescriptor): ...
