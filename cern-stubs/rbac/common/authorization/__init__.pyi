import cern.rbac.common
import java.lang
import java.security
import typing



class AuthorizationException(java.lang.Exception):
    """
    public class AuthorizationException extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`
    
        Authorization exception is thrown when a Authorization related request from a client fails.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CheckingPolicy(java.lang.Enum['CheckingPolicy']):
    """
    public enum CheckingPolicy extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.authorization.CheckingPolicy`>
    
        Enumeration allowing the specification of the checking policy (mode).
    """
    NO_CHECK: typing.ClassVar['CheckingPolicy'] = ...
    LENIENT: typing.ClassVar['CheckingPolicy'] = ...
    STRICT: typing.ClassVar['CheckingPolicy'] = ...
    @staticmethod
    def fromString(string: str) -> 'CheckingPolicy':
        """
            Returns enumeration value by it's name.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Name of the checking policy.
        
            Returns:
                enumeration value by it's name.
        
            Raises:
                : if there is no such checking policy type.
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns name of the checking policy.
        
            Returns:
                name of the operation.
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CheckingPolicy':
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
    def values() -> typing.List['CheckingPolicy']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (CheckingPolicy c : CheckingPolicy.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class McsRole(cern.rbac.common.Role):
    """
    public interface McsRole extends :class:`~cern.rbac.common.Role`
    
        Domain object containing information about an MCS role.
    """
    def getPublicKey(self) -> java.security.PublicKey:
        """
            Returns the public key associated with this MCS role.
        
            Returns:
                the public key associated with this MCS role
        
        
        """
        ...

class Operation(java.lang.Enum['Operation']):
    """
    public enum Operation extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.rbac.common.authorization.Operation`>
    
        Enumeration allowing the specification of the operation type (get, set, monitor)
    """
    GET: typing.ClassVar['Operation'] = ...
    SET: typing.ClassVar['Operation'] = ...
    SUBSCRIBE: typing.ClassVar['Operation'] = ...
    @staticmethod
    def fromString(string: str) -> 'Operation':
        """
            Returns enumeration value by it's name.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): Name of the operation.
        
            Returns:
                enumeration value by it's name.
        
            Raises:
                : if there is no such operation type.
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns name of the operation.
        
            Returns:
                name of the operation.
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Operation':
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
    def values() -> typing.List['Operation']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (Operation c : Operation.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.authorization")``.

    AuthorizationException: typing.Type[AuthorizationException]
    CheckingPolicy: typing.Type[CheckingPolicy]
    McsRole: typing.Type[McsRole]
    Operation: typing.Type[Operation]
