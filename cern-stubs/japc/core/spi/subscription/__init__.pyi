import cern.japc.core
import cern.japc.core.spi.transaction
import cern.japc.core.transaction
import java.util
import typing



class SubscriptionFilter:
    """
    public abstract class SubscriptionFilter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        The goal of this class is to prevent a lot of subscriptions to the same parameter with the same
        :class:`~cern.japc.core.Selector`. So, it subscribes to the parameter with some Selector when the first client appears
        and unsubscribes if the last client disappears. SubscriptionSources don't subscribe/unsubscribe by themselves, but
        delegate this activity to the SubscriptionFilter.
    """
    def __init__(self): ...
    def startSubscription(self, parameter: cern.japc.core.Parameter, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def stopSubscription(self, parameter: cern.japc.core.Parameter, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None:
        """
            This method removes ParameterValueListener passed from the clients list of combination [Parameter/Selector]. If it was
            the last client the subscription will be stopped.
        
            Parameters:
                parameter (:class:`~cern.japc.core.Parameter`): parameter of subscription
                selector (:class:`~cern.japc.core.Selector`): selector of subscription
                pvl (:class:`~cern.japc.core.ParameterValueListener`): listener of subscription
        
        
        """
        ...
    class JmxMBean:
        def getSubscriptionNumber(self) -> int: ...
        def getSubscriptions(self) -> java.util.SortedSet[str]: ...

class WildcardParameterDecorator(cern.japc.core.spi.transaction.TransactionalParameterDecorator):
    """
    public class WildcardParameterDecorator extends :class:`~cern.japc.core.spi.transaction.TransactionalParameterDecorator`
    
        This decorator can subscribe with wildcard selector. The :class:`~cern.japc.core.SubscriptionHandle` returned by
        :meth:`~cern.japc.core.spi.subscription.WildcardParameterDecorator.createSubscription` is special
        :class:`~cern.japc.core.spi.subscription.WildcardSubscriptionHandle` implementation.
    """
    def __init__(self, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, wildcardSelectorResolver: 'WildcardSelectorResolver'): ...
    def createSubscription(self, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> cern.japc.core.SubscriptionHandle:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.createSubscription`
            Creates a private subscription for a given listener and on an given cycle selector. Using the subscription handle
            returned it is possible to start and stop monitoring this parameter on the given cycle selector. The handle returned
            must not be shared or accessed concurrently. In addition it is necessary to keep a strong reference on the handle
            returned as long as it useful. Not doing so exposes the returned handle to garbage collection and would potentially
            automatically stop the subscription for the given listener.
        
            The subscription handle can be configured in two mode : PUSH or PULL. The PUSH mode (@see
            SubscriptionConfiguration#PUSH_MODE) is the default mode the handle is created with. With this mode, value are sent
            (pushed) to the listener given to the handle as they are received. The PULL mode (@see
            SubscriptionConfiguration#PULL_MODE) is another mode where only immediate updates are sent to the listener. The other
            values received on a regular basis are not sent to the listener and must be looked up using the (@see
            SubscriptionHandle#peekValues(long)) method.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.createSubscription` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Overrides:
                :meth:`~cern.japc.core.spi.ImmutableParameterDecorator.createSubscription`Â in
                classÂ :class:`~cern.japc.core.spi.ImmutableParameterDecorator`
        
            Parameters:
                wildcardSelector (:class:`~cern.japc.core.Selector`): the cycle selector on which to monitor the parameter
                parameterValueListener (:class:`~cern.japc.core.ParameterValueListener`): the listener that will received the notification for that request
        
            Returns:
                the subscription handle that can be used to monitor this parameter.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.japc.core.spi.ImmutableParameterDecorator.toString`Â in
                classÂ :class:`~cern.japc.core.spi.ImmutableParameterDecorator`
        
        
        """
        ...

class WildcardSelectorResolver:
    """
    public interface WildcardSelectorResolver
    
        An implementation of this interface is responsible of matching a selector with wildcards to a set of real selectors. The
        typical syntax of wildcard selector is SPS.USER.CNGS*. It should be transformed into an array like this:
        [SPS.USER.CNGS1, SPS.USER.CNGS2, SPS.USER.CNGS3, SPS.USER.CNGS4]
    """
    SELECTOR_WILDCARD: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SELECTOR_WILDCARD
    
        The wildcard symbol
    
        Also see:
            :meth:`~constant`
    
    
    """
    def resolve(self, selector: cern.japc.core.Selector) -> typing.List[cern.japc.core.Selector]:
        """
            This method returns an array of all matching selectors for the given wildcard selector. If no match found the passed
            selector itself returned in an array.
        
            Parameters:
                wildcardSelector (:class:`~cern.japc.core.Selector`): wildcard selector
        
            Returns:
                if matches: an array with all matching selectors for the given wildcard selector; if no match: give back the selecotr
                passed as argument itself, in an array.
        
        
        """
        ...

class WildcardSubscriptionHandle(cern.japc.core.SubscriptionHandle):
    """
    public class WildcardSubscriptionHandle extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.SubscriptionHandle`
    
        Special implementation of :class:`~cern.japc.core.SubscriptionHandle` which handles a set of subscriptions to the same
        parameter but with :class:`~cern.japc.core.Selector`s matching a wildcard selector.
    """
    def __init__(self, selector: cern.japc.core.Selector, subscriptionHandleArray: typing.List[cern.japc.core.SubscriptionHandle]): ...
    def getDataDeliveryMode(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.SubscriptionConfigurator.getDataDeliveryMode`
            Returns the current mode of data delivery.
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionConfigurator.getDataDeliveryMode`Â in
                interfaceÂ :class:`~cern.japc.core.SubscriptionConfigurator`
        
            Returns:
                the current mode of data delivery.
        
        
        """
        ...
    def getListener(self) -> cern.japc.core.ParameterValueListener:
        """
            Description copied from interface: :meth:`~cern.japc.core.SubscriptionHandle.getListener`
            Returns the non null registered listener.
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionHandle.getListener` in interface :class:`~cern.japc.core.SubscriptionHandle`
        
            Returns:
                the non null registered listener.
        
        
        """
        ...
    def getParameter(self) -> cern.japc.core.ImmutableParameter:
        """
            Description copied from interface: :meth:`~cern.japc.core.SubscriptionHandle.getParameter`
            Returns the parameter for which this handle has been created
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionHandle.getParameter` in interface :class:`~cern.japc.core.SubscriptionHandle`
        
            Returns:
                the parameter for which this handle has been created
        
        
        """
        ...
    def getSelector(self) -> cern.japc.core.Selector:
        """
            Description copied from interface: :meth:`~cern.japc.core.SubscriptionConfigurator.getSelector`
            Returns the cycle selector on which this request is activated
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionConfigurator.getSelector`Â in
                interfaceÂ :class:`~cern.japc.core.SubscriptionConfigurator`
        
            Returns:
                the cycle selector on which this request is activated
        
        
        """
        ...
    def isMonitoring(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.SubscriptionHandle.isMonitoring`
            Returns true is this monitorable is currently monitoring the associated parameter
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionHandle.isMonitoring` in interface :class:`~cern.japc.core.SubscriptionHandle`
        
            Returns:
                true is the parameter is currently monitoring the value
        
        
        """
        ...
    def peekValue(self, long: int) -> cern.japc.core.AcquiredParameterValue: ...
    def setDataDeliveryMode(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.SubscriptionConfigurator.setDataDeliveryMode`
            Sets the fetch mode of this handle to :code:`PUSH_MODE` or :code:`PULL_MODE`. Default is :code:`MODE_PUSH_ONLY`.
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionConfigurator.setDataDeliveryMode`Â in
                interfaceÂ :class:`~cern.japc.core.SubscriptionConfigurator`
        
            Parameters:
                mode (int): the data delivery mode either :code:`PUSH_MODE` or :code:`PULL_MODE`
        
        
        """
        ...
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None:
        """
            Stops subscription for all the selectors.
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionHandle.stopMonitoring` in interface :class:`~cern.japc.core.SubscriptionHandle`
        
        
        """
        ...

class ListSelectorResolver(WildcardSelectorResolver):
    """
    public class ListSelectorResolver extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.subscription.WildcardSelectorResolver`
    
        This class resolves a selector containing "|"-separated list of selector names into a list of selectors corresponding to
        the names.
    
        Example: "SPS.USER.CNGS1|SPS.USER.SFTPRO3|SPS.USER.MD2" => "SPS.USER.CNGS1", "SPS.USER.SFTPRO3", "SPS.USER.MD2"
    """
    SELECTOR_SEPARATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SELECTOR_SEPARATOR
    
        A symbol used for separation of selector names.
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def resolve(self, selector: cern.japc.core.Selector) -> typing.List[cern.japc.core.Selector]:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.subscription.WildcardSelectorResolver.resolve`
            This method returns an array of all matching selectors for the given wildcard selector. If no match found the passed
            selector itself returned in an array.
        
            Specified by:
                :meth:`~cern.japc.core.spi.subscription.WildcardSelectorResolver.resolve`Â in
                interfaceÂ :class:`~cern.japc.core.spi.subscription.WildcardSelectorResolver`
        
            Parameters:
                wildcardSelector (:class:`~cern.japc.core.Selector`): wildcard selector
        
            Returns:
                if matches: an array with all matching selectors for the given wildcard selector; if no match: give back the selecotr
                passed as argument itself, in an array.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.subscription")``.

    ListSelectorResolver: typing.Type[ListSelectorResolver]
    SubscriptionFilter: typing.Type[SubscriptionFilter]
    WildcardParameterDecorator: typing.Type[WildcardParameterDecorator]
    WildcardSelectorResolver: typing.Type[WildcardSelectorResolver]
    WildcardSubscriptionHandle: typing.Type[WildcardSubscriptionHandle]
