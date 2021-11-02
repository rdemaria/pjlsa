import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import cern.lsa.domain.cern.timing.enums
import cern.lsa.domain.cern.timing.spi
import java.lang
import java.util
import typing



class ActiveTimingUsers:
    """
    public interface ActiveTimingUsers
    
        Holds information about currently played timing users i.e. users defined in the active Beam Card Deck.
    
        To understand more the BCD - look at the :code:`accsoft-timing-app-bcdsetviewer` and/or contact J.C. Bau.
    """
    def contains(self, string: str) -> bool:
        """
            Returns :code:`true` if the specified user is contained in the list of
            :meth:`~cern.lsa.domain.cern.timing.ActiveTimingUsers.getNormalUsers` or in the list of
            :meth:`~cern.lsa.domain.cern.timing.ActiveTimingUsers.getSpareUsers`.
        
            Parameters:
                user (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the considered user
        
            Returns:
                :code:`true` if the given user is active (normal or spare) in the active BCD, :code:`false` otherwise
        
        
        """
        ...
    def getNormalUsers(self) -> java.util.List[str]: ...
    def getSpareUsers(self) -> java.util.List[str]: ...

class BunchPattern:
    """
    public interface BunchPattern
    
        a Bunch pattern is a list of LHC bunch position filled by one SPS injection into the LHC. The position unit is the
        bucket the first position is always 0. When associated with a bunch configuration that contain the first filled bucket
        number, we get all the absolute bucket position for each bunch
    """
    def addBunchPosition(self, int: int) -> None:
        """
            add a new bunch at the given position
        
            Parameters:
                relativeBucketNbr (int): : the bucket number relative to the first bunch bucket nbr
        
        
        """
        ...
    def getBatchSpacing(self) -> int:
        """
        
            Returns:
                the batch spacing- if the spacing between batches is different it returns the minimum batch spacing.
        
        
        """
        ...
    def getBunchPatternDescription(self) -> str:
        """
        
            Returns:
                a string giving a description of the bunch pattern
        
        
        """
        ...
    def getBunchPatternName(self) -> str:
        """
        
            Returns:
                the name of the bunch pattern
        
        
        """
        ...
    def getBunchSpacing(self) -> int:
        """
        
            Returns:
                the space between 2 consecutive bunches in ns.
        
        
        """
        ...
    def getBunchesPosition(self) -> typing.List[int]:
        """
        
            Returns:
                the relative bunch positions in bucket unit the int[] array is always in increasing order
        
        
        """
        ...
    def getNbrOfBunches(self) -> int:
        """
        
            Returns:
                the number of bunches that will be injected
        
        
        """
        ...
    def getNbrOfBunchesPerPSBatch(self) -> int:
        """
        
            Returns:
                the number of bunches for each PS batch
        
        
        """
        ...
    def getNbrOfPSBatches(self) -> int:
        """
        
            Returns:
                the number of PS batches that will be injected.
        
        
        """
        ...
    def isDoubletsBeam(self) -> bool:
        """
        
            Returns:
                :code:`true` if the pattern is a pattern of a doublet beam.
        
        
        """
        ...
    def setBunchPositions(self, intArray: typing.List[int]) -> None:
        """
            set the bunches positions
        
            Parameters:
                buketNumbers (int[]): : the buckets filled by bunches
        
        
        """
        ...
    def setBunchSpacing(self, int: int) -> None:
        """
        
            Parameters:
                bunchSpacing (int): the bunchSpacing to set
        
        
        """
        ...
    def setDoubletsBeam(self, boolean: bool) -> None:
        """
        
            Parameters:
                doubletsBeam (boolean): indicates if the pattern is of a doublet beam
        
            Also see:
                :meth:`~cern.lsa.domain.cern.timing.BunchPattern.isDoubletsBeam`
        
        
        """
        ...
    def setNbrOfBunches(self, int: int) -> None:
        """
        
            Parameters:
                nbrOfBunches (int): the nbrOfBunches to set
        
        
        """
        ...
    def setNbrOfBunchesPerPSBatch(self, int: int) -> None:
        """
        
            Parameters:
                nbrOfBunchesPerPSBatch (int): the nbrOfBunchesPerPSBatch to set
        
        
        """
        ...
    def setNbrOfPSBatches(self, int: int) -> None:
        """
        
            Parameters:
                nbrOfPSBatches (int): the nbrOfPSBatches to set
        
        
        """
        ...

class Event(java.lang.Comparable['Event'], cern.accsoft.commons.util.Named):
    """
    public interface Event extends `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.Event`>, cern.accsoft.commons.util.Named
    
        Basic element in the timing API, the :code:`Event` class represents the timing events sent over the General Machine
        Timing (GMT). Each :code:`Event` instance can have a payload (16-bit value). Two instances with the same name can have a
        different payload.
    """
    def getDescription(self) -> str:
        """
        
            Returns:
                the event description
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                the event name
        
        
        """
        ...
    def getPayload(self) -> int:
        """
        
            Returns:
                the event payload
        
        
        """
        ...
    def getType(self) -> 'EventType':
        """
            Returns the :code:`EventType` which this :code:`Event` is based on.
        
            Returns:
                the :code:`EventType` of the :code:`Event`.
        
        
        """
        ...

class EventTable:
    """
    public interface EventTable
    
        An :code:`EventTable` represents a list of :code:`Event`s with, for each entry, a time offset (in millisecond) relative
        to the start of the table. A table can be run once, any number of time or infinitely until stopped. An
        :code:`EventTable` is started by the specified event.
    """
    INFINITE_RUN: typing.ClassVar[int] = ...
    """
    static final int INFINITE_RUN
    
        Tells the timing system to run the table forever
    
        Also see:
            :meth:`~constant`
    
    
    """
    def addEvent(self, event: Event, int: int) -> bool:
        """
            Adds an event in the table.
        
            Parameters:
                event (:class:`~cern.lsa.domain.cern.timing.Event`): : event to be added.
                offsetMs (int): : time offset of the new event. This value must be positive or zero
        
        
        """
        ...
    def addEvents(self, sortedSet: java.util.SortedSet['EventTableEntry']) -> None: ...
    def getEventList(self) -> java.util.SortedSet['EventTableEntry']: ...
    def getName(self) -> str:
        """
            Returns the table name
        
        """
        ...
    def getRunCount(self) -> int:
        """
            Returns the table run count i.e. the number of times the timing system will play it.
        
            Returns:
                the table run count.
        
        
        """
        ...
    def getStartingEvent(self) -> Event:
        """
            Returns the :code:`Event` the table will be started on.
        
            Returns:
                the starting event
        
        
        """
        ...
    def removeEvent(self, event: Event, int: int) -> None:
        """
            Removes the given event with the given offset
        
            Parameters:
                event (:class:`~cern.lsa.domain.cern.timing.Event`): : the event to remove
                offsetMs (int): : the event's offset
        
        
        """
        ...
    def removeEvents(self) -> None:
        """
            Removes all the events.
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Sets table name
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the table name
        
        
        """
        ...
    def setRunCount(self, int: int) -> None:
        """
            Sets the table run count i.e. the number of times the timing system will play it.
        
            Parameters:
                runCount (int): the table run count.
        
        
        """
        ...
    def setStartingEvent(self, event: Event) -> None:
        """
            Sets the starting event for this table.
        
            Parameters:
                event (:class:`~cern.lsa.domain.cern.timing.Event`): the starting event
        
        
        """
        ...

class EventTableEntry(java.lang.Comparable['EventTableEntry']):
    """
    public interface EventTableEntry extends `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.EventTableEntry`>
    
        This interface represents the entries in a :code:`EventTable`.
    """
    def getEvent(self) -> Event:
        """
            Return the event associated with this entry
        
        """
        ...
    def getOffset(self) -> int:
        """
            Returns the time offset in milliseconds.
        
        """
        ...

class EventTableStatus:
    def getHardwareStatus(self) -> java.util.List[cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW]: ...
    def getSoftwareStatus(self) -> cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW: ...
    def getTableName(self) -> str: ...

class EventType(cern.accsoft.commons.util.Named):
    def getDescription(self) -> str: ...
    def getEvent(self, int: int) -> Event: ...
    def getGroup(self) -> str: ...
    def getName(self) -> str: ...
    def getXtimName(self) -> str: ...

class InvalidEventException(java.lang.RuntimeException):
    """
    public class InvalidEventException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
        Exception thrown when a timing event is invalid
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class InvalidEventTableEntryException(java.lang.RuntimeException):
    """
    public class InvalidEventTableEntryException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
        Exception thrown when an event table entry is invalid (offset negative...)
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class InvalidEventTableException(java.lang.RuntimeException):
    """
    public class InvalidEventTableException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
        Exception thrown when an event table is invalid (no run count, no starting event...)
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class LhcCirculatingBunchConfiguration:
    """
    public interface LhcCirculatingBunchConfiguration
    """
    def getBeamNbr(self) -> int: ...
    def getFilledBuckets(self) -> java.util.SortedSet[int]: ...
    def getFirstFilledBucket(self) -> int: ...

class LhcInjection(cern.accsoft.commons.util.Named):
    """
    public interface LhcInjection extends cern.accsoft.commons.util.Named
    
        This class represent an lhc injection. It contains the fields necessary to post an injection request to the timing
        system, and some additional fields for information Some field need to be clarified like nextInjectionBeamType and
        nextInjectionParticleType.
    """
    def getBunchConfiguration(self) -> 'LhcInjectionBunchConfiguration':
        """
        
            Returns:
                the bunch configuration (the buckets that will be filled by the injected beam)
        
        
        """
        ...
    def getNextInjectionBeamType(self) -> cern.lsa.domain.cern.timing.enums.BEAM_TYPE:
        """
        
            Returns:
                the beam type (intermediate or nominal intensity)
        
        
        """
        ...
    def getNextInjectionBunchIntensity(self) -> int:
        """
        
            Returns:
                the intensity per bunch
        
        
        """
        ...
    def getNextInjectionBunchNumber(self) -> int:
        """
        
            Returns:
                the number of bunch that will be injected
        
        
        """
        ...
    def getNextInjectionBunchSpacing(self) -> int:
        """
        
            Returns:
                the space (in ns) between 2 bunches
        
        
        """
        ...
    def getNextInjectionNbrOfBunchesPerPSBatch(self) -> int:
        """
        
            Returns:
                the number of bunches for each PS batch
        
        
        """
        ...
    def getNextInjectionPSbatchNbr(self) -> int:
        """
        
            Returns:
                the number of batches in the PS needed for the next beam this info is needed to post an injection request to the timing
                system
        
        
        """
        ...
    def getNextInjectionParticleType(self) -> int:
        """
        
            Returns:
                the particle type of the next injected beam
        
        
        """
        ...
    def getNextInjectionRFBucket(self) -> int:
        """
        
            Returns:
                the bucket number where the first bunch will be injected this info is needed to post an injection request to the timing
                system
        
        
        """
        ...
    def getNextInjectionRing(self) -> cern.lsa.domain.cern.timing.enums.RNGI:
        """
        
            Returns:
                the ring that will receive the next injection this info is needed to post an injection request to the timing system
        
        
        """
        ...
    def setBunchConfiguration(self, lhcInjectionBunchConfiguration: 'LhcInjectionBunchConfiguration') -> None:
        """
            set the associated bunch configuration
        
            Parameters:
                bunchConfiguration (:class:`~cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration`): 
        
        """
        ...
    def setName(self, string: str) -> None: ...
    def setNextInjectionBeamType(self, bEAM_TYPE: cern.lsa.domain.cern.timing.enums.BEAM_TYPE) -> None:
        """
        
            Parameters:
                nextInjectionBeamType (:class:`~cern.lsa.domain.cern.timing.enums.BEAM_TYPE`): 
        
        """
        ...
    def setNextInjectionBunchIntensity(self, int: int) -> None:
        """
            Set the intensity per bunch
        
            Parameters:
                nextInjectionBunchIntensity (int): 
        
        """
        ...
    def setNextInjectionParticleType(self, int: int) -> None:
        """
            set the particle type of the next injected beam
        
            Parameters:
                nextInjectionParticleType (int): 
        
        """
        ...
    @typing.overload
    def setNextInjectionRing(self, rNGI: cern.lsa.domain.cern.timing.enums.RNGI) -> None:
        """
            Set the next injection ring
        
            Parameters:
                nextInjectionRing (int): : an integer 0=beam 1, 1=beam2, 2= no beam
        
            set the next injection ring
        
            Parameters:
                nextInjectionRing (:class:`~cern.lsa.domain.cern.timing.enums.RNGI`): : enum giving the possible rings
        
        
        """
        ...
    @typing.overload
    def setNextInjectionRing(self, int: int) -> None: ...

class LhcInjectionBunchConfiguration(cern.accsoft.commons.util.Named):
    """
    public interface LhcInjectionBunchConfiguration extends cern.accsoft.commons.util.Named
    
        The LhcInjectionBunchConfiguration represents the list of buckets that will be filled after injecting beam into LHC It
        is attached to a injection request. The bucket list is always ordered and the list index gives the bunch number A map is
        also available for compatibility with ClientDIPControllerImpl, but this class could be modified to use the method get
        filled buckets
    """
    def getBunchPattern(self) -> BunchPattern:
        """
        
            Returns:
                the bunch pattern used for this configuration
        
        
        """
        ...
    def getFilledBuckets(self) -> typing.List[int]:
        """
            returns an int array of the bucket number that will be filled at the next injection The bucket numbers are the absolute
            bucket number values
        
        """
        ...
    def getFirstFilledBucket(self) -> int:
        """
        
            Returns:
                the first bucket that is filled by the next injection
        
        
        """
        ...
    def setBunchPattern(self, bunchPattern: BunchPattern) -> None:
        """
            set the bunch pattern
        
            Parameters:
                bunchPattern (:class:`~cern.lsa.domain.cern.timing.BunchPattern`): 
        
        """
        ...
    def setFirstFilledBucket(self, int: int) -> None:
        """
            set the first bucket that is filled by the next injection
        
            Parameters:
                firstBucket (int): 
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Set the name of the configuration A configuration can be created without name, but a name should be set before the
            configuration is saved to the database
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...

class LhcInjectionScheme:
    """
    public interface LhcInjectionScheme
    
        This class represent a serie of predefiened injection that are ordered and have to be requested one after the other.
    """
    def addInjection(self, lhcInjection: LhcInjection) -> None:
        """
            add an entry to the existing entry list
        
            Parameters:
                anInjection (:class:`~cern.lsa.domain.cern.timing.LhcInjection`): : the new injection to add
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            get the date the scheme has been created
        
            Returns:
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            get the description text for the scheme
        
            Returns:
                the description
        
        
        """
        ...
    def getInjectionSchemeGroup(self) -> str:
        """
        
            Returns:
                the category of the injection Scheme
        
        
        """
        ...
    def getInjectionSchemeName(self) -> str:
        """
        
            Returns:
                the name of the injection scheme
        
        
        """
        ...
    def getInjections(self) -> java.util.Set[LhcInjection]: ...
    def getMinBunchSpacing(self) -> int:
        """
            returns the minimum bunch spacing of the scheme
        
            Returns:
        
        
        """
        ...
    def getNbCollisionIP1(self) -> int:
        """
            returns the number of collision in IP1 we obtain from this scheme.
        
            Returns:
        
        
        """
        ...
    def getNbCollisionIP2(self) -> int:
        """
            returns the number of collision in IP2 we obtain from this scheme.
        
            Returns:
        
        
        """
        ...
    def getNbCollisionIP5(self) -> int:
        """
            returns the number of collision in IP5 we obtain from this scheme.
        
            Returns:
        
        
        """
        ...
    def getNbCollisionIP8(self) -> int:
        """
            returns the number of collision in IP8 we obtain from this scheme.
        
            Returns:
        
        
        """
        ...
    def getNumberOfBunchesB1(self) -> int:
        """
        
            Returns:
                the number of bunches for beam 1
        
        
        """
        ...
    def getNumberOfBunchesB2(self) -> int:
        """
        
            Returns:
                the number of bunches for beam 2
        
        
        """
        ...
    def getPilotPositionB1(self) -> int:
        """
        
            Returns:
                the position of the pilot for beam 1
        
        
        """
        ...
    def getPilotPositionB2(self) -> int:
        """
        
            Returns:
                the position of the pilot for beam 2
        
        
        """
        ...
    def getPredictedBunchConfiguration(self, rNGI: cern.lsa.domain.cern.timing.enums.RNGI) -> typing.List[int]:
        """
            get the predicted circulation bunch configuration after all the injection defined in the scheme have been send an
            successfully executed
        
            Returns:
                an int array with the filled bucket numbers
        
        
        """
        ...
    def isInjectionCleaningEnabled(self) -> bool:
        """
        
            Returns:
                true if the injection cleaning has to be enabled by default.
        
        
        """
        ...
    def isWithOverInjection(self) -> bool:
        """
        
            Returns:
                true if an overinjection is needed with this scheme
        
        
        """
        ...
    def removeInjection(self, lhcInjection: LhcInjection) -> None: ...
    def setBunchIntForAllRequests(self, int: int) -> None:
        """
            change the bunch intensity for all the requests
        
            Parameters:
                the (int): intensity to set in 10E9 particles unit
        
        
        """
        ...
    def setDescription(self, string: str) -> None:
        """
            set the description text for the scheme
        
            Parameters:
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...
    def setInjectionSchemeGroup(self, string: str) -> None:
        """
        
            Parameters:
                categorie (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): : the name of the scheme category
        
        
        """
        ...
    def setInjectionSchemeName(self, string: str) -> None:
        """
            set the name of the scheme
        
            Parameters:
                injectionSchemeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...
    def setIsInjectionCleaningEnabled(self, boolean: bool) -> None:
        """
        
            Parameters:
                injectionCleaningEnabled (boolean): 
        
        """
        ...
    def setIsWithOverInjection(self, boolean: bool) -> None:
        """
        
            Parameters:
                withOverInjection (boolean): 
        
        """
        ...
    def setNbCollisionIP1(self, int: int) -> None:
        """
            set the number of collision in IP1 we obtain from this scheme.
        
            Parameters:
                nbCollisionIP1 (int): 
        
        """
        ...
    def setNbCollisionIP2(self, int: int) -> None:
        """
            set the number of collision in IP2 we obtain from this scheme.
        
            Parameters:
                nbCollisionIP2 (int): 
        
        """
        ...
    def setNbCollisionIP5(self, int: int) -> None:
        """
            set the number of collision in IP5 we obtain from this scheme.
        
            Parameters:
                nbCollisionIP5 (int): 
        
        """
        ...
    def setNbCollisionIP8(self, int: int) -> None:
        """
            set the number of collision in IP8 we obtain from this scheme.
        
            Parameters:
                nbCollisionIP8 (int): 
        
        """
        ...
    def setPilotPositionB1(self, int: int) -> None:
        """
            set the position of the pilot for beam 2
        
        """
        ...
    def setPilotPositionB2(self, int: int) -> None:
        """
            set the position of the pilot for beam 2
        
        """
        ...

class LhcInjectionSchemeEntry_Obs(java.lang.Comparable['LhcInjectionSchemeEntry_Obs']):
    """
    public interface LhcInjectionSchemeEntry_Obs extends `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs`>
    """
    def getDelay(self) -> int: ...
    def getInjection(self) -> LhcInjection: ...
    def getInjectionOrder(self) -> int: ...
    def setDelay(self, int: int) -> None: ...
    def setInjectionOrder(self, int: int) -> None: ...

class LoadedEventTable:
    """
    public interface LoadedEventTable
    """
    def getEventTable(self) -> EventTable:
        """
        
            Returns:
                the event table
        
        
        """
        ...
    def getTableStatus(self) -> EventTableStatus:
        """
        
            Returns:
                the event table status. It contains the software and the hardware statuses.
        
        
        """
        ...

class LowLevelTimingException(java.lang.RuntimeException):
    """
    public class LowLevelTimingException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
        Root class of the low level timing exception hierarchy (under construction...) This class is thrown when the system
        encounters any kind of problem
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class NoSuchEventTableException(java.lang.Exception):
    """
    public class NoSuchEventTableException extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`
    
        Exception thrown when the finder can't find the given table
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class NoSuchEventTypeException(java.lang.Exception):
    """
    public class NoSuchEventTypeException extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`
    
        Exception thrown when the finder can't find an event type with the given name.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class TimingEvent(cern.accsoft.commons.util.Named):
    """
    public interface TimingEvent extends cern.accsoft.commons.util.Named
    
        Timing event that can be sent by the Central Timing.
    """
    def getHardwareEventName(self) -> str:
        """
            Returns name of the physical hardware event sent on the wire. Note that a single hardware event can be used for several
            logical events.
        
            Returns:
                name of the physical hardware event
        
        
        """
        ...
    def getName(self) -> str:
        """
            Logical name of the event i.e. name to be used by the operations team. The name of physical hardware event sent on the
            wire you can retrieve using :meth:`~cern.lsa.domain.cern.timing.TimingEvent.getHardwareEventName`. Several logical
            events can be associated with the same hardware event.
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                logical (OP) name of the timing event
        
        
        """
        ...
    def getPayloadAttributeName(self) -> str:
        """
            Returns name of a cycle segment attribute whose value should be used as a payload for this event. Can be :code:`null` if
            the event doesn't carry any payload.
        
        """
        ...

class TimingEventScheduling:
    """
    public interface TimingEventScheduling
    
        Represents scheduling of a timing event within a :class:`~cern.lsa.domain.cern.timing.TimingProcess`.
    """
    def getOffsetInMillis(self) -> int:
        """
        
            Returns:
                offset (negative or positive) relative to the time of the parent process
        
        
        """
        ...
    def getTimingEvent(self) -> TimingEvent:
        """
        
            Returns:
                the scheduled timing event
        
        
        """
        ...

class TimingProcess(cern.accsoft.commons.util.Named):
    """
    public interface TimingProcess extends cern.accsoft.commons.util.Named
    
        Represents a family of timing events that linked together i.e. either all of them or none of them should be sent. Timing
        process can represent for instance all events related to start of a ramp.
    """
    def getScheduledTimingEvents(self) -> java.util.Set[TimingEventScheduling]: ...
    def getTimingDomain(self) -> cern.accsoft.commons.domain.TimingDomain:
        """
        
            Returns:
                non-null timing domain for which the process is defined
        
        
        """
        ...

class TimingProcessAnchor(java.lang.Enum['TimingProcessAnchor']):
    """
    public enum TimingProcessAnchor extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.TimingProcessAnchor`>
    
        Indicates if the :meth:`~cern.lsa.domain.cern.timing.TimingProcessScheduling.getOffsetInMillis` is relative to the start
        or the end of the segment.
    """
    SEGMENT_START: typing.ClassVar['TimingProcessAnchor'] = ...
    SEGMENT_END: typing.ClassVar['TimingProcessAnchor'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TimingProcessAnchor':
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
    def values() -> typing.List['TimingProcessAnchor']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (TimingProcessAnchor c : TimingProcessAnchor.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TimingProcessScheduling:
    """
    public interface TimingProcessScheduling
    
        Represents scheduling of a :class:`~cern.lsa.domain.cern.timing.TimingProcess` within a cycle segment.
    """
    def getOffsetInMillis(self) -> int:
        """
        
            Returns:
                offset (negative or positive) in milliseconds relative to the time of the cycle segment start
        
            Also see:
                :meth:`~cern.lsa.domain.cern.timing.TimingProcessScheduling.setOffsetInMillis`
        
        
        """
        ...
    def getTimingProcess(self) -> TimingProcess:
        """
        
            Returns:
                the scheduled timing process
        
        
        """
        ...
    def getTimingProcessAnchor(self) -> TimingProcessAnchor:
        """
        
            Returns:
                the current anchor of the scheduling
        
        
        """
        ...
    def setOffsetInMillis(self, int: int) -> None:
        """
        
            Parameters:
                offsetInMillis (int): (negative or positive) in milliseconds relative to the time of the cycle segment start
        
            Also see:
                :meth:`~cern.lsa.domain.cern.timing.TimingProcessScheduling.getOffsetInMillis`
        
        
        """
        ...
    def setTimingProcessAnchor(self, timingProcessAnchor: TimingProcessAnchor) -> None:
        """
        
            Parameters:
                anchor (:class:`~cern.lsa.domain.cern.timing.TimingProcessAnchor`): anchor to be used for this scheduling
        
        
        """
        ...

class XtimInfo:
    """
    public interface XtimInfo
    """
    def getAcqStamp(self) -> int: ...
    def getEvenTypeName(self) -> str: ...
    def getMilliseconde(self) -> int:
        """
            la miliseconde dans le cycle a laquelle le timing est sorti... dans le cas du LHC, il y a un "user" qui est joue pour
            des raisons de compatibilite avec FESA, c'est toujours le meme ("LHC") et il dure une BasicPeriod, laquelle, au LHC, est
            1s
        
            Returns:
        
        
        """
        ...
    def getOccurence(self) -> int:
        """
            nombre de fois qu'un timing est sorti; sur certains timings (a grande frequence) il se peut que ces nombre ne soit pas
            recu dans l'ordre au niveau de l'aplication graphique (Fesa Navigateur par exemple)
        
            Returns:
        
        
        """
        ...
    def getPayload(self) -> int:
        """
            la payload de l'evenement en question(CTIM) ou la payload de l'evenement qui demarre un LTIM(dans le cas ou un XTIM est
            lie a un LTIM)
        
            Returns:
        
        
        """
        ...
    def getUtcNanoseconde(self) -> int:
        """
            la nanoseconde de la seconde UTC
        
            Returns:
        
        
        """
        ...
    def getUtcSeconde(self) -> int:
        """
            le temps UTC, en secondes, auquel le timing est sorti
        
            Returns:
        
        
        """
        ...
    def getXtimName(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.timing")``.

    ActiveTimingUsers: typing.Type[ActiveTimingUsers]
    BunchPattern: typing.Type[BunchPattern]
    Event: typing.Type[Event]
    EventTable: typing.Type[EventTable]
    EventTableEntry: typing.Type[EventTableEntry]
    EventTableStatus: typing.Type[EventTableStatus]
    EventType: typing.Type[EventType]
    InvalidEventException: typing.Type[InvalidEventException]
    InvalidEventTableEntryException: typing.Type[InvalidEventTableEntryException]
    InvalidEventTableException: typing.Type[InvalidEventTableException]
    LhcCirculatingBunchConfiguration: typing.Type[LhcCirculatingBunchConfiguration]
    LhcInjection: typing.Type[LhcInjection]
    LhcInjectionBunchConfiguration: typing.Type[LhcInjectionBunchConfiguration]
    LhcInjectionScheme: typing.Type[LhcInjectionScheme]
    LhcInjectionSchemeEntry_Obs: typing.Type[LhcInjectionSchemeEntry_Obs]
    LoadedEventTable: typing.Type[LoadedEventTable]
    LowLevelTimingException: typing.Type[LowLevelTimingException]
    NoSuchEventTableException: typing.Type[NoSuchEventTableException]
    NoSuchEventTypeException: typing.Type[NoSuchEventTypeException]
    TimingEvent: typing.Type[TimingEvent]
    TimingEventScheduling: typing.Type[TimingEventScheduling]
    TimingProcess: typing.Type[TimingProcess]
    TimingProcessAnchor: typing.Type[TimingProcessAnchor]
    TimingProcessScheduling: typing.Type[TimingProcessScheduling]
    XtimInfo: typing.Type[XtimInfo]
    enums: cern.lsa.domain.cern.timing.enums.__module_protocol__
    spi: cern.lsa.domain.cern.timing.spi.__module_protocol__
