import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.lsa.domain.commons.spi
import cern.lsa.domain.devices
import cern.lsa.domain.devices.spi.type
import cern.lsa.domain.settings
import java.io
import java.util
import typing



class DeviceGroupImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.devices.DeviceGroup], cern.lsa.domain.devices.DeviceGroup):
    """
    public class DeviceGroupImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.devices.DeviceGroup`> implements :class:`~cern.lsa.domain.devices.DeviceGroup`
    
        Default implementation of :class:`~cern.lsa.domain.devices.DeviceGroup` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup): ...
    @typing.overload
    def __init__(self, string: str, deviceGroupType: cern.lsa.domain.devices.DeviceGroupType, accelerator: cern.accsoft.commons.domain.Accelerator): ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DeviceGroup.getAccelerator`
            Returns the accelerator which this device group belongs to.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceGroup.getAccelerator` in interface :class:`~cern.lsa.domain.devices.DeviceGroup`
        
            Returns:
                the accelerator which this device group belongs to
        
        
        """
        ...
    def getChildGroups(self) -> java.util.Set[cern.lsa.domain.devices.DeviceGroup]: ...
    def getCreateTime(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DeviceGroup.getCreateTime`
            Time of creation of the group.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceGroup.getCreateTime` in interface :class:`~cern.lsa.domain.devices.DeviceGroup`
        
            Returns:
                time of creation
        
        
        """
        ...
    def getCreator(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DeviceGroup.getCreator`
            Login name of user who created this group.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceGroup.getCreator` in interface :class:`~cern.lsa.domain.devices.DeviceGroup`
        
            Returns:
                name of user who created this group
        
        
        """
        ...
    def getDisplayName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DeviceGroup.getDisplayName`
            Returns the display name of this device group.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceGroup.getDisplayName` in interface :class:`~cern.lsa.domain.devices.DeviceGroup`
        
            Returns:
                the display name of this device group
        
        
        """
        ...
    def getModifier(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DeviceGroup.getModifier`
            Login name of user who performed last modification. If the group hasn't been modified after creation, this method
            returns :meth:`~cern.lsa.domain.devices.DeviceGroup.getCreator`.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceGroup.getModifier` in interface :class:`~cern.lsa.domain.devices.DeviceGroup`
        
            Returns:
                name of user who performed last modification
        
        
        """
        ...
    def getModifyTime(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DeviceGroup.getModifyTime`
            Time of last modification. If the group hasn't been modified after creation, this method returns the
            :meth:`~cern.lsa.domain.devices.DeviceGroup.getCreateTime`.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceGroup.getModifyTime` in interface :class:`~cern.lsa.domain.devices.DeviceGroup`
        
            Returns:
                time of last modification
        
        
        """
        ...
    def getType(self) -> cern.lsa.domain.devices.DeviceGroupType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DeviceGroup.getType`
            Returns the name of type which this group belongs to.
        
            The device group type is used to indicate what kind of devices (or other device groups) it contains. Examples of device
            group types might be "working sets" containing devices of certain types used to control certain area of the accelerator,
            "processes" that consist of working sets, "sets of circuits" that group power converters etc.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceGroup.getType` in interface :class:`~cern.lsa.domain.devices.DeviceGroup`
        
            Returns:
                the non-null type name which this group belongs to
        
        
        """
        ...
    def isOperational(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DeviceGroup.isOperational`
            Returns :code:`true` if this device group is operational i.e. used by users in the production environment. A
            non-operational groups can be created for debugging or testing purposes.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceGroup.isOperational` in interface :class:`~cern.lsa.domain.devices.DeviceGroup`
        
            Returns:
                :code:`true` if this device group is operational, :code:`false` otherwise
        
        
        """
        ...
    def setAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> None: ...
    def setChildGroups(self, set: java.util.Set[cern.lsa.domain.devices.DeviceGroup]) -> None: ...
    def setCreateTime(self, date: java.util.Date) -> None: ...
    def setCreator(self, string: str) -> None:
        """
            Sets name of the creator.
        
            Parameters:
                creator (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): login name of the user who created this device group
        
            Also see:
                :meth:`~cern.lsa.domain.devices.spi.DeviceGroupImpl.getCreator`
        
        
        """
        ...
    def setDisplayName(self, string: str) -> None: ...
    def setModifier(self, string: str) -> None:
        """
            Sets name of the user who recently modified this group.
        
            Parameters:
                modifier (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): user who recently modified this group
        
            Also see:
                :meth:`~cern.lsa.domain.devices.spi.DeviceGroupImpl.getModifier`
        
        
        """
        ...
    def setModifyTime(self, date: java.util.Date) -> None:
        """
            Sets time of last modification of this group.
        
            Parameters:
                modifyTime (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): modification time
        
            Also see:
                :meth:`~cern.lsa.domain.devices.spi.DeviceGroupImpl.getModifyTime`
        
        
        """
        ...
    def setOperational(self, boolean: bool) -> None: ...
    def setType(self, deviceGroupType: cern.lsa.domain.devices.DeviceGroupType) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.devices.DeviceGroup`
        
        
        """
        ...

class DeviceGroupsRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.devices.DeviceGroupsRequest):
    """
    public class DeviceGroupsRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.devices.DeviceGroupsRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.devices.DeviceGroupsRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    ACCELERATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ACCELERATOR
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DeviceGroupsRequestImpl.getAccelerator`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_GROUP_NAME_PATTERN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_GROUP_NAME_PATTERN
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DeviceGroupsRequestImpl.getDeviceGroupNamePattern`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_GROUP_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_GROUP_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DeviceGroupsRequestImpl.getDeviceGroupNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_GROUP_TYPES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_GROUP_TYPES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DeviceGroupsRequestImpl.getDeviceGroupTypes`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceGroupsRequest.getAccelerator`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceGroupsRequest`
        
            Returns:
                accelerator that the device of the groups should belong to
        
        
        """
        ...
    def getDeviceGroupNamePattern(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DeviceGroupsRequest.getDeviceGroupNamePattern`
            Returns device group name pattern that is used to search the matching device groups. The pattern is used for SQL LIKE
            statement so it can contains characters supported by the statement like % or _ (underscore). The matching is case
            insensitive i.e. if the device group name is ABC123 - pattern abc% will match it.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceGroupsRequest.getDeviceGroupNamePattern`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceGroupsRequest`
        
            Returns:
                the device group name pattern
        
        
        """
        ...
    def getDeviceGroupNames(self) -> java.util.Set[str]: ...
    def getDeviceGroupTypes(self) -> java.util.Set[cern.lsa.domain.devices.DeviceGroupType]: ...

class DeviceImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.devices.Device], cern.lsa.domain.devices.Device):
    """
    public class DeviceImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.devices.Device`> implements :class:`~cern.lsa.domain.devices.Device`
    
        Default implementation of the :class:`~cern.lsa.domain.devices.Device` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, device: cern.lsa.domain.devices.Device): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...
    def addDeviceGroup(self, string: str) -> None: ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getAccelerator` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                the accelerator to which this device belongs.
        
        
        """
        ...
    def getAcceleratorZone(self) -> cern.accsoft.commons.domain.zones.AcceleratorZone:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.getAcceleratorZone`
            Returns the accelerator zone this device belongs to.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getAcceleratorZone` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                the accelerator zone this device belongs to
        
        
        """
        ...
    def getAlias(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getAlias` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                Alias name of the device. An alias is another way of naming the devices used commonly by the operators.
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.getDescription`
            Returns an optional description of this device
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getDescription` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                an description of this device or :code:`null`
        
        
        """
        ...
    def getDeviceGroups(self) -> java.util.Set[str]: ...
    def getDeviceType(self) -> cern.lsa.domain.devices.DeviceType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.getDeviceType`
            Returns type of this device.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getDeviceType` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                the non :code:`null` type of this device
        
        
        """
        ...
    def getDeviceTypeVersion(self) -> cern.lsa.domain.devices.DeviceTypeVersion:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.getDeviceTypeVersion`
            The type version of this device.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getDeviceTypeVersion` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                the non :code:`null` type version of this device
        
        
        """
        ...
    def getFecName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.getFecName`
            Name of the FEC responsible for device.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getFecName` in interface :class:`~cern.lsa.domain.devices.Device`
        
        
        """
        ...
    def getPosition(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.getPosition`
            Devices can be located relative to the start of the corresponding accelerator zone. The position indicates the position
            e.g. in meters. If the value is not filled, the position will be zero.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getPosition` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                the position of the device
        
        
        """
        ...
    def getServerName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.getServerName`
            Name of the server (e.g. CMW).
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getServerName` in interface :class:`~cern.lsa.domain.devices.Device`
        
        
        """
        ...
    def getSortOrder(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.getSortOrder`
            Devices can be located relative to the start of the corresponding accelerator zone. When two devices have the same
            position, then the sort order will be taken into account e.g. in the GUIs.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getSortOrder` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                the sort order for devices with the same position
        
        
        """
        ...
    def getState(self) -> cern.lsa.domain.devices.Device.DeviceState:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.getState` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                device state
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.isCycleBound`
            Returns :code:`true` if this device is cycle-bound, meaning that updates of at least one of its acquisition properties
            are valid only for the cycle when the acquisition has been done. More details can be found in "Device Property behaviour
            and contextual data" EDMS document: [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.isCycleBound` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                :code:`true` if this device is cycle-bound
        
        
        """
        ...
    def isLsaImplementation(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.isLsaImplementation`
            Indicate whether the device is served by InCA/LSA
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.isLsaImplementation` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                :code:`true`, if the the server corresponds to InCA or LSA server. :code:`false` otherwise.
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.Device.isMultiplexed`
            Returns :code:`true` if this device is multiplexed, meaning at least one of its setting properties is capable of storing
            settings for different timing users. More details can be found in "Device Property behaviour and contextual data" EDMS
            document: [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.Device.isMultiplexed` in interface :class:`~cern.lsa.domain.devices.Device`
        
            Returns:
                :code:`true` if this device is multiplexed
        
        
        """
        ...
    def setAcceleratorZone(self, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> None:
        """
            Assigns this devices to specified accelerator zone.
        
        """
        ...
    def setAlias(self, string: str) -> None: ...
    def setCycleBound(self, boolean: bool) -> None: ...
    def setDescription(self, string: str) -> None: ...
    def setDeviceGroups(self, set: java.util.Set[str]) -> None: ...
    def setDeviceTypeVersion(self, deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion) -> None:
        """
            Sets device type to which this device belong.
        
        """
        ...
    def setFecName(self, string: str) -> None: ...
    def setLsaImplementation(self, boolean: bool) -> None: ...
    def setMultiplexed(self, boolean: bool) -> None: ...
    def setPosition(self, double: float) -> None: ...
    def setServerName(self, string: str) -> None: ...
    def setSortOrder(self, int: int) -> None: ...
    def setState(self, deviceState: cern.lsa.domain.devices.Device.DeviceState) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.devices.Device`
        
        
        """
        ...

class DeviceTypeImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.devices.DeviceType], cern.lsa.domain.devices.DeviceType):
    """
    public class DeviceTypeImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.devices.DeviceType`> implements :class:`~cern.lsa.domain.devices.DeviceType`
    
        Default implementation of the :class:`~cern.lsa.domain.devices.DeviceType` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, long: int, string: str): ...
    def addVersion(self, deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion) -> None: ...
    def compareTo(self, deviceType: cern.lsa.domain.devices.DeviceType) -> int:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                :code:`compareTo` in class :class:`~cern.lsa.domain.devices.DeviceType`
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceType.getDescription` in interface :class:`~cern.lsa.domain.devices.DeviceType`
        
            Returns:
                the description for the device type or :code:`null` if not defined
        
        
        """
        ...
    def getMetaType(self) -> cern.lsa.domain.devices.DeviceMetaTypeEnum:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceType.getMetaType` in interface :class:`~cern.lsa.domain.devices.DeviceType`
        
            Returns:
                the meta type of the device Type : can be 'B' for BEAM , 'L' for LOGICAL or 'A' for ACTUAL.
        
        
        """
        ...
    def getVersions(self) -> java.util.SortedSet[cern.lsa.domain.devices.DeviceTypeVersion]: ...
    def setDescription(self, string: str) -> None: ...
    def setMetaType(self, deviceMetaTypeEnum: cern.lsa.domain.devices.DeviceMetaTypeEnum) -> None: ...
    def setVersions(self, set: java.util.Set[cern.lsa.domain.devices.DeviceTypeVersion]) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.devices.DeviceType`
        
        
        """
        ...

class DeviceTypeVersionImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedEntity[cern.lsa.domain.devices.DeviceTypeVersion], cern.lsa.domain.devices.DeviceTypeVersion):
    """
    public class DeviceTypeVersionImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity`<:class:`~cern.lsa.domain.devices.DeviceTypeVersion`> implements :class:`~cern.lsa.domain.devices.DeviceTypeVersion`
    
        Default implementation of the :code:`DeviceTypeVersion` interface
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, long: int, deviceType: cern.lsa.domain.devices.DeviceType, deviceTypeImplementation: cern.lsa.domain.devices.DeviceTypeImplementation, deviceTypeVersionNumber: cern.lsa.domain.devices.DeviceTypeVersionNumber): ...
    def compareTo(self, deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion) -> int:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.compareTo`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Description copied from class: :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.equals`
            Returns :code:`true` if the given object is of the same class and has the same ID.
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.equals`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity`
        
            Also see:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.getId`
        
        
        """
        ...
    def getDeviceType(self) -> cern.lsa.domain.devices.DeviceType:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceTypeVersion.getDeviceType`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceTypeVersion`
        
            Returns:
                the device type this version is specified for
        
        
        """
        ...
    def getImplementation(self) -> cern.lsa.domain.devices.DeviceTypeImplementation:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceTypeVersion.getImplementation`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceTypeVersion`
        
            Returns:
                the implementation type for this device type version. Can be :code:`null` in case of implementation types we still have
                in the DB but not support anymore (like SL)
        
        
        """
        ...
    def getVersionNumber(self) -> cern.lsa.domain.devices.DeviceTypeVersionNumber:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceTypeVersion.getVersionNumber`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceTypeVersion`
        
            Returns:
                the version number (major, minor)
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Description copied from class: :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.hashCode`
            Redefines equals in term of the name
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.hashCode`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity`
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#hashCode()>`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class DeviceTypeVersionNumberImpl(cern.lsa.domain.devices.DeviceTypeVersionNumber, java.io.Serializable):
    """
    public class DeviceTypeVersionNumberImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.devices.DeviceTypeVersionNumber`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :code:`DeviceTypeVersionNumber` interface
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, int: int, int2: int): ...
    def compareTo(self, deviceTypeVersionNumber: cern.lsa.domain.devices.DeviceTypeVersionNumber) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getMajor(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceTypeVersionNumber.getMajor`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceTypeVersionNumber`
        
        
        """
        ...
    def getMinor(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceTypeVersionNumber.getMinor`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceTypeVersionNumber`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class DeviceTypesRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.devices.DeviceTypesRequest):
    """
    public class DeviceTypesRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.devices.DeviceTypesRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.devices.DeviceTypesRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    ACCELERATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ACCELERATOR
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DeviceTypesRequestImpl.getAccelerator`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ALL_DEV_TYPES_REQUESTED: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ALL_DEV_TYPES_REQUESTED
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DeviceTypesRequestImpl.getAllTypesRequested` indicating that all
        the device types are requested.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_TYPE_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_TYPE_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DeviceTypesRequestImpl.getDeviceTypeNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_TYPE_NAME_PATTERN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_TYPE_NAME_PATTERN
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DeviceTypesRequestImpl.getDeviceTypeNamePattern`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_TYPE_VERSION_NUMBER: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_TYPE_VERSION_NUMBER
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DeviceTypesRequestImpl.getDeviceTypeVersionNumber`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_TYPE_IMPLEMENTATION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_TYPE_IMPLEMENTATION
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DeviceTypesRequestImpl.getDeviceTypeImplementations`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceTypesRequest.getAccelerator`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceTypesRequest`
        
            Returns:
                accelerator that the device of the groups should belong to
        
        
        """
        ...
    def getAllTypesRequested(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceTypesRequest.getAllTypesRequested`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceTypesRequest`
        
            Returns:
                :code:`true` if all types were requested
        
        
        """
        ...
    def getDeviceTypeImplementations(self) -> java.util.Set[cern.lsa.domain.devices.DeviceTypeImplementation]: ...
    def getDeviceTypeNamePattern(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DeviceTypesRequest.getDeviceTypeNamePattern`
            Returns device type name pattern which all device type names should match. The pattern is a SQL pattern accepted by the
            :code:`LIKE` clause (containing **%** or **_** (underscore) characters). Matching is case insensitive.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceTypesRequest.getDeviceTypeNamePattern`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceTypesRequest`
        
        
        """
        ...
    def getDeviceTypeNames(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersionNumber(self) -> cern.lsa.domain.devices.DeviceTypeVersionNumber:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DeviceTypesRequest.getDeviceTypeVersionNumber`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DeviceTypesRequest`
        
            Returns:
                the device type version number the searched device type should have
        
        
        """
        ...

class DevicesRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.devices.DevicesRequest):
    """
    public class DevicesRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.devices.DevicesRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.devices.DevicesRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    ACCELERATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ACCELERATOR
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getAccelerator`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ACCELERATOR_ZONES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ACCELERATOR_ZONES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getAcceleratorZones`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARTICLE_TRANSFERS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARTICLE_TRANSFERS
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getParticleTransfers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_TYPE_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_TYPE_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getDeviceTypeNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_TYPE_NAME_PATTERN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_TYPE_NAME_PATTERN
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getDeviceTypeNamePattern`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    META_TYPE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` META_TYPE
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getMetaType`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getDeviceNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_NAME_PATTERN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_NAME_PATTERN
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getDeviceNamePattern`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MULTIPLEXED: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MULTIPLEXED
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.isMultiplexed` flag.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_GROUP_IDS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_GROUP_IDS
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getDeviceGroupNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_GROUP_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_GROUP_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getDeviceGroupNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ELEMENT_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ELEMENT_NAME
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getElementName`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_ALIAS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_ALIAS
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getDeviceAliases`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FEC_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` FEC_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getFecNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SERVER_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SERVER_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getServerNames` RDA server names}.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_TYPE_VERSIONS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_TYPE_VERSIONS
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.getDeviceTypeVersions`
    
        Also see:
            :meth:`~constant`
    
    
    """
    EXIST_IN_LSA_ONLY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` EXIST_IN_LSA_ONLY
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.DevicesRequestImpl.existInLsaOnly`
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def existInLsaOnly(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.existInLsaOnly`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DevicesRequest`
        
            Returns:
                true if we want to see devices that exists only in LSA (and not in CCDB)
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getAccelerator`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DevicesRequest`
        
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
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceNamePattern`
            Returns device name pattern that is used to search the matching devices. The pattern is used for SQL LIKE statement so
            it can contains characters supported by the statement like % or _ (underscore). The matching is case insensitive i.e. if
            the device name is ABC123 - pattern abc% will match it.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceNamePattern`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DevicesRequest`
        
            Returns:
                the device name pattern
        
        
        """
        ...
    def getDeviceNames(self) -> java.util.Set[str]: ...
    def getDeviceTypeNamePattern(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceTypeNamePattern`
            Returns device type name pattern that can contain the following wildcard characters: *****, **%** and **_**
            (underscore). The ***** character has the same meaning as **%** (any string).
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getDeviceTypeNamePattern`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DevicesRequest`
        
            Returns:
                device type name pattern
        
        
        """
        ...
    def getDeviceTypeNames(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersions(self) -> java.util.Set[cern.lsa.domain.devices.DeviceTypeVersion]: ...
    def getElementName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getElementName`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DevicesRequest`
        
            Returns:
                element name
        
        
        """
        ...
    def getFecNames(self) -> java.util.Set[str]: ...
    def getMetaType(self) -> cern.lsa.domain.devices.DeviceMetaTypeEnum:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.getMetaType`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DevicesRequest`
        
            Returns:
                device meta type, that the requested devices should belong to.
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getServerNames(self) -> java.util.Set[str]: ...
    def isMultiplexed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.devices.DevicesRequest.isMultiplexed`
            Determines whether devices to be returned should be multiplexed or not.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.DevicesRequest.isMultiplexed`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.DevicesRequest`
        
            Returns:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#TRUE>` if multiplexed
                devices should be returned, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#FALSE>` if non-multiplexed,
                :code:`null` if both, multiplexed and non-multiplexed should be returned
        
            Also see:
                :meth:`~cern.lsa.domain.devices.Device.isMultiplexed`
        
        
        """
        ...

class ParameterGroupImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.settings.ParameterGroup], cern.lsa.domain.settings.ParameterGroup):
    """
    public class ParameterGroupImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.settings.ParameterGroup`> implements :class:`~cern.lsa.domain.settings.ParameterGroup`
    
        Default implementation of :class:`~cern.lsa.domain.settings.ParameterGroup`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterGroup.getAccelerator`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterGroup`
        
            Returns:
                accelerator to which group belongs.
        
        
        """
        ...
    def getCreateDate(self) -> java.util.Date:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterGroup.getCreateDate`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterGroup`
        
            Returns:
                date when group was created
        
        
        """
        ...
    def getCreator(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterGroup.getCreator`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterGroup`
        
            Returns:
                identifier of a person who created this group.
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterGroup.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterGroup`
        
            Returns:
                descriptions of group.
        
        
        """
        ...
    def setAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> None:
        """
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): 
        
        """
        ...
    def setCreateDate(self, date: java.util.Date) -> None:
        """
        
            Parameters:
                createDate (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): 
        
        """
        ...
    def setCreator(self, string: str) -> None:
        """
        
            Parameters:
                creator (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...
    def setDescription(self, string: str) -> None:
        """
        
            Parameters:
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.settings.ParameterGroup`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.devices.spi")``.

    DeviceGroupImpl: typing.Type[DeviceGroupImpl]
    DeviceGroupsRequestImpl: typing.Type[DeviceGroupsRequestImpl]
    DeviceImpl: typing.Type[DeviceImpl]
    DeviceTypeImpl: typing.Type[DeviceTypeImpl]
    DeviceTypeVersionImpl: typing.Type[DeviceTypeVersionImpl]
    DeviceTypeVersionNumberImpl: typing.Type[DeviceTypeVersionNumberImpl]
    DeviceTypesRequestImpl: typing.Type[DeviceTypesRequestImpl]
    DevicesRequestImpl: typing.Type[DevicesRequestImpl]
    ParameterGroupImpl: typing.Type[ParameterGroupImpl]
    type: cern.lsa.domain.devices.spi.type.__module_protocol__
