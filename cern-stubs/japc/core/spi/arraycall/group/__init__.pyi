import cern.japc.core
import cern.japc.core.group
import cern.japc.core.spi.group
import typing



class ArrayCallGroupParameterValueListenerAdapter(cern.japc.core.spi.group.AbstractGroupParameterValueListenerAdapter):
    """
    Java class 'cern.japc.core.spi.arraycall.group.ArrayCallGroupParameterValueListenerAdapter'
    
        Extends:
            cern.japc.core.spi.group.AbstractGroupParameterValueListenerAdapter
    
      Constructors:
        * ArrayCallGroupParameterValueListenerAdapter(cern.japc.core.group.FailSafeParameterValueListener, cern.japc.core.Parameter[], cern.japc.core.Selector, cern.japc.core.spi.group.GroupSubscriptionStrategyFactory)
        * ArrayCallGroupParameterValueListenerAdapter(cern.japc.core.group.FailSafeParameterValueListener, cern.japc.core.Parameter[], cern.japc.core.spi.group.GroupSubscriptionStrategyFactory)
    
    """
    @typing.overload
    def __init__(self, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, parameterArray: typing.List[cern.japc.core.Parameter], selector: cern.japc.core.Selector, groupSubscriptionStrategyFactory: cern.japc.core.spi.group.GroupSubscriptionStrategyFactory): ...
    @typing.overload
    def __init__(self, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, parameterArray: typing.List[cern.japc.core.Parameter], groupSubscriptionStrategyFactory: cern.japc.core.spi.group.GroupSubscriptionStrategyFactory): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None: ...
    def peekValue(self, int: int, long: int) -> cern.japc.core.AcquiredParameterValue: ...
    def setDataDeliveryModeImpl(self, int: int) -> None: ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None: ...

class ArrayCallGroupSubscriptionHandle(cern.japc.core.spi.group.AbstractGroupSubscriptionHandle):
    """
    Java class 'cern.japc.core.spi.arraycall.group.ArrayCallGroupSubscriptionHandle'
    
        Extends:
            cern.japc.core.spi.group.AbstractGroupSubscriptionHandle
    
      Constructors:
        * ArrayCallGroupSubscriptionHandle(cern.japc.core.group.ImmutableParameterGroup, cern.japc.core.Selector, cern.japc.core.group.FailSafeParameterValueListener, cern.japc.core.spi.group.GroupSubscriptionStrategyFactory)
    
    """
    def __init__(self, immutableParameterGroup: cern.japc.core.group.ImmutableParameterGroup, selector: cern.japc.core.Selector, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, groupSubscriptionStrategyFactory: cern.japc.core.spi.group.GroupSubscriptionStrategyFactory): ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.arraycall.group")``.

    ArrayCallGroupParameterValueListenerAdapter: typing.Type[ArrayCallGroupParameterValueListenerAdapter]
    ArrayCallGroupSubscriptionHandle: typing.Type[ArrayCallGroupSubscriptionHandle]
