import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import cern.lsa.domain.cern.timing
import cern.lsa.domain.cern.timing.enums
import java.io
import java.util
import typing



class ActiveTimingUsersImpl(cern.lsa.domain.cern.timing.ActiveTimingUsers, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.ActiveTimingUsersImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.ActiveTimingUsers,
            java.io.Serializable
    
      Constructors:
        * ActiveTimingUsersImpl()
        * ActiveTimingUsersImpl(java.util.List, java.util.List)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, list: java.util.List[str], list2: java.util.List[str]): ...
    def contains(self, string: str) -> bool: ...
    def getNormalUsers(self) -> java.util.List[str]: ...
    def getSpareUsers(self) -> java.util.List[str]: ...

class BunchPatternImpl(cern.lsa.domain.cern.timing.BunchPattern, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.BunchPatternImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.BunchPattern, java.io.Serializable
    
      Constructors:
        * BunchPatternImpl(java.lang.String, java.lang.String)
    
    """
    def __init__(self, string: str, string2: str): ...
    def addBunchPosition(self, int: int) -> None: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBatchSpacing(self) -> int: ...
    def getBunchPatternDescription(self) -> str: ...
    def getBunchPatternName(self) -> str: ...
    def getBunchSpacing(self) -> int: ...
    def getBunchesPosition(self) -> typing.List[int]: ...
    def getNbrOfBunches(self) -> int: ...
    def getNbrOfBunchesPerPSBatch(self) -> int: ...
    def getNbrOfPSBatches(self) -> int: ...
    def hashCode(self) -> int: ...
    def isDoubletsBeam(self) -> bool: ...
    def setBatchSpacing(self, int: int) -> None: ...
    def setBunchPositions(self, intArray: typing.List[int]) -> None: ...
    def setBunchSpacing(self, int: int) -> None: ...
    def setDoubletsBeam(self, boolean: bool) -> None: ...
    def setNbrOfBunches(self, int: int) -> None: ...
    def setNbrOfBunchesPerPSBatch(self, int: int) -> None: ...
    def setNbrOfPSBatches(self, int: int) -> None: ...
    def toString(self) -> str: ...

class EventTableImpl(cern.lsa.domain.cern.timing.EventTable, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.EventTableImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.EventTable, java.io.Serializable
    
      Constructors:
        * EventTableImpl()
        * EventTableImpl(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    def addEvent(self, event: cern.lsa.domain.cern.timing.Event, int: int) -> bool: ...
    def addEvents(self, sortedSet: java.util.SortedSet[cern.lsa.domain.cern.timing.EventTableEntry]) -> None: ...
    def dumpTable(self) -> str: ...
    def getEventList(self) -> java.util.SortedSet[cern.lsa.domain.cern.timing.EventTableEntry]: ...
    def getName(self) -> str: ...
    def getRunCount(self) -> int: ...
    def getStartingEvent(self) -> cern.lsa.domain.cern.timing.Event: ...
    def removeEvent(self, event: cern.lsa.domain.cern.timing.Event, int: int) -> None: ...
    def removeEvents(self) -> None: ...
    def setName(self, string: str) -> None: ...
    def setRunCount(self, int: int) -> None: ...
    def setStartingEvent(self, event: cern.lsa.domain.cern.timing.Event) -> None: ...
    def toString(self) -> str: ...

class EventTableStatusImpl(cern.lsa.domain.cern.timing.EventTableStatus, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.EventTableStatusImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.EventTableStatus,
            java.io.Serializable
    
      Constructors:
        * EventTableStatusImpl(java.lang.String, cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW, java.util.List)
    
    """
    def __init__(self, string: str, tABLE_STATUS_SW: cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW, list: java.util.List[cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW]): ...
    def getHardwareStatus(self) -> java.util.List[cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW]: ...
    def getSoftwareStatus(self) -> cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW: ...
    def getTableName(self) -> str: ...
    def toString(self) -> str: ...

class EventTypeImpl(cern.lsa.domain.cern.timing.EventType, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.EventTypeImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.EventType, java.io.Serializable
    
      Constructors:
        * EventTypeImpl(java.lang.String, java.lang.String, java.lang.String)
    
    """
    def __init__(self, string: str, string2: str, string3: str): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDescription(self) -> str: ...
    def getEvent(self, int: int) -> cern.lsa.domain.cern.timing.Event: ...
    def getGroup(self) -> str: ...
    def getName(self) -> str: ...
    def getXtimName(self) -> str: ...
    def hashCode(self) -> int: ...
    def setGroup(self, string: str) -> None: ...
    def toString(self) -> str: ...

class LhcCirculatingBunchConfigurationImpl(cern.lsa.domain.cern.timing.LhcCirculatingBunchConfiguration, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.LhcCirculatingBunchConfigurationImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.LhcCirculatingBunchConfiguration,
            java.io.Serializable
    
      Constructors:
        * LhcCirculatingBunchConfigurationImpl()
    
    """
    def __init__(self): ...
    def addFilledBucket(self, int: int) -> None: ...
    def getBeamNbr(self) -> int: ...
    def getFilledBuckets(self) -> java.util.SortedSet[int]: ...
    def getFirstFilledBucket(self) -> int: ...
    def setBeamNbr(self, int: int) -> None: ...

class LhcInjectionBunchConfigurationImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration], cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.LhcInjectionBunchConfigurationImpl'
    
        Extends:
            cern.accsoft.commons.util.AbstractNamedSerializable
    
        Interfaces:
            cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration,
            java.io.Serializable
    
      Constructors:
        * LhcInjectionBunchConfigurationImpl()
        * LhcInjectionBunchConfigurationImpl(java.lang.String, int)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBunchPattern(self) -> cern.lsa.domain.cern.timing.BunchPattern: ...
    def getFilledBuckets(self) -> typing.List[int]: ...
    def getFirstFilledBucket(self) -> int: ...
    def hashCode(self) -> int: ...
    def setBunchPattern(self, bunchPattern: cern.lsa.domain.cern.timing.BunchPattern) -> None: ...
    def setFirstFilledBucket(self, int: int) -> None: ...
    def toString(self) -> str: ...

class LhcInjectionImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.timing.LhcInjection], cern.lsa.domain.cern.timing.LhcInjection):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.LhcInjectionImpl'
    
        Extends:
            cern.accsoft.commons.util.AbstractNamedSerializable
    
        Interfaces:
            cern.lsa.domain.cern.timing.LhcInjection
    
      Constructors:
        * LhcInjectionImpl()
    
    """
    def __init__(self): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBunchConfiguration(self) -> cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration: ...
    def getNextInjectionBeamType(self) -> cern.lsa.domain.cern.timing.enums.BEAM_TYPE: ...
    def getNextInjectionBunchIntensity(self) -> int: ...
    def getNextInjectionBunchNumber(self) -> int: ...
    def getNextInjectionBunchSpacing(self) -> int: ...
    def getNextInjectionNbrOfBunchesPerPSBatch(self) -> int: ...
    def getNextInjectionPSbatchNbr(self) -> int: ...
    def getNextInjectionParticleType(self) -> int: ...
    def getNextInjectionRFBucket(self) -> int: ...
    def getNextInjectionRing(self) -> cern.lsa.domain.cern.timing.enums.RNGI: ...
    def hashCode(self) -> int: ...
    def setBunchConfiguration(self, lhcInjectionBunchConfiguration: cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration) -> None: ...
    def setNextInjectionBeamType(self, bEAM_TYPE: cern.lsa.domain.cern.timing.enums.BEAM_TYPE) -> None: ...
    def setNextInjectionBunchIntensity(self, int: int) -> None: ...
    def setNextInjectionParticleType(self, int: int) -> None: ...
    @typing.overload
    def setNextInjectionRing(self, rNGI: cern.lsa.domain.cern.timing.enums.RNGI) -> None: ...
    @typing.overload
    def setNextInjectionRing(self, int: int) -> None: ...
    def toString(self) -> str: ...

class LhcInjectionSchemeEntryImpl(cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.LhcInjectionSchemeEntryImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs,
            java.io.Serializable
    
      Constructors:
        * LhcInjectionSchemeEntryImpl(cern.lsa.domain.cern.timing.LhcInjection, int, int)
    
    """
    def __init__(self, lhcInjection: cern.lsa.domain.cern.timing.LhcInjection, int: int, int2: int): ...
    def compareTo(self, lhcInjectionSchemeEntry_Obs: cern.lsa.domain.cern.timing.LhcInjectionSchemeEntry_Obs) -> int: ...
    def getDelay(self) -> int: ...
    def getInjection(self) -> cern.lsa.domain.cern.timing.LhcInjection: ...
    def getInjectionOrder(self) -> int: ...
    def setDelay(self, int: int) -> None: ...
    def setInjectionOrder(self, int: int) -> None: ...

class LhcInjectionSchemeImpl(cern.lsa.domain.cern.timing.LhcInjectionScheme, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.LhcInjectionSchemeImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.LhcInjectionScheme,
            java.io.Serializable
    
      Constructors:
        * LhcInjectionSchemeImpl(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    def addInjection(self, lhcInjection: cern.lsa.domain.cern.timing.LhcInjection) -> None: ...
    def getCreationDate(self) -> java.util.Date: ...
    def getDescription(self) -> str: ...
    def getInjectionSchemeGroup(self) -> str: ...
    def getInjectionSchemeName(self) -> str: ...
    def getInjections(self) -> java.util.Set[cern.lsa.domain.cern.timing.LhcInjection]: ...
    def getMinBunchSpacing(self) -> int: ...
    def getNbCollisionIP1(self) -> int: ...
    def getNbCollisionIP2(self) -> int: ...
    def getNbCollisionIP5(self) -> int: ...
    def getNbCollisionIP8(self) -> int: ...
    def getNumberOfBunchesB1(self) -> int: ...
    def getNumberOfBunchesB2(self) -> int: ...
    def getPilotPositionB1(self) -> int: ...
    def getPilotPositionB2(self) -> int: ...
    def getPredictedBunchConfiguration(self, rNGI: cern.lsa.domain.cern.timing.enums.RNGI) -> typing.List[int]: ...
    def isInjectionCleaningEnabled(self) -> bool: ...
    def isWithOverInjection(self) -> bool: ...
    def removeInjection(self, lhcInjection: cern.lsa.domain.cern.timing.LhcInjection) -> None: ...
    def setBunchIntForAllRequests(self, int: int) -> None: ...
    def setCreationDate(self, date: java.util.Date) -> None: ...
    def setDescription(self, string: str) -> None: ...
    def setInjectionSchemeGroup(self, string: str) -> None: ...
    def setInjectionSchemeName(self, string: str) -> None: ...
    def setIsInjectionCleaningEnabled(self, boolean: bool) -> None: ...
    def setIsWithOverInjection(self, boolean: bool) -> None: ...
    def setNbCollisionIP1(self, int: int) -> None: ...
    def setNbCollisionIP2(self, int: int) -> None: ...
    def setNbCollisionIP5(self, int: int) -> None: ...
    def setNbCollisionIP8(self, int: int) -> None: ...
    def setPilotPositionB1(self, int: int) -> None: ...
    def setPilotPositionB2(self, int: int) -> None: ...
    def toString(self) -> str: ...

class LoadedEventTableImpl(cern.lsa.domain.cern.timing.LoadedEventTable, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.LoadedEventTableImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.LoadedEventTable,
            java.io.Serializable
    
      Constructors:
        * LoadedEventTableImpl(cern.lsa.domain.cern.timing.EventTableStatus, cern.lsa.domain.cern.timing.EventTable)
    
    """
    def __init__(self, eventTableStatus: cern.lsa.domain.cern.timing.EventTableStatus, eventTable2: cern.lsa.domain.cern.timing.EventTable): ...
    def getEventTable(self) -> cern.lsa.domain.cern.timing.EventTable: ...
    def getTableStatus(self) -> cern.lsa.domain.cern.timing.EventTableStatus: ...
    def toString(self) -> str: ...

class TimingEventImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.timing.TimingEvent], cern.lsa.domain.cern.timing.TimingEvent):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.TimingEventImpl'
    
        Extends:
            cern.accsoft.commons.util.AbstractNamedSerializable
    
        Interfaces:
            cern.lsa.domain.cern.timing.TimingEvent
    
      Constructors:
        * TimingEventImpl(java.lang.String, java.lang.String, java.lang.String)
    
    """
    def __init__(self, string: str, string2: str, string3: str): ...
    def getHardwareEventName(self) -> str: ...
    def getPayloadAttributeName(self) -> str: ...

class TimingEventSchedulingImpl(cern.lsa.domain.cern.timing.TimingEventScheduling, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.TimingEventSchedulingImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.TimingEventScheduling,
            java.io.Serializable
    
      Constructors:
        * TimingEventSchedulingImpl(cern.lsa.domain.cern.timing.TimingEvent, int)
    
    """
    def __init__(self, timingEvent: cern.lsa.domain.cern.timing.TimingEvent, int: int): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getOffsetInMillis(self) -> int: ...
    def getTimingEvent(self) -> cern.lsa.domain.cern.timing.TimingEvent: ...
    def hashCode(self) -> int: ...

class TimingProcessImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.timing.TimingProcess], cern.lsa.domain.cern.timing.TimingProcess):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.TimingProcessImpl'
    
        Extends:
            cern.accsoft.commons.util.AbstractNamedSerializable
    
        Interfaces:
            cern.lsa.domain.cern.timing.TimingProcess
    
      Constructors:
        * TimingProcessImpl(java.lang.String, cern.accsoft.commons.domain.TimingDomain)
    
    """
    def __init__(self, string: str, timingDomain: cern.accsoft.commons.domain.TimingDomain): ...
    def addTimingEventScheduling(self, timingEventScheduling: cern.lsa.domain.cern.timing.TimingEventScheduling) -> None: ...
    def getName(self) -> str: ...
    def getScheduledTimingEvents(self) -> java.util.Set[cern.lsa.domain.cern.timing.TimingEventScheduling]: ...
    def getTimingDomain(self) -> cern.accsoft.commons.domain.TimingDomain: ...

class TimingProcessSchedulingImpl(cern.lsa.domain.cern.timing.TimingProcessScheduling, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.TimingProcessSchedulingImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.TimingProcessScheduling,
            java.io.Serializable
    
      Constructors:
        * TimingProcessSchedulingImpl(cern.lsa.domain.cern.timing.TimingProcess, int, cern.lsa.domain.cern.timing.TimingProcessAnchor)
    
    """
    def __init__(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess, int: int, timingProcessAnchor: cern.lsa.domain.cern.timing.TimingProcessAnchor): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getOffsetInMillis(self) -> int: ...
    def getTimingProcess(self) -> cern.lsa.domain.cern.timing.TimingProcess: ...
    def getTimingProcessAnchor(self) -> cern.lsa.domain.cern.timing.TimingProcessAnchor: ...
    def getTimingProcessAnchorName(self) -> str: ...
    def getTimingProcessName(self) -> str: ...
    def hashCode(self) -> int: ...
    def setOffsetInMillis(self, int: int) -> None: ...
    def setTimingProcess(self, timingProcess: cern.lsa.domain.cern.timing.TimingProcess) -> None: ...
    def setTimingProcessAnchor(self, timingProcessAnchor: cern.lsa.domain.cern.timing.TimingProcessAnchor) -> None: ...
    def setTimingProcessAnchorName(self, string: str) -> None: ...
    def setTimingProcessName(self, string: str) -> None: ...
    def toString(self) -> str: ...

class XtimInfoImpl(cern.lsa.domain.cern.timing.XtimInfo, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.timing.spi.XtimInfoImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.timing.XtimInfo, java.io.Serializable
    
      Constructors:
        * XtimInfoImpl(java.lang.String, java.lang.String)
    
    """
    def __init__(self, string: str, string2: str): ...
    def getAcqStamp(self) -> int: ...
    def getEvenTypeName(self) -> str: ...
    def getMilliseconde(self) -> int: ...
    def getOccurence(self) -> int: ...
    def getPayload(self) -> int: ...
    def getUtcNanoseconde(self) -> int: ...
    def getUtcSeconde(self) -> int: ...
    def getXtimName(self) -> str: ...
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
