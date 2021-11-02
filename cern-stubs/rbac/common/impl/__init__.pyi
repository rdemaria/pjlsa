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
    public class AppPrincipalImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.rbac.common.AppPrincipal`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.rbac.common.AppPrincipal` interface.
    """
    def __init__(self, string: str, boolean: bool, integer: int): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getTimeout(self) -> int:
        """
            Description copied from interface: :meth:`~cern.rbac.common.AppPrincipal.getTimeout`
            Gets the application timeout in minutes.
        
            Specified by:
                :meth:`~cern.rbac.common.AppPrincipal.getTimeout` in interface :class:`~cern.rbac.common.AppPrincipal`
        
            Returns:
                application timeout in minutes or null value if it is not defined.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isCritical(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.rbac.common.AppPrincipal.isCritical`
            Checks whether this is a critical application.
        
            Specified by:
                :meth:`~cern.rbac.common.AppPrincipal.isCritical` in interface :class:`~cern.rbac.common.AppPrincipal`
        
            Returns:
                :code:`true` if this is a critical application, otherwise :code:`false`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...

class LocationPrincipalImpl(cern.rbac.common.LocationPrincipal, java.lang.Cloneable):
    """
    public class LocationPrincipalImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.rbac.common.LocationPrincipal`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.rbac.common.LocationPrincipal` interface.
    """
    @typing.overload
    def __init__(self, string: str, string2: str, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, inetAddress: java.net.InetAddress, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str, inetAddress: java.net.InetAddress, boolean: bool, string2: str): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getAddress(self) -> java.net.InetAddress:
        """
            Description copied from interface: :meth:`~cern.rbac.common.LocationPrincipal.getAddress`
            Gets the network address of the location.
        
            Specified by:
                :meth:`~cern.rbac.common.LocationPrincipal.getAddress` in interface :class:`~cern.rbac.common.LocationPrincipal`
        
            Returns:
                network address of the location
        
        
        """
        ...
    def getDefaultUser(self) -> str:
        """
            Description copied from interface: :meth:`~cern.rbac.common.LocationPrincipal.getDefaultUser`
            TODO: review if this is still used !! Gets default user for this location.
        
            Specified by:
                :meth:`~cern.rbac.common.LocationPrincipal.getDefaultUser` in interface :class:`~cern.rbac.common.LocationPrincipal`
        
            Returns:
                default user for this location
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isAuthRequired(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.rbac.common.LocationPrincipal.isAuthRequired`
            Checks whether the user authentication is required for this location.
        
            Specified by:
                :meth:`~cern.rbac.common.LocationPrincipal.isAuthRequired` in interface :class:`~cern.rbac.common.LocationPrincipal`
        
            Returns:
                :code:`true` if the user authentication is required for this location
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...

class RbaConstants:
    """
    public interface RbaConstants
    
        Common place for constants used in several different classes.
    """
    VERSION: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` VERSION
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_ENCODING: typing.ClassVar[java.nio.charset.Charset] = ...
    """
    static final `Charset <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/nio/charset/Charset.html?is-external=true>` DEFAULT_ENCODING
    
    
    """
    SIGNATURE_ALGORITHM: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SIGNATURE_ALGORITHM
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    KEY_ALGORITHM: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` KEY_ALGORITHM
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    KEY_SIZE: typing.ClassVar[int] = ...
    """
    static final int KEY_SIZE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNDEFINED_TOKEN_LIFETIME: typing.ClassVar[int] = ...
    """
    static final int UNDEFINED_TOKEN_LIFETIME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_TOKEN_LIFETIME: typing.ClassVar[int] = ...
    """
    static final int DEFAULT_TOKEN_LIFETIME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_READ_TIMEOUT: typing.ClassVar[int] = ...
    """
    static final int DEFAULT_READ_TIMEOUT
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CRITICAL_ROLE_PREFIX: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CRITICAL_ROLE_PREFIX
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    AUTHORIZATION_SCHEME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` AUTHORIZATION_SCHEME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    AUTHORIZATION_HEADER: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` AUTHORIZATION_HEADER
    
    
        Also see:
            :meth:`~constant`
    
    
    """

class RoleImpl(cern.rbac.common.Role, java.lang.Cloneable, java.lang.Comparable['RoleImpl']):
    """
    public class RoleImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.rbac.common.Role`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.rbac.common.impl.RoleImpl`>
    
        Default implementation of the :class:`~cern.rbac.common.Role` interface.
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    def clone(self) -> typing.Any: ...
    def compareTo(self, roleImpl: 'RoleImpl') -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getLifetime(self) -> int:
        """
            Description copied from interface: :meth:`~cern.rbac.common.Role.getLifetime`
            Returns lifetime (in minutes) of the role i.e. period of time for this role when it is valid and available.
        
            Specified by:
                :meth:`~cern.rbac.common.Role.getLifetime` in interface :class:`~cern.rbac.common.Role`
        
            Returns:
                lifetime (in minutes) of the role
        
        
        """
        ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.rbac.common.Role.getName`
            Returns name of the role.
        
            Specified by:
                :meth:`~cern.rbac.common.Role.getName` in interface :class:`~cern.rbac.common.Role`
        
            Returns:
                name of the role
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isCritical(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.rbac.common.Role.isCritical`
            Returns :code:`true` when this role is critical, otherwise :code:`false` is returned.
        
            Specified by:
                :meth:`~cern.rbac.common.Role.isCritical` in interface :class:`~cern.rbac.common.Role`
        
            Returns:
                :code:`true` when this role is critical, otherwise :code:`false` is returned
        
        
        """
        ...
    def isLifetimeDefined(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.rbac.common.Role.isLifetimeDefined`
            Returns :code:`true` when this role has a defined lifetime period, otherwise :code:`false` is returned.
        
            Specified by:
                :meth:`~cern.rbac.common.Role.isLifetimeDefined` in interface :class:`~cern.rbac.common.Role`
        
            Returns:
                :code:`true` when this role has a defined lifetime period, otherwise :code:`false` is returned
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ServiceLocator:
    """
    public abstract class ServiceLocator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Service locator finds an instance of a requested service and returns it to a client.
    """
    @staticmethod
    def getExecutionService() -> cern.rbac.common.impl.exec_.ExecutionService: ...

class UserPrincipalImpl(cern.rbac.common.UserPrincipal, java.lang.Cloneable):
    """
    public class UserPrincipalImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.rbac.common.UserPrincipal`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.rbac.common.UserPrincipal` interface.
    """
    def __init__(self, string: str, string2: str, string3: str, roleArray: typing.List[cern.rbac.common.Role], accountType: cern.rbac.common.UserPrincipal.AccountType): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getAccountType(self) -> cern.rbac.common.UserPrincipal.AccountType:
        """
            Description copied from interface: :meth:`~cern.rbac.common.UserPrincipal.getAccountType`
            The user type of account.
        
            Specified by:
                :meth:`~cern.rbac.common.UserPrincipal.getAccountType` in interface :class:`~cern.rbac.common.UserPrincipal`
        
            Returns:
                The user type of account.
        
        
        """
        ...
    def getEmail(self) -> str:
        """
            Description copied from interface: :meth:`~cern.rbac.common.UserPrincipal.getEmail`
            The user e-mail address.
        
            Specified by:
                :meth:`~cern.rbac.common.UserPrincipal.getEmail` in interface :class:`~cern.rbac.common.UserPrincipal`
        
            Returns:
                The user e-mail address.
        
        
        """
        ...
    def getFullName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.rbac.common.UserPrincipal.getFullName`
            The user full name.
        
            Specified by:
                :meth:`~cern.rbac.common.UserPrincipal.getFullName` in interface :class:`~cern.rbac.common.UserPrincipal`
        
            Returns:
                The user full name.
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getRoles(self) -> typing.List[cern.rbac.common.Role]:
        """
            Description copied from interface: :meth:`~cern.rbac.common.UserPrincipal.getRoles`
            Gets the list of roles assigned to the user.
        
            Specified by:
                :meth:`~cern.rbac.common.UserPrincipal.getRoles` in interface :class:`~cern.rbac.common.UserPrincipal`
        
            Returns:
                non-null array of user roles, can be empty if no roles are assigned
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...

class McsRoleImpl(RoleImpl, cern.rbac.common.authorization.McsRole):
    """
    public class McsRoleImpl extends :class:`~cern.rbac.common.impl.RoleImpl` implements :class:`~cern.rbac.common.authorization.McsRole`
    """
    def __init__(self, string: str, publicKey: java.security.PublicKey): ...
    def getPublicKey(self) -> java.security.PublicKey:
        """
            Description copied from interface: :meth:`~cern.rbac.common.authorization.McsRole.getPublicKey`
            Returns the public key associated with this MCS role.
        
            Specified by:
                :meth:`~cern.rbac.common.authorization.McsRole.getPublicKey`Â in
                interfaceÂ :class:`~cern.rbac.common.authorization.McsRole`
        
            Returns:
                the public key associated with this MCS role
        
        
        """
        ...


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
