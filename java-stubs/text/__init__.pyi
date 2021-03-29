import java.io
import java.lang
import java.math
import java.util
import typing


class Annotation:
    def __init__(self, object: typing.Any): ...
    def getValue(self) -> typing.Any: ...
    def toString(self) -> str: ...

class AttributedString:
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, map: typing.Union[java.util.Map['AttributedCharacterIterator.Attribute', typing.Any], typing.Mapping['AttributedCharacterIterator.Attribute', typing.Any]]): ...
    @typing.overload
    def __init__(self, attributedCharacterIterator: 'AttributedCharacterIterator'): ...
    @typing.overload
    def __init__(self, attributedCharacterIterator: 'AttributedCharacterIterator', int: int, int2: int): ...
    @typing.overload
    def __init__(self, attributedCharacterIterator: 'AttributedCharacterIterator', int: int, int2: int, attributeArray: typing.List['AttributedCharacterIterator.Attribute']): ...
    @typing.overload
    def addAttribute(self, attribute: 'AttributedCharacterIterator.Attribute', object: typing.Any) -> None: ...
    @typing.overload
    def addAttribute(self, attribute: 'AttributedCharacterIterator.Attribute', object: typing.Any, int: int, int2: int) -> None: ...
    def addAttributes(self, map: typing.Union[java.util.Map['AttributedCharacterIterator.Attribute', typing.Any], typing.Mapping['AttributedCharacterIterator.Attribute', typing.Any]], int: int, int2: int) -> None: ...
    @typing.overload
    def getIterator(self) -> 'AttributedCharacterIterator': ...
    @typing.overload
    def getIterator(self, attributeArray: typing.List['AttributedCharacterIterator.Attribute']) -> 'AttributedCharacterIterator': ...
    @typing.overload
    def getIterator(self, attributeArray: typing.List['AttributedCharacterIterator.Attribute'], int: int, int2: int) -> 'AttributedCharacterIterator': ...

class Bidi:
    DIRECTION_LEFT_TO_RIGHT: typing.ClassVar[int] = ...
    DIRECTION_RIGHT_TO_LEFT: typing.ClassVar[int] = ...
    DIRECTION_DEFAULT_LEFT_TO_RIGHT: typing.ClassVar[int] = ...
    DIRECTION_DEFAULT_RIGHT_TO_LEFT: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, charArray: typing.List[str], int: int, byteArray: typing.List[int], int2: int, int3: int, int4: int): ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    @typing.overload
    def __init__(self, attributedCharacterIterator: 'AttributedCharacterIterator'): ...
    def baseIsLeftToRight(self) -> bool: ...
    def createLineBidi(self, int: int, int2: int) -> 'Bidi': ...
    def getBaseLevel(self) -> int: ...
    def getLength(self) -> int: ...
    def getLevelAt(self, int: int) -> int: ...
    def getRunCount(self) -> int: ...
    def getRunLevel(self, int: int) -> int: ...
    def getRunLimit(self, int: int) -> int: ...
    def getRunStart(self, int: int) -> int: ...
    def isLeftToRight(self) -> bool: ...
    def isMixed(self) -> bool: ...
    def isRightToLeft(self) -> bool: ...
    @staticmethod
    def reorderVisually(byteArray: typing.List[int], int: int, objectArray: typing.List[typing.Any], int2: int, int3: int) -> None: ...
    @staticmethod
    def requiresBidi(charArray: typing.List[str], int: int, int2: int) -> bool: ...
    def toString(self) -> str: ...

class BreakIterator(java.lang.Cloneable):
    DONE: typing.ClassVar[int] = ...
    def clone(self) -> typing.Any: ...
    def current(self) -> int: ...
    def first(self) -> int: ...
    def following(self, int: int) -> int: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]: ...
    @typing.overload
    @staticmethod
    def getCharacterInstance() -> 'BreakIterator': ...
    @typing.overload
    @staticmethod
    def getCharacterInstance(locale: java.util.Locale) -> 'BreakIterator': ...
    @typing.overload
    @staticmethod
    def getLineInstance() -> 'BreakIterator': ...
    @typing.overload
    @staticmethod
    def getLineInstance(locale: java.util.Locale) -> 'BreakIterator': ...
    @typing.overload
    @staticmethod
    def getSentenceInstance() -> 'BreakIterator': ...
    @typing.overload
    @staticmethod
    def getSentenceInstance(locale: java.util.Locale) -> 'BreakIterator': ...
    def getText(self) -> 'CharacterIterator': ...
    @typing.overload
    @staticmethod
    def getWordInstance() -> 'BreakIterator': ...
    @typing.overload
    @staticmethod
    def getWordInstance(locale: java.util.Locale) -> 'BreakIterator': ...
    def isBoundary(self, int: int) -> bool: ...
    def last(self) -> int: ...
    @typing.overload
    def next(self) -> int: ...
    @typing.overload
    def next(self, int: int) -> int: ...
    def preceding(self, int: int) -> int: ...
    def previous(self) -> int: ...
    @typing.overload
    def setText(self, characterIterator: 'CharacterIterator') -> None: ...
    @typing.overload
    def setText(self, string: str) -> None: ...

class CharacterIterator(java.lang.Cloneable):
    DONE: typing.ClassVar[str] = ...
    def clone(self) -> typing.Any: ...
    def current(self) -> str: ...
    def first(self) -> str: ...
    def getBeginIndex(self) -> int: ...
    def getEndIndex(self) -> int: ...
    def getIndex(self) -> int: ...
    def last(self) -> str: ...
    def next(self) -> str: ...
    def previous(self) -> str: ...
    def setIndex(self, int: int) -> str: ...

class CollationElementIterator:
    NULLORDER: typing.ClassVar[int] = ...
    def getMaxExpansion(self, int: int) -> int: ...
    def getOffset(self) -> int: ...
    def next(self) -> int: ...
    def previous(self) -> int: ...
    @staticmethod
    def primaryOrder(int: int) -> int: ...
    def reset(self) -> None: ...
    @staticmethod
    def secondaryOrder(int: int) -> int: ...
    def setOffset(self, int: int) -> None: ...
    @typing.overload
    def setText(self, string: str) -> None: ...
    @typing.overload
    def setText(self, characterIterator: CharacterIterator) -> None: ...
    @staticmethod
    def tertiaryOrder(int: int) -> int: ...

class CollationKey(java.lang.Comparable['CollationKey']):
    def compareTo(self, collationKey: 'CollationKey') -> int: ...
    def getSourceString(self) -> str: ...
    def toByteArray(self) -> typing.List[int]: ...

class Collator(java.util.Comparator[typing.Any], java.lang.Cloneable):
    PRIMARY: typing.ClassVar[int] = ...
    SECONDARY: typing.ClassVar[int] = ...
    TERTIARY: typing.ClassVar[int] = ...
    IDENTICAL: typing.ClassVar[int] = ...
    NO_DECOMPOSITION: typing.ClassVar[int] = ...
    CANONICAL_DECOMPOSITION: typing.ClassVar[int] = ...
    FULL_DECOMPOSITION: typing.ClassVar[int] = ...
    def clone(self) -> typing.Any: ...
    @typing.overload
    def compare(self, string: str, string2: str) -> int: ...
    @typing.overload
    def compare(self, object: typing.Any, object2: typing.Any) -> int: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def equals(self, string: str, string2: str) -> bool: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]: ...
    def getCollationKey(self, string: str) -> CollationKey: ...
    def getDecomposition(self) -> int: ...
    @typing.overload
    @staticmethod
    def getInstance(locale: java.util.Locale) -> 'Collator': ...
    @typing.overload
    @staticmethod
    def getInstance() -> 'Collator': ...
    def getStrength(self) -> int: ...
    def hashCode(self) -> int: ...
    def setDecomposition(self, int: int) -> None: ...
    def setStrength(self, int: int) -> None: ...

class DateFormatSymbols(java.io.Serializable, java.lang.Cloneable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, locale: java.util.Locale): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAmPmStrings(self) -> typing.List[str]: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]: ...
    def getEras(self) -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def getInstance() -> 'DateFormatSymbols': ...
    @typing.overload
    @staticmethod
    def getInstance(locale: java.util.Locale) -> 'DateFormatSymbols': ...
    def getLocalPatternChars(self) -> str: ...
    def getMonths(self) -> typing.List[str]: ...
    def getShortMonths(self) -> typing.List[str]: ...
    def getShortWeekdays(self) -> typing.List[str]: ...
    def getWeekdays(self) -> typing.List[str]: ...
    def getZoneStrings(self) -> typing.List[typing.List[str]]: ...
    def hashCode(self) -> int: ...
    def setAmPmStrings(self, stringArray: typing.List[str]) -> None: ...
    def setEras(self, stringArray: typing.List[str]) -> None: ...
    def setLocalPatternChars(self, string: str) -> None: ...
    def setMonths(self, stringArray: typing.List[str]) -> None: ...
    def setShortMonths(self, stringArray: typing.List[str]) -> None: ...
    def setShortWeekdays(self, stringArray: typing.List[str]) -> None: ...
    def setWeekdays(self, stringArray: typing.List[str]) -> None: ...
    def setZoneStrings(self, stringArray: typing.List[typing.List[str]]) -> None: ...

class DecimalFormatSymbols(java.lang.Cloneable, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, locale: java.util.Locale): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]: ...
    def getCurrency(self) -> java.util.Currency: ...
    def getCurrencySymbol(self) -> str: ...
    def getDecimalSeparator(self) -> str: ...
    def getDigit(self) -> str: ...
    def getExponentSeparator(self) -> str: ...
    def getGroupingSeparator(self) -> str: ...
    def getInfinity(self) -> str: ...
    @typing.overload
    @staticmethod
    def getInstance() -> 'DecimalFormatSymbols': ...
    @typing.overload
    @staticmethod
    def getInstance(locale: java.util.Locale) -> 'DecimalFormatSymbols': ...
    def getInternationalCurrencySymbol(self) -> str: ...
    def getMinusSign(self) -> str: ...
    def getMonetaryDecimalSeparator(self) -> str: ...
    def getNaN(self) -> str: ...
    def getPatternSeparator(self) -> str: ...
    def getPerMill(self) -> str: ...
    def getPercent(self) -> str: ...
    def getZeroDigit(self) -> str: ...
    def hashCode(self) -> int: ...
    def setCurrency(self, currency: java.util.Currency) -> None: ...
    def setCurrencySymbol(self, string: str) -> None: ...
    def setDecimalSeparator(self, char: str) -> None: ...
    def setDigit(self, char: str) -> None: ...
    def setExponentSeparator(self, string: str) -> None: ...
    def setGroupingSeparator(self, char: str) -> None: ...
    def setInfinity(self, string: str) -> None: ...
    def setInternationalCurrencySymbol(self, string: str) -> None: ...
    def setMinusSign(self, char: str) -> None: ...
    def setMonetaryDecimalSeparator(self, char: str) -> None: ...
    def setNaN(self, string: str) -> None: ...
    def setPatternSeparator(self, char: str) -> None: ...
    def setPerMill(self, char: str) -> None: ...
    def setPercent(self, char: str) -> None: ...
    def setZeroDigit(self, char: str) -> None: ...

class FieldPosition:
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, field: 'Format.Field'): ...
    @typing.overload
    def __init__(self, field: 'Format.Field', int: int): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBeginIndex(self) -> int: ...
    def getEndIndex(self) -> int: ...
    def getField(self) -> int: ...
    def getFieldAttribute(self) -> 'Format.Field': ...
    def hashCode(self) -> int: ...
    def setBeginIndex(self, int: int) -> None: ...
    def setEndIndex(self, int: int) -> None: ...
    def toString(self) -> str: ...

class Normalizer:
    @staticmethod
    def isNormalized(charSequence: typing.Union[java.lang.CharSequence, str], form: 'Normalizer.Form') -> bool: ...
    @staticmethod
    def normalize(charSequence: typing.Union[java.lang.CharSequence, str], form: 'Normalizer.Form') -> str: ...
    class Form(java.lang.Enum['Normalizer.Form']):
        NFD: typing.ClassVar['Normalizer.Form'] = ...
        NFC: typing.ClassVar['Normalizer.Form'] = ...
        NFKD: typing.ClassVar['Normalizer.Form'] = ...
        NFKC: typing.ClassVar['Normalizer.Form'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'Normalizer.Form': ...
        @staticmethod
        def values() -> typing.List['Normalizer.Form']: ...

class ParseException(java.lang.Exception):
    def __init__(self, string: str, int: int): ...
    def getErrorOffset(self) -> int: ...

class ParsePosition:
    def __init__(self, int: int): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getErrorIndex(self) -> int: ...
    def getIndex(self) -> int: ...
    def hashCode(self) -> int: ...
    def setErrorIndex(self, int: int) -> None: ...
    def setIndex(self, int: int) -> None: ...
    def toString(self) -> str: ...

class AttributedCharacterIterator(CharacterIterator):
    def getAllAttributeKeys(self) -> java.util.Set['AttributedCharacterIterator.Attribute']: ...
    def getAttribute(self, attribute: 'AttributedCharacterIterator.Attribute') -> typing.Any: ...
    def getAttributes(self) -> java.util.Map['AttributedCharacterIterator.Attribute', typing.Any]: ...
    @typing.overload
    def getRunLimit(self) -> int: ...
    @typing.overload
    def getRunLimit(self, attribute: 'AttributedCharacterIterator.Attribute') -> int: ...
    @typing.overload
    def getRunLimit(self, set: java.util.Set['AttributedCharacterIterator.Attribute']) -> int: ...
    @typing.overload
    def getRunStart(self) -> int: ...
    @typing.overload
    def getRunStart(self, attribute: 'AttributedCharacterIterator.Attribute') -> int: ...
    @typing.overload
    def getRunStart(self, set: java.util.Set['AttributedCharacterIterator.Attribute']) -> int: ...
    class Attribute(java.io.Serializable):
        LANGUAGE: typing.ClassVar['AttributedCharacterIterator.Attribute'] = ...
        READING: typing.ClassVar['AttributedCharacterIterator.Attribute'] = ...
        INPUT_METHOD_SEGMENT: typing.ClassVar['AttributedCharacterIterator.Attribute'] = ...
        def equals(self, object: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def toString(self) -> str: ...

class RuleBasedCollator(Collator):
    def __init__(self, string: str): ...
    def clone(self) -> typing.Any: ...
    @typing.overload
    def compare(self, object: typing.Any, object2: typing.Any) -> int: ...
    @typing.overload
    def compare(self, string: str, string2: str) -> int: ...
    @typing.overload
    def equals(self, string: str, string2: str) -> bool: ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def getCollationElementIterator(self, string: str) -> CollationElementIterator: ...
    @typing.overload
    def getCollationElementIterator(self, characterIterator: CharacterIterator) -> CollationElementIterator: ...
    def getCollationKey(self, string: str) -> CollationKey: ...
    def getRules(self) -> str: ...
    def hashCode(self) -> int: ...

class StringCharacterIterator(CharacterIterator):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    @typing.overload
    def __init__(self, string: str, int: int, int2: int, int3: int): ...
    def clone(self) -> typing.Any: ...
    def current(self) -> str: ...
    def equals(self, object: typing.Any) -> bool: ...
    def first(self) -> str: ...
    def getBeginIndex(self) -> int: ...
    def getEndIndex(self) -> int: ...
    def getIndex(self) -> int: ...
    def hashCode(self) -> int: ...
    def last(self) -> str: ...
    def next(self) -> str: ...
    def previous(self) -> str: ...
    def setIndex(self, int: int) -> str: ...
    def setText(self, string: str) -> None: ...

class Format(java.io.Serializable, java.lang.Cloneable):
    def clone(self) -> typing.Any: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    def formatToCharacterIterator(self, object: typing.Any) -> AttributedCharacterIterator: ...
    @typing.overload
    def parseObject(self, string: str, parsePosition: ParsePosition) -> typing.Any: ...
    @typing.overload
    def parseObject(self, string: str) -> typing.Any: ...
    class Field(AttributedCharacterIterator.Attribute): ...

class DateFormat(Format):
    ERA_FIELD: typing.ClassVar[int] = ...
    YEAR_FIELD: typing.ClassVar[int] = ...
    MONTH_FIELD: typing.ClassVar[int] = ...
    DATE_FIELD: typing.ClassVar[int] = ...
    HOUR_OF_DAY1_FIELD: typing.ClassVar[int] = ...
    HOUR_OF_DAY0_FIELD: typing.ClassVar[int] = ...
    MINUTE_FIELD: typing.ClassVar[int] = ...
    SECOND_FIELD: typing.ClassVar[int] = ...
    MILLISECOND_FIELD: typing.ClassVar[int] = ...
    DAY_OF_WEEK_FIELD: typing.ClassVar[int] = ...
    DAY_OF_YEAR_FIELD: typing.ClassVar[int] = ...
    DAY_OF_WEEK_IN_MONTH_FIELD: typing.ClassVar[int] = ...
    WEEK_OF_YEAR_FIELD: typing.ClassVar[int] = ...
    WEEK_OF_MONTH_FIELD: typing.ClassVar[int] = ...
    AM_PM_FIELD: typing.ClassVar[int] = ...
    HOUR1_FIELD: typing.ClassVar[int] = ...
    HOUR0_FIELD: typing.ClassVar[int] = ...
    TIMEZONE_FIELD: typing.ClassVar[int] = ...
    FULL: typing.ClassVar[int] = ...
    LONG: typing.ClassVar[int] = ...
    MEDIUM: typing.ClassVar[int] = ...
    SHORT: typing.ClassVar[int] = ...
    DEFAULT: typing.ClassVar[int] = ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def format(self, date: java.util.Date, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, date: java.util.Date) -> str: ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]: ...
    def getCalendar(self) -> java.util.Calendar: ...
    @typing.overload
    @staticmethod
    def getDateInstance() -> 'DateFormat': ...
    @typing.overload
    @staticmethod
    def getDateInstance(int: int) -> 'DateFormat': ...
    @typing.overload
    @staticmethod
    def getDateInstance(int: int, locale: java.util.Locale) -> 'DateFormat': ...
    @typing.overload
    @staticmethod
    def getDateTimeInstance() -> 'DateFormat': ...
    @typing.overload
    @staticmethod
    def getDateTimeInstance(int: int, int2: int) -> 'DateFormat': ...
    @typing.overload
    @staticmethod
    def getDateTimeInstance(int: int, int2: int, locale: java.util.Locale) -> 'DateFormat': ...
    @staticmethod
    def getInstance() -> 'DateFormat': ...
    def getNumberFormat(self) -> 'NumberFormat': ...
    @typing.overload
    @staticmethod
    def getTimeInstance() -> 'DateFormat': ...
    @typing.overload
    @staticmethod
    def getTimeInstance(int: int) -> 'DateFormat': ...
    @typing.overload
    @staticmethod
    def getTimeInstance(int: int, locale: java.util.Locale) -> 'DateFormat': ...
    def getTimeZone(self) -> java.util.TimeZone: ...
    def hashCode(self) -> int: ...
    def isLenient(self) -> bool: ...
    @typing.overload
    def parse(self, string: str, parsePosition: ParsePosition) -> java.util.Date: ...
    @typing.overload
    def parse(self, string: str) -> java.util.Date: ...
    @typing.overload
    def parseObject(self, string: str, parsePosition: ParsePosition) -> typing.Any: ...
    @typing.overload
    def parseObject(self, string: str) -> typing.Any: ...
    def setCalendar(self, calendar: java.util.Calendar) -> None: ...
    def setLenient(self, boolean: bool) -> None: ...
    def setNumberFormat(self, numberFormat: 'NumberFormat') -> None: ...
    def setTimeZone(self, timeZone: java.util.TimeZone) -> None: ...
    class Field(Format.Field):
        ERA: typing.ClassVar['DateFormat.Field'] = ...
        YEAR: typing.ClassVar['DateFormat.Field'] = ...
        MONTH: typing.ClassVar['DateFormat.Field'] = ...
        DAY_OF_MONTH: typing.ClassVar['DateFormat.Field'] = ...
        HOUR_OF_DAY1: typing.ClassVar['DateFormat.Field'] = ...
        HOUR_OF_DAY0: typing.ClassVar['DateFormat.Field'] = ...
        MINUTE: typing.ClassVar['DateFormat.Field'] = ...
        SECOND: typing.ClassVar['DateFormat.Field'] = ...
        MILLISECOND: typing.ClassVar['DateFormat.Field'] = ...
        DAY_OF_WEEK: typing.ClassVar['DateFormat.Field'] = ...
        DAY_OF_YEAR: typing.ClassVar['DateFormat.Field'] = ...
        DAY_OF_WEEK_IN_MONTH: typing.ClassVar['DateFormat.Field'] = ...
        WEEK_OF_YEAR: typing.ClassVar['DateFormat.Field'] = ...
        WEEK_OF_MONTH: typing.ClassVar['DateFormat.Field'] = ...
        AM_PM: typing.ClassVar['DateFormat.Field'] = ...
        HOUR1: typing.ClassVar['DateFormat.Field'] = ...
        HOUR0: typing.ClassVar['DateFormat.Field'] = ...
        TIME_ZONE: typing.ClassVar['DateFormat.Field'] = ...
        def getCalendarField(self) -> int: ...
        @staticmethod
        def ofCalendarField(int: int) -> 'DateFormat.Field': ...

class MessageFormat(Format):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, locale: java.util.Locale): ...
    def applyPattern(self, string: str) -> None: ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, objectArray: typing.List[typing.Any], stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    @staticmethod
    def format(string: str, objectArray: typing.List[typing.Any]) -> str: ...
    def formatToCharacterIterator(self, object: typing.Any) -> AttributedCharacterIterator: ...
    def getFormats(self) -> typing.List[Format]: ...
    def getFormatsByArgumentIndex(self) -> typing.List[Format]: ...
    def getLocale(self) -> java.util.Locale: ...
    def hashCode(self) -> int: ...
    @typing.overload
    def parse(self, string: str) -> typing.List[typing.Any]: ...
    @typing.overload
    def parse(self, string: str, parsePosition: ParsePosition) -> typing.List[typing.Any]: ...
    @typing.overload
    def parseObject(self, string: str) -> typing.Any: ...
    @typing.overload
    def parseObject(self, string: str, parsePosition: ParsePosition) -> typing.Any: ...
    def setFormat(self, int: int, format: Format) -> None: ...
    def setFormatByArgumentIndex(self, int: int, format: Format) -> None: ...
    def setFormats(self, formatArray: typing.List[Format]) -> None: ...
    def setFormatsByArgumentIndex(self, formatArray: typing.List[Format]) -> None: ...
    def setLocale(self, locale: java.util.Locale) -> None: ...
    def toPattern(self) -> str: ...
    class Field(Format.Field):
        ARGUMENT: typing.ClassVar['MessageFormat.Field'] = ...

class NumberFormat(Format):
    INTEGER_FIELD: typing.ClassVar[int] = ...
    FRACTION_FIELD: typing.ClassVar[int] = ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def format(self, double: float, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, long: int, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]: ...
    def getCurrency(self) -> java.util.Currency: ...
    @typing.overload
    @staticmethod
    def getCurrencyInstance() -> 'NumberFormat': ...
    @typing.overload
    @staticmethod
    def getCurrencyInstance(locale: java.util.Locale) -> 'NumberFormat': ...
    @typing.overload
    @staticmethod
    def getInstance() -> 'NumberFormat': ...
    @typing.overload
    @staticmethod
    def getInstance(locale: java.util.Locale) -> 'NumberFormat': ...
    @typing.overload
    @staticmethod
    def getIntegerInstance() -> 'NumberFormat': ...
    @typing.overload
    @staticmethod
    def getIntegerInstance(locale: java.util.Locale) -> 'NumberFormat': ...
    def getMaximumFractionDigits(self) -> int: ...
    def getMaximumIntegerDigits(self) -> int: ...
    def getMinimumFractionDigits(self) -> int: ...
    def getMinimumIntegerDigits(self) -> int: ...
    @typing.overload
    @staticmethod
    def getNumberInstance() -> 'NumberFormat': ...
    @typing.overload
    @staticmethod
    def getNumberInstance(locale: java.util.Locale) -> 'NumberFormat': ...
    @typing.overload
    @staticmethod
    def getPercentInstance() -> 'NumberFormat': ...
    @typing.overload
    @staticmethod
    def getPercentInstance(locale: java.util.Locale) -> 'NumberFormat': ...
    def getRoundingMode(self) -> java.math.RoundingMode: ...
    def hashCode(self) -> int: ...
    def isGroupingUsed(self) -> bool: ...
    def isParseIntegerOnly(self) -> bool: ...
    @typing.overload
    def parse(self, string: str, parsePosition: ParsePosition) -> java.lang.Number: ...
    @typing.overload
    def parse(self, string: str) -> java.lang.Number: ...
    @typing.overload
    def parseObject(self, string: str, parsePosition: ParsePosition) -> typing.Any: ...
    @typing.overload
    def parseObject(self, string: str) -> typing.Any: ...
    def setCurrency(self, currency: java.util.Currency) -> None: ...
    def setGroupingUsed(self, boolean: bool) -> None: ...
    def setMaximumFractionDigits(self, int: int) -> None: ...
    def setMaximumIntegerDigits(self, int: int) -> None: ...
    def setMinimumFractionDigits(self, int: int) -> None: ...
    def setMinimumIntegerDigits(self, int: int) -> None: ...
    def setParseIntegerOnly(self, boolean: bool) -> None: ...
    def setRoundingMode(self, roundingMode: java.math.RoundingMode) -> None: ...
    class Field(Format.Field):
        INTEGER: typing.ClassVar['NumberFormat.Field'] = ...
        FRACTION: typing.ClassVar['NumberFormat.Field'] = ...
        EXPONENT: typing.ClassVar['NumberFormat.Field'] = ...
        DECIMAL_SEPARATOR: typing.ClassVar['NumberFormat.Field'] = ...
        SIGN: typing.ClassVar['NumberFormat.Field'] = ...
        GROUPING_SEPARATOR: typing.ClassVar['NumberFormat.Field'] = ...
        EXPONENT_SYMBOL: typing.ClassVar['NumberFormat.Field'] = ...
        PERCENT: typing.ClassVar['NumberFormat.Field'] = ...
        PERMILLE: typing.ClassVar['NumberFormat.Field'] = ...
        CURRENCY: typing.ClassVar['NumberFormat.Field'] = ...
        EXPONENT_SIGN: typing.ClassVar['NumberFormat.Field'] = ...

class ChoiceFormat(NumberFormat):
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], stringArray: typing.List[str]): ...
    @typing.overload
    def __init__(self, string: str): ...
    def applyPattern(self, string: str) -> None: ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, double: float, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, long: int, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    def getFormats(self) -> typing.List[typing.Any]: ...
    def getLimits(self) -> typing.List[float]: ...
    def hashCode(self) -> int: ...
    @typing.overload
    @staticmethod
    def nextDouble(double: float, boolean: bool) -> float: ...
    @typing.overload
    @staticmethod
    def nextDouble(double: float) -> float: ...
    @typing.overload
    def parse(self, string: str, parsePosition: ParsePosition) -> java.lang.Number: ...
    @typing.overload
    def parse(self, string: str) -> java.lang.Number: ...
    @staticmethod
    def previousDouble(double: float) -> float: ...
    def setChoices(self, doubleArray: typing.List[float], stringArray: typing.List[str]) -> None: ...
    def toPattern(self) -> str: ...

class DecimalFormat(NumberFormat):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, decimalFormatSymbols: DecimalFormatSymbols): ...
    def applyLocalizedPattern(self, string: str) -> None: ...
    def applyPattern(self, string: str) -> None: ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    @typing.overload
    def format(self, double: float) -> str: ...
    @typing.overload
    def format(self, long: int) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, double: float, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, long: int, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    def formatToCharacterIterator(self, object: typing.Any) -> AttributedCharacterIterator: ...
    def getCurrency(self) -> java.util.Currency: ...
    def getDecimalFormatSymbols(self) -> DecimalFormatSymbols: ...
    def getGroupingSize(self) -> int: ...
    def getMaximumFractionDigits(self) -> int: ...
    def getMaximumIntegerDigits(self) -> int: ...
    def getMinimumFractionDigits(self) -> int: ...
    def getMinimumIntegerDigits(self) -> int: ...
    def getMultiplier(self) -> int: ...
    def getNegativePrefix(self) -> str: ...
    def getNegativeSuffix(self) -> str: ...
    def getPositivePrefix(self) -> str: ...
    def getPositiveSuffix(self) -> str: ...
    def getRoundingMode(self) -> java.math.RoundingMode: ...
    def hashCode(self) -> int: ...
    def isDecimalSeparatorAlwaysShown(self) -> bool: ...
    def isParseBigDecimal(self) -> bool: ...
    @typing.overload
    def parse(self, string: str, parsePosition: ParsePosition) -> java.lang.Number: ...
    @typing.overload
    def parse(self, string: str) -> java.lang.Number: ...
    def setCurrency(self, currency: java.util.Currency) -> None: ...
    def setDecimalFormatSymbols(self, decimalFormatSymbols: DecimalFormatSymbols) -> None: ...
    def setDecimalSeparatorAlwaysShown(self, boolean: bool) -> None: ...
    def setGroupingSize(self, int: int) -> None: ...
    def setGroupingUsed(self, boolean: bool) -> None: ...
    def setMaximumFractionDigits(self, int: int) -> None: ...
    def setMaximumIntegerDigits(self, int: int) -> None: ...
    def setMinimumFractionDigits(self, int: int) -> None: ...
    def setMinimumIntegerDigits(self, int: int) -> None: ...
    def setMultiplier(self, int: int) -> None: ...
    def setNegativePrefix(self, string: str) -> None: ...
    def setNegativeSuffix(self, string: str) -> None: ...
    def setParseBigDecimal(self, boolean: bool) -> None: ...
    def setPositivePrefix(self, string: str) -> None: ...
    def setPositiveSuffix(self, string: str) -> None: ...
    def setRoundingMode(self, roundingMode: java.math.RoundingMode) -> None: ...
    def toLocalizedPattern(self) -> str: ...
    def toPattern(self) -> str: ...

class SimpleDateFormat(DateFormat):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dateFormatSymbols: DateFormatSymbols): ...
    @typing.overload
    def __init__(self, string: str, locale: java.util.Locale): ...
    def applyLocalizedPattern(self, string: str) -> None: ...
    def applyPattern(self, string: str) -> None: ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def format(self, date: java.util.Date) -> str: ...
    @typing.overload
    def format(self, object: typing.Any) -> str: ...
    @typing.overload
    def format(self, object: typing.Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @typing.overload
    def format(self, date: java.util.Date, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    def formatToCharacterIterator(self, object: typing.Any) -> AttributedCharacterIterator: ...
    def get2DigitYearStart(self) -> java.util.Date: ...
    def getDateFormatSymbols(self) -> DateFormatSymbols: ...
    def hashCode(self) -> int: ...
    @typing.overload
    def parse(self, string: str) -> java.util.Date: ...
    @typing.overload
    def parse(self, string: str, parsePosition: ParsePosition) -> java.util.Date: ...
    def set2DigitYearStart(self, date: java.util.Date) -> None: ...
    def setDateFormatSymbols(self, dateFormatSymbols: DateFormatSymbols) -> None: ...
    def toLocalizedPattern(self) -> str: ...
    def toPattern(self) -> str: ...
