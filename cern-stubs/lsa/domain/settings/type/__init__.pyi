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
    public class BaseTypes extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class for BaseTypes.
    """
    BASE_TYPE_NAME_COMPARATOR: typing.ClassVar[java.util.Comparator] = ...
    """
    public static final `Comparator <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Comparator.html?is-external=true>`<:class:`~cern.lsa.domain.settings.type.ContextType`> BASE_TYPE_NAME_COMPARATOR
    
        Comparator to compare two BaseTypes (sorts them by name)
    
    """
    @staticmethod
    def isPreCycling(beamProcessType: 'BeamProcessType') -> bool:
        """
            Returns :code:`true` if given beam process type represents pre-cycling type. The check is done based on first segment
            name of this type. If first segment name equals to :code:`LHC_PRECYCLING` - the method returns :code:`true`, otherwise
            :code:`false`.
        
            Parameters:
                bpType (:class:`~cern.lsa.domain.settings.type.BeamProcessType`): beam process type to be examined
        
            Returns:
                :code:`true` if specified beam process type represents pre-cycling type.
        
        
        """
        ...

class BeamProcessPurpose(cern.accsoft.commons.util.Named):
    """
    public interface BeamProcessPurpose extends cern.accsoft.commons.util.Named
    
        Describes the purpose of a :class:`~cern.lsa.domain.settings.BeamProcess`.
    """
    def isDefault(self) -> bool:
        """
        
            Returns:
                true if this :class:`~cern.lsa.domain.settings.type.BeamProcessPurpose` is default, false otherwise
        
        
        """
        ...

class BeamProcessPurposes:
    """
    public final class BeamProcessPurposes extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    _filterBeamProcessesByPurposes__T = typing.TypeVar('_filterBeamProcessesByPurposes__T', bound=cern.lsa.domain.settings.BeamProcess)  # <T>
    @staticmethod
    def filterBeamProcessesByPurposes(collection: typing.Union[java.util.Collection[_filterBeamProcessesByPurposes__T], typing.Sequence[_filterBeamProcessesByPurposes__T]], collection2: typing.Union[java.util.Collection[BeamProcessPurpose], typing.Sequence[BeamProcessPurpose]]) -> java.util.Collection[_filterBeamProcessesByPurposes__T]: ...
    _getBeamProcessByPurpose__T = typing.TypeVar('_getBeamProcessByPurpose__T', bound=cern.lsa.domain.settings.BeamProcess)  # <T>
    @staticmethod
    def getBeamProcessByPurpose(collection: typing.Union[java.util.Collection[_getBeamProcessByPurpose__T], typing.Sequence[_getBeamProcessByPurpose__T]], beamProcessPurpose: BeamProcessPurpose) -> _getBeamProcessByPurpose__T: ...

class BeamProcessTypeCategory(java.lang.Enum['BeamProcessTypeCategory']):
    """
    public enum BeamProcessTypeCategory extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.settings.type.BeamProcessTypeCategory`>
    
        Enumeration of possible beam process type categories.
    """
    FUNCTION_BEAM_IN: typing.ClassVar['BeamProcessTypeCategory'] = ...
    FUNCTION_BEAM_OUT: typing.ClassVar['BeamProcessTypeCategory'] = ...
    DISCRETE: typing.ClassVar['BeamProcessTypeCategory'] = ...
    def isBeamIn(self) -> bool:
        """
            Returns true if this category is FUNCTION_BEAM_IN
        
            Returns:
                true if this category is FUNCTION_BEAM_IN
        
        
        """
        ...
    def isBeamOut(self) -> bool:
        """
            Returns true if this category is FUNCTION_BEAM_OUT
        
            Returns:
                true if this category is FUNCTION_BEAM_OUT
        
        
        """
        ...
    def isDiscrete(self) -> bool:
        """
            Returns true if this category is DISCRETE
        
            Returns:
                true if this category is DISCRETE
        
        
        """
        ...
    def isFunction(self) -> bool:
        """
            Returns true if this category is FUNCTION (beam in or out)
        
            Returns:
                true if this category is FUNCTION (beam in or out)
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'BeamProcessTypeCategory':
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
    def values() -> typing.List['BeamProcessTypeCategory']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (BeamProcessTypeCategory c : BeamProcessTypeCategory.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class BeamProcessTypeSegmentAttribute(cern.lsa.domain.commons.Attribute):
    """
    public interface BeamProcessTypeSegmentAttribute extends :class:`~cern.lsa.domain.commons.Attribute`
    
        Extension of the :class:`~cern.lsa.domain.commons.Attribute` interface to provide additional information related to Beam
        Process Type Segments
    """
    def getAttributeDefinition(self) -> 'BeamProcessTypeSegmentAttributeDefinition':
        """
            Gets extended attribute definition
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.Attribute.getAttributeDefinition`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.Attribute`
        
            Returns:
                definition of the associated attribute
        
        
        """
        ...
    def getSegmentIndex(self) -> int:
        """
        
            Returns:
                segment number in which this value is defined within a beam process type
        
        
        """
        ...

class BeamProcessTypeSegmentAttributeDefinition(cern.lsa.domain.commons.AttributeDefinition):
    """
    public interface BeamProcessTypeSegmentAttributeDefinition extends :class:`~cern.lsa.domain.commons.AttributeDefinition`
    
        Extension of the :class:`~cern.lsa.domain.commons.AttributeDefinition` interface to provide additional information
        related to BeamProcessTypeSegment attributes
    """
    def getSegmentId(self) -> int:
        """
        
            Returns:
                returns the ID of the beam process type segment as stored in the DB
        
        
        """
        ...
    def getSegmentName(self) -> str:
        """
        
            Returns:
                Retrieves beam process type segment name this attribute definition is defined for
        
        
        """
        ...

class BeamProcessTypeSegmentAttributes:
    """
    public abstract class BeamProcessTypeSegmentAttributes extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Provides static methods to be used when working with :code:`BeamProcessTypeSegmentAttribute`s
    """
    def __init__(self): ...
    @staticmethod
    def getSegmentNames(collection: typing.Union[java.util.Collection[BeamProcessTypeSegmentAttributeDefinition], typing.Sequence[BeamProcessTypeSegmentAttributeDefinition]]) -> java.util.SortedSet[str]: ...
    @staticmethod
    def mapAttributeDefinitionsBySegmentName(collection: typing.Union[java.util.Collection[BeamProcessTypeSegmentAttributeDefinition], typing.Sequence[BeamProcessTypeSegmentAttributeDefinition]]) -> java.util.Map[str, java.util.Set[BeamProcessTypeSegmentAttributeDefinition]]: ...

class BeamProcessTypeSegments:
    """
    public interface BeamProcessTypeSegments
    
        Represents the segments within a beam process type.
    """
    def getAttributeDoubleValue(self, int: int, string: str) -> float:
        """
            Returns the matching attribute value of this beam process type or NaN if no attribute of that name and index is found.
        
            Parameters:
                segmentIndex (int): the index of the segment where to look for the attribute
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the attribute to return
        
            Returns:
                the matching attribute or null
        
        
        """
        ...
    def getAttributeDoubleValues(self, string: str) -> typing.List[float]:
        """
            Returns the value of the matching attribute for all segments. If the attribute name if not defined for one or more
            segment(s), Double.NaN will be found in the resulting array. The resulting array is guaranted to be non null and of same
            size as the number of segments
        
            Parameters:
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the attribute to return
        
            Returns:
                the array of values for the attribute of given name for all segments
        
        
        """
        ...
    def getAttributeNames(self, int: int) -> java.util.Set[str]: ...
    def getAttributeStringValue(self, int: int, string: str) -> str:
        """
            Returns the matching attribute value of this beam process type or null if no attribute of that name and index is found.
        
            Parameters:
                segmentIndex (int): the index of the segment where to look for the attribute
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the attribute to return
        
            Returns:
                the matching attribute or null
        
        
        """
        ...
    def getAttributes(self) -> java.util.List[BeamProcessTypeSegmentAttribute]: ...
    def getSegmentCount(self) -> int:
        """
            Returns the number of segment in that beam process type. A segment represents a period of time over the beam process
            type duration where parameters have the same value
        
            Returns:
                the number of segment in that beam process type
        
        
        """
        ...
    def getSegmentName(self, int: int) -> str:
        """
            Returns the name of the segment at index segmentIndex
        
            Parameters:
                segmentIndex (int): the index of the segment where to look for the attribute
        
            Returns:
                the name of the segment at index segmentIndex
        
        
        """
        ...
    def hasAttribute(self, int: int, string: str) -> bool:
        """
            Returns true if the attribute of given name exists for the given segment
        
            Parameters:
                segmentIndex (int): the index of the segment where to look for the attribute
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the attribute to return
        
            Returns:
                true if the attribute of given name exists for the given segment
        
        
        """
        ...

class ContextType(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named, java.lang.Comparable['ContextType']):
    """
    public interface ContextType extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`, cern.accsoft.commons.util.Named, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.settings.type.ContextType`>
    
        Represents type of a context. It's a base interface extended by all context types: :code:`BeamProcessType`,
        :code:`CycleType`.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
            Returns the accelerator this type is for
        
            Returns:
                the accelerator this type is for
        
        
        """
        ...
    def getContextCategory(self) -> cern.lsa.domain.settings.ContextCategory:
        """
            Returns category name which this context type belongs to.
        
            Returns:
                category name which this context type belongs to
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Returns the date when the type has been created.
        
            Returns:
                creation date
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Returns a description of this type entered by creator.
        
            Returns:
                a description of this type or :code:`null` if no description has been provided
        
        
        """
        ...
    def getLength(self) -> int:
        """
            Returns the length in time of the this type. The unit of the length may depend on the accelerator. Typically it is
            expressed in milliseconds but can be also in seconds.
        
            Returns:
                the length in time of this type
        
        
        """
        ...

class CycleTypeAttribute(cern.accsoft.commons.util.Named):
    """
    public interface CycleTypeAttribute extends cern.accsoft.commons.util.Named
    
        Represents a custom attribute of a cycle type that may be configured when cycle type is created and used by value
        generators or by make rules.
    
        Examples of cycle type attributes may be injection time, ramp start and end, extraction time etc.
    """
    def getDescription(self) -> str:
        """
            Returns optional description of the attribute.
        
            Returns:
                description
        
        
        """
        ...
    def getValue(self) -> cern.accsoft.commons.value.ImmutableScalar:
        """
            Returns value of the attribute.
        
            Returns:
                value of the attribute
        
        
        """
        ...

class IncorporationBounds:
    """
    public final class IncorporationBounds extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Defines function boundaries that incorporation rules should be limited by.
    
        In each incorporation range one can define in and out incorporation rule and its parameter. The incorporation rule
        parameter typically specifies the length (on X coordinate) on which the new value should be incorporated in the
        destination function. The length can be specified either by an absolute value (expressed in units of the X coordinates
        of the function - typically milliseconds or seconds) or by a relative value that depends on the considered beam process
        or incorporation range.
    
        This class is used to define the relative boundaries.
    """
    def __init__(self): ...
    class Backward(java.lang.Enum['IncorporationBounds.Backward']):
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
    public interface IncorporationRange
    
        Define a range of time in which given incorporation rules apply to incorporate the changes made to a point in the range
        into the function holding this point.
    """
    def clone(self) -> typing.Any:
        """
            Returns clone of this object.
        
        """
        ...
    def getBackwardIncorporationRule(self) -> str:
        """
            Returns the name of the incorporation rule to apply in this incorporation range to incorporate a point in the function
            for the part of the function before the moved point.
        
            Returns:
                the name of the incorporation rule to apply to incorporate the moved point before
        
        
        """
        ...
    def getBackwardIncorporationRuleParameter(self) -> str:
        """
            Returns an optional parameter to the backward incorporation rule.
        
            Returns:
                the optional parameter to the backward incorporation rule or null.
        
        
        """
        ...
    def getBeamProcessTypeName(self) -> str:
        """
            Returns the beam process type name
        
            Returns:
                the beam process type name
        
        
        """
        ...
    def getEndTime(self) -> int:
        """
            Returns the end time of this incorporation range in ms
        
            Returns:
                the end time of this incorporation range in ms
        
        
        """
        ...
    def getForwardIncorporationRule(self) -> str:
        """
            Returns the name of the incorporation rule to apply in this incorporation range to incorporate a point in the function
            for the part of the function after the moved point.
        
            Returns:
                the name of the incorporation rule to apply to incorporate the moved point after
        
        
        """
        ...
    def getForwardIncorporationRuleParameter(self) -> str:
        """
            Returns an optional parameter to the forward incorporation rule.
        
            Returns:
                the optional parameter to the forward incorporation rule or null.
        
        
        """
        ...
    def getParameterGroupName(self) -> str:
        """
            Returns the parameter group name associated to this incorporation range. If it's null, it means this incorporation range
            isn't linked to a specific group.
        
            Returns:
        
        
        """
        ...
    def getParameterTypeName(self) -> str:
        """
            Returns parameter type name
        
            Returns:
                parameter type name
        
        
        """
        ...
    def getStartTime(self) -> int:
        """
            Returns the start time of this incorporation range in ms
        
            Returns:
                the start time of this incorporation range in ms
        
        
        """
        ...
    def setBeamProcessTypeName(self, string: str) -> None:
        """
            Sets the beam process type name
        
            Parameters:
                beamProcessTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...

class IncorporationRuleDescriptor:
    """
    public interface IncorporationRuleDescriptor
    
        Represents information describing rule: rule name and indicator whether rule has got parameters
    """
    def getRuleName(self) -> str:
        """
            Returns the name of the rule
        
            Returns:
                the name of the rule
        
        
        """
        ...
    def isParametrized(self) -> bool:
        """
            Returns true if rule has parameters
        
            Returns:
                true if rule has parameters
        
        
        """
        ...

class TypeSchedulingItem:
    """
    public interface TypeSchedulingItem
    
        Defines the interface for the scheduling of @link BeamProcessType objects
    """
    SCHEDULING_START_TIME_COMPARATOR: typing.ClassVar[java.util.Comparator] = ...
    """
    static final `Comparator <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Comparator.html?is-external=true>`<:class:`~cern.lsa.domain.settings.type.TypeSchedulingItem`> SCHEDULING_START_TIME_COMPARATOR
    
        A comparator that can be used to compare two sub contexts on their start time
    
    """
    def getScheduledType(self) -> ContextType:
        """
            Returns the scheduled type.
        
            Returns:
                the scheduled type
        
        
        """
        ...
    def getStartTime(self) -> int:
        """
            Returns the start time for a scheduled type in the scheduling type.
        
            Returns:
                the start time
        
        
        """
        ...

class BeamProcessType(ContextType):
    """
    public interface BeamProcessType extends :class:`~cern.lsa.domain.settings.type.ContextType`
    
        Represents type of a beam process.
    """
    def getCategory(self) -> BeamProcessTypeCategory:
        """
            Returns the non null category of this beam process type.
        
            Returns:
                the non null category of this beam process type.
        
        
        """
        ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
            Returns the name of the particle transfer this type is associated with
        
            Returns:
                the name of the particle transfer this type is associated with
        
        
        """
        ...
    def getParticleType(self) -> cern.accsoft.commons.domain.ParticleType:
        """
            Returns particle type associated with this beam process type.
        
            Returns:
                the particle type attached to this beam process type
        
        
        """
        ...
    def getPurpose(self) -> BeamProcessPurpose:
        """
            Returns the beamProcess purpose, defining e.g. if it is a RAMP, FLATTOP, etc.
        
            Returns:
                the beamProcess purpose
        
        
        """
        ...
    def getSegments(self) -> BeamProcessTypeSegments:
        """
            Returns the collection of segments defined for this beam process type
        
            Returns:
                the collection of segments defined for this beam process type
        
        
        """
        ...
    def isExplicit(self) -> bool:
        """
            Returns true, if a BP type was created explicitly (default). Only certain system-generated beam-out types will have
            explicitly == false
        
        """
        ...

class TypeScheduler(ContextType):
    """
    public interface TypeScheduler extends :class:`~cern.lsa.domain.settings.type.ContextType`
    
        An object implementing this interface is a type that schedule other types. Scheduled types and stored in a type
        scheduling object together with their start time. The type schedulings are ordered using
        :meth:`~cern.lsa.domain.settings.type.TypeSchedulingItem.SCHEDULING_START_TIME_COMPARATOR`
    """
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getSchedulings(self) -> java.util.List[TypeSchedulingItem]: ...

class CycleType(TypeScheduler, cern.lsa.domain.commons.AttributeAware):
    """
    public interface CycleType extends :class:`~cern.lsa.domain.settings.type.TypeScheduler`, :class:`~cern.lsa.domain.commons.AttributeAware`
    """
    def getBeamProcessType(self, string: str) -> BeamProcessType:
        """
            Finds the beam process type of given name amongst those that are scheduled
        
            Parameters:
                beamProcessTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the beam process type to find
        
            Returns:
                the beam process type of that name or null if none is found
        
        
        """
        ...


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
