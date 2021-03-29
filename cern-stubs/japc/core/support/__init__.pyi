import cern.japc.core
import cern.japc.core.factory
import cern.japc.value
import java.io
import java.util
import typing


class Descriptors:
    RDA: typing.ClassVar[str] = ...
    RDA3: typing.ClassVar[str] = ...
    DEFAULT_STRING: typing.ClassVar[str] = ...
    IS_VALID: typing.ClassVar[str] = ...
    ERROR_STRING: typing.ClassVar[str] = ...
    SERVER_NAME: typing.ClassVar[str] = ...
    DEVICE_ALIAS: typing.ClassVar[str] = ...
    RESPONSIBLE: typing.ClassVar[str] = ...
    CLASS_VERSION: typing.ClassVar[str] = ...
    IMPL_UNKNOWN: typing.ClassVar[str] = ...
    IMPL_VIRTUAL: typing.ClassVar[str] = ...
    IMPL_HARDWARE: typing.ClassVar[str] = ...
    IMPL_SLEQUIP: typing.ClassVar[str] = ...
    IMPL_GM: typing.ClassVar[str] = ...
    IMPL_FESA: typing.ClassVar[str] = ...
    IMPL_FGC: typing.ClassVar[str] = ...
    IMPL_BISCOTO: typing.ClassVar[str] = ...
    DATA_SOURCE: typing.ClassVar[str] = ...
    DATA_SOURCE_UNKNOWN: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def getAccelerator(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getClassVersion(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getClassVersion(string: str) -> str: ...
    @staticmethod
    def getDataSource(string: str) -> str: ...
    @staticmethod
    def getDescription(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getDeviceAlias(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getDeviceAlias(string: str) -> str: ...
    @staticmethod
    def getDeviceClassName(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getDeviceResponsible(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getDeviceResponsible(string: str) -> str: ...
    @staticmethod
    def getEnumItemSymbols(string: str) -> java.util.Collection[str]: ...
    @staticmethod
    def getEnumType(string: str) -> cern.japc.value.EnumType: ...
    @typing.overload
    @staticmethod
    def getErrors(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getErrors(parameterDescriptor: cern.japc.core.ParameterDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getErrors(string: str) -> str: ...
    @staticmethod
    def getFormatPattern(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getHostName(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getHostName(string: str) -> str: ...
    @staticmethod
    def getImplementation(string: str) -> int: ...
    @staticmethod
    def getImplementationAsString(string: str) -> str: ...
    @staticmethod
    def getLength(string: str) -> int: ...
    @staticmethod
    def getMapPropertyFieldNames(string: str) -> typing.List[str]: ...
    @staticmethod
    def getMaxValue(string: str) -> float: ...
    @staticmethod
    def getMinValue(string: str) -> float: ...
    @typing.overload
    @staticmethod
    def getServerName(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> str: ...
    @typing.overload
    @staticmethod
    def getServerName(string: str) -> str: ...
    @staticmethod
    def getSettableEnumItemSymbols(string: str) -> java.util.Collection[str]: ...
    @typing.overload
    @staticmethod
    def getSimpleValueDescriptor(valueDescriptor: cern.japc.value.ValueDescriptor, string: str) -> cern.japc.value.SimpleDescriptor: ...
    @typing.overload
    @staticmethod
    def getSimpleValueDescriptor(string: str) -> cern.japc.value.SimpleDescriptor: ...
    @staticmethod
    def getTgmName(string: str) -> str: ...
    @staticmethod
    def getTitle(string: str) -> str: ...
    @staticmethod
    def getType(string: str) -> cern.japc.value.Type: ...
    @staticmethod
    def getUnit(string: str) -> str: ...
    @staticmethod
    def getValueDescriptor(string: str) -> cern.japc.value.MapDescriptor: ...
    @typing.overload
    @staticmethod
    def getValueType(simpleDescriptor: cern.japc.value.SimpleDescriptor) -> cern.japc.value.ValueType: ...
    @typing.overload
    @staticmethod
    def getValueType(string: str) -> cern.japc.value.ValueType: ...
    @staticmethod
    def isAcquisition(parameterDescriptor: cern.japc.core.ParameterDescriptor) -> bool: ...
    @typing.overload
    @staticmethod
    def isConstant(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isConstant(valueDescriptor: cern.japc.value.ValueDescriptor) -> bool: ...
    @staticmethod
    def isControl(parameterDescriptor: cern.japc.core.ParameterDescriptor) -> bool: ...
    @staticmethod
    def isCycleBound(string: str) -> bool: ...
    @staticmethod
    def isCycleDependent(string: str) -> bool: ...
    @staticmethod
    def isDefaultString(string: str) -> bool: ...
    @staticmethod
    def isDiscrete(string: str) -> bool: ...
    @staticmethod
    def isFilterable(string: str) -> bool: ...
    @staticmethod
    def isMonitorable(string: str) -> bool: ...
    @staticmethod
    def isMultiplexed(string: str) -> bool: ...
    @staticmethod
    def isNonCycleBoundAcquisition(parameterDescriptor: cern.japc.core.ParameterDescriptor) -> bool: ...
    @staticmethod
    def isReadable(string: str) -> bool: ...
    @staticmethod
    def isTransactional(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(deviceDescriptor: cern.japc.core.DeviceDescriptor) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(parameterDescriptor: cern.japc.core.ParameterDescriptor) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(valueDescriptor: cern.japc.value.ValueDescriptor) -> bool: ...
    @typing.overload
    @staticmethod
    def isValid(string: str) -> bool: ...
    @staticmethod
    def isWritable(string: str) -> bool: ...

class DiagTrace:
    RDA_SUBSCRIPTION: typing.ClassVar[int] = ...
    RDA_DATA_RECEPTION: typing.ClassVar[int] = ...
    RDA_DATA_SET: typing.ClassVar[int] = ...
    RDA_PARAMETER_CREATION: typing.ClassVar[int] = ...
    def __init__(self): ...
    @staticmethod
    def displayTrace(int: int, string: str) -> None: ...
    @staticmethod
    def getTraceLevel() -> int: ...
    @staticmethod
    def println(string: str, string2: str) -> None: ...
    @staticmethod
    def setTraceLevel(int: int) -> None: ...
    @staticmethod
    def setTraceOutput(printStream: java.io.PrintStream) -> None: ...
    @staticmethod
    def timeStamp() -> str: ...

class FirstUpdateDiscardingPVL(cern.japc.core.ParameterValueListener):
    def __init__(self, parameterValueListener: cern.japc.core.ParameterValueListener): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None: ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None: ...

class ParameterCatalog:
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, parameterFactory: cern.japc.core.factory.ParameterFactory): ...
    @typing.overload
    def __init__(self, parameterFactory: cern.japc.core.factory.ParameterFactory, boolean: bool): ...
    def destroy(self) -> None: ...
    def destroyParameter(self, string: str) -> None: ...
    def getParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    @typing.overload
    def getValue(self, string: str, selector: cern.japc.core.Selector) -> cern.japc.core.AcquiredParameterValue: ...
    @typing.overload
    def getValue(self, string: str, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def getValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def isMonitoring(self, string: str, selector: cern.japc.core.Selector) -> bool: ...
    def newParameter(self, string: str) -> None: ...
    @typing.overload
    def setValue(self, string: str, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue) -> None: ...
    @typing.overload
    def setValue(self, string: str, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def startMonitoring(self, string: str, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def stopMonitoring(self, string: str, selector: cern.japc.core.Selector) -> None: ...

class ParameterGroupValues:
    @typing.overload
    @staticmethod
    def checkForException(failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> cern.japc.core.FailSafeParameterValue: ...
    @typing.overload
    @staticmethod
    def checkForException(failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue], boolean: bool) -> cern.japc.core.FailSafeParameterValue: ...
    @staticmethod
    def joinSimple2ManyMaps(acquiredParameterValueArray: typing.List[cern.japc.core.AcquiredParameterValue]) -> typing.List[cern.japc.core.AcquiredParameterValue]: ...
    @staticmethod
    def joinSimple2ManyMapsFailSafe(failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    @staticmethod
    def joinSimple2OneMap(acquiredParameterValueArray: typing.List[cern.japc.core.AcquiredParameterValue]) -> cern.japc.core.AcquiredParameterValue: ...
    @staticmethod
    def joinSimple2OneMapFailSafe(failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> cern.japc.core.FailSafeParameterValue: ...
    @staticmethod
    def splitOneMap2Simple(acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> typing.List[cern.japc.core.AcquiredParameterValue]: ...

class ParameterValues:
    @typing.overload
    @staticmethod
    def extractParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def extractParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def extractParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def extractParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str, int: int) -> typing.Any: ...
    @staticmethod
    def extractSimpleParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def getFieldStatus(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int, string: str) -> cern.japc.value.ValueStatus: ...
    @typing.overload
    @staticmethod
    def getFieldStatus(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int, string: str, int2: int) -> cern.japc.value.ValueStatus: ...
    @typing.overload
    @staticmethod
    def getFieldStatus(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> cern.japc.value.ValueStatus: ...
    @typing.overload
    @staticmethod
    def getFieldStatus(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str, int: int) -> cern.japc.value.ValueStatus: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, int: int, string: str, int2: int) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(failSafeParameterValue: cern.japc.core.FailSafeParameterValue, int: int, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(failSafeParameterValue: cern.japc.core.FailSafeParameterValue, int: int, string: str, int2: int) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(failSafeParameterValue: cern.japc.core.FailSafeParameterValue, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def getFieldValue(failSafeParameterValue: cern.japc.core.FailSafeParameterValue, string: str, int: int) -> str: ...
    @staticmethod
    def getMaxValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> float: ...
    @staticmethod
    def getMinValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> float: ...
    @staticmethod
    def getUnit(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> str: ...
    @staticmethod
    def getValueAsBoolean(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> bool: ...
    @staticmethod
    def getValueAsDouble(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> float: ...
    @staticmethod
    def getValueAsFloat(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> float: ...
    @staticmethod
    def getValueAsInt(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> int: ...
    @staticmethod
    def getValueAsLong(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> int: ...
    @staticmethod
    def getValueAsStrings(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, string: str) -> typing.List[str]: ...
    @staticmethod
    def printArray(parameterValueArray: typing.List[cern.japc.value.ParameterValue]) -> None: ...
    @typing.overload
    @staticmethod
    def replaceControlStatus(simpleParameterValue: cern.japc.value.SimpleParameterValue, simpleValueControlStatus: cern.japc.value.SimpleValueControlStatus) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def replaceControlStatus(simpleValueStatus: cern.japc.value.SimpleValueStatus, simpleValueControlStatus: cern.japc.value.SimpleValueControlStatus) -> cern.japc.value.SimpleValueStatus: ...

class SysoutParameterValueListener(cern.japc.core.ParameterValueListener):
    def __init__(self): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None: ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None: ...
