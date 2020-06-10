from typing import TypeVar as _py_TypeVar
import cern.rbac.common
import java.util.concurrent


class RbaUtils:
    def __init__(self): ...
    _fireActionWithRbaToken__T = _py_TypeVar('_fireActionWithRbaToken__T')  # <T>
    @classmethod
    def fireActionWithRbaToken(cls, callable: java.util.concurrent.Callable[_fireActionWithRbaToken__T], rbaToken: cern.rbac.common.RbaToken) -> _fireActionWithRbaToken__T: ...
    _fireActionWithRbaTokenInSeparateThread__T = _py_TypeVar('_fireActionWithRbaTokenInSeparateThread__T')  # <T>
    @classmethod
    def fireActionWithRbaTokenInSeparateThread(cls, callable: java.util.concurrent.Callable[_fireActionWithRbaTokenInSeparateThread__T], rbaToken: cern.rbac.common.RbaToken) -> java.util.concurrent.Future[_fireActionWithRbaTokenInSeparateThread__T]: ...
