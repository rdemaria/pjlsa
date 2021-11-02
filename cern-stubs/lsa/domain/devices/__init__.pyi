import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.util
import cern.lsa.domain.commons
import cern.lsa.domain.devices.factory
import cern.lsa.domain.devices.inca
import cern.lsa.domain.devices.spi
import cern.lsa.domain.devices.type
import com.google.common.collect
import java.io
import java.lang
import java.util
import typing



class CalibrationsRequest:
    """
    @Immutable public interface CalibrationsRequest
    """
    ALL: typing.ClassVar['CalibrationsRequest'] = ...
    """
    static final :class:`~cern.lsa.domain.devices.CalibrationsRequest` ALL
    
    
    """
    @staticmethod
    def builder() -> 'DefaultCalibrationsRequest.Builder': ...
    @staticmethod
    def byCalibrationNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'CalibrationsRequest': ...
    @staticmethod
    def byLogicalHardwareName(string: str) -> 'CalibrationsRequest': ...
    @staticmethod
    def byParticleTransfer(particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'CalibrationsRequest': ...
    def getCalibrationNames(self) -> java.util.Set[str]: ...
    def getLogicalHardwareName(self) -> str: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...

class Device(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity, java.lang.Comparable['Device']):
    """
    public interface Device extends cern.accsoft.commons.util.Named, :class:`~cern.lsa.domain.commons.IdentifiedEntity`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.devices.Device`>
    
        Represents a device in the accelerator complex.
    
        Typically a :code:`Device` represents a real equipment installed in the accelerator but in some cases it may also
        represent a logical or LSA implementation device e.g. a beam device like LHCBEAM.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                the accelerator to which this device belongs.
        
        
        """
        ...
    def getAcceleratorZone(self) -> cern.accsoft.commons.domain.zones.AcceleratorZone:
        """
            Returns the accelerator zone this device belongs to.
        
            Returns:
                the accelerator zone this device belongs to
        
        
        """
        ...
    def getAlias(self) -> str:
        """
        
            Returns:
                Alias name of the device. An alias is another way of naming the devices used commonly by the operators.
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Returns an optional description of this device
        
            Returns:
                an description of this device or :code:`null`
        
        
        """
        ...
    def getDeviceGroups(self) -> java.util.Set[str]: ...
    def getDeviceType(self) -> 'DeviceType':
        """
            Returns type of this device.
        
            Returns:
                the non :code:`null` type of this device
        
        
        """
        ...
    def getDeviceTypeVersion(self) -> 'DeviceTypeVersion':
        """
            The type version of this device.
        
            Returns:
                the non :code:`null` type version of this device
        
        
        """
        ...
    def getFecName(self) -> str:
        """
            Name of the FEC responsible for device.
        
        """
        ...
    def getPosition(self) -> float:
        """
            Devices can be located relative to the start of the corresponding accelerator zone. The position indicates the position
            e.g. in meters. If the value is not filled, the position will be zero.
        
            Returns:
                the position of the device
        
        
        """
        ...
    def getServerName(self) -> str:
        """
            Name of the server (e.g. CMW).
        
        """
        ...
    def getSortOrder(self) -> int:
        """
            Devices can be located relative to the start of the corresponding accelerator zone. When two devices have the same
            position, then the sort order will be taken into account e.g. in the GUIs.
        
            Returns:
                the sort order for devices with the same position
        
        
        """
        ...
    def getState(self) -> 'Device.DeviceState':
        """
        
            Returns:
                device state
        
        
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
    def isLsaImplementation(self) -> bool:
        """
            Indicate whether the device is served by InCA/LSA
        
            Returns:
                :code:`true`, if the the server corresponds to InCA or LSA server. :code:`false` otherwise.
        
        
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
    class DeviceState(java.lang.Enum['Device.DeviceState']):
        OPERATIONAL: typing.ClassVar['Device.DeviceState'] = ...
        EXPERT: typing.ClassVar['Device.DeviceState'] = ...
        DEVELOPMENT: typing.ClassVar['Device.DeviceState'] = ...
        OBSOLETE: typing.ClassVar['Device.DeviceState'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'Device.DeviceState': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['Device.DeviceState']: ...

class DeviceFilter(cern.accsoft.commons.util.Filters.Filter[Device]):
    """
    public class DeviceFilter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.devices.Device`>
    
        Simple :class:`~cern.lsa.domain.devices.Device` filter.
    """
    def __init__(self): ...
    @staticmethod
    def acceleratorZone(acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> 'DeviceFilter':
        """
        
            Parameters:
                acceleratorZone (cern.accsoft.commons.domain.zones.AcceleratorZone): 
            Returns:
                the filter
        
        
        """
        ...
    @staticmethod
    def acceleratorZoneIn(collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.zones.AcceleratorZone], typing.Sequence[cern.accsoft.commons.domain.zones.AcceleratorZone]]) -> 'DeviceFilter': ...
    def accepts(self, device: Device) -> bool:
        """
        
            Specified by:
                :code:`accepts` in interface :class:`~cern.lsa.domain.devices.Device`
        
        
        """
        ...
    @staticmethod
    def deviceGroupName(string: str) -> 'DeviceFilter':
        """
        
            Parameters:
                deviceGroupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                the filter
        
        
        """
        ...
    @staticmethod
    def deviceTypeName(string: str) -> 'DeviceFilter':
        """
        
            Parameters:
                deviceTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                the filter
        
        
        """
        ...
    @staticmethod
    def deviceTypeNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DeviceFilter': ...
    def setAcceleratorZone(self, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> 'DeviceFilter':
        """
        
            Parameters:
                acceleratorZone (cern.accsoft.commons.domain.zones.AcceleratorZone): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setAcceleratorZones(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.zones.AcceleratorZone], typing.Sequence[cern.accsoft.commons.domain.zones.AcceleratorZone]]) -> 'DeviceFilter': ...
    def setDeviceGroupName(self, string: str) -> 'DeviceFilter':
        """
        
            Parameters:
                deviceGroupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setDeviceGroupNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DeviceFilter': ...
    def setDeviceType(self, deviceType: 'DeviceType') -> 'DeviceFilter':
        """
        
            Parameters:
                deviceType (:class:`~cern.lsa.domain.devices.DeviceType`): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setDeviceTypeName(self, string: str) -> 'DeviceFilter':
        """
        
            Parameters:
                deviceTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setDeviceTypeNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DeviceFilter': ...
    def setDeviceTypeVersions(self, collection: typing.Union[java.util.Collection['DeviceTypeVersion'], typing.Sequence['DeviceTypeVersion']]) -> 'DeviceFilter': ...
    def setDeviceTypes(self, collection: typing.Union[java.util.Collection['DeviceType'], typing.Sequence['DeviceType']]) -> 'DeviceFilter': ...

class DeviceGroup(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface DeviceGroup extends cern.accsoft.commons.util.Named, :class:`~cern.lsa.domain.commons.IdentifiedEntity`
    
        Represents a group of devices of any type. A device group can contain actual (real) devices, logical devices (like
        magnets), beam devices or LSA implementation devices.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
            Returns the accelerator which this device group belongs to.
        
            Returns:
                the accelerator which this device group belongs to
        
        
        """
        ...
    def getChildGroups(self) -> java.util.Set['DeviceGroup']: ...
    def getCreateTime(self) -> java.util.Date:
        """
            Time of creation of the group.
        
            Returns:
                time of creation
        
        
        """
        ...
    def getCreator(self) -> str:
        """
            Login name of user who created this group.
        
            Returns:
                name of user who created this group
        
        
        """
        ...
    def getDisplayName(self) -> str:
        """
            Returns the display name of this device group.
        
            Returns:
                the display name of this device group
        
        
        """
        ...
    def getModifier(self) -> str:
        """
            Login name of user who performed last modification. If the group hasn't been modified after creation, this method
            returns :meth:`~cern.lsa.domain.devices.DeviceGroup.getCreator`.
        
            Returns:
                name of user who performed last modification
        
        
        """
        ...
    def getModifyTime(self) -> java.util.Date:
        """
            Time of last modification. If the group hasn't been modified after creation, this method returns the
            :meth:`~cern.lsa.domain.devices.DeviceGroup.getCreateTime`.
        
            Returns:
                time of last modification
        
        
        """
        ...
    def getType(self) -> 'DeviceGroupType':
        """
            Returns the name of type which this group belongs to.
        
            The device group type is used to indicate what kind of devices (or other device groups) it contains. Examples of device
            group types might be "working sets" containing devices of certain types used to control certain area of the accelerator,
            "processes" that consist of working sets, "sets of circuits" that group power converters etc.
        
            Returns:
                the non-null type name which this group belongs to
        
        
        """
        ...
    def isOperational(self) -> bool:
        """
            Returns :code:`true` if this device group is operational i.e. used by users in the production environment. A
            non-operational groups can be created for debugging or testing purposes.
        
            Returns:
                :code:`true` if this device group is operational, :code:`false` otherwise
        
        
        """
        ...

class DeviceGroupFilter(cern.accsoft.commons.util.Filters.Filter[DeviceGroup]):
    """
    public class DeviceGroupFilter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.devices.DeviceGroup`>
    
        Simple :class:`~cern.lsa.domain.devices.DeviceGroup` filter.
    """
    def __init__(self): ...
    @staticmethod
    def accelerator(accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DeviceGroupFilter':
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): 
            Returns:
                the filter
        
        
        """
        ...
    def accepts(self, deviceGroup: DeviceGroup) -> bool:
        """
        
            Specified by:
                :code:`accepts` in interface :class:`~cern.lsa.domain.devices.DeviceGroup`
        
        
        """
        ...
    def setAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DeviceGroupFilter':
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setType(self, deviceGroupType: 'DeviceGroupType') -> 'DeviceGroupFilter':
        """
        
            Parameters:
                type (:class:`~cern.lsa.domain.devices.DeviceGroupType`): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setTypes(self, collection: typing.Union[java.util.Collection['DeviceGroupType'], typing.Sequence['DeviceGroupType']]) -> 'DeviceGroupFilter': ...
    @staticmethod
    def type(deviceGroupType: 'DeviceGroupType') -> 'DeviceGroupFilter':
        """
        
            Parameters:
                type (:class:`~cern.lsa.domain.devices.DeviceGroupType`): 
            Returns:
                the filter
        
        
        """
        ...
    @staticmethod
    def typeIn(collection: typing.Union[java.util.Collection['DeviceGroupType'], typing.Sequence['DeviceGroupType']]) -> 'DeviceGroupFilter': ...

class DeviceGroupType(cern.accsoft.commons.util.Named):
    """
    public interface DeviceGroupType extends cern.accsoft.commons.util.Named
    
        Represents type of a device group. Examples of such types can be 'PROCESS', 'WORKING_SET', 'SET OF CIRCUITS' or simply
        'DEVICES'.
    """
    def getDescription(self) -> str:
        """
        
            Returns:
                description of the type
        
        
        """
        ...

class DeviceGroups:
    """
    public class DeviceGroups extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods to work with :class:`~cern.lsa.domain.devices.DeviceGroup`'s.
    """
    CHILD_GROUPS: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.devices.DeviceGroup`, `Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<:class:`~cern.lsa.domain.devices.DeviceGroup`>> CHILD_GROUPS
    
        Mapper :code:`DeviceGroup to Collection<DeviceGroup> (child groups)`
    
    """
    def __init__(self): ...
    @staticmethod
    def filterGroupsByType(collection: typing.Union[java.util.Collection[DeviceGroup], typing.Sequence[DeviceGroup]], deviceGroupType: DeviceGroupType) -> java.util.Set[DeviceGroup]: ...
    @staticmethod
    def getAllChildDeviceGroups(collection: typing.Union[java.util.Collection[DeviceGroup], typing.Sequence[DeviceGroup]]) -> java.util.Set[DeviceGroup]: ...
    @staticmethod
    def getDirectChildDeviceGroups(collection: typing.Union[java.util.Collection[DeviceGroup], typing.Sequence[DeviceGroup]]) -> java.util.Set[DeviceGroup]: ...

class DeviceGroupsRequest:
    """
    public interface DeviceGroupsRequest
    
        Describes criteria when searching for LSA device groups. This object should be created using
        :class:`~cern.lsa.domain.devices.factory.DeviceGroupsRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> cern.lsa.domain.devices.factory.DeviceGroupsRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.devices.DeviceGroupsRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                accelerator that the device of the groups should belong to
        
        
        """
        ...
    def getDeviceGroupNamePattern(self) -> str:
        """
            Returns device group name pattern that is used to search the matching device groups. The pattern is used for SQL LIKE
            statement so it can contains characters supported by the statement like % or _ (underscore). The matching is case
            insensitive i.e. if the device group name is ABC123 - pattern abc% will match it.
        
            Returns:
                the device group name pattern
        
        
        """
        ...
    def getDeviceGroupNames(self) -> java.util.Set[str]: ...
    def getDeviceGroupTypes(self) -> java.util.Set[DeviceGroupType]: ...

class DeviceMetaTypeEnum(java.lang.Enum['DeviceMetaTypeEnum']):
    """
    public enum DeviceMetaTypeEnum extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.devices.DeviceMetaTypeEnum`>
    
        Defines a meta type of a device. At the moment we have 3 meta types: ACTUAL, LOGICAL and BEAM. See JavaDoc of each enum
        value for details.
    
        Also see:
            :class:`~cern.lsa.domain.devices.DeviceType`
    """
    ACTUAL: typing.ClassVar['DeviceMetaTypeEnum'] = ...
    LOGICAL: typing.ClassVar['DeviceMetaTypeEnum'] = ...
    BEAM: typing.ClassVar['DeviceMetaTypeEnum'] = ...
    ALL: typing.ClassVar['DeviceMetaTypeEnum'] = ...
    NONE: typing.ClassVar['DeviceMetaTypeEnum'] = ...
    def getMetaType(self) -> str:
        """
            Returns character representation of this meta type:
        
              - 'A' - for ACTUAL
              - 'L' - for LOGICAL
              - 'B' - for BEAM
        
        
            Returns:
                character representing this meta type (stored in database)
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    _valueOf_2__T = typing.TypeVar('_valueOf_2__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(char: str) -> 'DeviceMetaTypeEnum':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
            For given :meth:`~cern.lsa.domain.devices.DeviceMetaTypeEnum.getMetaType` returns the corresponding enum value.
        
            Parameters:
                metaType (char): 'A', 'L' or 'B'
        
            Returns:
                enum value
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'DeviceMetaTypeEnum': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_2__T], string: str) -> _valueOf_2__T: ...
    @staticmethod
    def values() -> typing.List['DeviceMetaTypeEnum']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (DeviceMetaTypeEnum c : DeviceMetaTypeEnum.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DeviceType(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity, java.lang.Comparable['DeviceType']):
    """
    public interface DeviceType extends cern.accsoft.commons.util.Named, :class:`~cern.lsa.domain.commons.IdentifiedEntity`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.devices.DeviceType`>
    
        Represents a type (class) of a device. The versions of a device type (or device class) are returned by
        :meth:`~cern.lsa.domain.devices.DeviceType.getVersions` method.
    
        Also see:
            :class:`~cern.lsa.domain.devices.DeviceMetaTypeEnum`
    """
    def getDescription(self) -> str:
        """
        
            Returns:
                the description for the device type or :code:`null` if not defined
        
        
        """
        ...
    def getMetaType(self) -> DeviceMetaTypeEnum:
        """
        
            Returns:
                the meta type of the device Type : can be 'B' for BEAM , 'L' for LOGICAL or 'A' for ACTUAL.
        
        
        """
        ...
    def getVersions(self) -> java.util.SortedSet['DeviceTypeVersion']: ...

class DeviceTypeImplementation(java.lang.Enum['DeviceTypeImplementation'], cern.accsoft.commons.util.Named):
    """
    public enum DeviceTypeImplementation extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.devices.DeviceTypeImplementation`> implements cern.accsoft.commons.util.Named
    
        Specifies the implementation information for a device type
    """
    HARDWARE: typing.ClassVar['DeviceTypeImplementation'] = ...
    FESA2: typing.ClassVar['DeviceTypeImplementation'] = ...
    FESA3: typing.ClassVar['DeviceTypeImplementation'] = ...
    VIRTUAL: typing.ClassVar['DeviceTypeImplementation'] = ...
    GM: typing.ClassVar['DeviceTypeImplementation'] = ...
    DEVACC: typing.ClassVar['DeviceTypeImplementation'] = ...
    LSA: typing.ClassVar['DeviceTypeImplementation'] = ...
    FGC: typing.ClassVar['DeviceTypeImplementation'] = ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'DeviceTypeImplementation':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['DeviceTypeImplementation']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (DeviceTypeImplementation c : DeviceTypeImplementation.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DeviceTypeVersion(cern.lsa.domain.commons.IdentifiedEntity, java.lang.Comparable['DeviceTypeVersion']):
    """
    public interface DeviceTypeVersion extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.devices.DeviceTypeVersion`>
    
        :code:`DeviceTypeVersion` represents a specific version of a :class:`~cern.lsa.domain.devices.DeviceType`. Note that for
        frameworks that don't support versioning of classes (e.g. virtual, FGC, GM) - there is always a single device type
        version, typically 0.0
    """
    def getDeviceType(self) -> DeviceType:
        """
        
            Returns:
                the device type this version is specified for
        
        
        """
        ...
    def getImplementation(self) -> DeviceTypeImplementation:
        """
        
            Returns:
                the implementation type for this device type version. Can be :code:`null` in case of implementation types we still have
                in the DB but not support anymore (like SL)
        
        
        """
        ...
    def getVersionNumber(self) -> 'DeviceTypeVersionNumber':
        """
        
            Returns:
                the version number (major, minor)
        
        
        """
        ...

class DeviceTypeVersionNumber(java.lang.Comparable['DeviceTypeVersionNumber']):
    """
    public interface DeviceTypeVersionNumber extends `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.devices.DeviceTypeVersionNumber`>
    
        Version number of a :class:`~cern.lsa.domain.devices.DeviceType` composed of major and minor version number
    """
    def getMajor(self) -> int: ...
    def getMinor(self) -> int: ...

class DeviceTypes:
    """
    public class DeviceTypes extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class to work with :class:`~cern.lsa.domain.devices.DeviceType`s
    """
    def __init__(self): ...
    @staticmethod
    def getLatestVersion(deviceType: DeviceType) -> DeviceTypeVersion:
        """
        
            Returns:
                extracts the latest (newest) :code:`DeviceTypeVersion` out of a :code:`DeviceType`
        
        
        """
        ...
    @staticmethod
    def toDeviceTypeVersionByDeviceTypeMap(collection: typing.Union[java.util.Collection[DeviceTypeVersion], typing.Sequence[DeviceTypeVersion]]) -> java.util.Map[DeviceType, java.util.SortedSet[DeviceTypeVersion]]: ...
    @staticmethod
    def toDeviceTypeVersions(collection: typing.Union[java.util.Collection[DeviceType], typing.Sequence[DeviceType]]) -> java.util.Set[DeviceTypeVersion]: ...
    @staticmethod
    def toDeviceTypes(collection: typing.Union[java.util.Collection[DeviceTypeVersion], typing.Sequence[DeviceTypeVersion]]) -> java.util.Set[DeviceType]: ...

class DeviceTypesRequest:
    """
    public interface DeviceTypesRequest
    
        Describes criteria when searching for LSA device types. This object should be created using
        :class:`~cern.lsa.domain.devices.factory.DeviceTypesRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> cern.lsa.domain.devices.factory.DeviceTypesRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.devices.DeviceTypesRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                accelerator that the device of the groups should belong to
        
        
        """
        ...
    def getAllTypesRequested(self) -> bool:
        """
        
            Returns:
                :code:`true` if all types were requested
        
        
        """
        ...
    def getDeviceTypeImplementations(self) -> java.util.Set[DeviceTypeImplementation]: ...
    def getDeviceTypeNamePattern(self) -> str:
        """
            Returns device type name pattern which all device type names should match. The pattern is a SQL pattern accepted by the
            :code:`LIKE` clause (containing **%** or **_** (underscore) characters). Matching is case insensitive.
        
        """
        ...
    def getDeviceTypeNames(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersionNumber(self) -> DeviceTypeVersionNumber:
        """
        
            Returns:
                the device type version number the searched device type should have
        
        
        """
        ...

class Devices:
    """
    public class Devices extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class with methods applying to devices.
    """
    DEVICE_TYPES: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.devices.Device`, :class:`~cern.lsa.domain.devices.DeviceType`> DEVICE_TYPES
    
        Mapper :class:`~cern.lsa.domain.devices.Device` to :class:`~cern.lsa.domain.devices.DeviceType`
    
    """
    DEVICE_TYPE_NAMES: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.devices.Device`, `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`> DEVICE_TYPE_NAMES
    
        Mapper :class:`~cern.lsa.domain.devices.Device` to :class:`~cern.lsa.domain.devices.DeviceType` name
    
    """
    DEVICE_TYPE_VERSIONS: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.devices.Device`, :class:`~cern.lsa.domain.devices.DeviceTypeVersion`> DEVICE_TYPE_VERSIONS
    
    
    """
    FRONT_END_NAMES: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.devices.Device`, `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`> FRONT_END_NAMES
    
        Mapper :class:`~cern.lsa.domain.devices.Device` to :meth:`~cern.lsa.domain.devices.Device.getFecName` name
    
    """
    DEVICE_GROUP_NAMES: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.devices.Device`, `Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`>> DEVICE_GROUP_NAMES
    
        Mapper :class:`~cern.lsa.domain.devices.Device` to :class:`~cern.lsa.domain.devices.DeviceGroup` names
    
    """
    def __init__(self): ...
    @staticmethod
    def deviceGroupNameIn(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.accsoft.commons.util.Filters.Filter[Device]: ...
    @staticmethod
    def filterDevicesByGroupNames(collection: typing.Union[java.util.Collection[Device], typing.Sequence[Device]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[Device]: ...
    @staticmethod
    def filterDevicesNotAssignedToAnyGroup(collection: typing.Union[java.util.Collection[Device], typing.Sequence[Device]]) -> java.util.Set[Device]: ...
    @staticmethod
    def filterDevicesNotAssignedToGroup(collection: typing.Union[java.util.Collection[Device], typing.Sequence[Device]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[Device]: ...
    @staticmethod
    def findGroupsContainingDeviceByType(collection: typing.Union[java.util.Collection[DeviceGroup], typing.Sequence[DeviceGroup]], deviceGroupType: DeviceGroupType, device2: Device) -> java.util.Set[DeviceGroup]: ...
    @staticmethod
    def getDeviceGroupNames(set: java.util.Set[Device]) -> java.util.Set[str]: ...
    @staticmethod
    def getDeviceTypeNames(collection: typing.Union[java.util.Collection[Device], typing.Sequence[Device]]) -> java.util.Set[str]: ...
    @staticmethod
    def getDeviceTypeVersions(collection: typing.Union[java.util.Collection[Device], typing.Sequence[Device]]) -> java.util.Set[DeviceTypeVersion]: ...
    @staticmethod
    def getDeviceTypes(collection: typing.Union[java.util.Collection[Device], typing.Sequence[Device]]) -> java.util.Set[DeviceType]: ...
    @staticmethod
    def getDeviceTypesByDeviceGroup(set: java.util.Set[Device], string: str) -> java.util.Set[DeviceType]: ...
    @staticmethod
    def getFrontEndNames(set: java.util.Set[Device]) -> java.util.Set[str]: ...
    @staticmethod
    def groupDevicesByDeviceGroup(collection: typing.Union[java.util.Collection[Device], typing.Sequence[Device]]) -> java.util.Map[str, java.util.Set[Device]]: ...

class DevicesRequest:
    """
    public interface DevicesRequest
    
        Describes criteria when searching for LSA devices. This object should be created using
        :class:`~cern.lsa.domain.devices.factory.DevicesRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> cern.lsa.domain.devices.factory.DevicesRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.devices.DevicesRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def existInLsaOnly(self) -> bool:
        """
        
            Returns:
                true if we want to see devices that exists only in LSA (and not in CCDB)
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                accelerator that the devices should belong to
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.Set[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDeviceAliases(self) -> java.util.Set[str]: ...
    def getDeviceGroupIds(self) -> java.util.Set[int]: ...
    def getDeviceGroupNames(self) -> java.util.Set[str]: ...
    def getDeviceNamePattern(self) -> str:
        """
            Returns device name pattern that is used to search the matching devices. The pattern is used for SQL LIKE statement so
            it can contains characters supported by the statement like % or _ (underscore). The matching is case insensitive i.e. if
            the device name is ABC123 - pattern abc% will match it.
        
            Returns:
                the device name pattern
        
        
        """
        ...
    def getDeviceNames(self) -> java.util.Set[str]: ...
    def getDeviceTypeNamePattern(self) -> str:
        """
            Returns device type name pattern that can contain the following wildcard characters: *****, **%** and **_**
            (underscore). The ***** character has the same meaning as **%** (any string).
        
            Returns:
                device type name pattern
        
        
        """
        ...
    def getDeviceTypeNames(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersions(self) -> java.util.Set[DeviceTypeVersion]: ...
    def getElementName(self) -> str:
        """
        
            Returns:
                element name
        
        
        """
        ...
    def getFecNames(self) -> java.util.Set[str]: ...
    def getMetaType(self) -> DeviceMetaTypeEnum:
        """
        
            Returns:
                device meta type, that the requested devices should belong to.
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getServerNames(self) -> java.util.Set[str]: ...
    def isMultiplexed(self) -> bool:
        """
            Determines whether devices to be returned should be multiplexed or not.
        
            Returns:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#TRUE>` if multiplexed
                devices should be returned, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#FALSE>` if non-multiplexed,
                :code:`null` if both, multiplexed and non-multiplexed should be returned
        
            Also see:
                :meth:`~cern.lsa.domain.devices.Device.isMultiplexed`
        
        
        """
        ...

class PowerConverterNestedCircuitInfo:
    """
    @Immutable public interface PowerConverterNestedCircuitInfo
    """
    def getActualDeviceName(self) -> str: ...
    def getCoefficient(self) -> int: ...
    def getLogicalDeviceName(self) -> str: ...

class PowerConverterNestedCircuitInfosRequest:
    """
    @Immutable public interface PowerConverterNestedCircuitInfosRequest
    """
    @staticmethod
    def builder() -> 'DefaultPowerConverterNestedCircuitInfosRequest.Builder': ...
    @staticmethod
    def byActualDeviceNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'PowerConverterNestedCircuitInfosRequest': ...
    @staticmethod
    def byActualDevices(collection: typing.Union[java.util.Collection[Device], typing.Sequence[Device]]) -> 'PowerConverterNestedCircuitInfosRequest': ...
    @staticmethod
    def byLogicalDeviceNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'PowerConverterNestedCircuitInfosRequest': ...
    @staticmethod
    def byLogicalDevices(collection: typing.Union[java.util.Collection[Device], typing.Sequence[Device]]) -> 'PowerConverterNestedCircuitInfosRequest': ...
    def check(self) -> None: ...
    @staticmethod
    def forSingleLogicalActualRelation(string: str, string2: str) -> 'PowerConverterNestedCircuitInfosRequest': ...
    def getActualDeviceNames(self) -> java.util.List[str]: ...
    def getLogicalDeviceNames(self) -> java.util.List[str]: ...

class DefaultCalibrationsRequest(CalibrationsRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultCalibrationsRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.devices.CalibrationsRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.devices.CalibrationsRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultCalibrationsRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultCalibrationsRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.devices.DefaultCalibrationsRequest`.
        
            .. code-block: java
            
             DefaultCalibrationsRequest.builder()
                .particleTransfer(cern.accsoft.commons.domain.particletransfers.ParticleTransfer | null) // nullable :meth:`~cern.lsa.domain.devices.CalibrationsRequest.getParticleTransfer`
                .calibrationNames(Set<String> | null) // nullable :meth:`~cern.lsa.domain.devices.CalibrationsRequest.getCalibrationNames`
                .logicalHardwareName(String | null) // nullable :meth:`~cern.lsa.domain.devices.CalibrationsRequest.getLogicalHardwareName`
                .build();
             
        
            Returns:
                A new DefaultCalibrationsRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(calibrationsRequest: CalibrationsRequest) -> 'DefaultCalibrationsRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.devices.CalibrationsRequest` value. Uses accessors to get values
            to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.devices.CalibrationsRequest`): The instance to copy
        
            Returns:
                A copied immutable CalibrationsRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getCalibrationNames(self) -> com.google.common.collect.ImmutableSet[str]: ...
    def getLogicalHardwareName(self) -> str: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`particleTransfer`, :code:`calibrationNames`, :code:`logicalHardwareName`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`CalibrationsRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withCalibrationNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultCalibrationsRequest': ...
    @typing.overload
    def withCalibrationNames(self, stringArray: typing.List[str]) -> 'DefaultCalibrationsRequest': ...
    def withLogicalHardwareName(self, string: str) -> 'DefaultCalibrationsRequest': ...
    def withParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultCalibrationsRequest': ...
    class Builder:
        def addAllCalibrationNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultCalibrationsRequest.Builder': ...
        def addCalibrationName(self, string: str) -> 'DefaultCalibrationsRequest.Builder': ...
        def addCalibrationNames(self, stringArray: typing.List[str]) -> 'DefaultCalibrationsRequest.Builder': ...
        def build(self) -> 'DefaultCalibrationsRequest': ...
        def calibrationNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultCalibrationsRequest.Builder': ...
        def logicalHardwareName(self, string: str) -> 'DefaultCalibrationsRequest.Builder': ...
        def particleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultCalibrationsRequest.Builder': ...

class DefaultPowerConverterNestedCircuitInfo(PowerConverterNestedCircuitInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultPowerConverterNestedCircuitInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultPowerConverterNestedCircuitInfo.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultPowerConverterNestedCircuitInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.devices.DefaultPowerConverterNestedCircuitInfo`.
        
            .. code-block: java
            
             DefaultPowerConverterNestedCircuitInfo.builder()
                .logicalDeviceName(String) // required :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo.getLogicalDeviceName`
                .actualDeviceName(String) // required :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo.getActualDeviceName`
                .coefficient(int) // required :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo.getCoefficient`
                .build();
             
        
            Returns:
                A new DefaultPowerConverterNestedCircuitInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(powerConverterNestedCircuitInfo: PowerConverterNestedCircuitInfo) -> 'DefaultPowerConverterNestedCircuitInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo`): The instance to copy
        
            Returns:
                A copied immutable PowerConverterNestedCircuitInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getActualDeviceName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo.getActualDeviceName`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo`
        
            Returns:
                The value of the :code:`actualDeviceName` attribute
        
        
        """
        ...
    def getCoefficient(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo.getCoefficient`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo`
        
            Returns:
                The value of the :code:`coefficient` attribute
        
        
        """
        ...
    def getLogicalDeviceName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo.getLogicalDeviceName`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo`
        
            Returns:
                The value of the :code:`logicalDeviceName` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`logicalDeviceName`, :code:`actualDeviceName`, :code:`coefficient`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`PowerConverterNestedCircuitInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withActualDeviceName(self, string: str) -> 'DefaultPowerConverterNestedCircuitInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo.getActualDeviceName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for actualDeviceName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withCoefficient(self, int: int) -> 'DefaultPowerConverterNestedCircuitInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo.getCoefficient` attribute. A value equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (int): A new value for coefficient
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withLogicalDeviceName(self, string: str) -> 'DefaultPowerConverterNestedCircuitInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfo.getLogicalDeviceName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for logicalDeviceName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def actualDeviceName(self, string: str) -> 'DefaultPowerConverterNestedCircuitInfo.Builder': ...
        def build(self) -> 'DefaultPowerConverterNestedCircuitInfo': ...
        def coefficient(self, int: int) -> 'DefaultPowerConverterNestedCircuitInfo.Builder': ...
        def logicalDeviceName(self, string: str) -> 'DefaultPowerConverterNestedCircuitInfo.Builder': ...

class DefaultPowerConverterNestedCircuitInfosRequest(PowerConverterNestedCircuitInfosRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultPowerConverterNestedCircuitInfosRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfosRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfosRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultPowerConverterNestedCircuitInfosRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultPowerConverterNestedCircuitInfosRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.devices.DefaultPowerConverterNestedCircuitInfosRequest`.
        
            .. code-block: java
            
             DefaultPowerConverterNestedCircuitInfosRequest.builder()
                .logicalDeviceNames(List<String> | null) // nullable :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfosRequest.getLogicalDeviceNames`
                .actualDeviceNames(List<String> | null) // nullable :meth:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfosRequest.getActualDeviceNames`
                .build();
             
        
            Returns:
                A new DefaultPowerConverterNestedCircuitInfosRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(powerConverterNestedCircuitInfosRequest: PowerConverterNestedCircuitInfosRequest) -> 'DefaultPowerConverterNestedCircuitInfosRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfosRequest` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.devices.PowerConverterNestedCircuitInfosRequest`): The instance to copy
        
            Returns:
                A copied immutable PowerConverterNestedCircuitInfosRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getActualDeviceNames(self) -> java.util.List[str]: ...
    def getLogicalDeviceNames(self) -> java.util.List[str]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`logicalDeviceNames`, :code:`actualDeviceNames`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`PowerConverterNestedCircuitInfosRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withActualDeviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPowerConverterNestedCircuitInfosRequest': ...
    @typing.overload
    def withActualDeviceNames(self, stringArray: typing.List[str]) -> 'DefaultPowerConverterNestedCircuitInfosRequest': ...
    @typing.overload
    def withLogicalDeviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPowerConverterNestedCircuitInfosRequest': ...
    @typing.overload
    def withLogicalDeviceNames(self, stringArray: typing.List[str]) -> 'DefaultPowerConverterNestedCircuitInfosRequest': ...
    class Builder:
        def actualDeviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPowerConverterNestedCircuitInfosRequest.Builder': ...
        def addActualDeviceName(self, string: str) -> 'DefaultPowerConverterNestedCircuitInfosRequest.Builder': ...
        def addActualDeviceNames(self, stringArray: typing.List[str]) -> 'DefaultPowerConverterNestedCircuitInfosRequest.Builder': ...
        def addAllActualDeviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPowerConverterNestedCircuitInfosRequest.Builder': ...
        def addAllLogicalDeviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPowerConverterNestedCircuitInfosRequest.Builder': ...
        def addLogicalDeviceName(self, string: str) -> 'DefaultPowerConverterNestedCircuitInfosRequest.Builder': ...
        def addLogicalDeviceNames(self, stringArray: typing.List[str]) -> 'DefaultPowerConverterNestedCircuitInfosRequest.Builder': ...
        def build(self) -> 'DefaultPowerConverterNestedCircuitInfosRequest': ...
        def logicalDeviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultPowerConverterNestedCircuitInfosRequest.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.devices")``.

    CalibrationsRequest: typing.Type[CalibrationsRequest]
    DefaultCalibrationsRequest: typing.Type[DefaultCalibrationsRequest]
    DefaultPowerConverterNestedCircuitInfo: typing.Type[DefaultPowerConverterNestedCircuitInfo]
    DefaultPowerConverterNestedCircuitInfosRequest: typing.Type[DefaultPowerConverterNestedCircuitInfosRequest]
    Device: typing.Type[Device]
    DeviceFilter: typing.Type[DeviceFilter]
    DeviceGroup: typing.Type[DeviceGroup]
    DeviceGroupFilter: typing.Type[DeviceGroupFilter]
    DeviceGroupType: typing.Type[DeviceGroupType]
    DeviceGroups: typing.Type[DeviceGroups]
    DeviceGroupsRequest: typing.Type[DeviceGroupsRequest]
    DeviceMetaTypeEnum: typing.Type[DeviceMetaTypeEnum]
    DeviceType: typing.Type[DeviceType]
    DeviceTypeImplementation: typing.Type[DeviceTypeImplementation]
    DeviceTypeVersion: typing.Type[DeviceTypeVersion]
    DeviceTypeVersionNumber: typing.Type[DeviceTypeVersionNumber]
    DeviceTypes: typing.Type[DeviceTypes]
    DeviceTypesRequest: typing.Type[DeviceTypesRequest]
    Devices: typing.Type[Devices]
    DevicesRequest: typing.Type[DevicesRequest]
    PowerConverterNestedCircuitInfo: typing.Type[PowerConverterNestedCircuitInfo]
    PowerConverterNestedCircuitInfosRequest: typing.Type[PowerConverterNestedCircuitInfosRequest]
    factory: cern.lsa.domain.devices.factory.__module_protocol__
    inca: cern.lsa.domain.devices.inca.__module_protocol__
    spi: cern.lsa.domain.devices.spi.__module_protocol__
    type: cern.lsa.domain.devices.type.__module_protocol__
