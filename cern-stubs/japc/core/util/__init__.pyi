import cern.japc.core
import cern.japc.value
import java.lang
import java.util
import typing



class JapcExceptions:
    """
    Java class 'cern.japc.core.util.JapcExceptions'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def isNoDataAvailableException(throwable: java.lang.Throwable) -> bool: ...
    @staticmethod
    def isNoValueException(throwable: java.lang.Throwable) -> bool: ...
    @staticmethod
    def isWaitingForDataException(throwable: java.lang.Throwable) -> bool: ...

class JapcUtils:
    """
    Java class 'cern.japc.core.util.JapcUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * JapcUtils()
    
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
