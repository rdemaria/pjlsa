import java.util.concurrent
import typing



class ExecutionService:
    """
    public interface ExecutionService
    
        TODO: to be removed, unnecessary interface and implementation This service is wrapper over java `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/ExecutorService.html?is-external=true>` and
        provides API for submitting new tasks which should be executed by an another thread. However it is up to the service to
        decide what policy to use for managing the worker threads (single, pool, cache, etc.).
    """
    _submit__T = typing.TypeVar('_submit__T')  # <T>
    def submit(self, callable: typing.Union[java.util.concurrent.Callable[_submit__T], typing.Callable[[], _submit__T]]) -> java.util.concurrent.Future[_submit__T]: ...

class ExecutionServiceImpl(ExecutionService):
    """
    public class ExecutionServiceImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.rbac.common.impl.exec.ExecutionService`
    
        TODO: to be removed, unnecessary interface and implementation Default implementation of the
        :class:`~cern.rbac.common.impl.exec.ExecutionService` interface which executes submitted tasks in a cached thread pool,
        which may reuse same thread for subsequent executions.
    """
    def __init__(self): ...
    _submit__T = typing.TypeVar('_submit__T')  # <T>
    def submit(self, callable: typing.Union[java.util.concurrent.Callable[_submit__T], typing.Callable[[], _submit__T]]) -> java.util.concurrent.Future[_submit__T]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl.exec_")``.

    ExecutionService: typing.Type[ExecutionService]
    ExecutionServiceImpl: typing.Type[ExecutionServiceImpl]
