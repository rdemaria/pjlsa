import cern.rbac.common
import cern.rbac.common.authorization
import cern.rbac.common.impl.decode
import cern.rbac.common.impl.exec_
import cern.rbac.common.impl.keys
import cern.rbac.common.impl.request
import cern.rbac.common.impl.response
import cern.rbac.common.impl.serialization
import java.lang
import java.net
import java.nio.charset
import java.security
import typing



class AppPrincipalImpl(cern.rbac.common.AppPrincipal, java.lang.Cloneable):
    """
    Java class 'cern.rbac.common.impl.AppPrincipalImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.rbac.common.AppPrincipal, java.lang.Cloneable
    
      Constructors:
        * AppPrincipalImpl(java.lang.String, boolean, java.lang.Integer)
    
    """
    def __init__(self, string: str, boolean: bool, integer: int): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str: ...
    def getTimeout(self) -> int: ...
    def hashCode(self) -> int: ...
    def isCritical(self) -> bool: ...
    def toString(self) -> str: ...

class LocationPrincipalImpl(cern.rbac.common.LocationPrincipal, java.lang.Cloneable):
    """
    Java class 'cern.rbac.common.impl.LocationPrincipalImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.rbac.common.LocationPrincipal, java.lang.Cloneable
    
      Constructors:
        * LocationPrincipalImpl(java.lang.String, java.lang.String, boolean)
        * LocationPrincipalImpl(java.lang.String, java.net.InetAddress, boolean, java.lang.String)
        * LocationPrincipalImpl(java.lang.String, java.net.InetAddress, boolean)
    
      Raises:
        java.net.UnknownHostException: from java
    
    """
    @typing.overload
    def __init__(self, string: str, string2: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, inetAddress: java.net.InetAddress, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, inetAddress: java.net.InetAddress, boolean: bool, string2: str): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAddress(self) -> java.net.InetAddress: ...
    def getDefaultUser(self) -> str: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def isAuthRequired(self) -> bool: ...
    def toString(self) -> str: ...

class RbaConstants:
    """
    Java class 'cern.rbac.common.impl.RbaConstants'
    
      Attributes:
        VERSION (java.lang.String): final static field
        DEFAULT_ENCODING (java.nio.charset.Charset): final static field
        SIGNATURE_ALGORITHM (java.lang.String): final static field
        KEY_ALGORITHM (java.lang.String): final static field
        KEY_SIZE (int): final static field
        UNDEFINED_TOKEN_LIFETIME (int): final static field
        DEFAULT_TOKEN_LIFETIME (int): final static field
        DEFAULT_READ_TIMEOUT (int): final static field
        CRITICAL_ROLE_PREFIX (java.lang.String): final static field
        AUTHORIZATION_SCHEME (java.lang.String): final static field
        AUTHORIZATION_HEADER (java.lang.String): final static field
    
    """
    VERSION: typing.ClassVar[str] = ...
    DEFAULT_ENCODING: typing.ClassVar[java.nio.charset.Charset] = ...
    SIGNATURE_ALGORITHM: typing.ClassVar[str] = ...
    KEY_ALGORITHM: typing.ClassVar[str] = ...
    KEY_SIZE: typing.ClassVar[int] = ...
    UNDEFINED_TOKEN_LIFETIME: typing.ClassVar[int] = ...
    DEFAULT_TOKEN_LIFETIME: typing.ClassVar[int] = ...
    DEFAULT_READ_TIMEOUT: typing.ClassVar[int] = ...
    CRITICAL_ROLE_PREFIX: typing.ClassVar[str] = ...
    AUTHORIZATION_SCHEME: typing.ClassVar[str] = ...
    AUTHORIZATION_HEADER: typing.ClassVar[str] = ...

class RoleImpl(cern.rbac.common.Role, java.lang.Cloneable, java.lang.Comparable['RoleImpl']):
    """
    Java class 'cern.rbac.common.impl.RoleImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.rbac.common.Role, java.lang.Cloneable,
            java.lang.Comparable
    
      Constructors:
        * RoleImpl(java.lang.String)
        * RoleImpl(java.lang.String, int)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    def clone(self) -> typing.Any: ...
    def compareTo(self, roleImpl: 'RoleImpl') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getLifetime(self) -> int: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def isCritical(self) -> bool: ...
    def isLifetimeDefined(self) -> bool: ...
    def toString(self) -> str: ...

class ServiceLocator:
    """
    Java class 'cern.rbac.common.impl.ServiceLocator'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def getExecutionService() -> cern.rbac.common.impl.exec_.ExecutionService: ...

class UserPrincipalImpl(cern.rbac.common.UserPrincipal, java.lang.Cloneable):
    """
    Java class 'cern.rbac.common.impl.UserPrincipalImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.rbac.common.UserPrincipal, java.lang.Cloneable
    
      Constructors:
        * UserPrincipalImpl(java.lang.String, java.lang.String, java.lang.String, cern.rbac.common.Role[], cern.rbac.common.UserPrincipal.AccountType)
    
    """
    def __init__(self, string: str, string2: str, string3: str, roleArray: typing.List[cern.rbac.common.Role], accountType: cern.rbac.common.UserPrincipal.AccountType): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAccountType(self) -> cern.rbac.common.UserPrincipal.AccountType: ...
    def getEmail(self) -> str: ...
    def getFullName(self) -> str: ...
    def getName(self) -> str: ...
    def getRoles(self) -> typing.List[cern.rbac.common.Role]: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class McsRoleImpl(RoleImpl, cern.rbac.common.authorization.McsRole):
    """
    Java class 'cern.rbac.common.impl.McsRoleImpl'
    
        Extends:
            cern.rbac.common.impl.RoleImpl
    
        Interfaces:
            cern.rbac.common.authorization.McsRole
    
      Constructors:
        * McsRoleImpl(java.lang.String, java.security.PublicKey)
    
    """
    def __init__(self, string: str, publicKey: java.security.PublicKey): ...
    def getPublicKey(self) -> java.security.PublicKey: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl")``.

    AppPrincipalImpl: typing.Type[AppPrincipalImpl]
    LocationPrincipalImpl: typing.Type[LocationPrincipalImpl]
    McsRoleImpl: typing.Type[McsRoleImpl]
    RbaConstants: typing.Type[RbaConstants]
    RoleImpl: typing.Type[RoleImpl]
    ServiceLocator: typing.Type[ServiceLocator]
    UserPrincipalImpl: typing.Type[UserPrincipalImpl]
    decode: cern.rbac.common.impl.decode.__module_protocol__
    exec_: cern.rbac.common.impl.exec_.__module_protocol__
    keys: cern.rbac.common.impl.keys.__module_protocol__
    request: cern.rbac.common.impl.request.__module_protocol__
    response: cern.rbac.common.impl.response.__module_protocol__
    serialization: cern.rbac.common.impl.serialization.__module_protocol__
