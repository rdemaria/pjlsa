import cern.japc.core
import cern.japc.core.group.support
import cern.japc.core.transaction
import cern.japc.value
import typing



class BasicParameterGroup:
    """
    Java class 'cern.japc.core.group.BasicParameterGroup'
    
    """
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
    def size(self) -> int: ...

class FailSafeParameterValueListener:
    """
    Java class 'cern.japc.core.group.FailSafeParameterValueListener'
    
    """
    def valueReceived(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> None: ...

class GroupSubscriptionHandle(cern.japc.core.SubscriptionConfigurator):
    """
    Java class 'cern.japc.core.group.GroupSubscriptionHandle'
    
        Interfaces:
            cern.japc.core.SubscriptionConfigurator
    
    """
    def getImmediateUpdateListener(self) -> cern.japc.core.ParameterValueListener: ...
    def getListener(self) -> FailSafeParameterValueListener: ...
    def getParameterGroup(self) -> 'ImmutableParameterGroup': ...
    def isMonitoring(self) -> bool: ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    def registerImmediateUpdateListener(self, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None: ...

class ParameterFieldNames:
    """
    Java class 'cern.japc.core.group.ParameterFieldNames'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ParameterFieldNames(java.lang.String, java.lang.String[])
    
    """
    def __init__(self, string: str, stringArray: typing.List[str]): ...
    @staticmethod
    def concatParameterFieldNames(parameterFieldNamesArray: typing.List['ParameterFieldNames']) -> typing.List[str]: ...
    def getFieldNames(self) -> typing.List[str]: ...
    def getFullParameterNames(self) -> typing.List[str]: ...
    def getParameterName(self) -> str: ...

class ParameterGroupValueReceivedAdapter:
    """
    Java class 'cern.japc.core.group.ParameterGroupValueReceivedAdapter'
    
    """
    def adaptValueReceived(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> cern.japc.core.AcquiredParameterValue: ...

class ParameterGroupValueSentAdapter:
    """
    Java class 'cern.japc.core.group.ParameterGroupValueSentAdapter'
    
    """
    def adaptValueSent(self, parameterValue: cern.japc.value.ParameterValue) -> typing.List[cern.japc.value.ParameterValue]: ...

class ImmutableParameterGroup(BasicParameterGroup):
    """
    Java class 'cern.japc.core.group.ImmutableParameterGroup'
    
        Interfaces:
            cern.japc.core.group.BasicParameterGroup
    
    """
    def createSubscription(self, selector: cern.japc.core.Selector, failSafeParameterValueListener: FailSafeParameterValueListener) -> GroupSubscriptionHandle: ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector, failSafeParameterValueListener: FailSafeParameterValueListener) -> None: ...

class ParameterGroup(ImmutableParameterGroup):
    """
    Java class 'cern.japc.core.group.ParameterGroup'
    
        Interfaces:
            cern.japc.core.group.ImmutableParameterGroup
    
    """
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue]) -> typing.List[cern.japc.core.FailSafeParameterValue]: ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue], failSafeParameterValueListener: FailSafeParameterValueListener) -> None: ...

class TransactionalParameterGroup(ParameterGroup):
    """
    Java class 'cern.japc.core.group.TransactionalParameterGroup'
    
        Interfaces:
            cern.japc.core.group.ParameterGroup
    
    """
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue], compositeTransaction: cern.japc.core.transaction.CompositeTransaction) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.group")``.

    BasicParameterGroup: typing.Type[BasicParameterGroup]
    FailSafeParameterValueListener: typing.Type[FailSafeParameterValueListener]
    GroupSubscriptionHandle: typing.Type[GroupSubscriptionHandle]
    ImmutableParameterGroup: typing.Type[ImmutableParameterGroup]
    ParameterFieldNames: typing.Type[ParameterFieldNames]
    ParameterGroup: typing.Type[ParameterGroup]
    ParameterGroupValueReceivedAdapter: typing.Type[ParameterGroupValueReceivedAdapter]
    ParameterGroupValueSentAdapter: typing.Type[ParameterGroupValueSentAdapter]
    TransactionalParameterGroup: typing.Type[TransactionalParameterGroup]
    support: cern.japc.core.group.support.__module_protocol__
