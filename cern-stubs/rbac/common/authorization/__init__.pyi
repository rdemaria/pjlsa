import cern.rbac.common
import java.lang
import java.security
import typing



class AuthorizationException(java.lang.Exception):
    """
    Java class 'cern.rbac.common.authorization.AuthorizationException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * AuthorizationException(java.lang.String)
        * AuthorizationException(java.lang.Throwable)
        * AuthorizationException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CheckingPolicy(java.lang.Enum['CheckingPolicy']):
    """
    Java class 'cern.rbac.common.authorization.CheckingPolicy'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        NO_CHECK (cern.rbac.common.authorization.CheckingPolicy): final static enum constant
        LENIENT (cern.rbac.common.authorization.CheckingPolicy): final static enum constant
        STRICT (cern.rbac.common.authorization.CheckingPolicy): final static enum constant
    
    """
    NO_CHECK: typing.ClassVar['CheckingPolicy'] = ...
    LENIENT: typing.ClassVar['CheckingPolicy'] = ...
    STRICT: typing.ClassVar['CheckingPolicy'] = ...
    @staticmethod
    def fromString(string: str) -> 'CheckingPolicy': ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CheckingPolicy': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['CheckingPolicy']: ...

class McsRole(cern.rbac.common.Role):
    """
    Java class 'cern.rbac.common.authorization.McsRole'
    
        Interfaces:
            cern.rbac.common.Role
    
    """
    def getPublicKey(self) -> java.security.PublicKey: ...

class Operation(java.lang.Enum['Operation']):
    """
    Java class 'cern.rbac.common.authorization.Operation'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        GET (cern.rbac.common.authorization.Operation): final static enum constant
        SET (cern.rbac.common.authorization.Operation): final static enum constant
        SUBSCRIBE (cern.rbac.common.authorization.Operation): final static enum constant
    
    """
    GET: typing.ClassVar['Operation'] = ...
    SET: typing.ClassVar['Operation'] = ...
    SUBSCRIBE: typing.ClassVar['Operation'] = ...
    @staticmethod
    def fromString(string: str) -> 'Operation': ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Operation': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['Operation']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.authorization")``.

    AuthorizationException: typing.Type[AuthorizationException]
    CheckingPolicy: typing.Type[CheckingPolicy]
    McsRole: typing.Type[McsRole]
    Operation: typing.Type[Operation]
