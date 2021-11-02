import cern.lsa.domain.cern.settings.ad
import cern.lsa.domain.cern.timing
import cern.lsa.domain.commons.spi
import java.io
import java.lang
import java.util
import typing



class ADCycleSerializer:
    """
    public final class ADCycleSerializer extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class responsible for converting :class:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure` to XML and vice
        versa using JAXB.
    """
    def __init__(self): ...
    def marshal(self, adCycleStructure: cern.lsa.domain.cern.settings.ad.AdCycleStructure) -> str: ...
    def unmarshal(self, string: str) -> 'AdCycleStructureImpl': ...

class AbstractAdCycleSegment(cern.lsa.domain.cern.settings.ad.AdCycleSegment, java.io.Serializable):
    """
    public abstract class AbstractAdCycleSegment extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Keep links to the neighbor segments plus common attributes.
    
        Also see:
            :meth:`~serialized`
    """
    def addTimingProcess(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess, int: int, timingProcessAnchor: cern.lsa.domain.cern.timing.TimingProcessAnchor) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.addTimingProcess`
            Adds timing process that should be executed in this segment with specified offset with respect to the beginning of the
            segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.addTimingProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Parameters:
                process (:class:`~cern.lsa.domain.cern.timing.TimingProcess`): the process to be executed
                offsetInMillis (int): offset in milliseconds (positive or negative) with respect to the beginning of this segment
                anchor (:class:`~cern.lsa.domain.cern.timing.TimingProcessAnchor`): indicates if the :code:`offsetInMillis` is relative to the start or end of the segment
        
        
        """
        ...
    def getAttribute(self, string: str) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getAttribute`
            Returns the attribute value bound with specified name or :code:`null` if no attribute is added with such name.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute
        
            Returns:
                value of the attribute (as given by the :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.setAttribute` method) or
                :code:`null` if no attribute is defined with such name
        
        
        """
        ...
    def getAttributeNames(self) -> java.util.Set[str]: ...
    def getAttributes(self) -> java.util.Set['AbstractAdCycleSegment.Attribute']: ...
    def getInitialMomentum(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getInitialMomentum`
            Returns momentum at the beginning of this segment which is equal to the end momentum of the previous segment.
        
            Note that the initial momentum of the first segment is equal to the end momentum of the last segment in the cycle.
        
            The momentum is expressed in MeV * 100 e.g. for 3.5 GeV the method would return 350000.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getInitialMomentum`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
        
        """
        ...
    def getLength(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getLength`
            Returns length of the segment in milliseconds.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def getScheduledTimingProcesses(self) -> java.util.Set[cern.lsa.domain.cern.timing.TimingProcessScheduling]: ...
    def getStartTime(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getStartTime`
            Returns start time of this segment within the cycle. The start time of the first ramp segment is 0, the start time of
            the following flat top segment is equal to the first ramp length, etc..
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getStartTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Returns:
                start time in milliseconds
        
        
        """
        ...
    def getType(self) -> cern.lsa.domain.cern.settings.ad.SegmentType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getType`
            Returns type of this segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getType`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Returns:
                non-null segment type
        
        
        """
        ...
    def isFirstSegmentInCycle(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.isFirstSegmentInCycle`
            Indicates if this segment is the first ramp-up segment in the cycle.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.isFirstSegmentInCycle`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Returns:
                :code:`true` if it is the first segment, :code:`false` otherwise
        
        
        """
        ...
    def nextSegment(self) -> cern.lsa.domain.cern.settings.ad.AdCycleSegment:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.nextSegment`
            Returns next segment in the cycle. For the last segment in the cycle, the method returns the first segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.nextSegment`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
        
        """
        ...
    def previousSegment(self) -> cern.lsa.domain.cern.settings.ad.AdCycleSegment:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.previousSegment`
            Returns proceeding segment in the cycle. For the first segment in the cycle, the method returns the last segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.previousSegment`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
        
        """
        ...
    def removeAttribute(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.removeAttribute`
            Removes attribute with specified name from this segment. If no such attribute is defined, the method does nothing.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.removeAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute to be removed
        
        
        """
        ...
    def removeTimingProcess(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.removeTimingProcess`
            Removes specified timing process from this segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.removeTimingProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Parameters:
                process (:class:`~cern.lsa.domain.cern.timing.TimingProcess`): the process to be removed
        
        
        """
        ...
    def setAttribute(self, string: str, string2: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.setAttribute`
            Sets an attribute value for this segment. If a attribute of the same name is already bound to this segment, its value is
            replaced.
        
            If the value passed is :code:`null`, this has the same effect as calling
            :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.removeAttribute`.
        
            Attributes are used to program the Central Timing. Their values can be used for instance as payloads for certain timing
            events - see :meth:`~cern.lsa.domain.cern.timing.TimingEvent.getPayloadAttributeName`.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.setAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value of the attribute (can be :code:`null`).
        
        
        """
        ...
    def setAttributes(self, set: java.util.Set['AbstractAdCycleSegment.Attribute']) -> None: ...
    def setLength(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.setLength`
            Changes length of the segment to the specified one.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.setLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Parameters:
                newLength (int): new length in milliseconds
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Needed also by JAXB.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.setName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the segment
        
        
        """
        ...
    class Attribute: ...

class AdCycleStructureImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedEntity['AdCycleStructureImpl'], cern.lsa.domain.cern.settings.ad.AdCycleStructure, java.io.Serializable):
    """
    public class AdCycleStructureImpl extends cern.lsa.domain.commons.spi.AbstractIdentifiedEntity<:class:`~cern.lsa.domain.cern.settings.spi.ad.AdCycleStructureImpl`> implements :class:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    PARAMETER_CYCLE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETER_CYCLE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARAMETER_CYCLE_TEST: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETER_CYCLE_TEST
    
        Used to test AD Central Timing, make rules, cycle editor, etc.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, list: java.util.List[cern.lsa.domain.cern.settings.ad.AdCycleSegment]): ...
    @staticmethod
    def getCycleParameterName(boolean: bool) -> str: ...
    def getId(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getId`
            Returns ID of the cycle structure version.
        
            The returned ID corresponds to the ID of the underlying Setting.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getId`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure`
        
            Specified by:
                :code:`getId` in interface :code:`cern.lsa.domain.commons.IdentifiedEntity`
        
            Overrides:
                :code:`getId` in class :class:`~cern.lsa.domain.cern.settings.spi.ad.AdCycleStructureImpl`
        
        
        """
        ...
    def getLength(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getLength`
            Returns the total length of the cycle in milliseconds.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure`
        
        
        """
        ...
    def getSegment(self, int: int) -> cern.lsa.domain.cern.settings.ad.AdCycleSegment:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getSegment`
            Returns segment at given index.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getSegment`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure`
        
            Parameters:
                index (int): from 0 to :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getSegmentsCount` - 1
        
            Returns:
                ramp or one of flat segment types
        
        
        """
        ...
    def getSegments(self) -> java.util.List[cern.lsa.domain.cern.settings.ad.AdCycleSegment]: ...
    def getSegmentsCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getSegmentsCount`
            Returns the total number of segments in the cycle.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getSegmentsCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure`
        
        
        """
        ...
    def getVersion(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.getVersion`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure`
        
            Returns:
                current version of the cycle. The version is increased by 1 every time the cycle is changed and sent to the Central
                Timing
        
        
        """
        ...
    def insertFlatSegment(self, rampSegment: cern.lsa.domain.cern.settings.ad.RampSegment, int: int) -> cern.lsa.domain.cern.settings.ad.FlatSegment:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.insertFlatSegment`
            Creates and inserts a flat segment inside specified ramp and at specified time within the ramp.
        
            The returned segment has a default value of 0 ms. It can be changed with
            :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.setLength` method.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.insertFlatSegment`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure`
        
            Parameters:
                destRampSegment (:class:`~cern.lsa.domain.cern.settings.ad.RampSegment`): the ramp segment where the flat top should be inserted
                rampEnergy (int): ramp momentum at which the flat segment should be inserted
        
            Returns:
                the inserted flat segment
        
        
        """
        ...
    def isTestCycle(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.isTestCycle`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure`
        
            Returns:
                :code:`true` if this cycle structure comes from the special ADBEAM.TEST/Cycle parameter.
        
        
        """
        ...
    def removeFlatSegment(self, flatSegment: cern.lsa.domain.cern.settings.ad.FlatSegment) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.removeFlatSegment`
            Removes the specified flat segment. Note that removing the last flat segment is not allowed.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure.removeFlatSegment`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleStructure`
        
            Parameters:
                flatSegment (:class:`~cern.lsa.domain.cern.settings.ad.FlatSegment`): the segment to be removed
        
        
        """
        ...
    def setSegments(self, list: java.util.List[cern.lsa.domain.cern.settings.ad.AdCycleSegment]) -> None: ...
    def setTestCycle(self, boolean: bool) -> None: ...
    def setVersion(self, int: int) -> None:
        """
        
            Parameters:
                version (int): set by JAXB when reading from XML
        
        
        """
        ...

class SettingsUpdateState(java.lang.Enum['SettingsUpdateState']):
    """
    public enum SettingsUpdateState extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.spi.ad.SettingsUpdateState`>
    """
    CURRENT_SETTINGS: typing.ClassVar['SettingsUpdateState'] = ...
    UPDATED_SETTINGS: typing.ClassVar['SettingsUpdateState'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SettingsUpdateState':
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
    def values() -> typing.List['SettingsUpdateState']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SettingsUpdateState c : SettingsUpdateState.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class FlatSegmentImpl(AbstractAdCycleSegment, cern.lsa.domain.cern.settings.ad.FlatSegment):
    """
    public class FlatSegmentImpl extends :class:`~cern.lsa.domain.cern.settings.spi.ad.AbstractAdCycleSegment` implements :class:`~cern.lsa.domain.cern.settings.ad.FlatSegment`
    
        Represents segment of type :meth:`~cern.lsa.domain.cern.settings.ad.SegmentType.FLAT`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    def getEndMomentum(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getEndMomentum`
            Returns the momentum at the end of the segment.
        
            The momentum is expressed in MeV * 100 e.g. for 3.5 GeV the method would return 350000.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getEndMomentum`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
        
        """
        ...
    def getPauseLocation(self) -> cern.lsa.domain.cern.settings.ad.PauseLocation:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.FlatSegment.getPauseLocation`
            Indicates if there is a pause configured for this segment and if yes, where it is located.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.FlatSegment.getPauseLocation`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.FlatSegment`
        
        
        """
        ...
    def getStartTime(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getStartTime`
            Returns start time of this segment within the cycle. The start time of the first ramp segment is 0, the start time of
            the following flat top segment is equal to the first ramp length, etc..
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getStartTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
            Overrides:
                :meth:`~cern.lsa.domain.cern.settings.spi.ad.AbstractAdCycleSegment.getStartTime`Â in
                classÂ :class:`~cern.lsa.domain.cern.settings.spi.ad.AbstractAdCycleSegment`
        
            Returns:
                start time in milliseconds
        
        
        """
        ...
    def setPauseLocation(self, pauseLocation: cern.lsa.domain.cern.settings.ad.PauseLocation) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.FlatSegment.setPauseLocation`
            Configures pause location (or lack of pause) in this segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.FlatSegment.setPauseLocation`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.FlatSegment`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class RampSegmentImpl(AbstractAdCycleSegment, cern.lsa.domain.cern.settings.ad.RampSegment):
    """
    public class RampSegmentImpl extends :class:`~cern.lsa.domain.cern.settings.spi.ad.AbstractAdCycleSegment` implements :class:`~cern.lsa.domain.cern.settings.ad.RampSegment`
    
        Represents segment of type :meth:`~cern.lsa.domain.cern.settings.ad.SegmentType.RAMP`.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, int: int): ...
    def getEndMomentum(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getEndMomentum`
            Returns the momentum at the end of the segment.
        
            The momentum is expressed in MeV * 100 e.g. for 3.5 GeV the method would return 350000.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getEndMomentum`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment`
        
        
        """
        ...
    def getFlatPartLength(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.RampSegment.getFlatPartLength`
            Returns length of the flat part inserted at the join with the following flat segment. See "AD Cycle Specification"
            document for details.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.RampSegment.getFlatPartLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.RampSegment`
        
            Returns:
                flat part length in ms
        
        
        """
        ...
    def getRoundPartLength(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.RampSegment.getRoundPartLength`
            Returns length of the rounding part that is inserted at the join with the previous and following flat part. See "AD
            Cycle Specification" document for details.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.RampSegment.getRoundPartLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.RampSegment`
        
            Returns:
                round part length in ms
        
        
        """
        ...
    def setEndMomentum(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.ad.RampSegment.setEndMomentum`
            Changes end momentum of the segment to the specified one. Note that changing the end momentum of one segment will modify
            also the momentum of the following segments.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.RampSegment.setEndMomentum`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.RampSegment`
        
            Parameters:
                newEnergy (int): the new momentum expressed in MeV * 100
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.ad.AdCycleSegment.getEndMomentum`
        
        
        """
        ...
    def setFlatPartLength(self, int: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.RampSegment.setFlatPartLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.RampSegment`
        
            Parameters:
                newLength (int): the new length of the flat part added to before and after rounding part
        
        
        """
        ...
    def setRoundPartLength(self, int: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ad.RampSegment.setRoundPartLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ad.RampSegment`
        
            Parameters:
                newLength (int): the new length of the round part added at the join with neighbor flat parts
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.settings.spi.ad")``.

    ADCycleSerializer: typing.Type[ADCycleSerializer]
    AbstractAdCycleSegment: typing.Type[AbstractAdCycleSegment]
    AdCycleStructureImpl: typing.Type[AdCycleStructureImpl]
    FlatSegmentImpl: typing.Type[FlatSegmentImpl]
    RampSegmentImpl: typing.Type[RampSegmentImpl]
    SettingsUpdateState: typing.Type[SettingsUpdateState]
