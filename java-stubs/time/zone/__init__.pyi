from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.io
import java.lang
import java.time
import java.util


class Ser(java.io.Externalizable):
    def __init__(self): ...
    def readExternal(self, objectInput: java.io.ObjectInput) -> None: ...
    def writeExternal(self, objectOutput: java.io.ObjectOutput) -> None: ...

class ZoneOffsetTransition(java.lang.Comparable['ZoneOffsetTransition'], java.io.Serializable):
    @overload
    def compareTo(self, object: _py_Any) -> int: ...
    @overload
    def compareTo(self, zoneOffsetTransition: 'ZoneOffsetTransition') -> int: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getDateTimeAfter(self) -> java.time.LocalDateTime: ...
    def getDateTimeBefore(self) -> java.time.LocalDateTime: ...
    def getDuration(self) -> java.time.Duration: ...
    def getInstant(self) -> java.time.Instant: ...
    def getOffsetAfter(self) -> java.time.ZoneOffset: ...
    def getOffsetBefore(self) -> java.time.ZoneOffset: ...
    def hashCode(self) -> int: ...
    def isGap(self) -> bool: ...
    def isOverlap(self) -> bool: ...
    def isValidOffset(self, zoneOffset: java.time.ZoneOffset) -> bool: ...
    @classmethod
    def of(cls, localDateTime: java.time.LocalDateTime, zoneOffset: java.time.ZoneOffset, zoneOffset2: java.time.ZoneOffset) -> 'ZoneOffsetTransition': ...
    def toEpochSecond(self) -> int: ...
    def toString(self) -> str: ...

class ZoneOffsetTransitionRule(java.io.Serializable):
    def createTransition(self, int: int) -> ZoneOffsetTransition: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getDayOfMonthIndicator(self) -> int: ...
    def getDayOfWeek(self) -> java.time.DayOfWeek: ...
    def getLocalTime(self) -> java.time.LocalTime: ...
    def getMonth(self) -> java.time.Month: ...
    def getOffsetAfter(self) -> java.time.ZoneOffset: ...
    def getOffsetBefore(self) -> java.time.ZoneOffset: ...
    def getStandardOffset(self) -> java.time.ZoneOffset: ...
    def getTimeDefinition(self) -> 'ZoneOffsetTransitionRule.TimeDefinition': ...
    def hashCode(self) -> int: ...
    def isMidnightEndOfDay(self) -> bool: ...
    @classmethod
    def of(cls, month: java.time.Month, int: int, dayOfWeek: java.time.DayOfWeek, localTime: java.time.LocalTime, boolean: bool, timeDefinition: 'ZoneOffsetTransitionRule.TimeDefinition', zoneOffset: java.time.ZoneOffset, zoneOffset2: java.time.ZoneOffset, zoneOffset3: java.time.ZoneOffset) -> 'ZoneOffsetTransitionRule': ...
    def toString(self) -> str: ...
    class TimeDefinition(java.lang.Enum['ZoneOffsetTransitionRule.TimeDefinition']):
        UTC: _py_ClassVar['ZoneOffsetTransitionRule.TimeDefinition'] = ...
        WALL: _py_ClassVar['ZoneOffsetTransitionRule.TimeDefinition'] = ...
        STANDARD: _py_ClassVar['ZoneOffsetTransitionRule.TimeDefinition'] = ...
        def createDateTime(self, localDateTime: java.time.LocalDateTime, zoneOffset: java.time.ZoneOffset, zoneOffset2: java.time.ZoneOffset) -> java.time.LocalDateTime: ...
        _valueOf_0__T = _py_TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @overload
        def valueOf(cls, class_: _py_Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @classmethod
        @overload
        def valueOf(cls, string: str) -> 'ZoneOffsetTransitionRule.TimeDefinition': ...
        @classmethod
        def values(cls) -> _py_List['ZoneOffsetTransitionRule.TimeDefinition']: ...

class ZoneRules(java.io.Serializable):
    def equals(self, object: _py_Any) -> bool: ...
    def getDaylightSavings(self, instant: java.time.Instant) -> java.time.Duration: ...
    @overload
    def getOffset(self, instant: java.time.Instant) -> java.time.ZoneOffset: ...
    @overload
    def getOffset(self, localDateTime: java.time.LocalDateTime) -> java.time.ZoneOffset: ...
    def getStandardOffset(self, instant: java.time.Instant) -> java.time.ZoneOffset: ...
    def getTransition(self, localDateTime: java.time.LocalDateTime) -> ZoneOffsetTransition: ...
    def getTransitionRules(self) -> java.util.List[ZoneOffsetTransitionRule]: ...
    def getTransitions(self) -> java.util.List[ZoneOffsetTransition]: ...
    def getValidOffsets(self, localDateTime: java.time.LocalDateTime) -> java.util.List[java.time.ZoneOffset]: ...
    def hashCode(self) -> int: ...
    def isDaylightSavings(self, instant: java.time.Instant) -> bool: ...
    def isFixedOffset(self) -> bool: ...
    def isValidOffset(self, localDateTime: java.time.LocalDateTime, zoneOffset: java.time.ZoneOffset) -> bool: ...
    def nextTransition(self, instant: java.time.Instant) -> ZoneOffsetTransition: ...
    @classmethod
    @overload
    def of(cls, zoneOffset: java.time.ZoneOffset) -> 'ZoneRules': ...
    @classmethod
    @overload
    def of(cls, zoneOffset: java.time.ZoneOffset, zoneOffset2: java.time.ZoneOffset, list: java.util.List[ZoneOffsetTransition], list2: java.util.List[ZoneOffsetTransition], list3: java.util.List[ZoneOffsetTransitionRule]) -> 'ZoneRules': ...
    def previousTransition(self, instant: java.time.Instant) -> ZoneOffsetTransition: ...
    def toString(self) -> str: ...

class ZoneRulesException(java.time.DateTimeException):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...

class ZoneRulesProvider:
    @classmethod
    def getAvailableZoneIds(cls) -> java.util.Set[str]: ...
    @classmethod
    def getRules(cls, string: str, boolean: bool) -> ZoneRules: ...
    @classmethod
    def getVersions(cls, string: str) -> java.util.NavigableMap[str, ZoneRules]: ...
    @classmethod
    def refresh(cls) -> bool: ...
    @classmethod
    def registerProvider(cls, zoneRulesProvider: 'ZoneRulesProvider') -> None: ...

class TzdbZoneRulesProvider(ZoneRulesProvider):
    def __init__(self): ...
    def toString(self) -> str: ...
