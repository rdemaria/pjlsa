import java.lang
import typing



class LoginPolicy(java.lang.Enum['LoginPolicy']):
    """
    Java class 'cern.rbac.common.authentication.LoginPolicy'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        DEFAULT (cern.rbac.common.authentication.LoginPolicy): final static enum constant
        LOCATION (cern.rbac.common.authentication.LoginPolicy): final static enum constant
        KERBEROS (cern.rbac.common.authentication.LoginPolicy): final static enum constant
        EXPLICIT (cern.rbac.common.authentication.LoginPolicy): final static enum constant
        SSO (cern.rbac.common.authentication.LoginPolicy): final static enum constant
        SAML (cern.rbac.common.authentication.LoginPolicy): final static enum constant
        OAUTH (cern.rbac.common.authentication.LoginPolicy): final static enum constant
    
    """
    DEFAULT: typing.ClassVar['LoginPolicy'] = ...
    LOCATION: typing.ClassVar['LoginPolicy'] = ...
    KERBEROS: typing.ClassVar['LoginPolicy'] = ...
    EXPLICIT: typing.ClassVar['LoginPolicy'] = ...
    SSO: typing.ClassVar['LoginPolicy'] = ...
    SAML: typing.ClassVar['LoginPolicy'] = ...
    OAUTH: typing.ClassVar['LoginPolicy'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LoginPolicy': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['LoginPolicy']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.authentication")``.

    LoginPolicy: typing.Type[LoginPolicy]
