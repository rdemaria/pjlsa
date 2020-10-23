from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import cern.cmw.util.config
import cern.rbac.common.impl.serialization.decode
import java.io
import java.lang
import java.net
import java.nio
import java.security
import java.util


class AppPrincipal(java.security.Principal):
    def equals(self, object: _py_Any) -> bool: ...
    def getTimeout(self) -> int: ...
    def hashCode(self) -> int: ...
    def isCritical(self) -> bool: ...
    def toString(self) -> str: ...

class AuthenticationType(java.lang.Enum['AuthenticationType']):
    NICE: _py_ClassVar['AuthenticationType'] = ...
    LOCATION: _py_ClassVar['AuthenticationType'] = ...
    CERTIFICATE: _py_ClassVar['AuthenticationType'] = ...
    SSO_PICKER: _py_ClassVar['AuthenticationType'] = ...
    RENEWAL: _py_ClassVar['AuthenticationType'] = ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'AuthenticationType': ...
    _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @classmethod
    def values(cls) -> _py_List['AuthenticationType']: ...

class ExtraFields:
    def __init__(self, tokenType: 'TokenType', roleArray: _py_List['Role'], date: java.util.Date): ...
    def getRenewTill(self) -> java.util.Date: ...
    def getRolesHint(self) -> _py_List['Role']: ...
    def getTokenType(self) -> 'TokenType': ...
    def toString(self) -> str: ...

class LocationPrincipal(java.security.Principal):
    def equals(self, object: _py_Any) -> bool: ...
    def getAddress(self) -> java.net.InetAddress: ...
    def getDefaultUser(self) -> str: ...
    def hashCode(self) -> int: ...
    def isAuthRequired(self) -> bool: ...
    def toString(self) -> str: ...

class RbaToken(java.io.Serializable):
    EMPTY_TOKEN: _py_ClassVar['RbaToken'] = ...
    @overload
    def __init__(self, byteArray: _py_List[int]): ...
    @overload
    def __init__(self, byteArray: _py_List[int], tokenDecoder: cern.rbac.common.impl.serialization.decode.TokenDecoder): ...
    @overload
    def __init__(self, byteArray: _py_List[int], int: int, int2: int): ...
    def equals(self, object: _py_Any) -> bool: ...
    def getApplication(self) -> AppPrincipal: ...
    def getAuthTime(self) -> java.util.Date: ...
    def getEncoded(self) -> _py_List[int]: ...
    def getEndTime(self) -> java.util.Date: ...
    def getExtra(self) -> ExtraFields: ...
    def getLocation(self) -> LocationPrincipal: ...
    def getRenewTill(self) -> java.util.Date: ...
    def getSerialId(self) -> int: ...
    def getType(self) -> 'TokenType': ...
    def getUser(self) -> 'UserPrincipal': ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    @overload
    def isValid(self) -> bool: ...
    @overload
    def isValid(self, int: int) -> bool: ...
    @classmethod
    def parseAndValidate(cls, byteBuffer: java.nio.ByteBuffer, rbacConfiguration: 'RbacConfiguration') -> 'RbaToken': ...
    @classmethod
    def parseNoValidate(cls, byteBuffer: java.nio.ByteBuffer) -> 'RbaToken': ...
    def toString(self) -> str: ...
    def verify(self, collection: java.util.Collection[java.security.PublicKey]) -> bool: ...

class RbaTokenExpirationListener:
    def __init__(self, rbaToken: RbaToken): ...
    def addExpirationListener(self, tokenExpirationListener: 'TokenExpirationListener') -> None: ...
    def removeExpirationListener(self, tokenExpirationListener: 'TokenExpirationListener') -> None: ...
    def removeExpirationListeners(self) -> None: ...

class RbacConfiguration:
    SYSTEM_PROPERTY_RBAC_ENV: _py_ClassVar[str] = ...
    RBAC_ENVIRONMENT_DEFAULT: _py_ClassVar['RbacConfiguration.Environment'] = ...
    @classmethod
    def create(cls, configuration: cern.cmw.util.config.Configuration) -> 'RbacConfiguration': ...
    @classmethod
    def getCurrent(cls) -> 'RbacConfiguration': ...
    def getEnvironment(self) -> 'RbacConfiguration.Environment': ...
    class Environment(java.lang.Enum['RbacConfiguration.Environment']):
        PRO: _py_ClassVar['RbacConfiguration.Environment'] = ...
        DEV: _py_ClassVar['RbacConfiguration.Environment'] = ...
        INT: _py_ClassVar['RbacConfiguration.Environment'] = ...
        TEST: _py_ClassVar['RbacConfiguration.Environment'] = ...
        LOCAL: _py_ClassVar['RbacConfiguration.Environment'] = ...
        _selectValue__T = _py_TypeVar('_selectValue__T')  # <T>
        def selectValue(self, t: _selectValue__T, t2: _selectValue__T, t3: _selectValue__T) -> _selectValue__T: ...
        @classmethod
        @overload
        def valueOf(cls, string: str) -> 'RbacConfiguration.Environment': ...
        _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @overload
        def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @classmethod
        def values(cls) -> _py_List['RbacConfiguration.Environment']: ...

class Role:
    def getLifetime(self) -> int: ...
    def getName(self) -> str: ...
    def isCritical(self) -> bool: ...
    def isLifetimeDefined(self) -> bool: ...

class RoleUtils:
    @classmethod
    def createRole(cls, string: str) -> Role: ...
    @classmethod
    @overload
    def createRoles(cls, stringArray: _py_List[str]) -> _py_List[Role]: ...
    @classmethod
    @overload
    def createRoles(cls, stringArray: _py_List[str], intArray: _py_List[int]) -> _py_List[Role]: ...
    @classmethod
    @overload
    def createRoles(cls, collection: java.util.Collection[str]) -> java.util.List[Role]: ...
    @classmethod
    @overload
    def getRoleLifetimes(cls, roleArray: _py_List[Role]) -> _py_List[int]: ...
    @classmethod
    @overload
    def getRoleLifetimes(cls, collection: java.util.Collection[Role]) -> java.util.Map[str, int]: ...
    @classmethod
    @overload
    def getRoleNames(cls, roleArray: _py_List[Role]) -> _py_List[str]: ...
    @classmethod
    @overload
    def getRoleNames(cls, collection: java.util.Collection[Role]) -> java.util.List[str]: ...
    @classmethod
    @overload
    def getSignatureRole(cls, roleArray: _py_List[Role]) -> Role: ...
    @classmethod
    @overload
    def getSignatureRole(cls, collection: java.util.Collection[Role]) -> Role: ...
    @classmethod
    @overload
    def hasAllRequestedRoles(cls, rbaToken: RbaToken, roleArray: _py_List[Role]) -> bool: ...
    @classmethod
    @overload
    def hasAllRequestedRoles(cls, rbaToken: RbaToken, stringArray: _py_List[str]) -> bool: ...
    @classmethod
    @overload
    def hasAllRequestedRoles(cls, rbaToken: RbaToken, collection: java.util.Collection[Role]) -> bool: ...
    @classmethod
    @overload
    def hasAllRequestedRoles(cls, collection: java.util.Collection[Role], roleArray: _py_List[Role]) -> bool: ...
    @classmethod
    @overload
    def hasAllRequestedRoles(cls, collection: java.util.Collection[Role], collection2: java.util.Collection[Role]) -> bool: ...
    @classmethod
    @overload
    def hasAnyRequestedRole(cls, rbaToken: RbaToken, roleArray: _py_List[Role]) -> bool: ...
    @classmethod
    @overload
    def hasAnyRequestedRole(cls, rbaToken: RbaToken, stringArray: _py_List[str]) -> bool: ...
    @classmethod
    @overload
    def hasAnyRequestedRole(cls, rbaToken: RbaToken, collection: java.util.Collection[Role]) -> bool: ...
    @classmethod
    @overload
    def hasAnyRequestedRole(cls, collection: java.util.Collection[Role], roleArray: _py_List[Role]) -> bool: ...
    @classmethod
    @overload
    def hasAnyRequestedRole(cls, collection: java.util.Collection[Role], collection2: java.util.Collection[Role]) -> bool: ...
    @classmethod
    @overload
    def verifyCriticalRoles(cls, roleArray: _py_List[Role]) -> None: ...
    @classmethod
    @overload
    def verifyCriticalRoles(cls, collection: java.util.Collection[Role]) -> None: ...
    @classmethod
    @overload
    def verifySignatureRoles(cls, roleArray: _py_List[Role]) -> None: ...
    @classmethod
    @overload
    def verifySignatureRoles(cls, collection: java.util.Collection[Role]) -> None: ...

class TokenExpirationListener:
    def tokenExpired(self) -> None: ...

class TokenFormatException(java.io.IOException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @overload
    def __init__(self, throwable: java.lang.Throwable): ...

class TokenType(java.lang.Enum['TokenType']):
    APPLICATION: _py_ClassVar['TokenType'] = ...
    MASTER: _py_ClassVar['TokenType'] = ...
    LOCAL_MASTER: _py_ClassVar['TokenType'] = ...
    @classmethod
    def fromIndex(cls, int: int) -> 'TokenType': ...
    def isApplication(self) -> bool: ...
    def isMaster(self) -> bool: ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'TokenType': ...
    _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @classmethod
    def values(cls) -> _py_List['TokenType']: ...

class UserPrincipal(java.security.Principal):
    def equals(self, object: _py_Any) -> bool: ...
    def getAccountType(self) -> 'UserPrincipal.AccountType': ...
    def getEmail(self) -> str: ...
    def getFullName(self) -> str: ...
    def getRoles(self) -> _py_List[Role]: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    class AccountType(java.lang.Enum['UserPrincipal.AccountType']):
        PRIMARY: _py_ClassVar['UserPrincipal.AccountType'] = ...
        SECONDARY: _py_ClassVar['UserPrincipal.AccountType'] = ...
        SERVICE: _py_ClassVar['UserPrincipal.AccountType'] = ...
        UNKNOWN: _py_ClassVar['UserPrincipal.AccountType'] = ...
        @classmethod
        def fromString(cls, string: str) -> 'UserPrincipal.AccountType': ...
        def getName(self) -> str: ...
        def toString(self) -> str: ...
        @classmethod
        @overload
        def valueOf(cls, string: str) -> 'UserPrincipal.AccountType': ...
        _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @overload
        def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @classmethod
        def values(cls) -> _py_List['UserPrincipal.AccountType']: ...