import java.util
import typing



class EnumEmulationUtils:
    """
    public class EnumEmulationUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Allows to work with classes emulating enum behavior while not being Java enums. A class is considered to emulate Java
        enum behavior if it declares public static final fields of its own type.
    """
    _getEnumConstants__T = typing.TypeVar('_getEnumConstants__T')  # <T>
    @staticmethod
    def getEnumConstants(class_: typing.Type[_getEnumConstants__T]) -> typing.List[_getEnumConstants__T]: ...
    _getEnumConstantsMap__T = typing.TypeVar('_getEnumConstantsMap__T')  # <T>
    @staticmethod
    def getEnumConstantsMap(class_: typing.Type[_getEnumConstantsMap__T]) -> java.util.Map[str, _getEnumConstantsMap__T]: ...
    _valueOf__T = typing.TypeVar('_valueOf__T')  # <T>
    @staticmethod
    def valueOf(string: str, class_: typing.Type[_valueOf__T]) -> _valueOf__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.enums")``.

    EnumEmulationUtils: typing.Type[EnumEmulationUtils]
