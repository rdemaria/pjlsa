import cern.rbac.common
import cern.rbac.common.authorization
import java.lang
import java.util
import typing



class AbstractRequest(java.lang.Cloneable):
    """
    public abstract class AbstractRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        This class represents abstract collection of the parameters for HTTP RBAC server.
    """
    def __init__(self): ...
    def clone(self) -> typing.Any:
        """
            Return clone of the object
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getParameters(self) -> java.util.Map['RequestParameterType', typing.Any]: ...
    def getRequestType(self) -> 'RequestType':
        """
            Returns the request type.
        
        """
        ...
    def getVersion(self) -> str:
        """
            Returns version string
        
            Returns:
                Version string
        
        
        """
        ...
    def isVerbose(self) -> bool:
        """
            Returns verbose flag
        
        """
        ...
    def toString(self) -> str:
        """
            Converts parameters into String. If the password is present, it's value replaced with stars.
        
            Overrides:
                 in class 
        
            Returns:
                String representation of the abstract parameters
        
        
        """
        ...

class AccessMapCommand(java.lang.Enum['AccessMapCommand']):
    """
    public enum AccessMapCommand extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.impl.request.AccessMapCommand`>
    
        This enumeration represents a set of commands acceptable for the access map generation.
    """
    MAPS_FOR_SERVER: typing.ClassVar['AccessMapCommand'] = ...
    MAPS_FOR_CLASS: typing.ClassVar['AccessMapCommand'] = ...
    MAPS_FOR_CLASS_TEST: typing.ClassVar['AccessMapCommand'] = ...
    MAPS_FOR_FRONT_END: typing.ClassVar['AccessMapCommand'] = ...
    @staticmethod
    def fromString(string: str) -> 'AccessMapCommand':
        """
            Returns enumeration value by it's name.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Name of the command
        
            Returns:
                enumeration value by it's name.
        
            Raises:
                : if there is no entry with such name.
        
        
        """
        ...
    def getBunchSize(self) -> int:
        """
            Returns bunch size for command.
        
            Returns:
                bunch size for command.
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns command name.
        
            Returns:
                Command name.
        
        
        """
        ...
    def getScriptName(self) -> str:
        """
            Returns script name.
        
            Returns:
                Script name.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AccessMapCommand':
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
    def values() -> typing.List['AccessMapCommand']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AccessMapCommand c : AccessMapCommand.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_RequestBuilder__Request = typing.TypeVar('_RequestBuilder__Request', bound=AbstractRequest)  # <Request>
class RequestBuilder(typing.Generic[_RequestBuilder__Request]):
    """
    public abstract class RequestBuilder<Request extends :class:`~cern.rbac.common.impl.request.AbstractRequest`> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Abstract builder base class for subclasses of the :class:`~cern.rbac.common.impl.request.AbstractRequest`.
    """
    def __init__(self, request: _RequestBuilder__Request): ...
    def addParameters(self, map: typing.Union[java.util.Map['RequestParameterType', typing.Any], typing.Mapping['RequestParameterType', typing.Any]]) -> None: ...
    def buildRequest(self) -> _RequestBuilder__Request:
        """
            Builds the target request
        
            Returns:
                Target request
        
            Raises:
                : if some arguments are missing or not correct
        
        
        """
        ...
    def setRequestType(self, requestType: 'RequestType') -> None:
        """
            Sets the request type
        
            Parameters:
                requestType (:class:`~cern.rbac.common.impl.request.RequestType`): the type of the request to set
        
        
        """
        ...
    def setVerbose(self, boolean: bool) -> 'RequestBuilder'[_RequestBuilder__Request]: ...
    def setVersion(self, string: str) -> 'RequestBuilder'[_RequestBuilder__Request]: ...

class RequestParameterType(java.lang.Enum['RequestParameterType']):
    """
    public enum RequestParameterType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.impl.request.RequestParameterType`>
    
        This enumeration defines all the possible request parameters to the remote RBAC server.
    """
    SERVER_ADDR_SUFFIX: typing.ClassVar['RequestParameterType'] = ...
    APPLICATION: typing.ClassVar['RequestParameterType'] = ...
    APPLICATION_ID: typing.ClassVar['RequestParameterType'] = ...
    TOKEN_FORMAT: typing.ClassVar['RequestParameterType'] = ...
    TOKEN_TYPE: typing.ClassVar['RequestParameterType'] = ...
    LIFETIME: typing.ClassVar['RequestParameterType'] = ...
    ACCOUNT_NAME: typing.ClassVar['RequestParameterType'] = ...
    USER_NAME: typing.ClassVar['RequestParameterType'] = ...
    PASSWORD: typing.ClassVar['RequestParameterType'] = ...
    ORIGIN: typing.ClassVar['RequestParameterType'] = ...
    ROLE: typing.ClassVar['RequestParameterType'] = ...
    TOKEN: typing.ClassVar['RequestParameterType'] = ...
    SIGN_BUFFER: typing.ClassVar['RequestParameterType'] = ...
    VERBOSE: typing.ClassVar['RequestParameterType'] = ...
    BUILD: typing.ClassVar['RequestParameterType'] = ...
    PARAMETER: typing.ClassVar['RequestParameterType'] = ...
    CLASS: typing.ClassVar['RequestParameterType'] = ...
    DEVICE: typing.ClassVar['RequestParameterType'] = ...
    PROPERTY: typing.ClassVar['RequestParameterType'] = ...
    OPERATION: typing.ClassVar['RequestParameterType'] = ...
    MCS_ROLE: typing.ClassVar['RequestParameterType'] = ...
    VERSION: typing.ClassVar['RequestParameterType'] = ...
    SAML_RESPONSE: typing.ClassVar['RequestParameterType'] = ...
    OAUTH_ACCESS_TOKEN: typing.ClassVar['RequestParameterType'] = ...
    KRB5_TICKET: typing.ClassVar['RequestParameterType'] = ...
    CHECKING_POLICY: typing.ClassVar['RequestParameterType'] = ...
    @staticmethod
    def fromString(string: str) -> 'RequestParameterType':
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
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RequestParameterType':
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
    def values() -> typing.List['RequestParameterType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (RequestParameterType c : RequestParameterType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...
    class ParameterTypeConstants:
        SERVER_ADDR_SUFFIX_CONSTANT: typing.ClassVar[str] = ...
        APPLICATION_CONSTANT: typing.ClassVar[str] = ...
        APPLICATION_ID_CONSTANT: typing.ClassVar[str] = ...
        TOKEN_FORMAT_CONSTANT: typing.ClassVar[str] = ...
        TOKEN_TYPE_CONSTANT: typing.ClassVar[str] = ...
        LIFETIME_CONSTANT: typing.ClassVar[str] = ...
        ACCOUNT_NAME_CONSTANT: typing.ClassVar[str] = ...
        USER_NAME_CONSTANT: typing.ClassVar[str] = ...
        PASSWORD_CONSTANT: typing.ClassVar[str] = ...
        ORIGIN_CONSTANT: typing.ClassVar[str] = ...
        ROLE_CONSTANT: typing.ClassVar[str] = ...
        TOKEN_CONSTANT: typing.ClassVar[str] = ...
        SIGN_BUFFER_CONSTANT: typing.ClassVar[str] = ...
        VERBOSE_CONSTANT: typing.ClassVar[str] = ...
        BUILD_CONSTANT: typing.ClassVar[str] = ...
        PARAMETER_CONSTANT: typing.ClassVar[str] = ...
        CLASS_CONSTANT: typing.ClassVar[str] = ...
        DEVICE_CONSTANT: typing.ClassVar[str] = ...
        PROPERTY_CONSTANT: typing.ClassVar[str] = ...
        OPERATION_CONSTANT: typing.ClassVar[str] = ...
        MCS_ROLE_CONSTANT: typing.ClassVar[str] = ...
        VERSION_CONSTANT: typing.ClassVar[str] = ...
        SAML_RESPONSE_CONSTANT: typing.ClassVar[str] = ...
        OAUTH_ACCESS_TOKEN_CONSTANT: typing.ClassVar[str] = ...
        KRB5_TICKET_CONSTANT: typing.ClassVar[str] = ...
        CHECKING_POLICY_CONSTANT: typing.ClassVar[str] = ...
        def __init__(self, requestParameterType: 'RequestParameterType'): ...

class RequestType(java.lang.Enum['RequestType']):
    """
    public enum RequestType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.impl.request.RequestType`>
    """
    AUTHENTICATE_EXPLICIT: typing.ClassVar['RequestType'] = ...
    AUTHENTICATE_LOCATION: typing.ClassVar['RequestType'] = ...
    AUTHENTICATE_KERBEROS: typing.ClassVar['RequestType'] = ...
    AUTHENTICATE_SAML: typing.ClassVar['RequestType'] = ...
    AUTHENTICATE_OAUTH: typing.ClassVar['RequestType'] = ...
    AUTHENTICATE_RENEWAL: typing.ClassVar['RequestType'] = ...
    CHECK_ACCESS: typing.ClassVar['RequestType'] = ...
    GENERATE_MAP: typing.ClassVar['RequestType'] = ...
    MCS_ROLE: typing.ClassVar['RequestType'] = ...
    MCS_PUBLIC_KEY: typing.ClassVar['RequestType'] = ...
    MCS_SIGN: typing.ClassVar['RequestType'] = ...
    @staticmethod
    def fromUri(string: str) -> 'RequestType': ...
    def getUri(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RequestType':
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
    def values() -> typing.List['RequestType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (RequestType c : RequestType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...
    class UriConstants:
        AUTHENTICATE_EXPLICIT_URI: typing.ClassVar[str] = ...
        AUTHENTICATE_LOCATION_URI: typing.ClassVar[str] = ...
        AUTHENTICATE_KERBEROS_URI: typing.ClassVar[str] = ...
        AUTHENTICATE_SAML_URI: typing.ClassVar[str] = ...
        AUTHENTICATE_OAUTH_URI: typing.ClassVar[str] = ...
        AUTHENTICATE_RENEWAL_URI: typing.ClassVar[str] = ...
        CHECK_ACCESS_URI: typing.ClassVar[str] = ...
        GENERATE_MAP_URI: typing.ClassVar[str] = ...
        MCS_ROLE_URI: typing.ClassVar[str] = ...
        MCS_PUBLIC_KEY_URI: typing.ClassVar[str] = ...
        MCS_SIGN_URI: typing.ClassVar[str] = ...

class ServerErrorCode(java.lang.Enum['ServerErrorCode']):
    """
    public enum ServerErrorCode extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.impl.request.ServerErrorCode`>
    
        This enumeration keeps all HTTP error codes for all Rba servers
    """
    BAD_REQUEST: typing.ClassVar['ServerErrorCode'] = ...
    AUTHENTICATION_FAILED: typing.ClassVar['ServerErrorCode'] = ...
    PROCESSING_ERROR: typing.ClassVar['ServerErrorCode'] = ...
    @staticmethod
    def fromInt(int: int) -> 'ServerErrorCode':
        """
            Converts error code into enumeration entry.
        
            Parameters:
                code (int): Error code as integer
        
            Returns:
                Enumeration entry
        
            Raises:
                : if unable to find an entry with given code
        
        
        """
        ...
    def getCode(self) -> int:
        """
            Retrieves HTTP error code as integer
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ServerErrorCode':
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
    def values() -> typing.List['ServerErrorCode']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ServerErrorCode c : ServerErrorCode.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AccessCheckerRequest(AbstractRequest):
    """
    public abstract class AccessCheckerRequest extends :class:`~cern.rbac.common.impl.request.AbstractRequest`
    
        Represents access checker request parameters
    """
    def __init__(self): ...
    def getCheckingPolicy(self) -> cern.rbac.common.authorization.CheckingPolicy:
        """
            Returns the checking policy
        
            Returns:
                the checking policy
        
        
        """
        ...
    def getDevice(self) -> str:
        """
            Returns the device name
        
            Returns:
                the device name
        
        
        """
        ...
    def getDeviceClass(self) -> str:
        """
            Returns the device class
        
            Returns:
                the device class
        
        
        """
        ...
    def getOperation(self) -> cern.rbac.common.authorization.Operation:
        """
            Returns the operation
        
            Returns:
                the operation
        
        
        """
        ...
    def getProperty(self) -> str:
        """
            Returns the property
        
            Returns:
                the property
        
        
        """
        ...
    def getToken(self) -> cern.rbac.common.RbaToken:
        """
            Returns the token
        
            Returns:
                the token
        
        
        """
        ...

class AccessCheckerRequestBuilder(RequestBuilder[AccessCheckerRequest]):
    """
    public class AccessCheckerRequestBuilder extends :class:`~cern.rbac.common.impl.request.RequestBuilder`<:class:`~cern.rbac.common.impl.request.AccessCheckerRequest`>
    
        Builder for the :class:`~cern.rbac.common.impl.request.AccessCheckerRequest` instances.
    """
    def buildRequest(self) -> AccessCheckerRequest:
        """
            Description copied from class: :meth:`~cern.rbac.common.impl.request.RequestBuilder.buildRequest`
            Builds the target request
        
            Overrides:
                :meth:`~cern.rbac.common.impl.request.RequestBuilder.buildRequest`Â in
                classÂ :class:`~cern.rbac.common.impl.request.RequestBuilder`
        
            Returns:
                Target request
        
        
        """
        ...
    @staticmethod
    def newInstance() -> 'AccessCheckerRequestBuilder':
        """
            Creates a new instance of the builder.
        
            Returns:
                new instance of the builder
        
        
        """
        ...
    def setCheckingPolicy(self, checkingPolicy: cern.rbac.common.authorization.CheckingPolicy) -> 'AccessCheckerRequestBuilder':
        """
            Sets the checking policy
        
            Parameters:
                checkingPolicy (:class:`~cern.rbac.common.authorization.CheckingPolicy`): Checking policy to set
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setDevice(self, string: str) -> 'AccessCheckerRequestBuilder':
        """
            Sets the device
        
            Parameters:
                device (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Device to set
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setDeviceClass(self, string: str) -> 'AccessCheckerRequestBuilder':
        """
            Sets the device class
        
            Parameters:
                deviceClass (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Device class to set
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setOperation(self, operation: cern.rbac.common.authorization.Operation) -> 'AccessCheckerRequestBuilder':
        """
            Sets the operation
        
            Parameters:
                operation (:class:`~cern.rbac.common.authorization.Operation`): Operation to set
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setProperty(self, string: str) -> 'AccessCheckerRequestBuilder':
        """
            Sets the property
        
            Parameters:
                property (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Property to set
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setToken(self, rbaToken: cern.rbac.common.RbaToken) -> 'AccessCheckerRequestBuilder':
        """
            Sets the token
        
            Parameters:
                token (:class:`~cern.rbac.common.RbaToken`): Token to set
        
            Returns:
                Reference to itself
        
        
        """
        ...

class AccessMapRequest(AbstractRequest):
    """
    public abstract class AccessMapRequest extends :class:`~cern.rbac.common.impl.request.AbstractRequest`
    
        Represents access map builder parameters
    """
    def __init__(self): ...
    def getCommand(self) -> AccessMapCommand:
        """
            Returns access map command
        
            Returns:
                access map command
        
        
        """
        ...
    def getParameter(self) -> str:
        """
            Returns command parameters (comma-separated list of strings)
        
            Returns:
                command parameters
        
        
        """
        ...
    def getToken(self) -> cern.rbac.common.RbaToken:
        """
            Returns the token
        
            Returns:
                the token
        
        
        """
        ...

class AccessMapRequestBuilder(RequestBuilder[AccessMapRequest]):
    """
    public class AccessMapRequestBuilder extends :class:`~cern.rbac.common.impl.request.RequestBuilder`<:class:`~cern.rbac.common.impl.request.AccessMapRequest`>
    
        Builder for the :class:`~cern.rbac.common.impl.request.AccessMapRequest` instances.
    """
    def buildRequest(self) -> AccessMapRequest:
        """
            Description copied from class: :meth:`~cern.rbac.common.impl.request.RequestBuilder.buildRequest`
            Builds the target request
        
            Overrides:
                :meth:`~cern.rbac.common.impl.request.RequestBuilder.buildRequest`Â in
                classÂ :class:`~cern.rbac.common.impl.request.RequestBuilder`
        
            Returns:
                Target request
        
        
        """
        ...
    @staticmethod
    def newInstance() -> 'AccessMapRequestBuilder':
        """
            Creates a new instance of the builder.
        
            Returns:
                new instance of the builder
        
        
        """
        ...
    def setCommand(self, accessMapCommand: AccessMapCommand) -> 'AccessMapRequestBuilder':
        """
            Sets :class:`~cern.rbac.common.impl.request.AccessMapCommand` for request
        
            Parameters:
                command (:class:`~cern.rbac.common.impl.request.AccessMapCommand`): :class:`~cern.rbac.common.impl.request.AccessMapCommand` for request
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setParameter(self, string: str) -> 'AccessMapRequestBuilder':
        """
            Sets parameter for the request
        
            Parameters:
                parameter (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Parameter to set
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setToken(self, rbaToken: cern.rbac.common.RbaToken) -> 'AccessMapRequestBuilder':
        """
            Sets the token
        
            Parameters:
                token (:class:`~cern.rbac.common.RbaToken`): Token to set
        
            Returns:
                Reference to itself
        
        
        """
        ...

class AuthenticationRequest(AbstractRequest):
    """
    public abstract class AuthenticationRequest extends :class:`~cern.rbac.common.impl.request.AbstractRequest`
    
        This class represents parameters for all types of authentication requests
    """
    def __init__(self): ...
    def getAccountName(self) -> str:
        """
            Returns account name
        
            Returns:
                the account name
        
        
        """
        ...
    def getApplication(self) -> str:
        """
            Returns application name
        
            Returns:
                application name
        
        
        """
        ...
    def getKerberosTicket(self) -> str:
        """
            Returns Kerberos ticket encoded in Base64
        
            Returns:
                Kerberos ticket encoded in Base64
        
        
        """
        ...
    def getLifetime(self) -> int:
        """
            Returns token lifetime
        
            Returns:
                the token lifetime
        
        
        """
        ...
    def getOauthAccessToken(self) -> str:
        """
            Returns OAuth 2.0 access token
        
            Returns:
                OAuth 2.0 access token
        
        
        """
        ...
    def getOrigin(self) -> cern.rbac.common.RbaToken:
        """
            Returns the original token
        
            Returns:
                the original token
        
        
        """
        ...
    def getPassword(self) -> str:
        """
            Returns the password
        
            Returns:
                the password
        
        
        """
        ...
    def getRoles(self) -> typing.List[str]:
        """
            Returns roles
        
            Returns:
                the roles
        
        
        """
        ...
    def getSamlResponse(self) -> str:
        """
            Returns SAML response
        
            Returns:
                SAML response
        
        
        """
        ...
    def getTokenType(self) -> cern.rbac.common.TokenType:
        """
            Returns token type
        
            Returns:
                the token type
        
        
        """
        ...
    def getUserName(self) -> str:
        """
            Returns user name
        
            Returns:
                the user name
        
        
        """
        ...

class AuthenticationRequestBuilder(RequestBuilder[AuthenticationRequest]):
    """
    public class AuthenticationRequestBuilder extends :class:`~cern.rbac.common.impl.request.RequestBuilder`<:class:`~cern.rbac.common.impl.request.AuthenticationRequest`>
    
        Builder for the :class:`~cern.rbac.common.impl.request.AuthenticationRequest` instances.
    """
    @staticmethod
    def newInstance() -> 'AuthenticationRequestBuilder':
        """
            Creates a new instance of the builder.
        
            Returns:
                new instance of the builder
        
        
        """
        ...
    def setAccountName(self, string: str) -> 'AuthenticationRequestBuilder': ...
    def setApplication(self, string: str) -> 'AuthenticationRequestBuilder': ...
    def setKerberosTicket(self, byteArray: typing.List[int]) -> 'AuthenticationRequestBuilder': ...
    def setLifetime(self, int: int) -> 'AuthenticationRequestBuilder': ...
    def setOauthAccessToken(self, string: str) -> 'AuthenticationRequestBuilder': ...
    def setOrigin(self, rbaToken: cern.rbac.common.RbaToken) -> 'AuthenticationRequestBuilder':
        """
            Sets original token
        
            Parameters:
                origin (:class:`~cern.rbac.common.RbaToken`): the original token to set
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setPassword(self, string: str) -> 'AuthenticationRequestBuilder': ...
    def setRoles(self, stringArray: typing.List[str]) -> 'AuthenticationRequestBuilder': ...
    def setSamlResponse(self, string: str) -> 'AuthenticationRequestBuilder': ...
    def setTokenType(self, tokenType: cern.rbac.common.TokenType) -> 'AuthenticationRequestBuilder': ...
    def setUserName(self, string: str) -> 'AuthenticationRequestBuilder': ...

class McsKeyRequest(AbstractRequest):
    """
    public abstract class McsKeyRequest extends :class:`~cern.rbac.common.impl.request.AbstractRequest`
    
        Represents parameters for MSC request for getting public key
    """
    def __init__(self): ...
    def getDevice(self) -> str:
        """
            Returns device name
        
            Returns:
                device name
        
        
        """
        ...
    def getDeviceClass(self) -> str:
        """
            Returns device class name
        
            Returns:
                device class name
        
        
        """
        ...
    def getMCSRole(self) -> str:
        """
            Returns MCS role
        
            Returns:
                MCS role
        
        
        """
        ...
    def getProperty(self) -> str:
        """
            Returns property name
        
            Returns:
                property name
        
        
        """
        ...

class McsKeyRequestBuilder(RequestBuilder[McsKeyRequest]):
    """
    public class McsKeyRequestBuilder extends :class:`~cern.rbac.common.impl.request.RequestBuilder`<:class:`~cern.rbac.common.impl.request.McsKeyRequest`>
    
        Builder for the :class:`~cern.rbac.common.impl.request.McsKeyRequest` instances.
    """
    def buildRequest(self) -> McsKeyRequest:
        """
            Description copied from class: :meth:`~cern.rbac.common.impl.request.RequestBuilder.buildRequest`
            Builds the target request
        
            Overrides:
                :meth:`~cern.rbac.common.impl.request.RequestBuilder.buildRequest`Â in
                classÂ :class:`~cern.rbac.common.impl.request.RequestBuilder`
        
            Returns:
                Target request
        
        
        """
        ...
    @staticmethod
    def newInstance() -> 'McsKeyRequestBuilder':
        """
            Creates a new instance of the builder.
        
            Returns:
                new instance of the builder
        
        
        """
        ...
    def setDevice(self, string: str) -> 'McsKeyRequestBuilder':
        """
            Sets the device
        
            Parameters:
                device (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Device to set
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setDeviceClass(self, string: str) -> 'McsKeyRequestBuilder':
        """
            Sets the device class
        
            Parameters:
                deviceClass (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Device class to set
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setMCSRole(self, string: str) -> 'McsKeyRequestBuilder':
        """
            Sets the MCS role
        
            Parameters:
                role (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): MCS role to set
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setProperty(self, string: str) -> 'McsKeyRequestBuilder':
        """
            Sets the property
        
            Parameters:
                property (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Property to set
        
            Returns:
                Reference to itself
        
        
        """
        ...

class McsRoleRequest(AbstractRequest):
    """
    public class McsRoleRequest extends :class:`~cern.rbac.common.impl.request.AbstractRequest`
    """
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, map: typing.Union[java.util.Map[RequestParameterType, typing.Any], typing.Mapping[RequestParameterType, typing.Any]]): ...
    def getDevice(self) -> str: ...
    def getDeviceClass(self) -> str: ...
    def getProperty(self) -> str: ...

class McsSignRequest(AbstractRequest):
    """
    public abstract class McsSignRequest extends :class:`~cern.rbac.common.impl.request.AbstractRequest`
    
        Represents parameters for MSC request for signing buffer of bytes
    """
    def __init__(self): ...
    def getSignBuffer(self) -> typing.List[int]:
        """
            Returns sign buffer
        
            Returns:
                sign buffer
        
        
        """
        ...
    def getToken(self) -> cern.rbac.common.RbaToken:
        """
            Returns the token
        
            Returns:
                the token
        
        
        """
        ...

class McsSignRequestBuilder(RequestBuilder[McsSignRequest]):
    """
    public class McsSignRequestBuilder extends :class:`~cern.rbac.common.impl.request.RequestBuilder`<:class:`~cern.rbac.common.impl.request.McsSignRequest`>
    
        Builder for the :class:`~cern.rbac.common.impl.request.McsSignRequest` instances.
    """
    def buildRequest(self) -> McsSignRequest:
        """
            Description copied from class: :meth:`~cern.rbac.common.impl.request.RequestBuilder.buildRequest`
            Builds the target request
        
            Overrides:
                :meth:`~cern.rbac.common.impl.request.RequestBuilder.buildRequest`Â in
                classÂ :class:`~cern.rbac.common.impl.request.RequestBuilder`
        
            Returns:
                Target request
        
        
        """
        ...
    @staticmethod
    def newInstance() -> 'McsSignRequestBuilder':
        """
            Creates a new instance of the builder.
        
            Returns:
                new instance of the builder
        
        
        """
        ...
    def setSignBuffer(self, byteArray: typing.List[int]) -> 'McsSignRequestBuilder':
        """
            Sets sign buffer
        
            Parameters:
                signBuffer (byte[]): Bytes buffer to sign
        
            Returns:
                Reference to itself
        
        
        """
        ...
    def setToken(self, rbaToken: cern.rbac.common.RbaToken) -> 'McsSignRequestBuilder':
        """
            Sets the token
        
            Parameters:
                token (:class:`~cern.rbac.common.RbaToken`): Token to set
        
            Returns:
                Reference to itself
        
        
        """
        ...

class AccessCheckerRequestImpl(AccessCheckerRequest):
    """
    public class AccessCheckerRequestImpl extends :class:`~cern.rbac.common.impl.request.AccessCheckerRequest`
    
        Represents access checker request parameters
    """
    def __init__(self): ...

class AccessMapRequestImpl(AccessMapRequest):
    """
    public class AccessMapRequestImpl extends :class:`~cern.rbac.common.impl.request.AccessMapRequest`
    
        Represents access checker request parameters
    """
    def __init__(self): ...
    def setCommand(self, accessMapCommand: AccessMapCommand) -> None:
        """
            Sets :class:`~cern.rbac.common.impl.request.AccessMapCommand` for request
        
            Parameters:
                command (:class:`~cern.rbac.common.impl.request.AccessMapCommand`): :class:`~cern.rbac.common.impl.request.AccessMapCommand` for request
        
        
        """
        ...
    def setParameter(self, string: str) -> None:
        """
            Sets parameter for the request
        
            Parameters:
                parameter (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Parameter to set
        
        
        """
        ...
    def setToken(self, rbaToken: cern.rbac.common.RbaToken) -> None:
        """
            Sets the token
        
            Parameters:
                token (:class:`~cern.rbac.common.RbaToken`): Token to set
        
        
        """
        ...

class McsKeyRequestImpl(McsKeyRequest):
    """
    public class McsKeyRequestImpl extends :class:`~cern.rbac.common.impl.request.McsKeyRequest`
    
        Represents parameters for MCS public key request
    """
    def __init__(self): ...

class McsSignRequestImpl(McsSignRequest):
    """
    public class McsSignRequestImpl extends :class:`~cern.rbac.common.impl.request.McsSignRequest`
    
        Represents parameters for MSC request for signing buffer of bytes
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl.request")``.

    AbstractRequest: typing.Type[AbstractRequest]
    AccessCheckerRequest: typing.Type[AccessCheckerRequest]
    AccessCheckerRequestBuilder: typing.Type[AccessCheckerRequestBuilder]
    AccessCheckerRequestImpl: typing.Type[AccessCheckerRequestImpl]
    AccessMapCommand: typing.Type[AccessMapCommand]
    AccessMapRequest: typing.Type[AccessMapRequest]
    AccessMapRequestBuilder: typing.Type[AccessMapRequestBuilder]
    AccessMapRequestImpl: typing.Type[AccessMapRequestImpl]
    AuthenticationRequest: typing.Type[AuthenticationRequest]
    AuthenticationRequestBuilder: typing.Type[AuthenticationRequestBuilder]
    McsKeyRequest: typing.Type[McsKeyRequest]
    McsKeyRequestBuilder: typing.Type[McsKeyRequestBuilder]
    McsKeyRequestImpl: typing.Type[McsKeyRequestImpl]
    McsRoleRequest: typing.Type[McsRoleRequest]
    McsSignRequest: typing.Type[McsSignRequest]
    McsSignRequestBuilder: typing.Type[McsSignRequestBuilder]
    McsSignRequestImpl: typing.Type[McsSignRequestImpl]
    RequestBuilder: typing.Type[RequestBuilder]
    RequestParameterType: typing.Type[RequestParameterType]
    RequestType: typing.Type[RequestType]
    ServerErrorCode: typing.Type[ServerErrorCode]
