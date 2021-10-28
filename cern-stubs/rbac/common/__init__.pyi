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
    Java class 'cern.rbac.common.AppPrincipal'
    
        Interfaces:
            java.security.Principal
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getTimeout(self) -> int: ...
    def hashCode(self) -> int: ...
    def isCritical(self) -> bool: ...
    def toString(self) -> str: ...

class AuthenticationType(java.lang.Enum['AuthenticationType']):
    """
    Java class 'cern.rbac.common.AuthenticationType'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        NICE (cern.rbac.common.AuthenticationType): final static enum constant
        LOCATION (cern.rbac.common.AuthenticationType): final static enum constant
        CERTIFICATE (cern.rbac.common.AuthenticationType): final static enum constant
        SSO_PICKER (cern.rbac.common.AuthenticationType): final static enum constant
        RENEWAL (cern.rbac.common.AuthenticationType): final static enum constant
    
    """
    NICE: typing.ClassVar['AuthenticationType'] = ...
    LOCATION: typing.ClassVar['AuthenticationType'] = ...
    CERTIFICATE: typing.ClassVar['AuthenticationType'] = ...
    SSO_PICKER: typing.ClassVar['AuthenticationType'] = ...
    RENEWAL: typing.ClassVar['AuthenticationType'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AuthenticationType': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['AuthenticationType']: ...

class ExtraFields:
    """
    Java class 'cern.rbac.common.ExtraFields'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ExtraFields(cern.rbac.common.TokenType, cern.rbac.common.Role[])
    
    """
    def __init__(self, tokenType: 'TokenType', roleArray: typing.List['Role']): ...
    def getRolesHint(self) -> typing.List['Role']: ...
    def getTokenType(self) -> 'TokenType': ...
    def toString(self) -> str: ...

class LocationPrincipal(java.security.Principal):
    """
    Java class 'cern.rbac.common.LocationPrincipal'
    
        Interfaces:
            java.security.Principal
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getAddress(self) -> java.net.InetAddress: ...
    def getDefaultUser(self) -> str: ...
    def hashCode(self) -> int: ...
    def isAuthRequired(self) -> bool: ...
    def toString(self) -> str: ...

class MasterToken:
    """
    Java class 'cern.rbac.common.MasterToken'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MasterToken(cern.rbac.common.RbaToken)
    
    """
    def __init__(self, rbaToken: 'RbaToken'): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAuthTime(self) -> java.time.Instant: ...
    def getEncoded(self) -> typing.List[int]: ...
    def getEndTime(self) -> java.time.Instant: ...
    def getExtra(self) -> ExtraFields: ...
    def getLocation(self) -> LocationPrincipal: ...
    def getUser(self) -> 'UserPrincipal': ...
    def hashCode(self) -> int: ...
    @typing.overload
    def isValid(self) -> bool: ...
    @typing.overload
    def isValid(self, duration: java.time.Duration) -> bool: ...
    def toString(self) -> str: ...

class RbaToken(java.io.Serializable):
    """
    Java class 'cern.rbac.common.RbaToken'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * RbaToken(byte[], int, int)
        * RbaToken(byte[], cern.rbac.common.impl.serialization.decode.TokenDecoder)
        * RbaToken(byte[])
    
      Raises:
        cern.rbac.common.TokenFormatException: from java
    
      Attributes:
        EMPTY_TOKEN (cern.rbac.common.RbaToken): final static field
    
    """
    EMPTY_TOKEN: typing.ClassVar['RbaToken'] = ...
    @typing.overload
    def __init__(self, byteArray: typing.List[int]): ...
    @typing.overload
    def __init__(self, byteArray: typing.List[int], tokenDecoder: cern.rbac.common.impl.serialization.decode.TokenDecoder): ...
    @typing.overload
    def __init__(self, byteArray: typing.List[int], int: int, int2: int): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getApplication(self) -> AppPrincipal: ...
    def getAuthTime(self) -> java.util.Date: ...
    def getEncoded(self) -> typing.List[int]: ...
    def getEndTime(self) -> java.util.Date: ...
    def getExtra(self) -> ExtraFields: ...
    def getLocation(self) -> LocationPrincipal: ...
    def getSerialId(self) -> int: ...
    def getType(self) -> 'TokenType': ...
    def getUser(self) -> 'UserPrincipal': ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    @typing.overload
    def isValid(self) -> bool: ...
    @typing.overload
    def isValid(self, int: int) -> bool: ...
    @typing.overload
    @staticmethod
    def parseAndValidate(byteBuffer: java.nio.ByteBuffer) -> 'RbaToken': ...
    @typing.overload
    @staticmethod
    def parseAndValidate(byteBuffer: java.nio.ByteBuffer, rbacConfiguration: 'RbacConfiguration') -> 'RbaToken': ...
    @staticmethod
    def parseNoValidate(byteBuffer: java.nio.ByteBuffer) -> 'RbaToken': ...
    def toHttpHeader(self) -> java.util.Map.Entry[str, str]: ...
    def toString(self) -> str: ...
    def verify(self, collection: typing.Union[java.util.Collection[java.security.PublicKey], typing.Sequence[java.security.PublicKey]]) -> bool: ...

class RbaTokenExpirationListener:
    """
    Java class 'cern.rbac.common.RbaTokenExpirationListener'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RbaTokenExpirationListener(cern.rbac.common.RbaToken)
    
    """
    def __init__(self, rbaToken: RbaToken): ...
    def addExpirationListener(self, tokenExpirationListener: 'TokenExpirationListener') -> None: ...
    def removeExpirationListener(self, tokenExpirationListener: 'TokenExpirationListener') -> None: ...
    def removeExpirationListeners(self) -> None: ...

class RbacConfiguration:
    """
    Java class 'cern.rbac.common.RbacConfiguration'
    
        Extends:
            java.lang.Object
    
      Attributes:
        SYSTEM_PROPERTY_RBAC_ENV (java.lang.String): final static field
        RBAC_ENVIRONMENT_DEFAULT (cern.rbac.common.RbacConfiguration$Environment): final static field
    
    """
    SYSTEM_PROPERTY_RBAC_ENV: typing.ClassVar[str] = ...
    RBAC_ENVIRONMENT_DEFAULT: typing.ClassVar['RbacConfiguration.Environment'] = ...
    @staticmethod
    def create(configuration: cern.cmw.util.config.Configuration) -> 'RbacConfiguration': ...
    @staticmethod
    def getCurrent() -> 'RbacConfiguration': ...
    def getEnvironment(self) -> 'RbacConfiguration.Environment': ...
    def getOAuth2Service(self) -> 'RbacConfiguration.OAuth2Service': ...
    class Environment(java.lang.Enum['RbacConfiguration.Environment']):
        """
        Java class 'cern.rbac.common.RbacConfiguration$Environment'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            PRO (cern.rbac.common.RbacConfiguration$Environment): final static enum constant
            TEST (cern.rbac.common.RbacConfiguration$Environment): final static enum constant
            INT (cern.rbac.common.RbacConfiguration$Environment): final static enum constant
            LOCAL (cern.rbac.common.RbacConfiguration$Environment): final static enum constant
        
        """
        PRO: typing.ClassVar['RbacConfiguration.Environment'] = ...
        TEST: typing.ClassVar['RbacConfiguration.Environment'] = ...
        INT: typing.ClassVar['RbacConfiguration.Environment'] = ...
        LOCAL: typing.ClassVar['RbacConfiguration.Environment'] = ...
        _selectValue__T = typing.TypeVar('_selectValue__T')  # <T>
        def selectValue(self, t: _selectValue__T, t2: _selectValue__T, t3: _selectValue__T) -> _selectValue__T: ...
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
        """
        Java class 'cern.rbac.common.RbacConfiguration$OAuth2Service'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            PRO (cern.rbac.common.RbacConfiguration$OAuth2Service): final static enum constant
            TESTBED (cern.rbac.common.RbacConfiguration$OAuth2Service): final static enum constant
            INT (cern.rbac.common.RbacConfiguration$OAuth2Service): final static enum constant
        
        """
        PRO: typing.ClassVar['RbacConfiguration.OAuth2Service'] = ...
        TESTBED: typing.ClassVar['RbacConfiguration.OAuth2Service'] = ...
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
    Java class 'cern.rbac.common.Role'
    
    """
    def getLifetime(self) -> int: ...
    def getName(self) -> str: ...
    def isCritical(self) -> bool: ...
    def isLifetimeDefined(self) -> bool: ...

class RoleUtils:
    """
    Java class 'cern.rbac.common.RoleUtils'
    
        Extends:
            java.lang.Object
    
    """
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
    Java class 'cern.rbac.common.TokenExpirationListener'
    
    """
    def tokenExpired(self) -> None: ...

class TokenFormatException(java.io.IOException):
    """
    Java class 'cern.rbac.common.TokenFormatException'
    
        Extends:
            java.io.IOException
    
      Constructors:
        * TokenFormatException(java.lang.String, java.lang.Throwable)
        * TokenFormatException(java.lang.Throwable)
        * TokenFormatException(java.lang.String)
        * TokenFormatException()
    
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
    Java class 'cern.rbac.common.TokenType'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        APPLICATION (cern.rbac.common.TokenType): final static enum constant
        MASTER (cern.rbac.common.TokenType): final static enum constant
        LOCAL_MASTER (cern.rbac.common.TokenType): final static enum constant
    
    """
    APPLICATION: typing.ClassVar['TokenType'] = ...
    MASTER: typing.ClassVar['TokenType'] = ...
    LOCAL_MASTER: typing.ClassVar['TokenType'] = ...
    @staticmethod
    def fromIndex(int: int) -> 'TokenType': ...
    @staticmethod
    def fromString(string: str) -> 'TokenType': ...
    def isApplication(self) -> bool: ...
    def isMaster(self) -> bool: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TokenType': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['TokenType']: ...

class UserPrincipal(java.security.Principal):
    """
    Java class 'cern.rbac.common.UserPrincipal'
    
        Interfaces:
            java.security.Principal
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getAccountType(self) -> 'UserPrincipal.AccountType': ...
    def getEmail(self) -> str: ...
    def getFullName(self) -> str: ...
    def getRoles(self) -> typing.List[Role]: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    class AccountType(java.lang.Enum['UserPrincipal.AccountType']):
        """
        Java class 'cern.rbac.common.UserPrincipal$AccountType'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            PRIMARY (cern.rbac.common.UserPrincipal$AccountType): final static enum constant
            SECONDARY (cern.rbac.common.UserPrincipal$AccountType): final static enum constant
            SERVICE (cern.rbac.common.UserPrincipal$AccountType): final static enum constant
            UNKNOWN (cern.rbac.common.UserPrincipal$AccountType): final static enum constant
        
        """
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
