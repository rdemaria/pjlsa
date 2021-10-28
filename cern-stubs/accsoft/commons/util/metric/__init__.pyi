import java.util
import typing



_RequestCounter__T = typing.TypeVar('_RequestCounter__T')  # <T>
class RequestCounter(typing.Generic[_RequestCounter__T]):
    """
    Java class 'cern.accsoft.commons.util.metric.RequestCounter'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RequestCounter()
    
    """
    def __init__(self): ...
    @typing.overload
    def getNumberOfRequests(self) -> java.util.Map[_RequestCounter__T, int]: ...
    @typing.overload
    def getNumberOfRequests(self, t: _RequestCounter__T) -> int: ...
    def getTotalNumberOfRequests(self) -> int: ...
    def onRequest(self, t: _RequestCounter__T) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.metric")``.

    RequestCounter: typing.Type[RequestCounter]
