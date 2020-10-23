from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.lang


class AuthorizationException(java.lang.Exception):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CheckingPolicy(java.lang.Enum['CheckingPolicy']):
    NO_CHECK: _py_ClassVar['CheckingPolicy'] = ...
    LENIENT: _py_ClassVar['CheckingPolicy'] = ...
    STRICT: _py_ClassVar['CheckingPolicy'] = ...
    @classmethod
    def fromString(cls, string: str) -> 'CheckingPolicy': ...
    def getName(self) -> str: ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'CheckingPolicy': ...
    _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @classmethod
    def values(cls) -> _py_List['CheckingPolicy']: ...

class Operation(java.lang.Enum['Operation']):
    GET: _py_ClassVar['Operation'] = ...
    SET: _py_ClassVar['Operation'] = ...
    SUBSCRIBE: _py_ClassVar['Operation'] = ...
    @classmethod
    def fromString(cls, string: str) -> 'Operation': ...
    def getName(self) -> str: ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'Operation': ...
    _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @classmethod
    def values(cls) -> _py_List['Operation']: ...