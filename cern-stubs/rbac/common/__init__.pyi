import cern.cmw.util.config
import cern.rbac.common.authentication
import cern.rbac.common.authorization
import cern.rbac.common.impl
import cern.rbac.common.impl.serialization.decode
import cern.rbac.common.test
import java.io
import java.lang
import java.net
import java.nio
import java.security
import java.time
import java.util
import typing



class AppPrincipal(java.security.Principal):
    """
    public interface AppPrincipal extends `Principal <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/security/Principal.html?is-external=true>`
    
        Descriptor of an Application which is providing client-side execution environment.
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getTimeout(self) -> int:
        """
            Gets the application timeout in minutes.
        
            Returns:
                application timeout in minutes or null value if it is not defined.
        
        
        """
        ...
    def hashCode(self) -> int: ...
    def isCritical(self) -> bool:
        """
            Checks whether this is a critical application.
        
            Returns:
                :code:`true` if this is a critical application, otherwise :code:`false`
        
        
        """
        ...
    def toString(self) -> str: ...

class AuthenticationType(java.lang.Enum['AuthenticationType']):
    """
    public enum AuthenticationType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.AuthenticationType`>
    
        Enum type which specifies different methods of authentication.
    """
    NICE: typing.ClassVar['AuthenticationType'] = ...
    LOCATION: typing.ClassVar['AuthenticationType'] = ...
    CERTIFICATE: typing.ClassVar['AuthenticationType'] = ...
    SSO_PICKER: typing.ClassVar['AuthenticationType'] = ...
    RENEWAL: typing.ClassVar['AuthenticationType'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AuthenticationType':
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
    def values() -> typing.List['AuthenticationType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AuthenticationType c : AuthenticationType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ExtraFields:
    """
    public class ExtraFields extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Extra fields in the Rba token. This data is used internally by the Rba client and should be disregarded elsewhere.
    """
    def __init__(self, tokenType: 'TokenType', roleArray: typing.List['Role']): ...
    def getRolesHint(self) -> typing.List['Role']:
        """
            Returns roles hints
        
            Returns:
                roles hints
        
        
        """
        ...
    def getTokenType(self) -> 'TokenType':
        """
            Returns token type
        
            Returns:
                token type
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class LocationPrincipal(java.security.Principal):
    """
    public interface LocationPrincipal extends `Principal <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/security/Principal.html?is-external=true>`
    
        Descriptor of a Location from where the authentication process was performed.
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getAddress(self) -> java.net.InetAddress:
        """
            Gets the network address of the location.
        
            Returns:
                network address of the location
        
        
        """
        ...
    def getDefaultUser(self) -> str:
        """
            TODO: review if this is still used !! Gets default user for this location.
        
            Returns:
                default user for this location
        
        
        """
        ...
    def hashCode(self) -> int: ...
    def isAuthRequired(self) -> bool:
        """
            Checks whether the user authentication is required for this location.
        
            Returns:
                :code:`true` if the user authentication is required for this location
        
        
        """
        ...
    def toString(self) -> str: ...

class MasterToken:
    """
    public class MasterToken extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self, rbaToken: 'RbaToken'): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getAuthTime(self) -> java.time.Instant:
        """
            Gets the time when this token was created.
        
            Returns:
                token creation time.
        
        
        """
        ...
    def getEncoded(self) -> typing.List[int]:
        """
            Gets a binary representation of the underlying RbaToken. This includes all the fields and the original signature.
        
            Returns:
                a copy of the internal byte array.
        
        
        """
        ...
    def getEndTime(self) -> java.time.Instant:
        """
            Gets the time when this token expires. If the token never expires, this method returns a very large date, not null.
        
            Returns:
                token expiration time.
        
        
        """
        ...
    def getExtra(self) -> ExtraFields:
        """
            Gets the ExtraFields of the underlying RbaToken. ExtraFields contain the token type and the roles hint.
        
            Returns:
                the :class:`~cern.rbac.common.ExtraFields` of the token.
        
        
        """
        ...
    def getLocation(self) -> LocationPrincipal:
        """
            Gets the location descriptor.
        
            Returns:
                location descriptor.
        
        
        """
        ...
    def getUser(self) -> 'UserPrincipal':
        """
            Gets the user principal.
        
            Returns:
                user principal.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def isValid(self) -> bool:
        """
            Checks whether the token is still valid (hasn't expired). As it's impossible to create tokens in the future, we don't
            check the authentication time here.
        
            Returns:
                true if the token has not expired yet
        
        """
        ...
    @typing.overload
    def isValid(self, duration: java.time.Duration) -> bool:
        """
            Checks whether the token is still valid (hasn't expired) for the requested duration.. As it's impossible to create
            tokens in the future, we don't check the authentication time here.
        
            Parameters:
                timeFrame (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>`): requested duration when token should be still valid
        
            Returns:
                true if the token will be still valid for the requested amount of seconds
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class RbaToken(java.io.Serializable):
    """
    public final class RbaToken extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        The RBA Token represents a security credential for the client application, based on the application's name, location,
        and the user name. The token is issued by the RBA server and is digitally signed with a private key. The application can
        use the token as a proof of its identity during critical operations (e.g., settings).
    
        Three main attributes of the token are **application**, **location**, and **user**. When the RBA server issues a token,
        it's supposed to have reasonable evidences that these three values are correct. For example, the location attribute
        matches a network address where the request comes from, and the user is authenticated in a way adequate to the
        situation.
    
        Two time attributes, **authTime** and **endTime**, describe when the token was initially created and when it expires. As
        it's not possible to issue postponed tokens, the authentication time is merely informative. The expiration time is set
        by the RBA server according to an information from the database and must be used to check whether the ticket is still
        valid - the :meth:`~cern.rbac.common.RbaToken.isValid` method should be used to check the validity of a token.
    
        The RBA server signs tokens with its private key. It's assumed that nobody else in the world knows it. So, if the
        application can verify the signature using the :meth:`~cern.rbac.common.RbaToken.verify` method providing the server's
        public key, it may reasonable believe that the token is genuine. For the case when the server is changing its private
        keys, the :meth:`~cern.rbac.common.RbaToken.verify` method can accept more than one public key. The method succeeds if
        at least one public key can verify the signature. It's a responsibility of other part of the infrastructure to
        distribute the server public keys in a secure manner.
    
        The supplementary **serialId** attribute contains a random unique identifier. It is automatically assigned to every
        instance and retains its value through all serializations. This field can be used by a high-level protocol for caching
        the tokens, replay detection, etc.
    
        The primary RBA token data is stored as a byte array, in a format defined in the specification on RBAC wiki page. To
        obtain a copy of this array, use the :meth:`~cern.rbac.common.RbaToken.getEncoded` method. In order to restore the
        token, use the :meth:`~cern.rbac.common.RbaToken.parseAndValidate` constructor which de-serializes the state of a token
        from the byte array. The same mechanism is used during normal Java serialization. The byte array is the only
        *non-transient* attribute of the class. All other fields are automatically filled out from it after the default
        de-serialization procedure is complete. This guarantees the integrity of the token and speeds up its serialization and
        signature verification.
    
        Also see:
            :meth:`~serialized`
    """
    EMPTY_TOKEN: typing.ClassVar['RbaToken'] = ...
    """
    public static final :class:`~cern.rbac.common.RbaToken` EMPTY_TOKEN
    
        Singleton empty token
    
    """
    @typing.overload
    def __init__(self, byteArray: typing.List[int]): ...
    @typing.overload
    def __init__(self, byteArray: typing.List[int], tokenDecoder: cern.rbac.common.impl.serialization.decode.TokenDecoder): ...
    @typing.overload
    def __init__(self, byteArray: typing.List[int], int: int, int2: int): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getApplication(self) -> AppPrincipal:
        """
            Gets the application descriptor.
        
            Returns:
                application descriptor.
        
        
        """
        ...
    def getAuthTime(self) -> java.util.Date:
        """
            Gets the time when this token was created.
        
            Returns:
                token creation time.
        
        
        """
        ...
    def getEncoded(self) -> typing.List[int]:
        """
            Gets a binary representation of this token. This includes all the fields and the original signature.
        
            Returns:
                a copy of the internal byte array.
        
        
        """
        ...
    def getEndTime(self) -> java.util.Date:
        """
            Gets the time when this token expires. If the token never expires, this method returns a very large date, not null.
        
            Returns:
                token expiration time.
        
        
        """
        ...
    def getExtra(self) -> ExtraFields:
        """
            Gets the ExtraFields of the underlying RbaToken.
        
            Returns:
                the :class:`~cern.rbac.common.ExtraFields` of the token.
        
            Also see:
                :class:`~cern.rbac.common.ExtraFields`
        
        
        """
        ...
    def getLocation(self) -> LocationPrincipal:
        """
            Gets the location descriptor.
        
            Returns:
                location descriptor.
        
        
        """
        ...
    def getSerialId(self) -> int:
        """
            Gets the unique serial ID number of this token.
        
            Returns:
                serial ID.
        
        
        """
        ...
    def getType(self) -> 'TokenType':
        """
            Gets the type of this token which can be either Application, Master or Local Master.
        
            Returns:
                type of this token
        
        
        """
        ...
    def getUser(self) -> 'UserPrincipal':
        """
            Gets the user principal.
        
            Returns:
                user principal.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            This method returns boolean flag indicating whether the token is empty. Empty token means no authentication was done.
        
            Returns:
                true if token is empty
        
        
        """
        ...
    @typing.overload
    def isValid(self) -> bool:
        """
            Checks whether the token is still valid (hasn't expired). As it's impossible to create tokens in the future, we don't
            check the authentication time here.
        
            Returns:
                true if the token has not expired yet
        
        """
        ...
    @typing.overload
    def isValid(self, int: int) -> bool:
        """
            Checks whether the token is still valid (hasn't expired) for the requested amount of seconds. As it's impossible to
            create tokens in the future, we don't check the authentication time here.
        
            Parameters:
                timeFrame (int): requested amount of seconds when token should be still valid
        
            Returns:
                true if the token will be still valid for the requested amount of seconds
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parseAndValidate(byteBuffer: java.nio.ByteBuffer) -> 'RbaToken': ...
    @typing.overload
    @staticmethod
    def parseAndValidate(byteBuffer: java.nio.ByteBuffer, rbacConfiguration: 'RbacConfiguration') -> 'RbaToken': ...
    @staticmethod
    def parseNoValidate(byteBuffer: java.nio.ByteBuffer) -> 'RbaToken': ...
    def toHttpHeader(self) -> java.util.Map.Entry[str, str]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def verify(self, collection: typing.Union[java.util.Collection[java.security.PublicKey], typing.Sequence[java.security.PublicKey]]) -> bool: ...

class RbaTokenExpirationListener:
    """
    public class RbaTokenExpirationListener extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self, rbaToken: RbaToken): ...
    def addExpirationListener(self, tokenExpirationListener: 'TokenExpirationListener') -> None:
        """
            This method enables client applications to register listeners for the token expiration.
        
            Parameters:
                listener (:class:`~cern.rbac.common.TokenExpirationListener`): the object that implements the :class:`~cern.rbac.common.TokenExpirationListener` interface
        
        
        """
        ...
    def removeExpirationListener(self, tokenExpirationListener: 'TokenExpirationListener') -> None:
        """
            This method allows client applications to remove token expiration listeners.
        
            Parameters:
                listener (:class:`~cern.rbac.common.TokenExpirationListener`): the object that implements the :class:`~cern.rbac.common.TokenExpirationListener` interface
        
        
        """
        ...
    def removeExpirationListeners(self) -> None:
        """
            This method removes all the registered token expiration listeners.
        
        """
        ...

class RbacConfiguration:
    """
    public final class RbacConfiguration extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        The runtime configuration for RBAC client. You can either create a new one using
        :meth:`~cern.rbac.common.RbacConfiguration.create` or use the default one via
        :meth:`~cern.rbac.common.RbacConfiguration.getCurrent` which is initialized from the system properties.
    
        Also see:
            :meth:`~cern.rbac.common.RbacConfiguration.getCurrent`, :meth:`~cern.rbac.common.RbacConfiguration.create`
    """
    SYSTEM_PROPERTY_RBAC_ENV: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSTEM_PROPERTY_RBAC_ENV
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    RBAC_ENVIRONMENT_DEFAULT: typing.ClassVar['RbacConfiguration.Environment'] = ...
    """
    public static final :class:`~cern.rbac.common.RbacConfiguration.Environment` RBAC_ENVIRONMENT_DEFAULT
    
    
    """
    @staticmethod
    def create(configuration: cern.cmw.util.config.Configuration) -> 'RbacConfiguration':
        """
            Creates a new rbac configuration from the supplied configuration properties. This newly-created configuration becomes
            the current configuration.
        
        """
        ...
    @staticmethod
    def getCurrent() -> 'RbacConfiguration':
        """
            The current configuration is the default one, until you :meth:`~cern.rbac.common.RbacConfiguration.create` one.
        
        """
        ...
    def getEnvironment(self) -> 'RbacConfiguration.Environment':
        """
            Returns the RBAC environment assigned to this configuration instance.
        
            System property name: rbac.env
        
        
            Environment variable: RBAC_ENV
        
        
            Default value: PRO
        
            Returns:
                the RBAC environment assigned to this configuration instance
        
        
        """
        ...
    def getOAuth2Service(self) -> 'RbacConfiguration.OAuth2Service':
        """
            Returns the RBAC service used for the OAuth 2.0 token exchange protocol.
        
            Returns:
                the RBAC service used for the OAuth 2.0 token exchange protocol
        
        
        """
        ...
    class Environment(java.lang.Enum['RbacConfiguration.Environment']):
        PRO: typing.ClassVar['RbacConfiguration.Environment'] = ...
        TEST: typing.ClassVar['RbacConfiguration.Environment'] = ...
        ITQA: typing.ClassVar['RbacConfiguration.Environment'] = ...
        INT: typing.ClassVar['RbacConfiguration.Environment'] = ...
        LOCAL: typing.ClassVar['RbacConfiguration.Environment'] = ...
        _selectValue_0__T = typing.TypeVar('_selectValue_0__T')  # <T>
        _selectValue_1__T = typing.TypeVar('_selectValue_1__T')  # <T>
        @typing.overload
        def selectValue(self, t: _selectValue_0__T, t2: _selectValue_0__T, t3: _selectValue_0__T) -> _selectValue_0__T: ...
        @typing.overload
        def selectValue(self, t: _selectValue_1__T, t2: _selectValue_1__T, t3: _selectValue_1__T, t4: _selectValue_1__T) -> _selectValue_1__T: ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'RbacConfiguration.Environment': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['RbacConfiguration.Environment']: ...
    class OAuth2Service(java.lang.Enum['RbacConfiguration.OAuth2Service']):
        PRO: typing.ClassVar['RbacConfiguration.OAuth2Service'] = ...
        TESTBED: typing.ClassVar['RbacConfiguration.OAuth2Service'] = ...
        ITQA: typing.ClassVar['RbacConfiguration.OAuth2Service'] = ...
        INT: typing.ClassVar['RbacConfiguration.OAuth2Service'] = ...
        def getName(self) -> str: ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'RbacConfiguration.OAuth2Service': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['RbacConfiguration.OAuth2Service']: ...

class Role:
    """
    public interface Role
    
        This interface represents the RBAC role. Roles are used to group certain access rights to the resources e.g. device and
        their properties. Any user can have one or more roles assigned to his account which allow him/her to perform certain
        actions on the resources which are protected by these roles.
    """
    def getLifetime(self) -> int:
        """
            Returns lifetime (in minutes) of the role i.e. period of time for this role when it is valid and available.
        
            Returns:
                lifetime (in minutes) of the role
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns name of the role.
        
            Returns:
                name of the role
        
        
        """
        ...
    def isCritical(self) -> bool:
        """
            Returns :code:`true` when this role is critical, otherwise :code:`false` is returned.
        
            Returns:
                :code:`true` when this role is critical, otherwise :code:`false` is returned
        
        
        """
        ...
    def isLifetimeDefined(self) -> bool:
        """
            Returns :code:`true` when this role has a defined lifetime period, otherwise :code:`false` is returned.
        
            Returns:
                :code:`true` when this role has a defined lifetime period, otherwise :code:`false` is returned
        
        
        """
        ...

class RoleUtils:
    @staticmethod
    def createRole(string: str) -> Role: ...
    @typing.overload
    @staticmethod
    def createRoles(stringArray: typing.List[str]) -> typing.List[Role]: ...
    @typing.overload
    @staticmethod
    def createRoles(stringArray: typing.List[str], intArray: typing.List[int]) -> typing.List[Role]: ...
    @typing.overload
    @staticmethod
    def createRoles(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.List[Role]: ...
    @typing.overload
    @staticmethod
    def getRoleLifetimes(roleArray: typing.List[Role]) -> typing.List[int]: ...
    @typing.overload
    @staticmethod
    def getRoleLifetimes(collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]]) -> java.util.Map[str, int]: ...
    @typing.overload
    @staticmethod
    def getRoleNames(roleArray: typing.List[Role]) -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def getRoleNames(collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]]) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def getSignatureRole(roleArray: typing.List[Role]) -> Role: ...
    @typing.overload
    @staticmethod
    def getSignatureRole(collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]]) -> Role: ...
    @typing.overload
    @staticmethod
    def hasAllRequestedRoles(rbaToken: RbaToken, roleArray: typing.List[Role]) -> bool: ...
    @typing.overload
    @staticmethod
    def hasAllRequestedRoles(rbaToken: RbaToken, stringArray: typing.List[str]) -> bool: ...
    @typing.overload
    @staticmethod
    def hasAllRequestedRoles(rbaToken: RbaToken, collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]]) -> bool: ...
    @typing.overload
    @staticmethod
    def hasAllRequestedRoles(collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]], roleArray: typing.List[Role]) -> bool: ...
    @typing.overload
    @staticmethod
    def hasAllRequestedRoles(collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]], collection2: typing.Union[java.util.Collection[Role], typing.Sequence[Role]]) -> bool: ...
    @typing.overload
    @staticmethod
    def hasAnyRequestedRole(rbaToken: RbaToken, roleArray: typing.List[Role]) -> bool: ...
    @typing.overload
    @staticmethod
    def hasAnyRequestedRole(rbaToken: RbaToken, stringArray: typing.List[str]) -> bool: ...
    @typing.overload
    @staticmethod
    def hasAnyRequestedRole(rbaToken: RbaToken, collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]]) -> bool: ...
    @typing.overload
    @staticmethod
    def hasAnyRequestedRole(collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]], roleArray: typing.List[Role]) -> bool: ...
    @typing.overload
    @staticmethod
    def hasAnyRequestedRole(collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]], collection2: typing.Union[java.util.Collection[Role], typing.Sequence[Role]]) -> bool: ...
    @typing.overload
    @staticmethod
    def verifyCriticalRoles(roleArray: typing.List[Role]) -> None: ...
    @typing.overload
    @staticmethod
    def verifyCriticalRoles(collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]]) -> None: ...
    @typing.overload
    @staticmethod
    def verifySignatureRoles(roleArray: typing.List[Role]) -> None: ...
    @typing.overload
    @staticmethod
    def verifySignatureRoles(collection: typing.Union[java.util.Collection[Role], typing.Sequence[Role]]) -> None: ...

class TokenExpirationListener:
    """
    public interface TokenExpirationListener
    
        The listener is used by RbaToken to notify an application when the token has expired.
    """
    def tokenExpired(self) -> None: ...

class TokenFormatException(java.io.IOException):
    """
    public class TokenFormatException extends `IOException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/IOException.html?is-external=true>`
    
        This exception occurs during de-serialization of RbaToken, when an incorrect binary format is used.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class TokenType(java.lang.Enum['TokenType']):
    """
    public enum TokenType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.TokenType`>
    
        Enum which defines all possible types of tokens.
    """
    APPLICATION: typing.ClassVar['TokenType'] = ...
    MASTER: typing.ClassVar['TokenType'] = ...
    LOCAL_MASTER: typing.ClassVar['TokenType'] = ...
    @staticmethod
    def fromIndex(int: int) -> 'TokenType': ...
    @staticmethod
    def fromString(string: str) -> 'TokenType':
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
    def isApplication(self) -> bool: ...
    def isMaster(self) -> bool: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TokenType':
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
    def values() -> typing.List['TokenType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (TokenType c : TokenType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class UserPrincipal(java.security.Principal):
    """
    public interface UserPrincipal extends `Principal <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/security/Principal.html?is-external=true>`
    
        Descriptor of an authenticated User with it's roles.
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getAccountType(self) -> 'UserPrincipal.AccountType':
        """
            The user type of account.
        
            Returns:
                The user type of account.
        
        
        """
        ...
    def getEmail(self) -> str:
        """
            The user e-mail address.
        
            Returns:
                The user e-mail address.
        
        
        """
        ...
    def getFullName(self) -> str:
        """
            The user full name.
        
            Returns:
                The user full name.
        
        
        """
        ...
    def getRoles(self) -> typing.List[Role]:
        """
            Gets the list of roles assigned to the user.
        
            Returns:
                non-null array of user roles, can be empty if no roles are assigned
        
        
        """
        ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    class AccountType(java.lang.Enum['UserPrincipal.AccountType']):
        PRIMARY: typing.ClassVar['UserPrincipal.AccountType'] = ...
        SECONDARY: typing.ClassVar['UserPrincipal.AccountType'] = ...
        SERVICE: typing.ClassVar['UserPrincipal.AccountType'] = ...
        UNKNOWN: typing.ClassVar['UserPrincipal.AccountType'] = ...
        @staticmethod
        def fromString(string: str) -> 'UserPrincipal.AccountType': ...
        def getName(self) -> str: ...
        def toString(self) -> str: ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'UserPrincipal.AccountType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['UserPrincipal.AccountType']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common")``.

    AppPrincipal: typing.Type[AppPrincipal]
    AuthenticationType: typing.Type[AuthenticationType]
    ExtraFields: typing.Type[ExtraFields]
    LocationPrincipal: typing.Type[LocationPrincipal]
    MasterToken: typing.Type[MasterToken]
    RbaToken: typing.Type[RbaToken]
    RbaTokenExpirationListener: typing.Type[RbaTokenExpirationListener]
    RbacConfiguration: typing.Type[RbacConfiguration]
    Role: typing.Type[Role]
    RoleUtils: typing.Type[RoleUtils]
    TokenExpirationListener: typing.Type[TokenExpirationListener]
    TokenFormatException: typing.Type[TokenFormatException]
    TokenType: typing.Type[TokenType]
    UserPrincipal: typing.Type[UserPrincipal]
    authentication: cern.rbac.common.authentication.__module_protocol__
    authorization: cern.rbac.common.authorization.__module_protocol__
    impl: cern.rbac.common.impl.__module_protocol__
    test: cern.rbac.common.test.__module_protocol__
