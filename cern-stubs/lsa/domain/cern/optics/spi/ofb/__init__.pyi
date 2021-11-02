import cern.lsa.domain.cern.optics.ofb
import cern.lsa.domain.commons.spi
import java.io
import java.util
import typing



class OfbKnobOverlayImpl(cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay, java.io.Serializable):
    """
    public class OfbKnobOverlayImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        An implementation of the :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getKnobId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay.getKnobId`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`
        
            Returns:
                The id of the knob.
        
        
        """
        ...
    def getKnobName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay.getKnobName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`
        
            Returns:
                The name of knob to take into account when calculating the expected beam position.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def setKnobId(self, long: int) -> None:
        """
            Sets the :code:`knobId` property.
        
            Parameters:
                knobId (`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`): The identifier of the knob.
        
        
        """
        ...
    def setKnobName(self, string: str) -> None:
        """
            Sets the :code:`knobName` property.
        
            Parameters:
                knobName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The name of the knob.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class OfbMonitorReadingImpl(cern.lsa.domain.cern.optics.ofb.OfbMonitorReading, java.io.Serializable):
    """
    public class OfbMonitorReadingImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, boolean: bool, double3: float, boolean2: bool): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, double3: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getHorizontal(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getHorizontal`
            Returns reading of the horizontal position of the beam.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getHorizontal`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`
        
            Returns:
                reading of the horizontal position of the beam
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isHorizontalValid`
        
        
        """
        ...
    def getMonitorName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getMonitorName`
            Returns name of the corresponding element.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getMonitorName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`
        
            Returns:
                name of the corresponding element
        
        
        """
        ...
    def getPosition(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getPosition`
            Returns position of the corresponding element.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getPosition`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`
        
            Returns:
                position of the corresponding element
        
        
        """
        ...
    def getVertical(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getVertical`
            Returns reading of the vertical position of the beam.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getVertical`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`
        
            Returns:
                reading of the vertical position of the beam
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isVerticalValid`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isHorizontalValid(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isHorizontalValid`
            Determines if the horizontal reading is valid and should be used by the orbit feedback system.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isHorizontalValid`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`
        
            Returns:
                :code:`true` if the horizontal reading is valid and should be used by the orbit feedback system
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getHorizontal`
        
        
        """
        ...
    def isVerticalValid(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isVerticalValid`
            Determines if the vertical reading is valid and should be used by the orbit feedback system.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isVerticalValid`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`
        
            Returns:
                :code:`true` if the vertical reading is valid and should be used by the orbit feedback system
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.getVertical`,
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.setVerticalValid`
        
        
        """
        ...
    def setHorizontal(self, double: float) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.setHorizontal`
            Sets reading of the horizontal position of the beam at the element.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.setHorizontal`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`
        
            Parameters:
                horizontal (double): horizontal position of the beam
        
        
        """
        ...
    def setHorizontalValid(self, boolean: bool) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.setHorizontalValid`
            Modifies the validity of the horizontal reading.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.setHorizontalValid`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`
        
            Parameters:
                valid (boolean): The horizontalValid to set.
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isHorizontalValid`
        
        
        """
        ...
    def setMonitorName(self, string: str) -> None:
        """
            Sets :code:`monitorName` property.
        
            Parameters:
                monitorName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the :code:`monitorName` to set
        
        
        """
        ...
    def setPosition(self, double: float) -> None:
        """
            Sets :code:`position` property.
        
        
            SHOULD ONLY BE USED IN OrbitFeedbackFinder : this value won't be saved when persisting this java bean.
        
            Parameters:
                position (double): the :code:`position` to set
        
        
        """
        ...
    def setVertical(self, double: float) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.setVertical`
            Sets reading of the vertical position of the beam.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.setVertical`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`
        
            Parameters:
                vertical (double): vertical position of the beam.
        
        
        """
        ...
    def setVerticalValid(self, boolean: bool) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.setVerticalValid`
            Modifies the validity of the vertical reading.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.setVerticalValid`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`
        
            Parameters:
                valid (boolean): The verticalValid to set.
        
            Also see:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading.isVerticalValid`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class OfbOrbitImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.cern.optics.ofb.OfbOrbit], cern.lsa.domain.cern.optics.ofb.OfbOrbit):
    """
    public class OfbOrbitImpl extends cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity<:class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`> implements :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...
    def addKnobOverlay(self, ofbKnobOverlay: cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.addKnobOverlay`
            Adds the given :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay` to the orbit.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.addKnobOverlay`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
            Parameters:
                knobOverlay (:class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`): The :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay` to add.
        
        
        """
        ...
    def addStaticOverlay(self, ofbStaticOverlay: cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.addStaticOverlay`
            Adds the given :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` to the orbit.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.addStaticOverlay`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
            Parameters:
                staticOverlay (:class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay`): The :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` to add.
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :code:`equals` in class :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
        
        """
        ...
    def getBaseReadingSet(self) -> cern.lsa.domain.cern.optics.ofb.OfbReadingSet:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.getBaseReadingSet`
            Returns base reading set for this orbit.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.getBaseReadingSet`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
            Returns:
                base reading set for this orbit
        
        
        """
        ...
    def getCreateTime(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.getCreateTime`
            Returns creation date of the orbit.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.getCreateTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
            Returns:
                creation date of the orbit
        
        
        """
        ...
    def getKnobOverlays(self) -> java.util.Set[cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay]: ...
    def getStaticOverlay(self, ofbReadingSet: cern.lsa.domain.cern.optics.ofb.OfbReadingSet) -> cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.getStaticOverlay`
            retrieves the :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` for the given readingSet, if the orbit contains
            one. Otherwise null is returned
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.getStaticOverlay`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
            Parameters:
                readingSet (:class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`): the readingSet for which to retrieve the overlay
        
            Returns:
                the static overlay for the readingSet
        
        
        """
        ...
    def getStaticOverlays(self) -> java.util.Set[cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :code:`hashCode` in class :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
        
        """
        ...
    def removeKnobOverlay(self, ofbKnobOverlay: cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.removeKnobOverlay`
            Removes the given :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay` from the orbit.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.removeKnobOverlay`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
            Parameters:
                knobOverlay (:class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay`): The :class:`~cern.lsa.domain.cern.optics.ofb.OfbKnobOverlay` to remove.
        
        
        """
        ...
    def removeStaticOverlay(self, ofbStaticOverlay: cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.removeStaticOverlay`
            Removes the given :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` from the orbit.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.removeStaticOverlay`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
            Parameters:
                staticOverlay (:class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay`): The :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay` to remove.
        
        
        """
        ...
    def setBaseReadingSet(self, ofbReadingSet: cern.lsa.domain.cern.optics.ofb.OfbReadingSet) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.setBaseReadingSet`
            sets another readingSet as base-readingSet
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit.setBaseReadingSet`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
            Parameters:
                baseReadingSet (:class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`): the readingSet to set as base-readingSet
        
        
        """
        ...
    def setCreateTime(self, date: java.util.Date) -> None:
        """
            Sets :code:`createTime` property.
        
            Parameters:
                createTime (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): the :code:`createTime` to set
        
        
        """
        ...
    def setOverlays(self, set: java.util.Set[cern.lsa.domain.cern.optics.ofb.OfbOverlay]) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.cern.optics.ofb.OfbOrbit`
        
        
        """
        ...

class OfbReadingSetImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.cern.optics.ofb.OfbReadingSet], cern.lsa.domain.cern.optics.ofb.OfbReadingSet):
    """
    public class OfbReadingSetImpl extends cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity<:class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`> implements :class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...
    def addReading(self, ofbMonitorReading: cern.lsa.domain.cern.optics.ofb.OfbMonitorReading) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet.addReading`
            adds a monitor reading to the ReadingSet
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet.addReading`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`
        
            Parameters:
                reading (:class:`~cern.lsa.domain.cern.optics.ofb.OfbMonitorReading`): the reading to add
        
        
        """
        ...
    def getAllReadings(self) -> java.util.SortedSet[cern.lsa.domain.cern.optics.ofb.OfbMonitorReading]: ...
    def getReading(self, string: str) -> cern.lsa.domain.cern.optics.ofb.OfbMonitorReading:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet.getReading`
            retrieves the reading for one monitor.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet.getReading`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`
        
            Parameters:
                elementName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the monitor for which to get the reading
        
            Returns:
                the reading
        
        
        """
        ...
    def getType(self) -> cern.lsa.domain.cern.optics.ofb.OfbReadingSetType:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet.getType`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`
        
            Returns:
                the type of the reading-set.
        
        
        """
        ...
    def setType(self, ofbReadingSetType: cern.lsa.domain.cern.optics.ofb.OfbReadingSetType) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet.setType`
            sets the type of the readingSet
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet.setType`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`
        
        
        """
        ...

class OfbStaticOverlayImpl(cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay, java.io.Serializable):
    """
    public class OfbStaticOverlayImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, ofbReadingSet: cern.lsa.domain.cern.optics.ofb.OfbReadingSet, double: float): ...
    def getReadingSet(self) -> cern.lsa.domain.cern.optics.ofb.OfbReadingSet:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay.getReadingSet`
            retrieves the reading set for this overlay.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay.getReadingSet`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay`
        
            Returns:
                the reading set
        
        
        """
        ...
    def getScaling(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay.getScaling`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.ofb.OfbStaticOverlay`
        
            Returns:
                the scaling of the readingSet within the orbit
        
        
        """
        ...
    def setReadingSet(self, ofbReadingSet: cern.lsa.domain.cern.optics.ofb.OfbReadingSet) -> None:
        """
            Sets :code:`readingSet` property.
        
            Parameters:
                readingSet (:class:`~cern.lsa.domain.cern.optics.ofb.OfbReadingSet`): the :code:`readingSet` to set
        
        
        """
        ...
    def setScaling(self, double: float) -> None:
        """
            Sets :code:`scaling` property.
        
            Parameters:
                scaling (double): the :code:`scaling` to set
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.optics.spi.ofb")``.

    OfbKnobOverlayImpl: typing.Type[OfbKnobOverlayImpl]
    OfbMonitorReadingImpl: typing.Type[OfbMonitorReadingImpl]
    OfbOrbitImpl: typing.Type[OfbOrbitImpl]
    OfbReadingSetImpl: typing.Type[OfbReadingSetImpl]
    OfbStaticOverlayImpl: typing.Type[OfbStaticOverlayImpl]
