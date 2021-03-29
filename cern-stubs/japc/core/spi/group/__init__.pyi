import cern.japc.core
import cern.japc.core.group
import cern.japc.core.transaction
import cern.japc.value
import java.util
import typing


class AbstractGroupSubscriptionHandle(cern.japc.core.group.GroupSubscriptionHandle):
    def __init__(self, immutableParameterGroup: cern.japc.core.group.ImmutableParameterGroup, selector: cern.japc.core.Selector, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, abstractGroupParameterValueListenerAdapter: 'AbstractGroupParameterValueListenerAdapter'): ...
    def getDataDeliveryMode(self) -> int: ...
    def getImmediateUpdateListener(self) -> cern.japc.core.ParameterValueListener: ...
    def getListener(self) -> cern.japc.core.group.FailSafeParameterValueListener: ...
    def getParameterGroup(self) -> cern.japc.core.group.ImmutableParameterGroup: ...
    def getSelector(self) -> cern.japc.core.Selector: ...
    def isMonitoring(self) -> bool: ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    def registerImmediateUpdateListener(self, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def setDataDeliveryMode(self, int: int) -> None: ...
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None: ...
    def toString(self) -> str: ...

class BasicParameterGroupImpl(cern.japc.core.group.BasicParameterGroup):
    def add(self, parameter: cern.japc.core.Parameter) -> None: ...
    def addAll(self, parameterArray: typing.List[cern.japc.core.Parameter]) -> None: ...
    def clear(self) -> None: ...
    @typing.overload
    def get(self, int: int) -> cern.japc.core.Parameter: ...
    @typing.overload
    def get(self, string: str) -> cern.japc.core.Parameter: ...
    def getName(self) -> str: ...
    def getNames(self) -> typing.List[str]: ...
    def getParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def getParameters(self) -> typing.List[cern.japc.core.Parameter]: ...
    def getValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def isEmpty(self) -> bool: ...
    def remove(self, parameter: cern.japc.core.Parameter) -> None: ...
    def removeAll(self, parameterArray: typing.List[cern.japc.core.Parameter]) -> None: ...
    def setName(self, string: str) -> None: ...
    def size(self) -> int: ...

class GroupParameterCurrentValue:
    def __init__(self, stringArray: typing.List[str]): ...
    def allValuesPresent(self) -> bool: ...
    def getParameterIndexes(self, string: str) -> java.util.Collection[int]: ...
    def getReceivedCount(self) -> int: ...
    def getValues(self) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    def isFree(self, string: str) -> bool: ...
    def receiveResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None: ...
    def reset(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue], booleanArray: typing.List[bool]) -> None: ...
    def toString(self) -> str: ...

class GroupParameterUtil:
    def __init__(self): ...
    @staticmethod
    def readCycleStamp(failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> int: ...
    @staticmethod
    def readFirstUpdateFlag(failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> bool: ...

class GroupParameterValueListenerAdapter:
    def getImmediateUpdateListener(self) -> cern.japc.core.ParameterValueListener: ...
    def getLastValue(self, int: int) -> cern.japc.core.FailSafeParameterValue: ...
    def getParameterNames(self) -> typing.List[str]: ...
    def getSubscriptionProblem(self, int: int) -> cern.japc.core.ParameterException: ...
    def isConstantParameter(self, int: int) -> bool: ...
    def isOnChangeParameter(self, int: int) -> bool: ...
    def peekValue(self, int: int, long: int) -> cern.japc.core.AcquiredParameterValue: ...
    def sendImmediateUpdate(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None: ...
    def sendUpdate(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> None: ...

class GroupSubscriptionStrategy:
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    def updateResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None: ...

class GroupSubscriptionStrategyFactory:
    def getAsyncGetSetStrategy(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter, parameterArray: typing.List[cern.japc.core.Parameter]) -> GroupSubscriptionStrategy: ...
    def getSubscriptionStrategy(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter, parameterArray: typing.List[cern.japc.core.Parameter], selector: cern.japc.core.Selector) -> GroupSubscriptionStrategy: ...

class AbstractGroupParameterValueListenerAdapter(cern.japc.core.ParameterValueListener, GroupParameterValueListenerAdapter):
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None: ...
    def getDataDeliveryMode(self) -> int: ...
    def getImmediateUpdateListener(self) -> cern.japc.core.ParameterValueListener: ...
    def getLastValue(self, int: int) -> cern.japc.core.FailSafeParameterValue: ...
    def getParameterNames(self) -> typing.List[str]: ...
    def getSubscriptionProblem(self, int: int) -> cern.japc.core.ParameterException: ...
    def isConstantParameter(self, int: int) -> bool: ...
    def isMonitoring(self) -> bool: ...
    def isOnChangeParameter(self, int: int) -> bool: ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    def registerImmediateUpdateListener(self, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def sendImmediateUpdate(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None: ...
    def sendUpdate(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> None: ...
    def setDataDeliveryMode(self, int: int) -> None: ...
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None: ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None: ...

class AbstractGroupSubscriptionStrategy(GroupSubscriptionStrategy):
    def __init__(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter): ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    def updateResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None: ...

class DefaultGroupSubscriptionStrategyFactory(GroupSubscriptionStrategyFactory):
    def __init__(self): ...
    @staticmethod
    def get() -> 'DefaultGroupSubscriptionStrategyFactory': ...
    def getAsyncGetSetStrategy(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter, parameterArray: typing.List[cern.japc.core.Parameter]) -> GroupSubscriptionStrategy: ...
    def getSubscriptionStrategy(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter, parameterArray: typing.List[cern.japc.core.Parameter], selector: cern.japc.core.Selector) -> GroupSubscriptionStrategy: ...

class GPCSCurrentValue(GroupParameterCurrentValue):
    def __init__(self, stringArray: typing.List[str]): ...
    def compareCycleStamps(self, long: int) -> int: ...
    def compareCycleStampsAndFlags(self, long: int, boolean: bool) -> int: ...
    def getCycleStamp(self) -> int: ...
    def getFirstUpdateFlag(self) -> bool: ...
    def receiveResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None: ...
    def reset(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue], booleanArray: typing.List[bool]) -> None: ...

class GroupSubscriptionHandleImpl(AbstractGroupSubscriptionHandle):
    def __init__(self, immutableParameterGroup: cern.japc.core.group.ImmutableParameterGroup, selector: cern.japc.core.Selector, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    def toString(self) -> str: ...

class ImmutableParameterGroupImpl(BasicParameterGroupImpl, cern.japc.core.group.ImmutableParameterGroup):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    def createSubscription(self, selector: cern.japc.core.Selector, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener) -> cern.japc.core.group.GroupSubscriptionHandle: ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener) -> None: ...
    def isArrayCallMode(self) -> bool: ...
    def setArrayCallMode(self, boolean: bool) -> None: ...

class PullGroupSubscriptionStrategy(GroupSubscriptionStrategy):
    def __init__(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter): ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    def updateResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None: ...

class PushGroupSubscriptionStrategy(GroupSubscriptionStrategy):
    NO_TIMEOUT: typing.ClassVar[int] = ...
    def __init__(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter): ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    def setTimeout(self, long: int) -> None: ...
    def updateResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None: ...

class GroupParameterValueListenerAdapterImpl(AbstractGroupParameterValueListenerAdapter):
    @typing.overload
    def __init__(self, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, parameterArray: typing.List[cern.japc.core.Parameter], selector: cern.japc.core.Selector, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    @typing.overload
    def __init__(self, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, parameterArray: typing.List[cern.japc.core.Parameter], groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    def peekValue(self, int: int, long: int) -> cern.japc.core.AcquiredParameterValue: ...
    def setDataDeliveryModeImpl(self, int: int) -> None: ...

class ParameterGroupImpl(ImmutableParameterGroupImpl, cern.japc.core.group.ParameterGroup):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue]) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue], failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener) -> None: ...

class TransactionalParameterGroupImpl(ParameterGroupImpl, cern.japc.core.group.TransactionalParameterGroup):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue], compositeTransaction: cern.japc.core.transaction.CompositeTransaction) -> None: ...
