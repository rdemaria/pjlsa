import java.util
import typing



class AccsoftDomainHelper:
    """
    Java class 'cern.accsoft.commons.domain.helper.AccsoftDomainHelper'
    
        Extends:
            java.lang.Object
    
    """
    _immutableListOf__E = typing.TypeVar('_immutableListOf__E')  # <E>
    @staticmethod
    def immutableListOf(eArray: typing.List[_immutableListOf__E]) -> java.util.List[_immutableListOf__E]: ...
    _immutableMapByNameOf__E = typing.TypeVar('_immutableMapByNameOf__E')  # <E>
    @staticmethod
    def immutableMapByNameOf(class_: typing.Type[_immutableMapByNameOf__E]) -> java.util.Map[str, _immutableMapByNameOf__E]: ...
    _immutableSetOf_0__E = typing.TypeVar('_immutableSetOf_0__E')  # <E>
    _immutableSetOf_1__E = typing.TypeVar('_immutableSetOf_1__E')  # <E>
    @typing.overload
    @staticmethod
    def immutableSetOf(class_: typing.Type[_immutableSetOf_0__E]) -> java.util.Set[_immutableSetOf_0__E]: ...
    @typing.overload
    @staticmethod
    def immutableSetOf(eArray: typing.List[_immutableSetOf_1__E]) -> java.util.Set[_immutableSetOf_1__E]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.helper")``.

    AccsoftDomainHelper: typing.Type[AccsoftDomainHelper]
