from typing import List as _py_List
from typing import overload
import cern
import cern.japc.core
import cern.japc.core.group
import cern.japc.core.spi.transaction
import cern.japc.value


class GroupBasedViewParameter(cern.japc.core.spi.transaction.TransactionalParameterSupport):
    def __init__(self, string: str, immutableParameterGroup: cern.japc.core.group.ImmutableParameterGroup, parameterGroupValueReceivedAdapter: cern.japc.core.group.ParameterGroupValueReceivedAdapter): ...
    def getImmutableParameterGroup(self) -> cern.japc.core.group.ImmutableParameterGroup: ...
    def toString(self) -> str: ...

class ParameterGroupValueReceivedConcentrator(cern.japc.core.group.ParameterGroupValueReceivedAdapter):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, lengthExtractor: 'ConcentratorHelper.LengthExtractor'): ...
    def adaptValueReceived(self, failSafeParameterValueArray: _py_List[cern.japc.core.FailSafeParameterValue]) -> cern.japc.core.AcquiredParameterValue: ...

class SysoutFailSafeParameterValueListener(cern.japc.core.group.FailSafeParameterValueListener):
    def __init__(self): ...
    def valueReceived(self, failSafeParameterValueArray: _py_List[cern.japc.core.FailSafeParameterValue]) -> None: ...

class GroupBasedParameter(GroupBasedViewParameter):
    def __init__(self, string: str, transactionalParameterGroup: cern.japc.core.group.TransactionalParameterGroup, parameterGroupValueReceivedAdapter: cern.japc.core.group.ParameterGroupValueReceivedAdapter, parameterGroupValueSentAdapter: cern.japc.core.group.ParameterGroupValueSentAdapter): ...
    def getTransactionalParameterGroup(self) -> cern.japc.core.group.TransactionalParameterGroup: ...

class ConcentratorHelper:
    def __init__(self): ...
    @classmethod
    def appendParameterValue(cls, mapParameterValueArray: _py_List[cern.japc.value.MapParameterValue], string: str) -> cern.japc.value.SimpleParameterValue: ...
    @classmethod
    @overload
    def mergeParameterValue(cls, mapParameterValueArray: _py_List[cern.japc.value.MapParameterValue]) -> cern.japc.value.MapParameterValue: ...
    @classmethod
    @overload
    def mergeParameterValue(cls, mapParameterValueArray: _py_List[cern.japc.value.MapParameterValue], string: str) -> cern.japc.value.SimpleParameterValue: ...
    @classmethod
    @overload
    def mergeParameterValue(cls, mapParameterValueArray: _py_List[cern.japc.value.MapParameterValue], string: str, lengthExtractor: 'ConcentratorHelper.LengthExtractor') -> cern.japc.value.SimpleParameterValue: ...
    class LengthExtractor:
        def extractLength(self, mapParameterValue: cern.japc.value.MapParameterValue, int: int, string: str) -> int: ...
    class NameBasedLengthExtractor(cern.japc.core.group.support.ConcentratorHelper.LengthExtractor):
        def __init__(self, string: str): ...
        def extractLength(self, mapParameterValue: cern.japc.value.MapParameterValue, int: int, string: str) -> int: ...
    class Selector:
        def select(self, simpleParameterValue: cern.japc.value.SimpleParameterValue, int: int) -> bool: ...
    class SelectorBasedLengthExtractor(cern.japc.core.group.support.ConcentratorHelper.LengthExtractor):
        @overload
        def __init__(self, string: str, selector: 'ConcentratorHelper.Selector'): ...
        @overload
        def __init__(self, string: str, selector: 'ConcentratorHelper.Selector', boolean: bool): ...
        def extractLength(self, mapParameterValue: cern.japc.value.MapParameterValue, int: int, string: str) -> int: ...
