import java.lang
import java.util
import typing



class AbstractResponse(java.lang.Cloneable):
    """
    Java class 'cern.rbac.common.impl.response.AbstractResponse'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.lang.Cloneable
    
      Constructors:
        * AbstractResponse()
    
    """
    def __init__(self): ...
    def clone(self) -> typing.Any: ...
    def getException(self) -> str: ...
    def getExceptionTrace(self) -> str: ...
    def getLog(self) -> str: ...
    def getParameters(self) -> java.util.Map['ResponseParameterType', typing.Any]: ...
    def getProcessTime(self) -> int: ...
    def getResponseStatus(self) -> 'ResponseStatus': ...
    def toString(self) -> str: ...

class FaultResponse:
    """
    Java class 'cern.rbac.common.impl.response.FaultResponse'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * FaultResponse(java.lang.String)
        * FaultResponse(java.lang.Exception)
        * FaultResponse()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    def getMessage(self) -> str: ...
    def getStacktrace(self) -> str: ...

_ResponseBuilder__Response = typing.TypeVar('_ResponseBuilder__Response', bound=AbstractResponse)  # <Response>
class ResponseBuilder(typing.Generic[_ResponseBuilder__Response]):
    """
    Java class 'cern.rbac.common.impl.response.ResponseBuilder'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ResponseBuilder(cern.rbac.common.impl.response.AbstractResponse)
    
    """
    def __init__(self, response: _ResponseBuilder__Response): ...
    def addParameters(self, map: typing.Union[java.util.Map['ResponseParameterType', typing.Any], typing.Mapping['ResponseParameterType', typing.Any]]) -> None: ...
    def buildResponse(self) -> _ResponseBuilder__Response: ...
    @typing.overload
    def setException(self, exception: java.lang.Exception, responseStatus: 'ResponseStatus') -> None: ...
    @typing.overload
    def setException(self, string: str) -> None: ...
    def setExceptionTrace(self, string: str) -> None: ...
    def setLog(self, string: str) -> None: ...
    def setProcessTime(self, int: int) -> None: ...
    def setResponseStatus(self, responseStatus: 'ResponseStatus') -> None: ...

class ResponseParameterType(java.lang.Enum['ResponseParameterType']):
    """
    Java class 'cern.rbac.common.impl.response.ResponseParameterType'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        STATUS (cern.rbac.common.impl.response.ResponseParameterType): final static enum constant
        EXCEPTION (cern.rbac.common.impl.response.ResponseParameterType): final static enum constant
        EXCEPTION_TRACE (cern.rbac.common.impl.response.ResponseParameterType): final static enum constant
        PROCESS_TIME (cern.rbac.common.impl.response.ResponseParameterType): final static enum constant
        LOG (cern.rbac.common.impl.response.ResponseParameterType): final static enum constant
    
    """
    STATUS: typing.ClassVar['ResponseParameterType'] = ...
    EXCEPTION: typing.ClassVar['ResponseParameterType'] = ...
    EXCEPTION_TRACE: typing.ClassVar['ResponseParameterType'] = ...
    PROCESS_TIME: typing.ClassVar['ResponseParameterType'] = ...
    LOG: typing.ClassVar['ResponseParameterType'] = ...
    @staticmethod
    def fromString(string: str) -> 'ResponseParameterType': ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ResponseParameterType': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['ResponseParameterType']: ...

class ResponseStatus(java.lang.Enum['ResponseStatus']):
    """
    Java class 'cern.rbac.common.impl.response.ResponseStatus'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        OK (cern.rbac.common.impl.response.ResponseStatus): final static enum constant
        BAD_REQUEST (cern.rbac.common.impl.response.ResponseStatus): final static enum constant
        AUTHENTICATION_FAILED (cern.rbac.common.impl.response.ResponseStatus): final static enum constant
        PROCESSING_ERROR (cern.rbac.common.impl.response.ResponseStatus): final static enum constant
    
    """
    OK: typing.ClassVar['ResponseStatus'] = ...
    BAD_REQUEST: typing.ClassVar['ResponseStatus'] = ...
    AUTHENTICATION_FAILED: typing.ClassVar['ResponseStatus'] = ...
    PROCESSING_ERROR: typing.ClassVar['ResponseStatus'] = ...
    @staticmethod
    def fromString(string: str) -> 'ResponseStatus': ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ResponseStatus': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['ResponseStatus']: ...

class AccessMapResponse(AbstractResponse):
    """
    Java class 'cern.rbac.common.impl.response.AccessMapResponse'
    
        Extends:
            cern.rbac.common.impl.response.AbstractResponse
    
      Constructors:
        * AccessMapResponse()
    
    """
    def __init__(self): ...

class AccessMapResponseBuilder(ResponseBuilder[AccessMapResponse]):
    """
    Java class 'cern.rbac.common.impl.response.AccessMapResponseBuilder'
    
        Extends:
            cern.rbac.common.impl.response.ResponseBuilder
    
    """
    @staticmethod
    def newInstance() -> 'AccessMapResponseBuilder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl.response")``.

    AbstractResponse: typing.Type[AbstractResponse]
    AccessMapResponse: typing.Type[AccessMapResponse]
    AccessMapResponseBuilder: typing.Type[AccessMapResponseBuilder]
    FaultResponse: typing.Type[FaultResponse]
    ResponseBuilder: typing.Type[ResponseBuilder]
    ResponseParameterType: typing.Type[ResponseParameterType]
    ResponseStatus: typing.Type[ResponseStatus]
