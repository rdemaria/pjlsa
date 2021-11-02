import cern.japc.core
import cern.japc.core.group.support
import cern.japc.core.transaction
import cern.japc.value
import typing



class BasicParameterGroup:
    """
    public interface BasicParameterGroup
    
        Basic interface for parameter group implementation.
    
        The group guarantees to to keep in the same order of parameters as they have been added to the group. This allows to
        work with parameters in the group using their index. Any array of values received from the group are guaranteed to be in
        the same order as the parameters in the group. Any array of values passed to the group must be in the same order as the
        parameters in the group.
    
        The group can have a same parameter multiple times.
    
        A group of parameters is not thread safe. It needs synchronization to be accessed concurrently.
    """
    def add(self, parameter: cern.japc.core.Parameter) -> None:
        """
            Adds the given parameter to this group. The parameter is added after the parameters already present in this group. The
            parameter is added whether or not it is already present in this group.
        
            Parameters:
                parameter (:class:`~cern.japc.core.Parameter`): the non null parameter to add to this group
        
        
        """
        ...
    def addAll(self, parameterArray: typing.List[cern.japc.core.Parameter]) -> None:
        """
            Adds the given parameters to this group. The parameters are added to this group in the same order as given in the array.
        
            Parameters:
                parameters (:class:`~cern.japc.core.Parameter`[]): the non null parameters to add to this group
        
        
        """
        ...
    def clear(self) -> None:
        """
            Removes the all parameters from this group.
        
        """
        ...
    @typing.overload
    def get(self, int: int) -> cern.japc.core.Parameter:
        """
            Returns the parameter of this group whose name match the given name. If no parameter in this group has the given name
            null is returned.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to find in this group.
        
            Returns:
                the parameter of given name or null if it is not in the group
        
            Returns the parameter of this group at the given position. The position has to be included in [0, size()-1]
        
            Parameters:
                index (int): the index of the parameter to find in the group.
        
            Returns:
                the non null parameter at the given index
        
        
        """
        ...
    @typing.overload
    def get(self, string: str) -> cern.japc.core.Parameter: ...
    def getName(self) -> str:
        """
            Returns the name that identified this group. The name of the group is optional and can be null.
        
            Returns:
                the name that identified this group. The name of the group is optional and can be null.
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
            Returns the names of all parameters in this group. The names are returned in the same order as the parameters in this
            group.
        
            Returns:
                returns the names of all parameters in this group.
        
        
        """
        ...
    def getParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor:
        """
            Returns the descriptor of the parameter of given name in the group. If the parameter of given name is not member of the
            group null is returned.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter in the group
        
            Returns:
                the descriptor of the parameter of given name in the group.
        
        
        """
        ...
    def getParameters(self) -> typing.List[cern.japc.core.Parameter]:
        """
            Returns all parameters in this group. The parameters are returned in the same order as they are in this group.
        
            Returns:
                returns all parameters in this group.
        
        
        """
        ...
    def getValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor:
        """
            Returns the value descriptor of the parameter of given name in the group. If the parameter of given name is not member
            of the group null is returned.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter in the group
        
            Returns:
                the value descriptor of the parameter of given name in the group.
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Returns true if this group does not contain any parameter false else.
        
            Returns:
                true if this group does not contain any parameter false else.
        
        
        """
        ...
    def remove(self, parameter: cern.japc.core.Parameter) -> None:
        """
            Removes the first instance of the given parameter from this group. If the parameter is not found in this group this
            method has no effect.
        
            Parameters:
                parameter (:class:`~cern.japc.core.Parameter`): the non null parameter to remove from this group
        
        
        """
        ...
    def removeAll(self, parameterArray: typing.List[cern.japc.core.Parameter]) -> None:
        """
            Removes all the occurrences of the given parameters from this group.
        
            Parameters:
                parameters (:class:`~cern.japc.core.Parameter`[]): the non null parameters to remove from this group
        
        
        """
        ...
    def size(self) -> int:
        """
            Returns how many parameters are contained inside of this parameter group
        
            Returns:
                how many parameters are contained inside of this parameter group
        
        
        """
        ...

class FailSafeParameterValueListener:
    """
    public interface FailSafeParameterValueListener
    
        Defines a listener of values received on a parameter group.
    """
    def valueReceived(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> None:
        """
            Notifies this listener that the new values have been received.
        
            Parameters:
                values (:class:`~cern.japc.core.FailSafeParameterValue`[]): the new values received for the monitored parameters.
        
        
        """
        ...

class GroupSubscriptionHandle(cern.japc.core.SubscriptionConfigurator):
    """
    public interface GroupSubscriptionHandle extends :class:`~cern.japc.core.SubscriptionConfigurator`
    
        A class implementing this interface represents the SubscriptionHandle aspect of a ParameterGroup.
    
        A GroupSubscriptionHandle implementation is a private channel for a given listener. It must not be shared without proper
        synchronization.
    """
    def getImmediateUpdateListener(self) -> cern.japc.core.ParameterValueListener:
        """
            Returns the registered listener for immediate update. This listener can received all value received by this group
            subscription.
        
            Returns:
                the registered listener for immediate update or null if no listener has been registered for that.
        
        
        """
        ...
    def getListener(self) -> FailSafeParameterValueListener:
        """
            Returns the registered listener or null if no listener has been registered.
        
            Returns:
                the registered listener or null if no listener has been registered.
        
        
        """
        ...
    def getParameterGroup(self) -> 'ImmutableParameterGroup':
        """
            Returns the parameter group for which this handle has been created
        
            Returns:
                the parameter group for which this handle has been created
        
        
        """
        ...
    def isMonitoring(self) -> bool:
        """
            Returns true if this monitorable is currently monitoring the associated parameter
        
            Returns:
                true if the parameter is currently monitoring the value
        
        
        """
        ...
    def peekValues(self, long: int) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Returns the values received for the given cycleId. If the given cycleId is 0 or less, the values for the last cycle Id
            received are returned. If the cycle Id is greater than 0, the values matching that cycle id are returned. If no values
            have been received for that cycle id, null is returned. The array returned is guaranteed to be either null or of same
            length as the number of parameters in the group.
        
            Parameters:
                cycleId (long): the cycle id to retrieve or 0 to get the last one
        
            Returns:
                the matching group of value or null if no match.
        
        
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
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None:
        """
            Stops monitoring on this subscription request if it is not already stopped.
        
        """
        ...

class ParameterFieldNames:
    """
    public class ParameterFieldNames extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class contains a parameter name of a composite property (e.g. BTVI10/Setting) and the array of field names (e.g.
        gain, position, ...). Used to pass this information from and to methods.
    """
    def __init__(self, string: str, stringArray: typing.List[str]): ...
    @staticmethod
    def concatParameterFieldNames(parameterFieldNamesArray: typing.List['ParameterFieldNames']) -> typing.List[str]:
        """
            Returns a concatenation of all field parameterNames (e.g. BTVI10/Acquisition#count) contained in the ParameterFieldNames
            array
        
            For example, concatenating the following two ProprtyFieldNames, yields the array with all full parameterNames:
        
            .. code-block: java
            
             propertyFieldName1 = { "Dev_A/prop1" [ "field1", "field2", "field3" ] };
             propertyFieldName2 = { "Dev_B/prop1" [ "field1", "field2" ] }; 
             
             => [ "Dev_A/prop1#field1", "Dev_A/prop1#field2", "Dev_A/prop1#field3", "Dev_B/prop1#field1", "Dev_B/prop1#field2" ]
             
        
            Parameters:
                pfn (:class:`~cern.japc.core.group.ParameterFieldNames`[]): the array to be converted
        
            Returns:
                an array of Strings with field parameterNames
        
        
        """
        ...
    def getFieldNames(self) -> typing.List[str]:
        """
            Returns an array of field names.
        
            The array should not be modified by external code!
        
        
            Returns:
                an array of field names
        
        
        """
        ...
    def getFullParameterNames(self) -> typing.List[str]:
        """
            Returns an array of full parameter names (device/property#field).
        
            Returns:
                an array of full parameter names
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
            Returns the composite parameter name (device/property).
        
        
            Returns:
                the composite parameter name
        
        
        """
        ...

class ParameterGroupValueReceivedAdapter:
    """
    public interface ParameterGroupValueReceivedAdapter
    
        This interface defines a method to adapt values received from a group of parameter to an value that can be received from
        a regular parameter. This is useful to implement a parameter based on a group of parameters.
    """
    def adaptValueReceived(self, failSafeParameterValueArray: typing.List[cern.japc.core.FailSafeParameterValue]) -> cern.japc.core.AcquiredParameterValue: ...

class ParameterGroupValueSentAdapter:
    """
    public interface ParameterGroupValueSentAdapter
    
        This interface defines a method to adapt a ParameterValue sent to a parameter that is made of a group of parameters. It
        only takes care of the adaptation for sending value. This is useful when a parameter is made of a group of parameters
        and that one need to adapt the value sent to create a value for each parameter of the group.
    """
    def adaptValueSent(self, parameterValue: cern.japc.value.ParameterValue) -> typing.List[cern.japc.value.ParameterValue]: ...

class ImmutableParameterGroup(BasicParameterGroup):
    """
    public interface ImmutableParameterGroup extends :class:`~cern.japc.core.group.BasicParameterGroup`
    
        A class implementing this interface represents a group of immutable parameters.
    
        So, it can read and monitor the parameters.
    
        The group guarantees to to keep in the same order of parameters as they have been added to the group. This allows to
        work with parameters in the group using their index. Any array of values received from the group are guaranteed to be in
        the same order as the parameters in the group. Any array of values passed to the group must be in the same order as the
        parameters in the group.
    
        The group can have a same parameter multiple times.
    
        A group of parameters is not thread safe. It needs synchronization to be accessed concurrently.
    """
    def createSubscription(self, selector: cern.japc.core.Selector, failSafeParameterValueListener: FailSafeParameterValueListener) -> GroupSubscriptionHandle:
        """
            Creates a private subscription for a given listener and on an given cycle selector. Using the subscription handler
            returned it is possible to start and stop monitoring this parameter on the given cycle selector. The handler returned
            must not be shared or accessed concurrently. In addition it is necessary to keep a strong reference on the handler
            returned as long as it useful. Not doing so exposes the returned handler to garbage collection and would potentially
            automatically stop the subscription for the given listener.
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the cycle selector on which to monitor the parameter
                listener (:class:`~cern.japc.core.group.FailSafeParameterValueListener`): the listener that will received the notification for that request.
        
            Returns:
                the subscription request that can be used to monitor this parameter.
        
            Raises:
                :class:`~cern.japc.core.ParameterRuntimeException`: if the monitoring is not supported by this parameter (see :code:`isMonitorable()` on the descriptor of the parameter.
        
        
        """
        ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Reads synchronously the values of the parameters of this group for the given selector. This method returns the values of
            all parameters in the group. This method is synchronous and blocks until the values are read or until problems occur.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
        
            Returns:
                the non null array of values for the parameters of this group and for the given cycle. The number of value is guaranted
                to be the same as the number of parameter in the group and the order of the value in the array is the same as the order
                of the parameters in the group.
        
            Reads asynchronously the values of the parameters of this group for the given selector. The provider listener is
            notified of the value read or if a problem occurs.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
                listener (:class:`~cern.japc.core.group.FailSafeParameterValueListener`): the listener to notify when the value is read or when a problem occurs
        
        
        """
        ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector, failSafeParameterValueListener: FailSafeParameterValueListener) -> None: ...

class ParameterGroup(ImmutableParameterGroup):
    """
    public interface ParameterGroup extends :class:`~cern.japc.core.group.ImmutableParameterGroup`
    
        A class implementing this interface represents a group of parameters.
    
        So, it can read, write and monitor the parameters.
    
        The group guarantees to to keep in the same order of parameters as they have been added to the group. This allows to
        work with parameters in the group using their index. Any array of values received from the group are guaranteed to be in
        the same order as the parameters in the group. Any array of values passed to the group must be in the same order as the
        parameters in the group.
    
        The group can have a same parameter multiple times.
    
        A group of parameters is not thread safe. It needs synchronization to be accessed concurrently.
    """
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue]) -> typing.List[cern.japc.core.FailSafeParameterValue]:
        """
            Sets the value of the parameters of this group for a given cycle synchronously.
        
            This method is synchronous and blocks until all parameters are set with the given value.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
                values (cern.japc.value.ParameterValue[]): the value to set for each parameter of the group. The size of the array of values must exactly match the size of this
                    group so that each parameter has one value.
        
            Returns:
                an array of FailSafe values containing the value-to-set in case of success or an exception in case of failure.
        
            Sets the value of this parameter for a given cycle asynchronously.
        
            More precisely this method sends the signal to transfer the given value to the parameter holder of this parameter. This
            method is asynchronous and should delegate the actual downloading to another process. When the given value will actually
            be received by the parameter holder is undefined and can be tracked using the given listener.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
                values (cern.japc.value.ParameterValue[]): the values to set for each parameter of this group
                listener (:class:`~cern.japc.core.group.FailSafeParameterValueListener`): the listener for the feedback
        
        
        """
        ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValueArray: typing.List[cern.japc.value.ParameterValue], failSafeParameterValueListener: FailSafeParameterValueListener) -> None: ...

class TransactionalParameterGroup(ParameterGroup):
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
