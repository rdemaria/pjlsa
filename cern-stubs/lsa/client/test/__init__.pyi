import typing



class MockServiceLocator:
    """
    public final class MockServiceLocator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        The class can be used to mock LSA services. It is used by the :code:`ServiceLocator` to check if there is a mock
        instance of a requested bean. The typical usage would be like this:
    
        .. code-block: java
        
         OpticService service = mock(OpticService.class);
         when(service.findAccelerators()).thenReturn(ACCELERATORS);
         //Set the mock implementation of the controller      
         MockServiceLocator.setMockBean(OpticService.class, service);
    """
    def __init__(self): ...
    @staticmethod
    def getMockBean(string: str) -> typing.Any:
        """
            Returns bean registered for the specified interface name. The :code:`ServiceLocator` uses this method to check if there
            is a mock bean registered for a given interface and returns it if there is one.
        
            Parameters:
                interfaceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): decapitalized `null
                    <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true#getSimpleName()>` of the
                    interface class
        
            Returns:
                bean registered for this name
        
        
        """
        ...
    _setMockBean__T = typing.TypeVar('_setMockBean__T')  # <T>
    @staticmethod
    def setMockBean(class_: typing.Type[_setMockBean__T], t: _setMockBean__T) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.test")``.

    MockServiceLocator: typing.Type[MockServiceLocator]
