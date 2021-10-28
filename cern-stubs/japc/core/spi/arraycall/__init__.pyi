import cern.japc.core
import cern.japc.core.spi.arraycall.group
import typing



class ParameterArrayCaller:
    """
    Java class 'cern.japc.core.spi.arraycall.ParameterArrayCaller'
    
    """
    def getValue(self, immutableParameter: cern.japc.core.ImmutableParameter, selector: cern.japc.core.Selector) -> cern.japc.core.FailSafeParameterValue: ...
    def registerParameter(self, immutableParameter: cern.japc.core.ImmutableParameter) -> None: ...
    def startSubscription(self, immutableParameter: cern.japc.core.ImmutableParameter, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def stopSubscription(self, immutableParameter: cern.japc.core.ImmutableParameter, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...

class ParameterArrayCallerManager:
    """
    Java class 'cern.japc.core.spi.arraycall.ParameterArrayCallerManager'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ParameterArrayCallerManager()
    
    """
    def __init__(self): ...
    def generateArrayCallerId(self) -> str: ...
    @staticmethod
    def get() -> 'ParameterArrayCallerManager': ...
    _getArrayCaller__T = typing.TypeVar('_getArrayCaller__T', bound=ParameterArrayCaller)  # <T>
    def getArrayCaller(self, class_: typing.Type[_getArrayCaller__T], string: str) -> _getArrayCaller__T: ...

class AbstractParameterArrayCaller(ParameterArrayCaller): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.arraycall")``.

    AbstractParameterArrayCaller: typing.Type[AbstractParameterArrayCaller]
    ParameterArrayCaller: typing.Type[ParameterArrayCaller]
    ParameterArrayCallerManager: typing.Type[ParameterArrayCallerManager]
    group: cern.japc.core.spi.arraycall.group.__module_protocol__
