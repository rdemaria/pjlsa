import cern.accsoft.commons.util.collections
import cern.japc.core
import cern.japc.core.spi.adaptation
import cern.japc.core.spi.arraycall
import cern.japc.core.spi.beans
import cern.japc.core.spi.cache
import cern.japc.core.spi.factory
import cern.japc.core.spi.group
import cern.japc.core.spi.jmx
import cern.japc.core.spi.provider
import cern.japc.core.spi.subscription
import cern.japc.core.spi.transaction
import cern.japc.core.spi.util
import cern.japc.core.spi.value
import cern.japc.core.transaction
import cern.japc.value
import cern.japc.value.spi.value.core
import java.io
import java.util
import typing



class AbstractImmutableParameter(cern.japc.core.ImmutableParameter, cern.japc.core.spi.cache.JapcCache):
    """
    public abstract class AbstractImmutableParameter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ImmutableParameter`, :class:`~cern.japc.core.spi.cache.JapcCache`
    
        Implements a ImmutableParameter with default implementation for all methods. The default implementation of the
        informative methods is implemented using information passed to the constructor.
    
        The get methods and the monitoring methods simply throw an exception if they are not supported, else they are delegated
        to a protected implementation method that subclasses should override if they want to support it.
    
        This parameter also supports dynamic descriptors if :class:`~cern.japc.core.spi.provider.DescriptorProvider`
        implementation is provided with the methods
        :meth:`~cern.japc.core.spi.AbstractImmutableParameter.setParameterDescriptor` and
        :meth:`~cern.japc.core.spi.AbstractImmutableParameter.setValueDescriptor`.
    """
    def __init__(self, string: str): ...
    def clearAll(self) -> None: ...
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
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the cycle selector on which to monitor the parameter
                parameterValueListener (:class:`~cern.japc.core.ParameterValueListener`): the listener that will received the notification for that request
        
            Returns:
                the subscription handle that can be used to monitor this parameter.
        
        
        """
        ...
    def getDeviceName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getDeviceName`
            Returns the name of the device holding this parameter.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getDeviceName` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Returns:
                the name of the device holding this parameter
        
        
        """
        ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getName`
            Returns the name that identified this parameter. The name of the parameter is formed by concatenating the name of the
            device that holds this parameter with the name of the property the parameter represents. For instance : [device
            name]/[property name]. The separator used is chosen by the ParameterFactory that creates the parameters.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getName` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                the name identifying this parameter
        
        
        """
        ...
    def getParameterDescriptor(self) -> cern.japc.core.ParameterDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getParameterDescriptor`
            Returns a descriptor of this parameter. The descriptor provides information that describes the parameter.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getParameterDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.ImmutableParameter`
        
            Returns:
                a descriptor of this parameter
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getPropertyName`
            Returns the name of the property represented by this parameter.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getPropertyName` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Returns:
                the name of the property represented by this parameter
        
        
        """
        ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector) -> cern.japc.core.AcquiredParameterValue:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getValue`
            Reads asynchronously the value of this parameter for the given selector. The provider listener is notified of the value
            read or if a problem occurs.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getValue` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener to notify when the value is read or when a problem occurs
        
        public :class:`~cern.japc.core.AcquiredParameterValue` getValue (:class:`~cern.japc.core.Selector` selector) throws :class:`~cern.japc.core.ParameterException`
        
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getValue`
            Reads synchronously the value of this parameter for the given selector. This method returns the value of this parameter.
            This method is synchronous and blocks until the value is read or until a problem occurs.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getValue` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
        
            Returns:
                the non null value of this parameter for the given cycle
        
            Raises:
                :class:`~cern.japc.core.ParameterException`: if a problem occurs preventing the value to be read
        
        
        """
        ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def getValueDescriptor(self) -> cern.japc.value.ValueDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getValueDescriptor`
            Returns a descriptor of the value returned by this parameter. The descriptor provides meta information that describes
            the value.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getValueDescriptor` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Returns:
                a descriptor of this value.
        
        
        """
        ...
    @typing.overload
    def setParameterDescriptor(self, parameterDescriptor: cern.japc.core.ParameterDescriptor, descriptorProvider: cern.japc.core.spi.provider.DescriptorProvider) -> None:
        """
            Sets the descriptor of this parameter. This method must be called by the creator of this parameter in order to set a
            proper descriptor that enables get, set, monitor based on what is possible on the specific parameter.
        
            The descriptor is available for automatic refreshing if :code:`descriptorProvider` is not :code:`null`.
        
            Parameters:
                parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`): the parameter descriptor (can't be :code:`null`)
                descriptorProvider (:class:`~cern.japc.core.spi.provider.DescriptorProvider`): the descriptor provider to use to refresh the descriptor
        
        
        """
        ...
    @typing.overload
    def setParameterDescriptor(self, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> None:
        """
            Sets the descriptor of this parameter. This method must be called by the creator of this parameter in order to set a
            proper descriptor that enables get, set, monitor based on what is possible on the specific parameter.
        
            Such a descriptor becomes fixed, so it is not possible to refresh it later.
        
            Parameters:
                parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`): the parameter descriptor (can't be :code:`null`)
        
        """
        ...
    @typing.overload
    def setValueDescriptor(self, valueDescriptor: cern.japc.value.ValueDescriptor) -> None:
        """
            Sets the value descriptor of this parameter. This method must be called by the creator of this parameter in order to set
            a proper value descriptor that describes the value the parameter can take. By default, at the creation of the parameter,
            the value descriptor is :code:`null`.
        
            Such a descriptor becomes fixed, so it is not possible to refresh it later.
        
            Parameters:
                valueDescriptor (cern.japc.value.ValueDescriptor): the value descriptor (can be :code:`null`)
        
            Sets the value descriptor of this parameter. This method must be called by the creator of this parameter in order to set
            a proper value descriptor that describes the value the parameter can take. By default, at the creation of the parameter,
            the value descriptor is null.
        
            The descriptor is available for automatic refreshing if :code:`descriptorProvider` is not :code:`null`.
        
            Parameters:
                valueDescriptor (cern.japc.value.ValueDescriptor): the value descriptor (can be :code:`null`)
                descriptorProvider (:class:`~cern.japc.core.spi.provider.DescriptorProvider`): the descriptor provider to use to refresh the descriptor
        
        
        """
        ...
    @typing.overload
    def setValueDescriptor(self, valueDescriptor: cern.japc.value.ValueDescriptor, descriptorProvider: cern.japc.core.spi.provider.DescriptorProvider) -> None: ...
    def toString(self) -> str:
        """
            Return a string representation of this object.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation of this object.
        
        
        """
        ...

class CumulativeWait:
    """
    public class CumulativeWait extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A class used to keep track of how much a thread wait for a global request.
    
        It is used for example in :class:`~cern.japc.core.spi.PullSubscriptionStrategy` to limit a time of a global call
        involving several parameters.
    """
    def __init__(self, long: int): ...
    @staticmethod
    def cleanThreadTimeToWait() -> None:
        """
            Cleans the time to wait for a global request on the current thread.
        
        """
        ...
    def remainingTimeToWait(self) -> int:
        """
            Returns remaining time to wait for a value expected for particular cycle stamp.
        
            Returns:
                remaining time to wait for a value expected for particular cycle stamp
        
        
        """
        ...
    @staticmethod
    def setThreadTimeToWait(long: int) -> 'CumulativeWait':
        """
            Sets the maximum time to wait for a global request on the current thread.
        
            Parameters:
                maxTimeToWaitMs (long): the maximum time to wait in milliseconds
        
            Returns:
                the corresponding :class:`~cern.japc.core.spi.CumulativeWait` instance
        
        
        """
        ...
    def updateTimeWaited(self, long: int) -> None:
        """
            Updates the time waited.
        
            Parameters:
                timeWaited (long): 
        
        """
        ...

class DeviceDescriptorImpl(cern.japc.core.DeviceDescriptor, java.io.Serializable):
    """
    public class DeviceDescriptorImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.DeviceDescriptor`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...
    def addExtraCharacteristic(self, string: str, string2: str) -> None:
        """
            Add an extra characteristic of the device associated with this descriptor. If the same name is entered twice the value
            is overwritten.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The name of the extra device characteristic
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The value of the extra device characteristic
        
        
        """
        ...
    def getControlProperty(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getControlProperty`
            Returns the device main CONTROL property name. If no property is defined null can be returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getControlProperty` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device main CONTROL property name.
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getDescription`
            Returns an optional description of this device
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getDescription` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                an optional description of this device or null
        
        
        """
        ...
    def getDeviceClassDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getDeviceClassDescription`
            Returns the description of the device class.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getDeviceClassDescription`Â in
                interfaceÂ :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                an optional description of this device class.
        
        
        """
        ...
    def getDeviceClassName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getDeviceClassName`
            Returns the name of the device class.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getDeviceClassName` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                device class name
        
        
        """
        ...
    def getExtraCharacteristic(self, string: str) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getExtraCharacteristic`
            Returns the value of the characteristic of the device defined by the given name. If no characteristic of that name is
            defined for this parameter the value returned is null.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getExtraCharacteristic` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the extra characteristic to get
        
            Returns:
                the value of the characteristic of the device defined by the given name.
        
        
        """
        ...
    def getExtraCharacteristicNames(self) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getExtraCharacteristicNames`
            Returns the names of the possible extra characteristic of the device. The returned value is guaranted to be non null. It
            is an array that is possibly empty.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getExtraCharacteristicNames`Â in
                interfaceÂ :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the names of the possible extra characteristic of the device.
        
        
        """
        ...
    def getHostName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getHostName`
            Returns the device host name. If no location is defined null can be returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getHostName` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device host name.
        
        
        """
        ...
    def getImplementation(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getImplementation`
            Returns the device implementation: :meth:`~cern.japc.core.DeviceDescriptor.IMPL_FESA`,
            :meth:`~cern.japc.core.DeviceDescriptor.IMPL_GM`, :meth:`~cern.japc.core.DeviceDescriptor.IMPL_SLEQP`,
            :meth:`~cern.japc.core.DeviceDescriptor.IMPL_BISCOTO`, :meth:`~cern.japc.core.DeviceDescriptor.IMPL_HARDWARE`,
            :meth:`~cern.japc.core.DeviceDescriptor.IMPL_VIRTUAL`, :meth:`~cern.japc.core.DeviceDescriptor.IMPL_UNKNOWN`
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getImplementation` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device implementation.
        
        
        """
        ...
    def getLogicalLocation(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getLogicalLocation`
            Returns the device location (Accelerator, transfert line name, etc). If no location is defined null can be returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getLogicalLocation` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device location (Accelerator, transfert line name, etc).
        
        
        """
        ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getName`
            Returns the name of this device.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getName` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the name of this device.
        
        
        """
        ...
    def getResetProperty(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getResetProperty`
            Returns the device RESET property name, which can be used to reset a device If no property is defined null can be
            returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getResetProperty` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device RESET property name.
        
        
        """
        ...
    def getStatusProperty(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getStatusProperty`
            Returns the device main STATUS property name. If no property is defined null can be returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getStatusProperty` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device main STATUS property name.
        
        
        """
        ...
    def getTgmName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getTgmName`
            Returns the device TGM machine name. If no TGM machine is defined null can be returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getTgmName` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device TGM machine name.
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.isCycleBound`
            Returns :code:`true` if this device is cycle-bound, meaning that updates of at least one of its acquisition properties
            are valid only for the cycle when the acquisition has been done. More details can be found in "Device Property behaviour
            and contextual data" EDMS document: [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.isCycleBound` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                :code:`true` if this device is cycle-bound
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.isMultiplexed`
            Returns :code:`true` if this device is multiplexed, meaning at least one of its setting properties is capable of storing
            settings for different timing users. More details can be found in "Device Property behaviour and contextual data" EDMS
            document: [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.isMultiplexed` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                :code:`true` if this device is multiplexed
        
        
        """
        ...
    def setControlProperty(self, string: str) -> None:
        """
            Sets the control property of the device associated with this descriptor
        
            Parameters:
                controlProperty (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The control property to set.
        
        
        """
        ...
    def setCycleBound(self, boolean: bool) -> None:
        """
            Sets whether the device is cycle-bound or not.
        
            Parameters:
                cycleBound (boolean): :code:`true` if the device is cycle-bound
        
        
        """
        ...
    def setDescription(self, string: str) -> None:
        """
            Sets the description of the device described by this descriptor
        
            Parameters:
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the description of the device described by this descriptor
        
        
        """
        ...
    def setDeviceClassDescription(self, string: str) -> None:
        """
        
            Parameters:
                deviceClassDescription (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the device class description
        
        
        """
        ...
    def setDeviceClassName(self, string: str) -> None:
        """
        
            Parameters:
                deviceClassName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the device class name
        
        
        """
        ...
    def setHostName(self, string: str) -> None:
        """
            Sets the host Name of the device associated with this descriptor
        
            Parameters:
                hostName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The host Name to set.
        
        
        """
        ...
    def setImplementation(self, int: int) -> None:
        """
            Sets the device implementation
        
            Parameters:
                implementation (int): The device implementation to set.
        
        
        """
        ...
    def setLogicalLocation(self, string: str) -> None:
        """
            Sets the logical location (Accelerator, transfert line name) of the device associated with this descriptor
        
            Parameters:
                logicalLocation (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The logical Location to set.
        
        
        """
        ...
    def setMultiplexed(self, boolean: bool) -> None:
        """
            Sets whether the device is multiplexed or not.
        
            Parameters:
                multiplexed (boolean): :code:`true` if the device is multiplexed
        
        
        """
        ...
    def setResetProperty(self, string: str) -> None:
        """
            Sets the reset property of the device associated with this descriptor
        
            Parameters:
                resetProperty (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The reset property to set.
        
        
        """
        ...
    def setStatusProperty(self, string: str) -> None:
        """
            Sets the status property of the device associated with this descriptor
        
            Parameters:
                statusProperty (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The statusProperty to set.
        
        
        """
        ...
    def setTgmName(self, string: str) -> None:
        """
            Sets the TGM machine name of the device associated with this descriptor
        
            Parameters:
                tgmName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The tgmName to set.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class DeviceDescriptorSupport(cern.japc.core.DeviceDescriptor, java.io.Serializable):
    """
    public class DeviceDescriptorSupport extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.DeviceDescriptor`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getControlProperty(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getControlProperty`
            Returns the device main CONTROL property name. If no property is defined null can be returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getControlProperty` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device main CONTROL property name.
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getDescription`
            Returns an optional description of this device
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getDescription` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                an optional description of this device or null
        
        
        """
        ...
    def getDeviceClassDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getDeviceClassDescription`
            Returns the description of the device class.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getDeviceClassDescription`Â in
                interfaceÂ :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                an optional description of this device class.
        
        
        """
        ...
    def getDeviceClassName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getDeviceClassName`
            Returns the name of the device class.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getDeviceClassName` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                device class name
        
        
        """
        ...
    def getExtraCharacteristic(self, string: str) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getExtraCharacteristic`
            Returns the value of the characteristic of the device defined by the given name. If no characteristic of that name is
            defined for this parameter the value returned is null.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getExtraCharacteristic` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the extra characteristic to get
        
            Returns:
                the value of the characteristic of the device defined by the given name.
        
        
        """
        ...
    def getExtraCharacteristicNames(self) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getExtraCharacteristicNames`
            Returns the names of the possible extra characteristic of the device. The returned value is guaranted to be non null. It
            is an array that is possibly empty.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getExtraCharacteristicNames`Â in
                interfaceÂ :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the names of the possible extra characteristic of the device.
        
        
        """
        ...
    def getHostName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getHostName`
            Returns the device host name. If no location is defined null can be returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getHostName` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device host name.
        
        
        """
        ...
    def getImplementation(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getImplementation`
            Returns the device implementation: :meth:`~cern.japc.core.DeviceDescriptor.IMPL_FESA`,
            :meth:`~cern.japc.core.DeviceDescriptor.IMPL_GM`, :meth:`~cern.japc.core.DeviceDescriptor.IMPL_SLEQP`,
            :meth:`~cern.japc.core.DeviceDescriptor.IMPL_BISCOTO`, :meth:`~cern.japc.core.DeviceDescriptor.IMPL_HARDWARE`,
            :meth:`~cern.japc.core.DeviceDescriptor.IMPL_VIRTUAL`, :meth:`~cern.japc.core.DeviceDescriptor.IMPL_UNKNOWN`
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getImplementation` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device implementation.
        
        
        """
        ...
    def getLogicalLocation(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getLogicalLocation`
            Returns the device location (Accelerator, transfert line name, etc). If no location is defined null can be returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getLogicalLocation` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device location (Accelerator, transfert line name, etc).
        
        
        """
        ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getName`
            Returns the name of this device.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getName` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the name of this device.
        
        
        """
        ...
    def getResetProperty(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getResetProperty`
            Returns the device RESET property name, which can be used to reset a device If no property is defined null can be
            returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getResetProperty` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device RESET property name.
        
        
        """
        ...
    def getStatusProperty(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getStatusProperty`
            Returns the device main STATUS property name. If no property is defined null can be returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getStatusProperty` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device main STATUS property name.
        
        
        """
        ...
    def getTgmName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.getTgmName`
            Returns the device TGM machine name. If no TGM machine is defined null can be returned.
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.getTgmName` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                the device TGM machine name.
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.isCycleBound`
            Returns :code:`true` if this device is cycle-bound, meaning that updates of at least one of its acquisition properties
            are valid only for the cycle when the acquisition has been done. More details can be found in "Device Property behaviour
            and contextual data" EDMS document: [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.isCycleBound` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                :code:`true` if this device is cycle-bound
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.DeviceDescriptor.isMultiplexed`
            Returns :code:`true` if this device is multiplexed, meaning at least one of its setting properties is capable of storing
            settings for different timing users. More details can be found in "Device Property behaviour and contextual data" EDMS
            document: [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Specified by:
                :meth:`~cern.japc.core.DeviceDescriptor.isMultiplexed` in interface :class:`~cern.japc.core.DeviceDescriptor`
        
            Returns:
                :code:`true` if this device is multiplexed
        
        
        """
        ...

class FspvCollector(cern.accsoft.commons.util.collections.ValueCollector[cern.japc.core.FailSafeParameterValue], cern.japc.core.ParameterValueListener):
    """
    public interface FspvCollector extends cern.accsoft.commons.util.collections.ValueCollector<:class:`~cern.japc.core.FailSafeParameterValue`>, :class:`~cern.japc.core.ParameterValueListener`
    
        Interface represents a collector for the JAPC values.
    
        This collector can be used just as :class:`~cern.japc.core.ParameterValueListener`.
    """
    ...

class FspvPeekingStrategy(cern.accsoft.commons.util.collections.ValuePeekingStrategy[cern.japc.core.FailSafeParameterValue]):
    """
    public interface FspvPeekingStrategy extends cern.accsoft.commons.util.collections.ValuePeekingStrategy<:class:`~cern.japc.core.FailSafeParameterValue`>
    
        Interface describing a strategy which chooses the values provided by :class:`~cern.japc.core.spi.FspvCollector`.
    """
    ...

class IgnoreSetParameterDecorator(cern.japc.core.spi.transaction.TransactionalParameterDecorator):
    """
    public class IgnoreSetParameterDecorator extends :class:`~cern.japc.core.spi.transaction.TransactionalParameterDecorator`
    """
    def __init__(self, transactionalParameter: cern.japc.core.transaction.TransactionalParameter): ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.Parameter.setValue`
            Sets the value of this parameter for a given cycle asynchronously.
        
            More precisely this method sends the signal to transfert the given value to the parameter holder of this parameter. This
            method is asynchronous and should delegate the actual downloading to another process. When the given value will actually
            be received by the parameter holder is undefined and can be tracked using the given listener.
        
            The value is **activated** once received by the parameter holder.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.Parameter.setValue` in interface :class:`~cern.japc.core.Parameter`
        
            Overrides:
                :meth:`~cern.japc.core.spi.ParameterDecorator.setValue` in class :class:`~cern.japc.core.spi.ParameterDecorator`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
                value (cern.japc.value.ParameterValue): the value to set for this parameter
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener for the feedback
        
        
        """
        ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...

class ImmutableParameterDecorator(cern.japc.core.ImmutableParameter):
    """
    public class ImmutableParameterDecorator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ImmutableParameter`
    
        :class:`~cern.japc.core.ImmutableParameter` decorator delegating all the methods to the embedded parameter.
    """
    def __init__(self, immutableParameter: cern.japc.core.ImmutableParameter): ...
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
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the cycle selector on which to monitor the parameter
                parameterValueListener (:class:`~cern.japc.core.ParameterValueListener`): the listener that will received the notification for that request
        
            Returns:
                the subscription handle that can be used to monitor this parameter.
        
        
        """
        ...
    def getDeviceName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getDeviceName`
            Returns the name of the device holding this parameter.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getDeviceName` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Returns:
                the name of the device holding this parameter
        
        
        """
        ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getName`
            Returns the name that identified this parameter. The name of the parameter is formed by concatenating the name of the
            device that holds this parameter with the name of the property the parameter represents. For instance : [device
            name]/[property name]. The separator used is chosen by the ParameterFactory that creates the parameters.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getName` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                the name identifying this parameter
        
        
        """
        ...
    def getParameterDescriptor(self) -> cern.japc.core.ParameterDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getParameterDescriptor`
            Returns a descriptor of this parameter. The descriptor provides information that describes the parameter.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getParameterDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.ImmutableParameter`
        
            Returns:
                a descriptor of this parameter
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getPropertyName`
            Returns the name of the property represented by this parameter.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getPropertyName` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Returns:
                the name of the property represented by this parameter
        
        
        """
        ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector) -> cern.japc.core.AcquiredParameterValue:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getValue`
            Reads asynchronously the value of this parameter for the given selector. The provider listener is notified of the value
            read or if a problem occurs.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getValue` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener to notify when the value is read or when a problem occurs
        
        
        """
        ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def getValueDescriptor(self) -> cern.japc.value.ValueDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getValueDescriptor`
            Returns a descriptor of the value returned by this parameter. The descriptor provides meta information that describes
            the value.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getValueDescriptor` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Returns:
                a descriptor of this value.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ParameterDescriptorImpl(cern.japc.value.spi.value.core.TypedObject, cern.japc.core.ParameterDescriptor):
    """
    public abstract class ParameterDescriptorImpl extends cern.japc.value.spi.value.core.TypedObject implements :class:`~cern.japc.core.ParameterDescriptor`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, type: cern.japc.value.Type, string: str): ...
    def addExtraCharacteristic(self, string: str, string2: str) -> None:
        """
            Add an extra characteristic of the parameter associated with this descriptor. If the same name is entered twice the
            value is overwritten.
        
            Parameters:
                extCharName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the extra parameter characteristic
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the value of the extra parameter characteristic
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.getDescription`
            Returns an optional description of this parameter
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.getDescription` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                an optional description of this parameter or null
        
        
        """
        ...
    def getExtraCharacteristic(self, string: str) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.getExtraCharacteristic`
            Returns the value of the characteristic of the parameter defined by the given name. If no characteristic of that name is
            defined for this parameter the value returned is null.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.getExtraCharacteristic`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterDescriptor`
        
            Parameters:
                extCharName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the extra characteristic to get
        
            Returns:
                the value of the characteristic of the parameter defined by the given name.
        
        
        """
        ...
    def getExtraCharacteristicNames(self) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.getExtraCharacteristicNames`
            Returns the names of the possible extra characteristics of the parameter. The returned value is guaranteed to be non
            null. It is an array that is possibly empty.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.getExtraCharacteristicNames`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                the names of the possible extra characteristic of the parameter.
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
        
            Returns:
                parameter name
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.isCycleBound`
            Returns :code:`true` if this parameter is a cycle-bound acquisition parameter. More details can be found in "Device
            Property behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs] **** All the operations (get,
            subscribe) with cycle-bound parameters require a proper non-empty cycle selector.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isCycleBound` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                :code:`true` if this parameter is a cycle-bound acquisition parameter
        
        
        """
        ...
    def isFilterable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.isFilterable`
            Returns :code:`true` if the parameter described by this descriptor can be filtered. If the filtering is supported, it is
            possible to pass a filter on the parameter to control what part of the value is returned. The default value is
            :code:`false`.
        
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isFilterable` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                :code:`true` if the parameter described by this descriptor can be filtered.
        
        
        """
        ...
    def isMonitorable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.isMonitorable`
            Returns true if the parameter support monitoring and false else. If the parameter does not support monitoring a call to
            the method :code:`startMonitoring` will throw an exception.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isMonitorable` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                true if the parameter support monitoring and false else.
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.isMultiplexed`
            Returns :code:`true` if this parameter is a multiplexed setting parameter. More details can be found in "Device Property
            behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs] **** All the operations (get, set,
            subscribe) with multiplexed parameters require a proper non-empty cycle selector.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isMultiplexed` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                :code:`true` if this parameter is a multiplexed setting parameter
        
        
        """
        ...
    def isReadable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.isReadable`
            Returns true if this parameter is readable which means that it does support the get methods.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isReadable` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                boolean true if the get/monitor methods are supported false else.
        
        
        """
        ...
    def isTransactional(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.isTransactional`
            Returns true if this parameter supports transaction on the set. If the parameter does not support transaction an attempt
            to set a value using a transaction will throw an exception.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isTransactional` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                true is this parameter supports transaction on the set, false else.
        
        
        """
        ...
    def isValueMutable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.isValueMutable`
            Returns true if the value returned from JAPC (read or as an update) must be mutable. By default all the values coming
            from JAPC are immutable to guarantee thread-safety of the value.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isValueMutable` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                true if the value returned from JAPC must be mutable and false otherwise
        
        
        """
        ...
    def isWritable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterDescriptor.isWritable`
            Returns true if this parameter is mutable which means that it does support the setValue methods.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isWritable` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                boolean true if the set methods are supported false else.
        
        
        """
        ...
    def setCycleBound(self, boolean: bool) -> None:
        """
            Sets whether the parameter is cycle-bound acquisition parameter or not.
        
            Parameters:
                cycleBound (boolean): :code:`true` if the parameter is cycle-bound acquisition parameter
        
        
        """
        ...
    def setDescription(self, string: str) -> None:
        """
            Sets the description of the parameter
        
            Parameters:
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the description of the parameter
        
        
        """
        ...
    def setFilterable(self, boolean: bool) -> None:
        """
            Sets the isFilterable flag.
        
            Parameters:
                isFilterable (boolean): true igf the parameter is filterable, false else
        
        
        """
        ...
    def setMonitorable(self, boolean: bool) -> None:
        """
            Sets whether the parameter is monitorable or not
        
            Parameters:
                monitorable (boolean): true if the parameter is monitorable, false else
        
        
        """
        ...
    def setMultiplexed(self, boolean: bool) -> None:
        """
            Sets whether the parameter is multiplexed setting parameter or not.
        
            Parameters:
                multiplexed (boolean): :code:`true` if the parameter is multiplexed setting parameter
        
        
        """
        ...
    def setReadable(self, boolean: bool) -> None:
        """
            Sets whether the parameter is readable or not
        
            Parameters:
                readable (boolean): true if the parameter is readable, false else
        
        
        """
        ...
    def setTransactional(self, boolean: bool) -> None:
        """
            Sets whether the parameter is transactional or not
        
            Parameters:
                transactional (boolean): true if the parameter is readable, false else
        
        
        """
        ...
    def setValueMutable(self, boolean: bool) -> None:
        """
            Sets whether the value returned by the parameter must be mutable or not
        
            Parameters:
                valueMutable (boolean): true if the value returned by the parameter must be mutable, false else
        
        
        """
        ...
    def setWritable(self, boolean: bool) -> None:
        """
            Sets whether the parameter is writable or not
        
            Parameters:
                writable (boolean): true if the parameter is readable, false else
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ParameterDescriptorSupport(cern.japc.core.ParameterDescriptor, java.io.Serializable):
    """
    public class ParameterDescriptorSupport extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ParameterDescriptor`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Support class for implementing the ParameterDescriptor interface that returns default values.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getDescription(self) -> str:
        """
            By default no description is provided and this method returns null.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.getDescription` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                null as no description is provided by default
        
        
        """
        ...
    def getExtraCharacteristic(self, string: str) -> str:
        """
            By default no Extra Characteristic are provided and this method returns null.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.getExtraCharacteristic`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterDescriptor`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the extra characteristic to get
        
            Returns:
                null as no Extra Characteristic are provided by default
        
        
        """
        ...
    def getExtraCharacteristicNames(self) -> typing.List[str]:
        """
            By default no Extra Characteristic Names are provided and this method returns an empty String array.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.getExtraCharacteristicNames`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                an empty String array as no Extra Characteristic Names are provided by default
        
        
        """
        ...
    def getType(self) -> cern.japc.value.Type:
        """
            Returns the type of this parameter descriptor.
        
        
            Which is SIMPLE here due to backward compatibility reasons.
        
        
        
        
            **IMPORTANT: MUST BE OVERWRITEN IN SUBCLASSES IN ORDER TO RETURN THE CORRECT TYPE.**
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.getType` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                the type of this parameter descriptor
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
            By default the parameter is not cycle-bound and this method return false.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isCycleBound` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                false as the parameter is not cycle-bound
        
        
        """
        ...
    def isFilterable(self) -> bool:
        """
            Default implementation that returns false. Override to return proper value.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isFilterable` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                :code:`true` if the parameter described by this descriptor can be filtered.
        
            Also see:
                :meth:`~cern.japc.core.ParameterDescriptor.isFilterable`
        
        
        """
        ...
    def isMonitorable(self) -> bool:
        """
            By default Monitoring is not supported and this method returns false. Sub-classes should override this method if they
            want to support monitoring.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isMonitorable` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                false as monitoring is not supported by default
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            By default the parameter is not multiplexed and this method return false.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isMultiplexed` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                false as the parameter is not multiplexed
        
        
        """
        ...
    def isReadable(self) -> bool:
        """
            By default get methods are not supported and this method returns false. Sub-classes should override this method if they
            want to support get operations.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isReadable` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                false as get operations are not supported by default
        
        
        """
        ...
    def isTransactional(self) -> bool:
        """
            By default Transaction are not supported and this method returns false. Sub-classes should override this method if they
            want to support transactions.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isTransactional` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                false as transactions are not supported by default
        
        
        """
        ...
    def isValueMutable(self) -> bool:
        """
            By default values returned from a parameter are immutable and this method returns false. Sub-classes should override
            this method if they want to have values returned from JAPC to be mutable.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isValueMutable` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                false as values returned from a parameter are immutable by default
        
        
        """
        ...
    def isWritable(self) -> bool:
        """
            By default set methods are not supported and this method returns false. Sub-classes should override this method if they
            want to support set operations.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterDescriptor.isWritable` in interface :class:`~cern.japc.core.ParameterDescriptor`
        
            Returns:
                false as set operations are not supported by default
        
        
        """
        ...

class ParameterUrl:
    """
    public interface ParameterUrl
    
        Defines a Parameter URL which represents full parameter information:
    
    
    
          1.  protocol
          2.  service
          3.  device
          4.  property
          5.  field
    """
    PROTOCOL_SEPARATOR: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROTOCOL_SEPARATOR
    
        the separator to separate protocol from service
    
        Also see:
            :meth:`~constant`
    
    
    """
    SERVICE_SEPARATOR: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SERVICE_SEPARATOR
    
        the separator to use between service and deviceName
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_PROPERTY_NAME_SEPARATOR: typing.ClassVar[str] = ...
    """
    static final char DEVICE_PROPERTY_NAME_SEPARATOR
    
        the separator to use between deviceName and propertyName
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROPERTY_NAME_FIELD_SEPARATOR: typing.ClassVar[str] = ...
    """
    static final char PROPERTY_NAME_FIELD_SEPARATOR
    
        the separator to use between propertyName and the MAP KEY name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def cloneWithoutField(self) -> 'ParameterUrl':
        """
            Returns the parameter URL representing the same parameter without field information
        
            Returns:
                the parameter URL representing the same parameter without field information
        
        
        """
        ...
    def getDeviceAndProperty(self) -> str:
        """
        
            Returns:
                the part of parameter name containing device and property only
        
        
        """
        ...
    def getDeviceName(self) -> str:
        """
        
            Returns:
                Returns the deviceName.
        
        
        """
        ...
    def getFieldName(self) -> str:
        """
        
            Returns:
                Returns the fieldName.
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
        
            Returns:
                Returns the parameter name
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
        
            Returns:
                Returns the propertyName.
        
        
        """
        ...
    def getProtocolName(self) -> str:
        """
        
            Returns:
                Returns the protocolName.
        
        
        """
        ...
    def getServiceName(self) -> str:
        """
        
            Returns:
                Returns the serviceName.
        
        
        """
        ...
    def hasFieldName(self) -> bool:
        """
        
            Returns:
                Returns true if the URL contains field information
        
        
        """
        ...
    def isDimParameter(self) -> bool:
        """
        
            Returns:
                Returns true if the URL contains DIM parameter name
        
        
        """
        ...
    def isFull(self) -> bool:
        """
        
            Returns:
                Returns true if the URL contains protocol and service information
        
        
        """
        ...

class SelectorImpl(cern.japc.core.Selector, java.io.Serializable):
    """
    public class SelectorImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.Selector`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, selector: cern.japc.core.Selector): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, parameterValue: cern.japc.value.ParameterValue): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getDataFilter(self) -> cern.japc.value.ParameterValue:
        """
            Description copied from interface: :meth:`~cern.japc.core.Selector.getDataFilter`
            Returns an optional filter on the data (can be :code:`null`). The filter can be used to request a subset of the data
            from the device (ex. specify sampling rate).
        
            Specified by:
                :meth:`~cern.japc.core.Selector.getDataFilter` in interface :class:`~cern.japc.core.Selector`
        
            Returns:
                an optional filter (can be :code:`null`)
        
        
        """
        ...
    def getId(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.Selector.getId`
            Returns string representation of the identifier of the cycle.
        
        
            Can be either:
        
        
        
              1.  empty string for non-cycle-dependent cases
              2.  TGM_NAME.GROUP.VALUE for cycle-dependent case, ex. SPS.USER.SFTPRO1
        
        
            Specified by:
                :meth:`~cern.japc.core.Selector.getId` in interface :class:`~cern.japc.core.Selector`
        
            Returns:
                string representation of the identifier of the cycle
        
        
        """
        ...
    def getPeriod(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.Selector.getPeriod`
            For a periodic subscription, returns the period of the subscription in milliseconds or a negative number if the
            subscription is not periodic.
        
            Specified by:
                :meth:`~cern.japc.core.Selector.getPeriod` in interface :class:`~cern.japc.core.Selector`
        
            Returns:
                the period length in milliseconds or a negative number if the subscription is not periodic
        
            Also see:
                :meth:`~cern.japc.core.Selector.isPeriodic`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isPeriodic(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.Selector.isPeriodic`
            Returns a boolean which says if the Selector correspond to a periodic subscription.
        
            Specified by:
                :meth:`~cern.japc.core.Selector.isPeriodic` in interface :class:`~cern.japc.core.Selector`
        
            Returns:
                true of the subscription is periodic
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class SubscriptionConfigurationImpl(cern.japc.core.SubscriptionConfigurator):
    """
    public class SubscriptionConfigurationImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.SubscriptionConfigurator`
    
        Decorator of a subscription request that delegates everything to the embedded one.
    """
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
    def setDataDeliveryMode(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.SubscriptionConfigurator.setDataDeliveryMode`
            Sets the fetch mode of this handle to :code:`PUSH_MODE` or :code:`PULL_MODE`. Default is :code:`MODE_PUSH_ONLY`.
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionConfigurator.setDataDeliveryMode`Â in
                interfaceÂ :class:`~cern.japc.core.SubscriptionConfigurator`
        
            Parameters:
                dataDeliveryMode (int): the data delivery mode either :code:`PUSH_MODE` or :code:`PULL_MODE`
        
        
        """
        ...

class SubscriptionHandleDecorator(cern.japc.core.SubscriptionHandle):
    """
    public class SubscriptionHandleDecorator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.SubscriptionHandle`
    
        Decorator of a subscription request that delegates everything to the embedded one.
    """
    def __init__(self, subscriptionHandle: cern.japc.core.SubscriptionHandle): ...
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
            Description copied from interface: :meth:`~cern.japc.core.SubscriptionHandle.stopMonitoring`
            Stops monitoring on this subscription request if it is not already stopped.
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionHandle.stopMonitoring` in interface :class:`~cern.japc.core.SubscriptionHandle`
        
        
        """
        ...

class SubscriptionSource:
    """
    public interface SubscriptionSource
    
        The source that produces events on a subscription.
    """
    def getSelector(self) -> cern.japc.core.Selector:
        """
            Returns the cycle selector on which this source is activated
        
            Returns:
                the possibly null cycle selector on which this source is activated
        
        
        """
        ...
    def initializeSubscriptionSource(self, parameterValueListener: cern.japc.core.ParameterValueListener) -> None:
        """
            Initializes this source with the listener to which forward all events of the subscription. This method must be called
            only once before start or stop methods are called.
        
            Parameters:
                listener (:class:`~cern.japc.core.ParameterValueListener`): the non null listener of the subscription.
        
        
        """
        ...
    def startSubscription(self) -> None: ...
    def stopSubscription(self) -> None:
        """
            This method should perform the effective stop of the subscription on the target source and on the given cycle selector.
            The method must not do anything if the subscription is already stopped.
        
        """
        ...

class SubscriptionStrategy:
    """
    public interface SubscriptionStrategy
    
        Interface defining a strategy for sending the data to the client listener (either push or pull).
    """
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Receives new exception for parameter.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def peekValue(self, long: int) -> cern.japc.core.AcquiredParameterValue: ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None:
        """
            Receives new value for a parameter.
        
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...

class UpdatableAcquiredParameterValue:
    """
    public interface UpdatableAcquiredParameterValue
    
        This interface can be used to check if an AcquiredParameterValue support the setXXX methods.
    """
    def addAdditionalError(self, string: str) -> None:
        """
            Set the additional error String to an AcquiredParameterValue
        
            Parameters:
                additionalError (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The additional error String to set.
        
        
        """
        ...
    def setHeader(self, valueHeader: cern.japc.core.ValueHeader) -> None:
        """
            Set the :class:`~cern.japc.core.ValueHeader` to an AcquiredParameterValue
        
            Parameters:
                header (:class:`~cern.japc.core.ValueHeader`): The ValueHeader to set.
        
        
        """
        ...
    def setStatus(self, valueStatus: cern.japc.value.ValueStatus) -> None:
        """
            Set the :code:`ValueStatus` to an AcquiredParameterValue
        
            Parameters:
                status (cern.japc.value.ValueStatus): The ValueStatus to set.
        
        
        """
        ...

class ValueHeaderImpl(cern.japc.core.ValueHeader, java.io.Serializable):
    """
    public class ValueHeaderImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ValueHeader`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of :class:`~cern.japc.core.ValueHeader`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, long: int, selector: cern.japc.core.Selector): ...
    @typing.overload
    def __init__(self, long: int, long2: int, selector: cern.japc.core.Selector): ...
    def getAcqStamp(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.ValueHeader.getAcqStamp`
            Returns the acquisition Time Stamp (UTC in nanoseconds). It is the absolute time in nanoseconds this value has been
            acquired. If the timestamp is not known or not relevant the constant :code:`0` should be returned.
        
            Specified by:
                :meth:`~cern.japc.core.ValueHeader.getAcqStamp` in interface :class:`~cern.japc.core.ValueHeader`
        
            Returns:
                the absolute time in nanoseconds this value has been acquired.
        
        
        """
        ...
    def getAcqStampMillis(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.ValueHeader.getAcqStampMillis`
            Returns the acquisition Time Stamp (UTC in milliseconds). It is the absolute time in milliseconds this value has been
            acquired. If the timestamp is not known or not relevant the constant :code:`0` should be returned.
        
            Specified by:
                :meth:`~cern.japc.core.ValueHeader.getAcqStampMillis` in interface :class:`~cern.japc.core.ValueHeader`
        
            Returns:
                the absolute time in milliseconds this value has been acquired.
        
        
        """
        ...
    def getCycleStamp(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.ValueHeader.getCycleStamp`
            Returns unique time stamp that identifies a unique cycle occurrence. Time UTC (in nanoseconds). If the cycleStamp is not
            known or not relevant :code:`0` should be returned.
        
            Specified by:
                :meth:`~cern.japc.core.ValueHeader.getCycleStamp` in interface :class:`~cern.japc.core.ValueHeader`
        
            Returns:
                the unique time stamp that identifies a unique cycle occurrence this value belongs to in nanoseconds
        
        
        """
        ...
    def getCycleStampMillis(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.ValueHeader.getCycleStampMillis`
            Returns unique time stamp that identifies a unique cycle occurrence. Time UTC (in milliseconds). If the cycleStamp is
            not known or not relevant :code:`0` should be returned.
        
            Specified by:
                :meth:`~cern.japc.core.ValueHeader.getCycleStampMillis` in interface :class:`~cern.japc.core.ValueHeader`
        
            Returns:
                the unique time stamp that identifies a unique cycle occurrence this value belongs to in milliseconds
        
        
        """
        ...
    def getSelector(self) -> cern.japc.core.Selector:
        """
            Description copied from interface: :meth:`~cern.japc.core.ValueHeader.getSelector`
            Returns the Selector identifying the cycle the value stamped with this header is for. Null can be returned if the cycle
            is not relevant or unknown.
        
            Specified by:
                :meth:`~cern.japc.core.ValueHeader.getSelector` in interface :class:`~cern.japc.core.ValueHeader`
        
            Returns:
                the Selector identifying the cycle the value stamped with this header is for or null.
        
        
        """
        ...
    def getSetStamp(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.ValueHeader.getSetStamp`
            Returns the last SET Time Stamp (UTC in nanoseconds). It is the absolute time in nanoseconds the last SET has been
            performed. If the timestamp is not known or not relevant the constant :code:`0` should be returned.
        
            Specified by:
                :meth:`~cern.japc.core.ValueHeader.getSetStamp` in interface :class:`~cern.japc.core.ValueHeader`
        
            Returns:
                the absolute time in nanoseconds of the last performed SET
        
        
        """
        ...
    def getSetStampMillis(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.ValueHeader.getSetStampMillis`
            Returns the last SET Time Stamp (UTC in milliseconds). It is the absolute time in milliseconds the last SET has been
            performed. If the timestamp is not known or not relevant the constant :code:`0` should be returned.
        
            Specified by:
                :meth:`~cern.japc.core.ValueHeader.getSetStampMillis` in interface :class:`~cern.japc.core.ValueHeader`
        
            Returns:
                the absolute time in milliseconds of the last performed SET
        
        
        """
        ...
    def isFirstUpdate(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ValueHeader.isFirstUpdate`
            Returns true if this value is coming the immediate update. The first time a subscription is started, a value is supposed
            to be sent immediately to reflect the current value of the parameter being monitored. This first value should have this
            flag set to true.
        
            Specified by:
                :meth:`~cern.japc.core.ValueHeader.isFirstUpdate` in interface :class:`~cern.japc.core.ValueHeader`
        
            Returns:
                true if this value is coming the first update.
        
        
        """
        ...
    def isImmediateUpdate(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ValueHeader.isImmediateUpdate`
            Returns true in case this value has been sent following a untriggered change in the value being monitored. In case of
            monitoring, values are expected to come when the given selector is trigged. In case the parameter is a writable value, a
            write operation can occur anytime and the new value is expected to be sent to all client monitoring the value. The new
            value is not sent because of a given trigger acting on the selector but because of an untriggered condition. The value
            sent should have this flag set to true to be distinguished from the regular update.
        
            Specified by:
                :meth:`~cern.japc.core.ValueHeader.isImmediateUpdate` in interface :class:`~cern.japc.core.ValueHeader`
        
            Returns:
                true in case this value has been sent following a untriggered change in the value being monitored.
        
        
        """
        ...
    def setAcqStamp(self, long: int) -> None:
        """
            Sets the acquisition stamp (in nanoseconds).
        
            Parameters:
                acqStamp (long): the acquisition stamp to set (in nanoseconds)
        
        
        """
        ...
    def setAcqStampMillis(self, long: int) -> None:
        """
            Sets the acquisition stamp (in milliseconds).
        
            Parameters:
                acqStampMillis (long): the acquisition stamp to set (in milliseconds)
        
        
        """
        ...
    def setCycleStamp(self, long: int) -> None:
        """
            Sets the cycle stamp (in nanoseconds).
        
            Parameters:
                cycleStamp (long): the cycle stamp to set (in nanoseconds)
        
        
        """
        ...
    def setCycleStampMillis(self, long: int) -> None:
        """
            Sets the cycle stamp (in milliseconds).
        
            Parameters:
                cycleStampMillis (long): the cycle stamp to set (in milliseconds)
        
        
        """
        ...
    def setFirstUpdate(self, boolean: bool) -> None:
        """
        
            Parameters:
                firstUpdate (boolean): the first-update to set
        
        
        """
        ...
    def setImmediateUpdate(self, boolean: bool) -> None:
        """
        
            Parameters:
                immediateUpdate (boolean): the immediate update to set
        
        
        """
        ...
    def setSelector(self, selector: cern.japc.core.Selector) -> None:
        """
            Sets the selector.
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the selector to set
        
        
        """
        ...
    def setSetStamp(self, long: int) -> None:
        """
            Sets the last SET stamp (in nanoseconds).
        
            Parameters:
                setStamp (long): The last SET stamp to set (in nanoseconds)
        
        
        """
        ...
    def setSetStampMillis(self, long: int) -> None:
        """
            Sets the last SET stamp (in milliseconds).
        
            Parameters:
                setStampMillis (long): last SET stamp to set (in milliseconds)
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class AbstractParameter(AbstractImmutableParameter, cern.japc.core.Parameter):
    """
    public abstract class AbstractParameter extends :class:`~cern.japc.core.spi.AbstractImmutableParameter` implements :class:`~cern.japc.core.Parameter`
    
        Implements a simple Parameter with default implementation for all methods. This parameter delegates all set methods to a
        corresponding implementation method if the descriptor indicate they are supported. Else an exception is thrown
        indicating they are unsupported.
    """
    def __init__(self, string: str): ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.Parameter.setValue`
            Sets the value of this parameter for a given cycle asynchronously.
        
            More precisely this method sends the signal to transfert the given value to the parameter holder of this parameter. This
            method is asynchronous and should delegate the actual downloading to another process. When the given value will actually
            be received by the parameter holder is undefined and can be tracked using the given listener.
        
            The value is **activated** once received by the parameter holder.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.Parameter.setValue` in interface :class:`~cern.japc.core.Parameter`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
                value (cern.japc.value.ParameterValue): the value to set for this parameter
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener for the feedback
        
        public void setValue (:class:`~cern.japc.core.Selector` selector, cern.japc.value.ParameterValue value) throws :class:`~cern.japc.core.ParameterException`
        
            Description copied from interface: :meth:`~cern.japc.core.Parameter.setValue`
            Sets the value of this parameter for a given cycle synchronously.
        
            This method is synchronous and blocks until the parameter is set with the given value. The value is automatically
            activated once the method returns.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.Parameter.setValue` in interface :class:`~cern.japc.core.Parameter`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
                value (cern.japc.value.ParameterValue): the value to set for this parameter
        
            Raises:
                :class:`~cern.japc.core.ParameterException`: if a problem occurs preventing the value to be set or if the parameter does not support a set operation
        
        
        """
        ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...

class AbstractWeakSubscriptionSource(SubscriptionSource, cern.japc.core.ParameterValueListener):
    """
    public abstract class AbstractWeakSubscriptionSource extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.SubscriptionSource`, :class:`~cern.japc.core.ParameterValueListener`
    
        An abstract subscription source that keeps a weak reference on the registered subscription listener. As soon as the
        registered listener becomes unavailable (garbage collected), the subscription is terminated. This class manages the
        start and stop succession to guarantee that one is not called more than it should.
    
        For convenience, this class implements the interface :code:`ParameterValueListener` so that this source can be
        registered in place where a standard listener is expected (for the data feed).
    
        This class is not thread safe and should not be used concurrently without proper synchronization.
    """
    def __init__(self, string: str, selector: cern.japc.core.Selector): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`
            Notifies this listener that a problem occurred preventing the get/set to be done.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def getSelector(self) -> cern.japc.core.Selector:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.SubscriptionSource.getSelector`
            Returns the cycle selector on which this source is activated
        
            Specified by:
                :meth:`~cern.japc.core.spi.SubscriptionSource.getSelector` in interface :class:`~cern.japc.core.spi.SubscriptionSource`
        
            Returns:
                the possibly null cycle selector on which this source is activated
        
        
        """
        ...
    def initializeSubscriptionSource(self, parameterValueListener: cern.japc.core.ParameterValueListener) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.SubscriptionSource.initializeSubscriptionSource`
            Initializes this source with the listener to which forward all events of the subscription. This method must be called
            only once before start or stop methods are called.
        
            Specified by:
                :meth:`~cern.japc.core.spi.SubscriptionSource.initializeSubscriptionSource`Â in
                interfaceÂ :class:`~cern.japc.core.spi.SubscriptionSource`
        
            Parameters:
                listener (:class:`~cern.japc.core.ParameterValueListener`): the non null listener of the subscription.
        
        
        """
        ...
    def startSubscription(self) -> None: ...
    def stopSubscription(self) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.SubscriptionSource.stopSubscription`
            This method should perform the effective stop of the subscription on the target source and on the given cycle selector.
            The method must not do anything if the subscription is already stopped.
        
            Specified by:
                :meth:`~cern.japc.core.spi.SubscriptionSource.stopSubscription`Â in
                interfaceÂ :class:`~cern.japc.core.spi.SubscriptionSource`
        
        
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
                parName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...

class AcquiredParameterValueImpl(cern.japc.core.AcquiredParameterValue, UpdatableAcquiredParameterValue, java.io.Serializable):
    """
    public class AcquiredParameterValueImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.AcquiredParameterValue`, :class:`~cern.japc.core.spi.UpdatableAcquiredParameterValue`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Implements a simple AcquiredParameterValue with default implementation returning the properties set at construction time
        or using the provided setters. By default the Status is set to NONE.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, acquiredParameterValue: cern.japc.core.AcquiredParameterValue): ...
    @typing.overload
    def __init__(self, string: str, valueHeader: cern.japc.core.ValueHeader, parameterValue: cern.japc.value.ParameterValue): ...
    @typing.overload
    def __init__(self, string: str, parameterValue: cern.japc.value.ParameterValue): ...
    @typing.overload
    def __init__(self, string: str, parameterValue: cern.japc.value.ParameterValue, long: int, selector: cern.japc.core.Selector): ...
    @typing.overload
    def __init__(self, string: str, parameterValue: cern.japc.value.ParameterValue, long: int, long2: int, selector: cern.japc.core.Selector): ...
    def addAdditionalError(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.UpdatableAcquiredParameterValue.addAdditionalError`
            Set the additional error String to an AcquiredParameterValue
        
            Specified by:
                :meth:`~cern.japc.core.spi.UpdatableAcquiredParameterValue.addAdditionalError`Â in
                interfaceÂ :class:`~cern.japc.core.spi.UpdatableAcquiredParameterValue`
        
            Parameters:
                additionalError (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The additional error String to set.
        
        
        """
        ...
    def getAdditionalErrors(self) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.AcquiredParameterValue.getAdditionalErrors`
            Returns possible additional errors that could have occurred while trying to get additional dynamic data for this value.
            It can happen that in order to return this value, additional values such as status, unit, min or max have to be
            dynamically fetched. The method returns errors that could have happened while fetching those dynamic values.
        
            Specified by:
                :meth:`~cern.japc.core.AcquiredParameterValue.getAdditionalErrors`Â in
                interfaceÂ :class:`~cern.japc.core.AcquiredParameterValue`
        
            Returns:
                possible additional errors that could have occurred while trying to get additional dynamic data. The value returned can
                be null if there is no error.
        
        
        """
        ...
    def getDescriptor(self) -> cern.japc.value.ValueDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.AcquiredParameterValue.getDescriptor`
            Returns the descriptor of this value. This is the same descriptor as the one that could be obtained from the pararameter
            that returned the value. The descriptor provides meta information that describes the value.
        
            Specified by:
                :meth:`~cern.japc.core.AcquiredParameterValue.getDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.AcquiredParameterValue`
        
            Returns:
                a descriptor of this value.
        
        
        """
        ...
    def getHeader(self) -> cern.japc.core.ValueHeader:
        """
            Description copied from interface: :meth:`~cern.japc.core.AcquiredParameterValue.getHeader`
            Returns the header of this value
        
            Specified by:
                :meth:`~cern.japc.core.AcquiredParameterValue.getHeader` in interface :class:`~cern.japc.core.AcquiredParameterValue`
        
            Returns:
                the header of this value
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.AcquiredParameterValue.getParameterName`
            Returns the parameter name the value has been read from
        
            Specified by:
                :meth:`~cern.japc.core.AcquiredParameterValue.getParameterName`Â in
                interfaceÂ :class:`~cern.japc.core.AcquiredParameterValue`
        
            Returns:
                the parameter name the value has been read from
        
        
        """
        ...
    def getStatus(self) -> cern.japc.value.ValueStatus:
        """
            Description copied from interface: :meth:`~cern.japc.core.AcquiredParameterValue.getStatus`
            Returns the optional status of the value.
        
            Specified by:
                :meth:`~cern.japc.core.AcquiredParameterValue.getStatus` in interface :class:`~cern.japc.core.AcquiredParameterValue`
        
            Returns:
                the status of the value.
        
        
        """
        ...
    def getValue(self) -> cern.japc.value.ParameterValue:
        """
            Description copied from interface: :meth:`~cern.japc.core.AcquiredParameterValue.getValue`
            Returns the non null value received in this AcquiredParameterValue.
        
            Specified by:
                :meth:`~cern.japc.core.AcquiredParameterValue.getValue` in interface :class:`~cern.japc.core.AcquiredParameterValue`
        
            Returns:
                the non null value received in this AcquiredParameterValue.
        
        
        """
        ...
    def setDescriptor(self, valueDescriptor: cern.japc.value.ValueDescriptor) -> None:
        """
        
            Parameters:
                descriptor (cern.japc.value.ValueDescriptor): The valueDescriptor to set.
        
        
        """
        ...
    def setHeader(self, valueHeader: cern.japc.core.ValueHeader) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.UpdatableAcquiredParameterValue.setHeader`
            Set the :class:`~cern.japc.core.ValueHeader` to an AcquiredParameterValue
        
            Specified by:
                :meth:`~cern.japc.core.spi.UpdatableAcquiredParameterValue.setHeader`Â in
                interfaceÂ :class:`~cern.japc.core.spi.UpdatableAcquiredParameterValue`
        
            Parameters:
                header (:class:`~cern.japc.core.ValueHeader`): The ValueHeader to set.
        
        
        """
        ...
    def setParameterName(self, string: str) -> None:
        """
            Setter for parameter name.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name to set.
        
        
        """
        ...
    def setStatus(self, valueStatus: cern.japc.value.ValueStatus) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.UpdatableAcquiredParameterValue.setStatus`
            Set the :code:`ValueStatus` to an AcquiredParameterValue
        
            Specified by:
                :meth:`~cern.japc.core.spi.UpdatableAcquiredParameterValue.setStatus`Â in
                interfaceÂ :class:`~cern.japc.core.spi.UpdatableAcquiredParameterValue`
        
            Parameters:
                status (cern.japc.value.ValueStatus): The ValueStatus to set.
        
        
        """
        ...
    def setValue(self, parameterValue: cern.japc.value.ParameterValue) -> None:
        """
            Setter for parameter value.
        
            Parameters:
                value (cern.japc.value.ParameterValue): parameter value to set.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class CycleStampValuePeekingStrategy(FspvPeekingStrategy):
    """
    public class CycleStampValuePeekingStrategy extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.FspvPeekingStrategy`
    
        A :class:`~cern.japc.core.spi.FspvPeekingStrategy` which peeks a value by a cycle stamp.
    """
    def __init__(self, long: int): ...
    def getCycleStamp(self) -> int:
        """
            Returns the cycle stamp.
        
            Returns:
                the cycle stamp
        
        
        """
        ...
    def peek(self, circularBuffer: cern.accsoft.commons.util.collections.CircularBuffer[cern.japc.core.FailSafeParameterValue], boolean: bool) -> java.util.Collection[cern.japc.core.FailSafeParameterValue]: ...

class FirstValueInWindowPeekingStrategy(FspvPeekingStrategy):
    """
    public class FirstValueInWindowPeekingStrategy extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.FspvPeekingStrategy`
    
        Implementation of :class:`~cern.japc.core.spi.FspvPeekingStrategy` searching for the first value which has an
        acquisition stamp in a certain time window.
    
        This implementation ignores the exceptions while the timeout is not yet expired. If the timeout has expired and no
        suitable value found and the last update was an exception then the exception is returned.
    """
    def __init__(self, long: int, long2: int): ...
    def peek(self, circularBuffer: cern.accsoft.commons.util.collections.CircularBuffer[cern.japc.core.FailSafeParameterValue], boolean: bool) -> java.util.Collection[cern.japc.core.FailSafeParameterValue]: ...

class FspvCollectorImpl(cern.accsoft.commons.util.collections.AbstractValueCollector[cern.japc.core.FailSafeParameterValue], FspvCollector):
    """
    public class FspvCollectorImpl extends cern.accsoft.commons.util.collections.AbstractValueCollector<:class:`~cern.japc.core.FailSafeParameterValue`> implements :class:`~cern.japc.core.spi.FspvCollector`
    
        Default implementation of :class:`~cern.japc.core.spi.FspvCollector`.
    
        This collector can be used just as :class:`~cern.japc.core.ParameterValueListener` or can start monitoring on a
        parameter itself.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, parameter: cern.japc.core.Parameter, selector: cern.japc.core.Selector): ...
    @typing.overload
    def __init__(self, parameter: cern.japc.core.Parameter, selector: cern.japc.core.Selector, int: int): ...
    @typing.overload
    def __init__(self, int: int): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`
            Notifies this listener that a problem occurred preventing the get/set to be done.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                paramName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def startCollection(self) -> None: ...
    def stopCollection(self) -> None:
        """
            Stops the data collection.
        
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
                paramName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...

class LastBeforeTimestampStrategy(FspvPeekingStrategy):
    """
    public class LastBeforeTimestampStrategy extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.FspvPeekingStrategy`
    
        Strategy which peeks the value which is last before a certain timestamp.
    """
    def __init__(self, long: int): ...
    def peek(self, circularBuffer: cern.accsoft.commons.util.collections.CircularBuffer[cern.japc.core.FailSafeParameterValue], boolean: bool) -> java.util.Collection[cern.japc.core.FailSafeParameterValue]: ...

class MapParameterDescriptorImpl(ParameterDescriptorImpl, cern.japc.core.MapParameterDescriptor):
    """
    public class MapParameterDescriptorImpl extends :class:`~cern.japc.core.spi.ParameterDescriptorImpl` implements :class:`~cern.japc.core.MapParameterDescriptor`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, map: typing.Union[java.util.Map[str, cern.japc.core.SimpleParameterDescriptor], typing.Mapping[str, cern.japc.core.SimpleParameterDescriptor]]): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def get(self, string: str) -> cern.japc.core.SimpleParameterDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.MapParameterDescriptor.get`
            Returns the matching descriptor for the given named value
        
            Specified by:
                :meth:`~cern.japc.core.MapParameterDescriptor.get` in interface :class:`~cern.japc.core.MapParameterDescriptor`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the property field
        
            Returns:
                the matching descriptor for the given named value or null if no match
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.MapParameterDescriptor.getNames`
            Returns the name of all available property fields
        
            Specified by:
                :meth:`~cern.japc.core.MapParameterDescriptor.getNames` in interface :class:`~cern.japc.core.MapParameterDescriptor`
        
            Returns:
                the name of all available property fields
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def put(self, string: str, simpleParameterDescriptor: cern.japc.core.SimpleParameterDescriptor) -> None:
        """
            Adds a parameter descriptor for a field.
        
            Parameters:
                fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): field name
                descriptor (:class:`~cern.japc.core.SimpleParameterDescriptor`): descriptor
        
        
        """
        ...
    def remove(self, string: str) -> cern.japc.core.SimpleParameterDescriptor:
        """
            Removes a descriptor of a field.
        
            Parameters:
                fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): field name
        
            Returns:
                the removed descriptor
        
        
        """
        ...
    def size(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.MapParameterDescriptor.size`
            Returns the number of entries in this map if constant or the maximum number if not constant. -1 can be returned to
            signal that no information is know.
        
            Specified by:
                :meth:`~cern.japc.core.MapParameterDescriptor.size` in interface :class:`~cern.japc.core.MapParameterDescriptor`
        
            Returns:
                the number of entries in this map
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.japc.core.spi.ParameterDescriptorImpl.toString`Â in
                classÂ :class:`~cern.japc.core.spi.ParameterDescriptorImpl`
        
        
        """
        ...

class ParameterDecorator(ImmutableParameterDecorator, cern.japc.core.Parameter):
    """
    public class ParameterDecorator extends :class:`~cern.japc.core.spi.ImmutableParameterDecorator` implements :class:`~cern.japc.core.Parameter`
    
        :class:`~cern.japc.core.Parameter` decorator delegating all the methods to the embedded parameter.
    """
    def __init__(self, parameter: cern.japc.core.Parameter): ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.Parameter.setValue`
            Sets the value of this parameter for a given cycle asynchronously.
        
            More precisely this method sends the signal to transfert the given value to the parameter holder of this parameter. This
            method is asynchronous and should delegate the actual downloading to another process. When the given value will actually
            be received by the parameter holder is undefined and can be tracked using the given listener.
        
            The value is **activated** once received by the parameter holder.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Specified by:
                :meth:`~cern.japc.core.Parameter.setValue` in interface :class:`~cern.japc.core.Parameter`
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
                value (cern.japc.value.ParameterValue): the value to set for this parameter
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener for the feedback
        
        
        """
        ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...

class ParameterUrlImpl(ParameterUrl, java.io.Serializable):
    """
    public class ParameterUrlImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.ParameterUrl`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Class which parses full parameter name.
    
    
        **[protocol]://[service]/[device]/[property]#[field]**
    
    
    
          1.  protocol: protocol of parameter communication. Could be: rda, tgm, jms, http etc.
          2.  service: particular service (remote) providing the parameter requested.
          3.  device: device, containing property specified.
          4.  property: property specified.
          5.  field: property field specified.
    
    
    
        This class also can handle a special case of DIM parameters for sps2001. The syntax of these parameters is:
    
    
        **//SPS/AAA/BBB/CCC.DDD**
    
    
        In the future this special case should be removed.
    
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str, string5: str): ...
    def cloneWithoutField(self) -> ParameterUrl:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.ParameterUrl.cloneWithoutField`
            Returns the parameter URL representing the same parameter without field information
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.cloneWithoutField` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                the parameter URL representing the same parameter without field information
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getDeviceAndProperty(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.getDeviceAndProperty` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                the part of parameter name containing device and property only
        
        
        """
        ...
    def getDeviceName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.getDeviceName` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                Returns the deviceName.
        
        
        """
        ...
    def getFieldName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.getFieldName` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                Returns the fieldName.
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.getParameterName` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                Returns the parameter name
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.getPropertyName` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                Returns the propertyName.
        
        
        """
        ...
    def getProtocolName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.getProtocolName` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                Returns the protocolName.
        
        
        """
        ...
    def getServiceName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.getServiceName` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                Returns the serviceName.
        
        
        """
        ...
    def hasFieldName(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.hasFieldName` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                Returns true if the URL contains field information
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isDimParameter(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.isDimParameter` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                Returns true if the URL contains DIM parameter name
        
        
        """
        ...
    def isFull(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.japc.core.spi.ParameterUrl.isFull` in interface :class:`~cern.japc.core.spi.ParameterUrl`
        
            Returns:
                Returns true if the URL contains protocol and service information
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class PullSubscriptionStrategy(SubscriptionStrategy):
    """
    public class PullSubscriptionStrategy extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.SubscriptionStrategy`
    
        Implementation of the strategy that is waiting for the client to pull the data unless for the immediate update that are
        pushed anyway.
    
        Important to remember that first updates and immediate updates have cycleStamp=0.
    
        Another thing to notice is that this strategy can participate in a global request limited in time. That means that when
        :meth:`~cern.japc.core.spi.PullSubscriptionStrategy.peekValue` is called the strategy checks how much time it can spend
        at most. This is done with thread-local :class:`~cern.japc.core.spi.CumulativeWait` which keeps track on how long the
        global operation can still take. If the thread-local is not set then the local one is created and cleaned up at the and
        of the call. This functionality is important for parameter groups and working sets.
    """
    def __init__(self, parameterValueListener: cern.japc.core.ParameterValueListener, string: str): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.SubscriptionStrategy.exceptionOccured`
            Receives new exception for parameter.
        
            Specified by:
                :meth:`~cern.japc.core.spi.SubscriptionStrategy.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.spi.SubscriptionStrategy`
        
            Parameters:
                parName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def peekValue(self, long: int) -> cern.japc.core.AcquiredParameterValue: ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.SubscriptionStrategy.valueReceived`
            Receives new value for a parameter.
        
        
            Specified by:
                :meth:`~cern.japc.core.spi.SubscriptionStrategy.valueReceived`Â in
                interfaceÂ :class:`~cern.japc.core.spi.SubscriptionStrategy`
        
            Parameters:
                parName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...

class PushSubscriptionStrategy(SubscriptionStrategy):
    """
    public class PushSubscriptionStrategy extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.SubscriptionStrategy`
    
        Implementation of the strategy that simply push the values received to the client listener
    """
    def __init__(self, parameterValueListener: cern.japc.core.ParameterValueListener): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.SubscriptionStrategy.exceptionOccured`
            Receives new exception for parameter.
        
            Specified by:
                :meth:`~cern.japc.core.spi.SubscriptionStrategy.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.spi.SubscriptionStrategy`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def peekValue(self, long: int) -> cern.japc.core.AcquiredParameterValue: ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.SubscriptionStrategy.valueReceived`
            Receives new value for a parameter.
        
        
            Specified by:
                :meth:`~cern.japc.core.spi.SubscriptionStrategy.valueReceived`Â in
                interfaceÂ :class:`~cern.japc.core.spi.SubscriptionStrategy`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...

class SimpleParameterDescriptorImpl(ParameterDescriptorImpl, cern.japc.core.SimpleParameterDescriptor):
    """
    public class SimpleParameterDescriptorImpl extends :class:`~cern.japc.core.spi.ParameterDescriptorImpl` implements :class:`~cern.japc.core.SimpleParameterDescriptor`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...
    def get(self, string: str) -> cern.japc.core.SimpleParameterDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.MapParameterDescriptor.get`
            Returns the matching descriptor for the given named value
        
            Specified by:
                :meth:`~cern.japc.core.MapParameterDescriptor.get` in interface :class:`~cern.japc.core.MapParameterDescriptor`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the property field
        
            Returns:
                the matching descriptor for the given named value or null if no match
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.MapParameterDescriptor.getNames`
            Returns the name of all available property fields
        
            Specified by:
                :meth:`~cern.japc.core.MapParameterDescriptor.getNames` in interface :class:`~cern.japc.core.MapParameterDescriptor`
        
            Returns:
                the name of all available property fields
        
        
        """
        ...
    def size(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.core.MapParameterDescriptor.size`
            Returns the number of entries in this map if constant or the maximum number if not constant. -1 can be returned to
            signal that no information is know.
        
            Specified by:
                :meth:`~cern.japc.core.MapParameterDescriptor.size` in interface :class:`~cern.japc.core.MapParameterDescriptor`
        
            Returns:
                the number of entries in this map
        
        
        """
        ...

class SubscriptionHandleImpl(SubscriptionConfigurationImpl, cern.japc.core.SubscriptionHandle, cern.japc.core.ParameterValueListener):
    """
    public class SubscriptionHandleImpl extends :class:`~cern.japc.core.spi.SubscriptionConfigurationImpl` implements :class:`~cern.japc.core.SubscriptionHandle`, :class:`~cern.japc.core.ParameterValueListener`
    
        Implements a SubscriptionRequest referencing a value listener.
    """
    @typing.overload
    def __init__(self, immutableParameter: cern.japc.core.ImmutableParameter, subscriptionSource: SubscriptionSource, parameterValueListener: cern.japc.core.ParameterValueListener): ...
    @typing.overload
    def __init__(self, immutableParameter: cern.japc.core.ImmutableParameter, subscriptionSource: SubscriptionSource, parameterValueListener: cern.japc.core.ParameterValueListener, int: int): ...
    def exceptionOccured(self, string: str, string2: str, parameterException: cern.japc.core.ParameterException) -> None:
        """
            Notifies the registered listener that a problem occurred preventing the value to be received.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def getListener(self) -> cern.japc.core.ParameterValueListener:
        """
            Returns the non null registered listener.
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionHandle.getListener` in interface :class:`~cern.japc.core.SubscriptionHandle`
        
            Returns:
                the non null registered listener
        
        
        """
        ...
    def getParameter(self) -> cern.japc.core.ImmutableParameter:
        """
            Returns the parameter from which this request has been created
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionHandle.getParameter` in interface :class:`~cern.japc.core.SubscriptionHandle`
        
            Returns:
                the parameter from which this request has been created
        
        
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
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.SubscriptionHandle.stopMonitoring`
            Stops monitoring on this subscription request if it is not already stopped.
        
            Specified by:
                :meth:`~cern.japc.core.SubscriptionHandle.stopMonitoring` in interface :class:`~cern.japc.core.SubscriptionHandle`
        
        
        """
        ...
    def valueReceived(self, string: str, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> None:
        """
            Notifies this listener that a new value has been received.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterValueListener.valueReceived`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterValueListener`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received for the monitored parameter.
        
        
        """
        ...

class FailSafeParameterValueImpl(AcquiredParameterValueImpl, cern.japc.core.FailSafeParameterValue):
    """
    public class FailSafeParameterValueImpl extends :class:`~cern.japc.core.spi.AcquiredParameterValueImpl` implements :class:`~cern.japc.core.FailSafeParameterValue`
    
        Implements a value holder which can contain either a :code:`ParameterValue` or a
        :class:`~cern.japc.core.ParameterException`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, acquiredParameterValue: cern.japc.core.AcquiredParameterValue): ...
    @typing.overload
    def __init__(self, string: str, parameterException: cern.japc.core.ParameterException): ...
    @typing.overload
    def __init__(self, string: str, valueHeader: cern.japc.core.ValueHeader, parameterValue: cern.japc.value.ParameterValue): ...
    def exception(self) -> cern.japc.core.ParameterException: ...
    def getException(self) -> cern.japc.core.ParameterException:
        """
            Description copied from interface: :meth:`~cern.japc.core.FailSafeParameterValue.getException`
            Returns the possible exception in case of error.
        
            Specified by:
                :meth:`~cern.japc.core.FailSafeParameterValue.getException`Â in
                interfaceÂ :class:`~cern.japc.core.FailSafeParameterValue`
        
            Returns:
                the value received in this AcquiredParameterValue.
        
        
        """
        ...
    def getString(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.FailSafeParameterValue.getString`
            This utility method returns a string representing, either the :code:`ParameterValue` or the
            :class:`~cern.japc.core.ParameterException` contained in this object if the :code:`ParameterValue` is :code:`null`. It
            cannot return :code:`null`.
        
            Specified by:
                :meth:`~cern.japc.core.FailSafeParameterValue.getString` in interface :class:`~cern.japc.core.FailSafeParameterValue`
        
            Returns:
                a string representing the value information as a string.
        
        
        """
        ...
    def isValue(self) -> bool:
        """
        
            Specified by:
                :code:`isValue` in interface :class:`~cern.japc.core.ParameterException`
        
        
        """
        ...
    def setValue(self, parameterValue: cern.japc.value.ParameterValue) -> None:
        """
            Description copied from class: :meth:`~cern.japc.core.spi.AcquiredParameterValueImpl.setValue`
            Setter for parameter value.
        
            Overrides:
                :meth:`~cern.japc.core.spi.AcquiredParameterValueImpl.setValue`Â in
                classÂ :class:`~cern.japc.core.spi.AcquiredParameterValueImpl`
        
            Parameters:
                value (cern.japc.value.ParameterValue): parameter value to set.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.japc.core.spi.AcquiredParameterValueImpl.toString`Â in
                classÂ :class:`~cern.japc.core.spi.AcquiredParameterValueImpl`
        
        
        """
        ...
    def value(self) -> cern.japc.core.AcquiredParameterValue: ...

class PullingSubscriptionSource(AbstractWeakSubscriptionSource):
    """
    public class PullingSubscriptionSource extends :class:`~cern.japc.core.spi.AbstractWeakSubscriptionSource`
    
        The subscription source which simulates the regular subscription by periodically doing "get" on a parameter. This source
        is used in case when a parameter doen't support regular subscription notification mechanism or if a client wants to
        force this kind of subscription mechanism.
    
        This class is not thread-safe. Stop/start subscription is not synchronized.
    """
    def __init__(self, selector: cern.japc.core.Selector, immutableParameter: cern.japc.core.ImmutableParameter): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi")``.

    AbstractImmutableParameter: typing.Type[AbstractImmutableParameter]
    AbstractParameter: typing.Type[AbstractParameter]
    AbstractWeakSubscriptionSource: typing.Type[AbstractWeakSubscriptionSource]
    AcquiredParameterValueImpl: typing.Type[AcquiredParameterValueImpl]
    CumulativeWait: typing.Type[CumulativeWait]
    CycleStampValuePeekingStrategy: typing.Type[CycleStampValuePeekingStrategy]
    DeviceDescriptorImpl: typing.Type[DeviceDescriptorImpl]
    DeviceDescriptorSupport: typing.Type[DeviceDescriptorSupport]
    FailSafeParameterValueImpl: typing.Type[FailSafeParameterValueImpl]
    FirstValueInWindowPeekingStrategy: typing.Type[FirstValueInWindowPeekingStrategy]
    FspvCollector: typing.Type[FspvCollector]
    FspvCollectorImpl: typing.Type[FspvCollectorImpl]
    FspvPeekingStrategy: typing.Type[FspvPeekingStrategy]
    IgnoreSetParameterDecorator: typing.Type[IgnoreSetParameterDecorator]
    ImmutableParameterDecorator: typing.Type[ImmutableParameterDecorator]
    LastBeforeTimestampStrategy: typing.Type[LastBeforeTimestampStrategy]
    MapParameterDescriptorImpl: typing.Type[MapParameterDescriptorImpl]
    ParameterDecorator: typing.Type[ParameterDecorator]
    ParameterDescriptorImpl: typing.Type[ParameterDescriptorImpl]
    ParameterDescriptorSupport: typing.Type[ParameterDescriptorSupport]
    ParameterUrl: typing.Type[ParameterUrl]
    ParameterUrlImpl: typing.Type[ParameterUrlImpl]
    PullSubscriptionStrategy: typing.Type[PullSubscriptionStrategy]
    PullingSubscriptionSource: typing.Type[PullingSubscriptionSource]
    PushSubscriptionStrategy: typing.Type[PushSubscriptionStrategy]
    SelectorImpl: typing.Type[SelectorImpl]
    SimpleParameterDescriptorImpl: typing.Type[SimpleParameterDescriptorImpl]
    SubscriptionConfigurationImpl: typing.Type[SubscriptionConfigurationImpl]
    SubscriptionHandleDecorator: typing.Type[SubscriptionHandleDecorator]
    SubscriptionHandleImpl: typing.Type[SubscriptionHandleImpl]
    SubscriptionSource: typing.Type[SubscriptionSource]
    SubscriptionStrategy: typing.Type[SubscriptionStrategy]
    UpdatableAcquiredParameterValue: typing.Type[UpdatableAcquiredParameterValue]
    ValueHeaderImpl: typing.Type[ValueHeaderImpl]
    adaptation: cern.japc.core.spi.adaptation.__module_protocol__
    arraycall: cern.japc.core.spi.arraycall.__module_protocol__
    beans: cern.japc.core.spi.beans.__module_protocol__
    cache: cern.japc.core.spi.cache.__module_protocol__
    factory: cern.japc.core.spi.factory.__module_protocol__
    group: cern.japc.core.spi.group.__module_protocol__
    jmx: cern.japc.core.spi.jmx.__module_protocol__
    provider: cern.japc.core.spi.provider.__module_protocol__
    subscription: cern.japc.core.spi.subscription.__module_protocol__
    transaction: cern.japc.core.spi.transaction.__module_protocol__
    util: cern.japc.core.spi.util.__module_protocol__
    value: cern.japc.core.spi.value.__module_protocol__
