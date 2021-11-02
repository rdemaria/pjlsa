import com.google.common.collect
import java.io
import java.lang
import java.util.function
import typing



_Either__L = typing.TypeVar('_Either__L')  # <L>
_Either__R = typing.TypeVar('_Either__R')  # <R>
class Either(typing.Generic[_Either__L, _Either__R]):
    """
    public interface Either<L, R>
    
        Inspired by Haskell's either type, contains either L or R type. Values cannot be null. The convention is to use the left
        for errors, and right for values.
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
    public interface FailSafe<E extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`, T>
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
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class FailSafeValue<V> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Deprecated.
        Please use the :class:`~cern.accsoft.commons.util.value.FailSafe` type, please note that
        :class:`~cern.accsoft.commons.util.value.FailSafe` no longer accept null values.
        Value holder which can contain either a value or an exception.
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, v: _FailSafeValue__V): ...
    def containsException(self) -> bool:
        """
            Deprecated.
        
            Returns:
                :code:`true` if the :class:`~cern.accsoft.commons.util.value.FailSafeValue` contains an exception
        
        
        """
        ...
    def containsValue(self) -> bool:
        """
            Deprecated.
        
            Returns:
                :code:`true` if the :class:`~cern.accsoft.commons.util.value.FailSafeValue` contains a value
        
        
        """
        ...
    _emptyValue__V = typing.TypeVar('_emptyValue__V')  # <V>
    @staticmethod
    def emptyValue() -> 'FailSafeValue'[_emptyValue__V]: ...
    def getException(self) -> java.lang.Exception:
        """
            Deprecated.
        
            Returns:
                the exception
        
        
        """
        ...
    def getValue(self) -> _FailSafeValue__V:
        """
            Deprecated.
        
            Returns:
                the value
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Deprecated.
        
            Returns:
                :code:`true` if the :class:`~cern.accsoft.commons.util.value.FailSafeValue` contains neither value nor exception.
        
        
        """
        ...
    def toString(self) -> str:
        """
            Deprecated.
        
            Overrides:
                 in class 
        
        
        """
        ...

_Pair__E = typing.TypeVar('_Pair__E')  # <E>
_Pair__T = typing.TypeVar('_Pair__T')  # <T>
class Pair(java.io.Serializable, typing.Generic[_Pair__E, _Pair__T]):
    """
    public class Pair<E, T> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This generic class :code:`Pair<E, T>` reflects a pair of two objects of type :code:`<E>` and :code:`<T>`. Instances of
        this class are immutable.
    
    
        The class can be used, for instance, when in a map the key value needs to be a pair of two objects or when a method
        needs to return two different objects. Because of this purpose the
        :meth:`~cern.accsoft.commons.util.value.Pair.hashCode` and :meth:`~cern.accsoft.commons.util.value.Pair.equals` methods
        have been implemented and the classes of the objects that are used in the pair also must implement these methods. TODO:
        Greg: Consider if we need here newInstance(..) method or rather we should use directly constructor..
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, e: _Pair__E, t: _Pair__T): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getFirst(self) -> _Pair__E:
        """
            Returns the first part of the pair.
        
            Returns:
                the first.
        
        
        """
        ...
    def getSecond(self) -> _Pair__T:
        """
            Return the second part of the pair.
        
            Returns:
                the second.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    _newInstance__R = typing.TypeVar('_newInstance__R')  # <R>
    _newInstance__S = typing.TypeVar('_newInstance__S')  # <S>
    @staticmethod
    def newInstance(r: _newInstance__R, s: _newInstance__S) -> 'Pair'[_newInstance__R, _newInstance__S]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class Ranges:
    """
    public class Ranges extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Operations on :code:`Range`'s.
    """
    def __init__(self): ...
    class DoubleRanges:
        EMPTY_RANGE: typing.ClassVar[com.google.common.collect.Range] = ...
        def __init__(self): ...
        @staticmethod
        def contains(range: com.google.common.collect.Range[float], double: float) -> bool: ...
        @staticmethod
        def getCenter(range: com.google.common.collect.Range[float]) -> float: ...
        @staticmethod
        def getLength(range: com.google.common.collect.Range[float]) -> float: ...
    class LongRanges:
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
    public class FailSafeImpl<E extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`, T> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.value.FailSafe`<E, T>
    
        This class is designed for inheritance, you can extend it to build your own
        :class:`~cern.accsoft.commons.util.value.FailSafe` type.
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def exception(self) -> _FailSafeImpl__E:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.value.FailSafe.exception`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.value.FailSafe`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isValue(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.value.FailSafe.isValue`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.value.FailSafe`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def value(self) -> _FailSafeImpl__T:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.value.FailSafe.value` in interface :class:`~cern.accsoft.commons.util.value.FailSafe`
        
        
        """
        ...

_Left__L = typing.TypeVar('_Left__L')  # <L>
_Left__R = typing.TypeVar('_Left__R')  # <R>
class Left(Either[_Left__L, _Left__R], typing.Generic[_Left__L, _Left__R]):
    """
    public class Left<L, R> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.value.Either`<L, R>
    
    
        Also see:
            :class:`~cern.accsoft.commons.util.value.Either`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isRight(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.value.Either.isRight` in interface :class:`~cern.accsoft.commons.util.value.Either`
        
        
        """
        ...
    def left(self) -> _Left__L: ...
    def right(self) -> _Left__R: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_Right__L = typing.TypeVar('_Right__L')  # <L>
_Right__R = typing.TypeVar('_Right__R')  # <R>
class Right(Either[_Right__L, _Right__R], typing.Generic[_Right__L, _Right__R]):
    """
    public class Right<L, R> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.value.Either`<L, R>
    
    
        Also see:
            :class:`~cern.accsoft.commons.util.value.Either`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isRight(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.value.Either.isRight` in interface :class:`~cern.accsoft.commons.util.value.Either`
        
        
        """
        ...
    def left(self) -> _Right__L: ...
    def right(self) -> _Right__R: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_SerializablePair__E = typing.TypeVar('_SerializablePair__E', bound=java.io.Serializable)  # <E>
_SerializablePair__T = typing.TypeVar('_SerializablePair__T', bound=java.io.Serializable)  # <T>
class SerializablePair(Pair[_SerializablePair__E, _SerializablePair__T], java.io.Serializable, typing.Generic[_SerializablePair__E, _SerializablePair__T]):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class SerializablePair<E extends `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, T extends `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`> extends :class:`~cern.accsoft.commons.util.value.Pair`<E, T> implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use :class:`~cern.accsoft.commons.util.value.Pair` class instead. It has been made :code:`Serializable`
        Serializable version of cern.accsoft.commons.util.value.Pair .
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def main(stringArray: typing.List[str]) -> None:
        """
            Deprecated.
            The main method is for testing purpose and contains examples.
        
            Parameters:
                args (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the command line arguments to pass.
        
        
        """
        ...
    _newInstance_0__R = typing.TypeVar('_newInstance_0__R')  # <R>
    _newInstance_0__S = typing.TypeVar('_newInstance_0__S')  # <S>
    _newInstance_1__R = typing.TypeVar('_newInstance_1__R', bound=java.io.Serializable)  # <R>
    _newInstance_1__S = typing.TypeVar('_newInstance_1__S', bound=java.io.Serializable)  # <S>
    @typing.overload
    @staticmethod
    def newInstance(r: _newInstance_0__R, s: _newInstance_0__S) -> Pair[_newInstance_0__R, _newInstance_0__S]:
        """
            Deprecated.
            Convenience method to be able to instantiate this class easily:
        
        
            :code:`SerializablePair<String, Integer> stringIntPair = SerializablePair.newInstance(first, second);`
        
            Parameters:
                first (R): the first part of the pair
                second (S): the second part of the pair
        
            Returns:
                a new instance of this class.
        
        
        """
        ...
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
