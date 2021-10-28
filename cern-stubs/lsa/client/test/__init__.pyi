import typing



class MockServiceLocator:
    """
    Java class 'cern.lsa.client.test.MockServiceLocator'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MockServiceLocator()
    
    """
    def __init__(self): ...
    @staticmethod
    def getMockBean(string: str) -> typing.Any: ...
    _setMockBean__T = typing.TypeVar('_setMockBean__T')  # <T>
    @staticmethod
    def setMockBean(class_: typing.Type[_setMockBean__T], t: _setMockBean__T) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.test")``.

    MockServiceLocator: typing.Type[MockServiceLocator]
