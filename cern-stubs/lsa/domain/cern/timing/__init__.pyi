import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import cern.lsa.domain.cern.timing.enums
import java.lang
import java.util
import typing


class ActiveTimingUsers:
    def contains(self, string: str) -> bool: ...
    def getNormalUsers(self) -> java.util.List[str]: ...
    def getSpareUsers(self) -> java.util.List[str]: ...

class BunchPattern:
    def addBunchPosition(self, int: int) -> None: ...
    def getBatchSpacing(self) -> int: ...
    def getBunchPatternDescription(self) -> str: ...
    def getBunchPatternName(self) -> str: ...
    def getBunchSpacing(self) -> int: ...
    def getBunchesPosition(self) -> typing.List[int]: ...
    def getNbrOfBunches(self) -> int: ...
    def getNbrOfBunchesPerPSBatch(self) -> int: ...
    def getNbrOfPSBatches(self) -> int: ...
    def isDoubletsBeam(self) -> bool: ...
    def setBunchPositions(self, intArray: typing.List[int]) -> None: ...
    def setBunchSpacing(self, int: int) -> None: ...
    def setDoubletsBeam(self, boolean: bool) -> None: ...
    def setNbrOfBunches(self, int: int) -> None: ...
    def setNbrOfBunchesPerPSBatch(self, int: int) -> None: ...
    def setNbrOfPSBatches(self, int: int) -> None: ...

class Event(java.lang.Comparable['Event'], cern.accsoft.commons.util.Named):
    def getDescription(self) -> str: ...
    def getName(self) -> str: ...
    def getPayload(self) -> int: ...
    def getType(self) -> 'EventType': ...

class EventTable:
    INFINITE_RUN: typing.ClassVar[int] = ...
    def addEvent(self, event: Event, int: int) -> bool: ...
    def addEvents(self, sortedSet: java.util.SortedSet['EventTableEntry']) -> None: ...
    def getEventList(self) -> java.util.SortedSet['EventTableEntry']: ...
    def getName(self) -> str: ...
    def getRunCount(self) -> int: ...
    def getStartingEvent(self) -> Event: ...
    def removeEvent(self, event: Event, int: int) -> None: ...
    def removeEvents(self) -> None: ...
    def setName(self, string: str) -> None: ...
    def setRunCount(self, int: int) -> None: ...
    def setStartingEvent(self, event: Event) -> None: ...

class EventTableEntry(java.lang.Comparable['EventTableEntry']):
    def getEvent(self) -> Event: ...
    def getOffset(self) -> int: ...

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
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class InvalidEventTableEntryException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class InvalidEventTableException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class LhcCirculatingBunchConfiguration:
    def getBeamNbr(self) -> int: ...
    def getFilledBuckets(self) -> java.util.SortedSet[int]: ...
    def getFirstFilledBucket(self) -> int: ...

class LhcInjection(cern.accsoft.commons.util.Named):
    def getBunchConfiguration(self) -> 'LhcInjectionBunchConfiguration': ...
    def getNextInjectionBeamType(self) -> cern.lsa.domain.cern.timing.enums.BEAM_TYPE: ...
    def getNextInjectionBunchIntensity(self) -> int: ...
    def getNextInjectionBunchNumber(self) -> int: ...
    def getNextInjectionBunchSpacing(self) -> int: ...
    def getNextInjectionNbrOfBunchesPerPSBatch(self) -> int: ...
    def getNextInjectionPSbatchNbr(self) -> int: ...
    def getNextInjectionParticleType(self) -> int: ...
    def getNextInjectionRFBucket(self) -> int: ...
    def getNextInjectionRing(self) -> cern.lsa.domain.cern.timing.enums.RNGI: ...
    def setBunchConfiguration(self, lhcInjectionBunchConfiguration: 'LhcInjectionBunchConfiguration') -> None: ...
    def setName(self, string: str) -> None: ...
    def setNextInjectionBeamType(self, bEAM_TYPE: cern.lsa.domain.cern.timing.enums.BEAM_TYPE) -> None: ...
    def setNextInjectionBunchIntensity(self, int: int) -> None: ...
    def setNextInjectionParticleType(self, int: int) -> None: ...
    @typing.overload
    def setNextInjectionRing(self, rNGI: cern.lsa.domain.cern.timing.enums.RNGI) -> None: ...
    @typing.overload
    def setNextInjectionRing(self, int: int) -> None: ...

class LhcInjectionBunchConfiguration(cern.accsoft.commons.util.Named):
    def getBunchPattern(self) -> BunchPattern: ...
    def getFilledBuckets(self) -> typing.List[int]: ...
    def getFirstFilledBucket(self) -> int: ...
    def setBunchPattern(self, bunchPattern: BunchPattern) -> None: ...
    def setFirstFilledBucket(self, int: int) -> None: ...
    def setName(self, string: str) -> None: ...

class LhcInjectionScheme:
    def addInjection(self, lhcInjection: LhcInjection) -> None: ...
    def getCreationDate(self) -> java.util.Date: ...
    def getDescription(self) -> str: ...
    def getInjectionSchemeGroup(self) -> str: ...
    def getInjectionSchemeName(self) -> str: ...
    def getInjections(self) -> java.util.Set[LhcInjection]: ...
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
    def removeInjection(self, lhcInjection: LhcInjection) -> None: ...
    def setBunchIntForAllRequests(self, int: int) -> None: ...
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

class LhcInjectionSchemeEntry_Obs(java.lang.Comparable['LhcInjectionSchemeEntry_Obs']):
    def getDelay(self) -> int: ...
    def getInjection(self) -> LhcInjection: ...
    def getInjectionOrder(self) -> int: ...
    def setDelay(self, int: int) -> None: ...
    def setInjectionOrder(self, int: int) -> None: ...

class LoadedEventTable:
    def getEventTable(self) -> EventTable: ...
    def getTableStatus(self) -> EventTableStatus: ...

class LowLevelTimingException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class NoSuchEventTableException(java.lang.Exception):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class NoSuchEventTypeException(java.lang.Exception):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class TimingEvent(cern.accsoft.commons.util.Named):
    def getHardwareEventName(self) -> str: ...
    def getName(self) -> str: ...
    def getPayloadAttributeName(self) -> str: ...

class TimingEventScheduling:
    def getOffsetInMillis(self) -> int: ...
    def getTimingEvent(self) -> TimingEvent: ...

class TimingProcess(cern.accsoft.commons.util.Named):
    def getScheduledTimingEvents(self) -> java.util.Set[TimingEventScheduling]: ...
    def getTimingDomain(self) -> cern.accsoft.commons.domain.TimingDomain: ...

class TimingProcessAnchor(java.lang.Enum['TimingProcessAnchor']):
    SEGMENT_START: typing.ClassVar['TimingProcessAnchor'] = ...
    SEGMENT_END: typing.ClassVar['TimingProcessAnchor'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TimingProcessAnchor': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['TimingProcessAnchor']: ...

class TimingProcessScheduling:
    def getOffsetInMillis(self) -> int: ...
    def getTimingProcess(self) -> TimingProcess: ...
    def getTimingProcessAnchor(self) -> TimingProcessAnchor: ...
    def setOffsetInMillis(self, int: int) -> None: ...
    def setTimingProcessAnchor(self, timingProcessAnchor: TimingProcessAnchor) -> None: ...

class XtimInfo:
    def getAcqStamp(self) -> int: ...
    def getEvenTypeName(self) -> str: ...
    def getMilliseconde(self) -> int: ...
    def getOccurence(self) -> int: ...
    def getPayload(self) -> int: ...
    def getUtcNanoseconde(self) -> int: ...
    def getUtcSeconde(self) -> int: ...
    def getXtimName(self) -> str: ...
