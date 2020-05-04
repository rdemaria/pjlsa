from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.lang


class EnumInca(java.lang.Enum['EnumInca']):
    DIR: _py_ClassVar['EnumInca'] = ...
    CTX: _py_ClassVar['EnumInca'] = ...
    CODEC: _py_ClassVar['EnumInca'] = ...
    GUI: _py_ClassVar['EnumInca'] = ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'EnumInca': ...
    _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @classmethod
    def values(cls) -> _py_List['EnumInca']: ...

class EnumUtility:
    @classmethod
    def checkPropertyValue(cls, string: str, enum: java.lang.Enum[_py_Any]) -> bool: ...

class EnumWildcard(java.lang.Enum['EnumWildcard']):
    ALL: _py_ClassVar['EnumWildcard'] = ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'EnumWildcard': ...
    _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @classmethod
    def values(cls) -> _py_List['EnumWildcard']: ...
