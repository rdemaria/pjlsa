import java.util.concurrent
import typing



class ExecutionService:
    """
    Java class 'cern.rbac.common.impl.exec.ExecutionService'
    
    """
    _submit__T = typing.TypeVar('_submit__T')  # <T>
    def submit(self, callable: typing.Union[java.util.concurrent.Callable[_submit__T], typing.Callable[[], _submit__T]]) -> java.util.concurrent.Future[_submit__T]: ...

class ExecutionServiceImpl(ExecutionService):
    """
    Java class 'cern.rbac.common.impl.exec.ExecutionServiceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.rbac.common.impl.exec.ExecutionService
    
      Constructors:
        * ExecutionServiceImpl()
    
    """
    def __init__(self): ...
    _submit__T = typing.TypeVar('_submit__T')  # <T>
    def submit(self, callable: typing.Union[java.util.concurrent.Callable[_submit__T], typing.Callable[[], _submit__T]]) -> java.util.concurrent.Future[_submit__T]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl.exec_")``.

    ExecutionService: typing.Type[ExecutionService]
    ExecutionServiceImpl: typing.Type[ExecutionServiceImpl]
