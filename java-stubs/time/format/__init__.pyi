from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.lang
import java.text
import java.time
import java.time.chrono
import java.time.temporal
import java.util


class DateTimeFormatter:
    ISO_LOCAL_DATE: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_OFFSET_DATE: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_DATE: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_LOCAL_TIME: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_OFFSET_TIME: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_TIME: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_LOCAL_DATE_TIME: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_OFFSET_DATE_TIME: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_ZONED_DATE_TIME: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_DATE_TIME: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_ORDINAL_DATE: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_WEEK_DATE: _py_ClassVar['DateTimeFormatter'] = ...
    ISO_INSTANT: _py_ClassVar['DateTimeFormatter'] = ...
    BASIC_ISO_DATE: _py_ClassVar['DateTimeFormatter'] = ...
    RFC_1123_DATE_TIME: _py_ClassVar['DateTimeFormatter'] = ...
    def format(self, temporalAccessor: java.time.temporal.TemporalAccessor) -> str: ...
    def formatTo(self, temporalAccessor: java.time.temporal.TemporalAccessor, appendable: java.lang.Appendable) -> None: ...
    def getChronology(self) -> java.time.chrono.Chronology: ...
    def getDecimalStyle(self) -> 'DecimalStyle': ...
    def getLocale(self) -> java.util.Locale: ...
    def getResolverFields(self) -> java.util.Set[java.time.temporal.TemporalField]: ...
    def getResolverStyle(self) -> 'ResolverStyle': ...
    def getZone(self) -> java.time.ZoneId: ...
    @classmethod
    def ofLocalizedDate(cls, formatStyle: 'FormatStyle') -> 'DateTimeFormatter': ...
    @classmethod
    @overload
    def ofLocalizedDateTime(cls, formatStyle: 'FormatStyle') -> 'DateTimeFormatter': ...
    @classmethod
    @overload
    def ofLocalizedDateTime(cls, formatStyle: 'FormatStyle', formatStyle2: 'FormatStyle') -> 'DateTimeFormatter': ...
    @classmethod
    def ofLocalizedTime(cls, formatStyle: 'FormatStyle') -> 'DateTimeFormatter': ...
    @classmethod
    @overload
    def ofPattern(cls, string: str) -> 'DateTimeFormatter': ...
    @classmethod
    @overload
    def ofPattern(cls, string: str, locale: java.util.Locale) -> 'DateTimeFormatter': ...
    _parse_0__T = _py_TypeVar('_parse_0__T')  # <T>
    @overload
    def parse(self, charSequence: java.lang.CharSequence, temporalQuery: java.time.temporal.TemporalQuery[_parse_0__T]) -> _parse_0__T: ...
    @overload
    def parse(self, charSequence: java.lang.CharSequence) -> java.time.temporal.TemporalAccessor: ...
    @overload
    def parse(self, charSequence: java.lang.CharSequence, parsePosition: java.text.ParsePosition) -> java.time.temporal.TemporalAccessor: ...
    def parseBest(self, charSequence: java.lang.CharSequence, temporalQueryArray: _py_List[java.time.temporal.TemporalQuery[_py_Any]]) -> java.time.temporal.TemporalAccessor: ...
    def parseUnresolved(self, charSequence: java.lang.CharSequence, parsePosition: java.text.ParsePosition) -> java.time.temporal.TemporalAccessor: ...
    @classmethod
    def parsedExcessDays(cls) -> java.time.temporal.TemporalQuery[java.time.Period]: ...
    @classmethod
    def parsedLeapSecond(cls) -> java.time.temporal.TemporalQuery[bool]: ...
    @overload
    def toFormat(self) -> java.text.Format: ...
    @overload
    def toFormat(self, temporalQuery: java.time.temporal.TemporalQuery[_py_Any]) -> java.text.Format: ...
    def toString(self) -> str: ...
    def withChronology(self, chronology: java.time.chrono.Chronology) -> 'DateTimeFormatter': ...
    def withDecimalStyle(self, decimalStyle: 'DecimalStyle') -> 'DateTimeFormatter': ...
    def withLocale(self, locale: java.util.Locale) -> 'DateTimeFormatter': ...
    @overload
    def withResolverFields(self, temporalFieldArray: _py_List[java.time.temporal.TemporalField]) -> 'DateTimeFormatter': ...
    @overload
    def withResolverFields(self, set: java.util.Set[java.time.temporal.TemporalField]) -> 'DateTimeFormatter': ...
    def withResolverStyle(self, resolverStyle: 'ResolverStyle') -> 'DateTimeFormatter': ...
    def withZone(self, zoneId: java.time.ZoneId) -> 'DateTimeFormatter': ...

class DateTimeFormatterBuilder:
    def __init__(self): ...
    def append(self, dateTimeFormatter: DateTimeFormatter) -> 'DateTimeFormatterBuilder': ...
    def appendChronologyId(self) -> 'DateTimeFormatterBuilder': ...
    def appendChronologyText(self, textStyle: 'TextStyle') -> 'DateTimeFormatterBuilder': ...
    def appendFraction(self, temporalField: java.time.temporal.TemporalField, int: int, int2: int, boolean: bool) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendInstant(self) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendInstant(self, int: int) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendLiteral(self, char: str) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendLiteral(self, string: str) -> 'DateTimeFormatterBuilder': ...
    def appendLocalized(self, formatStyle: 'FormatStyle', formatStyle2: 'FormatStyle') -> 'DateTimeFormatterBuilder': ...
    def appendLocalizedOffset(self, textStyle: 'TextStyle') -> 'DateTimeFormatterBuilder': ...
    def appendOffset(self, string: str, string2: str) -> 'DateTimeFormatterBuilder': ...
    def appendOffsetId(self) -> 'DateTimeFormatterBuilder': ...
    def appendOptional(self, dateTimeFormatter: DateTimeFormatter) -> 'DateTimeFormatterBuilder': ...
    def appendPattern(self, string: str) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendText(self, temporalField: java.time.temporal.TemporalField) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendText(self, temporalField: java.time.temporal.TemporalField, textStyle: 'TextStyle') -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendText(self, temporalField: java.time.temporal.TemporalField, map: java.util.Map[int, str]) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendValue(self, temporalField: java.time.temporal.TemporalField) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendValue(self, temporalField: java.time.temporal.TemporalField, int: int) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendValue(self, temporalField: java.time.temporal.TemporalField, int: int, int2: int, signStyle: 'SignStyle') -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendValueReduced(self, temporalField: java.time.temporal.TemporalField, int: int, int2: int, int3: int) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendValueReduced(self, temporalField: java.time.temporal.TemporalField, int: int, int2: int, chronoLocalDate: java.time.chrono.ChronoLocalDate) -> 'DateTimeFormatterBuilder': ...
    def appendZoneId(self) -> 'DateTimeFormatterBuilder': ...
    def appendZoneOrOffsetId(self) -> 'DateTimeFormatterBuilder': ...
    def appendZoneRegionId(self) -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendZoneText(self, textStyle: 'TextStyle') -> 'DateTimeFormatterBuilder': ...
    @overload
    def appendZoneText(self, textStyle: 'TextStyle', set: java.util.Set[java.time.ZoneId]) -> 'DateTimeFormatterBuilder': ...
    @classmethod
    def getLocalizedDateTimePattern(cls, formatStyle: 'FormatStyle', formatStyle2: 'FormatStyle', chronology: java.time.chrono.Chronology, locale: java.util.Locale) -> str: ...
    def optionalEnd(self) -> 'DateTimeFormatterBuilder': ...
    def optionalStart(self) -> 'DateTimeFormatterBuilder': ...
    @overload
    def padNext(self, int: int) -> 'DateTimeFormatterBuilder': ...
    @overload
    def padNext(self, int: int, char: str) -> 'DateTimeFormatterBuilder': ...
    def parseCaseInsensitive(self) -> 'DateTimeFormatterBuilder': ...
    def parseCaseSensitive(self) -> 'DateTimeFormatterBuilder': ...
    def parseDefaulting(self, temporalField: java.time.temporal.TemporalField, long: int) -> 'DateTimeFormatterBuilder': ...
    def parseLenient(self) -> 'DateTimeFormatterBuilder': ...
    def parseStrict(self) -> 'DateTimeFormatterBuilder': ...
    @overload
    def toFormatter(self) -> DateTimeFormatter: ...
    @overload
    def toFormatter(self, locale: java.util.Locale) -> DateTimeFormatter: ...

class DateTimeParseContext:
    def toString(self) -> str: ...

class DateTimeParseException(java.time.DateTimeException):
    @overload
    def __init__(self, string: str, charSequence: java.lang.CharSequence, int: int): ...
    @overload
    def __init__(self, string: str, charSequence: java.lang.CharSequence, int: int, throwable: java.lang.Throwable): ...
    def getErrorIndex(self) -> int: ...
    def getParsedString(self) -> str: ...

class DateTimePrintContext:
    def toString(self) -> str: ...

class DateTimeTextProvider:
    @overload
    def getText(self, chronology: java.time.chrono.Chronology, temporalField: java.time.temporal.TemporalField, long: int, textStyle: 'TextStyle', locale: java.util.Locale) -> str: ...
    @overload
    def getText(self, temporalField: java.time.temporal.TemporalField, long: int, textStyle: 'TextStyle', locale: java.util.Locale) -> str: ...
    @overload
    def getTextIterator(self, chronology: java.time.chrono.Chronology, temporalField: java.time.temporal.TemporalField, textStyle: 'TextStyle', locale: java.util.Locale) -> java.util.Iterator[java.util.Map.Entry[str, int]]: ...
    @overload
    def getTextIterator(self, temporalField: java.time.temporal.TemporalField, textStyle: 'TextStyle', locale: java.util.Locale) -> java.util.Iterator[java.util.Map.Entry[str, int]]: ...

class DecimalStyle:
    STANDARD: _py_ClassVar['DecimalStyle'] = ...
    def equals(self, object: _py_Any) -> bool: ...
    @classmethod
    def getAvailableLocales(cls) -> java.util.Set[java.util.Locale]: ...
    def getDecimalSeparator(self) -> str: ...
    def getNegativeSign(self) -> str: ...
    def getPositiveSign(self) -> str: ...
    def getZeroDigit(self) -> str: ...
    def hashCode(self) -> int: ...
    @classmethod
    def of(cls, locale: java.util.Locale) -> 'DecimalStyle': ...
    @classmethod
    def ofDefaultLocale(cls) -> 'DecimalStyle': ...
    def toString(self) -> str: ...
    def withDecimalSeparator(self, char: str) -> 'DecimalStyle': ...
    def withNegativeSign(self, char: str) -> 'DecimalStyle': ...
    def withPositiveSign(self, char: str) -> 'DecimalStyle': ...
    def withZeroDigit(self, char: str) -> 'DecimalStyle': ...

class FormatStyle(java.lang.Enum['FormatStyle']):
    FULL: _py_ClassVar['FormatStyle'] = ...
    LONG: _py_ClassVar['FormatStyle'] = ...
    MEDIUM: _py_ClassVar['FormatStyle'] = ...
    SHORT: _py_ClassVar['FormatStyle'] = ...
    _valueOf_0__T = _py_TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'FormatStyle': ...
    @classmethod
    def values(cls) -> _py_List['FormatStyle']: ...

class Parsed(java.time.temporal.TemporalAccessor):
    def getLong(self, temporalField: java.time.temporal.TemporalField) -> int: ...
    def isSupported(self, temporalField: java.time.temporal.TemporalField) -> bool: ...
    _query__R = _py_TypeVar('_query__R')  # <R>
    def query(self, temporalQuery: java.time.temporal.TemporalQuery[_query__R]) -> _query__R: ...
    def toString(self) -> str: ...

class ResolverStyle(java.lang.Enum['ResolverStyle']):
    STRICT: _py_ClassVar['ResolverStyle'] = ...
    SMART: _py_ClassVar['ResolverStyle'] = ...
    LENIENT: _py_ClassVar['ResolverStyle'] = ...
    _valueOf_0__T = _py_TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'ResolverStyle': ...
    @classmethod
    def values(cls) -> _py_List['ResolverStyle']: ...

class SignStyle(java.lang.Enum['SignStyle']):
    NORMAL: _py_ClassVar['SignStyle'] = ...
    ALWAYS: _py_ClassVar['SignStyle'] = ...
    NEVER: _py_ClassVar['SignStyle'] = ...
    NOT_NEGATIVE: _py_ClassVar['SignStyle'] = ...
    EXCEEDS_PAD: _py_ClassVar['SignStyle'] = ...
    _valueOf_0__T = _py_TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'SignStyle': ...
    @classmethod
    def values(cls) -> _py_List['SignStyle']: ...

class TextStyle(java.lang.Enum['TextStyle']):
    FULL: _py_ClassVar['TextStyle'] = ...
    FULL_STANDALONE: _py_ClassVar['TextStyle'] = ...
    SHORT: _py_ClassVar['TextStyle'] = ...
    SHORT_STANDALONE: _py_ClassVar['TextStyle'] = ...
    NARROW: _py_ClassVar['TextStyle'] = ...
    NARROW_STANDALONE: _py_ClassVar['TextStyle'] = ...
    def asNormal(self) -> 'TextStyle': ...
    def asStandalone(self) -> 'TextStyle': ...
    def isStandalone(self) -> bool: ...
    _valueOf_0__T = _py_TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'TextStyle': ...
    @classmethod
    def values(cls) -> _py_List['TextStyle']: ...

class ZoneName:
    @classmethod
    @overload
    def toZid(cls, string: str) -> str: ...
    @classmethod
    @overload
    def toZid(cls, string: str, locale: java.util.Locale) -> str: ...