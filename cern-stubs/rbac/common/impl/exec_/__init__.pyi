import java.util.concurrent
import typing


class ExecutionService:
    _submit__T = typing.TypeVar('_submit__T')  # <T>
    def submit(self, callable: typing.Union[java.util.concurrent.Callable[_submit__T], typing.Callable[[], _submit__T]]) -> java.util.concurrent.Future[_submit__T]: ...

class ExecutionServiceImpl(ExecutionService):
    def __init__(self): ...
    _submit__T = typing.TypeVar('_submit__T')  # <T>
    def submit(self, callable: typing.Union[java.util.concurrent.Callable[_submit__T], typing.Callable[[], _submit__T]]) -> java.util.concurrent.Future[_submit__T]: ...
