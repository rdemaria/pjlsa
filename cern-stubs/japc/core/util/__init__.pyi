import cern.japc.core
import cern.japc.value
import java.lang
import java.util
import typing



class JapcExceptions:
    """
    public class JapcExceptions extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utilities methods related to Exception validation.
    """
    @staticmethod
    def isNoDataAvailableException(throwable: java.lang.Throwable) -> bool:
        """
        
            Parameters:
                throwable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): a Throwable to check
        
            Returns:
                :code:`true` if the given Throwable is an instance of :class:`~cern.japc.core.NoDataAvailableException` and
                :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def isNoValueException(throwable: java.lang.Throwable) -> bool:
        """
        
            Parameters:
                throwable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): a Throwable to check
        
            Returns:
                :code:`true` if the given Throwable is an instance of :class:`~cern.japc.core.NoValueException` and :code:`false`
                otherwise
        
        
        """
        ...
    @staticmethod
    def isWaitingForDataException(throwable: java.lang.Throwable) -> bool:
        """
        
            Parameters:
                throwable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): a Throwable to check
        
            Returns:
                :code:`true` if the given Throwable is an instance of :class:`~cern.japc.core.WaitingForDataException` and :code:`false`
                otherwise
        
        
        """
        ...

class JapcUtils:
    """
    public class JapcUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def getValuesAsync(set: java.util.Set[cern.japc.core.ImmutableParameter], selector: cern.japc.core.Selector) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...
    @typing.overload
    @staticmethod
    def getValuesAsync(set: java.util.Set[cern.japc.core.ImmutableParameter], selector: cern.japc.core.Selector, long: int) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...
    @typing.overload
    @staticmethod
    def setValuesAsync(map: typing.Union[java.util.Map[cern.japc.core.Parameter, cern.japc.value.ParameterValue], typing.Mapping[cern.japc.core.Parameter, cern.japc.value.ParameterValue]], selector: cern.japc.core.Selector) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...
    @typing.overload
    @staticmethod
    def setValuesAsync(map: typing.Union[java.util.Map[cern.japc.core.Parameter, cern.japc.value.ParameterValue], typing.Mapping[cern.japc.core.Parameter, cern.japc.value.ParameterValue]], selector: cern.japc.core.Selector, long: int) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.util")``.

    JapcExceptions: typing.Type[JapcExceptions]
    JapcUtils: typing.Type[JapcUtils]
