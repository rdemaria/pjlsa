from typing import Any as _py_Any
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type


class MockServiceLocator:
    def __init__(self): ...
    @classmethod
    def getMockBean(cls, string: str) -> _py_Any: ...
    _setMockBean__T = _py_TypeVar('_setMockBean__T')  # <T>
    @classmethod
    def setMockBean(cls, class_: _py_Type[_setMockBean__T], t: _setMockBean__T) -> None: ...
