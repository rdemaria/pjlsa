from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import overload
import java.util


class AccsoftDomainHelper:
    _immutableListOf__E = _py_TypeVar('_immutableListOf__E')  # <E>
    @classmethod
    def immutableListOf(cls, eArray: _py_List[_immutableListOf__E]) -> java.util.List[_immutableListOf__E]: ...
    _immutableMapByNameOf__E = _py_TypeVar('_immutableMapByNameOf__E')  # <E>
    @classmethod
    def immutableMapByNameOf(cls, class_: _py_Type[_immutableMapByNameOf__E]) -> java.util.Map[str, _immutableMapByNameOf__E]: ...
    _immutableSetOf_0__E = _py_TypeVar('_immutableSetOf_0__E')  # <E>
    @classmethod
    @overload
    def immutableSetOf(cls, class_: _py_Type[_immutableSetOf_0__E]) -> java.util.Set[_immutableSetOf_0__E]: ...
    _immutableSetOf_1__E = _py_TypeVar('_immutableSetOf_1__E')  # <E>
    @classmethod
    @overload
    def immutableSetOf(cls, eArray: _py_List[_immutableSetOf_1__E]) -> java.util.Set[_immutableSetOf_1__E]: ...
