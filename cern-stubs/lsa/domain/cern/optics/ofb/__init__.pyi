import cern.accsoft.commons.util
import cern.lsa.domain.commons
import cern.lsa.domain.optics
import java.io
import java.lang
import java.util
import typing



class OfbMonitorReading:
    """
    public interface OfbMonitorReading
    
        Represents a single reading of a BPM. Such a BPM reading has one reading for each plane and a validity flag for each
        BPM.
    """
    def getHorizontal(self) -> float:
        """
            Returns reading of the horizontal position of the beam.
        
            Returns:
                reading of the horizontal position of the beam
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isHorizontalValid`
        
        
        """
        ...
    def getMonitorName(self) -> str:
        """
            Returns name of the corresponding element.
        
            Returns:
                name of the corresponding element
        
        
        """
        ...
    def getPosition(self) -> float:
        """
            Returns position of the corresponding element.
        
            Returns:
                position of the corresponding element
        
        
        """
        ...
    def getVertical(self) -> float:
        """
            Returns reading of the vertical position of the beam.
        
            Returns:
                reading of the vertical position of the beam
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isVerticalValid`
        
        
        """
        ...
    def isHorizontalValid(self) -> bool:
        """
            Determines if the horizontal reading is valid and should be used by the orbit feedback system.
        
            Returns:
                :code:`true` if the horizontal reading is valid and should be used by the orbit feedback system
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getHorizontal`
        
        
        """
        ...
    def isVerticalValid(self) -> bool:
        """
            Determines if the vertical reading is valid and should be used by the orbit feedback system.
        
            Returns:
                :code:`true` if the vertical reading is valid and should be used by the orbit feedback system
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getVertical`,
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.setVerticalValid`
        
        
        """
        ...
    def setHorizontal(self, double: float) -> None:
        """
            Sets reading of the horizontal position of the beam at the element.
        
            Parameters:
                horizontal (double): horizontal position of the beam
        
        
        """
        ...
    def setHorizontalValid(self, boolean: bool) -> None:
        """
            Modifies the validity of the horizontal reading.
        
            Parameters:
                valid (boolean): The horizontalValid to set.
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isHorizontalValid`
        
        
        """
        ...
    def setVertical(self, double: float) -> None:
        """
            Sets reading of the vertical position of the beam.
        
            Parameters:
                vertical (double): vertical position of the beam.
        
        
        """
        ...
    def setVerticalValid(self, boolean: bool) -> None:
        """
            Modifies the validity of the vertical reading.
        
            Parameters:
                valid (boolean): The verticalValid to set.
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isVerticalValid`
        
        
        """
        ...

class OfbOpticsTableInfo:
    """
    @Immutable public interface OfbOpticsTableInfo
    """
    @staticmethod
    def builder() -> 'DefaultOfbOpticsTableInfo.Builder': ...
    def check(self) -> None: ...
    def getOfbRefOrbit(self, opticsTableItem: cern.lsa.domain.optics.OpticsTableItem) -> 'OfbOrbit':
        """
            Get the :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit` attached to a particular optics table item, or :code:`null`
            if there is none (meaning that the reference orbit does not change at the specified optics point).
        
            Raises:
                : if the opticsTableItem is not contained in the base OpticsTable.
        
        
        """
        ...
    def getOfbRefOrbits(self) -> java.util.Map[cern.lsa.domain.optics.OpticsTableItem, 'OfbOrbit']: ...
    def getOfbResponseMatrixInfo(self, opticsTableItem: cern.lsa.domain.optics.OpticsTableItem) -> 'OfbResponseMatrixInfo':
        """
            Get the :class:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo` attached to a particular optics table item, or
            :code:`null` if there is none (meaning that the specified optics point is not used by the OFB to build a response
            matrix).
        
            Raises:
                : if the opticsTableItem is not contained in the base OpticsTable.
        
        
        """
        ...
    def getOfbResponseMatrixInfos(self) -> java.util.Map[cern.lsa.domain.optics.OpticsTableItem, 'OfbResponseMatrixInfo']: ...
    def getOpticsTable(self) -> cern.lsa.domain.optics.OpticsTable:
        """
            The base :code:`OpticsTable`
        
        """
        ...
    def getOpticsTableItems(self) -> java.util.List[cern.lsa.domain.optics.OpticsTableItem]: ...
    def getRefOrbitActiveAtTime(self, int: int) -> 'OfbOrbit':
        """
            Get the reference orbit active at a particular time, defined as the last reference orbit before the specified time. In
            case no such reference orbit exists, returns :code:`null`.
        
        """
        ...

class OfbOrbit(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface OfbOrbit extends cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity
    
    
        Pepresents an orbit for the Orbit-Feedback (OFB). The purpose of such orbits is to be stored in LSA database and being
        sent to the orbit-feedback service unit. The orbit feedback will use these orbits to correct the beams as good as
        possible to these orbits.
    
        An orbit consist of a base reading-set which in the normal case is an acquired orbit (usually from Yasp) with no bumps
        or crossing angles on it. Additionally it can have several overlays, which usually come from simulations (JMad). These
        overlays are either static (:class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay`) with a fixed shape (from a
        reading-set) and value, or dynamic (:class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`) where both shape and value
        is derived from a :code:`Knob`, retrieved when the orbit is calculated.
    
        Also see:
            :class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`
    """
    def addKnobOverlay(self, ofbKnobOverlay: 'OfbKnobOverlay') -> None:
        """
            Adds the given :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay` to the orbit.
        
            Parameters:
                knobOverlay (:class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`): The :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay` to add.
        
        
        """
        ...
    def addStaticOverlay(self, ofbStaticOverlay: 'OfbStaticOverlay') -> None:
        """
            Adds the given :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` to the orbit.
        
            Parameters:
                staticOverlay (:class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay`): The :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` to add.
        
        
        """
        ...
    def getBaseReadingSet(self) -> 'OfbReadingSet':
        """
            Returns base reading set for this orbit.
        
            Returns:
                base reading set for this orbit
        
        
        """
        ...
    def getCreateTime(self) -> java.util.Date:
        """
            Returns creation date of the orbit.
        
            Returns:
                creation date of the orbit
        
        
        """
        ...
    def getKnobOverlays(self) -> java.util.Set['OfbKnobOverlay']: ...
    def getStaticOverlay(self, ofbReadingSet: 'OfbReadingSet') -> 'OfbStaticOverlay':
        """
            retrieves the :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` for the given readingSet, if the orbit contains
            one. Otherwise null is returned
        
            Parameters:
                readingSet (:class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`): the readingSet for which to retrieve the overlay
        
            Returns:
                the static overlay for the readingSet
        
        
        """
        ...
    def getStaticOverlays(self) -> java.util.Set['OfbStaticOverlay']: ...
    def removeKnobOverlay(self, ofbKnobOverlay: 'OfbKnobOverlay') -> None:
        """
            Removes the given :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay` from the orbit.
        
            Parameters:
                knobOverlay (:class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`): The :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay` to remove.
        
        
        """
        ...
    def removeStaticOverlay(self, ofbStaticOverlay: 'OfbStaticOverlay') -> None:
        """
            Removes the given :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` from the orbit.
        
            Parameters:
                staticOverlay (:class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay`): The :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` to remove.
        
        
        """
        ...
    def setBaseReadingSet(self, ofbReadingSet: 'OfbReadingSet') -> None:
        """
            sets another readingSet as base-readingSet
        
            Parameters:
                readingSet (:class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`): the readingSet to set as base-readingSet
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            sets the name of the orbit
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name to set
        
        
        """
        ...

class OfbOverlay:
    """
    public interface OfbOverlay
    
        Represents an orbit like structure, that can be added to a base orbit. The overlay can either be static (
        :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay`) or dynamic
        (:class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`).
    
        Also see:
            :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`, :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay`
    """
    ...

class OfbReadingSet(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface OfbReadingSet extends cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity
    
        represents an orbit-like structure. It contains readings at least for a subset of the BPMs available in the database,
        depending on the type. A readingset of type 'BASE_ORBIT' usually contains readings for all the monitors. A readingset of
        another type, which is used in the overlays only should contain non-zero readings, since they only are added to the
        base-readingset of an orbit.
    
        Also see:
            :class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSetType`, :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
    """
    def addReading(self, ofbMonitorReading: OfbMonitorReading) -> None:
        """
            adds a monitor reading to the ReadingSet
        
            Parameters:
                reading (:class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`): the reading to add
        
        
        """
        ...
    def getAllReadings(self) -> java.util.SortedSet[OfbMonitorReading]: ...
    def getReading(self, string: str) -> OfbMonitorReading:
        """
            retrieves the reading for one monitor.
        
            Parameters:
                elementName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the monitor for which to get the reading
        
            Returns:
                the reading
        
        
        """
        ...
    def getType(self) -> 'OfbReadingSetType':
        """
        
            Returns:
                the type of the reading-set.
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            sets the name of the readingSet
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name to set
        
        
        """
        ...
    def setType(self, ofbReadingSetType: 'OfbReadingSetType') -> None:
        """
            sets the type of the readingSet
        
            Parameters:
                selectedItem (:class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSetType`): 
        
        """
        ...

class OfbReadingSetType(java.lang.Enum['OfbReadingSetType']):
    """
    public enum OfbReadingSetType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSetType`>
    
        defines the type of a readingset. One has to distinguish between two different categories:
    
    
          - BASE_ORBIT: readingsets of this type can be used as base readingsets of an orbit. These readingsets should contain
            readings for all monitors.
          - All the others: readingsets of types others thatn BASE_ORBIT are intended to be ovlerlays in an orbit object. These
            should only contain readings which are not zero.
    
    
        Also see:
            :class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`
    """
    BASE_ORBIT: typing.ClassVar['OfbReadingSetType'] = ...
    SEPARATION_BUMP_IR1: typing.ClassVar['OfbReadingSetType'] = ...
    SEPARATION_BUMP_IR2: typing.ClassVar['OfbReadingSetType'] = ...
    SEPARATION_BUMP_IR5: typing.ClassVar['OfbReadingSetType'] = ...
    SEPARATION_BUMP_IR8: typing.ClassVar['OfbReadingSetType'] = ...
    CROSSING_ANGLE_IR1: typing.ClassVar['OfbReadingSetType'] = ...
    CROSSING_ANGLE_IR2: typing.ClassVar['OfbReadingSetType'] = ...
    CROSSING_ANGLE_IR5: typing.ClassVar['OfbReadingSetType'] = ...
    CROSSING_ANGLE_IR8: typing.ClassVar['OfbReadingSetType'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OfbReadingSetType':
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
    def values() -> typing.List['OfbReadingSetType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OfbReadingSetType c : OfbReadingSetType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class OfbResponseMatrixInfo:
    """
    @Immutable public interface OfbResponseMatrixInfo
    """
    @staticmethod
    def builder() -> 'DefaultOfbResponseMatrixInfo.Builder': ...
    def getHorizontalEigenvalueCutRatio(self) -> float:
        """
            The eigenvalues cutoff ratio for the horizontal orbit correction
        
        """
        ...
    def getNumberOfHorizontalEigenvalues(self) -> int:
        """
            The number of eigenvalues to use for the horizontal orbit correction
        
        """
        ...
    def getNumberOfVerticalEigenvalues(self) -> int:
        """
            The number of eigenvalues to use for the vertical orbit correction
        
        """
        ...
    def getVerticalEigenvalueCutRatio(self) -> float:
        """
            The eigenvalues cutoff ratio for the vertical orbit correction
        
        """
        ...

class DefaultOfbOpticsTableInfo(OfbOpticsTableInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultOfbOpticsTableInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultOfbOpticsTableInfo.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultOfbOpticsTableInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.cern.optics.ofb.DefaultOfbOpticsTableInfo`.
        
            .. code-block: java
            
             DefaultOfbOpticsTableInfo.builder()
                .opticsTable(cern.lsa.domain.optics.OpticsTable) // required :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo.getOpticsTable`
                .putOfbRefOrbit|putAllOfbRefOrbits(cern.lsa.domain.optics.OpticsTableItem => cern.lsa.domain.cern.optics.ofb.OfbOrbit) // :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo.getOfbRefOrbits` mappings
                .putOfbResponseMatrixInfo|putAllOfbResponseMatrixInfos(cern.lsa.domain.optics.OpticsTableItem => cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo) // :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo.getOfbResponseMatrixInfos` mappings
                .build();
             
        
            Returns:
                A new DefaultOfbOpticsTableInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(ofbOpticsTableInfo: OfbOpticsTableInfo) -> 'DefaultOfbOpticsTableInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo`): The instance to copy
        
            Returns:
                A copied immutable OfbOpticsTableInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getOfbRefOrbits(self) -> java.util.Map[cern.lsa.domain.optics.OpticsTableItem, OfbOrbit]: ...
    def getOfbResponseMatrixInfos(self) -> java.util.Map[cern.lsa.domain.optics.OpticsTableItem, OfbResponseMatrixInfo]: ...
    def getOpticsTable(self) -> cern.lsa.domain.optics.OpticsTable:
        """
            The base :code:`OpticsTable`
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo.getOpticsTable`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`opticsTable`, :code:`ofbRefOrbits`, :code:`ofbResponseMatrixInfos`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`OfbOpticsTableInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withOfbRefOrbits(self, map: typing.Union[java.util.Map[cern.lsa.domain.optics.OpticsTableItem, OfbOrbit], typing.Mapping[cern.lsa.domain.optics.OpticsTableItem, OfbOrbit]]) -> 'DefaultOfbOpticsTableInfo': ...
    def withOfbResponseMatrixInfos(self, map: typing.Union[java.util.Map[cern.lsa.domain.optics.OpticsTableItem, OfbResponseMatrixInfo], typing.Mapping[cern.lsa.domain.optics.OpticsTableItem, OfbResponseMatrixInfo]]) -> 'DefaultOfbOpticsTableInfo': ...
    def withOpticsTable(self, opticsTable: cern.lsa.domain.optics.OpticsTable) -> 'DefaultOfbOpticsTableInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo.getOpticsTable` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (cern.lsa.domain.optics.OpticsTable): A new value for opticsTable
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultOfbOpticsTableInfo': ...
        def ofbRefOrbits(self, map: typing.Union[java.util.Map[cern.lsa.domain.optics.OpticsTableItem, OfbOrbit], typing.Mapping[cern.lsa.domain.optics.OpticsTableItem, OfbOrbit]]) -> 'DefaultOfbOpticsTableInfo.Builder': ...
        def ofbResponseMatrixInfos(self, map: typing.Union[java.util.Map[cern.lsa.domain.optics.OpticsTableItem, OfbResponseMatrixInfo], typing.Mapping[cern.lsa.domain.optics.OpticsTableItem, OfbResponseMatrixInfo]]) -> 'DefaultOfbOpticsTableInfo.Builder': ...
        def opticsTable(self, opticsTable: cern.lsa.domain.optics.OpticsTable) -> 'DefaultOfbOpticsTableInfo.Builder': ...
        def putAllOfbRefOrbits(self, map: typing.Union[java.util.Map[cern.lsa.domain.optics.OpticsTableItem, OfbOrbit], typing.Mapping[cern.lsa.domain.optics.OpticsTableItem, OfbOrbit]]) -> 'DefaultOfbOpticsTableInfo.Builder': ...
        def putAllOfbResponseMatrixInfos(self, map: typing.Union[java.util.Map[cern.lsa.domain.optics.OpticsTableItem, OfbResponseMatrixInfo], typing.Mapping[cern.lsa.domain.optics.OpticsTableItem, OfbResponseMatrixInfo]]) -> 'DefaultOfbOpticsTableInfo.Builder': ...
        @typing.overload
        def putOfbRefOrbit(self, opticsTableItem: cern.lsa.domain.optics.OpticsTableItem, ofbOrbit: OfbOrbit) -> 'DefaultOfbOpticsTableInfo.Builder': ...
        @typing.overload
        def putOfbRefOrbit(self, entry: java.util.Map.Entry[cern.lsa.domain.optics.OpticsTableItem, OfbOrbit]) -> 'DefaultOfbOpticsTableInfo.Builder': ...
        @typing.overload
        def putOfbResponseMatrixInfo(self, opticsTableItem: cern.lsa.domain.optics.OpticsTableItem, ofbResponseMatrixInfo: OfbResponseMatrixInfo) -> 'DefaultOfbOpticsTableInfo.Builder': ...
        @typing.overload
        def putOfbResponseMatrixInfo(self, entry: java.util.Map.Entry[cern.lsa.domain.optics.OpticsTableItem, OfbResponseMatrixInfo]) -> 'DefaultOfbOpticsTableInfo.Builder': ...

class DefaultOfbResponseMatrixInfo(OfbResponseMatrixInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultOfbResponseMatrixInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultOfbResponseMatrixInfo.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultOfbResponseMatrixInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.cern.optics.ofb.DefaultOfbResponseMatrixInfo`.
        
            .. code-block: java
            
             DefaultOfbResponseMatrixInfo.builder()
                .numberOfHorizontalEigenvalues(int) // required :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getNumberOfHorizontalEigenvalues`
                .numberOfVerticalEigenvalues(int) // required :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getNumberOfVerticalEigenvalues`
                .horizontalEigenvalueCutRatio(double) // required :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getHorizontalEigenvalueCutRatio`
                .verticalEigenvalueCutRatio(double) // required :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getVerticalEigenvalueCutRatio`
                .build();
             
        
            Returns:
                A new DefaultOfbResponseMatrixInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(ofbResponseMatrixInfo: OfbResponseMatrixInfo) -> 'DefaultOfbResponseMatrixInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo`): The instance to copy
        
            Returns:
                A copied immutable OfbResponseMatrixInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getHorizontalEigenvalueCutRatio(self) -> float:
        """
            The eigenvalues cutoff ratio for the horizontal orbit correction
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getHorizontalEigenvalueCutRatio`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo`
        
        
        """
        ...
    def getNumberOfHorizontalEigenvalues(self) -> int:
        """
            The number of eigenvalues to use for the horizontal orbit correction
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getNumberOfHorizontalEigenvalues`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo`
        
        
        """
        ...
    def getNumberOfVerticalEigenvalues(self) -> int:
        """
            The number of eigenvalues to use for the vertical orbit correction
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getNumberOfVerticalEigenvalues`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo`
        
        
        """
        ...
    def getVerticalEigenvalueCutRatio(self) -> float:
        """
            The eigenvalues cutoff ratio for the vertical orbit correction
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getVerticalEigenvalueCutRatio`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`numberOfHorizontalEigenvalues`, :code:`numberOfVerticalEigenvalues`,
            :code:`horizontalEigenvalueCutRatio`, :code:`verticalEigenvalueCutRatio`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`OfbResponseMatrixInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withHorizontalEigenvalueCutRatio(self, double: float) -> 'DefaultOfbResponseMatrixInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getHorizontalEigenvalueCutRatio` attribute. A value strict
            bits equality used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (double): A new value for horizontalEigenvalueCutRatio
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withNumberOfHorizontalEigenvalues(self, int: int) -> 'DefaultOfbResponseMatrixInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getNumberOfHorizontalEigenvalues` attribute. A value
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (int): A new value for numberOfHorizontalEigenvalues
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withNumberOfVerticalEigenvalues(self, int: int) -> 'DefaultOfbResponseMatrixInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getNumberOfVerticalEigenvalues` attribute. A value
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (int): A new value for numberOfVerticalEigenvalues
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withVerticalEigenvalueCutRatio(self, double: float) -> 'DefaultOfbResponseMatrixInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.cern.optics.ofb.OfbResponseMatrixInfo.getVerticalEigenvalueCutRatio` attribute. A value strict
            bits equality used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (double): A new value for verticalEigenvalueCutRatio
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultOfbResponseMatrixInfo': ...
        def horizontalEigenvalueCutRatio(self, double: float) -> 'DefaultOfbResponseMatrixInfo.Builder': ...
        def numberOfHorizontalEigenvalues(self, int: int) -> 'DefaultOfbResponseMatrixInfo.Builder': ...
        def numberOfVerticalEigenvalues(self, int: int) -> 'DefaultOfbResponseMatrixInfo.Builder': ...
        def verticalEigenvalueCutRatio(self, double: float) -> 'DefaultOfbResponseMatrixInfo.Builder': ...

class OfbKnobOverlay(OfbOverlay):
    """
    public interface OfbKnobOverlay extends :class:`~cern.lsa.domain.cern.optics.ofb.OfbOverlay`
    
        An :class:`~cern.lsa.domain.cern.optics.ofb.OfbOverlay` that is linked to a :code:`Knob`. Contrary to a
        :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` this :class:`~cern.lsa.domain.cern.optics.ofb.OfbOverlay`
        doesn't have a fixed scalar, but depends instead on the value of the associated knob. This value shoud be used when the
        overlay is added to the orbit.
    """
    def getKnobId(self) -> int:
        """
        
            Returns:
                The id of the knob.
        
        
        """
        ...
    def getKnobName(self) -> str:
        """
        
            Returns:
                The name of knob to take into account when calculating the expected beam position.
        
        
        """
        ...

class OfbStaticOverlay(OfbOverlay):
    """
    public interface OfbStaticOverlay extends :class:`~cern.lsa.domain.cern.optics.ofb.OfbOverlay`
    
        An orbit overlay which uses a reading set to determine the shape of the overlay, and a fixed scale to scale the
        reading-set associated with an :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`.
    
        Also see:
            :class:`~cern.lsa.domain.cern.optics.ofb.OfbOverlay`, :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`
    """
    def getReadingSet(self) -> OfbReadingSet:
        """
            retrieves the reading set for this overlay.
        
            Returns:
                the reading set
        
        
        """
        ...
    def getScaling(self) -> float:
        """
        
            Returns:
                the scaling of the readingSet within the orbit
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.optics.ofb")``.

    DefaultOfbOpticsTableInfo: typing.Type[DefaultOfbOpticsTableInfo]
    DefaultOfbResponseMatrixInfo: typing.Type[DefaultOfbResponseMatrixInfo]
    OfbKnobOverlay: typing.Type[OfbKnobOverlay]
    OfbMonitorReading: typing.Type[OfbMonitorReading]
    OfbOpticsTableInfo: typing.Type[OfbOpticsTableInfo]
    OfbOrbit: typing.Type[OfbOrbit]
    OfbOverlay: typing.Type[OfbOverlay]
    OfbReadingSet: typing.Type[OfbReadingSet]
    OfbReadingSetType: typing.Type[OfbReadingSetType]
    OfbResponseMatrixInfo: typing.Type[OfbResponseMatrixInfo]
    OfbStaticOverlay: typing.Type[OfbStaticOverlay]
