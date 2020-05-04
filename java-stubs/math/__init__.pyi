from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.io
import java.lang
import java.util


class BigDecimal(java.lang.Number, java.lang.Comparable['BigDecimal']):
    ZERO: _py_ClassVar['BigDecimal'] = ...
    ONE: _py_ClassVar['BigDecimal'] = ...
    TEN: _py_ClassVar['BigDecimal'] = ...
    ROUND_UP: _py_ClassVar[int] = ...
    ROUND_DOWN: _py_ClassVar[int] = ...
    ROUND_CEILING: _py_ClassVar[int] = ...
    ROUND_FLOOR: _py_ClassVar[int] = ...
    ROUND_HALF_UP: _py_ClassVar[int] = ...
    ROUND_HALF_DOWN: _py_ClassVar[int] = ...
    ROUND_HALF_EVEN: _py_ClassVar[int] = ...
    ROUND_UNNECESSARY: _py_ClassVar[int] = ...
    @overload
    def __init__(self, int: int): ...
    @overload
    def __init__(self, bigInteger: 'BigInteger', int: int, mathContext: 'MathContext'): ...
    @overload
    def __init__(self, bigInteger: 'BigInteger', int: int): ...
    @overload
    def __init__(self, bigInteger: 'BigInteger'): ...
    @overload
    def __init__(self, bigInteger: 'BigInteger', mathContext: 'MathContext'): ...
    @overload
    def __init__(self, long: int, mathContext: 'MathContext'): ...
    @overload
    def __init__(self, long: int): ...
    @overload
    def __init__(self, int: int, mathContext: 'MathContext'): ...
    @overload
    def __init__(self, charArray: _py_List[str], mathContext: 'MathContext'): ...
    @overload
    def __init__(self, charArray: _py_List[str]): ...
    @overload
    def __init__(self, charArray: _py_List[str], int: int, int2: int, mathContext: 'MathContext'): ...
    @overload
    def __init__(self, charArray: _py_List[str], int: int, int2: int): ...
    @overload
    def __init__(self, double: float, mathContext: 'MathContext'): ...
    @overload
    def __init__(self, double: float): ...
    @overload
    def __init__(self, string: str, mathContext: 'MathContext'): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def abs(self) -> 'BigDecimal': ...
    @overload
    def abs(self, mathContext: 'MathContext') -> 'BigDecimal': ...
    @overload
    def add(self, bigDecimal: 'BigDecimal') -> 'BigDecimal': ...
    @overload
    def add(self, bigDecimal: 'BigDecimal', mathContext: 'MathContext') -> 'BigDecimal': ...
    def byteValueExact(self) -> int: ...
    @overload
    def compareTo(self, bigDecimal: 'BigDecimal') -> int: ...
    @overload
    def compareTo(self, object: _py_Any) -> int: ...
    @overload
    def divide(self, bigDecimal: 'BigDecimal', int: int, roundingMode: 'RoundingMode') -> 'BigDecimal': ...
    @overload
    def divide(self, bigDecimal: 'BigDecimal', int: int, int2: int) -> 'BigDecimal': ...
    @overload
    def divide(self, bigDecimal: 'BigDecimal') -> 'BigDecimal': ...
    @overload
    def divide(self, bigDecimal: 'BigDecimal', roundingMode: 'RoundingMode') -> 'BigDecimal': ...
    @overload
    def divide(self, bigDecimal: 'BigDecimal', int: int) -> 'BigDecimal': ...
    @overload
    def divide(self, bigDecimal: 'BigDecimal', mathContext: 'MathContext') -> 'BigDecimal': ...
    @overload
    def divideAndRemainder(self, bigDecimal: 'BigDecimal') -> _py_List['BigDecimal']: ...
    @overload
    def divideAndRemainder(self, bigDecimal: 'BigDecimal', mathContext: 'MathContext') -> _py_List['BigDecimal']: ...
    @overload
    def divideToIntegralValue(self, bigDecimal: 'BigDecimal') -> 'BigDecimal': ...
    @overload
    def divideToIntegralValue(self, bigDecimal: 'BigDecimal', mathContext: 'MathContext') -> 'BigDecimal': ...
    def doubleValue(self) -> float: ...
    def equals(self, object: _py_Any) -> bool: ...
    def floatValue(self) -> float: ...
    def hashCode(self) -> int: ...
    def intValue(self) -> int: ...
    def intValueExact(self) -> int: ...
    def longValue(self) -> int: ...
    def longValueExact(self) -> int: ...
    def max(self, bigDecimal: 'BigDecimal') -> 'BigDecimal': ...
    def min(self, bigDecimal: 'BigDecimal') -> 'BigDecimal': ...
    def movePointLeft(self, int: int) -> 'BigDecimal': ...
    def movePointRight(self, int: int) -> 'BigDecimal': ...
    @overload
    def multiply(self, bigDecimal: 'BigDecimal') -> 'BigDecimal': ...
    @overload
    def multiply(self, bigDecimal: 'BigDecimal', mathContext: 'MathContext') -> 'BigDecimal': ...
    @overload
    def negate(self) -> 'BigDecimal': ...
    @overload
    def negate(self, mathContext: 'MathContext') -> 'BigDecimal': ...
    @overload
    def plus(self, mathContext: 'MathContext') -> 'BigDecimal': ...
    @overload
    def plus(self) -> 'BigDecimal': ...
    @overload
    def pow(self, int: int, mathContext: 'MathContext') -> 'BigDecimal': ...
    @overload
    def pow(self, int: int) -> 'BigDecimal': ...
    def precision(self) -> int: ...
    @overload
    def remainder(self, bigDecimal: 'BigDecimal') -> 'BigDecimal': ...
    @overload
    def remainder(self, bigDecimal: 'BigDecimal', mathContext: 'MathContext') -> 'BigDecimal': ...
    def round(self, mathContext: 'MathContext') -> 'BigDecimal': ...
    def scale(self) -> int: ...
    def scaleByPowerOfTen(self, int: int) -> 'BigDecimal': ...
    @overload
    def setScale(self, int: int) -> 'BigDecimal': ...
    @overload
    def setScale(self, int: int, roundingMode: 'RoundingMode') -> 'BigDecimal': ...
    @overload
    def setScale(self, int: int, int2: int) -> 'BigDecimal': ...
    def shortValueExact(self) -> int: ...
    def signum(self) -> int: ...
    def stripTrailingZeros(self) -> 'BigDecimal': ...
    @overload
    def subtract(self, bigDecimal: 'BigDecimal') -> 'BigDecimal': ...
    @overload
    def subtract(self, bigDecimal: 'BigDecimal', mathContext: 'MathContext') -> 'BigDecimal': ...
    def toBigInteger(self) -> 'BigInteger': ...
    def toBigIntegerExact(self) -> 'BigInteger': ...
    def toEngineeringString(self) -> str: ...
    def toPlainString(self) -> str: ...
    def toString(self) -> str: ...
    def ulp(self) -> 'BigDecimal': ...
    def unscaledValue(self) -> 'BigInteger': ...
    @classmethod
    @overload
    def valueOf(cls, long: int) -> 'BigDecimal': ...
    @classmethod
    @overload
    def valueOf(cls, double: float) -> 'BigDecimal': ...
    @classmethod
    @overload
    def valueOf(cls, long: int, int: int) -> 'BigDecimal': ...

class BigInteger(java.lang.Number, java.lang.Comparable['BigInteger']):
    ZERO: _py_ClassVar['BigInteger'] = ...
    ONE: _py_ClassVar['BigInteger'] = ...
    TEN: _py_ClassVar['BigInteger'] = ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, int: int, random: java.util.Random): ...
    @overload
    def __init__(self, int: int, int2: int, random: java.util.Random): ...
    @overload
    def __init__(self, byteArray: _py_List[int]): ...
    @overload
    def __init__(self, int: int, byteArray: _py_List[int]): ...
    @overload
    def __init__(self, string: str, int: int): ...
    def abs(self) -> 'BigInteger': ...
    def add(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def andNot(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def bitCount(self) -> int: ...
    def bitLength(self) -> int: ...
    def byteValueExact(self) -> int: ...
    def clearBit(self, int: int) -> 'BigInteger': ...
    @overload
    def compareTo(self, object: _py_Any) -> int: ...
    @overload
    def compareTo(self, bigInteger: 'BigInteger') -> int: ...
    def divide(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def divideAndRemainder(self, bigInteger: 'BigInteger') -> _py_List['BigInteger']: ...
    def doubleValue(self) -> float: ...
    def equals(self, object: _py_Any) -> bool: ...
    def flipBit(self, int: int) -> 'BigInteger': ...
    def floatValue(self) -> float: ...
    def gcd(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def getLowestSetBit(self) -> int: ...
    def hashCode(self) -> int: ...
    def intValue(self) -> int: ...
    def intValueExact(self) -> int: ...
    def isProbablePrime(self, int: int) -> bool: ...
    def longValue(self) -> int: ...
    def longValueExact(self) -> int: ...
    def max(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def min(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def mod(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def modInverse(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def modPow(self, bigInteger: 'BigInteger', bigInteger2: 'BigInteger') -> 'BigInteger': ...
    def multiply(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def negate(self) -> 'BigInteger': ...
    def nextProbablePrime(self) -> 'BigInteger': ...
    def pow(self, int: int) -> 'BigInteger': ...
    @classmethod
    def probablePrime(cls, int: int, random: java.util.Random) -> 'BigInteger': ...
    def remainder(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def setBit(self, int: int) -> 'BigInteger': ...
    def shiftLeft(self, int: int) -> 'BigInteger': ...
    def shiftRight(self, int: int) -> 'BigInteger': ...
    def shortValueExact(self) -> int: ...
    def signum(self) -> int: ...
    def subtract(self, bigInteger: 'BigInteger') -> 'BigInteger': ...
    def testBit(self, int: int) -> bool: ...
    def toByteArray(self) -> _py_List[int]: ...
    @overload
    def toString(self) -> str: ...
    @overload
    def toString(self, int: int) -> str: ...
    @classmethod
    def valueOf(cls, long: int) -> 'BigInteger': ...
    def xor(self, bigInteger: 'BigInteger') -> 'BigInteger': ...

class BitSieve: ...

class MathContext(java.io.Serializable):
    UNLIMITED: _py_ClassVar['MathContext'] = ...
    DECIMAL32: _py_ClassVar['MathContext'] = ...
    DECIMAL64: _py_ClassVar['MathContext'] = ...
    DECIMAL128: _py_ClassVar['MathContext'] = ...
    @overload
    def __init__(self, int: int): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, int: int, roundingMode: 'RoundingMode'): ...
    def equals(self, object: _py_Any) -> bool: ...
    def getPrecision(self) -> int: ...
    def getRoundingMode(self) -> 'RoundingMode': ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class MutableBigInteger:
    def toString(self) -> str: ...

class RoundingMode(java.lang.Enum['RoundingMode']):
    UP: _py_ClassVar['RoundingMode'] = ...
    DOWN: _py_ClassVar['RoundingMode'] = ...
    CEILING: _py_ClassVar['RoundingMode'] = ...
    FLOOR: _py_ClassVar['RoundingMode'] = ...
    HALF_UP: _py_ClassVar['RoundingMode'] = ...
    HALF_DOWN: _py_ClassVar['RoundingMode'] = ...
    HALF_EVEN: _py_ClassVar['RoundingMode'] = ...
    UNNECESSARY: _py_ClassVar['RoundingMode'] = ...
    @classmethod
    @overload
    def valueOf(cls, int: int) -> 'RoundingMode': ...
    @classmethod
    @overload
    def valueOf(cls, string: str) -> 'RoundingMode': ...
    _valueOf_2__T = _py_TypeVar('_valueOf_2__T', bound=java.lang.Enum)  # <T>
    @classmethod
    @overload
    def valueOf(cls, class_: _py_Type[_valueOf_2__T], string: str) -> _valueOf_2__T: ...
    @classmethod
    def values(cls) -> _py_List['RoundingMode']: ...

class SignedMutableBigInteger(MutableBigInteger):
    def toString(self) -> str: ...
