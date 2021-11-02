import java.lang
import java.util
import typing



class AbstractResponse(java.lang.Cloneable):
    """
    public abstract class AbstractResponse extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Class :class:`~cern.rbac.common.impl.response.AbstractResponse` represents response of the RBAC server with some
        predefined parameters.
    """
    def __init__(self): ...
    def clone(self) -> typing.Any:
        """
            Clones the object
        
            Overrides:
                 in class 
        
            Returns:
                Clone of the request
        
        
        """
        ...
    def getException(self) -> str:
        """
            Returns response exception or empty string if no exception happened
        
            Returns:
                Response exception
        
        
        """
        ...
    def getExceptionTrace(self) -> str:
        """
            Returns response exception trace or empty string if no exception happened
        
            Returns:
                Response exception
        
        
        """
        ...
    def getLog(self) -> str:
        """
            Returns log from the server side for the request handling
        
            Returns:
                log from the server side for the request handling
        
        
        """
        ...
    def getParameters(self) -> java.util.Map['ResponseParameterType', typing.Any]: ...
    def getProcessTime(self) -> int:
        """
            Returns time that server spent handling the request, in milliseconds
        
            Returns:
                time that server spent handling the request, in milliseconds
        
        
        """
        ...
    def getResponseStatus(self) -> 'ResponseStatus':
        """
            Returns response status :class:`~cern.rbac.common.impl.response.ResponseStatus`
        
            Returns:
                Response status :class:`~cern.rbac.common.impl.response.ResponseStatus`
        
        
        """
        ...
    def toString(self) -> str:
        """
            Converts parameters into String.
        
            Overrides:
                 in class 
        
            Returns:
                String representation of the abstract parameters
        
        
        """
        ...

class FaultResponse:
    """
    public class FaultResponse extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Contains basic information about processing errors that occurred on the server.
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
    public abstract class ResponseBuilder<Response extends :class:`~cern.rbac.common.impl.response.AbstractResponse`> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Abstract builder base class for subclasses of the :class:`~cern.rbac.common.impl.response.AbstractResponse`
    """
    def __init__(self, response: _ResponseBuilder__Response): ...
    def addParameters(self, map: typing.Union[java.util.Map['ResponseParameterType', typing.Any], typing.Mapping['ResponseParameterType', typing.Any]]) -> None: ...
    def buildResponse(self) -> _ResponseBuilder__Response:
        """
            Builds the target response
        
            Returns:
                Target response
        
            Raises:
                : if some arguments are missing or not correct
        
        
        """
        ...
    @typing.overload
    def setException(self, exception: java.lang.Exception, responseStatus: 'ResponseStatus') -> None:
        """
            This method accepts `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>` and then stores
            exception message and exception stack trace inside the response.
        
            Parameters:
                exception (`Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`): Exception to store
        
        
        """
        ...
    @typing.overload
    def setException(self, string: str) -> None:
        """
            Sets response exception
        
            Parameters:
                exception (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Response exception
        
        """
        ...
    def setExceptionTrace(self, string: str) -> None:
        """
            Sets response exception trace
        
            Parameters:
                exception (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Response exception trace
        
        
        """
        ...
    def setLog(self, string: str) -> None:
        """
            Sets response server log
        
            Parameters:
                log (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Response server log
        
        
        """
        ...
    def setProcessTime(self, int: int) -> None:
        """
            Sets response process time
        
            Parameters:
                time (int): Response process time
        
        
        """
        ...
    def setResponseStatus(self, responseStatus: 'ResponseStatus') -> None:
        """
            Sets response status
        
            Parameters:
                status (:class:`~cern.rbac.common.impl.response.ResponseStatus`): Response status
        
        
        """
        ...

class ResponseParameterType(java.lang.Enum['ResponseParameterType']):
    """
    public enum ResponseParameterType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.impl.response.ResponseParameterType`>
    
        ResponseParameterType enumeration defined all the possible types of the server response parameters. Each entry comes
        together with its name, that used to store parameter in the cmw-serializer container.
    """
    STATUS: typing.ClassVar['ResponseParameterType'] = ...
    EXCEPTION: typing.ClassVar['ResponseParameterType'] = ...
    EXCEPTION_TRACE: typing.ClassVar['ResponseParameterType'] = ...
    PROCESS_TIME: typing.ClassVar['ResponseParameterType'] = ...
    LOG: typing.ClassVar['ResponseParameterType'] = ...
    @staticmethod
    def fromString(string: str) -> 'ResponseParameterType':
        """
            Converts String value into enumeration entry.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Name of the entry
        
            Returns:
                Enumeration entry
        
            Raises:
                : if unable to find an entry with given name
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns entry name, used to make response on the server.
        
            Returns:
                entry name, used to make response on the server.
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ResponseParameterType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['ResponseParameterType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ResponseParameterType c : ResponseParameterType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ResponseStatus(java.lang.Enum['ResponseStatus']):
    """
    public enum ResponseStatus extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.impl.response.ResponseStatus`>
    
        This enumeration defines all statuses of the RBAC server responses
    """
    OK: typing.ClassVar['ResponseStatus'] = ...
    BAD_REQUEST: typing.ClassVar['ResponseStatus'] = ...
    AUTHENTICATION_FAILED: typing.ClassVar['ResponseStatus'] = ...
    PROCESSING_ERROR: typing.ClassVar['ResponseStatus'] = ...
    @staticmethod
    def fromString(string: str) -> 'ResponseStatus':
        """
            Converts String value into enumeration entry.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Name of the entry
        
            Returns:
                Enumeration entry
        
            Raises:
                : if unable to find an entry with given name
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns status name
        
            Returns:
                status name
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ResponseStatus':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['ResponseStatus']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ResponseStatus c : ResponseStatus.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AccessMapResponse(AbstractResponse):
    """
    public class AccessMapResponse extends :class:`~cern.rbac.common.impl.response.AbstractResponse`
    
        Represents response of the access map generation
    """
    def __init__(self): ...

class AccessMapResponseBuilder(ResponseBuilder[AccessMapResponse]):
    """
    public class AccessMapResponseBuilder extends :class:`~cern.rbac.common.impl.response.ResponseBuilder`<:class:`~cern.rbac.common.impl.response.AccessMapResponse`>
    
        Builder for the :class:`~cern.rbac.common.impl.response.AccessMapResponse` instances.
    """
    @staticmethod
    def newInstance() -> 'AccessMapResponseBuilder':
        """
            Creates a new instance of the builder.
        
            Returns:
                new instance of the builder
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl.response")``.

    AbstractResponse: typing.Type[AbstractResponse]
    AccessMapResponse: typing.Type[AccessMapResponse]
    AccessMapResponseBuilder: typing.Type[AccessMapResponseBuilder]
    FaultResponse: typing.Type[FaultResponse]
    ResponseBuilder: typing.Type[ResponseBuilder]
    ResponseParameterType: typing.Type[ResponseParameterType]
    ResponseStatus: typing.Type[ResponseStatus]
