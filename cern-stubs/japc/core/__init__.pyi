import cern.accsoft.commons.util
import cern.accsoft.commons.util.value
import cern.japc.core.device
import cern.japc.core.directory
import cern.japc.core.factory
import cern.japc.core.group
import cern.japc.core.spi
import cern.japc.core.support
import cern.japc.core.transaction
import cern.japc.core.trigger
import cern.japc.core.util
import cern.japc.value
import java.lang
import java.util
import typing



class AcquiredParameterValue:
    """
    public interface AcquiredParameterValue
    
        A class implementing this interface represents the value of a parameter that has been acquired from the device
        (typically a measurement). The value is dependent of the associated Parameter.
    """
    def getAdditionalErrors(self) -> typing.List[str]:
        """
            Returns possible additional errors that could have occurred while trying to get additional dynamic data for this value.
            It can happen that in order to return this value, additional values such as status, unit, min or max have to be
            dynamically fetched. The method returns errors that could have happened while fetching those dynamic values.
        
            Returns:
                possible additional errors that could have occurred while trying to get additional dynamic data. The value returned can
                be null if there is no error.
        
        
        """
        ...
    def getDescriptor(self) -> cern.japc.value.ValueDescriptor:
        """
            Returns the descriptor of this value. This is the same descriptor as the one that could be obtained from the pararameter
            that returned the value. The descriptor provides meta information that describes the value.
        
            Returns:
                a descriptor of this value.
        
        
        """
        ...
    def getHeader(self) -> 'ValueHeader':
        """
            Returns the header of this value
        
            Returns:
                the header of this value
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
            Returns the parameter name the value has been read from
        
            Returns:
                the parameter name the value has been read from
        
        
        """
        ...
    def getStatus(self) -> cern.japc.value.ValueStatus:
        """
            Returns the optional status of the value.
        
            Returns:
                the status of the value.
        
        
        """
        ...
    def getValue(self) -> cern.japc.value.ParameterValue:
        """
            Returns the non null value received in this AcquiredParameterValue.
        
            Returns:
                the non null value received in this AcquiredParameterValue.
        
        
        """
        ...

class DeviceDescriptor:
    """
    public interface DeviceDescriptor
    
        A class implementing this interface represents a holder of parameters.
    
        A device holds one or more parameters. A device can belongs to a specific family
    """
    IMPL_FESA: typing.ClassVar[int] = ...
    """
    static final short IMPL_FESA
    
        Enumerated device implementation=1.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IMPL_GM: typing.ClassVar[int] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` static final short IMPL_GM
    
        Deprecated.
        Not used anymore from LS2
        Enumerated device implementation=2.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IMPL_SLEQP: typing.ClassVar[int] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` static final short IMPL_SLEQP
    
        Deprecated.
        Not used anymore from LS2
        Enumerated device implementation=3.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IMPL_BISCOTO: typing.ClassVar[int] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` static final short IMPL_BISCOTO
    
        Deprecated.
        Not used anymore from LS2
        Enumerated device implementation=4.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IMPL_HARDWARE: typing.ClassVar[int] = ...
    """
    static final short IMPL_HARDWARE
    
        Enumerated device implementation=5.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IMPL_VIRTUAL: typing.ClassVar[int] = ...
    """
    static final short IMPL_VIRTUAL
    
        Enumerated device implementation=6.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IMPL_FGC: typing.ClassVar[int] = ...
    """
    static final short IMPL_FGC
    
        Enumerated device implementation=7.
    
        Also see:
            :meth:`~constant`
    
    
    """
    IMPL_UNKNOWN: typing.ClassVar[int] = ...
    """
    static final short IMPL_UNKNOWN
    
        Enumerated device implementation=9.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getControlProperty(self) -> str: ...
    def getDescription(self) -> str:
        """
            Returns an optional description of this device
        
            Returns:
                an optional description of this device or null
        
        
        """
        ...
    def getDeviceClassDescription(self) -> str:
        """
            Returns the description of the device class.
        
            Returns:
                an optional description of this device class.
        
        
        """
        ...
    def getDeviceClassName(self) -> str:
        """
            Returns the name of the device class.
        
            Returns:
                device class name
        
        
        """
        ...
    def getExtraCharacteristic(self, string: str) -> str:
        """
            Returns the value of the characteristic of the device defined by the given name. If no characteristic of that name is
            defined for this parameter the value returned is null.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the extra characteristic to get
        
            Returns:
                the value of the characteristic of the device defined by the given name.
        
        
        """
        ...
    def getExtraCharacteristicNames(self) -> typing.List[str]:
        """
            Returns the names of the possible extra characteristic of the device. The returned value is guaranted to be non null. It
            is an array that is possibly empty.
        
            Returns:
                the names of the possible extra characteristic of the device.
        
        
        """
        ...
    def getHostName(self) -> str:
        """
            Returns the device host name. If no location is defined null can be returned.
        
            Returns:
                the device host name.
        
        
        """
        ...
    def getImplementation(self) -> int:
        """
            Returns the device implementation: :meth:`~cern.japc.core.DeviceDescriptor.IMPL_FESA`,
            :meth:`~cern.japc.core.DeviceDescriptor.IMPL_GM`, :meth:`~cern.japc.core.DeviceDescriptor.IMPL_SLEQP`,
            :meth:`~cern.japc.core.DeviceDescriptor.IMPL_BISCOTO`, :meth:`~cern.japc.core.DeviceDescriptor.IMPL_HARDWARE`,
            :meth:`~cern.japc.core.DeviceDescriptor.IMPL_VIRTUAL`, :meth:`~cern.japc.core.DeviceDescriptor.IMPL_UNKNOWN`
        
            Returns:
                the device implementation.
        
        
        """
        ...
    def getLogicalLocation(self) -> str:
        """
            Returns the device location (Accelerator, transfert line name, etc). If no location is defined null can be returned.
        
            Returns:
                the device location (Accelerator, transfert line name, etc).
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns the name of this device.
        
            Returns:
                the name of this device.
        
        
        """
        ...
    def getResetProperty(self) -> str: ...
    def getStatusProperty(self) -> str:
        """
            Returns the device main STATUS property name. If no property is defined null can be returned.
        
            Returns:
                the device main STATUS property name.
        
        
        """
        ...
    def getTgmName(self) -> str:
        """
            Returns the device TGM machine name. If no TGM machine is defined null can be returned.
        
            Returns:
                the device TGM machine name.
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
            Returns :code:`true` if this device is cycle-bound, meaning that updates of at least one of its acquisition properties
            are valid only for the cycle when the acquisition has been done. More details can be found in "Device Property behaviour
            and contextual data" EDMS document: [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Returns:
                :code:`true` if this device is cycle-bound
        
        
        """
        ...
    def isCycleDependent(self) -> bool:
        """
            Returns :code:`true` if the device is dependent on the cycle. It means that it is either a multiplexed or cycle-bound.
            More details can be found in "Device Property behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Returns:
                :code:`true` if the device is dependent on the cycle
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Returns :code:`true` if this device is multiplexed, meaning at least one of its setting properties is capable of storing
            settings for different timing users. More details can be found in "Device Property behaviour and contextual data" EDMS
            document: [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Returns:
                :code:`true` if this device is multiplexed
        
        
        """
        ...

class ImmutableParameter(cern.accsoft.commons.util.Named):
    """
    public interface ImmutableParameter extends cern.accsoft.commons.util.Named
    
        A class implementing this interface represents a parameter on a given entity.
    
        It is a measurable variable associated to a given entity called device which is the holder of the parameter. A device
        can be a physical equipment as well as a virtual or logical entity such as SPSRing.
    
        A parameter is identified by its name which is made of the name of the device it belongs to and the name of the property
        on that device that the parameter represents. For instance a parameter can be :
    
        .. code-block: java
        
         SPSRing / tune
         
        where the logical device is SPSRing and the property is tune. Another example would be
    
        .. code-block: java
        
         MPSH4140 / State
         
        where the device is a physical equipment and the property is State.
    
        This version of parameter does not support setting making the parameter immutable. An immutable parameter can be
        monitorable.
    
        A parameter is thread safe. It can be shared and accessed concurrently.
    """
    def createSubscription(self, selector: 'Selector', parameterValueListener: 'ParameterValueListener') -> 'SubscriptionHandle':
        """
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
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the cycle selector on which to monitor the parameter
                parameterValueListener (:class:`~cern.japc.core.ParameterValueListener`): the listener that will received the notification for that request
        
            Returns:
                the subscription handle that can be used to monitor this parameter.
        
            Raises:
                :class:`~cern.japc.core.ParameterRuntimeException`: if the monitoring is not supported by this parameter (see :code:`isMonitorable()` on the descriptor of the parameter.
        
        
        """
        ...
    def getDeviceName(self) -> str:
        """
            Returns the name of the device holding this parameter.
        
            Returns:
                the name of the device holding this parameter
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns the name that identified this parameter. The name of the parameter is formed by concatenating the name of the
            device that holds this parameter with the name of the property the parameter represents. For instance : [device
            name]/[property name]. The separator used is chosen by the ParameterFactory that creates the parameters.
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                the name identifying this parameter
        
        
        """
        ...
    def getParameterDescriptor(self) -> 'ParameterDescriptor':
        """
            Returns a descriptor of this parameter. The descriptor provides information that describes the parameter.
        
            Returns:
                a descriptor of this parameter
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
            Returns the name of the property represented by this parameter.
        
            Returns:
                the name of the property represented by this parameter
        
        
        """
        ...
    @typing.overload
    def getValue(self, selector: 'Selector') -> AcquiredParameterValue:
        """
            Reads asynchronously the value of this parameter for the given selector. The provider listener is notified of the value
            read or if a problem occurs.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null for cycle independent parameter
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener to notify when the value is read or when a problem occurs
        
        
        """
        ...
    @typing.overload
    def getValue(self, selector: 'Selector', parameterValueListener: 'ParameterValueListener') -> None: ...
    def getValueDescriptor(self) -> cern.japc.value.ValueDescriptor:
        """
            Returns a descriptor of the value returned by this parameter. The descriptor provides meta information that describes
            the value.
        
            Returns:
                a descriptor of this value.
        
        
        """
        ...

class ObjectDescriptor(cern.japc.value.ValueDescriptor):
    """
    public interface ObjectDescriptor extends cern.japc.value.ValueDescriptor
    
        A class implementing this interface provides a description on a parameter value that holds an abitrary object.
    """
    def getDescription(self) -> str:
        """
            Returns an optional description of this value. If no description is defined null is returned.
        
            Returns:
                an optional description of this value or null
        
        
        """
        ...

class ObjectParameterValue(cern.japc.value.ParameterValue):
    """
    public interface ObjectParameterValue extends cern.japc.value.ParameterValue
    
        This parameter value holds an arbitrary object. There must be an agreement between the source and the client on the type
        of the object passed in order for that type to be useful.
    """
    def getValue(self) -> typing.Any:
        """
            Returns the value hold by this ParameterValue. The value returned can be null.
        
            Returns:
                the possibly null value hold by this ParameterValue
        
        
        """
        ...
    def makeMutable(self) -> 'ObjectParameterValue':
        """
        
            Specified by:
                :code:`makeMutable` in interface :code:`cern.japc.value.ParameterValue`
        
        
        """
        ...
    def setValue(self, object: typing.Any) -> None:
        """
            Sets the value of this ParameterValue. The given value can bu null.
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the possibly null value of this parameter value.
        
        
        """
        ...

class ParameterCharacteristics:
    """
    public interface ParameterCharacteristics
    
        Describes desired characteristics of a parameter to create. Basicly 2 implementations exist:
    
    
    
          - :code:`ParameterCharacteristicsImpl` is used by clients to pass some information about parameter to be created (ex.
            wildcard functionality needed)
          - :class:`~cern.japc.core.spi.factory.InternalParameterCharacteristics` is used inside ParameterFactory to keep track of
            parameter creation process.
    """
    PARAMETER_CHARACTERISTIC_ARRAY_CALL_ID: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETER_CHARACTERISTIC_ARRAY_CALL_ID
    
        Key to store/retrieve parameter the "array call" characteristic in ParameterCharacteristics map.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getAdditionalInformation(self) -> java.util.Map[str, typing.Any]: ...
    def isWildcardSubscriptionParameter(self) -> bool:
        """
            Returns true if wildcard functionality must be available for a parameter
        
            Returns:
                true if wildcard functionality must be available for a parameter
        
        
        """
        ...

class ParameterDescriptor:
    """
    public interface ParameterDescriptor
    
        Contains static information about a parameter, which is valid over the whole lifetime of the parameter and for all
        interactions (get/set/subscribe) it is used for.
    
        A Parameter Descriptor always exists, even if the parameter itself is invalid (e.g. if it was instantiated with a wrong
        device name)
    
        This interface group together methods that describe a given parameter. That information is available directly on the
        parameter but the parameter itself can delegate those informational methods to an internal descriptor.
    """
    def castAsMap(self) -> 'MapParameterDescriptor':
        """
            Returns this descriptor casted as a :class:`~cern.japc.core.MapParameterDescriptor`
        
            Returns:
                this descriptor casted as a :class:`~cern.japc.core.MapParameterDescriptor`
        
        
        """
        ...
    def castAsSimple(self) -> 'SimpleParameterDescriptor':
        """
            Returns this descriptor casted as a :class:`~cern.japc.core.SimpleParameterDescriptor`
        
            Returns:
                this descriptor casted as a :class:`~cern.japc.core.SimpleParameterDescriptor`
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Returns an optional description of this parameter
        
            Returns:
                an optional description of this parameter or null
        
        
        """
        ...
    def getExtraCharacteristic(self, string: str) -> str:
        """
            Returns the value of the characteristic of the parameter defined by the given name. If no characteristic of that name is
            defined for this parameter the value returned is null.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the extra characteristic to get
        
            Returns:
                the value of the characteristic of the parameter defined by the given name.
        
        
        """
        ...
    def getExtraCharacteristicNames(self) -> typing.List[str]:
        """
            Returns the names of the possible extra characteristics of the parameter. The returned value is guaranteed to be non
            null. It is an array that is possibly empty.
        
            Returns:
                the names of the possible extra characteristic of the parameter.
        
        
        """
        ...
    def getType(self) -> cern.japc.value.Type:
        """
            Returns the type of this parameter descriptor. Which is SIMPLE here due to backward compatibility reasons. Same as
            :code:`ValueDescriptor.getType()`
        
            Returns:
                the type of this parameter descriptor
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
            Returns :code:`true` if this parameter is a cycle-bound acquisition parameter. More details can be found in "Device
            Property behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs] **** All the operations (get,
            subscribe) with cycle-bound parameters require a proper non-empty cycle selector.
        
            Returns:
                :code:`true` if this parameter is a cycle-bound acquisition parameter
        
        
        """
        ...
    def isCycleDependent(self) -> bool:
        """
            Returns :code:`true` if the parameter is dependent on the cycle. It means that it is either a multiplexed setting or
            cycle-bound acquisition parameter. More details can be found in "Device Property behaviour and contextual data" EDMS
            document: [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs] **** All the operations
            (get, set, subscribe) with cycle-dependent parameters require a proper non-empty cycle selector.
        
            Returns:
                :code:`true` if the parameter is dependent on the cycle.
        
        
        """
        ...
    def isFilterable(self) -> bool:
        """
            Returns :code:`true` if the parameter described by this descriptor can be filtered. If the filtering is supported, it is
            possible to pass a filter on the parameter to control what part of the value is returned. The default value is
            :code:`false`.
        
        
            Returns:
                :code:`true` if the parameter described by this descriptor can be filtered.
        
        
        """
        ...
    def isMonitorable(self) -> bool:
        """
            Returns true if the parameter support monitoring and false else. If the parameter does not support monitoring a call to
            the method :code:`startMonitoring` will throw an exception.
        
            Returns:
                true if the parameter support monitoring and false else.
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Returns :code:`true` if this parameter is a multiplexed setting parameter. More details can be found in "Device Property
            behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs] **** All the operations (get, set,
            subscribe) with multiplexed parameters require a proper non-empty cycle selector.
        
            Returns:
                :code:`true` if this parameter is a multiplexed setting parameter
        
        
        """
        ...
    def isReadable(self) -> bool:
        """
            Returns true if this parameter is readable which means that it does support the get methods.
        
            Returns:
                boolean true if the get/monitor methods are supported false else.
        
        
        """
        ...
    def isTransactional(self) -> bool:
        """
            Returns true if this parameter supports transaction on the set. If the parameter does not support transaction an attempt
            to set a value using a transaction will throw an exception.
        
            Returns:
                true is this parameter supports transaction on the set, false else.
        
        
        """
        ...
    def isValueMutable(self) -> bool:
        """
            Returns true if the value returned from JAPC (read or as an update) must be mutable. By default all the values coming
            from JAPC are immutable to guarantee thread-safety of the value.
        
            Returns:
                true if the value returned from JAPC must be mutable and false otherwise
        
        
        """
        ...
    def isWritable(self) -> bool:
        """
            Returns true if this parameter is mutable which means that it does support the setValue methods.
        
            Returns:
                boolean true if the set methods are supported false else.
        
        
        """
        ...

class ParameterException(java.lang.Exception):
    """
    public class ParameterException extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`
    
        Thrown when a problem occurs while dealing with parameters
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: 'ValueHeader'): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: 'ValueHeader', int: int): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, int: int): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, long: int, selector: 'Selector'): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, long: int, selector: 'Selector', int: int): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, long: int, long2: int, selector: 'Selector'): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    def getCode(self) -> int:
        """
            Returns an int value representing the error Code. If no error Code is provided when the exception is build 0 is
            returned.
        
            Returns:
                an int value representing the error Code.
        
        
        """
        ...
    def getCycleStamp(self) -> int:
        """
            Returns a long identifying on which cycle stamp the error occurred
        
            Returns:
                The error cycle stamp value
        
        
        """
        ...
    def getHeader(self) -> 'ValueHeader':
        """
        
            Returns:
                the header
        
        
        """
        ...
    def getSelector(self) -> 'Selector':
        """
            Returns a cycle selector corresponding to the cycle stamp (if available)
        
            Returns:
                a cycle selector corresponding to the cycle stamp (if available)
        
        
        """
        ...

class ParameterExplorer:
    """
    public interface ParameterExplorer
    
        A class implementing this interface provide a way to browse the devices and parameters through their relationships.
    
        We consider here a parameter model where parameters have the following relationship between them :
    
          - **source** : a parameter *A* is source of another parameter *B* if the value of B depend or is related to the value of
            *A*. If *A* is source of *B* it implies that *B* is dependent of *A*.
          - **dependent** : a parameter *A* is dependent of another parameter *B* if the value of *A* depend or is related to the
            value of *B*. If *A* is dependent of *B* it implies that *B* is source of *A*.
          - **root parameter** : not a relationship but a property a parameter can have if it doesn't have any source parameter. *A*
            is a root parameter if there is no parameter *B* such as *B* is source of *A*.
    
    
        In addition to this model, the parameter do belongs to a device (physical, logical or virtuel). They represent a
        property on a device. Therefore, it is also possible to browse the parameters by asking the list of properties belonging
        to a given device.
    
        This explorer also allow to retrieve the list of accelarators and the list of devices. It is possible to browse from the
        accelerators, down to the devices, down to the properties and the parameters.
    """
    def getAcceleratorNames(self, boolean: bool) -> typing.List[str]:
        """
            Returns the list of all known accelerators.
        
            Parameters:
                operationalOnly (boolean): if true only operational accelerators are returned. If false all accelerators regardless.
        
            Returns:
                the list of all known accelerators.
        
        
        """
        ...
    def getDependentParameterNames(self, string: str) -> typing.List[str]:
        """
            Returns the names of the dependent parameters of the given parameter. The value returned is null only if the given
            parameterName does not match any known parameter. Otherwise the value returned is guarantee to be a non null array of
            String (possibly empty)
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to get the dependent parameters for
        
            Returns:
                the names of the dependent parameters of the given parameter or null if the parameter name is not known.
        
        
        """
        ...
    def getDeviceNamesForAccelerator(self, string: str, filter: 'ParameterExplorer.Filter') -> typing.List[str]:
        """
            Returns the list of all device names for a given accelerator.
        
            Parameters:
                accelerator (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the accelerator to get the devices for
                deviceNameFilter (:class:`~cern.japc.core.ParameterExplorer.Filter`): an eventual filter for the devices to return
        
            Returns:
                the list of all devices matching the criterias.
        
        
        """
        ...
    def getDeviceNamesForHost(self, string: str, filter: 'ParameterExplorer.Filter') -> typing.List[str]:
        """
            Returns the list of all device names for a given host.
        
            Parameters:
                hostname (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the host to get the devices for
                deviceNameFilter (:class:`~cern.japc.core.ParameterExplorer.Filter`): an eventual filter for the devices to return
        
            Returns:
                the list of all devices matching the criterias.
        
        
        """
        ...
    def getFamilyNamesForAccelerator(self, string: str, filter: 'ParameterExplorer.Filter') -> typing.List[str]:
        """
            Returns the list of all family names for a given accelerator.
        
            Parameters:
                accelerator (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the accelerator to get the families for
                familyNameFilter (:class:`~cern.japc.core.ParameterExplorer.Filter`): an eventual filter for the families to return
        
            Returns:
                the list of all families matching the criterias.
        
        
        """
        ...
    def getFamilyNamesForHost(self, string: str, filter: 'ParameterExplorer.Filter') -> typing.List[str]:
        """
            Returns the list of all family names for a given host.
        
            Parameters:
                hostname (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the host to get the families for
                familyNameFilter (:class:`~cern.japc.core.ParameterExplorer.Filter`): an eventual filter for the families to return
        
            Returns:
                the list of all families matching the criterias.
        
        
        """
        ...
    def getHostNamesForAccelerator(self, string: str, filter: 'ParameterExplorer.Filter') -> typing.List[str]:
        """
            Returns the list of all host names for a given accelerator.
        
            Parameters:
                accelerator (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the accelerator to get the host names for
                hostNameFilter (:class:`~cern.japc.core.ParameterExplorer.Filter`): an eventual filter for the host names to return
        
            Returns:
                the list of all host names matching the criterias.
        
        
        """
        ...
    def getPropertyNameDescriptions(self, string: str) -> typing.List['ParameterExplorer.NameDescription']:
        """
            Returns together the names and the description of all properties supported by given device.
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the device to get the properties and the descriptions for
        
            Returns:
                together the names and the description of all properties supported by the device. A device with no properties should
                return an empty array. If the device does not exist the returned value should be null.
        
        
        """
        ...
    def getRootParameterNames(self) -> typing.List[str]:
        """
            Returns the names of the root parameters. The value returned is never null but can be an empty array if this explorer
            doesn't define any root parameters.
        
            Returns:
                the names of the root parameters
        
        
        """
        ...
    def getSourceParameterNames(self, string: str) -> typing.List[str]:
        """
            Returns the names of the source parameters of the given parameter. The value returned is null only if the given
            parameterName does not match any known parameter. Otherwise the value returned is guarantee to be a non null array of
            String (possibly empty)
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to get the source parameters for
        
            Returns:
                the names of the source parameters of the given parameter or null if the parameter name is not known.
        
        
        """
        ...
    class Filter:
        def getFilteredValues(self) -> typing.List[str]: ...
    class NameDescription:
        def getDescription(self) -> str: ...
        def getName(self) -> str: ...

class ParameterRuntimeException(java.lang.RuntimeException):
    """
    public class ParameterRuntimeException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
        Thrown when a problem occurs with a hardware transaction.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ParameterValueListener:
    """
    public interface ParameterValueListener
    
        Defines a listener of values received or set on a parameter.
    """
    def exceptionOccured(self, string: str, string2: str, parameterException: ParameterException) -> None:
        """
            Notifies this listener that a problem occurred preventing the get/set to be done.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter on which the problem has occurred.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a non null description of the problem that occurred
                exception (:class:`~cern.japc.core.ParameterException`): an exception possibly null representing the problem that occurred
        
        
        """
        ...
    def valueReceived(self, string: str, acquiredParameterValue: AcquiredParameterValue) -> None:
        """
            Notifies this listener that a new value has been received (get or monitor) or set to the parameter. In the case of the
            notification of the set the value can be null.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter for which the value has been received or set.
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the new value received from a get/set or monitor or null in case of set where the value is optional.
        
        
        """
        ...

class Parameters:
    @staticmethod
    def appendFieldName(string: str, string2: str) -> str: ...
    @typing.overload
    @staticmethod
    def buildParameterName(string: str, string2: str) -> str: ...
    @typing.overload
    @staticmethod
    def buildParameterName(string: str, string2: str, string3: str) -> str: ...
    @staticmethod
    def extractDeviceAndProperty(string: str) -> str: ...
    @staticmethod
    def extractDeviceName(string: str) -> str: ...
    @staticmethod
    def extractDevicesAndProperties(stringArray: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def extractDistinctDevicesAndProperties(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[str]: ...
    @staticmethod
    def extractFieldName(string: str) -> str: ...
    @staticmethod
    def extractPropertyAndField(string: str) -> str: ...
    @staticmethod
    def extractPropertyName(string: str) -> str: ...
    @staticmethod
    def getDevicePropertyNameSeparator() -> str: ...
    @staticmethod
    def getMaxValue(string: str, selector: 'Selector') -> float: ...
    @staticmethod
    def getMinValue(string: str, selector: 'Selector') -> float: ...
    @staticmethod
    def getPropertyFieldSeparator() -> str: ...
    @staticmethod
    def getUnit(string: str, selector: 'Selector') -> str: ...
    @staticmethod
    def hasFieldName(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isParameterName(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isParameterName(string: str, boolean: bool) -> bool: ...

class Selector:
    """
    public interface Selector
    
        Defines a global selector that includes an unique identifier of a cycle that is recognized by the hardware interfaces or
        a period at which data should be received. It also defines a data filter that allows to specify a subset of data to
        return.
    """
    PERIODIC_PULLING: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PERIODIC_PULLING
    
        String that can be used to create a subscription via pulling. A getValue is performed at regular interval.
    
        The valid syntax for PULL selectors is
    
        .. code-block: java
        
            PULL.[interval in ms]@[regular selector]
         
    
        where interval is the interval in milliseconds between 2 :code:`getValue` and :code:`regular selector` is the regular
        selector on which to perform the monitoring.
    
        For instance "PULL.400@SFTPRO" will perform a pulling every 400 milliseconds on the user SFTPRO.
    
        This type of cycle selector is useful for simulating a subscription on parameters that do not support it. The part
        @[regular selector] is optional. If no selector is specified it will be using a
        :meth:`~cern.japc.core.Selectors.NO_SELECTOR` one.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PERIODIC_2SEC: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PERIODIC_2SEC
    
        Periodic selector with 2 seconds period
    
        Also see:
            :meth:`~constant`
    
    
    """
    PERIODIC_4SEC: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PERIODIC_4SEC
    
        Periodic selector with 4 seconds period
    
        Also see:
            :meth:`~constant`
    
    
    """
    PERIODIC_16SEC: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PERIODIC_16SEC
    
        Periodic selector with 16 seconds period
    
        Also see:
            :meth:`~constant`
    
    
    """
    PERIODIC_64SEC: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PERIODIC_64SEC
    
        Periodic selector with 64 seconds period
    
        Also see:
            :meth:`~constant`
    
    
    """
    PERIODIC_256SEC: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PERIODIC_256SEC
    
        Periodic selector with 256 seconds period
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getDataFilter(self) -> cern.japc.value.ParameterValue:
        """
            Returns an optional filter on the data (can be :code:`null`). The filter can be used to request a subset of the data
            from the device (ex. specify sampling rate).
        
            Returns:
                an optional filter (can be :code:`null`)
        
        
        """
        ...
    def getId(self) -> str:
        """
            Returns string representation of the identifier of the cycle.
        
        
            Can be either:
        
        
        
              1.  empty string for non-cycle-dependent cases
              2.  TGM_NAME.GROUP.VALUE for cycle-dependent case, ex. SPS.USER.SFTPRO1
        
        
            Returns:
                string representation of the identifier of the cycle
        
        
        """
        ...
    def getPeriod(self) -> int:
        """
            For a periodic subscription, returns the period of the subscription in milliseconds or a negative number if the
            subscription is not periodic.
        
            Returns:
                the period length in milliseconds or a negative number if the subscription is not periodic
        
            Also see:
                :meth:`~cern.japc.core.Selector.isPeriodic`
        
        
        """
        ...
    def isPeriodic(self) -> bool:
        """
            Returns a boolean which says if the Selector correspond to a periodic subscription.
        
            Returns:
                true of the subscription is periodic
        
        
        """
        ...

class Selectors:
    NO_SELECTOR: typing.ClassVar[Selector] = ...
    NON_PPM_SELECTOR: typing.ClassVar[Selector] = ...
    USER_ALL_SUFFIX: typing.ClassVar[str] = ...
    @staticmethod
    def adapt(selector: Selector) -> 'Selectors.OngoingSelectorAdaptation': ...
    @staticmethod
    def adaptIfPossible(selector: Selector) -> 'Selectors.OngoingSelectorAdaptation': ...
    @staticmethod
    def assertSelectorIdValid(string: str) -> None: ...
    @staticmethod
    def assertSelectorValid(selector: Selector) -> None: ...
    @typing.overload
    @staticmethod
    def createUserAllSelector(string: str) -> Selector: ...
    @typing.overload
    @staticmethod
    def createUserAllSelector(string: str, parameterValue: cern.japc.value.ParameterValue) -> Selector: ...
    @staticmethod
    def createUserAllSelectorId(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def extractTimingDomain(selector: Selector) -> str: ...
    @typing.overload
    @staticmethod
    def extractTimingDomain(string: str) -> str: ...
    @staticmethod
    def isNoSelector(selector: Selector) -> bool: ...
    @staticmethod
    def isNoSelectorId(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isUserAllSelector(selector: Selector) -> bool: ...
    @typing.overload
    @staticmethod
    def isUserAllSelector(string: str) -> bool: ...
    @staticmethod
    def isUserAllSelectorId(string: str) -> bool: ...
    @staticmethod
    def isUserSelector(selector: Selector) -> bool: ...
    @staticmethod
    def isUserSelectorId(string: str) -> bool: ...
    class OngoingSelectorAdaptation:
        def to(self, immutableParameter: ImmutableParameter) -> Selector: ...

class SubscriptionConfigurator:
    """
    public interface SubscriptionConfigurator
    
        A class implementing this interface represents the configuration of a subscription.
    
        This configuration provides 2 ways to be notified of the values received. One is to received them through the listener,
        and the other one is to use an alternative method to fetch the value on demand (PULL_MODE).
    """
    PUSH_MODE: typing.ClassVar[int] = ...
    """
    static final int PUSH_MODE
    
        Use this constant to set this handle to the default mode where the listener is notified everytime the values are ready.
        The use of the method :code:`peekValues` does not affect the delivery of the value to the listener
    
        Also see:
            :meth:`~constant`
    
    
    """
    PULL_MODE: typing.ClassVar[int] = ...
    """
    static final int PULL_MODE
    
        Use this constant to set this handle to the mode where the listener is not notified when the values are ready. The
        method :code:`peekValues` must be used to retrieve the values when they are ready. The listener is never notified.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getDataDeliveryMode(self) -> int:
        """
            Returns the current mode of data delivery.
        
            Returns:
                the current mode of data delivery.
        
        
        """
        ...
    def getSelector(self) -> Selector:
        """
            Returns the cycle selector on which this request is activated
        
            Returns:
                the cycle selector on which this request is activated
        
        
        """
        ...
    def setDataDeliveryMode(self, int: int) -> None:
        """
            Sets the fetch mode of this handle to :code:`PUSH_MODE` or :code:`PULL_MODE`. Default is :code:`MODE_PUSH_ONLY`.
        
            Parameters:
                mode (int): the data delivery mode either :code:`PUSH_MODE` or :code:`PULL_MODE`
        
        
        """
        ...

class ValueHeader:
    """
    public interface ValueHeader
    
        A class implementing this interface represents a header providing information on a value.
    """
    def getAcqStamp(self) -> int:
        """
            Returns the acquisition Time Stamp (UTC in nanoseconds). It is the absolute time in nanoseconds this value has been
            acquired. If the timestamp is not known or not relevant the constant :code:`0` should be returned.
        
            Returns:
                the absolute time in nanoseconds this value has been acquired.
        
        
        """
        ...
    def getAcqStampMillis(self) -> int:
        """
            Returns the acquisition Time Stamp (UTC in milliseconds). It is the absolute time in milliseconds this value has been
            acquired. If the timestamp is not known or not relevant the constant :code:`0` should be returned.
        
            Returns:
                the absolute time in milliseconds this value has been acquired.
        
        
        """
        ...
    def getCycleStamp(self) -> int:
        """
            Returns unique time stamp that identifies a unique cycle occurrence. Time UTC (in nanoseconds). If the cycleStamp is not
            known or not relevant :code:`0` should be returned.
        
            Returns:
                the unique time stamp that identifies a unique cycle occurrence this value belongs to in nanoseconds
        
        
        """
        ...
    def getCycleStampMillis(self) -> int:
        """
            Returns unique time stamp that identifies a unique cycle occurrence. Time UTC (in milliseconds). If the cycleStamp is
            not known or not relevant :code:`0` should be returned.
        
            Returns:
                the unique time stamp that identifies a unique cycle occurrence this value belongs to in milliseconds
        
        
        """
        ...
    def getSelector(self) -> Selector:
        """
            Returns the Selector identifying the cycle the value stamped with this header is for. Null can be returned if the cycle
            is not relevant or unknown.
        
            Returns:
                the Selector identifying the cycle the value stamped with this header is for or null.
        
        
        """
        ...
    def getSetStamp(self) -> int:
        """
            Returns the last SET Time Stamp (UTC in nanoseconds). It is the absolute time in nanoseconds the last SET has been
            performed. If the timestamp is not known or not relevant the constant :code:`0` should be returned.
        
            Returns:
                the absolute time in nanoseconds of the last performed SET
        
        
        """
        ...
    def getSetStampMillis(self) -> int:
        """
            Returns the last SET Time Stamp (UTC in milliseconds). It is the absolute time in milliseconds the last SET has been
            performed. If the timestamp is not known or not relevant the constant :code:`0` should be returned.
        
            Returns:
                the absolute time in milliseconds of the last performed SET
        
        
        """
        ...
    def isFirstUpdate(self) -> bool:
        """
            Returns true if this value is coming the immediate update. The first time a subscription is started, a value is supposed
            to be sent immediately to reflect the current value of the parameter being monitored. This first value should have this
            flag set to true.
        
            Returns:
                true if this value is coming the first update.
        
        
        """
        ...
    def isImmediateUpdate(self) -> bool:
        """
            Returns true in case this value has been sent following a untriggered change in the value being monitored. In case of
            monitoring, values are expected to come when the given selector is trigged. In case the parameter is a writable value, a
            write operation can occur anytime and the new value is expected to be sent to all client monitoring the value. The new
            value is not sent because of a given trigger acting on the selector but because of an untriggered condition. The value
            sent should have this flag set to true to be distinguished from the regular update.
        
            Returns:
                true in case this value has been sent following a untriggered change in the value being monitored.
        
        
        """
        ...

class AuthorizationExpiredException(ParameterException):
    """
    public class AuthorizationExpiredException extends :class:`~cern.japc.core.ParameterException`
    
        Exception which is thrown/sent if the authorization has expired (for example, if RBA token has expired).
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class FailSafeParameterValue(AcquiredParameterValue, cern.accsoft.commons.util.value.FailSafe[ParameterException, AcquiredParameterValue]):
    """
    public interface FailSafeParameterValue extends :class:`~cern.japc.core.AcquiredParameterValue`, cern.accsoft.commons.util.value.FailSafe<:class:`~cern.japc.core.ParameterException`, :class:`~cern.japc.core.AcquiredParameterValue`>
    
        A class implementing this interface represents an AcquiredParameterValue where the value is not guaranteed. Two case are
        possible :
    
          - This AcquiredParameterValue is correct and the methods :code:`getHeader()` and :code:`getValue()` return a non null
            value. The method :code:`getException` returns a null value.
          - This AcquiredParameterValue is not correct because an exception occurred when it was read. In this case, the methods
            :code:`getHeader()` and :code:`getValue()` return a null value and the method :code:`getException` returns a non null
            value.
    
    
        This interface is particularly useful when returning an array of AcquiredParameterValue for many parameters where some
        of them could have succeeded and some of them failed.
    """
    def getException(self) -> ParameterException:
        """
            Returns the possible exception in case of error.
        
            Returns:
                the value received in this AcquiredParameterValue.
        
        
        """
        ...
    def getString(self) -> str:
        """
            This utility method returns a string representing, either the :code:`ParameterValue` or the
            :class:`~cern.japc.core.ParameterException` contained in this object if the :code:`ParameterValue` is :code:`null`. It
            cannot return :code:`null`.
        
            Returns:
                a string representing the value information as a string.
        
        
        """
        ...

class MapParameterDescriptor(ParameterDescriptor):
    """
    public interface MapParameterDescriptor extends :class:`~cern.japc.core.ParameterDescriptor`
    """
    def get(self, string: str) -> 'SimpleParameterDescriptor':
        """
            Returns the matching descriptor for the given named value
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the property field
        
            Returns:
                the matching descriptor for the given named value or null if no match
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
            Returns the name of all available property fields
        
            Returns:
                the name of all available property fields
        
        
        """
        ...
    def size(self) -> int:
        """
            Returns the number of entries in this map if constant or the maximum number if not constant. -1 can be returned to
            signal that no information is know.
        
            Returns:
                the number of entries in this map
        
        
        """
        ...

class NoDataAvailableException(ParameterException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, selector: Selector): ...
    @typing.overload
    def __init__(self, string: str, valueHeader: ValueHeader): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, selector: Selector): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: ValueHeader): ...

class NoValueException(ParameterException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, valueHeader: ValueHeader): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: ValueHeader): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, long: int, selector: Selector): ...
    @typing.overload
    def __init__(self, string: str, long: int): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class Parameter(ImmutableParameter):
    """
    public interface Parameter extends :class:`~cern.japc.core.ImmutableParameter`
    
        A class implementing this interface represents a parameter of a given entity. This version of parameter support setting
        and subscription.
    
        Setting the value of this parameter triggers setting the value on the parameter on the given entity such as a device.
    """
    @typing.overload
    def setValue(self, selector: Selector, parameterValue: cern.japc.value.ParameterValue) -> None:
        """
            Sets the value of this parameter for a given cycle asynchronously.
        
            More precisely this method sends the signal to transfert the given value to the parameter holder of this parameter. This
            method is asynchronous and should delegate the actual downloading to another process. When the given value will actually
            be received by the parameter holder is undefined and can be tracked using the given listener.
        
            The value is **activated** once received by the parameter holder.
        
            The cycle selector can be null for parameters that are not cycle dependent.
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): the identification of the cycle the value is for or null
                value (cern.japc.value.ParameterValue): the value to set for this parameter
                listener (:class:`~cern.japc.core.ParameterValueListener`): the listener for the feedback
        
        
        """
        ...
    @typing.overload
    def setValue(self, selector: Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: ParameterValueListener) -> None: ...

class SubscriptionHandle(SubscriptionConfigurator):
    """
    public interface SubscriptionHandle extends :class:`~cern.japc.core.SubscriptionConfigurator`
    
        A class implementing this interface represents the Subscription aspect of a Parameter. The fact to be monitorable is a
        characteristic of a parameter that allow to get periodic update on the value. A monitorable Parameter must provide a way
        to create implementation of this interface based on a listener.
    
        A SubscriptionHandle implementation is a private channel for a given listener. It must not be shared without proper
        synchronization.
    """
    def getListener(self) -> ParameterValueListener:
        """
            Returns the non null registered listener.
        
            Returns:
                the non null registered listener.
        
        
        """
        ...
    def getParameter(self) -> ImmutableParameter:
        """
            Returns the parameter for which this handle has been created
        
            Returns:
                the parameter for which this handle has been created
        
        
        """
        ...
    def isMonitoring(self) -> bool:
        """
            Returns true is this monitorable is currently monitoring the associated parameter
        
            Returns:
                true is the parameter is currently monitoring the value
        
        
        """
        ...
    def peekValue(self, long: int) -> AcquiredParameterValue: ...
    def startMonitoring(self) -> None: ...
    def stopMonitoring(self) -> None:
        """
            Stops monitoring on this subscription request if it is not already stopped.
        
        """
        ...

class SubscriptionProblemException(ParameterException):
    """
    public class SubscriptionProblemException extends :class:`~cern.japc.core.ParameterException`
    
        Thrown when a problem occurs during a subscription
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, valueHeader: ValueHeader): ...

class SubscriptionRecoveredException(ParameterException):
    """
    public class SubscriptionRecoveredException extends :class:`~cern.japc.core.ParameterException`
    
        Thrown when the subscription is recovered from problematic state. The reason is that client uses
        :class:`~cern.japc.core.ParameterValueListener` to get updates or exception reports. There is no way to inform client
        about recovered subscription. We can't use a special parameter value in
        :meth:`~cern.japc.core.ParameterValueListener.valueReceived`, because all the clients logic doesn't expect such a value.
        So the only choise to inform client is to use :meth:`~cern.japc.core.ParameterValueListener.exceptionOccured` with
        special exception which in certain cases will be treated in a certain way.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...

class WaitingForDataException(ParameterException):
    """
    public class WaitingForDataException extends :class:`~cern.japc.core.ParameterException`
    
        Exception which is thrown/sent if no data is received after a subscription creation.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class SimpleParameterDescriptor(MapParameterDescriptor):
    """
    public interface SimpleParameterDescriptor extends :class:`~cern.japc.core.MapParameterDescriptor`
    
        A class implementing this interface provides a description of a simple parameter that is not a composite parameter. This
        interface is only there for logical structure purpose.
    """
    ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core")``.

    AcquiredParameterValue: typing.Type[AcquiredParameterValue]
    AuthorizationExpiredException: typing.Type[AuthorizationExpiredException]
    DeviceDescriptor: typing.Type[DeviceDescriptor]
    FailSafeParameterValue: typing.Type[FailSafeParameterValue]
    ImmutableParameter: typing.Type[ImmutableParameter]
    MapParameterDescriptor: typing.Type[MapParameterDescriptor]
    NoDataAvailableException: typing.Type[NoDataAvailableException]
    NoValueException: typing.Type[NoValueException]
    ObjectDescriptor: typing.Type[ObjectDescriptor]
    ObjectParameterValue: typing.Type[ObjectParameterValue]
    Parameter: typing.Type[Parameter]
    ParameterCharacteristics: typing.Type[ParameterCharacteristics]
    ParameterDescriptor: typing.Type[ParameterDescriptor]
    ParameterException: typing.Type[ParameterException]
    ParameterExplorer: typing.Type[ParameterExplorer]
    ParameterRuntimeException: typing.Type[ParameterRuntimeException]
    ParameterValueListener: typing.Type[ParameterValueListener]
    Parameters: typing.Type[Parameters]
    Selector: typing.Type[Selector]
    Selectors: typing.Type[Selectors]
    SimpleParameterDescriptor: typing.Type[SimpleParameterDescriptor]
    SubscriptionConfigurator: typing.Type[SubscriptionConfigurator]
    SubscriptionHandle: typing.Type[SubscriptionHandle]
    SubscriptionProblemException: typing.Type[SubscriptionProblemException]
    SubscriptionRecoveredException: typing.Type[SubscriptionRecoveredException]
    ValueHeader: typing.Type[ValueHeader]
    WaitingForDataException: typing.Type[WaitingForDataException]
    device: cern.japc.core.device.__module_protocol__
    directory: cern.japc.core.directory.__module_protocol__
    factory: cern.japc.core.factory.__module_protocol__
    group: cern.japc.core.group.__module_protocol__
    spi: cern.japc.core.spi.__module_protocol__
    support: cern.japc.core.support.__module_protocol__
    transaction: cern.japc.core.transaction.__module_protocol__
    trigger: cern.japc.core.trigger.__module_protocol__
    util: cern.japc.core.util.__module_protocol__
