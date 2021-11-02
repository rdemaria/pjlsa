import java.lang
import java.util
import java.util.concurrent
import java.util.function
import typing



class ContextAwareExecutors:
    @typing.overload
    def newCachedThreadPool(self) -> java.util.concurrent.ExecutorService: ...
    @typing.overload
    def newCachedThreadPool(self, threadFactory: java.util.concurrent.ThreadFactory) -> java.util.concurrent.ExecutorService: ...
    @typing.overload
    def newFixedThreadPool(self, int: int) -> java.util.concurrent.ExecutorService: ...
    @typing.overload
    def newFixedThreadPool(self, int: int, threadFactory: java.util.concurrent.ThreadFactory) -> java.util.concurrent.ExecutorService: ...
    @typing.overload
    def newScheduledThreadPool(self, int: int) -> java.util.concurrent.ScheduledExecutorService: ...
    @typing.overload
    def newScheduledThreadPool(self, int: int, threadFactory: java.util.concurrent.ThreadFactory) -> java.util.concurrent.ScheduledExecutorService: ...
    @typing.overload
    def newSingleThreadScheduledExecutor(self) -> java.util.concurrent.ScheduledExecutorService: ...
    @typing.overload
    def newSingleThreadScheduledExecutor(self, threadFactory: java.util.concurrent.ThreadFactory) -> java.util.concurrent.ScheduledExecutorService: ...
    @staticmethod
    def withContexts(contextDefinitionArray: typing.List['ContextDefinition']) -> 'ContextAwareExecutors': ...

class ContextDefinition:
    """
    public class ContextDefinition extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Definition of a context, which is the combination of a :class:`~cern.accsoft.commons.util.executor.ContextForwarder` and
        an :class:`~cern.accsoft.commons.util.executor.ExecutionValidator`.
    """
    @typing.overload
    def __init__(self, supplier: typing.Union[java.util.function.Supplier['ContextForwarder'], typing.Callable[[], 'ContextForwarder']]): ...
    @typing.overload
    def __init__(self, supplier: typing.Union[java.util.function.Supplier['ContextForwarder'], typing.Callable[[], 'ContextForwarder']], supplier2: typing.Union[java.util.function.Supplier['ExecutionValidator'], typing.Callable[[], 'ExecutionValidator']]): ...

class ContextForwarder:
    """
    public interface ContextForwarder
    
        Context Forwarder for the :class:`~cern.accsoft.commons.util.executor.ContextAwareExecutors`.
    """
    def clearContext(self) -> None:
        """
            Clears the context after the end of execution.
        
        """
        ...
    def setContext(self) -> None:
        """
            Sets the context from the calling thread.
        
        """
        ...

class ExecutionValidator:
    """
    public interface ExecutionValidator
    
        The execution validator is used to configure exclusions for some of the `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/ExecutorService.html?is-external=true>`
        methods, for example by sending an `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/UnsupportedOperationException.html?is-external=true>` in
        one of the validation methods. By default, the :class:`~cern.accsoft.commons.util.executor.ExecutionValidator` allows
        all method calls.
    """
    def validateExecute(self, runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> None: ...
    _validateInvokeAll_0__T = typing.TypeVar('_validateInvokeAll_0__T')  # <T>
    _validateInvokeAll_1__T = typing.TypeVar('_validateInvokeAll_1__T')  # <T>
    @typing.overload
    def validateInvokeAll(self, collection: typing.Union[java.util.Collection[java.util.concurrent.Callable[_validateInvokeAll_0__T]], typing.Sequence[java.util.concurrent.Callable[_validateInvokeAll_0__T]]]) -> None: ...
    @typing.overload
    def validateInvokeAll(self, collection: typing.Union[java.util.Collection[java.util.concurrent.Callable[_validateInvokeAll_1__T]], typing.Sequence[java.util.concurrent.Callable[_validateInvokeAll_1__T]]], long: int, timeUnit: java.util.concurrent.TimeUnit) -> None: ...
    _validateInvokeAny_0__T = typing.TypeVar('_validateInvokeAny_0__T')  # <T>
    _validateInvokeAny_1__T = typing.TypeVar('_validateInvokeAny_1__T')  # <T>
    @typing.overload
    def validateInvokeAny(self, collection: typing.Union[java.util.Collection[java.util.concurrent.Callable[_validateInvokeAny_0__T]], typing.Sequence[java.util.concurrent.Callable[_validateInvokeAny_0__T]]]) -> None: ...
    @typing.overload
    def validateInvokeAny(self, collection: typing.Union[java.util.Collection[java.util.concurrent.Callable[_validateInvokeAny_1__T]], typing.Sequence[java.util.concurrent.Callable[_validateInvokeAny_1__T]]], long: int, timeUnit: java.util.concurrent.TimeUnit) -> None: ...
    _validateSchedule_1__V = typing.TypeVar('_validateSchedule_1__V')  # <V>
    @typing.overload
    def validateSchedule(self, runnable: typing.Union[java.lang.Runnable, typing.Callable], long: int, timeUnit: java.util.concurrent.TimeUnit) -> None:
        """
        default <V> void validateSchedule (`Callable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/Callable.html?is-external=true>`<V> callable, long delay, `TimeUnit <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/TimeUnit.html?is-external=true>` unit)
        
        
        """
        ...
    @typing.overload
    def validateSchedule(self, callable: typing.Union[java.util.concurrent.Callable[_validateSchedule_1__V], typing.Callable[[], _validateSchedule_1__V]], long: int, timeUnit: java.util.concurrent.TimeUnit) -> None: ...
    def validateScheduleAtFixedRate(self, runnable: typing.Union[java.lang.Runnable, typing.Callable], long: int, long2: int, timeUnit: java.util.concurrent.TimeUnit) -> None: ...
    def validateScheduleWithFixedDelay(self, runnable: typing.Union[java.lang.Runnable, typing.Callable], long: int, long2: int, timeUnit: java.util.concurrent.TimeUnit) -> None: ...
    _validateSubmit_1__T = typing.TypeVar('_validateSubmit_1__T')  # <T>
    _validateSubmit_2__T = typing.TypeVar('_validateSubmit_2__T')  # <T>
    @typing.overload
    def validateSubmit(self, runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> None: ...
    @typing.overload
    def validateSubmit(self, runnable: typing.Union[java.lang.Runnable, typing.Callable], t: _validateSubmit_1__T) -> None:
        """
        default void validateSubmit (`Runnable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Runnable.html?is-external=true>` task)
        
        
        """
        ...
    @typing.overload
    def validateSubmit(self, callable: typing.Union[java.util.concurrent.Callable[_validateSubmit_2__T], typing.Callable[[], _validateSubmit_2__T]]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.executor")``.

    ContextAwareExecutors: typing.Type[ContextAwareExecutors]
    ContextDefinition: typing.Type[ContextDefinition]
    ContextForwarder: typing.Type[ContextForwarder]
    ExecutionValidator: typing.Type[ExecutionValidator]
