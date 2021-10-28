import java.lang
import typing



class EnumInca(java.lang.Enum['EnumInca']):
    """
    Java class 'cern.accsoft.commons.util.enums.EnumInca'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        DIR (cern.accsoft.commons.util.enums.EnumInca): final static enum constant
        CTX (cern.accsoft.commons.util.enums.EnumInca): final static enum constant
        CODEC (cern.accsoft.commons.util.enums.EnumInca): final static enum constant
        GUI (cern.accsoft.commons.util.enums.EnumInca): final static enum constant
    
    """
    DIR: typing.ClassVar['EnumInca'] = ...
    CTX: typing.ClassVar['EnumInca'] = ...
    CODEC: typing.ClassVar['EnumInca'] = ...
    GUI: typing.ClassVar['EnumInca'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'EnumInca': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['EnumInca']: ...

class EnumUtility:
    """
    Java class 'cern.accsoft.commons.util.enums.EnumUtility'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def checkPropertyValue(string: str, enum: java.lang.Enum[typing.Any]) -> bool: ...

class EnumWildcard(java.lang.Enum['EnumWildcard']):
    """
    Java class 'cern.accsoft.commons.util.enums.EnumWildcard'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        ALL (cern.accsoft.commons.util.enums.EnumWildcard): final static enum constant
    
    """
    ALL: typing.ClassVar['EnumWildcard'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'EnumWildcard': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['EnumWildcard']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.enums")``.

    EnumInca: typing.Type[EnumInca]
    EnumUtility: typing.Type[EnumUtility]
    EnumWildcard: typing.Type[EnumWildcard]
