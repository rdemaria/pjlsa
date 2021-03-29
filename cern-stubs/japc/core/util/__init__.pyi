import cern.japc.core
import cern.japc.value
import java.util
import typing


class JapcUtils:
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
