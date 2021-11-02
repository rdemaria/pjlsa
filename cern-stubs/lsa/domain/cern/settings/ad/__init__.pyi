import cern.accsoft.commons.util
import cern.lsa.domain.cern.timing
import cern.lsa.domain.commons
import java.lang
import java.util
import typing



class AdCycleSegment(cern.accsoft.commons.util.Named):
    """
    public interface AdCycleSegment extends cern.accsoft.commons.util.Named
    
        Represents a single segment of AD cycle being e.g. ramp, injection segment, flat top or extraction.
    """
    def addTimingProcess(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess, int: int, timingProcessAnchor: cern.lsa.domain.cern.timing.TimingProcessAnchor) -> None:
        """
            Adds timing process that should be executed in this segment with specified offset with respect to the beginning of the
            segment.
        
            Parameters:
                process (:class:`~cern.lsa.domain.cern.timing.TimingProcess`): the process to be executed
                offsetInMillis (int): offset in milliseconds (positive or negative) with respect to the beginning of this segment
                anchor (:class:`~cern.lsa.domain.cern.timing.TimingProcessAnchor`): indicates if the :code:`offsetInMillis` is relative to the start or end of the segment
        
        
        """
        ...
    def getAttribute(self, string: str) -> str:
        """
            Returns the attribute value bound with specified name or :code:`null` if no attribute is added with such name.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute
        
            Returns:
                value of the attribute (as given by the :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.setAttribute` method) or
                :code:`null` if no attribute is defined with such name
        
        
        """
        ...
    def getAttributeNames(self) -> java.util.Set[str]: ...
    def getEndMomentum(self) -> int:
        """
            Returns the momentum at the end of the segment.
        
            The momentum is expressed in MeV * 100 e.g. for 3.5 GeV the method would return 350000.
        
        """
        ...
    def getInitialMomentum(self) -> int:
        """
            Returns momentum at the beginning of this segment which is equal to the end momentum of the previous segment.
        
            Note that the initial momentum of the first segment is equal to the end momentum of the last segment in the cycle.
        
            The momentum is expressed in MeV * 100 e.g. for 3.5 GeV the method would return 350000.
        
        """
        ...
    def getLength(self) -> int:
        """
            Returns length of the segment in milliseconds.
        
        """
        ...
    def getScheduledTimingProcesses(self) -> java.util.Set[cern.lsa.domain.cern.timing.TimingProcessScheduling]: ...
    def getStartTime(self) -> int:
        """
            Returns start time of this segment within the cycle. The start time of the first ramp segment is 0, the start time of
            the following flat top segment is equal to the first ramp length, etc..
        
            Returns:
                start time in milliseconds
        
        
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
            Indicates if this segment is the first ramp-up segment in the cycle.
        
            Returns:
                :code:`true` if it is the first segment, :code:`false` otherwise
        
        
        """
        ...
    def nextSegment(self) -> 'AdCycleSegment':
        """
            Returns next segment in the cycle. For the last segment in the cycle, the method returns the first segment.
        
        """
        ...
    def previousSegment(self) -> 'AdCycleSegment':
        """
            Returns proceeding segment in the cycle. For the first segment in the cycle, the method returns the last segment.
        
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
                process (:class:`~cern.lsa.domain.cern.timing.TimingProcess`): the process to be removed
        
        
        """
        ...
    def setAttribute(self, string: str, string2: str) -> None:
        """
            Sets an attribute value for this segment. If a attribute of the same name is already bound to this segment, its value is
            replaced.
        
            If the value passed is :code:`null`, this has the same effect as calling
            :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.removeAttribute`.
        
            Attributes are used to program the Central Timing. Their values can be used for instance as payloads for certain timing
            events - see :meth:`~cern.lsa.domain.cern.timing.TimingEvent.getPayloadAttributeName`.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value of the attribute (can be :code:`null`).
        
        
        """
        ...
    def setLength(self, int: int) -> None:
        """
            Changes length of the segment to the specified one.
        
            Parameters:
                newLength (int): new length in milliseconds
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
        
            Parameters:
                segmentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the segment
        
        
        """
        ...

class AdCycleStructure(cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface AdCycleStructure extends cern.lsa.domain.commons.IdentifiedEntity
    
        Represents the AD cycle structure describing all the ramp and flat segments, with their lengths, momentums and other
        attributes.
    
        Note that there are no methods that would allow creation of a AD cycle structure from scratch. The assumption (after
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
    def getLength(self) -> int:
        """
            Returns the total length of the cycle in milliseconds.
        
        """
        ...
    def getSegment(self, int: int) -> AdCycleSegment:
        """
            Returns segment at given index.
        
            Parameters:
                index (int): from 0 to :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getSegmentsCount` - 1
        
            Returns:
                ramp or one of flat segment types
        
        
        """
        ...
    def getSegments(self) -> java.util.List[AdCycleSegment]: ...
    def getSegmentsCount(self) -> int:
        """
            Returns the total number of segments in the cycle.
        
        """
        ...
    def getVersion(self) -> int:
        """
        
            Returns:
                current version of the cycle. The version is increased by 1 every time the cycle is changed and sent to the Central
                Timing
        
        
        """
        ...
    def insertFlatSegment(self, rampSegment: 'RampSegment', int: int) -> 'FlatSegment':
        """
            Creates and inserts a flat segment inside specified ramp and at specified time within the ramp.
        
            The returned segment has a default value of 0 ms. It can be changed with
            :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.setLength` method.
        
            Parameters:
                destRampSegment (:class:`~cern.lsa.domain.cern.settings.ad.RampSegment`): the ramp segment where the flat top should be inserted
                rampMomentum (int): ramp momentum at which the flat segment should be inserted
        
            Returns:
                the inserted flat segment
        
        
        """
        ...
    def isTestCycle(self) -> bool: ...
    def removeFlatSegment(self, flatSegment: 'FlatSegment') -> None:
        """
            Removes the specified flat segment. Note that removing the last flat segment is not allowed.
        
            Parameters:
                flatSegment (:class:`~cern.lsa.domain.cern.settings.ad.FlatSegment`): the segment to be removed
        
            Raises:
                : if the given segment is :code:`null` or it is the last flat segment in the cycle
        
        
        """
        ...

class PauseLocation(java.lang.Enum['PauseLocation']):
    """
    public enum PauseLocation extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.ad.PauseLocation`>
    
        Represents location of a pause that can be set on a
        :meth:`~cern.lsa.domain.cern.settings.ad.FlatSegment.setPauseLocation`.
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
    public enum SegmentAttribute extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.ad.SegmentAttribute`>
    
        Definition of standard attributes of :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`.
    
        Also see:
            :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.setAttribute`
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
    public enum SegmentType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.ad.SegmentType`>
    
        AD cycle segment types.
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

class FlatSegment(AdCycleSegment):
    """
    public interface FlatSegment extends :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
    
        Flat segment that has the same initial and end momentum.
    """
    def getPauseLocation(self) -> PauseLocation:
        """
            Indicates if there is a pause configured for this segment and if yes, where it is located.
        
        """
        ...
    def setPauseLocation(self, pauseLocation: PauseLocation) -> None:
        """
            Configures pause location (or lack of pause) in this segment.
        
        """
        ...

class RampSegment(AdCycleSegment):
    """
    public interface RampSegment extends :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
    
        Raising or falling segment of AD cycle. Energy at the start and end of the segment are different.
    """
    def getFlatPartLength(self) -> int:
        """
            Returns length of the flat part inserted at the join with the following flat segment. See "AD Cycle Specification"
            document for details.
        
            Returns:
                flat part length in ms
        
        
        """
        ...
    def getRoundPartLength(self) -> int:
        """
            Returns length of the rounding part that is inserted at the join with the previous and following flat part. See "AD
            Cycle Specification" document for details.
        
            Returns:
                round part length in ms
        
        
        """
        ...
    def setEndMomentum(self, int: int) -> None:
        """
            Changes end momentum of the segment to the specified one. Note that changing the end momentum of one segment will modify
            also the momentum of the following segments.
        
            Parameters:
                newMomentum (int): the new momentum expressed in MeV * 100
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getEndMomentum`
        
        
        """
        ...
    def setFlatPartLength(self, int: int) -> None:
        """
        
            Parameters:
                newLength (int): the new length of the flat part added to before and after rounding part
        
        
        """
        ...
    def setRoundPartLength(self, int: int) -> None:
        """
        
            Parameters:
                newLength (int): the new length of the round part added at the join with neighbor flat parts
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.settings.ad")``.

    AdCycleSegment: typing.Type[AdCycleSegment]
    AdCycleStructure: typing.Type[AdCycleStructure]
    FlatSegment: typing.Type[FlatSegment]
    PauseLocation: typing.Type[PauseLocation]
    RampSegment: typing.Type[RampSegment]
    SegmentAttribute: typing.Type[SegmentAttribute]
    SegmentType: typing.Type[SegmentType]
