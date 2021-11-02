import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import cern.lsa.domain.cern.timing
import cern.lsa.domain.cern.timing.enums
import java.io
import java.util
import typing



class ActiveTimingUsersImpl(cern.lsa.domain.cern.timing.ActiveTimingUsers, java.io.Serializable):
    """
    public class ActiveTimingUsersImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.ActiveTimingUsers`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.cern.timing.ActiveTimingUsers` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, list: java.util.List[str], list2: java.util.List[str]): ...
    def contains(self, string: str) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.ActiveTimingUsers.contains`
            Returns :code:`true` if the specified user is contained in the list of
            :meth:`~cern.lsa.domain.cern.timing.ActiveTimingUsers.getNormalUsers` or in the list of
            :meth:`~cern.lsa.domain.cern.timing.ActiveTimingUsers.getSpareUsers`.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.ActiveTimingUsers.contains`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.ActiveTimingUsers`
        
            Parameters:
                user (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the considered user
        
            Returns:
                :code:`true` if the given user is active (normal or spare) in the active BCD, :code:`false` otherwise
        
        
        """
        ...
    def getNormalUsers(self) -> java.util.List[str]: ...
    def getSpareUsers(self) -> java.util.List[str]: ...

class BunchPatternImpl(cern.lsa.domain.cern.timing.BunchPattern, java.io.Serializable):
    """
    public class BunchPatternImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.BunchPattern`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class represent a bunch pattern: it gives the relative bunch position, expressed in bucket units, for one SPS
        injection into LHC the returned int array is always in increasing order.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, string2: str): ...
    def addBunchPosition(self, int: int) -> None:
        """
            add a new bunch at the given position
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.addBunchPosition`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Parameters:
                relativeBucketNbr (int): : the bucket number relative to the first bunch bucket nbr
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getBatchSpacing(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.getBatchSpacing`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Returns:
                the batch spacing- if the spacing between batches is different it returns the minimum batch spacing.
        
        
        """
        ...
    def getBunchPatternDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.getBunchPatternDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Returns:
                a string giving a description of the bunch pattern
        
        
        """
        ...
    def getBunchPatternName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.getBunchPatternName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Returns:
                the name of the bunch pattern
        
        
        """
        ...
    def getBunchSpacing(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.getBunchSpacing`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Returns:
                the space between 2 consecutive bunches in ns.
        
        
        """
        ...
    def getBunchesPosition(self) -> typing.List[int]:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.getBunchesPosition`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Returns:
                the relative bunch positions in bucket unit the int[] array is always in increasing order
        
        
        """
        ...
    def getNbrOfBunches(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.getNbrOfBunches`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Returns:
                the number of bunches that will be injected
        
        
        """
        ...
    def getNbrOfBunchesPerPSBatch(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.getNbrOfBunchesPerPSBatch`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Returns:
                the number of bunches for each PS batch
        
        
        """
        ...
    def getNbrOfPSBatches(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.getNbrOfPSBatches`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Returns:
                the number of PS batches that will be injected.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isDoubletsBeam(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.isDoubletsBeam`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Returns:
                :code:`true` if the pattern is a pattern of a doublet beam.
        
        
        """
        ...
    def setBatchSpacing(self, int: int) -> None:
        """
        
            Parameters:
                batchSpacing (int): the batchSpacing to set
        
        
        """
        ...
    def setBunchPositions(self, intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.BunchPattern.setBunchPositions`
            set the bunches positions
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.setBunchPositions`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Parameters:
                buketNumbers (int[]): : the buckets filled by bunches
        
        
        """
        ...
    def setBunchSpacing(self, int: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.setBunchSpacing`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Parameters:
                bunchSpacing (int): the bunchSpacing to set
        
        
        """
        ...
    def setDoubletsBeam(self, boolean: bool) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.setDoubletsBeam`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Parameters:
                doubletsBeam (boolean): indicates if the pattern is of a doublet beam
        
            Also see:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.isDoubletsBeam`
        
        
        """
        ...
    def setNbrOfBunches(self, int: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.setNbrOfBunches`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Parameters:
                nbrOfBunches (int): the nbrOfBunches to set
        
        
        """
        ...
    def setNbrOfBunchesPerPSBatch(self, int: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.setNbrOfBunchesPerPSBatch`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Parameters:
                nbrOfBunchesPerPSBatch (int): the nbrOfBunchesPerPSBatch to set
        
        
        """
        ...
    def setNbrOfPSBatches(self, int: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.setNbrOfPSBatches`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.BunchPattern`
        
            Parameters:
                nbrOfPSBatches (int): the nbrOfPSBatches to set
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class EventTableImpl(cern.lsa.domain.cern.timing.EventTable, java.io.Serializable):
    """
    public class EventTableImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.EventTable`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    def addEvent(self, event: cern.lsa.domain.cern.timing.Event, int: int) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventTable.addEvent`
            Adds an event in the table.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventTable.addEvent` in interface :class:`~cern.lsa.domain.cern.timing.EventTable`
        
            Parameters:
                event (:class:`~cern.lsa.domain.cern.timing.Event`): : event to be added.
                offsetMs (int): : time offset of the new event. This value must be positive or zero
        
        
        """
        ...
    def addEvents(self, sortedSet: java.util.SortedSet[cern.lsa.domain.cern.timing.EventTableEntry]) -> None: ...
    def dumpTable(self) -> str:
        """
        
            Returns:
                a String with a complete dump of the table
        
        
        """
        ...
    def getEventList(self) -> java.util.SortedSet[cern.lsa.domain.cern.timing.EventTableEntry]: ...
    def getName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventTable.getName`
            Returns the table name
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventTable.getName` in interface :class:`~cern.lsa.domain.cern.timing.EventTable`
        
        
        """
        ...
    def getRunCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventTable.getRunCount`
            Returns the table run count i.e. the number of times the timing system will play it.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventTable.getRunCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.EventTable`
        
            Returns:
                the table run count.
        
        
        """
        ...
    def getStartingEvent(self) -> cern.lsa.domain.cern.timing.Event:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventTable.getStartingEvent`
            Returns the :code:`Event` the table will be started on.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventTable.getStartingEvent`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.EventTable`
        
            Returns:
                the starting event
        
        
        """
        ...
    def removeEvent(self, event: cern.lsa.domain.cern.timing.Event, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventTable.removeEvent`
            Removes the given event with the given offset
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventTable.removeEvent`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.EventTable`
        
            Parameters:
                event (:class:`~cern.lsa.domain.cern.timing.Event`): : the event to remove
                offsetMs (int): : the event's offset
        
        
        """
        ...
    def removeEvents(self) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventTable.removeEvents`
            Removes all the events.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventTable.removeEvents`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.EventTable`
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventTable.setName`
            Sets table name
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventTable.setName` in interface :class:`~cern.lsa.domain.cern.timing.EventTable`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the table name
        
        
        """
        ...
    def setRunCount(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventTable.setRunCount`
            Sets the table run count i.e. the number of times the timing system will play it.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventTable.setRunCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.EventTable`
        
            Parameters:
                runCount (int): the table run count.
        
        
        """
        ...
    def setStartingEvent(self, event: cern.lsa.domain.cern.timing.Event) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventTable.setStartingEvent`
            Sets the starting event for this table.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventTable.setStartingEvent`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.EventTable`
        
            Parameters:
                event (:class:`~cern.lsa.domain.cern.timing.Event`): the starting event
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class EventTableStatusImpl(cern.lsa.domain.cern.timing.EventTableStatus, java.io.Serializable):
    def __init__(self, string: str, tABLE_STATUS_SW: cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW, list: java.util.List[cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW]): ...
    def getHardwareStatus(self) -> java.util.List[cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW]: ...
    def getSoftwareStatus(self) -> cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW: ...
    def getTableName(self) -> str: ...
    def toString(self) -> str: ...

class EventTypeImpl(cern.lsa.domain.cern.timing.EventType, java.io.Serializable):
    """
    public class EventTypeImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.EventType`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        EventType implementation. **Do not create** instances of this class with :code:`new` but use instead the
        :code:`EventTypeFinder` to retrieve a type or a list of types
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, string2: str, string3: str): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventType.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.EventType`
        
            Returns:
                the event description
        
        
        """
        ...
    def getEvent(self, int: int) -> cern.lsa.domain.cern.timing.Event:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventType.getEvent`
            Return a new Event based on this EventType with the given payload.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventType.getEvent` in interface :class:`~cern.lsa.domain.cern.timing.EventType`
        
            Returns:
        
        
        """
        ...
    def getGroup(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventType.getGroup` in interface :class:`~cern.lsa.domain.cern.timing.EventType`
        
            Returns:
                the event group
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventType.getName` in interface :class:`~cern.lsa.domain.cern.timing.EventType`
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                the event name
        
        
        """
        ...
    def getXtimName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.EventType.getXtimName`
            return the name of the XTIM associated with the timing type.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.EventType.getXtimName` in interface :class:`~cern.lsa.domain.cern.timing.EventType`
        
            Returns:
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def setGroup(self, string: str) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class LhcCirculatingBunchConfigurationImpl(cern.lsa.domain.cern.timing.LhcCirculatingBunchConfiguration, java.io.Serializable):
    """
    public class LhcCirculatingBunchConfigurationImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.LhcCirculatingBunchConfiguration`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def addFilledBucket(self, int: int) -> None: ...
    def getBeamNbr(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcCirculatingBunchConfiguration.getBeamNbr`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcCirculatingBunchConfiguration`
        
        
        """
        ...
    def getFilledBuckets(self) -> java.util.SortedSet[int]: ...
    def getFirstFilledBucket(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcCirculatingBunchConfiguration.getFirstFilledBucket`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcCirculatingBunchConfiguration`
        
        
        """
        ...
    def setBeamNbr(self, int: int) -> None: ...

class LhcInjectionBunchConfigurationImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration], cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration, java.io.Serializable):
    """
    public class LhcInjectionBunchConfigurationImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`> implements :class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :code:`equals` in class :class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`
        
        
        """
        ...
    def getBunchPattern(self) -> cern.lsa.domain.cern.timing.BunchPattern:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration.getBunchPattern`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`
        
            Returns:
                the bunch pattern used for this configuration
        
        
        """
        ...
    def getFilledBuckets(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration.getFilledBuckets`
            returns an int array of the bucket number that will be filled at the next injection The bucket numbers are the absolute
            bucket number values
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration.getFilledBuckets`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`
        
        
        """
        ...
    def getFirstFilledBucket(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration.getFirstFilledBucket`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`
        
            Returns:
                the first bucket that is filled by the next injection
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :code:`hashCode` in class :class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`
        
        
        """
        ...
    def setBunchPattern(self, bunchPattern: cern.lsa.domain.cern.timing.BunchPattern) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration.setBunchPattern`
            set the bunch pattern
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration.setBunchPattern`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`
        
        
        """
        ...
    def setFirstFilledBucket(self, int: int) -> None:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration.setFirstFilledBucket`
            set the first bucket that is filled by the next injection
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration.setFirstFilledBucket`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`
        
        
        """
        ...

class LhcInjectionImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.timing.LhcInjection], cern.lsa.domain.cern.timing.LhcInjection):
    """
    public class LhcInjectionImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.cern.timing.LhcInjection`> implements :class:`~cern.lsa.domain.cern.timing.LhcInjection`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :code:`equals` in class :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
        
        """
        ...
    def getBunchConfiguration(self) -> cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.getBunchConfiguration`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Returns:
                the bunch configuration (the buckets that will be filled by the injected beam)
        
        
        """
        ...
    def getNextInjectionBeamType(self) -> cern.lsa.domain.cern.timing.enums.BEAM_TYPE:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.getNextInjectionBeamType`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Returns:
                the beam type (intermediate or nominal intensity)
        
        
        """
        ...
    def getNextInjectionBunchIntensity(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.getNextInjectionBunchIntensity`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Returns:
                the intensity per bunch
        
        
        """
        ...
    def getNextInjectionBunchNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.getNextInjectionBunchNumber`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Returns:
                the number of bunch that will be injected
        
        
        """
        ...
    def getNextInjectionBunchSpacing(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.getNextInjectionBunchSpacing`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Returns:
                the space (in ns) between 2 bunches
        
        
        """
        ...
    def getNextInjectionNbrOfBunchesPerPSBatch(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.getNextInjectionNbrOfBunchesPerPSBatch`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Returns:
                the number of bunches for each PS batch
        
        
        """
        ...
    def getNextInjectionPSbatchNbr(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.getNextInjectionPSbatchNbr`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Returns:
                the number of batches in the PS needed for the next beam this info is needed to post an injection request to the timing
                system
        
        
        """
        ...
    def getNextInjectionParticleType(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.getNextInjectionParticleType`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Returns:
                the particle type of the next injected beam
        
        
        """
        ...
    def getNextInjectionRFBucket(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.getNextInjectionRFBucket`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Returns:
                the bucket number where the first bunch will be injected this info is needed to post an injection request to the timing
                system
        
        
        """
        ...
    def getNextInjectionRing(self) -> cern.lsa.domain.cern.timing.enums.RNGI:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.getNextInjectionRing`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Returns:
                the ring that will receive the next injection this info is needed to post an injection request to the timing system
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :code:`hashCode` in class :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
        
        """
        ...
    def setBunchConfiguration(self, lhcInjectionBunchConfiguration: cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setBunchConfiguration`
            set the associated bunch configuration
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setBunchConfiguration`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
        
        """
        ...
    def setNextInjectionBeamType(self, bEAM_TYPE: cern.lsa.domain.cern.timing.enums.BEAM_TYPE) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setNextInjectionBeamType`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
        
        """
        ...
    def setNextInjectionBunchIntensity(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setNextInjectionBunchIntensity`
            Set the intensity per bunch
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setNextInjectionBunchIntensity`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
        
        """
        ...
    def setNextInjectionParticleType(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setNextInjectionParticleType`
            set the particle type of the next injected beam
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setNextInjectionParticleType`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
        
        """
        ...
    @typing.overload
    def setNextInjectionRing(self, rNGI: cern.lsa.domain.cern.timing.enums.RNGI) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setNextInjectionRing`
            Set the next injection ring
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setNextInjectionRing`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Parameters:
                nextInjectionRing (int): : an integer 0=beam 1, 1=beam2, 2= no beam
        
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setNextInjectionRing`
            set the next injection ring
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjection.setNextInjectionRing`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
            Parameters:
                nextInjectionRing (:class:`~cern.lsa.domain.cern.timing.enums.RNGI`): : enum giving the possible rings
        
        
        """
        ...
    @typing.overload
    def setNextInjectionRing(self, int: int) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.cern.timing.LhcInjection`
        
        
        """
        ...

class LhcInjectionSchemeEntryImpl(cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs, java.io.Serializable):
    """
    public class LhcInjectionSchemeEntryImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, lhcInjection: cern.lsa.domain.cern.timing.LhcInjection, int: int, int2: int): ...
    def compareTo(self, lhcInjectionSchemeEntry_Obs: cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getDelay(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs.getDelay`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs`
        
        
        """
        ...
    def getInjection(self) -> cern.lsa.domain.cern.timing.LhcInjection:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs.getInjection`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs`
        
        
        """
        ...
    def getInjectionOrder(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs.getInjectionOrder`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs`
        
        
        """
        ...
    def setDelay(self, int: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs.setDelay`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs`
        
        
        """
        ...
    def setInjectionOrder(self, int: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs.setInjectionOrder`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs`
        
        
        """
        ...

class LhcInjectionSchemeImpl(cern.lsa.domain.cern.timing.LhcInjectionScheme, java.io.Serializable):
    """
    public class LhcInjectionSchemeImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...
    def addInjection(self, lhcInjection: cern.lsa.domain.cern.timing.LhcInjection) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.addInjection`
            add an entry to the existing entry list
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.addInjection`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Parameters:
                anInjection (:class:`~cern.lsa.domain.cern.timing.LhcInjection`): : the new injection to add
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getCreationDate`
            get the date the scheme has been created
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getCreationDate`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getDescription`
            get the description text for the scheme
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
                the description
        
        
        """
        ...
    def getInjectionSchemeGroup(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getInjectionSchemeGroup`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
                the group of the injection Scheme
        
        
        """
        ...
    def getInjectionSchemeName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getInjectionSchemeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
                the name of the injection scheme
        
        
        """
        ...
    def getInjections(self) -> java.util.Set[cern.lsa.domain.cern.timing.LhcInjection]: ...
    def getMinBunchSpacing(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getMinBunchSpacing`
            returns the minimum bunch spacing of the scheme
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getMinBunchSpacing`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
        
        
        """
        ...
    def getNbCollisionIP1(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getNbCollisionIP1`
            returns the number of collision in IP1 we obtain from this scheme.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getNbCollisionIP1`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
        
        
        """
        ...
    def getNbCollisionIP2(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getNbCollisionIP2`
            returns the number of collision in IP2 we obtain from this scheme.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getNbCollisionIP2`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
        
        
        """
        ...
    def getNbCollisionIP5(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getNbCollisionIP5`
            returns the number of collision in IP5 we obtain from this scheme.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getNbCollisionIP5`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
        
        
        """
        ...
    def getNbCollisionIP8(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getNbCollisionIP8`
            returns the number of collision in IP8 we obtain from this scheme.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getNbCollisionIP8`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
        
        
        """
        ...
    def getNumberOfBunchesB1(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getNumberOfBunchesB1`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
                the number of bunches for beam 1
        
        
        """
        ...
    def getNumberOfBunchesB2(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getNumberOfBunchesB2`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
                the number of bunches for beam 2
        
        
        """
        ...
    def getPilotPositionB1(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getPilotPositionB1`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
                the position of the pilot for beam 1
        
        
        """
        ...
    def getPilotPositionB2(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getPilotPositionB2`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
                the position of the pilot for beam 2
        
        
        """
        ...
    def getPredictedBunchConfiguration(self, rNGI: cern.lsa.domain.cern.timing.enums.RNGI) -> typing.List[int]:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getPredictedBunchConfiguration`
            get the predicted circulation bunch configuration after all the injection defined in the scheme have been send an
            successfully executed
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.getPredictedBunchConfiguration`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
                an int array with the filled bucket numbers
        
        
        """
        ...
    def isInjectionCleaningEnabled(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.isInjectionCleaningEnabled`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
                true if the injection cleaning has to be enabled by default.
        
        
        """
        ...
    def isWithOverInjection(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.isWithOverInjection`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Returns:
                true if an overinjection is needed with this scheme
        
        
        """
        ...
    def removeInjection(self, lhcInjection: cern.lsa.domain.cern.timing.LhcInjection) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.removeInjection`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setBunchIntForAllRequests(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setBunchIntForAllRequests`
            change the bunch intensity for all the requests
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setBunchIntForAllRequests`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setCreationDate(self, date: java.util.Date) -> None: ...
    def setDescription(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setDescription`
            set the description text for the scheme
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setInjectionSchemeGroup(self, string: str) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setInjectionSchemeGroup`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
            Parameters:
                categorie (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): : the name of the scheme group
        
        
        """
        ...
    def setInjectionSchemeName(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setInjectionSchemeName`
            set the name of the scheme
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setInjectionSchemeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setIsInjectionCleaningEnabled(self, boolean: bool) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setIsInjectionCleaningEnabled`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setIsWithOverInjection(self, boolean: bool) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setIsWithOverInjection`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setNbCollisionIP1(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setNbCollisionIP1`
            set the number of collision in IP1 we obtain from this scheme.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setNbCollisionIP1`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setNbCollisionIP2(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setNbCollisionIP2`
            set the number of collision in IP2 we obtain from this scheme.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setNbCollisionIP2`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setNbCollisionIP5(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setNbCollisionIP5`
            set the number of collision in IP5 we obtain from this scheme.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setNbCollisionIP5`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setNbCollisionIP8(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setNbCollisionIP8`
            set the number of collision in IP8 we obtain from this scheme.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setNbCollisionIP8`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setPilotPositionB1(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setPilotPositionB1`
            set the position of the pilot for beam 2
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setPilotPositionB1`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def setPilotPositionB2(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setPilotPositionB2`
            set the position of the pilot for beam 2
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LhcInjectionScheme.setPilotPositionB2`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LhcInjectionScheme`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class LoadedEventTableImpl(cern.lsa.domain.cern.timing.LoadedEventTable, java.io.Serializable):
    """
    public class LoadedEventTableImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.LoadedEventTable`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, eventTableStatus: cern.lsa.domain.cern.timing.EventTableStatus, eventTable2: cern.lsa.domain.cern.timing.EventTable): ...
    def getEventTable(self) -> cern.lsa.domain.cern.timing.EventTable:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LoadedEventTable.getEventTable`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LoadedEventTable`
        
            Returns:
                the event table
        
        
        """
        ...
    def getTableStatus(self) -> cern.lsa.domain.cern.timing.EventTableStatus:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.LoadedEventTable.getTableStatus`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.LoadedEventTable`
        
            Returns:
                the event table status. It contains the software and the hardware statuses.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class TimingEventImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.timing.TimingEvent], cern.lsa.domain.cern.timing.TimingEvent):
    """
    public class TimingEventImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.cern.timing.TimingEvent`> implements :class:`~cern.lsa.domain.cern.timing.TimingEvent`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, string2: str, string3: str): ...
    def getHardwareEventName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.TimingEvent.getHardwareEventName`
            Returns name of the physical hardware event sent on the wire. Note that a single hardware event can be used for several
            logical events.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.TimingEvent.getHardwareEventName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.TimingEvent`
        
            Returns:
                name of the physical hardware event
        
        
        """
        ...
    def getPayloadAttributeName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.timing.TimingEvent.getPayloadAttributeName`
            Returns name of a cycle segment attribute whose value should be used as a payload for this event. Can be :code:`null` if
            the event doesn't carry any payload.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.TimingEvent.getPayloadAttributeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.TimingEvent`
        
        
        """
        ...

class TimingEventSchedulingImpl(cern.lsa.domain.cern.timing.TimingEventScheduling, java.io.Serializable):
    """
    public class TimingEventSchedulingImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.TimingEventScheduling`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, timingEvent: cern.lsa.domain.cern.timing.TimingEvent, int: int): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getOffsetInMillis(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.TimingEventScheduling.getOffsetInMillis`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.TimingEventScheduling`
        
            Returns:
                offset (negative or positive) relative to the time of the parent process
        
        
        """
        ...
    def getTimingEvent(self) -> cern.lsa.domain.cern.timing.TimingEvent:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.TimingEventScheduling.getTimingEvent`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.TimingEventScheduling`
        
            Returns:
                the scheduled timing event
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class TimingProcessImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.timing.TimingProcess], cern.lsa.domain.cern.timing.TimingProcess):
    """
    public class TimingProcessImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.cern.timing.TimingProcess`> implements :class:`~cern.lsa.domain.cern.timing.TimingProcess`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, timingDomain: cern.accsoft.commons.domain.TimingDomain): ...
    def addTimingEventScheduling(self, timingEventScheduling: cern.lsa.domain.cern.timing.TimingEventScheduling) -> None: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Overrides:
                :code:`getName` in class :class:`~cern.lsa.domain.cern.timing.TimingProcess`
        
        
        """
        ...
    def getScheduledTimingEvents(self) -> java.util.Set[cern.lsa.domain.cern.timing.TimingEventScheduling]: ...
    def getTimingDomain(self) -> cern.accsoft.commons.domain.TimingDomain:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.TimingProcess.getTimingDomain`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.TimingProcess`
        
            Returns:
                non-null timing domain for which the process is defined
        
        
        """
        ...

class TimingProcessSchedulingImpl(cern.lsa.domain.cern.timing.TimingProcessScheduling, java.io.Serializable):
    """
    public class TimingProcessSchedulingImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.TimingProcessScheduling`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Note that we have a redundancy here because we keep both timingProcess and its name separately. This is due to the fact
        that in the serialized XML we only keep name of the process so when deserializing the cycle structure, having the name
        we need to look up the :class:`~cern.lsa.domain.cern.timing.TimingProcess` instances in the database. So when
        deserializing from XML we have only name, which is then used to associate the corresponding TimingProcess object.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess, int: int, timingProcessAnchor: cern.lsa.domain.cern.timing.TimingProcessAnchor): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getOffsetInMillis(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.TimingProcessScheduling.getOffsetInMillis`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.TimingProcessScheduling`
        
            Returns:
                offset (negative or positive) in milliseconds relative to the time of the cycle segment start
        
            Also see:
                :meth:`~cern.lsa.domain.cern.timing.TimingProcessScheduling.setOffsetInMillis`
        
        
        """
        ...
    def getTimingProcess(self) -> cern.lsa.domain.cern.timing.TimingProcess:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.TimingProcessScheduling.getTimingProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.TimingProcessScheduling`
        
            Returns:
                the scheduled timing process
        
        
        """
        ...
    def getTimingProcessAnchor(self) -> cern.lsa.domain.cern.timing.TimingProcessAnchor:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.TimingProcessScheduling.getTimingProcessAnchor`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.TimingProcessScheduling`
        
            Returns:
                the current anchor of the scheduling
        
        
        """
        ...
    def getTimingProcessAnchorName(self) -> str: ...
    def getTimingProcessName(self) -> str: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def setOffsetInMillis(self, int: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.TimingProcessScheduling.setOffsetInMillis`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.TimingProcessScheduling`
        
            Parameters:
                offsetInMillis (int): (negative or positive) in milliseconds relative to the time of the cycle segment start
        
            Also see:
                :meth:`~cern.lsa.domain.cern.timing.TimingProcessScheduling.getOffsetInMillis`
        
        
        """
        ...
    def setTimingProcess(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess) -> None: ...
    def setTimingProcessAnchor(self, timingProcessAnchor: cern.lsa.domain.cern.timing.TimingProcessAnchor) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.TimingProcessScheduling.setTimingProcessAnchor`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.TimingProcessScheduling`
        
            Parameters:
                anchor (:class:`~cern.lsa.domain.cern.timing.TimingProcessAnchor`): anchor to be used for this scheduling
        
        
        """
        ...
    def setTimingProcessAnchorName(self, string: str) -> None:
        """
            Used by JAXB during deserialization.
        
        """
        ...
    def setTimingProcessName(self, string: str) -> None:
        """
            Used by JAXB during deserialization.
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class XtimInfoImpl(cern.lsa.domain.cern.timing.XtimInfo, java.io.Serializable):
    """
    public class XtimInfoImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.timing.XtimInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, string2: str): ...
    def getAcqStamp(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.XtimInfo.getAcqStamp` in interface :class:`~cern.lsa.domain.cern.timing.XtimInfo`
        
        
        """
        ...
    def getEvenTypeName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.XtimInfo.getEvenTypeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.XtimInfo`
        
        
        """
        ...
    def getMilliseconde(self) -> int:
        """
            la miliseconde dans le cycle a laquelle le timing est sorti... dans le cas du LHC, il y a un "user" qui est joue pour
            des raisons de compatibilite avec FESA, c'est toujours le meme ("LHC") et il dure une BasicPeriod, laquelle, au LHC, est
            1s
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.XtimInfo.getMilliseconde`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.XtimInfo`
        
            Returns:
        
        
        """
        ...
    def getOccurence(self) -> int:
        """
            nombre de fois qu'un timing est sorti; sur certains timings (a grande frequence) il se peut que ces nombre ne soit pas
            recu dans l'ordre au niveau de l'aplication graphique (Fesa Navigateur par exemple)
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.XtimInfo.getOccurence` in interface :class:`~cern.lsa.domain.cern.timing.XtimInfo`
        
            Returns:
        
        
        """
        ...
    def getPayload(self) -> int:
        """
            la payload de l'evenement en question(CTIM) ou la payload de l'evenement qui demarre un LTIM(dans le cas ou un XTIM est
            lie a un LTIM)
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.XtimInfo.getPayload` in interface :class:`~cern.lsa.domain.cern.timing.XtimInfo`
        
            Returns:
        
        
        """
        ...
    def getUtcNanoseconde(self) -> int:
        """
            la nanoseconde de la seconde UTC
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.XtimInfo.getUtcNanoseconde`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.timing.XtimInfo`
        
            Returns:
        
        
        """
        ...
    def getUtcSeconde(self) -> int:
        """
            le temps UTC, en secondes, auquel le timing est sorti
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.XtimInfo.getUtcSeconde` in interface :class:`~cern.lsa.domain.cern.timing.XtimInfo`
        
            Returns:
        
        
        """
        ...
    def getXtimName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.timing.XtimInfo.getXtimName` in interface :class:`~cern.lsa.domain.cern.timing.XtimInfo`
        
        
        """
        ...
    def setAcqStamp(self, long: int) -> None: ...
    def setMilliseconde(self, long: int) -> None: ...
    def setOccurence(self, long: int) -> None: ...
    def setPayload(self, long: int) -> None: ...
    def setUtcNanoseconde(self, long: int) -> None: ...
    def setUtcSeconde(self, long: int) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.timing.spi")``.

    ActiveTimingUsersImpl: typing.Type[ActiveTimingUsersImpl]
    BunchPatternImpl: typing.Type[BunchPatternImpl]
    EventTableImpl: typing.Type[EventTableImpl]
    EventTableStatusImpl: typing.Type[EventTableStatusImpl]
    EventTypeImpl: typing.Type[EventTypeImpl]
    LhcCirculatingBunchConfigurationImpl: typing.Type[LhcCirculatingBunchConfigurationImpl]
    LhcInjectionBunchConfigurationImpl: typing.Type[LhcInjectionBunchConfigurationImpl]
    LhcInjectionImpl: typing.Type[LhcInjectionImpl]
    LhcInjectionSchemeEntryImpl: typing.Type[LhcInjectionSchemeEntryImpl]
    LhcInjectionSchemeImpl: typing.Type[LhcInjectionSchemeImpl]
    LoadedEventTableImpl: typing.Type[LoadedEventTableImpl]
    TimingEventImpl: typing.Type[TimingEventImpl]
    TimingEventSchedulingImpl: typing.Type[TimingEventSchedulingImpl]
    TimingProcessImpl: typing.Type[TimingProcessImpl]
    TimingProcessSchedulingImpl: typing.Type[TimingProcessSchedulingImpl]
    XtimInfoImpl: typing.Type[XtimInfoImpl]
