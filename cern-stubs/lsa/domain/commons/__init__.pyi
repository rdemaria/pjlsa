import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.commons.japc
import cern.lsa.domain.commons.logging
import cern.lsa.domain.commons.spi
import cern.lsa.domain.commons.util
import java.lang.annotation
import java.util
import java.util.function
import typing



class Accelerators(java.lang.annotation.Annotation):
    """
    Java class 'cern.lsa.domain.commons.Accelerators'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def value(self) -> typing.List[typing.Type[java.util.function.Supplier[cern.accsoft.commons.domain.Accelerator]]]: ...
    class Resolver:
        """
        Java class 'cern.lsa.domain.commons.Accelerators$Resolver'
        
            Extends:
                java.lang.Object
        
        """
        @staticmethod
        def anyMatch(accelerator: cern.accsoft.commons.domain.Accelerator, accelerators: 'Accelerators') -> bool: ...
        @staticmethod
        def getAccelerators(accelerators: 'Accelerators') -> java.util.Set[cern.accsoft.commons.domain.Accelerator]: ...
        @staticmethod
        def isClassApplicableForAccelerator(class_: typing.Type[typing.Any], accelerator: cern.accsoft.commons.domain.Accelerator) -> bool: ...

class Attribute(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.lsa.domain.commons.Attribute'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getAttributeDefinition(self) -> 'AttributeDefinition': ...
    def getBoolean(self) -> bool: ...
    def getDouble(self) -> float: ...
    def getInt(self) -> int: ...
    def getLong(self) -> int: ...
    def getValue(self) -> str: ...

class AttributeAware:
    """
    Java class 'cern.lsa.domain.commons.AttributeAware'
    
    """
    def getAttribute(self, string: str) -> Attribute: ...
    def getAttributes(self) -> java.util.Set[Attribute]: ...

class AttributeWritableAware:
    """
    Java class 'cern.lsa.domain.commons.AttributeWritableAware'
    
    """
    def addAttribute(self, attribute: Attribute) -> None: ...
    def setAttributes(self, collection: typing.Union[java.util.Collection[Attribute], typing.Sequence[Attribute]]) -> None: ...

class Entities:
    """
    Java class 'cern.lsa.domain.commons.Entities'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Entities()
    
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def getIds(collection: typing.Union[java.util.Collection['IdentifiedEntity'], typing.Sequence['IdentifiedEntity']]) -> java.util.Collection[int]: ...
    @typing.overload
    @staticmethod
    def getIds(list: java.util.List['IdentifiedEntity']) -> java.util.List[int]: ...
    @typing.overload
    @staticmethod
    def getIds(set: java.util.Set['IdentifiedEntity']) -> java.util.Set[int]: ...
    @staticmethod
    def getIdsList(collection: typing.Union[java.util.Collection['IdentifiedEntity'], typing.Sequence['IdentifiedEntity']]) -> java.util.List[int]: ...
    @staticmethod
    def getIdsSet(collection: typing.Union[java.util.Collection['IdentifiedEntity'], typing.Sequence['IdentifiedEntity']]) -> java.util.Set[int]: ...
    @staticmethod
    def idsIn(collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> cern.accsoft.commons.util.Filters.Filter['IdentifiedEntity']: ...
    _toIdsMap__V = typing.TypeVar('_toIdsMap__V', bound='IdentifiedEntity')  # <V>
    @staticmethod
    def toIdsMap(collection: typing.Union[java.util.Collection[_toIdsMap__V], typing.Sequence[_toIdsMap__V]]) -> java.util.Map[int, _toIdsMap__V]: ...

class IdentifiedEntity:
    """
    Java class 'cern.lsa.domain.commons.IdentifiedEntity'
    
    """
    def getId(self) -> int: ...

class LSAConstants:
    """
    Java class 'cern.lsa.domain.commons.LSAConstants'
    
        Extends:
            java.lang.Object
    
    """
    class ContextsConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$ContextsConstants'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * ContextsConstants()
        
          Attributes:
            DEFAULT_CONTEXT_CATEGORY_NAME (java.lang.String): final static field
            OBSOLETE_CONTEXT_CATEGORY_NAME (java.lang.String): final static field
        
        """
        DEFAULT_CONTEXT_CATEGORY_NAME: typing.ClassVar[str] = ...
        OBSOLETE_CONTEXT_CATEGORY_NAME: typing.ClassVar[str] = ...
        def __init__(self): ...
    class CriticalPropertyConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$CriticalPropertyConstants'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * CriticalPropertyConstants()
        
          Attributes:
            CRITICAL_PROPERTIES_ADMIN_ROLE (java.lang.String): final static field
            SIGNATURE_FIELD_NAME (java.lang.String): final static field
        
        """
        CRITICAL_PROPERTIES_ADMIN_ROLE: typing.ClassVar[str] = ...
        SIGNATURE_FIELD_NAME: typing.ClassVar[str] = ...
        def __init__(self): ...
    class DriveConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$DriveConstants'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * DriveConstants()
        
          Attributes:
            TRANSACTION_ID_FILTER_FIELD_NAME (java.lang.String): final static field
            TRANSACTION_ID_PROPERTY (java.lang.String): final static field
            TRANSACTION_TEST_PROPERTY (java.lang.String): final static field
            TRANSACTION_COMMIT_PROPERTY (java.lang.String): final static field
            TRANSACTION_ROLLBACK_PROPERTY (java.lang.String): final static field
        
        """
        TRANSACTION_ID_FILTER_FIELD_NAME: typing.ClassVar[str] = ...
        TRANSACTION_ID_PROPERTY: typing.ClassVar[str] = ...
        TRANSACTION_TEST_PROPERTY: typing.ClassVar[str] = ...
        TRANSACTION_COMMIT_PROPERTY: typing.ClassVar[str] = ...
        TRANSACTION_ROLLBACK_PROPERTY: typing.ClassVar[str] = ...
        def __init__(self): ...
    class JmxConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$JmxConstants'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * JmxConstants()
        
          Attributes:
            LSA_JMX_DOMAIN (java.lang.String): final static field
        
        """
        LSA_JMX_DOMAIN: typing.ClassVar[str] = ...
        def __init__(self): ...
    class LayoutConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$LayoutConstants'
        
            Extends:
                java.lang.Object
        
          Attributes:
            DEFAULT_PARTICLE_TRANSFER_NAME (java.lang.String): final static field
            DEFAULT_BEAMPROCESS_TYPE_NAME (java.lang.String): final static field
        
        """
        DEFAULT_PARTICLE_TRANSFER_NAME: typing.ClassVar[str] = ...
        DEFAULT_BEAMPROCESS_TYPE_NAME: typing.ClassVar[str] = ...
    class MetaDeviceConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$MetaDeviceConstants'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * MetaDeviceConstants()
        
          Attributes:
            LSA_META_DEVICE_SUFFIX (java.lang.String): final static field
            CYCLES_PROPERTY_NAME (java.lang.String): final static field
            LSA_CONTEXT_MAPPING_PROPERTY_NAME (java.lang.String): final static field
            LSA_CONTEXT_PROPERTY_NAME (java.lang.String): final static field
            REFERENCE_UPDATE_PROPERTY_NAME (java.lang.String): final static field
            TRIM_PROPERTY_NAME (java.lang.String): final static field
            DRIVE_PROPERTY_NAME (java.lang.String): final static field
            DRIVABLE_CONTEXTS_FIELD_NAME (java.lang.String): final static field
            DRIVABLE_CONTEXT_NAME_FIELD_NAME (java.lang.String): final static field
            CONTEXT_SELECTORS_FIELD_NAME (java.lang.String): final static field
            DRIVABLE_CONTEXT_TYPE_FIELD_NAME (java.lang.String): final static field
            LIST_FIELD_NAME (java.lang.String): final static field
            PARAMETER_NAMES_FIELD_NAME (java.lang.String): final static field
            USERS_FIELD_NAME (java.lang.String): final static field
            USER_FIELD_NAME (java.lang.String): final static field
        
        """
        LSA_META_DEVICE_SUFFIX: typing.ClassVar[str] = ...
        CYCLES_PROPERTY_NAME: typing.ClassVar[str] = ...
        LSA_CONTEXT_MAPPING_PROPERTY_NAME: typing.ClassVar[str] = ...
        LSA_CONTEXT_PROPERTY_NAME: typing.ClassVar[str] = ...
        REFERENCE_UPDATE_PROPERTY_NAME: typing.ClassVar[str] = ...
        TRIM_PROPERTY_NAME: typing.ClassVar[str] = ...
        DRIVE_PROPERTY_NAME: typing.ClassVar[str] = ...
        DRIVABLE_CONTEXTS_FIELD_NAME: typing.ClassVar[str] = ...
        DRIVABLE_CONTEXT_NAME_FIELD_NAME: typing.ClassVar[str] = ...
        CONTEXT_SELECTORS_FIELD_NAME: typing.ClassVar[str] = ...
        DRIVABLE_CONTEXT_TYPE_FIELD_NAME: typing.ClassVar[str] = ...
        LIST_FIELD_NAME: typing.ClassVar[str] = ...
        PARAMETER_NAMES_FIELD_NAME: typing.ClassVar[str] = ...
        USERS_FIELD_NAME: typing.ClassVar[str] = ...
        USER_FIELD_NAME: typing.ClassVar[str] = ...
        def __init__(self): ...
    class ParameterConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$ParameterConstants'
        
            Extends:
                java.lang.Object
        
          Attributes:
            SIGNATURE_PARAMETER_TYPE (java.lang.String): final static field
            KNOB_PARAMETER_TYPE (java.lang.String): final static field
            MOMENTUM_PROPERTY (java.lang.String): final static field
            MOMENTUM_PARAMETER_TYPE (java.lang.String): final static field
            K_STEERING_PARAMETER_TYPE (java.lang.String): final static field
            DEFAULT_PARAMETER_HIERARCHY (java.lang.String): final static field
            LSA_INTERNAL_PARAMETER_TYPES (java.util.Set): final static field
        
        """
        SIGNATURE_PARAMETER_TYPE: typing.ClassVar[str] = ...
        KNOB_PARAMETER_TYPE: typing.ClassVar[str] = ...
        MOMENTUM_PROPERTY: typing.ClassVar[str] = ...
        MOMENTUM_PARAMETER_TYPE: typing.ClassVar[str] = ...
        K_STEERING_PARAMETER_TYPE: typing.ClassVar[str] = ...
        DEFAULT_PARAMETER_HIERARCHY: typing.ClassVar[str] = ...
        LSA_INTERNAL_PARAMETER_TYPES: typing.ClassVar[java.util.Set] = ...
    class ParameterGroupConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$ParameterGroupConstants'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * ParameterGroupConstants()
        
          Attributes:
            NOT_USED_PARAMETER_GROUP (java.lang.String): final static field
            FAKE_NO_PARAMETER_GROUP (java.lang.String): final static field
            ALL_PARAMETER_GROUPS (java.lang.String): final static field
        
        """
        NOT_USED_PARAMETER_GROUP: typing.ClassVar[str] = ...
        FAKE_NO_PARAMETER_GROUP: typing.ClassVar[str] = ...
        ALL_PARAMETER_GROUPS: typing.ClassVar[str] = ...
        def __init__(self): ...
    class ParameterUrlConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$ParameterUrlConstants'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * ParameterUrlConstants()
        
          Attributes:
            LSA_SERVER_NAMES_PREFIX (java.lang.String): final static field
            INCA_SERVER_NAMES_PREFIX (java.lang.String): final static field
            META_SERVICE_PREFIX (java.lang.String): final static field
        
        """
        LSA_SERVER_NAMES_PREFIX: typing.ClassVar[str] = ...
        INCA_SERVER_NAMES_PREFIX: typing.ClassVar[str] = ...
        META_SERVICE_PREFIX: typing.ClassVar[str] = ...
        def __init__(self): ...
    class SettingCopyConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$SettingCopyConstants'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * SettingCopyConstants()
        
          Attributes:
            ATTR_IS_SETTINGS_COPY (java.lang.String): final static field
            ATTR_SOURCE_CONTEXT (java.lang.String): final static field
            ATTR_DESTINATION_TO_SOURCE_BEAMPROCESS (java.lang.String): final static field
            ATTR_TRIM_DATE (java.lang.String): final static field
            ATTR_ARCHIVE_VERSION (java.lang.String): final static field
            ATTR_COPY_ALL_PARAMETERS (java.lang.String): final static field
            ATTR_COPY_BEAM_OUT (java.lang.String): final static field
        
        """
        ATTR_IS_SETTINGS_COPY: typing.ClassVar[str] = ...
        ATTR_SOURCE_CONTEXT: typing.ClassVar[str] = ...
        ATTR_DESTINATION_TO_SOURCE_BEAMPROCESS: typing.ClassVar[str] = ...
        ATTR_TRIM_DATE: typing.ClassVar[str] = ...
        ATTR_ARCHIVE_VERSION: typing.ClassVar[str] = ...
        ATTR_COPY_ALL_PARAMETERS: typing.ClassVar[str] = ...
        ATTR_COPY_BEAM_OUT: typing.ClassVar[str] = ...
        def __init__(self): ...
    class TrimConstants:
        """
        Java class 'cern.lsa.domain.commons.LSAConstants$TrimConstants'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * TrimConstants()
        
          Attributes:
            ATTR_CONTEXT_SETTINGS (java.lang.String): final static field
            ATTR_TRIMMED_CONTEXT_SETTINGS (java.lang.String): final static field
            ATTR_ALLOW_NON_TRIMMABLE_PARAMETERS (java.lang.String): final static field
            ATTR_PARAMETER_HIERARCHY (java.lang.String): final static field
        
        """
        ATTR_CONTEXT_SETTINGS: typing.ClassVar[str] = ...
        ATTR_TRIMMED_CONTEXT_SETTINGS: typing.ClassVar[str] = ...
        ATTR_ALLOW_NON_TRIMMABLE_PARAMETERS: typing.ClassVar[str] = ...
        ATTR_PARAMETER_HIERARCHY: typing.ClassVar[str] = ...
        def __init__(self): ...

class AttributeDefinition(IdentifiedEntity, cern.accsoft.commons.util.Named):
    """
    Java class 'cern.lsa.domain.commons.AttributeDefinition'
    
        Interfaces:
            cern.lsa.domain.commons.IdentifiedEntity,
            cern.accsoft.commons.util.Named
    
    """
    def getDefaultValue(self) -> str: ...
    def getDescription(self) -> str: ...
    def getEnumValues(self) -> java.util.Set[str]: ...
    def getUnits(self) -> str: ...
    def getValueType(self) -> cern.accsoft.commons.value.Type: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons")``.

    Accelerators: typing.Type[Accelerators]
    Attribute: typing.Type[Attribute]
    AttributeAware: typing.Type[AttributeAware]
    AttributeDefinition: typing.Type[AttributeDefinition]
    AttributeWritableAware: typing.Type[AttributeWritableAware]
    Entities: typing.Type[Entities]
    IdentifiedEntity: typing.Type[IdentifiedEntity]
    LSAConstants: typing.Type[LSAConstants]
    japc: cern.lsa.domain.commons.japc.__module_protocol__
    logging: cern.lsa.domain.commons.logging.__module_protocol__
    spi: cern.lsa.domain.commons.spi.__module_protocol__
    util: cern.lsa.domain.commons.util.__module_protocol__
