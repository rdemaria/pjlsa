import cern.rbac.common
import java.util.concurrent
import typing


class RbaUtils:
    def __init__(self): ...
    _fireActionWithRbaToken__T = typing.TypeVar('_fireActionWithRbaToken__T')  # <T>
    @staticmethod
    def fireActionWithRbaToken(callable: typing.Union[java.util.concurrent.Callable[_fireActionWithRbaToken__T], typing.Callable[[], _fireActionWithRbaToken__T]], rbaToken: cern.rbac.common.RbaToken) -> _fireActionWithRbaToken__T: ...
    _fireActionWithRbaTokenInSeparateThread__T = typing.TypeVar('_fireActionWithRbaTokenInSeparateThread__T')  # <T>
    @staticmethod
    def fireActionWithRbaTokenInSeparateThread(callable: typing.Union[java.util.concurrent.Callable[_fireActionWithRbaTokenInSeparateThread__T], typing.Callable[[], _fireActionWithRbaTokenInSeparateThread__T]], rbaToken: cern.rbac.common.RbaToken) -> java.util.concurrent.Future[_fireActionWithRbaTokenInSeparateThread__T]: ...
