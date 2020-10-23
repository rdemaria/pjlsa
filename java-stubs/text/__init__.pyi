from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import java
import java.io
import java.lang
import java.math
import java.util


class Annotation:
    def __init__(self, object: _py_Any): ...
    def getValue(self) -> _py_Any: ...
    def toString(self) -> str: ...

class AttributeEntry(java.util.Map.Entry['AttributedCharacterIterator.Attribute', _py_Any]):
    def equals(self, object: _py_Any) -> bool: ...
    @overload
    def getKey(self) -> _py_Any: ...
    @overload
    def getKey(self) -> 'AttributedCharacterIterator.Attribute': ...
    def getValue(self) -> _py_Any: ...
    def hashCode(self) -> int: ...
    def setValue(self, object: _py_Any) -> _py_Any: ...
    def toString(self) -> str: ...

class AttributedString:
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, map: java.util.Map['AttributedCharacterIterator.Attribute', _py_Any]): ...
    @overload
    def __init__(self, attributedCharacterIterator: 'AttributedCharacterIterator'): ...
    @overload
    def __init__(self, attributedCharacterIterator: 'AttributedCharacterIterator', int: int, int2: int): ...
    @overload
    def __init__(self, attributedCharacterIterator: 'AttributedCharacterIterator', int: int, int2: int, attributeArray: _py_List['AttributedCharacterIterator.Attribute']): ...
    @overload
    def addAttribute(self, attribute: 'AttributedCharacterIterator.Attribute', object: _py_Any) -> None: ...
    @overload
    def addAttribute(self, attribute: 'AttributedCharacterIterator.Attribute', object: _py_Any, int: int, int2: int) -> None: ...
    def addAttributes(self, map: java.util.Map['AttributedCharacterIterator.Attribute', _py_Any], int: int, int2: int) -> None: ...
    @overload
    def getIterator(self) -> 'AttributedCharacterIterator': ...
    @overload
    def getIterator(self, attributeArray: _py_List['AttributedCharacterIterator.Attribute']) -> 'AttributedCharacterIterator': ...
    @overload
    def getIterator(self, attributeArray: _py_List['AttributedCharacterIterator.Attribute'], int: int, int2: int) -> 'AttributedCharacterIterator': ...

class Bidi:
    DIRECTION_LEFT_TO_RIGHT: _py_ClassVar[int] = ...
    DIRECTION_RIGHT_TO_LEFT: _py_ClassVar[int] = ...
    DIRECTION_DEFAULT_LEFT_TO_RIGHT: _py_ClassVar[int] = ...
    DIRECTION_DEFAULT_RIGHT_TO_LEFT: _py_ClassVar[int] = ...
    @overload
    def __init__(self, charArray: _py_List[str], int: int, byteArray: _py_List[int], int2: int, int3: int, int4: int): ...
    @overload
    def __init__(self, string: str, int: int): ...
    @overload
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
    @classmethod
    def reorderVisually(cls, byteArray: _py_List[int], int: int, objectArray: _py_List[_py_Any], int2: int, int3: int) -> None: ...
    @classmethod
    def requiresBidi(cls, charArray: _py_List[str], int: int, int2: int) -> bool: ...
    def toString(self) -> str: ...

class BreakIterator(java.lang.Cloneable):
    DONE: _py_ClassVar[int] = ...
    def clone(self) -> _py_Any: ...
    def current(self) -> int: ...
    def first(self) -> int: ...
    def following(self, int: int) -> int: ...
    @classmethod
    def getAvailableLocales(cls) -> _py_List[java.util.Locale]: ...
    @classmethod
    @overload
    def getCharacterInstance(cls) -> 'BreakIterator': ...
    @classmethod
    @overload
    def getCharacterInstance(cls, locale: java.util.Locale) -> 'BreakIterator': ...
    @classmethod
    @overload
    def getLineInstance(cls) -> 'BreakIterator': ...
    @classmethod
    @overload
    def getLineInstance(cls, locale: java.util.Locale) -> 'BreakIterator': ...
    @classmethod
    @overload
    def getSentenceInstance(cls) -> 'BreakIterator': ...
    @classmethod
    @overload
    def getSentenceInstance(cls, locale: java.util.Locale) -> 'BreakIterator': ...
    def getText(self) -> 'CharacterIterator': ...
    @classmethod
    @overload
    def getWordInstance(cls) -> 'BreakIterator': ...
    @classmethod
    @overload
    def getWordInstance(cls, locale: java.util.Locale) -> 'BreakIterator': ...
    def isBoundary(self, int: int) -> bool: ...
    def last(self) -> int: ...
    @overload
    def next(self) -> int: ...
    @overload
    def next(self, int: int) -> int: ...
    def preceding(self, int: int) -> int: ...
    def previous(self) -> int: ...
    @overload
    def setText(self, characterIterator: 'CharacterIterator') -> None: ...
    @overload
    def setText(self, string: str) -> None: ...

class CalendarBuilder:
    WEEK_YEAR: _py_ClassVar[int] = ...
    ISO_DAY_OF_WEEK: _py_ClassVar[int] = ...
    def toString(self) -> str: ...

class CharacterIterator(java.lang.Cloneable):
    DONE: _py_ClassVar[str] = ...
    def clone(self) -> _py_Any: ...
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
    NULLORDER: _py_ClassVar[int] = ...
    def getMaxExpansion(self, int: int) -> int: ...
    def getOffset(self) -> int: ...
    def next(self) -> int: ...
    def previous(self) -> int: ...
    @classmethod
    def primaryOrder(cls, int: int) -> int: ...
    def reset(self) -> None: ...
    @classmethod
    def secondaryOrder(cls, int: int) -> int: ...
    def setOffset(self, int: int) -> None: ...
    @overload
    def setText(self, string: str) -> None: ...
    @overload
    def setText(self, characterIterator: CharacterIterator) -> None: ...
    @classmethod
    def tertiaryOrder(cls, int: int) -> int: ...

class CollationKey(java.lang.Comparable['CollationKey']):
    @overload
    def compareTo(self, collationKey: 'CollationKey') -> int: ...
    @overload
    def compareTo(self, object: _py_Any) -> int: ...
    def getSourceString(self) -> str: ...
    def toByteArray(self) -> _py_List[int]: ...

class Collator(java.util.Comparator[_py_Any], java.lang.Cloneable):
    PRIMARY: _py_ClassVar[int] = ...
    SECONDARY: _py_ClassVar[int] = ...
    TERTIARY: _py_ClassVar[int] = ...
    IDENTICAL: _py_ClassVar[int] = ...
    NO_DECOMPOSITION: _py_ClassVar[int] = ...
    CANONICAL_DECOMPOSITION: _py_ClassVar[int] = ...
    FULL_DECOMPOSITION: _py_ClassVar[int] = ...
    def clone(self) -> _py_Any: ...
    @overload
    def compare(self, string: str, string2: str) -> int: ...
    @overload
    def compare(self, object: _py_Any, object2: _py_Any) -> int: ...
    @overload
    def equals(self, object: _py_Any) -> bool: ...
    @overload
    def equals(self, string: str, string2: str) -> bool: ...
    @classmethod
    def getAvailableLocales(cls) -> _py_List[java.util.Locale]: ...
    def getCollationKey(self, string: str) -> CollationKey: ...
    def getDecomposition(self) -> int: ...
    @classmethod
    @overload
    def getInstance(cls, locale: java.util.Locale) -> 'Collator': ...
    @classmethod
    @overload
    def getInstance(cls) -> 'Collator': ...
    def getStrength(self) -> int: ...
    def hashCode(self) -> int: ...
    def setDecomposition(self, int: int) -> None: ...
    def setStrength(self, int: int) -> None: ...

class DateFormatSymbols(java.io.Serializable, java.lang.Cloneable):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, locale: java.util.Locale): ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getAmPmStrings(self) -> _py_List[str]: ...
    @classmethod
    def getAvailableLocales(cls) -> _py_List[java.util.Locale]: ...
    def getEras(self) -> _py_List[str]: ...
    @classmethod
    @overload
    def getInstance(cls) -> 'DateFormatSymbols': ...
    @classmethod
    @overload
    def getInstance(cls, locale: java.util.Locale) -> 'DateFormatSymbols': ...
    def getLocalPatternChars(self) -> str: ...
    def getMonths(self) -> _py_List[str]: ...
    def getShortMonths(self) -> _py_List[str]: ...
    def getShortWeekdays(self) -> _py_List[str]: ...
    def getWeekdays(self) -> _py_List[str]: ...
    def getZoneStrings(self) -> _py_List[_py_List[str]]: ...
    def hashCode(self) -> int: ...
    def setAmPmStrings(self, stringArray: _py_List[str]) -> None: ...
    def setEras(self, stringArray: _py_List[str]) -> None: ...
    def setLocalPatternChars(self, string: str) -> None: ...
    def setMonths(self, stringArray: _py_List[str]) -> None: ...
    def setShortMonths(self, stringArray: _py_List[str]) -> None: ...
    def setShortWeekdays(self, stringArray: _py_List[str]) -> None: ...
    def setWeekdays(self, stringArray: _py_List[str]) -> None: ...
    def setZoneStrings(self, stringArray: _py_List[_py_List[str]]) -> None: ...

class DecimalFormatSymbols(java.lang.Cloneable, java.io.Serializable):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, locale: java.util.Locale): ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    @classmethod
    def getAvailableLocales(cls) -> _py_List[java.util.Locale]: ...
    def getCurrency(self) -> java.util.Currency: ...
    def getCurrencySymbol(self) -> str: ...
    def getDecimalSeparator(self) -> str: ...
    def getDigit(self) -> str: ...
    def getExponentSeparator(self) -> str: ...
    def getGroupingSeparator(self) -> str: ...
    def getInfinity(self) -> str: ...
    @classmethod
    @overload
    def getInstance(cls) -> 'DecimalFormatSymbols': ...
    @classmethod
    @overload
    def getInstance(cls, locale: java.util.Locale) -> 'DecimalFormatSymbols': ...
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

class DigitList(java.lang.Cloneable):
    MAX_COUNT: _py_ClassVar[int] = ...
    decimalAt: int = ...
    count: int = ...
    digits: _py_List[str] = ...
    def append(self, char: str) -> None: ...
    def clear(self) -> None: ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getBigDecimal(self) -> java.math.BigDecimal: ...
    def getDouble(self) -> float: ...
    def getLong(self) -> int: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class EntryPair:
    entryName: str = ...
    value: int = ...
    fwd: bool = ...
    @overload
    def __init__(self, string: str, int: int): ...
    @overload
    def __init__(self, string: str, int: int, boolean: bool): ...

class FieldPosition:
    @overload
    def __init__(self, int: int): ...
    @overload
    def __init__(self, field: 'Format.Field'): ...
    @overload
    def __init__(self, field: 'Format.Field', int: int): ...
    def equals(self, object: _py_Any) -> bool: ...
    def getBeginIndex(self) -> int: ...
    def getEndIndex(self) -> int: ...
    def getField(self) -> int: ...
    def getFieldAttribute(self) -> 'Format.Field': ...
    def hashCode(self) -> int: ...
    def setBeginIndex(self, int: int) -> None: ...
    def setEndIndex(self, int: int) -> None: ...
    def toString(self) -> str: ...

class MergeCollation:
    def __init__(self, string: str): ...
    def addPattern(self, string: str) -> None: ...
    @overload
    def emitPattern(self) -> str: ...
    @overload
    def emitPattern(self, boolean: bool) -> str: ...
    def getCount(self) -> int: ...
    def getItemAt(self, int: int) -> 'PatternEntry': ...
    @overload
    def getPattern(self) -> str: ...
    @overload
    def getPattern(self, boolean: bool) -> str: ...
    def setPattern(self, string: str) -> None: ...

class Normalizer:
    @classmethod
    def isNormalized(cls, charSequence: java.lang.CharSequence, form: 'Normalizer.Form') -> bool: ...
    @classmethod
    def normalize(cls, charSequence: java.lang.CharSequence, form: 'Normalizer.Form') -> str: ...
    class Form(java.lang.Enum['Normalizer.Form']):
        NFD: _py_ClassVar['Normalizer.Form'] = ...
        NFC: _py_ClassVar['Normalizer.Form'] = ...
        NFKD: _py_ClassVar['Normalizer.Form'] = ...
        NFKC: _py_ClassVar['Normalizer.Form'] = ...
        _valueOf_0__T = _py_TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @overload
        def valueOf(cls, class_: _py_Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @classmethod
        @overload
        def valueOf(cls, string: str) -> 'Normalizer.Form': ...
        @classmethod
        def values(cls) -> _py_List['Normalizer.Form']: ...

class ParseException(java.lang.Exception):
    def __init__(self, string: str, int: int): ...
    def getErrorOffset(self) -> int: ...

class ParsePosition:
    def __init__(self, int: int): ...
    def equals(self, object: _py_Any) -> bool: ...
    def getErrorIndex(self) -> int: ...
    def getIndex(self) -> int: ...
    def hashCode(self) -> int: ...
    def setErrorIndex(self, int: int) -> None: ...
    def setIndex(self, int: int) -> None: ...
    def toString(self) -> str: ...

class PatternEntry:
    def appendQuotedChars(self, stringBuffer: java.lang.StringBuffer) -> None: ...
    def appendQuotedExtension(self, stringBuffer: java.lang.StringBuffer) -> None: ...
    def equals(self, object: _py_Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class RBCollationTables:
    def __init__(self, string: str, int: int): ...
    def getRules(self) -> str: ...
    def isFrenchSec(self) -> bool: ...
    def isSEAsianSwapping(self) -> bool: ...

class RBTableBuilder:
    def __init__(self, buildAPI: 'RBCollationTables.BuildAPI'): ...
    def build(self, string: str, int: int) -> None: ...

class AttributedCharacterIterator(CharacterIterator):
    def getAllAttributeKeys(self) -> java.util.Set['AttributedCharacterIterator.Attribute']: ...
    def getAttribute(self, attribute: 'AttributedCharacterIterator.Attribute') -> _py_Any: ...
    def getAttributes(self) -> java.util.Map['AttributedCharacterIterator.Attribute', _py_Any]: ...
    @overload
    def getRunLimit(self) -> int: ...
    @overload
    def getRunLimit(self, attribute: 'AttributedCharacterIterator.Attribute') -> int: ...
    @overload
    def getRunLimit(self, set: java.util.Set['AttributedCharacterIterator.Attribute']) -> int: ...
    @overload
    def getRunStart(self) -> int: ...
    @overload
    def getRunStart(self, attribute: 'AttributedCharacterIterator.Attribute') -> int: ...
    @overload
    def getRunStart(self, set: java.util.Set['AttributedCharacterIterator.Attribute']) -> int: ...
    class Attribute(java.io.Serializable):
        LANGUAGE: _py_ClassVar['AttributedCharacterIterator.Attribute'] = ...
        READING: _py_ClassVar['AttributedCharacterIterator.Attribute'] = ...
        INPUT_METHOD_SEGMENT: _py_ClassVar['AttributedCharacterIterator.Attribute'] = ...
        def equals(self, object: _py_Any) -> bool: ...
        def hashCode(self) -> int: ...
        def toString(self) -> str: ...

class DontCareFieldPosition(FieldPosition): ...

class RuleBasedCollationKey(CollationKey):
    @overload
    def compareTo(self, object: _py_Any) -> int: ...
    @overload
    def compareTo(self, collationKey: CollationKey) -> int: ...
    def equals(self, object: _py_Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toByteArray(self) -> _py_List[int]: ...

class RuleBasedCollator(Collator):
    def __init__(self, string: str): ...
    def clone(self) -> _py_Any: ...
    @overload
    def compare(self, object: _py_Any, object2: _py_Any) -> int: ...
    @overload
    def compare(self, string: str, string2: str) -> int: ...
    @overload
    def equals(self, string: str, string2: str) -> bool: ...
    @overload
    def equals(self, object: _py_Any) -> bool: ...
    @overload
    def getCollationElementIterator(self, string: str) -> CollationElementIterator: ...
    @overload
    def getCollationElementIterator(self, characterIterator: CharacterIterator) -> CollationElementIterator: ...
    def getCollationKey(self, string: str) -> CollationKey: ...
    def getRules(self) -> str: ...
    def hashCode(self) -> int: ...

class StringCharacterIterator(CharacterIterator):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, int: int): ...
    @overload
    def __init__(self, string: str, int: int, int2: int, int3: int): ...
    def clone(self) -> _py_Any: ...
    def current(self) -> str: ...
    def equals(self, object: _py_Any) -> bool: ...
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

class CharacterIteratorFieldDelegate(java.text.Format.FieldDelegate):
    @overload
    def formatted(self, int: int, field: 'Format.Field', object: _py_Any, int2: int, int3: int, stringBuffer: java.lang.StringBuffer) -> None: ...
    @overload
    def formatted(self, field: 'Format.Field', object: _py_Any, int: int, int2: int, stringBuffer: java.lang.StringBuffer) -> None: ...
    def getIterator(self, string: str) -> AttributedCharacterIterator: ...

class ChoiceFormat(java.text.NumberFormat):
    @overload
    def __init__(self, doubleArray: _py_List[float], stringArray: _py_List[str]): ...
    @overload
    def __init__(self, string: str): ...
    def applyPattern(self, string: str) -> None: ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    @overload
    def format(self, object: _py_Any) -> str: ...
    @overload
    def format(self, double: float) -> str: ...
    @overload
    def format(self, long: int) -> str: ...
    @overload
    def format(self, double: float, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @overload
    def format(self, long: int, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @overload
    def format(self, object: _py_Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    def getFormats(self) -> _py_List[_py_Any]: ...
    def getLimits(self) -> _py_List[float]: ...
    def hashCode(self) -> int: ...
    @classmethod
    @overload
    def nextDouble(cls, double: float, boolean: bool) -> float: ...
    @classmethod
    @overload
    def nextDouble(cls, double: float) -> float: ...
    @overload
    def parse(self, string: str, parsePosition: ParsePosition) -> java.lang.Number: ...
    @overload
    def parse(self, string: str) -> java.lang.Number: ...
    @classmethod
    def previousDouble(cls, double: float) -> float: ...
    def setChoices(self, doubleArray: _py_List[float], stringArray: _py_List[str]) -> None: ...
    def toPattern(self) -> str: ...

class DateFormat(java.text.Format):
    ERA_FIELD: _py_ClassVar[int] = ...
    YEAR_FIELD: _py_ClassVar[int] = ...
    MONTH_FIELD: _py_ClassVar[int] = ...
    DATE_FIELD: _py_ClassVar[int] = ...
    HOUR_OF_DAY1_FIELD: _py_ClassVar[int] = ...
    HOUR_OF_DAY0_FIELD: _py_ClassVar[int] = ...
    MINUTE_FIELD: _py_ClassVar[int] = ...
    SECOND_FIELD: _py_ClassVar[int] = ...
    MILLISECOND_FIELD: _py_ClassVar[int] = ...
    DAY_OF_WEEK_FIELD: _py_ClassVar[int] = ...
    DAY_OF_YEAR_FIELD: _py_ClassVar[int] = ...
    DAY_OF_WEEK_IN_MONTH_FIELD: _py_ClassVar[int] = ...
    WEEK_OF_YEAR_FIELD: _py_ClassVar[int] = ...
    WEEK_OF_MONTH_FIELD: _py_ClassVar[int] = ...
    AM_PM_FIELD: _py_ClassVar[int] = ...
    HOUR1_FIELD: _py_ClassVar[int] = ...
    HOUR0_FIELD: _py_ClassVar[int] = ...
    TIMEZONE_FIELD: _py_ClassVar[int] = ...
    FULL: _py_ClassVar[int] = ...
    LONG: _py_ClassVar[int] = ...
    MEDIUM: _py_ClassVar[int] = ...
    SHORT: _py_ClassVar[int] = ...
    DEFAULT: _py_ClassVar[int] = ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    @overload
    def format(self, date: java.util.Date, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @overload
    def format(self, date: java.util.Date) -> str: ...
    @overload
    def format(self, object: _py_Any) -> str: ...
    @overload
    def format(self, object: _py_Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @classmethod
    def getAvailableLocales(cls) -> _py_List[java.util.Locale]: ...
    def getCalendar(self) -> java.util.Calendar: ...
    @classmethod
    @overload
    def getDateInstance(cls) -> 'DateFormat': ...
    @classmethod
    @overload
    def getDateInstance(cls, int: int) -> 'DateFormat': ...
    @classmethod
    @overload
    def getDateInstance(cls, int: int, locale: java.util.Locale) -> 'DateFormat': ...
    @classmethod
    @overload
    def getDateTimeInstance(cls) -> 'DateFormat': ...
    @classmethod
    @overload
    def getDateTimeInstance(cls, int: int, int2: int) -> 'DateFormat': ...
    @classmethod
    @overload
    def getDateTimeInstance(cls, int: int, int2: int, locale: java.util.Locale) -> 'DateFormat': ...
    @classmethod
    def getInstance(cls) -> 'DateFormat': ...
    def getNumberFormat(self) -> 'NumberFormat': ...
    @classmethod
    @overload
    def getTimeInstance(cls) -> 'DateFormat': ...
    @classmethod
    @overload
    def getTimeInstance(cls, int: int) -> 'DateFormat': ...
    @classmethod
    @overload
    def getTimeInstance(cls, int: int, locale: java.util.Locale) -> 'DateFormat': ...
    def getTimeZone(self) -> java.util.TimeZone: ...
    def hashCode(self) -> int: ...
    def isLenient(self) -> bool: ...
    @overload
    def parse(self, string: str, parsePosition: ParsePosition) -> java.util.Date: ...
    @overload
    def parse(self, string: str) -> java.util.Date: ...
    @overload
    def parseObject(self, string: str, parsePosition: ParsePosition) -> _py_Any: ...
    @overload
    def parseObject(self, string: str) -> _py_Any: ...
    def setCalendar(self, calendar: java.util.Calendar) -> None: ...
    def setLenient(self, boolean: bool) -> None: ...
    def setNumberFormat(self, numberFormat: 'NumberFormat') -> None: ...
    def setTimeZone(self, timeZone: java.util.TimeZone) -> None: ...
    class Field(java.text.Format.Field):
        ERA: _py_ClassVar['DateFormat.Field'] = ...
        YEAR: _py_ClassVar['DateFormat.Field'] = ...
        MONTH: _py_ClassVar['DateFormat.Field'] = ...
        DAY_OF_MONTH: _py_ClassVar['DateFormat.Field'] = ...
        HOUR_OF_DAY1: _py_ClassVar['DateFormat.Field'] = ...
        HOUR_OF_DAY0: _py_ClassVar['DateFormat.Field'] = ...
        MINUTE: _py_ClassVar['DateFormat.Field'] = ...
        SECOND: _py_ClassVar['DateFormat.Field'] = ...
        MILLISECOND: _py_ClassVar['DateFormat.Field'] = ...
        DAY_OF_WEEK: _py_ClassVar['DateFormat.Field'] = ...
        DAY_OF_YEAR: _py_ClassVar['DateFormat.Field'] = ...
        DAY_OF_WEEK_IN_MONTH: _py_ClassVar['DateFormat.Field'] = ...
        WEEK_OF_YEAR: _py_ClassVar['DateFormat.Field'] = ...
        WEEK_OF_MONTH: _py_ClassVar['DateFormat.Field'] = ...
        AM_PM: _py_ClassVar['DateFormat.Field'] = ...
        HOUR1: _py_ClassVar['DateFormat.Field'] = ...
        HOUR0: _py_ClassVar['DateFormat.Field'] = ...
        TIME_ZONE: _py_ClassVar['DateFormat.Field'] = ...
        def getCalendarField(self) -> int: ...
        @classmethod
        def ofCalendarField(cls, int: int) -> 'DateFormat.Field': ...

class DecimalFormat(java.text.NumberFormat):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, decimalFormatSymbols: DecimalFormatSymbols): ...
    def applyLocalizedPattern(self, string: str) -> None: ...
    def applyPattern(self, string: str) -> None: ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    @overload
    def format(self, object: _py_Any) -> str: ...
    @overload
    def format(self, double: float) -> str: ...
    @overload
    def format(self, long: int) -> str: ...
    @overload
    def format(self, object: _py_Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @overload
    def format(self, double: float, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @overload
    def format(self, long: int, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    def formatToCharacterIterator(self, object: _py_Any) -> AttributedCharacterIterator: ...
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
    @overload
    def parse(self, string: str, parsePosition: ParsePosition) -> java.lang.Number: ...
    @overload
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

class Format(java.io.Serializable, java.lang.Cloneable):
    def clone(self) -> _py_Any: ...
    @overload
    def format(self, object: _py_Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @overload
    def format(self, object: _py_Any) -> str: ...
    def formatToCharacterIterator(self, object: _py_Any) -> AttributedCharacterIterator: ...
    @overload
    def parseObject(self, string: str, parsePosition: ParsePosition) -> _py_Any: ...
    @overload
    def parseObject(self, string: str) -> _py_Any: ...
    class Field(AttributedCharacterIterator.Attribute): ...
    class FieldDelegate:
        @overload
        def formatted(self, int: int, field: 'Format.Field', object: _py_Any, int2: int, int3: int, stringBuffer: java.lang.StringBuffer) -> None: ...
        @overload
        def formatted(self, field: 'Format.Field', object: _py_Any, int: int, int2: int, stringBuffer: java.lang.StringBuffer) -> None: ...

class MessageFormat(Format):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, locale: java.util.Locale): ...
    def applyPattern(self, string: str) -> None: ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    @overload
    def format(self, object: _py_Any) -> str: ...
    @overload
    def format(self, object: _py_Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @overload
    def format(self, objectArray: _py_List[_py_Any], stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @classmethod
    @overload
    def format(cls, string: str, objectArray: _py_List[_py_Any]) -> str: ...
    def formatToCharacterIterator(self, object: _py_Any) -> AttributedCharacterIterator: ...
    def getFormats(self) -> _py_List[Format]: ...
    def getFormatsByArgumentIndex(self) -> _py_List[Format]: ...
    def getLocale(self) -> java.util.Locale: ...
    def hashCode(self) -> int: ...
    @overload
    def parse(self, string: str) -> _py_List[_py_Any]: ...
    @overload
    def parse(self, string: str, parsePosition: ParsePosition) -> _py_List[_py_Any]: ...
    @overload
    def parseObject(self, string: str) -> _py_Any: ...
    @overload
    def parseObject(self, string: str, parsePosition: ParsePosition) -> _py_Any: ...
    def setFormat(self, int: int, format: Format) -> None: ...
    def setFormatByArgumentIndex(self, int: int, format: Format) -> None: ...
    def setFormats(self, formatArray: _py_List[Format]) -> None: ...
    def setFormatsByArgumentIndex(self, formatArray: _py_List[Format]) -> None: ...
    def setLocale(self, locale: java.util.Locale) -> None: ...
    def toPattern(self) -> str: ...
    class Field(Format.Field):
        ARGUMENT: _py_ClassVar['MessageFormat.Field'] = ...

class NumberFormat(Format):
    INTEGER_FIELD: _py_ClassVar[int] = ...
    FRACTION_FIELD: _py_ClassVar[int] = ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    @overload
    def format(self, double: float, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @overload
    def format(self, long: int, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @overload
    def format(self, object: _py_Any) -> str: ...
    @overload
    def format(self, double: float) -> str: ...
    @overload
    def format(self, long: int) -> str: ...
    @overload
    def format(self, object: _py_Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @classmethod
    def getAvailableLocales(cls) -> _py_List[java.util.Locale]: ...
    def getCurrency(self) -> java.util.Currency: ...
    @classmethod
    @overload
    def getCurrencyInstance(cls) -> 'NumberFormat': ...
    @classmethod
    @overload
    def getCurrencyInstance(cls, locale: java.util.Locale) -> 'NumberFormat': ...
    @classmethod
    @overload
    def getInstance(cls) -> 'NumberFormat': ...
    @classmethod
    @overload
    def getInstance(cls, locale: java.util.Locale) -> 'NumberFormat': ...
    @classmethod
    @overload
    def getIntegerInstance(cls) -> 'NumberFormat': ...
    @classmethod
    @overload
    def getIntegerInstance(cls, locale: java.util.Locale) -> 'NumberFormat': ...
    def getMaximumFractionDigits(self) -> int: ...
    def getMaximumIntegerDigits(self) -> int: ...
    def getMinimumFractionDigits(self) -> int: ...
    def getMinimumIntegerDigits(self) -> int: ...
    @classmethod
    @overload
    def getNumberInstance(cls) -> 'NumberFormat': ...
    @classmethod
    @overload
    def getNumberInstance(cls, locale: java.util.Locale) -> 'NumberFormat': ...
    @classmethod
    @overload
    def getPercentInstance(cls) -> 'NumberFormat': ...
    @classmethod
    @overload
    def getPercentInstance(cls, locale: java.util.Locale) -> 'NumberFormat': ...
    def getRoundingMode(self) -> java.math.RoundingMode: ...
    def hashCode(self) -> int: ...
    def isGroupingUsed(self) -> bool: ...
    def isParseIntegerOnly(self) -> bool: ...
    @overload
    def parse(self, string: str, parsePosition: ParsePosition) -> java.lang.Number: ...
    @overload
    def parse(self, string: str) -> java.lang.Number: ...
    @overload
    def parseObject(self, string: str, parsePosition: ParsePosition) -> _py_Any: ...
    @overload
    def parseObject(self, string: str) -> _py_Any: ...
    def setCurrency(self, currency: java.util.Currency) -> None: ...
    def setGroupingUsed(self, boolean: bool) -> None: ...
    def setMaximumFractionDigits(self, int: int) -> None: ...
    def setMaximumIntegerDigits(self, int: int) -> None: ...
    def setMinimumFractionDigits(self, int: int) -> None: ...
    def setMinimumIntegerDigits(self, int: int) -> None: ...
    def setParseIntegerOnly(self, boolean: bool) -> None: ...
    def setRoundingMode(self, roundingMode: java.math.RoundingMode) -> None: ...
    class Field(Format.Field):
        INTEGER: _py_ClassVar['NumberFormat.Field'] = ...
        FRACTION: _py_ClassVar['NumberFormat.Field'] = ...
        EXPONENT: _py_ClassVar['NumberFormat.Field'] = ...
        DECIMAL_SEPARATOR: _py_ClassVar['NumberFormat.Field'] = ...
        SIGN: _py_ClassVar['NumberFormat.Field'] = ...
        GROUPING_SEPARATOR: _py_ClassVar['NumberFormat.Field'] = ...
        EXPONENT_SYMBOL: _py_ClassVar['NumberFormat.Field'] = ...
        PERCENT: _py_ClassVar['NumberFormat.Field'] = ...
        PERMILLE: _py_ClassVar['NumberFormat.Field'] = ...
        CURRENCY: _py_ClassVar['NumberFormat.Field'] = ...
        EXPONENT_SIGN: _py_ClassVar['NumberFormat.Field'] = ...

class SimpleDateFormat(DateFormat):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, dateFormatSymbols: DateFormatSymbols): ...
    @overload
    def __init__(self, string: str, locale: java.util.Locale): ...
    def applyLocalizedPattern(self, string: str) -> None: ...
    def applyPattern(self, string: str) -> None: ...
    def clone(self) -> _py_Any: ...
    def equals(self, object: _py_Any) -> bool: ...
    @overload
    def format(self, date: java.util.Date) -> str: ...
    @overload
    def format(self, object: _py_Any) -> str: ...
    @overload
    def format(self, object: _py_Any, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    @overload
    def format(self, date: java.util.Date, stringBuffer: java.lang.StringBuffer, fieldPosition: FieldPosition) -> java.lang.StringBuffer: ...
    def formatToCharacterIterator(self, object: _py_Any) -> AttributedCharacterIterator: ...
    def get2DigitYearStart(self) -> java.util.Date: ...
    def getDateFormatSymbols(self) -> DateFormatSymbols: ...
    def hashCode(self) -> int: ...
    @overload
    def parse(self, string: str) -> java.util.Date: ...
    @overload
    def parse(self, string: str, parsePosition: ParsePosition) -> java.util.Date: ...
    def set2DigitYearStart(self, date: java.util.Date) -> None: ...
    def setDateFormatSymbols(self, dateFormatSymbols: DateFormatSymbols) -> None: ...
    def toLocalizedPattern(self) -> str: ...
    def toPattern(self) -> str: ...