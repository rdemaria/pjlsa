import cern.accsoft.commons.domain
import cern.lsa.domain.cern.settings.elena
import cern.lsa.domain.cern.timing
import cern.lsa.domain.commons.spi
import java.io
import java.time
import java.util
import javax.xml.bind.annotation.adapters
import typing



class AbstractElenaCycleSegment(cern.lsa.domain.cern.settings.elena.ElenaCycleSegment, java.io.Serializable):
    """
    public abstract class AbstractElenaCycleSegment extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Keep links to the neighbor segments plus common attributes.
    
        Also see:
            :meth:`~serialized`
    """
    def addTimingProcess(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess, duration: java.time.Duration, timingProcessAnchor: cern.lsa.domain.cern.timing.TimingProcessAnchor) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.addTimingProcess`
            Adds timing process that should be executed in this segment with specified offset with respect to the beginning of the
            segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.addTimingProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Parameters:
                timingProcess (:class:`~cern.lsa.domain.cern.timing.TimingProcess`): the process to be executed
                offset (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>`): offset (positive or negative) with respect to the beginning of this segment
                anchor (:class:`~cern.lsa.domain.cern.timing.TimingProcessAnchor`): indicates if the :code:`offsetInMillis` is relative to the start or end of the segment
        
        
        """
        ...
    def getAttribute(self, string: str) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getAttribute`
            Returns the attribute value bound with specified name or :code:`null` if no attribute is added with such name.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute
        
            Returns:
                value of the attribute (as given by the :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setAttribute`
                method) or :code:`null` if no attribute is defined with such name
        
        
        """
        ...
    def getAttributeNames(self) -> java.util.Set[str]: ...
    def getAttributes(self) -> java.util.Set['AbstractElenaCycleSegment.Attribute']: ...
    def getHarmonicNumber(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getHarmonicNumber`
            Returns the harmonic number for this segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getHarmonicNumber`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Returns:
                the harmonic number for this segment
        
        
        """
        ...
    def getLength(self) -> java.time.Duration:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getLength`
            Returns length of the segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Returns:
                length of the segment
        
        
        """
        ...
    def getLengthMillis(self) -> int:
        """
        
            Returns:
                length in milliseconds for JAXB
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def getScheduledTimingProcesses(self) -> java.util.Set[cern.lsa.domain.cern.timing.TimingProcessScheduling]: ...
    def getStartMomentum(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getStartMomentum`
            Returns momentum at the start of this segment which is equal to the end momentum of the previous segment.
        
            Note that the start momentum of the first segment is equal to the end momentum of the last segment in the cycle.
        
            The momentum is expressed in MeV * 100 e.g. for 3.5 GeV the method would return 350000.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getStartMomentum`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Returns:
                momentum at the start of this segment
        
        
        """
        ...
    def getStartTime(self) -> java.time.Duration:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getStartTime`
            Returns start time of this segment within the cycle, so the offset from the beginning of the cycle. The start time of
            the first ramp segment is 0, the start time of the following flat top segment is equal to the first ramp length, etc..
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getStartTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Returns:
                start time
        
        
        """
        ...
    def getType(self) -> cern.lsa.domain.cern.settings.elena.SegmentType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getType`
            Returns type of this segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getType`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Returns:
                non-null segment type
        
        
        """
        ...
    def isFirstSegmentInCycle(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.isFirstSegmentInCycle`
            Indicates if this segment is the first segment in the cycle.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.isFirstSegmentInCycle`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Returns:
                :code:`true` if it is the first segment, :code:`false` otherwise
        
        
        """
        ...
    def nextSegment(self) -> cern.lsa.domain.cern.settings.elena.ElenaCycleSegment:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.nextSegment`
            Returns next segment in the cycle. For the last segment in the cycle, the method returns the first segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.nextSegment`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Returns:
                next segment in the cycle or first segment for the last one
        
        
        """
        ...
    def previousSegment(self) -> cern.lsa.domain.cern.settings.elena.ElenaCycleSegment:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.previousSegment`
            Returns proceeding segment in the cycle. For the first segment in the cycle, the method returns the last segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.previousSegment`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Returns:
                proceeding segment in the cycle or last segment for the first one
        
        
        """
        ...
    def removeAttribute(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.removeAttribute`
            Removes attribute with specified name from this segment. If no such attribute is defined, the method does nothing.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.removeAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute to be removed
        
        
        """
        ...
    def removeTimingProcess(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.removeTimingProcess`
            Removes specified timing process from this segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.removeTimingProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Parameters:
                timingProcess (:class:`~cern.lsa.domain.cern.timing.TimingProcess`): the process to be removed
        
        
        """
        ...
    def setAttribute(self, string: str, string2: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setAttribute`
            Sets an attribute value for this segment. If a attribute of the same name is already bound to this segment, its value is
            replaced.
        
            If the value passed is :code:`null`, this has the same effect as calling
            :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.removeAttribute`.
        
            Attributes are used to program the Central Timing. Their values can be used for instance as payloads for certain timing
            events - see :meth:`~cern.lsa.domain.cern.timing.TimingEvent.getPayloadAttributeName`.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): non-null name of the attribute
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value of the attribute (can be :code:`null`).
        
        
        """
        ...
    def setAttributes(self, set: java.util.Set['AbstractElenaCycleSegment.Attribute']) -> None: ...
    def setHarmonicNumber(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setHarmonicNumber`
            Sets the harmonic number for this segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setHarmonicNumber`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Parameters:
                harmonicNumber (int): the new harmonic number for this segment
        
        
        """
        ...
    def setLength(self, duration: java.time.Duration) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setLength`
            Changes length of the segment to the specified one.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Parameters:
                newLength (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>`): new length
        
        
        """
        ...
    def setLengthMillis(self, long: int) -> None:
        """
        
            Parameters:
                lengthMillis (long): length in milliseconds from JAXB
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setName`
            Sets segment name.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the segment
        
        
        """
        ...
    class Attribute: ...

class ElenaCycleSerializer:
    """
    public final class ElenaCycleSerializer extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class responsible for converting :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure` to XML and
        vice versa using JAXB.
    """
    def __init__(self): ...
    def marshal(self, elenaCycleStructure: cern.lsa.domain.cern.settings.elena.ElenaCycleStructure) -> str: ...
    def unmarshal(self, string: str) -> 'ElenaCycleStructureImpl': ...

class ElenaCycleStructureImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedEntity['ElenaCycleStructureImpl'], cern.lsa.domain.cern.settings.elena.ElenaCycleStructure, java.io.Serializable):
    """
    public class ElenaCycleStructureImpl extends cern.lsa.domain.commons.spi.AbstractIdentifiedEntity<:class:`~cern.lsa.domain.cern.settings.spi.elena.ElenaCycleStructureImpl`> implements :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, list: java.util.List[cern.lsa.domain.cern.settings.elena.ElenaCycleSegment], particleType: cern.accsoft.commons.domain.ParticleType, injectionMode: cern.lsa.domain.cern.settings.elena.InjectionMode): ...
    def getId(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getId`
            Returns ID of the cycle structure version.
        
            The returned ID corresponds to the ID of the underlying Setting.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getId`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`
        
            Specified by:
                :code:`getId` in interface :code:`cern.lsa.domain.commons.IdentifiedEntity`
        
            Overrides:
                :code:`getId` in class :class:`~cern.lsa.domain.cern.settings.spi.elena.ElenaCycleStructureImpl`
        
        
        """
        ...
    def getInjectionMode(self) -> cern.lsa.domain.cern.settings.elena.InjectionMode:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getInjectionMode`
            Returns the injection mode of the cycle.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getInjectionMode`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`
        
            Returns:
                the injection mode of the cycle
        
        
        """
        ...
    def getLength(self) -> java.time.Duration:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getLength`
            Returns the total length of the cycle including ramp segment roundings.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`
        
            Returns:
                the total length of the cycle
        
        
        """
        ...
    def getParticleType(self) -> cern.accsoft.commons.domain.ParticleType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getParticleType`
            Returns the particle type of the cycle.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getParticleType`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`
        
            Returns:
                the particle type of the cycle
        
        
        """
        ...
    def getSegments(self) -> java.util.List[cern.lsa.domain.cern.settings.elena.ElenaCycleSegment]: ...
    def getSegmentsCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getSegmentsCount`
            Returns the total number of segments in the cycle.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getSegmentsCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`
        
            Returns:
                the total number of segments in the cycle
        
        
        """
        ...
    def getVersion(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getVersion`
            Returns the current version of the cycle. The version is increased by 1 every time the cycle is changed and sent to the
            Central Timing
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.getVersion`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`
        
            Returns:
                current version of the cycle
        
        
        """
        ...
    def insertFlatSegment(self, rampSegment: cern.lsa.domain.cern.settings.elena.RampSegment, int: int) -> cern.lsa.domain.cern.settings.elena.FlatSegment:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.insertFlatSegment`
            Creates and inserts a flat segment into the specified ramp segment at the specified energy level.
        
            The returned segment has a default length of 0. It can be changed with
            :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.setLength` method.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.insertFlatSegment`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`
        
            Parameters:
                destRampSegment (:class:`~cern.lsa.domain.cern.settings.elena.RampSegment`): the ramp segment where the flat top should be inserted into
                rampEnergy (int): ramp the energy level at which the flat segment should be inserted
        
            Returns:
                the inserted flat segment
        
        
        """
        ...
    def removeFlatSegment(self, flatSegment: cern.lsa.domain.cern.settings.elena.FlatSegment) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.removeFlatSegment`
            Removes the specified flat segment. Note that removing the last flat segment is not allowed.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.removeFlatSegment`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`
        
            Parameters:
                flatSegment (:class:`~cern.lsa.domain.cern.settings.elena.FlatSegment`): the segment to be removed
        
        
        """
        ...
    def setInjectionMode(self, injectionMode: cern.lsa.domain.cern.settings.elena.InjectionMode) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.setInjectionMode`
            Sets the injection mode of the cycle.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.setInjectionMode`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`
        
            Parameters:
                injectionMode (:class:`~cern.lsa.domain.cern.settings.elena.InjectionMode`): the injection mode of the cycle
        
        
        """
        ...
    def setParticleType(self, particleType: cern.accsoft.commons.domain.ParticleType) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.setParticleType`
            Sets the particle type of the cycle.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure.setParticleType`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleStructure`
        
            Parameters:
                particleType (cern.accsoft.commons.domain.ParticleType): the particle type of the cycle
        
        
        """
        ...
    def setSegments(self, list: java.util.List[cern.lsa.domain.cern.settings.elena.ElenaCycleSegment]) -> None: ...
    def setVersion(self, int: int) -> None:
        """
        
            Parameters:
                version (int): set by JAXB when reading from XML
        
        
        """
        ...

class ParticleTypeToStringAdapter(javax.xml.bind.annotation.adapters.XmlAdapter[str, cern.accsoft.commons.domain.ParticleType]):
    """
    public class ParticleTypeToStringAdapter extends `XmlAdapter <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/xml/bind/annotation/adapters/XmlAdapter.html?is-external=true>`<`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`, cern.accsoft.commons.domain.ParticleType>
    
        Marshal/Unmarshal a @:code:`ParticleType` to a `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`
    """
    def __init__(self): ...
    def marshal(self, particleType: cern.accsoft.commons.domain.ParticleType) -> str:
        """
        
            Specified by:
                 in class 
        
        
        """
        ...
    def unmarshal(self, string: str) -> cern.accsoft.commons.domain.ParticleType:
        """
        
            Specified by:
                 in class 
        
        
        """
        ...

class FlatSegmentImpl(AbstractElenaCycleSegment, cern.lsa.domain.cern.settings.elena.FlatSegment):
    """
    public class FlatSegmentImpl extends :class:`~cern.lsa.domain.cern.settings.spi.elena.AbstractElenaCycleSegment` implements :class:`~cern.lsa.domain.cern.settings.elena.FlatSegment`
    
        Represents segment of type :meth:`~cern.lsa.domain.cern.settings.elena.SegmentType.FLAT`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, duration: java.time.Duration): ...
    def getEndMomentum(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getEndMomentum`
            Returns the momentum at the end of the segment.
        
            The momentum is expressed in MeV * 100 e.g. for 3.5 GeV the method would return 350000.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getEndMomentum`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Returns:
                the momentum at the end of the segment
        
        
        """
        ...
    def getPauseLocation(self) -> cern.lsa.domain.cern.settings.elena.PauseLocation:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.FlatSegment.getPauseLocation`
            Returns the pause location for this segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.FlatSegment.getPauseLocation`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.FlatSegment`
        
            Returns:
                the pause location for this segment
        
        
        """
        ...
    def setPauseLocation(self, pauseLocation: cern.lsa.domain.cern.settings.elena.PauseLocation) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.FlatSegment.setPauseLocation`
            Sets pause location (or lack of pause) in this segment.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.FlatSegment.setPauseLocation`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.FlatSegment`
        
            Parameters:
                pauseLocation (:class:`~cern.lsa.domain.cern.settings.elena.PauseLocation`): new pause location
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class RampSegmentImpl(AbstractElenaCycleSegment, cern.lsa.domain.cern.settings.elena.RampSegment):
    """
    public class RampSegmentImpl extends :class:`~cern.lsa.domain.cern.settings.spi.elena.AbstractElenaCycleSegment` implements :class:`~cern.lsa.domain.cern.settings.elena.RampSegment`
    
        Represents segment of type :meth:`~cern.lsa.domain.cern.settings.elena.SegmentType.RAMP`.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, duration: java.time.Duration): ...
    def getEndMomentum(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getEndMomentum`
            Returns the momentum at the end of the segment.
        
            The momentum is expressed in MeV * 100 e.g. for 3.5 GeV the method would return 350000.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getEndMomentum`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment`
        
            Returns:
                the momentum at the end of the segment
        
        
        """
        ...
    def getFlatPartLength(self) -> java.time.Duration:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.RampSegment.getFlatPartLength`
            Returns length of the flat part inserted at the join with the following flat segment. See "ELENA Cycle Specification"
            document for details.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.RampSegment.getFlatPartLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.RampSegment`
        
            Returns:
                flat part length
        
        
        """
        ...
    def getFlatPartLengthMillis(self) -> int:
        """
        
            Returns:
                flat part length in milliseconds for JAXB
        
        
        """
        ...
    def getRoundPartLength(self) -> java.time.Duration:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.RampSegment.getRoundPartLength`
            Returns length of the rounding part that is inserted at the join with the previous and following flat part. See "ELENA
            Cycle Specification" document for details.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.RampSegment.getRoundPartLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.RampSegment`
        
            Returns:
                round part length
        
        
        """
        ...
    def getRoundPartLengthMillis(self) -> int:
        """
        
            Returns:
                round part length in milliseconds for JAXB
        
        
        """
        ...
    def setEndMomentum(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.elena.RampSegment.setEndMomentum`
            Changes end momentum of the segment to the specified one. Note that changing the end momentum of one segment will modify
            also the momentum of the following segments.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.RampSegment.setEndMomentum`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.RampSegment`
        
            Parameters:
                newEnergy (int): the new momentum expressed in MeV * 100
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.elena.ElenaCycleSegment.getEndMomentum`
        
        
        """
        ...
    def setFlatPartLength(self, duration: java.time.Duration) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.RampSegment.setFlatPartLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.RampSegment`
        
            Parameters:
                newLength (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>`): the new length of the flat part added to before and after rounding part
        
        
        """
        ...
    def setFlatPartLengthMillis(self, long: int) -> None:
        """
        
            Parameters:
                flatPartLengthMillis (long): flat part length in milliseconds from JAXB
        
        
        """
        ...
    def setRoundPartLength(self, duration: java.time.Duration) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.elena.RampSegment.setRoundPartLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.elena.RampSegment`
        
            Parameters:
                newLength (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>`): the new length of the round part added at the join with neighbor flat parts
        
        
        """
        ...
    def setRoundPartLengthMillis(self, long: int) -> None:
        """
        
            Parameters:
                roundLengthMillis (long): round part length in milliseconds from JAXB
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.settings.spi.elena")``.

    AbstractElenaCycleSegment: typing.Type[AbstractElenaCycleSegment]
    ElenaCycleSerializer: typing.Type[ElenaCycleSerializer]
    ElenaCycleStructureImpl: typing.Type[ElenaCycleStructureImpl]
    FlatSegmentImpl: typing.Type[FlatSegmentImpl]
    ParticleTypeToStringAdapter: typing.Type[ParticleTypeToStringAdapter]
    RampSegmentImpl: typing.Type[RampSegmentImpl]
