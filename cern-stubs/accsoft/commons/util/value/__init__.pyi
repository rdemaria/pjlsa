import com.google.common.collect
import java.io
import java.lang
import java.util.function
import typing



_Either__L = typing.TypeVar('_Either__L')  # <L>
_Either__R = typing.TypeVar('_Either__R')  # <R>
class Either(typing.Generic[_Either__L, _Either__R]):
    """
    Java class 'cern.accsoft.commons.util.value.Either'
    
    """
    def accept(self, consumer: typing.Union[java.util.function.Consumer[_Either__L], typing.Callable[[_Either__L], None]], consumer2: typing.Union[java.util.function.Consumer[_Either__R], typing.Callable[[_Either__R], None]]) -> None: ...
    _bimap__LM = typing.TypeVar('_bimap__LM')  # <LM>
    _bimap__RM = typing.TypeVar('_bimap__RM')  # <RM>
    def bimap(self, function: typing.Union[java.util.function.Function[_Either__L, _bimap__LM], typing.Callable[[_Either__L], _bimap__LM]], function2: typing.Union[java.util.function.Function[_Either__R, _bimap__RM], typing.Callable[[_Either__R], _bimap__RM]]) -> 'Either'[_bimap__LM, _bimap__RM]: ...
    _either__L = typing.TypeVar('_either__L')  # <L>
    _either__R = typing.TypeVar('_either__R')  # <R>
    @staticmethod
    def either(l: _either__L, r: _either__R) -> 'Either'[_either__L, _either__R]: ...
    _fold__T = typing.TypeVar('_fold__T')  # <T>
    def fold(self, function: typing.Union[java.util.function.Function[_Either__L, _fold__T], typing.Callable[[_Either__L], _fold__T]], function2: typing.Union[java.util.function.Function[_Either__R, _fold__T], typing.Callable[[_Either__R], _fold__T]]) -> _fold__T: ...
    def ifLeft(self, consumer: typing.Union[java.util.function.Consumer[_Either__L], typing.Callable[[_Either__L], None]]) -> None: ...
    def ifRight(self, consumer: typing.Union[java.util.function.Consumer[_Either__R], typing.Callable[[_Either__R], None]]) -> None: ...
    def isLeft(self) -> bool: ...
    def isRight(self) -> bool: ...
    _left_1__L = typing.TypeVar('_left_1__L')  # <L>
    _left_1__R = typing.TypeVar('_left_1__R')  # <R>
    @typing.overload
    def left(self) -> _Either__L: ...
    @typing.overload
    @staticmethod
    def left(l: _left_1__L) -> 'Either'[_left_1__L, _left_1__R]: ...
    def leftOrElse(self, l: _Either__L) -> _Either__L: ...
    def leftOrElseGet(self, supplier: typing.Union[java.util.function.Supplier[_Either__L], typing.Callable[[], _Either__L]]) -> _Either__L: ...
    @typing.overload
    def leftOrThrow(self, exception: java.lang.Exception) -> _Either__L: ...
    @typing.overload
    def leftOrThrow(self, supplier: typing.Union[java.util.function.Supplier[java.lang.Exception], typing.Callable[[], java.lang.Exception]]) -> _Either__L: ...
    _mapLeft__LM = typing.TypeVar('_mapLeft__LM')  # <LM>
    def mapLeft(self, function: typing.Union[java.util.function.Function[_Either__L, _mapLeft__LM], typing.Callable[[_Either__L], _mapLeft__LM]]) -> 'Either'[_mapLeft__LM, _Either__R]: ...
    _mapRight__RM = typing.TypeVar('_mapRight__RM')  # <RM>
    def mapRight(self, function: typing.Union[java.util.function.Function[_Either__R, _mapRight__RM], typing.Callable[[_Either__R], _mapRight__RM]]) -> 'Either'[_Either__L, _mapRight__RM]: ...
    _right_1__L = typing.TypeVar('_right_1__L')  # <L>
    _right_1__R = typing.TypeVar('_right_1__R')  # <R>
    @typing.overload
    def right(self) -> _Either__R: ...
    @typing.overload
    @staticmethod
    def right(r: _right_1__R) -> 'Either'[_right_1__L, _right_1__R]: ...
    def rightOrElse(self, r: _Either__R) -> _Either__R: ...
    def rightOrElseGet(self, supplier: typing.Union[java.util.function.Supplier[_Either__R], typing.Callable[[], _Either__R]]) -> _Either__R: ...
    @typing.overload
    def rightOrThrow(self, exception: java.lang.Exception) -> _Either__R: ...
    @typing.overload
    def rightOrThrow(self, supplier: typing.Union[java.util.function.Supplier[java.lang.Exception], typing.Callable[[], java.lang.Exception]]) -> _Either__R: ...
    def swap(self) -> 'Either'[_Either__R, _Either__L]: ...

_FailSafe__E = typing.TypeVar('_FailSafe__E', bound=java.lang.Exception)  # <E>
_FailSafe__T = typing.TypeVar('_FailSafe__T')  # <T>
class FailSafe(typing.Generic[_FailSafe__E, _FailSafe__T]):
    """
    Java class 'cern.accsoft.commons.util.value.FailSafe'
    
    """
    def accept(self, consumer: typing.Union[java.util.function.Consumer[_FailSafe__E], typing.Callable[[_FailSafe__E], None]], consumer2: typing.Union[java.util.function.Consumer[_FailSafe__T], typing.Callable[[_FailSafe__T], None]]) -> None: ...
    def exception(self) -> _FailSafe__E: ...
    _flatMap__NE = typing.TypeVar('_flatMap__NE', bound=java.lang.Exception)  # <NE>
    _flatMap__U = typing.TypeVar('_flatMap__U')  # <U>
    def flatMap(self, function: typing.Union[java.util.function.Function[_FailSafe__T, 'FailSafe'[_flatMap__NE, _flatMap__U]], typing.Callable[[_FailSafe__T], 'FailSafe'[_flatMap__NE, _flatMap__U]]]) -> 'FailSafe'[_FailSafe__E, _flatMap__U]: ...
    _fold__V = typing.TypeVar('_fold__V')  # <V>
    def fold(self, function: typing.Union[java.util.function.Function[_FailSafe__E, _fold__V], typing.Callable[[_FailSafe__E], _fold__V]], function2: typing.Union[java.util.function.Function[_FailSafe__T, _fold__V], typing.Callable[[_FailSafe__T], _fold__V]]) -> _fold__V: ...
    def ifValuePresent(self, consumer: typing.Union[java.util.function.Consumer[_FailSafe__T], typing.Callable[[_FailSafe__T], None]]) -> None: ...
    def isEmpty(self) -> bool: ...
    def isException(self) -> bool: ...
    def isValue(self) -> bool: ...
    _map__U = typing.TypeVar('_map__U')  # <U>
    def map(self, function: typing.Union[java.util.function.Function[_FailSafe__T, _map__U], typing.Callable[[_FailSafe__T], _map__U]]) -> 'FailSafe'[_FailSafe__E, _map__U]: ...
    _of_0__E = typing.TypeVar('_of_0__E', bound=java.lang.Exception)  # <E>
    _of_0__T = typing.TypeVar('_of_0__T')  # <T>
    _of_1__E = typing.TypeVar('_of_1__E', bound=java.lang.Exception)  # <E>
    _of_1__T = typing.TypeVar('_of_1__T')  # <T>
    @typing.overload
    @staticmethod
    def of(e: _of_0__E) -> 'FailSafe'[_of_0__E, _of_0__T]: ...
    @typing.overload
    @staticmethod
    def of(t: _of_1__T) -> 'FailSafe'[_of_1__E, _of_1__T]: ...
    def orElse(self, t: _FailSafe__T) -> _FailSafe__T: ...
    def orElseGet(self, supplier: typing.Union[java.util.function.Supplier[_FailSafe__T], typing.Callable[[], _FailSafe__T]]) -> _FailSafe__T: ...
    @typing.overload
    def orElseThrow(self) -> _FailSafe__T: ...
    @typing.overload
    def orElseThrow(self, exception: java.lang.Exception) -> _FailSafe__T: ...
    @typing.overload
    def orElseThrow(self, supplier: typing.Union[java.util.function.Supplier[java.lang.Exception], typing.Callable[[], java.lang.Exception]]) -> _FailSafe__T: ...
    def value(self) -> _FailSafe__T: ...

_FailSafeValue__V = typing.TypeVar('_FailSafeValue__V')  # <V>
class FailSafeValue(typing.Generic[_FailSafeValue__V]):
    """
    Java class 'cern.accsoft.commons.util.value.FailSafeValue'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * FailSafeValue(java.lang.Object)
        * FailSafeValue(java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, v: _FailSafeValue__V): ...
    def containsException(self) -> bool: ...
    def containsValue(self) -> bool: ...
    _emptyValue__V = typing.TypeVar('_emptyValue__V')  # <V>
    @staticmethod
    def emptyValue() -> 'FailSafeValue'[_emptyValue__V]: ...
    def getException(self) -> java.lang.Exception: ...
    def getValue(self) -> _FailSafeValue__V: ...
    def isEmpty(self) -> bool: ...
    def toString(self) -> str: ...

_Pair__E = typing.TypeVar('_Pair__E')  # <E>
_Pair__T = typing.TypeVar('_Pair__T')  # <T>
class Pair(java.io.Serializable, typing.Generic[_Pair__E, _Pair__T]):
    """
    Java class 'cern.accsoft.commons.util.value.Pair'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * Pair(java.lang.Object, java.lang.Object)
    
    """
    def __init__(self, e: _Pair__E, t: _Pair__T): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getFirst(self) -> _Pair__E: ...
    def getSecond(self) -> _Pair__T: ...
    def hashCode(self) -> int: ...
    _newInstance__R = typing.TypeVar('_newInstance__R')  # <R>
    _newInstance__S = typing.TypeVar('_newInstance__S')  # <S>
    @staticmethod
    def newInstance(r: _newInstance__R, s: _newInstance__S) -> 'Pair'[_newInstance__R, _newInstance__S]: ...
    def toString(self) -> str: ...

class Ranges:
    """
    Java class 'cern.accsoft.commons.util.value.Ranges'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Ranges()
    
    """
    def __init__(self): ...
    class DoubleRanges:
        """
        Java class 'cern.accsoft.commons.util.value.Ranges$DoubleRanges'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * DoubleRanges()
        
          Attributes:
            EMPTY_RANGE (com.google.common.collect.Range): final static field
        
        """
        EMPTY_RANGE: typing.ClassVar[com.google.common.collect.Range] = ...
        def __init__(self): ...
        @staticmethod
        def contains(range: com.google.common.collect.Range[float], double: float) -> bool: ...
        @staticmethod
        def getCenter(range: com.google.common.collect.Range[float]) -> float: ...
        @staticmethod
        def getLength(range: com.google.common.collect.Range[float]) -> float: ...
    class LongRanges:
        """
        Java class 'cern.accsoft.commons.util.value.Ranges$LongRanges'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * LongRanges()
        
        """
        def __init__(self): ...
        @staticmethod
        def contains(range: com.google.common.collect.Range[int], long: int) -> bool: ...
        @staticmethod
        def getCenter(range: com.google.common.collect.Range[int]) -> float: ...
        @staticmethod
        def getLength(range: com.google.common.collect.Range[int]) -> int: ...

_FailSafeImpl__E = typing.TypeVar('_FailSafeImpl__E', bound=java.lang.Exception)  # <E>
_FailSafeImpl__T = typing.TypeVar('_FailSafeImpl__T')  # <T>
class FailSafeImpl(FailSafe[_FailSafeImpl__E, _FailSafeImpl__T], typing.Generic[_FailSafeImpl__E, _FailSafeImpl__T]):
    """
    Java class 'cern.accsoft.commons.util.value.FailSafeImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.value.FailSafe
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def exception(self) -> _FailSafeImpl__E: ...
    def hashCode(self) -> int: ...
    def isValue(self) -> bool: ...
    def toString(self) -> str: ...
    def value(self) -> _FailSafeImpl__T: ...

_Left__L = typing.TypeVar('_Left__L')  # <L>
_Left__R = typing.TypeVar('_Left__R')  # <R>
class Left(Either[_Left__L, _Left__R], typing.Generic[_Left__L, _Left__R]):
    """
    Java class 'cern.accsoft.commons.util.value.Left'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.value.Either
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def isRight(self) -> bool: ...
    def left(self) -> _Left__L: ...
    def right(self) -> _Left__R: ...
    def toString(self) -> str: ...

_Right__L = typing.TypeVar('_Right__L')  # <L>
_Right__R = typing.TypeVar('_Right__R')  # <R>
class Right(Either[_Right__L, _Right__R], typing.Generic[_Right__L, _Right__R]):
    """
    Java class 'cern.accsoft.commons.util.value.Right'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.value.Either
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def isRight(self) -> bool: ...
    def left(self) -> _Right__L: ...
    def right(self) -> _Right__R: ...
    def toString(self) -> str: ...

_SerializablePair__E = typing.TypeVar('_SerializablePair__E', bound=java.io.Serializable)  # <E>
_SerializablePair__T = typing.TypeVar('_SerializablePair__T', bound=java.io.Serializable)  # <T>
class SerializablePair(Pair[_SerializablePair__E, _SerializablePair__T], java.io.Serializable, typing.Generic[_SerializablePair__E, _SerializablePair__T]):
    """
    Java class 'cern.accsoft.commons.util.value.SerializablePair'
    
        Extends:
            cern.accsoft.commons.util.value.Pair
    
        Interfaces:
            java.io.Serializable
    
    """
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    _newInstance_0__R = typing.TypeVar('_newInstance_0__R')  # <R>
    _newInstance_0__S = typing.TypeVar('_newInstance_0__S')  # <S>
    _newInstance_1__R = typing.TypeVar('_newInstance_1__R', bound=java.io.Serializable)  # <R>
    _newInstance_1__S = typing.TypeVar('_newInstance_1__S', bound=java.io.Serializable)  # <S>
    @typing.overload
    @staticmethod
    def newInstance(r: _newInstance_0__R, s: _newInstance_0__S) -> Pair[_newInstance_0__R, _newInstance_0__S]: ...
    @typing.overload
    @staticmethod
    def newInstance(r: _newInstance_1__R, s: _newInstance_1__S) -> 'SerializablePair'[_newInstance_1__R, _newInstance_1__S]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.value")``.

    Either: typing.Type[Either]
    FailSafe: typing.Type[FailSafe]
    FailSafeImpl: typing.Type[FailSafeImpl]
    FailSafeValue: typing.Type[FailSafeValue]
    Left: typing.Type[Left]
    Pair: typing.Type[Pair]
    Ranges: typing.Type[Ranges]
    Right: typing.Type[Right]
    SerializablePair: typing.Type[SerializablePair]
