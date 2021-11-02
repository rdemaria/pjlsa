import java.lang
import typing



class LoginPolicy(java.lang.Enum['LoginPolicy']):
    """
    public enum LoginPolicy extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.authentication.LoginPolicy`>
    
        Enum defines possible login policies which can be specified when a new instance of RbaLoginContext is created. Login
        policy defines behavior of the login process and enables certain login modules e.g.: login by location or explicit
        login.
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
    def valueOf(string: str) -> 'LoginPolicy':
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
    def values() -> typing.List['LoginPolicy']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LoginPolicy c : LoginPolicy.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.authentication")``.

    LoginPolicy: typing.Type[LoginPolicy]
