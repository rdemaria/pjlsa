import java.lang
import java.util
import java.util.concurrent
import java.util.function
import typing



class ContextAwareExecutors:
    """
    Java class 'cern.accsoft.commons.util.executor.ContextAwareExecutors'
    
        Extends:
            java.lang.Object
    
    """
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
    Java class 'cern.accsoft.commons.util.executor.ContextDefinition'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ContextDefinition(java.util.function.Supplier)
        * ContextDefinition(java.util.function.Supplier, java.util.function.Supplier)
    
    """
    @typing.overload
    def __init__(self, supplier: typing.Union[java.util.function.Supplier['ContextForwarder'], typing.Callable[[], 'ContextForwarder']]): ...
    @typing.overload
    def __init__(self, supplier: typing.Union[java.util.function.Supplier['ContextForwarder'], typing.Callable[[], 'ContextForwarder']], supplier2: typing.Union[java.util.function.Supplier['ExecutionValidator'], typing.Callable[[], 'ExecutionValidator']]): ...

class ContextForwarder:
    """
    Java class 'cern.accsoft.commons.util.executor.ContextForwarder'
    
    """
    def clearContext(self) -> None: ...
    def setContext(self) -> None: ...

class ExecutionValidator:
    """
    Java class 'cern.accsoft.commons.util.executor.ExecutionValidator'
    
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
    def validateSchedule(self, runnable: typing.Union[java.lang.Runnable, typing.Callable], long: int, timeUnit: java.util.concurrent.TimeUnit) -> None: ...
    @typing.overload
    def validateSchedule(self, callable: typing.Union[java.util.concurrent.Callable[_validateSchedule_1__V], typing.Callable[[], _validateSchedule_1__V]], long: int, timeUnit: java.util.concurrent.TimeUnit) -> None: ...
    def validateScheduleAtFixedRate(self, runnable: typing.Union[java.lang.Runnable, typing.Callable], long: int, long2: int, timeUnit: java.util.concurrent.TimeUnit) -> None: ...
    def validateScheduleWithFixedDelay(self, runnable: typing.Union[java.lang.Runnable, typing.Callable], long: int, long2: int, timeUnit: java.util.concurrent.TimeUnit) -> None: ...
    _validateSubmit_1__T = typing.TypeVar('_validateSubmit_1__T')  # <T>
    _validateSubmit_2__T = typing.TypeVar('_validateSubmit_2__T')  # <T>
    @typing.overload
    def validateSubmit(self, runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> None: ...
    @typing.overload
    def validateSubmit(self, runnable: typing.Union[java.lang.Runnable, typing.Callable], t: _validateSubmit_1__T) -> None: ...
    @typing.overload
    def validateSubmit(self, callable: typing.Union[java.util.concurrent.Callable[_validateSubmit_2__T], typing.Callable[[], _validateSubmit_2__T]]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.executor")``.

    ContextAwareExecutors: typing.Type[ContextAwareExecutors]
    ContextDefinition: typing.Type[ContextDefinition]
    ContextForwarder: typing.Type[ContextForwarder]
    ExecutionValidator: typing.Type[ExecutionValidator]
