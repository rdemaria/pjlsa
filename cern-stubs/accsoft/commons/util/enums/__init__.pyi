import java.lang
import typing



class EnumInca(java.lang.Enum['EnumInca']):
    """
    public enum EnumInca extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.util.enums.EnumInca`>
    
    
    
        Contains the list of possible values to be checked for the "USE_INCA" system property via the
        :meth:`~cern.accsoft.commons.util.enums.EnumUtility.checkPropertyValue` method.
    """
    DIR: typing.ClassVar['EnumInca'] = ...
    CTX: typing.ClassVar['EnumInca'] = ...
    CODEC: typing.ClassVar['EnumInca'] = ...
    GUI: typing.ClassVar['EnumInca'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'EnumInca':
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
    def values() -> typing.List['EnumInca']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (EnumInca c : EnumInca.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class EnumUtility:
    """
    public class EnumUtility extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Contains utility methods related to java Enum support.
    """
    @staticmethod
    def checkPropertyValue(string: str, enum: java.lang.Enum[typing.Any]) -> bool: ...

class EnumWildcard(java.lang.Enum['EnumWildcard']):
    """
    public enum EnumWildcard extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.util.enums.EnumWildcard`>
    
        This value is the *wildcard* one overriding all possible enum values in the
        :meth:`~cern.accsoft.commons.util.enums.EnumUtility.checkPropertyValue` method.
    """
    ALL: typing.ClassVar['EnumWildcard'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'EnumWildcard':
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
    def values() -> typing.List['EnumWildcard']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (EnumWildcard c : EnumWildcard.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.enums")``.

    EnumInca: typing.Type[EnumInca]
    EnumUtility: typing.Type[EnumUtility]
    EnumWildcard: typing.Type[EnumWildcard]
