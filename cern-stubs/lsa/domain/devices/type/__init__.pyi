import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.commons
import cern.lsa.domain.devices
import cern.lsa.domain.devices.factory.type
import cern.lsa.domain.devices.spi.type
import com.google.common.collect
import java.io
import java.lang
import java.util
import typing



class LsaAddedPropertyFieldSaveRequest:
    """
    @Immutable public interface LsaAddedPropertyFieldSaveRequest
    
        Currently this request serves only "added" LSA property-fields.
    """
    @staticmethod
    def builder() -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
    def getDescription(self) -> str: ...
    def getDeviceTypeName(self) -> str: ...
    def getExistingPropertyHandling(self) -> 'LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling': ...
    def getFieldAccess(self) -> cern.lsa.domain.devices.spi.type.PropertyFieldAccess: ...
    def getFieldMaxValue(self) -> float: ...
    def getFieldMinValue(self) -> float: ...
    def getFieldName(self) -> str: ...
    def getFieldUnit(self) -> str: ...
    def getFieldValueType(self) -> cern.accsoft.commons.value.Type: ...
    def getPropertyName(self) -> str: ...
    def getReasonForAdding(self) -> str: ...
    def isPropertyCycleBound(self) -> bool: ...
    def isPropertyMultiplexed(self) -> bool: ...
    def isPropertyReadable(self) -> bool: ...
    def isPropertyWritable(self) -> bool: ...
    class ExistingPropertyHandling(java.lang.Enum['LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling']):
        THROW: typing.ClassVar['LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling'] = ...
        REUSE_EXISTING_PROPERTY: typing.ClassVar['LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling'] = ...
        ASSERT_EXISTING_PROPERTY_MATCH: typing.ClassVar['LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling'] = ...
        UPDATE_EXISTING_PROPERTY: typing.ClassVar['LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling']: ...

class PropertyField(cern.lsa.domain.commons.IdentifiedEntity):
    """
    @Immutable public interface PropertyField extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`
    """
    @staticmethod
    def builder() -> 'DefaultPropertyField.Builder':
        """
            For internal use only.
        
            Returns:
                the builder
        
        
        """
        ...
    def getDeviceTypeName(self) -> str: ...
    def getFieldName(self) -> str: ...
    def getPropertyName(self) -> str: ...

class PropertyFieldVersion(cern.accsoft.commons.util.Named):
    """
    public interface PropertyFieldVersion extends cern.accsoft.commons.util.Named
    
        Represents a single field of a :class:`~cern.lsa.domain.devices.type.PropertyVersion`.
    """
    def getDescription(self) -> str:
        """
        
            Returns:
                description of field or :code:`null`
        
        
        """
        ...
    def getPropertyField(self) -> PropertyField:
        """
        
            Returns:
                non versioned device type property field
        
        
        """
        ...
    def getPropertyVersion(self) -> 'PropertyVersion':
        """
            Returns property version that this field belongs to.
        
            Returns:
                property version that this field belongs to
        
        
        """
        ...
    def getValueDescriptor(self) -> cern.accsoft.commons.value.ValueDescriptor:
        """
            Returns the value descriptor associated with the field.
        
            Returns:
                the value descriptor associated with the field.
        
        
        """
        ...
    def getValueType(self) -> cern.accsoft.commons.value.Type:
        """
            Returns value type of this property field.
        
            Returns:
                value type of this field
        
        
        """
        ...
    def isReadable(self) -> bool:
        """
            Indicates if this property field is readable. A field might be not readable if the property that it belongs to is not
            readable i.e. it is a command (write-only) property.
        
            Returns:
                :code:`true` if this property field is readable, :code:`false` otherwise.
        
        
        """
        ...
    def isWritable(self) -> bool:
        """
            Indicates if this property field is writable i.e. its value can be changed. All fields belonging to a read-only property
            are not writable but also certain fields belonging to a read-write property can be non-writable e.g. fields representing
            units, min, max or other meta information about the property or about other fields in the same property.
        
            Returns:
                :code:`true` if this property field is writable, :code:`false` otherwise.
        
        
        """
        ...

class PropertyFields:
    """
    public final class PropertyFields extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def buildPropertyFieldDisplayName(string: str, string2: str) -> str: ...

class PropertyFieldsRequest:
    """
    @Immutable public interface PropertyFieldsRequest
    """
    @staticmethod
    def builder() -> 'DefaultPropertyFieldsRequest.Builder': ...
    @staticmethod
    def byDeviceTypeAndProperty(string: str, string2: str) -> 'DefaultPropertyFieldsRequest': ...
    @staticmethod
    def byDeviceTypeName(string: str) -> 'DefaultPropertyFieldsRequest': ...
    @staticmethod
    def byDeviceTypeNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DefaultPropertyFieldsRequest': ...
    @staticmethod
    def byDeviceTypePropertyAndField(string: str, string2: str, string3: str) -> 'DefaultPropertyFieldsRequest': ...
    def getDeviceTypeNames(self) -> java.util.Set[str]: ...
    def getFieldNames(self) -> java.util.Set[str]: ...
    def getPropertyNames(self) -> java.util.Set[str]: ...

class PropertyVersion(cern.accsoft.commons.util.Named):
    """
    public interface PropertyVersion extends cern.accsoft.commons.util.Named
    
        Represents a single device property, either simple (containing a single field called :code:`value` or map that may
        contain several fields of different value types.
    """
    def getDescription(self) -> str:
        """
            Returns description of this property.
        
            Returns:
                description of this property or :code:`null`
        
        
        """
        ...
    def getDeviceTypeVersion(self) -> cern.lsa.domain.devices.DeviceTypeVersion:
        """
            Returns :class:`~cern.lsa.domain.devices.DeviceTypeVersion` that this property belongs to.
        
            Returns:
                :class:`~cern.lsa.domain.devices.DeviceTypeVersion` that this property belongs to
        
        
        """
        ...
    def getFields(self) -> java.util.Set[PropertyFieldVersion]: ...
    def getPropertyVisibility(self) -> 'PropertyVersion.PropertyVisibility':
        """
            Represents the FESA visibility of the property, which represents the purpose of the property, e.g. to be used by OP, to
            be used only by experts. Property might be as well still in development or deprecated
        
            Returns:
                visibility of the property
        
        
        """
        ...
    def isAddedInLsa(self) -> bool:
        """
            Indicates if this property was added in LSA i.e. it does not exist on the design defined on CCDB.
        
            Returns:
                :code:`true` if this property was added to LSA, :code:`false` otherwise
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
            Returns :code:`true` if this parameter is a cycle-bound acquisition parameter. More details can be found in "Device
            Property behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Returns:
                :code:`true` if this property is cycle-bound, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.devices.Device.isCycleBound`
        
        
        """
        ...
    def isMonitorable(self) -> bool:
        """
            Indicates if this property can be monitored i.e. it is possible to subscribe to this property and receive updates when
            the value has changed.
        
            Returns:
                :code:`true` if this property is monitorable, :code:`false` otherwise
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Returns :code:`true` if this property is a multiplexed setting property. More details can be found in "Device Property
            behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
        
            A non-multiplexed property can have only one set of values at a time that are independent on the context.
        
            Returns:
                :code:`true` if this property is multiplexed, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.devices.Device.isMultiplexed`
        
        
        """
        ...
    def isReadable(self) -> bool:
        """
            Indicates if this property is readable i.e. it's value can be read. Non-readable properties are typically command
            properties that are used to perform an action such as reset a device or trigger certain behavior.
        
            Returns:
                :code:`true` if this property is readable, :code:`false` otherwise
        
        
        """
        ...
    def isSupportingPartialSet(self) -> bool:
        """
            Indicates if this property supports partial set on the hardware i.e. if individual fields of this property can be set
            separately or all of them must be always set together.
        
            Typically properties support partial set but in some cases the fields are strongly dependent on each other and it is not
            allowed to set them individually. In such case this method returns :code:`false`.
        
            Note that in case of simple properties (no fields or a single field), this attribute has no meaning but returns
            :code:`true`.
        
            Returns:
                :code:`true` if the property supports partial set, :code:`false` otherwise
        
        
        """
        ...
    def isWritable(self) -> bool:
        """
            Indicates if this property is writable i.e. its value can be modified.
        
            Returns:
                :code:`true` if this property is writable, :code:`false` otherwise
        
        
        """
        ...
    class PropertyVisibility(java.lang.Enum['PropertyVersion.PropertyVisibility']):
        OPERATIONAL: typing.ClassVar['PropertyVersion.PropertyVisibility'] = ...
        EXPERT: typing.ClassVar['PropertyVersion.PropertyVisibility'] = ...
        DEVELOPMENT: typing.ClassVar['PropertyVersion.PropertyVisibility'] = ...
        DEPRECATED: typing.ClassVar['PropertyVersion.PropertyVisibility'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'PropertyVersion.PropertyVisibility': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['PropertyVersion.PropertyVisibility']: ...

class PropertyVersionFilter(cern.accsoft.commons.util.Filters.Filter[PropertyVersion]):
    """
    public class PropertyVersionFilter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.devices.type.PropertyVersion`>
    
        Simple :class:`~cern.lsa.domain.devices.type.PropertyVersion` filter.
    """
    def __init__(self): ...
    def accepts(self, propertyVersion: PropertyVersion) -> bool:
        """
        
            Specified by:
                :code:`accepts` in interface :class:`~cern.lsa.domain.devices.type.PropertyVersion`
        
        
        """
        ...
    @staticmethod
    def deviceType(deviceType: cern.lsa.domain.devices.DeviceType) -> 'PropertyVersionFilter':
        """
        
            Returns:
                the filter
        
        
        """
        ...
    @staticmethod
    def deviceTypeIn(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceType], typing.Sequence[cern.lsa.domain.devices.DeviceType]]) -> 'PropertyVersionFilter': ...
    @staticmethod
    def deviceTypeName(string: str) -> 'PropertyVersionFilter':
        """
        
            Returns:
                the filter
        
        
        """
        ...
    @staticmethod
    def deviceTypeNameIn(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'PropertyVersionFilter': ...
    @staticmethod
    def multiplexed(boolean: bool) -> 'PropertyVersionFilter':
        """
        
            Returns:
                the filter
        
        
        """
        ...
    @staticmethod
    def propertyName(string: str) -> 'PropertyVersionFilter':
        """
        
            Returns:
                the filter
        
        
        """
        ...
    @staticmethod
    def propertyNameIn(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'PropertyVersionFilter': ...
    def setDeviceType(self, deviceType: cern.lsa.domain.devices.DeviceType) -> 'PropertyVersionFilter':
        """
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setDeviceTypeName(self, string: str) -> 'PropertyVersionFilter':
        """
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setDeviceTypeNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'PropertyVersionFilter': ...
    def setDeviceTypes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceType], typing.Sequence[cern.lsa.domain.devices.DeviceType]]) -> 'PropertyVersionFilter': ...
    def setMultiplexed(self, boolean: bool) -> 'PropertyVersionFilter':
        """
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setPropertyName(self, string: str) -> 'PropertyVersionFilter':
        """
        
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setPropertyNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'PropertyVersionFilter': ...

class PropertyVersions:
    """
    public final class PropertyVersions extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class with methods applying to :code:`PropertyVersion` objects.
    """
    def __init__(self): ...
    @staticmethod
    def findPropertyVersion(string: str, sortedMap: java.util.SortedMap[cern.lsa.domain.devices.DeviceTypeVersion, java.util.Set[PropertyVersion]], device: cern.lsa.domain.devices.Device) -> PropertyVersion: ...
    @staticmethod
    def isCycleDependent(propertyVersion: PropertyVersion) -> bool:
        """
            Returns true if the property is either multiplexed or cycle dependent
        
            Parameters:
                property (:class:`~cern.lsa.domain.devices.type.PropertyVersion`): the property for which cycle-depependency should be evaluated
        
            Returns:
                true if the property is either multiplexed or cycle dependent, false otherwise
        
        
        """
        ...
    @staticmethod
    def toDeviceTypeNamesMap(set: java.util.Set[PropertyVersion]) -> java.util.Map[str, java.util.Set[PropertyVersion]]: ...
    @staticmethod
    def toNamesMap(map: typing.Union[java.util.Map[str, java.util.Set[PropertyVersion]], typing.Mapping[str, java.util.Set[PropertyVersion]]]) -> java.util.Map[str, java.util.Map[str, PropertyVersion]]: ...

class PropertyVersionsRequest:
    """
    public interface PropertyVersionsRequest
    
        Describes criteria when searching for LSA device properties. This object should be created using
        :class:`~cern.lsa.domain.devices.factory.type.PropertyVersionsRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> cern.lsa.domain.devices.factory.type.PropertyVersionsRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.devices.type.PropertyVersionsRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getDeviceTypeNames(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersions(self) -> java.util.Set[cern.lsa.domain.devices.DeviceTypeVersion]: ...
    def getPropertyNames(self) -> java.util.Set[str]: ...

class DefaultLsaAddedPropertyFieldSaveRequest(LsaAddedPropertyFieldSaveRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultLsaAddedPropertyFieldSaveRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultLsaAddedPropertyFieldSaveRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.devices.type.DefaultLsaAddedPropertyFieldSaveRequest`.
        
            .. code-block: java
            
             DefaultLsaAddedPropertyFieldSaveRequest.builder()
                .deviceTypeName(String) // required :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getDeviceTypeName`
                .propertyName(String) // required :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getPropertyName`
                .fieldName(String) // required :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldName`
                .existingPropertyHandling(cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling) // required :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getExistingPropertyHandling`
                .propertyReadable(Boolean | null) // nullable :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.isPropertyReadable`
                .propertyWritable(Boolean | null) // nullable :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.isPropertyWritable`
                .propertyMultiplexed(Boolean | null) // nullable :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.isPropertyMultiplexed`
                .propertyCycleBound(Boolean | null) // nullable :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.isPropertyCycleBound`
                .fieldValueType(cern.accsoft.commons.value.Type) // required :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldValueType`
                .fieldUnit(String | null) // nullable :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldUnit`
                .fieldMinValue(Double | null) // nullable :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldMinValue`
                .fieldMaxValue(Double | null) // nullable :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldMaxValue`
                .fieldAccess(cern.lsa.domain.devices.spi.type.PropertyFieldAccess) // required :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldAccess`
                .description(String | null) // nullable :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getDescription`
                .reasonForAdding(String) // required :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getReasonForAdding`
                .build();
             
        
            Returns:
                A new DefaultLsaAddedPropertyFieldSaveRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(lsaAddedPropertyFieldSaveRequest: LsaAddedPropertyFieldSaveRequest) -> 'DefaultLsaAddedPropertyFieldSaveRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest`): The instance to copy
        
            Returns:
                A copied immutable LsaAddedPropertyFieldSaveRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDescription(self) -> str: ...
    def getDeviceTypeName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getDeviceTypeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest`
        
            Returns:
                The value of the :code:`deviceTypeName` attribute
        
        
        """
        ...
    def getExistingPropertyHandling(self) -> LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getExistingPropertyHandling`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest`
        
            Returns:
                The value of the :code:`existingPropertyHandling` attribute
        
        
        """
        ...
    def getFieldAccess(self) -> cern.lsa.domain.devices.spi.type.PropertyFieldAccess:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldAccess`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest`
        
            Returns:
                The value of the :code:`fieldAccess` attribute
        
        
        """
        ...
    def getFieldMaxValue(self) -> float: ...
    def getFieldMinValue(self) -> float: ...
    def getFieldName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldName`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest`
        
            Returns:
                The value of the :code:`fieldName` attribute
        
        
        """
        ...
    def getFieldUnit(self) -> str: ...
    def getFieldValueType(self) -> cern.accsoft.commons.value.Type:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldValueType`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest`
        
            Returns:
                The value of the :code:`fieldValueType` attribute
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getPropertyName`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest`
        
            Returns:
                The value of the :code:`propertyName` attribute
        
        
        """
        ...
    def getReasonForAdding(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getReasonForAdding`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest`
        
            Returns:
                The value of the :code:`reasonForAdding` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`deviceTypeName`, :code:`propertyName`, :code:`fieldName`,
            :code:`existingPropertyHandling`, :code:`propertyReadable`, :code:`propertyWritable`, :code:`propertyMultiplexed`,
            :code:`propertyCycleBound`, :code:`fieldValueType`, :code:`fieldUnit`, :code:`fieldMinValue`, :code:`fieldMaxValue`,
            :code:`fieldAccess`, :code:`description`, :code:`reasonForAdding`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isPropertyCycleBound(self) -> bool: ...
    def isPropertyMultiplexed(self) -> bool: ...
    def isPropertyReadable(self) -> bool: ...
    def isPropertyWritable(self) -> bool: ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`LsaAddedPropertyFieldSaveRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDescription(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest': ...
    def withDeviceTypeName(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getDeviceTypeName` attribute. An equals check used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for deviceTypeName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withExistingPropertyHandling(self, existingPropertyHandling: LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling) -> 'DefaultLsaAddedPropertyFieldSaveRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getExistingPropertyHandling` attribute. A value
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling`): A new value for existingPropertyHandling
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withFieldAccess(self, propertyFieldAccess: cern.lsa.domain.devices.spi.type.PropertyFieldAccess) -> 'DefaultLsaAddedPropertyFieldSaveRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldAccess` attribute. A value equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.devices.spi.type.PropertyFieldAccess`): A new value for fieldAccess
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withFieldMaxValue(self, double: float) -> 'DefaultLsaAddedPropertyFieldSaveRequest': ...
    def withFieldMinValue(self, double: float) -> 'DefaultLsaAddedPropertyFieldSaveRequest': ...
    def withFieldName(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for fieldName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withFieldUnit(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest': ...
    def withFieldValueType(self, type: cern.accsoft.commons.value.Type) -> 'DefaultLsaAddedPropertyFieldSaveRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getFieldValueType` attribute. A value equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (cern.accsoft.commons.value.Type): A new value for fieldValueType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyCycleBound(self, boolean: bool) -> 'DefaultLsaAddedPropertyFieldSaveRequest': ...
    def withPropertyMultiplexed(self, boolean: bool) -> 'DefaultLsaAddedPropertyFieldSaveRequest': ...
    def withPropertyName(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getPropertyName` attribute. An equals check used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for propertyName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyReadable(self, boolean: bool) -> 'DefaultLsaAddedPropertyFieldSaveRequest': ...
    def withPropertyWritable(self, boolean: bool) -> 'DefaultLsaAddedPropertyFieldSaveRequest': ...
    def withReasonForAdding(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.type.LsaAddedPropertyFieldSaveRequest.getReasonForAdding` attribute. An equals check
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for reasonForAdding
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultLsaAddedPropertyFieldSaveRequest': ...
        def description(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def deviceTypeName(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def existingPropertyHandling(self, existingPropertyHandling: LsaAddedPropertyFieldSaveRequest.ExistingPropertyHandling) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def fieldAccess(self, propertyFieldAccess: cern.lsa.domain.devices.spi.type.PropertyFieldAccess) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def fieldMaxValue(self, double: float) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def fieldMinValue(self, double: float) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def fieldName(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def fieldUnit(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def fieldValueType(self, type: cern.accsoft.commons.value.Type) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def propertyCycleBound(self, boolean: bool) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def propertyMultiplexed(self, boolean: bool) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def propertyName(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def propertyReadable(self, boolean: bool) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def propertyWritable(self, boolean: bool) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...
        def reasonForAdding(self, string: str) -> 'DefaultLsaAddedPropertyFieldSaveRequest.Builder': ...

class DefaultPropertyField(PropertyField, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultPropertyField extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.devices.type.PropertyField`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.devices.type.PropertyField`.
    
        Use the builder to create immutable instances: :code:`DefaultPropertyField.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultPropertyField.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.devices.type.DefaultPropertyField`.
        
            .. code-block: java
            
             DefaultPropertyField.builder()
                .id(long) // required :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId`
                .deviceTypeName(String) // required :meth:`~cern.lsa.domain.devices.type.PropertyField.getDeviceTypeName`
                .propertyName(String) // required :meth:`~cern.lsa.domain.devices.type.PropertyField.getPropertyName`
                .fieldName(String) // required :meth:`~cern.lsa.domain.devices.type.PropertyField.getFieldName`
                .build();
             
        
            Returns:
                A new DefaultPropertyField builder
        
        
        """
        ...
    @staticmethod
    def copyOf(propertyField: PropertyField) -> 'DefaultPropertyField':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.devices.type.PropertyField` value. Uses accessors to get values
            to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.devices.type.PropertyField`): The instance to copy
        
            Returns:
                A copied immutable PropertyField instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDeviceTypeName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.type.PropertyField.getDeviceTypeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.type.PropertyField`
        
            Returns:
                The value of the :code:`deviceTypeName` attribute
        
        
        """
        ...
    def getFieldName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.type.PropertyField.getFieldName`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.type.PropertyField`
        
            Returns:
                The value of the :code:`fieldName` attribute
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId` in interface :class:`~cern.lsa.domain.commons.IdentifiedEntity`
        
            Returns:
                identifier of this entity, any long number - positive, negative or 0
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.type.PropertyField.getPropertyName`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.type.PropertyField`
        
            Returns:
                The value of the :code:`propertyName` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`id`, :code:`deviceTypeName`, :code:`propertyName`, :code:`fieldName`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`PropertyField` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDeviceTypeName(self, string: str) -> 'DefaultPropertyField':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.type.PropertyField.getDeviceTypeName` attribute. An equals check used to prevent copying
            of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for deviceTypeName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withFieldName(self, string: str) -> 'DefaultPropertyField':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.type.PropertyField.getFieldName` attribute. An equals check used to prevent copying of
            the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for fieldName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultPropertyField':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId`
            attribute. A value equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyName(self, string: str) -> 'DefaultPropertyField':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.type.PropertyField.getPropertyName` attribute. An equals check used to prevent copying
            of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for propertyName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultPropertyField': ...
        def deviceTypeName(self, string: str) -> 'DefaultPropertyField.Builder': ...
        def fieldName(self, string: str) -> 'DefaultPropertyField.Builder': ...
        def id(self, long: int) -> 'DefaultPropertyField.Builder': ...
        def propertyName(self, string: str) -> 'DefaultPropertyField.Builder': ...

class DefaultPropertyFieldsRequest(PropertyFieldsRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultPropertyFieldsRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.devices.type.PropertyFieldsRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.devices.type.PropertyFieldsRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultPropertyFieldsRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultPropertyFieldsRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.devices.type.DefaultPropertyFieldsRequest`.
        
            .. code-block: java
            
             DefaultPropertyFieldsRequest.builder()
                .deviceTypeNames(Set<String> | null) // nullable :meth:`~cern.lsa.domain.devices.type.PropertyFieldsRequest.getDeviceTypeNames`
                .propertyNames(Set<String> | null) // nullable :meth:`~cern.lsa.domain.devices.type.PropertyFieldsRequest.getPropertyNames`
                .fieldNames(Set<String> | null) // nullable :meth:`~cern.lsa.domain.devices.type.PropertyFieldsRequest.getFieldNames`
                .build();
             
        
            Returns:
                A new DefaultPropertyFieldsRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(propertyFieldsRequest: PropertyFieldsRequest) -> 'DefaultPropertyFieldsRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.devices.type.PropertyFieldsRequest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.devices.type.PropertyFieldsRequest`): The instance to copy
        
            Returns:
                A copied immutable PropertyFieldsRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDeviceTypeNames(self) -> com.google.common.collect.ImmutableSet[str]: ...
    def getFieldNames(self) -> com.google.common.collect.ImmutableSet[str]: ...
    def getPropertyNames(self) -> com.google.common.collect.ImmutableSet[str]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`deviceTypeNames`, :code:`propertyNames`, :code:`fieldNames`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`PropertyFieldsRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withDeviceTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPropertyFieldsRequest': ...
    @typing.overload
    def withDeviceTypeNames(self, stringArray: typing.List[str]) -> 'DefaultPropertyFieldsRequest': ...
    @typing.overload
    def withFieldNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPropertyFieldsRequest': ...
    @typing.overload
    def withFieldNames(self, stringArray: typing.List[str]) -> 'DefaultPropertyFieldsRequest': ...
    @typing.overload
    def withPropertyNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPropertyFieldsRequest': ...
    @typing.overload
    def withPropertyNames(self, stringArray: typing.List[str]) -> 'DefaultPropertyFieldsRequest': ...
    class Builder:
        def addAllDeviceTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def addAllFieldNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def addAllPropertyNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def addDeviceTypeName(self, string: str) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def addDeviceTypeNames(self, stringArray: typing.List[str]) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def addFieldName(self, string: str) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def addFieldNames(self, stringArray: typing.List[str]) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def addPropertyName(self, string: str) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def addPropertyNames(self, stringArray: typing.List[str]) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def build(self) -> 'DefaultPropertyFieldsRequest': ...
        def deviceTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def fieldNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPropertyFieldsRequest.Builder': ...
        def propertyNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPropertyFieldsRequest.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.devices.type")``.

    DefaultLsaAddedPropertyFieldSaveRequest: typing.Type[DefaultLsaAddedPropertyFieldSaveRequest]
    DefaultPropertyField: typing.Type[DefaultPropertyField]
    DefaultPropertyFieldsRequest: typing.Type[DefaultPropertyFieldsRequest]
    LsaAddedPropertyFieldSaveRequest: typing.Type[LsaAddedPropertyFieldSaveRequest]
    PropertyField: typing.Type[PropertyField]
    PropertyFieldVersion: typing.Type[PropertyFieldVersion]
    PropertyFields: typing.Type[PropertyFields]
    PropertyFieldsRequest: typing.Type[PropertyFieldsRequest]
    PropertyVersion: typing.Type[PropertyVersion]
    PropertyVersionFilter: typing.Type[PropertyVersionFilter]
    PropertyVersions: typing.Type[PropertyVersions]
    PropertyVersionsRequest: typing.Type[PropertyVersionsRequest]
