import cern.japc.core
import cern.japc.core.spi.transaction
import cern.japc.core.transaction
import java.util
import typing



class SubscriptionFilter:
    """
    Java class 'cern.japc.core.spi.subscription.SubscriptionFilter'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SubscriptionFilter()
    
    """
    def __init__(self): ...
    def startSubscription(self, parameter: cern.japc.core.Parameter, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def stopSubscription(self, parameter: cern.japc.core.Parameter, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    class JmxMBean:
        """
        Java class 'cern.japc.core.spi.subscription.SubscriptionFilter$JmxMBean'
        
        """
        def getSubscriptionNumber(self) -> int: ...
        def getSubscriptions(self) -> java.util.SortedSet[str]: ...

class WildcardParameterDecorator(cern.japc.core.spi.transaction.TransactionalParameterDecorator):
    """
    Java class 'cern.japc.core.spi.subscription.WildcardParameterDecorator'
    
        Extends:
            cern.japc.core.spi.transaction.TransactionalParameterDecorator
    
      Constructors:
        * WildcardParameterDecorator(cern.japc.core.transaction.TransactionalParameter, cern.japc.core.spi.subscription.WildcardSelectorResolver)
    
    """
    def __init__(self, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, wildcardSelectorResolver: 'WildcardSelectorResolver'): ...
    def createSubscription(self, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> cern.japc.core.SubscriptionHandle: ...
    def toString(self) -> str: ...

class WildcardSelectorResolver:
    """
    Java class 'cern.japc.core.spi.subscription.WildcardSelectorResolver'
    
      Attributes:
        SELECTOR_WILDCARD (java.lang.String): final static field
    
    """
    SELECTOR_WILDCARD: typing.ClassVar[str] = ...
    def resolve(self, selector: cern.japc.core.Selector) -> typing.List[cern.japc.core.Selector]: ...

class WildcardSubscriptionHandle(cern.japc.core.SubscriptionHandle):
    """
    Java class 'cern.japc.core.spi.subscription.WildcardSubscriptionHandle'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.SubscriptionHandle
    
      Constructors:
        * WildcardSubscriptionHandle(cern.japc.core.Selector, cern.japc.core.SubscriptionHandle[])
    
    """
    def __init__(self, selector: cern.japc.core.Selector, subscriptionHandleArray: typing.List[cern.japc.core.SubscriptionHandle]): ...
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
    """
    Java class 'cern.japc.core.spi.subscription.ListSelectorResolver'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.subscription.WildcardSelectorResolver
    
      Constructors:
        * ListSelectorResolver()
    
      Attributes:
        SELECTOR_SEPARATOR (java.lang.String): final static field
    
    """
    SELECTOR_SEPARATOR: typing.ClassVar[str] = ...
    def __init__(self): ...
    def resolve(self, selector: cern.japc.core.Selector) -> typing.List[cern.japc.core.Selector]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.subscription")``.

    ListSelectorResolver: typing.Type[ListSelectorResolver]
    SubscriptionFilter: typing.Type[SubscriptionFilter]
    WildcardParameterDecorator: typing.Type[WildcardParameterDecorator]
    WildcardSelectorResolver: typing.Type[WildcardSelectorResolver]
    WildcardSubscriptionHandle: typing.Type[WildcardSubscriptionHandle]
