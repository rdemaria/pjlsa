import cern.japc.core
import cern.japc.core.group
import cern.japc.core.transaction
import cern.japc.value
import java.util
import typing



class AbstractGroupSubscriptionHandle(cern.japc.core.group.GroupSubscriptionHandle):
    """
    public abstract class AbstractGroupSubscriptionHandle extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.group.GroupSubscriptionHandle`
    
        An abstract subscription handle for group subscriptions.
    
        This class is not thread-safe.
    """
    def __init__(self, immutableParameterGroup: cern.japc.core.group.ImmutableParameterGroup, selector: cern.japc.core.Selector, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, abstractGroupParameterValueListenerAdapter: 'AbstractGroupParameterValueListenerAdapter'): ...
    def getDataDeliveryMode(self) -> int:
        """
            Returns the data delivery mode.
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionConfigurator.getDataDeliveryMode`Â in
                interfaceÂ :class:`~cern.japc.core.SubscriptionConfigurator`
        
            Returns:
                the dataDeliveryMode
        
        
        """
        ...
    def getImmediateUpdateListener(self) -> cern.japc.core.ParameterValueListener:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.GroupSubscriptionHandle.getImmediateUpdateListener`
            Returns the registered listener for immediate update. This listener can received all value received by this group
            subscription.
        
            Specified by:
                :meth:`~cern.japc.core.group.GroupSubscriptionHandle.getImmediateUpdateListener`Â in
                interfaceÂ :class:`~cern.japc.core.group.GroupSubscriptionHandle`
        
            Returns:
                the registered listener for immediate update or null if no listener has been registered for that.
        
        
        """
        ...
    def getListener(self) -> cern.japc.core.group.FailSafeParameterValueListener:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.GroupSubscriptionHandle.getListener`
            Returns the registered listener or null if no listener has been registered.
        
            Specified by:
                :meth:`~cern.japc.core.group.GroupSubscriptionHandle.getListener`Â in
                interfaceÂ :class:`~cern.japc.core.group.GroupSubscriptionHandle`
        
            Returns:
                the registered listener or null if no listener has been registered.
        
        
        """
        ...
    def getParameterGroup(self) -> cern.japc.core.group.ImmutableParameterGroup:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.GroupSubscriptionHandle.getParameterGroup`
            Returns the parameter group for which this handle has been created
        
            Specified by:
                :meth:`~cern.japc.core.group.GroupSubscriptionHandle.getParameterGroup`Â in
                interfaceÂ :class:`~cern.japc.core.group.GroupSubscriptionHandle`
        
            Returns:
                the parameter group for which this handle has been created
        
        
        """
        ...
    def getSelector(self) -> cern.japc.core.Selector:
        """
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
            Description copied from interface: :meth:`~cern.japc.core.group.GroupSubscriptionHandle.isMonitoring`
            Returns true if this monitorable is currently monitoring the associated parameter
        
            Specified by:
                :meth:`~cern.japc.core.group.GroupSubscriptionHandle.isMonitoring`Â in
                interfaceÂ :class:`~cern.japc.core.group.GroupSubscriptionHandle`
        
            Returns:
                true if the parameter is currently monitoring the value
        
        
        """
        ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.GroupSubscriptionHandle.peekValues`
            Returns the values received for the given cycleId. If the given cycleId is 0 or less, the values for the last cycle Id
            received are returned. If the cycle Id is greater than 0, the values matching that cycle id are returned. If no values
            have been received for that cycle id, null is returned. The array returned is guaranteed to be either null or of same
            length as the number of parameters in the group.
        
            Specified by:
                :meth:`~cern.japc.core.group.GroupSubscriptionHandle.peekValues`Â in
                interfaceÂ :class:`~cern.japc.core.group.GroupSubscriptionHandle`
        
            Parameters:
                cycleId (long): the cycle id to retrieve or 0 to get the last one
        
            Returns:
                the matching group of value or null if no match.
        
        
        """
        ...
    def registerImmediateUpdateListener(self, parameterValueListener: cern.japc.core.ParameterValueListener) -> None:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.group.GroupSubscriptionHandle.registerImmediateUpdateListener`
            Registers the listener for immediate update. This listener receives all value received by this group subscription as
            they come.
        
            Specified by:
                :meth:`~cern.japc.core.group.GroupSubscriptionHandle.registerImmediateUpdateListener`Â in
                interfaceÂ :class:`~cern.japc.core.group.GroupSubscriptionHandle`
        
            Parameters:
                iuListener (:class:`~cern.japc.core.ParameterValueListener`): the listener or null to unregister the current listener.
        
        
        """
        ...
    def setDataDeliveryMode(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.SubscriptionConfigurator.setDataDeliveryMode`
            Sets the fetch mode of this handle to :code:`PUSH_MODE` or :code:`PULL_MODE`. Default is :code:`MODE_PUSH_ONLY`.
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionConfigurator.setDataDeliveryMode`Â in
                interfaceÂ :class:`~cern.japc.core.SubscriptionConfigurator`
        
            Parameters:
                dataDeliveryMode (int): The dataDeliveryMode to set.
        
        
        """
        ...
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.GroupSubscriptionHandle.stopMonitoring`
            Stops monitoring on this subscription request if it is not already stopped.
        
            Specified by:
                :meth:`~cern.japc.core.group.GroupSubscriptionHandle.stopMonitoring`Â in
                interfaceÂ :class:`~cern.japc.core.group.GroupSubscriptionHandle`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class BasicParameterGroupImpl(cern.japc.core.group.BasicParameterGroup):
    """
    public abstract class BasicParameterGroupImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.group.BasicParameterGroup`
    
        :class:`~cern.japc.core.group.BasicParameterGroup` implementation providing the service needed to group parameters.
    
        The implementation is not thread safe!
    """
    def add(self, parameter: cern.japc.core.Parameter) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.add`
            Adds the given parameter to this group. The parameter is added after the parameters already present in this group. The
            parameter is added whether or not it is already present in this group.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.add` in interface :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Parameters:
                parameter (:class:`~cern.japc.core.Parameter`): the non null parameter to add to this group
        
        
        """
        ...
    def addAll(self, parameterArray: typing.List[cern.japc.core.Parameter]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.addAll`
            Adds the given parameters to this group. The parameters are added to this group in the same order as given in the array.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.addAll`Â in
                interfaceÂ :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Parameters:
                parameters (:class:`~cern.japc.core.Parameter`[]): the non null parameters to add to this group
        
        
        """
        ...
    def clear(self) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.clear`
            Removes the all parameters from this group.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.clear` in interface :class:`~cern.japc.core.group.BasicParameterGroup`
        
        
        """
        ...
    @typing.overload
    def get(self, int: int) -> cern.japc.core.Parameter:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.get`
            Returns the parameter of this group at the given position. The position has to be included in [0, size()-1]
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.get` in interface :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Parameters:
                i (int): the index of the parameter to find in the group.
        
            Returns:
                the non null parameter at the given index
        
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.get`
            Returns the parameter of this group whose name match the given name. If no parameter in this group has the given name
            null is returned.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.get` in interface :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to find in this group.
        
            Returns:
                the parameter of given name or null if it is not in the group
        
        
        """
        ...
    @typing.overload
    def get(self, string: str) -> cern.japc.core.Parameter: ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.getName`
            Returns the name that identified this group. The name of the group is optional and can be null.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.getName`Â in
                interfaceÂ :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Returns:
                the name that identified this group. The name of the group is optional and can be null.
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.getNames`
            Returns the names of all parameters in this group. The names are returned in the same order as the parameters in this
            group.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.getNames`Â in
                interfaceÂ :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Returns:
                returns the names of all parameters in this group.
        
        
        """
        ...
    def getParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.getParameterDescriptor`
            Returns the descriptor of the parameter of given name in the group. If the parameter of given name is not member of the
            group null is returned.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.getParameterDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter in the group
        
            Returns:
                the descriptor of the parameter of given name in the group.
        
        
        """
        ...
    def getParameters(self) -> typing.List[cern.japc.core.Parameter]:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.getParameters`
            Returns all parameters in this group. The parameters are returned in the same order as they are in this group.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.getParameters`Â in
                interfaceÂ :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Returns:
                returns all parameters in this group.
        
        
        """
        ...
    def getValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.getValueDescriptor`
            Returns the value descriptor of the parameter of given name in the group. If the parameter of given name is not member
            of the group null is returned.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.getValueDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter in the group
        
            Returns:
                the value descriptor of the parameter of given name in the group.
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.isEmpty`
            Returns true if this group does not contain any parameter false else.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.isEmpty`Â in
                interfaceÂ :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Returns:
                true if this group does not contain any parameter false else.
        
        
        """
        ...
    def remove(self, parameter: cern.japc.core.Parameter) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.remove`
            Removes the first instance of the given parameter from this group. If the parameter is not found in this group this
            method has no effect.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.remove`Â in
                interfaceÂ :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Parameters:
                parameter (:class:`~cern.japc.core.Parameter`): the non null parameter to remove from this group
        
        
        """
        ...
    def removeAll(self, parameterArray: typing.List[cern.japc.core.Parameter]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.removeAll`
            Removes all the occurrences of the given parameters from this group.
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.removeAll`Â in
                interfaceÂ :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Parameters:
                parameters (:class:`~cern.japc.core.Parameter`[]): the non null parameters to remove from this group
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Setter for the name of a parameter group.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of a parameter group, can be null.
        
        
        """
        ...
    def size(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.BasicParameterGroup.size`
            Returns how many parameters are contained inside of this parameter group
        
            Specified by:
                :meth:`~cern.japc.core.group.BasicParameterGroup.size` in interface :class:`~cern.japc.core.group.BasicParameterGroup`
        
            Returns:
                how many parameters are contained inside of this parameter group
        
        
        """
        ...

class GroupParameterCurrentValue:
    """
    public class GroupParameterCurrentValue extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class keeps the values grouped together for the current grouping cycle.
    
        Grouping cycle can be a real timing cycle, or another abstraction if values are grouped together by some other criteria
        (acqStamp, for example).
    
        Values are coming from different threads, so this class must be thread-safe!!! But of course it can't guarantee the
        thread safety of the logic around it, for example: [check coming value cycleStamp]-then-[act]. So, in this situation
        additional synchronization is needed. Synchronization should be done on the instance of
        :class:`~cern.japc.core.spi.group.GroupParameterCurrentValue`.
    
        So, this class is tread-safe.
    """
    def __init__(self, stringArray: typing.List[str]): ...
    def allValuesPresent(self) -> bool:
        """
            Checks whether the result contains the values for all the parameters.
        
            Returns:
                true if all the values present and false otherwise.
        
        
        """
        ...
    def getParameterIndexes(self, string: str) -> java.util.Collection[int]: ...
    def getReceivedCount(self) -> int:
        """
            Returns the number of parameter values already available for the current grouping cycle.
        
            Returns:
                the number of parameter values already available for the current grouping cycle.
        
        
        """
        ...
    def getValues(self) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Returns a copy of current result array.
        
            Returns:
                a copy of current result array.
        
        
        """
        ...
    def isFree(self, string: str) -> bool:
        """
            Checks whether the value for a parameter has not been already received.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of a parameter in the group
        
            Returns:
                true if the value for a parameter has not been received yet for current grouping cycle (real timing cycle, for example)
                and false otherwise.
        
        
        """
        ...
    def receiveResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None:
        """
            Receives and processes the value coming from a parameter.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                failSafeValue (:class:`~cern.japc.core.FailSafeParameterValue`): coming parameter value
        
        
        """
        ...
    def reset(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue], booleanArray: typing.List[bool]) -> None:
        """
            Resets the state of the result.
        
            Parameters:
                resetValues (:class:`~cern.japc.core.FailSafeParameterValue`[]): the values which should be immediately put into result. The length and order must correspond to the length and the order
                    of parameter names. :code:`null` is treated as no reset values. For example, there is a permanent subscription problem,
                    so we should immediately put an exception into result. Subscription problem is permanent if the exception occurred
                    during starting monitoring. Or the parameter is "constant" (information coming from descriptor). A special case when
                    parameter subscription is "on-change". In this case we also immediately put the value into result, but allow to
                    overwrite it during cycle.
                replacable (boolean[]): just an array of flags saying if the reset values can be replaced during the cycle or not. The length and order must
                    correspond to the length and the order of parameter names. :code:`null` is treated as "all the values are replacable".
                    Permanent subscription problems and constant values can't be replaced while values of "on-change" subscriptions can be
                    replaced.
        
        
        """
        ...
    def toString(self) -> str:
        """
            Return a string representation of this object
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this object
        
        
        """
        ...

class GroupParameterUtil:
    """
    public class GroupParameterUtil extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Class containing constants and common functionality for all the classes participating in collecting and grouping values
        of parameters of a :class:`~cern.japc.core.group.ParameterGroup`.
    """
    def __init__(self): ...
    @staticmethod
    def readCycleStamp(failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> int:
        """
            Helper method which tries to read the cycle stamp of a value and returns 0 if the cycle stamp is not available by some
            reason
        
            Parameters:
                failSafeValue (:class:`~cern.japc.core.FailSafeParameterValue`): value to analyze
        
            Returns:
                the cycle stamp of the value or 0
        
        
        """
        ...
    @staticmethod
    def readFirstUpdateFlag(failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> bool:
        """
            Helper method which tries to read the first update of a value and returns :code:`null` if the flag is not available by
            some reason (for example, new value is exception)
        
            Parameters:
                failSafeValue (:class:`~cern.japc.core.FailSafeParameterValue`): value to analyze
        
            Returns:
                true if it is first update, false if not and null is it is impossible to define
        
        
        """
        ...

class GroupParameterValueListenerAdapter:
    """
    public interface GroupParameterValueListenerAdapter
    
        Interface describing a class implementing the infrastructure between client and subscription strategies while
        subscribing to parameter groups.
    """
    def getImmediateUpdateListener(self) -> cern.japc.core.ParameterValueListener:
        """
            Returns the registered listener for immediate update. This listener can received all value received by this group
            subscription.
        
            Returns:
                the registered listener for immediate update or null if no listener has been registered for that.
        
        
        """
        ...
    def getLastValue(self, int: int) -> cern.japc.core.FailSafeParameterValue:
        """
            Returns the last value received for a parameter identified with its index.
        
            Parameters:
                index (int): the parameter index
        
            Returns:
                the last value received for a parameter identified with its index.
        
        
        """
        ...
    def getParameterNames(self) -> typing.List[str]:
        """
            Getter for parameter names.
        
            Returns:
                parameter names
        
        
        """
        ...
    def getSubscriptionProblem(self, int: int) -> cern.japc.core.ParameterException:
        """
            Returns a subscription problem for a parameter or :code:`null` if this parameter has started monitoring successfully
        
            Parameters:
                index (int): parameter index
        
            Returns:
                a subscription problem for a parameter or :code:`null` if this parameter has started monitoring successfully
        
        
        """
        ...
    def isConstantParameter(self, int: int) -> bool:
        """
            Check whether a parameter identified by its index has constant values.
        
            Parameters:
                index (int): parameter index
        
            Returns:
                true if a parameter identified by its index has constant values and false otherwise
        
        
        """
        ...
    def isOnChangeParameter(self, int: int) -> bool:
        """
            Check whether a parameter identified by its index has "on-change" subscription.
        
            Parameters:
                index (int): parameter index
        
            Returns:
                true if a parameter identified by its index has "on-change" subscription and false otherwise
        
        
        """
        ...
    def peekValue(self, int: int, long: int) -> cern.japc.core.AcquiredParameterValue: ...
    def sendImmediateUpdate(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None:
        """
            Sends an immediate update coming from a parameter to the client immediate update listener.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                value (:class:`~cern.japc.core.FailSafeParameterValue`): the value of immediate update
        
        
        """
        ...
    def sendUpdate(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> None:
        """
            Sends a collected and grouped update to the client listener.
        
            Parameters:
                values (:class:`~cern.japc.core.FailSafeParameterValue`[]): collected and grouped values
        
        
        """
        ...

class GroupSubscriptionStrategy:
    """
    public interface GroupSubscriptionStrategy
    
        Interface defining a strategy for collecting, grouping and sending to the client listener the values of parameters in
        the group.
    """
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Peeks the values of parameters in the group for a given cycle stamp.
        
            Parameters:
                cycleStamp (long): cycle stamp
        
            Returns:
                the parameter values available for requested cycle stamp.
        
        
        """
        ...
    def updateResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None:
        """
            Receives the value of a parameter of a group.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                failSafeValue (:class:`~cern.japc.core.FailSafeParameterValue`): parameter value
        
        
        """
        ...

class GroupSubscriptionStrategyFactory:
    """
    public interface GroupSubscriptionStrategyFactory
    
        Interface for a factory to produce grouping strategies for parameter groups subscriptions.
    """
    def getAsyncGetSetStrategy(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter, parameterArray: typing.List[cern.japc.core.Parameter]) -> GroupSubscriptionStrategy:
        """
            The factory method to produce a grouping strategy for a parameter group asynchronous GET.
        
            Parameters:
                gpvla (:class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`): infrastructure class for parameter group subscription
                groupedParameters (:class:`~cern.japc.core.Parameter`[]): the parameters of the group
        
            Returns:
                the grouping strategy for asynchronous SET (if null is returned then the default strategy will be used:
                :class:`~cern.japc.core.spi.group.PushGroupSubscriptionStrategy` without any timeout)
        
        
        """
        ...
    def getSubscriptionStrategy(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter, parameterArray: typing.List[cern.japc.core.Parameter], selector: cern.japc.core.Selector) -> GroupSubscriptionStrategy:
        """
            The factory method to produce a grouping strategy for a parameter group subscription.
        
            Parameters:
                gpvla (:class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`): infrastructure class for parameter group subscription
                groupedParameters (:class:`~cern.japc.core.Parameter`[]): the parameters of the group
                selector (:class:`~cern.japc.core.Selector`): the selector for the subscription
        
            Returns:
                the grouping strategy for subscription (if null is returned then the default strategy will be used:
                :class:`~cern.japc.core.spi.group.PushGroupSubscriptionStrategy` without any timeout)
        
        
        """
        ...

class AbstractGroupParameterValueListenerAdapter(cern.japc.core.ParameterValueListener, GroupParameterValueListenerAdapter):
    """
    public abstract class AbstractGroupParameterValueListenerAdapter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ParameterValueListener`, :class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`
    
        Basic abstract class for an adapter between the listener of a group that expect an array of values, and the listener of
        a given parameter that expect a single value. This adapter is given to each one parameter of the group and receives
        values from all those parameters. The values are grouped together into one array that is sent at once to the group
        listener.
    
        This adapter has two mode for data delivery. In PUSH mode, data are sent to the listener as soon as they are ready.
    
        In PULL mode, data are never sent but the client has to call peekValues() to fetch the data that are ready.
    
        Implementations should take care about the case with duplicated parameters. The contract is that since when an update
        from a parameter arrives we don't have any information about index of that parameter in the parameter array the logic of
        this class and grouping strategies always distribute the update to all parameter occurrences. That means that the
        implementations should filter out duplicates and not subscribe twice to the same parameter.
    
        Apart from the parameter group subscription this class is also used for asynchronous GET/SET operations.
    
        This class is not thread-safe from client point of view, so all the client actions must be properly synchronized.
    """
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`
            Notifies this listener that a problem occurred preventing the get/set to be done.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def getDataDeliveryMode(self) -> int:
        """
            Returns the data delivery mode.
        
            Returns:
                the dataDeliveryMode
        
        
        """
        ...
    def getImmediateUpdateListener(self) -> cern.japc.core.ParameterValueListener:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.getImmediateUpdateListener`
            Returns the registered listener for immediate update. This listener can received all value received by this group
            subscription.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.getImmediateUpdateListener`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`
        
            Returns:
                the registered listener for immediate update or null if no listener has been registered for that.
        
        
        """
        ...
    def getLastValue(self, int: int) -> cern.japc.core.FailSafeParameterValue:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.getLastValue`
            Returns the last value received for a parameter identified with its index.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.getLastValue`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`
        
            Parameters:
                index (int): the parameter index
        
            Returns:
                the last value received for a parameter identified with its index.
        
        
        """
        ...
    def getParameterNames(self) -> typing.List[str]:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.getParameterNames`
            Getter for parameter names.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.getParameterNames`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`
        
            Returns:
                parameter names
        
        
        """
        ...
    def getSubscriptionProblem(self, int: int) -> cern.japc.core.ParameterException:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.getSubscriptionProblem`
            Returns a subscription problem for a parameter or :code:`null` if this parameter has started monitoring successfully
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.getSubscriptionProblem`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`
        
            Parameters:
                index (int): parameter index
        
            Returns:
                a subscription problem for a parameter or :code:`null` if this parameter has started monitoring successfully
        
        
        """
        ...
    def isConstantParameter(self, int: int) -> bool:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.isConstantParameter`
            Check whether a parameter identified by its index has constant values.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.isConstantParameter`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`
        
            Parameters:
                index (int): parameter index
        
            Returns:
                true if a parameter identified by its index has constant values and false otherwise
        
        
        """
        ...
    def isMonitoring(self) -> bool:
        """
            Returns true if this adapter is currently monitoring the associated parameter group
        
            Returns:
                true if this adapter is currently monitoring the associated parameter group
        
        
        """
        ...
    def isOnChangeParameter(self, int: int) -> bool:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.isOnChangeParameter`
            Check whether a parameter identified by its index has "on-change" subscription.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.isOnChangeParameter`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`
        
            Parameters:
                index (int): parameter index
        
            Returns:
                true if a parameter identified by its index has "on-change" subscription and false otherwise
        
        
        """
        ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Returns the values belonging to requested cycle stamp if current subscription strategy supports this.
        
            Zero or negative cycle stamp means "return the values for the last received cycle stamp". Read java doc for
            :meth:`~cern.japc.core.group.GroupSubscriptionHandle.peekValues`.
        
            Parameters:
                cycleStamp (long): cycle stamp
        
            Returns:
                the values belonging to requested cycle defined by cycle stamp.
        
        
        """
        ...
    def registerImmediateUpdateListener(self, parameterValueListener: cern.japc.core.ParameterValueListener) -> None:
        """
            Registers the listener for immediate update. This listener receives all value received by this group subscription as
            they come.
        
            Parameters:
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener or null to unregister the current listener.
        
        
        """
        ...
    def sendImmediateUpdate(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.sendImmediateUpdate`
            Sends an immediate update coming from a parameter to the client immediate update listener.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.sendImmediateUpdate`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                value (:class:`~cern.japc.core.FailSafeParameterValue`): the value of immediate update
        
        
        """
        ...
    def sendUpdate(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.sendUpdate`
            Sends a collected and grouped update to the client listener.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter.sendUpdate`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`
        
            Parameters:
                values (:class:`~cern.japc.core.FailSafeParameterValue`[]): collected and grouped values
        
        
        """
        ...
    def setDataDeliveryMode(self, int: int) -> None:
        """
            Sets the data delivery mode (see :class:`~cern.japc.core.SubscriptionConfigurator`).
        
            This method also switches the grouping strategy to :class:`~cern.japc.core.spi.group.PullGroupSubscriptionStrategy` if
            the requested delivery mode if :meth:`~cern.japc.core.SubscriptionConfigurator.PULL_MODE` or to user defined strategy if
            the requested delivery mode if :meth:`~cern.japc.core.SubscriptionConfigurator.PUSH_MODE`. If there is no user defined
            strategy then :class:`~cern.japc.core.spi.group.PushGroupSubscriptionStrategy` is used.
        
            Parameters:
                dataDeliveryMode (int): requested delivery mode.
        
        
        """
        ...
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None:
        """
            Stops monitoring on all the parameters.
        
        """
        ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.valueReceived`
            Notifies this listener that a new value has been received (get or monitor) or set to the parameter. In the case of the
            notification of the set the value can be null.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.valueReceived`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...

class AbstractGroupSubscriptionStrategy(GroupSubscriptionStrategy):
    """
    public abstract class AbstractGroupSubscriptionStrategy extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategy`
    
        An abstract strategy, parent class for custom strategies.
    """
    def __init__(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter): ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategy.peekValues`
            Peeks the values of parameters in the group for a given cycle stamp.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategy.peekValues`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategy`
        
            Parameters:
                cycleStamp (long): cycle stamp
        
            Returns:
                the parameter values available for requested cycle stamp.
        
        
        """
        ...
    def updateResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None:
        """
            This method processes an update of one of parameters.
        
            To avoid race conditions (updates are coming concurrently) we use synchronization. Sending values are potential long
            operation, so it is kept outside of synchronized block.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategy.updateResult`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategy`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the updated parameter
                failSafeValue (:class:`~cern.japc.core.FailSafeParameterValue`): the value update for the parameter
        
        
        """
        ...

class DefaultGroupSubscriptionStrategyFactory(GroupSubscriptionStrategyFactory):
    """
    public class DefaultGroupSubscriptionStrategyFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategyFactory`
    
        Default implementation of :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategyFactory`.
    
        It returns :class:`~cern.japc.core.spi.group.PushGroupSubscriptionStrategy`'s without timeout.
    """
    def __init__(self): ...
    @staticmethod
    def get() -> 'DefaultGroupSubscriptionStrategyFactory':
        """
            Getter for the singleton.
        
            Returns:
                a singleton of DefaultGroupSubscriptionStrategyFactory
        
        
        """
        ...
    def getAsyncGetSetStrategy(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter, parameterArray: typing.List[cern.japc.core.Parameter]) -> GroupSubscriptionStrategy:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategyFactory.getAsyncGetSetStrategy`
            The factory method to produce a grouping strategy for a parameter group asynchronous GET.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategyFactory.getAsyncGetSetStrategy`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategyFactory`
        
            Parameters:
                gpvla (:class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`): infrastructure class for parameter group subscription
                groupedParameters (:class:`~cern.japc.core.Parameter`[]): the parameters of the group
        
            Returns:
                the grouping strategy for asynchronous SET (if null is returned then the default strategy will be used:
                :class:`~cern.japc.core.spi.group.PushGroupSubscriptionStrategy` without any timeout)
        
        
        """
        ...
    def getSubscriptionStrategy(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter, parameterArray: typing.List[cern.japc.core.Parameter], selector: cern.japc.core.Selector) -> GroupSubscriptionStrategy:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategyFactory.getSubscriptionStrategy`
            The factory method to produce a grouping strategy for a parameter group subscription.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategyFactory.getSubscriptionStrategy`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategyFactory`
        
            Parameters:
                gpvla (:class:`~cern.japc.core.spi.group.GroupParameterValueListenerAdapter`): infrastructure class for parameter group subscription
                groupedParameters (:class:`~cern.japc.core.Parameter`[]): the parameters of the group
                selector (:class:`~cern.japc.core.Selector`): the selector for the subscription
        
            Returns:
                the grouping strategy for subscription (if null is returned then the default strategy will be used:
                :class:`~cern.japc.core.spi.group.PushGroupSubscriptionStrategy` without any timeout)
        
        
        """
        ...

class GPCSCurrentValue(GroupParameterCurrentValue):
    def __init__(self, stringArray: typing.List[str]): ...
    def compareCycleStamps(self, long: int) -> int: ...
    def compareCycleStampsAndFlags(self, long: int, boolean: bool) -> int: ...
    def getCycleStamp(self) -> int: ...
    def getFirstUpdateFlag(self) -> bool: ...
    def receiveResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None: ...
    def reset(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue], booleanArray: typing.List[bool]) -> None: ...

class GroupSubscriptionHandleImpl(AbstractGroupSubscriptionHandle):
    """
    public class GroupSubscriptionHandleImpl extends :class:`~cern.japc.core.spi.group.AbstractGroupSubscriptionHandle`
    
        Default GroupSubscriptionHandle implementation.
    """
    def __init__(self, immutableParameterGroup: cern.japc.core.group.ImmutableParameterGroup, selector: cern.japc.core.Selector, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.japc.core.spi.group.AbstractGroupSubscriptionHandle.toString`Â in
                classÂ :class:`~cern.japc.core.spi.group.AbstractGroupSubscriptionHandle`
        
        
        """
        ...

class ImmutableParameterGroupImpl(BasicParameterGroupImpl, cern.japc.core.group.ImmutableParameterGroup):
    """
    public class ImmutableParameterGroupImpl extends :class:`~cern.japc.core.spi.group.BasicParameterGroupImpl` implements :class:`~cern.japc.core.group.ImmutableParameterGroup`
    
        Default implementation of :class:`~cern.japc.core.group.ImmutableParameterGroup`.
    
        This group has 2 modes of working. In **normal/traditional** mode the group works with parameters individually packing
        the data together afterwards:
    
          - **GET**: the GET call is done one parameter after another. The results are returned all together as an array of
            :class:`~cern.japc.core.FailSafeParameterValue`
          - **ASYNC GET**: the ASYNC GET call is done one parameter after another. In fact the duplicated parameters are ignored,
            since each individual update is distributed over all the duplicates. The results are returned all together as an array
            of :class:`~cern.japc.core.FailSafeParameterValue`
          - **MONITOR**: the START MONITORING call is done one parameter after another. In fact the duplicated parameters are
            ignored, since each individual update is distributed over all the duplicates. The results are coming one by one and are
            packed together by some criteria (usually, cycleStamp) and are sent as an array of
            :class:`~cern.japc.core.FailSafeParameterValue` for each update. STOP MONITORING is also done one parameter after
            another ignoring the duplicates.
    
        In **array-call** mode the group assumes that all the parameters are served by an implementation of
        :class:`~cern.japc.core.spi.arraycall.ParameterArrayCaller`. Collaboration with a
        :class:`~cern.japc.core.spi.arraycall.ParameterArrayCaller` puts some requirements on the group behavior: the main
        difference from traditional behavior is that :class:`~cern.japc.core.spi.arraycall.ParameterArrayCaller` requires each
        parameter to make a request (GET/SET/MONITOR) in order to perform a real RDA call. That means that the group CAN NOT
        ignore duplicated parameters but should filter out the duplicated updates coming because of several started subscription
        for duplicated parameters. See :class:`~cern.japc.core.spi.arraycall.group.ArrayCallGroupParameterValueListenerAdapter`.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    def createSubscription(self, selector: cern.japc.core.Selector, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener) -> cern.japc.core.group.GroupSubscriptionHandle:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.ImmutableParameterGroup.createSubscription`
            Creates a private subscription for a given listener and on an given cycle selector. Using the subscription handler
            returned it is possible to start and stop monitoring this parameter on the given cycle selector. The handler returned
            must not be shared or accessed concurrently. In addition it is necessary to keep a strong reference on the handler
            returned as long as it useful. Not doing so exposes the returned handler to garbage collection and would potentially
            automatically stop the subscription for the given listener.
        
            Specified by:
                :meth:`~cern.japc.core.group.ImmutableParameterGroup.createSubscription`Â in
                interfaceÂ :class:`~cern.japc.core.group.ImmutableParameterGroup`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the cycle selector on which to monitor the parameter
                listener (:class:`~cern.japc.core.group.FailSafeParameterValueListener`): the listener that will received the notification for that request.
        
            Returns:
                the subscription request that can be used to monitor this parameter.
        
        
        """
        ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.ImmutableParameterGroup.getValue`
            Reads synchronously the values of the parameters of this group for the given selector. This method returns the values of
            all parameters in the group. This method is synchronous and blocks until the values are read or until problems occur.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.group.ImmutableParameterGroup.getValue`Â in
                interfaceÂ :class:`~cern.japc.core.group.ImmutableParameterGroup`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
        
            Returns:
                the non null array of values for the parameters of this group and for the given cycle. The number of value is guaranted
                to be the same as the number of parameter in the group and the order of the value in the array is the same as the order
                of the parameters in the group.
        
            Description copied from interface: :meth:`~cern.japc.core.group.ImmutableParameterGroup.getValue`
            Reads asynchronously the values of the parameters of this group for the given selector. The provider listener is
            notified of the value read or if a problem occurs.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.group.ImmutableParameterGroup.getValue`Â in
                interfaceÂ :class:`~cern.japc.core.group.ImmutableParameterGroup`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
                listener (:class:`~cern.japc.core.group.FailSafeParameterValueListener`): the listener to notify when the value is read or when a problem occurs
        
        
        """
        ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener) -> None: ...
    def isArrayCallMode(self) -> bool:
        """
            Checks whether the group is in "array-call" mode, that means the start monitoring request is performed even for
            duplicated parameters.
        
            Returns:
                true if the group is in "array-call" mode
        
        
        """
        ...
    def setArrayCallMode(self, boolean: bool) -> None:
        """
            Setter for the "array-call" mode of the parameter group.
        
            Parameters:
                arrayCallMode (boolean): true to set "array-call" behavior and false to use normal (old) behavior.
        
        
        """
        ...

class PullGroupSubscriptionStrategy(GroupSubscriptionStrategy):
    """
    public class PullGroupSubscriptionStrategy extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategy`
    
        A strategy implementing pull-mode subscription.
    """
    def __init__(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter): ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategy.peekValues`
            Peeks the values of parameters in the group for a given cycle stamp.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategy.peekValues`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategy`
        
            Parameters:
                cycleStamp (long): cycle stamp
        
            Returns:
                the parameter values available for requested cycle stamp.
        
        
        """
        ...
    def updateResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategy.updateResult`
            Receives the value of a parameter of a group.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategy.updateResult`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategy`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                failSafeValue (:class:`~cern.japc.core.FailSafeParameterValue`): parameter value
        
        
        """
        ...

class PushGroupSubscriptionStrategy(GroupSubscriptionStrategy):
    """
    public class PushGroupSubscriptionStrategy extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategy`
    
        A strategy implementing push-mode subscription.
    
        In default mode this strategy waits the updates from all the parameters to come and then sends the complete set of
        updates to the client. If an update from a newer cycle came while the current set of updates is incomplete then the set
        is completed with previous values/exceptions (in case of non-PPM parameters) or with
        :class:`~cern.japc.core.NoValueException`'s (in case of PPM parameters).
    
        It is possible to enable a timeout to wait for the set of updates to be complete. The timeout starts counting from the
        moment the first (not on-change) update of the set has arrived. If all the values arrived before the timeout has expired
        then the complete set is sent to the client. So, behavior is like in normal case. If some updates are still missing they
        are set to previous values/exceptions (in case of non-PPM parameters) or with
        :class:`~cern.japc.core.NoValueException`'s (in case of PPM parameters). So, the behavior is like values from the newer
        cycle started to arrive.
    
        **WARN 1:** care should be taken to correctly behave in the following cases:
    
          - a PPM update came after timeout (should be ignored)
          - the timeout expires at "the same moment" with the update coming (proper synchronization)
    
    
        **WARN2:** clients should be careful enabling the timeout feature for non-PPM parameters, since in this case there is a
        notion of cycle and therefore it is impossible to relate an update to a particular set of updates.
    
        **WARN3:** even for a PPM property there is no guarantee that the first update will be marked with cycle stamp. Both
        implementations exist and there is no standard there. So the first update should be always considered to be earlier than
        any regular update.
    """
    NO_TIMEOUT: typing.ClassVar[int] = ...
    """
    public static final long NO_TIMEOUT
    
        A constant to use to disable timeout functionality of the strategy
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, groupParameterValueListenerAdapter: GroupParameterValueListenerAdapter): ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategy.peekValues`
            Peeks the values of parameters in the group for a given cycle stamp.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategy.peekValues`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategy`
        
            Parameters:
                cycleStamp (long): cycle stamp
        
            Returns:
                the parameter values available for requested cycle stamp.
        
        
        """
        ...
    def setTimeout(self, long: int) -> None:
        """
            Setter for the timeout.
        
            Setting a positive value enables the feature of a timeout while waiting for the set of parameter updates to be complete.
        
            Parameters:
                timeout (long): 
        
        """
        ...
    def updateResult(self, string: str, failSafeParameterValue: cern.japc.core.FailSafeParameterValue) -> None:
        """
            This method processes an update of one of parameters. Different situations are possible:
        
              1.  Update has 0 as cycleStamp or it is an exception. In this case if the update of this parameter already presents the
                current result (state of values) is sent to the client, and the new update is put into the
                :class:`~cern.japc.core.spi.group.GroupParameterCurrentValue` afterwards. If the update for this parameter doesn't
                present yet the update is just put into the :class:`~cern.japc.core.spi.group.GroupParameterCurrentValue`.
              2.  Update has non-zero cycleStamp. In this case:
        
                  1.  if the cycleStamp matches the cycleStamp of the current result the behavior is like in previous paragraph. NB: getting
                    twice the same non-zero cycleStamp is strange and means some problems.
                  2.  if the cycleStamp is greater than the cycleStamp of the current result the current result is sent to the client and the
                    update is put into the (@link Result) afterwards.
                  3.  if the cycleStamp is less than the cycleStamp of the current result it means that the update came really late -
                    discarding.
        
        
            To avoid race conditions (updates are coming concurrently) we use synchronization. Sending values are potential long
            operation, so it is kept outside of synchronized block.
        
            Specified by:
                :meth:`~cern.japc.core.spi.group.GroupSubscriptionStrategy.updateResult`Â in
                interfaceÂ :class:`~cern.japc.core.spi.group.GroupSubscriptionStrategy`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the updated parameter
                failSafeValue (:class:`~cern.japc.core.FailSafeParameterValue`): the value update for the parameter
        
        
        """
        ...

class GroupParameterValueListenerAdapterImpl(AbstractGroupParameterValueListenerAdapter):
    @typing.overload
    def __init__(self, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, parameterArray: typing.List[cern.japc.core.Parameter], selector: cern.japc.core.Selector, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    @typing.overload
    def __init__(self, failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener, parameterArray: typing.List[cern.japc.core.Parameter], groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    def peekValue(self, int: int, long: int) -> cern.japc.core.AcquiredParameterValue: ...
    def setDataDeliveryModeImpl(self, int: int) -> None: ...

class ParameterGroupImpl(ImmutableParameterGroupImpl, cern.japc.core.group.ParameterGroup):
    """
    public class ParameterGroupImpl extends :class:`~cern.japc.core.spi.group.ImmutableParameterGroupImpl` implements :class:`~cern.japc.core.group.ParameterGroup`
    
        Default implementation of :class:`~cern.japc.core.group.ParameterGroup`.
    
        This group works with parameters individually packing the data together afterwards if necessary:
    
          - **GET**: the GET call is done one parameter after another. The results are returned all together as an array of
            :class:`~cern.japc.core.FailSafeParameterValue`
          - **ASYNC GET**: the ASYNC GET call is done one parameter after another. The results are returned all together as an array
            of :class:`~cern.japc.core.FailSafeParameterValue`
          - **SET**: the SET call is done one parameter after another. The results are returned all together as an array of
            :class:`~cern.japc.core.FailSafeParameterValue` containing for each parameter either the value-to-set in case of success
            or an exception in case of failure
          - **ASYNC SET**: the ASYNC SET call is done one parameter after another. The results are returned all together as an array
            of :class:`~cern.japc.core.FailSafeParameterValue` containing for each parameter either the value-to-set in case of
            success or an exception in case of failure
          - **MONITOR**: the START MONITOR call is done one parameter after another. The results are packed together by some
            criteria (usually, cycleStamp) and returned all together as an array of :class:`~cern.japc.core.FailSafeParameterValue`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue]) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Description copied from interface: :meth:`~cern.japc.core.group.ParameterGroup.setValue`
            Sets the value of the parameters of this group for a given cycle synchronously.
        
            This method is synchronous and blocks until all parameters are set with the given value.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.group.ParameterGroup.setValue` in interface :class:`~cern.japc.core.group.ParameterGroup`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
                values (cern.japc.value.ParameterValue[]): the value to set for each parameter of the group. The size of the array of values must exactly match the size of this
                    group so that each parameter has one value.
        
            Returns:
                an array of FailSafe values containing the value-to-set in case of success or an exception in case of failure.
        
            Description copied from interface: :meth:`~cern.japc.core.group.ParameterGroup.setValue`
            Sets the value of this parameter for a given cycle asynchronously.
        
            More precisely this method sends the signal to transfer the given value to the parameter holder of this parameter. This
            method is asynchronous and should delegate the actual downloading to another process. When the given value will actually
            be received by the parameter holder is undefined and can be tracked using the given listener.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.group.ParameterGroup.setValue` in interface :class:`~cern.japc.core.group.ParameterGroup`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
                values (cern.japc.value.ParameterValue[]): the values to set for each parameter of this group
                listener (:class:`~cern.japc.core.group.FailSafeParameterValueListener`): the listener for the feedback
        
        
        """
        ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue], failSafeParameterValueListener: cern.japc.core.group.FailSafeParameterValueListener) -> None: ...

class TransactionalParameterGroupImpl(ParameterGroupImpl, cern.japc.core.group.TransactionalParameterGroup):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, groupSubscriptionStrategyFactory: GroupSubscriptionStrategyFactory): ...
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue], compositeTransaction: cern.japc.core.transaction.CompositeTransaction) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.group")``.

    AbstractGroupParameterValueListenerAdapter: typing.Type[AbstractGroupParameterValueListenerAdapter]
    AbstractGroupSubscriptionHandle: typing.Type[AbstractGroupSubscriptionHandle]
    AbstractGroupSubscriptionStrategy: typing.Type[AbstractGroupSubscriptionStrategy]
    BasicParameterGroupImpl: typing.Type[BasicParameterGroupImpl]
    DefaultGroupSubscriptionStrategyFactory: typing.Type[DefaultGroupSubscriptionStrategyFactory]
    GPCSCurrentValue: typing.Type[GPCSCurrentValue]
    GroupParameterCurrentValue: typing.Type[GroupParameterCurrentValue]
    GroupParameterUtil: typing.Type[GroupParameterUtil]
    GroupParameterValueListenerAdapter: typing.Type[GroupParameterValueListenerAdapter]
    GroupParameterValueListenerAdapterImpl: typing.Type[GroupParameterValueListenerAdapterImpl]
    GroupSubscriptionHandleImpl: typing.Type[GroupSubscriptionHandleImpl]
    GroupSubscriptionStrategy: typing.Type[GroupSubscriptionStrategy]
    GroupSubscriptionStrategyFactory: typing.Type[GroupSubscriptionStrategyFactory]
    ImmutableParameterGroupImpl: typing.Type[ImmutableParameterGroupImpl]
    ParameterGroupImpl: typing.Type[ParameterGroupImpl]
    PullGroupSubscriptionStrategy: typing.Type[PullGroupSubscriptionStrategy]
    PushGroupSubscriptionStrategy: typing.Type[PushGroupSubscriptionStrategy]
    TransactionalParameterGroupImpl: typing.Type[TransactionalParameterGroupImpl]
