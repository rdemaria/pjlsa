from typing import List as _py_List
from typing import ClassVar as _py_ClassVar
import cern.japc.core
import cern.japc.core.spi.transaction
import cern.japc.core.transaction
import java.util


class SubscriptionFilter:
    def __init__(self): ...
    def startSubscription(self, parameter: cern.japc.core.Parameter, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def stopSubscription(self, parameter: cern.japc.core.Parameter, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    class JmxMBean:
        def getSubscriptionNumber(self) -> int: ...
        def getSubscriptions(self) -> java.util.SortedSet[str]: ...

class WildcardParameterDecorator(cern.japc.core.spi.transaction.TransactionalParameterDecorator):
    def __init__(self, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, wildcardSelectorResolver: 'WildcardSelectorResolver'): ...
    def createSubscription(self, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> cern.japc.core.SubscriptionHandle: ...
    def toString(self) -> str: ...

class WildcardSelectorResolver:
    SELECTOR_WILDCARD: _py_ClassVar[str] = ...
    def resolve(self, selector: cern.japc.core.Selector) -> _py_List[cern.japc.core.Selector]: ...

class WildcardSubscriptionHandle(cern.japc.core.SubscriptionHandle):
    def __init__(self, selector: cern.japc.core.Selector, subscriptionHandleArray: _py_List[cern.japc.core.SubscriptionHandle]): ...
    def getDataDeliveryMode(self) -> int: ...
    def getListener(self) -> cern.japc.core.ParameterValueListener: ...
    def getParameter(self) -> cern.japc.core.ImmutableParameter: ...
    def getSelector(self) -> cern.japc.core.Selector: ...
    def isMonitoring(self) -> bool: ...
    def peekValue(self, long: int) -> cern.japc.core.AcquiredParameterValue: ...
    def setDataDeliveryMode(self, int: int) -> None: ...
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None: ...

class ListSelectorResolver(WildcardSelectorResolver):
    SELECTOR_SEPARATOR: _py_ClassVar[str] = ...
    def __init__(self): ...
    def resolve(self, selector: cern.japc.core.Selector) -> _py_List[cern.japc.core.Selector]: ...
