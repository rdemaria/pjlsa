import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.lsa.domain.devices
import cern.lsa.domain.devices.factory.type
import java.util
import typing



class DeviceGroupsRequestBuilder:
    """
    public class DeviceGroupsRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder to be used when creating instances of :class:`~cern.lsa.domain.devices.DeviceGroupsRequest` class that describe
        search criteria for device groups. The typical usage is following:
    
        .. code-block: java
        
         DeviceGroupsRequestBuilder builder = DeviceGroupsRequestBuilder.newInstance();
         // Set search criteria
         builder.setAccelerator(CernAccelerator.PS);
         // Create the request
         DeviceGroupsRequest request = builder.build();
         // Call the DeviceFinder or DeviceService passing the request.
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.devices.DeviceGroupsRequest:
        """
        
            Returns:
                instance of the :class:`~cern.lsa.domain.devices.DeviceGroupsRequest`
        
        
        """
        ...
    @staticmethod
    def byAccelerator(accelerator: cern.accsoft.commons.domain.Accelerator) -> cern.lsa.domain.devices.DeviceGroupsRequest:
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): accelerator
        
            Returns:
                device groups request for specified accelerator
        
        
        """
        ...
    @staticmethod
    def byDeviceGroupNamePattern(string: str) -> cern.lsa.domain.devices.DeviceGroupsRequest:
        """
        
            Parameters:
                deviceGroupNamePattern (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                device groups request for specified device group name pattern
        
        
        """
        ...
    @staticmethod
    def byDeviceGroupNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.devices.DeviceGroupsRequest: ...
    @staticmethod
    def byDeviceGroupType(deviceGroupType: cern.lsa.domain.devices.DeviceGroupType) -> cern.lsa.domain.devices.DeviceGroupsRequest:
        """
        
            Parameters:
                deviceGroupType (:class:`~cern.lsa.domain.devices.DeviceGroupType`): device group type
        
            Returns:
                device groups request for specified device group type
        
        
        """
        ...
    @staticmethod
    def byDeviceGroupTypes(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceGroupType], typing.Sequence[cern.lsa.domain.devices.DeviceGroupType]]) -> cern.lsa.domain.devices.DeviceGroupsRequest: ...
    def setAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DeviceGroupsRequestBuilder':
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DeviceGroupsRequest.getAccelerator`
        
        
        """
        ...
    def setDeviceGroupName(self, string: str) -> 'DeviceGroupsRequestBuilder':
        """
        
            Parameters:
                deviceGroupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DeviceGroupsRequest.getDeviceGroupNames`
        
        
        """
        ...
    def setDeviceGroupNamePattern(self, string: str) -> 'DeviceGroupsRequestBuilder':
        """
        
            Parameters:
                deviceGroupNamePattern (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DeviceGroupsRequest.getDeviceGroupNamePattern`
        
        
        """
        ...
    def setDeviceGroupNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DeviceGroupsRequestBuilder': ...
    def setDeviceGroupType(self, deviceGroupType: cern.lsa.domain.devices.DeviceGroupType) -> 'DeviceGroupsRequestBuilder':
        """
        
            Parameters:
                deviceGroupType (:class:`~cern.lsa.domain.devices.DeviceGroupType`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DeviceGroupsRequest.getDeviceGroupTypes`
        
        
        """
        ...
    def setDeviceGroupTypes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceGroupType], typing.Sequence[cern.lsa.domain.devices.DeviceGroupType]]) -> 'DeviceGroupsRequestBuilder': ...

class DeviceTypesRequestBuilder:
    """
    public class DeviceTypesRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder to be used when creating instances of :class:`~cern.lsa.domain.devices.DeviceTypesRequest` class that describe
        search criteria for device types. The typical usage is following:
    
        .. code-block: java
        
         DeviceTypesRequestBuilder builder = DeviceTypesRequestBuilder.newInstance();
         // Set search criteria
         builder.setAccelerator(CernAccelerator.PS);
         // Create the request
         DeviceTypesRequest request = builder.build();
         // Call the DeviceFinder or DeviceService passing the request.
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    ALL_DEVICE_TYPES: typing.ClassVar[cern.lsa.domain.devices.DeviceTypesRequest] = ...
    """
    public static final :class:`~cern.lsa.domain.devices.DeviceTypesRequest` ALL_DEVICE_TYPES
    
        Request for all the device types
    
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.devices.DeviceTypesRequest:
        """
        
            Returns:
                instance of the :class:`~cern.lsa.domain.devices.DeviceTypesRequest`
        
        
        """
        ...
    @staticmethod
    def byAccelerator(accelerator: cern.accsoft.commons.domain.Accelerator) -> cern.lsa.domain.devices.DeviceTypesRequest:
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): accelerator
        
            Returns:
                device types request for specified accelerator
        
        
        """
        ...
    @staticmethod
    def byDeviceTypeNameImplementation(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceTypeImplementation], typing.Sequence[cern.lsa.domain.devices.DeviceTypeImplementation]]) -> cern.lsa.domain.devices.DeviceTypesRequest: ...
    @staticmethod
    def byDeviceTypeNamePattern(string: str) -> cern.lsa.domain.devices.DeviceTypesRequest:
        """
        
            Parameters:
                deviceTypeNamePattern (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): device type name pattern
        
            Returns:
                device types request for specified device type name pattern
        
        
        """
        ...
    @staticmethod
    def byDeviceTypeNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.devices.DeviceTypesRequest: ...
    def setAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DeviceTypesRequestBuilder':
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DeviceTypesRequest.getAccelerator`
        
        
        """
        ...
    def setDeviceTypeImplementation(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceTypeImplementation], typing.Sequence[cern.lsa.domain.devices.DeviceTypeImplementation]]) -> 'DeviceTypesRequestBuilder': ...
    def setDeviceTypeNamePattern(self, string: str) -> 'DeviceTypesRequestBuilder':
        """
        
            Parameters:
                pattern (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DeviceTypesRequest.getDeviceTypeNamePattern`
        
        
        """
        ...
    def setDeviceTypeNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DeviceTypesRequestBuilder': ...
    def setDeviceTypeVersionNumber(self, deviceTypeVersionNumber: cern.lsa.domain.devices.DeviceTypeVersionNumber) -> 'DeviceTypesRequestBuilder':
        """
        
            Parameters:
                versionNumber (:class:`~cern.lsa.domain.devices.DeviceTypeVersionNumber`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DeviceTypesRequest.getDeviceTypeVersionNumber`
        
        
        """
        ...

class DevicesRequestBuilder:
    """
    public class DevicesRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder to be used when creating instances of :class:`~cern.lsa.domain.devices.DevicesRequest` class that describe
        search criteria for devices. The typical usage is following:
    
        .. code-block: java
        
         DevicesRequestBuilder builder = DevicesRequestBuilder.newInstance();
         // Set search criteria
         builder.setDeviceClassName("BLM");
         builder.setParticleTransfer(SpsParticleTransfer.SPSRING);
         // Create the request
         DevicesRequest request = builder.build();
         // Call the DeviceFinder or DeviceService passing the request.
         DeviceService service = ServiceLocator.getService(DeviceService.class);
         Set<Device> devices = service.findDevices(builder.build());
         
         // Alternatively, if only a single criteria is used consider using one of the static factory methods e.g.:
         import static cern.lsa.domain.devices.factory.DevicesRequestBuilder.*;
         ...
         Set<Device> devices = service.findDevices(byAcceleratorZone(SpsAcceleratorZone.TT40));
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Returns:
                an instance of the :code:`DevicesRequest`.
        
        
        """
        ...
    @staticmethod
    def byAccelerator(accelerator: cern.accsoft.commons.domain.Accelerator) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): accelerator
        
            Returns:
                devices request for specified accelerator
        
        
        """
        ...
    @staticmethod
    def byAcceleratorZone(acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                acceleratorZone (cern.accsoft.commons.domain.zones.AcceleratorZone): accelerator zone
        
            Returns:
                devices request for specified accelerator zone
        
        
        """
        ...
    @staticmethod
    def byAcceleratorZones(collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.zones.AcceleratorZone], typing.Sequence[cern.accsoft.commons.domain.zones.AcceleratorZone]]) -> cern.lsa.domain.devices.DevicesRequest: ...
    @staticmethod
    def byDeviceAliases(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.devices.DevicesRequest: ...
    @staticmethod
    def byDeviceGroup(deviceGroup: cern.lsa.domain.devices.DeviceGroup) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                deviceGroup (:class:`~cern.lsa.domain.devices.DeviceGroup`): device group
        
            Returns:
                devices request for specified device group
        
        
        """
        ...
    @staticmethod
    def byDeviceGroupName(string: str) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                deviceGroupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): device group name
        
            Returns:
                devices request for specified device group
        
        
        """
        ...
    @staticmethod
    def byDeviceGroupNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.devices.DevicesRequest: ...
    @staticmethod
    def byDeviceGroups(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceGroup], typing.Sequence[cern.lsa.domain.devices.DeviceGroup]]) -> cern.lsa.domain.devices.DevicesRequest: ...
    @staticmethod
    def byDeviceName(string: str) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                devices request for specified device names
        
        
        """
        ...
    @staticmethod
    def byDeviceNamePattern(string: str) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                deviceNamePattern (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): device name pattern
        
            Returns:
                devices request for specified device name pattern
        
        
        """
        ...
    @staticmethod
    def byDeviceNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.devices.DevicesRequest: ...
    @staticmethod
    def byDeviceTypeName(string: str) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                deviceTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): device type name
        
            Returns:
                devices request for specified device type names
        
        
        """
        ...
    @staticmethod
    def byDeviceTypeNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.devices.DevicesRequest: ...
    @staticmethod
    def byDeviceTypeVersion(deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                deviceTypeVersion (:class:`~cern.lsa.domain.devices.DeviceTypeVersion`): device type version
        
            Returns:
                devices request for specified device type version
        
        
        """
        ...
    @staticmethod
    def byDeviceTypeVersions(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceTypeVersion], typing.Sequence[cern.lsa.domain.devices.DeviceTypeVersion]]) -> cern.lsa.domain.devices.DevicesRequest: ...
    @staticmethod
    def byElementName(string: str) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                elementName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                devices request for specified element name
        
        
        """
        ...
    @staticmethod
    def byFecName(string: str) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                fecName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                devices request for specified fec name
        
        
        """
        ...
    @staticmethod
    def byFecNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.devices.DevicesRequest: ...
    @staticmethod
    def byParticleTransfer(particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): particle transfer
        
            Returns:
                devices request for specified particle transfer
        
        
        """
        ...
    @staticmethod
    def byParticleTransfers(collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]]) -> cern.lsa.domain.devices.DevicesRequest: ...
    @staticmethod
    def byServerName(string: str) -> cern.lsa.domain.devices.DevicesRequest:
        """
        
            Parameters:
                serverName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                devices request for specified fec name
        
        
        """
        ...
    def setAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getAccelerator`
        
        
        """
        ...
    def setAcceleratorZone(self, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                acceleratorZone (cern.accsoft.commons.domain.zones.AcceleratorZone): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getAcceleratorZones`
        
        
        """
        ...
    def setAcceleratorZones(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.zones.AcceleratorZone], typing.Sequence[cern.accsoft.commons.domain.zones.AcceleratorZone]]) -> 'DevicesRequestBuilder': ...
    def setDeviceAliases(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DevicesRequestBuilder': ...
    def setDeviceGroup(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                deviceGroup (:class:`~cern.lsa.domain.devices.DeviceGroup`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceGroupIds`
        
        
        """
        ...
    def setDeviceGroupName(self, string: str) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                deviceGroupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceGroupNames`
        
        
        """
        ...
    def setDeviceGroupNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DevicesRequestBuilder': ...
    def setDeviceGroups(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceGroup], typing.Sequence[cern.lsa.domain.devices.DeviceGroup]]) -> 'DevicesRequestBuilder': ...
    def setDeviceName(self, string: str) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceNames`
        
        
        """
        ...
    def setDeviceNamePattern(self, string: str) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                pattern (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): SQL LIKE pattern
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceNamePattern`
        
        
        """
        ...
    def setDeviceNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DevicesRequestBuilder': ...
    def setDeviceTypeName(self, string: str) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                deviceTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceTypeNames`
        
        
        """
        ...
    def setDeviceTypeNamePattern(self, string: str) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                typeNamePattern (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceTypeNamePattern`
        
        
        """
        ...
    def setDeviceTypeNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DevicesRequestBuilder': ...
    def setDeviceTypeVersion(self, deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                deviceTypeVersion (:class:`~cern.lsa.domain.devices.DeviceTypeVersion`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceTypeVersions`
        
        
        """
        ...
    def setDeviceTypeVersions(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceTypeVersion], typing.Sequence[cern.lsa.domain.devices.DeviceTypeVersion]]) -> 'DevicesRequestBuilder': ...
    def setElementName(self, string: str) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                elementName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getElementName`
        
        
        """
        ...
    def setExistInLsaOnly(self, boolean: bool) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                existInLsaOnly (boolean): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.existInLsaOnly`
        
        
        """
        ...
    def setFecName(self, string: str) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                fecName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getFecNames`
        
        
        """
        ...
    def setFecNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DevicesRequestBuilder': ...
    def setMetaType(self, deviceMetaTypeEnum: cern.lsa.domain.devices.DeviceMetaTypeEnum) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                metaType (:class:`~cern.lsa.domain.devices.DeviceMetaTypeEnum`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getMetaType`
        
        
        """
        ...
    def setMultiplexed(self, boolean: bool) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                multiplexed (`Boolean <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.isMultiplexed`
        
        
        """
        ...
    def setParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getParticleTransfers`
        
        
        """
        ...
    def setParticleTransfers(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]]) -> 'DevicesRequestBuilder': ...
    def setServerName(self, string: str) -> 'DevicesRequestBuilder':
        """
        
            Parameters:
                serverName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getServerNames`
        
        
        """
        ...
    def setServerNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DevicesRequestBuilder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.devices.factory")``.

    DeviceGroupsRequestBuilder: typing.Type[DeviceGroupsRequestBuilder]
    DeviceTypesRequestBuilder: typing.Type[DeviceTypesRequestBuilder]
    DevicesRequestBuilder: typing.Type[DevicesRequestBuilder]
    type: cern.lsa.domain.devices.factory.type.__module_protocol__
