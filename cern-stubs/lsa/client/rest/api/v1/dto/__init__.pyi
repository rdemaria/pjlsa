import cern.accsoft.commons.util
import java.lang
import java.time
import java.util
import typing



class AcceleratorZoneRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface AcceleratorZoneRest extends cern.accsoft.commons.util.Named
    
        AcceleratorZoneRest
    """
    @staticmethod
    def builder() -> 'DefaultAcceleratorZoneRest.Builder': ...
    def getAcceleratorName(self) -> str: ...

class BooleanItemRest:
    """
    @Immutable public interface BooleanItemRest
    """
    @staticmethod
    def builder() -> 'DefaultBooleanItemRest.Builder': ...
    def getStandardMeaning(self) -> str: ...
    def getValue(self) -> bool: ...

class BooleanTypeRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface BooleanTypeRest extends cern.accsoft.commons.util.Named
    """
    @staticmethod
    def builder() -> 'DefaultBooleanTypeRest.Builder': ...
    def getBooleanItems(self) -> java.util.List[BooleanItemRest]: ...

class DeviceMetaTypeRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface DeviceMetaTypeRest extends cern.accsoft.commons.util.Named
    
        DeviceMetaTypeEnumRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceMetaTypeRest.Builder': ...

class DeviceRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface DeviceRest extends cern.accsoft.commons.util.Named
    
        DeviceRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceRest.Builder': ...
    def getAcceleratorZone(self) -> AcceleratorZoneRest: ...
    def getDescription(self) -> str: ...
    def getDeviceAlias(self) -> str: ...
    def getDeviceGroups(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersion(self) -> 'DeviceTypeVersionContainerRest': ...
    def getFecName(self) -> str: ...
    def getId(self) -> int: ...
    def getPosition(self) -> float: ...
    def getServerName(self) -> str: ...
    def getSortOrder(self) -> int: ...
    def getState(self) -> 'DeviceStateRest': ...
    def isCycleBound(self) -> bool: ...
    def isMultiplexed(self) -> bool: ...

class DeviceStateRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface DeviceStateRest extends cern.accsoft.commons.util.Named
    
        DeviceStateRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceStateRest.Builder': ...

class DeviceTypeImplementationRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface DeviceTypeImplementationRest extends cern.accsoft.commons.util.Named
    
        DeviceTypeImplementationRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeImplementationRest.Builder': ...

class DeviceTypeVersionContainerRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface DeviceTypeVersionContainerRest extends cern.accsoft.commons.util.Named
    
        DeviceTypeVersionContainerRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionContainerRest.Builder': ...
    def getDescription(self) -> str: ...
    def getId(self) -> int: ...
    def getMetaType(self) -> DeviceMetaTypeRest: ...
    def getOtherVersions(self) -> java.util.List['DeviceTypeVersionRest']: ...
    def getPrimaryVersion(self) -> 'DeviceTypeVersionRest': ...

class DeviceTypeVersionNumberRest:
    """
    @Immutable public interface DeviceTypeVersionNumberRest
    
        DeviceTypeVersionNumberRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionNumberRest.Builder': ...
    def getMajor(self) -> int: ...
    def getMinor(self) -> int: ...

class DeviceTypeVersionRest:
    """
    @Immutable public interface DeviceTypeVersionRest
    
        DeviceTypeVersionRest
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionRest.Builder': ...
    def getId(self) -> int: ...
    def getImplementation(self) -> DeviceTypeImplementationRest: ...
    def getVersionNumber(self) -> DeviceTypeVersionNumberRest: ...

class EnumItemRest:
    """
    @Immutable public interface EnumItemRest
    """
    @staticmethod
    def builder() -> 'DefaultEnumItemRest.Builder': ...
    def getCode(self) -> int: ...
    def getStandardMeaning(self) -> str: ...
    def getSymbol(self) -> str: ...
    def isSettable(self) -> bool: ...

class EnumTypeRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface EnumTypeRest extends cern.accsoft.commons.util.Named
    """
    @staticmethod
    def builder() -> 'DefaultEnumTypeRest.Builder': ...
    def getEnumItems(self) -> java.util.List[EnumItemRest]: ...
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

class IncaPropertyFieldInfoRest:
    """
    @Immutable public interface IncaPropertyFieldInfoRest
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfoRest.Builder': ...
    def getAssociatedPropertyFieldRest(self) -> 'PropertyFieldRest': ...
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
    def getPropertyFieldRest(self) -> 'PropertyFieldRest':
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

class IncaPropertyFieldInfosRequestRest:
    """
    @Immutable public interface IncaPropertyFieldInfosRequestRest
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfosRequestRest.Builder': ...
    @staticmethod
    def byPropertyFieldId(long: int) -> 'IncaPropertyFieldInfosRequestRest': ...
    @staticmethod
    def byPropertyFieldIds(set: java.util.Set[int]) -> 'IncaPropertyFieldInfosRequestRest': ...
    def getPropertyFieldIds(self) -> java.util.Set[int]: ...

class MakeRuleClassInfoRest:
    """
    @Immutable public interface MakeRuleClassInfoRest
    
        MakeRuleClassInfoRest
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleClassInfoRest.Builder': ...
    def getClassName(self) -> str: ...
    def getProductName(self) -> str: ...
    def getVersion(self) -> str: ...

class MakeRuleConfigInfoRest:
    """
    @Immutable public interface MakeRuleConfigInfoRest
    
        MakeRuleConfigInfoRest
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigInfoRest.Builder': ...
    def getMakeRuleConfigStatus(self) -> 'MakeRuleConfigStatusRest': ...
    def getMakeRuleInfo(self) -> 'MakeRuleInfoRest': ...

class MakeRuleConfigStatusRest:
    """
    @Immutable public interface MakeRuleConfigStatusRest
    
        MakeRuleConfigStatusRest
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigStatusRest.Builder': ...
    def getName(self) -> str: ...

class MakeRuleInfoRest:
    """
    @Immutable public interface MakeRuleInfoRest
    
        MakeRuleInfoRest
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleInfoRest.Builder': ...
    def getMakeRuleClassInfo(self) -> MakeRuleClassInfoRest: ...
    def getMakeRuleName(self) -> str: ...

class ParameterAttributesRest:
    """
    @Immutable public interface ParameterAttributesRest
    
        ParameterAttributesRest
    """
    @staticmethod
    def builder() -> 'DefaultParameterAttributesRest.Builder': ...
    def getAbsoluteTolerance(self) -> float: ...
    def getDefaultHierarchy(self) -> str: ...
    def getDevice(self) -> DeviceRest: ...
    def getMaxValue(self) -> float: ...
    def getMinValue(self) -> float: ...
    def getParameterId(self) -> int: ...
    def getParameterName(self) -> str: ...
    def getParameterType(self) -> 'ParameterTypeRest': ...
    def getPropertyField(self) -> 'PropertyFieldRest': ...
    def getRelativeTolerance(self) -> float: ...
    def getXPrecision(self) -> int: ...
    def getYPrecision(self) -> int: ...
    def isBelongsToFunctionBProc(self) -> bool: ...
    def isReservedForOpExperts(self) -> bool: ...
    def isTrimable(self) -> bool: ...

class ParameterGroupRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface ParameterGroupRest extends cern.accsoft.commons.util.Named
    
        ParameterGroupRest
    """
    @staticmethod
    def builder() -> 'DefaultParameterGroupRest.Builder': ...
    def getAcceleratorName(self) -> str: ...
    def getCreateDate(self) -> java.time.OffsetDateTime: ...
    def getCreator(self) -> str: ...
    def getDescription(self) -> str: ...
    def getId(self) -> int: ...

class ParameterRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface ParameterRest extends cern.accsoft.commons.util.Named
    """
    def belongsToFunctionBeamProcess(self) -> bool: ...
    @staticmethod
    def builder() -> 'DefaultParameterRest.Builder': ...
    def getDefaultHierarchy(self) -> str: ...
    def getDevice(self) -> DeviceRest: ...
    def getId(self) -> int: ...
    def getParameterGroups(self) -> java.util.List[str]: ...
    def getParameterType(self) -> 'ParameterTypeRest': ...
    def getPropertyField(self) -> 'PropertyFieldRest': ...
    def getValueDescriptor(self) -> 'ValueDescriptorRest': ...
    def getValueType(self) -> 'TypeRest': ...
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

class ParameterTreeDataRest:
    """
    @Immutable public interface ParameterTreeDataRest
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeDataRest.Builder': ...
    def getNodes(self) -> java.util.Set['ParameterTreeNodeRest']: ...
    def getRelations(self) -> java.util.Set['ParameterTreeRelationRest']: ...
    def getStartNodeIds(self) -> java.util.Set[int]: ...

class ParameterTreeNodeRest:
    """
    @Immutable public interface ParameterTreeNodeRest
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeNodeRest.Builder': ...
    def getParameter(self) -> ParameterRest: ...
    def isSource(self) -> bool: ...

class ParameterTreeRelationRest:
    """
    @Immutable public interface ParameterTreeRelationRest
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeRelationRest.Builder': ...
    def getChildParameterId(self) -> int: ...
    def getParentParameterId(self) -> int: ...

class ParameterTreesRequestRest:
    """
    @Immutable public interface ParameterTreesRequestRest
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreesRequestRest.Builder': ...
    def getHierarchy(self) -> str: ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getTreeDirection(self) -> str: ...

class ParameterTypeCategoryRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface ParameterTypeCategoryRest extends cern.accsoft.commons.util.Named
    
        ParameterTypeCategoryRest
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeCategoryRest.Builder': ...

class ParameterTypeRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface ParameterTypeRest extends cern.accsoft.commons.util.Named
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeRest.Builder': ...
    def getCategory(self) -> ParameterTypeCategoryRest: ...
    def getId(self) -> int: ...
    def isLinkRuleApplicable(self) -> bool: ...

class ParameterTypesRequestRest:
    """
    @Immutable public interface ParameterTypesRequestRest
    """
    def getParameterTypeNames(self) -> java.util.Set[str]: ...
    def isAllParameterTypesRequested(self) -> bool: ...

class ParametersRequestRest:
    """
    @Immutable public interface ParametersRequestRest
    
        Describes criteria when searching for LSA parameters. This object should be created using
        :code:`ParametersRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> 'DefaultParametersRequestRest.Builder': ...
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

class ParentToChildrenRelationRest:
    """
    @Immutable public interface ParentToChildrenRelationRest
    
        ParentToChildrenRelationRest
    """
    @staticmethod
    def builder() -> 'DefaultParentToChildrenRelationRest.Builder': ...
    def getChildrenIds(self) -> java.util.List[int]: ...
    def getParentId(self) -> int: ...

class PropertyAndDeviceRest:
    """
    @Immutable public interface PropertyAndDeviceRest
    
        PropertyAndDeviceRest
    """
    @staticmethod
    def builder() -> 'DefaultPropertyAndDeviceRest.Builder': ...
    def getDeviceId(self) -> int: ...
    def getPropertyName(self) -> str: ...

class PropertyFieldRest:
    """
    @Immutable public interface PropertyFieldRest
    """
    @staticmethod
    def builder() -> 'DefaultPropertyFieldRest.Builder': ...
    def getDeviceTypeName(self) -> str: ...
    def getFieldName(self) -> str: ...
    def getId(self) -> int: ...
    def getPropertyName(self) -> str: ...

class SaveParameterRelationRest:
    """
    @Immutable public interface SaveParameterRelationRest
    
        SaveParameterRelationRest
    """
    @staticmethod
    def builder() -> 'DefaultSaveParameterRelationRest.Builder': ...
    def getHierarchy(self) -> str: ...
    def getParent2ChildrenRelations(self) -> java.util.List[ParentToChildrenRelationRest]: ...

class TypeRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface TypeRest extends cern.accsoft.commons.util.Named
    
        TypeRest
    """
    @staticmethod
    def builder() -> 'DefaultTypeRest.Builder': ...

class ValueCompareTypeRest(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface ValueCompareTypeRest extends cern.accsoft.commons.util.Named
    """
    @staticmethod
    def builder() -> 'DefaultValueCompareTypeRest.Builder': ...

class ValueDescriptorRest:
    """
    @Immutable public interface ValueDescriptorRest
    """
    @staticmethod
    def builder() -> 'DefaultValueDescriptorRest.Builder': ...
    def getAbsoluteTolerance(self) -> float: ...
    def getBooleanType(self) -> BooleanTypeRest: ...
    def getColumnCount(self) -> int: ...
    def getEnumType(self) -> EnumTypeRest: ...
    def getMax(self) -> float: ...
    def getMin(self) -> float: ...
    def getRelativeTolerance(self) -> float: ...
    def getRowCount(self) -> int: ...
    def getXPrecision(self) -> int: ...
    def getXUnit(self) -> str: ...
    def getYPrecision(self) -> int: ...
    def getYUnit(self) -> str: ...

class DefaultAcceleratorZoneRest(AcceleratorZoneRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultAcceleratorZoneRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneRest`.
    
        Use the builder to create immutable instances: :code:`DefaultAcceleratorZoneRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultAcceleratorZoneRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultAcceleratorZoneRest`.
        
            .. code-block: java
            
             DefaultAcceleratorZoneRest.builder()
                .name(String) // required name
                .acceleratorName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneRest.getAcceleratorName`
                .build();
             
        
            Returns:
                A new DefaultAcceleratorZoneRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(acceleratorZoneRest: AcceleratorZoneRest) -> 'DefaultAcceleratorZoneRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneRest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneRest`): The instance to copy
        
            Returns:
                A copied immutable AcceleratorZoneRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAcceleratorName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneRest.getAcceleratorName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneRest`
        
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
            Prints the immutable value :code:`AcceleratorZoneRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAcceleratorName(self, string: str) -> 'DefaultAcceleratorZoneRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneRest.getAcceleratorName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for acceleratorName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultAcceleratorZoneRest':
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
        def acceleratorName(self, string: str) -> 'DefaultAcceleratorZoneRest.Builder': ...
        def build(self) -> 'DefaultAcceleratorZoneRest': ...
        def name(self, string: str) -> 'DefaultAcceleratorZoneRest.Builder': ...

class DefaultBooleanItemRest(BooleanItemRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultBooleanItemRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest`.
    
        Use the builder to create immutable instances: :code:`DefaultBooleanItemRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultBooleanItemRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultBooleanItemRest`.
        
            .. code-block: java
            
             DefaultBooleanItemRest.builder()
                .value(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest.getValue`
                .standardMeaning(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest.getStandardMeaning`
                .build();
             
        
            Returns:
                A new DefaultBooleanItemRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(booleanItemRest: BooleanItemRest) -> 'DefaultBooleanItemRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest`): The instance to copy
        
            Returns:
                A copied immutable BooleanItemRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getStandardMeaning(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest.getStandardMeaning`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest`
        
            Returns:
                The value of the :code:`standardMeaning` attribute
        
        
        """
        ...
    def getValue(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest.getValue`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest`
        
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
            Prints the immutable value :code:`BooleanItemRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withStandardMeaning(self, string: str) -> 'DefaultBooleanItemRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest.getStandardMeaning` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for standardMeaning
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withValue(self, boolean: bool) -> 'DefaultBooleanItemRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest.getValue` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for value
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultBooleanItemRest': ...
        def standardMeaning(self, string: str) -> 'DefaultBooleanItemRest.Builder': ...
        def value(self, boolean: bool) -> 'DefaultBooleanItemRest.Builder': ...

class DefaultBooleanTypeRest(BooleanTypeRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultBooleanTypeRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeRest`.
    
        Use the builder to create immutable instances: :code:`DefaultBooleanTypeRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultBooleanTypeRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultBooleanTypeRest`.
        
            .. code-block: java
            
             DefaultBooleanTypeRest.builder()
                .name(String) // required name
                .addBooleanItem|addAllBooleanItems(cern.lsa.client.rest.api.v1.dto.BooleanItemRest) // :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeRest.getBooleanItems` elements
                .build();
             
        
            Returns:
                A new DefaultBooleanTypeRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(booleanTypeRest: BooleanTypeRest) -> 'DefaultBooleanTypeRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeRest`): The instance to copy
        
            Returns:
                A copied immutable BooleanTypeRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBooleanItems(self) -> java.util.List[BooleanItemRest]: ...
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
            Prints the immutable value :code:`BooleanTypeRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withBooleanItems(self, booleanItemRestArray: typing.List[BooleanItemRest]) -> 'DefaultBooleanTypeRest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeRest.getBooleanItems`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultBooleanTypeRest` withBooleanItems (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.BooleanTypeRest.getBooleanItems`. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.BooleanItemRest`> elements): An iterable of booleanItems elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withBooleanItems(self, iterable: java.lang.Iterable[BooleanItemRest]) -> 'DefaultBooleanTypeRest': ...
    def withName(self, string: str) -> 'DefaultBooleanTypeRest':
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
        def addAllBooleanItems(self, iterable: java.lang.Iterable[BooleanItemRest]) -> 'DefaultBooleanTypeRest.Builder': ...
        def addBooleanItem(self, booleanItemRest: BooleanItemRest) -> 'DefaultBooleanTypeRest.Builder': ...
        def addBooleanItems(self, booleanItemRestArray: typing.List[BooleanItemRest]) -> 'DefaultBooleanTypeRest.Builder': ...
        def booleanItems(self, iterable: java.lang.Iterable[BooleanItemRest]) -> 'DefaultBooleanTypeRest.Builder': ...
        def build(self) -> 'DefaultBooleanTypeRest': ...
        def name(self, string: str) -> 'DefaultBooleanTypeRest.Builder': ...

class DefaultDeviceMetaTypeRest(DeviceMetaTypeRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceMetaTypeRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeRest`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceMetaTypeRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceMetaTypeRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceMetaTypeRest`.
        
            .. code-block: java
            
             DefaultDeviceMetaTypeRest.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultDeviceMetaTypeRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceMetaTypeRest: DeviceMetaTypeRest) -> 'DefaultDeviceMetaTypeRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeRest`): The instance to copy
        
            Returns:
                A copied immutable DeviceMetaTypeRest instance
        
        
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
            Prints the immutable value :code:`DeviceMetaTypeRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultDeviceMetaTypeRest':
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
        def build(self) -> 'DefaultDeviceMetaTypeRest': ...
        def name(self, string: str) -> 'DefaultDeviceMetaTypeRest.Builder': ...

class DefaultDeviceRest(DeviceRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceRest`.
        
            .. code-block: java
            
             DefaultDeviceRest.builder()
                .name(String) // required name
                .acceleratorZone(cern.lsa.client.rest.api.v1.dto.AcceleratorZoneRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getAcceleratorZone`
                .description(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getDescription`
                .deviceAlias(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getDeviceAlias`
                .addDeviceGroup|addAllDeviceGroups(String) // :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getDeviceGroups` elements
                .deviceTypeVersion(cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getDeviceTypeVersion`
                .fecName(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getFecName`
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getId`
                .multiplexed(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.isMultiplexed`
                .cycleBound(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.isCycleBound`
                .position(double) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getPosition`
                .sortOrder(int) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getSortOrder`
                .serverName(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getServerName`
                .state(cern.lsa.client.rest.api.v1.dto.DeviceStateRest | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getState`
                .build();
             
        
            Returns:
                A new DefaultDeviceRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceRest: DeviceRest) -> 'DefaultDeviceRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest` value. Uses accessors to get values
            to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`): The instance to copy
        
            Returns:
                A copied immutable DeviceRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAcceleratorZone(self) -> AcceleratorZoneRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getAcceleratorZone`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`
        
            Returns:
                The value of the :code:`acceleratorZone` attribute
        
        
        """
        ...
    def getDescription(self) -> str: ...
    def getDeviceAlias(self) -> str: ...
    def getDeviceGroups(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersion(self) -> DeviceTypeVersionContainerRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getDeviceTypeVersion`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`
        
            Returns:
                The value of the :code:`deviceTypeVersion` attribute
        
        
        """
        ...
    def getFecName(self) -> str: ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`
        
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
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getPosition`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`
        
            Returns:
                The value of the :code:`position` attribute
        
        
        """
        ...
    def getServerName(self) -> str: ...
    def getSortOrder(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getSortOrder`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`
        
            Returns:
                The value of the :code:`sortOrder` attribute
        
        
        """
        ...
    def getState(self) -> DeviceStateRest: ...
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
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.isCycleBound`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`
        
            Returns:
                The value of the :code:`cycleBound` attribute
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.isMultiplexed`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`
        
            Returns:
                The value of the :code:`multiplexed` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`DeviceRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAcceleratorZone(self, acceleratorZoneRest: AcceleratorZoneRest) -> 'DefaultDeviceRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getAcceleratorZone` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.AcceleratorZoneRest`): A new value for acceleratorZone
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withCycleBound(self, boolean: bool) -> 'DefaultDeviceRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.isCycleBound` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for cycleBound
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDescription(self, string: str) -> 'DefaultDeviceRest': ...
    def withDeviceAlias(self, string: str) -> 'DefaultDeviceRest': ...
    @typing.overload
    def withDeviceGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultDeviceRest': ...
    @typing.overload
    def withDeviceGroups(self, stringArray: typing.List[str]) -> 'DefaultDeviceRest': ...
    def withDeviceTypeVersion(self, deviceTypeVersionContainerRest: DeviceTypeVersionContainerRest) -> 'DefaultDeviceRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getDeviceTypeVersion` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest`): A new value for deviceTypeVersion
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withFecName(self, string: str) -> 'DefaultDeviceRest': ...
    def withId(self, long: int) -> 'DefaultDeviceRest':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getId`
            attribute. A value equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultDeviceRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.isMultiplexed` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for multiplexed
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultDeviceRest':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPosition(self, double: float) -> 'DefaultDeviceRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getPosition` attribute. A value strict bits equality used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (double): A new value for position
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withServerName(self, string: str) -> 'DefaultDeviceRest': ...
    def withSortOrder(self, int: int) -> 'DefaultDeviceRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceRest.getSortOrder` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (int): A new value for sortOrder
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withState(self, deviceStateRest: DeviceStateRest) -> 'DefaultDeviceRest': ...
    class Builder:
        def acceleratorZone(self, acceleratorZoneRest: AcceleratorZoneRest) -> 'DefaultDeviceRest.Builder': ...
        def addAllDeviceGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultDeviceRest.Builder': ...
        def addDeviceGroup(self, string: str) -> 'DefaultDeviceRest.Builder': ...
        def addDeviceGroups(self, stringArray: typing.List[str]) -> 'DefaultDeviceRest.Builder': ...
        def build(self) -> 'DefaultDeviceRest': ...
        def cycleBound(self, boolean: bool) -> 'DefaultDeviceRest.Builder': ...
        def description(self, string: str) -> 'DefaultDeviceRest.Builder': ...
        def deviceAlias(self, string: str) -> 'DefaultDeviceRest.Builder': ...
        def deviceGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultDeviceRest.Builder': ...
        def deviceTypeVersion(self, deviceTypeVersionContainerRest: DeviceTypeVersionContainerRest) -> 'DefaultDeviceRest.Builder': ...
        def fecName(self, string: str) -> 'DefaultDeviceRest.Builder': ...
        def id(self, long: int) -> 'DefaultDeviceRest.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultDeviceRest.Builder': ...
        def name(self, string: str) -> 'DefaultDeviceRest.Builder': ...
        def position(self, double: float) -> 'DefaultDeviceRest.Builder': ...
        def serverName(self, string: str) -> 'DefaultDeviceRest.Builder': ...
        def sortOrder(self, int: int) -> 'DefaultDeviceRest.Builder': ...
        def state(self, deviceStateRest: DeviceStateRest) -> 'DefaultDeviceRest.Builder': ...

class DefaultDeviceStateRest(DeviceStateRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceStateRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceStateRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceStateRest`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceStateRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceStateRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceStateRest`.
        
            .. code-block: java
            
             DefaultDeviceStateRest.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultDeviceStateRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceStateRest: DeviceStateRest) -> 'DefaultDeviceStateRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceStateRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceStateRest`): The instance to copy
        
            Returns:
                A copied immutable DeviceStateRest instance
        
        
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
            Prints the immutable value :code:`DeviceStateRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultDeviceStateRest':
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
        def build(self) -> 'DefaultDeviceStateRest': ...
        def name(self, string: str) -> 'DefaultDeviceStateRest.Builder': ...

class DefaultDeviceTypeImplementationRest(DeviceTypeImplementationRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceTypeImplementationRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationRest`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceTypeImplementationRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeImplementationRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceTypeImplementationRest`.
        
            .. code-block: java
            
             DefaultDeviceTypeImplementationRest.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultDeviceTypeImplementationRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceTypeImplementationRest: DeviceTypeImplementationRest) -> 'DefaultDeviceTypeImplementationRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationRest` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationRest`): The instance to copy
        
            Returns:
                A copied immutable DeviceTypeImplementationRest instance
        
        
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
            Prints the immutable value :code:`DeviceTypeImplementationRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultDeviceTypeImplementationRest':
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
        def build(self) -> 'DefaultDeviceTypeImplementationRest': ...
        def name(self, string: str) -> 'DefaultDeviceTypeImplementationRest.Builder': ...

class DefaultDeviceTypeVersionContainerRest(DeviceTypeVersionContainerRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceTypeVersionContainerRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceTypeVersionContainerRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionContainerRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceTypeVersionContainerRest`.
        
            .. code-block: java
            
             DefaultDeviceTypeVersionContainerRest.builder()
                .name(String) // required name
                .description(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getDescription`
                .id(Long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getId`
                .metaType(cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getMetaType`
                .addOtherVersion|addAllOtherVersions(cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest) // :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getOtherVersions` elements
                .primaryVersion(cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getPrimaryVersion`
                .build();
             
        
            Returns:
                A new DefaultDeviceTypeVersionContainerRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceTypeVersionContainerRest: DeviceTypeVersionContainerRest) -> 'DefaultDeviceTypeVersionContainerRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest`): The instance to copy
        
            Returns:
                A copied immutable DeviceTypeVersionContainerRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDescription(self) -> str: ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getMetaType(self) -> DeviceMetaTypeRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getMetaType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest`
        
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
    def getOtherVersions(self) -> java.util.List[DeviceTypeVersionRest]: ...
    def getPrimaryVersion(self) -> DeviceTypeVersionRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getPrimaryVersion`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest`
        
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
            Prints the immutable value :code:`DeviceTypeVersionContainerRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDescription(self, string: str) -> 'DefaultDeviceTypeVersionContainerRest': ...
    def withId(self, long: int) -> 'DefaultDeviceTypeVersionContainerRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getId` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMetaType(self, deviceMetaTypeRest: DeviceMetaTypeRest) -> 'DefaultDeviceTypeVersionContainerRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getMetaType` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceMetaTypeRest`): A new value for metaType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultDeviceTypeVersionContainerRest':
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
    def withOtherVersions(self, deviceTypeVersionRestArray: typing.List[DeviceTypeVersionRest]) -> 'DefaultDeviceTypeVersionContainerRest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getOtherVersions`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceTypeVersionContainerRest` withOtherVersions (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getOtherVersions`. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest`> elements): An iterable of otherVersions elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withOtherVersions(self, iterable: java.lang.Iterable[DeviceTypeVersionRest]) -> 'DefaultDeviceTypeVersionContainerRest': ...
    def withPrimaryVersion(self, deviceTypeVersionRest: DeviceTypeVersionRest) -> 'DefaultDeviceTypeVersionContainerRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionContainerRest.getPrimaryVersion` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest`): A new value for primaryVersion
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllOtherVersions(self, iterable: java.lang.Iterable[DeviceTypeVersionRest]) -> 'DefaultDeviceTypeVersionContainerRest.Builder': ...
        def addOtherVersion(self, deviceTypeVersionRest: DeviceTypeVersionRest) -> 'DefaultDeviceTypeVersionContainerRest.Builder': ...
        def addOtherVersions(self, deviceTypeVersionRestArray: typing.List[DeviceTypeVersionRest]) -> 'DefaultDeviceTypeVersionContainerRest.Builder': ...
        def build(self) -> 'DefaultDeviceTypeVersionContainerRest': ...
        def description(self, string: str) -> 'DefaultDeviceTypeVersionContainerRest.Builder': ...
        def id(self, long: int) -> 'DefaultDeviceTypeVersionContainerRest.Builder': ...
        def metaType(self, deviceMetaTypeRest: DeviceMetaTypeRest) -> 'DefaultDeviceTypeVersionContainerRest.Builder': ...
        def name(self, string: str) -> 'DefaultDeviceTypeVersionContainerRest.Builder': ...
        def otherVersions(self, iterable: java.lang.Iterable[DeviceTypeVersionRest]) -> 'DefaultDeviceTypeVersionContainerRest.Builder': ...
        def primaryVersion(self, deviceTypeVersionRest: DeviceTypeVersionRest) -> 'DefaultDeviceTypeVersionContainerRest.Builder': ...

class DefaultDeviceTypeVersionNumberRest(DeviceTypeVersionNumberRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceTypeVersionNumberRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceTypeVersionNumberRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionNumberRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceTypeVersionNumberRest`.
        
            .. code-block: java
            
             DefaultDeviceTypeVersionNumberRest.builder()
                .major(Integer) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest.getMajor`
                .minor(Integer) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest.getMinor`
                .build();
             
        
            Returns:
                A new DefaultDeviceTypeVersionNumberRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceTypeVersionNumberRest: DeviceTypeVersionNumberRest) -> 'DefaultDeviceTypeVersionNumberRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest`): The instance to copy
        
            Returns:
                A copied immutable DeviceTypeVersionNumberRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMajor(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest.getMajor`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest`
        
            Returns:
                The value of the :code:`major` attribute
        
        
        """
        ...
    def getMinor(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest.getMinor`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest`
        
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
            Prints the immutable value :code:`DeviceTypeVersionNumberRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withMajor(self, integer: int) -> 'DefaultDeviceTypeVersionNumberRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest.getMajor` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): A new value for major
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMinor(self, integer: int) -> 'DefaultDeviceTypeVersionNumberRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest.getMinor` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): A new value for minor
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultDeviceTypeVersionNumberRest': ...
        def major(self, integer: int) -> 'DefaultDeviceTypeVersionNumberRest.Builder': ...
        def minor(self, integer: int) -> 'DefaultDeviceTypeVersionNumberRest.Builder': ...

class DefaultDeviceTypeVersionRest(DeviceTypeVersionRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceTypeVersionRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceTypeVersionRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceTypeVersionRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultDeviceTypeVersionRest`.
        
            .. code-block: java
            
             DefaultDeviceTypeVersionRest.builder()
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest.getId`
                .implementation(cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest.getImplementation`
                .versionNumber(cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest.getVersionNumber`
                .build();
             
        
            Returns:
                A new DefaultDeviceTypeVersionRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceTypeVersionRest: DeviceTypeVersionRest) -> 'DefaultDeviceTypeVersionRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest`): The instance to copy
        
            Returns:
                A copied immutable DeviceTypeVersionRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getImplementation(self) -> DeviceTypeImplementationRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest.getImplementation`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest`
        
            Returns:
                The value of the :code:`implementation` attribute
        
        
        """
        ...
    def getVersionNumber(self) -> DeviceTypeVersionNumberRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest.getVersionNumber`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest`
        
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
            Prints the immutable value :code:`DeviceTypeVersionRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultDeviceTypeVersionRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest.getId` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withImplementation(self, deviceTypeImplementationRest: DeviceTypeImplementationRest) -> 'DefaultDeviceTypeVersionRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest.getImplementation` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeImplementationRest`): A new value for implementation
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withVersionNumber(self, deviceTypeVersionNumberRest: DeviceTypeVersionNumberRest) -> 'DefaultDeviceTypeVersionRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionRest.getVersionNumber` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceTypeVersionNumberRest`): A new value for versionNumber
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultDeviceTypeVersionRest': ...
        def id(self, long: int) -> 'DefaultDeviceTypeVersionRest.Builder': ...
        def implementation(self, deviceTypeImplementationRest: DeviceTypeImplementationRest) -> 'DefaultDeviceTypeVersionRest.Builder': ...
        def versionNumber(self, deviceTypeVersionNumberRest: DeviceTypeVersionNumberRest) -> 'DefaultDeviceTypeVersionRest.Builder': ...

class DefaultEnumItemRest(EnumItemRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultEnumItemRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest`.
    
        Use the builder to create immutable instances: :code:`DefaultEnumItemRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultEnumItemRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultEnumItemRest`.
        
            .. code-block: java
            
             DefaultEnumItemRest.builder()
                .code(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.getCode`
                .symbol(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.getSymbol`
                .standardMeaning(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.getStandardMeaning`
                .settable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.isSettable`
                .build();
             
        
            Returns:
                A new DefaultEnumItemRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(enumItemRest: EnumItemRest) -> 'DefaultEnumItemRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest`): The instance to copy
        
            Returns:
                A copied immutable EnumItemRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getCode(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.getCode`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest`
        
            Returns:
                The value of the :code:`code` attribute
        
        
        """
        ...
    def getStandardMeaning(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.getStandardMeaning`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest`
        
            Returns:
                The value of the :code:`standardMeaning` attribute
        
        
        """
        ...
    def getSymbol(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.getSymbol`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest`
        
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
                :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.isSettable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest`
        
            Returns:
                The value of the :code:`settable` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`EnumItemRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withCode(self, long: int) -> 'DefaultEnumItemRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.getCode` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for code
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withSettable(self, boolean: bool) -> 'DefaultEnumItemRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.isSettable` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for settable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withStandardMeaning(self, string: str) -> 'DefaultEnumItemRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.getStandardMeaning` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for standardMeaning
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withSymbol(self, string: str) -> 'DefaultEnumItemRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest.getSymbol` attribute. An equals check used to prevent copying of
            the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for symbol
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultEnumItemRest': ...
        def code(self, long: int) -> 'DefaultEnumItemRest.Builder': ...
        def settable(self, boolean: bool) -> 'DefaultEnumItemRest.Builder': ...
        def standardMeaning(self, string: str) -> 'DefaultEnumItemRest.Builder': ...
        def symbol(self, string: str) -> 'DefaultEnumItemRest.Builder': ...

class DefaultEnumTypeRest(EnumTypeRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultEnumTypeRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest`.
    
        Use the builder to create immutable instances: :code:`DefaultEnumTypeRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultEnumTypeRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultEnumTypeRest`.
        
            .. code-block: java
            
             DefaultEnumTypeRest.builder()
                .name(String) // required name
                .enumTypeBitSize(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest.getEnumTypeBitSize`
                .addEnumItem|addAllEnumItems(cern.lsa.client.rest.api.v1.dto.EnumItemRest) // :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest.getEnumItems` elements
                .build();
             
        
            Returns:
                A new DefaultEnumTypeRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(enumTypeRest: EnumTypeRest) -> 'DefaultEnumTypeRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest`): The instance to copy
        
            Returns:
                A copied immutable EnumTypeRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getEnumItems(self) -> java.util.List[EnumItemRest]: ...
    def getEnumTypeBitSize(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest.getEnumTypeBitSize`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest`
        
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
            Prints the immutable value :code:`EnumTypeRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withEnumItems(self, enumItemRestArray: typing.List[EnumItemRest]) -> 'DefaultEnumTypeRest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest.getEnumItems`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultEnumTypeRest` withEnumItems (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest.getEnumItems`. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.EnumItemRest`> elements): An iterable of enumItems elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withEnumItems(self, iterable: java.lang.Iterable[EnumItemRest]) -> 'DefaultEnumTypeRest': ...
    def withEnumTypeBitSize(self, string: str) -> 'DefaultEnumTypeRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.EnumTypeRest.getEnumTypeBitSize` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for enumTypeBitSize
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultEnumTypeRest':
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
        def addAllEnumItems(self, iterable: java.lang.Iterable[EnumItemRest]) -> 'DefaultEnumTypeRest.Builder': ...
        def addEnumItem(self, enumItemRest: EnumItemRest) -> 'DefaultEnumTypeRest.Builder': ...
        def addEnumItems(self, enumItemRestArray: typing.List[EnumItemRest]) -> 'DefaultEnumTypeRest.Builder': ...
        def build(self) -> 'DefaultEnumTypeRest': ...
        def enumItems(self, iterable: java.lang.Iterable[EnumItemRest]) -> 'DefaultEnumTypeRest.Builder': ...
        def enumTypeBitSize(self, string: str) -> 'DefaultEnumTypeRest.Builder': ...
        def name(self, string: str) -> 'DefaultEnumTypeRest.Builder': ...

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

class DefaultIncaPropertyFieldInfoRest(IncaPropertyFieldInfoRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultIncaPropertyFieldInfoRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest`.
    
        Use the builder to create immutable instances: :code:`DefaultIncaPropertyFieldInfoRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfoRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultIncaPropertyFieldInfoRest`.
        
            .. code-block: java
            
             DefaultIncaPropertyFieldInfoRest.builder()
                .propertyFieldRest(cern.lsa.client.rest.api.v1.dto.PropertyFieldRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.getPropertyFieldRest`
                .displayName(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.getDisplayName`
                .mainStatus(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.isMainStatus`
                .associatedPropertyFieldRest(cern.lsa.client.rest.api.v1.dto.PropertyFieldRest | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.getAssociatedPropertyFieldRest`
                .controlWarningMessage(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.getControlWarningMessage`
                .parameterValueCompareType(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.getParameterValueCompareType`
                .displayFormat(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.getDisplayFormat`
                .build();
             
        
            Returns:
                A new DefaultIncaPropertyFieldInfoRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(incaPropertyFieldInfoRest: IncaPropertyFieldInfoRest) -> 'DefaultIncaPropertyFieldInfoRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest`): The instance to copy
        
            Returns:
                A copied immutable IncaPropertyFieldInfoRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAssociatedPropertyFieldRest(self) -> PropertyFieldRest: ...
    def getControlWarningMessage(self) -> str: ...
    def getDisplayFormat(self) -> str: ...
    def getDisplayName(self) -> str: ...
    def getParameterValueCompareType(self) -> str:
        """
            Returns the comparison type that should be applied for this parameter type when calculating value status.
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.getParameterValueCompareType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest`
        
            Returns:
                type of parameter value comparison
        
        
        """
        ...
    def getPropertyFieldRest(self) -> PropertyFieldRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.getPropertyFieldRest`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest`
        
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
                :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.isMainStatus`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest`
        
            Returns:
                :code:`true` if this parameter type represents the main status property field
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`IncaPropertyFieldInfoRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAssociatedPropertyFieldRest(self, propertyFieldRest: PropertyFieldRest) -> 'DefaultIncaPropertyFieldInfoRest': ...
    def withControlWarningMessage(self, string: str) -> 'DefaultIncaPropertyFieldInfoRest': ...
    def withDisplayFormat(self, string: str) -> 'DefaultIncaPropertyFieldInfoRest': ...
    def withDisplayName(self, string: str) -> 'DefaultIncaPropertyFieldInfoRest': ...
    def withMainStatus(self, boolean: bool) -> 'DefaultIncaPropertyFieldInfoRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.isMainStatus` attribute. A value equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for mainStatus
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParameterValueCompareType(self, string: str) -> 'DefaultIncaPropertyFieldInfoRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.getParameterValueCompareType` attribute. An equals
            check used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for parameterValueCompareType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyFieldRest(self, propertyFieldRest: PropertyFieldRest) -> 'DefaultIncaPropertyFieldInfoRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest.getPropertyFieldRest` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest`): A new value for propertyFieldRest
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def associatedPropertyFieldRest(self, propertyFieldRest: PropertyFieldRest) -> 'DefaultIncaPropertyFieldInfoRest.Builder': ...
        def build(self) -> 'DefaultIncaPropertyFieldInfoRest': ...
        def controlWarningMessage(self, string: str) -> 'DefaultIncaPropertyFieldInfoRest.Builder': ...
        def displayFormat(self, string: str) -> 'DefaultIncaPropertyFieldInfoRest.Builder': ...
        def displayName(self, string: str) -> 'DefaultIncaPropertyFieldInfoRest.Builder': ...
        def mainStatus(self, boolean: bool) -> 'DefaultIncaPropertyFieldInfoRest.Builder': ...
        def parameterValueCompareType(self, string: str) -> 'DefaultIncaPropertyFieldInfoRest.Builder': ...
        def propertyFieldRest(self, propertyFieldRest: PropertyFieldRest) -> 'DefaultIncaPropertyFieldInfoRest.Builder': ...

class DefaultIncaPropertyFieldInfosRequestRest(IncaPropertyFieldInfosRequestRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultIncaPropertyFieldInfosRequestRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestRest`.
    
        Use the builder to create immutable instances: :code:`DefaultIncaPropertyFieldInfosRequestRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfosRequestRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultIncaPropertyFieldInfosRequestRest`.
        
            .. code-block: java
            
             DefaultIncaPropertyFieldInfosRequestRest.builder()
                .addPropertyFieldId|addAllPropertyFieldIds(long) // :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestRest.getPropertyFieldIds` elements
                .build();
             
        
            Returns:
                A new DefaultIncaPropertyFieldInfosRequestRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(incaPropertyFieldInfosRequestRest: IncaPropertyFieldInfosRequestRest) -> 'DefaultIncaPropertyFieldInfosRequestRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestRest` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestRest`): The instance to copy
        
            Returns:
                A copied immutable IncaPropertyFieldInfosRequestRest instance
        
        
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
            Prints the immutable value :code:`IncaPropertyFieldInfosRequestRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withPropertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultIncaPropertyFieldInfosRequestRest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestRest.getPropertyFieldIds`.
        
            Parameters:
                elements (long...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultIncaPropertyFieldInfosRequestRest` withPropertyFieldIds (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestRest.getPropertyFieldIds`. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements): An iterable of propertyFieldIds elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withPropertyFieldIds(self, longArray: typing.List[int]) -> 'DefaultIncaPropertyFieldInfosRequestRest': ...
    class Builder:
        def addAllPropertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultIncaPropertyFieldInfosRequestRest.Builder': ...
        def addPropertyFieldId(self, long: int) -> 'DefaultIncaPropertyFieldInfosRequestRest.Builder': ...
        def addPropertyFieldIds(self, longArray: typing.List[int]) -> 'DefaultIncaPropertyFieldInfosRequestRest.Builder': ...
        def build(self) -> 'DefaultIncaPropertyFieldInfosRequestRest': ...
        def propertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultIncaPropertyFieldInfosRequestRest.Builder': ...

class DefaultMakeRuleClassInfoRest(MakeRuleClassInfoRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleClassInfoRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleClassInfoRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleClassInfoRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultMakeRuleClassInfoRest`.
        
            .. code-block: java
            
             DefaultMakeRuleClassInfoRest.builder()
                .className(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest.getClassName`
                .productName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest.getProductName`
                .version(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest.getVersion`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleClassInfoRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleClassInfoRest: MakeRuleClassInfoRest) -> 'DefaultMakeRuleClassInfoRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleClassInfoRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getClassName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest.getClassName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest`
        
            Returns:
                The value of the :code:`className` attribute
        
        
        """
        ...
    def getProductName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest.getProductName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest`
        
            Returns:
                The value of the :code:`productName` attribute
        
        
        """
        ...
    def getVersion(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest.getVersion`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest`
        
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
            Prints the immutable value :code:`MakeRuleClassInfoRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withClassName(self, string: str) -> 'DefaultMakeRuleClassInfoRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest.getClassName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for className
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withProductName(self, string: str) -> 'DefaultMakeRuleClassInfoRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest.getProductName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for productName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withVersion(self, string: str) -> 'DefaultMakeRuleClassInfoRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest.getVersion` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for version
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleClassInfoRest': ...
        def className(self, string: str) -> 'DefaultMakeRuleClassInfoRest.Builder': ...
        def productName(self, string: str) -> 'DefaultMakeRuleClassInfoRest.Builder': ...
        def version(self, string: str) -> 'DefaultMakeRuleClassInfoRest.Builder': ...

class DefaultMakeRuleConfigInfoRest(MakeRuleConfigInfoRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleConfigInfoRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoRest`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleConfigInfoRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigInfoRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultMakeRuleConfigInfoRest`.
        
            .. code-block: java
            
             DefaultMakeRuleConfigInfoRest.builder()
                .makeRuleConfigStatus(cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoRest.getMakeRuleConfigStatus`
                .makeRuleInfo(cern.lsa.client.rest.api.v1.dto.MakeRuleInfoRest | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoRest.getMakeRuleInfo`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleConfigInfoRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleConfigInfoRest: MakeRuleConfigInfoRest) -> 'DefaultMakeRuleConfigInfoRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoRest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoRest`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleConfigInfoRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMakeRuleConfigStatus(self) -> MakeRuleConfigStatusRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoRest.getMakeRuleConfigStatus`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoRest`
        
            Returns:
                The value of the :code:`makeRuleConfigStatus` attribute
        
        
        """
        ...
    def getMakeRuleInfo(self) -> MakeRuleInfoRest: ...
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
            Prints the immutable value :code:`MakeRuleConfigInfoRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withMakeRuleConfigStatus(self, makeRuleConfigStatusRest: MakeRuleConfigStatusRest) -> 'DefaultMakeRuleConfigInfoRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoRest.getMakeRuleConfigStatus` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusRest`): A new value for makeRuleConfigStatus
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMakeRuleInfo(self, makeRuleInfoRest: MakeRuleInfoRest) -> 'DefaultMakeRuleConfigInfoRest': ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleConfigInfoRest': ...
        def makeRuleConfigStatus(self, makeRuleConfigStatusRest: MakeRuleConfigStatusRest) -> 'DefaultMakeRuleConfigInfoRest.Builder': ...
        def makeRuleInfo(self, makeRuleInfoRest: MakeRuleInfoRest) -> 'DefaultMakeRuleConfigInfoRest.Builder': ...

class DefaultMakeRuleConfigStatusRest(MakeRuleConfigStatusRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleConfigStatusRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusRest`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleConfigStatusRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigStatusRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultMakeRuleConfigStatusRest`.
        
            .. code-block: java
            
             DefaultMakeRuleConfigStatusRest.builder()
                .name(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusRest.getName`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleConfigStatusRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleConfigStatusRest: MakeRuleConfigStatusRest) -> 'DefaultMakeRuleConfigStatusRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusRest` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusRest`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleConfigStatusRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusRest.getName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusRest`
        
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
            Prints the immutable value :code:`MakeRuleConfigStatusRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultMakeRuleConfigStatusRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleConfigStatusRest.getName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleConfigStatusRest': ...
        def name(self, string: str) -> 'DefaultMakeRuleConfigStatusRest.Builder': ...

class DefaultMakeRuleInfoRest(MakeRuleInfoRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleInfoRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoRest`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleInfoRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleInfoRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultMakeRuleInfoRest`.
        
            .. code-block: java
            
             DefaultMakeRuleInfoRest.builder()
                .makeRuleClassInfo(cern.lsa.client.rest.api.v1.dto.MakeRuleClassInfoRest | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoRest.getMakeRuleClassInfo`
                .makeRuleName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoRest.getMakeRuleName`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleInfoRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleInfoRest: MakeRuleInfoRest) -> 'DefaultMakeRuleInfoRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoRest`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleInfoRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMakeRuleClassInfo(self) -> MakeRuleClassInfoRest: ...
    def getMakeRuleName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoRest.getMakeRuleName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoRest`
        
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
            Prints the immutable value :code:`MakeRuleInfoRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withMakeRuleClassInfo(self, makeRuleClassInfoRest: MakeRuleClassInfoRest) -> 'DefaultMakeRuleInfoRest': ...
    def withMakeRuleName(self, string: str) -> 'DefaultMakeRuleInfoRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.MakeRuleInfoRest.getMakeRuleName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for makeRuleName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleInfoRest': ...
        def makeRuleClassInfo(self, makeRuleClassInfoRest: MakeRuleClassInfoRest) -> 'DefaultMakeRuleInfoRest.Builder': ...
        def makeRuleName(self, string: str) -> 'DefaultMakeRuleInfoRest.Builder': ...

class DefaultParameterAttributesRest(ParameterAttributesRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterAttributesRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterAttributesRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterAttributesRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterAttributesRest`.
        
            .. code-block: java
            
             DefaultParameterAttributesRest.builder()
                .absoluteTolerance(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getAbsoluteTolerance`
                .belongsToFunctionBProc(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.isBelongsToFunctionBProc`
                .defaultHierarchy(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getDefaultHierarchy`
                .device(cern.lsa.client.rest.api.v1.dto.DeviceRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getDevice`
                .propertyField(cern.lsa.client.rest.api.v1.dto.PropertyFieldRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getPropertyField`
                .maxValue(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getMaxValue`
                .minValue(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getMinValue`
                .parameterId(Long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getParameterId`
                .parameterName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getParameterName`
                .parameterType(cern.lsa.client.rest.api.v1.dto.ParameterTypeRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getParameterType`
                .relativeTolerance(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getRelativeTolerance`
                .reservedForOpExperts(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.isReservedForOpExperts`
                .trimable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.isTrimable`
                .xPrecision(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getXPrecision`
                .yPrecision(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getYPrecision`
                .build();
             
        
            Returns:
                A new DefaultParameterAttributesRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterAttributesRest: ParameterAttributesRest) -> 'DefaultParameterAttributesRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`): The instance to copy
        
            Returns:
                A copied immutable ParameterAttributesRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAbsoluteTolerance(self) -> float: ...
    def getDefaultHierarchy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getDefaultHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`
        
            Returns:
                The value of the :code:`defaultHierarchy` attribute
        
        
        """
        ...
    def getDevice(self) -> DeviceRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getDevice`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`
        
            Returns:
                The value of the :code:`device` attribute
        
        
        """
        ...
    def getMaxValue(self) -> float: ...
    def getMinValue(self) -> float: ...
    def getParameterId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getParameterId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`
        
            Returns:
                The value of the :code:`parameterId` attribute
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getParameterName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`
        
            Returns:
                The value of the :code:`parameterName` attribute
        
        
        """
        ...
    def getParameterType(self) -> ParameterTypeRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getParameterType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`
        
            Returns:
                The value of the :code:`parameterType` attribute
        
        
        """
        ...
    def getPropertyField(self) -> PropertyFieldRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getPropertyField`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`
        
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
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.isBelongsToFunctionBProc`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`
        
            Returns:
                The value of the :code:`belongsToFunctionBProc` attribute
        
        
        """
        ...
    def isReservedForOpExperts(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.isReservedForOpExperts`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`
        
            Returns:
                The value of the :code:`reservedForOpExperts` attribute
        
        
        """
        ...
    def isTrimable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.isTrimable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest`
        
            Returns:
                The value of the :code:`trimable` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterAttributesRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAbsoluteTolerance(self, double: float) -> 'DefaultParameterAttributesRest': ...
    def withBelongsToFunctionBProc(self, boolean: bool) -> 'DefaultParameterAttributesRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.isBelongsToFunctionBProc` attribute. A value equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for belongsToFunctionBProc
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDefaultHierarchy(self, string: str) -> 'DefaultParameterAttributesRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getDefaultHierarchy` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for defaultHierarchy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDevice(self, deviceRest: DeviceRest) -> 'DefaultParameterAttributesRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getDevice` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`): A new value for device
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMaxValue(self, double: float) -> 'DefaultParameterAttributesRest': ...
    def withMinValue(self, double: float) -> 'DefaultParameterAttributesRest': ...
    def withParameterId(self, long: int) -> 'DefaultParameterAttributesRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getParameterId` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`): A new value for parameterId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParameterName(self, string: str) -> 'DefaultParameterAttributesRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getParameterName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for parameterName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParameterType(self, parameterTypeRest: ParameterTypeRest) -> 'DefaultParameterAttributesRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getParameterType` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest`): A new value for parameterType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyField(self, propertyFieldRest: PropertyFieldRest) -> 'DefaultParameterAttributesRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.getPropertyField` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest`): A new value for propertyField
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withRelativeTolerance(self, double: float) -> 'DefaultParameterAttributesRest': ...
    def withReservedForOpExperts(self, boolean: bool) -> 'DefaultParameterAttributesRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.isReservedForOpExperts` attribute. A value equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for reservedForOpExperts
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTrimable(self, boolean: bool) -> 'DefaultParameterAttributesRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest.isTrimable` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for trimable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withXPrecision(self, integer: int) -> 'DefaultParameterAttributesRest': ...
    def withYPrecision(self, integer: int) -> 'DefaultParameterAttributesRest': ...
    class Builder:
        def absoluteTolerance(self, double: float) -> 'DefaultParameterAttributesRest.Builder': ...
        def belongsToFunctionBProc(self, boolean: bool) -> 'DefaultParameterAttributesRest.Builder': ...
        def build(self) -> 'DefaultParameterAttributesRest': ...
        def defaultHierarchy(self, string: str) -> 'DefaultParameterAttributesRest.Builder': ...
        def device(self, deviceRest: DeviceRest) -> 'DefaultParameterAttributesRest.Builder': ...
        def maxValue(self, double: float) -> 'DefaultParameterAttributesRest.Builder': ...
        def minValue(self, double: float) -> 'DefaultParameterAttributesRest.Builder': ...
        def parameterId(self, long: int) -> 'DefaultParameterAttributesRest.Builder': ...
        def parameterName(self, string: str) -> 'DefaultParameterAttributesRest.Builder': ...
        def parameterType(self, parameterTypeRest: ParameterTypeRest) -> 'DefaultParameterAttributesRest.Builder': ...
        def propertyField(self, propertyFieldRest: PropertyFieldRest) -> 'DefaultParameterAttributesRest.Builder': ...
        def relativeTolerance(self, double: float) -> 'DefaultParameterAttributesRest.Builder': ...
        def reservedForOpExperts(self, boolean: bool) -> 'DefaultParameterAttributesRest.Builder': ...
        def trimable(self, boolean: bool) -> 'DefaultParameterAttributesRest.Builder': ...
        def xPrecision(self, integer: int) -> 'DefaultParameterAttributesRest.Builder': ...
        def yPrecision(self, integer: int) -> 'DefaultParameterAttributesRest.Builder': ...

class DefaultParameterGroupRest(ParameterGroupRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterGroupRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterGroupRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterGroupRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterGroupRest`.
        
            .. code-block: java
            
             DefaultParameterGroupRest.builder()
                .name(String) // required name
                .acceleratorName(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest.getAcceleratorName`
                .createDate(java.time.OffsetDateTime) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest.getCreateDate`
                .creator(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest.getCreator`
                .description(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest.getDescription`
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest.getId`
                .build();
             
        
            Returns:
                A new DefaultParameterGroupRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterGroupRest: ParameterGroupRest) -> 'DefaultParameterGroupRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest`): The instance to copy
        
            Returns:
                A copied immutable ParameterGroupRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAcceleratorName(self) -> str: ...
    def getCreateDate(self) -> java.time.OffsetDateTime:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest.getCreateDate`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest`
        
            Returns:
                The value of the :code:`createDate` attribute
        
        
        """
        ...
    def getCreator(self) -> str: ...
    def getDescription(self) -> str: ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest`
        
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
            Prints the immutable value :code:`ParameterGroupRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAcceleratorName(self, string: str) -> 'DefaultParameterGroupRest': ...
    def withCreateDate(self, offsetDateTime: java.time.OffsetDateTime) -> 'DefaultParameterGroupRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest.getCreateDate` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`OffsetDateTime <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/OffsetDateTime.html?is-external=true>`): A new value for createDate
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withCreator(self, string: str) -> 'DefaultParameterGroupRest': ...
    def withDescription(self, string: str) -> 'DefaultParameterGroupRest': ...
    def withId(self, long: int) -> 'DefaultParameterGroupRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterGroupRest.getId` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultParameterGroupRest':
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
        def acceleratorName(self, string: str) -> 'DefaultParameterGroupRest.Builder': ...
        def build(self) -> 'DefaultParameterGroupRest': ...
        def createDate(self, offsetDateTime: java.time.OffsetDateTime) -> 'DefaultParameterGroupRest.Builder': ...
        def creator(self, string: str) -> 'DefaultParameterGroupRest.Builder': ...
        def description(self, string: str) -> 'DefaultParameterGroupRest.Builder': ...
        def id(self, long: int) -> 'DefaultParameterGroupRest.Builder': ...
        def name(self, string: str) -> 'DefaultParameterGroupRest.Builder': ...

class DefaultParameterRest(ParameterRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterRest.builder()`.
    """
    def belongsToFunctionBeamProcess(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.belongsToFunctionBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`belongsToFunctionBeamProcess` attribute
        
        
        """
        ...
    @staticmethod
    def builder() -> 'DefaultParameterRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterRest`.
        
            .. code-block: java
            
             DefaultParameterRest.builder()
                .name(String) // required name
                .belongsToFunctionBeamProcess(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.belongsToFunctionBeamProcess`
                .critical(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isCritical`
                .defaultHierarchy(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getDefaultHierarchy`
                .device(cern.lsa.client.rest.api.v1.dto.DeviceRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getDevice`
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getId`
                .monitorable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isMonitorable`
                .multiplexed(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isMultiplexed`
                .cycleBound(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isCycleBound`
                .addParameterGroup|addAllParameterGroups(String) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getParameterGroups` elements
                .parameterType(cern.lsa.client.rest.api.v1.dto.ParameterTypeRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getParameterType`
                .propertySupportingPartialSet(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isPropertySupportingPartialSet`
                .readable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isReadable`
                .reservedForOpExperts(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isReservedForOpExperts`
                .trimable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isTrimable`
                .valueDescriptor(cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getValueDescriptor`
                .valueType(cern.lsa.client.rest.api.v1.dto.TypeRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getValueType`
                .lsaImplementation(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isLsaImplementation`
                .writable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isWritable`
                .propertyField(cern.lsa.client.rest.api.v1.dto.PropertyFieldRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getPropertyField`
                .build();
             
        
            Returns:
                A new DefaultParameterRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterRest: ParameterRest) -> 'DefaultParameterRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`): The instance to copy
        
            Returns:
                A copied immutable ParameterRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDefaultHierarchy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getDefaultHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`defaultHierarchy` attribute
        
        
        """
        ...
    def getDevice(self) -> DeviceRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getDevice`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`device` attribute
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
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
    def getParameterType(self) -> ParameterTypeRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getParameterType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`parameterType` attribute
        
        
        """
        ...
    def getPropertyField(self) -> PropertyFieldRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getPropertyField`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`propertyField` attribute
        
        
        """
        ...
    def getValueDescriptor(self) -> ValueDescriptorRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getValueDescriptor`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`valueDescriptor` attribute
        
        
        """
        ...
    def getValueType(self) -> TypeRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getValueType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
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
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isCritical`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`critical` attribute
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isCycleBound`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`cycleBound` attribute
        
        
        """
        ...
    def isLsaImplementation(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isLsaImplementation`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`lsaImplementation` attribute
        
        
        """
        ...
    def isMonitorable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isMonitorable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`monitorable` attribute
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isMultiplexed`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`multiplexed` attribute
        
        
        """
        ...
    def isPropertySupportingPartialSet(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isPropertySupportingPartialSet`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`propertySupportingPartialSet` attribute
        
        
        """
        ...
    def isReadable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isReadable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`readable` attribute
        
        
        """
        ...
    def isReservedForOpExperts(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isReservedForOpExperts`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`reservedForOpExperts` attribute
        
        
        """
        ...
    def isTrimable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isTrimable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`trimable` attribute
        
        
        """
        ...
    def isWritable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isWritable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`
        
            Returns:
                The value of the :code:`writable` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withBelongsToFunctionBeamProcess(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.belongsToFunctionBeamProcess` attribute. A value equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for belongsToFunctionBeamProcess
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withCritical(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isCritical` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for critical
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withCycleBound(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isCycleBound` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for cycleBound
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDefaultHierarchy(self, string: str) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getDefaultHierarchy` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for defaultHierarchy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDevice(self, deviceRest: DeviceRest) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getDevice` attribute. A shallow reference equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.DeviceRest`): A new value for device
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getId` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withLsaImplementation(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isLsaImplementation` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for lsaImplementation
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMonitorable(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isMonitorable` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for monitorable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isMultiplexed` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for multiplexed
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultParameterRest':
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
    def withParameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterRest': ...
    @typing.overload
    def withParameterGroups(self, stringArray: typing.List[str]) -> 'DefaultParameterRest': ...
    def withParameterType(self, parameterTypeRest: ParameterTypeRest) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getParameterType` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest`): A new value for parameterType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyField(self, propertyFieldRest: PropertyFieldRest) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getPropertyField` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest`): A new value for propertyField
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertySupportingPartialSet(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isPropertySupportingPartialSet` attribute. A value equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for propertySupportingPartialSet
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withReadable(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isReadable` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for readable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withReservedForOpExperts(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isReservedForOpExperts` attribute. A value equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for reservedForOpExperts
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTrimable(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isTrimable` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for trimable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withValueDescriptor(self, valueDescriptorRest: ValueDescriptorRest) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getValueDescriptor` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest`): A new value for valueDescriptor
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withValueType(self, typeRest: TypeRest) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.getValueType` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.TypeRest`): A new value for valueType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withWritable(self, boolean: bool) -> 'DefaultParameterRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterRest.isWritable` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for writable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllParameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterRest.Builder': ...
        def addParameterGroup(self, string: str) -> 'DefaultParameterRest.Builder': ...
        def addParameterGroups(self, stringArray: typing.List[str]) -> 'DefaultParameterRest.Builder': ...
        def belongsToFunctionBeamProcess(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...
        def build(self) -> 'DefaultParameterRest': ...
        def critical(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...
        def cycleBound(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...
        def defaultHierarchy(self, string: str) -> 'DefaultParameterRest.Builder': ...
        def device(self, deviceRest: DeviceRest) -> 'DefaultParameterRest.Builder': ...
        def id(self, long: int) -> 'DefaultParameterRest.Builder': ...
        def lsaImplementation(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...
        def monitorable(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...
        def name(self, string: str) -> 'DefaultParameterRest.Builder': ...
        def parameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterRest.Builder': ...
        def parameterType(self, parameterTypeRest: ParameterTypeRest) -> 'DefaultParameterRest.Builder': ...
        def propertyField(self, propertyFieldRest: PropertyFieldRest) -> 'DefaultParameterRest.Builder': ...
        def propertySupportingPartialSet(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...
        def readable(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...
        def reservedForOpExperts(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...
        def trimable(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...
        def valueDescriptor(self, valueDescriptorRest: ValueDescriptorRest) -> 'DefaultParameterRest.Builder': ...
        def valueType(self, typeRest: TypeRest) -> 'DefaultParameterRest.Builder': ...
        def writable(self, boolean: bool) -> 'DefaultParameterRest.Builder': ...

class DefaultParameterTreeDataRest(ParameterTreeDataRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTreeDataRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTreeDataRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeDataRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeDataRest`.
        
            .. code-block: java
            
             DefaultParameterTreeDataRest.builder()
                .addNode|addAllNodes(cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest.getNodes` elements
                .addRelation|addAllRelations(cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest.getRelations` elements
                .addStartNodeId|addAllStartNodeIds(long) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest.getStartNodeIds` elements
                .build();
             
        
            Returns:
                A new DefaultParameterTreeDataRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTreeDataRest: ParameterTreeDataRest) -> 'DefaultParameterTreeDataRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest`): The instance to copy
        
            Returns:
                A copied immutable ParameterTreeDataRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getNodes(self) -> java.util.Set[ParameterTreeNodeRest]: ...
    def getRelations(self) -> java.util.Set[ParameterTreeRelationRest]: ...
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
            Prints the immutable value :code:`ParameterTreeDataRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withNodes(self, parameterTreeNodeRestArray: typing.List[ParameterTreeNodeRest]) -> 'DefaultParameterTreeDataRest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest.getNodes`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeDataRest` withNodes (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest.getNodes`. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest`> elements): An iterable of nodes elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withNodes(self, iterable: java.lang.Iterable[ParameterTreeNodeRest]) -> 'DefaultParameterTreeDataRest': ...
    @typing.overload
    def withRelations(self, parameterTreeRelationRestArray: typing.List[ParameterTreeRelationRest]) -> 'DefaultParameterTreeDataRest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest.getRelations`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeDataRest` withRelations (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest.getRelations`. A shallow reference equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest`> elements): An iterable of relations elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withRelations(self, iterable: java.lang.Iterable[ParameterTreeRelationRest]) -> 'DefaultParameterTreeDataRest': ...
    @typing.overload
    def withStartNodeIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParameterTreeDataRest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest.getStartNodeIds`.
        
            Parameters:
                elements (long...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeDataRest` withStartNodeIds (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest.getStartNodeIds`. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements): An iterable of startNodeIds elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withStartNodeIds(self, longArray: typing.List[int]) -> 'DefaultParameterTreeDataRest': ...
    class Builder:
        def addAllNodes(self, iterable: java.lang.Iterable[ParameterTreeNodeRest]) -> 'DefaultParameterTreeDataRest.Builder': ...
        def addAllRelations(self, iterable: java.lang.Iterable[ParameterTreeRelationRest]) -> 'DefaultParameterTreeDataRest.Builder': ...
        def addAllStartNodeIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParameterTreeDataRest.Builder': ...
        def addNode(self, parameterTreeNodeRest: ParameterTreeNodeRest) -> 'DefaultParameterTreeDataRest.Builder': ...
        def addNodes(self, parameterTreeNodeRestArray: typing.List[ParameterTreeNodeRest]) -> 'DefaultParameterTreeDataRest.Builder': ...
        def addRelation(self, parameterTreeRelationRest: ParameterTreeRelationRest) -> 'DefaultParameterTreeDataRest.Builder': ...
        def addRelations(self, parameterTreeRelationRestArray: typing.List[ParameterTreeRelationRest]) -> 'DefaultParameterTreeDataRest.Builder': ...
        def addStartNodeId(self, long: int) -> 'DefaultParameterTreeDataRest.Builder': ...
        def addStartNodeIds(self, longArray: typing.List[int]) -> 'DefaultParameterTreeDataRest.Builder': ...
        def build(self) -> 'DefaultParameterTreeDataRest': ...
        def nodes(self, iterable: java.lang.Iterable[ParameterTreeNodeRest]) -> 'DefaultParameterTreeDataRest.Builder': ...
        def relations(self, iterable: java.lang.Iterable[ParameterTreeRelationRest]) -> 'DefaultParameterTreeDataRest.Builder': ...
        def startNodeIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParameterTreeDataRest.Builder': ...

class DefaultParameterTreeNodeRest(ParameterTreeNodeRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTreeNodeRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTreeNodeRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeNodeRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeNodeRest`.
        
            .. code-block: java
            
             DefaultParameterTreeNodeRest.builder()
                .parameter(cern.lsa.client.rest.api.v1.dto.ParameterRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest.getParameter`
                .source(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest.isSource`
                .build();
             
        
            Returns:
                A new DefaultParameterTreeNodeRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTreeNodeRest: ParameterTreeNodeRest) -> 'DefaultParameterTreeNodeRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest`): The instance to copy
        
            Returns:
                A copied immutable ParameterTreeNodeRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getParameter(self) -> ParameterRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest.getParameter`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest`
        
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
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest.isSource`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest`
        
            Returns:
                The value of the :code:`source` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTreeNodeRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withParameter(self, parameterRest: ParameterRest) -> 'DefaultParameterTreeNodeRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest.getParameter` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterRest`): A new value for parameter
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withSource(self, boolean: bool) -> 'DefaultParameterTreeNodeRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeNodeRest.isSource` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for source
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultParameterTreeNodeRest': ...
        def parameter(self, parameterRest: ParameterRest) -> 'DefaultParameterTreeNodeRest.Builder': ...
        def source(self, boolean: bool) -> 'DefaultParameterTreeNodeRest.Builder': ...

class DefaultParameterTreeRelationRest(ParameterTreeRelationRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTreeRelationRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTreeRelationRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreeRelationRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreeRelationRest`.
        
            .. code-block: java
            
             DefaultParameterTreeRelationRest.builder()
                .parentParameterId(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest.getParentParameterId`
                .childParameterId(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest.getChildParameterId`
                .build();
             
        
            Returns:
                A new DefaultParameterTreeRelationRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTreeRelationRest: ParameterTreeRelationRest) -> 'DefaultParameterTreeRelationRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest`): The instance to copy
        
            Returns:
                A copied immutable ParameterTreeRelationRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getChildParameterId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest.getChildParameterId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest`
        
            Returns:
                The value of the :code:`childParameterId` attribute
        
        
        """
        ...
    def getParentParameterId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest.getParentParameterId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest`
        
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
            Prints the immutable value :code:`ParameterTreeRelationRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withChildParameterId(self, long: int) -> 'DefaultParameterTreeRelationRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest.getChildParameterId` attribute. A value equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for childParameterId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParentParameterId(self, long: int) -> 'DefaultParameterTreeRelationRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreeRelationRest.getParentParameterId` attribute. A value equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for parentParameterId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultParameterTreeRelationRest': ...
        def childParameterId(self, long: int) -> 'DefaultParameterTreeRelationRest.Builder': ...
        def parentParameterId(self, long: int) -> 'DefaultParameterTreeRelationRest.Builder': ...

class DefaultParameterTreesRequestRest(ParameterTreesRequestRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTreesRequestRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTreesRequestRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTreesRequestRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTreesRequestRest`.
        
            .. code-block: java
            
             DefaultParameterTreesRequestRest.builder()
                .addParameterName|addAllParameterNames(String) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest.getParameterNames` elements
                .hierarchy(String) // optional :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest.getHierarchy`
                .treeDirection(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest.getTreeDirection`
                .build();
             
        
            Returns:
                A new DefaultParameterTreesRequestRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTreesRequestRest: ParameterTreesRequestRest) -> 'DefaultParameterTreesRequestRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest`): The instance to copy
        
            Returns:
                A copied immutable ParameterTreesRequestRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getHierarchy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest.getHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest`
        
            Returns:
                The value of the :code:`hierarchy` attribute
        
        
        """
        ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getTreeDirection(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest.getTreeDirection`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest`
        
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
            Prints the immutable value :code:`ParameterTreesRequestRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withHierarchy(self, string: str) -> 'DefaultParameterTreesRequestRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest.getHierarchy` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for hierarchy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTreesRequestRest': ...
    @typing.overload
    def withParameterNames(self, stringArray: typing.List[str]) -> 'DefaultParameterTreesRequestRest': ...
    def withTreeDirection(self, string: str) -> 'DefaultParameterTreesRequestRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest.getTreeDirection` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for treeDirection
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllParameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTreesRequestRest.Builder': ...
        def addParameterName(self, string: str) -> 'DefaultParameterTreesRequestRest.Builder': ...
        def addParameterNames(self, stringArray: typing.List[str]) -> 'DefaultParameterTreesRequestRest.Builder': ...
        def build(self) -> 'DefaultParameterTreesRequestRest': ...
        def hierarchy(self, string: str) -> 'DefaultParameterTreesRequestRest.Builder': ...
        def parameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTreesRequestRest.Builder': ...
        def treeDirection(self, string: str) -> 'DefaultParameterTreesRequestRest.Builder': ...

class DefaultParameterTypeCategoryRest(ParameterTypeCategoryRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTypeCategoryRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTypeCategoryRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeCategoryRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTypeCategoryRest`.
        
            .. code-block: java
            
             DefaultParameterTypeCategoryRest.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultParameterTypeCategoryRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTypeCategoryRest: ParameterTypeCategoryRest) -> 'DefaultParameterTypeCategoryRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryRest` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryRest`): The instance to copy
        
            Returns:
                A copied immutable ParameterTypeCategoryRest instance
        
        
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
            Prints the immutable value :code:`ParameterTypeCategoryRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultParameterTypeCategoryRest':
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
        def build(self) -> 'DefaultParameterTypeCategoryRest': ...
        def name(self, string: str) -> 'DefaultParameterTypeCategoryRest.Builder': ...

class DefaultParameterTypeRest(ParameterTypeRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTypeRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTypeRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTypeRest`.
        
            .. code-block: java
            
             DefaultParameterTypeRest.builder()
                .name(String) // required name
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest.getId`
                .linkRuleApplicable(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest.isLinkRuleApplicable`
                .category(cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryRest) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest.getCategory`
                .build();
             
        
            Returns:
                A new DefaultParameterTypeRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTypeRest: ParameterTypeRest) -> 'DefaultParameterTypeRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest`): The instance to copy
        
            Returns:
                A copied immutable ParameterTypeRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getCategory(self) -> ParameterTypeCategoryRest:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest.getCategory`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest`
        
            Returns:
                The value of the :code:`category` attribute
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest`
        
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
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest.isLinkRuleApplicable`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest`
        
            Returns:
                The value of the :code:`linkRuleApplicable` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTypeRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withCategory(self, parameterTypeCategoryRest: ParameterTypeCategoryRest) -> 'DefaultParameterTypeRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest.getCategory` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeCategoryRest`): A new value for category
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultParameterTypeRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest.getId` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withLinkRuleApplicable(self, boolean: bool) -> 'DefaultParameterTypeRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypeRest.isLinkRuleApplicable` attribute. A value equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for linkRuleApplicable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultParameterTypeRest':
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
        def build(self) -> 'DefaultParameterTypeRest': ...
        def category(self, parameterTypeCategoryRest: ParameterTypeCategoryRest) -> 'DefaultParameterTypeRest.Builder': ...
        def id(self, long: int) -> 'DefaultParameterTypeRest.Builder': ...
        def linkRuleApplicable(self, boolean: bool) -> 'DefaultParameterTypeRest.Builder': ...
        def name(self, string: str) -> 'DefaultParameterTypeRest.Builder': ...

class DefaultParameterTypesRequestRest(ParameterTypesRequestRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTypesRequestRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTypesRequestRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypesRequestRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParameterTypesRequestRest`.
        
            .. code-block: java
            
             DefaultParameterTypesRequestRest.builder()
                .addParameterTypeName|addAllParameterTypeNames(String) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestRest.getParameterTypeNames` elements
                .allParameterTypesRequested(boolean) // optional :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestRest.isAllParameterTypesRequested`
                .build();
             
        
            Returns:
                A new DefaultParameterTypesRequestRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTypesRequestRest: ParameterTypesRequestRest) -> 'DefaultParameterTypesRequestRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestRest` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestRest`): The instance to copy
        
            Returns:
                A copied immutable ParameterTypesRequestRest instance
        
        
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
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestRest.isAllParameterTypesRequested`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestRest`
        
            Returns:
                The value of the :code:`allParameterTypesRequested` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTypesRequestRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAllParameterTypesRequested(self, boolean: bool) -> 'DefaultParameterTypesRequestRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestRest.isAllParameterTypesRequested` attribute. A value
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for allParameterTypesRequested
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTypesRequestRest': ...
    @typing.overload
    def withParameterTypeNames(self, stringArray: typing.List[str]) -> 'DefaultParameterTypesRequestRest': ...
    class Builder:
        def addAllParameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTypesRequestRest.Builder': ...
        def addParameterTypeName(self, string: str) -> 'DefaultParameterTypesRequestRest.Builder': ...
        def addParameterTypeNames(self, stringArray: typing.List[str]) -> 'DefaultParameterTypesRequestRest.Builder': ...
        def allParameterTypesRequested(self, boolean: bool) -> 'DefaultParameterTypesRequestRest.Builder': ...
        def build(self) -> 'DefaultParameterTypesRequestRest': ...
        def parameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParameterTypesRequestRest.Builder': ...

class DefaultParametersRequestRest(ParametersRequestRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParametersRequestRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParametersRequestRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParametersRequestRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParametersRequestRest`.
        
            .. code-block: java
            
             DefaultParametersRequestRest.builder()
                .acceleratorName(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getAcceleratorName`
                .parameterNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getParameterNames`
                .propertyFieldIds(Set<Long> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getPropertyFieldIds`
                .acceleratorZoneNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getAcceleratorZoneNames`
                .particleTransferNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getParticleTransferNames`
                .parameterTypeNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getParameterTypeNames`
                .parameterGroups(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getParameterGroups`
                .deviceNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getDeviceNames`
                .deviceIds(Set<Long> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getDeviceIds`
                .propertyNames(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getPropertyNames`
                .multiplexed(Boolean | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.isMultiplexed`
                .lsaImplementation(Boolean | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.isLsaImplementation`
                .writable(Boolean | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.isWritable`
                .readable(Boolean | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.isReadable`
                .parameterNamePattern(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getParameterNamePattern`
                .critical(Boolean | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.isCritical`
                .valueTypes(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest.getValueTypes`
                .build();
             
        
            Returns:
                A new DefaultParametersRequestRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parametersRequestRest: ParametersRequestRest) -> 'DefaultParametersRequestRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParametersRequestRest`): The instance to copy
        
            Returns:
                A copied immutable ParametersRequestRest instance
        
        
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
            Prints the immutable value :code:`ParametersRequestRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAcceleratorName(self, string: str) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withAcceleratorZoneNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withAcceleratorZoneNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest': ...
    def withCritical(self, boolean: bool) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withDeviceIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withDeviceIds(self, longArray: typing.List[int]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withDeviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withDeviceNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest': ...
    def withLsaImplementation(self, boolean: bool) -> 'DefaultParametersRequestRest': ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withParameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withParameterGroups(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest': ...
    def withParameterNamePattern(self, string: str) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withParameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withParameterNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withParameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withParameterTypeNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withParticleTransferNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withParticleTransferNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withPropertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withPropertyFieldIds(self, longArray: typing.List[int]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withPropertyNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withPropertyNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest': ...
    def withReadable(self, boolean: bool) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withValueTypes(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest': ...
    @typing.overload
    def withValueTypes(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest': ...
    def withWritable(self, boolean: bool) -> 'DefaultParametersRequestRest': ...
    class Builder:
        def acceleratorName(self, string: str) -> 'DefaultParametersRequestRest.Builder': ...
        def acceleratorZoneNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAcceleratorZoneName(self, string: str) -> 'DefaultParametersRequestRest.Builder': ...
        def addAcceleratorZoneNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAllAcceleratorZoneNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAllDeviceIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAllDeviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAllParameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAllParameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAllParameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAllParticleTransferNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAllPropertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAllPropertyNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addAllValueTypes(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addDeviceId(self, long: int) -> 'DefaultParametersRequestRest.Builder': ...
        def addDeviceIds(self, longArray: typing.List[int]) -> 'DefaultParametersRequestRest.Builder': ...
        def addDeviceName(self, string: str) -> 'DefaultParametersRequestRest.Builder': ...
        def addDeviceNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addParameterGroup(self, string: str) -> 'DefaultParametersRequestRest.Builder': ...
        def addParameterGroups(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addParameterName(self, string: str) -> 'DefaultParametersRequestRest.Builder': ...
        def addParameterNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addParameterTypeName(self, string: str) -> 'DefaultParametersRequestRest.Builder': ...
        def addParameterTypeNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addParticleTransferName(self, string: str) -> 'DefaultParametersRequestRest.Builder': ...
        def addParticleTransferNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addPropertyFieldId(self, long: int) -> 'DefaultParametersRequestRest.Builder': ...
        def addPropertyFieldIds(self, longArray: typing.List[int]) -> 'DefaultParametersRequestRest.Builder': ...
        def addPropertyName(self, string: str) -> 'DefaultParametersRequestRest.Builder': ...
        def addPropertyNames(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def addValueType(self, string: str) -> 'DefaultParametersRequestRest.Builder': ...
        def addValueTypes(self, stringArray: typing.List[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def build(self) -> 'DefaultParametersRequestRest': ...
        def critical(self, boolean: bool) -> 'DefaultParametersRequestRest.Builder': ...
        def deviceIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestRest.Builder': ...
        def deviceNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def lsaImplementation(self, boolean: bool) -> 'DefaultParametersRequestRest.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultParametersRequestRest.Builder': ...
        def parameterGroups(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def parameterNamePattern(self, string: str) -> 'DefaultParametersRequestRest.Builder': ...
        def parameterNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def parameterTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def particleTransferNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def propertyFieldIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParametersRequestRest.Builder': ...
        def propertyNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def readable(self, boolean: bool) -> 'DefaultParametersRequestRest.Builder': ...
        def valueTypes(self, iterable: java.lang.Iterable[str]) -> 'DefaultParametersRequestRest.Builder': ...
        def writable(self, boolean: bool) -> 'DefaultParametersRequestRest.Builder': ...

class DefaultParentToChildrenRelationRest(ParentToChildrenRelationRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParentToChildrenRelationRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest`.
    
        Use the builder to create immutable instances: :code:`DefaultParentToChildrenRelationRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParentToChildrenRelationRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParentToChildrenRelationRest`.
        
            .. code-block: java
            
             DefaultParentToChildrenRelationRest.builder()
                .addChildrenId|addAllChildrenIds(long) // :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest.getChildrenIds` elements
                .parentId(Long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest.getParentId`
                .build();
             
        
            Returns:
                A new DefaultParentToChildrenRelationRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parentToChildrenRelationRest: ParentToChildrenRelationRest) -> 'DefaultParentToChildrenRelationRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest`): The instance to copy
        
            Returns:
                A copied immutable ParentToChildrenRelationRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getChildrenIds(self) -> java.util.List[int]: ...
    def getParentId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest.getParentId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest`
        
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
            Prints the immutable value :code:`ParentToChildrenRelationRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withChildrenIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParentToChildrenRelationRest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest.getChildrenIds`.
        
            Parameters:
                elements (long...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultParentToChildrenRelationRest` withChildrenIds (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest.getChildrenIds`. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements): An iterable of childrenIds elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withChildrenIds(self, longArray: typing.List[int]) -> 'DefaultParentToChildrenRelationRest': ...
    def withParentId(self, long: int) -> 'DefaultParentToChildrenRelationRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest.getParentId` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`): A new value for parentId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllChildrenIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParentToChildrenRelationRest.Builder': ...
        def addChildrenId(self, long: int) -> 'DefaultParentToChildrenRelationRest.Builder': ...
        def addChildrenIds(self, longArray: typing.List[int]) -> 'DefaultParentToChildrenRelationRest.Builder': ...
        def build(self) -> 'DefaultParentToChildrenRelationRest': ...
        def childrenIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultParentToChildrenRelationRest.Builder': ...
        def parentId(self, long: int) -> 'DefaultParentToChildrenRelationRest.Builder': ...

class DefaultPropertyAndDeviceRest(PropertyAndDeviceRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultPropertyAndDeviceRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest`.
    
        Use the builder to create immutable instances: :code:`DefaultPropertyAndDeviceRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultPropertyAndDeviceRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultPropertyAndDeviceRest`.
        
            .. code-block: java
            
             DefaultPropertyAndDeviceRest.builder()
                .deviceId(Long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest.getDeviceId`
                .propertyName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest.getPropertyName`
                .build();
             
        
            Returns:
                A new DefaultPropertyAndDeviceRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(propertyAndDeviceRest: PropertyAndDeviceRest) -> 'DefaultPropertyAndDeviceRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest`): The instance to copy
        
            Returns:
                A copied immutable PropertyAndDeviceRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDeviceId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest.getDeviceId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest`
        
            Returns:
                The value of the :code:`deviceId` attribute
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest.getPropertyName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest`
        
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
            Prints the immutable value :code:`PropertyAndDeviceRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDeviceId(self, long: int) -> 'DefaultPropertyAndDeviceRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest.getDeviceId` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`): A new value for deviceId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyName(self, string: str) -> 'DefaultPropertyAndDeviceRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest.getPropertyName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for propertyName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultPropertyAndDeviceRest': ...
        def deviceId(self, long: int) -> 'DefaultPropertyAndDeviceRest.Builder': ...
        def propertyName(self, string: str) -> 'DefaultPropertyAndDeviceRest.Builder': ...

class DefaultPropertyFieldRest(PropertyFieldRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultPropertyFieldRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest`.
    
        Use the builder to create immutable instances: :code:`DefaultPropertyFieldRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultPropertyFieldRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultPropertyFieldRest`.
        
            .. code-block: java
            
             DefaultPropertyFieldRest.builder()
                .id(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getId`
                .deviceTypeName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getDeviceTypeName`
                .propertyName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getPropertyName`
                .fieldName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getFieldName`
                .build();
             
        
            Returns:
                A new DefaultPropertyFieldRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(propertyFieldRest: PropertyFieldRest) -> 'DefaultPropertyFieldRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest`): The instance to copy
        
            Returns:
                A copied immutable PropertyFieldRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDeviceTypeName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getDeviceTypeName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest`
        
            Returns:
                The value of the :code:`deviceTypeName` attribute
        
        
        """
        ...
    def getFieldName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getFieldName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest`
        
            Returns:
                The value of the :code:`fieldName` attribute
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getPropertyName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getPropertyName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest`
        
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
            Prints the immutable value :code:`PropertyFieldRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDeviceTypeName(self, string: str) -> 'DefaultPropertyFieldRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getDeviceTypeName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for deviceTypeName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withFieldName(self, string: str) -> 'DefaultPropertyFieldRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getFieldName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for fieldName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultPropertyFieldRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getId` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyName(self, string: str) -> 'DefaultPropertyFieldRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.PropertyFieldRest.getPropertyName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for propertyName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultPropertyFieldRest': ...
        def deviceTypeName(self, string: str) -> 'DefaultPropertyFieldRest.Builder': ...
        def fieldName(self, string: str) -> 'DefaultPropertyFieldRest.Builder': ...
        def id(self, long: int) -> 'DefaultPropertyFieldRest.Builder': ...
        def propertyName(self, string: str) -> 'DefaultPropertyFieldRest.Builder': ...

class DefaultSaveParameterRelationRest(SaveParameterRelationRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultSaveParameterRelationRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest`.
    
        Use the builder to create immutable instances: :code:`DefaultSaveParameterRelationRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultSaveParameterRelationRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultSaveParameterRelationRest`.
        
            .. code-block: java
            
             DefaultSaveParameterRelationRest.builder()
                .hierarchy(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest.getHierarchy`
                .addParent2ChildrenRelation|addAllParent2ChildrenRelations(cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest) // :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest.getParent2ChildrenRelations` elements
                .build();
             
        
            Returns:
                A new DefaultSaveParameterRelationRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(saveParameterRelationRest: SaveParameterRelationRest) -> 'DefaultSaveParameterRelationRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest`): The instance to copy
        
            Returns:
                A copied immutable SaveParameterRelationRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getHierarchy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest.getHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest`
        
            Returns:
                The value of the :code:`hierarchy` attribute
        
        
        """
        ...
    def getParent2ChildrenRelations(self) -> java.util.List[ParentToChildrenRelationRest]: ...
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
            Prints the immutable value :code:`SaveParameterRelationRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withHierarchy(self, string: str) -> 'DefaultSaveParameterRelationRest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest.getHierarchy` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for hierarchy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParent2ChildrenRelations(self, parentToChildrenRelationRestArray: typing.List[ParentToChildrenRelationRest]) -> 'DefaultSaveParameterRelationRest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest.getParent2ChildrenRelations`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.DefaultSaveParameterRelationRest` withParent2ChildrenRelations (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.SaveParameterRelationRest.getParent2ChildrenRelations`. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParentToChildrenRelationRest`> elements): An iterable of parent2ChildrenRelations elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParent2ChildrenRelations(self, iterable: java.lang.Iterable[ParentToChildrenRelationRest]) -> 'DefaultSaveParameterRelationRest': ...
    class Builder:
        def addAllParent2ChildrenRelations(self, iterable: java.lang.Iterable[ParentToChildrenRelationRest]) -> 'DefaultSaveParameterRelationRest.Builder': ...
        def addParent2ChildrenRelation(self, parentToChildrenRelationRest: ParentToChildrenRelationRest) -> 'DefaultSaveParameterRelationRest.Builder': ...
        def addParent2ChildrenRelations(self, parentToChildrenRelationRestArray: typing.List[ParentToChildrenRelationRest]) -> 'DefaultSaveParameterRelationRest.Builder': ...
        def build(self) -> 'DefaultSaveParameterRelationRest': ...
        def hierarchy(self, string: str) -> 'DefaultSaveParameterRelationRest.Builder': ...
        def parent2ChildrenRelations(self, iterable: java.lang.Iterable[ParentToChildrenRelationRest]) -> 'DefaultSaveParameterRelationRest.Builder': ...

class DefaultTypeRest(TypeRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultTypeRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.TypeRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.TypeRest`.
    
        Use the builder to create immutable instances: :code:`DefaultTypeRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultTypeRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultTypeRest`.
        
            .. code-block: java
            
             DefaultTypeRest.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultTypeRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(typeRest: TypeRest) -> 'DefaultTypeRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.TypeRest` value. Uses accessors to get values to
            initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.TypeRest`): The instance to copy
        
            Returns:
                A copied immutable TypeRest instance
        
        
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
            Prints the immutable value :code:`TypeRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultTypeRest':
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
        def build(self) -> 'DefaultTypeRest': ...
        def name(self, string: str) -> 'DefaultTypeRest.Builder': ...

class DefaultValueCompareTypeRest(ValueCompareTypeRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultValueCompareTypeRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ValueCompareTypeRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ValueCompareTypeRest`.
    
        Use the builder to create immutable instances: :code:`DefaultValueCompareTypeRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultValueCompareTypeRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultValueCompareTypeRest`.
        
            .. code-block: java
            
             DefaultValueCompareTypeRest.builder()
                .name(String) // required name
                .build();
             
        
            Returns:
                A new DefaultValueCompareTypeRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(valueCompareTypeRest: ValueCompareTypeRest) -> 'DefaultValueCompareTypeRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ValueCompareTypeRest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ValueCompareTypeRest`): The instance to copy
        
            Returns:
                A copied immutable ValueCompareTypeRest instance
        
        
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
            Prints the immutable value :code:`ValueCompareTypeRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultValueCompareTypeRest':
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
        def build(self) -> 'DefaultValueCompareTypeRest': ...
        def name(self, string: str) -> 'DefaultValueCompareTypeRest.Builder': ...

class DefaultValueDescriptorRest(ValueDescriptorRest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultValueDescriptorRest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest`.
    
        Use the builder to create immutable instances: :code:`DefaultValueDescriptorRest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultValueDescriptorRest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.DefaultValueDescriptorRest`.
        
            .. code-block: java
            
             DefaultValueDescriptorRest.builder()
                .enumType(cern.lsa.client.rest.api.v1.dto.EnumTypeRest | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getEnumType`
                .booleanType(cern.lsa.client.rest.api.v1.dto.BooleanTypeRest | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getBooleanType`
                .columnCount(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getColumnCount`
                .rowCount(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getRowCount`
                .max(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getMax`
                .min(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getMin`
                .absoluteTolerance(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getAbsoluteTolerance`
                .relativeTolerance(Double | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getRelativeTolerance`
                .xPrecision(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getXPrecision`
                .xUnit(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getXUnit`
                .yPrecision(Integer | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getYPrecision`
                .yUnit(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest.getYUnit`
                .build();
             
        
            Returns:
                A new DefaultValueDescriptorRest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(valueDescriptorRest: ValueDescriptorRest) -> 'DefaultValueDescriptorRest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.ValueDescriptorRest`): The instance to copy
        
            Returns:
                A copied immutable ValueDescriptorRest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAbsoluteTolerance(self) -> float: ...
    def getBooleanType(self) -> BooleanTypeRest: ...
    def getColumnCount(self) -> int: ...
    def getEnumType(self) -> EnumTypeRest: ...
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
            Prints the immutable value :code:`ValueDescriptorRest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAbsoluteTolerance(self, double: float) -> 'DefaultValueDescriptorRest': ...
    def withBooleanType(self, booleanTypeRest: BooleanTypeRest) -> 'DefaultValueDescriptorRest': ...
    def withColumnCount(self, integer: int) -> 'DefaultValueDescriptorRest': ...
    def withEnumType(self, enumTypeRest: EnumTypeRest) -> 'DefaultValueDescriptorRest': ...
    def withMax(self, double: float) -> 'DefaultValueDescriptorRest': ...
    def withMin(self, double: float) -> 'DefaultValueDescriptorRest': ...
    def withRelativeTolerance(self, double: float) -> 'DefaultValueDescriptorRest': ...
    def withRowCount(self, integer: int) -> 'DefaultValueDescriptorRest': ...
    def withXPrecision(self, integer: int) -> 'DefaultValueDescriptorRest': ...
    def withXUnit(self, string: str) -> 'DefaultValueDescriptorRest': ...
    def withYPrecision(self, integer: int) -> 'DefaultValueDescriptorRest': ...
    def withYUnit(self, string: str) -> 'DefaultValueDescriptorRest': ...
    class Builder:
        def absoluteTolerance(self, double: float) -> 'DefaultValueDescriptorRest.Builder': ...
        def booleanType(self, booleanTypeRest: BooleanTypeRest) -> 'DefaultValueDescriptorRest.Builder': ...
        def build(self) -> 'DefaultValueDescriptorRest': ...
        def columnCount(self, integer: int) -> 'DefaultValueDescriptorRest.Builder': ...
        def enumType(self, enumTypeRest: EnumTypeRest) -> 'DefaultValueDescriptorRest.Builder': ...
        def max(self, double: float) -> 'DefaultValueDescriptorRest.Builder': ...
        def min(self, double: float) -> 'DefaultValueDescriptorRest.Builder': ...
        def relativeTolerance(self, double: float) -> 'DefaultValueDescriptorRest.Builder': ...
        def rowCount(self, integer: int) -> 'DefaultValueDescriptorRest.Builder': ...
        def xPrecision(self, integer: int) -> 'DefaultValueDescriptorRest.Builder': ...
        def xUnit(self, string: str) -> 'DefaultValueDescriptorRest.Builder': ...
        def yPrecision(self, integer: int) -> 'DefaultValueDescriptorRest.Builder': ...
        def yUnit(self, string: str) -> 'DefaultValueDescriptorRest.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1.dto")``.

    AcceleratorZoneRest: typing.Type[AcceleratorZoneRest]
    BooleanItemRest: typing.Type[BooleanItemRest]
    BooleanTypeRest: typing.Type[BooleanTypeRest]
    DefaultAcceleratorZoneRest: typing.Type[DefaultAcceleratorZoneRest]
    DefaultBooleanItemRest: typing.Type[DefaultBooleanItemRest]
    DefaultBooleanTypeRest: typing.Type[DefaultBooleanTypeRest]
    DefaultDeviceMetaTypeRest: typing.Type[DefaultDeviceMetaTypeRest]
    DefaultDeviceRest: typing.Type[DefaultDeviceRest]
    DefaultDeviceStateRest: typing.Type[DefaultDeviceStateRest]
    DefaultDeviceTypeImplementationRest: typing.Type[DefaultDeviceTypeImplementationRest]
    DefaultDeviceTypeVersionContainerRest: typing.Type[DefaultDeviceTypeVersionContainerRest]
    DefaultDeviceTypeVersionNumberRest: typing.Type[DefaultDeviceTypeVersionNumberRest]
    DefaultDeviceTypeVersionRest: typing.Type[DefaultDeviceTypeVersionRest]
    DefaultEnumItemRest: typing.Type[DefaultEnumItemRest]
    DefaultEnumTypeRest: typing.Type[DefaultEnumTypeRest]
    DefaultErrorDto: typing.Type[DefaultErrorDto]
    DefaultIncaPropertyFieldInfoRest: typing.Type[DefaultIncaPropertyFieldInfoRest]
    DefaultIncaPropertyFieldInfosRequestRest: typing.Type[DefaultIncaPropertyFieldInfosRequestRest]
    DefaultMakeRuleClassInfoRest: typing.Type[DefaultMakeRuleClassInfoRest]
    DefaultMakeRuleConfigInfoRest: typing.Type[DefaultMakeRuleConfigInfoRest]
    DefaultMakeRuleConfigStatusRest: typing.Type[DefaultMakeRuleConfigStatusRest]
    DefaultMakeRuleInfoRest: typing.Type[DefaultMakeRuleInfoRest]
    DefaultParameterAttributesRest: typing.Type[DefaultParameterAttributesRest]
    DefaultParameterGroupRest: typing.Type[DefaultParameterGroupRest]
    DefaultParameterRest: typing.Type[DefaultParameterRest]
    DefaultParameterTreeDataRest: typing.Type[DefaultParameterTreeDataRest]
    DefaultParameterTreeNodeRest: typing.Type[DefaultParameterTreeNodeRest]
    DefaultParameterTreeRelationRest: typing.Type[DefaultParameterTreeRelationRest]
    DefaultParameterTreesRequestRest: typing.Type[DefaultParameterTreesRequestRest]
    DefaultParameterTypeCategoryRest: typing.Type[DefaultParameterTypeCategoryRest]
    DefaultParameterTypeRest: typing.Type[DefaultParameterTypeRest]
    DefaultParameterTypesRequestRest: typing.Type[DefaultParameterTypesRequestRest]
    DefaultParametersRequestRest: typing.Type[DefaultParametersRequestRest]
    DefaultParentToChildrenRelationRest: typing.Type[DefaultParentToChildrenRelationRest]
    DefaultPropertyAndDeviceRest: typing.Type[DefaultPropertyAndDeviceRest]
    DefaultPropertyFieldRest: typing.Type[DefaultPropertyFieldRest]
    DefaultSaveParameterRelationRest: typing.Type[DefaultSaveParameterRelationRest]
    DefaultTypeRest: typing.Type[DefaultTypeRest]
    DefaultValueCompareTypeRest: typing.Type[DefaultValueCompareTypeRest]
    DefaultValueDescriptorRest: typing.Type[DefaultValueDescriptorRest]
    DeviceMetaTypeRest: typing.Type[DeviceMetaTypeRest]
    DeviceRest: typing.Type[DeviceRest]
    DeviceStateRest: typing.Type[DeviceStateRest]
    DeviceTypeImplementationRest: typing.Type[DeviceTypeImplementationRest]
    DeviceTypeVersionContainerRest: typing.Type[DeviceTypeVersionContainerRest]
    DeviceTypeVersionNumberRest: typing.Type[DeviceTypeVersionNumberRest]
    DeviceTypeVersionRest: typing.Type[DeviceTypeVersionRest]
    EnumItemRest: typing.Type[EnumItemRest]
    EnumTypeRest: typing.Type[EnumTypeRest]
    ErrorDto: typing.Type[ErrorDto]
    IncaPropertyFieldInfoRest: typing.Type[IncaPropertyFieldInfoRest]
    IncaPropertyFieldInfosRequestRest: typing.Type[IncaPropertyFieldInfosRequestRest]
    MakeRuleClassInfoRest: typing.Type[MakeRuleClassInfoRest]
    MakeRuleConfigInfoRest: typing.Type[MakeRuleConfigInfoRest]
    MakeRuleConfigStatusRest: typing.Type[MakeRuleConfigStatusRest]
    MakeRuleInfoRest: typing.Type[MakeRuleInfoRest]
    ParameterAttributesRest: typing.Type[ParameterAttributesRest]
    ParameterGroupRest: typing.Type[ParameterGroupRest]
    ParameterRest: typing.Type[ParameterRest]
    ParameterTreeDataRest: typing.Type[ParameterTreeDataRest]
    ParameterTreeNodeRest: typing.Type[ParameterTreeNodeRest]
    ParameterTreeRelationRest: typing.Type[ParameterTreeRelationRest]
    ParameterTreesRequestRest: typing.Type[ParameterTreesRequestRest]
    ParameterTypeCategoryRest: typing.Type[ParameterTypeCategoryRest]
    ParameterTypeRest: typing.Type[ParameterTypeRest]
    ParameterTypesRequestRest: typing.Type[ParameterTypesRequestRest]
    ParametersRequestRest: typing.Type[ParametersRequestRest]
    ParentToChildrenRelationRest: typing.Type[ParentToChildrenRelationRest]
    PropertyAndDeviceRest: typing.Type[PropertyAndDeviceRest]
    PropertyFieldRest: typing.Type[PropertyFieldRest]
    SaveParameterRelationRest: typing.Type[SaveParameterRelationRest]
    TypeRest: typing.Type[TypeRest]
    ValueCompareTypeRest: typing.Type[ValueCompareTypeRest]
    ValueDescriptorRest: typing.Type[ValueDescriptorRest]
