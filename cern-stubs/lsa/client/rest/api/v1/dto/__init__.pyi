import cern.accsoft.commons.util
import cern.lsa.client.rest.api.v1.dto.commons
import cern.lsa.client.rest.api.v1.dto.settings
import cern.lsa.client.rest.api.v1.dto.trim
import java.lang
import java.time
import java.util
import typing



class AcceleratorZoneDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface AcceleratorZoneDto extends cern.accsoft.commons.util.Named
    
        AcceleratorZoneRest
    """
    @staticmethod
    def builder() -> 'DefaultAcceleratorZoneDto.Builder': ...
    def getAcceleratorName(self) -> str: ...

class BooleanItemDto:
    """
    @Immutable public interface BooleanItemDto
    """
    @staticmethod
    def builder() -> 'DefaultBooleanItemDto.Builder': ...
    def getStandardMeaning(self) -> str: ...
    def getValue(self) -> bool: ...

class BooleanTypeDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface BooleanTypeDto extends cern.accsoft.commons.util.Named
    """
    @staticmethod
    def builder() -> 'DefaultBooleanTypeDto.Builder': ...
    def getBooleanItems(self) -> java.util.List[BooleanItemDto]: ...

class DeviceDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface DeviceDto extends cern.accsoft.commons.util.Named
    
        DeviceRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceDto.Builder': ...
    def getAcceleratorZone(self) -> AcceleratorZoneDto: ...
    def getDescription(self) -> str: ...
    def getDeviceAlias(self) -> str: ...
    def getDeviceGroups(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersion(self) -> 'DeviceTypeVersionContainerDto': ...
    def getFecName(self) -> str: ...
    def getId(self) -> int: ...
    def getPosition(self) -> float: ...
    def getServerName(self) -> str: ...
    def getSortOrder(self) -> int: ...
    def getState(self) -> 'DeviceStateDto': ...
    def isCycleBound(self) -> bool: ...
    def isMultiplexed(self) -> bool: ...

class DeviceMetaTypeDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface DeviceMetaTypeDto extends cern.accsoft.commons.util.Named
    
        DeviceMetaTypeEnumRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceMetaTypeDto.Builder': ...

class DeviceStateDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface DeviceStateDto extends cern.accsoft.commons.util.Named
    
        DeviceStateRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceStateDto.Builder': ...

class DeviceTypeImplementationDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface DeviceTypeImplementationDto extends cern.accsoft.commons.util.Named
    
        DeviceTypeImplementationRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeImplementationDto.Builder': ...

class DeviceTypeVersionContainerDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface DeviceTypeVersionContainerDto extends cern.accsoft.commons.util.Named
    
        DeviceTypeVersionContainerRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionContainerDto.Builder': ...
    def getDescription(self) -> str: ...
    def getId(self) -> int: ...
    def getMetaType(self) -> DeviceMetaTypeDto: ...
    def getOtherVersions(self) -> java.util.List['DeviceTypeVersionDto']: ...
    def getPrimaryVersion(self) -> 'DeviceTypeVersionDto': ...

class DeviceTypeVersionDto:
    """
    @Immutable public interface DeviceTypeVersionDto
    
        DeviceTypeVersionRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionDto.Builder': ...
    def getId(self) -> int: ...
    def getImplementation(self) -> DeviceTypeImplementationDto: ...
    def getVersionNumber(self) -> 'DeviceTypeVersionNumberDto': ...

class DeviceTypeVersionNumberDto:
    """
    @Immutable public interface DeviceTypeVersionNumberDto
    
        DeviceTypeVersionNumberRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionNumberDto.Builder': ...
    def getMajor(self) -> int: ...
    def getMinor(self) -> int: ...

class EnumItemDto:
    """
    @Immutable public interface EnumItemDto
    """
    @staticmethod
    def builder() -> 'DefaultEnumItemDto.Builder': ...
    def getCode(self) -> int: ...
    def getStandardMeaning(self) -> str: ...
    def getSymbol(self) -> str: ...
    def isSettable(self) -> bool: ...

class EnumTypeDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface EnumTypeDto extends cern.accsoft.commons.util.Named
    """
    @staticmethod
    def builder() -> 'DefaultEnumTypeDto.Builder': ...
    def getEnumItems(self) -> java.util.List[EnumItemDto]: ...
    def getEnumTypeBitSize(self) -> str: ...

class ErrorDto:
    """
    @Immutable public interface ErrorDto
    
        ErrorDto
    """
    @staticmethod
    def builder() -> 'DefaultErrorDto.Builder': ...
    def getErrorType(self) -> str: ...
    def getMessage(self) -> str: ...
    def getPath(self) -> str: ...
    def getTimestamp(self) -> java.time.OffsetDateTime: ...

class IncaPropertyFieldInfoDto:
    """
    @Immutable public interface IncaPropertyFieldInfoDto
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfoDto.Builder': ...
    def getAssociatedPropertyFieldRest(self) -> 'PropertyFieldDto': ...
    def getControlWarningMessage(self) -> str: ...
    def getDisplayFormat(self) -> str: ...
    def getDisplayName(self) -> str: ...
    def getParameterValueCompareType(self) -> str:
        """
            Returns the comparison type that should be applied for this parameter type when calculating value status.
        
            Returns:
                type of parameter value comparison
        
        
        """
        ...
    def getPropertyFieldRest(self) -> 'PropertyFieldDto':
        """
        
            Returns:
                property-field this info is attached to
        
        
        """
        ...
    def isMainStatus(self) -> bool:
        """
            Indicates if this parameter type represents the main status property for given device type. The main status property
            typically indicates if the device is enabled, disabled or in a faulty state. It's value type is either an enumeration or
            boolean. Note that for a given device type, only a single parameter type can represent the main status.
        
            Returns:
                :code:`true` if this parameter type represents the main status property field
        
        
        """
        ...

class IncaPropertyFieldInfosRequestDto:
    """
    @Immutable public interface IncaPropertyFieldInfosRequestDto
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfosRequestDto.Builder': ...
    @staticmethod
    def byPropertyFieldId(long: int) -> 'IncaPropertyFieldInfosRequestDto': ...
    @staticmethod
    def byPropertyFieldIds(set: java.util.Set[int]) -> 'IncaPropertyFieldInfosRequestDto': ...
    def getPropertyFieldIds(self) -> java.util.Set[int]: ...

class MakeRuleClassInfoDto:
    """
    @Immutable public interface MakeRuleClassInfoDto
    
        MakeRuleClassInfoRest
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleClassInfoDto.Builder': ...
    def getClassName(self) -> str: ...
    def getProductName(self) -> str: ...
    def getVersion(self) -> str: ...

class MakeRuleConfigInfoDto:
    """
    @Immutable public interface MakeRuleConfigInfoDto
    
        MakeRuleConfigInfoRest
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigInfoDto.Builder': ...
    def getMakeRuleConfigStatus(self) -> 'MakeRuleConfigStatusDto': ...
    def getMakeRuleInfo(self) -> 'MakeRuleInfoDto': ...

class MakeRuleConfigStatusDto:
    """
    @Immutable public interface MakeRuleConfigStatusDto
    
        MakeRuleConfigStatusRest
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigStatusDto.Builder': ...
    def getName(self) -> str: ...

class MakeRuleInfoDto:
    """
    @Immutable public interface MakeRuleInfoDto
    
        MakeRuleInfoRest
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleInfoDto.Builder': ...
    def getMakeRuleClassInfo(self) -> MakeRuleClassInfoDto: ...
    def getMakeRuleName(self) -> str: ...

class ParameterAttributesDto:
    """
    @Immutable public interface ParameterAttributesDto
    
        ParameterAttributesRest
    """
    @staticmethod
    def builder() -> 'DefaultParameterAttributesDto.Builder': ...
    def getAbsoluteTolerance(self) -> float: ...
    def getDefaultHierarchy(self) -> str: ...
    def getDevice(self) -> DeviceDto: ...
    def getMaxValue(self) -> float: ...
    def getMinValue(self) -> float: ...
    def getParameterId(self) -> int: ...
    def getParameterName(self) -> str: ...
    def getParameterType(self) -> 'ParameterTypeDto': ...
    def getPropertyField(self) -> 'PropertyFieldDto': ...
    def getRelativeTolerance(self) -> float: ...
    def getXPrecision(self) -> int: ...
    def getYPrecision(self) -> int: ...
    def isBelongsToFunctionBProc(self) -> bool: ...
    def isReservedForOpExperts(self) -> bool: ...
    def isTrimable(self) -> bool: ...

class ParameterDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface ParameterDto extends cern.accsoft.commons.util.Named
    """
    def belongsToFunctionBeamProcess(self) -> bool: ...
    @staticmethod
    def builder() -> 'DefaultParameterDto.Builder': ...
    def getDefaultHierarchy(self) -> str: ...
    def getDevice(self) -> DeviceDto: ...
    def getId(self) -> int: ...
    def getParameterGroups(self) -> java.util.List[str]: ...
    def getParameterType(self) -> 'ParameterTypeDto': ...
    def getPropertyField(self) -> 'PropertyFieldDto': ...
    def getValueDescriptor(self) -> 'ValueDescriptorDto': ...
    def getValueType(self) -> 'TypeDto': ...
    def isCritical(self) -> bool: ...
    def isCycleBound(self) -> bool: ...
    def isLsaImplementation(self) -> bool: ...
    def isMonitorable(self) -> bool: ...
    def isMultiplexed(self) -> bool: ...
    def isPropertySupportingPartialSet(self) -> bool: ...
    def isReadable(self) -> bool: ...
    def isReservedForOpExperts(self) -> bool: ...
    def isTrimable(self) -> bool: ...
    def isWritable(self) -> bool: ...

class ParameterGroupDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface ParameterGroupDto extends cern.accsoft.commons.util.Named
    
        ParameterGroupRest
    """
    @staticmethod
    def builder() -> 'DefaultParameterGroupDto.Builder': ...
    def getAcceleratorName(self) -> str: ...
    def getCreateDate(self) -> java.time.OffsetDateTime: ...
    def getCreator(self) -> str: ...
    def getDescription(self) -> str: ...
    def getId(self) -> int: ...

class ParameterTreeDataDto:
    """
    @Immutable public interface ParameterTreeDataDto
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeDataDto.Builder': ...
    def getNodes(self) -> java.util.Set['ParameterTreeNodeDto']: ...
    def getRelations(self) -> java.util.Set['ParameterTreeRelationDto']: ...
    def getStartNodeIds(self) -> java.util.Set[int]: ...

class ParameterTreeNodeDto:
    """
    @Immutable public interface ParameterTreeNodeDto
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeNodeDto.Builder': ...
    def getParameter(self) -> ParameterDto: ...
    def isSource(self) -> bool: ...

class ParameterTreeRelationDto:
    """
    @Immutable public interface ParameterTreeRelationDto
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeRelationDto.Builder': ...
    def getChildParameterId(self) -> int: ...
    def getParentParameterId(self) -> int: ...

class ParameterTreesRequestDto:
    """
    @Immutable public interface ParameterTreesRequestDto
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreesRequestDto.Builder': ...
    def getHierarchy(self) -> str: ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getTreeDirection(self) -> str: ...

class ParameterTypeCategoryDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface ParameterTypeCategoryDto extends cern.accsoft.commons.util.Named
    
        ParameterTypeCategoryRest
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeCategoryDto.Builder': ...

class ParameterTypeDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface ParameterTypeDto extends cern.accsoft.commons.util.Named
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeDto.Builder': ...
    def getCategory(self) -> ParameterTypeCategoryDto: ...
    def getId(self) -> int: ...
    def isLinkRuleApplicable(self) -> bool: ...

class ParameterTypesRequestDto:
    """
    @Immutable public interface ParameterTypesRequestDto
    """
    def getParameterTypeNames(self) -> java.util.Set[str]: ...
    def isAllParameterTypesRequested(self) -> bool: ...

class ParametersRequestDto:
    """
    @Immutable public interface ParametersRequestDto
    
        Describes criteria when searching for LSA parameters. This object should be created using
        :code:`ParametersRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> 'DefaultParametersRequestDto.Builder': ...
    def getAcceleratorName(self) -> str: ...
    def getAcceleratorZoneNames(self) -> java.util.Set[str]: ...
    def getDeviceIds(self) -> java.util.Set[int]: ...
    def getDeviceNames(self) -> java.util.Set[str]: ...
    def getParameterGroups(self) -> java.util.Set[str]: ...
    def getParameterNamePattern(self) -> str: ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getParameterTypeNames(self) -> java.util.Set[str]: ...
    def getParticleTransferNames(self) -> java.util.Set[str]: ...
    def getPropertyFieldIds(self) -> java.util.Set[int]: ...
    def getPropertyNames(self) -> java.util.Set[str]: ...
    def getValueTypes(self) -> java.util.Set[str]: ...
    def isCritical(self) -> bool: ...
    def isLsaImplementation(self) -> bool: ...
    def isMultiplexed(self) -> bool: ...
    def isReadable(self) -> bool: ...
    def isWritable(self) -> bool: ...

class ParentToChildrenRelationDto:
    """
    @Immutable public interface ParentToChildrenRelationDto
    
        ParentToChildrenRelationRest
    """
    @staticmethod
    def builder() -> 'DefaultParentToChildrenRelationDto.Builder': ...
    def getChildrenIds(self) -> java.util.List[int]: ...
    def getParentId(self) -> int: ...

class PropertyAndDeviceDto:
    """
    @Immutable public interface PropertyAndDeviceDto
    
        PropertyAndDeviceRest
    """
    @staticmethod
    def builder() -> 'DefaultPropertyAndDeviceDto.Builder': ...
    def getDeviceId(self) -> int: ...
    def getPropertyName(self) -> str: ...

class PropertyFieldDto:
    """
    @Immutable public interface PropertyFieldDto
    """
    @staticmethod
    def builder() -> 'DefaultPropertyFieldDto.Builder': ...
    def getDeviceTypeName(self) -> str: ...
    def getFieldName(self) -> str: ...
    def getId(self) -> int: ...
    def getPropertyName(self) -> str: ...

class SaveParameterRelationDto:
    """
    @Immutable public interface SaveParameterRelationDto
    
        SaveParameterRelationRest
    """
    @staticmethod
    def builder() -> 'DefaultSaveParameterRelationDto.Builder': ...
    def getHierarchy(self) -> str: ...
    def getParent2ChildrenRelations(self) -> java.util.List[ParentToChildrenRelationDto]: ...

class TypeDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface TypeDto extends cern.accsoft.commons.util.Named
    
        TypeRest
    """
    @staticmethod
    def builder() -> 'DefaultTypeDto.Builder': ...

class ValueCompareTypeDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface ValueCompareTypeDto extends cern.accsoft.commons.util.Named
    """
    @staticmethod
    def builder() -> 'DefaultValueCompareTypeDto.Builder': ...

class ValueDescriptorDto:
    """
    @Immutable public interface ValueDescriptorDto
    """
    @staticmethod
    def builder() -> 'DefaultValueDescriptorDto.Builder': ...
    def getAbsoluteTolerance(self) -> float: ...
    def getBooleanType(self) -> BooleanTypeDto: ...
    def getColumnCount(self) -> int: ...
    def getEnumType(self) -> EnumTypeDto: ...
    def getMax(self) -> float: ...
    def getMin(self) -> float: ...
    def getRelativeTolerance(self) -> float: ...
    def getRowCount(self) -> int: ...
    def getXPrecision(self) -> int: ...
    def getXUnit(self) -> str: ...
    def getYPrecision(self) -> int: ...
    def getYUnit(self) -> str: ...

class DefaultAcceleratorZoneDto(AcceleratorZoneDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultAcceleratorZoneDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneDto`.
    
        Use the builder to create immutable instances: :code:`DefaultAcceleratorZoneDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultAcceleratorZoneDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultAcceleratorZoneDto`.
        
            .. code-block: java
            
             DefaultAcceleratorZoneDto.builder()
                .name(String) // required name
                .acceleratorName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneDto.getAcceleratorName`
                .build();
             
        
            Returns:
                A new DefaultAcceleratorZoneDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(acceleratorZoneDto: AcceleratorZoneDto) -> 'DefaultAcceleratorZoneDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneDto`): The instance to copy
        
            Returns:
                A copied immutable AcceleratorZoneDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAcceleratorName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneDto.getAcceleratorName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneDto`
        
            Returns:
                The value of the :code:`acceleratorName` attribute
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`, :code:`acceleratorName`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`AcceleratorZoneDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAcceleratorName(self, string: str) -> 'DefaultAcceleratorZoneDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneDto.getAcceleratorName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for acceleratorName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultAcceleratorZoneDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def acceleratorName(self, string: str) -> 'DefaultAcceleratorZoneDto.Builder': ...
        def build(self) -> 'DefaultAcceleratorZoneDto': ...
        def name(self, string: str) -> 'DefaultAcceleratorZoneDto.Builder': ...

class DefaultBooleanItemDto(BooleanItemDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultBooleanItemDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto`.
    
        Use the builder to create immutable instances: :code:`DefaultBooleanItemDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultBooleanItemDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultBooleanItemDto`.
        
            .. code-block: java
            
             DefaultBooleanItemDto.builder()
                .value(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto.getValue`
                .standardMeaning(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto.getStandardMeaning`
                .build();
             
        
            Returns:
                A new DefaultBooleanItemDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(booleanItemDto: BooleanItemDto) -> 'DefaultBooleanItemDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto`): The instance to copy
        
            Returns:
                A copied immutable BooleanItemDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getStandardMeaning(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto.getStandardMeaning`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto`
        
            Returns:
                The value of the :code:`standardMeaning` attribute
        
        
        """
        ...
    def getValue(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto.getValue`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto`
        
            Returns:
                The value of the :code:`value` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`value`, :code:`standardMeaning`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`BooleanItemDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withStandardMeaning(self, string: str) -> 'DefaultBooleanItemDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto.getStandardMeaning` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for standardMeaning
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withValue(self, boolean: bool) -> 'DefaultBooleanItemDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto.getValue` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for value
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultBooleanItemDto': ...
        def standardMeaning(self, string: str) -> 'DefaultBooleanItemDto.Builder': ...
        def value(self, boolean: bool) -> 'DefaultBooleanItemDto.Builder': ...

class DefaultBooleanTypeDto(BooleanTypeDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultBooleanTypeDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeDto`.
    
        Use the builder to create immutable instances: :code:`DefaultBooleanTypeDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultBooleanTypeDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultBooleanTypeDto`.
        
            .. code-block: java
            
             DefaultBooleanTypeDto.builder()
                .name(String) // required name
                .addBooleanItem|addAllBooleanItems(cern.lsa.client.rest.api.v1.dto.BooleanItemDto) // :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeDto.getBooleanItems` elements
                .build();
             
        
            Returns:
                A new DefaultBooleanTypeDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(booleanTypeDto: BooleanTypeDto) -> 'DefaultBooleanTypeDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeDto`): The instance to copy
        
            Returns:
                A copied immutable BooleanTypeDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBooleanItems(self) -> java.util.List[BooleanItemDto]: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`, :code:`booleanItems`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`BooleanTypeDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withBooleanItems(self, booleanItemDtoArray: typing.List[BooleanItemDto]) -> 'DefaultBooleanTypeDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeDto.getBooleanItems`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultBooleanTypeDto` withBooleanItems (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeDto.getBooleanItems`. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemDto`> elements): An iterable of booleanItems elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withBooleanItems(self, iterable: java.lang.Iterable[BooleanItemDto]) -> 'DefaultBooleanTypeDto': ...
    def withName(self, string: str) -> 'DefaultBooleanTypeDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllBooleanItems(self, iterable: java.lang.Iterable[BooleanItemDto]) -> 'DefaultBooleanTypeDto.Builder': ...
        def addBooleanItem(self, booleanItemDto: BooleanItemDto) -> 'DefaultBooleanTypeDto.Builder': ...
        def addBooleanItems(self, booleanItemDtoArray: typing.List[BooleanItemDto]) -> 'DefaultBooleanTypeDto.Builder': ...
        def booleanItems(self, iterable: java.lang.Iterable[BooleanItemDto]) -> 'DefaultBooleanTypeDto.Builder': ...
        def build(self) -> 'DefaultBooleanTypeDto': ...
        def name(self, string: str) -> 'DefaultBooleanTypeDto.Builder': ...

class DefaultDeviceDto(DeviceDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceDto`.
        
            .. code-block: java
            
             DefaultDeviceDto.builder()
                .name(String) // required name
                .acceleratorZone(cern.lsa.client.rest.api.v1.dto.AcceleratorZoneDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getAcceleratorZone`
                .description(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getDescription`
                .deviceAlias(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getDeviceAlias`
                .addDeviceGroup|addAllDeviceGroups(String) // :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getDeviceGroups` elements
                .deviceTypeVersion(cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getDeviceTypeVersion`
                .fecName(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getFecName`
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getId`
                .multiplexed(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.isMultiplexed`
                .cycleBound(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.isCycleBound`
                .position(double) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getPosition`
                .sortOrder(int) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getSortOrder`
                .serverName(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getServerName`
                .state(cern.lsa.client.rest.api.v1.dto.DeviceStateDto | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getState`
                .build();
             
        
            Returns:
                A new DefaultDeviceDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceDto: DeviceDto) -> 'DefaultDeviceDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto` value. Uses accessors to get values
            to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`): The instance to copy
        
            Returns:
                A copied immutable DeviceDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAcceleratorZone(self) -> AcceleratorZoneDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getAcceleratorZone`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`
        
            Returns:
                The value of the :code:`acceleratorZone` attribute
        
        
        """
        ...
    def getDescription(self) -> str: ...
    def getDeviceAlias(self) -> str: ...
    def getDeviceGroups(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersion(self) -> DeviceTypeVersionContainerDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getDeviceTypeVersion`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`
        
            Returns:
                The value of the :code:`deviceTypeVersion` attribute
        
        
        """
        ...
    def getFecName(self) -> str: ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def getPosition(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getPosition`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`
        
            Returns:
                The value of the :code:`position` attribute
        
        
        """
        ...
    def getServerName(self) -> str: ...
    def getSortOrder(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getSortOrder`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`
        
            Returns:
                The value of the :code:`sortOrder` attribute
        
        
        """
        ...
    def getState(self) -> DeviceStateDto: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`, :code:`acceleratorZone`, :code:`description`, :code:`deviceAlias`,
            :code:`deviceGroups`, :code:`deviceTypeVersion`, :code:`fecName`, :code:`id`, :code:`multiplexed`, :code:`cycleBound`,
            :code:`position`, :code:`sortOrder`, :code:`serverName`, :code:`state`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.isCycleBound`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`
        
            Returns:
                The value of the :code:`cycleBound` attribute
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.isMultiplexed`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`
        
            Returns:
                The value of the :code:`multiplexed` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`DeviceDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAcceleratorZone(self, acceleratorZoneDto: AcceleratorZoneDto) -> 'DefaultDeviceDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getAcceleratorZone` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneDto`): A new value for acceleratorZone
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withCycleBound(self, boolean: bool) -> 'DefaultDeviceDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.isCycleBound` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for cycleBound
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDescription(self, string: str) -> 'DefaultDeviceDto': ...
    def withDeviceAlias(self, string: str) -> 'DefaultDeviceDto': ...
    @typing.overload
    def withDeviceGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultDeviceDto': ...
    @typing.overload
    def withDeviceGroups(self, stringArray: typing.List[str]) -> 'DefaultDeviceDto': ...
    def withDeviceTypeVersion(self, deviceTypeVersionContainerDto: DeviceTypeVersionContainerDto) -> 'DefaultDeviceDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getDeviceTypeVersion` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto`): A new value for deviceTypeVersion
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withFecName(self, string: str) -> 'DefaultDeviceDto': ...
    def withId(self, long: int) -> 'DefaultDeviceDto':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getId`
            attribute. A value equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultDeviceDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.isMultiplexed` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for multiplexed
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultDeviceDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPosition(self, double: float) -> 'DefaultDeviceDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getPosition` attribute. A value strict bits equality used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (double): A new value for position
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withServerName(self, string: str) -> 'DefaultDeviceDto': ...
    def withSortOrder(self, int: int) -> 'DefaultDeviceDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceDto.getSortOrder` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (int): A new value for sortOrder
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withState(self, deviceStateDto: DeviceStateDto) -> 'DefaultDeviceDto': ...
    class Builder:
        def acceleratorZone(self, acceleratorZoneDto: AcceleratorZoneDto) -> 'DefaultDeviceDto.Builder': ...
        def addAllDeviceGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultDeviceDto.Builder': ...
        def addDeviceGroup(self, string: str) -> 'DefaultDeviceDto.Builder': ...
        def addDeviceGroups(self, stringArray: typing.List[str]) -> 'DefaultDeviceDto.Builder': ...
        def build(self) -> 'DefaultDeviceDto': ...
        def cycleBound(self, boolean: bool) -> 'DefaultDeviceDto.Builder': ...
        def description(self, string: str) -> 'DefaultDeviceDto.Builder': ...
        def deviceAlias(self, string: str) -> 'DefaultDeviceDto.Builder': ...
        def deviceGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultDeviceDto.Builder': ...
        def deviceTypeVersion(self, deviceTypeVersionContainerDto: DeviceTypeVersionContainerDto) -> 'DefaultDeviceDto.Builder': ...
        def fecName(self, string: str) -> 'DefaultDeviceDto.Builder': ...
        def id(self, long: int) -> 'DefaultDeviceDto.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultDeviceDto.Builder': ...
        def name(self, string: str) -> 'DefaultDeviceDto.Builder': ...
        def position(self, double: float) -> 'DefaultDeviceDto.Builder': ...
        def serverName(self, string: str) -> 'DefaultDeviceDto.Builder': ...
        def sortOrder(self, int: int) -> 'DefaultDeviceDto.Builder': ...
        def state(self, deviceStateDto: DeviceStateDto) -> 'DefaultDeviceDto.Builder': ...

class DefaultDeviceMetaTypeDto(DeviceMetaTypeDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceMetaTypeDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeDto`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceMetaTypeDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceMetaTypeDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceMetaTypeDto`.
        
            .. code-block: java
            
             DefaultDeviceMetaTypeDto.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultDeviceMetaTypeDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceMetaTypeDto: DeviceMetaTypeDto) -> 'DefaultDeviceMetaTypeDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeDto`): The instance to copy
        
            Returns:
                A copied immutable DeviceMetaTypeDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`DeviceMetaTypeDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultDeviceMetaTypeDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultDeviceMetaTypeDto': ...
        def name(self, string: str) -> 'DefaultDeviceMetaTypeDto.Builder': ...

class DefaultDeviceStateDto(DeviceStateDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceStateDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceStateDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceStateDto`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceStateDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceStateDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceStateDto`.
        
            .. code-block: java
            
             DefaultDeviceStateDto.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultDeviceStateDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceStateDto: DeviceStateDto) -> 'DefaultDeviceStateDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceStateDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceStateDto`): The instance to copy
        
            Returns:
                A copied immutable DeviceStateDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`DeviceStateDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultDeviceStateDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultDeviceStateDto': ...
        def name(self, string: str) -> 'DefaultDeviceStateDto.Builder': ...

class DefaultDeviceTypeImplementationDto(DeviceTypeImplementationDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceTypeImplementationDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationDto`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceTypeImplementationDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeImplementationDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceTypeImplementationDto`.
        
            .. code-block: java
            
             DefaultDeviceTypeImplementationDto.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultDeviceTypeImplementationDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceTypeImplementationDto: DeviceTypeImplementationDto) -> 'DefaultDeviceTypeImplementationDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationDto` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationDto`): The instance to copy
        
            Returns:
                A copied immutable DeviceTypeImplementationDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`DeviceTypeImplementationDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultDeviceTypeImplementationDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultDeviceTypeImplementationDto': ...
        def name(self, string: str) -> 'DefaultDeviceTypeImplementationDto.Builder': ...

class DefaultDeviceTypeVersionContainerDto(DeviceTypeVersionContainerDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceTypeVersionContainerDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceTypeVersionContainerDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionContainerDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceTypeVersionContainerDto`.
        
            .. code-block: java
            
             DefaultDeviceTypeVersionContainerDto.builder()
                .name(String) // required name
                .description(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getDescription`
                .id(Long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getId`
                .metaType(cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getMetaType`
                .addOtherVersion|addAllOtherVersions(cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto) // :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getOtherVersions` elements
                .primaryVersion(cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getPrimaryVersion`
                .build();
             
        
            Returns:
                A new DefaultDeviceTypeVersionContainerDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceTypeVersionContainerDto: DeviceTypeVersionContainerDto) -> 'DefaultDeviceTypeVersionContainerDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto`): The instance to copy
        
            Returns:
                A copied immutable DeviceTypeVersionContainerDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDescription(self) -> str: ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getMetaType(self) -> DeviceMetaTypeDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getMetaType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto`
        
            Returns:
                The value of the :code:`metaType` attribute
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def getOtherVersions(self) -> java.util.List[DeviceTypeVersionDto]: ...
    def getPrimaryVersion(self) -> DeviceTypeVersionDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getPrimaryVersion`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto`
        
            Returns:
                The value of the :code:`primaryVersion` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`, :code:`description`, :code:`id`, :code:`metaType`,
            :code:`otherVersions`, :code:`primaryVersion`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`DeviceTypeVersionContainerDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDescription(self, string: str) -> 'DefaultDeviceTypeVersionContainerDto': ...
    def withId(self, long: int) -> 'DefaultDeviceTypeVersionContainerDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getId` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMetaType(self, deviceMetaTypeDto: DeviceMetaTypeDto) -> 'DefaultDeviceTypeVersionContainerDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getMetaType` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeDto`): A new value for metaType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultDeviceTypeVersionContainerDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withOtherVersions(self, deviceTypeVersionDtoArray: typing.List[DeviceTypeVersionDto]) -> 'DefaultDeviceTypeVersionContainerDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getOtherVersions`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceTypeVersionContainerDto` withOtherVersions (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getOtherVersions`. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto`> elements): An iterable of otherVersions elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withOtherVersions(self, iterable: java.lang.Iterable[DeviceTypeVersionDto]) -> 'DefaultDeviceTypeVersionContainerDto': ...
    def withPrimaryVersion(self, deviceTypeVersionDto: DeviceTypeVersionDto) -> 'DefaultDeviceTypeVersionContainerDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerDto.getPrimaryVersion` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto`): A new value for primaryVersion
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllOtherVersions(self, iterable: java.lang.Iterable[DeviceTypeVersionDto]) -> 'DefaultDeviceTypeVersionContainerDto.Builder': ...
        def addOtherVersion(self, deviceTypeVersionDto: DeviceTypeVersionDto) -> 'DefaultDeviceTypeVersionContainerDto.Builder': ...
        def addOtherVersions(self, deviceTypeVersionDtoArray: typing.List[DeviceTypeVersionDto]) -> 'DefaultDeviceTypeVersionContainerDto.Builder': ...
        def build(self) -> 'DefaultDeviceTypeVersionContainerDto': ...
        def description(self, string: str) -> 'DefaultDeviceTypeVersionContainerDto.Builder': ...
        def id(self, long: int) -> 'DefaultDeviceTypeVersionContainerDto.Builder': ...
        def metaType(self, deviceMetaTypeDto: DeviceMetaTypeDto) -> 'DefaultDeviceTypeVersionContainerDto.Builder': ...
        def name(self, string: str) -> 'DefaultDeviceTypeVersionContainerDto.Builder': ...
        def otherVersions(self, iterable: java.lang.Iterable[DeviceTypeVersionDto]) -> 'DefaultDeviceTypeVersionContainerDto.Builder': ...
        def primaryVersion(self, deviceTypeVersionDto: DeviceTypeVersionDto) -> 'DefaultDeviceTypeVersionContainerDto.Builder': ...

class DefaultDeviceTypeVersionDto(DeviceTypeVersionDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceTypeVersionDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceTypeVersionDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceTypeVersionDto`.
        
            .. code-block: java
            
             DefaultDeviceTypeVersionDto.builder()
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto.getId`
                .implementation(cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto.getImplementation`
                .versionNumber(cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto.getVersionNumber`
                .build();
             
        
            Returns:
                A new DefaultDeviceTypeVersionDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceTypeVersionDto: DeviceTypeVersionDto) -> 'DefaultDeviceTypeVersionDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto`): The instance to copy
        
            Returns:
                A copied immutable DeviceTypeVersionDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getImplementation(self) -> DeviceTypeImplementationDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto.getImplementation`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto`
        
            Returns:
                The value of the :code:`implementation` attribute
        
        
        """
        ...
    def getVersionNumber(self) -> DeviceTypeVersionNumberDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto.getVersionNumber`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto`
        
            Returns:
                The value of the :code:`versionNumber` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`id`, :code:`implementation`, :code:`versionNumber`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`DeviceTypeVersionDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultDeviceTypeVersionDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto.getId` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withImplementation(self, deviceTypeImplementationDto: DeviceTypeImplementationDto) -> 'DefaultDeviceTypeVersionDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto.getImplementation` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationDto`): A new value for implementation
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withVersionNumber(self, deviceTypeVersionNumberDto: DeviceTypeVersionNumberDto) -> 'DefaultDeviceTypeVersionDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionDto.getVersionNumber` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto`): A new value for versionNumber
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultDeviceTypeVersionDto': ...
        def id(self, long: int) -> 'DefaultDeviceTypeVersionDto.Builder': ...
        def implementation(self, deviceTypeImplementationDto: DeviceTypeImplementationDto) -> 'DefaultDeviceTypeVersionDto.Builder': ...
        def versionNumber(self, deviceTypeVersionNumberDto: DeviceTypeVersionNumberDto) -> 'DefaultDeviceTypeVersionDto.Builder': ...

class DefaultDeviceTypeVersionNumberDto(DeviceTypeVersionNumberDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceTypeVersionNumberDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceTypeVersionNumberDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionNumberDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceTypeVersionNumberDto`.
        
            .. code-block: java
            
             DefaultDeviceTypeVersionNumberDto.builder()
                .major(Integer) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto.getMajor`
                .minor(Integer) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto.getMinor`
                .build();
             
        
            Returns:
                A new DefaultDeviceTypeVersionNumberDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceTypeVersionNumberDto: DeviceTypeVersionNumberDto) -> 'DefaultDeviceTypeVersionNumberDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto`): The instance to copy
        
            Returns:
                A copied immutable DeviceTypeVersionNumberDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMajor(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto.getMajor`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto`
        
            Returns:
                The value of the :code:`major` attribute
        
        
        """
        ...
    def getMinor(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto.getMinor`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto`
        
            Returns:
                The value of the :code:`minor` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`major`, :code:`minor`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`DeviceTypeVersionNumberDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withMajor(self, integer: int) -> 'DefaultDeviceTypeVersionNumberDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto.getMajor` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): A new value for major
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMinor(self, integer: int) -> 'DefaultDeviceTypeVersionNumberDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberDto.getMinor` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): A new value for minor
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultDeviceTypeVersionNumberDto': ...
        def major(self, integer: int) -> 'DefaultDeviceTypeVersionNumberDto.Builder': ...
        def minor(self, integer: int) -> 'DefaultDeviceTypeVersionNumberDto.Builder': ...

class DefaultEnumItemDto(EnumItemDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultEnumItemDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto`.
    
        Use the builder to create immutable instances: :code:`DefaultEnumItemDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultEnumItemDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultEnumItemDto`.
        
            .. code-block: java
            
             DefaultEnumItemDto.builder()
                .code(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.getCode`
                .symbol(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.getSymbol`
                .standardMeaning(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.getStandardMeaning`
                .settable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.isSettable`
                .build();
             
        
            Returns:
                A new DefaultEnumItemDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(enumItemDto: EnumItemDto) -> 'DefaultEnumItemDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto` value. Uses accessors to get values
            to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto`): The instance to copy
        
            Returns:
                A copied immutable EnumItemDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getCode(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.getCode`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto`
        
            Returns:
                The value of the :code:`code` attribute
        
        
        """
        ...
    def getStandardMeaning(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.getStandardMeaning`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto`
        
            Returns:
                The value of the :code:`standardMeaning` attribute
        
        
        """
        ...
    def getSymbol(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.getSymbol`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto`
        
            Returns:
                The value of the :code:`symbol` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`code`, :code:`symbol`, :code:`standardMeaning`, :code:`settable`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isSettable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.isSettable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto`
        
            Returns:
                The value of the :code:`settable` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`EnumItemDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withCode(self, long: int) -> 'DefaultEnumItemDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.getCode` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for code
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withSettable(self, boolean: bool) -> 'DefaultEnumItemDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.isSettable` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for settable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withStandardMeaning(self, string: str) -> 'DefaultEnumItemDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.getStandardMeaning` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for standardMeaning
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withSymbol(self, string: str) -> 'DefaultEnumItemDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto.getSymbol` attribute. An equals check used to prevent copying of the
            same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for symbol
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultEnumItemDto': ...
        def code(self, long: int) -> 'DefaultEnumItemDto.Builder': ...
        def settable(self, boolean: bool) -> 'DefaultEnumItemDto.Builder': ...
        def standardMeaning(self, string: str) -> 'DefaultEnumItemDto.Builder': ...
        def symbol(self, string: str) -> 'DefaultEnumItemDto.Builder': ...

class DefaultEnumTypeDto(EnumTypeDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultEnumTypeDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto`.
    
        Use the builder to create immutable instances: :code:`DefaultEnumTypeDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultEnumTypeDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultEnumTypeDto`.
        
            .. code-block: java
            
             DefaultEnumTypeDto.builder()
                .name(String) // required name
                .enumTypeBitSize(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto.getEnumTypeBitSize`
                .addEnumItem|addAllEnumItems(cern.lsa.client.rest.api.v1.dto.EnumItemDto) // :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto.getEnumItems` elements
                .build();
             
        
            Returns:
                A new DefaultEnumTypeDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(enumTypeDto: EnumTypeDto) -> 'DefaultEnumTypeDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto` value. Uses accessors to get values
            to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto`): The instance to copy
        
            Returns:
                A copied immutable EnumTypeDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getEnumItems(self) -> java.util.List[EnumItemDto]: ...
    def getEnumTypeBitSize(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto.getEnumTypeBitSize`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto`
        
            Returns:
                The value of the :code:`enumTypeBitSize` attribute
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`, :code:`enumTypeBitSize`, :code:`enumItems`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`EnumTypeDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withEnumItems(self, enumItemDtoArray: typing.List[EnumItemDto]) -> 'DefaultEnumTypeDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto.getEnumItems`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultEnumTypeDto` withEnumItems (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto.getEnumItems`. A shallow reference equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemDto`> elements): An iterable of enumItems elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withEnumItems(self, iterable: java.lang.Iterable[EnumItemDto]) -> 'DefaultEnumTypeDto': ...
    def withEnumTypeBitSize(self, string: str) -> 'DefaultEnumTypeDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeDto.getEnumTypeBitSize` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for enumTypeBitSize
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultEnumTypeDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllEnumItems(self, iterable: java.lang.Iterable[EnumItemDto]) -> 'DefaultEnumTypeDto.Builder': ...
        def addEnumItem(self, enumItemDto: EnumItemDto) -> 'DefaultEnumTypeDto.Builder': ...
        def addEnumItems(self, enumItemDtoArray: typing.List[EnumItemDto]) -> 'DefaultEnumTypeDto.Builder': ...
        def build(self) -> 'DefaultEnumTypeDto': ...
        def enumItems(self, iterable: java.lang.Iterable[EnumItemDto]) -> 'DefaultEnumTypeDto.Builder': ...
        def enumTypeBitSize(self, string: str) -> 'DefaultEnumTypeDto.Builder': ...
        def name(self, string: str) -> 'DefaultEnumTypeDto.Builder': ...

class DefaultErrorDto(ErrorDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultErrorDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ErrorDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ErrorDto`.
    
        Use the builder to create immutable instances: :code:`DefaultErrorDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultErrorDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultErrorDto`.
        
            .. code-block: java
            
             DefaultErrorDto.builder()
                .errorType(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getErrorType`
                .message(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getMessage`
                .path(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getPath`
                .timestamp(java.time.OffsetDateTime) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getTimestamp`
                .build();
             
        
            Returns:
                A new DefaultErrorDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(errorDto: ErrorDto) -> 'DefaultErrorDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ErrorDto` value. Uses accessors to get values to
            initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ErrorDto`): The instance to copy
        
            Returns:
                A copied immutable ErrorDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getErrorType(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getErrorType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ErrorDto`
        
            Returns:
                The value of the :code:`errorType` attribute
        
        
        """
        ...
    def getMessage(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getMessage`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ErrorDto`
        
            Returns:
                The value of the :code:`message` attribute
        
        
        """
        ...
    def getPath(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getPath`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ErrorDto`
        
            Returns:
                The value of the :code:`path` attribute
        
        
        """
        ...
    def getTimestamp(self) -> java.time.OffsetDateTime:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getTimestamp`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ErrorDto`
        
            Returns:
                The value of the :code:`timestamp` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`errorType`, :code:`message`, :code:`path`, :code:`timestamp`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ErrorDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withErrorType(self, string: str) -> 'DefaultErrorDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getErrorType` attribute. An equals check used to prevent copying of the
            same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for errorType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMessage(self, string: str) -> 'DefaultErrorDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getMessage` attribute. An equals check used to prevent copying of the
            same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for message
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPath(self, string: str) -> 'DefaultErrorDto':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getPath`
            attribute. An equals check used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for path
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTimestamp(self, offsetDateTime: java.time.OffsetDateTime) -> 'DefaultErrorDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ErrorDto.getTimestamp` attribute. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`OffsetDateTime <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/OffsetDateTime.html?is-external=true>`): A new value for timestamp
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultErrorDto': ...
        def errorType(self, string: str) -> 'DefaultErrorDto.Builder': ...
        def message(self, string: str) -> 'DefaultErrorDto.Builder': ...
        def path(self, string: str) -> 'DefaultErrorDto.Builder': ...
        def timestamp(self, offsetDateTime: java.time.OffsetDateTime) -> 'DefaultErrorDto.Builder': ...

class DefaultIncaPropertyFieldInfoDto(IncaPropertyFieldInfoDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultIncaPropertyFieldInfoDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto`.
    
        Use the builder to create immutable instances: :code:`DefaultIncaPropertyFieldInfoDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfoDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultIncaPropertyFieldInfoDto`.
        
            .. code-block: java
            
             DefaultIncaPropertyFieldInfoDto.builder()
                .propertyFieldRest(cern.lsa.client.rest.api.v1.dto.PropertyFieldDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.getPropertyFieldRest`
                .displayName(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.getDisplayName`
                .mainStatus(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.isMainStatus`
                .associatedPropertyFieldRest(cern.lsa.client.rest.api.v1.dto.PropertyFieldDto | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.getAssociatedPropertyFieldRest`
                .controlWarningMessage(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.getControlWarningMessage`
                .parameterValueCompareType(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.getParameterValueCompareType`
                .displayFormat(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.getDisplayFormat`
                .build();
             
        
            Returns:
                A new DefaultIncaPropertyFieldInfoDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(incaPropertyFieldInfoDto: IncaPropertyFieldInfoDto) -> 'DefaultIncaPropertyFieldInfoDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto`): The instance to copy
        
            Returns:
                A copied immutable IncaPropertyFieldInfoDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAssociatedPropertyFieldRest(self) -> PropertyFieldDto: ...
    def getControlWarningMessage(self) -> str: ...
    def getDisplayFormat(self) -> str: ...
    def getDisplayName(self) -> str: ...
    def getParameterValueCompareType(self) -> str:
        """
            Returns the comparison type that should be applied for this parameter type when calculating value status.
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.getParameterValueCompareType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto`
        
            Returns:
                type of parameter value comparison
        
        
        """
        ...
    def getPropertyFieldRest(self) -> PropertyFieldDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.getPropertyFieldRest`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto`
        
            Returns:
                property-field this info is attached to
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`propertyFieldRest`, :code:`displayName`, :code:`mainStatus`,
            :code:`associatedPropertyFieldRest`, :code:`controlWarningMessage`, :code:`parameterValueCompareType`,
            :code:`displayFormat`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isMainStatus(self) -> bool:
        """
            Indicates if this parameter type represents the main status property for given device type. The main status property
            typically indicates if the device is enabled, disabled or in a faulty state. It's value type is either an enumeration or
            boolean. Note that for a given device type, only a single parameter type can represent the main status.
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.isMainStatus`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto`
        
            Returns:
                :code:`true` if this parameter type represents the main status property field
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`IncaPropertyFieldInfoDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAssociatedPropertyFieldRest(self, propertyFieldDto: PropertyFieldDto) -> 'DefaultIncaPropertyFieldInfoDto': ...
    def withControlWarningMessage(self, string: str) -> 'DefaultIncaPropertyFieldInfoDto': ...
    def withDisplayFormat(self, string: str) -> 'DefaultIncaPropertyFieldInfoDto': ...
    def withDisplayName(self, string: str) -> 'DefaultIncaPropertyFieldInfoDto': ...
    def withMainStatus(self, boolean: bool) -> 'DefaultIncaPropertyFieldInfoDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.isMainStatus` attribute. A value equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for mainStatus
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParameterValueCompareType(self, string: str) -> 'DefaultIncaPropertyFieldInfoDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.getParameterValueCompareType` attribute. An equals
            check used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for parameterValueCompareType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyFieldRest(self, propertyFieldDto: PropertyFieldDto) -> 'DefaultIncaPropertyFieldInfoDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto.getPropertyFieldRest` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto`): A new value for propertyFieldRest
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def associatedPropertyFieldRest(self, propertyFieldDto: PropertyFieldDto) -> 'DefaultIncaPropertyFieldInfoDto.Builder': ...
        def build(self) -> 'DefaultIncaPropertyFieldInfoDto': ...
        def controlWarningMessage(self, string: str) -> 'DefaultIncaPropertyFieldInfoDto.Builder': ...
        def displayFormat(self, string: str) -> 'DefaultIncaPropertyFieldInfoDto.Builder': ...
        def displayName(self, string: str) -> 'DefaultIncaPropertyFieldInfoDto.Builder': ...
        def mainStatus(self, boolean: bool) -> 'DefaultIncaPropertyFieldInfoDto.Builder': ...
        def parameterValueCompareType(self, string: str) -> 'DefaultIncaPropertyFieldInfoDto.Builder': ...
        def propertyFieldRest(self, propertyFieldDto: PropertyFieldDto) -> 'DefaultIncaPropertyFieldInfoDto.Builder': ...

class DefaultIncaPropertyFieldInfosRequestDto(IncaPropertyFieldInfosRequestDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultIncaPropertyFieldInfosRequestDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestDto`.
    
        Use the builder to create immutable instances: :code:`DefaultIncaPropertyFieldInfosRequestDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfosRequestDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultIncaPropertyFieldInfosRequestDto`.
        
            .. code-block: java
            
             DefaultIncaPropertyFieldInfosRequestDto.builder()
                .addPropertyFieldId|addAllPropertyFieldIds(long) // :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestDto.getPropertyFieldIds` elements
                .build();
             
        
            Returns:
                A new DefaultIncaPropertyFieldInfosRequestDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(incaPropertyFieldInfosRequestDto: IncaPropertyFieldInfosRequestDto) -> 'DefaultIncaPropertyFieldInfosRequestDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestDto` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestDto`): The instance to copy
        
            Returns:
                A copied immutable IncaPropertyFieldInfosRequestDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getPropertyFieldIds(self) -> java.util.Set[int]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`propertyFieldIds`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`IncaPropertyFieldInfosRequestDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withPropertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultIncaPropertyFieldInfosRequestDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestDto.getPropertyFieldIds`.
        
            Parameters:
                elements (long...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultIncaPropertyFieldInfosRequestDto` withPropertyFieldIds (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestDto.getPropertyFieldIds`. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements): An iterable of propertyFieldIds elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withPropertyFieldIds(self, longArray: typing.List[int]) -> 'DefaultIncaPropertyFieldInfosRequestDto': ...
    class Builder:
        def addAllPropertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultIncaPropertyFieldInfosRequestDto.Builder': ...
        def addPropertyFieldId(self, long: int) -> 'DefaultIncaPropertyFieldInfosRequestDto.Builder': ...
        def addPropertyFieldIds(self, longArray: typing.List[int]) -> 'DefaultIncaPropertyFieldInfosRequestDto.Builder': ...
        def build(self) -> 'DefaultIncaPropertyFieldInfosRequestDto': ...
        def propertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultIncaPropertyFieldInfosRequestDto.Builder': ...

class DefaultMakeRuleClassInfoDto(MakeRuleClassInfoDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleClassInfoDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleClassInfoDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleClassInfoDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultMakeRuleClassInfoDto`.
        
            .. code-block: java
            
             DefaultMakeRuleClassInfoDto.builder()
                .className(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto.getClassName`
                .productName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto.getProductName`
                .version(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto.getVersion`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleClassInfoDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleClassInfoDto: MakeRuleClassInfoDto) -> 'DefaultMakeRuleClassInfoDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleClassInfoDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getClassName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto.getClassName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto`
        
            Returns:
                The value of the :code:`className` attribute
        
        
        """
        ...
    def getProductName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto.getProductName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto`
        
            Returns:
                The value of the :code:`productName` attribute
        
        
        """
        ...
    def getVersion(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto.getVersion`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto`
        
            Returns:
                The value of the :code:`version` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`className`, :code:`productName`, :code:`version`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`MakeRuleClassInfoDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withClassName(self, string: str) -> 'DefaultMakeRuleClassInfoDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto.getClassName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for className
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withProductName(self, string: str) -> 'DefaultMakeRuleClassInfoDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto.getProductName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for productName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withVersion(self, string: str) -> 'DefaultMakeRuleClassInfoDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto.getVersion` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for version
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleClassInfoDto': ...
        def className(self, string: str) -> 'DefaultMakeRuleClassInfoDto.Builder': ...
        def productName(self, string: str) -> 'DefaultMakeRuleClassInfoDto.Builder': ...
        def version(self, string: str) -> 'DefaultMakeRuleClassInfoDto.Builder': ...

class DefaultMakeRuleConfigInfoDto(MakeRuleConfigInfoDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleConfigInfoDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoDto`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleConfigInfoDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigInfoDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultMakeRuleConfigInfoDto`.
        
            .. code-block: java
            
             DefaultMakeRuleConfigInfoDto.builder()
                .makeRuleConfigStatus(cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoDto.getMakeRuleConfigStatus`
                .makeRuleInfo(cern.lsa.client.rest.api.v1.dto.MakeRuleInfoDto | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoDto.getMakeRuleInfo`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleConfigInfoDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleConfigInfoDto: MakeRuleConfigInfoDto) -> 'DefaultMakeRuleConfigInfoDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoDto`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleConfigInfoDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMakeRuleConfigStatus(self) -> MakeRuleConfigStatusDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoDto.getMakeRuleConfigStatus`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoDto`
        
            Returns:
                The value of the :code:`makeRuleConfigStatus` attribute
        
        
        """
        ...
    def getMakeRuleInfo(self) -> MakeRuleInfoDto: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`makeRuleConfigStatus`, :code:`makeRuleInfo`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`MakeRuleConfigInfoDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withMakeRuleConfigStatus(self, makeRuleConfigStatusDto: MakeRuleConfigStatusDto) -> 'DefaultMakeRuleConfigInfoDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoDto.getMakeRuleConfigStatus` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusDto`): A new value for makeRuleConfigStatus
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMakeRuleInfo(self, makeRuleInfoDto: MakeRuleInfoDto) -> 'DefaultMakeRuleConfigInfoDto': ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleConfigInfoDto': ...
        def makeRuleConfigStatus(self, makeRuleConfigStatusDto: MakeRuleConfigStatusDto) -> 'DefaultMakeRuleConfigInfoDto.Builder': ...
        def makeRuleInfo(self, makeRuleInfoDto: MakeRuleInfoDto) -> 'DefaultMakeRuleConfigInfoDto.Builder': ...

class DefaultMakeRuleConfigStatusDto(MakeRuleConfigStatusDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleConfigStatusDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusDto`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleConfigStatusDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigStatusDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultMakeRuleConfigStatusDto`.
        
            .. code-block: java
            
             DefaultMakeRuleConfigStatusDto.builder()
                .name(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusDto.getName`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleConfigStatusDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleConfigStatusDto: MakeRuleConfigStatusDto) -> 'DefaultMakeRuleConfigStatusDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusDto` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusDto`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleConfigStatusDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusDto.getName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusDto`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`MakeRuleConfigStatusDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultMakeRuleConfigStatusDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusDto.getName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleConfigStatusDto': ...
        def name(self, string: str) -> 'DefaultMakeRuleConfigStatusDto.Builder': ...

class DefaultMakeRuleInfoDto(MakeRuleInfoDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleInfoDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoDto`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleInfoDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleInfoDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultMakeRuleInfoDto`.
        
            .. code-block: java
            
             DefaultMakeRuleInfoDto.builder()
                .makeRuleClassInfo(cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoDto | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoDto.getMakeRuleClassInfo`
                .makeRuleName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoDto.getMakeRuleName`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleInfoDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleInfoDto: MakeRuleInfoDto) -> 'DefaultMakeRuleInfoDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoDto`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleInfoDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMakeRuleClassInfo(self) -> MakeRuleClassInfoDto: ...
    def getMakeRuleName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoDto.getMakeRuleName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoDto`
        
            Returns:
                The value of the :code:`makeRuleName` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`makeRuleClassInfo`, :code:`makeRuleName`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`MakeRuleInfoDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withMakeRuleClassInfo(self, makeRuleClassInfoDto: MakeRuleClassInfoDto) -> 'DefaultMakeRuleInfoDto': ...
    def withMakeRuleName(self, string: str) -> 'DefaultMakeRuleInfoDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoDto.getMakeRuleName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for makeRuleName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleInfoDto': ...
        def makeRuleClassInfo(self, makeRuleClassInfoDto: MakeRuleClassInfoDto) -> 'DefaultMakeRuleInfoDto.Builder': ...
        def makeRuleName(self, string: str) -> 'DefaultMakeRuleInfoDto.Builder': ...

class DefaultParameterAttributesDto(ParameterAttributesDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterAttributesDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterAttributesDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterAttributesDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterAttributesDto`.
        
            .. code-block: java
            
             DefaultParameterAttributesDto.builder()
                .absoluteTolerance(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getAbsoluteTolerance`
                .belongsToFunctionBProc(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.isBelongsToFunctionBProc`
                .defaultHierarchy(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getDefaultHierarchy`
                .device(cern.lsa.client.rest.api.v1.dto.DeviceDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getDevice`
                .propertyField(cern.lsa.client.rest.api.v1.dto.PropertyFieldDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getPropertyField`
                .maxValue(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getMaxValue`
                .minValue(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getMinValue`
                .parameterId(Long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getParameterId`
                .parameterName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getParameterName`
                .parameterType(cern.lsa.client.rest.api.v1.dto.ParameterTypeDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getParameterType`
                .relativeTolerance(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getRelativeTolerance`
                .reservedForOpExperts(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.isReservedForOpExperts`
                .trimable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.isTrimable`
                .xPrecision(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getXPrecision`
                .yPrecision(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getYPrecision`
                .build();
             
        
            Returns:
                A new DefaultParameterAttributesDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterAttributesDto: ParameterAttributesDto) -> 'DefaultParameterAttributesDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`): The instance to copy
        
            Returns:
                A copied immutable ParameterAttributesDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAbsoluteTolerance(self) -> float: ...
    def getDefaultHierarchy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getDefaultHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`
        
            Returns:
                The value of the :code:`defaultHierarchy` attribute
        
        
        """
        ...
    def getDevice(self) -> DeviceDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getDevice`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`
        
            Returns:
                The value of the :code:`device` attribute
        
        
        """
        ...
    def getMaxValue(self) -> float: ...
    def getMinValue(self) -> float: ...
    def getParameterId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getParameterId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`
        
            Returns:
                The value of the :code:`parameterId` attribute
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getParameterName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`
        
            Returns:
                The value of the :code:`parameterName` attribute
        
        
        """
        ...
    def getParameterType(self) -> ParameterTypeDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getParameterType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`
        
            Returns:
                The value of the :code:`parameterType` attribute
        
        
        """
        ...
    def getPropertyField(self) -> PropertyFieldDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getPropertyField`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`
        
            Returns:
                The value of the :code:`propertyField` attribute
        
        
        """
        ...
    def getRelativeTolerance(self) -> float: ...
    def getXPrecision(self) -> int: ...
    def getYPrecision(self) -> int: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`absoluteTolerance`, :code:`belongsToFunctionBProc`,
            :code:`defaultHierarchy`, :code:`device`, :code:`propertyField`, :code:`maxValue`, :code:`minValue`,
            :code:`parameterId`, :code:`parameterName`, :code:`parameterType`, :code:`relativeTolerance`,
            :code:`reservedForOpExperts`, :code:`trimable`, :code:`xPrecision`, :code:`yPrecision`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isBelongsToFunctionBProc(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.isBelongsToFunctionBProc`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`
        
            Returns:
                The value of the :code:`belongsToFunctionBProc` attribute
        
        
        """
        ...
    def isReservedForOpExperts(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.isReservedForOpExperts`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`
        
            Returns:
                The value of the :code:`reservedForOpExperts` attribute
        
        
        """
        ...
    def isTrimable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.isTrimable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto`
        
            Returns:
                The value of the :code:`trimable` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterAttributesDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAbsoluteTolerance(self, double: float) -> 'DefaultParameterAttributesDto': ...
    def withBelongsToFunctionBProc(self, boolean: bool) -> 'DefaultParameterAttributesDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.isBelongsToFunctionBProc` attribute. A value equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for belongsToFunctionBProc
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDefaultHierarchy(self, string: str) -> 'DefaultParameterAttributesDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getDefaultHierarchy` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for defaultHierarchy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDevice(self, deviceDto: DeviceDto) -> 'DefaultParameterAttributesDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getDevice` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`): A new value for device
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMaxValue(self, double: float) -> 'DefaultParameterAttributesDto': ...
    def withMinValue(self, double: float) -> 'DefaultParameterAttributesDto': ...
    def withParameterId(self, long: int) -> 'DefaultParameterAttributesDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getParameterId` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`): A new value for parameterId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParameterName(self, string: str) -> 'DefaultParameterAttributesDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getParameterName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for parameterName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParameterType(self, parameterTypeDto: ParameterTypeDto) -> 'DefaultParameterAttributesDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getParameterType` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto`): A new value for parameterType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyField(self, propertyFieldDto: PropertyFieldDto) -> 'DefaultParameterAttributesDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.getPropertyField` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto`): A new value for propertyField
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withRelativeTolerance(self, double: float) -> 'DefaultParameterAttributesDto': ...
    def withReservedForOpExperts(self, boolean: bool) -> 'DefaultParameterAttributesDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.isReservedForOpExperts` attribute. A value equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for reservedForOpExperts
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTrimable(self, boolean: bool) -> 'DefaultParameterAttributesDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto.isTrimable` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for trimable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withXPrecision(self, integer: int) -> 'DefaultParameterAttributesDto': ...
    def withYPrecision(self, integer: int) -> 'DefaultParameterAttributesDto': ...
    class Builder:
        def absoluteTolerance(self, double: float) -> 'DefaultParameterAttributesDto.Builder': ...
        def belongsToFunctionBProc(self, boolean: bool) -> 'DefaultParameterAttributesDto.Builder': ...
        def build(self) -> 'DefaultParameterAttributesDto': ...
        def defaultHierarchy(self, string: str) -> 'DefaultParameterAttributesDto.Builder': ...
        def device(self, deviceDto: DeviceDto) -> 'DefaultParameterAttributesDto.Builder': ...
        def maxValue(self, double: float) -> 'DefaultParameterAttributesDto.Builder': ...
        def minValue(self, double: float) -> 'DefaultParameterAttributesDto.Builder': ...
        def parameterId(self, long: int) -> 'DefaultParameterAttributesDto.Builder': ...
        def parameterName(self, string: str) -> 'DefaultParameterAttributesDto.Builder': ...
        def parameterType(self, parameterTypeDto: ParameterTypeDto) -> 'DefaultParameterAttributesDto.Builder': ...
        def propertyField(self, propertyFieldDto: PropertyFieldDto) -> 'DefaultParameterAttributesDto.Builder': ...
        def relativeTolerance(self, double: float) -> 'DefaultParameterAttributesDto.Builder': ...
        def reservedForOpExperts(self, boolean: bool) -> 'DefaultParameterAttributesDto.Builder': ...
        def trimable(self, boolean: bool) -> 'DefaultParameterAttributesDto.Builder': ...
        def xPrecision(self, integer: int) -> 'DefaultParameterAttributesDto.Builder': ...
        def yPrecision(self, integer: int) -> 'DefaultParameterAttributesDto.Builder': ...

class DefaultParameterDto(ParameterDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterDto.builder()`.
    """
    def belongsToFunctionBeamProcess(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.belongsToFunctionBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`belongsToFunctionBeamProcess` attribute
        
        
        """
        ...
    @staticmethod
    def builder() -> 'DefaultParameterDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterDto`.
        
            .. code-block: java
            
             DefaultParameterDto.builder()
                .name(String) // required name
                .belongsToFunctionBeamProcess(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.belongsToFunctionBeamProcess`
                .critical(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isCritical`
                .defaultHierarchy(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getDefaultHierarchy`
                .device(cern.lsa.client.rest.api.v1.dto.DeviceDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getDevice`
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getId`
                .monitorable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isMonitorable`
                .multiplexed(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isMultiplexed`
                .cycleBound(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isCycleBound`
                .addParameterGroup|addAllParameterGroups(String) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getParameterGroups` elements
                .parameterType(cern.lsa.client.rest.api.v1.dto.ParameterTypeDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getParameterType`
                .propertySupportingPartialSet(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isPropertySupportingPartialSet`
                .readable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isReadable`
                .reservedForOpExperts(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isReservedForOpExperts`
                .trimable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isTrimable`
                .valueDescriptor(cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getValueDescriptor`
                .valueType(cern.lsa.client.rest.api.v1.dto.TypeDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getValueType`
                .lsaImplementation(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isLsaImplementation`
                .writable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isWritable`
                .propertyField(cern.lsa.client.rest.api.v1.dto.PropertyFieldDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getPropertyField`
                .build();
             
        
            Returns:
                A new DefaultParameterDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterDto: ParameterDto) -> 'DefaultParameterDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`): The instance to copy
        
            Returns:
                A copied immutable ParameterDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDefaultHierarchy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getDefaultHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`defaultHierarchy` attribute
        
        
        """
        ...
    def getDevice(self) -> DeviceDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getDevice`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`device` attribute
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def getParameterGroups(self) -> java.util.List[str]: ...
    def getParameterType(self) -> ParameterTypeDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getParameterType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`parameterType` attribute
        
        
        """
        ...
    def getPropertyField(self) -> PropertyFieldDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getPropertyField`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`propertyField` attribute
        
        
        """
        ...
    def getValueDescriptor(self) -> ValueDescriptorDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getValueDescriptor`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`valueDescriptor` attribute
        
        
        """
        ...
    def getValueType(self) -> TypeDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getValueType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`valueType` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`, :code:`belongsToFunctionBeamProcess`, :code:`critical`,
            :code:`defaultHierarchy`, :code:`device`, :code:`id`, :code:`monitorable`, :code:`multiplexed`, :code:`cycleBound`,
            :code:`parameterGroups`, :code:`parameterType`, :code:`propertySupportingPartialSet`, :code:`readable`,
            :code:`reservedForOpExperts`, :code:`trimable`, :code:`valueDescriptor`, :code:`valueType`, :code:`lsaImplementation`,
            :code:`writable`, :code:`propertyField`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isCritical(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isCritical`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`critical` attribute
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isCycleBound`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`cycleBound` attribute
        
        
        """
        ...
    def isLsaImplementation(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isLsaImplementation`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`lsaImplementation` attribute
        
        
        """
        ...
    def isMonitorable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isMonitorable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`monitorable` attribute
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isMultiplexed`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`multiplexed` attribute
        
        
        """
        ...
    def isPropertySupportingPartialSet(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isPropertySupportingPartialSet`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`propertySupportingPartialSet` attribute
        
        
        """
        ...
    def isReadable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isReadable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`readable` attribute
        
        
        """
        ...
    def isReservedForOpExperts(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isReservedForOpExperts`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`reservedForOpExperts` attribute
        
        
        """
        ...
    def isTrimable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isTrimable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`trimable` attribute
        
        
        """
        ...
    def isWritable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isWritable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`
        
            Returns:
                The value of the :code:`writable` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withBelongsToFunctionBeamProcess(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.belongsToFunctionBeamProcess` attribute. A value equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for belongsToFunctionBeamProcess
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withCritical(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isCritical` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for critical
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withCycleBound(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isCycleBound` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for cycleBound
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDefaultHierarchy(self, string: str) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getDefaultHierarchy` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for defaultHierarchy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDevice(self, deviceDto: DeviceDto) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getDevice` attribute. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceDto`): A new value for device
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getId`
            attribute. A value equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withLsaImplementation(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isLsaImplementation` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for lsaImplementation
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMonitorable(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isMonitorable` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for monitorable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isMultiplexed` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for multiplexed
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterDto': ...
    @typing.overload
    def withParameterGroups(self, stringArray: typing.List[str]) -> 'DefaultParameterDto': ...
    def withParameterType(self, parameterTypeDto: ParameterTypeDto) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getParameterType` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto`): A new value for parameterType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyField(self, propertyFieldDto: PropertyFieldDto) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getPropertyField` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto`): A new value for propertyField
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertySupportingPartialSet(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isPropertySupportingPartialSet` attribute. A value equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for propertySupportingPartialSet
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withReadable(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isReadable` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for readable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withReservedForOpExperts(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isReservedForOpExperts` attribute. A value equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for reservedForOpExperts
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTrimable(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isTrimable` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for trimable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withValueDescriptor(self, valueDescriptorDto: ValueDescriptorDto) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getValueDescriptor` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto`): A new value for valueDescriptor
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withValueType(self, typeDto: TypeDto) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.getValueType` attribute. A shallow reference equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.TypeDto`): A new value for valueType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withWritable(self, boolean: bool) -> 'DefaultParameterDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterDto.isWritable` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for writable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllParameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterDto.Builder': ...
        def addParameterGroup(self, string: str) -> 'DefaultParameterDto.Builder': ...
        def addParameterGroups(self, stringArray: typing.List[str]) -> 'DefaultParameterDto.Builder': ...
        def belongsToFunctionBeamProcess(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...
        def build(self) -> 'DefaultParameterDto': ...
        def critical(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...
        def cycleBound(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...
        def defaultHierarchy(self, string: str) -> 'DefaultParameterDto.Builder': ...
        def device(self, deviceDto: DeviceDto) -> 'DefaultParameterDto.Builder': ...
        def id(self, long: int) -> 'DefaultParameterDto.Builder': ...
        def lsaImplementation(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...
        def monitorable(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...
        def name(self, string: str) -> 'DefaultParameterDto.Builder': ...
        def parameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterDto.Builder': ...
        def parameterType(self, parameterTypeDto: ParameterTypeDto) -> 'DefaultParameterDto.Builder': ...
        def propertyField(self, propertyFieldDto: PropertyFieldDto) -> 'DefaultParameterDto.Builder': ...
        def propertySupportingPartialSet(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...
        def readable(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...
        def reservedForOpExperts(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...
        def trimable(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...
        def valueDescriptor(self, valueDescriptorDto: ValueDescriptorDto) -> 'DefaultParameterDto.Builder': ...
        def valueType(self, typeDto: TypeDto) -> 'DefaultParameterDto.Builder': ...
        def writable(self, boolean: bool) -> 'DefaultParameterDto.Builder': ...

class DefaultParameterGroupDto(ParameterGroupDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterGroupDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterGroupDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterGroupDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterGroupDto`.
        
            .. code-block: java
            
             DefaultParameterGroupDto.builder()
                .name(String) // required name
                .acceleratorName(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto.getAcceleratorName`
                .createDate(java.time.OffsetDateTime) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto.getCreateDate`
                .creator(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto.getCreator`
                .description(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto.getDescription`
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto.getId`
                .build();
             
        
            Returns:
                A new DefaultParameterGroupDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterGroupDto: ParameterGroupDto) -> 'DefaultParameterGroupDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto`): The instance to copy
        
            Returns:
                A copied immutable ParameterGroupDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAcceleratorName(self) -> str: ...
    def getCreateDate(self) -> java.time.OffsetDateTime:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto.getCreateDate`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto`
        
            Returns:
                The value of the :code:`createDate` attribute
        
        
        """
        ...
    def getCreator(self) -> str: ...
    def getDescription(self) -> str: ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`, :code:`acceleratorName`, :code:`createDate`, :code:`creator`,
            :code:`description`, :code:`id`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterGroupDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAcceleratorName(self, string: str) -> 'DefaultParameterGroupDto': ...
    def withCreateDate(self, offsetDateTime: java.time.OffsetDateTime) -> 'DefaultParameterGroupDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto.getCreateDate` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`OffsetDateTime <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/OffsetDateTime.html?is-external=true>`): A new value for createDate
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withCreator(self, string: str) -> 'DefaultParameterGroupDto': ...
    def withDescription(self, string: str) -> 'DefaultParameterGroupDto': ...
    def withId(self, long: int) -> 'DefaultParameterGroupDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupDto.getId` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultParameterGroupDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def acceleratorName(self, string: str) -> 'DefaultParameterGroupDto.Builder': ...
        def build(self) -> 'DefaultParameterGroupDto': ...
        def createDate(self, offsetDateTime: java.time.OffsetDateTime) -> 'DefaultParameterGroupDto.Builder': ...
        def creator(self, string: str) -> 'DefaultParameterGroupDto.Builder': ...
        def description(self, string: str) -> 'DefaultParameterGroupDto.Builder': ...
        def id(self, long: int) -> 'DefaultParameterGroupDto.Builder': ...
        def name(self, string: str) -> 'DefaultParameterGroupDto.Builder': ...

class DefaultParameterTreeDataDto(ParameterTreeDataDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTreeDataDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTreeDataDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeDataDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeDataDto`.
        
            .. code-block: java
            
             DefaultParameterTreeDataDto.builder()
                .addNode|addAllNodes(cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto.getNodes` elements
                .addRelation|addAllRelations(cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto.getRelations` elements
                .addStartNodeId|addAllStartNodeIds(long) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto.getStartNodeIds` elements
                .build();
             
        
            Returns:
                A new DefaultParameterTreeDataDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTreeDataDto: ParameterTreeDataDto) -> 'DefaultParameterTreeDataDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto`): The instance to copy
        
            Returns:
                A copied immutable ParameterTreeDataDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getNodes(self) -> java.util.Set[ParameterTreeNodeDto]: ...
    def getRelations(self) -> java.util.Set[ParameterTreeRelationDto]: ...
    def getStartNodeIds(self) -> java.util.Set[int]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`nodes`, :code:`relations`, :code:`startNodeIds`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTreeDataDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withNodes(self, parameterTreeNodeDtoArray: typing.List[ParameterTreeNodeDto]) -> 'DefaultParameterTreeDataDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto.getNodes`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeDataDto` withNodes (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto.getNodes`. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto`> elements): An iterable of nodes elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withNodes(self, iterable: java.lang.Iterable[ParameterTreeNodeDto]) -> 'DefaultParameterTreeDataDto': ...
    @typing.overload
    def withRelations(self, parameterTreeRelationDtoArray: typing.List[ParameterTreeRelationDto]) -> 'DefaultParameterTreeDataDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto.getRelations`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeDataDto` withRelations (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto.getRelations`. A shallow reference equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto`> elements): An iterable of relations elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withRelations(self, iterable: java.lang.Iterable[ParameterTreeRelationDto]) -> 'DefaultParameterTreeDataDto': ...
    @typing.overload
    def withStartNodeIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParameterTreeDataDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto.getStartNodeIds`.
        
            Parameters:
                elements (long...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeDataDto` withStartNodeIds (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto.getStartNodeIds`. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements): An iterable of startNodeIds elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withStartNodeIds(self, longArray: typing.List[int]) -> 'DefaultParameterTreeDataDto': ...
    class Builder:
        def addAllNodes(self, iterable: java.lang.Iterable[ParameterTreeNodeDto]) -> 'DefaultParameterTreeDataDto.Builder': ...
        def addAllRelations(self, iterable: java.lang.Iterable[ParameterTreeRelationDto]) -> 'DefaultParameterTreeDataDto.Builder': ...
        def addAllStartNodeIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParameterTreeDataDto.Builder': ...
        def addNode(self, parameterTreeNodeDto: ParameterTreeNodeDto) -> 'DefaultParameterTreeDataDto.Builder': ...
        def addNodes(self, parameterTreeNodeDtoArray: typing.List[ParameterTreeNodeDto]) -> 'DefaultParameterTreeDataDto.Builder': ...
        def addRelation(self, parameterTreeRelationDto: ParameterTreeRelationDto) -> 'DefaultParameterTreeDataDto.Builder': ...
        def addRelations(self, parameterTreeRelationDtoArray: typing.List[ParameterTreeRelationDto]) -> 'DefaultParameterTreeDataDto.Builder': ...
        def addStartNodeId(self, long: int) -> 'DefaultParameterTreeDataDto.Builder': ...
        def addStartNodeIds(self, longArray: typing.List[int]) -> 'DefaultParameterTreeDataDto.Builder': ...
        def build(self) -> 'DefaultParameterTreeDataDto': ...
        def nodes(self, iterable: java.lang.Iterable[ParameterTreeNodeDto]) -> 'DefaultParameterTreeDataDto.Builder': ...
        def relations(self, iterable: java.lang.Iterable[ParameterTreeRelationDto]) -> 'DefaultParameterTreeDataDto.Builder': ...
        def startNodeIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParameterTreeDataDto.Builder': ...

class DefaultParameterTreeNodeDto(ParameterTreeNodeDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTreeNodeDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTreeNodeDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeNodeDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeNodeDto`.
        
            .. code-block: java
            
             DefaultParameterTreeNodeDto.builder()
                .parameter(cern.lsa.client.rest.api.v1.dto.ParameterDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto.getParameter`
                .source(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto.isSource`
                .build();
             
        
            Returns:
                A new DefaultParameterTreeNodeDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTreeNodeDto: ParameterTreeNodeDto) -> 'DefaultParameterTreeNodeDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto`): The instance to copy
        
            Returns:
                A copied immutable ParameterTreeNodeDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getParameter(self) -> ParameterDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto.getParameter`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto`
        
            Returns:
                The value of the :code:`parameter` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`parameter`, :code:`source`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isSource(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto.isSource`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto`
        
            Returns:
                The value of the :code:`source` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTreeNodeDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withParameter(self, parameterDto: ParameterDto) -> 'DefaultParameterTreeNodeDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto.getParameter` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`): A new value for parameter
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withSource(self, boolean: bool) -> 'DefaultParameterTreeNodeDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeDto.isSource` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for source
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultParameterTreeNodeDto': ...
        def parameter(self, parameterDto: ParameterDto) -> 'DefaultParameterTreeNodeDto.Builder': ...
        def source(self, boolean: bool) -> 'DefaultParameterTreeNodeDto.Builder': ...

class DefaultParameterTreeRelationDto(ParameterTreeRelationDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTreeRelationDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTreeRelationDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeRelationDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeRelationDto`.
        
            .. code-block: java
            
             DefaultParameterTreeRelationDto.builder()
                .parentParameterId(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto.getParentParameterId`
                .childParameterId(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto.getChildParameterId`
                .build();
             
        
            Returns:
                A new DefaultParameterTreeRelationDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTreeRelationDto: ParameterTreeRelationDto) -> 'DefaultParameterTreeRelationDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto`): The instance to copy
        
            Returns:
                A copied immutable ParameterTreeRelationDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getChildParameterId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto.getChildParameterId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto`
        
            Returns:
                The value of the :code:`childParameterId` attribute
        
        
        """
        ...
    def getParentParameterId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto.getParentParameterId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto`
        
            Returns:
                The value of the :code:`parentParameterId` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`parentParameterId`, :code:`childParameterId`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTreeRelationDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withChildParameterId(self, long: int) -> 'DefaultParameterTreeRelationDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto.getChildParameterId` attribute. A value equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for childParameterId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParentParameterId(self, long: int) -> 'DefaultParameterTreeRelationDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationDto.getParentParameterId` attribute. A value equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for parentParameterId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultParameterTreeRelationDto': ...
        def childParameterId(self, long: int) -> 'DefaultParameterTreeRelationDto.Builder': ...
        def parentParameterId(self, long: int) -> 'DefaultParameterTreeRelationDto.Builder': ...

class DefaultParameterTreesRequestDto(ParameterTreesRequestDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTreesRequestDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTreesRequestDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreesRequestDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreesRequestDto`.
        
            .. code-block: java
            
             DefaultParameterTreesRequestDto.builder()
                .addParameterName|addAllParameterNames(String) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto.getParameterNames` elements
                .hierarchy(String) // optional :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto.getHierarchy`
                .treeDirection(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto.getTreeDirection`
                .build();
             
        
            Returns:
                A new DefaultParameterTreesRequestDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTreesRequestDto: ParameterTreesRequestDto) -> 'DefaultParameterTreesRequestDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto`): The instance to copy
        
            Returns:
                A copied immutable ParameterTreesRequestDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getHierarchy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto.getHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto`
        
            Returns:
                The value of the :code:`hierarchy` attribute
        
        
        """
        ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getTreeDirection(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto.getTreeDirection`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto`
        
            Returns:
                The value of the :code:`treeDirection` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`parameterNames`, :code:`hierarchy`, :code:`treeDirection`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTreesRequestDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withHierarchy(self, string: str) -> 'DefaultParameterTreesRequestDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto.getHierarchy` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for hierarchy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTreesRequestDto': ...
    @typing.overload
    def withParameterNames(self, stringArray: typing.List[str]) -> 'DefaultParameterTreesRequestDto': ...
    def withTreeDirection(self, string: str) -> 'DefaultParameterTreesRequestDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto.getTreeDirection` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for treeDirection
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllParameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTreesRequestDto.Builder': ...
        def addParameterName(self, string: str) -> 'DefaultParameterTreesRequestDto.Builder': ...
        def addParameterNames(self, stringArray: typing.List[str]) -> 'DefaultParameterTreesRequestDto.Builder': ...
        def build(self) -> 'DefaultParameterTreesRequestDto': ...
        def hierarchy(self, string: str) -> 'DefaultParameterTreesRequestDto.Builder': ...
        def parameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTreesRequestDto.Builder': ...
        def treeDirection(self, string: str) -> 'DefaultParameterTreesRequestDto.Builder': ...

class DefaultParameterTypeCategoryDto(ParameterTypeCategoryDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTypeCategoryDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTypeCategoryDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeCategoryDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTypeCategoryDto`.
        
            .. code-block: java
            
             DefaultParameterTypeCategoryDto.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultParameterTypeCategoryDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTypeCategoryDto: ParameterTypeCategoryDto) -> 'DefaultParameterTypeCategoryDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryDto` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryDto`): The instance to copy
        
            Returns:
                A copied immutable ParameterTypeCategoryDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTypeCategoryDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultParameterTypeCategoryDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultParameterTypeCategoryDto': ...
        def name(self, string: str) -> 'DefaultParameterTypeCategoryDto.Builder': ...

class DefaultParameterTypeDto(ParameterTypeDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTypeDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTypeDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTypeDto`.
        
            .. code-block: java
            
             DefaultParameterTypeDto.builder()
                .name(String) // required name
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto.getId`
                .linkRuleApplicable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto.isLinkRuleApplicable`
                .category(cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto.getCategory`
                .build();
             
        
            Returns:
                A new DefaultParameterTypeDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTypeDto: ParameterTypeDto) -> 'DefaultParameterTypeDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto`): The instance to copy
        
            Returns:
                A copied immutable ParameterTypeDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getCategory(self) -> ParameterTypeCategoryDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto.getCategory`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto`
        
            Returns:
                The value of the :code:`category` attribute
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`, :code:`id`, :code:`linkRuleApplicable`, :code:`category`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isLinkRuleApplicable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto.isLinkRuleApplicable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto`
        
            Returns:
                The value of the :code:`linkRuleApplicable` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTypeDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withCategory(self, parameterTypeCategoryDto: ParameterTypeCategoryDto) -> 'DefaultParameterTypeDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto.getCategory` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryDto`): A new value for category
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultParameterTypeDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto.getId` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withLinkRuleApplicable(self, boolean: bool) -> 'DefaultParameterTypeDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeDto.isLinkRuleApplicable` attribute. A value equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for linkRuleApplicable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultParameterTypeDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultParameterTypeDto': ...
        def category(self, parameterTypeCategoryDto: ParameterTypeCategoryDto) -> 'DefaultParameterTypeDto.Builder': ...
        def id(self, long: int) -> 'DefaultParameterTypeDto.Builder': ...
        def linkRuleApplicable(self, boolean: bool) -> 'DefaultParameterTypeDto.Builder': ...
        def name(self, string: str) -> 'DefaultParameterTypeDto.Builder': ...

class DefaultParameterTypesRequestDto(ParameterTypesRequestDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTypesRequestDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTypesRequestDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypesRequestDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTypesRequestDto`.
        
            .. code-block: java
            
             DefaultParameterTypesRequestDto.builder()
                .addParameterTypeName|addAllParameterTypeNames(String) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestDto.getParameterTypeNames` elements
                .allParameterTypesRequested(boolean) // optional :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestDto.isAllParameterTypesRequested`
                .build();
             
        
            Returns:
                A new DefaultParameterTypesRequestDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTypesRequestDto: ParameterTypesRequestDto) -> 'DefaultParameterTypesRequestDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestDto` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestDto`): The instance to copy
        
            Returns:
                A copied immutable ParameterTypesRequestDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getParameterTypeNames(self) -> java.util.Set[str]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`parameterTypeNames`, :code:`allParameterTypesRequested`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isAllParameterTypesRequested(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestDto.isAllParameterTypesRequested`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestDto`
        
            Returns:
                The value of the :code:`allParameterTypesRequested` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTypesRequestDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAllParameterTypesRequested(self, boolean: bool) -> 'DefaultParameterTypesRequestDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestDto.isAllParameterTypesRequested` attribute. A value
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for allParameterTypesRequested
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTypesRequestDto': ...
    @typing.overload
    def withParameterTypeNames(self, stringArray: typing.List[str]) -> 'DefaultParameterTypesRequestDto': ...
    class Builder:
        def addAllParameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTypesRequestDto.Builder': ...
        def addParameterTypeName(self, string: str) -> 'DefaultParameterTypesRequestDto.Builder': ...
        def addParameterTypeNames(self, stringArray: typing.List[str]) -> 'DefaultParameterTypesRequestDto.Builder': ...
        def allParameterTypesRequested(self, boolean: bool) -> 'DefaultParameterTypesRequestDto.Builder': ...
        def build(self) -> 'DefaultParameterTypesRequestDto': ...
        def parameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTypesRequestDto.Builder': ...

class DefaultParametersRequestDto(ParametersRequestDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParametersRequestDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParametersRequestDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParametersRequestDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParametersRequestDto`.
        
            .. code-block: java
            
             DefaultParametersRequestDto.builder()
                .acceleratorName(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getAcceleratorName`
                .parameterNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getParameterNames`
                .propertyFieldIds(Set<Long> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getPropertyFieldIds`
                .acceleratorZoneNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getAcceleratorZoneNames`
                .particleTransferNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getParticleTransferNames`
                .parameterTypeNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getParameterTypeNames`
                .parameterGroups(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getParameterGroups`
                .deviceNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getDeviceNames`
                .deviceIds(Set<Long> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getDeviceIds`
                .propertyNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getPropertyNames`
                .multiplexed(Boolean | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.isMultiplexed`
                .lsaImplementation(Boolean | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.isLsaImplementation`
                .writable(Boolean | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.isWritable`
                .readable(Boolean | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.isReadable`
                .parameterNamePattern(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getParameterNamePattern`
                .critical(Boolean | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.isCritical`
                .valueTypes(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto.getValueTypes`
                .build();
             
        
            Returns:
                A new DefaultParametersRequestDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parametersRequestDto: ParametersRequestDto) -> 'DefaultParametersRequestDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestDto`): The instance to copy
        
            Returns:
                A copied immutable ParametersRequestDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAcceleratorName(self) -> str: ...
    def getAcceleratorZoneNames(self) -> java.util.Set[str]: ...
    def getDeviceIds(self) -> java.util.Set[int]: ...
    def getDeviceNames(self) -> java.util.Set[str]: ...
    def getParameterGroups(self) -> java.util.Set[str]: ...
    def getParameterNamePattern(self) -> str: ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getParameterTypeNames(self) -> java.util.Set[str]: ...
    def getParticleTransferNames(self) -> java.util.Set[str]: ...
    def getPropertyFieldIds(self) -> java.util.Set[int]: ...
    def getPropertyNames(self) -> java.util.Set[str]: ...
    def getValueTypes(self) -> java.util.Set[str]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`acceleratorName`, :code:`parameterNames`, :code:`propertyFieldIds`,
            :code:`acceleratorZoneNames`, :code:`particleTransferNames`, :code:`parameterTypeNames`, :code:`parameterGroups`,
            :code:`deviceNames`, :code:`deviceIds`, :code:`propertyNames`, :code:`multiplexed`, :code:`lsaImplementation`,
            :code:`writable`, :code:`readable`, :code:`parameterNamePattern`, :code:`critical`, :code:`valueTypes`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isCritical(self) -> bool: ...
    def isLsaImplementation(self) -> bool: ...
    def isMultiplexed(self) -> bool: ...
    def isReadable(self) -> bool: ...
    def isWritable(self) -> bool: ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParametersRequestDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAcceleratorName(self, string: str) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withAcceleratorZoneNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withAcceleratorZoneNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto': ...
    def withCritical(self, boolean: bool) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withDeviceIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withDeviceIds(self, longArray: typing.List[int]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withDeviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withDeviceNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto': ...
    def withLsaImplementation(self, boolean: bool) -> 'DefaultParametersRequestDto': ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withParameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withParameterGroups(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto': ...
    def withParameterNamePattern(self, string: str) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withParameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withParameterNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withParameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withParameterTypeNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withParticleTransferNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withParticleTransferNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withPropertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withPropertyFieldIds(self, longArray: typing.List[int]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withPropertyNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withPropertyNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto': ...
    def withReadable(self, boolean: bool) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withValueTypes(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto': ...
    @typing.overload
    def withValueTypes(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto': ...
    def withWritable(self, boolean: bool) -> 'DefaultParametersRequestDto': ...
    class Builder:
        def acceleratorName(self, string: str) -> 'DefaultParametersRequestDto.Builder': ...
        def acceleratorZoneNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAcceleratorZoneName(self, string: str) -> 'DefaultParametersRequestDto.Builder': ...
        def addAcceleratorZoneNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAllAcceleratorZoneNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAllDeviceIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAllDeviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAllParameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAllParameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAllParameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAllParticleTransferNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAllPropertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAllPropertyNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addAllValueTypes(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addDeviceId(self, long: int) -> 'DefaultParametersRequestDto.Builder': ...
        def addDeviceIds(self, longArray: typing.List[int]) -> 'DefaultParametersRequestDto.Builder': ...
        def addDeviceName(self, string: str) -> 'DefaultParametersRequestDto.Builder': ...
        def addDeviceNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addParameterGroup(self, string: str) -> 'DefaultParametersRequestDto.Builder': ...
        def addParameterGroups(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addParameterName(self, string: str) -> 'DefaultParametersRequestDto.Builder': ...
        def addParameterNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addParameterTypeName(self, string: str) -> 'DefaultParametersRequestDto.Builder': ...
        def addParameterTypeNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addParticleTransferName(self, string: str) -> 'DefaultParametersRequestDto.Builder': ...
        def addParticleTransferNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addPropertyFieldId(self, long: int) -> 'DefaultParametersRequestDto.Builder': ...
        def addPropertyFieldIds(self, longArray: typing.List[int]) -> 'DefaultParametersRequestDto.Builder': ...
        def addPropertyName(self, string: str) -> 'DefaultParametersRequestDto.Builder': ...
        def addPropertyNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def addValueType(self, string: str) -> 'DefaultParametersRequestDto.Builder': ...
        def addValueTypes(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def build(self) -> 'DefaultParametersRequestDto': ...
        def critical(self, boolean: bool) -> 'DefaultParametersRequestDto.Builder': ...
        def deviceIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestDto.Builder': ...
        def deviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def lsaImplementation(self, boolean: bool) -> 'DefaultParametersRequestDto.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultParametersRequestDto.Builder': ...
        def parameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def parameterNamePattern(self, string: str) -> 'DefaultParametersRequestDto.Builder': ...
        def parameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def parameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def particleTransferNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def propertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestDto.Builder': ...
        def propertyNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def readable(self, boolean: bool) -> 'DefaultParametersRequestDto.Builder': ...
        def valueTypes(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestDto.Builder': ...
        def writable(self, boolean: bool) -> 'DefaultParametersRequestDto.Builder': ...

class DefaultParentToChildrenRelationDto(ParentToChildrenRelationDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParentToChildrenRelationDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto`.
    
        Use the builder to create immutable instances: :code:`DefaultParentToChildrenRelationDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParentToChildrenRelationDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParentToChildrenRelationDto`.
        
            .. code-block: java
            
             DefaultParentToChildrenRelationDto.builder()
                .addChildrenId|addAllChildrenIds(long) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto.getChildrenIds` elements
                .parentId(Long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto.getParentId`
                .build();
             
        
            Returns:
                A new DefaultParentToChildrenRelationDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parentToChildrenRelationDto: ParentToChildrenRelationDto) -> 'DefaultParentToChildrenRelationDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto`): The instance to copy
        
            Returns:
                A copied immutable ParentToChildrenRelationDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getChildrenIds(self) -> java.util.List[int]: ...
    def getParentId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto.getParentId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto`
        
            Returns:
                The value of the :code:`parentId` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`childrenIds`, :code:`parentId`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParentToChildrenRelationDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withChildrenIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParentToChildrenRelationDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto.getChildrenIds`.
        
            Parameters:
                elements (long...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParentToChildrenRelationDto` withChildrenIds (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto.getChildrenIds`. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements): An iterable of childrenIds elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withChildrenIds(self, longArray: typing.List[int]) -> 'DefaultParentToChildrenRelationDto': ...
    def withParentId(self, long: int) -> 'DefaultParentToChildrenRelationDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto.getParentId` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`): A new value for parentId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllChildrenIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParentToChildrenRelationDto.Builder': ...
        def addChildrenId(self, long: int) -> 'DefaultParentToChildrenRelationDto.Builder': ...
        def addChildrenIds(self, longArray: typing.List[int]) -> 'DefaultParentToChildrenRelationDto.Builder': ...
        def build(self) -> 'DefaultParentToChildrenRelationDto': ...
        def childrenIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParentToChildrenRelationDto.Builder': ...
        def parentId(self, long: int) -> 'DefaultParentToChildrenRelationDto.Builder': ...

class DefaultPropertyAndDeviceDto(PropertyAndDeviceDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultPropertyAndDeviceDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto`.
    
        Use the builder to create immutable instances: :code:`DefaultPropertyAndDeviceDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultPropertyAndDeviceDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultPropertyAndDeviceDto`.
        
            .. code-block: java
            
             DefaultPropertyAndDeviceDto.builder()
                .deviceId(Long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto.getDeviceId`
                .propertyName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto.getPropertyName`
                .build();
             
        
            Returns:
                A new DefaultPropertyAndDeviceDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(propertyAndDeviceDto: PropertyAndDeviceDto) -> 'DefaultPropertyAndDeviceDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto`): The instance to copy
        
            Returns:
                A copied immutable PropertyAndDeviceDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDeviceId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto.getDeviceId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto`
        
            Returns:
                The value of the :code:`deviceId` attribute
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto.getPropertyName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto`
        
            Returns:
                The value of the :code:`propertyName` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`deviceId`, :code:`propertyName`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`PropertyAndDeviceDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDeviceId(self, long: int) -> 'DefaultPropertyAndDeviceDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto.getDeviceId` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`): A new value for deviceId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyName(self, string: str) -> 'DefaultPropertyAndDeviceDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto.getPropertyName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for propertyName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultPropertyAndDeviceDto': ...
        def deviceId(self, long: int) -> 'DefaultPropertyAndDeviceDto.Builder': ...
        def propertyName(self, string: str) -> 'DefaultPropertyAndDeviceDto.Builder': ...

class DefaultPropertyFieldDto(PropertyFieldDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultPropertyFieldDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto`.
    
        Use the builder to create immutable instances: :code:`DefaultPropertyFieldDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultPropertyFieldDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultPropertyFieldDto`.
        
            .. code-block: java
            
             DefaultPropertyFieldDto.builder()
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getId`
                .deviceTypeName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getDeviceTypeName`
                .propertyName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getPropertyName`
                .fieldName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getFieldName`
                .build();
             
        
            Returns:
                A new DefaultPropertyFieldDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(propertyFieldDto: PropertyFieldDto) -> 'DefaultPropertyFieldDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto`): The instance to copy
        
            Returns:
                A copied immutable PropertyFieldDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDeviceTypeName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getDeviceTypeName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto`
        
            Returns:
                The value of the :code:`deviceTypeName` attribute
        
        
        """
        ...
    def getFieldName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getFieldName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto`
        
            Returns:
                The value of the :code:`fieldName` attribute
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getPropertyName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto`
        
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
            Prints the immutable value :code:`PropertyFieldDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDeviceTypeName(self, string: str) -> 'DefaultPropertyFieldDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getDeviceTypeName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for deviceTypeName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withFieldName(self, string: str) -> 'DefaultPropertyFieldDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getFieldName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for fieldName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultPropertyFieldDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getId` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyName(self, string: str) -> 'DefaultPropertyFieldDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldDto.getPropertyName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for propertyName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultPropertyFieldDto': ...
        def deviceTypeName(self, string: str) -> 'DefaultPropertyFieldDto.Builder': ...
        def fieldName(self, string: str) -> 'DefaultPropertyFieldDto.Builder': ...
        def id(self, long: int) -> 'DefaultPropertyFieldDto.Builder': ...
        def propertyName(self, string: str) -> 'DefaultPropertyFieldDto.Builder': ...

class DefaultSaveParameterRelationDto(SaveParameterRelationDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultSaveParameterRelationDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto`.
    
        Use the builder to create immutable instances: :code:`DefaultSaveParameterRelationDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultSaveParameterRelationDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultSaveParameterRelationDto`.
        
            .. code-block: java
            
             DefaultSaveParameterRelationDto.builder()
                .hierarchy(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto.getHierarchy`
                .addParent2ChildrenRelation|addAllParent2ChildrenRelations(cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto) // :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto.getParent2ChildrenRelations` elements
                .build();
             
        
            Returns:
                A new DefaultSaveParameterRelationDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(saveParameterRelationDto: SaveParameterRelationDto) -> 'DefaultSaveParameterRelationDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto`): The instance to copy
        
            Returns:
                A copied immutable SaveParameterRelationDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getHierarchy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto.getHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto`
        
            Returns:
                The value of the :code:`hierarchy` attribute
        
        
        """
        ...
    def getParent2ChildrenRelations(self) -> java.util.List[ParentToChildrenRelationDto]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`hierarchy`, :code:`parent2ChildrenRelations`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`SaveParameterRelationDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withHierarchy(self, string: str) -> 'DefaultSaveParameterRelationDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto.getHierarchy` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for hierarchy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParent2ChildrenRelations(self, parentToChildrenRelationDtoArray: typing.List[ParentToChildrenRelationDto]) -> 'DefaultSaveParameterRelationDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto.getParent2ChildrenRelations`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultSaveParameterRelationDto` withParent2ChildrenRelations (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationDto.getParent2ChildrenRelations`. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationDto`> elements): An iterable of parent2ChildrenRelations elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParent2ChildrenRelations(self, iterable: java.lang.Iterable[ParentToChildrenRelationDto]) -> 'DefaultSaveParameterRelationDto': ...
    class Builder:
        def addAllParent2ChildrenRelations(self, iterable: java.lang.Iterable[ParentToChildrenRelationDto]) -> 'DefaultSaveParameterRelationDto.Builder': ...
        def addParent2ChildrenRelation(self, parentToChildrenRelationDto: ParentToChildrenRelationDto) -> 'DefaultSaveParameterRelationDto.Builder': ...
        def addParent2ChildrenRelations(self, parentToChildrenRelationDtoArray: typing.List[ParentToChildrenRelationDto]) -> 'DefaultSaveParameterRelationDto.Builder': ...
        def build(self) -> 'DefaultSaveParameterRelationDto': ...
        def hierarchy(self, string: str) -> 'DefaultSaveParameterRelationDto.Builder': ...
        def parent2ChildrenRelations(self, iterable: java.lang.Iterable[ParentToChildrenRelationDto]) -> 'DefaultSaveParameterRelationDto.Builder': ...

class DefaultTypeDto(TypeDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultTypeDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.TypeDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.TypeDto`.
    
        Use the builder to create immutable instances: :code:`DefaultTypeDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultTypeDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultTypeDto`.
        
            .. code-block: java
            
             DefaultTypeDto.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultTypeDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(typeDto: TypeDto) -> 'DefaultTypeDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.TypeDto` value. Uses accessors to get values to
            initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.TypeDto`): The instance to copy
        
            Returns:
                A copied immutable TypeDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`TypeDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultTypeDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultTypeDto': ...
        def name(self, string: str) -> 'DefaultTypeDto.Builder': ...

class DefaultValueCompareTypeDto(ValueCompareTypeDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultValueCompareTypeDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ValueCompareTypeDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ValueCompareTypeDto`.
    
        Use the builder to create immutable instances: :code:`DefaultValueCompareTypeDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultValueCompareTypeDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultValueCompareTypeDto`.
        
            .. code-block: java
            
             DefaultValueCompareTypeDto.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultValueCompareTypeDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(valueCompareTypeDto: ValueCompareTypeDto) -> 'DefaultValueCompareTypeDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ValueCompareTypeDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ValueCompareTypeDto`): The instance to copy
        
            Returns:
                A copied immutable ValueCompareTypeDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ValueCompareTypeDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultValueCompareTypeDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultValueCompareTypeDto': ...
        def name(self, string: str) -> 'DefaultValueCompareTypeDto.Builder': ...

class DefaultValueDescriptorDto(ValueDescriptorDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultValueDescriptorDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto`.
    
        Use the builder to create immutable instances: :code:`DefaultValueDescriptorDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultValueDescriptorDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultValueDescriptorDto`.
        
            .. code-block: java
            
             DefaultValueDescriptorDto.builder()
                .enumType(cern.lsa.client.rest.api.v1.dto.EnumTypeDto | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getEnumType`
                .booleanType(cern.lsa.client.rest.api.v1.dto.BooleanTypeDto | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getBooleanType`
                .columnCount(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getColumnCount`
                .rowCount(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getRowCount`
                .max(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getMax`
                .min(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getMin`
                .absoluteTolerance(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getAbsoluteTolerance`
                .relativeTolerance(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getRelativeTolerance`
                .xPrecision(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getXPrecision`
                .xUnit(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getXUnit`
                .yPrecision(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getYPrecision`
                .yUnit(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto.getYUnit`
                .build();
             
        
            Returns:
                A new DefaultValueDescriptorDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(valueDescriptorDto: ValueDescriptorDto) -> 'DefaultValueDescriptorDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorDto`): The instance to copy
        
            Returns:
                A copied immutable ValueDescriptorDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAbsoluteTolerance(self) -> float: ...
    def getBooleanType(self) -> BooleanTypeDto: ...
    def getColumnCount(self) -> int: ...
    def getEnumType(self) -> EnumTypeDto: ...
    def getMax(self) -> float: ...
    def getMin(self) -> float: ...
    def getRelativeTolerance(self) -> float: ...
    def getRowCount(self) -> int: ...
    def getXPrecision(self) -> int: ...
    def getXUnit(self) -> str: ...
    def getYPrecision(self) -> int: ...
    def getYUnit(self) -> str: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`enumType`, :code:`booleanType`, :code:`columnCount`, :code:`rowCount`,
            :code:`max`, :code:`min`, :code:`absoluteTolerance`, :code:`relativeTolerance`, :code:`xPrecision`, :code:`xUnit`,
            :code:`yPrecision`, :code:`yUnit`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ValueDescriptorDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAbsoluteTolerance(self, double: float) -> 'DefaultValueDescriptorDto': ...
    def withBooleanType(self, booleanTypeDto: BooleanTypeDto) -> 'DefaultValueDescriptorDto': ...
    def withColumnCount(self, integer: int) -> 'DefaultValueDescriptorDto': ...
    def withEnumType(self, enumTypeDto: EnumTypeDto) -> 'DefaultValueDescriptorDto': ...
    def withMax(self, double: float) -> 'DefaultValueDescriptorDto': ...
    def withMin(self, double: float) -> 'DefaultValueDescriptorDto': ...
    def withRelativeTolerance(self, double: float) -> 'DefaultValueDescriptorDto': ...
    def withRowCount(self, integer: int) -> 'DefaultValueDescriptorDto': ...
    def withXPrecision(self, integer: int) -> 'DefaultValueDescriptorDto': ...
    def withXUnit(self, string: str) -> 'DefaultValueDescriptorDto': ...
    def withYPrecision(self, integer: int) -> 'DefaultValueDescriptorDto': ...
    def withYUnit(self, string: str) -> 'DefaultValueDescriptorDto': ...
    class Builder:
        def absoluteTolerance(self, double: float) -> 'DefaultValueDescriptorDto.Builder': ...
        def booleanType(self, booleanTypeDto: BooleanTypeDto) -> 'DefaultValueDescriptorDto.Builder': ...
        def build(self) -> 'DefaultValueDescriptorDto': ...
        def columnCount(self, integer: int) -> 'DefaultValueDescriptorDto.Builder': ...
        def enumType(self, enumTypeDto: EnumTypeDto) -> 'DefaultValueDescriptorDto.Builder': ...
        def max(self, double: float) -> 'DefaultValueDescriptorDto.Builder': ...
        def min(self, double: float) -> 'DefaultValueDescriptorDto.Builder': ...
        def relativeTolerance(self, double: float) -> 'DefaultValueDescriptorDto.Builder': ...
        def rowCount(self, integer: int) -> 'DefaultValueDescriptorDto.Builder': ...
        def xPrecision(self, integer: int) -> 'DefaultValueDescriptorDto.Builder': ...
        def xUnit(self, string: str) -> 'DefaultValueDescriptorDto.Builder': ...
        def yPrecision(self, integer: int) -> 'DefaultValueDescriptorDto.Builder': ...
        def yUnit(self, string: str) -> 'DefaultValueDescriptorDto.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1.dto")``.

    AcceleratorZoneDto: typing.Type[AcceleratorZoneDto]
    BooleanItemDto: typing.Type[BooleanItemDto]
    BooleanTypeDto: typing.Type[BooleanTypeDto]
    DefaultAcceleratorZoneDto: typing.Type[DefaultAcceleratorZoneDto]
    DefaultBooleanItemDto: typing.Type[DefaultBooleanItemDto]
    DefaultBooleanTypeDto: typing.Type[DefaultBooleanTypeDto]
    DefaultDeviceDto: typing.Type[DefaultDeviceDto]
    DefaultDeviceMetaTypeDto: typing.Type[DefaultDeviceMetaTypeDto]
    DefaultDeviceStateDto: typing.Type[DefaultDeviceStateDto]
    DefaultDeviceTypeImplementationDto: typing.Type[DefaultDeviceTypeImplementationDto]
    DefaultDeviceTypeVersionContainerDto: typing.Type[DefaultDeviceTypeVersionContainerDto]
    DefaultDeviceTypeVersionDto: typing.Type[DefaultDeviceTypeVersionDto]
    DefaultDeviceTypeVersionNumberDto: typing.Type[DefaultDeviceTypeVersionNumberDto]
    DefaultEnumItemDto: typing.Type[DefaultEnumItemDto]
    DefaultEnumTypeDto: typing.Type[DefaultEnumTypeDto]
    DefaultErrorDto: typing.Type[DefaultErrorDto]
    DefaultIncaPropertyFieldInfoDto: typing.Type[DefaultIncaPropertyFieldInfoDto]
    DefaultIncaPropertyFieldInfosRequestDto: typing.Type[DefaultIncaPropertyFieldInfosRequestDto]
    DefaultMakeRuleClassInfoDto: typing.Type[DefaultMakeRuleClassInfoDto]
    DefaultMakeRuleConfigInfoDto: typing.Type[DefaultMakeRuleConfigInfoDto]
    DefaultMakeRuleConfigStatusDto: typing.Type[DefaultMakeRuleConfigStatusDto]
    DefaultMakeRuleInfoDto: typing.Type[DefaultMakeRuleInfoDto]
    DefaultParameterAttributesDto: typing.Type[DefaultParameterAttributesDto]
    DefaultParameterDto: typing.Type[DefaultParameterDto]
    DefaultParameterGroupDto: typing.Type[DefaultParameterGroupDto]
    DefaultParameterTreeDataDto: typing.Type[DefaultParameterTreeDataDto]
    DefaultParameterTreeNodeDto: typing.Type[DefaultParameterTreeNodeDto]
    DefaultParameterTreeRelationDto: typing.Type[DefaultParameterTreeRelationDto]
    DefaultParameterTreesRequestDto: typing.Type[DefaultParameterTreesRequestDto]
    DefaultParameterTypeCategoryDto: typing.Type[DefaultParameterTypeCategoryDto]
    DefaultParameterTypeDto: typing.Type[DefaultParameterTypeDto]
    DefaultParameterTypesRequestDto: typing.Type[DefaultParameterTypesRequestDto]
    DefaultParametersRequestDto: typing.Type[DefaultParametersRequestDto]
    DefaultParentToChildrenRelationDto: typing.Type[DefaultParentToChildrenRelationDto]
    DefaultPropertyAndDeviceDto: typing.Type[DefaultPropertyAndDeviceDto]
    DefaultPropertyFieldDto: typing.Type[DefaultPropertyFieldDto]
    DefaultSaveParameterRelationDto: typing.Type[DefaultSaveParameterRelationDto]
    DefaultTypeDto: typing.Type[DefaultTypeDto]
    DefaultValueCompareTypeDto: typing.Type[DefaultValueCompareTypeDto]
    DefaultValueDescriptorDto: typing.Type[DefaultValueDescriptorDto]
    DeviceDto: typing.Type[DeviceDto]
    DeviceMetaTypeDto: typing.Type[DeviceMetaTypeDto]
    DeviceStateDto: typing.Type[DeviceStateDto]
    DeviceTypeImplementationDto: typing.Type[DeviceTypeImplementationDto]
    DeviceTypeVersionContainerDto: typing.Type[DeviceTypeVersionContainerDto]
    DeviceTypeVersionDto: typing.Type[DeviceTypeVersionDto]
    DeviceTypeVersionNumberDto: typing.Type[DeviceTypeVersionNumberDto]
    EnumItemDto: typing.Type[EnumItemDto]
    EnumTypeDto: typing.Type[EnumTypeDto]
    ErrorDto: typing.Type[ErrorDto]
    IncaPropertyFieldInfoDto: typing.Type[IncaPropertyFieldInfoDto]
    IncaPropertyFieldInfosRequestDto: typing.Type[IncaPropertyFieldInfosRequestDto]
    MakeRuleClassInfoDto: typing.Type[MakeRuleClassInfoDto]
    MakeRuleConfigInfoDto: typing.Type[MakeRuleConfigInfoDto]
    MakeRuleConfigStatusDto: typing.Type[MakeRuleConfigStatusDto]
    MakeRuleInfoDto: typing.Type[MakeRuleInfoDto]
    ParameterAttributesDto: typing.Type[ParameterAttributesDto]
    ParameterDto: typing.Type[ParameterDto]
    ParameterGroupDto: typing.Type[ParameterGroupDto]
    ParameterTreeDataDto: typing.Type[ParameterTreeDataDto]
    ParameterTreeNodeDto: typing.Type[ParameterTreeNodeDto]
    ParameterTreeRelationDto: typing.Type[ParameterTreeRelationDto]
    ParameterTreesRequestDto: typing.Type[ParameterTreesRequestDto]
    ParameterTypeCategoryDto: typing.Type[ParameterTypeCategoryDto]
    ParameterTypeDto: typing.Type[ParameterTypeDto]
    ParameterTypesRequestDto: typing.Type[ParameterTypesRequestDto]
    ParametersRequestDto: typing.Type[ParametersRequestDto]
    ParentToChildrenRelationDto: typing.Type[ParentToChildrenRelationDto]
    PropertyAndDeviceDto: typing.Type[PropertyAndDeviceDto]
    PropertyFieldDto: typing.Type[PropertyFieldDto]
    SaveParameterRelationDto: typing.Type[SaveParameterRelationDto]
    TypeDto: typing.Type[TypeDto]
    ValueCompareTypeDto: typing.Type[ValueCompareTypeDto]
    ValueDescriptorDto: typing.Type[ValueDescriptorDto]
    commons: cern.lsa.client.rest.api.v1.dto.commons.__module_protocol__
    settings: cern.lsa.client.rest.api.v1.dto.settings.__module_protocol__
    trim: cern.lsa.client.rest.api.v1.dto.trim.__module_protocol__
