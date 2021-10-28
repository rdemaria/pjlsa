import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.commons
import cern.lsa.domain.settings
import java.lang
import java.util
import typing



class BaseTypes:
    """
    Java class 'cern.lsa.domain.settings.type.BaseTypes'
    
        Extends:
            java.lang.Object
    
      Attributes:
        BASE_TYPE_NAME_COMPARATOR (java.util.Comparator): final static field
    
    """
    BASE_TYPE_NAME_COMPARATOR: typing.ClassVar[java.util.Comparator] = ...
    @staticmethod
    def isPreCycling(beamProcessType: 'BeamProcessType') -> bool: ...

class BeamProcessPurpose(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.lsa.domain.settings.type.BeamProcessPurpose'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def isDefault(self) -> bool: ...

class BeamProcessPurposes:
    """
    Java class 'cern.lsa.domain.settings.type.BeamProcessPurposes'
    
        Extends:
            java.lang.Object
    
    """
    _filterBeamProcessesByPurposes__T = typing.TypeVar('_filterBeamProcessesByPurposes__T', bound=cern.lsa.domain.settings.BeamProcess)  # <T>
    @staticmethod
    def filterBeamProcessesByPurposes(collection: typing.Union[java.util.Collection[_filterBeamProcessesByPurposes__T], typing.Sequence[_filterBeamProcessesByPurposes__T]], collection2: typing.Union[java.util.Collection[BeamProcessPurpose], typing.Sequence[BeamProcessPurpose]]) -> java.util.Collection[_filterBeamProcessesByPurposes__T]: ...
    _getBeamProcessByPurpose__T = typing.TypeVar('_getBeamProcessByPurpose__T', bound=cern.lsa.domain.settings.BeamProcess)  # <T>
    @staticmethod
    def getBeamProcessByPurpose(collection: typing.Union[java.util.Collection[_getBeamProcessByPurpose__T], typing.Sequence[_getBeamProcessByPurpose__T]], beamProcessPurpose: BeamProcessPurpose) -> _getBeamProcessByPurpose__T: ...

class BeamProcessTypeCategory(java.lang.Enum['BeamProcessTypeCategory']):
    """
    Java class 'cern.lsa.domain.settings.type.BeamProcessTypeCategory'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        FUNCTION_BEAM_IN (cern.lsa.domain.settings.type.BeamProcessTypeCategory): final static enum constant
        FUNCTION_BEAM_OUT (cern.lsa.domain.settings.type.BeamProcessTypeCategory): final static enum constant
        DISCRETE (cern.lsa.domain.settings.type.BeamProcessTypeCategory): final static enum constant
    
    """
    FUNCTION_BEAM_IN: typing.ClassVar['BeamProcessTypeCategory'] = ...
    FUNCTION_BEAM_OUT: typing.ClassVar['BeamProcessTypeCategory'] = ...
    DISCRETE: typing.ClassVar['BeamProcessTypeCategory'] = ...
    def isBeamIn(self) -> bool: ...
    def isBeamOut(self) -> bool: ...
    def isDiscrete(self) -> bool: ...
    def isFunction(self) -> bool: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'BeamProcessTypeCategory': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['BeamProcessTypeCategory']: ...

class BeamProcessTypeSegmentAttribute(cern.lsa.domain.commons.Attribute):
    """
    Java class 'cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute'
    
        Interfaces:
            cern.lsa.domain.commons.Attribute
    
    """
    def getAttributeDefinition(self) -> 'BeamProcessTypeSegmentAttributeDefinition': ...
    def getSegmentIndex(self) -> int: ...

class BeamProcessTypeSegmentAttributeDefinition(cern.lsa.domain.commons.AttributeDefinition):
    """
    Java class 'cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition'
    
        Interfaces:
            cern.lsa.domain.commons.AttributeDefinition
    
    """
    def getSegmentId(self) -> int: ...
    def getSegmentName(self) -> str: ...

class BeamProcessTypeSegmentAttributes:
    """
    Java class 'cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributes'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * BeamProcessTypeSegmentAttributes()
    
    """
    def __init__(self): ...
    @staticmethod
    def getSegmentNames(collection: typing.Union[java.util.Collection[BeamProcessTypeSegmentAttributeDefinition], typing.Sequence[BeamProcessTypeSegmentAttributeDefinition]]) -> java.util.SortedSet[str]: ...
    @staticmethod
    def mapAttributeDefinitionsBySegmentName(collection: typing.Union[java.util.Collection[BeamProcessTypeSegmentAttributeDefinition], typing.Sequence[BeamProcessTypeSegmentAttributeDefinition]]) -> java.util.Map[str, java.util.Set[BeamProcessTypeSegmentAttributeDefinition]]: ...

class BeamProcessTypeSegments:
    """
    Java class 'cern.lsa.domain.settings.type.BeamProcessTypeSegments'
    
    """
    def getAttributeDoubleValue(self, int: int, string: str) -> float: ...
    def getAttributeDoubleValues(self, string: str) -> typing.List[float]: ...
    def getAttributeNames(self, int: int) -> java.util.Set[str]: ...
    def getAttributeStringValue(self, int: int, string: str) -> str: ...
    def getAttributes(self) -> java.util.List[BeamProcessTypeSegmentAttribute]: ...
    def getSegmentCount(self) -> int: ...
    def getSegmentName(self, int: int) -> str: ...
    def hasAttribute(self, int: int, string: str) -> bool: ...

class ContextType(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named, java.lang.Comparable['ContextType']):
    """
    Java class 'cern.lsa.domain.settings.type.ContextType'
    
        Interfaces:
            cern.lsa.domain.commons.IdentifiedEntity,
            cern.accsoft.commons.util.Named, java.lang.Comparable
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getContextCategory(self) -> cern.lsa.domain.settings.ContextCategory: ...
    def getCreationDate(self) -> java.util.Date: ...
    def getDescription(self) -> str: ...
    def getLength(self) -> int: ...

class CycleTypeAttribute(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.lsa.domain.settings.type.CycleTypeAttribute'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getDescription(self) -> str: ...
    def getValue(self) -> cern.accsoft.commons.value.ImmutableScalar: ...

class IncorporationBounds:
    """
    Java class 'cern.lsa.domain.settings.type.IncorporationBounds'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * IncorporationBounds()
    
    """
    def __init__(self): ...
    class Backward(java.lang.Enum['IncorporationBounds.Backward']):
        """
        Java class 'cern.lsa.domain.settings.type.IncorporationBounds$Backward'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            BP_START (cern.lsa.domain.settings.type.IncorporationBounds$Backward): final static enum constant
            RANGE_START (cern.lsa.domain.settings.type.IncorporationBounds$Backward): final static enum constant
            PREV_OPTIC (cern.lsa.domain.settings.type.IncorporationBounds$Backward): final static enum constant
            CUSTOM (cern.lsa.domain.settings.type.IncorporationBounds$Backward): final static enum constant
        
        """
        BP_START: typing.ClassVar['IncorporationBounds.Backward'] = ...
        RANGE_START: typing.ClassVar['IncorporationBounds.Backward'] = ...
        PREV_OPTIC: typing.ClassVar['IncorporationBounds.Backward'] = ...
        CUSTOM: typing.ClassVar['IncorporationBounds.Backward'] = ...
        @staticmethod
        def fromString(string: str) -> 'IncorporationBounds.Backward': ...
        def toString(self) -> str: ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'IncorporationBounds.Backward': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['IncorporationBounds.Backward']: ...
    class Forward(java.lang.Enum['IncorporationBounds.Forward']):
        """
        Java class 'cern.lsa.domain.settings.type.IncorporationBounds$Forward'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            BP_END (cern.lsa.domain.settings.type.IncorporationBounds$Forward): final static enum constant
            RANGE_END (cern.lsa.domain.settings.type.IncorporationBounds$Forward): final static enum constant
            NEXT_OPTIC (cern.lsa.domain.settings.type.IncorporationBounds$Forward): final static enum constant
            CUSTOM (cern.lsa.domain.settings.type.IncorporationBounds$Forward): final static enum constant
        
        """
        BP_END: typing.ClassVar['IncorporationBounds.Forward'] = ...
        RANGE_END: typing.ClassVar['IncorporationBounds.Forward'] = ...
        NEXT_OPTIC: typing.ClassVar['IncorporationBounds.Forward'] = ...
        CUSTOM: typing.ClassVar['IncorporationBounds.Forward'] = ...
        @staticmethod
        def fromString(string: str) -> 'IncorporationBounds.Forward': ...
        def toString(self) -> str: ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'IncorporationBounds.Forward': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['IncorporationBounds.Forward']: ...

class IncorporationRange:
    """
    Java class 'cern.lsa.domain.settings.type.IncorporationRange'
    
    """
    def clone(self) -> typing.Any: ...
    def getBackwardIncorporationRule(self) -> str: ...
    def getBackwardIncorporationRuleParameter(self) -> str: ...
    def getBeamProcessTypeName(self) -> str: ...
    def getEndTime(self) -> int: ...
    def getForwardIncorporationRule(self) -> str: ...
    def getForwardIncorporationRuleParameter(self) -> str: ...
    def getParameterGroupName(self) -> str: ...
    def getParameterTypeName(self) -> str: ...
    def getStartTime(self) -> int: ...
    def setBeamProcessTypeName(self, string: str) -> None: ...

class IncorporationRuleDescriptor:
    """
    Java class 'cern.lsa.domain.settings.type.IncorporationRuleDescriptor'
    
    """
    def getRuleName(self) -> str: ...
    def isParametrized(self) -> bool: ...

class TypeSchedulingItem:
    """
    Java class 'cern.lsa.domain.settings.type.TypeSchedulingItem'
    
      Attributes:
        SCHEDULING_START_TIME_COMPARATOR (java.util.Comparator): final static field
    
    """
    SCHEDULING_START_TIME_COMPARATOR: typing.ClassVar[java.util.Comparator] = ...
    def getScheduledType(self) -> ContextType: ...
    def getStartTime(self) -> int: ...

class BeamProcessType(ContextType):
    """
    Java class 'cern.lsa.domain.settings.type.BeamProcessType'
    
        Interfaces:
            cern.lsa.domain.settings.type.ContextType
    
    """
    def getCategory(self) -> BeamProcessTypeCategory: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...
    def getParticleType(self) -> cern.accsoft.commons.domain.ParticleType: ...
    def getPurpose(self) -> BeamProcessPurpose: ...
    def getSegments(self) -> BeamProcessTypeSegments: ...
    def isExplicit(self) -> bool: ...

class TypeScheduler(ContextType):
    """
    Java class 'cern.lsa.domain.settings.type.TypeScheduler'
    
        Interfaces:
            cern.lsa.domain.settings.type.ContextType
    
    """
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getSchedulings(self) -> java.util.List[TypeSchedulingItem]: ...

class CycleType(TypeScheduler, cern.lsa.domain.commons.AttributeAware):
    """
    Java class 'cern.lsa.domain.settings.type.CycleType'
    
        Interfaces:
            cern.lsa.domain.settings.type.TypeScheduler,
            cern.lsa.domain.commons.AttributeAware
    
    """
    def getBeamProcessType(self, string: str) -> BeamProcessType: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings.type")``.

    BaseTypes: typing.Type[BaseTypes]
    BeamProcessPurpose: typing.Type[BeamProcessPurpose]
    BeamProcessPurposes: typing.Type[BeamProcessPurposes]
    BeamProcessType: typing.Type[BeamProcessType]
    BeamProcessTypeCategory: typing.Type[BeamProcessTypeCategory]
    BeamProcessTypeSegmentAttribute: typing.Type[BeamProcessTypeSegmentAttribute]
    BeamProcessTypeSegmentAttributeDefinition: typing.Type[BeamProcessTypeSegmentAttributeDefinition]
    BeamProcessTypeSegmentAttributes: typing.Type[BeamProcessTypeSegmentAttributes]
    BeamProcessTypeSegments: typing.Type[BeamProcessTypeSegments]
    ContextType: typing.Type[ContextType]
    CycleType: typing.Type[CycleType]
    CycleTypeAttribute: typing.Type[CycleTypeAttribute]
    IncorporationBounds: typing.Type[IncorporationBounds]
    IncorporationRange: typing.Type[IncorporationRange]
    IncorporationRuleDescriptor: typing.Type[IncorporationRuleDescriptor]
    TypeScheduler: typing.Type[TypeScheduler]
    TypeSchedulingItem: typing.Type[TypeSchedulingItem]
