import cern.rbac.common
import java.util.concurrent
import typing



class RbaUtils:
    """
    public class RbaUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class containing common methods dealing with RBAC
    """
    def __init__(self): ...
    _fireActionWithRbaToken__T = typing.TypeVar('_fireActionWithRbaToken__T')  # <T>
    @staticmethod
    def fireActionWithRbaToken(callable: typing.Union[java.util.concurrent.Callable[_fireActionWithRbaToken__T], typing.Callable[[], _fireActionWithRbaToken__T]], rbaToken: cern.rbac.common.RbaToken) -> _fireActionWithRbaToken__T: ...
    _fireActionWithRbaTokenInSeparateThread__T = typing.TypeVar('_fireActionWithRbaTokenInSeparateThread__T')  # <T>
    @staticmethod
    def fireActionWithRbaTokenInSeparateThread(callable: typing.Union[java.util.concurrent.Callable[_fireActionWithRbaTokenInSeparateThread__T], typing.Callable[[], _fireActionWithRbaTokenInSeparateThread__T]], rbaToken: cern.rbac.common.RbaToken) -> java.util.concurrent.Future[_fireActionWithRbaTokenInSeparateThread__T]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.spi.rba")``.

    RbaUtils: typing.Type[RbaUtils]
