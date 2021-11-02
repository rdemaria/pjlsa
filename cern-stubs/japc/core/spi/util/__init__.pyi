import cern.japc.core
import java.lang
import java.util
import java.util.concurrent
import typing



class FanoutParameterValueListener(cern.japc.core.ParameterValueListener):
    """
    public class FanoutParameterValueListener extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ParameterValueListener`
    
        Implementation of :class:`~cern.japc.core.ParameterValueListener` which redistributes the updates to a list of
        :class:`~cern.japc.core.ParameterValueListener`'s.
    
        Each :class:`~cern.japc.core.ParameterValueListener` is notified in a separate thread.
    """
    def __init__(self, collection: typing.Union[java.util.Collection[cern.japc.core.ParameterValueListener], typing.Sequence[cern.japc.core.ParameterValueListener]]): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`
            Notifies this listener that a problem occurred preventing the get/set to be done.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.valueReceived`
            Notifies this listener that a new value has been received (get or monitor) or set to the parameter. In the case of the
            notification of the set the value can be null.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.valueReceived`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...

class JapcExecutor:
    """
    public final class JapcExecutor extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A class that provides the Executor from the concurrent package to be used for JAPC.
    """
    SYSPROP_MAXTHREADS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_MAXTHREADS
    
        System property for maximum number of thread in the pool of executor. Default is 40.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_BLOCKSTRAT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_BLOCKSTRAT
    
        System property for blocking strategy used in executor. Default is
        :meth:`~cern.japc.core.spi.util.JapcExecutor.BS_DISCARD`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_BUFSIZE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_BUFSIZE
    
        System property for a maximum buffer size to keep tasks when all the thread are busy. Default is 900.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_INSTRUMENTATION_DISABLED: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_INSTRUMENTATION_DISABLED
    
        System property for a enabling/disabling instrumentation. Default is disabled.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_INSTRUMENTATION_INTERVAL_SEC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_INSTRUMENTATION_INTERVAL_SEC
    
        System property for setting instrumentation statistic gathering interval (in seconds). Default is 60 seconds.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_SCHEDULED_THREADS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_SCHEDULED_THREADS
    
        System property for the number of thread in the scheduled executor. Default is 2.
    
        Also see:
            :meth:`~constant`
    
    
    """
    BS_ABORT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` BS_ABORT
    
        Constant to specify ABORT policy via system property :meth:`~cern.japc.core.spi.util.JapcExecutor.SYSPROP_BLOCKSTRAT`.
    
        This policy means: throw an unchecked `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/RejectedExecutionException.html?is-external=true>`
        if the buffer is full.
    
        Also see:
            :meth:`~constant`
    
    
    """
    BS_WAIT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` BS_WAIT
    
        Constant to specify WAIT policy via system property :meth:`~cern.japc.core.spi.util.JapcExecutor.SYSPROP_BLOCKSTRAT`.
    
        This policy means: if the buffer is full wait a bit and try to re-submit the task again.
    
        Also see:
            :meth:`~constant`
    
    
    """
    BS_DISCARD: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` BS_DISCARD
    
        Constant to specify DISCARD policy via system property :meth:`~cern.japc.core.spi.util.JapcExecutor.SYSPROP_BLOCKSTRAT`.
    
        This policy means: if the buffer is full discard the oldest task.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def execute(self, runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> None: ...
    @staticmethod
    def get() -> 'JapcExecutor':
        """
            get the singleton executor instance, which is created lazily
        
            Returns:
                the Executor instance
        
        
        """
        ...
    def getBlockedExcecutionStrategy(self) -> str:
        """
            accessor method
        
            Returns:
                the active strategy of what is done when the buffer is full and all threads are busy one of
                :meth:`~cern.japc.core.spi.util.JapcExecutor.BS_WAIT` or :meth:`~cern.japc.core.spi.util.JapcExecutor.BS_DISCARD` or
                :meth:`~cern.japc.core.spi.util.JapcExecutor.BS_ABORT`
        
        
        """
        ...
    def getBufferSize(self) -> int:
        """
            Returns the buffer size, so the number of queued tasks.
        
            Returns:
                the buffer size, so the number of queued tasks
        
        
        """
        ...
    def getMaximumPoolSize(self) -> int:
        """
        
            Returns:
                the maximum number of threads that the pool can contain
        
        
        """
        ...
    def getMinimumPoolSize(self) -> int:
        """
        
            Returns:
                the minimum number of threads that are always instantiated
        
        
        """
        ...
    def getPoolSize(self) -> int:
        """
            Return the current number of threads in the pool of executor.
        
            Returns:
                the current number of threads in the pool of executor
        
        
        """
        ...
    def getRequestBufferMaxSize(self) -> int:
        """
            Returns maximum number of buffered tasks in the executor.
        
            Returns:
                maximum number of buffered tasks in the executor.
        
        
        """
        ...
    @staticmethod
    def getScheduledExecutor() -> java.util.concurrent.ScheduledExecutorService:
        """
            get the singleton scheduled executor instance, which is created lazily
        
            Returns:
                the Scheduled Executor instance
        
        
        """
        ...
    class JmxMBean:
        def getActiveThreadNumber(self) -> int: ...
        def getCurrentBufferSize(self) -> int: ...
        def getCurrentThreadPoolSize(self) -> int: ...
        def getDeliveredUpdateNumber(self) -> int: ...
        def getDiscardedUpdateNumber(self) -> int: ...
        def getInstrumentationState(self) -> str: ...
        def getMaxBufferSize(self) -> int: ...
        def getMaxThreadPoolSize(self) -> int: ...
        def getRejectedUpdateNumber(self) -> int: ...
        def getSaturationPolicy(self) -> str: ...
        def getSubmittedUpdateNumber(self) -> int: ...

_MultiValueMap__K = typing.TypeVar('_MultiValueMap__K')  # <K>
_MultiValueMap__V = typing.TypeVar('_MultiValueMap__V')  # <V>
class MultiValueMap(typing.Generic[_MultiValueMap__K, _MultiValueMap__V]):
    """
    public class MultiValueMap<K, V> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A map that can contain for each key multiple values.
    
        Key is mapped to a collection of values.
    
        Internally this map can use any type of collection to keep the values (lists, sets). By default a `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/LinkedList.html?is-external=true>` is used.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, class_: typing.Type[java.util.Collection]): ...
    @typing.overload
    def __init__(self, class_: typing.Type[java.util.Collection]): ...
    def clear(self) -> None:
        """
            Clears the whole map.
        
        
        """
        ...
    def contains(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> bool:
        """
            Checks whether the key-value pair is stored in this MultiValueMap.
        
        
            Parameters:
                key (:class:`~cern.japc.core.spi.util.MultiValueMap`): the key (must be non-null)
                value (:class:`~cern.japc.core.spi.util.MultiValueMap`): the value (must be non-null)
        
            Returns:
                true if the key-value pair is stored in this MultiValueMap
        
        
        """
        ...
    def containsAll(self, k: _MultiValueMap__K, collection: typing.Union[java.util.Collection[_MultiValueMap__V], typing.Sequence[_MultiValueMap__V]]) -> bool: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getKeys(self) -> java.util.Set[_MultiValueMap__K]: ...
    def getValues(self, k: _MultiValueMap__K) -> java.util.Collection[_MultiValueMap__V]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Checks whether the map is empty.
        
        
            Returns:
                true if the map is empty and false otherwise.
        
        
        """
        ...
    def put(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> None:
        """
            Adds the key-value pair to this MultiValueMap.
        
        
            Parameters:
                key (:class:`~cern.japc.core.spi.util.MultiValueMap`): the key (must be non-null)
                value (:class:`~cern.japc.core.spi.util.MultiValueMap`): the value (must be non-null)
        
        
        """
        ...
    def putAll(self, k: _MultiValueMap__K, collection: typing.Union[java.util.Collection[_MultiValueMap__V], typing.Sequence[_MultiValueMap__V]]) -> None: ...
    @typing.overload
    def remove(self, k: _MultiValueMap__K) -> bool:
        """
            Removes all the values for particular key.
        
        
            Parameters:
                key (:class:`~cern.japc.core.spi.util.MultiValueMap`): the key (must be non-null)
        
            Returns:
                true if it was successfully removed
        
            Removes the key-value pair from this MultiValueMap.
        
        
            Parameters:
                key (:class:`~cern.japc.core.spi.util.MultiValueMap`): the key (must be non-null)
                value (:class:`~cern.japc.core.spi.util.MultiValueMap`): the value (must be non-null)
        
            Returns:
                true if it was successfully removed
        
        
        """
        ...
    @typing.overload
    def remove(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> bool: ...
    def removeAll(self, k: _MultiValueMap__K, collection: typing.Union[java.util.Collection[_MultiValueMap__V], typing.Sequence[_MultiValueMap__V]]) -> bool: ...
    def size(self, k: _MultiValueMap__K) -> int:
        """
            Returns the number of elements stored with the key.
        
        
            Parameters:
                key (:class:`~cern.japc.core.spi.util.MultiValueMap`): the key (must be non-null)
        
            Returns:
                the number of elements stored with the key.
        
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class SwingThreadParameterValueListener(cern.japc.core.ParameterValueListener):
    """
    public abstract class SwingThreadParameterValueListener extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ParameterValueListener`
    
        Abstract implementation of :class:`~cern.japc.core.ParameterValueListener` that passes all calls to the Swing thread for
        GUI updates.
    
        This listener provides the basic functionality for GUI developers by releasing the JAPC thread and switching the
        reaction execution (on JAPC values and exception) to be performed in the Event Dispatcher thread.
    """
    def __init__(self): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`
            Notifies this listener that a problem occurred preventing the get/set to be done.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                desc (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                pe (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.valueReceived`
            Notifies this listener that a new value has been received (get or monitor) or set to the parameter. In the case of the
            notification of the set the value can be null.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.valueReceived`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                acqVal (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...

_SynchronizedMultiValueMap__K = typing.TypeVar('_SynchronizedMultiValueMap__K')  # <K>
_SynchronizedMultiValueMap__V = typing.TypeVar('_SynchronizedMultiValueMap__V')  # <V>
class SynchronizedMultiValueMap(typing.Generic[_SynchronizedMultiValueMap__K, _SynchronizedMultiValueMap__V]):
    """
    public class SynchronizedMultiValueMap<K, V> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A synchronized map that can contain for each key multiple values.
    
        Key is mapped to a collection of values.
    
        This class is thread-safe. The access to the higher level map structure is guarded by the lock on **this**. The access
        to the elements of the collections are guarded by the locks on those collections. The same collections are returned with
        :meth:`~cern.japc.core.spi.util.SynchronizedMultiValueMap.getValues`.
    
        Care must be taken while iterating through the map components or internal collections elements. Proper synchronization
        is still necessary: synchronize on the :class:`~cern.japc.core.spi.util.SynchronizedMultiValueMap` itself while
        iterating through map components (keys, collections, map entries), synchronize on returned collections while iterating
        through them.
    
        Internally this map uses lists to keep collections of values.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    def clear(self) -> None:
        """
            Clears the whole map.
        
        
        """
        ...
    def contains(self, k: _SynchronizedMultiValueMap__K, v: _SynchronizedMultiValueMap__V) -> bool:
        """
            Checks whether the key-value pair is stored in this MultiValueMap.
        
        
            Parameters:
                key (:class:`~cern.japc.core.spi.util.SynchronizedMultiValueMap`): the key (must be non-null)
                value (:class:`~cern.japc.core.spi.util.SynchronizedMultiValueMap`): the value (must be non-null)
        
            Returns:
                true if the key-value pair is stored in this MultiValueMap
        
        
        """
        ...
    def containsAll(self, k: _SynchronizedMultiValueMap__K, collection: typing.Union[java.util.Collection[_SynchronizedMultiValueMap__V], typing.Sequence[_SynchronizedMultiValueMap__V]]) -> bool: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getKeys(self) -> java.util.Set[_SynchronizedMultiValueMap__K]: ...
    def getValues(self, k: _SynchronizedMultiValueMap__K) -> java.util.Collection[_SynchronizedMultiValueMap__V]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Checks whether the map is empty.
        
        
            Returns:
                true if the map is empty and false otherwise.
        
        
        """
        ...
    def put(self, k: _SynchronizedMultiValueMap__K, v: _SynchronizedMultiValueMap__V) -> None:
        """
            Adds the key-value pair to this MultiValueMap.
        
        
            Parameters:
                key (:class:`~cern.japc.core.spi.util.SynchronizedMultiValueMap`): the key (must be non-null)
                value (:class:`~cern.japc.core.spi.util.SynchronizedMultiValueMap`): the value (must be non-null)
        
        
        """
        ...
    @typing.overload
    def remove(self, k: _SynchronizedMultiValueMap__K) -> bool:
        """
            Removes all the values for particular key.
        
        
            Parameters:
                key (:class:`~cern.japc.core.spi.util.SynchronizedMultiValueMap`): the key (must be non-null)
        
            Returns:
                true if it was successfully removed
        
            Removes the key-value pair from this MultiValueMap.
        
        
            Parameters:
                key (:class:`~cern.japc.core.spi.util.SynchronizedMultiValueMap`): the key (must be non-null)
                value (:class:`~cern.japc.core.spi.util.SynchronizedMultiValueMap`): the value (must be non-null)
        
            Returns:
                true if it was successfully removed
        
        
        """
        ...
    @typing.overload
    def remove(self, k: _SynchronizedMultiValueMap__K, v: _SynchronizedMultiValueMap__V) -> bool: ...
    def size(self, k: _SynchronizedMultiValueMap__K) -> int:
        """
            Returns the number of elements stored with the key.
        
        
            Parameters:
                key (:class:`~cern.japc.core.spi.util.SynchronizedMultiValueMap`): the key (must be non-null)
        
            Returns:
                the number of elements stored with the key.
        
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ThreadedParameterValueListener(cern.japc.core.ParameterValueListener):
    """
    public class ThreadedParameterValueListener extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ParameterValueListener`
    
        A ParameterValueListener implementation that uses a separate thread to forward data passed via the valueReceived() and
        exceptionOccured() methods
    """
    @typing.overload
    def __init__(self, parameterValueListener: cern.japc.core.ParameterValueListener): ...
    @typing.overload
    def __init__(self, japcExecutor: JapcExecutor, parameterValueListener: cern.japc.core.ParameterValueListener): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`
            Notifies this listener that a problem occurred preventing the get/set to be done.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.valueReceived`
            Notifies this listener that a new value has been received (get or monitor) or set to the parameter. In the case of the
            notification of the set the value can be null.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.valueReceived`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...
    class ValueReceivedCommand(java.lang.Runnable):
        def getValue(self) -> cern.japc.core.AcquiredParameterValue: ...
        def run(self) -> None: ...
        def toString(self) -> str: ...

class TimeUtils:
    """
    public class TimeUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def currentTimeNanos() -> int:
        """
        
            Returns:
                system time in nanoseconds (with millisecond precision)
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.util")``.

    FanoutParameterValueListener: typing.Type[FanoutParameterValueListener]
    JapcExecutor: typing.Type[JapcExecutor]
    MultiValueMap: typing.Type[MultiValueMap]
    SwingThreadParameterValueListener: typing.Type[SwingThreadParameterValueListener]
    SynchronizedMultiValueMap: typing.Type[SynchronizedMultiValueMap]
    ThreadedParameterValueListener: typing.Type[ThreadedParameterValueListener]
    TimeUtils: typing.Type[TimeUtils]
