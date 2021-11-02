import cern.japc.core
import cern.japc.core.spi.cache
import cern.japc.value
import java.util
import typing



class CompositeParameterExplorer(cern.japc.core.ParameterExplorer):
    """
    public class CompositeParameterExplorer extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ParameterExplorer`
    
        This class allows the grouping of several parameter explorer as one. The result of each explorer is combined to make the
        result of this explorer.
    """
    def __init__(self, parameterExplorerArray: typing.List[cern.japc.core.ParameterExplorer]): ...
    def getAcceleratorNames(self, boolean: bool) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterExplorer.getAcceleratorNames`
            Returns the list of all known accelerators.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterExplorer.getAcceleratorNames` in interface :class:`~cern.japc.core.ParameterExplorer`
        
            Parameters:
                operationalOnly (boolean): if true only operational accelerators are returned. If false all accelerators regardless.
        
            Returns:
                the list of all known accelerators.
        
        
        """
        ...
    def getDependentParameterNames(self, string: str) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterExplorer.getDependentParameterNames`
            Returns the names of the dependent parameters of the given parameter. The value returned is null only if the given
            parameterName does not match any known parameter. Otherwise the value returned is guarantee to be a non null array of
            String (possibly empty)
        
            Specified by:
                :meth:`~cern.japc.core.ParameterExplorer.getDependentParameterNames`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterExplorer`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to get the dependent parameters for
        
            Returns:
                the names of the dependent parameters of the given parameter or null if the parameter name is not known.
        
        
        """
        ...
    def getDeviceNamesForAccelerator(self, string: str, filter: cern.japc.core.ParameterExplorer.Filter) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterExplorer.getDeviceNamesForAccelerator`
            Returns the list of all device names for a given accelerator.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterExplorer.getDeviceNamesForAccelerator`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterExplorer`
        
            Parameters:
                accelerator (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the accelerator to get the devices for
                deviceNameFilter (:class:`~cern.japc.core.ParameterExplorer.Filter`): an eventual filter for the devices to return
        
            Returns:
                the list of all devices matching the criterias.
        
        
        """
        ...
    def getDeviceNamesForHost(self, string: str, filter: cern.japc.core.ParameterExplorer.Filter) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterExplorer.getDeviceNamesForHost`
            Returns the list of all device names for a given host.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterExplorer.getDeviceNamesForHost` in interface :class:`~cern.japc.core.ParameterExplorer`
        
            Parameters:
                hostname (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the host to get the devices for
                deviceNameFilter (:class:`~cern.japc.core.ParameterExplorer.Filter`): an eventual filter for the devices to return
        
            Returns:
                the list of all devices matching the criterias.
        
        
        """
        ...
    def getFamilyNamesForAccelerator(self, string: str, filter: cern.japc.core.ParameterExplorer.Filter) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterExplorer.getFamilyNamesForAccelerator`
            Returns the list of all family names for a given accelerator.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterExplorer.getFamilyNamesForAccelerator`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterExplorer`
        
            Parameters:
                accelerator (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the accelerator to get the families for
                familyNameFilter (:class:`~cern.japc.core.ParameterExplorer.Filter`): an eventual filter for the families to return
        
            Returns:
                the list of all families matching the criterias.
        
        
        """
        ...
    def getFamilyNamesForHost(self, string: str, filter: cern.japc.core.ParameterExplorer.Filter) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterExplorer.getFamilyNamesForHost`
            Returns the list of all family names for a given host.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterExplorer.getFamilyNamesForHost` in interface :class:`~cern.japc.core.ParameterExplorer`
        
            Parameters:
                hostname (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the host to get the families for
                familyNameFilter (:class:`~cern.japc.core.ParameterExplorer.Filter`): an eventual filter for the families to return
        
            Returns:
                the list of all families matching the criterias.
        
        
        """
        ...
    def getHostNamesForAccelerator(self, string: str, filter: cern.japc.core.ParameterExplorer.Filter) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterExplorer.getHostNamesForAccelerator`
            Returns the list of all host names for a given accelerator.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterExplorer.getHostNamesForAccelerator`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterExplorer`
        
            Parameters:
                accelerator (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the accelerator to get the host names for
                hostNameFilter (:class:`~cern.japc.core.ParameterExplorer.Filter`): an eventual filter for the host names to return
        
            Returns:
                the list of all host names matching the criterias.
        
        
        """
        ...
    def getPropertyNameDescriptions(self, string: str) -> typing.List[cern.japc.core.ParameterExplorer.NameDescription]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterExplorer.getPropertyNameDescriptions`
            Returns together the names and the description of all properties supported by given device.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterExplorer.getPropertyNameDescriptions`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterExplorer`
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the device to get the properties and the descriptions for
        
            Returns:
                together the names and the description of all properties supported by the device. A device with no properties should
                return an empty array. If the device does not exist the returned value should be null.
        
        
        """
        ...
    def getRootParameterNames(self) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterExplorer.getRootParameterNames`
            Returns the names of the root parameters. The value returned is never null but can be an empty array if this explorer
            doesn't define any root parameters.
        
            Specified by:
                :meth:`~cern.japc.core.ParameterExplorer.getRootParameterNames` in interface :class:`~cern.japc.core.ParameterExplorer`
        
            Returns:
                the names of the root parameters
        
        
        """
        ...
    def getSourceParameterNames(self, string: str) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterExplorer.getSourceParameterNames`
            Returns the names of the source parameters of the given parameter. The value returned is null only if the given
            parameterName does not match any known parameter. Otherwise the value returned is guarantee to be a non null array of
            String (possibly empty)
        
            Specified by:
                :meth:`~cern.japc.core.ParameterExplorer.getSourceParameterNames`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterExplorer`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to get the source parameters for
        
            Returns:
                the names of the source parameters of the given parameter or null if the parameter name is not known.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def mergeResults(nameDescriptionArray: typing.List[typing.List[cern.japc.core.ParameterExplorer.NameDescription]], int: int) -> typing.List[cern.japc.core.ParameterExplorer.NameDescription]:
        """
        public static final :class:`~cern.japc.core.ParameterExplorer.NameDescription`[] mergeResults (:class:`~cern.japc.core.ParameterExplorer.NameDescription`[][] results, int count)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def mergeResults(stringArray: typing.List[typing.List[str]], int: int) -> typing.List[str]: ...

class DescriptorContainer:
    """
    public interface DescriptorContainer
    
        An interface describing the descriptor container. Normally used by CustomizableDescriptorProvider. An implementing class
        should return Maps objects for device descriptors with device names as keys, parameter descriptors and value descriptors
        with parameter names as keys. An implementing class should have a constructor without arguments, because
        :class:`~cern.japc.core.spi.provider.CustomizableDescriptorProvider` uses Java Reflection to instantiate it.
    """
    def getDeviceDescriptors(self) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    def getParameterDescriptors(self) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def getValueDescriptors(self) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...

class DescriptorProvider:
    """
    public interface DescriptorProvider
    
        A class implementing this interface provides the needed descriptor to build parameters. Parameters implementation are
        reusable classes that need specific information for a given parameter. That specific information is stored in the
        descriptor. The provider is able to return those data.
    """
    SYSPROP_CDP_DATA_CONTAINERS: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_CDP_DATA_CONTAINERS
    
        System property to pass a ':'-separated list of DescriptorContainer classes names to ParameterFactory
    
        Also see:
            :meth:`~constant`
    
    
    """
    def findDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor:
        """
            Returns the device descriptor for the device of given name or null if it cannot be found
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the device the descriptor is for
        
            Returns:
                the descriptor for the device of given name or null
        
        
        """
        ...
    def findDeviceDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    def findParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def findParameterDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def findValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def findValueDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...

class CachingDescriptorProvider(DescriptorProvider, cern.japc.core.spi.cache.JapcCache):
    """
    public class CachingDescriptorProvider extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.provider.DescriptorProvider`, :class:`~cern.japc.core.spi.cache.JapcCache`
    
        :class:`~cern.japc.core.spi.provider.DescriptorProvider` decorator which caches the descriptors.
    """
    def __init__(self, descriptorProvider: DescriptorProvider): ...
    def clearAll(self) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.cache.JapcCache.clearAll`
            Requests to invalidate all the caches.
        
            Specified by:
                :meth:`~cern.japc.core.spi.cache.JapcCache.clearAll` in interface :class:`~cern.japc.core.spi.cache.JapcCache`
        
        
        """
        ...
    def findDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findDeviceDescriptor`
            Returns the device descriptor for the device of given name or null if it cannot be found
        
            Specified by:
                :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findDeviceDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.spi.provider.DescriptorProvider`
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the device the descriptor is for
        
            Returns:
                the descriptor for the device of given name or null
        
        
        """
        ...
    def findDeviceDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    def findParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def findParameterDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def findValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def findValueDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...

class CompositeDescriptorProvider(DescriptorProvider):
    """
    public class CompositeDescriptorProvider extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.provider.DescriptorProvider`
    
        This composite descriptor provider is able to look for descriptors from one or several providers. The providers are
        queried in the same order as they are passed in the array.
    """
    def __init__(self, descriptorProviderArray: typing.List[DescriptorProvider]): ...
    def createParameterExplorer(self) -> cern.japc.core.ParameterExplorer:
        """
            Not used and not declared in the :class:`~cern.japc.core.spi.provider.DescriptorProvider`.
        
        
            Returns:
                parameter explorer
        
        
        """
        ...
    def findDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findDeviceDescriptor`
            Returns the device descriptor for the device of given name or null if it cannot be found
        
            Specified by:
                :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findDeviceDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.spi.provider.DescriptorProvider`
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the device the descriptor is for
        
            Returns:
                the descriptor for the device of given name or null
        
        
        """
        ...
    def findDeviceDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    def findParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def findParameterDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def findValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def findValueDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...

class DefaultDescriptorProvider(DescriptorProvider):
    """
    public class DefaultDescriptorProvider extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.provider.DescriptorProvider`
    
        A descriptor provider that has access to no external source of information. It returns :code:`null` as a value
        descriptor and builds a default parameter descriptor allowing read/write/monitor access. The parameter is described as
        neither multiplexed nor cycle bound and having immutable values returned from JAPC.
    """
    def __init__(self): ...
    @staticmethod
    def createDefaultParameterDescriptor(string: str) -> cern.japc.core.ParameterDescriptor: ...
    def createParameterExplorer(self) -> cern.japc.core.ParameterExplorer:
        """
            Not used and not declared in the :class:`~cern.japc.core.spi.provider.DescriptorProvider`.
        
            Returns:
                parameter explorer
        
        
        """
        ...
    def findDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findDeviceDescriptor`
            Returns the device descriptor for the device of given name or null if it cannot be found
        
            Specified by:
                :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findDeviceDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.spi.provider.DescriptorProvider`
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the device the descriptor is for
        
            Returns:
                the descriptor for the device of given name or null
        
        
        """
        ...
    def findDeviceDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    def findParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findParameterDescriptor`
            Returns the parameter descriptor for the parameter of given name or null if it cannot be found
        
            Specified by:
                :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findParameterDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.spi.provider.DescriptorProvider`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter the descriptor is for
        
            Returns:
                the parameter descriptor for the parameter of given name or null
        
        
        """
        ...
    def findParameterDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def findValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findValueDescriptor`
            Returns the value descriptor for the parameter of given name or null if it cannot be found
        
            Specified by:
                :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findValueDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.spi.provider.DescriptorProvider`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter the value descriptor is for
        
            Returns:
                the value descriptor for the parameter of given name or null
        
        
        """
        ...
    def findValueDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...

class CustomizableDescriptorProvider(DefaultDescriptorProvider):
    """
    public class CustomizableDescriptorProvider extends :class:`~cern.japc.core.spi.provider.DefaultDescriptorProvider`
    
        A descriptor provider which could be filled with information by client. This provider has a possibility to add
        descriptors for different devices or parameters. It can use full device instance name, like MAGEA_900, or only device
        class name, for example MAGEA, in parameterNames. The correct lookups will be done.
    """
    DATA_CONTAINER_SEPARATOR: typing.ClassVar[str] = ...
    """
    public static `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DATA_CONTAINER_SEPARATOR
    
        A ':'-separated list of classes implementing DescriptorContainer interface.
    
    """
    def __init__(self): ...
    @staticmethod
    def addAllDescriptors(string: str, deviceDescriptor: cern.japc.core.DeviceDescriptor, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor) -> None:
        """
            Adds a device descriptor into the list of known devices
        
        
            Adds a parameter descriptor into the list of known parameters
        
        
            Adds a value descriptor into the list of known parameter values
        
        
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The full name of the device could be used, for example MAGEA_900/Acquisition, or only a device class name, for example
                    MAGEA/Acquisition.
                deviceDescriptor (:class:`~cern.japc.core.DeviceDescriptor`):         parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`):         valueDescriptor (cern.japc.value.ValueDescriptor): 
        
        """
        ...
    @staticmethod
    def addDeviceDescriptor(string: str, deviceDescriptor: cern.japc.core.DeviceDescriptor) -> None:
        """
            Adds a device descriptor into the list of known devices
        
        
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): It could be the full name of the device, for example MAGEA_900, or only a device class name, for example MAGEA.
                deviceDescriptor (:class:`~cern.japc.core.DeviceDescriptor`): 
        
        """
        ...
    @staticmethod
    def addParameterAndValueDescriptor(string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor) -> None:
        """
            Adds a parameter descriptor into the list of known parameters
        
        
            Adds a value descriptor into the list of known parameter values
        
        
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The full name of the device could be used, for example MAGEA_900/Acquisition, or only a device class name, for example
                    MAGEA/Acquisition.
                parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`):         valueDescriptor (cern.japc.value.ValueDescriptor): 
        
        """
        ...
    @staticmethod
    def addParameterDescriptor(string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> None:
        """
            Adds a parameter descriptor into the list of known parameters
        
        
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The full name of the device could be used, for example MAGEA_900/Acquisition, or only a device class name, for example
                    MAGEA/Acquisition.
                parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`): 
        
        """
        ...
    @staticmethod
    def addValueDescriptor(string: str, valueDescriptor: cern.japc.value.ValueDescriptor) -> None:
        """
            Adds a value descriptor into the list of known parameter values
        
        
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The full name of the device could be used, for example MAGEA_900/Acquisition, or only a device class name, for example
                    MAGEA/Acquisition.
                valueDescriptor (cern.japc.value.ValueDescriptor): 
        
        """
        ...
    def findDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findDeviceDescriptor`
            Returns the device descriptor for the device of given name or null if it cannot be found
        
            Specified by:
                :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findDeviceDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.spi.provider.DescriptorProvider`
        
            Overrides:
                :meth:`~cern.japc.core.spi.provider.DefaultDescriptorProvider.findDeviceDescriptor`Â in
                classÂ :class:`~cern.japc.core.spi.provider.DefaultDescriptorProvider`
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the device the descriptor is for
        
            Returns:
                the descriptor for the device of given name or null
        
        
        """
        ...
    def findParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findParameterDescriptor`
            Returns the parameter descriptor for the parameter of given name or null if it cannot be found
        
            Specified by:
                :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findParameterDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.spi.provider.DescriptorProvider`
        
            Overrides:
                :meth:`~cern.japc.core.spi.provider.DefaultDescriptorProvider.findParameterDescriptor`Â in
                classÂ :class:`~cern.japc.core.spi.provider.DefaultDescriptorProvider`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter the descriptor is for
        
            Returns:
                the parameter descriptor for the parameter of given name or null
        
        
        """
        ...
    def findValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findValueDescriptor`
            Returns the value descriptor for the parameter of given name or null if it cannot be found
        
            Specified by:
                :meth:`~cern.japc.core.spi.provider.DescriptorProvider.findValueDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.spi.provider.DescriptorProvider`
        
            Overrides:
                :meth:`~cern.japc.core.spi.provider.DefaultDescriptorProvider.findValueDescriptor`Â in
                classÂ :class:`~cern.japc.core.spi.provider.DefaultDescriptorProvider`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name identifying the parameter the value descriptor is for
        
            Returns:
                the value descriptor for the parameter of given name or null
        
        
        """
        ...
    @staticmethod
    def getDeviceInstanceSeparator() -> str:
        """
            Returns the device instance separator.
        
        
            Returns:
                the device instance separator
        
        
        """
        ...
    @staticmethod
    def setDeviceInstanceSeparator(string: str) -> None:
        """
            Sets new separator between device class and instance name
        
            Parameters:
                deviceInstanceSeparator (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.provider")``.

    CachingDescriptorProvider: typing.Type[CachingDescriptorProvider]
    CompositeDescriptorProvider: typing.Type[CompositeDescriptorProvider]
    CompositeParameterExplorer: typing.Type[CompositeParameterExplorer]
    CustomizableDescriptorProvider: typing.Type[CustomizableDescriptorProvider]
    DefaultDescriptorProvider: typing.Type[DefaultDescriptorProvider]
    DescriptorContainer: typing.Type[DescriptorContainer]
    DescriptorProvider: typing.Type[DescriptorProvider]
