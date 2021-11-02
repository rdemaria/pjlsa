import java.lang
import typing



class ParameterExceptionCode(java.lang.Enum['ParameterExceptionCode']):
    """
    public enum ParameterExceptionCode extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.commons.japc.ParameterExceptionCode`>
    
        Exception codes published in :code:`ParameterException` in different situations. Can be used to filter certain
        exceptions by client applications.
    """
    USER_IS_NOT_MAPPED: typing.ClassVar['ParameterExceptionCode'] = ...
    USER_WAS_UNMAPPED_FROM_ALL_CONTEXTS: typing.ClassVar['ParameterExceptionCode'] = ...
    NO_SETTINGS_IN_NEW_CONTEXT: typing.ClassVar['ParameterExceptionCode'] = ...
    NO_SETTINGS: typing.ClassVar['ParameterExceptionCode'] = ...
    def getCode(self) -> int:
        """
        
            Returns:
                The exception's code.
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ParameterExceptionCode':
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
    def values() -> typing.List['ParameterExceptionCode']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ParameterExceptionCode c : ParameterExceptionCode.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons.japc")``.

    ParameterExceptionCode: typing.Type[ParameterExceptionCode]
