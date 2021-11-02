import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.cern.timing
import cern.lsa.domain.commons
import cern.lsa.domain.settings
import com.google.common.collect
import java.io
import java.lang
import java.time
import java.util
import typing



class ELTAG(java.lang.Enum['ELTAG']):
    """
    public enum ELTAG extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.elena.ELTAG`>
    
        Possible values of the TGM ELTAG group.
    """
    FT1: typing.ClassVar['ELTAG'] = ...
    FT2: typing.ClassVar['ELTAG'] = ...
    FT3: typing.ClassVar['ELTAG'] = ...
    FT4: typing.ClassVar['ELTAG'] = ...
    FTSP1: typing.ClassVar['ELTAG'] = ...
    FTSP2: typing.ClassVar['ELTAG'] = ...
    FTSP3: typing.ClassVar['ELTAG'] = ...
    FT2A: typing.ClassVar['ELTAG'] = ...
    FT2B: typing.ClassVar['ELTAG'] = ...
    FT3A: typing.ClassVar['ELTAG'] = ...
    FT3B: typing.ClassVar['ELTAG'] = ...
    FT3C: typing.ClassVar['ELTAG'] = ...
    FT3D: typing.ClassVar['ELTAG'] = ...
    FT4A: typing.ClassVar['ELTAG'] = ...
    FT4B: typing.ClassVar['ELTAG'] = ...
    FT4C: typing.ClassVar['ELTAG'] = ...
    RMP: typing.ClassVar['ELTAG'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ELTAG':
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
    def values() -> typing.List['ELTAG']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ELTAG c : ELTAG.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ElenaCycleSegment(cern.accsoft.commons.util.Named):
    """
    public interface ElenaCycleSegment extends cern.accsoft.commons.util.Named
    
        Represents a single segment of ELENA cycle being e.g. ramp, injection segment, flat top or extraction.
    """
    def addTimingProcess(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess, duration: java.time.Duration, timingProcessAnchor: cern.lsa.domain.cern.timing.TimingProcessAnchor) -> None:
        """
            Adds timing process that should be executed in this segment with specified offset with respect to the beginning of the
            segment.
        
            Parameters:
                timingProcess (:class:`~cern.lsa.domain.cern.timing.TimingProcess`): the process to be executed
                offset (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>`): offset (positive or negative) with respect to the beginning of this segment
                anchor (:class:`~cern.lsa.domain.cern.timing.TimingProcessAnchor`): indicates if the :code:`offsetInMillis` is relative to the start or end of the segment
        
        
        """
        ...
    def getAttribute(self, string: str) -> str:
        """
            Returns the attribute value bound with specified name or :code:`null` if no attribute is added with such name.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute
        
            Returns:
                value of the attribute (as given by the :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setAttribute`
                method) or :code:`null` if no attribute is defined with such name
        
        
        """
        ...
    def getAttributeNames(self) -> java.util.Set[str]: ...
    def getEndMomentum(self) -> int:
        """
            Returns the momentum at the end of the segment.
        
            The momentum is expressed in MeV * 100 e.g. for 3.5 GeV the method would return 350000.
        
            Returns:
                the momentum at the end of the segment
        
        
        """
        ...
    def getHarmonicNumber(self) -> int:
        """
            Returns the harmonic number for this segment.
        
            Returns:
                the harmonic number for this segment
        
        
        """
        ...
    def getLength(self) -> java.time.Duration:
        """
            Returns length of the segment.
        
            Returns:
                length of the segment
        
        
        """
        ...
    def getScheduledTimingProcesses(self) -> java.util.Set[cern.lsa.domain.cern.timing.TimingProcessScheduling]: ...
    def getStartMomentum(self) -> int:
        """
            Returns momentum at the start of this segment which is equal to the end momentum of the previous segment.
        
            Note that the start momentum of the first segment is equal to the end momentum of the last segment in the cycle.
        
            The momentum is expressed in MeV * 100 e.g. for 3.5 GeV the method would return 350000.
        
            Returns:
                momentum at the start of this segment
        
        
        """
        ...
    def getStartTime(self) -> java.time.Duration:
        """
            Returns start time of this segment within the cycle, so the offset from the beginning of the cycle. The start time of
            the first ramp segment is 0, the start time of the following flat top segment is equal to the first ramp length, etc..
        
            Returns:
                start time
        
        
        """
        ...
    def getType(self) -> 'SegmentType':
        """
            Returns type of this segment.
        
            Returns:
                non-null segment type
        
        
        """
        ...
    def isFirstSegmentInCycle(self) -> bool:
        """
            Indicates if this segment is the first segment in the cycle.
        
            Returns:
                :code:`true` if it is the first segment, :code:`false` otherwise
        
        
        """
        ...
    def nextSegment(self) -> 'ElenaCycleSegment':
        """
            Returns next segment in the cycle. For the last segment in the cycle, the method returns the first segment.
        
            Returns:
                next segment in the cycle or first segment for the last one
        
        
        """
        ...
    def previousSegment(self) -> 'ElenaCycleSegment':
        """
            Returns proceeding segment in the cycle. For the first segment in the cycle, the method returns the last segment.
        
            Returns:
                proceeding segment in the cycle or last segment for the first one
        
        
        """
        ...
    def removeAttribute(self, string: str) -> None:
        """
            Removes attribute with specified name from this segment. If no such attribute is defined, the method does nothing.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute to be removed
        
        
        """
        ...
    def removeTimingProcess(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess) -> None:
        """
            Removes specified timing process from this segment.
        
            Parameters:
                timingProcess (:class:`~cern.lsa.domain.cern.timing.TimingProcess`): the process to be removed
        
        
        """
        ...
    def setAttribute(self, string: str, string2: str) -> None:
        """
            Sets an attribute value for this segment. If a attribute of the same name is already bound to this segment, its value is
            replaced.
        
            If the value passed is :code:`null`, this has the same effect as calling
            :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.removeAttribute`.
        
            Attributes are used to program the Central Timing. Their values can be used for instance as payloads for certain timing
            events - see :meth:`~cern.lsa.domain.cern.timing.TimingEvent.getPayloadAttributeName`.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value of the attribute (can be :code:`null`).
        
        
        """
        ...
    def setHarmonicNumber(self, int: int) -> None:
        """
            Sets the harmonic number for this segment.
        
            Parameters:
                harmonicNumber (int): the new harmonic number for this segment
        
        
        """
        ...
    def setLength(self, duration: java.time.Duration) -> None:
        """
            Changes length of the segment to the specified one.
        
            Parameters:
                newLength (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>`): new length
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Sets segment name.
        
            Parameters:
                segmentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the segment
        
        
        """
        ...

class ElenaCycleSettings:
    """
    @Immutable public interface ElenaCycleSettings
    
        ELENA cycle settings
    """
    @staticmethod
    def builder() -> 'DefaultElenaCycleSettings.Builder': ...
    def getElenaCycleStructure(self) -> 'ElenaCycleStructure':
        """
        
            Returns:
                ELENA cycle structure
        
        
        """
        ...
    def getParameterToCorrectionFunction(self) -> java.util.Map[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]: ...
    def getParameterToTargetFunction(self) -> java.util.Map[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]: ...

class ElenaCycleStructure(cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface ElenaCycleStructure extends cern.lsa.domain.commons.IdentifiedEntity
    
        Represents the ELENA cycle structure describing all the ramp and flat segments, with their lengths, momentums and other
        attributes.
    
        Note that there are no methods that would allow creation of an ELENA cycle structure from scratch. The assumption (after
        confirmation with OP) is that we always start with an existing structure and we modify it by adding/removing flat
        segments.
    """
    def getId(self) -> int:
        """
            Returns ID of the cycle structure version.
        
            The returned ID corresponds to the ID of the underlying Setting.
        
            Specified by:
                :code:`getId` in interface :code:`cern.lsa.domain.commons.IdentifiedEntity`
        
        
        """
        ...
    def getInjectionMode(self) -> 'InjectionMode':
        """
            Returns the injection mode of the cycle.
        
            Returns:
                the injection mode of the cycle
        
        
        """
        ...
    def getLength(self) -> java.time.Duration:
        """
            Returns the total length of the cycle including ramp segment roundings.
        
            Returns:
                the total length of the cycle
        
        
        """
        ...
    def getParticleType(self) -> cern.accsoft.commons.domain.ParticleType:
        """
            Returns the particle type of the cycle.
        
            Returns:
                the particle type of the cycle
        
        
        """
        ...
    def getSegments(self) -> java.util.List[ElenaCycleSegment]: ...
    def getSegmentsCount(self) -> int:
        """
            Returns the total number of segments in the cycle.
        
            Returns:
                the total number of segments in the cycle
        
        
        """
        ...
    def getVersion(self) -> int:
        """
            Returns the current version of the cycle. The version is increased by 1 every time the cycle is changed and sent to the
            Central Timing
        
            Returns:
                current version of the cycle
        
        
        """
        ...
    def insertFlatSegment(self, rampSegment: 'RampSegment', int: int) -> 'FlatSegment':
        """
            Creates and inserts a flat segment into the specified ramp segment at the specified energy level.
        
            The returned segment has a default length of 0. It can be changed with
            :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setLength` method.
        
            Parameters:
                destRampSegment (:class:`~cern.lsa.domain.cern.settings.elena.RampSegment`): the ramp segment where the flat top should be inserted into
                rampMomentum (int): ramp the energy level at which the flat segment should be inserted
        
            Returns:
                the inserted flat segment
        
        
        """
        ...
    def removeFlatSegment(self, flatSegment: 'FlatSegment') -> None:
        """
            Removes the specified flat segment. Note that removing the last flat segment is not allowed.
        
            Parameters:
                flatSegment (:class:`~cern.lsa.domain.cern.settings.elena.FlatSegment`): the segment to be removed
        
            Raises:
                : if the given segment is :code:`null` or it is the last flat segment in the cycle
        
        
        """
        ...
    def setInjectionMode(self, injectionMode: 'InjectionMode') -> None:
        """
            Sets the injection mode of the cycle.
        
            Parameters:
                injectionMode (:class:`~cern.lsa.domain.cern.settings.elena.InjectionMode`): the injection mode of the cycle
        
        
        """
        ...
    def setParticleType(self, particleType: cern.accsoft.commons.domain.ParticleType) -> None:
        """
            Sets the particle type of the cycle.
        
            Parameters:
                particleType (cern.accsoft.commons.domain.ParticleType): the particle type of the cycle
        
        
        """
        ...

class InjectionMode(java.lang.Enum['InjectionMode']):
    """
    public enum InjectionMode extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.elena.InjectionMode`>
    
        ELENA injection modes.
    """
    AD: typing.ClassVar['InjectionMode'] = ...
    LOCAL_SOURCE: typing.ClassVar['InjectionMode'] = ...
    STANDALONE: typing.ClassVar['InjectionMode'] = ...
    def getTimingValue(self) -> str:
        """
        
            Returns:
                the corresponding value in ELENA timing
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'InjectionMode':
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
    def values() -> typing.List['InjectionMode']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (InjectionMode c : InjectionMode.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PauseLocation(java.lang.Enum['PauseLocation']):
    """
    public enum PauseLocation extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.elena.PauseLocation`>
    
        Represents location of a pause that can be set on a
        :meth:`~cern.lsa.domain.cern.settings.elena.FlatSegment.setPauseLocation`.
    """
    NONE: typing.ClassVar['PauseLocation'] = ...
    BEFORE_START: typing.ClassVar['PauseLocation'] = ...
    BEFORE_END: typing.ClassVar['PauseLocation'] = ...
    AFTER_END: typing.ClassVar['PauseLocation'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PauseLocation':
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
    def values() -> typing.List['PauseLocation']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (PauseLocation c : PauseLocation.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SegmentAttribute(java.lang.Enum['SegmentAttribute']):
    """
    public enum SegmentAttribute extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.elena.SegmentAttribute`>
    
        Definition of standard attributes of :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`.
    
        Also see:
            :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setAttribute`
    """
    ELTAG: typing.ClassVar['SegmentAttribute'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SegmentAttribute':
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
    def values() -> typing.List['SegmentAttribute']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SegmentAttribute c : SegmentAttribute.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SegmentType(java.lang.Enum['SegmentType']):
    """
    public enum SegmentType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.elena.SegmentType`>
    
        ELENA cycle segment types.
    """
    RAMP: typing.ClassVar['SegmentType'] = ...
    FLAT: typing.ClassVar['SegmentType'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SegmentType':
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
    def values() -> typing.List['SegmentType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SegmentType c : SegmentType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DefaultElenaCycleSettings(ElenaCycleSettings, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultElenaCycleSettings extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings`.
    
        Use the builder to create immutable instances: :code:`DefaultElenaCycleSettings.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultElenaCycleSettings.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.cern.settings.elena.DefaultElenaCycleSettings`.
        
            .. code-block: java
            
             DefaultElenaCycleSettings.builder()
                .elenaCycleStructure(cern.lsa.domain.cern.settings.elena.ElenaCycleStructure) // required :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings.getElenaCycleStructure`
                .putParameterToTargetFunction|putAllParameterToTargetFunction(cern.lsa.domain.settings.Parameter => cern.accsoft.commons.value.ImmutableDiscreteFunction) // :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings.getParameterToTargetFunction` mappings
                .putParameterToCorrectionFunction|putAllParameterToCorrectionFunction(cern.lsa.domain.settings.Parameter => cern.accsoft.commons.value.ImmutableDiscreteFunction) // :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings.getParameterToCorrectionFunction` mappings
                .build();
             
        
            Returns:
                A new DefaultElenaCycleSettings builder
        
        
        """
        ...
    @staticmethod
    def copyOf(elenaCycleSettings: ElenaCycleSettings) -> 'DefaultElenaCycleSettings':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings`): The instance to copy
        
            Returns:
                A copied immutable ElenaCycleSettings instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getElenaCycleStructure(self) -> ElenaCycleStructure:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings.getElenaCycleStructure`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings`
        
            Returns:
                ELENA cycle structure
        
        
        """
        ...
    def getParameterToCorrectionFunction(self) -> com.google.common.collect.ImmutableMap[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings.getParameterToCorrectionFunction`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings`
        
            Returns:
                parameters pointing to corresponding correction function (all functions must be provided)
        
        
        """
        ...
    def getParameterToTargetFunction(self) -> com.google.common.collect.ImmutableMap[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings.getParameterToTargetFunction`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings`
        
            Returns:
                parameters pointing to corresponding target function (functions to calculate the full hierarchy must be provided)
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`elenaCycleStructure`, :code:`parameterToTargetFunction`,
            :code:`parameterToCorrectionFunction`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ElenaCycleSettings` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withElenaCycleStructure(self, elenaCycleStructure: ElenaCycleStructure) -> 'DefaultElenaCycleSettings':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSettings.getElenaCycleStructure` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`): A new value for elenaCycleStructure
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParameterToCorrectionFunction(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]]) -> 'DefaultElenaCycleSettings': ...
    def withParameterToTargetFunction(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]]) -> 'DefaultElenaCycleSettings': ...
    class Builder:
        def build(self) -> 'DefaultElenaCycleSettings': ...
        def elenaCycleStructure(self, elenaCycleStructure: ElenaCycleStructure) -> 'DefaultElenaCycleSettings.Builder': ...
        def parameterToCorrectionFunction(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]]) -> 'DefaultElenaCycleSettings.Builder': ...
        def parameterToTargetFunction(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]]) -> 'DefaultElenaCycleSettings.Builder': ...
        def putAllParameterToCorrectionFunction(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]]) -> 'DefaultElenaCycleSettings.Builder': ...
        def putAllParameterToTargetFunction(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]]) -> 'DefaultElenaCycleSettings.Builder': ...
        @typing.overload
        def putParameterToCorrectionFunction(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> 'DefaultElenaCycleSettings.Builder': ...
        @typing.overload
        def putParameterToCorrectionFunction(self, entry: java.util.Map.Entry[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]) -> 'DefaultElenaCycleSettings.Builder': ...
        @typing.overload
        def putParameterToTargetFunction(self, parameter: cern.lsa.domain.settings.Parameter, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> 'DefaultElenaCycleSettings.Builder': ...
        @typing.overload
        def putParameterToTargetFunction(self, entry: java.util.Map.Entry[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunction]) -> 'DefaultElenaCycleSettings.Builder': ...

class FlatSegment(ElenaCycleSegment):
    """
    public interface FlatSegment extends :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
    
        Flat segment that has the same initial and end momentum.
    """
    def getPauseLocation(self) -> PauseLocation:
        """
            Returns the pause location for this segment.
        
            Returns:
                the pause location for this segment
        
        
        """
        ...
    def setPauseLocation(self, pauseLocation: PauseLocation) -> None:
        """
            Sets pause location (or lack of pause) in this segment.
        
            Parameters:
                pauseLocation (:class:`~cern.lsa.domain.cern.settings.elena.PauseLocation`): new pause location
        
        
        """
        ...

class RampSegment(ElenaCycleSegment):
    """
    public interface RampSegment extends :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
    
        Raising or falling segment of ELENA cycle. Energy at the start and end of the segment are different.
    """
    def getFlatPartLength(self) -> java.time.Duration:
        """
            Returns length of the flat part inserted at the join with the following flat segment. See "ELENA Cycle Specification"
            document for details.
        
            Returns:
                flat part length
        
        
        """
        ...
    def getRoundPartLength(self) -> java.time.Duration:
        """
            Returns length of the rounding part that is inserted at the join with the previous and following flat part. See "ELENA
            Cycle Specification" document for details.
        
            Returns:
                round part length
        
        
        """
        ...
    def setEndMomentum(self, int: int) -> None:
        """
            Changes end momentum of the segment to the specified one. Note that changing the end momentum of one segment will modify
            also the momentum of the following segments.
        
            Parameters:
                newMomentum (int): the new momentum expressed in MeV * 100
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getEndMomentum`
        
        
        """
        ...
    def setFlatPartLength(self, duration: java.time.Duration) -> None:
        """
        
            Parameters:
                newLength (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>`): the new length of the flat part added to before and after rounding part
        
        
        """
        ...
    def setRoundPartLength(self, duration: java.time.Duration) -> None:
        """
        
            Parameters:
                newLength (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>`): the new length of the round part added at the join with neighbor flat parts
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.settings.elena")``.

    DefaultElenaCycleSettings: typing.Type[DefaultElenaCycleSettings]
    ELTAG: typing.Type[ELTAG]
    ElenaCycleSegment: typing.Type[ElenaCycleSegment]
    ElenaCycleSettings: typing.Type[ElenaCycleSettings]
    ElenaCycleStructure: typing.Type[ElenaCycleStructure]
    FlatSegment: typing.Type[FlatSegment]
    InjectionMode: typing.Type[InjectionMode]
    PauseLocation: typing.Type[PauseLocation]
    RampSegment: typing.Type[RampSegment]
    SegmentAttribute: typing.Type[SegmentAttribute]
    SegmentType: typing.Type[SegmentType]
