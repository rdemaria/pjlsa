from typing import Any as _py_Any
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import Generic as _py_Generic
from typing import overload
import cern.japc.core
import java.lang
import java.util
import java.util.concurrent


class FanoutParameterValueListener(cern.japc.core.ParameterValueListener):
    def __init__(self, collection: java.util.Collection[cern.japc.core.ParameterValueListener]): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None: ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None: ...

class JapcExecutor:
    SYSPROP_MAXTHREADS: _py_ClassVar[str] = ...
    SYSPROP_BLOCKSTRAT: _py_ClassVar[str] = ...
    SYSPROP_BUFSIZE: _py_ClassVar[str] = ...
    SYSPROP_INSTRUMENTATION_ENABLED: _py_ClassVar[str] = ...
    SYSPROP_INSTRUMENTATION_INTERVAL_SEC: _py_ClassVar[str] = ...
    SYSPROP_SCHEDULED_THREADS: _py_ClassVar[str] = ...
    BS_ABORT: _py_ClassVar[str] = ...
    BS_WAIT: _py_ClassVar[str] = ...
    BS_DISCARD: _py_ClassVar[str] = ...
    def execute(self, runnable: java.lang.Runnable) -> None: ...
    @classmethod
    def get(cls) -> 'JapcExecutor': ...
    def getBlockedExcecutionStrategy(self) -> str: ...
    def getBufferSize(self) -> int: ...
    def getMaximumPoolSize(self) -> int: ...
    def getMinimumPoolSize(self) -> int: ...
    def getPoolSize(self) -> int: ...
    def getRequestBufferMaxSize(self) -> int: ...
    @classmethod
    def getScheduledExecutor(cls) -> java.util.concurrent.ScheduledExecutorService: ...
    class JmxMBean:
        def getActiveThreadNumber(self) -> int: ...
        def getCurrentBufferSize(self) -> int: ...
        def getCurrentThreadPoolSize(self) -> int: ...
        def getDeliveredUpdateNumber(self) -> int: ...
        def getMaxBufferSize(self) -> int: ...
        def getMaxThreadPoolSize(self) -> int: ...
        def getSaturationPolicy(self) -> str: ...

_MultiValueMap__K = _py_TypeVar('_MultiValueMap__K')  # <K>
_MultiValueMap__V = _py_TypeVar('_MultiValueMap__V')  # <V>
class MultiValueMap(_py_Generic[_MultiValueMap__K, _MultiValueMap__V]):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, class_: _py_Type[java.util.Collection]): ...
    @overload
    def __init__(self, int: int): ...
    @overload
    def __init__(self, int: int, class_: _py_Type[java.util.Collection]): ...
    def clear(self) -> None: ...
    def contains(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> bool: ...
    def containsAll(self, k: _MultiValueMap__K, collection: java.util.Collection[_MultiValueMap__V]) -> bool: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getKeys(self) -> java.util.Set[_MultiValueMap__K]: ...
    def getValues(self, k: _MultiValueMap__K) -> java.util.Collection[_MultiValueMap__V]: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def put(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> None: ...
    def putAll(self, k: _MultiValueMap__K, collection: java.util.Collection[_MultiValueMap__V]) -> None: ...
    @overload
    def remove(self, k: _MultiValueMap__K) -> bool: ...
    @overload
    def remove(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> bool: ...
    def removeAll(self, k: _MultiValueMap__K, collection: java.util.Collection[_MultiValueMap__V]) -> bool: ...
    def size(self, k: _MultiValueMap__K) -> int: ...
    def toString(self) -> str: ...

class SwingThreadParameterValueListener(cern.japc.core.ParameterValueListener):
    def __init__(self): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None: ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None: ...

_SynchronizedMultiValueMap__K = _py_TypeVar('_SynchronizedMultiValueMap__K')  # <K>
_SynchronizedMultiValueMap__V = _py_TypeVar('_SynchronizedMultiValueMap__V')  # <V>
class SynchronizedMultiValueMap(_py_Generic[_SynchronizedMultiValueMap__K, _SynchronizedMultiValueMap__V]):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, int: int): ...
    def clear(self) -> None: ...
    def contains(self, k: _SynchronizedMultiValueMap__K, v: _SynchronizedMultiValueMap__V) -> bool: ...
    def containsAll(self, k: _SynchronizedMultiValueMap__K, collection: java.util.Collection[_SynchronizedMultiValueMap__V]) -> bool: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getKeys(self) -> java.util.Set[_SynchronizedMultiValueMap__K]: ...
    def getValues(self, k: _SynchronizedMultiValueMap__K) -> java.util.Collection[_SynchronizedMultiValueMap__V]: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def put(self, k: _SynchronizedMultiValueMap__K, v: _SynchronizedMultiValueMap__V) -> None: ...
    @overload
    def remove(self, k: _SynchronizedMultiValueMap__K) -> bool: ...
    @overload
    def remove(self, k: _SynchronizedMultiValueMap__K, v: _SynchronizedMultiValueMap__V) -> bool: ...
    def size(self, k: _SynchronizedMultiValueMap__K) -> int: ...
    def toString(self) -> str: ...

class ThreadedParameterValueListener(cern.japc.core.ParameterValueListener):
    @overload
    def __init__(self, japcExecutor: JapcExecutor, parameterValueListener: cern.japc.core.ParameterValueListener): ...
    @overload
    def __init__(self, parameterValueListener: cern.japc.core.ParameterValueListener): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None: ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None: ...
    class ValueReceivedCommand(java.lang.Runnable):
        def getValue(self) -> cern.japc.core.AcquiredParameterValue: ...
        def run(self) -> None: ...
        def toString(self) -> str: ...

class TimeUtils:
    @classmethod
    def currentTimeNanos(cls) -> int: ...
