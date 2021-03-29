import typing


class MockServiceLocator:
    def __init__(self): ...
    @staticmethod
    def getMockBean(string: str) -> typing.Any: ...
    _setMockBean__T = typing.TypeVar('_setMockBean__T')  # <T>
    @staticmethod
    def setMockBean(class_: typing.Type[_setMockBean__T], t: _setMockBean__T) -> None: ...
