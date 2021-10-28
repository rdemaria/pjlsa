import java.lang
import typing



class ParameterExceptionCode(java.lang.Enum['ParameterExceptionCode']):
    """
    Java class 'cern.lsa.domain.commons.japc.ParameterExceptionCode'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        USER_IS_NOT_MAPPED (cern.lsa.domain.commons.japc.ParameterExceptionCode): final static enum constant
        USER_WAS_UNMAPPED_FROM_ALL_CONTEXTS (cern.lsa.domain.commons.japc.ParameterExceptionCode): final static enum constant
        NO_SETTINGS_IN_NEW_CONTEXT (cern.lsa.domain.commons.japc.ParameterExceptionCode): final static enum constant
        NO_SETTINGS (cern.lsa.domain.commons.japc.ParameterExceptionCode): final static enum constant
    
    """
    USER_IS_NOT_MAPPED: typing.ClassVar['ParameterExceptionCode'] = ...
    USER_WAS_UNMAPPED_FROM_ALL_CONTEXTS: typing.ClassVar['ParameterExceptionCode'] = ...
    NO_SETTINGS_IN_NEW_CONTEXT: typing.ClassVar['ParameterExceptionCode'] = ...
    NO_SETTINGS: typing.ClassVar['ParameterExceptionCode'] = ...
    def getCode(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ParameterExceptionCode': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['ParameterExceptionCode']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons.japc")``.

    ParameterExceptionCode: typing.Type[ParameterExceptionCode]
