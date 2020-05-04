from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.lang
import java.security
import java.util
import javax.management


class LockInfo:
    def __init__(self, string: str, int: int): ...
    def getClassName(self) -> str: ...
    def getIdentityHashCode(self) -> int: ...
    def toString(self) -> str: ...

class ManagementFactory:
    CLASS_LOADING_MXBEAN_NAME: _py_ClassVar[str] = ...
    COMPILATION_MXBEAN_NAME: _py_ClassVar[str] = ...
    MEMORY_MXBEAN_NAME: _py_ClassVar[str] = ...
    OPERATING_SYSTEM_MXBEAN_NAME: _py_ClassVar[str] = ...
    RUNTIME_MXBEAN_NAME: _py_ClassVar[str] = ...
    THREAD_MXBEAN_NAME: _py_ClassVar[str] = ...
    GARBAGE_COLLECTOR_MXBEAN_DOMAIN_TYPE: _py_ClassVar[str] = ...
    MEMORY_MANAGER_MXBEAN_DOMAIN_TYPE: _py_ClassVar[str] = ...
    MEMORY_POOL_MXBEAN_DOMAIN_TYPE: _py_ClassVar[str] = ...
    @classmethod
    def getClassLoadingMXBean(cls) -> 'ClassLoadingMXBean': ...
    @classmethod
    def getCompilationMXBean(cls) -> 'CompilationMXBean': ...
    @classmethod
    def getGarbageCollectorMXBeans(cls) -> java.util.List['GarbageCollectorMXBean']: ...
    @classmethod
    def getMemoryMXBean(cls) -> 'MemoryMXBean': ...
    @classmethod
    def getMemoryManagerMXBeans(cls) -> java.util.List['MemoryManagerMXBean']: ...
    @classmethod
    def getMemoryPoolMXBeans(cls) -> java.util.List['MemoryPoolMXBean']: ...
    @classmethod
    def getOperatingSystemMXBean(cls) -> 'OperatingSystemMXBean': ...
    @classmethod
    def getPlatformMBeanServer(cls) -> javax.management.MBeanServer: ...
    _getPlatformMXBean_0__T = _py_TypeVar('_getPlatformMXBean_0__T', bound='PlatformManagedObject')  # <T>
    @classmethod
    @overload
    def getPlatformMXBean(cls, mBeanServerConnection: javax.management.MBeanServerConnection, class_: _py_Type[_getPlatformMXBean_0__T]) -> _getPlatformMXBean_0__T: ...
    _getPlatformMXBean_1__T = _py_TypeVar('_getPlatformMXBean_1__T', bound='PlatformManagedObject')  # <T>
    @classmethod
    @overload
    def getPlatformMXBean(cls, class_: _py_Type[_getPlatformMXBean_1__T]) -> _getPlatformMXBean_1__T: ...
    _getPlatformMXBeans_0__T = _py_TypeVar('_getPlatformMXBeans_0__T', bound='PlatformManagedObject')  # <T>
    @classmethod
    @overload
    def getPlatformMXBeans(cls, mBeanServerConnection: javax.management.MBeanServerConnection, class_: _py_Type[_getPlatformMXBeans_0__T]) -> java.util.List[_getPlatformMXBeans_0__T]: ...
    _getPlatformMXBeans_1__T = _py_TypeVar('_getPlatformMXBeans_1__T', bound='PlatformManagedObject')  # <T>
    @classmethod
    @overload
    def getPlatformMXBeans(cls, class_: _py_Type[_getPlatformMXBeans_1__T]) -> java.util.List[_getPlatformMXBeans_1__T]: ...
    @classmethod
    def getPlatformManagementInterfaces(cls) -> java.util.Set[_py_Type['PlatformManagedObject']]: ...
    @classmethod
    def getRuntimeMXBean(cls) -> 'RuntimeMXBean': ...
    @classmethod
    def getThreadMXBean(cls) -> 'ThreadMXBean': ...
    _newPlatformMXBeanProxy__T = _py_TypeVar('_newPlatformMXBeanProxy__T')  # <T>
    @classmethod
    def newPlatformMXBeanProxy(cls, mBeanServerConnection: javax.management.MBeanServerConnection, string: str, class_: _py_Type[_newPlatformMXBeanProxy__T]) -> _newPlatformMXBeanProxy__T: ...

class ManagementPermission(java.security.BasicPermission):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, string2: str): ...

class MemoryNotificationInfo:
    MEMORY_THRESHOLD_EXCEEDED: _py_ClassVar[str] = ...
    MEMORY_COLLECTION_THRESHOLD_EXCEEDED: _py_ClassVar[str] = ...
    def __init__(self, string: str, memoryUsage: 'MemoryUsage', long: int): ...
    def getCount(self) -> int: ...
    def getPoolName(self) -> str: ...
    def getUsage(self) -> 'MemoryUsage': ...

class MemoryType(java.lang.Enum['MemoryType']):
    HEAP: _py_ClassVar['MemoryType'] = ...
    NON_HEAP: _py_ClassVar['MemoryType'] = ...
    def toString(self) -> str: ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'MemoryType': ...
    _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @classmethod
    def values(cls) -> _py_List['MemoryType']: ...

class MemoryUsage:
    def __init__(self, long: int, long2: int, long3: int, long4: int): ...
    def getCommitted(self) -> int: ...
    def getInit(self) -> int: ...
    def getMax(self) -> int: ...
    def getUsed(self) -> int: ...
    def toString(self) -> str: ...

class PlatformComponent(java.lang.Enum['PlatformComponent']):
    CLASS_LOADING: _py_ClassVar['PlatformComponent'] = ...
    COMPILATION: _py_ClassVar['PlatformComponent'] = ...
    MEMORY: _py_ClassVar['PlatformComponent'] = ...
    GARBAGE_COLLECTOR: _py_ClassVar['PlatformComponent'] = ...
    MEMORY_MANAGER: _py_ClassVar['PlatformComponent'] = ...
    MEMORY_POOL: _py_ClassVar['PlatformComponent'] = ...
    OPERATING_SYSTEM: _py_ClassVar['PlatformComponent'] = ...
    RUNTIME: _py_ClassVar['PlatformComponent'] = ...
    THREADING: _py_ClassVar['PlatformComponent'] = ...
    LOGGING: _py_ClassVar['PlatformComponent'] = ...
    BUFFER_POOL: _py_ClassVar['PlatformComponent'] = ...
    SUN_GARBAGE_COLLECTOR: _py_ClassVar['PlatformComponent'] = ...
    SUN_OPERATING_SYSTEM: _py_ClassVar['PlatformComponent'] = ...
    SUN_UNIX_OPERATING_SYSTEM: _py_ClassVar['PlatformComponent'] = ...
    HOTSPOT_DIAGNOSTIC: _py_ClassVar['PlatformComponent'] = ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'PlatformComponent': ...
    _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @classmethod
    def values(cls) -> _py_List['PlatformComponent']: ...

class PlatformManagedObject:
    def getObjectName(self) -> javax.management.ObjectName: ...

class ThreadInfo:
    def getBlockedCount(self) -> int: ...
    def getBlockedTime(self) -> int: ...
    def getLockInfo(self) -> LockInfo: ...
    def getLockName(self) -> str: ...
    def getLockOwnerId(self) -> int: ...
    def getLockOwnerName(self) -> str: ...
    def getLockedMonitors(self) -> _py_List['MonitorInfo']: ...
    def getLockedSynchronizers(self) -> _py_List[LockInfo]: ...
    def getStackTrace(self) -> _py_List[java.lang.StackTraceElement]: ...
    def getThreadId(self) -> int: ...
    def getThreadName(self) -> str: ...
    def getThreadState(self) -> java.lang.Thread.State: ...
    def getWaitedCount(self) -> int: ...
    def getWaitedTime(self) -> int: ...
    def isInNative(self) -> bool: ...
    def isSuspended(self) -> bool: ...
    def toString(self) -> str: ...

class BufferPoolMXBean(PlatformManagedObject):
    def getCount(self) -> int: ...
    def getMemoryUsed(self) -> int: ...
    def getName(self) -> str: ...
    def getTotalCapacity(self) -> int: ...

class ClassLoadingMXBean(PlatformManagedObject):
    def getLoadedClassCount(self) -> int: ...
    def getTotalLoadedClassCount(self) -> int: ...
    def getUnloadedClassCount(self) -> int: ...
    def isVerbose(self) -> bool: ...
    def setVerbose(self, boolean: bool) -> None: ...

class CompilationMXBean(PlatformManagedObject):
    def getName(self) -> str: ...
    def getTotalCompilationTime(self) -> int: ...
    def isCompilationTimeMonitoringSupported(self) -> bool: ...

class MemoryMXBean(PlatformManagedObject):
    def gc(self) -> None: ...
    def getHeapMemoryUsage(self) -> MemoryUsage: ...
    def getNonHeapMemoryUsage(self) -> MemoryUsage: ...
    def getObjectPendingFinalizationCount(self) -> int: ...
    def isVerbose(self) -> bool: ...
    def setVerbose(self, boolean: bool) -> None: ...

class MemoryManagerMXBean(PlatformManagedObject):
    def getMemoryPoolNames(self) -> _py_List[str]: ...
    def getName(self) -> str: ...
    def isValid(self) -> bool: ...

class MemoryPoolMXBean(PlatformManagedObject):
    def getCollectionUsage(self) -> MemoryUsage: ...
    def getCollectionUsageThreshold(self) -> int: ...
    def getCollectionUsageThresholdCount(self) -> int: ...
    def getMemoryManagerNames(self) -> _py_List[str]: ...
    def getName(self) -> str: ...
    def getPeakUsage(self) -> MemoryUsage: ...
    def getType(self) -> MemoryType: ...
    def getUsage(self) -> MemoryUsage: ...
    def getUsageThreshold(self) -> int: ...
    def getUsageThresholdCount(self) -> int: ...
    def isCollectionUsageThresholdExceeded(self) -> bool: ...
    def isCollectionUsageThresholdSupported(self) -> bool: ...
    def isUsageThresholdExceeded(self) -> bool: ...
    def isUsageThresholdSupported(self) -> bool: ...
    def isValid(self) -> bool: ...
    def resetPeakUsage(self) -> None: ...
    def setCollectionUsageThreshold(self, long: int) -> None: ...
    def setUsageThreshold(self, long: int) -> None: ...

class MonitorInfo(LockInfo):
    def __init__(self, string: str, int: int, int2: int, stackTraceElement: java.lang.StackTraceElement): ...
    def getLockedStackDepth(self) -> int: ...
    def getLockedStackFrame(self) -> java.lang.StackTraceElement: ...

class OperatingSystemMXBean(PlatformManagedObject):
    def getArch(self) -> str: ...
    def getAvailableProcessors(self) -> int: ...
    def getName(self) -> str: ...
    def getSystemLoadAverage(self) -> float: ...
    def getVersion(self) -> str: ...

class PlatformLoggingMXBean(PlatformManagedObject):
    def getLoggerLevel(self, string: str) -> str: ...
    def getLoggerNames(self) -> java.util.List[str]: ...
    def getParentLoggerName(self, string: str) -> str: ...
    def setLoggerLevel(self, string: str, string2: str) -> None: ...

class RuntimeMXBean(PlatformManagedObject):
    def getBootClassPath(self) -> str: ...
    def getClassPath(self) -> str: ...
    def getInputArguments(self) -> java.util.List[str]: ...
    def getLibraryPath(self) -> str: ...
    def getManagementSpecVersion(self) -> str: ...
    def getName(self) -> str: ...
    def getSpecName(self) -> str: ...
    def getSpecVendor(self) -> str: ...
    def getSpecVersion(self) -> str: ...
    def getStartTime(self) -> int: ...
    def getSystemProperties(self) -> java.util.Map[str, str]: ...
    def getUptime(self) -> int: ...
    def getVmName(self) -> str: ...
    def getVmVendor(self) -> str: ...
    def getVmVersion(self) -> str: ...
    def isBootClassPathSupported(self) -> bool: ...

class ThreadMXBean(PlatformManagedObject):
    def dumpAllThreads(self, boolean: bool, boolean2: bool) -> _py_List[ThreadInfo]: ...
    def findDeadlockedThreads(self) -> _py_List[int]: ...
    def findMonitorDeadlockedThreads(self) -> _py_List[int]: ...
    def getAllThreadIds(self) -> _py_List[int]: ...
    def getCurrentThreadCpuTime(self) -> int: ...
    def getCurrentThreadUserTime(self) -> int: ...
    def getDaemonThreadCount(self) -> int: ...
    def getPeakThreadCount(self) -> int: ...
    def getThreadCount(self) -> int: ...
    def getThreadCpuTime(self, long: int) -> int: ...
    @overload
    def getThreadInfo(self, long: int) -> ThreadInfo: ...
    @overload
    def getThreadInfo(self, longArray: _py_List[int]) -> _py_List[ThreadInfo]: ...
    @overload
    def getThreadInfo(self, longArray: _py_List[int], boolean: bool, boolean2: bool) -> _py_List[ThreadInfo]: ...
    @overload
    def getThreadInfo(self, longArray: _py_List[int], int: int) -> _py_List[ThreadInfo]: ...
    @overload
    def getThreadInfo(self, long: int, int: int) -> ThreadInfo: ...
    def getThreadUserTime(self, long: int) -> int: ...
    def getTotalStartedThreadCount(self) -> int: ...
    def isCurrentThreadCpuTimeSupported(self) -> bool: ...
    def isObjectMonitorUsageSupported(self) -> bool: ...
    def isSynchronizerUsageSupported(self) -> bool: ...
    def isThreadContentionMonitoringEnabled(self) -> bool: ...
    def isThreadContentionMonitoringSupported(self) -> bool: ...
    def isThreadCpuTimeEnabled(self) -> bool: ...
    def isThreadCpuTimeSupported(self) -> bool: ...
    def resetPeakThreadCount(self) -> None: ...
    def setThreadContentionMonitoringEnabled(self, boolean: bool) -> None: ...
    def setThreadCpuTimeEnabled(self, boolean: bool) -> None: ...

class GarbageCollectorMXBean(MemoryManagerMXBean):
    def getCollectionCount(self) -> int: ...
    def getCollectionTime(self) -> int: ...
