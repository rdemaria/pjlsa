from typing import Any as _py_Any
from typing import List as _py_List
from typing import ClassVar as _py_ClassVar
from typing import overload
import cern.rbac.common
import cern.rbac.common.impl.exec
import java.lang
import java.net


class AppPrincipalImpl(cern.rbac.common.AppPrincipal, java.lang.Cloneable):
    def __init__(self, string: str, boolean: bool, integer: int): ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getName(self) -> str: ...
    def getTimeout(self) -> int: ...
    def hashCode(self) -> int: ...
    def isCritical(self) -> bool: ...
    def toString(self) -> str: ...

class LocationPrincipalImpl(cern.rbac.common.LocationPrincipal, java.lang.Cloneable):
    @overload
    def __init__(self, string: str, string2: str, boolean: bool): ...
    @overload
    def __init__(self, string: str, inetAddress: java.net.InetAddress, boolean: bool): ...
    @overload
    def __init__(self, string: str, inetAddress: java.net.InetAddress, boolean: bool, string2: str): ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getAddress(self) -> java.net.InetAddress: ...
    def getDefaultUser(self) -> str: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def isAuthRequired(self) -> bool: ...
    def toString(self) -> str: ...

class RbaConstants:
    VERSION: _py_ClassVar[str] = ...
    DEFAULT_ENCODING: _py_ClassVar[str] = ...
    SIGNATURE_ALGORITHM: _py_ClassVar[str] = ...
    KEY_ALGORITHM: _py_ClassVar[str] = ...
    KEY_SIZE: _py_ClassVar[int] = ...
    UNDEFINED_TOKEN_LIFETIME: _py_ClassVar[int] = ...
    DEFAULT_TOKEN_LIFETIME: _py_ClassVar[int] = ...
    DEFAULT_READ_TIMEOUT: _py_ClassVar[int] = ...
    CRITICAL_ROLE_PREFIX: _py_ClassVar[str] = ...

class RoleImpl(cern.rbac.common.Role, java.lang.Cloneable, java.lang.Comparable['RoleImpl']):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, int: int): ...
    def clone(self) -> _py_Any: ...
    @overload
    def compareTo(self, roleImpl: 'RoleImpl') -> int: ...
    @overload
    def compareTo(self, object: _py_Any) -> int: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getLifetime(self) -> int: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def isCritical(self) -> bool: ...
    def isLifetimeDefined(self) -> bool: ...
    def toString(self) -> str: ...

class ServiceLocator:
    @classmethod
    def getExecutionService(cls) -> cern.rbac.common.impl.exec_.ExecutionService: ...

class UserPrincipalImpl(cern.rbac.common.UserPrincipal, java.lang.Cloneable):
    def __init__(self, string: str, string2: str, string3: str, roleArray: _py_List[cern.rbac.common.Role], accountType: cern.rbac.common.UserPrincipal.AccountType): ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getAccountType(self) -> cern.rbac.common.UserPrincipal.AccountType: ...
    def getEmail(self) -> str: ...
    def getFullName(self) -> str: ...
    def getName(self) -> str: ...
    def getRoles(self) -> _py_List[cern.rbac.common.Role]: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
