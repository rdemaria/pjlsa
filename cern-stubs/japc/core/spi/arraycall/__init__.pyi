import cern.japc.core
import cern.japc.core.spi.arraycall.group
import typing



class ParameterArrayCaller:
    def getValue(self, immutableParameter: cern.japc.core.ImmutableParameter, selector: cern.japc.core.Selector) -> cern.japc.core.FailSafeParameterValue: ...
    def registerParameter(self, immutableParameter: cern.japc.core.ImmutableParameter) -> None: ...
    def startSubscription(self, immutableParameter: cern.japc.core.ImmutableParameter, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def stopSubscription(self, immutableParameter: cern.japc.core.ImmutableParameter, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...

class ParameterArrayCallerManager:
    """
    public class ParameterArrayCallerManager extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class is used as a singleton and contains all the existing instances of
        :class:`~cern.japc.core.spi.arraycall.ParameterArrayCaller`'s. This class is also capable of generating unique
        identifiers for :class:`~cern.japc.core.spi.arraycall.ParameterArrayCaller` instances.
    """
    def __init__(self): ...
    def generateArrayCallerId(self) -> str:
        """
            Returns generated unique RDA Parameter Array Caller ID.
        
            Returns:
                generated unique RDA Parameter Array Caller ID
        
        
        """
        ...
    @staticmethod
    def get() -> 'ParameterArrayCallerManager':
        """
            Returns the singleton.
        
            Returns:
                the singleton
        
        
        """
        ...
    _getArrayCaller__T = typing.TypeVar('_getArrayCaller__T', bound=ParameterArrayCaller)  # <T>
    def getArrayCaller(self, class_: typing.Type[_getArrayCaller__T], string: str) -> _getArrayCaller__T: ...

class AbstractParameterArrayCaller(ParameterArrayCaller):
    """
    public abstract class AbstractParameterArrayCaller extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.arraycall.ParameterArrayCaller`
    
        All specific implementations of :code:`ParameterArrayCaller` shall inherit from that class
    """
    ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.arraycall")``.

    AbstractParameterArrayCaller: typing.Type[AbstractParameterArrayCaller]
    ParameterArrayCaller: typing.Type[ParameterArrayCaller]
    ParameterArrayCallerManager: typing.Type[ParameterArrayCallerManager]
    group: cern.japc.core.spi.arraycall.group.__module_protocol__
