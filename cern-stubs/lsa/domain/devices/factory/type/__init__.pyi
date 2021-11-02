import cern.lsa.domain.devices
import cern.lsa.domain.devices.type
import java.util
import typing



class PropertyVersionsRequestBuilder:
    """
    public class PropertyVersionsRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder to be used when creating instances of :class:`~cern.lsa.domain.devices.type.PropertyVersionsRequest` class that
        describe search criteria for properties. The typical usage is following:
    
        .. code-block: java
        
         PropertyVersionsRequestBuilder builder = PropertyVersionsRequestBuilder.newInstance();
         // Set search criteria
         builder.setDeviceTypes(deviceTypes);
         // Create the request
         PropertyVersionsRequest request = builder.build();
         // Call the PropertyFinder or DeviceService passing the request.
         
    
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    def __init__(self): ...
    def build(self) -> cern.lsa.domain.devices.type.PropertyVersionsRequest:
        """
        
            Returns:
                instance of the :class:`~cern.lsa.domain.devices.type.PropertyVersionsRequest`
        
        
        """
        ...
    @staticmethod
    def byDeviceTypeName(string: str) -> cern.lsa.domain.devices.type.PropertyVersionsRequest:
        """
        
            Parameters:
                deviceTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): device type name
        
            Returns:
                properties request for specified device type name
        
        
        """
        ...
    @staticmethod
    def byDeviceTypeNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.devices.type.PropertyVersionsRequest: ...
    @staticmethod
    def byDeviceTypeVersion(deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion) -> cern.lsa.domain.devices.type.PropertyVersionsRequest:
        """
        
            Parameters:
                deviceTypeVersion (:class:`~cern.lsa.domain.devices.DeviceTypeVersion`): device type version
        
            Returns:
                properties request for specified device type version
        
        
        """
        ...
    @staticmethod
    def byDeviceTypeVersions(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceTypeVersion], typing.Sequence[cern.lsa.domain.devices.DeviceTypeVersion]]) -> cern.lsa.domain.devices.type.PropertyVersionsRequest: ...
    @typing.overload
    @staticmethod
    def byDeviceTypes(deviceType: cern.lsa.domain.devices.DeviceType) -> cern.lsa.domain.devices.type.PropertyVersionsRequest:
        """
        
            Parameters:
                deviceType (:class:`~cern.lsa.domain.devices.DeviceType`): device type
        
            Returns:
                properties request for the given device type
        
        public static :class:`~cern.lsa.domain.devices.type.PropertyVersionsRequest` byDeviceTypes (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<:class:`~cern.lsa.domain.devices.DeviceType`> deviceTypes)
        
        
            Parameters:
                deviceTypes (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<:class:`~cern.lsa.domain.devices.DeviceType`> deviceTypes): device types
        
            Returns:
                properties request for the given device types
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def byDeviceTypes(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceType], typing.Sequence[cern.lsa.domain.devices.DeviceType]]) -> cern.lsa.domain.devices.type.PropertyVersionsRequest: ...
    def setDeviceTypeName(self, string: str) -> 'PropertyVersionsRequestBuilder':
        """
        
            Parameters:
                deviceTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersionsRequest.getDeviceTypeNames`
        
        
        """
        ...
    def setDeviceTypeNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'PropertyVersionsRequestBuilder': ...
    def setDeviceTypeVersion(self, deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion) -> 'PropertyVersionsRequestBuilder':
        """
        
            Parameters:
                deviceTypeVersion (:class:`~cern.lsa.domain.devices.DeviceTypeVersion`): the :class:`~cern.lsa.domain.devices.DeviceTypeVersion` that will be requested
        
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersionsRequest.getDeviceTypeVersions`
        
        
        """
        ...
    def setDeviceTypeVersions(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceTypeVersion], typing.Sequence[cern.lsa.domain.devices.DeviceTypeVersion]]) -> 'PropertyVersionsRequestBuilder': ...
    def setPropertyName(self, string: str) -> 'PropertyVersionsRequestBuilder':
        """
        
            Parameters:
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersionsRequest.getPropertyNames`
        
        
        """
        ...
    def setPropertyNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'PropertyVersionsRequestBuilder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.devices.factory.type")``.

    PropertyVersionsRequestBuilder: typing.Type[PropertyVersionsRequestBuilder]
