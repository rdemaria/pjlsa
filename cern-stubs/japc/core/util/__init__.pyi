from typing import ClassVar as _py_ClassVar
from typing import overload
import cern.japc.core
import cern.japc.value
import java.util


class JapcAsyncUtils:
    MSG_ASYNC_SET_TIMEOUT: _py_ClassVar[str] = ...
    MSG_ASYNC_GET_TIMEOUT: _py_ClassVar[str] = ...
    SYSPROP_JAPC_ASYNC_TIMEOUT: _py_ClassVar[str] = ...
    @classmethod
    @overload
    def getValuesAsync(cls, set: java.util.Set[cern.japc.core.ImmutableParameter], selector: cern.japc.core.Selector) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...
    @classmethod
    @overload
    def getValuesAsync(cls, set: java.util.Set[cern.japc.core.ImmutableParameter], selector: cern.japc.core.Selector, long: int) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...
    @classmethod
    @overload
    def setValuesAsync(cls, map: java.util.Map[cern.japc.core.Parameter, cern.japc.value.ParameterValue], selector: cern.japc.core.Selector) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...
    @classmethod
    @overload
    def setValuesAsync(cls, map: java.util.Map[cern.japc.core.Parameter, cern.japc.value.ParameterValue], selector: cern.japc.core.Selector, long: int) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...

class JapcUtils:
    def __init__(self): ...
    @classmethod
    @overload
    def getValuesAsync(cls, set: java.util.Set[cern.japc.core.ImmutableParameter], selector: cern.japc.core.Selector) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...
    @classmethod
    @overload
    def getValuesAsync(cls, set: java.util.Set[cern.japc.core.ImmutableParameter], selector: cern.japc.core.Selector, long: int) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...
    @classmethod
    @overload
    def setValuesAsync(cls, map: java.util.Map[cern.japc.core.Parameter, cern.japc.value.ParameterValue], selector: cern.japc.core.Selector) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...
    @classmethod
    @overload
    def setValuesAsync(cls, map: java.util.Map[cern.japc.core.Parameter, cern.japc.value.ParameterValue], selector: cern.japc.core.Selector, long: int) -> java.util.Map[str, cern.japc.core.FailSafeParameterValue]: ...
