from typing import TypeVar as _py_TypeVar
import java.util.concurrent


class ExecutionService:
    _submit__T = _py_TypeVar('_submit__T')  # <T>
    def submit(self, callable: java.util.concurrent.Callable[_submit__T]) -> java.util.concurrent.Future[_submit__T]: ...

class ExecutionServiceImpl(ExecutionService):
    def __init__(self): ...
    _submit__T = _py_TypeVar('_submit__T')  # <T>
    def submit(self, callable: java.util.concurrent.Callable[_submit__T]) -> java.util.concurrent.Future[_submit__T]: ...
