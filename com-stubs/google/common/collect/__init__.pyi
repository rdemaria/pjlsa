import com
import com.google.common.base
import java.io
import java.lang
import java.math
import java.time
import java.util
import java.util.concurrent
import java.util.concurrent.atomic
import java.util.function
import java.util.stream
import typing



_BiMap__K = typing.TypeVar('_BiMap__K')  # <K>
_BiMap__V = typing.TypeVar('_BiMap__V')  # <V>
class BiMap(java.util.Map[_BiMap__K, _BiMap__V], typing.Generic[_BiMap__K, _BiMap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<K,V> extends Map<K,V>
    
        A bimap (or "bidirectional map") is a map that preserves the uniqueness of its values as well as that of its keys. This
        constraint enables bimaps to support an "inverse view", which is another bimap containing the same entries as this bimap
        but with reversed keys and values.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    def equals(self, object: typing.Any) -> bool: ...
    def forcePut(self, k: _BiMap__K, v: _BiMap__V) -> _BiMap__V: ...
    def hashCode(self) -> int: ...
    def inverse(self) -> 'BiMap'[_BiMap__V, _BiMap__K]: ...
    def put(self, k: _BiMap__K, v: _BiMap__V) -> _BiMap__V: ...
    def putAll(self, map: typing.Union[java.util.Map[_BiMap__K, _BiMap__V], typing.Mapping[_BiMap__K, _BiMap__V]]) -> None: ...
    def values(self) -> java.util.Set[_BiMap__V]: ...

class BoundType(java.lang.Enum['BoundType']):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public enum :meth:`~src` extends Enum<:class:`~com.google.common.collect.BoundType`>
    
        Indicates whether an endpoint of some range is contained in the range itself ("closed") or not ("open"). If a range is
        unbounded on a side, it is neither open nor closed on that side; the bound simply does not exist.
    
        Since:
            10.0
    """
    OPEN: typing.ClassVar['BoundType'] = ...
    CLOSED: typing.ClassVar['BoundType'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'BoundType': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['BoundType']: ...

_ClassToInstanceMap__B = typing.TypeVar('_ClassToInstanceMap__B')  # <B>
class ClassToInstanceMap(java.util.Map[typing.Type[_ClassToInstanceMap__B], _ClassToInstanceMap__B], typing.Generic[_ClassToInstanceMap__B]):
    """
    @DoNotMock(value="Use ImmutableClassToInstanceMap or MutableClassToInstanceMap") :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<B> extends Map<Class<? extends B>,B>
    
        A map, each entry of which maps a Java `raw type <http://tinyurl.com/2cmwkz>` to an instance of that type. In addition
        to implementing :code:`Map`, the additional type-safe operations
        :meth:`~com.google.common.collect.ClassToInstanceMap.putInstance` and
        :meth:`~com.google.common.collect.ClassToInstanceMap.getInstance` are available.
    
        Like any other :code:`Map<Class, Object>`, this map may contain entries for primitive types, and a primitive type and
        its corresponding wrapper type may map to different values.
    
        See the Guava User Guide article on null.
    
        To map a generic type to an instance of that type, use :class:`~com.google.common.reflect.TypeToInstanceMap` instead.
    
        Since:
            2.0
    """
    def equals(self, object: typing.Any) -> bool: ...
    _getInstance__T = typing.TypeVar('_getInstance__T')  # <T>
    def getInstance(self, class_: typing.Type[_getInstance__T]) -> _getInstance__T: ...
    def hashCode(self) -> int: ...
    _putInstance__T = typing.TypeVar('_putInstance__T')  # <T>
    def putInstance(self, class_: typing.Type[_putInstance__T], t: _putInstance__T) -> _putInstance__T: ...

class Collections2:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Provides static methods for working with :code:`Collection` instances.
    
        **Java 8 users:** several common uses for this class are now more comprehensively addressed by the new null library.
        Read the method documentation below for comparisons. These methods are not being deprecated, but we gently encourage you
        to migrate to streams.
    
        Since:
            2.0
    """
    _filter__E = typing.TypeVar('_filter__E')  # <E>
    @staticmethod
    def filter(collection: typing.Union[java.util.Collection[_filter__E], typing.Sequence[_filter__E]], predicate: typing.Union[com.google.common.base.Predicate[_filter__E], typing.Callable[[_filter__E], bool]]) -> java.util.Collection[_filter__E]: ...
    _orderedPermutations_0__E = typing.TypeVar('_orderedPermutations_0__E', bound=java.lang.Comparable)  # <E>
    _orderedPermutations_1__E = typing.TypeVar('_orderedPermutations_1__E')  # <E>
    @typing.overload
    @staticmethod
    def orderedPermutations(iterable: java.lang.Iterable[_orderedPermutations_0__E]) -> java.util.Collection[java.util.List[_orderedPermutations_0__E]]: ...
    @typing.overload
    @staticmethod
    def orderedPermutations(iterable: java.lang.Iterable[_orderedPermutations_1__E], comparator: typing.Union[java.util.Comparator[_orderedPermutations_1__E], typing.Callable[[_orderedPermutations_1__E, _orderedPermutations_1__E], int]]) -> java.util.Collection[java.util.List[_orderedPermutations_1__E]]: ...
    _permutations__E = typing.TypeVar('_permutations__E')  # <E>
    @staticmethod
    def permutations(collection: typing.Union[java.util.Collection[_permutations__E], typing.Sequence[_permutations__E]]) -> java.util.Collection[java.util.List[_permutations__E]]: ...
    _transform__F = typing.TypeVar('_transform__F')  # <F>
    _transform__T = typing.TypeVar('_transform__T')  # <T>
    @staticmethod
    def transform(collection: typing.Union[java.util.Collection[_transform__F], typing.Sequence[_transform__F]], function: typing.Union[com.google.common.base.Function[_transform__F, _transform__T], typing.Callable[[_transform__F], _transform__T]]) -> java.util.Collection[_transform__T]: ...

class Comparators:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Provides static methods for working with null instances. For many other helpful comparator utilities, see either
        :code:`Comparator` itself (for Java 8 or later), or :code:`com.google.common.collect.Ordering` (otherwise).
    
        Relationship to :code:`Ordering`
    --------------------------------
    
    
        In light of the significant enhancements to :code:`Comparator` in Java 8, the overwhelming majority of usages of
        :code:`Ordering` can be written using only built-in JDK APIs. This class is intended to "fill the gap" and provide those
        features of :code:`Ordering` not already provided by the JDK.
    
        Since:
            21.0
    """
    _emptiesFirst__T = typing.TypeVar('_emptiesFirst__T')  # <T>
    @staticmethod
    def emptiesFirst(comparator: typing.Union[java.util.Comparator[_emptiesFirst__T], typing.Callable[[_emptiesFirst__T, _emptiesFirst__T], int]]) -> java.util.Comparator[java.util.Optional[_emptiesFirst__T]]: ...
    _emptiesLast__T = typing.TypeVar('_emptiesLast__T')  # <T>
    @staticmethod
    def emptiesLast(comparator: typing.Union[java.util.Comparator[_emptiesLast__T], typing.Callable[[_emptiesLast__T, _emptiesLast__T], int]]) -> java.util.Comparator[java.util.Optional[_emptiesLast__T]]: ...
    _greatest__T = typing.TypeVar('_greatest__T')  # <T>
    @staticmethod
    def greatest(int: int, comparator: typing.Union[java.util.Comparator[_greatest__T], typing.Callable[[_greatest__T, _greatest__T], int]]) -> java.util.stream.Collector[_greatest__T, typing.Any, java.util.List[_greatest__T]]: ...
    _isInOrder__T = typing.TypeVar('_isInOrder__T')  # <T>
    @staticmethod
    def isInOrder(iterable: java.lang.Iterable[_isInOrder__T], comparator: typing.Union[java.util.Comparator[_isInOrder__T], typing.Callable[[_isInOrder__T, _isInOrder__T], int]]) -> bool: ...
    _isInStrictOrder__T = typing.TypeVar('_isInStrictOrder__T')  # <T>
    @staticmethod
    def isInStrictOrder(iterable: java.lang.Iterable[_isInStrictOrder__T], comparator: typing.Union[java.util.Comparator[_isInStrictOrder__T], typing.Callable[[_isInStrictOrder__T, _isInStrictOrder__T], int]]) -> bool: ...
    _least__T = typing.TypeVar('_least__T')  # <T>
    @staticmethod
    def least(int: int, comparator: typing.Union[java.util.Comparator[_least__T], typing.Callable[[_least__T, _least__T], int]]) -> java.util.stream.Collector[_least__T, typing.Any, java.util.List[_least__T]]: ...
    _lexicographical__T = typing.TypeVar('_lexicographical__T')  # <T>
    _lexicographical__S = typing.TypeVar('_lexicographical__S')  # <S>
    @staticmethod
    def lexicographical(comparator: typing.Union[java.util.Comparator[_lexicographical__T], typing.Callable[[_lexicographical__T, _lexicographical__T], int]]) -> java.util.Comparator[java.lang.Iterable[_lexicographical__S]]: ...

class ComparisonChain:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src` extends Object
    
        A utility for performing a chained comparison statement. For example:
    
        .. code-block: java
        
         public int compareTo(Foo that) {
           return ComparisonChain.start()
               .compare(this.aString, that.aString)
               .compare(this.anInt, that.anInt)
               .compare(this.anEnum, that.anEnum, Ordering.natural().nullsLast())
               .result();
         }
         
    
        The value of this expression will have the same sign as the *first nonzero* comparison result in the chain, or will be
        zero if every comparison result was zero.
    
        **Note:** :code:`ComparisonChain` instances are **immutable**. For this utility to work correctly, calls must be chained
        as illustrated above.
    
        Performance note: Even though the :code:`ComparisonChain` caller always invokes its :code:`compare` methods
        unconditionally, the :code:`ComparisonChain` implementation stops calling its inputs' null and null methods as soon as
        one of them returns a nonzero result. This optimization is typically important only in the presence of expensive
        :code:`compareTo` and :code:`compare` implementations.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    _compare_4__T = typing.TypeVar('_compare_4__T')  # <T>
    @typing.overload
    def compare(self, double: float, double2: float) -> 'ComparisonChain': ...
    @typing.overload
    def compare(self, float: float, float2: float) -> 'ComparisonChain': ...
    @typing.overload
    def compare(self, int: int, int2: int) -> 'ComparisonChain': ...
    @typing.overload
    def compare(self, comparable: java.lang.Comparable[typing.Any], comparable2: java.lang.Comparable[typing.Any]) -> 'ComparisonChain': ...
    @typing.overload
    def compare(self, t: _compare_4__T, t2: _compare_4__T, comparator: typing.Union[java.util.Comparator[_compare_4__T], typing.Callable[[_compare_4__T, _compare_4__T], int]]) -> 'ComparisonChain': ...
    @typing.overload
    def compare(self, long: int, long2: int) -> 'ComparisonChain': ...
    @typing.overload
    def compare(self, boolean: bool, boolean2: bool) -> 'ComparisonChain': ...
    def compareFalseFirst(self, boolean: bool, boolean2: bool) -> 'ComparisonChain': ...
    def compareTrueFirst(self, boolean: bool, boolean2: bool) -> 'ComparisonChain': ...
    def result(self) -> int: ...
    @staticmethod
    def start() -> 'ComparisonChain': ...

class ComputationException(java.lang.RuntimeException):
    """
    Deprecated. 
    This exception is no longer thrown by :code:`com.google.common`. Previously, it was thrown by
    :class:`~com.google.common.collect.MapMaker` computing maps. When support for computing maps was removed from
    :code:`MapMaker`, it was added to :code:`CacheBuilder`, which throws :code:`ExecutionException`,
    :code:`UncheckedExecutionException`, and :code:`ExecutionError`. Any code that is still catching
    :code:`ComputationException` may need to be updated to catch some of those types instead. (Note that this type, though
    deprecated, is not planned to be removed from Guava.)
    @Deprecated :class:`~com.google.common.annotations.GwtCompatible` public class :meth:`~src` extends RuntimeException
    
        Wraps an exception that occurred during a computation.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, throwable: java.lang.Throwable): ...

_DiscreteDomain__C = typing.TypeVar('_DiscreteDomain__C', bound=java.lang.Comparable)  # <C>
class DiscreteDomain(typing.Generic[_DiscreteDomain__C]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<C extends Comparable> extends Object
    
        A descriptor for a *discrete* :code:`Comparable` domain such as all null instances. A discrete domain is one that
        supports the three basic operations: :meth:`~com.google.common.collect.DiscreteDomain.next`,
        :meth:`~com.google.common.collect.DiscreteDomain.previous` and
        :meth:`~com.google.common.collect.DiscreteDomain.distance`, according to their specifications. The methods
        :meth:`~com.google.common.collect.DiscreteDomain.minValue` and
        :meth:`~com.google.common.collect.DiscreteDomain.maxValue` should also be overridden for bounded types.
    
        A discrete domain always represents the *entire* set of values of its type; it cannot represent partial domains such as
        "prime integers" or "strings of length 5."
    
        See the Guava User Guide section on null.
    
        Since:
            10.0
    """
    @staticmethod
    def bigIntegers() -> 'DiscreteDomain'[java.math.BigInteger]: ...
    def distance(self, c: _DiscreteDomain__C, c2: _DiscreteDomain__C) -> int: ...
    @staticmethod
    def integers() -> 'DiscreteDomain'[int]: ...
    @staticmethod
    def longs() -> 'DiscreteDomain'[int]: ...
    def maxValue(self) -> _DiscreteDomain__C: ...
    def minValue(self) -> _DiscreteDomain__C: ...
    def next(self, c: _DiscreteDomain__C) -> _DiscreteDomain__C: ...
    def previous(self, c: _DiscreteDomain__C) -> _DiscreteDomain__C: ...

_FluentIterable__E = typing.TypeVar('_FluentIterable__E')  # <E>
class FluentIterable(java.lang.Iterable[_FluentIterable__E], typing.Generic[_FluentIterable__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<E> extends Object implements Iterable<E>
    
        A discouraged (but not deprecated) precursor to Java's superior null library.
    
        The following types of methods are provided:
    
          - chaining methods which return a new :code:`FluentIterable` based in some way on the contents of the current one (for
            example :meth:`~com.google.common.collect.FluentIterable.transform`)
          - element extraction methods which facilitate the retrieval of certain elements (for example
            :meth:`~com.google.common.collect.FluentIterable.last`)
          - query methods which answer questions about the :code:`FluentIterable`'s contents (for example
            :meth:`~com.google.common.collect.FluentIterable.anyMatch`)
          - conversion methods which copy the :code:`FluentIterable`'s contents into a new collection or array (for example
            :meth:`~com.google.common.collect.FluentIterable.toList`)
    
    
        Several lesser-used features are currently available only as static methods on the
        :class:`~com.google.common.collect.Iterables` class.
    
        :class:`~com.google.common.collect`
    
        Comparison to streams
    ---------------------
    
    
        null is similar to this class, but generally more powerful, and certainly more standard. Key differences include:
    
          - A stream is *single-use*; it becomes invalid as soon as any "terminal operation" such as :code:`findFirst()` or
            :code:`iterator()` is invoked. (Even though :code:`Stream` contains all the right method *signatures* to implement null,
            it does not actually do so, to avoid implying repeat-iterability.) :code:`FluentIterable`, on the other hand, is
            multiple-use, and does implement null.
          - Streams offer many features not found here, including :code:`min/max`, :code:`distinct`, :code:`reduce`, :code:`sorted`,
            the very powerful :code:`collect`, and built-in support for parallelizing stream operations.
          - :code:`FluentIterable` contains several features not available on :code:`Stream`, which are noted in the method
            descriptions below.
          - Streams include primitive-specialized variants such as :code:`IntStream`, the use of which is strongly recommended.
          - Streams are standard Java, not requiring a third-party dependency.
    
    
        Example
    -------
    
    
        Here is an example that accepts a list from a database call, filters it based on a predicate, transforms it by invoking
        :code:`toString()` on each element, and returns the first 10 elements as a :code:`List`:
    
        .. code-block: java
        
         ImmutableList<String> results =
             FluentIterable.from(database.getClientList())
                 .filter(Client::isActiveInLastMonth)
                 .transform(Object::toString)
                 .limit(10)
                 .toList();
         
        The approximate stream equivalent is:
    
        .. code-block: java
        
         List<String> results =
             database.getClientList()
                 .stream()
                 .filter(Client::isActiveInLastMonth)
                 .map(Object::toString)
                 .limit(10)
                 .collect(Collectors.toList());
         
    
        Since:
            12.0
    """
    def allMatch(self, predicate: typing.Union[com.google.common.base.Predicate[_FluentIterable__E], typing.Callable[[_FluentIterable__E], bool]]) -> bool: ...
    def anyMatch(self, predicate: typing.Union[com.google.common.base.Predicate[_FluentIterable__E], typing.Callable[[_FluentIterable__E], bool]]) -> bool: ...
    @typing.overload
    def append(self, iterable: java.lang.Iterable[_FluentIterable__E]) -> 'FluentIterable'[_FluentIterable__E]: ...
    @typing.overload
    def append(self, eArray: typing.List[_FluentIterable__E]) -> 'FluentIterable'[_FluentIterable__E]: ...
    _concat_0__T = typing.TypeVar('_concat_0__T')  # <T>
    _concat_1__T = typing.TypeVar('_concat_1__T')  # <T>
    _concat_2__T = typing.TypeVar('_concat_2__T')  # <T>
    _concat_3__T = typing.TypeVar('_concat_3__T')  # <T>
    _concat_4__T = typing.TypeVar('_concat_4__T')  # <T>
    @typing.overload
    @staticmethod
    def concat(iterable: java.lang.Iterable[java.lang.Iterable[_concat_0__T]]) -> 'FluentIterable'[_concat_0__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterable: java.lang.Iterable[_concat_1__T], iterable2: java.lang.Iterable[_concat_1__T]) -> 'FluentIterable'[_concat_1__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterable: java.lang.Iterable[_concat_2__T], iterable2: java.lang.Iterable[_concat_2__T], iterable3: java.lang.Iterable[_concat_2__T]) -> 'FluentIterable'[_concat_2__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterable: java.lang.Iterable[_concat_3__T], iterable2: java.lang.Iterable[_concat_3__T], iterable3: java.lang.Iterable[_concat_3__T], iterable4: java.lang.Iterable[_concat_3__T]) -> 'FluentIterable'[_concat_3__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterableArray: typing.List[java.lang.Iterable[_concat_4__T]]) -> 'FluentIterable'[_concat_4__T]: ...
    def contains(self, object: typing.Any) -> bool: ...
    _copyInto__C = typing.TypeVar('_copyInto__C', bound=java.util.Collection)  # <C>
    def copyInto(self, c: _copyInto__C) -> _copyInto__C: ...
    def cycle(self) -> 'FluentIterable'[_FluentIterable__E]: ...
    _filter_1__T = typing.TypeVar('_filter_1__T')  # <T>
    @typing.overload
    def filter(self, predicate: typing.Union[com.google.common.base.Predicate[_FluentIterable__E], typing.Callable[[_FluentIterable__E], bool]]) -> 'FluentIterable'[_FluentIterable__E]: ...
    @typing.overload
    def filter(self, class_: typing.Type[_filter_1__T]) -> 'FluentIterable'[_filter_1__T]: ...
    def first(self) -> com.google.common.base.Optional[_FluentIterable__E]: ...
    def firstMatch(self, predicate: typing.Union[com.google.common.base.Predicate[_FluentIterable__E], typing.Callable[[_FluentIterable__E], bool]]) -> com.google.common.base.Optional[_FluentIterable__E]: ...
    def get(self, int: int) -> _FluentIterable__E: ...
    _index__K = typing.TypeVar('_index__K')  # <K>
    def index(self, function: typing.Union[com.google.common.base.Function[_FluentIterable__E, _index__K], typing.Callable[[_FluentIterable__E], _index__K]]) -> 'ImmutableListMultimap'[_index__K, _FluentIterable__E]: ...
    def isEmpty(self) -> bool: ...
    def join(self, joiner: com.google.common.base.Joiner) -> str: ...
    def last(self) -> com.google.common.base.Optional[_FluentIterable__E]: ...
    def limit(self, int: int) -> 'FluentIterable'[_FluentIterable__E]: ...
    _of_0__E = typing.TypeVar('_of_0__E')  # <E>
    _of_1__E = typing.TypeVar('_of_1__E')  # <E>
    @typing.overload
    @staticmethod
    def of() -> 'FluentIterable'[_of_0__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_1__E, eArray: typing.List[_of_1__E]) -> 'FluentIterable'[_of_1__E]: ...
    def size(self) -> int: ...
    def skip(self, int: int) -> 'FluentIterable'[_FluentIterable__E]: ...
    def stream(self) -> java.util.stream.Stream[_FluentIterable__E]: ...
    def toArray(self, class_: typing.Type[_FluentIterable__E]) -> typing.List[_FluentIterable__E]: ...
    def toList(self) -> 'ImmutableList'[_FluentIterable__E]: ...
    _toMap__V = typing.TypeVar('_toMap__V')  # <V>
    def toMap(self, function: typing.Union[com.google.common.base.Function[_FluentIterable__E, _toMap__V], typing.Callable[[_FluentIterable__E], _toMap__V]]) -> 'ImmutableMap'[_FluentIterable__E, _toMap__V]: ...
    def toMultiset(self) -> 'ImmutableMultiset'[_FluentIterable__E]: ...
    def toSet(self) -> 'ImmutableSet'[_FluentIterable__E]: ...
    def toSortedList(self, comparator: typing.Union[java.util.Comparator[_FluentIterable__E], typing.Callable[[_FluentIterable__E, _FluentIterable__E], int]]) -> 'ImmutableList'[_FluentIterable__E]: ...
    def toSortedSet(self, comparator: typing.Union[java.util.Comparator[_FluentIterable__E], typing.Callable[[_FluentIterable__E, _FluentIterable__E], int]]) -> 'ImmutableSortedSet'[_FluentIterable__E]: ...
    def toString(self) -> str: ...
    _transform__T = typing.TypeVar('_transform__T')  # <T>
    def transform(self, function: typing.Union[com.google.common.base.Function[_FluentIterable__E, _transform__T], typing.Callable[[_FluentIterable__E], _transform__T]]) -> 'FluentIterable'[_transform__T]: ...
    _transformAndConcat__T = typing.TypeVar('_transformAndConcat__T')  # <T>
    def transformAndConcat(self, function: typing.Union[com.google.common.base.Function[_FluentIterable__E, java.lang.Iterable[_transformAndConcat__T]], typing.Callable[[_FluentIterable__E], java.lang.Iterable[_transformAndConcat__T]]]) -> 'FluentIterable'[_transformAndConcat__T]: ...
    _uniqueIndex__K = typing.TypeVar('_uniqueIndex__K')  # <K>
    def uniqueIndex(self, function: typing.Union[com.google.common.base.Function[_FluentIterable__E, _uniqueIndex__K], typing.Callable[[_FluentIterable__E], _uniqueIndex__K]]) -> 'ImmutableMap'[_uniqueIndex__K, _FluentIterable__E]: ...

class ForwardingObject:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src` extends Object
    
        An abstract base class for implementing the `decorator pattern <http://en.wikipedia.org/wiki/Decorator_pattern>`. The
        :meth:`~com.google.common.collect.ForwardingObject.delegate` method must be overridden to return the instance being
        decorated.
    
        This class does *not* forward the :code:`hashCode` and :code:`equals` methods through to the backing object, but relies
        on :code:`Object`'s implementation. This is necessary to preserve the symmetry of :code:`equals`. Custom definitions of
        equality are usually based on an interface, such as :code:`Set` or :code:`List`, so that the implementation of
        :code:`equals` can cast the object being tested for equality to the custom interface. :code:`ForwardingObject`
        implements no such custom interfaces directly; they are implemented only in subclasses. Therefore, forwarding
        :code:`equals` would break symmetry, as the forwarding object might consider itself equal to the object being tested,
        but the reverse could not be true. This behavior is consistent with the JDK's collection wrappers, such as null. Use an
        interface-specific subclass of :code:`ForwardingObject`, such as :class:`~com.google.common.collect.ForwardingList`, to
        preserve equality behavior, or override :code:`equals` directly.
    
        The :code:`toString` method is forwarded to the delegate. Although this class does not implement null, a serializable
        subclass may be created since this class has a parameter-less constructor.
    
        Since:
            2.0
    """
    def toString(self) -> str: ...

_ImmutableCollection__Builder__E = typing.TypeVar('_ImmutableCollection__Builder__E')  # <E>
_ImmutableCollection__E = typing.TypeVar('_ImmutableCollection__E')  # <E>
class ImmutableCollection(java.util.AbstractCollection[_ImmutableCollection__E], java.io.Serializable, typing.Generic[_ImmutableCollection__E]):
    """
    @DoNotMock(value="Use ImmutableList.of or another implementation") :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<E> extends AbstractCollection<E> implements Serializable
    
        A null whose contents will never change, and which offers a few additional guarantees detailed below.
    
        **Warning:** avoid *direct* usage of :class:`~com.google.common.collect.ImmutableCollection` as a type (just as with
        null itself). Prefer subtypes such as :class:`~com.google.common.collect.ImmutableSet` or
        :class:`~com.google.common.collect.ImmutableList`, which have well-defined null semantics, thus avoiding a common source
        of bugs and confusion.
    
        About *all* :code:`Immutable-` collections
    ------------------------------------------
    
    
        The remainder of this documentation applies to every public :code:`Immutable-` type in this package, whether it is a
        subtype of :code:`ImmutableCollection` or not.
    
        Guarantees
    ----------
    
    
        Each makes the following guarantees:
    
          - **Shallow immutability.** Elements can never be added, removed or replaced in this collection. This is a stronger
            guarantee than that of null, whose contents change whenever the wrapped collection is modified.
          - **Null-hostility.** This collection will never contain a null element.
          - **Deterministic iteration.** The iteration order is always well-defined, depending on how the collection was created.
            Typically this is insertion order unless an explicit ordering is otherwise specified (e.g.
            :meth:`~com.google.common.collect.ImmutableSortedSet.naturalOrder`). See the appropriate factory method for details.
            View collections such as :meth:`~com.google.common.collect.ImmutableMultiset.elementSet` iterate in the same order as
            the parent, except as noted.
          - **Thread safety.** It is safe to access this collection concurrently from multiple threads.
          - **Integrity.** This type cannot be subclassed outside this package (which would allow these guarantees to be violated).
    
    
        "Interfaces", not implementations
    ---------------------------------
    
    
        These are classes instead of interfaces to prevent external subtyping, but should be thought of as interfaces in every
        important sense. Each public class such as :class:`~com.google.common.collect.ImmutableSet` is a *type* offering
        meaningful behavioral guarantees. This is substantially different from the case of (say) null, which is an
        *implementation*, with semantics that were largely defined by its supertype.
    
        For field types and method return types, you should generally use the immutable type (such as
        :class:`~com.google.common.collect.ImmutableList`) instead of the general collection interface type (such as null). This
        communicates to your callers all of the semantic guarantees listed above, which is almost always very useful
        information.
    
        On the other hand, a *parameter* type of :class:`~com.google.common.collect.ImmutableList` is generally a nuisance to
        callers. Instead, accept null and have your method or constructor body pass it to the appropriate :code:`copyOf` method
        itself.
    
        Expressing the immutability guarantee directly in the type that user code references is a powerful advantage. Although
        Java offers certain immutable collection factory methods, such as null and null, we recommend using *these* classes
        instead for this reason (as well as for consistency).
    
        Creation
    --------
    
    
        Except for logically "abstract" types like :code:`ImmutableCollection` itself, each :code:`Immutable` type provides the
        static operations you need to obtain instances of that type. These usually include:
    
          - Static methods named :code:`of`, accepting an explicit list of elements or entries.
          - Static methods named :code:`copyOf` (or :code:`copyOfSorted`), accepting an existing collection whose contents should be
            copied.
          - A static nested :code:`Builder` class which can be used to populate a new immutable instance.
    
    
        Warnings
    --------
    
    
          - **Warning:** as with any collection, it is almost always a bad idea to modify an element (in a way that affects its null
            behavior) while it is contained in a collection. Undefined behavior and bugs will result. It's generally best to avoid
            using mutable objects as elements at all, as many users may expect your "immutable" object to be *deeply* immutable.
    
    
        Performance notes
    -----------------
    
    
          - Implementations can be generally assumed to prioritize memory efficiency, then speed of access, and lastly speed of
            creation.
          - The :code:`copyOf` methods will sometimes recognize that the actual copy operation is unnecessary; for example,
            :code:`copyOf(copyOf(anArrayList))` should copy the data only once. This reduces the expense of habitually making
            defensive copies at API boundaries. However, the precise conditions for skipping the copy operation are undefined.
          - **Warning:** a view collection such as :meth:`~com.google.common.collect.ImmutableMap.keySet` or
            :meth:`~com.google.common.collect.ImmutableList.subList` may retain a reference to the entire data set, preventing it
            from being garbage collected. If some of the data is no longer reachable through other means, this constitutes a memory
            leak. Pass the view collection to the appropriate :code:`copyOf` method to obtain a correctly-sized copy.
          - The performance of using the associated :code:`Builder` class can be assumed to be no worse, and possibly better, than
            creating a mutable collection and copying it.
          - Implementations generally do not cache hash codes. If your element or key type has a slow :code:`hashCode`
            implementation, it should cache it itself.
    
    
        Example usage
    -------------
    
    
        .. code-block: java
        
         class Foo {
           private static final ImmutableSet<String> RESERVED_CODES =
               ImmutableSet.of("AZ", "CQ", "ZX");
        
           private final ImmutableSet<String> codes;
        
           public Foo(Iterable<String> codes) {
             this.codes = ImmutableSet.copyOf(codes);
             checkArgument(Collections.disjoint(this.codes, RESERVED_CODES));
           }
         }
         
    
        See also
    --------
    
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def add(self, e: _ImmutableCollection__E) -> bool: ...
    def addAll(self, collection: typing.Union[java.util.Collection[_ImmutableCollection__E], typing.Sequence[_ImmutableCollection__E]]) -> bool: ...
    def asList(self) -> 'ImmutableList'[_ImmutableCollection__E]: ...
    def clear(self) -> None: ...
    def contains(self, object: typing.Any) -> bool: ...
    def iterator(self) -> 'UnmodifiableIterator'[_ImmutableCollection__E]: ...
    def remove(self, object: typing.Any) -> bool: ...
    def removeAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def removeIf(self, predicate: typing.Union[java.util.function.Predicate[_ImmutableCollection__E], typing.Callable[[_ImmutableCollection__E], bool]]) -> bool: ...
    def retainAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def spliterator(self) -> java.util.Spliterator[_ImmutableCollection__E]: ...
    _toArray_0__T = typing.TypeVar('_toArray_0__T')  # <T>
    _toArray_2__T = typing.TypeVar('_toArray_2__T')  # <T>
    @typing.overload
    def toArray(self, intFunction: typing.Union[java.util.function.IntFunction[typing.List[_toArray_0__T]], typing.Callable[[int], typing.List[_toArray_0__T]]]) -> typing.List[_toArray_0__T]: ...
    @typing.overload
    def toArray(self) -> typing.List[typing.Any]: ...
    @typing.overload
    def toArray(self, tArray: typing.List[_toArray_2__T]) -> typing.List[_toArray_2__T]: ...
    class Builder(typing.Generic[_ImmutableCollection__Builder__E]):
        @typing.overload
        def add(self, e: _ImmutableCollection__Builder__E) -> 'ImmutableCollection.Builder'[_ImmutableCollection__Builder__E]: ...
        @typing.overload
        def add(self, eArray: typing.List[_ImmutableCollection__Builder__E]) -> 'ImmutableCollection.Builder'[_ImmutableCollection__Builder__E]: ...
        @typing.overload
        def addAll(self, iterable: java.lang.Iterable[_ImmutableCollection__Builder__E]) -> 'ImmutableCollection.Builder'[_ImmutableCollection__Builder__E]: ...
        @typing.overload
        def addAll(self, iterator: java.util.Iterator[_ImmutableCollection__Builder__E]) -> 'ImmutableCollection.Builder'[_ImmutableCollection__Builder__E]: ...
        def build(self) -> 'ImmutableCollection'[_ImmutableCollection__Builder__E]: ...

_ImmutableMap__Builder__K = typing.TypeVar('_ImmutableMap__Builder__K')  # <K>
_ImmutableMap__Builder__V = typing.TypeVar('_ImmutableMap__Builder__V')  # <V>
_ImmutableMap__K = typing.TypeVar('_ImmutableMap__K')  # <K>
_ImmutableMap__V = typing.TypeVar('_ImmutableMap__V')  # <V>
class ImmutableMap(java.util.Map[_ImmutableMap__K, _ImmutableMap__V], java.io.Serializable, typing.Generic[_ImmutableMap__K, _ImmutableMap__V]):
    """
    @DoNotMock(value="Use ImmutableMap.of or another implementation") :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<K,V> extends Object implements Map<K,V>, Serializable
    
        A null whose contents will never change, with many other important properties detailed at
        :class:`~com.google.common.collect.ImmutableCollection`.
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def asMultimap(self) -> 'ImmutableSetMultimap'[_ImmutableMap__K, _ImmutableMap__V]: ...
    _builder__K = typing.TypeVar('_builder__K')  # <K>
    _builder__V = typing.TypeVar('_builder__V')  # <V>
    @staticmethod
    def builder() -> 'ImmutableMap.Builder'[_builder__K, _builder__V]: ...
    _builderWithExpectedSize__K = typing.TypeVar('_builderWithExpectedSize__K')  # <K>
    _builderWithExpectedSize__V = typing.TypeVar('_builderWithExpectedSize__V')  # <V>
    @staticmethod
    def builderWithExpectedSize(int: int) -> 'ImmutableMap.Builder'[_builderWithExpectedSize__K, _builderWithExpectedSize__V]: ...
    def clear(self) -> None: ...
    def compute(self, k: _ImmutableMap__K, biFunction: typing.Union[java.util.function.BiFunction[_ImmutableMap__K, _ImmutableMap__V, _ImmutableMap__V], typing.Callable[[_ImmutableMap__K, _ImmutableMap__V], _ImmutableMap__V]]) -> _ImmutableMap__V: ...
    def computeIfAbsent(self, k: _ImmutableMap__K, function: typing.Union[java.util.function.Function[_ImmutableMap__K, _ImmutableMap__V], typing.Callable[[_ImmutableMap__K], _ImmutableMap__V]]) -> _ImmutableMap__V: ...
    def computeIfPresent(self, k: _ImmutableMap__K, biFunction: typing.Union[java.util.function.BiFunction[_ImmutableMap__K, _ImmutableMap__V, _ImmutableMap__V], typing.Callable[[_ImmutableMap__K, _ImmutableMap__V], _ImmutableMap__V]]) -> _ImmutableMap__V: ...
    def containsKey(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    _copyOf_0__K = typing.TypeVar('_copyOf_0__K')  # <K>
    _copyOf_0__V = typing.TypeVar('_copyOf_0__V')  # <V>
    _copyOf_1__K = typing.TypeVar('_copyOf_1__K')  # <K>
    _copyOf_1__V = typing.TypeVar('_copyOf_1__V')  # <V>
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_0__K, _copyOf_0__V]]) -> 'ImmutableMap'[_copyOf_0__K, _copyOf_0__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(map: typing.Union[java.util.Map[_copyOf_1__K, _copyOf_1__V], typing.Mapping[_copyOf_1__K, _copyOf_1__V]]) -> 'ImmutableMap'[_copyOf_1__K, _copyOf_1__V]: ...
    def entrySet(self) -> 'ImmutableSet'[java.util.Map.Entry[_ImmutableMap__K, _ImmutableMap__V]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, object: typing.Any) -> _ImmutableMap__V: ...
    def getOrDefault(self, object: typing.Any, v: _ImmutableMap__V) -> _ImmutableMap__V: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def keySet(self) -> 'ImmutableSet'[_ImmutableMap__K]: ...
    def merge(self, k: _ImmutableMap__K, v: _ImmutableMap__V, biFunction: typing.Union[java.util.function.BiFunction[_ImmutableMap__V, _ImmutableMap__V, _ImmutableMap__V], typing.Callable[[_ImmutableMap__V, _ImmutableMap__V], _ImmutableMap__V]]) -> _ImmutableMap__V: ...
    _of_0__K = typing.TypeVar('_of_0__K')  # <K>
    _of_0__V = typing.TypeVar('_of_0__V')  # <V>
    _of_1__K = typing.TypeVar('_of_1__K')  # <K>
    _of_1__V = typing.TypeVar('_of_1__V')  # <V>
    _of_2__K = typing.TypeVar('_of_2__K')  # <K>
    _of_2__V = typing.TypeVar('_of_2__V')  # <V>
    _of_3__K = typing.TypeVar('_of_3__K')  # <K>
    _of_3__V = typing.TypeVar('_of_3__V')  # <V>
    _of_4__K = typing.TypeVar('_of_4__K')  # <K>
    _of_4__V = typing.TypeVar('_of_4__V')  # <V>
    _of_5__K = typing.TypeVar('_of_5__K')  # <K>
    _of_5__V = typing.TypeVar('_of_5__V')  # <V>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableMap'[_of_0__K, _of_0__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_1__K, v: _of_1__V) -> 'ImmutableMap'[_of_1__K, _of_1__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_2__K, v: _of_2__V, k2: _of_2__K, v2: _of_2__V) -> 'ImmutableMap'[_of_2__K, _of_2__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_3__K, v: _of_3__V, k2: _of_3__K, v2: _of_3__V, k3: _of_3__K, v3: _of_3__V) -> 'ImmutableMap'[_of_3__K, _of_3__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_4__K, v: _of_4__V, k2: _of_4__K, v2: _of_4__V, k3: _of_4__K, v3: _of_4__V, k4: _of_4__K, v4: _of_4__V) -> 'ImmutableMap'[_of_4__K, _of_4__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_5__K, v: _of_5__V, k2: _of_5__K, v2: _of_5__V, k3: _of_5__K, v3: _of_5__V, k4: _of_5__K, v4: _of_5__V, k5: _of_5__K, v5: _of_5__V) -> 'ImmutableMap'[_of_5__K, _of_5__V]: ...
    def put(self, k: _ImmutableMap__K, v: _ImmutableMap__V) -> _ImmutableMap__V: ...
    def putAll(self, map: typing.Union[java.util.Map[_ImmutableMap__K, _ImmutableMap__V], typing.Mapping[_ImmutableMap__K, _ImmutableMap__V]]) -> None: ...
    def putIfAbsent(self, k: _ImmutableMap__K, v: _ImmutableMap__V) -> _ImmutableMap__V: ...
    @typing.overload
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any) -> _ImmutableMap__V: ...
    @typing.overload
    def replace(self, k: _ImmutableMap__K, v: _ImmutableMap__V, v2: _ImmutableMap__V) -> bool: ...
    @typing.overload
    def replace(self, k: _ImmutableMap__K, v: _ImmutableMap__V) -> _ImmutableMap__V: ...
    def replaceAll(self, biFunction: typing.Union[java.util.function.BiFunction[_ImmutableMap__K, _ImmutableMap__V, _ImmutableMap__V], typing.Callable[[_ImmutableMap__K, _ImmutableMap__V], _ImmutableMap__V]]) -> None: ...
    _toImmutableMap_0__T = typing.TypeVar('_toImmutableMap_0__T')  # <T>
    _toImmutableMap_0__K = typing.TypeVar('_toImmutableMap_0__K')  # <K>
    _toImmutableMap_0__V = typing.TypeVar('_toImmutableMap_0__V')  # <V>
    _toImmutableMap_1__T = typing.TypeVar('_toImmutableMap_1__T')  # <T>
    _toImmutableMap_1__K = typing.TypeVar('_toImmutableMap_1__K')  # <K>
    _toImmutableMap_1__V = typing.TypeVar('_toImmutableMap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def toImmutableMap(function: typing.Union[java.util.function.Function[_toImmutableMap_0__T, _toImmutableMap_0__K], typing.Callable[[_toImmutableMap_0__T], _toImmutableMap_0__K]], function2: typing.Union[java.util.function.Function[_toImmutableMap_0__T, _toImmutableMap_0__V], typing.Callable[[_toImmutableMap_0__T], _toImmutableMap_0__V]]) -> java.util.stream.Collector[_toImmutableMap_0__T, typing.Any, 'ImmutableMap'[_toImmutableMap_0__K, _toImmutableMap_0__V]]: ...
    @typing.overload
    @staticmethod
    def toImmutableMap(function: typing.Union[java.util.function.Function[_toImmutableMap_1__T, _toImmutableMap_1__K], typing.Callable[[_toImmutableMap_1__T], _toImmutableMap_1__K]], function2: typing.Union[java.util.function.Function[_toImmutableMap_1__T, _toImmutableMap_1__V], typing.Callable[[_toImmutableMap_1__T], _toImmutableMap_1__V]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toImmutableMap_1__V], typing.Callable]) -> java.util.stream.Collector[_toImmutableMap_1__T, typing.Any, 'ImmutableMap'[_toImmutableMap_1__K, _toImmutableMap_1__V]]: ...
    def toString(self) -> str: ...
    def values(self) -> ImmutableCollection[_ImmutableMap__V]: ...
    class Builder(typing.Generic[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V]):
        def __init__(self): ...
        def build(self) -> 'ImmutableMap'[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V]: ...
        def orderEntriesByValue(self, comparator: typing.Union[java.util.Comparator[_ImmutableMap__Builder__V], typing.Callable[[_ImmutableMap__Builder__V, _ImmutableMap__Builder__V], int]]) -> 'ImmutableMap.Builder'[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V]: ...
        @typing.overload
        def put(self, k: _ImmutableMap__Builder__K, v: _ImmutableMap__Builder__V) -> 'ImmutableMap.Builder'[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V]: ...
        @typing.overload
        def put(self, entry: java.util.Map.Entry[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V]) -> 'ImmutableMap.Builder'[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V]: ...
        @typing.overload
        def putAll(self, iterable: java.lang.Iterable[java.util.Map.Entry[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V]]) -> 'ImmutableMap.Builder'[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V]: ...
        @typing.overload
        def putAll(self, map: typing.Union[java.util.Map[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V], typing.Mapping[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V]]) -> 'ImmutableMap.Builder'[_ImmutableMap__Builder__K, _ImmutableMap__Builder__V]: ...

_Interner__E = typing.TypeVar('_Interner__E')  # <E>
class Interner(typing.Generic[_Interner__E]):
    """
    :class:`~com.google.common.annotations.Beta` @DoNotMock(value="Use Interners.new*Interner") :class:`~com.google.common.annotations.GwtIncompatible` public interface :meth:`~src`<E>
    
        Provides equivalent behavior to null for other immutable types. Common implementations are available from the
        :class:`~com.google.common.collect.Interners` class.
    
        Since:
            3.0
    """
    def intern(self, e: _Interner__E) -> _Interner__E: ...

class Interners:
    """
    :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtIncompatible` public final class :meth:`~src` extends Object
    
        Contains static methods pertaining to instances of :class:`~com.google.common.collect.Interner`.
    
        Since:
            3.0
    """
    _asFunction__E = typing.TypeVar('_asFunction__E')  # <E>
    @staticmethod
    def asFunction(interner: Interner[_asFunction__E]) -> com.google.common.base.Function[_asFunction__E, _asFunction__E]: ...
    @staticmethod
    def newBuilder() -> 'Interners.InternerBuilder': ...
    _newStrongInterner__E = typing.TypeVar('_newStrongInterner__E')  # <E>
    @staticmethod
    def newStrongInterner() -> Interner[_newStrongInterner__E]: ...
    _newWeakInterner__E = typing.TypeVar('_newWeakInterner__E')  # <E>
    @staticmethod
    def newWeakInterner() -> Interner[_newWeakInterner__E]: ...
    class InternerBuilder:
        _build__E = typing.TypeVar('_build__E')  # <E>
        def build(self) -> Interner[_build__E]: ...
        def concurrencyLevel(self, int: int) -> 'Interners.InternerBuilder': ...
        def strong(self) -> 'Interners.InternerBuilder': ...
        def weak(self) -> 'Interners.InternerBuilder': ...

class Iterables:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        An assortment of mainly legacy static utility methods that operate on or return objects of type :code:`Iterable`. Except
        as noted, each method has a corresponding null-based method in the :class:`~com.google.common.collect.Iterators` class.
    
        **Java 8 users:** several common uses for this class are now more comprehensively addressed by the new null library.
        Read the method documentation below for comparisons. This class is not being deprecated, but we gently encourage you to
        migrate to streams.
    
        *Performance notes:* Unless otherwise noted, all of the iterables produced in this class are *lazy*, which means that
        their iterators only advance the backing iteration when absolutely necessary.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    _addAll__T = typing.TypeVar('_addAll__T')  # <T>
    @staticmethod
    def addAll(collection: typing.Union[java.util.Collection[_addAll__T], typing.Sequence[_addAll__T]], iterable: java.lang.Iterable[_addAll__T]) -> bool: ...
    _all__T = typing.TypeVar('_all__T')  # <T>
    @staticmethod
    def all(iterable: java.lang.Iterable[_all__T], predicate: typing.Union[com.google.common.base.Predicate[_all__T], typing.Callable[[_all__T], bool]]) -> bool: ...
    _any__T = typing.TypeVar('_any__T')  # <T>
    @staticmethod
    def any(iterable: java.lang.Iterable[_any__T], predicate: typing.Union[com.google.common.base.Predicate[_any__T], typing.Callable[[_any__T], bool]]) -> bool: ...
    _concat_0__T = typing.TypeVar('_concat_0__T')  # <T>
    _concat_1__T = typing.TypeVar('_concat_1__T')  # <T>
    _concat_2__T = typing.TypeVar('_concat_2__T')  # <T>
    _concat_3__T = typing.TypeVar('_concat_3__T')  # <T>
    _concat_4__T = typing.TypeVar('_concat_4__T')  # <T>
    @typing.overload
    @staticmethod
    def concat(iterable: java.lang.Iterable[java.lang.Iterable[_concat_0__T]]) -> java.lang.Iterable[_concat_0__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterable: java.lang.Iterable[_concat_1__T], iterable2: java.lang.Iterable[_concat_1__T]) -> java.lang.Iterable[_concat_1__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterable: java.lang.Iterable[_concat_2__T], iterable2: java.lang.Iterable[_concat_2__T], iterable3: java.lang.Iterable[_concat_2__T]) -> java.lang.Iterable[_concat_2__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterable: java.lang.Iterable[_concat_3__T], iterable2: java.lang.Iterable[_concat_3__T], iterable3: java.lang.Iterable[_concat_3__T], iterable4: java.lang.Iterable[_concat_3__T]) -> java.lang.Iterable[_concat_3__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterableArray: typing.List[java.lang.Iterable[_concat_4__T]]) -> java.lang.Iterable[_concat_4__T]: ...
    _consumingIterable__T = typing.TypeVar('_consumingIterable__T')  # <T>
    @staticmethod
    def consumingIterable(iterable: java.lang.Iterable[_consumingIterable__T]) -> java.lang.Iterable[_consumingIterable__T]: ...
    @staticmethod
    def contains(iterable: java.lang.Iterable[typing.Any], object: typing.Any) -> bool: ...
    _cycle_0__T = typing.TypeVar('_cycle_0__T')  # <T>
    _cycle_1__T = typing.TypeVar('_cycle_1__T')  # <T>
    @typing.overload
    @staticmethod
    def cycle(iterable: java.lang.Iterable[_cycle_0__T]) -> java.lang.Iterable[_cycle_0__T]: ...
    @typing.overload
    @staticmethod
    def cycle(tArray: typing.List[_cycle_1__T]) -> java.lang.Iterable[_cycle_1__T]: ...
    @staticmethod
    def elementsEqual(iterable: java.lang.Iterable[typing.Any], iterable2: java.lang.Iterable[typing.Any]) -> bool: ...
    _filter_0__T = typing.TypeVar('_filter_0__T')  # <T>
    _filter_1__T = typing.TypeVar('_filter_1__T')  # <T>
    @typing.overload
    @staticmethod
    def filter(iterable: java.lang.Iterable[_filter_0__T], predicate: typing.Union[com.google.common.base.Predicate[_filter_0__T], typing.Callable[[_filter_0__T], bool]]) -> java.lang.Iterable[_filter_0__T]: ...
    @typing.overload
    @staticmethod
    def filter(iterable: java.lang.Iterable[typing.Any], class_: typing.Type[_filter_1__T]) -> java.lang.Iterable[_filter_1__T]: ...
    _find_0__T = typing.TypeVar('_find_0__T')  # <T>
    _find_1__T = typing.TypeVar('_find_1__T')  # <T>
    @typing.overload
    @staticmethod
    def find(iterable: java.lang.Iterable[_find_0__T], predicate: typing.Union[com.google.common.base.Predicate[_find_0__T], typing.Callable[[_find_0__T], bool]]) -> _find_0__T: ...
    @typing.overload
    @staticmethod
    def find(iterable: java.lang.Iterable[_find_1__T], predicate: typing.Union[com.google.common.base.Predicate[_find_1__T], typing.Callable[[_find_1__T], bool]], t: _find_1__T) -> _find_1__T: ...
    @staticmethod
    def frequency(iterable: java.lang.Iterable[typing.Any], object: typing.Any) -> int: ...
    _get_0__T = typing.TypeVar('_get_0__T')  # <T>
    _get_1__T = typing.TypeVar('_get_1__T')  # <T>
    @typing.overload
    @staticmethod
    def get(iterable: java.lang.Iterable[_get_0__T], int: int) -> _get_0__T: ...
    @typing.overload
    @staticmethod
    def get(iterable: java.lang.Iterable[_get_1__T], int: int, t: _get_1__T) -> _get_1__T: ...
    _getFirst__T = typing.TypeVar('_getFirst__T')  # <T>
    @staticmethod
    def getFirst(iterable: java.lang.Iterable[_getFirst__T], t: _getFirst__T) -> _getFirst__T: ...
    _getLast_0__T = typing.TypeVar('_getLast_0__T')  # <T>
    _getLast_1__T = typing.TypeVar('_getLast_1__T')  # <T>
    @typing.overload
    @staticmethod
    def getLast(iterable: java.lang.Iterable[_getLast_0__T]) -> _getLast_0__T: ...
    @typing.overload
    @staticmethod
    def getLast(iterable: java.lang.Iterable[_getLast_1__T], t: _getLast_1__T) -> _getLast_1__T: ...
    _getOnlyElement_0__T = typing.TypeVar('_getOnlyElement_0__T')  # <T>
    _getOnlyElement_1__T = typing.TypeVar('_getOnlyElement_1__T')  # <T>
    @typing.overload
    @staticmethod
    def getOnlyElement(iterable: java.lang.Iterable[_getOnlyElement_0__T]) -> _getOnlyElement_0__T: ...
    @typing.overload
    @staticmethod
    def getOnlyElement(iterable: java.lang.Iterable[_getOnlyElement_1__T], t: _getOnlyElement_1__T) -> _getOnlyElement_1__T: ...
    _indexOf__T = typing.TypeVar('_indexOf__T')  # <T>
    @staticmethod
    def indexOf(iterable: java.lang.Iterable[_indexOf__T], predicate: typing.Union[com.google.common.base.Predicate[_indexOf__T], typing.Callable[[_indexOf__T], bool]]) -> int: ...
    @staticmethod
    def isEmpty(iterable: java.lang.Iterable[typing.Any]) -> bool: ...
    _limit__T = typing.TypeVar('_limit__T')  # <T>
    @staticmethod
    def limit(iterable: java.lang.Iterable[_limit__T], int: int) -> java.lang.Iterable[_limit__T]: ...
    _mergeSorted__T = typing.TypeVar('_mergeSorted__T')  # <T>
    @staticmethod
    def mergeSorted(iterable: java.lang.Iterable[java.lang.Iterable[_mergeSorted__T]], comparator: typing.Union[java.util.Comparator[_mergeSorted__T], typing.Callable[[_mergeSorted__T, _mergeSorted__T], int]]) -> java.lang.Iterable[_mergeSorted__T]: ...
    _paddedPartition__T = typing.TypeVar('_paddedPartition__T')  # <T>
    @staticmethod
    def paddedPartition(iterable: java.lang.Iterable[_paddedPartition__T], int: int) -> java.lang.Iterable[java.util.List[_paddedPartition__T]]: ...
    _partition__T = typing.TypeVar('_partition__T')  # <T>
    @staticmethod
    def partition(iterable: java.lang.Iterable[_partition__T], int: int) -> java.lang.Iterable[java.util.List[_partition__T]]: ...
    @staticmethod
    def removeAll(iterable: java.lang.Iterable[typing.Any], collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    _removeIf__T = typing.TypeVar('_removeIf__T')  # <T>
    @staticmethod
    def removeIf(iterable: java.lang.Iterable[_removeIf__T], predicate: typing.Union[com.google.common.base.Predicate[_removeIf__T], typing.Callable[[_removeIf__T], bool]]) -> bool: ...
    @staticmethod
    def retainAll(iterable: java.lang.Iterable[typing.Any], collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    @staticmethod
    def size(iterable: java.lang.Iterable[typing.Any]) -> int: ...
    _skip__T = typing.TypeVar('_skip__T')  # <T>
    @staticmethod
    def skip(iterable: java.lang.Iterable[_skip__T], int: int) -> java.lang.Iterable[_skip__T]: ...
    _toArray__T = typing.TypeVar('_toArray__T')  # <T>
    @staticmethod
    def toArray(iterable: java.lang.Iterable[_toArray__T], class_: typing.Type[_toArray__T]) -> typing.List[_toArray__T]: ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    @staticmethod
    def toString(iterable: java.lang.Iterable[typing.Any]) -> str: ...
    _transform__F = typing.TypeVar('_transform__F')  # <F>
    _transform__T = typing.TypeVar('_transform__T')  # <T>
    @staticmethod
    def transform(iterable: java.lang.Iterable[_transform__F], function: typing.Union[com.google.common.base.Function[_transform__F, _transform__T], typing.Callable[[_transform__F], _transform__T]]) -> java.lang.Iterable[_transform__T]: ...
    _tryFind__T = typing.TypeVar('_tryFind__T')  # <T>
    @staticmethod
    def tryFind(iterable: java.lang.Iterable[_tryFind__T], predicate: typing.Union[com.google.common.base.Predicate[_tryFind__T], typing.Callable[[_tryFind__T], bool]]) -> com.google.common.base.Optional[_tryFind__T]: ...
    _unmodifiableIterable_0__E = typing.TypeVar('_unmodifiableIterable_0__E')  # <E>
    _unmodifiableIterable_1__T = typing.TypeVar('_unmodifiableIterable_1__T')  # <T>
    @typing.overload
    @staticmethod
    def unmodifiableIterable(immutableCollection: ImmutableCollection[_unmodifiableIterable_0__E]) -> java.lang.Iterable[_unmodifiableIterable_0__E]: ...
    @typing.overload
    @staticmethod
    def unmodifiableIterable(iterable: java.lang.Iterable[_unmodifiableIterable_1__T]) -> java.lang.Iterable[_unmodifiableIterable_1__T]: ...

class Iterators:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        This class contains static utility methods that operate on or return objects of type null. Except as noted, each method
        has a corresponding null-based method in the :class:`~com.google.common.collect.Iterables` class.
    
        *Performance notes:* Unless otherwise noted, all of the iterators produced in this class are *lazy*, which means that
        they only advance the backing iteration when absolutely necessary.
    
        See the Guava User Guide section on null.
    
        Since:
            2.0
    """
    _addAll__T = typing.TypeVar('_addAll__T')  # <T>
    @staticmethod
    def addAll(collection: typing.Union[java.util.Collection[_addAll__T], typing.Sequence[_addAll__T]], iterator: java.util.Iterator[_addAll__T]) -> bool: ...
    @staticmethod
    def advance(iterator: java.util.Iterator[typing.Any], int: int) -> int: ...
    _all__T = typing.TypeVar('_all__T')  # <T>
    @staticmethod
    def all(iterator: java.util.Iterator[_all__T], predicate: typing.Union[com.google.common.base.Predicate[_all__T], typing.Callable[[_all__T], bool]]) -> bool: ...
    _any__T = typing.TypeVar('_any__T')  # <T>
    @staticmethod
    def any(iterator: java.util.Iterator[_any__T], predicate: typing.Union[com.google.common.base.Predicate[_any__T], typing.Callable[[_any__T], bool]]) -> bool: ...
    _asEnumeration__T = typing.TypeVar('_asEnumeration__T')  # <T>
    @staticmethod
    def asEnumeration(iterator: java.util.Iterator[_asEnumeration__T]) -> java.util.Enumeration[_asEnumeration__T]: ...
    _concat_0__T = typing.TypeVar('_concat_0__T')  # <T>
    _concat_1__T = typing.TypeVar('_concat_1__T')  # <T>
    _concat_2__T = typing.TypeVar('_concat_2__T')  # <T>
    _concat_3__T = typing.TypeVar('_concat_3__T')  # <T>
    _concat_4__T = typing.TypeVar('_concat_4__T')  # <T>
    @typing.overload
    @staticmethod
    def concat(iterator: java.util.Iterator[java.util.Iterator[_concat_0__T]]) -> java.util.Iterator[_concat_0__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterator: java.util.Iterator[_concat_1__T], iterator2: java.util.Iterator[_concat_1__T]) -> java.util.Iterator[_concat_1__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterator: java.util.Iterator[_concat_2__T], iterator2: java.util.Iterator[_concat_2__T], iterator3: java.util.Iterator[_concat_2__T]) -> java.util.Iterator[_concat_2__T]: ...
    @typing.overload
    @staticmethod
    def concat(iterator: java.util.Iterator[_concat_3__T], iterator2: java.util.Iterator[_concat_3__T], iterator3: java.util.Iterator[_concat_3__T], iterator4: java.util.Iterator[_concat_3__T]) -> java.util.Iterator[_concat_3__T]: ...
    @typing.overload
    @staticmethod
    def concat(iteratorArray: typing.List[java.util.Iterator[_concat_4__T]]) -> java.util.Iterator[_concat_4__T]: ...
    _consumingIterator__T = typing.TypeVar('_consumingIterator__T')  # <T>
    @staticmethod
    def consumingIterator(iterator: java.util.Iterator[_consumingIterator__T]) -> java.util.Iterator[_consumingIterator__T]: ...
    @staticmethod
    def contains(iterator: java.util.Iterator[typing.Any], object: typing.Any) -> bool: ...
    _cycle_0__T = typing.TypeVar('_cycle_0__T')  # <T>
    _cycle_1__T = typing.TypeVar('_cycle_1__T')  # <T>
    @typing.overload
    @staticmethod
    def cycle(iterable: java.lang.Iterable[_cycle_0__T]) -> java.util.Iterator[_cycle_0__T]: ...
    @typing.overload
    @staticmethod
    def cycle(tArray: typing.List[_cycle_1__T]) -> java.util.Iterator[_cycle_1__T]: ...
    @staticmethod
    def elementsEqual(iterator: java.util.Iterator[typing.Any], iterator2: java.util.Iterator[typing.Any]) -> bool: ...
    _filter_0__T = typing.TypeVar('_filter_0__T')  # <T>
    _filter_1__T = typing.TypeVar('_filter_1__T')  # <T>
    @typing.overload
    @staticmethod
    def filter(iterator: java.util.Iterator[_filter_0__T], predicate: typing.Union[com.google.common.base.Predicate[_filter_0__T], typing.Callable[[_filter_0__T], bool]]) -> 'UnmodifiableIterator'[_filter_0__T]: ...
    @typing.overload
    @staticmethod
    def filter(iterator: java.util.Iterator[typing.Any], class_: typing.Type[_filter_1__T]) -> 'UnmodifiableIterator'[_filter_1__T]: ...
    _find_0__T = typing.TypeVar('_find_0__T')  # <T>
    _find_1__T = typing.TypeVar('_find_1__T')  # <T>
    @typing.overload
    @staticmethod
    def find(iterator: java.util.Iterator[_find_0__T], predicate: typing.Union[com.google.common.base.Predicate[_find_0__T], typing.Callable[[_find_0__T], bool]]) -> _find_0__T: ...
    @typing.overload
    @staticmethod
    def find(iterator: java.util.Iterator[_find_1__T], predicate: typing.Union[com.google.common.base.Predicate[_find_1__T], typing.Callable[[_find_1__T], bool]], t: _find_1__T) -> _find_1__T: ...
    _forArray__T = typing.TypeVar('_forArray__T')  # <T>
    @staticmethod
    def forArray(tArray: typing.List[_forArray__T]) -> 'UnmodifiableIterator'[_forArray__T]: ...
    _forEnumeration__T = typing.TypeVar('_forEnumeration__T')  # <T>
    @staticmethod
    def forEnumeration(enumeration: java.util.Enumeration[_forEnumeration__T]) -> 'UnmodifiableIterator'[_forEnumeration__T]: ...
    @staticmethod
    def frequency(iterator: java.util.Iterator[typing.Any], object: typing.Any) -> int: ...
    _get_0__T = typing.TypeVar('_get_0__T')  # <T>
    _get_1__T = typing.TypeVar('_get_1__T')  # <T>
    @typing.overload
    @staticmethod
    def get(iterator: java.util.Iterator[_get_0__T], int: int) -> _get_0__T: ...
    @typing.overload
    @staticmethod
    def get(iterator: java.util.Iterator[_get_1__T], int: int, t: _get_1__T) -> _get_1__T: ...
    _getLast_0__T = typing.TypeVar('_getLast_0__T')  # <T>
    _getLast_1__T = typing.TypeVar('_getLast_1__T')  # <T>
    @typing.overload
    @staticmethod
    def getLast(iterator: java.util.Iterator[_getLast_0__T]) -> _getLast_0__T: ...
    @typing.overload
    @staticmethod
    def getLast(iterator: java.util.Iterator[_getLast_1__T], t: _getLast_1__T) -> _getLast_1__T: ...
    _getNext__T = typing.TypeVar('_getNext__T')  # <T>
    @staticmethod
    def getNext(iterator: java.util.Iterator[_getNext__T], t: _getNext__T) -> _getNext__T: ...
    _getOnlyElement_0__T = typing.TypeVar('_getOnlyElement_0__T')  # <T>
    _getOnlyElement_1__T = typing.TypeVar('_getOnlyElement_1__T')  # <T>
    @typing.overload
    @staticmethod
    def getOnlyElement(iterator: java.util.Iterator[_getOnlyElement_0__T]) -> _getOnlyElement_0__T: ...
    @typing.overload
    @staticmethod
    def getOnlyElement(iterator: java.util.Iterator[_getOnlyElement_1__T], t: _getOnlyElement_1__T) -> _getOnlyElement_1__T: ...
    _indexOf__T = typing.TypeVar('_indexOf__T')  # <T>
    @staticmethod
    def indexOf(iterator: java.util.Iterator[_indexOf__T], predicate: typing.Union[com.google.common.base.Predicate[_indexOf__T], typing.Callable[[_indexOf__T], bool]]) -> int: ...
    _limit__T = typing.TypeVar('_limit__T')  # <T>
    @staticmethod
    def limit(iterator: java.util.Iterator[_limit__T], int: int) -> java.util.Iterator[_limit__T]: ...
    _mergeSorted__T = typing.TypeVar('_mergeSorted__T')  # <T>
    @staticmethod
    def mergeSorted(iterable: java.lang.Iterable[java.util.Iterator[_mergeSorted__T]], comparator: typing.Union[java.util.Comparator[_mergeSorted__T], typing.Callable[[_mergeSorted__T, _mergeSorted__T], int]]) -> 'UnmodifiableIterator'[_mergeSorted__T]: ...
    _paddedPartition__T = typing.TypeVar('_paddedPartition__T')  # <T>
    @staticmethod
    def paddedPartition(iterator: java.util.Iterator[_paddedPartition__T], int: int) -> 'UnmodifiableIterator'[java.util.List[_paddedPartition__T]]: ...
    _partition__T = typing.TypeVar('_partition__T')  # <T>
    @staticmethod
    def partition(iterator: java.util.Iterator[_partition__T], int: int) -> 'UnmodifiableIterator'[java.util.List[_partition__T]]: ...
    _peekingIterator_0__T = typing.TypeVar('_peekingIterator_0__T')  # <T>
    _peekingIterator_1__T = typing.TypeVar('_peekingIterator_1__T')  # <T>
    @typing.overload
    @staticmethod
    def peekingIterator(peekingIterator: 'PeekingIterator'[_peekingIterator_0__T]) -> 'PeekingIterator'[_peekingIterator_0__T]: ...
    @typing.overload
    @staticmethod
    def peekingIterator(iterator: java.util.Iterator[_peekingIterator_1__T]) -> 'PeekingIterator'[_peekingIterator_1__T]: ...
    @staticmethod
    def removeAll(iterator: java.util.Iterator[typing.Any], collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    _removeIf__T = typing.TypeVar('_removeIf__T')  # <T>
    @staticmethod
    def removeIf(iterator: java.util.Iterator[_removeIf__T], predicate: typing.Union[com.google.common.base.Predicate[_removeIf__T], typing.Callable[[_removeIf__T], bool]]) -> bool: ...
    @staticmethod
    def retainAll(iterator: java.util.Iterator[typing.Any], collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    _singletonIterator__T = typing.TypeVar('_singletonIterator__T')  # <T>
    @staticmethod
    def singletonIterator(t: _singletonIterator__T) -> 'UnmodifiableIterator'[_singletonIterator__T]: ...
    @staticmethod
    def size(iterator: java.util.Iterator[typing.Any]) -> int: ...
    _toArray__T = typing.TypeVar('_toArray__T')  # <T>
    @staticmethod
    def toArray(iterator: java.util.Iterator[_toArray__T], class_: typing.Type[_toArray__T]) -> typing.List[_toArray__T]: ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    @staticmethod
    def toString(iterator: java.util.Iterator[typing.Any]) -> str: ...
    _transform__F = typing.TypeVar('_transform__F')  # <F>
    _transform__T = typing.TypeVar('_transform__T')  # <T>
    @staticmethod
    def transform(iterator: java.util.Iterator[_transform__F], function: typing.Union[com.google.common.base.Function[_transform__F, _transform__T], typing.Callable[[_transform__F], _transform__T]]) -> java.util.Iterator[_transform__T]: ...
    _tryFind__T = typing.TypeVar('_tryFind__T')  # <T>
    @staticmethod
    def tryFind(iterator: java.util.Iterator[_tryFind__T], predicate: typing.Union[com.google.common.base.Predicate[_tryFind__T], typing.Callable[[_tryFind__T], bool]]) -> com.google.common.base.Optional[_tryFind__T]: ...
    _unmodifiableIterator_0__T = typing.TypeVar('_unmodifiableIterator_0__T')  # <T>
    _unmodifiableIterator_1__T = typing.TypeVar('_unmodifiableIterator_1__T')  # <T>
    @typing.overload
    @staticmethod
    def unmodifiableIterator(unmodifiableIterator: 'UnmodifiableIterator'[_unmodifiableIterator_0__T]) -> 'UnmodifiableIterator'[_unmodifiableIterator_0__T]: ...
    @typing.overload
    @staticmethod
    def unmodifiableIterator(iterator: java.util.Iterator[_unmodifiableIterator_1__T]) -> 'UnmodifiableIterator'[_unmodifiableIterator_1__T]: ...

class Lists:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Static utility methods pertaining to null instances. Also see this class's counterparts
        :class:`~com.google.common.collect.Sets`, :class:`~com.google.common.collect.Maps` and
        :class:`~com.google.common.collect.Queues`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    _asList_0__E = typing.TypeVar('_asList_0__E')  # <E>
    _asList_1__E = typing.TypeVar('_asList_1__E')  # <E>
    @typing.overload
    @staticmethod
    def asList(e: _asList_0__E, e2: _asList_0__E, eArray: typing.List[_asList_0__E]) -> java.util.List[_asList_0__E]: ...
    @typing.overload
    @staticmethod
    def asList(e: _asList_1__E, eArray: typing.List[_asList_1__E]) -> java.util.List[_asList_1__E]: ...
    _cartesianProduct_0__B = typing.TypeVar('_cartesianProduct_0__B')  # <B>
    _cartesianProduct_1__B = typing.TypeVar('_cartesianProduct_1__B')  # <B>
    @typing.overload
    @staticmethod
    def cartesianProduct(list: java.util.List[java.util.List[_cartesianProduct_0__B]]) -> java.util.List[java.util.List[_cartesianProduct_0__B]]: ...
    @typing.overload
    @staticmethod
    def cartesianProduct(listArray: typing.List[java.util.List[_cartesianProduct_1__B]]) -> java.util.List[java.util.List[_cartesianProduct_1__B]]: ...
    @typing.overload
    @staticmethod
    def charactersOf(string: str) -> 'ImmutableList'[str]: ...
    @typing.overload
    @staticmethod
    def charactersOf(charSequence: typing.Union[java.lang.CharSequence, str]) -> java.util.List[str]: ...
    _newArrayList_0__E = typing.TypeVar('_newArrayList_0__E')  # <E>
    _newArrayList_1__E = typing.TypeVar('_newArrayList_1__E')  # <E>
    _newArrayList_2__E = typing.TypeVar('_newArrayList_2__E')  # <E>
    _newArrayList_3__E = typing.TypeVar('_newArrayList_3__E')  # <E>
    @typing.overload
    @staticmethod
    def newArrayList() -> java.util.ArrayList[_newArrayList_0__E]: ...
    @typing.overload
    @staticmethod
    def newArrayList(iterable: java.lang.Iterable[_newArrayList_1__E]) -> java.util.ArrayList[_newArrayList_1__E]: ...
    @typing.overload
    @staticmethod
    def newArrayList(eArray: typing.List[_newArrayList_2__E]) -> java.util.ArrayList[_newArrayList_2__E]: ...
    @typing.overload
    @staticmethod
    def newArrayList(iterator: java.util.Iterator[_newArrayList_3__E]) -> java.util.ArrayList[_newArrayList_3__E]: ...
    _newArrayListWithCapacity__E = typing.TypeVar('_newArrayListWithCapacity__E')  # <E>
    @staticmethod
    def newArrayListWithCapacity(int: int) -> java.util.ArrayList[_newArrayListWithCapacity__E]: ...
    _newArrayListWithExpectedSize__E = typing.TypeVar('_newArrayListWithExpectedSize__E')  # <E>
    @staticmethod
    def newArrayListWithExpectedSize(int: int) -> java.util.ArrayList[_newArrayListWithExpectedSize__E]: ...
    _newCopyOnWriteArrayList_0__E = typing.TypeVar('_newCopyOnWriteArrayList_0__E')  # <E>
    _newCopyOnWriteArrayList_1__E = typing.TypeVar('_newCopyOnWriteArrayList_1__E')  # <E>
    @typing.overload
    @staticmethod
    def newCopyOnWriteArrayList() -> java.util.concurrent.CopyOnWriteArrayList[_newCopyOnWriteArrayList_0__E]: ...
    @typing.overload
    @staticmethod
    def newCopyOnWriteArrayList(iterable: java.lang.Iterable[_newCopyOnWriteArrayList_1__E]) -> java.util.concurrent.CopyOnWriteArrayList[_newCopyOnWriteArrayList_1__E]: ...
    _newLinkedList_0__E = typing.TypeVar('_newLinkedList_0__E')  # <E>
    _newLinkedList_1__E = typing.TypeVar('_newLinkedList_1__E')  # <E>
    @typing.overload
    @staticmethod
    def newLinkedList() -> java.util.LinkedList[_newLinkedList_0__E]: ...
    @typing.overload
    @staticmethod
    def newLinkedList(iterable: java.lang.Iterable[_newLinkedList_1__E]) -> java.util.LinkedList[_newLinkedList_1__E]: ...
    _partition__T = typing.TypeVar('_partition__T')  # <T>
    @staticmethod
    def partition(list: java.util.List[_partition__T], int: int) -> java.util.List[java.util.List[_partition__T]]: ...
    _reverse__T = typing.TypeVar('_reverse__T')  # <T>
    @staticmethod
    def reverse(list: java.util.List[_reverse__T]) -> java.util.List[_reverse__T]: ...
    _transform__F = typing.TypeVar('_transform__F')  # <F>
    _transform__T = typing.TypeVar('_transform__T')  # <T>
    @staticmethod
    def transform(list: java.util.List[_transform__F], function: typing.Union[com.google.common.base.Function[_transform__F, _transform__T], typing.Callable[[_transform__F], _transform__T]]) -> java.util.List[_transform__T]: ...

_MapDifference__ValueDifference__V = typing.TypeVar('_MapDifference__ValueDifference__V')  # <V>
_MapDifference__K = typing.TypeVar('_MapDifference__K')  # <K>
_MapDifference__V = typing.TypeVar('_MapDifference__V')  # <V>
class MapDifference(typing.Generic[_MapDifference__K, _MapDifference__V]):
    """
    @DoNotMock(value="Use Maps.difference") :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<K,V>
    
        An object representing the differences between two maps.
    
        Since:
            2.0
    """
    def areEqual(self) -> bool: ...
    def entriesDiffering(self) -> java.util.Map[_MapDifference__K, 'MapDifference.ValueDifference'[_MapDifference__V]]: ...
    def entriesInCommon(self) -> java.util.Map[_MapDifference__K, _MapDifference__V]: ...
    def entriesOnlyOnLeft(self) -> java.util.Map[_MapDifference__K, _MapDifference__V]: ...
    def entriesOnlyOnRight(self) -> java.util.Map[_MapDifference__K, _MapDifference__V]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    class ValueDifference(typing.Generic[_MapDifference__ValueDifference__V]):
        def equals(self, object: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def leftValue(self) -> _MapDifference__ValueDifference__V: ...
        def rightValue(self) -> _MapDifference__ValueDifference__V: ...

class MapMaker:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        A builder of null instances that can have keys or values automatically wrapped in weak references.
    
        Usage example:
    
        .. code-block: java
        
         ConcurrentMap<Request, Stopwatch> timers = new MapMaker()
             .concurrencyLevel(4)
             .weakKeys()
             .makeMap();
         
    
        These features are all optional; :code:`new MapMaker().makeMap()` returns a valid concurrent map that behaves similarly
        to a null.
    
        The returned map is implemented as a hash table with similar performance characteristics to null. It supports all
        optional operations of the :code:`ConcurrentMap` interface. It does not permit null keys or values.
    
        **Note:** by default, the returned map uses equality comparisons (the null method) to determine equality for keys or
        values. However, if :meth:`~com.google.common.collect.MapMaker.weakKeys` was specified, the map uses identity
        (:code:`==`) comparisons instead for keys. Likewise, if :meth:`~com.google.common.collect.MapMaker.weakValues` was
        specified, the map uses identity comparisons for values.
    
        The view collections of the returned map have *weakly consistent iterators*. This means that they are safe for
        concurrent use, but if other threads modify the map after the iterator is created, it is undefined which of these
        changes, if any, are reflected in that iterator. These iterators never throw null.
    
        If :meth:`~com.google.common.collect.MapMaker.weakKeys` or :meth:`~com.google.common.collect.MapMaker.weakValues` are
        requested, it is possible for a key or value present in the map to be reclaimed by the garbage collector. Entries with
        reclaimed keys or values may be removed from the map on each map modification or on occasional map accesses; such
        entries may be counted by null, but will never be visible to read or write operations. A partially-reclaimed entry is
        never exposed to the user. Any :code:`Map.Entry` instance retrieved from the map's entry set is a snapshot of that
        entry's state at the time of retrieval; such entries do, however, support :code:`Map.Entry#setValue`, which simply calls
        null on the entry's key.
    
        The maps produced by :code:`MapMaker` are serializable, and the deserialized maps retain all the configuration
        properties of the original map. During deserialization, if the original map had used weak references, the entries are
        reconstructed as they were, but it's not unlikely they'll be quickly garbage-collected before they are ever accessed.
    
        :code:`new MapMaker().weakKeys().makeMap()` is a recommended replacement for null, but note that it compares keys using
        object identity whereas :code:`WeakHashMap` uses null.
    
        Since:
            2.0
    """
    def __init__(self): ...
    def concurrencyLevel(self, int: int) -> 'MapMaker': ...
    def initialCapacity(self, int: int) -> 'MapMaker': ...
    _makeMap__K = typing.TypeVar('_makeMap__K')  # <K>
    _makeMap__V = typing.TypeVar('_makeMap__V')  # <V>
    def makeMap(self) -> java.util.concurrent.ConcurrentMap[_makeMap__K, _makeMap__V]: ...
    def toString(self) -> str: ...
    def weakKeys(self) -> 'MapMaker': ...
    def weakValues(self) -> 'MapMaker': ...

_Maps__EntryTransformer__K = typing.TypeVar('_Maps__EntryTransformer__K')  # <K>
_Maps__EntryTransformer__V1 = typing.TypeVar('_Maps__EntryTransformer__V1')  # <V1>
_Maps__EntryTransformer__V2 = typing.TypeVar('_Maps__EntryTransformer__V2')  # <V2>
class Maps:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Static utility methods pertaining to null instances (including instances of null,
        :class:`~com.google.common.collect.BiMap`, etc.). Also see this class's counterparts
        :class:`~com.google.common.collect.Lists`, :class:`~com.google.common.collect.Sets` and
        :class:`~com.google.common.collect.Queues`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    _asConverter__A = typing.TypeVar('_asConverter__A')  # <A>
    _asConverter__B = typing.TypeVar('_asConverter__B')  # <B>
    @staticmethod
    def asConverter(biMap: BiMap[_asConverter__A, _asConverter__B]) -> com.google.common.base.Converter[_asConverter__A, _asConverter__B]: ...
    _asMap_0__K = typing.TypeVar('_asMap_0__K')  # <K>
    _asMap_0__V = typing.TypeVar('_asMap_0__V')  # <V>
    _asMap_1__K = typing.TypeVar('_asMap_1__K')  # <K>
    _asMap_1__V = typing.TypeVar('_asMap_1__V')  # <V>
    _asMap_2__K = typing.TypeVar('_asMap_2__K')  # <K>
    _asMap_2__V = typing.TypeVar('_asMap_2__V')  # <V>
    @typing.overload
    @staticmethod
    def asMap(set: java.util.Set[_asMap_0__K], function: typing.Union[com.google.common.base.Function[_asMap_0__K, _asMap_0__V], typing.Callable[[_asMap_0__K], _asMap_0__V]]) -> java.util.Map[_asMap_0__K, _asMap_0__V]: ...
    @typing.overload
    @staticmethod
    def asMap(navigableSet: java.util.NavigableSet[_asMap_1__K], function: typing.Union[com.google.common.base.Function[_asMap_1__K, _asMap_1__V], typing.Callable[[_asMap_1__K], _asMap_1__V]]) -> java.util.NavigableMap[_asMap_1__K, _asMap_1__V]: ...
    @typing.overload
    @staticmethod
    def asMap(sortedSet: java.util.SortedSet[_asMap_2__K], function: typing.Union[com.google.common.base.Function[_asMap_2__K, _asMap_2__V], typing.Callable[[_asMap_2__K], _asMap_2__V]]) -> java.util.SortedMap[_asMap_2__K, _asMap_2__V]: ...
    _difference_0__K = typing.TypeVar('_difference_0__K')  # <K>
    _difference_0__V = typing.TypeVar('_difference_0__V')  # <V>
    _difference_1__K = typing.TypeVar('_difference_1__K')  # <K>
    _difference_1__V = typing.TypeVar('_difference_1__V')  # <V>
    _difference_2__K = typing.TypeVar('_difference_2__K')  # <K>
    _difference_2__V = typing.TypeVar('_difference_2__V')  # <V>
    @typing.overload
    @staticmethod
    def difference(map: typing.Union[java.util.Map[_difference_0__K, _difference_0__V], typing.Mapping[_difference_0__K, _difference_0__V]], map2: typing.Union[java.util.Map[_difference_0__K, _difference_0__V], typing.Mapping[_difference_0__K, _difference_0__V]]) -> MapDifference[_difference_0__K, _difference_0__V]: ...
    @typing.overload
    @staticmethod
    def difference(map: typing.Union[java.util.Map[_difference_1__K, _difference_1__V], typing.Mapping[_difference_1__K, _difference_1__V]], map2: typing.Union[java.util.Map[_difference_1__K, _difference_1__V], typing.Mapping[_difference_1__K, _difference_1__V]], equivalence: com.google.common.base.Equivalence[_difference_1__V]) -> MapDifference[_difference_1__K, _difference_1__V]: ...
    @typing.overload
    @staticmethod
    def difference(sortedMap: java.util.SortedMap[_difference_2__K, _difference_2__V], map: typing.Union[java.util.Map[_difference_2__K, _difference_2__V], typing.Mapping[_difference_2__K, _difference_2__V]]) -> 'SortedMapDifference'[_difference_2__K, _difference_2__V]: ...
    _filterEntries_0__K = typing.TypeVar('_filterEntries_0__K')  # <K>
    _filterEntries_0__V = typing.TypeVar('_filterEntries_0__V')  # <V>
    _filterEntries_1__K = typing.TypeVar('_filterEntries_1__K')  # <K>
    _filterEntries_1__V = typing.TypeVar('_filterEntries_1__V')  # <V>
    _filterEntries_2__K = typing.TypeVar('_filterEntries_2__K')  # <K>
    _filterEntries_2__V = typing.TypeVar('_filterEntries_2__V')  # <V>
    _filterEntries_3__K = typing.TypeVar('_filterEntries_3__K')  # <K>
    _filterEntries_3__V = typing.TypeVar('_filterEntries_3__V')  # <V>
    @typing.overload
    @staticmethod
    def filterEntries(biMap: BiMap[_filterEntries_0__K, _filterEntries_0__V], predicate: typing.Union[com.google.common.base.Predicate[java.util.Map.Entry[_filterEntries_0__K, _filterEntries_0__V]], typing.Callable[[java.util.Map.Entry[_filterEntries_0__K, _filterEntries_0__V]], bool]]) -> BiMap[_filterEntries_0__K, _filterEntries_0__V]: ...
    @typing.overload
    @staticmethod
    def filterEntries(map: typing.Union[java.util.Map[_filterEntries_1__K, _filterEntries_1__V], typing.Mapping[_filterEntries_1__K, _filterEntries_1__V]], predicate: typing.Union[com.google.common.base.Predicate[java.util.Map.Entry[_filterEntries_1__K, _filterEntries_1__V]], typing.Callable[[java.util.Map.Entry[_filterEntries_1__K, _filterEntries_1__V]], bool]]) -> java.util.Map[_filterEntries_1__K, _filterEntries_1__V]: ...
    @typing.overload
    @staticmethod
    def filterEntries(navigableMap: java.util.NavigableMap[_filterEntries_2__K, _filterEntries_2__V], predicate: typing.Union[com.google.common.base.Predicate[java.util.Map.Entry[_filterEntries_2__K, _filterEntries_2__V]], typing.Callable[[java.util.Map.Entry[_filterEntries_2__K, _filterEntries_2__V]], bool]]) -> java.util.NavigableMap[_filterEntries_2__K, _filterEntries_2__V]: ...
    @typing.overload
    @staticmethod
    def filterEntries(sortedMap: java.util.SortedMap[_filterEntries_3__K, _filterEntries_3__V], predicate: typing.Union[com.google.common.base.Predicate[java.util.Map.Entry[_filterEntries_3__K, _filterEntries_3__V]], typing.Callable[[java.util.Map.Entry[_filterEntries_3__K, _filterEntries_3__V]], bool]]) -> java.util.SortedMap[_filterEntries_3__K, _filterEntries_3__V]: ...
    _filterKeys_0__K = typing.TypeVar('_filterKeys_0__K')  # <K>
    _filterKeys_0__V = typing.TypeVar('_filterKeys_0__V')  # <V>
    _filterKeys_1__K = typing.TypeVar('_filterKeys_1__K')  # <K>
    _filterKeys_1__V = typing.TypeVar('_filterKeys_1__V')  # <V>
    _filterKeys_2__K = typing.TypeVar('_filterKeys_2__K')  # <K>
    _filterKeys_2__V = typing.TypeVar('_filterKeys_2__V')  # <V>
    _filterKeys_3__K = typing.TypeVar('_filterKeys_3__K')  # <K>
    _filterKeys_3__V = typing.TypeVar('_filterKeys_3__V')  # <V>
    @typing.overload
    @staticmethod
    def filterKeys(biMap: BiMap[_filterKeys_0__K, _filterKeys_0__V], predicate: typing.Union[com.google.common.base.Predicate[_filterKeys_0__K], typing.Callable[[_filterKeys_0__K], bool]]) -> BiMap[_filterKeys_0__K, _filterKeys_0__V]: ...
    @typing.overload
    @staticmethod
    def filterKeys(map: typing.Union[java.util.Map[_filterKeys_1__K, _filterKeys_1__V], typing.Mapping[_filterKeys_1__K, _filterKeys_1__V]], predicate: typing.Union[com.google.common.base.Predicate[_filterKeys_1__K], typing.Callable[[_filterKeys_1__K], bool]]) -> java.util.Map[_filterKeys_1__K, _filterKeys_1__V]: ...
    @typing.overload
    @staticmethod
    def filterKeys(navigableMap: java.util.NavigableMap[_filterKeys_2__K, _filterKeys_2__V], predicate: typing.Union[com.google.common.base.Predicate[_filterKeys_2__K], typing.Callable[[_filterKeys_2__K], bool]]) -> java.util.NavigableMap[_filterKeys_2__K, _filterKeys_2__V]: ...
    @typing.overload
    @staticmethod
    def filterKeys(sortedMap: java.util.SortedMap[_filterKeys_3__K, _filterKeys_3__V], predicate: typing.Union[com.google.common.base.Predicate[_filterKeys_3__K], typing.Callable[[_filterKeys_3__K], bool]]) -> java.util.SortedMap[_filterKeys_3__K, _filterKeys_3__V]: ...
    _filterValues_0__K = typing.TypeVar('_filterValues_0__K')  # <K>
    _filterValues_0__V = typing.TypeVar('_filterValues_0__V')  # <V>
    _filterValues_1__K = typing.TypeVar('_filterValues_1__K')  # <K>
    _filterValues_1__V = typing.TypeVar('_filterValues_1__V')  # <V>
    _filterValues_2__K = typing.TypeVar('_filterValues_2__K')  # <K>
    _filterValues_2__V = typing.TypeVar('_filterValues_2__V')  # <V>
    _filterValues_3__K = typing.TypeVar('_filterValues_3__K')  # <K>
    _filterValues_3__V = typing.TypeVar('_filterValues_3__V')  # <V>
    @typing.overload
    @staticmethod
    def filterValues(biMap: BiMap[_filterValues_0__K, _filterValues_0__V], predicate: typing.Union[com.google.common.base.Predicate[_filterValues_0__V], typing.Callable[[_filterValues_0__V], bool]]) -> BiMap[_filterValues_0__K, _filterValues_0__V]: ...
    @typing.overload
    @staticmethod
    def filterValues(map: typing.Union[java.util.Map[_filterValues_1__K, _filterValues_1__V], typing.Mapping[_filterValues_1__K, _filterValues_1__V]], predicate: typing.Union[com.google.common.base.Predicate[_filterValues_1__V], typing.Callable[[_filterValues_1__V], bool]]) -> java.util.Map[_filterValues_1__K, _filterValues_1__V]: ...
    @typing.overload
    @staticmethod
    def filterValues(navigableMap: java.util.NavigableMap[_filterValues_2__K, _filterValues_2__V], predicate: typing.Union[com.google.common.base.Predicate[_filterValues_2__V], typing.Callable[[_filterValues_2__V], bool]]) -> java.util.NavigableMap[_filterValues_2__K, _filterValues_2__V]: ...
    @typing.overload
    @staticmethod
    def filterValues(sortedMap: java.util.SortedMap[_filterValues_3__K, _filterValues_3__V], predicate: typing.Union[com.google.common.base.Predicate[_filterValues_3__V], typing.Callable[[_filterValues_3__V], bool]]) -> java.util.SortedMap[_filterValues_3__K, _filterValues_3__V]: ...
    @staticmethod
    def fromProperties(properties: java.util.Properties) -> ImmutableMap[str, str]: ...
    _immutableEntry__K = typing.TypeVar('_immutableEntry__K')  # <K>
    _immutableEntry__V = typing.TypeVar('_immutableEntry__V')  # <V>
    @staticmethod
    def immutableEntry(k: _immutableEntry__K, v: _immutableEntry__V) -> java.util.Map.Entry[_immutableEntry__K, _immutableEntry__V]: ...
    _immutableEnumMap__K = typing.TypeVar('_immutableEnumMap__K', bound=java.lang.Enum)  # <K>
    _immutableEnumMap__V = typing.TypeVar('_immutableEnumMap__V')  # <V>
    @staticmethod
    def immutableEnumMap(map: typing.Union[java.util.Map[_immutableEnumMap__K, _immutableEnumMap__V], typing.Mapping[_immutableEnumMap__K, _immutableEnumMap__V]]) -> ImmutableMap[_immutableEnumMap__K, _immutableEnumMap__V]: ...
    _newConcurrentMap__K = typing.TypeVar('_newConcurrentMap__K')  # <K>
    _newConcurrentMap__V = typing.TypeVar('_newConcurrentMap__V')  # <V>
    @staticmethod
    def newConcurrentMap() -> java.util.concurrent.ConcurrentMap[_newConcurrentMap__K, _newConcurrentMap__V]: ...
    _newEnumMap_0__K = typing.TypeVar('_newEnumMap_0__K', bound=java.lang.Enum)  # <K>
    _newEnumMap_0__V = typing.TypeVar('_newEnumMap_0__V')  # <V>
    _newEnumMap_1__K = typing.TypeVar('_newEnumMap_1__K', bound=java.lang.Enum)  # <K>
    _newEnumMap_1__V = typing.TypeVar('_newEnumMap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def newEnumMap(class_: typing.Type[_newEnumMap_0__K]) -> java.util.EnumMap[_newEnumMap_0__K, _newEnumMap_0__V]: ...
    @typing.overload
    @staticmethod
    def newEnumMap(map: typing.Union[java.util.Map[_newEnumMap_1__K, _newEnumMap_1__V], typing.Mapping[_newEnumMap_1__K, _newEnumMap_1__V]]) -> java.util.EnumMap[_newEnumMap_1__K, _newEnumMap_1__V]: ...
    _newHashMap_0__K = typing.TypeVar('_newHashMap_0__K')  # <K>
    _newHashMap_0__V = typing.TypeVar('_newHashMap_0__V')  # <V>
    _newHashMap_1__K = typing.TypeVar('_newHashMap_1__K')  # <K>
    _newHashMap_1__V = typing.TypeVar('_newHashMap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def newHashMap() -> java.util.HashMap[_newHashMap_0__K, _newHashMap_0__V]: ...
    @typing.overload
    @staticmethod
    def newHashMap(map: typing.Union[java.util.Map[_newHashMap_1__K, _newHashMap_1__V], typing.Mapping[_newHashMap_1__K, _newHashMap_1__V]]) -> java.util.HashMap[_newHashMap_1__K, _newHashMap_1__V]: ...
    _newHashMapWithExpectedSize__K = typing.TypeVar('_newHashMapWithExpectedSize__K')  # <K>
    _newHashMapWithExpectedSize__V = typing.TypeVar('_newHashMapWithExpectedSize__V')  # <V>
    @staticmethod
    def newHashMapWithExpectedSize(int: int) -> java.util.HashMap[_newHashMapWithExpectedSize__K, _newHashMapWithExpectedSize__V]: ...
    _newIdentityHashMap__K = typing.TypeVar('_newIdentityHashMap__K')  # <K>
    _newIdentityHashMap__V = typing.TypeVar('_newIdentityHashMap__V')  # <V>
    @staticmethod
    def newIdentityHashMap() -> java.util.IdentityHashMap[_newIdentityHashMap__K, _newIdentityHashMap__V]: ...
    _newLinkedHashMap_0__K = typing.TypeVar('_newLinkedHashMap_0__K')  # <K>
    _newLinkedHashMap_0__V = typing.TypeVar('_newLinkedHashMap_0__V')  # <V>
    _newLinkedHashMap_1__K = typing.TypeVar('_newLinkedHashMap_1__K')  # <K>
    _newLinkedHashMap_1__V = typing.TypeVar('_newLinkedHashMap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def newLinkedHashMap() -> java.util.LinkedHashMap[_newLinkedHashMap_0__K, _newLinkedHashMap_0__V]: ...
    @typing.overload
    @staticmethod
    def newLinkedHashMap(map: typing.Union[java.util.Map[_newLinkedHashMap_1__K, _newLinkedHashMap_1__V], typing.Mapping[_newLinkedHashMap_1__K, _newLinkedHashMap_1__V]]) -> java.util.LinkedHashMap[_newLinkedHashMap_1__K, _newLinkedHashMap_1__V]: ...
    _newLinkedHashMapWithExpectedSize__K = typing.TypeVar('_newLinkedHashMapWithExpectedSize__K')  # <K>
    _newLinkedHashMapWithExpectedSize__V = typing.TypeVar('_newLinkedHashMapWithExpectedSize__V')  # <V>
    @staticmethod
    def newLinkedHashMapWithExpectedSize(int: int) -> java.util.LinkedHashMap[_newLinkedHashMapWithExpectedSize__K, _newLinkedHashMapWithExpectedSize__V]: ...
    _newTreeMap_0__K = typing.TypeVar('_newTreeMap_0__K', bound=java.lang.Comparable)  # <K>
    _newTreeMap_0__V = typing.TypeVar('_newTreeMap_0__V')  # <V>
    _newTreeMap_1__C = typing.TypeVar('_newTreeMap_1__C')  # <C>
    _newTreeMap_1__K = typing.TypeVar('_newTreeMap_1__K')  # <K>
    _newTreeMap_1__V = typing.TypeVar('_newTreeMap_1__V')  # <V>
    _newTreeMap_2__K = typing.TypeVar('_newTreeMap_2__K')  # <K>
    _newTreeMap_2__V = typing.TypeVar('_newTreeMap_2__V')  # <V>
    @typing.overload
    @staticmethod
    def newTreeMap() -> java.util.TreeMap[_newTreeMap_0__K, _newTreeMap_0__V]: ...
    @typing.overload
    @staticmethod
    def newTreeMap(comparator: typing.Union[java.util.Comparator[_newTreeMap_1__C], typing.Callable[[_newTreeMap_1__C, _newTreeMap_1__C], int]]) -> java.util.TreeMap[_newTreeMap_1__K, _newTreeMap_1__V]: ...
    @typing.overload
    @staticmethod
    def newTreeMap(sortedMap: java.util.SortedMap[_newTreeMap_2__K, _newTreeMap_2__V]) -> java.util.TreeMap[_newTreeMap_2__K, _newTreeMap_2__V]: ...
    _subMap__K = typing.TypeVar('_subMap__K', bound=java.lang.Comparable)  # <K>
    _subMap__V = typing.TypeVar('_subMap__V')  # <V>
    @staticmethod
    def subMap(navigableMap: java.util.NavigableMap[_subMap__K, _subMap__V], range: 'Range'[_subMap__K]) -> java.util.NavigableMap[_subMap__K, _subMap__V]: ...
    _synchronizedBiMap__K = typing.TypeVar('_synchronizedBiMap__K')  # <K>
    _synchronizedBiMap__V = typing.TypeVar('_synchronizedBiMap__V')  # <V>
    @staticmethod
    def synchronizedBiMap(biMap: BiMap[_synchronizedBiMap__K, _synchronizedBiMap__V]) -> BiMap[_synchronizedBiMap__K, _synchronizedBiMap__V]: ...
    _synchronizedNavigableMap__K = typing.TypeVar('_synchronizedNavigableMap__K')  # <K>
    _synchronizedNavigableMap__V = typing.TypeVar('_synchronizedNavigableMap__V')  # <V>
    @staticmethod
    def synchronizedNavigableMap(navigableMap: java.util.NavigableMap[_synchronizedNavigableMap__K, _synchronizedNavigableMap__V]) -> java.util.NavigableMap[_synchronizedNavigableMap__K, _synchronizedNavigableMap__V]: ...
    _toImmutableEnumMap_0__T = typing.TypeVar('_toImmutableEnumMap_0__T')  # <T>
    _toImmutableEnumMap_0__K = typing.TypeVar('_toImmutableEnumMap_0__K', bound=java.lang.Enum)  # <K>
    _toImmutableEnumMap_0__V = typing.TypeVar('_toImmutableEnumMap_0__V')  # <V>
    _toImmutableEnumMap_1__T = typing.TypeVar('_toImmutableEnumMap_1__T')  # <T>
    _toImmutableEnumMap_1__K = typing.TypeVar('_toImmutableEnumMap_1__K', bound=java.lang.Enum)  # <K>
    _toImmutableEnumMap_1__V = typing.TypeVar('_toImmutableEnumMap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def toImmutableEnumMap(function: typing.Union[java.util.function.Function[_toImmutableEnumMap_0__T, _toImmutableEnumMap_0__K], typing.Callable[[_toImmutableEnumMap_0__T], _toImmutableEnumMap_0__K]], function2: typing.Union[java.util.function.Function[_toImmutableEnumMap_0__T, _toImmutableEnumMap_0__V], typing.Callable[[_toImmutableEnumMap_0__T], _toImmutableEnumMap_0__V]]) -> java.util.stream.Collector[_toImmutableEnumMap_0__T, typing.Any, ImmutableMap[_toImmutableEnumMap_0__K, _toImmutableEnumMap_0__V]]: ...
    @typing.overload
    @staticmethod
    def toImmutableEnumMap(function: typing.Union[java.util.function.Function[_toImmutableEnumMap_1__T, _toImmutableEnumMap_1__K], typing.Callable[[_toImmutableEnumMap_1__T], _toImmutableEnumMap_1__K]], function2: typing.Union[java.util.function.Function[_toImmutableEnumMap_1__T, _toImmutableEnumMap_1__V], typing.Callable[[_toImmutableEnumMap_1__T], _toImmutableEnumMap_1__V]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toImmutableEnumMap_1__V], typing.Callable]) -> java.util.stream.Collector[_toImmutableEnumMap_1__T, typing.Any, ImmutableMap[_toImmutableEnumMap_1__K, _toImmutableEnumMap_1__V]]: ...
    _toMap_0__K = typing.TypeVar('_toMap_0__K')  # <K>
    _toMap_0__V = typing.TypeVar('_toMap_0__V')  # <V>
    _toMap_1__K = typing.TypeVar('_toMap_1__K')  # <K>
    _toMap_1__V = typing.TypeVar('_toMap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def toMap(iterable: java.lang.Iterable[_toMap_0__K], function: typing.Union[com.google.common.base.Function[_toMap_0__K, _toMap_0__V], typing.Callable[[_toMap_0__K], _toMap_0__V]]) -> ImmutableMap[_toMap_0__K, _toMap_0__V]: ...
    @typing.overload
    @staticmethod
    def toMap(iterator: java.util.Iterator[_toMap_1__K], function: typing.Union[com.google.common.base.Function[_toMap_1__K, _toMap_1__V], typing.Callable[[_toMap_1__K], _toMap_1__V]]) -> ImmutableMap[_toMap_1__K, _toMap_1__V]: ...
    _transformEntries_0__K = typing.TypeVar('_transformEntries_0__K')  # <K>
    _transformEntries_0__V1 = typing.TypeVar('_transformEntries_0__V1')  # <V1>
    _transformEntries_0__V2 = typing.TypeVar('_transformEntries_0__V2')  # <V2>
    _transformEntries_1__K = typing.TypeVar('_transformEntries_1__K')  # <K>
    _transformEntries_1__V1 = typing.TypeVar('_transformEntries_1__V1')  # <V1>
    _transformEntries_1__V2 = typing.TypeVar('_transformEntries_1__V2')  # <V2>
    _transformEntries_2__K = typing.TypeVar('_transformEntries_2__K')  # <K>
    _transformEntries_2__V1 = typing.TypeVar('_transformEntries_2__V1')  # <V1>
    _transformEntries_2__V2 = typing.TypeVar('_transformEntries_2__V2')  # <V2>
    @typing.overload
    @staticmethod
    def transformEntries(map: typing.Union[java.util.Map[_transformEntries_0__K, _transformEntries_0__V1], typing.Mapping[_transformEntries_0__K, _transformEntries_0__V1]], entryTransformer: typing.Union['Maps.EntryTransformer'[_transformEntries_0__K, _transformEntries_0__V1, _transformEntries_0__V2], typing.Callable[[_transformEntries_0__K, _transformEntries_0__V1], _transformEntries_0__V2]]) -> java.util.Map[_transformEntries_0__K, _transformEntries_0__V2]: ...
    @typing.overload
    @staticmethod
    def transformEntries(navigableMap: java.util.NavigableMap[_transformEntries_1__K, _transformEntries_1__V1], entryTransformer: typing.Union['Maps.EntryTransformer'[_transformEntries_1__K, _transformEntries_1__V1, _transformEntries_1__V2], typing.Callable[[_transformEntries_1__K, _transformEntries_1__V1], _transformEntries_1__V2]]) -> java.util.NavigableMap[_transformEntries_1__K, _transformEntries_1__V2]: ...
    @typing.overload
    @staticmethod
    def transformEntries(sortedMap: java.util.SortedMap[_transformEntries_2__K, _transformEntries_2__V1], entryTransformer: typing.Union['Maps.EntryTransformer'[_transformEntries_2__K, _transformEntries_2__V1, _transformEntries_2__V2], typing.Callable[[_transformEntries_2__K, _transformEntries_2__V1], _transformEntries_2__V2]]) -> java.util.SortedMap[_transformEntries_2__K, _transformEntries_2__V2]: ...
    _transformValues_0__K = typing.TypeVar('_transformValues_0__K')  # <K>
    _transformValues_0__V1 = typing.TypeVar('_transformValues_0__V1')  # <V1>
    _transformValues_0__V2 = typing.TypeVar('_transformValues_0__V2')  # <V2>
    _transformValues_1__K = typing.TypeVar('_transformValues_1__K')  # <K>
    _transformValues_1__V1 = typing.TypeVar('_transformValues_1__V1')  # <V1>
    _transformValues_1__V2 = typing.TypeVar('_transformValues_1__V2')  # <V2>
    _transformValues_2__K = typing.TypeVar('_transformValues_2__K')  # <K>
    _transformValues_2__V1 = typing.TypeVar('_transformValues_2__V1')  # <V1>
    _transformValues_2__V2 = typing.TypeVar('_transformValues_2__V2')  # <V2>
    @typing.overload
    @staticmethod
    def transformValues(map: typing.Union[java.util.Map[_transformValues_0__K, _transformValues_0__V1], typing.Mapping[_transformValues_0__K, _transformValues_0__V1]], function: typing.Union[com.google.common.base.Function[_transformValues_0__V1, _transformValues_0__V2], typing.Callable[[_transformValues_0__V1], _transformValues_0__V2]]) -> java.util.Map[_transformValues_0__K, _transformValues_0__V2]: ...
    @typing.overload
    @staticmethod
    def transformValues(navigableMap: java.util.NavigableMap[_transformValues_1__K, _transformValues_1__V1], function: typing.Union[com.google.common.base.Function[_transformValues_1__V1, _transformValues_1__V2], typing.Callable[[_transformValues_1__V1], _transformValues_1__V2]]) -> java.util.NavigableMap[_transformValues_1__K, _transformValues_1__V2]: ...
    @typing.overload
    @staticmethod
    def transformValues(sortedMap: java.util.SortedMap[_transformValues_2__K, _transformValues_2__V1], function: typing.Union[com.google.common.base.Function[_transformValues_2__V1, _transformValues_2__V2], typing.Callable[[_transformValues_2__V1], _transformValues_2__V2]]) -> java.util.SortedMap[_transformValues_2__K, _transformValues_2__V2]: ...
    _uniqueIndex_0__K = typing.TypeVar('_uniqueIndex_0__K')  # <K>
    _uniqueIndex_0__V = typing.TypeVar('_uniqueIndex_0__V')  # <V>
    _uniqueIndex_1__K = typing.TypeVar('_uniqueIndex_1__K')  # <K>
    _uniqueIndex_1__V = typing.TypeVar('_uniqueIndex_1__V')  # <V>
    @typing.overload
    @staticmethod
    def uniqueIndex(iterable: java.lang.Iterable[_uniqueIndex_0__V], function: typing.Union[com.google.common.base.Function[_uniqueIndex_0__V, _uniqueIndex_0__K], typing.Callable[[_uniqueIndex_0__V], _uniqueIndex_0__K]]) -> ImmutableMap[_uniqueIndex_0__K, _uniqueIndex_0__V]: ...
    @typing.overload
    @staticmethod
    def uniqueIndex(iterator: java.util.Iterator[_uniqueIndex_1__V], function: typing.Union[com.google.common.base.Function[_uniqueIndex_1__V, _uniqueIndex_1__K], typing.Callable[[_uniqueIndex_1__V], _uniqueIndex_1__K]]) -> ImmutableMap[_uniqueIndex_1__K, _uniqueIndex_1__V]: ...
    _unmodifiableBiMap__K = typing.TypeVar('_unmodifiableBiMap__K')  # <K>
    _unmodifiableBiMap__V = typing.TypeVar('_unmodifiableBiMap__V')  # <V>
    @staticmethod
    def unmodifiableBiMap(biMap: BiMap[_unmodifiableBiMap__K, _unmodifiableBiMap__V]) -> BiMap[_unmodifiableBiMap__K, _unmodifiableBiMap__V]: ...
    _unmodifiableNavigableMap__K = typing.TypeVar('_unmodifiableNavigableMap__K')  # <K>
    _unmodifiableNavigableMap__V = typing.TypeVar('_unmodifiableNavigableMap__V')  # <V>
    @staticmethod
    def unmodifiableNavigableMap(navigableMap: java.util.NavigableMap[_unmodifiableNavigableMap__K, _unmodifiableNavigableMap__V]) -> java.util.NavigableMap[_unmodifiableNavigableMap__K, _unmodifiableNavigableMap__V]: ...
    class EntryTransformer(typing.Generic[_Maps__EntryTransformer__K, _Maps__EntryTransformer__V1, _Maps__EntryTransformer__V2]):
        def transformEntry(self, k: _Maps__EntryTransformer__K, v1: _Maps__EntryTransformer__V1) -> _Maps__EntryTransformer__V2: ...

_MinMaxPriorityQueue__Builder__B = typing.TypeVar('_MinMaxPriorityQueue__Builder__B')  # <B>
_MinMaxPriorityQueue__E = typing.TypeVar('_MinMaxPriorityQueue__E')  # <E>
class MinMaxPriorityQueue(java.util.AbstractQueue[_MinMaxPriorityQueue__E], typing.Generic[_MinMaxPriorityQueue__E]):
    """
    :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src`<E> extends AbstractQueue<E>
    
        A double-ended priority queue, which provides constant-time access to both its least element and its greatest element,
        as determined by the queue's specified comparator. If no comparator is given at creation time, the natural order of
        elements is used. If no maximum size is given at creation time, the queue is unbounded.
    
        Usage example:
    
        .. code-block: java
        
         MinMaxPriorityQueue<User> users = MinMaxPriorityQueue.orderedBy(userComparator)
             .maximumSize(1000)
             .create();
         
    
        As a null it functions exactly as a null: its head element -- the implicit target of the methods
        :meth:`~com.google.common.collect.MinMaxPriorityQueue.peek`, :meth:`~com.google.common.collect.MinMaxPriorityQueue.poll`
        and null -- is defined as the *least* element in the queue according to the queue's comparator. But unlike a regular
        priority queue, the methods :meth:`~com.google.common.collect.MinMaxPriorityQueue.peekLast`,
        :meth:`~com.google.common.collect.MinMaxPriorityQueue.pollLast` and
        :meth:`~com.google.common.collect.MinMaxPriorityQueue.removeLast` are also provided, to act on the *greatest* element in
        the queue instead.
    
        A min-max priority queue can be configured with a maximum size. If so, each time the size of the queue exceeds that
        value, the queue automatically removes its greatest element according to its comparator (which might be the element that
        was just added). This is different from conventional bounded queues, which either block or reject new elements when
        full.
    
        This implementation is based on the `min-max heap <http://portal.acm.org/citation.cfm?id=6621>` developed by Atkinson,
        et al. Unlike many other double-ended priority queues, it stores elements in a single array, as compact as the
        traditional heap data structure used in null.
    
        This class is not thread-safe, and does not accept null elements.
    
        *Performance notes:*
    
          - If you only access one end of the queue, and do use a maximum size, this class will perform significantly worse than a
            :code:`PriorityQueue` with manual eviction above the maximum size. In many cases
            :meth:`~com.google.common.collect.Ordering.leastOf` may work for your use case with significantly improved (and
            asymptotically superior) performance.
          - The retrieval operations :meth:`~com.google.common.collect.MinMaxPriorityQueue.peek`,
            :meth:`~com.google.common.collect.MinMaxPriorityQueue.peekFirst`,
            :meth:`~com.google.common.collect.MinMaxPriorityQueue.peekLast`, null, and
            :meth:`~com.google.common.collect.MinMaxPriorityQueue.size` are constant-time.
          - The enqueuing and dequeuing operations (:meth:`~com.google.common.collect.MinMaxPriorityQueue.offer`,
            :meth:`~com.google.common.collect.MinMaxPriorityQueue.add`, and all the forms of
            :meth:`~com.google.common.collect.MinMaxPriorityQueue.poll` and null) run in :code:`O(log n) time`.
          - The null and null operations require linear (:code:`O(n)`) time.
          - If you only access one end of the queue, and don't use a maximum size, this class is functionally equivalent to null,
            but significantly slower.
    
    
        Since:
            8.0
    """
    def add(self, e: _MinMaxPriorityQueue__E) -> bool: ...
    def addAll(self, collection: typing.Union[java.util.Collection[_MinMaxPriorityQueue__E], typing.Sequence[_MinMaxPriorityQueue__E]]) -> bool: ...
    def clear(self) -> None: ...
    def comparator(self) -> java.util.Comparator[_MinMaxPriorityQueue__E]: ...
    _create_0__E = typing.TypeVar('_create_0__E', bound=java.lang.Comparable)  # <E>
    _create_1__E = typing.TypeVar('_create_1__E', bound=java.lang.Comparable)  # <E>
    @typing.overload
    @staticmethod
    def create() -> 'MinMaxPriorityQueue'[_create_0__E]: ...
    @typing.overload
    @staticmethod
    def create(iterable: java.lang.Iterable[_create_1__E]) -> 'MinMaxPriorityQueue'[_create_1__E]: ...
    @staticmethod
    def expectedSize(int: int) -> 'MinMaxPriorityQueue.Builder'[java.lang.Comparable]: ...
    def iterator(self) -> java.util.Iterator[_MinMaxPriorityQueue__E]: ...
    @staticmethod
    def maximumSize(int: int) -> 'MinMaxPriorityQueue.Builder'[java.lang.Comparable]: ...
    def offer(self, e: _MinMaxPriorityQueue__E) -> bool: ...
    _orderedBy__B = typing.TypeVar('_orderedBy__B')  # <B>
    @staticmethod
    def orderedBy(comparator: typing.Union[java.util.Comparator[_orderedBy__B], typing.Callable[[_orderedBy__B, _orderedBy__B], int]]) -> 'MinMaxPriorityQueue.Builder'[_orderedBy__B]: ...
    def peek(self) -> _MinMaxPriorityQueue__E: ...
    def peekFirst(self) -> _MinMaxPriorityQueue__E: ...
    def peekLast(self) -> _MinMaxPriorityQueue__E: ...
    def poll(self) -> _MinMaxPriorityQueue__E: ...
    def pollFirst(self) -> _MinMaxPriorityQueue__E: ...
    def pollLast(self) -> _MinMaxPriorityQueue__E: ...
    def removeFirst(self) -> _MinMaxPriorityQueue__E: ...
    def removeLast(self) -> _MinMaxPriorityQueue__E: ...
    def size(self) -> int: ...
    _toArray_0__T = typing.TypeVar('_toArray_0__T')  # <T>
    _toArray_2__T = typing.TypeVar('_toArray_2__T')  # <T>
    @typing.overload
    def toArray(self, intFunction: typing.Union[java.util.function.IntFunction[typing.List[_toArray_0__T]], typing.Callable[[int], typing.List[_toArray_0__T]]]) -> typing.List[_toArray_0__T]: ...
    @typing.overload
    def toArray(self) -> typing.List[typing.Any]: ...
    @typing.overload
    def toArray(self, tArray: typing.List[_toArray_2__T]) -> typing.List[_toArray_2__T]: ...
    class Builder(typing.Generic[_MinMaxPriorityQueue__Builder__B]):
        _create_0__T = typing.TypeVar('_create_0__T')  # <T>
        _create_1__T = typing.TypeVar('_create_1__T')  # <T>
        @typing.overload
        def create(self) -> 'MinMaxPriorityQueue'[_create_0__T]: ...
        @typing.overload
        def create(self, iterable: java.lang.Iterable[_create_1__T]) -> 'MinMaxPriorityQueue'[_create_1__T]: ...
        def expectedSize(self, int: int) -> 'MinMaxPriorityQueue.Builder'[_MinMaxPriorityQueue__Builder__B]: ...
        def maximumSize(self, int: int) -> 'MinMaxPriorityQueue.Builder'[_MinMaxPriorityQueue__Builder__B]: ...

class MoreCollectors:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Collectors not present in :code:`java.util.stream.Collectors` that are not otherwise associated with a
        :code:`com.google.common` type.
    
        Since:
            21.0
    """
    _onlyElement__T = typing.TypeVar('_onlyElement__T')  # <T>
    @staticmethod
    def onlyElement() -> java.util.stream.Collector[_onlyElement__T, typing.Any, _onlyElement__T]: ...
    _toOptional__T = typing.TypeVar('_toOptional__T')  # <T>
    @staticmethod
    def toOptional() -> java.util.stream.Collector[_toOptional__T, typing.Any, java.util.Optional[_toOptional__T]]: ...

_Multimap__K = typing.TypeVar('_Multimap__K')  # <K>
_Multimap__V = typing.TypeVar('_Multimap__V')  # <V>
class Multimap(typing.Generic[_Multimap__K, _Multimap__V]):
    """
    @DoNotMock(value="Use ImmutableMultimap, HashMultimap, or another implementation") :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<K,V>
    
        A collection that maps keys to values, similar to null, but in which each key may be associated with *multiple* values.
        You can visualize the contents of a multimap either as a map from keys to *nonempty* collections of values:
    
          - a â†’ 1, 2
          - b â†’ 3
    
        ... or as a single "flattened" collection of key-value pairs:
    
          - a â†’ 1
          - a â†’ 2
          - b â†’ 3
    
    
        **Important:** although the first interpretation resembles how most multimaps are *implemented*, the design of the
        :code:`Multimap` API is based on the *second* form. So, using the multimap shown above as an example, the
        :meth:`~com.google.common.collect.Multimap.size` is :code:`3`, not :code:`2`, and the
        :meth:`~com.google.common.collect.Multimap.values` collection is :code:`[1, 2, 3]`, not :code:`[[1, 2], [3]]`. For those
        times when the first style is more useful, use the multimap's :meth:`~com.google.common.collect.Multimap.asMap` view (or
        create a :code:`Map<K, Collection<V>>` in the first place).
    
        Example
    -------
    
    
        The following code:
    
        .. code-block: java
        
         ListMultimap<String, String> multimap = ArrayListMultimap.create();
         for (President pres : US_PRESIDENTS_IN_ORDER) {
           multimap.put(pres.firstName(), pres.lastName());
         }
         for (String firstName : multimap.keySet()) {
           List<String> lastNames = multimap.get(firstName);
           out.println(firstName + ": " + lastNames);
         }
         
        ... produces output such as:
    
        .. code-block: java
        
         Zachary: [Taylor]
         John: [Adams, Adams, Tyler, Kennedy]  // Remember, Quincy!
         George: [Washington, Bush, Bush]
         Grover: [Cleveland, Cleveland]        // Two, non-consecutive terms, rep'ing NJ!
         ...
         
    
        Views
    -----
    
    
        Much of the power of the multimap API comes from the *view collections* it provides. These always reflect the latest
        state of the multimap itself. When they support modification, the changes are *write-through* (they automatically update
        the backing multimap). These view collections are:
    
          - :meth:`~com.google.common.collect.Multimap.asMap`, mentioned above
          - :meth:`~com.google.common.collect.Multimap.keys`, :meth:`~com.google.common.collect.Multimap.keySet`,
            :meth:`~com.google.common.collect.Multimap.values`, :meth:`~com.google.common.collect.Multimap.entries`, which are
            similar to the corresponding view collections of null
          - and, notably, even the collection returned by :meth:`~com.google.common.collect.Multimap.get` is an active view of the
            values corresponding to :code:`key`
    
    
        The collections returned by the :meth:`~com.google.common.collect.Multimap.replaceValues` and
        :meth:`~com.google.common.collect.Multimap.removeAll` methods, which contain values that have just been removed from the
        multimap, are naturally *not* views.
    
        Subinterfaces
    -------------
    
    
        Instead of using the :code:`Multimap` interface directly, prefer the subinterfaces
        :class:`~com.google.common.collect.ListMultimap` and :class:`~com.google.common.collect.SetMultimap`. These take their
        names from the fact that the collections they return from :code:`get` behave like (and, of course, implement) null and
        null, respectively.
    
        For example, the "presidents" code snippet above used a :code:`ListMultimap`; if it had used a :code:`SetMultimap`
        instead, two presidents would have vanished, and last names might or might not appear in chronological order.
    
        **Warning:** instances of type :code:`Multimap` may not implement null in the way you expect. Multimaps containing the
        same key-value pairs, even in the same order, may or may not be equal and may or may not have the same :code:`hashCode`.
        The recommended subinterfaces provide much stronger guarantees.
    
        Comparison to a map of collections
    ----------------------------------
    
    
        Multimaps are commonly used in places where a :code:`Map<K, Collection<V>>` would otherwise have appeared. The
        differences include:
    
          - There is no need to populate an empty collection before adding an entry with
            :meth:`~com.google.common.collect.Multimap.put`.
          - :code:`get` never returns :code:`null`, only an empty collection.
          - A key is contained in the multimap if and only if it maps to at least one value. Any operation that causes a key to have
            zero associated values has the effect of *removing* that key from the multimap.
          - The total entry count is available as :meth:`~com.google.common.collect.Multimap.size`.
          - Many complex operations become easier; for example, :code:`Collections.min(multimap.values())` finds the smallest value
            across all keys.
    
    
        Implementations
    ---------------
    
    
        As always, prefer the immutable implementations, :class:`~com.google.common.collect.ImmutableListMultimap` and
        :class:`~com.google.common.collect.ImmutableSetMultimap`. General-purpose mutable implementations are listed above under
        "All Known Implementing Classes". You can also create a *custom* multimap, backed by any :code:`Map` and null types,
        using the :meth:`~com.google.common.collect.Multimaps.newMultimap` family of methods. Finally, another popular way to
        obtain a multimap is using :meth:`~com.google.common.collect.Multimaps.index`. See the
        :class:`~com.google.common.collect.Multimaps` class for these and other static utilities related to multimaps.
    
        Other Notes
    -----------
    
    
        As with :code:`Map`, the behavior of a :code:`Multimap` is not specified if key objects already present in the multimap
        change in a manner that affects :code:`equals` comparisons. Use caution if mutable objects are used as keys in a
        :code:`Multimap`.
    
        All methods that modify the multimap are optional. The view collections returned by the multimap may or may not be
        modifiable. Any modification method that is not supported will throw null.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    def asMap(self) -> java.util.Map[_Multimap__K, java.util.Collection[_Multimap__V]]: ...
    def clear(self) -> None: ...
    def containsEntry(self, object: typing.Any, object2: typing.Any) -> bool: ...
    def containsKey(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    def entries(self) -> java.util.Collection[java.util.Map.Entry[_Multimap__K, _Multimap__V]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def forEach(self, biConsumer: typing.Union[java.util.function.BiConsumer[_Multimap__K, _Multimap__V], typing.Callable[[_Multimap__K, _Multimap__V], None]]) -> None: ...
    def get(self, k: _Multimap__K) -> java.util.Collection[_Multimap__V]: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def keySet(self) -> java.util.Set[_Multimap__K]: ...
    def keys(self) -> 'Multiset'[_Multimap__K]: ...
    def put(self, k: _Multimap__K, v: _Multimap__V) -> bool: ...
    @typing.overload
    def putAll(self, multimap: 'Multimap'[_Multimap__K, _Multimap__V]) -> bool: ...
    @typing.overload
    def putAll(self, k: _Multimap__K, iterable: java.lang.Iterable[_Multimap__V]) -> bool: ...
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...
    def removeAll(self, object: typing.Any) -> java.util.Collection[_Multimap__V]: ...
    def replaceValues(self, k: _Multimap__K, iterable: java.lang.Iterable[_Multimap__V]) -> java.util.Collection[_Multimap__V]: ...
    def size(self) -> int: ...
    def values(self) -> java.util.Collection[_Multimap__V]: ...

class Multimaps:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Provides static methods acting on or generating a :code:`Multimap`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    _asMap_0__K = typing.TypeVar('_asMap_0__K')  # <K>
    _asMap_0__V = typing.TypeVar('_asMap_0__V')  # <V>
    _asMap_1__K = typing.TypeVar('_asMap_1__K')  # <K>
    _asMap_1__V = typing.TypeVar('_asMap_1__V')  # <V>
    _asMap_2__K = typing.TypeVar('_asMap_2__K')  # <K>
    _asMap_2__V = typing.TypeVar('_asMap_2__V')  # <V>
    _asMap_3__K = typing.TypeVar('_asMap_3__K')  # <K>
    _asMap_3__V = typing.TypeVar('_asMap_3__V')  # <V>
    @typing.overload
    @staticmethod
    def asMap(listMultimap: 'ListMultimap'[_asMap_0__K, _asMap_0__V]) -> java.util.Map[_asMap_0__K, java.util.List[_asMap_0__V]]: ...
    @typing.overload
    @staticmethod
    def asMap(multimap: Multimap[_asMap_1__K, _asMap_1__V]) -> java.util.Map[_asMap_1__K, java.util.Collection[_asMap_1__V]]: ...
    @typing.overload
    @staticmethod
    def asMap(setMultimap: 'SetMultimap'[_asMap_2__K, _asMap_2__V]) -> java.util.Map[_asMap_2__K, java.util.Set[_asMap_2__V]]: ...
    @typing.overload
    @staticmethod
    def asMap(sortedSetMultimap: 'SortedSetMultimap'[_asMap_3__K, _asMap_3__V]) -> java.util.Map[_asMap_3__K, java.util.SortedSet[_asMap_3__V]]: ...
    _filterEntries_0__K = typing.TypeVar('_filterEntries_0__K')  # <K>
    _filterEntries_0__V = typing.TypeVar('_filterEntries_0__V')  # <V>
    _filterEntries_1__K = typing.TypeVar('_filterEntries_1__K')  # <K>
    _filterEntries_1__V = typing.TypeVar('_filterEntries_1__V')  # <V>
    @typing.overload
    @staticmethod
    def filterEntries(multimap: Multimap[_filterEntries_0__K, _filterEntries_0__V], predicate: typing.Union[com.google.common.base.Predicate[java.util.Map.Entry[_filterEntries_0__K, _filterEntries_0__V]], typing.Callable[[java.util.Map.Entry[_filterEntries_0__K, _filterEntries_0__V]], bool]]) -> Multimap[_filterEntries_0__K, _filterEntries_0__V]: ...
    @typing.overload
    @staticmethod
    def filterEntries(setMultimap: 'SetMultimap'[_filterEntries_1__K, _filterEntries_1__V], predicate: typing.Union[com.google.common.base.Predicate[java.util.Map.Entry[_filterEntries_1__K, _filterEntries_1__V]], typing.Callable[[java.util.Map.Entry[_filterEntries_1__K, _filterEntries_1__V]], bool]]) -> 'SetMultimap'[_filterEntries_1__K, _filterEntries_1__V]: ...
    _filterKeys_0__K = typing.TypeVar('_filterKeys_0__K')  # <K>
    _filterKeys_0__V = typing.TypeVar('_filterKeys_0__V')  # <V>
    _filterKeys_1__K = typing.TypeVar('_filterKeys_1__K')  # <K>
    _filterKeys_1__V = typing.TypeVar('_filterKeys_1__V')  # <V>
    _filterKeys_2__K = typing.TypeVar('_filterKeys_2__K')  # <K>
    _filterKeys_2__V = typing.TypeVar('_filterKeys_2__V')  # <V>
    @typing.overload
    @staticmethod
    def filterKeys(listMultimap: 'ListMultimap'[_filterKeys_0__K, _filterKeys_0__V], predicate: typing.Union[com.google.common.base.Predicate[_filterKeys_0__K], typing.Callable[[_filterKeys_0__K], bool]]) -> 'ListMultimap'[_filterKeys_0__K, _filterKeys_0__V]: ...
    @typing.overload
    @staticmethod
    def filterKeys(multimap: Multimap[_filterKeys_1__K, _filterKeys_1__V], predicate: typing.Union[com.google.common.base.Predicate[_filterKeys_1__K], typing.Callable[[_filterKeys_1__K], bool]]) -> Multimap[_filterKeys_1__K, _filterKeys_1__V]: ...
    @typing.overload
    @staticmethod
    def filterKeys(setMultimap: 'SetMultimap'[_filterKeys_2__K, _filterKeys_2__V], predicate: typing.Union[com.google.common.base.Predicate[_filterKeys_2__K], typing.Callable[[_filterKeys_2__K], bool]]) -> 'SetMultimap'[_filterKeys_2__K, _filterKeys_2__V]: ...
    _filterValues_0__K = typing.TypeVar('_filterValues_0__K')  # <K>
    _filterValues_0__V = typing.TypeVar('_filterValues_0__V')  # <V>
    _filterValues_1__K = typing.TypeVar('_filterValues_1__K')  # <K>
    _filterValues_1__V = typing.TypeVar('_filterValues_1__V')  # <V>
    @typing.overload
    @staticmethod
    def filterValues(multimap: Multimap[_filterValues_0__K, _filterValues_0__V], predicate: typing.Union[com.google.common.base.Predicate[_filterValues_0__V], typing.Callable[[_filterValues_0__V], bool]]) -> Multimap[_filterValues_0__K, _filterValues_0__V]: ...
    @typing.overload
    @staticmethod
    def filterValues(setMultimap: 'SetMultimap'[_filterValues_1__K, _filterValues_1__V], predicate: typing.Union[com.google.common.base.Predicate[_filterValues_1__V], typing.Callable[[_filterValues_1__V], bool]]) -> 'SetMultimap'[_filterValues_1__K, _filterValues_1__V]: ...
    _flatteningToMultimap__T = typing.TypeVar('_flatteningToMultimap__T')  # <T>
    _flatteningToMultimap__K = typing.TypeVar('_flatteningToMultimap__K')  # <K>
    _flatteningToMultimap__V = typing.TypeVar('_flatteningToMultimap__V')  # <V>
    _flatteningToMultimap__M = typing.TypeVar('_flatteningToMultimap__M', bound=Multimap)  # <M>
    @staticmethod
    def flatteningToMultimap(function: typing.Union[java.util.function.Function[_flatteningToMultimap__T, _flatteningToMultimap__K], typing.Callable[[_flatteningToMultimap__T], _flatteningToMultimap__K]], function2: typing.Union[java.util.function.Function[_flatteningToMultimap__T, java.util.stream.Stream[_flatteningToMultimap__V]], typing.Callable[[_flatteningToMultimap__T], java.util.stream.Stream[_flatteningToMultimap__V]]], supplier: typing.Union[java.util.function.Supplier[_flatteningToMultimap__M], typing.Callable[[], _flatteningToMultimap__M]]) -> java.util.stream.Collector[_flatteningToMultimap__T, typing.Any, _flatteningToMultimap__M]: ...
    _forMap__K = typing.TypeVar('_forMap__K')  # <K>
    _forMap__V = typing.TypeVar('_forMap__V')  # <V>
    @staticmethod
    def forMap(map: typing.Union[java.util.Map[_forMap__K, _forMap__V], typing.Mapping[_forMap__K, _forMap__V]]) -> 'SetMultimap'[_forMap__K, _forMap__V]: ...
    _index_0__K = typing.TypeVar('_index_0__K')  # <K>
    _index_0__V = typing.TypeVar('_index_0__V')  # <V>
    _index_1__K = typing.TypeVar('_index_1__K')  # <K>
    _index_1__V = typing.TypeVar('_index_1__V')  # <V>
    @typing.overload
    @staticmethod
    def index(iterable: java.lang.Iterable[_index_0__V], function: typing.Union[com.google.common.base.Function[_index_0__V, _index_0__K], typing.Callable[[_index_0__V], _index_0__K]]) -> 'ImmutableListMultimap'[_index_0__K, _index_0__V]: ...
    @typing.overload
    @staticmethod
    def index(iterator: java.util.Iterator[_index_1__V], function: typing.Union[com.google.common.base.Function[_index_1__V, _index_1__K], typing.Callable[[_index_1__V], _index_1__K]]) -> 'ImmutableListMultimap'[_index_1__K, _index_1__V]: ...
    _invertFrom__K = typing.TypeVar('_invertFrom__K')  # <K>
    _invertFrom__V = typing.TypeVar('_invertFrom__V')  # <V>
    _invertFrom__M = typing.TypeVar('_invertFrom__M', bound=Multimap)  # <M>
    @staticmethod
    def invertFrom(multimap: Multimap[_invertFrom__V, _invertFrom__K], m2: _invertFrom__M) -> _invertFrom__M: ...
    _newListMultimap__K = typing.TypeVar('_newListMultimap__K')  # <K>
    _newListMultimap__V = typing.TypeVar('_newListMultimap__V')  # <V>
    @staticmethod
    def newListMultimap(map: typing.Union[java.util.Map[_newListMultimap__K, typing.Union[java.util.Collection[_newListMultimap__V], typing.Sequence[_newListMultimap__V]]], typing.Mapping[_newListMultimap__K, typing.Union[java.util.Collection[_newListMultimap__V], typing.Sequence[_newListMultimap__V]]]], supplier: typing.Union[com.google.common.base.Supplier[java.util.List[_newListMultimap__V]], typing.Callable[[], java.util.List[_newListMultimap__V]]]) -> 'ListMultimap'[_newListMultimap__K, _newListMultimap__V]: ...
    _newMultimap__K = typing.TypeVar('_newMultimap__K')  # <K>
    _newMultimap__V = typing.TypeVar('_newMultimap__V')  # <V>
    @staticmethod
    def newMultimap(map: typing.Union[java.util.Map[_newMultimap__K, typing.Union[java.util.Collection[_newMultimap__V], typing.Sequence[_newMultimap__V]]], typing.Mapping[_newMultimap__K, typing.Union[java.util.Collection[_newMultimap__V], typing.Sequence[_newMultimap__V]]]], supplier: typing.Union[com.google.common.base.Supplier[java.util.Collection[_newMultimap__V]], typing.Callable[[], java.util.Collection[_newMultimap__V]]]) -> Multimap[_newMultimap__K, _newMultimap__V]: ...
    _newSetMultimap__K = typing.TypeVar('_newSetMultimap__K')  # <K>
    _newSetMultimap__V = typing.TypeVar('_newSetMultimap__V')  # <V>
    @staticmethod
    def newSetMultimap(map: typing.Union[java.util.Map[_newSetMultimap__K, typing.Union[java.util.Collection[_newSetMultimap__V], typing.Sequence[_newSetMultimap__V]]], typing.Mapping[_newSetMultimap__K, typing.Union[java.util.Collection[_newSetMultimap__V], typing.Sequence[_newSetMultimap__V]]]], supplier: typing.Union[com.google.common.base.Supplier[java.util.Set[_newSetMultimap__V]], typing.Callable[[], java.util.Set[_newSetMultimap__V]]]) -> 'SetMultimap'[_newSetMultimap__K, _newSetMultimap__V]: ...
    _newSortedSetMultimap__K = typing.TypeVar('_newSortedSetMultimap__K')  # <K>
    _newSortedSetMultimap__V = typing.TypeVar('_newSortedSetMultimap__V')  # <V>
    @staticmethod
    def newSortedSetMultimap(map: typing.Union[java.util.Map[_newSortedSetMultimap__K, typing.Union[java.util.Collection[_newSortedSetMultimap__V], typing.Sequence[_newSortedSetMultimap__V]]], typing.Mapping[_newSortedSetMultimap__K, typing.Union[java.util.Collection[_newSortedSetMultimap__V], typing.Sequence[_newSortedSetMultimap__V]]]], supplier: typing.Union[com.google.common.base.Supplier[java.util.SortedSet[_newSortedSetMultimap__V]], typing.Callable[[], java.util.SortedSet[_newSortedSetMultimap__V]]]) -> 'SortedSetMultimap'[_newSortedSetMultimap__K, _newSortedSetMultimap__V]: ...
    _synchronizedListMultimap__K = typing.TypeVar('_synchronizedListMultimap__K')  # <K>
    _synchronizedListMultimap__V = typing.TypeVar('_synchronizedListMultimap__V')  # <V>
    @staticmethod
    def synchronizedListMultimap(listMultimap: 'ListMultimap'[_synchronizedListMultimap__K, _synchronizedListMultimap__V]) -> 'ListMultimap'[_synchronizedListMultimap__K, _synchronizedListMultimap__V]: ...
    _synchronizedMultimap__K = typing.TypeVar('_synchronizedMultimap__K')  # <K>
    _synchronizedMultimap__V = typing.TypeVar('_synchronizedMultimap__V')  # <V>
    @staticmethod
    def synchronizedMultimap(multimap: Multimap[_synchronizedMultimap__K, _synchronizedMultimap__V]) -> Multimap[_synchronizedMultimap__K, _synchronizedMultimap__V]: ...
    _synchronizedSetMultimap__K = typing.TypeVar('_synchronizedSetMultimap__K')  # <K>
    _synchronizedSetMultimap__V = typing.TypeVar('_synchronizedSetMultimap__V')  # <V>
    @staticmethod
    def synchronizedSetMultimap(setMultimap: 'SetMultimap'[_synchronizedSetMultimap__K, _synchronizedSetMultimap__V]) -> 'SetMultimap'[_synchronizedSetMultimap__K, _synchronizedSetMultimap__V]: ...
    _synchronizedSortedSetMultimap__K = typing.TypeVar('_synchronizedSortedSetMultimap__K')  # <K>
    _synchronizedSortedSetMultimap__V = typing.TypeVar('_synchronizedSortedSetMultimap__V')  # <V>
    @staticmethod
    def synchronizedSortedSetMultimap(sortedSetMultimap: 'SortedSetMultimap'[_synchronizedSortedSetMultimap__K, _synchronizedSortedSetMultimap__V]) -> 'SortedSetMultimap'[_synchronizedSortedSetMultimap__K, _synchronizedSortedSetMultimap__V]: ...
    _toMultimap__T = typing.TypeVar('_toMultimap__T')  # <T>
    _toMultimap__K = typing.TypeVar('_toMultimap__K')  # <K>
    _toMultimap__V = typing.TypeVar('_toMultimap__V')  # <V>
    _toMultimap__M = typing.TypeVar('_toMultimap__M', bound=Multimap)  # <M>
    @staticmethod
    def toMultimap(function: typing.Union[java.util.function.Function[_toMultimap__T, _toMultimap__K], typing.Callable[[_toMultimap__T], _toMultimap__K]], function2: typing.Union[java.util.function.Function[_toMultimap__T, _toMultimap__V], typing.Callable[[_toMultimap__T], _toMultimap__V]], supplier: typing.Union[java.util.function.Supplier[_toMultimap__M], typing.Callable[[], _toMultimap__M]]) -> java.util.stream.Collector[_toMultimap__T, typing.Any, _toMultimap__M]: ...
    _transformEntries_0__K = typing.TypeVar('_transformEntries_0__K')  # <K>
    _transformEntries_0__V1 = typing.TypeVar('_transformEntries_0__V1')  # <V1>
    _transformEntries_0__V2 = typing.TypeVar('_transformEntries_0__V2')  # <V2>
    _transformEntries_1__K = typing.TypeVar('_transformEntries_1__K')  # <K>
    _transformEntries_1__V1 = typing.TypeVar('_transformEntries_1__V1')  # <V1>
    _transformEntries_1__V2 = typing.TypeVar('_transformEntries_1__V2')  # <V2>
    @typing.overload
    @staticmethod
    def transformEntries(listMultimap: 'ListMultimap'[_transformEntries_0__K, _transformEntries_0__V1], entryTransformer: typing.Union[Maps.EntryTransformer[_transformEntries_0__K, _transformEntries_0__V1, _transformEntries_0__V2], typing.Callable[[_transformEntries_0__K, _transformEntries_0__V1], _transformEntries_0__V2]]) -> 'ListMultimap'[_transformEntries_0__K, _transformEntries_0__V2]: ...
    @typing.overload
    @staticmethod
    def transformEntries(multimap: Multimap[_transformEntries_1__K, _transformEntries_1__V1], entryTransformer: typing.Union[Maps.EntryTransformer[_transformEntries_1__K, _transformEntries_1__V1, _transformEntries_1__V2], typing.Callable[[_transformEntries_1__K, _transformEntries_1__V1], _transformEntries_1__V2]]) -> Multimap[_transformEntries_1__K, _transformEntries_1__V2]: ...
    _transformValues_0__K = typing.TypeVar('_transformValues_0__K')  # <K>
    _transformValues_0__V1 = typing.TypeVar('_transformValues_0__V1')  # <V1>
    _transformValues_0__V2 = typing.TypeVar('_transformValues_0__V2')  # <V2>
    _transformValues_1__K = typing.TypeVar('_transformValues_1__K')  # <K>
    _transformValues_1__V1 = typing.TypeVar('_transformValues_1__V1')  # <V1>
    _transformValues_1__V2 = typing.TypeVar('_transformValues_1__V2')  # <V2>
    @typing.overload
    @staticmethod
    def transformValues(listMultimap: 'ListMultimap'[_transformValues_0__K, _transformValues_0__V1], function: typing.Union[com.google.common.base.Function[_transformValues_0__V1, _transformValues_0__V2], typing.Callable[[_transformValues_0__V1], _transformValues_0__V2]]) -> 'ListMultimap'[_transformValues_0__K, _transformValues_0__V2]: ...
    @typing.overload
    @staticmethod
    def transformValues(multimap: Multimap[_transformValues_1__K, _transformValues_1__V1], function: typing.Union[com.google.common.base.Function[_transformValues_1__V1, _transformValues_1__V2], typing.Callable[[_transformValues_1__V1], _transformValues_1__V2]]) -> Multimap[_transformValues_1__K, _transformValues_1__V2]: ...
    _unmodifiableListMultimap_0__K = typing.TypeVar('_unmodifiableListMultimap_0__K')  # <K>
    _unmodifiableListMultimap_0__V = typing.TypeVar('_unmodifiableListMultimap_0__V')  # <V>
    _unmodifiableListMultimap_1__K = typing.TypeVar('_unmodifiableListMultimap_1__K')  # <K>
    _unmodifiableListMultimap_1__V = typing.TypeVar('_unmodifiableListMultimap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def unmodifiableListMultimap(immutableListMultimap: 'ImmutableListMultimap'[_unmodifiableListMultimap_0__K, _unmodifiableListMultimap_0__V]) -> 'ListMultimap'[_unmodifiableListMultimap_0__K, _unmodifiableListMultimap_0__V]: ...
    @typing.overload
    @staticmethod
    def unmodifiableListMultimap(listMultimap: 'ListMultimap'[_unmodifiableListMultimap_1__K, _unmodifiableListMultimap_1__V]) -> 'ListMultimap'[_unmodifiableListMultimap_1__K, _unmodifiableListMultimap_1__V]: ...
    _unmodifiableMultimap_0__K = typing.TypeVar('_unmodifiableMultimap_0__K')  # <K>
    _unmodifiableMultimap_0__V = typing.TypeVar('_unmodifiableMultimap_0__V')  # <V>
    _unmodifiableMultimap_1__K = typing.TypeVar('_unmodifiableMultimap_1__K')  # <K>
    _unmodifiableMultimap_1__V = typing.TypeVar('_unmodifiableMultimap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def unmodifiableMultimap(immutableMultimap: 'ImmutableMultimap'[_unmodifiableMultimap_0__K, _unmodifiableMultimap_0__V]) -> Multimap[_unmodifiableMultimap_0__K, _unmodifiableMultimap_0__V]: ...
    @typing.overload
    @staticmethod
    def unmodifiableMultimap(multimap: Multimap[_unmodifiableMultimap_1__K, _unmodifiableMultimap_1__V]) -> Multimap[_unmodifiableMultimap_1__K, _unmodifiableMultimap_1__V]: ...
    _unmodifiableSetMultimap_0__K = typing.TypeVar('_unmodifiableSetMultimap_0__K')  # <K>
    _unmodifiableSetMultimap_0__V = typing.TypeVar('_unmodifiableSetMultimap_0__V')  # <V>
    _unmodifiableSetMultimap_1__K = typing.TypeVar('_unmodifiableSetMultimap_1__K')  # <K>
    _unmodifiableSetMultimap_1__V = typing.TypeVar('_unmodifiableSetMultimap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def unmodifiableSetMultimap(immutableSetMultimap: 'ImmutableSetMultimap'[_unmodifiableSetMultimap_0__K, _unmodifiableSetMultimap_0__V]) -> 'SetMultimap'[_unmodifiableSetMultimap_0__K, _unmodifiableSetMultimap_0__V]: ...
    @typing.overload
    @staticmethod
    def unmodifiableSetMultimap(setMultimap: 'SetMultimap'[_unmodifiableSetMultimap_1__K, _unmodifiableSetMultimap_1__V]) -> 'SetMultimap'[_unmodifiableSetMultimap_1__K, _unmodifiableSetMultimap_1__V]: ...
    _unmodifiableSortedSetMultimap__K = typing.TypeVar('_unmodifiableSortedSetMultimap__K')  # <K>
    _unmodifiableSortedSetMultimap__V = typing.TypeVar('_unmodifiableSortedSetMultimap__V')  # <V>
    @staticmethod
    def unmodifiableSortedSetMultimap(sortedSetMultimap: 'SortedSetMultimap'[_unmodifiableSortedSetMultimap__K, _unmodifiableSortedSetMultimap__V]) -> 'SortedSetMultimap'[_unmodifiableSortedSetMultimap__K, _unmodifiableSortedSetMultimap__V]: ...

_Multiset__Entry__E = typing.TypeVar('_Multiset__Entry__E')  # <E>
_Multiset__E = typing.TypeVar('_Multiset__E')  # <E>
class Multiset(java.util.Collection[_Multiset__E], typing.Generic[_Multiset__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<E> extends Collection<E>
    
        A collection that supports order-independent equality, like null, but may have duplicate elements. A multiset is also
        sometimes called a *bag*.
    
        Elements of a multiset that are equal to one another are referred to as *occurrences* of the same single element. The
        total number of occurrences of an element in a multiset is called the *count* of that element (the terms "frequency" and
        "multiplicity" are equivalent, but not used in this API). Since the count of an element is represented as an
        :code:`int`, a multiset may never contain more than null occurrences of any one element.
    
        :code:`Multiset` refines the specifications of several methods from :code:`Collection`. It also defines an additional
        query operation, :meth:`~com.google.common.collect.Multiset.count`, which returns the count of an element. There are
        five new bulk-modification operations, for example :meth:`~com.google.common.collect.Multiset.add`, to add or remove
        multiple occurrences of an element at once, or to set the count of an element to a specific value. These modification
        operations are optional, but implementations which support the standard collection operations
        :meth:`~com.google.common.collect.Multiset.add` or :meth:`~com.google.common.collect.Multiset.remove` are encouraged to
        implement the related methods as well. Finally, two collection views are provided:
        :meth:`~com.google.common.collect.Multiset.elementSet` contains the distinct elements of the multiset "with duplicates
        collapsed", and :meth:`~com.google.common.collect.Multiset.entrySet` is similar but contains
        :class:`~com.google.common.collect.Multiset.Entry` instances, each providing both a distinct element and the count of
        that element.
    
        In addition to these required methods, implementations of :code:`Multiset` are expected to provide two :code:`static`
        creation methods: :code:`create()`, returning an empty multiset, and :code:`create(Iterable<? extends E>)`, returning a
        multiset containing the given initial elements. This is simply a refinement of :code:`Collection`'s constructor
        recommendations, reflecting the new developments of Java 5.
    
        As with other collection types, the modification operations are optional, and should throw null when they are not
        implemented. Most implementations should support either all add operations or none of them, all removal operations or
        none of them, and if and only if all of these are supported, the :code:`setCount` methods as well.
    
        A multiset uses null to determine whether two instances should be considered "the same," *unless specified otherwise* by
        the implementation.
    
        Common implementations include :class:`~com.google.common.collect.ImmutableMultiset`,
        :class:`~com.google.common.collect.HashMultiset`, and :class:`~com.google.common.collect.ConcurrentHashMultiset`.
    
        If your values may be zero, negative, or outside the range of an int, you may wish to use
        :class:`~com.google.common.util.concurrent.AtomicLongMap` instead. Note, however, that unlike :code:`Multiset`,
        :code:`AtomicLongMap` does not automatically remove zeros.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    @typing.overload
    def add(self, e: _Multiset__E) -> bool: ...
    @typing.overload
    def add(self, e: _Multiset__E, int: int) -> int: ...
    def contains(self, object: typing.Any) -> bool: ...
    def containsAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def count(self, object: typing.Any) -> int: ...
    def elementSet(self) -> java.util.Set[_Multiset__E]: ...
    def entrySet(self) -> java.util.Set['Multiset.Entry'[_Multiset__E]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def forEach(self, consumer: typing.Union[java.util.function.Consumer[_Multiset__E], typing.Callable[[_Multiset__E], None]]) -> None: ...
    def forEachEntry(self, objIntConsumer: typing.Union[java.util.function.ObjIntConsumer[_Multiset__E], typing.Callable[[_Multiset__E, int], None]]) -> None: ...
    def hashCode(self) -> int: ...
    def iterator(self) -> java.util.Iterator[_Multiset__E]: ...
    @typing.overload
    def remove(self, object: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any, int: int) -> int: ...
    def removeAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def retainAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    @typing.overload
    def setCount(self, e: _Multiset__E, int: int, int2: int) -> bool: ...
    @typing.overload
    def setCount(self, e: _Multiset__E, int: int) -> int: ...
    def size(self) -> int: ...
    def spliterator(self) -> java.util.Spliterator[_Multiset__E]: ...
    def toString(self) -> str: ...
    class Entry(typing.Generic[_Multiset__Entry__E]):
        def equals(self, object: typing.Any) -> bool: ...
        def getCount(self) -> int: ...
        def getElement(self) -> _Multiset__Entry__E: ...
        def hashCode(self) -> int: ...
        def toString(self) -> str: ...

class Multisets:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Provides static utility methods for creating and working with :class:`~com.google.common.collect.Multiset` instances.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    @staticmethod
    def containsOccurrences(multiset: Multiset[typing.Any], multiset2: Multiset[typing.Any]) -> bool: ...
    _copyHighestCountFirst__E = typing.TypeVar('_copyHighestCountFirst__E')  # <E>
    @staticmethod
    def copyHighestCountFirst(multiset: Multiset[_copyHighestCountFirst__E]) -> 'ImmutableMultiset'[_copyHighestCountFirst__E]: ...
    _difference__E = typing.TypeVar('_difference__E')  # <E>
    @staticmethod
    def difference(multiset: Multiset[_difference__E], multiset2: Multiset[typing.Any]) -> Multiset[_difference__E]: ...
    _filter__E = typing.TypeVar('_filter__E')  # <E>
    @staticmethod
    def filter(multiset: Multiset[_filter__E], predicate: typing.Union[com.google.common.base.Predicate[_filter__E], typing.Callable[[_filter__E], bool]]) -> Multiset[_filter__E]: ...
    _immutableEntry__E = typing.TypeVar('_immutableEntry__E')  # <E>
    @staticmethod
    def immutableEntry(e: _immutableEntry__E, int: int) -> Multiset.Entry[_immutableEntry__E]: ...
    _intersection__E = typing.TypeVar('_intersection__E')  # <E>
    @staticmethod
    def intersection(multiset: Multiset[_intersection__E], multiset2: Multiset[typing.Any]) -> Multiset[_intersection__E]: ...
    @typing.overload
    @staticmethod
    def removeOccurrences(multiset: Multiset[typing.Any], multiset2: Multiset[typing.Any]) -> bool: ...
    @typing.overload
    @staticmethod
    def removeOccurrences(multiset: Multiset[typing.Any], iterable: java.lang.Iterable[typing.Any]) -> bool: ...
    @staticmethod
    def retainOccurrences(multiset: Multiset[typing.Any], multiset2: Multiset[typing.Any]) -> bool: ...
    _sum__E = typing.TypeVar('_sum__E')  # <E>
    @staticmethod
    def sum(multiset: Multiset[_sum__E], multiset2: Multiset[_sum__E]) -> Multiset[_sum__E]: ...
    _toMultiset__T = typing.TypeVar('_toMultiset__T')  # <T>
    _toMultiset__E = typing.TypeVar('_toMultiset__E')  # <E>
    _toMultiset__M = typing.TypeVar('_toMultiset__M', bound=Multiset)  # <M>
    @staticmethod
    def toMultiset(function: typing.Union[java.util.function.Function[_toMultiset__T, _toMultiset__E], typing.Callable[[_toMultiset__T], _toMultiset__E]], toIntFunction: typing.Union[java.util.function.ToIntFunction[_toMultiset__T], typing.Callable[[_toMultiset__T], int]], supplier: typing.Union[java.util.function.Supplier[_toMultiset__M], typing.Callable[[], _toMultiset__M]]) -> java.util.stream.Collector[_toMultiset__T, typing.Any, _toMultiset__M]: ...
    _union__E = typing.TypeVar('_union__E')  # <E>
    @staticmethod
    def union(multiset: Multiset[_union__E], multiset2: Multiset[_union__E]) -> Multiset[_union__E]: ...
    _unmodifiableMultiset_0__E = typing.TypeVar('_unmodifiableMultiset_0__E')  # <E>
    _unmodifiableMultiset_1__E = typing.TypeVar('_unmodifiableMultiset_1__E')  # <E>
    @typing.overload
    @staticmethod
    def unmodifiableMultiset(immutableMultiset: 'ImmutableMultiset'[_unmodifiableMultiset_0__E]) -> Multiset[_unmodifiableMultiset_0__E]: ...
    @typing.overload
    @staticmethod
    def unmodifiableMultiset(multiset: Multiset[_unmodifiableMultiset_1__E]) -> Multiset[_unmodifiableMultiset_1__E]: ...
    _unmodifiableSortedMultiset__E = typing.TypeVar('_unmodifiableSortedMultiset__E')  # <E>
    @staticmethod
    def unmodifiableSortedMultiset(sortedMultiset: 'SortedMultiset'[_unmodifiableSortedMultiset__E]) -> 'SortedMultiset'[_unmodifiableSortedMultiset__E]: ...

class ObjectArrays:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Static utility methods pertaining to object arrays.
    
        Since:
            2.0
    """
    _concat_0__T = typing.TypeVar('_concat_0__T')  # <T>
    _concat_1__T = typing.TypeVar('_concat_1__T')  # <T>
    _concat_2__T = typing.TypeVar('_concat_2__T')  # <T>
    @typing.overload
    @staticmethod
    def concat(t: _concat_0__T, tArray: typing.List[_concat_0__T]) -> typing.List[_concat_0__T]: ...
    @typing.overload
    @staticmethod
    def concat(tArray: typing.List[_concat_1__T], t2: _concat_1__T) -> typing.List[_concat_1__T]: ...
    @typing.overload
    @staticmethod
    def concat(tArray: typing.List[_concat_2__T], tArray2: typing.List[_concat_2__T], class_: typing.Type[_concat_2__T]) -> typing.List[_concat_2__T]: ...
    _newArray_0__T = typing.TypeVar('_newArray_0__T')  # <T>
    _newArray_1__T = typing.TypeVar('_newArray_1__T')  # <T>
    @typing.overload
    @staticmethod
    def newArray(class_: typing.Type[_newArray_0__T], int: int) -> typing.List[_newArray_0__T]: ...
    @typing.overload
    @staticmethod
    def newArray(tArray: typing.List[_newArray_1__T], int: int) -> typing.List[_newArray_1__T]: ...

_Ordering__T = typing.TypeVar('_Ordering__T')  # <T>
class Ordering(java.util.Comparator[_Ordering__T], typing.Generic[_Ordering__T]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<T> extends Object implements Comparator<T>
    
        A comparator, with additional methods to support common operations. This is an "enriched" version of :code:`Comparator`
        for pre-Java-8 users, in the same sense that :class:`~com.google.common.collect.FluentIterable` is an enriched null for
        pre-Java-8 users.
    
        Three types of methods
    ----------------------
    
        Like other fluent types, there are three types of methods present: methods for *acquiring*, *chaining*, and *using*.
    
        Acquiring
    ---------
    
    
        The common ways to get an instance of :code:`Ordering` are:
    
          - Subclass it and implement :meth:`~com.google.common.collect.Ordering.compare` instead of implementing null directly
          - Pass a *pre-existing* null instance to :meth:`~com.google.common.collect.Ordering.from`
          - Use the natural ordering, :meth:`~com.google.common.collect.Ordering.natural`
    
    
        Chaining
    --------
    
    
        Then you can use the *chaining* methods to get an altered version of that :code:`Ordering`, including:
    
          - :meth:`~com.google.common.collect.Ordering.reverse`
          - :meth:`~com.google.common.collect.Ordering.compound`
          - :meth:`~com.google.common.collect.Ordering.onResultOf`
          - :meth:`~com.google.common.collect.Ordering.nullsFirst` / :meth:`~com.google.common.collect.Ordering.nullsLast`
    
    
        Using
    -----
    
    
        Finally, use the resulting :code:`Ordering` anywhere a null is required, or use any of its special operations, such as:
    
          - :meth:`~com.google.common.collect.Ordering.immutableSortedCopy`
          - :meth:`~com.google.common.collect.Ordering.isOrdered` / :meth:`~com.google.common.collect.Ordering.isStrictlyOrdered`
          - :meth:`~com.google.common.collect.Ordering.min` / :meth:`~com.google.common.collect.Ordering.max`
    
    
        Understanding complex orderings
    -------------------------------
    
    
        Complex chained orderings like the following example can be challenging to understand.
    
        .. code-block: java
        
         Ordering<Foo> ordering =
             Ordering.natural()
                 .nullsFirst()
                 .onResultOf(getBarFunction)
                 .nullsLast();
         
        Note that each chaining method returns a new ordering instance which is backed by the previous instance, but has the
        chance to act on values *before* handing off to that backing instance. As a result, it usually helps to read chained
        ordering expressions *backwards*. For example, when :code:`compare` is called on the above ordering:
    
          1.  First, if only one :code:`Foo` is null, that null value is treated as *greater*
          2.  Next, non-null :code:`Foo` values are passed to :code:`getBarFunction` (we will be comparing :code:`Bar` values from now
            on)
          3.  Next, if only one :code:`Bar` is null, that null value is treated as *lesser*
          4.  Finally, natural ordering is used (i.e. the result of :code:`Bar.compareTo(Bar)` is returned)
    
    
        Alas, :meth:`~com.google.common.collect.Ordering.reverse` is a little different. As you read backwards through a chain
        and encounter a call to :code:`reverse`, continue working backwards until a result is determined, and then reverse that
        result.
    
        Additional notes
    ----------------
    
    
        Except as noted, the orderings returned by the factory methods of this class are serializable if and only if the
        provided instances that back them are. For example, if :code:`ordering` and :code:`function` can themselves be
        serialized, then :code:`ordering.onResultOf(function)` can as well.
    
        For Java 8 users
    ----------------
    
    
        If you are using Java 8, this class is now obsolete. Most of its functionality is now provided by null and by null
        itself, and the rest can now be found as static methods in our new :class:`~com.google.common.collect.Comparators`
        class. See each method below for further instructions. Whenever possible, you should change any references of type
        :code:`Ordering` to be of type :code:`Comparator` instead. However, at this time we have no plan to *deprecate* this
        class.
    
        Many replacements involve adopting :code:`Stream`, and these changes can sometimes make your code verbose. Whenever
        following this advice, you should check whether :code:`Stream` could be adopted more comprehensively in your code; the
        end result may be quite a bit simpler.
    
        See also
    --------
    
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    @staticmethod
    def allEqual() -> 'Ordering'[typing.Any]: ...
    @staticmethod
    def arbitrary() -> 'Ordering'[typing.Any]: ...
    def binarySearch(self, list: java.util.List[_Ordering__T], t: _Ordering__T) -> int: ...
    def compare(self, t: _Ordering__T, t2: _Ordering__T) -> int: ...
    _compound_0__U = typing.TypeVar('_compound_0__U')  # <U>
    _compound_1__T = typing.TypeVar('_compound_1__T')  # <T>
    @typing.overload
    def compound(self, comparator: typing.Union[java.util.Comparator[_compound_0__U], typing.Callable[[_compound_0__U, _compound_0__U], int]]) -> 'Ordering'[_compound_0__U]: ...
    @typing.overload
    @staticmethod
    def compound(iterable: java.lang.Iterable[java.util.Comparator[_compound_1__T]]) -> 'Ordering'[_compound_1__T]: ...
    _explicit_0__T = typing.TypeVar('_explicit_0__T')  # <T>
    _explicit_1__T = typing.TypeVar('_explicit_1__T')  # <T>
    @typing.overload
    @staticmethod
    def explicit(t: _explicit_0__T, tArray: typing.List[_explicit_0__T]) -> 'Ordering'[_explicit_0__T]: ...
    @typing.overload
    @staticmethod
    def explicit(list: java.util.List[_explicit_1__T]) -> 'Ordering'[_explicit_1__T]: ...
    _greatestOf_0__E = typing.TypeVar('_greatestOf_0__E')  # <E>
    _greatestOf_1__E = typing.TypeVar('_greatestOf_1__E')  # <E>
    @typing.overload
    def greatestOf(self, iterable: java.lang.Iterable[_greatestOf_0__E], int: int) -> java.util.List[_greatestOf_0__E]: ...
    @typing.overload
    def greatestOf(self, iterator: java.util.Iterator[_greatestOf_1__E], int: int) -> java.util.List[_greatestOf_1__E]: ...
    _immutableSortedCopy__E = typing.TypeVar('_immutableSortedCopy__E')  # <E>
    def immutableSortedCopy(self, iterable: java.lang.Iterable[_immutableSortedCopy__E]) -> 'ImmutableList'[_immutableSortedCopy__E]: ...
    def isOrdered(self, iterable: java.lang.Iterable[_Ordering__T]) -> bool: ...
    def isStrictlyOrdered(self, iterable: java.lang.Iterable[_Ordering__T]) -> bool: ...
    _leastOf_0__E = typing.TypeVar('_leastOf_0__E')  # <E>
    _leastOf_1__E = typing.TypeVar('_leastOf_1__E')  # <E>
    @typing.overload
    def leastOf(self, iterable: java.lang.Iterable[_leastOf_0__E], int: int) -> java.util.List[_leastOf_0__E]: ...
    @typing.overload
    def leastOf(self, iterator: java.util.Iterator[_leastOf_1__E], int: int) -> java.util.List[_leastOf_1__E]: ...
    _lexicographical__S = typing.TypeVar('_lexicographical__S')  # <S>
    def lexicographical(self) -> 'Ordering'[java.lang.Iterable[_lexicographical__S]]: ...
    _max_0__E = typing.TypeVar('_max_0__E')  # <E>
    _max_1__E = typing.TypeVar('_max_1__E')  # <E>
    _max_2__E = typing.TypeVar('_max_2__E')  # <E>
    _max_3__E = typing.TypeVar('_max_3__E')  # <E>
    @typing.overload
    def max(self, iterable: java.lang.Iterable[_max_0__E]) -> _max_0__E: ...
    @typing.overload
    def max(self, e: _max_1__E, e2: _max_1__E) -> _max_1__E: ...
    @typing.overload
    def max(self, e: _max_2__E, e2: _max_2__E, e3: _max_2__E, eArray: typing.List[_max_2__E]) -> _max_2__E: ...
    @typing.overload
    def max(self, iterator: java.util.Iterator[_max_3__E]) -> _max_3__E: ...
    _min_0__E = typing.TypeVar('_min_0__E')  # <E>
    _min_1__E = typing.TypeVar('_min_1__E')  # <E>
    _min_2__E = typing.TypeVar('_min_2__E')  # <E>
    _min_3__E = typing.TypeVar('_min_3__E')  # <E>
    @typing.overload
    def min(self, iterable: java.lang.Iterable[_min_0__E]) -> _min_0__E: ...
    @typing.overload
    def min(self, e: _min_1__E, e2: _min_1__E) -> _min_1__E: ...
    @typing.overload
    def min(self, e: _min_2__E, e2: _min_2__E, e3: _min_2__E, eArray: typing.List[_min_2__E]) -> _min_2__E: ...
    @typing.overload
    def min(self, iterator: java.util.Iterator[_min_3__E]) -> _min_3__E: ...
    _natural__C = typing.TypeVar('_natural__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def natural() -> 'Ordering'[_natural__C]: ...
    _nullsFirst__S = typing.TypeVar('_nullsFirst__S')  # <S>
    def nullsFirst(self) -> 'Ordering'[_nullsFirst__S]: ...
    _nullsLast__S = typing.TypeVar('_nullsLast__S')  # <S>
    def nullsLast(self) -> 'Ordering'[_nullsLast__S]: ...
    _onResultOf__F = typing.TypeVar('_onResultOf__F')  # <F>
    def onResultOf(self, function: typing.Union[com.google.common.base.Function[_onResultOf__F, _Ordering__T], typing.Callable[[_onResultOf__F], _Ordering__T]]) -> 'Ordering'[_onResultOf__F]: ...
    _reverse__S = typing.TypeVar('_reverse__S')  # <S>
    def reverse(self) -> 'Ordering'[_reverse__S]: ...
    _sortedCopy__E = typing.TypeVar('_sortedCopy__E')  # <E>
    def sortedCopy(self, iterable: java.lang.Iterable[_sortedCopy__E]) -> java.util.List[_sortedCopy__E]: ...
    @staticmethod
    def usingToString() -> 'Ordering'[typing.Any]: ...

_PeekingIterator__E = typing.TypeVar('_PeekingIterator__E')  # <E>
class PeekingIterator(java.util.Iterator[_PeekingIterator__E], typing.Generic[_PeekingIterator__E]):
    """
    @DoNotMock(value="Use Iterators.peekingIterator") :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<E> extends Iterator<E>
    
        An iterator that supports a one-element lookahead while iterating.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    def next(self) -> _PeekingIterator__E: ...
    def peek(self) -> _PeekingIterator__E: ...
    def remove(self) -> None: ...

class Queues:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Static utility methods pertaining to null and null instances. Also see this class's counterparts
        :class:`~com.google.common.collect.Lists`, :class:`~com.google.common.collect.Sets`, and
        :class:`~com.google.common.collect.Maps`.
    
        Since:
            11.0
    """
    _drain_0__E = typing.TypeVar('_drain_0__E')  # <E>
    _drain_1__E = typing.TypeVar('_drain_1__E')  # <E>
    @typing.overload
    @staticmethod
    def drain(blockingQueue: java.util.concurrent.BlockingQueue[_drain_0__E], collection: typing.Union[java.util.Collection[_drain_0__E], typing.Sequence[_drain_0__E]], int: int, duration: java.time.Duration) -> int: ...
    @typing.overload
    @staticmethod
    def drain(blockingQueue: java.util.concurrent.BlockingQueue[_drain_1__E], collection: typing.Union[java.util.Collection[_drain_1__E], typing.Sequence[_drain_1__E]], int: int, long: int, timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    _drainUninterruptibly_0__E = typing.TypeVar('_drainUninterruptibly_0__E')  # <E>
    _drainUninterruptibly_1__E = typing.TypeVar('_drainUninterruptibly_1__E')  # <E>
    @typing.overload
    @staticmethod
    def drainUninterruptibly(blockingQueue: java.util.concurrent.BlockingQueue[_drainUninterruptibly_0__E], collection: typing.Union[java.util.Collection[_drainUninterruptibly_0__E], typing.Sequence[_drainUninterruptibly_0__E]], int: int, duration: java.time.Duration) -> int: ...
    @typing.overload
    @staticmethod
    def drainUninterruptibly(blockingQueue: java.util.concurrent.BlockingQueue[_drainUninterruptibly_1__E], collection: typing.Union[java.util.Collection[_drainUninterruptibly_1__E], typing.Sequence[_drainUninterruptibly_1__E]], int: int, long: int, timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    _newArrayBlockingQueue__E = typing.TypeVar('_newArrayBlockingQueue__E')  # <E>
    @staticmethod
    def newArrayBlockingQueue(int: int) -> java.util.concurrent.ArrayBlockingQueue[_newArrayBlockingQueue__E]: ...
    _newArrayDeque_0__E = typing.TypeVar('_newArrayDeque_0__E')  # <E>
    _newArrayDeque_1__E = typing.TypeVar('_newArrayDeque_1__E')  # <E>
    @typing.overload
    @staticmethod
    def newArrayDeque() -> java.util.ArrayDeque[_newArrayDeque_0__E]: ...
    @typing.overload
    @staticmethod
    def newArrayDeque(iterable: java.lang.Iterable[_newArrayDeque_1__E]) -> java.util.ArrayDeque[_newArrayDeque_1__E]: ...
    _newConcurrentLinkedQueue_0__E = typing.TypeVar('_newConcurrentLinkedQueue_0__E')  # <E>
    _newConcurrentLinkedQueue_1__E = typing.TypeVar('_newConcurrentLinkedQueue_1__E')  # <E>
    @typing.overload
    @staticmethod
    def newConcurrentLinkedQueue() -> java.util.concurrent.ConcurrentLinkedQueue[_newConcurrentLinkedQueue_0__E]: ...
    @typing.overload
    @staticmethod
    def newConcurrentLinkedQueue(iterable: java.lang.Iterable[_newConcurrentLinkedQueue_1__E]) -> java.util.concurrent.ConcurrentLinkedQueue[_newConcurrentLinkedQueue_1__E]: ...
    _newLinkedBlockingDeque_0__E = typing.TypeVar('_newLinkedBlockingDeque_0__E')  # <E>
    _newLinkedBlockingDeque_1__E = typing.TypeVar('_newLinkedBlockingDeque_1__E')  # <E>
    _newLinkedBlockingDeque_2__E = typing.TypeVar('_newLinkedBlockingDeque_2__E')  # <E>
    @typing.overload
    @staticmethod
    def newLinkedBlockingDeque() -> java.util.concurrent.LinkedBlockingDeque[_newLinkedBlockingDeque_0__E]: ...
    @typing.overload
    @staticmethod
    def newLinkedBlockingDeque(int: int) -> java.util.concurrent.LinkedBlockingDeque[_newLinkedBlockingDeque_1__E]: ...
    @typing.overload
    @staticmethod
    def newLinkedBlockingDeque(iterable: java.lang.Iterable[_newLinkedBlockingDeque_2__E]) -> java.util.concurrent.LinkedBlockingDeque[_newLinkedBlockingDeque_2__E]: ...
    _newLinkedBlockingQueue_0__E = typing.TypeVar('_newLinkedBlockingQueue_0__E')  # <E>
    _newLinkedBlockingQueue_1__E = typing.TypeVar('_newLinkedBlockingQueue_1__E')  # <E>
    _newLinkedBlockingQueue_2__E = typing.TypeVar('_newLinkedBlockingQueue_2__E')  # <E>
    @typing.overload
    @staticmethod
    def newLinkedBlockingQueue() -> java.util.concurrent.LinkedBlockingQueue[_newLinkedBlockingQueue_0__E]: ...
    @typing.overload
    @staticmethod
    def newLinkedBlockingQueue(int: int) -> java.util.concurrent.LinkedBlockingQueue[_newLinkedBlockingQueue_1__E]: ...
    @typing.overload
    @staticmethod
    def newLinkedBlockingQueue(iterable: java.lang.Iterable[_newLinkedBlockingQueue_2__E]) -> java.util.concurrent.LinkedBlockingQueue[_newLinkedBlockingQueue_2__E]: ...
    _newPriorityBlockingQueue_0__E = typing.TypeVar('_newPriorityBlockingQueue_0__E', bound=java.lang.Comparable)  # <E>
    _newPriorityBlockingQueue_1__E = typing.TypeVar('_newPriorityBlockingQueue_1__E', bound=java.lang.Comparable)  # <E>
    @typing.overload
    @staticmethod
    def newPriorityBlockingQueue() -> java.util.concurrent.PriorityBlockingQueue[_newPriorityBlockingQueue_0__E]: ...
    @typing.overload
    @staticmethod
    def newPriorityBlockingQueue(iterable: java.lang.Iterable[_newPriorityBlockingQueue_1__E]) -> java.util.concurrent.PriorityBlockingQueue[_newPriorityBlockingQueue_1__E]: ...
    _newPriorityQueue_0__E = typing.TypeVar('_newPriorityQueue_0__E', bound=java.lang.Comparable)  # <E>
    _newPriorityQueue_1__E = typing.TypeVar('_newPriorityQueue_1__E', bound=java.lang.Comparable)  # <E>
    @typing.overload
    @staticmethod
    def newPriorityQueue() -> java.util.PriorityQueue[_newPriorityQueue_0__E]: ...
    @typing.overload
    @staticmethod
    def newPriorityQueue(iterable: java.lang.Iterable[_newPriorityQueue_1__E]) -> java.util.PriorityQueue[_newPriorityQueue_1__E]: ...
    _newSynchronousQueue__E = typing.TypeVar('_newSynchronousQueue__E')  # <E>
    @staticmethod
    def newSynchronousQueue() -> java.util.concurrent.SynchronousQueue[_newSynchronousQueue__E]: ...
    _synchronizedDeque__E = typing.TypeVar('_synchronizedDeque__E')  # <E>
    @staticmethod
    def synchronizedDeque(deque: java.util.Deque[_synchronizedDeque__E]) -> java.util.Deque[_synchronizedDeque__E]: ...
    _synchronizedQueue__E = typing.TypeVar('_synchronizedQueue__E')  # <E>
    @staticmethod
    def synchronizedQueue(queue: java.util.Queue[_synchronizedQueue__E]) -> java.util.Queue[_synchronizedQueue__E]: ...

_RangeMap__K = typing.TypeVar('_RangeMap__K', bound=java.lang.Comparable)  # <K>
_RangeMap__V = typing.TypeVar('_RangeMap__V')  # <V>
class RangeMap(typing.Generic[_RangeMap__K, _RangeMap__V]):
    """
    :class:`~com.google.common.annotations.Beta` @DoNotMock(value="Use ImmutableRangeMap or TreeRangeMap") :class:`~com.google.common.annotations.GwtIncompatible` public interface :meth:`~src`<K extends Comparable,V>
    
        A mapping from disjoint nonempty ranges to non-null values. Queries look up the value associated with the range (if any)
        that contains a specified key.
    
        In contrast to :class:`~com.google.common.collect.RangeSet`, no "coalescing" is done of
        :meth:`~com.google.common.collect.Range.isConnected` ranges, even if they are mapped to the same value.
    
        Since:
            14.0
    """
    def asDescendingMapOfRanges(self) -> java.util.Map['Range'[_RangeMap__K], _RangeMap__V]: ...
    def asMapOfRanges(self) -> java.util.Map['Range'[_RangeMap__K], _RangeMap__V]: ...
    def clear(self) -> None: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, k: _RangeMap__K) -> _RangeMap__V: ...
    def getEntry(self, k: _RangeMap__K) -> java.util.Map.Entry['Range'[_RangeMap__K], _RangeMap__V]: ...
    def hashCode(self) -> int: ...
    def merge(self, range: 'Range'[_RangeMap__K], v: _RangeMap__V, biFunction: typing.Union[java.util.function.BiFunction[_RangeMap__V, _RangeMap__V, _RangeMap__V], typing.Callable[[_RangeMap__V, _RangeMap__V], _RangeMap__V]]) -> None: ...
    def put(self, range: 'Range'[_RangeMap__K], v: _RangeMap__V) -> None: ...
    def putAll(self, rangeMap: 'RangeMap'[_RangeMap__K, _RangeMap__V]) -> None: ...
    def putCoalescing(self, range: 'Range'[_RangeMap__K], v: _RangeMap__V) -> None: ...
    def remove(self, range: 'Range'[_RangeMap__K]) -> None: ...
    def span(self) -> 'Range'[_RangeMap__K]: ...
    def subRangeMap(self, range: 'Range'[_RangeMap__K]) -> 'RangeMap'[_RangeMap__K, _RangeMap__V]: ...
    def toString(self) -> str: ...

_RangeSet__C = typing.TypeVar('_RangeSet__C', bound=java.lang.Comparable)  # <C>
class RangeSet(typing.Generic[_RangeSet__C]):
    """
    :class:`~com.google.common.annotations.Beta` @DoNotMock(value="Use ImmutableRangeSet or TreeRangeSet") :class:`~com.google.common.annotations.GwtIncompatible` public interface :meth:`~src`<C extends Comparable>
    
        A set comprising zero or more :meth:`~com.google.common.collect.Range.isEmpty`,
        :meth:`~com.google.common.collect.Range.isConnected` ranges of type :code:`C`.
    
        Implementations that choose to support the :meth:`~com.google.common.collect.RangeSet.add` operation are required to
        ignore empty ranges and coalesce connected ranges. For example:
    
        .. code-block: java
        
         RangeSet<Integer> rangeSet = TreeRangeSet.create();
         rangeSet.add(Range.closed(1, 10)); // {[1, 10]}
         rangeSet.add(Range.closedOpen(11, 15)); // disconnected range; {[1, 10], [11, 15)}
         rangeSet.add(Range.closedOpen(15, 20)); // connected range; {[1, 10], [11, 20)}
         rangeSet.add(Range.openClosed(0, 0)); // empty range; {[1, 10], [11, 20)}
         rangeSet.remove(Range.open(5, 10)); // splits [1, 10]; {[1, 5], [10, 10], [11, 20)}
         
    
        Note that the behavior of :meth:`~com.google.common.collect.Range.isEmpty` and
        :meth:`~com.google.common.collect.Range.isConnected` may not be as expected on discrete ranges. See the Javadoc of those
        methods for details.
    
        For a null whose contents are specified by a :class:`~com.google.common.collect.Range`, see
        :class:`~com.google.common.collect.ContiguousSet`.
    
        See the Guava User Guide article on RangeSets.
    
        Since:
            14.0
    """
    def add(self, range: 'Range'[_RangeSet__C]) -> None: ...
    @typing.overload
    def addAll(self, rangeSet: 'RangeSet'[_RangeSet__C]) -> None: ...
    @typing.overload
    def addAll(self, iterable: java.lang.Iterable['Range'[_RangeSet__C]]) -> None: ...
    def asDescendingSetOfRanges(self) -> java.util.Set['Range'[_RangeSet__C]]: ...
    def asRanges(self) -> java.util.Set['Range'[_RangeSet__C]]: ...
    def clear(self) -> None: ...
    def complement(self) -> 'RangeSet'[_RangeSet__C]: ...
    def contains(self, c: _RangeSet__C) -> bool: ...
    def encloses(self, range: 'Range'[_RangeSet__C]) -> bool: ...
    @typing.overload
    def enclosesAll(self, rangeSet: 'RangeSet'[_RangeSet__C]) -> bool: ...
    @typing.overload
    def enclosesAll(self, iterable: java.lang.Iterable['Range'[_RangeSet__C]]) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def intersects(self, range: 'Range'[_RangeSet__C]) -> bool: ...
    def isEmpty(self) -> bool: ...
    def rangeContaining(self, c: _RangeSet__C) -> 'Range'[_RangeSet__C]: ...
    def remove(self, range: 'Range'[_RangeSet__C]) -> None: ...
    @typing.overload
    def removeAll(self, rangeSet: 'RangeSet'[_RangeSet__C]) -> None: ...
    @typing.overload
    def removeAll(self, iterable: java.lang.Iterable['Range'[_RangeSet__C]]) -> None: ...
    def span(self) -> 'Range'[_RangeSet__C]: ...
    def subRangeSet(self, range: 'Range'[_RangeSet__C]) -> 'RangeSet'[_RangeSet__C]: ...
    def toString(self) -> str: ...

_Sets__SetView__E = typing.TypeVar('_Sets__SetView__E')  # <E>
class Sets:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Static utility methods pertaining to null instances. Also see this class's counterparts
        :class:`~com.google.common.collect.Lists`, :class:`~com.google.common.collect.Maps` and
        :class:`~com.google.common.collect.Queues`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    _cartesianProduct_0__B = typing.TypeVar('_cartesianProduct_0__B')  # <B>
    _cartesianProduct_1__B = typing.TypeVar('_cartesianProduct_1__B')  # <B>
    @typing.overload
    @staticmethod
    def cartesianProduct(list: java.util.List[java.util.Set[_cartesianProduct_0__B]]) -> java.util.Set[java.util.List[_cartesianProduct_0__B]]: ...
    @typing.overload
    @staticmethod
    def cartesianProduct(setArray: typing.List[java.util.Set[_cartesianProduct_1__B]]) -> java.util.Set[java.util.List[_cartesianProduct_1__B]]: ...
    _combinations__E = typing.TypeVar('_combinations__E')  # <E>
    @staticmethod
    def combinations(set: java.util.Set[_combinations__E], int: int) -> java.util.Set[java.util.Set[_combinations__E]]: ...
    _complementOf_0__E = typing.TypeVar('_complementOf_0__E', bound=java.lang.Enum)  # <E>
    _complementOf_1__E = typing.TypeVar('_complementOf_1__E', bound=java.lang.Enum)  # <E>
    @typing.overload
    @staticmethod
    def complementOf(collection: typing.Union[java.util.Collection[_complementOf_0__E], typing.Sequence[_complementOf_0__E]]) -> java.util.EnumSet[_complementOf_0__E]: ...
    @typing.overload
    @staticmethod
    def complementOf(collection: typing.Union[java.util.Collection[_complementOf_1__E], typing.Sequence[_complementOf_1__E]], class_: typing.Type[_complementOf_1__E]) -> java.util.EnumSet[_complementOf_1__E]: ...
    _difference__E = typing.TypeVar('_difference__E')  # <E>
    @staticmethod
    def difference(set: java.util.Set[_difference__E], set2: java.util.Set[typing.Any]) -> 'Sets.SetView'[_difference__E]: ...
    _filter_0__E = typing.TypeVar('_filter_0__E')  # <E>
    _filter_1__E = typing.TypeVar('_filter_1__E')  # <E>
    _filter_2__E = typing.TypeVar('_filter_2__E')  # <E>
    @typing.overload
    @staticmethod
    def filter(navigableSet: java.util.NavigableSet[_filter_0__E], predicate: typing.Union[com.google.common.base.Predicate[_filter_0__E], typing.Callable[[_filter_0__E], bool]]) -> java.util.NavigableSet[_filter_0__E]: ...
    @typing.overload
    @staticmethod
    def filter(set: java.util.Set[_filter_1__E], predicate: typing.Union[com.google.common.base.Predicate[_filter_1__E], typing.Callable[[_filter_1__E], bool]]) -> java.util.Set[_filter_1__E]: ...
    @typing.overload
    @staticmethod
    def filter(sortedSet: java.util.SortedSet[_filter_2__E], predicate: typing.Union[com.google.common.base.Predicate[_filter_2__E], typing.Callable[[_filter_2__E], bool]]) -> java.util.SortedSet[_filter_2__E]: ...
    _immutableEnumSet_0__E = typing.TypeVar('_immutableEnumSet_0__E', bound=java.lang.Enum)  # <E>
    _immutableEnumSet_1__E = typing.TypeVar('_immutableEnumSet_1__E', bound=java.lang.Enum)  # <E>
    @typing.overload
    @staticmethod
    def immutableEnumSet(e: _immutableEnumSet_0__E, eArray: typing.List[_immutableEnumSet_0__E]) -> 'ImmutableSet'[_immutableEnumSet_0__E]: ...
    @typing.overload
    @staticmethod
    def immutableEnumSet(iterable: java.lang.Iterable[_immutableEnumSet_1__E]) -> 'ImmutableSet'[_immutableEnumSet_1__E]: ...
    _intersection__E = typing.TypeVar('_intersection__E')  # <E>
    @staticmethod
    def intersection(set: java.util.Set[_intersection__E], set2: java.util.Set[typing.Any]) -> 'Sets.SetView'[_intersection__E]: ...
    _newConcurrentHashSet_0__E = typing.TypeVar('_newConcurrentHashSet_0__E')  # <E>
    _newConcurrentHashSet_1__E = typing.TypeVar('_newConcurrentHashSet_1__E')  # <E>
    @typing.overload
    @staticmethod
    def newConcurrentHashSet() -> java.util.Set[_newConcurrentHashSet_0__E]: ...
    @typing.overload
    @staticmethod
    def newConcurrentHashSet(iterable: java.lang.Iterable[_newConcurrentHashSet_1__E]) -> java.util.Set[_newConcurrentHashSet_1__E]: ...
    _newCopyOnWriteArraySet_0__E = typing.TypeVar('_newCopyOnWriteArraySet_0__E')  # <E>
    _newCopyOnWriteArraySet_1__E = typing.TypeVar('_newCopyOnWriteArraySet_1__E')  # <E>
    @typing.overload
    @staticmethod
    def newCopyOnWriteArraySet() -> java.util.concurrent.CopyOnWriteArraySet[_newCopyOnWriteArraySet_0__E]: ...
    @typing.overload
    @staticmethod
    def newCopyOnWriteArraySet(iterable: java.lang.Iterable[_newCopyOnWriteArraySet_1__E]) -> java.util.concurrent.CopyOnWriteArraySet[_newCopyOnWriteArraySet_1__E]: ...
    _newEnumSet__E = typing.TypeVar('_newEnumSet__E', bound=java.lang.Enum)  # <E>
    @staticmethod
    def newEnumSet(iterable: java.lang.Iterable[_newEnumSet__E], class_: typing.Type[_newEnumSet__E]) -> java.util.EnumSet[_newEnumSet__E]: ...
    _newHashSet_0__E = typing.TypeVar('_newHashSet_0__E')  # <E>
    _newHashSet_1__E = typing.TypeVar('_newHashSet_1__E')  # <E>
    _newHashSet_2__E = typing.TypeVar('_newHashSet_2__E')  # <E>
    _newHashSet_3__E = typing.TypeVar('_newHashSet_3__E')  # <E>
    @typing.overload
    @staticmethod
    def newHashSet() -> java.util.HashSet[_newHashSet_0__E]: ...
    @typing.overload
    @staticmethod
    def newHashSet(iterable: java.lang.Iterable[_newHashSet_1__E]) -> java.util.HashSet[_newHashSet_1__E]: ...
    @typing.overload
    @staticmethod
    def newHashSet(eArray: typing.List[_newHashSet_2__E]) -> java.util.HashSet[_newHashSet_2__E]: ...
    @typing.overload
    @staticmethod
    def newHashSet(iterator: java.util.Iterator[_newHashSet_3__E]) -> java.util.HashSet[_newHashSet_3__E]: ...
    _newHashSetWithExpectedSize__E = typing.TypeVar('_newHashSetWithExpectedSize__E')  # <E>
    @staticmethod
    def newHashSetWithExpectedSize(int: int) -> java.util.HashSet[_newHashSetWithExpectedSize__E]: ...
    _newIdentityHashSet__E = typing.TypeVar('_newIdentityHashSet__E')  # <E>
    @staticmethod
    def newIdentityHashSet() -> java.util.Set[_newIdentityHashSet__E]: ...
    _newLinkedHashSet_0__E = typing.TypeVar('_newLinkedHashSet_0__E')  # <E>
    _newLinkedHashSet_1__E = typing.TypeVar('_newLinkedHashSet_1__E')  # <E>
    @typing.overload
    @staticmethod
    def newLinkedHashSet() -> java.util.LinkedHashSet[_newLinkedHashSet_0__E]: ...
    @typing.overload
    @staticmethod
    def newLinkedHashSet(iterable: java.lang.Iterable[_newLinkedHashSet_1__E]) -> java.util.LinkedHashSet[_newLinkedHashSet_1__E]: ...
    _newLinkedHashSetWithExpectedSize__E = typing.TypeVar('_newLinkedHashSetWithExpectedSize__E')  # <E>
    @staticmethod
    def newLinkedHashSetWithExpectedSize(int: int) -> java.util.LinkedHashSet[_newLinkedHashSetWithExpectedSize__E]: ...
    _newSetFromMap__E = typing.TypeVar('_newSetFromMap__E')  # <E>
    @staticmethod
    def newSetFromMap(map: typing.Union[java.util.Map[_newSetFromMap__E, bool], typing.Mapping[_newSetFromMap__E, bool]]) -> java.util.Set[_newSetFromMap__E]: ...
    _newTreeSet_0__E = typing.TypeVar('_newTreeSet_0__E', bound=java.lang.Comparable)  # <E>
    _newTreeSet_1__E = typing.TypeVar('_newTreeSet_1__E', bound=java.lang.Comparable)  # <E>
    _newTreeSet_2__E = typing.TypeVar('_newTreeSet_2__E')  # <E>
    @typing.overload
    @staticmethod
    def newTreeSet() -> java.util.TreeSet[_newTreeSet_0__E]: ...
    @typing.overload
    @staticmethod
    def newTreeSet(iterable: java.lang.Iterable[_newTreeSet_1__E]) -> java.util.TreeSet[_newTreeSet_1__E]: ...
    @typing.overload
    @staticmethod
    def newTreeSet(comparator: typing.Union[java.util.Comparator[_newTreeSet_2__E], typing.Callable[[_newTreeSet_2__E, _newTreeSet_2__E], int]]) -> java.util.TreeSet[_newTreeSet_2__E]: ...
    _powerSet__E = typing.TypeVar('_powerSet__E')  # <E>
    @staticmethod
    def powerSet(set: java.util.Set[_powerSet__E]) -> java.util.Set[java.util.Set[_powerSet__E]]: ...
    _subSet__K = typing.TypeVar('_subSet__K', bound=java.lang.Comparable)  # <K>
    @staticmethod
    def subSet(navigableSet: java.util.NavigableSet[_subSet__K], range: 'Range'[_subSet__K]) -> java.util.NavigableSet[_subSet__K]: ...
    _symmetricDifference__E = typing.TypeVar('_symmetricDifference__E')  # <E>
    @staticmethod
    def symmetricDifference(set: java.util.Set[_symmetricDifference__E], set2: java.util.Set[_symmetricDifference__E]) -> 'Sets.SetView'[_symmetricDifference__E]: ...
    _synchronizedNavigableSet__E = typing.TypeVar('_synchronizedNavigableSet__E')  # <E>
    @staticmethod
    def synchronizedNavigableSet(navigableSet: java.util.NavigableSet[_synchronizedNavigableSet__E]) -> java.util.NavigableSet[_synchronizedNavigableSet__E]: ...
    _toImmutableEnumSet__E = typing.TypeVar('_toImmutableEnumSet__E', bound=java.lang.Enum)  # <E>
    @staticmethod
    def toImmutableEnumSet() -> java.util.stream.Collector[_toImmutableEnumSet__E, typing.Any, 'ImmutableSet'[_toImmutableEnumSet__E]]: ...
    _union__E = typing.TypeVar('_union__E')  # <E>
    @staticmethod
    def union(set: java.util.Set[_union__E], set2: java.util.Set[_union__E]) -> 'Sets.SetView'[_union__E]: ...
    _unmodifiableNavigableSet__E = typing.TypeVar('_unmodifiableNavigableSet__E')  # <E>
    @staticmethod
    def unmodifiableNavigableSet(navigableSet: java.util.NavigableSet[_unmodifiableNavigableSet__E]) -> java.util.NavigableSet[_unmodifiableNavigableSet__E]: ...
    class SetView(java.util.AbstractSet[_Sets__SetView__E], typing.Generic[_Sets__SetView__E]):
        def add(self, e: _Sets__SetView__E) -> bool: ...
        def addAll(self, collection: typing.Union[java.util.Collection[_Sets__SetView__E], typing.Sequence[_Sets__SetView__E]]) -> bool: ...
        def clear(self) -> None: ...
        _copyInto__S = typing.TypeVar('_copyInto__S', bound=java.util.Set)  # <S>
        def copyInto(self, s2: _copyInto__S) -> _copyInto__S: ...
        def immutableCopy(self) -> 'ImmutableSet'[_Sets__SetView__E]: ...
        def iterator(self) -> 'UnmodifiableIterator'[_Sets__SetView__E]: ...
        def remove(self, object: typing.Any) -> bool: ...
        def removeAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
        def removeIf(self, predicate: typing.Union[java.util.function.Predicate[_Sets__SetView__E], typing.Callable[[_Sets__SetView__E], bool]]) -> bool: ...
        def retainAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...

_Streams__DoubleFunctionWithIndex__R = typing.TypeVar('_Streams__DoubleFunctionWithIndex__R')  # <R>
_Streams__FunctionWithIndex__T = typing.TypeVar('_Streams__FunctionWithIndex__T')  # <T>
_Streams__FunctionWithIndex__R = typing.TypeVar('_Streams__FunctionWithIndex__R')  # <R>
_Streams__IntFunctionWithIndex__R = typing.TypeVar('_Streams__IntFunctionWithIndex__R')  # <R>
_Streams__LongFunctionWithIndex__R = typing.TypeVar('_Streams__LongFunctionWithIndex__R')  # <R>
class Streams:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Static utility methods related to :code:`Stream` instances.
    
        Since:
            21.0
    """
    _concat_3__T = typing.TypeVar('_concat_3__T')  # <T>
    @typing.overload
    @staticmethod
    def concat(doubleStreamArray: typing.List[java.util.stream.DoubleStream]) -> java.util.stream.DoubleStream: ...
    @typing.overload
    @staticmethod
    def concat(intStreamArray: typing.List[java.util.stream.IntStream]) -> java.util.stream.IntStream: ...
    @typing.overload
    @staticmethod
    def concat(longStreamArray: typing.List[java.util.stream.LongStream]) -> java.util.stream.LongStream: ...
    @typing.overload
    @staticmethod
    def concat(streamArray: typing.List[java.util.stream.Stream[_concat_3__T]]) -> java.util.stream.Stream[_concat_3__T]: ...
    _findLast_0__T = typing.TypeVar('_findLast_0__T')  # <T>
    @typing.overload
    @staticmethod
    def findLast(stream: java.util.stream.Stream[_findLast_0__T]) -> java.util.Optional[_findLast_0__T]: ...
    @typing.overload
    @staticmethod
    def findLast(doubleStream: java.util.stream.DoubleStream) -> java.util.OptionalDouble: ...
    @typing.overload
    @staticmethod
    def findLast(intStream: java.util.stream.IntStream) -> java.util.OptionalInt: ...
    @typing.overload
    @staticmethod
    def findLast(longStream: java.util.stream.LongStream) -> java.util.OptionalLong: ...
    _forEachPair__A = typing.TypeVar('_forEachPair__A')  # <A>
    _forEachPair__B = typing.TypeVar('_forEachPair__B')  # <B>
    @staticmethod
    def forEachPair(stream: java.util.stream.Stream[_forEachPair__A], stream2: java.util.stream.Stream[_forEachPair__B], biConsumer: typing.Union[java.util.function.BiConsumer[_forEachPair__A, _forEachPair__B], typing.Callable[[_forEachPair__A, _forEachPair__B], None]]) -> None: ...
    _mapWithIndex_0__R = typing.TypeVar('_mapWithIndex_0__R')  # <R>
    _mapWithIndex_1__R = typing.TypeVar('_mapWithIndex_1__R')  # <R>
    _mapWithIndex_2__R = typing.TypeVar('_mapWithIndex_2__R')  # <R>
    _mapWithIndex_3__T = typing.TypeVar('_mapWithIndex_3__T')  # <T>
    _mapWithIndex_3__R = typing.TypeVar('_mapWithIndex_3__R')  # <R>
    @typing.overload
    @staticmethod
    def mapWithIndex(doubleStream: java.util.stream.DoubleStream, doubleFunctionWithIndex: 'Streams.DoubleFunctionWithIndex'[_mapWithIndex_0__R]) -> java.util.stream.Stream[_mapWithIndex_0__R]: ...
    @typing.overload
    @staticmethod
    def mapWithIndex(intStream: java.util.stream.IntStream, intFunctionWithIndex: 'Streams.IntFunctionWithIndex'[_mapWithIndex_1__R]) -> java.util.stream.Stream[_mapWithIndex_1__R]: ...
    @typing.overload
    @staticmethod
    def mapWithIndex(longStream: java.util.stream.LongStream, longFunctionWithIndex: 'Streams.LongFunctionWithIndex'[_mapWithIndex_2__R]) -> java.util.stream.Stream[_mapWithIndex_2__R]: ...
    @typing.overload
    @staticmethod
    def mapWithIndex(stream: java.util.stream.Stream[_mapWithIndex_3__T], functionWithIndex: 'Streams.FunctionWithIndex'[_mapWithIndex_3__T, _mapWithIndex_3__R]) -> java.util.stream.Stream[_mapWithIndex_3__R]: ...
    _stream_3__T = typing.TypeVar('_stream_3__T')  # <T>
    _stream_4__T = typing.TypeVar('_stream_4__T')  # <T>
    _stream_5__T = typing.TypeVar('_stream_5__T')  # <T>
    _stream_6__T = typing.TypeVar('_stream_6__T')  # <T>
    _stream_7__T = typing.TypeVar('_stream_7__T')  # <T>
    @typing.overload
    @staticmethod
    def stream(optionalDouble: java.util.OptionalDouble) -> java.util.stream.DoubleStream: ...
    @typing.overload
    @staticmethod
    def stream(optionalInt: java.util.OptionalInt) -> java.util.stream.IntStream: ...
    @typing.overload
    @staticmethod
    def stream(optionalLong: java.util.OptionalLong) -> java.util.stream.LongStream: ...
    @typing.overload
    @staticmethod
    def stream(optional: com.google.common.base.Optional[_stream_3__T]) -> java.util.stream.Stream[_stream_3__T]: ...
    @typing.overload
    @staticmethod
    def stream(iterable: java.lang.Iterable[_stream_4__T]) -> java.util.stream.Stream[_stream_4__T]: ...
    @typing.overload
    @staticmethod
    def stream(collection: typing.Union[java.util.Collection[_stream_5__T], typing.Sequence[_stream_5__T]]) -> java.util.stream.Stream[_stream_5__T]: ...
    @typing.overload
    @staticmethod
    def stream(iterator: java.util.Iterator[_stream_6__T]) -> java.util.stream.Stream[_stream_6__T]: ...
    @typing.overload
    @staticmethod
    def stream(optional: java.util.Optional[_stream_7__T]) -> java.util.stream.Stream[_stream_7__T]: ...
    _zip__A = typing.TypeVar('_zip__A')  # <A>
    _zip__B = typing.TypeVar('_zip__B')  # <B>
    _zip__R = typing.TypeVar('_zip__R')  # <R>
    @staticmethod
    def zip(stream: java.util.stream.Stream[_zip__A], stream2: java.util.stream.Stream[_zip__B], biFunction: typing.Union[java.util.function.BiFunction[_zip__A, _zip__B, _zip__R], typing.Callable[[_zip__A, _zip__B], _zip__R]]) -> java.util.stream.Stream[_zip__R]: ...
    class DoubleFunctionWithIndex(typing.Generic[_Streams__DoubleFunctionWithIndex__R]):
        def apply(self, double: float, long: int) -> _Streams__DoubleFunctionWithIndex__R: ...
    class FunctionWithIndex(typing.Generic[_Streams__FunctionWithIndex__T, _Streams__FunctionWithIndex__R]):
        def apply(self, t: _Streams__FunctionWithIndex__T, long: int) -> _Streams__FunctionWithIndex__R: ...
    class IntFunctionWithIndex(typing.Generic[_Streams__IntFunctionWithIndex__R]):
        def apply(self, int: int, long: int) -> _Streams__IntFunctionWithIndex__R: ...
    class LongFunctionWithIndex(typing.Generic[_Streams__LongFunctionWithIndex__R]):
        def apply(self, long: int, long2: int) -> _Streams__LongFunctionWithIndex__R: ...

_Table__Cell__R = typing.TypeVar('_Table__Cell__R')  # <R>
_Table__Cell__C = typing.TypeVar('_Table__Cell__C')  # <C>
_Table__Cell__V = typing.TypeVar('_Table__Cell__V')  # <V>
_Table__R = typing.TypeVar('_Table__R')  # <R>
_Table__C = typing.TypeVar('_Table__C')  # <C>
_Table__V = typing.TypeVar('_Table__V')  # <V>
class Table(typing.Generic[_Table__R, _Table__C, _Table__V]):
    def cellSet(self) -> java.util.Set['Table.Cell'[_Table__R, _Table__C, _Table__V]]: ...
    def clear(self) -> None: ...
    def column(self, c: _Table__C) -> java.util.Map[_Table__R, _Table__V]: ...
    def columnKeySet(self) -> java.util.Set[_Table__C]: ...
    def columnMap(self) -> java.util.Map[_Table__C, java.util.Map[_Table__R, _Table__V]]: ...
    def contains(self, object: typing.Any, object2: typing.Any) -> bool: ...
    def containsColumn(self, object: typing.Any) -> bool: ...
    def containsRow(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, object: typing.Any, object2: typing.Any) -> _Table__V: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def put(self, r: _Table__R, c: _Table__C, v: _Table__V) -> _Table__V: ...
    def putAll(self, table: 'Table'[_Table__R, _Table__C, _Table__V]) -> None: ...
    def remove(self, object: typing.Any, object2: typing.Any) -> _Table__V: ...
    def row(self, r: _Table__R) -> java.util.Map[_Table__C, _Table__V]: ...
    def rowKeySet(self) -> java.util.Set[_Table__R]: ...
    def rowMap(self) -> java.util.Map[_Table__R, java.util.Map[_Table__C, _Table__V]]: ...
    def size(self) -> int: ...
    def values(self) -> java.util.Collection[_Table__V]: ...
    class Cell(typing.Generic[_Table__Cell__R, _Table__Cell__C, _Table__Cell__V]):
        def equals(self, object: typing.Any) -> bool: ...
        def getColumnKey(self) -> _Table__Cell__C: ...
        def getRowKey(self) -> _Table__Cell__R: ...
        def getValue(self) -> _Table__Cell__V: ...
        def hashCode(self) -> int: ...

class Tables:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Provides static methods that involve a :code:`Table`.
    
        See the Guava User Guide article on null.
    
        Since:
            7.0
    """
    _immutableCell__R = typing.TypeVar('_immutableCell__R')  # <R>
    _immutableCell__C = typing.TypeVar('_immutableCell__C')  # <C>
    _immutableCell__V = typing.TypeVar('_immutableCell__V')  # <V>
    @staticmethod
    def immutableCell(r: _immutableCell__R, c: _immutableCell__C, v: _immutableCell__V) -> Table.Cell[_immutableCell__R, _immutableCell__C, _immutableCell__V]: ...
    _newCustomTable__R = typing.TypeVar('_newCustomTable__R')  # <R>
    _newCustomTable__C = typing.TypeVar('_newCustomTable__C')  # <C>
    _newCustomTable__V = typing.TypeVar('_newCustomTable__V')  # <V>
    @staticmethod
    def newCustomTable(map: typing.Union[java.util.Map[_newCustomTable__R, typing.Union[java.util.Map[_newCustomTable__C, _newCustomTable__V], typing.Mapping[_newCustomTable__C, _newCustomTable__V]]], typing.Mapping[_newCustomTable__R, typing.Union[java.util.Map[_newCustomTable__C, _newCustomTable__V], typing.Mapping[_newCustomTable__C, _newCustomTable__V]]]], supplier: typing.Union[com.google.common.base.Supplier[java.util.Map[_newCustomTable__C, _newCustomTable__V]], typing.Callable[[], java.util.Map[_newCustomTable__C, _newCustomTable__V]]]) -> Table[_newCustomTable__R, _newCustomTable__C, _newCustomTable__V]: ...
    _synchronizedTable__R = typing.TypeVar('_synchronizedTable__R')  # <R>
    _synchronizedTable__C = typing.TypeVar('_synchronizedTable__C')  # <C>
    _synchronizedTable__V = typing.TypeVar('_synchronizedTable__V')  # <V>
    @staticmethod
    def synchronizedTable(table: Table[_synchronizedTable__R, _synchronizedTable__C, _synchronizedTable__V]) -> Table[_synchronizedTable__R, _synchronizedTable__C, _synchronizedTable__V]: ...
    _toTable_0__T = typing.TypeVar('_toTable_0__T')  # <T>
    _toTable_0__R = typing.TypeVar('_toTable_0__R')  # <R>
    _toTable_0__C = typing.TypeVar('_toTable_0__C')  # <C>
    _toTable_0__V = typing.TypeVar('_toTable_0__V')  # <V>
    _toTable_0__I = typing.TypeVar('_toTable_0__I', bound=Table)  # <I>
    _toTable_1__T = typing.TypeVar('_toTable_1__T')  # <T>
    _toTable_1__R = typing.TypeVar('_toTable_1__R')  # <R>
    _toTable_1__C = typing.TypeVar('_toTable_1__C')  # <C>
    _toTable_1__V = typing.TypeVar('_toTable_1__V')  # <V>
    _toTable_1__I = typing.TypeVar('_toTable_1__I', bound=Table)  # <I>
    @typing.overload
    @staticmethod
    def toTable(function: typing.Union[java.util.function.Function[_toTable_0__T, _toTable_0__R], typing.Callable[[_toTable_0__T], _toTable_0__R]], function2: typing.Union[java.util.function.Function[_toTable_0__T, _toTable_0__C], typing.Callable[[_toTable_0__T], _toTable_0__C]], function3: typing.Union[java.util.function.Function[_toTable_0__T, _toTable_0__V], typing.Callable[[_toTable_0__T], _toTable_0__V]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toTable_0__V], typing.Callable], supplier: typing.Union[java.util.function.Supplier[_toTable_0__I], typing.Callable[[], _toTable_0__I]]) -> java.util.stream.Collector[_toTable_0__T, typing.Any, _toTable_0__I]: ...
    @typing.overload
    @staticmethod
    def toTable(function: typing.Union[java.util.function.Function[_toTable_1__T, _toTable_1__R], typing.Callable[[_toTable_1__T], _toTable_1__R]], function2: typing.Union[java.util.function.Function[_toTable_1__T, _toTable_1__C], typing.Callable[[_toTable_1__T], _toTable_1__C]], function3: typing.Union[java.util.function.Function[_toTable_1__T, _toTable_1__V], typing.Callable[[_toTable_1__T], _toTable_1__V]], supplier: typing.Union[java.util.function.Supplier[_toTable_1__I], typing.Callable[[], _toTable_1__I]]) -> java.util.stream.Collector[_toTable_1__T, typing.Any, _toTable_1__I]: ...
    _transformValues__R = typing.TypeVar('_transformValues__R')  # <R>
    _transformValues__C = typing.TypeVar('_transformValues__C')  # <C>
    _transformValues__V1 = typing.TypeVar('_transformValues__V1')  # <V1>
    _transformValues__V2 = typing.TypeVar('_transformValues__V2')  # <V2>
    @staticmethod
    def transformValues(table: Table[_transformValues__R, _transformValues__C, _transformValues__V1], function: typing.Union[com.google.common.base.Function[_transformValues__V1, _transformValues__V2], typing.Callable[[_transformValues__V1], _transformValues__V2]]) -> Table[_transformValues__R, _transformValues__C, _transformValues__V2]: ...
    _transpose__R = typing.TypeVar('_transpose__R')  # <R>
    _transpose__C = typing.TypeVar('_transpose__C')  # <C>
    _transpose__V = typing.TypeVar('_transpose__V')  # <V>
    @staticmethod
    def transpose(table: Table[_transpose__R, _transpose__C, _transpose__V]) -> Table[_transpose__C, _transpose__R, _transpose__V]: ...
    _unmodifiableRowSortedTable__R = typing.TypeVar('_unmodifiableRowSortedTable__R')  # <R>
    _unmodifiableRowSortedTable__C = typing.TypeVar('_unmodifiableRowSortedTable__C')  # <C>
    _unmodifiableRowSortedTable__V = typing.TypeVar('_unmodifiableRowSortedTable__V')  # <V>
    @staticmethod
    def unmodifiableRowSortedTable(rowSortedTable: 'RowSortedTable'[_unmodifiableRowSortedTable__R, _unmodifiableRowSortedTable__C, _unmodifiableRowSortedTable__V]) -> 'RowSortedTable'[_unmodifiableRowSortedTable__R, _unmodifiableRowSortedTable__C, _unmodifiableRowSortedTable__V]: ...
    _unmodifiableTable__R = typing.TypeVar('_unmodifiableTable__R')  # <R>
    _unmodifiableTable__C = typing.TypeVar('_unmodifiableTable__C')  # <C>
    _unmodifiableTable__V = typing.TypeVar('_unmodifiableTable__V')  # <V>
    @staticmethod
    def unmodifiableTable(table: Table[_unmodifiableTable__R, _unmodifiableTable__C, _unmodifiableTable__V]) -> Table[_unmodifiableTable__R, _unmodifiableTable__C, _unmodifiableTable__V]: ...

_TreeTraverser__T = typing.TypeVar('_TreeTraverser__T')  # <T>
class TreeTraverser(typing.Generic[_TreeTraverser__T]):
    """
    Deprecated. 
    Use :class:`~com.google.common.graph.Traverser` instead. All instance methods have their equivalent on the result of
    :code:`Traverser.forTree(tree)` where :code:`tree` implements :code:`SuccessorsFunction`, which has a similar API as
    :meth:`~com.google.common.collect.TreeTraverser.children` or can be the same lambda function as passed into
    :meth:`~com.google.common.collect.TreeTraverser.using`. This class is scheduled to be removed in October 2019.
    @Deprecated :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<T> extends Object
    
        Views elements of a type :code:`T` as nodes in a tree, and provides methods to traverse the trees induced by this
        traverser.
    
        For example, the tree
    
        .. code-block: java
        
                h
              / | \
             /  e  \
            d       g
           /|\      |
          / | \     f
         a  b  c
         
    
        can be iterated over in preorder (hdabcegf), postorder (abcdefgh), or breadth-first order (hdegabcf).
    
        Null nodes are strictly forbidden.
    
        **For Java 8 users:** Because this is an abstract class, not an interface, you can't use a lambda expression to extend
        it:
    
        .. code-block: java
        
         // won't work
         TreeTraverser<NodeType> traverser = node -> node.getChildNodes();
         
        Instead, you can pass a lambda expression to the :code:`using` factory method:
    
        .. code-block: java
        
         TreeTraverser<NodeType> traverser = TreeTraverser.using(node -> node.getChildNodes());
         
    
        Since:
            15.0
    """
    def __init__(self): ...
    def breadthFirstTraversal(self, t: _TreeTraverser__T) -> FluentIterable[_TreeTraverser__T]: ...
    def children(self, t: _TreeTraverser__T) -> java.lang.Iterable[_TreeTraverser__T]: ...
    def postOrderTraversal(self, t: _TreeTraverser__T) -> FluentIterable[_TreeTraverser__T]: ...
    def preOrderTraversal(self, t: _TreeTraverser__T) -> FluentIterable[_TreeTraverser__T]: ...
    _using__T = typing.TypeVar('_using__T')  # <T>
    @staticmethod
    def using(function: typing.Union[com.google.common.base.Function[_using__T, java.lang.Iterable[_using__T]], typing.Callable[[_using__T], java.lang.Iterable[_using__T]]]) -> 'TreeTraverser'[_using__T]: ...

_UnmodifiableIterator__E = typing.TypeVar('_UnmodifiableIterator__E')  # <E>
class UnmodifiableIterator(java.util.Iterator[_UnmodifiableIterator__E], typing.Generic[_UnmodifiableIterator__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<E> extends Object implements Iterator<E>
    
        An iterator that does not support :meth:`~com.google.common.collect.UnmodifiableIterator.remove`.
    
        :code:`UnmodifiableIterator` is used primarily in conjunction with implementations of
        :class:`~com.google.common.collect.ImmutableCollection`, such as :class:`~com.google.common.collect.ImmutableList`. You
        can, however, convert an existing iterator to an :code:`UnmodifiableIterator` using
        :meth:`~com.google.common.collect.Iterators.unmodifiableIterator`.
    
        Since:
            2.0
    """
    def remove(self) -> None: ...

_AbstractIterator__T = typing.TypeVar('_AbstractIterator__T')  # <T>
class AbstractIterator(UnmodifiableIterator[_AbstractIterator__T], typing.Generic[_AbstractIterator__T]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<T> extends :class:`~com.google.common.collect.UnmodifiableIterator`<T>
    
        This class provides a skeletal implementation of the :code:`Iterator` interface, to make this interface easier to
        implement for certain types of data sources.
    
        :code:`Iterator` requires its implementations to support querying the end-of-data status without changing the iterator's
        state, using the :meth:`~com.google.common.collect.AbstractIterator.hasNext` method. But many data sources, such as
        null, do not expose this information; the only way to discover whether there is any data left is by trying to retrieve
        it. These types of data sources are ordinarily difficult to write iterators for. But using this class, one must
        implement only the :meth:`~com.google.common.collect.AbstractIterator.computeNext` method, and invoke the
        :meth:`~com.google.common.collect.AbstractIterator.endOfData` method when appropriate.
    
        Another example is an iterator that skips over null elements in a backing iterator. This could be implemented as:
    
        .. code-block: java
        
         public static Iterator<String> skipNulls(final Iterator<String> in) {
           return new AbstractIterator<String>() {
             protected String computeNext() {
               while (in.hasNext()) {
                 String s = in.next();
                 if (s != null) {
                   return s;
                 }
               }
               return endOfData();
             }
           };
         }
         
    
        This class supports iterators that include null elements.
    
        Since:
            2.0
    """
    def hasNext(self) -> bool: ...
    def next(self) -> _AbstractIterator__T: ...
    def peek(self) -> _AbstractIterator__T: ...

_AbstractSequentialIterator__T = typing.TypeVar('_AbstractSequentialIterator__T')  # <T>
class AbstractSequentialIterator(UnmodifiableIterator[_AbstractSequentialIterator__T], typing.Generic[_AbstractSequentialIterator__T]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<T> extends :class:`~com.google.common.collect.UnmodifiableIterator`<T>
    
        This class provides a skeletal implementation of the :code:`Iterator` interface for sequences whose next element can
        always be derived from the previous element. Null elements are not supported, nor is the
        :meth:`~com.google.common.collect.UnmodifiableIterator.remove` method.
    
        Example:
    
        .. code-block: java
        
         Iterator<Integer> powersOfTwo =
             new AbstractSequentialIterator<Integer>(1) {
               protected Integer computeNext(Integer previous) {
                 return (previous == 1 << 30) ? null : previous * 2;
               }
             };
         
    
        Since:
            12.0 (in Guava as :code:`AbstractLinkedIterator` since 8.0)
    """
    def hasNext(self) -> bool: ...
    def next(self) -> _AbstractSequentialIterator__T: ...

_ForwardingCollection__E = typing.TypeVar('_ForwardingCollection__E')  # <E>
class ForwardingCollection(ForwardingObject, java.util.Collection[_ForwardingCollection__E], typing.Generic[_ForwardingCollection__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingObject` implements Collection<E>
    
        A collection which forwards all its method calls to another collection. Subclasses should override one or more methods
        to modify the behavior of the backing collection as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingCollection` forward **indiscriminately** to the methods of the delegate.
        For example, overriding :meth:`~com.google.common.collect.ForwardingCollection.add` alone **will not** change the
        behavior of :meth:`~com.google.common.collect.ForwardingCollection.addAll`, which can lead to unexpected behavior. In
        this case, you should override :code:`addAll` as well, either providing your own implementation, or delegating to the
        provided :code:`standardAddAll` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingCollection`.
    
        The :code:`standard` methods are not guaranteed to be thread-safe, even when all of the methods that they depend on are
        thread-safe.
    
        Since:
            2.0
    """
    def add(self, e: _ForwardingCollection__E) -> bool: ...
    def addAll(self, collection: typing.Union[java.util.Collection[_ForwardingCollection__E], typing.Sequence[_ForwardingCollection__E]]) -> bool: ...
    def clear(self) -> None: ...
    def contains(self, object: typing.Any) -> bool: ...
    def containsAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> java.util.Iterator[_ForwardingCollection__E]: ...
    def remove(self, object: typing.Any) -> bool: ...
    def removeAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def retainAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def size(self) -> int: ...
    _toArray_0__T = typing.TypeVar('_toArray_0__T')  # <T>
    _toArray_2__T = typing.TypeVar('_toArray_2__T')  # <T>
    @typing.overload
    def toArray(self, intFunction: typing.Union[java.util.function.IntFunction[typing.List[_toArray_0__T]], typing.Callable[[int], typing.List[_toArray_0__T]]]) -> typing.List[_toArray_0__T]: ...
    @typing.overload
    def toArray(self) -> typing.List[typing.Any]: ...
    @typing.overload
    def toArray(self, tArray: typing.List[_toArray_2__T]) -> typing.List[_toArray_2__T]: ...

_ForwardingIterator__T = typing.TypeVar('_ForwardingIterator__T')  # <T>
class ForwardingIterator(ForwardingObject, java.util.Iterator[_ForwardingIterator__T], typing.Generic[_ForwardingIterator__T]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<T> extends :class:`~com.google.common.collect.ForwardingObject` implements Iterator<T>
    
        An iterator which forwards all its method calls to another iterator. Subclasses should override one or more methods to
        modify the behavior of the backing iterator as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **:code:`default` method warning:** This class forwards calls to *only some* :code:`default` methods. Specifically, it
        forwards calls only for methods that existed null. For newer methods, like :code:`forEachRemaining`, it inherits their
        default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingIterator`.
    
        Since:
            2.0
    """
    def hasNext(self) -> bool: ...
    def next(self) -> _ForwardingIterator__T: ...
    def remove(self) -> None: ...

_ForwardingMap__K = typing.TypeVar('_ForwardingMap__K')  # <K>
_ForwardingMap__V = typing.TypeVar('_ForwardingMap__V')  # <V>
class ForwardingMap(ForwardingObject, java.util.Map[_ForwardingMap__K, _ForwardingMap__V], typing.Generic[_ForwardingMap__K, _ForwardingMap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ForwardingObject` implements Map<K,V>
    
        A map which forwards all its method calls to another map. Subclasses should override one or more methods to modify the
        behavior of the backing map as desired per the `decorator pattern <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingMap` forward *indiscriminately* to the methods of the delegate. For
        example, overriding :meth:`~com.google.common.collect.ForwardingMap.put` alone *will not* change the behavior of
        :meth:`~com.google.common.collect.ForwardingMap.putAll`, which can lead to unexpected behavior. In this case, you should
        override :code:`putAll` as well, either providing your own implementation, or delegating to the provided
        :code:`standardPutAll` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingMap`.
    
        Each of the :code:`standard` methods, where appropriate, use :meth:`~com.google.common.base.Objects.equal` to test
        equality for both keys and values. This may not be the desired behavior for map implementations that use non-standard
        notions of key equality, such as a :code:`SortedMap` whose comparator is not consistent with :code:`equals`.
    
        The :code:`standard` methods and the collection views they return are not guaranteed to be thread-safe, even when all of
        the methods that they depend on are thread-safe.
    
        Since:
            2.0
    """
    def clear(self) -> None: ...
    def containsKey(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    def entrySet(self) -> java.util.Set[java.util.Map.Entry[_ForwardingMap__K, _ForwardingMap__V]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, object: typing.Any) -> _ForwardingMap__V: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def keySet(self) -> java.util.Set[_ForwardingMap__K]: ...
    def put(self, k: _ForwardingMap__K, v: _ForwardingMap__V) -> _ForwardingMap__V: ...
    def putAll(self, map: typing.Union[java.util.Map[_ForwardingMap__K, _ForwardingMap__V], typing.Mapping[_ForwardingMap__K, _ForwardingMap__V]]) -> None: ...
    @typing.overload
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any) -> _ForwardingMap__V: ...
    def size(self) -> int: ...
    def values(self) -> java.util.Collection[_ForwardingMap__V]: ...

_ForwardingMapEntry__K = typing.TypeVar('_ForwardingMapEntry__K')  # <K>
_ForwardingMapEntry__V = typing.TypeVar('_ForwardingMapEntry__V')  # <V>
class ForwardingMapEntry(ForwardingObject, java.util.Map.Entry[_ForwardingMapEntry__K, _ForwardingMapEntry__V], typing.Generic[_ForwardingMapEntry__K, _ForwardingMapEntry__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ForwardingObject` implements Map.Entry<K,V>
    
        A map entry which forwards all its method calls to another map entry. Subclasses should override one or more methods to
        modify the behavior of the backing map entry as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingMapEntry` forward *indiscriminately* to the methods of the delegate. For
        example, overriding :meth:`~com.google.common.collect.ForwardingMapEntry.getValue` alone *will not* change the behavior
        of :meth:`~com.google.common.collect.ForwardingMapEntry.equals`, which can lead to unexpected behavior. In this case,
        you should override :code:`equals` as well, either providing your own implementation, or delegating to the provided
        :code:`standardEquals` method.
    
        Each of the :code:`standard` methods, where appropriate, use :meth:`~com.google.common.base.Objects.equal` to test
        equality for both keys and values. This may not be the desired behavior for map implementations that use non-standard
        notions of key equality, such as the entry of a :code:`SortedMap` whose comparator is not consistent with
        :code:`equals`.
    
        The :code:`standard` methods are not guaranteed to be thread-safe, even when all of the methods that they depend on are
        thread-safe.
    
        Since:
            2.0
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getKey(self) -> _ForwardingMapEntry__K: ...
    def getValue(self) -> _ForwardingMapEntry__V: ...
    def hashCode(self) -> int: ...
    def setValue(self, v: _ForwardingMapEntry__V) -> _ForwardingMapEntry__V: ...

_ForwardingMultimap__K = typing.TypeVar('_ForwardingMultimap__K')  # <K>
_ForwardingMultimap__V = typing.TypeVar('_ForwardingMultimap__V')  # <V>
class ForwardingMultimap(ForwardingObject, Multimap[_ForwardingMultimap__K, _ForwardingMultimap__V], typing.Generic[_ForwardingMultimap__K, _ForwardingMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ForwardingObject` implements :class:`~com.google.common.collect.Multimap`<K,V>
    
        A multimap which forwards all its method calls to another multimap. Subclasses should override one or more methods to
        modify the behavior of the backing multimap as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingMultimap`.
    
        Since:
            2.0
    """
    def asMap(self) -> java.util.Map[_ForwardingMultimap__K, java.util.Collection[_ForwardingMultimap__V]]: ...
    def clear(self) -> None: ...
    def containsEntry(self, object: typing.Any, object2: typing.Any) -> bool: ...
    def containsKey(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    def entries(self) -> java.util.Collection[java.util.Map.Entry[_ForwardingMultimap__K, _ForwardingMultimap__V]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, k: _ForwardingMultimap__K) -> java.util.Collection[_ForwardingMultimap__V]: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def keySet(self) -> java.util.Set[_ForwardingMultimap__K]: ...
    def keys(self) -> Multiset[_ForwardingMultimap__K]: ...
    def put(self, k: _ForwardingMultimap__K, v: _ForwardingMultimap__V) -> bool: ...
    @typing.overload
    def putAll(self, multimap: Multimap[_ForwardingMultimap__K, _ForwardingMultimap__V]) -> bool: ...
    @typing.overload
    def putAll(self, k: _ForwardingMultimap__K, iterable: java.lang.Iterable[_ForwardingMultimap__V]) -> bool: ...
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...
    def removeAll(self, object: typing.Any) -> java.util.Collection[_ForwardingMultimap__V]: ...
    def replaceValues(self, k: _ForwardingMultimap__K, iterable: java.lang.Iterable[_ForwardingMultimap__V]) -> java.util.Collection[_ForwardingMultimap__V]: ...
    def size(self) -> int: ...
    def values(self) -> java.util.Collection[_ForwardingMultimap__V]: ...

_ForwardingTable__R = typing.TypeVar('_ForwardingTable__R')  # <R>
_ForwardingTable__C = typing.TypeVar('_ForwardingTable__C')  # <C>
_ForwardingTable__V = typing.TypeVar('_ForwardingTable__V')  # <V>
class ForwardingTable(ForwardingObject, Table[_ForwardingTable__R, _ForwardingTable__C, _ForwardingTable__V], typing.Generic[_ForwardingTable__R, _ForwardingTable__C, _ForwardingTable__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<R,C,V> extends :class:`~com.google.common.collect.ForwardingObject` implements :class:`~com.google.common.collect.Table`<R,C,V>
    
        A table which forwards all its method calls to another table. Subclasses should override one or more methods to modify
        the behavior of the backing map as desired per the `decorator pattern <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        Since:
            7.0
    """
    def cellSet(self) -> java.util.Set[Table.Cell[_ForwardingTable__R, _ForwardingTable__C, _ForwardingTable__V]]: ...
    def clear(self) -> None: ...
    def column(self, c: _ForwardingTable__C) -> java.util.Map[_ForwardingTable__R, _ForwardingTable__V]: ...
    def columnKeySet(self) -> java.util.Set[_ForwardingTable__C]: ...
    def columnMap(self) -> java.util.Map[_ForwardingTable__C, java.util.Map[_ForwardingTable__R, _ForwardingTable__V]]: ...
    def contains(self, object: typing.Any, object2: typing.Any) -> bool: ...
    def containsColumn(self, object: typing.Any) -> bool: ...
    def containsRow(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, object: typing.Any, object2: typing.Any) -> _ForwardingTable__V: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def put(self, r: _ForwardingTable__R, c: _ForwardingTable__C, v: _ForwardingTable__V) -> _ForwardingTable__V: ...
    def putAll(self, table: Table[_ForwardingTable__R, _ForwardingTable__C, _ForwardingTable__V]) -> None: ...
    def remove(self, object: typing.Any, object2: typing.Any) -> _ForwardingTable__V: ...
    def row(self, r: _ForwardingTable__R) -> java.util.Map[_ForwardingTable__C, _ForwardingTable__V]: ...
    def rowKeySet(self) -> java.util.Set[_ForwardingTable__R]: ...
    def rowMap(self) -> java.util.Map[_ForwardingTable__R, java.util.Map[_ForwardingTable__C, _ForwardingTable__V]]: ...
    def size(self) -> int: ...
    def values(self) -> java.util.Collection[_ForwardingTable__V]: ...

_ImmutableList__Builder__E = typing.TypeVar('_ImmutableList__Builder__E')  # <E>
_ImmutableList__E = typing.TypeVar('_ImmutableList__E')  # <E>
class ImmutableList(ImmutableCollection[_ImmutableList__E], java.util.List[_ImmutableList__E], java.util.RandomAccess, typing.Generic[_ImmutableList__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ImmutableCollection`<E> implements List<E>, RandomAccess
    
        A null whose contents will never change, with many other important properties detailed at
        :class:`~com.google.common.collect.ImmutableCollection`.
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            2.0
    
        Also see:
            :class:`~com.google.common.collect.ImmutableMap`, :class:`~com.google.common.collect.ImmutableSet`, :meth:`~serialized`
    """
    @typing.overload
    def add(self, e: _ImmutableList__E) -> bool: ...
    @typing.overload
    def add(self, int: int, e: _ImmutableList__E) -> None: ...
    @typing.overload
    def addAll(self, collection: typing.Union[java.util.Collection[_ImmutableList__E], typing.Sequence[_ImmutableList__E]]) -> bool: ...
    @typing.overload
    def addAll(self, int: int, collection: typing.Union[java.util.Collection[_ImmutableList__E], typing.Sequence[_ImmutableList__E]]) -> bool: ...
    def asList(self) -> 'ImmutableList'[_ImmutableList__E]: ...
    _builder__E = typing.TypeVar('_builder__E')  # <E>
    @staticmethod
    def builder() -> 'ImmutableList.Builder'[_builder__E]: ...
    _builderWithExpectedSize__E = typing.TypeVar('_builderWithExpectedSize__E')  # <E>
    @staticmethod
    def builderWithExpectedSize(int: int) -> 'ImmutableList.Builder'[_builderWithExpectedSize__E]: ...
    def contains(self, object: typing.Any) -> bool: ...
    _copyOf_0__E = typing.TypeVar('_copyOf_0__E')  # <E>
    _copyOf_1__E = typing.TypeVar('_copyOf_1__E')  # <E>
    _copyOf_2__E = typing.TypeVar('_copyOf_2__E')  # <E>
    _copyOf_3__E = typing.TypeVar('_copyOf_3__E')  # <E>
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[_copyOf_0__E]) -> 'ImmutableList'[_copyOf_0__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(eArray: typing.List[_copyOf_1__E]) -> 'ImmutableList'[_copyOf_1__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(collection: typing.Union[java.util.Collection[_copyOf_2__E], typing.Sequence[_copyOf_2__E]]) -> 'ImmutableList'[_copyOf_2__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterator: java.util.Iterator[_copyOf_3__E]) -> 'ImmutableList'[_copyOf_3__E]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def forEach(self, consumer: typing.Union[java.util.function.Consumer[_ImmutableList__E], typing.Callable[[_ImmutableList__E], None]]) -> None: ...
    def hashCode(self) -> int: ...
    def indexOf(self, object: typing.Any) -> int: ...
    def iterator(self) -> UnmodifiableIterator[_ImmutableList__E]: ...
    def lastIndexOf(self, object: typing.Any) -> int: ...
    @typing.overload
    def listIterator(self) -> 'UnmodifiableListIterator'[_ImmutableList__E]: ...
    @typing.overload
    def listIterator(self, int: int) -> 'UnmodifiableListIterator'[_ImmutableList__E]: ...
    _of_0__E = typing.TypeVar('_of_0__E')  # <E>
    _of_1__E = typing.TypeVar('_of_1__E')  # <E>
    _of_2__E = typing.TypeVar('_of_2__E')  # <E>
    _of_3__E = typing.TypeVar('_of_3__E')  # <E>
    _of_4__E = typing.TypeVar('_of_4__E')  # <E>
    _of_5__E = typing.TypeVar('_of_5__E')  # <E>
    _of_6__E = typing.TypeVar('_of_6__E')  # <E>
    _of_7__E = typing.TypeVar('_of_7__E')  # <E>
    _of_8__E = typing.TypeVar('_of_8__E')  # <E>
    _of_9__E = typing.TypeVar('_of_9__E')  # <E>
    _of_10__E = typing.TypeVar('_of_10__E')  # <E>
    _of_11__E = typing.TypeVar('_of_11__E')  # <E>
    _of_12__E = typing.TypeVar('_of_12__E')  # <E>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableList'[_of_0__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_1__E) -> 'ImmutableList'[_of_1__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_2__E, e2: _of_2__E) -> 'ImmutableList'[_of_2__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_3__E, e2: _of_3__E, e3: _of_3__E) -> 'ImmutableList'[_of_3__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_4__E, e2: _of_4__E, e3: _of_4__E, e4: _of_4__E) -> 'ImmutableList'[_of_4__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_5__E, e2: _of_5__E, e3: _of_5__E, e4: _of_5__E, e5: _of_5__E) -> 'ImmutableList'[_of_5__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_6__E, e2: _of_6__E, e3: _of_6__E, e4: _of_6__E, e5: _of_6__E, e6: _of_6__E) -> 'ImmutableList'[_of_6__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_7__E, e2: _of_7__E, e3: _of_7__E, e4: _of_7__E, e5: _of_7__E, e6: _of_7__E, e7: _of_7__E) -> 'ImmutableList'[_of_7__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_8__E, e2: _of_8__E, e3: _of_8__E, e4: _of_8__E, e5: _of_8__E, e6: _of_8__E, e7: _of_8__E, e8: _of_8__E) -> 'ImmutableList'[_of_8__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_9__E, e2: _of_9__E, e3: _of_9__E, e4: _of_9__E, e5: _of_9__E, e6: _of_9__E, e7: _of_9__E, e8: _of_9__E, e9: _of_9__E) -> 'ImmutableList'[_of_9__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_10__E, e2: _of_10__E, e3: _of_10__E, e4: _of_10__E, e5: _of_10__E, e6: _of_10__E, e7: _of_10__E, e8: _of_10__E, e9: _of_10__E, e10: _of_10__E) -> 'ImmutableList'[_of_10__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_11__E, e2: _of_11__E, e3: _of_11__E, e4: _of_11__E, e5: _of_11__E, e6: _of_11__E, e7: _of_11__E, e8: _of_11__E, e9: _of_11__E, e10: _of_11__E, e11: _of_11__E) -> 'ImmutableList'[_of_11__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_12__E, e2: _of_12__E, e3: _of_12__E, e4: _of_12__E, e5: _of_12__E, e6: _of_12__E, e7: _of_12__E, e8: _of_12__E, e9: _of_12__E, e10: _of_12__E, e11: _of_12__E, e12: _of_12__E, eArray: typing.List[_of_12__E]) -> 'ImmutableList'[_of_12__E]: ...
    def replaceAll(self, unaryOperator: typing.Union[java.util.function.UnaryOperator[_ImmutableList__E], typing.Callable]) -> None: ...
    def reverse(self) -> 'ImmutableList'[_ImmutableList__E]: ...
    def set(self, int: int, e: _ImmutableList__E) -> _ImmutableList__E: ...
    def sort(self, comparator: typing.Union[java.util.Comparator[_ImmutableList__E], typing.Callable[[_ImmutableList__E, _ImmutableList__E], int]]) -> None: ...
    _sortedCopyOf_0__E = typing.TypeVar('_sortedCopyOf_0__E', bound=java.lang.Comparable)  # <E>
    _sortedCopyOf_1__E = typing.TypeVar('_sortedCopyOf_1__E')  # <E>
    @typing.overload
    @staticmethod
    def sortedCopyOf(iterable: java.lang.Iterable[_sortedCopyOf_0__E]) -> 'ImmutableList'[_sortedCopyOf_0__E]: ...
    @typing.overload
    @staticmethod
    def sortedCopyOf(comparator: typing.Union[java.util.Comparator[_sortedCopyOf_1__E], typing.Callable[[_sortedCopyOf_1__E, _sortedCopyOf_1__E], int]], iterable: java.lang.Iterable[_sortedCopyOf_1__E]) -> 'ImmutableList'[_sortedCopyOf_1__E]: ...
    def spliterator(self) -> java.util.Spliterator[_ImmutableList__E]: ...
    def subList(self, int: int, int2: int) -> 'ImmutableList'[_ImmutableList__E]: ...
    _toImmutableList__E = typing.TypeVar('_toImmutableList__E')  # <E>
    @staticmethod
    def toImmutableList() -> java.util.stream.Collector[_toImmutableList__E, typing.Any, 'ImmutableList'[_toImmutableList__E]]: ...
    class Builder(ImmutableCollection.Builder[_ImmutableList__Builder__E], typing.Generic[_ImmutableList__Builder__E]):
        def __init__(self): ...
        @typing.overload
        def add(self, e: _ImmutableList__Builder__E) -> 'ImmutableList.Builder'[_ImmutableList__Builder__E]: ...
        @typing.overload
        def add(self, eArray: typing.List[_ImmutableList__Builder__E]) -> 'ImmutableList.Builder'[_ImmutableList__Builder__E]: ...
        @typing.overload
        def addAll(self, iterable: java.lang.Iterable[_ImmutableList__Builder__E]) -> 'ImmutableList.Builder'[_ImmutableList__Builder__E]: ...
        @typing.overload
        def addAll(self, iterator: java.util.Iterator[_ImmutableList__Builder__E]) -> 'ImmutableList.Builder'[_ImmutableList__Builder__E]: ...
        def build(self) -> 'ImmutableList'[_ImmutableList__Builder__E]: ...

_ImmutableRangeMap__Builder__K = typing.TypeVar('_ImmutableRangeMap__Builder__K', bound=java.lang.Comparable)  # <K>
_ImmutableRangeMap__Builder__V = typing.TypeVar('_ImmutableRangeMap__Builder__V')  # <V>
_ImmutableRangeMap__K = typing.TypeVar('_ImmutableRangeMap__K', bound=java.lang.Comparable)  # <K>
_ImmutableRangeMap__V = typing.TypeVar('_ImmutableRangeMap__V')  # <V>
class ImmutableRangeMap(RangeMap[_ImmutableRangeMap__K, _ImmutableRangeMap__V], java.io.Serializable, typing.Generic[_ImmutableRangeMap__K, _ImmutableRangeMap__V]):
    """
    :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtIncompatible` public class :meth:`~src`<K extends Comparable<?>,V> extends Object implements :class:`~com.google.common.collect.RangeMap`<K,V>, Serializable
    
        A :class:`~com.google.common.collect.RangeMap` whose contents will never change, with many other important properties
        detailed at :class:`~com.google.common.collect.ImmutableCollection`.
    
        Since:
            14.0
    
        Also see:
            :meth:`~serialized`
    """
    def asDescendingMapOfRanges(self) -> ImmutableMap['Range'[_ImmutableRangeMap__K], _ImmutableRangeMap__V]: ...
    def asMapOfRanges(self) -> ImmutableMap['Range'[_ImmutableRangeMap__K], _ImmutableRangeMap__V]: ...
    _builder__K = typing.TypeVar('_builder__K', bound=java.lang.Comparable)  # <K>
    _builder__V = typing.TypeVar('_builder__V')  # <V>
    @staticmethod
    def builder() -> 'ImmutableRangeMap.Builder'[_builder__K, _builder__V]: ...
    def clear(self) -> None: ...
    _copyOf__K = typing.TypeVar('_copyOf__K', bound=java.lang.Comparable)  # <K>
    _copyOf__V = typing.TypeVar('_copyOf__V')  # <V>
    @staticmethod
    def copyOf(rangeMap: RangeMap[_copyOf__K, _copyOf__V]) -> 'ImmutableRangeMap'[_copyOf__K, _copyOf__V]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, k: _ImmutableRangeMap__K) -> _ImmutableRangeMap__V: ...
    def getEntry(self, k: _ImmutableRangeMap__K) -> java.util.Map.Entry['Range'[_ImmutableRangeMap__K], _ImmutableRangeMap__V]: ...
    def hashCode(self) -> int: ...
    def merge(self, range: 'Range'[_ImmutableRangeMap__K], v: _ImmutableRangeMap__V, biFunction: typing.Union[java.util.function.BiFunction[_ImmutableRangeMap__V, _ImmutableRangeMap__V, _ImmutableRangeMap__V], typing.Callable[[_ImmutableRangeMap__V, _ImmutableRangeMap__V], _ImmutableRangeMap__V]]) -> None: ...
    _of_0__K = typing.TypeVar('_of_0__K', bound=java.lang.Comparable)  # <K>
    _of_0__V = typing.TypeVar('_of_0__V')  # <V>
    _of_1__K = typing.TypeVar('_of_1__K', bound=java.lang.Comparable)  # <K>
    _of_1__V = typing.TypeVar('_of_1__V')  # <V>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableRangeMap'[_of_0__K, _of_0__V]: ...
    @typing.overload
    @staticmethod
    def of(range: 'Range'[_of_1__K], v: _of_1__V) -> 'ImmutableRangeMap'[_of_1__K, _of_1__V]: ...
    def put(self, range: 'Range'[_ImmutableRangeMap__K], v: _ImmutableRangeMap__V) -> None: ...
    def putAll(self, rangeMap: RangeMap[_ImmutableRangeMap__K, _ImmutableRangeMap__V]) -> None: ...
    def putCoalescing(self, range: 'Range'[_ImmutableRangeMap__K], v: _ImmutableRangeMap__V) -> None: ...
    def remove(self, range: 'Range'[_ImmutableRangeMap__K]) -> None: ...
    def span(self) -> 'Range'[_ImmutableRangeMap__K]: ...
    def subRangeMap(self, range: 'Range'[_ImmutableRangeMap__K]) -> 'ImmutableRangeMap'[_ImmutableRangeMap__K, _ImmutableRangeMap__V]: ...
    _toImmutableRangeMap__T = typing.TypeVar('_toImmutableRangeMap__T')  # <T>
    _toImmutableRangeMap__K = typing.TypeVar('_toImmutableRangeMap__K', bound=java.lang.Comparable)  # <K>
    _toImmutableRangeMap__V = typing.TypeVar('_toImmutableRangeMap__V')  # <V>
    @staticmethod
    def toImmutableRangeMap(function: typing.Union[java.util.function.Function[_toImmutableRangeMap__T, 'Range'[_toImmutableRangeMap__K]], typing.Callable[[_toImmutableRangeMap__T], 'Range'[_toImmutableRangeMap__K]]], function2: typing.Union[java.util.function.Function[_toImmutableRangeMap__T, _toImmutableRangeMap__V], typing.Callable[[_toImmutableRangeMap__T], _toImmutableRangeMap__V]]) -> java.util.stream.Collector[_toImmutableRangeMap__T, typing.Any, 'ImmutableRangeMap'[_toImmutableRangeMap__K, _toImmutableRangeMap__V]]: ...
    def toString(self) -> str: ...
    class Builder(typing.Generic[_ImmutableRangeMap__Builder__K, _ImmutableRangeMap__Builder__V]):
        def __init__(self): ...
        def build(self) -> 'ImmutableRangeMap'[_ImmutableRangeMap__Builder__K, _ImmutableRangeMap__Builder__V]: ...
        def put(self, range: 'Range'[_ImmutableRangeMap__Builder__K], v: _ImmutableRangeMap__Builder__V) -> 'ImmutableRangeMap.Builder'[_ImmutableRangeMap__Builder__K, _ImmutableRangeMap__Builder__V]: ...
        def putAll(self, rangeMap: RangeMap[_ImmutableRangeMap__Builder__K, _ImmutableRangeMap__Builder__V]) -> 'ImmutableRangeMap.Builder'[_ImmutableRangeMap__Builder__K, _ImmutableRangeMap__Builder__V]: ...

_ImmutableSet__Builder__E = typing.TypeVar('_ImmutableSet__Builder__E')  # <E>
_ImmutableSet__E = typing.TypeVar('_ImmutableSet__E')  # <E>
class ImmutableSet(ImmutableCollection[_ImmutableSet__E], java.util.Set[_ImmutableSet__E], typing.Generic[_ImmutableSet__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ImmutableCollection`<E> implements Set<E>
    
        A null whose contents will never change, with many other important properties detailed at
        :class:`~com.google.common.collect.ImmutableCollection`.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def asList(self) -> ImmutableList[_ImmutableSet__E]: ...
    _builder__E = typing.TypeVar('_builder__E')  # <E>
    @staticmethod
    def builder() -> 'ImmutableSet.Builder'[_builder__E]: ...
    _builderWithExpectedSize__E = typing.TypeVar('_builderWithExpectedSize__E')  # <E>
    @staticmethod
    def builderWithExpectedSize(int: int) -> 'ImmutableSet.Builder'[_builderWithExpectedSize__E]: ...
    _copyOf_0__E = typing.TypeVar('_copyOf_0__E')  # <E>
    _copyOf_1__E = typing.TypeVar('_copyOf_1__E')  # <E>
    _copyOf_2__E = typing.TypeVar('_copyOf_2__E')  # <E>
    _copyOf_3__E = typing.TypeVar('_copyOf_3__E')  # <E>
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[_copyOf_0__E]) -> 'ImmutableSet'[_copyOf_0__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(eArray: typing.List[_copyOf_1__E]) -> 'ImmutableSet'[_copyOf_1__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(collection: typing.Union[java.util.Collection[_copyOf_2__E], typing.Sequence[_copyOf_2__E]]) -> 'ImmutableSet'[_copyOf_2__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterator: java.util.Iterator[_copyOf_3__E]) -> 'ImmutableSet'[_copyOf_3__E]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def iterator(self) -> UnmodifiableIterator[_ImmutableSet__E]: ...
    _of_0__E = typing.TypeVar('_of_0__E')  # <E>
    _of_1__E = typing.TypeVar('_of_1__E')  # <E>
    _of_2__E = typing.TypeVar('_of_2__E')  # <E>
    _of_3__E = typing.TypeVar('_of_3__E')  # <E>
    _of_4__E = typing.TypeVar('_of_4__E')  # <E>
    _of_5__E = typing.TypeVar('_of_5__E')  # <E>
    _of_6__E = typing.TypeVar('_of_6__E')  # <E>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableSet'[_of_0__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_1__E) -> 'ImmutableSet'[_of_1__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_2__E, e2: _of_2__E) -> 'ImmutableSet'[_of_2__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_3__E, e2: _of_3__E, e3: _of_3__E) -> 'ImmutableSet'[_of_3__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_4__E, e2: _of_4__E, e3: _of_4__E, e4: _of_4__E) -> 'ImmutableSet'[_of_4__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_5__E, e2: _of_5__E, e3: _of_5__E, e4: _of_5__E, e5: _of_5__E) -> 'ImmutableSet'[_of_5__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_6__E, e2: _of_6__E, e3: _of_6__E, e4: _of_6__E, e5: _of_6__E, e6: _of_6__E, eArray: typing.List[_of_6__E]) -> 'ImmutableSet'[_of_6__E]: ...
    _toImmutableSet__E = typing.TypeVar('_toImmutableSet__E')  # <E>
    @staticmethod
    def toImmutableSet() -> java.util.stream.Collector[_toImmutableSet__E, typing.Any, 'ImmutableSet'[_toImmutableSet__E]]: ...
    class Builder(ImmutableCollection.Builder[_ImmutableSet__Builder__E], typing.Generic[_ImmutableSet__Builder__E]):
        def __init__(self): ...
        @typing.overload
        def add(self, e: _ImmutableSet__Builder__E) -> 'ImmutableSet.Builder'[_ImmutableSet__Builder__E]: ...
        @typing.overload
        def add(self, eArray: typing.List[_ImmutableSet__Builder__E]) -> 'ImmutableSet.Builder'[_ImmutableSet__Builder__E]: ...
        @typing.overload
        def addAll(self, iterable: java.lang.Iterable[_ImmutableSet__Builder__E]) -> 'ImmutableSet.Builder'[_ImmutableSet__Builder__E]: ...
        @typing.overload
        def addAll(self, iterator: java.util.Iterator[_ImmutableSet__Builder__E]) -> 'ImmutableSet.Builder'[_ImmutableSet__Builder__E]: ...
        def build(self) -> 'ImmutableSet'[_ImmutableSet__Builder__E]: ...

_ListMultimap__K = typing.TypeVar('_ListMultimap__K')  # <K>
_ListMultimap__V = typing.TypeVar('_ListMultimap__V')  # <V>
class ListMultimap(Multimap[_ListMultimap__K, _ListMultimap__V], typing.Generic[_ListMultimap__K, _ListMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<K,V> extends :class:`~com.google.common.collect.Multimap`<K,V>
    
        A :code:`Multimap` that can hold duplicate key-value pairs and that maintains the insertion ordering of values for a
        given key. See the :class:`~com.google.common.collect.Multimap` documentation for information common to all multimaps.
    
        The :meth:`~com.google.common.collect.ListMultimap.get`, :meth:`~com.google.common.collect.ListMultimap.removeAll`, and
        :meth:`~com.google.common.collect.ListMultimap.replaceValues` methods each return a null of values. Though the method
        signature doesn't say so explicitly, the map returned by :meth:`~com.google.common.collect.ListMultimap.asMap` has
        :code:`List` values.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    def asMap(self) -> java.util.Map[_ListMultimap__K, java.util.Collection[_ListMultimap__V]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, k: _ListMultimap__K) -> java.util.List[_ListMultimap__V]: ...
    def hashCode(self) -> int: ...
    def removeAll(self, object: typing.Any) -> java.util.List[_ListMultimap__V]: ...
    def replaceValues(self, k: _ListMultimap__K, iterable: java.lang.Iterable[_ListMultimap__V]) -> java.util.List[_ListMultimap__V]: ...

_RowSortedTable__R = typing.TypeVar('_RowSortedTable__R')  # <R>
_RowSortedTable__C = typing.TypeVar('_RowSortedTable__C')  # <C>
_RowSortedTable__V = typing.TypeVar('_RowSortedTable__V')  # <V>
class RowSortedTable(Table[_RowSortedTable__R, _RowSortedTable__C, _RowSortedTable__V], typing.Generic[_RowSortedTable__R, _RowSortedTable__C, _RowSortedTable__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<R,C,V> extends :class:`~com.google.common.collect.Table`<R,C,V>
    
        Interface that extends :code:`Table` and whose rows are sorted.
    
        The :meth:`~com.google.common.collect.RowSortedTable.rowKeySet` method returns a null and the
        :meth:`~com.google.common.collect.RowSortedTable.rowMap` method returns a null, instead of the null and null specified
        by the :class:`~com.google.common.collect.Table` interface.
    
        Since:
            8.0
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def rowKeySet(self) -> java.util.SortedSet[_RowSortedTable__R]: ...
    def rowMap(self) -> java.util.SortedMap[_RowSortedTable__R, java.util.Map[_RowSortedTable__C, _RowSortedTable__V]]: ...

_SetMultimap__K = typing.TypeVar('_SetMultimap__K')  # <K>
_SetMultimap__V = typing.TypeVar('_SetMultimap__V')  # <V>
class SetMultimap(Multimap[_SetMultimap__K, _SetMultimap__V], typing.Generic[_SetMultimap__K, _SetMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<K,V> extends :class:`~com.google.common.collect.Multimap`<K,V>
    
        A :code:`Multimap` that cannot hold duplicate key-value pairs. Adding a key-value pair that's already in the multimap
        has no effect. See the :class:`~com.google.common.collect.Multimap` documentation for information common to all
        multimaps.
    
        The :meth:`~com.google.common.collect.SetMultimap.get`, :meth:`~com.google.common.collect.SetMultimap.removeAll`, and
        :meth:`~com.google.common.collect.SetMultimap.replaceValues` methods each return a null of values, while
        :meth:`~com.google.common.collect.SetMultimap.entries` returns a :code:`Set` of map entries. Though the method signature
        doesn't say so explicitly, the map returned by :meth:`~com.google.common.collect.SetMultimap.asMap` has :code:`Set`
        values.
    
        If the values corresponding to a single key should be ordered according to a null (or the natural order), see the
        :class:`~com.google.common.collect.SortedSetMultimap` subinterface.
    
        Since the value collections are sets, the behavior of a :code:`SetMultimap` is not specified if key *or value* objects
        already present in the multimap change in a manner that affects :code:`equals` comparisons. Use caution if mutable
        objects are used as keys or values in a :code:`SetMultimap`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    def asMap(self) -> java.util.Map[_SetMultimap__K, java.util.Collection[_SetMultimap__V]]: ...
    def entries(self) -> java.util.Set[java.util.Map.Entry[_SetMultimap__K, _SetMultimap__V]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, k: _SetMultimap__K) -> java.util.Set[_SetMultimap__V]: ...
    def hashCode(self) -> int: ...
    def removeAll(self, object: typing.Any) -> java.util.Set[_SetMultimap__V]: ...
    def replaceValues(self, k: _SetMultimap__K, iterable: java.lang.Iterable[_SetMultimap__V]) -> java.util.Set[_SetMultimap__V]: ...

_SortedMapDifference__K = typing.TypeVar('_SortedMapDifference__K')  # <K>
_SortedMapDifference__V = typing.TypeVar('_SortedMapDifference__V')  # <V>
class SortedMapDifference(MapDifference[_SortedMapDifference__K, _SortedMapDifference__V], typing.Generic[_SortedMapDifference__K, _SortedMapDifference__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<K,V> extends :class:`~com.google.common.collect.MapDifference`<K,V>
    
        An object representing the differences between two sorted maps.
    
        Since:
            8.0
    """
    def entriesDiffering(self) -> java.util.SortedMap[_SortedMapDifference__K, MapDifference.ValueDifference[_SortedMapDifference__V]]: ...
    def entriesInCommon(self) -> java.util.SortedMap[_SortedMapDifference__K, _SortedMapDifference__V]: ...
    def entriesOnlyOnLeft(self) -> java.util.SortedMap[_SortedMapDifference__K, _SortedMapDifference__V]: ...
    def entriesOnlyOnRight(self) -> java.util.SortedMap[_SortedMapDifference__K, _SortedMapDifference__V]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...

_TreeRangeMap__K = typing.TypeVar('_TreeRangeMap__K', bound=java.lang.Comparable)  # <K>
_TreeRangeMap__V = typing.TypeVar('_TreeRangeMap__V')  # <V>
class TreeRangeMap(RangeMap[_TreeRangeMap__K, _TreeRangeMap__V], typing.Generic[_TreeRangeMap__K, _TreeRangeMap__V]):
    """
    :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtIncompatible` public final class :meth:`~src`<K extends Comparable,V> extends Object implements :class:`~com.google.common.collect.RangeMap`<K,V>
    
        An implementation of :code:`RangeMap` based on a :code:`TreeMap`, supporting all optional operations.
    
        Like all :code:`RangeMap` implementations, this supports neither null keys nor null values.
    
        Since:
            14.0
    """
    def asDescendingMapOfRanges(self) -> java.util.Map['Range'[_TreeRangeMap__K], _TreeRangeMap__V]: ...
    def asMapOfRanges(self) -> java.util.Map['Range'[_TreeRangeMap__K], _TreeRangeMap__V]: ...
    def clear(self) -> None: ...
    _create__K = typing.TypeVar('_create__K', bound=java.lang.Comparable)  # <K>
    _create__V = typing.TypeVar('_create__V')  # <V>
    @staticmethod
    def create() -> 'TreeRangeMap'[_create__K, _create__V]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, k: _TreeRangeMap__K) -> _TreeRangeMap__V: ...
    def getEntry(self, k: _TreeRangeMap__K) -> java.util.Map.Entry['Range'[_TreeRangeMap__K], _TreeRangeMap__V]: ...
    def hashCode(self) -> int: ...
    def merge(self, range: 'Range'[_TreeRangeMap__K], v: _TreeRangeMap__V, biFunction: typing.Union[java.util.function.BiFunction[_TreeRangeMap__V, _TreeRangeMap__V, _TreeRangeMap__V], typing.Callable[[_TreeRangeMap__V, _TreeRangeMap__V], _TreeRangeMap__V]]) -> None: ...
    def put(self, range: 'Range'[_TreeRangeMap__K], v: _TreeRangeMap__V) -> None: ...
    def putAll(self, rangeMap: RangeMap[_TreeRangeMap__K, _TreeRangeMap__V]) -> None: ...
    def putCoalescing(self, range: 'Range'[_TreeRangeMap__K], v: _TreeRangeMap__V) -> None: ...
    def remove(self, range: 'Range'[_TreeRangeMap__K]) -> None: ...
    def span(self) -> 'Range'[_TreeRangeMap__K]: ...
    def subRangeMap(self, range: 'Range'[_TreeRangeMap__K]) -> RangeMap[_TreeRangeMap__K, _TreeRangeMap__V]: ...
    def toString(self) -> str: ...

_UnmodifiableListIterator__E = typing.TypeVar('_UnmodifiableListIterator__E')  # <E>
class UnmodifiableListIterator(UnmodifiableIterator[_UnmodifiableListIterator__E], java.util.ListIterator[_UnmodifiableListIterator__E], typing.Generic[_UnmodifiableListIterator__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.UnmodifiableIterator`<E> implements ListIterator<E>
    
        A list iterator that does not support :meth:`~com.google.common.collect.UnmodifiableIterator.remove`,
        :meth:`~com.google.common.collect.UnmodifiableListIterator.add`, or
        :meth:`~com.google.common.collect.UnmodifiableListIterator.set`.
    
        Since:
            7.0
    """
    def add(self, e: _UnmodifiableListIterator__E) -> None: ...
    def set(self, e: _UnmodifiableListIterator__E) -> None: ...

_ForwardingConcurrentMap__K = typing.TypeVar('_ForwardingConcurrentMap__K')  # <K>
_ForwardingConcurrentMap__V = typing.TypeVar('_ForwardingConcurrentMap__V')  # <V>
class ForwardingConcurrentMap(ForwardingMap[_ForwardingConcurrentMap__K, _ForwardingConcurrentMap__V], java.util.concurrent.ConcurrentMap[_ForwardingConcurrentMap__K, _ForwardingConcurrentMap__V], typing.Generic[_ForwardingConcurrentMap__K, _ForwardingConcurrentMap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ForwardingMap`<K,V> implements ConcurrentMap<K,V>
    
        A concurrent map which forwards all its method calls to another concurrent map. Subclasses should override one or more
        methods to modify the behavior of the backing map as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **:code:`default` method warning:** This class forwards calls to *only some* :code:`default` methods. Specifically, it
        forwards calls only for methods that existed null. For newer methods, like :code:`forEach`, it inherits their default
        implementations. When those implementations invoke methods, they invoke methods on the :code:`ForwardingConcurrentMap`.
    
        Since:
            2.0
    """
    def putIfAbsent(self, k: _ForwardingConcurrentMap__K, v: _ForwardingConcurrentMap__V) -> _ForwardingConcurrentMap__V: ...
    @typing.overload
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any) -> _ForwardingConcurrentMap__V: ...
    @typing.overload
    def replace(self, k: _ForwardingConcurrentMap__K, v: _ForwardingConcurrentMap__V, v2: _ForwardingConcurrentMap__V) -> bool: ...
    @typing.overload
    def replace(self, k: _ForwardingConcurrentMap__K, v: _ForwardingConcurrentMap__V) -> _ForwardingConcurrentMap__V: ...

_ForwardingList__E = typing.TypeVar('_ForwardingList__E')  # <E>
class ForwardingList(ForwardingCollection[_ForwardingList__E], java.util.List[_ForwardingList__E], typing.Generic[_ForwardingList__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingCollection`<E> implements List<E>
    
        A list which forwards all its method calls to another list. Subclasses should override one or more methods to modify the
        behavior of the backing list as desired per the `decorator pattern <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        This class does not implement null. If the delegate supports random access, the :code:`ForwardingList` subclass should
        implement the :code:`RandomAccess` interface.
    
        **Warning:** The methods of :code:`ForwardingList` forward **indiscriminately** to the methods of the delegate. For
        example, overriding :meth:`~com.google.common.collect.ForwardingList.add` alone **will not** change the behavior of
        :meth:`~com.google.common.collect.ForwardingList.addAll`, which can lead to unexpected behavior. In this case, you
        should override :code:`addAll` as well, either providing your own implementation, or delegating to the provided
        :code:`standardAddAll` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingList`.
    
        The :code:`standard` methods and any collection views they return are not guaranteed to be thread-safe, even when all of
        the methods that they depend on are thread-safe.
    
        Since:
            2.0
    """
    @typing.overload
    def add(self, e: _ForwardingList__E) -> bool: ...
    @typing.overload
    def add(self, int: int, e: _ForwardingList__E) -> None: ...
    @typing.overload
    def addAll(self, collection: typing.Union[java.util.Collection[_ForwardingList__E], typing.Sequence[_ForwardingList__E]]) -> bool: ...
    @typing.overload
    def addAll(self, int: int, collection: typing.Union[java.util.Collection[_ForwardingList__E], typing.Sequence[_ForwardingList__E]]) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, int: int) -> _ForwardingList__E: ...
    def hashCode(self) -> int: ...
    def indexOf(self, object: typing.Any) -> int: ...
    def lastIndexOf(self, object: typing.Any) -> int: ...
    @typing.overload
    def listIterator(self) -> java.util.ListIterator[_ForwardingList__E]: ...
    @typing.overload
    def listIterator(self, int: int) -> java.util.ListIterator[_ForwardingList__E]: ...
    def set(self, int: int, e: _ForwardingList__E) -> _ForwardingList__E: ...
    def subList(self, int: int, int2: int) -> java.util.List[_ForwardingList__E]: ...

_ForwardingListIterator__E = typing.TypeVar('_ForwardingListIterator__E')  # <E>
class ForwardingListIterator(ForwardingIterator[_ForwardingListIterator__E], java.util.ListIterator[_ForwardingListIterator__E], typing.Generic[_ForwardingListIterator__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingIterator`<E> implements ListIterator<E>
    
        A list iterator which forwards all its method calls to another list iterator. Subclasses should override one or more
        methods to modify the behavior of the backing iterator as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **:code:`default` method warning:** This class forwards calls to *only some* :code:`default` methods. Specifically, it
        forwards calls only for methods that existed null. For newer methods, like :code:`forEachRemaining`, it inherits their
        default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingListIterator`.
    
        Since:
            2.0
    """
    def add(self, e: _ForwardingListIterator__E) -> None: ...
    def hasPrevious(self) -> bool: ...
    def nextIndex(self) -> int: ...
    def previous(self) -> _ForwardingListIterator__E: ...
    def previousIndex(self) -> int: ...
    def set(self, e: _ForwardingListIterator__E) -> None: ...

_ForwardingListMultimap__K = typing.TypeVar('_ForwardingListMultimap__K')  # <K>
_ForwardingListMultimap__V = typing.TypeVar('_ForwardingListMultimap__V')  # <V>
class ForwardingListMultimap(ForwardingMultimap[_ForwardingListMultimap__K, _ForwardingListMultimap__V], ListMultimap[_ForwardingListMultimap__K, _ForwardingListMultimap__V], typing.Generic[_ForwardingListMultimap__K, _ForwardingListMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ForwardingMultimap`<K,V> implements :class:`~com.google.common.collect.ListMultimap`<K,V>
    
        A list multimap which forwards all its method calls to another list multimap. Subclasses should override one or more
        methods to modify the behavior of the backing multimap as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingListMultimap`.
    
        Since:
            3.0
    """
    def get(self, k: _ForwardingListMultimap__K) -> java.util.List[_ForwardingListMultimap__V]: ...
    def removeAll(self, object: typing.Any) -> java.util.List[_ForwardingListMultimap__V]: ...
    def replaceValues(self, k: _ForwardingListMultimap__K, iterable: java.lang.Iterable[_ForwardingListMultimap__V]) -> java.util.List[_ForwardingListMultimap__V]: ...

_ForwardingMultiset__E = typing.TypeVar('_ForwardingMultiset__E')  # <E>
class ForwardingMultiset(ForwardingCollection[_ForwardingMultiset__E], Multiset[_ForwardingMultiset__E], typing.Generic[_ForwardingMultiset__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingCollection`<E> implements :class:`~com.google.common.collect.Multiset`<E>
    
        A multiset which forwards all its method calls to another multiset. Subclasses should override one or more methods to
        modify the behavior of the backing multiset as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingMultiset` forward **indiscriminately** to the methods of the delegate. For
        example, overriding :meth:`~com.google.common.collect.ForwardingMultiset.add` alone **will not** change the behavior of
        :meth:`~com.google.common.collect.ForwardingCollection.add`, which can lead to unexpected behavior. In this case, you
        should override :code:`add(Object)` as well, either providing your own implementation, or delegating to the provided
        :code:`standardAdd` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingMultiset`.
    
        The :code:`standard` methods and any collection views they return are not guaranteed to be thread-safe, even when all of
        the methods that they depend on are thread-safe.
    
        Since:
            2.0
    """
    @typing.overload
    def add(self, e: _ForwardingMultiset__E) -> bool: ...
    @typing.overload
    def add(self, e: _ForwardingMultiset__E, int: int) -> int: ...
    def count(self, object: typing.Any) -> int: ...
    def elementSet(self) -> java.util.Set[_ForwardingMultiset__E]: ...
    def entrySet(self) -> java.util.Set[Multiset.Entry[_ForwardingMultiset__E]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    @typing.overload
    def remove(self, object: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any, int: int) -> int: ...
    @typing.overload
    def setCount(self, e: _ForwardingMultiset__E, int: int, int2: int) -> bool: ...
    @typing.overload
    def setCount(self, e: _ForwardingMultiset__E, int: int) -> int: ...

_ForwardingQueue__E = typing.TypeVar('_ForwardingQueue__E')  # <E>
class ForwardingQueue(ForwardingCollection[_ForwardingQueue__E], java.util.Queue[_ForwardingQueue__E], typing.Generic[_ForwardingQueue__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingCollection`<E> implements Queue<E>
    
        A queue which forwards all its method calls to another queue. Subclasses should override one or more methods to modify
        the behavior of the backing queue as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingQueue` forward **indiscriminately** to the methods of the delegate. For
        example, overriding :meth:`~com.google.common.collect.ForwardingCollection.add` alone **will not** change the behavior
        of :meth:`~com.google.common.collect.ForwardingQueue.offer` which can lead to unexpected behavior. In this case, you
        should override :code:`offer` as well, either providing your own implementation, or delegating to the provided
        :code:`standardOffer` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingQueue`.
    
        The :code:`standard` methods are not guaranteed to be thread-safe, even when all of the methods that they depend on are
        thread-safe.
    
        Since:
            2.0
    """
    def element(self) -> _ForwardingQueue__E: ...
    def offer(self, e: _ForwardingQueue__E) -> bool: ...
    def peek(self) -> _ForwardingQueue__E: ...
    def poll(self) -> _ForwardingQueue__E: ...
    @typing.overload
    def remove(self, object: typing.Any) -> bool: ...
    @typing.overload
    def remove(self) -> _ForwardingQueue__E: ...

_ForwardingSet__E = typing.TypeVar('_ForwardingSet__E')  # <E>
class ForwardingSet(ForwardingCollection[_ForwardingSet__E], java.util.Set[_ForwardingSet__E], typing.Generic[_ForwardingSet__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingCollection`<E> implements Set<E>
    
        A set which forwards all its method calls to another set. Subclasses should override one or more methods to modify the
        behavior of the backing set as desired per the `decorator pattern <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingSet` forward **indiscriminately** to the methods of the delegate. For
        example, overriding :meth:`~com.google.common.collect.ForwardingCollection.add` alone **will not** change the behavior
        of :meth:`~com.google.common.collect.ForwardingCollection.addAll`, which can lead to unexpected behavior. In this case,
        you should override :code:`addAll` as well, either providing your own implementation, or delegating to the provided
        :code:`standardAddAll` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingSet`.
    
        The :code:`standard` methods are not guaranteed to be thread-safe, even when all of the methods that they depend on are
        thread-safe.
    
        Since:
            2.0
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...

_ForwardingSetMultimap__K = typing.TypeVar('_ForwardingSetMultimap__K')  # <K>
_ForwardingSetMultimap__V = typing.TypeVar('_ForwardingSetMultimap__V')  # <V>
class ForwardingSetMultimap(ForwardingMultimap[_ForwardingSetMultimap__K, _ForwardingSetMultimap__V], SetMultimap[_ForwardingSetMultimap__K, _ForwardingSetMultimap__V], typing.Generic[_ForwardingSetMultimap__K, _ForwardingSetMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ForwardingMultimap`<K,V> implements :class:`~com.google.common.collect.SetMultimap`<K,V>
    
        A set multimap which forwards all its method calls to another set multimap. Subclasses should override one or more
        methods to modify the behavior of the backing multimap as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingSetMultimap`.
    
        Since:
            3.0
    """
    def __init__(self): ...
    def entries(self) -> java.util.Set[java.util.Map.Entry[_ForwardingSetMultimap__K, _ForwardingSetMultimap__V]]: ...
    def get(self, k: _ForwardingSetMultimap__K) -> java.util.Set[_ForwardingSetMultimap__V]: ...
    def removeAll(self, object: typing.Any) -> java.util.Set[_ForwardingSetMultimap__V]: ...
    def replaceValues(self, k: _ForwardingSetMultimap__K, iterable: java.lang.Iterable[_ForwardingSetMultimap__V]) -> java.util.Set[_ForwardingSetMultimap__V]: ...

_ForwardingSortedMap__K = typing.TypeVar('_ForwardingSortedMap__K')  # <K>
_ForwardingSortedMap__V = typing.TypeVar('_ForwardingSortedMap__V')  # <V>
class ForwardingSortedMap(ForwardingMap[_ForwardingSortedMap__K, _ForwardingSortedMap__V], java.util.SortedMap[_ForwardingSortedMap__K, _ForwardingSortedMap__V], typing.Generic[_ForwardingSortedMap__K, _ForwardingSortedMap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ForwardingMap`<K,V> implements SortedMap<K,V>
    
        A sorted map which forwards all its method calls to another sorted map. Subclasses should override one or more methods
        to modify the behavior of the backing sorted map as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingSortedMap` forward *indiscriminately* to the methods of the delegate. For
        example, overriding :meth:`~com.google.common.collect.ForwardingMap.put` alone *will not* change the behavior of
        :meth:`~com.google.common.collect.ForwardingMap.putAll`, which can lead to unexpected behavior. In this case, you should
        override :code:`putAll` as well, either providing your own implementation, or delegating to the provided
        :code:`standardPutAll` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingSortedMap`.
    
        Each of the :code:`standard` methods, where appropriate, use the comparator of the map to test equality for both keys
        and values, unlike :code:`ForwardingMap`.
    
        The :code:`standard` methods and the collection views they return are not guaranteed to be thread-safe, even when all of
        the methods that they depend on are thread-safe.
    
        Since:
            2.0
    """
    def comparator(self) -> java.util.Comparator[_ForwardingSortedMap__K]: ...
    def firstKey(self) -> _ForwardingSortedMap__K: ...
    def headMap(self, k: _ForwardingSortedMap__K) -> java.util.SortedMap[_ForwardingSortedMap__K, _ForwardingSortedMap__V]: ...
    def lastKey(self) -> _ForwardingSortedMap__K: ...
    def subMap(self, k: _ForwardingSortedMap__K, k2: _ForwardingSortedMap__K) -> java.util.SortedMap[_ForwardingSortedMap__K, _ForwardingSortedMap__V]: ...
    def tailMap(self, k: _ForwardingSortedMap__K) -> java.util.SortedMap[_ForwardingSortedMap__K, _ForwardingSortedMap__V]: ...

_ImmutableClassToInstanceMap__Builder__B = typing.TypeVar('_ImmutableClassToInstanceMap__Builder__B')  # <B>
_ImmutableClassToInstanceMap__B = typing.TypeVar('_ImmutableClassToInstanceMap__B')  # <B>
class ImmutableClassToInstanceMap(ForwardingMap[typing.Type[_ImmutableClassToInstanceMap__B], _ImmutableClassToInstanceMap__B], ClassToInstanceMap[_ImmutableClassToInstanceMap__B], java.io.Serializable, typing.Generic[_ImmutableClassToInstanceMap__B]):
    """
    @Immutable(containerOf="B") :class:`~com.google.common.annotations.GwtIncompatible` public final class :meth:`~src`<B> extends :class:`~com.google.common.collect.ForwardingMap`<Class<? extends B>,B> implements :class:`~com.google.common.collect.ClassToInstanceMap`<B>, Serializable
    
        A :class:`~com.google.common.collect.ClassToInstanceMap` whose contents will never change, with many other important
        properties detailed at :class:`~com.google.common.collect.ImmutableCollection`.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    _builder__B = typing.TypeVar('_builder__B')  # <B>
    @staticmethod
    def builder() -> 'ImmutableClassToInstanceMap.Builder'[_builder__B]: ...
    _copyOf__B = typing.TypeVar('_copyOf__B')  # <B>
    _copyOf__S = typing.TypeVar('_copyOf__S')  # <S>
    @staticmethod
    def copyOf(map: typing.Union[java.util.Map[typing.Type[_copyOf__S], _copyOf__S], typing.Mapping[typing.Type[_copyOf__S], _copyOf__S]]) -> 'ImmutableClassToInstanceMap'[_copyOf__B]: ...
    _getInstance__T = typing.TypeVar('_getInstance__T')  # <T>
    def getInstance(self, class_: typing.Type[_getInstance__T]) -> _getInstance__T: ...
    _of_0__B = typing.TypeVar('_of_0__B')  # <B>
    _of_1__B = typing.TypeVar('_of_1__B')  # <B>
    _of_1__T = typing.TypeVar('_of_1__T')  # <T>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableClassToInstanceMap'[_of_0__B]: ...
    @typing.overload
    @staticmethod
    def of(class_: typing.Type[_of_1__T], t: _of_1__T) -> 'ImmutableClassToInstanceMap'[_of_1__B]: ...
    _putInstance__T = typing.TypeVar('_putInstance__T')  # <T>
    def putInstance(self, class_: typing.Type[_putInstance__T], t: _putInstance__T) -> _putInstance__T: ...
    class Builder(typing.Generic[_ImmutableClassToInstanceMap__Builder__B]):
        def __init__(self): ...
        def build(self) -> 'ImmutableClassToInstanceMap'[_ImmutableClassToInstanceMap__Builder__B]: ...
        _put__T = typing.TypeVar('_put__T')  # <T>
        def put(self, class_: typing.Type[_put__T], t: _put__T) -> 'ImmutableClassToInstanceMap.Builder'[_ImmutableClassToInstanceMap__Builder__B]: ...
        _putAll__T = typing.TypeVar('_putAll__T')  # <T>
        def putAll(self, map: typing.Union[java.util.Map[typing.Type[_putAll__T], _putAll__T], typing.Mapping[typing.Type[_putAll__T], _putAll__T]]) -> 'ImmutableClassToInstanceMap.Builder'[_ImmutableClassToInstanceMap__Builder__B]: ...

_MutableClassToInstanceMap__B = typing.TypeVar('_MutableClassToInstanceMap__B')  # <B>
class MutableClassToInstanceMap(ForwardingMap[typing.Type[_MutableClassToInstanceMap__B], _MutableClassToInstanceMap__B], ClassToInstanceMap[_MutableClassToInstanceMap__B], java.io.Serializable, typing.Generic[_MutableClassToInstanceMap__B]):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public final class :meth:`~src`<B> extends :class:`~com.google.common.collect.ForwardingMap`<Class<? extends B>,B> implements :class:`~com.google.common.collect.ClassToInstanceMap`<B>, Serializable
    
        A mutable class-to-instance map backed by an arbitrary user-provided map. See also
        :class:`~com.google.common.collect.ImmutableClassToInstanceMap`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    _create_0__B = typing.TypeVar('_create_0__B')  # <B>
    _create_1__B = typing.TypeVar('_create_1__B')  # <B>
    @typing.overload
    @staticmethod
    def create() -> 'MutableClassToInstanceMap'[_create_0__B]: ...
    @typing.overload
    @staticmethod
    def create(map: typing.Union[java.util.Map[typing.Type[_create_1__B], _create_1__B], typing.Mapping[typing.Type[_create_1__B], _create_1__B]]) -> 'MutableClassToInstanceMap'[_create_1__B]: ...
    def entrySet(self) -> java.util.Set[java.util.Map.Entry[typing.Type[_MutableClassToInstanceMap__B], _MutableClassToInstanceMap__B]]: ...
    _getInstance__T = typing.TypeVar('_getInstance__T')  # <T>
    def getInstance(self, class_: typing.Type[_getInstance__T]) -> _getInstance__T: ...
    def put(self, class_: typing.Type[_MutableClassToInstanceMap__B], b: _MutableClassToInstanceMap__B) -> _MutableClassToInstanceMap__B: ...
    def putAll(self, map: typing.Union[java.util.Map[typing.Type[_MutableClassToInstanceMap__B], _MutableClassToInstanceMap__B], typing.Mapping[typing.Type[_MutableClassToInstanceMap__B], _MutableClassToInstanceMap__B]]) -> None: ...
    _putInstance__T = typing.TypeVar('_putInstance__T')  # <T>
    def putInstance(self, class_: typing.Type[_putInstance__T], t: _putInstance__T) -> _putInstance__T: ...

_SortedSetMultimap__K = typing.TypeVar('_SortedSetMultimap__K')  # <K>
_SortedSetMultimap__V = typing.TypeVar('_SortedSetMultimap__V')  # <V>
class SortedSetMultimap(SetMultimap[_SortedSetMultimap__K, _SortedSetMultimap__V], typing.Generic[_SortedSetMultimap__K, _SortedSetMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<K,V> extends :class:`~com.google.common.collect.SetMultimap`<K,V>
    
        A :code:`SetMultimap` whose set of values for a given key are kept sorted; that is, they comprise a null. It cannot hold
        duplicate key-value pairs; adding a key-value pair that's already in the multimap has no effect. This interface does not
        specify the ordering of the multimap's keys. See the :class:`~com.google.common.collect.Multimap` documentation for
        information common to all multimaps.
    
        The :meth:`~com.google.common.collect.SortedSetMultimap.get`,
        :meth:`~com.google.common.collect.SortedSetMultimap.removeAll`, and
        :meth:`~com.google.common.collect.SortedSetMultimap.replaceValues` methods each return a null of values, while
        :meth:`~com.google.common.collect.Multimap.entries` returns a null of map entries. Though the method signature doesn't
        say so explicitly, the map returned by :meth:`~com.google.common.collect.SortedSetMultimap.asMap` has :code:`SortedSet`
        values.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    def asMap(self) -> java.util.Map[_SortedSetMultimap__K, java.util.Collection[_SortedSetMultimap__V]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, k: _SortedSetMultimap__K) -> java.util.SortedSet[_SortedSetMultimap__V]: ...
    def hashCode(self) -> int: ...
    def removeAll(self, object: typing.Any) -> java.util.SortedSet[_SortedSetMultimap__V]: ...
    def replaceValues(self, k: _SortedSetMultimap__K, iterable: java.lang.Iterable[_SortedSetMultimap__V]) -> java.util.SortedSet[_SortedSetMultimap__V]: ...
    def valueComparator(self) -> java.util.Comparator[_SortedSetMultimap__V]: ...

_EvictingQueue__E = typing.TypeVar('_EvictingQueue__E')  # <E>
class EvictingQueue(ForwardingQueue[_EvictingQueue__E], java.io.Serializable, typing.Generic[_EvictingQueue__E]):
    """
    :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingQueue`<E> implements Serializable
    
        A non-blocking queue which automatically evicts elements from the head of the queue when attempting to add new elements
        onto the queue and it is full. This queue orders elements FIFO (first-in-first-out). This data structure is logically
        equivalent to a circular buffer (i.e., cyclic buffer or ring buffer).
    
        An evicting queue must be configured with a maximum size. Each time an element is added to a full queue, the queue
        automatically removes its head element. This is different from conventional bounded queues, which either block or reject
        new elements when full.
    
        This class is not thread-safe, and does not accept null elements.
    
        Since:
            15.0
    
        Also see:
            :meth:`~serialized`
    """
    def add(self, e: _EvictingQueue__E) -> bool: ...
    def addAll(self, collection: typing.Union[java.util.Collection[_EvictingQueue__E], typing.Sequence[_EvictingQueue__E]]) -> bool: ...
    def contains(self, object: typing.Any) -> bool: ...
    _create__E = typing.TypeVar('_create__E')  # <E>
    @staticmethod
    def create(int: int) -> 'EvictingQueue'[_create__E]: ...
    def offer(self, e: _EvictingQueue__E) -> bool: ...
    def remainingCapacity(self) -> int: ...
    @typing.overload
    def remove(self, object: typing.Any) -> bool: ...
    @typing.overload
    def remove(self) -> _EvictingQueue__E: ...

_ForwardingDeque__E = typing.TypeVar('_ForwardingDeque__E')  # <E>
class ForwardingDeque(ForwardingQueue[_ForwardingDeque__E], java.util.Deque[_ForwardingDeque__E], typing.Generic[_ForwardingDeque__E]):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingQueue`<E> implements Deque<E>
    
        A deque which forwards all its method calls to another deque. Subclasses should override one or more methods to modify
        the behavior of the backing deque as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingDeque` forward **indiscriminately** to the methods of the delegate. For
        example, overriding :meth:`~com.google.common.collect.ForwardingCollection.add` alone **will not** change the behavior
        of :meth:`~com.google.common.collect.ForwardingQueue.offer` which can lead to unexpected behavior. In this case, you
        should override :code:`offer` as well.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingDeque`.
    
        Since:
            12.0
    """
    def addFirst(self, e: _ForwardingDeque__E) -> None: ...
    def addLast(self, e: _ForwardingDeque__E) -> None: ...
    def descendingIterator(self) -> java.util.Iterator[_ForwardingDeque__E]: ...
    def getFirst(self) -> _ForwardingDeque__E: ...
    def getLast(self) -> _ForwardingDeque__E: ...
    def offerFirst(self, e: _ForwardingDeque__E) -> bool: ...
    def offerLast(self, e: _ForwardingDeque__E) -> bool: ...
    def peekFirst(self) -> _ForwardingDeque__E: ...
    def peekLast(self) -> _ForwardingDeque__E: ...
    def pollFirst(self) -> _ForwardingDeque__E: ...
    def pollLast(self) -> _ForwardingDeque__E: ...
    def pop(self) -> _ForwardingDeque__E: ...
    def push(self, e: _ForwardingDeque__E) -> None: ...
    def removeFirst(self) -> _ForwardingDeque__E: ...
    def removeFirstOccurrence(self, object: typing.Any) -> bool: ...
    def removeLast(self) -> _ForwardingDeque__E: ...
    def removeLastOccurrence(self, object: typing.Any) -> bool: ...

_ForwardingNavigableMap__K = typing.TypeVar('_ForwardingNavigableMap__K')  # <K>
_ForwardingNavigableMap__V = typing.TypeVar('_ForwardingNavigableMap__V')  # <V>
class ForwardingNavigableMap(ForwardingSortedMap[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V], java.util.NavigableMap[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V], typing.Generic[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public abstract class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ForwardingSortedMap`<K,V> implements NavigableMap<K,V>
    
        A navigable map which forwards all its method calls to another navigable map. Subclasses should override one or more
        methods to modify the behavior of the backing map as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingNavigableMap` forward *indiscriminately* to the methods of the delegate.
        For example, overriding :meth:`~com.google.common.collect.ForwardingMap.put` alone *will not* change the behavior of
        :meth:`~com.google.common.collect.ForwardingMap.putAll`, which can lead to unexpected behavior. In this case, you should
        override :code:`putAll` as well, either providing your own implementation, or delegating to the provided
        :code:`standardPutAll` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingNavigableMap`.
    
        Each of the :code:`standard` methods uses the map's comparator (or the natural ordering of the elements, if there is no
        comparator) to test element equality. As a result, if the comparator is not consistent with equals, some of the standard
        implementations may violate the :code:`Map` contract.
    
        The :code:`standard` methods and the collection views they return are not guaranteed to be thread-safe, even when all of
        the methods that they depend on are thread-safe.
    
        Since:
            12.0
    """
    def ceilingEntry(self, k: _ForwardingNavigableMap__K) -> java.util.Map.Entry[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    def ceilingKey(self, k: _ForwardingNavigableMap__K) -> _ForwardingNavigableMap__K: ...
    def descendingKeySet(self) -> java.util.NavigableSet[_ForwardingNavigableMap__K]: ...
    def descendingMap(self) -> java.util.NavigableMap[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    def firstEntry(self) -> java.util.Map.Entry[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    def floorEntry(self, k: _ForwardingNavigableMap__K) -> java.util.Map.Entry[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    def floorKey(self, k: _ForwardingNavigableMap__K) -> _ForwardingNavigableMap__K: ...
    @typing.overload
    def headMap(self, k: _ForwardingNavigableMap__K, boolean: bool) -> java.util.NavigableMap[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    @typing.overload
    def headMap(self, k: _ForwardingNavigableMap__K) -> java.util.SortedMap[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    def higherEntry(self, k: _ForwardingNavigableMap__K) -> java.util.Map.Entry[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    def higherKey(self, k: _ForwardingNavigableMap__K) -> _ForwardingNavigableMap__K: ...
    def lastEntry(self) -> java.util.Map.Entry[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    def lowerEntry(self, k: _ForwardingNavigableMap__K) -> java.util.Map.Entry[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    def lowerKey(self, k: _ForwardingNavigableMap__K) -> _ForwardingNavigableMap__K: ...
    def navigableKeySet(self) -> java.util.NavigableSet[_ForwardingNavigableMap__K]: ...
    def pollFirstEntry(self) -> java.util.Map.Entry[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    def pollLastEntry(self) -> java.util.Map.Entry[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    @typing.overload
    def subMap(self, k: _ForwardingNavigableMap__K, boolean: bool, k2: _ForwardingNavigableMap__K, boolean2: bool) -> java.util.NavigableMap[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    @typing.overload
    def subMap(self, k: _ForwardingNavigableMap__K, k2: _ForwardingNavigableMap__K) -> java.util.SortedMap[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    @typing.overload
    def tailMap(self, k: _ForwardingNavigableMap__K, boolean: bool) -> java.util.NavigableMap[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...
    @typing.overload
    def tailMap(self, k: _ForwardingNavigableMap__K) -> java.util.SortedMap[_ForwardingNavigableMap__K, _ForwardingNavigableMap__V]: ...

_ForwardingSortedSet__E = typing.TypeVar('_ForwardingSortedSet__E')  # <E>
class ForwardingSortedSet(ForwardingSet[_ForwardingSortedSet__E], java.util.SortedSet[_ForwardingSortedSet__E], typing.Generic[_ForwardingSortedSet__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingSet`<E> implements SortedSet<E>
    
        A sorted set which forwards all its method calls to another sorted set. Subclasses should override one or more methods
        to modify the behavior of the backing sorted set as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingSortedSet` forward *indiscriminately* to the methods of the delegate. For
        example, overriding :meth:`~com.google.common.collect.ForwardingCollection.add` alone *will not* change the behavior of
        :meth:`~com.google.common.collect.ForwardingCollection.addAll`, which can lead to unexpected behavior. In this case, you
        should override :code:`addAll` as well, either providing your own implementation, or delegating to the provided
        :code:`standardAddAll` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingSortedSet`.
    
        Each of the :code:`standard` methods, where appropriate, uses the set's comparator (or the natural ordering of the
        elements, if there is no comparator) to test element equality. As a result, if the comparator is not consistent with
        equals, some of the standard implementations may violate the :code:`Set` contract.
    
        The :code:`standard` methods and the collection views they return are not guaranteed to be thread-safe, even when all of
        the methods that they depend on are thread-safe.
    
        Since:
            2.0
    """
    def comparator(self) -> java.util.Comparator[_ForwardingSortedSet__E]: ...
    def first(self) -> _ForwardingSortedSet__E: ...
    def headSet(self, e: _ForwardingSortedSet__E) -> java.util.SortedSet[_ForwardingSortedSet__E]: ...
    def last(self) -> _ForwardingSortedSet__E: ...
    def subSet(self, e: _ForwardingSortedSet__E, e2: _ForwardingSortedSet__E) -> java.util.SortedSet[_ForwardingSortedSet__E]: ...
    def tailSet(self, e: _ForwardingSortedSet__E) -> java.util.SortedSet[_ForwardingSortedSet__E]: ...

_ForwardingSortedSetMultimap__K = typing.TypeVar('_ForwardingSortedSetMultimap__K')  # <K>
_ForwardingSortedSetMultimap__V = typing.TypeVar('_ForwardingSortedSetMultimap__V')  # <V>
class ForwardingSortedSetMultimap(ForwardingSetMultimap[_ForwardingSortedSetMultimap__K, _ForwardingSortedSetMultimap__V], SortedSetMultimap[_ForwardingSortedSetMultimap__K, _ForwardingSortedSetMultimap__V], typing.Generic[_ForwardingSortedSetMultimap__K, _ForwardingSortedSetMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ForwardingSetMultimap`<K,V> implements :class:`~com.google.common.collect.SortedSetMultimap`<K,V>
    
        A sorted set multimap which forwards all its method calls to another sorted set multimap. Subclasses should override one
        or more methods to modify the behavior of the backing multimap as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingSortedSetMultimap`.
    
        Since:
            3.0
    """
    def get(self, k: _ForwardingSortedSetMultimap__K) -> java.util.SortedSet[_ForwardingSortedSetMultimap__V]: ...
    def removeAll(self, object: typing.Any) -> java.util.SortedSet[_ForwardingSortedSetMultimap__V]: ...
    def replaceValues(self, k: _ForwardingSortedSetMultimap__K, iterable: java.lang.Iterable[_ForwardingSortedSetMultimap__V]) -> java.util.SortedSet[_ForwardingSortedSetMultimap__V]: ...
    def valueComparator(self) -> java.util.Comparator[_ForwardingSortedSetMultimap__V]: ...

_ForwardingBlockingDeque__E = typing.TypeVar('_ForwardingBlockingDeque__E')  # <E>
class ForwardingBlockingDeque(ForwardingDeque[_ForwardingBlockingDeque__E], java.util.concurrent.BlockingDeque[_ForwardingBlockingDeque__E], typing.Generic[_ForwardingBlockingDeque__E]):
    """
    Deprecated. 
    This class has moved to :code:`com.google.common.util.concurrent`. Please use
    :class:`~com.google.common.util.concurrent.ForwardingBlockingDeque` instead.
    @Deprecated :class:`~com.google.common.annotations.GwtIncompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingDeque`<E> implements BlockingDeque<E>
    
        A null which forwards all its method calls to another :code:`BlockingDeque`. Subclasses should override one or more
        methods to modify the behavior of the backing deque as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingBlockingDeque` forward **indiscriminately** to the methods of the delegate.
        For example, overriding :meth:`~com.google.common.collect.ForwardingCollection.add` alone **will not** change the
        behaviour of :meth:`~com.google.common.collect.ForwardingBlockingDeque.offer` which can lead to unexpected behaviour. In
        this case, you should override :code:`offer` as well, either providing your own implementation, or delegating to the
        provided :code:`standardOffer` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingBlockingDeque`.
    
        The :code:`standard` methods are not guaranteed to be thread-safe, even when all of the methods that they depend on are
        thread-safe.
    
        Since:
            14.0
    """
    @typing.overload
    def drainTo(self, collection: typing.Union[java.util.Collection[_ForwardingBlockingDeque__E], typing.Sequence[_ForwardingBlockingDeque__E]]) -> int: ...
    @typing.overload
    def drainTo(self, collection: typing.Union[java.util.Collection[_ForwardingBlockingDeque__E], typing.Sequence[_ForwardingBlockingDeque__E]], int: int) -> int: ...
    @typing.overload
    def offer(self, e: _ForwardingBlockingDeque__E, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
    @typing.overload
    def offer(self, e: _ForwardingBlockingDeque__E) -> bool: ...
    @typing.overload
    def offerFirst(self, e: _ForwardingBlockingDeque__E, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
    @typing.overload
    def offerFirst(self, e: _ForwardingBlockingDeque__E) -> bool: ...
    @typing.overload
    def offerLast(self, e: _ForwardingBlockingDeque__E, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
    @typing.overload
    def offerLast(self, e: _ForwardingBlockingDeque__E) -> bool: ...
    @typing.overload
    def poll(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> _ForwardingBlockingDeque__E: ...
    @typing.overload
    def poll(self) -> _ForwardingBlockingDeque__E: ...
    @typing.overload
    def pollFirst(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> _ForwardingBlockingDeque__E: ...
    @typing.overload
    def pollFirst(self) -> _ForwardingBlockingDeque__E: ...
    @typing.overload
    def pollLast(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> _ForwardingBlockingDeque__E: ...
    @typing.overload
    def pollLast(self) -> _ForwardingBlockingDeque__E: ...
    def put(self, e: _ForwardingBlockingDeque__E) -> None: ...
    def putFirst(self, e: _ForwardingBlockingDeque__E) -> None: ...
    def putLast(self, e: _ForwardingBlockingDeque__E) -> None: ...
    def remainingCapacity(self) -> int: ...
    def take(self) -> _ForwardingBlockingDeque__E: ...
    def takeFirst(self) -> _ForwardingBlockingDeque__E: ...
    def takeLast(self) -> _ForwardingBlockingDeque__E: ...

_ForwardingNavigableSet__E = typing.TypeVar('_ForwardingNavigableSet__E')  # <E>
class ForwardingNavigableSet(ForwardingSortedSet[_ForwardingNavigableSet__E], java.util.NavigableSet[_ForwardingNavigableSet__E], typing.Generic[_ForwardingNavigableSet__E]):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingSortedSet`<E> implements NavigableSet<E>
    
        A navigable set which forwards all its method calls to another navigable set. Subclasses should override one or more
        methods to modify the behavior of the backing set as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingNavigableSet` forward *indiscriminately* to the methods of the delegate.
        For example, overriding :meth:`~com.google.common.collect.ForwardingCollection.add` alone *will not* change the behavior
        of :meth:`~com.google.common.collect.ForwardingCollection.addAll`, which can lead to unexpected behavior. In this case,
        you should override :code:`addAll` as well, either providing your own implementation, or delegating to the provided
        :code:`standardAddAll` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingNavigableSet`.
    
        Each of the :code:`standard` methods uses the set's comparator (or the natural ordering of the elements, if there is no
        comparator) to test element equality. As a result, if the comparator is not consistent with equals, some of the standard
        implementations may violate the :code:`Set` contract.
    
        The :code:`standard` methods and the collection views they return are not guaranteed to be thread-safe, even when all of
        the methods that they depend on are thread-safe.
    
        Since:
            12.0
    """
    def ceiling(self, e: _ForwardingNavigableSet__E) -> _ForwardingNavigableSet__E: ...
    def descendingIterator(self) -> java.util.Iterator[_ForwardingNavigableSet__E]: ...
    def descendingSet(self) -> java.util.NavigableSet[_ForwardingNavigableSet__E]: ...
    def floor(self, e: _ForwardingNavigableSet__E) -> _ForwardingNavigableSet__E: ...
    @typing.overload
    def headSet(self, e: _ForwardingNavigableSet__E, boolean: bool) -> java.util.NavigableSet[_ForwardingNavigableSet__E]: ...
    @typing.overload
    def headSet(self, e: _ForwardingNavigableSet__E) -> java.util.SortedSet[_ForwardingNavigableSet__E]: ...
    def higher(self, e: _ForwardingNavigableSet__E) -> _ForwardingNavigableSet__E: ...
    def lower(self, e: _ForwardingNavigableSet__E) -> _ForwardingNavigableSet__E: ...
    def pollFirst(self) -> _ForwardingNavigableSet__E: ...
    def pollLast(self) -> _ForwardingNavigableSet__E: ...
    @typing.overload
    def subSet(self, e: _ForwardingNavigableSet__E, boolean: bool, e2: _ForwardingNavigableSet__E, boolean2: bool) -> java.util.NavigableSet[_ForwardingNavigableSet__E]: ...
    @typing.overload
    def subSet(self, e: _ForwardingNavigableSet__E, e2: _ForwardingNavigableSet__E) -> java.util.SortedSet[_ForwardingNavigableSet__E]: ...
    @typing.overload
    def tailSet(self, e: _ForwardingNavigableSet__E, boolean: bool) -> java.util.NavigableSet[_ForwardingNavigableSet__E]: ...
    @typing.overload
    def tailSet(self, e: _ForwardingNavigableSet__E) -> java.util.SortedSet[_ForwardingNavigableSet__E]: ...

_ArrayListMultimap__K = typing.TypeVar('_ArrayListMultimap__K')  # <K>
_ArrayListMultimap__V = typing.TypeVar('_ArrayListMultimap__V')  # <V>
class ArrayListMultimap(com.google.common.collect.ArrayListMultimapGwtSerializationDependencies[_ArrayListMultimap__K, _ArrayListMultimap__V], typing.Generic[_ArrayListMultimap__K, _ArrayListMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<K,V> extends Object
    
        Implementation of :code:`Multimap` that uses an :code:`ArrayList` to store the values for a given key. A null associates
        each key with an null of values.
    
        When iterating through the collections supplied by this class, the ordering of values for a given key agrees with the
        order in which the values were added.
    
        This multimap allows duplicate key-value pairs. After adding a new key-value pair equal to an existing key-value pair,
        the :code:`ArrayListMultimap` will contain entries for both the new value and the old value.
    
        Keys and values may be null. All optional multimap methods are supported, and all returned views are modifiable.
    
        The lists returned by :meth:`~com.google.common.collect.ArrayListMultimap.get`,
        :meth:`~com.google.common.collect.ArrayListMultimap.removeAll`, and
        :meth:`~com.google.common.collect.ArrayListMultimap.replaceValues` all implement null.
    
        This class is not threadsafe when any concurrent operations update the multimap. Concurrent read operations will work
        correctly. To allow concurrent update operations, wrap your multimap with a call to
        :meth:`~com.google.common.collect.Multimaps.synchronizedListMultimap`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    _create_0__K = typing.TypeVar('_create_0__K')  # <K>
    _create_0__V = typing.TypeVar('_create_0__V')  # <V>
    _create_1__K = typing.TypeVar('_create_1__K')  # <K>
    _create_1__V = typing.TypeVar('_create_1__V')  # <V>
    _create_2__K = typing.TypeVar('_create_2__K')  # <K>
    _create_2__V = typing.TypeVar('_create_2__V')  # <V>
    @typing.overload
    @staticmethod
    def create() -> 'ArrayListMultimap'[_create_0__K, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(multimap: Multimap[_create_1__K, _create_1__V]) -> 'ArrayListMultimap'[_create_1__K, _create_1__V]: ...
    @typing.overload
    @staticmethod
    def create(int: int, int2: int) -> 'ArrayListMultimap'[_create_2__K, _create_2__V]: ...
    def trimToSize(self) -> None: ...

_ArrayTable__R = typing.TypeVar('_ArrayTable__R')  # <R>
_ArrayTable__C = typing.TypeVar('_ArrayTable__C')  # <C>
_ArrayTable__V = typing.TypeVar('_ArrayTable__V')  # <V>
class ArrayTable(com.google.common.collect.AbstractTable[_ArrayTable__R, _ArrayTable__C, _ArrayTable__V], java.io.Serializable, typing.Generic[_ArrayTable__R, _ArrayTable__C, _ArrayTable__V]):
    """
    :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<R,C,V> extends Object implements Serializable
    
        Fixed-size :class:`~com.google.common.collect.Table` implementation backed by a two-dimensional array.
    
        The allowed row and column keys must be supplied when the table is created. The table always contains a mapping for
        every row key / column pair. The value corresponding to a given row and column is null unless another value is provided.
    
        The table's size is constant: the product of the number of supplied row keys and the number of supplied column keys. The
        :code:`remove` and :code:`clear` methods are not supported by the table or its views. The
        :meth:`~com.google.common.collect.ArrayTable.erase` and :meth:`~com.google.common.collect.ArrayTable.eraseAll` methods
        may be used instead.
    
        The ordering of the row and column keys provided when the table is constructed determines the iteration ordering across
        rows and columns in the table's views. None of the view iterators support null. If the table is modified after an
        iterator is created, the iterator remains valid.
    
        This class requires less memory than the :class:`~com.google.common.collect.HashBasedTable` and
        :class:`~com.google.common.collect.TreeBasedTable` implementations, except when the table is sparse.
    
        Null row keys or column keys are not permitted.
    
        This class provides methods involving the underlying array structure, where the array indices correspond to the position
        of a row or column in the lists of allowed keys and values. See the :meth:`~com.google.common.collect.ArrayTable.at`,
        :meth:`~com.google.common.collect.ArrayTable.set`, :meth:`~com.google.common.collect.ArrayTable.toArray`,
        :meth:`~com.google.common.collect.ArrayTable.rowKeyList`, and
        :meth:`~com.google.common.collect.ArrayTable.columnKeyList` methods for more details.
    
        Note that this implementation is not synchronized. If multiple threads access the same cell of an :code:`ArrayTable`
        concurrently and one of the threads modifies its value, there is no guarantee that the new value will be fully visible
        to the other threads. To guarantee that modifications are visible, synchronize access to the table. Unlike other
        :code:`Table` implementations, synchronization is unnecessary between a thread that writes to one cell and a thread that
        reads from another.
    
        See the Guava User Guide article on null.
    
        Since:
            10.0
    
        Also see:
            :meth:`~serialized`
    """
    def at(self, int: int, int2: int) -> _ArrayTable__V: ...
    def cellSet(self) -> java.util.Set[Table.Cell[_ArrayTable__R, _ArrayTable__C, _ArrayTable__V]]: ...
    def clear(self) -> None: ...
    def column(self, c: _ArrayTable__C) -> java.util.Map[_ArrayTable__R, _ArrayTable__V]: ...
    def columnKeyList(self) -> ImmutableList[_ArrayTable__C]: ...
    def columnKeySet(self) -> ImmutableSet[_ArrayTable__C]: ...
    def columnMap(self) -> java.util.Map[_ArrayTable__C, java.util.Map[_ArrayTable__R, _ArrayTable__V]]: ...
    def contains(self, object: typing.Any, object2: typing.Any) -> bool: ...
    def containsColumn(self, object: typing.Any) -> bool: ...
    def containsRow(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    _create_0__R = typing.TypeVar('_create_0__R')  # <R>
    _create_0__C = typing.TypeVar('_create_0__C')  # <C>
    _create_0__V = typing.TypeVar('_create_0__V')  # <V>
    _create_1__R = typing.TypeVar('_create_1__R')  # <R>
    _create_1__C = typing.TypeVar('_create_1__C')  # <C>
    _create_1__V = typing.TypeVar('_create_1__V')  # <V>
    @typing.overload
    @staticmethod
    def create(table: Table[_create_0__R, _create_0__C, _create_0__V]) -> 'ArrayTable'[_create_0__R, _create_0__C, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(iterable: java.lang.Iterable[_create_1__R], iterable2: java.lang.Iterable[_create_1__C]) -> 'ArrayTable'[_create_1__R, _create_1__C, _create_1__V]: ...
    def erase(self, object: typing.Any, object2: typing.Any) -> _ArrayTable__V: ...
    def eraseAll(self) -> None: ...
    def get(self, object: typing.Any, object2: typing.Any) -> _ArrayTable__V: ...
    def isEmpty(self) -> bool: ...
    def put(self, r: _ArrayTable__R, c: _ArrayTable__C, v: _ArrayTable__V) -> _ArrayTable__V: ...
    def putAll(self, table: Table[_ArrayTable__R, _ArrayTable__C, _ArrayTable__V]) -> None: ...
    def remove(self, object: typing.Any, object2: typing.Any) -> _ArrayTable__V: ...
    def row(self, r: _ArrayTable__R) -> java.util.Map[_ArrayTable__C, _ArrayTable__V]: ...
    def rowKeyList(self) -> ImmutableList[_ArrayTable__R]: ...
    def rowKeySet(self) -> ImmutableSet[_ArrayTable__R]: ...
    def rowMap(self) -> java.util.Map[_ArrayTable__R, java.util.Map[_ArrayTable__C, _ArrayTable__V]]: ...
    def set(self, int: int, int2: int, v: _ArrayTable__V) -> _ArrayTable__V: ...
    def size(self) -> int: ...
    def toArray(self, class_: typing.Type[_ArrayTable__V]) -> typing.List[typing.List[_ArrayTable__V]]: ...
    def values(self) -> java.util.Collection[_ArrayTable__V]: ...

_ConcurrentHashMultiset__E = typing.TypeVar('_ConcurrentHashMultiset__E')  # <E>
class ConcurrentHashMultiset(com.google.common.collect.AbstractMultiset[_ConcurrentHashMultiset__E], java.io.Serializable, typing.Generic[_ConcurrentHashMultiset__E]):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public final class :meth:`~src`<E> extends AbstractCollection<E> implements Serializable
    
        A multiset that supports concurrent modifications and that provides atomic versions of most :code:`Multiset` operations
        (exceptions where noted). Null elements are not supported.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def add(self, e: _ConcurrentHashMultiset__E) -> bool: ...
    @typing.overload
    def add(self, e: _ConcurrentHashMultiset__E, int: int) -> int: ...
    def clear(self) -> None: ...
    def count(self, object: typing.Any) -> int: ...
    _create_0__E = typing.TypeVar('_create_0__E')  # <E>
    _create_1__E = typing.TypeVar('_create_1__E')  # <E>
    _create_2__E = typing.TypeVar('_create_2__E')  # <E>
    @typing.overload
    @staticmethod
    def create() -> 'ConcurrentHashMultiset'[_create_0__E]: ...
    @typing.overload
    @staticmethod
    def create(iterable: java.lang.Iterable[_create_1__E]) -> 'ConcurrentHashMultiset'[_create_1__E]: ...
    @typing.overload
    @staticmethod
    def create(concurrentMap: java.util.concurrent.ConcurrentMap[_create_2__E, java.util.concurrent.atomic.AtomicInteger]) -> 'ConcurrentHashMultiset'[_create_2__E]: ...
    def createEntrySet(self) -> java.util.Set[Multiset.Entry[_ConcurrentHashMultiset__E]]: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> java.util.Iterator[_ConcurrentHashMultiset__E]: ...
    @typing.overload
    def remove(self, object: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any, int: int) -> int: ...
    def removeExactly(self, object: typing.Any, int: int) -> bool: ...
    @typing.overload
    def setCount(self, e: _ConcurrentHashMultiset__E, int: int, int2: int) -> bool: ...
    @typing.overload
    def setCount(self, e: _ConcurrentHashMultiset__E, int: int) -> int: ...
    def size(self) -> int: ...
    _toArray_0__T = typing.TypeVar('_toArray_0__T')  # <T>
    _toArray_2__T = typing.TypeVar('_toArray_2__T')  # <T>
    @typing.overload
    def toArray(self, intFunction: typing.Union[java.util.function.IntFunction[typing.List[_toArray_0__T]], typing.Callable[[int], typing.List[_toArray_0__T]]]) -> typing.List[_toArray_0__T]: ...
    @typing.overload
    def toArray(self) -> typing.List[typing.Any]: ...
    @typing.overload
    def toArray(self, tArray: typing.List[_toArray_2__T]) -> typing.List[_toArray_2__T]: ...

_ContiguousSet__C = typing.TypeVar('_ContiguousSet__C', bound=java.lang.Comparable)  # <C>
class ContiguousSet(com.google.common.collect.ImmutableSortedSet[_ContiguousSet__C], typing.Generic[_ContiguousSet__C]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<C extends Comparable> extends :class:`~com.google.common.collect.ImmutableSortedSet`<C>
    
        A sorted set of contiguous values in a given :class:`~com.google.common.collect.DiscreteDomain`. Example:
    
        .. code-block: java
        
         ContiguousSet.create(Range.closed(5, 42), DiscreteDomain.integers())
         
    
        Note that because bounded ranges over :code:`int` and :code:`long` values are so common, this particular example can be
        written as just:
    
        .. code-block: java
        
         ContiguousSet.closed(5, 42)
         
    
        **Warning:** Be extremely careful what you do with conceptually large instances (such as
        :code:`ContiguousSet.create(Range.greaterThan(0), DiscreteDomain.integers()`). Certain operations on such a set can be
        performed efficiently, but others (such as null or null) can cause major performance problems.
    
        Since:
            10.0
    
        Also see:
            :meth:`~serialized`
    """
    _builder_0__E = typing.TypeVar('_builder_0__E')  # <E>
    _builder_1__E = typing.TypeVar('_builder_1__E')  # <E>
    @typing.overload
    @staticmethod
    def builder() -> ImmutableSet.Builder[_builder_0__E]: ...
    @typing.overload
    @staticmethod
    def builder() -> 'ImmutableSortedSet.Builder'[_builder_1__E]: ...
    @typing.overload
    @staticmethod
    def closed(int: int, int2: int) -> 'ContiguousSet'[int]: ...
    @typing.overload
    @staticmethod
    def closed(long: int, long2: int) -> 'ContiguousSet'[int]: ...
    @typing.overload
    @staticmethod
    def closedOpen(int: int, int2: int) -> 'ContiguousSet'[int]: ...
    @typing.overload
    @staticmethod
    def closedOpen(long: int, long2: int) -> 'ContiguousSet'[int]: ...
    _create__C = typing.TypeVar('_create__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def create(range: 'Range'[_create__C], discreteDomain: DiscreteDomain[_create__C]) -> 'ContiguousSet'[_create__C]: ...
    @typing.overload
    def headSet(self, c: _ContiguousSet__C) -> 'ContiguousSet'[_ContiguousSet__C]: ...
    @typing.overload
    def headSet(self, c: _ContiguousSet__C, boolean: bool) -> 'ContiguousSet'[_ContiguousSet__C]: ...
    def intersection(self, contiguousSet: 'ContiguousSet'[_ContiguousSet__C]) -> 'ContiguousSet'[_ContiguousSet__C]: ...
    @typing.overload
    def range(self) -> 'Range'[_ContiguousSet__C]: ...
    @typing.overload
    def range(self, boundType: BoundType, boundType2: BoundType) -> 'Range'[_ContiguousSet__C]: ...
    @typing.overload
    def subSet(self, c: _ContiguousSet__C, boolean: bool, c2: _ContiguousSet__C, boolean2: bool) -> 'ContiguousSet'[_ContiguousSet__C]: ...
    @typing.overload
    def subSet(self, c: _ContiguousSet__C, c2: _ContiguousSet__C) -> 'ContiguousSet'[_ContiguousSet__C]: ...
    @typing.overload
    def tailSet(self, c: _ContiguousSet__C) -> 'ContiguousSet'[_ContiguousSet__C]: ...
    @typing.overload
    def tailSet(self, c: _ContiguousSet__C, boolean: bool) -> 'ContiguousSet'[_ContiguousSet__C]: ...
    def toString(self) -> str: ...

_EnumBiMap__K = typing.TypeVar('_EnumBiMap__K', bound=java.lang.Enum)  # <K>
_EnumBiMap__V = typing.TypeVar('_EnumBiMap__V', bound=java.lang.Enum)  # <V>
class EnumBiMap(com.google.common.collect.AbstractBiMap[_EnumBiMap__K, _EnumBiMap__V], typing.Generic[_EnumBiMap__K, _EnumBiMap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<K extends Enum<K>,V extends Enum<V>> extends :class:`~com.google.common.collect.ForwardingMap`<K,V>
    
        A :code:`BiMap` backed by two :code:`EnumMap` instances. Null keys and values are not permitted. An :code:`EnumBiMap`
        and its inverse are both serializable.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    _create_0__K = typing.TypeVar('_create_0__K', bound=java.lang.Enum)  # <K>
    _create_0__V = typing.TypeVar('_create_0__V', bound=java.lang.Enum)  # <V>
    _create_1__K = typing.TypeVar('_create_1__K', bound=java.lang.Enum)  # <K>
    _create_1__V = typing.TypeVar('_create_1__V', bound=java.lang.Enum)  # <V>
    @typing.overload
    @staticmethod
    def create(class_: typing.Type[_create_0__K], class2: typing.Type[_create_0__V]) -> 'EnumBiMap'[_create_0__K, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(map: typing.Union[java.util.Map[_create_1__K, _create_1__V], typing.Mapping[_create_1__K, _create_1__V]]) -> 'EnumBiMap'[_create_1__K, _create_1__V]: ...
    def keyType(self) -> typing.Type[_EnumBiMap__K]: ...
    def valueType(self) -> typing.Type[_EnumBiMap__V]: ...

_EnumHashBiMap__K = typing.TypeVar('_EnumHashBiMap__K', bound=java.lang.Enum)  # <K>
_EnumHashBiMap__V = typing.TypeVar('_EnumHashBiMap__V')  # <V>
class EnumHashBiMap(com.google.common.collect.AbstractBiMap[_EnumHashBiMap__K, _EnumHashBiMap__V], typing.Generic[_EnumHashBiMap__K, _EnumHashBiMap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<K extends Enum<K>,V> extends :class:`~com.google.common.collect.ForwardingMap`<K,V>
    
        A :code:`BiMap` backed by an :code:`EnumMap` instance for keys-to-values, and a :code:`HashMap` instance for
        values-to-keys. Null keys are not permitted, but null values are. An :code:`EnumHashBiMap` and its inverse are both
        serializable.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    _create_0__K = typing.TypeVar('_create_0__K', bound=java.lang.Enum)  # <K>
    _create_0__V = typing.TypeVar('_create_0__V')  # <V>
    _create_1__K = typing.TypeVar('_create_1__K', bound=java.lang.Enum)  # <K>
    _create_1__V = typing.TypeVar('_create_1__V')  # <V>
    @typing.overload
    @staticmethod
    def create(class_: typing.Type[_create_0__K]) -> 'EnumHashBiMap'[_create_0__K, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(map: typing.Union[java.util.Map[_create_1__K, _create_1__V], typing.Mapping[_create_1__K, _create_1__V]]) -> 'EnumHashBiMap'[_create_1__K, _create_1__V]: ...
    def forcePut(self, k: _EnumHashBiMap__K, v: _EnumHashBiMap__V) -> _EnumHashBiMap__V: ...
    def keyType(self) -> typing.Type[_EnumHashBiMap__K]: ...
    def put(self, k: _EnumHashBiMap__K, v: _EnumHashBiMap__V) -> _EnumHashBiMap__V: ...
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...

_EnumMultiset__E = typing.TypeVar('_EnumMultiset__E', bound=java.lang.Enum)  # <E>
class EnumMultiset(com.google.common.collect.AbstractMultiset[_EnumMultiset__E], java.io.Serializable, typing.Generic[_EnumMultiset__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<E extends Enum<E>> extends AbstractCollection<E> implements Serializable
    
        Multiset implementation specialized for enum elements, supporting all single-element operations in O(1).
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def add(self, e: _EnumMultiset__E) -> bool: ...
    @typing.overload
    def add(self, e: _EnumMultiset__E, int: int) -> int: ...
    def clear(self) -> None: ...
    def count(self, object: typing.Any) -> int: ...
    _create_0__E = typing.TypeVar('_create_0__E', bound=java.lang.Enum)  # <E>
    _create_1__E = typing.TypeVar('_create_1__E', bound=java.lang.Enum)  # <E>
    _create_2__E = typing.TypeVar('_create_2__E', bound=java.lang.Enum)  # <E>
    @typing.overload
    @staticmethod
    def create(class_: typing.Type[_create_0__E]) -> 'EnumMultiset'[_create_0__E]: ...
    @typing.overload
    @staticmethod
    def create(iterable: java.lang.Iterable[_create_1__E]) -> 'EnumMultiset'[_create_1__E]: ...
    @typing.overload
    @staticmethod
    def create(iterable: java.lang.Iterable[_create_2__E], class_: typing.Type[_create_2__E]) -> 'EnumMultiset'[_create_2__E]: ...
    def forEachEntry(self, objIntConsumer: typing.Union[java.util.function.ObjIntConsumer[_EnumMultiset__E], typing.Callable[[_EnumMultiset__E, int], None]]) -> None: ...
    def iterator(self) -> java.util.Iterator[_EnumMultiset__E]: ...
    @typing.overload
    def remove(self, object: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any, int: int) -> int: ...
    @typing.overload
    def setCount(self, e: _EnumMultiset__E, int: int, int2: int) -> bool: ...
    @typing.overload
    def setCount(self, e: _EnumMultiset__E, int: int) -> int: ...
    def size(self) -> int: ...

_ForwardingSortedMultiset__E = typing.TypeVar('_ForwardingSortedMultiset__E')  # <E>
class ForwardingSortedMultiset(ForwardingMultiset[_ForwardingSortedMultiset__E], com.google.common.collect.SortedMultiset[_ForwardingSortedMultiset__E], typing.Generic[_ForwardingSortedMultiset__E]):
    """
    :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ForwardingMultiset`<E> implements :class:`~com.google.common.collect.SortedMultiset`<E>
    
        A sorted multiset which forwards all its method calls to another sorted multiset. Subclasses should override one or more
        methods to modify the behavior of the backing multiset as desired per the `decorator pattern
        <http://en.wikipedia.org/wiki/Decorator_pattern>`.
    
        **Warning:** The methods of :code:`ForwardingSortedMultiset` forward **indiscriminately** to the methods of the
        delegate. For example, overriding :meth:`~com.google.common.collect.ForwardingMultiset.add` alone **will not** change
        the behavior of :meth:`~com.google.common.collect.ForwardingCollection.add`, which can lead to unexpected behavior. In
        this case, you should override :code:`add(Object)` as well, either providing your own implementation, or delegating to
        the provided :code:`standardAdd` method.
    
        **:code:`default` method warning:** This class does *not* forward calls to :code:`default` methods. Instead, it inherits
        their default implementations. When those implementations invoke methods, they invoke methods on the
        :code:`ForwardingSortedMultiset`.
    
        The :code:`standard` methods and any collection views they return are not guaranteed to be thread-safe, even when all of
        the methods that they depend on are thread-safe.
    
        Since:
            15.0
    """
    def comparator(self) -> java.util.Comparator[_ForwardingSortedMultiset__E]: ...
    def descendingMultiset(self) -> 'SortedMultiset'[_ForwardingSortedMultiset__E]: ...
    def elementSet(self) -> java.util.NavigableSet[_ForwardingSortedMultiset__E]: ...
    def firstEntry(self) -> Multiset.Entry[_ForwardingSortedMultiset__E]: ...
    def headMultiset(self, e: _ForwardingSortedMultiset__E, boundType: BoundType) -> 'SortedMultiset'[_ForwardingSortedMultiset__E]: ...
    def lastEntry(self) -> Multiset.Entry[_ForwardingSortedMultiset__E]: ...
    def pollFirstEntry(self) -> Multiset.Entry[_ForwardingSortedMultiset__E]: ...
    def pollLastEntry(self) -> Multiset.Entry[_ForwardingSortedMultiset__E]: ...
    def subMultiset(self, e: _ForwardingSortedMultiset__E, boundType: BoundType, e2: _ForwardingSortedMultiset__E, boundType2: BoundType) -> 'SortedMultiset'[_ForwardingSortedMultiset__E]: ...
    def tailMultiset(self, e: _ForwardingSortedMultiset__E, boundType: BoundType) -> 'SortedMultiset'[_ForwardingSortedMultiset__E]: ...

_HashBasedTable__R = typing.TypeVar('_HashBasedTable__R')  # <R>
_HashBasedTable__C = typing.TypeVar('_HashBasedTable__C')  # <C>
_HashBasedTable__V = typing.TypeVar('_HashBasedTable__V')  # <V>
class HashBasedTable(com.google.common.collect.StandardTable[_HashBasedTable__R, _HashBasedTable__C, _HashBasedTable__V], typing.Generic[_HashBasedTable__R, _HashBasedTable__C, _HashBasedTable__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true) public class :meth:`~src`<R,C,V> extends Object
    
        Implementation of :class:`~com.google.common.collect.Table` using linked hash tables. This guarantees predictable
        iteration order of the various views.
    
        The views returned by :meth:`~com.google.common.collect.HashBasedTable.column`,
        :meth:`~com.google.common.collect.HashBasedTable.columnKeySet`, and
        :meth:`~com.google.common.collect.HashBasedTable.columnMap` have iterators that don't support :code:`remove()`.
        Otherwise, all optional operations are supported. Null row keys, columns keys, and values are not supported.
    
        Lookups by row key are often faster than lookups by column key, because the data is stored in a :code:`Map<R, Map<C,
        V>>`. A method call like :code:`column(columnKey).get(rowKey)` still runs quickly, since the row key is provided.
        However, :code:`column(columnKey).size()` takes longer, since an iteration across all row keys occurs.
    
        Note that this implementation is not synchronized. If multiple threads access this table concurrently and one of the
        threads modifies the table, it must be synchronized externally.
    
        See the Guava User Guide article on null.
    
        Since:
            7.0
    
        Also see:
            :meth:`~serialized`
    """
    def contains(self, object: typing.Any, object2: typing.Any) -> bool: ...
    def containsColumn(self, object: typing.Any) -> bool: ...
    def containsRow(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    _create_0__R = typing.TypeVar('_create_0__R')  # <R>
    _create_0__C = typing.TypeVar('_create_0__C')  # <C>
    _create_0__V = typing.TypeVar('_create_0__V')  # <V>
    _create_1__R = typing.TypeVar('_create_1__R')  # <R>
    _create_1__C = typing.TypeVar('_create_1__C')  # <C>
    _create_1__V = typing.TypeVar('_create_1__V')  # <V>
    _create_2__R = typing.TypeVar('_create_2__R')  # <R>
    _create_2__C = typing.TypeVar('_create_2__C')  # <C>
    _create_2__V = typing.TypeVar('_create_2__V')  # <V>
    @typing.overload
    @staticmethod
    def create() -> 'HashBasedTable'[_create_0__R, _create_0__C, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(table: Table[_create_1__R, _create_1__C, _create_1__V]) -> 'HashBasedTable'[_create_1__R, _create_1__C, _create_1__V]: ...
    @typing.overload
    @staticmethod
    def create(int: int, int2: int) -> 'HashBasedTable'[_create_2__R, _create_2__C, _create_2__V]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, object: typing.Any, object2: typing.Any) -> _HashBasedTable__V: ...
    def remove(self, object: typing.Any, object2: typing.Any) -> _HashBasedTable__V: ...

_HashBiMap__K = typing.TypeVar('_HashBiMap__K')  # <K>
_HashBiMap__V = typing.TypeVar('_HashBiMap__V')  # <V>
class HashBiMap(com.google.common.collect.Maps.IteratorBasedAbstractMap[_HashBiMap__K, _HashBiMap__V], BiMap[_HashBiMap__K, _HashBiMap__V], java.io.Serializable, typing.Generic[_HashBiMap__K, _HashBiMap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<K,V> extends AbstractMap<K,V> implements :class:`~com.google.common.collect.BiMap`<K,V>, Serializable
    
        A :class:`~com.google.common.collect.BiMap` backed by two hash tables. This implementation allows null keys and values.
        A :code:`HashBiMap` and its inverse are both serializable.
    
        This implementation guarantees insertion-based iteration order of its keys.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def clear(self) -> None: ...
    def containsKey(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    _create_0__K = typing.TypeVar('_create_0__K')  # <K>
    _create_0__V = typing.TypeVar('_create_0__V')  # <V>
    _create_1__K = typing.TypeVar('_create_1__K')  # <K>
    _create_1__V = typing.TypeVar('_create_1__V')  # <V>
    _create_2__K = typing.TypeVar('_create_2__K')  # <K>
    _create_2__V = typing.TypeVar('_create_2__V')  # <V>
    @typing.overload
    @staticmethod
    def create() -> 'HashBiMap'[_create_0__K, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(int: int) -> 'HashBiMap'[_create_1__K, _create_1__V]: ...
    @typing.overload
    @staticmethod
    def create(map: typing.Union[java.util.Map[_create_2__K, _create_2__V], typing.Mapping[_create_2__K, _create_2__V]]) -> 'HashBiMap'[_create_2__K, _create_2__V]: ...
    def forEach(self, biConsumer: typing.Union[java.util.function.BiConsumer[_HashBiMap__K, _HashBiMap__V], typing.Callable[[_HashBiMap__K, _HashBiMap__V], None]]) -> None: ...
    def forcePut(self, k: _HashBiMap__K, v: _HashBiMap__V) -> _HashBiMap__V: ...
    def get(self, object: typing.Any) -> _HashBiMap__V: ...
    def inverse(self) -> BiMap[_HashBiMap__V, _HashBiMap__K]: ...
    def keySet(self) -> java.util.Set[_HashBiMap__K]: ...
    def put(self, k: _HashBiMap__K, v: _HashBiMap__V) -> _HashBiMap__V: ...
    @typing.overload
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any) -> _HashBiMap__V: ...
    def replaceAll(self, biFunction: typing.Union[java.util.function.BiFunction[_HashBiMap__K, _HashBiMap__V, _HashBiMap__V], typing.Callable[[_HashBiMap__K, _HashBiMap__V], _HashBiMap__V]]) -> None: ...
    def size(self) -> int: ...
    def values(self) -> java.util.Set[_HashBiMap__V]: ...

_HashMultimap__K = typing.TypeVar('_HashMultimap__K')  # <K>
_HashMultimap__V = typing.TypeVar('_HashMultimap__V')  # <V>
class HashMultimap(com.google.common.collect.HashMultimapGwtSerializationDependencies[_HashMultimap__K, _HashMultimap__V], typing.Generic[_HashMultimap__K, _HashMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<K,V> extends Object
    
        Implementation of :class:`~com.google.common.collect.Multimap` using hash tables.
    
        The multimap does not store duplicate key-value pairs. Adding a new key-value pair equal to an existing key-value pair
        has no effect.
    
        Keys and values may be null. All optional multimap methods are supported, and all returned views are modifiable.
    
        This class is not threadsafe when any concurrent operations update the multimap. Concurrent read operations will work
        correctly. To allow concurrent update operations, wrap your multimap with a call to
        :meth:`~com.google.common.collect.Multimaps.synchronizedSetMultimap`.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    _create_0__K = typing.TypeVar('_create_0__K')  # <K>
    _create_0__V = typing.TypeVar('_create_0__V')  # <V>
    _create_1__K = typing.TypeVar('_create_1__K')  # <K>
    _create_1__V = typing.TypeVar('_create_1__V')  # <V>
    _create_2__K = typing.TypeVar('_create_2__K')  # <K>
    _create_2__V = typing.TypeVar('_create_2__V')  # <V>
    @typing.overload
    @staticmethod
    def create() -> 'HashMultimap'[_create_0__K, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(multimap: Multimap[_create_1__K, _create_1__V]) -> 'HashMultimap'[_create_1__K, _create_1__V]: ...
    @typing.overload
    @staticmethod
    def create(int: int, int2: int) -> 'HashMultimap'[_create_2__K, _create_2__V]: ...

_HashMultiset__E = typing.TypeVar('_HashMultiset__E')  # <E>
class HashMultiset(com.google.common.collect.AbstractMapBasedMultiset[_HashMultiset__E], typing.Generic[_HashMultiset__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<E> extends AbstractCollection<E>
    
        Multiset implementation backed by a null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def add(self, e: _HashMultiset__E) -> bool: ...
    _create_0__E = typing.TypeVar('_create_0__E')  # <E>
    _create_1__E = typing.TypeVar('_create_1__E')  # <E>
    _create_2__E = typing.TypeVar('_create_2__E')  # <E>
    @typing.overload
    @staticmethod
    def create() -> 'HashMultiset'[_create_0__E]: ...
    @typing.overload
    @staticmethod
    def create(int: int) -> 'HashMultiset'[_create_1__E]: ...
    @typing.overload
    @staticmethod
    def create(iterable: java.lang.Iterable[_create_2__E]) -> 'HashMultiset'[_create_2__E]: ...
    def remove(self, object: typing.Any) -> bool: ...

_ImmutableBiMap__Builder__K = typing.TypeVar('_ImmutableBiMap__Builder__K')  # <K>
_ImmutableBiMap__Builder__V = typing.TypeVar('_ImmutableBiMap__Builder__V')  # <V>
_ImmutableBiMap__K = typing.TypeVar('_ImmutableBiMap__K')  # <K>
_ImmutableBiMap__V = typing.TypeVar('_ImmutableBiMap__V')  # <V>
class ImmutableBiMap(com.google.common.collect.ImmutableBiMapFauxverideShim[_ImmutableBiMap__K, _ImmutableBiMap__V], BiMap[_ImmutableBiMap__K, _ImmutableBiMap__V], typing.Generic[_ImmutableBiMap__K, _ImmutableBiMap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ImmutableMap`<K,V> implements :class:`~com.google.common.collect.BiMap`<K,V>
    
        A :class:`~com.google.common.collect.BiMap` whose contents will never change, with many other important properties
        detailed at :class:`~com.google.common.collect.ImmutableCollection`.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    _builder_0__K = typing.TypeVar('_builder_0__K')  # <K>
    _builder_0__V = typing.TypeVar('_builder_0__V')  # <V>
    _builder_1__K = typing.TypeVar('_builder_1__K')  # <K>
    _builder_1__V = typing.TypeVar('_builder_1__V')  # <V>
    @typing.overload
    @staticmethod
    def builder() -> 'ImmutableBiMap.Builder'[_builder_0__K, _builder_0__V]: ...
    @typing.overload
    @staticmethod
    def builder() -> ImmutableMap.Builder[_builder_1__K, _builder_1__V]: ...
    _builderWithExpectedSize_0__K = typing.TypeVar('_builderWithExpectedSize_0__K')  # <K>
    _builderWithExpectedSize_0__V = typing.TypeVar('_builderWithExpectedSize_0__V')  # <V>
    _builderWithExpectedSize_1__K = typing.TypeVar('_builderWithExpectedSize_1__K')  # <K>
    _builderWithExpectedSize_1__V = typing.TypeVar('_builderWithExpectedSize_1__V')  # <V>
    @typing.overload
    @staticmethod
    def builderWithExpectedSize(int: int) -> 'ImmutableBiMap.Builder'[_builderWithExpectedSize_0__K, _builderWithExpectedSize_0__V]: ...
    @typing.overload
    @staticmethod
    def builderWithExpectedSize(int: int) -> ImmutableMap.Builder[_builderWithExpectedSize_1__K, _builderWithExpectedSize_1__V]: ...
    _copyOf_0__K = typing.TypeVar('_copyOf_0__K')  # <K>
    _copyOf_0__V = typing.TypeVar('_copyOf_0__V')  # <V>
    _copyOf_1__K = typing.TypeVar('_copyOf_1__K')  # <K>
    _copyOf_1__V = typing.TypeVar('_copyOf_1__V')  # <V>
    _copyOf_2__K = typing.TypeVar('_copyOf_2__K')  # <K>
    _copyOf_2__V = typing.TypeVar('_copyOf_2__V')  # <V>
    _copyOf_3__K = typing.TypeVar('_copyOf_3__K')  # <K>
    _copyOf_3__V = typing.TypeVar('_copyOf_3__V')  # <V>
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_0__K, _copyOf_0__V]]) -> 'ImmutableBiMap'[_copyOf_0__K, _copyOf_0__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(map: typing.Union[java.util.Map[_copyOf_1__K, _copyOf_1__V], typing.Mapping[_copyOf_1__K, _copyOf_1__V]]) -> 'ImmutableBiMap'[_copyOf_1__K, _copyOf_1__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_2__K, _copyOf_2__V]]) -> ImmutableMap[_copyOf_2__K, _copyOf_2__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(map: typing.Union[java.util.Map[_copyOf_3__K, _copyOf_3__V], typing.Mapping[_copyOf_3__K, _copyOf_3__V]]) -> ImmutableMap[_copyOf_3__K, _copyOf_3__V]: ...
    def forcePut(self, k: _ImmutableBiMap__K, v: _ImmutableBiMap__V) -> _ImmutableBiMap__V: ...
    def inverse(self) -> 'ImmutableBiMap'[_ImmutableBiMap__V, _ImmutableBiMap__K]: ...
    _of_0__K = typing.TypeVar('_of_0__K')  # <K>
    _of_0__V = typing.TypeVar('_of_0__V')  # <V>
    _of_1__K = typing.TypeVar('_of_1__K')  # <K>
    _of_1__V = typing.TypeVar('_of_1__V')  # <V>
    _of_2__K = typing.TypeVar('_of_2__K')  # <K>
    _of_2__V = typing.TypeVar('_of_2__V')  # <V>
    _of_3__K = typing.TypeVar('_of_3__K')  # <K>
    _of_3__V = typing.TypeVar('_of_3__V')  # <V>
    _of_4__K = typing.TypeVar('_of_4__K')  # <K>
    _of_4__V = typing.TypeVar('_of_4__V')  # <V>
    _of_5__K = typing.TypeVar('_of_5__K')  # <K>
    _of_5__V = typing.TypeVar('_of_5__V')  # <V>
    _of_6__K = typing.TypeVar('_of_6__K')  # <K>
    _of_6__V = typing.TypeVar('_of_6__V')  # <V>
    _of_7__K = typing.TypeVar('_of_7__K')  # <K>
    _of_7__V = typing.TypeVar('_of_7__V')  # <V>
    _of_8__K = typing.TypeVar('_of_8__K')  # <K>
    _of_8__V = typing.TypeVar('_of_8__V')  # <V>
    _of_9__K = typing.TypeVar('_of_9__K')  # <K>
    _of_9__V = typing.TypeVar('_of_9__V')  # <V>
    _of_10__K = typing.TypeVar('_of_10__K')  # <K>
    _of_10__V = typing.TypeVar('_of_10__V')  # <V>
    _of_11__K = typing.TypeVar('_of_11__K')  # <K>
    _of_11__V = typing.TypeVar('_of_11__V')  # <V>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableBiMap'[_of_0__K, _of_0__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_1__K, v: _of_1__V) -> 'ImmutableBiMap'[_of_1__K, _of_1__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_2__K, v: _of_2__V, k2: _of_2__K, v2: _of_2__V) -> 'ImmutableBiMap'[_of_2__K, _of_2__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_3__K, v: _of_3__V, k2: _of_3__K, v2: _of_3__V, k3: _of_3__K, v3: _of_3__V) -> 'ImmutableBiMap'[_of_3__K, _of_3__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_4__K, v: _of_4__V, k2: _of_4__K, v2: _of_4__V, k3: _of_4__K, v3: _of_4__V, k4: _of_4__K, v4: _of_4__V) -> 'ImmutableBiMap'[_of_4__K, _of_4__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_5__K, v: _of_5__V, k2: _of_5__K, v2: _of_5__V, k3: _of_5__K, v3: _of_5__V, k4: _of_5__K, v4: _of_5__V, k5: _of_5__K, v5: _of_5__V) -> 'ImmutableBiMap'[_of_5__K, _of_5__V]: ...
    @typing.overload
    @staticmethod
    def of() -> ImmutableMap[_of_6__K, _of_6__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_7__K, v: _of_7__V) -> ImmutableMap[_of_7__K, _of_7__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_8__K, v: _of_8__V, k2: _of_8__K, v2: _of_8__V) -> ImmutableMap[_of_8__K, _of_8__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_9__K, v: _of_9__V, k2: _of_9__K, v2: _of_9__V, k3: _of_9__K, v3: _of_9__V) -> ImmutableMap[_of_9__K, _of_9__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_10__K, v: _of_10__V, k2: _of_10__K, v2: _of_10__V, k3: _of_10__K, v3: _of_10__V, k4: _of_10__K, v4: _of_10__V) -> ImmutableMap[_of_10__K, _of_10__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_11__K, v: _of_11__V, k2: _of_11__K, v2: _of_11__V, k3: _of_11__K, v3: _of_11__V, k4: _of_11__K, v4: _of_11__V, k5: _of_11__K, v5: _of_11__V) -> ImmutableMap[_of_11__K, _of_11__V]: ...
    _toImmutableBiMap__T = typing.TypeVar('_toImmutableBiMap__T')  # <T>
    _toImmutableBiMap__K = typing.TypeVar('_toImmutableBiMap__K')  # <K>
    _toImmutableBiMap__V = typing.TypeVar('_toImmutableBiMap__V')  # <V>
    @staticmethod
    def toImmutableBiMap(function: typing.Union[java.util.function.Function[_toImmutableBiMap__T, _toImmutableBiMap__K], typing.Callable[[_toImmutableBiMap__T], _toImmutableBiMap__K]], function2: typing.Union[java.util.function.Function[_toImmutableBiMap__T, _toImmutableBiMap__V], typing.Callable[[_toImmutableBiMap__T], _toImmutableBiMap__V]]) -> java.util.stream.Collector[_toImmutableBiMap__T, typing.Any, 'ImmutableBiMap'[_toImmutableBiMap__K, _toImmutableBiMap__V]]: ...
    def values(self) -> ImmutableSet[_ImmutableBiMap__V]: ...
    class Builder(ImmutableMap.Builder[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V], typing.Generic[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V]):
        def __init__(self): ...
        def build(self) -> 'ImmutableBiMap'[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V]: ...
        def orderEntriesByValue(self, comparator: typing.Union[java.util.Comparator[_ImmutableBiMap__Builder__V], typing.Callable[[_ImmutableBiMap__Builder__V, _ImmutableBiMap__Builder__V], int]]) -> 'ImmutableBiMap.Builder'[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V]: ...
        @typing.overload
        def put(self, k: _ImmutableBiMap__Builder__K, v: _ImmutableBiMap__Builder__V) -> 'ImmutableBiMap.Builder'[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V]: ...
        @typing.overload
        def put(self, entry: java.util.Map.Entry[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V]) -> 'ImmutableBiMap.Builder'[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V]: ...
        @typing.overload
        def putAll(self, iterable: java.lang.Iterable[java.util.Map.Entry[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V]]) -> 'ImmutableBiMap.Builder'[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V]: ...
        @typing.overload
        def putAll(self, map: typing.Union[java.util.Map[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V], typing.Mapping[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V]]) -> 'ImmutableBiMap.Builder'[_ImmutableBiMap__Builder__K, _ImmutableBiMap__Builder__V]: ...

_ImmutableListMultimap__Builder__K = typing.TypeVar('_ImmutableListMultimap__Builder__K')  # <K>
_ImmutableListMultimap__Builder__V = typing.TypeVar('_ImmutableListMultimap__Builder__V')  # <V>
_ImmutableListMultimap__K = typing.TypeVar('_ImmutableListMultimap__K')  # <K>
_ImmutableListMultimap__V = typing.TypeVar('_ImmutableListMultimap__V')  # <V>
class ImmutableListMultimap(com.google.common.collect.ImmutableMultimap[_ImmutableListMultimap__K, _ImmutableListMultimap__V], ListMultimap[_ImmutableListMultimap__K, _ImmutableListMultimap__V], typing.Generic[_ImmutableListMultimap__K, _ImmutableListMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ImmutableMultimap`<K,V> implements :class:`~com.google.common.collect.ListMultimap`<K,V>
    
        A :class:`~com.google.common.collect.ListMultimap` whose contents will never change, with many other important
        properties detailed at :class:`~com.google.common.collect.ImmutableCollection`.
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    _builder_0__K = typing.TypeVar('_builder_0__K')  # <K>
    _builder_0__V = typing.TypeVar('_builder_0__V')  # <V>
    _builder_1__K = typing.TypeVar('_builder_1__K')  # <K>
    _builder_1__V = typing.TypeVar('_builder_1__V')  # <V>
    @typing.overload
    @staticmethod
    def builder() -> 'ImmutableListMultimap.Builder'[_builder_0__K, _builder_0__V]: ...
    @typing.overload
    @staticmethod
    def builder() -> 'ImmutableMultimap.Builder'[_builder_1__K, _builder_1__V]: ...
    _copyOf_0__K = typing.TypeVar('_copyOf_0__K')  # <K>
    _copyOf_0__V = typing.TypeVar('_copyOf_0__V')  # <V>
    _copyOf_1__K = typing.TypeVar('_copyOf_1__K')  # <K>
    _copyOf_1__V = typing.TypeVar('_copyOf_1__V')  # <V>
    _copyOf_2__K = typing.TypeVar('_copyOf_2__K')  # <K>
    _copyOf_2__V = typing.TypeVar('_copyOf_2__V')  # <V>
    _copyOf_3__K = typing.TypeVar('_copyOf_3__K')  # <K>
    _copyOf_3__V = typing.TypeVar('_copyOf_3__V')  # <V>
    @typing.overload
    @staticmethod
    def copyOf(multimap: Multimap[_copyOf_0__K, _copyOf_0__V]) -> 'ImmutableListMultimap'[_copyOf_0__K, _copyOf_0__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_1__K, _copyOf_1__V]]) -> 'ImmutableListMultimap'[_copyOf_1__K, _copyOf_1__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(multimap: Multimap[_copyOf_2__K, _copyOf_2__V]) -> 'ImmutableMultimap'[_copyOf_2__K, _copyOf_2__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_3__K, _copyOf_3__V]]) -> 'ImmutableMultimap'[_copyOf_3__K, _copyOf_3__V]: ...
    _flatteningToImmutableListMultimap__T = typing.TypeVar('_flatteningToImmutableListMultimap__T')  # <T>
    _flatteningToImmutableListMultimap__K = typing.TypeVar('_flatteningToImmutableListMultimap__K')  # <K>
    _flatteningToImmutableListMultimap__V = typing.TypeVar('_flatteningToImmutableListMultimap__V')  # <V>
    @staticmethod
    def flatteningToImmutableListMultimap(function: typing.Union[java.util.function.Function[_flatteningToImmutableListMultimap__T, _flatteningToImmutableListMultimap__K], typing.Callable[[_flatteningToImmutableListMultimap__T], _flatteningToImmutableListMultimap__K]], function2: typing.Union[java.util.function.Function[_flatteningToImmutableListMultimap__T, java.util.stream.Stream[_flatteningToImmutableListMultimap__V]], typing.Callable[[_flatteningToImmutableListMultimap__T], java.util.stream.Stream[_flatteningToImmutableListMultimap__V]]]) -> java.util.stream.Collector[_flatteningToImmutableListMultimap__T, typing.Any, 'ImmutableListMultimap'[_flatteningToImmutableListMultimap__K, _flatteningToImmutableListMultimap__V]]: ...
    def get(self, k: _ImmutableListMultimap__K) -> ImmutableList[_ImmutableListMultimap__V]: ...
    def inverse(self) -> 'ImmutableListMultimap'[_ImmutableListMultimap__V, _ImmutableListMultimap__K]: ...
    _of_0__K = typing.TypeVar('_of_0__K')  # <K>
    _of_0__V = typing.TypeVar('_of_0__V')  # <V>
    _of_1__K = typing.TypeVar('_of_1__K')  # <K>
    _of_1__V = typing.TypeVar('_of_1__V')  # <V>
    _of_2__K = typing.TypeVar('_of_2__K')  # <K>
    _of_2__V = typing.TypeVar('_of_2__V')  # <V>
    _of_3__K = typing.TypeVar('_of_3__K')  # <K>
    _of_3__V = typing.TypeVar('_of_3__V')  # <V>
    _of_4__K = typing.TypeVar('_of_4__K')  # <K>
    _of_4__V = typing.TypeVar('_of_4__V')  # <V>
    _of_5__K = typing.TypeVar('_of_5__K')  # <K>
    _of_5__V = typing.TypeVar('_of_5__V')  # <V>
    _of_6__K = typing.TypeVar('_of_6__K')  # <K>
    _of_6__V = typing.TypeVar('_of_6__V')  # <V>
    _of_7__K = typing.TypeVar('_of_7__K')  # <K>
    _of_7__V = typing.TypeVar('_of_7__V')  # <V>
    _of_8__K = typing.TypeVar('_of_8__K')  # <K>
    _of_8__V = typing.TypeVar('_of_8__V')  # <V>
    _of_9__K = typing.TypeVar('_of_9__K')  # <K>
    _of_9__V = typing.TypeVar('_of_9__V')  # <V>
    _of_10__K = typing.TypeVar('_of_10__K')  # <K>
    _of_10__V = typing.TypeVar('_of_10__V')  # <V>
    _of_11__K = typing.TypeVar('_of_11__K')  # <K>
    _of_11__V = typing.TypeVar('_of_11__V')  # <V>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableListMultimap'[_of_0__K, _of_0__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_1__K, v: _of_1__V) -> 'ImmutableListMultimap'[_of_1__K, _of_1__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_2__K, v: _of_2__V, k2: _of_2__K, v2: _of_2__V) -> 'ImmutableListMultimap'[_of_2__K, _of_2__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_3__K, v: _of_3__V, k2: _of_3__K, v2: _of_3__V, k3: _of_3__K, v3: _of_3__V) -> 'ImmutableListMultimap'[_of_3__K, _of_3__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_4__K, v: _of_4__V, k2: _of_4__K, v2: _of_4__V, k3: _of_4__K, v3: _of_4__V, k4: _of_4__K, v4: _of_4__V) -> 'ImmutableListMultimap'[_of_4__K, _of_4__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_5__K, v: _of_5__V, k2: _of_5__K, v2: _of_5__V, k3: _of_5__K, v3: _of_5__V, k4: _of_5__K, v4: _of_5__V, k5: _of_5__K, v5: _of_5__V) -> 'ImmutableListMultimap'[_of_5__K, _of_5__V]: ...
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableMultimap'[_of_6__K, _of_6__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_7__K, v: _of_7__V) -> 'ImmutableMultimap'[_of_7__K, _of_7__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_8__K, v: _of_8__V, k2: _of_8__K, v2: _of_8__V) -> 'ImmutableMultimap'[_of_8__K, _of_8__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_9__K, v: _of_9__V, k2: _of_9__K, v2: _of_9__V, k3: _of_9__K, v3: _of_9__V) -> 'ImmutableMultimap'[_of_9__K, _of_9__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_10__K, v: _of_10__V, k2: _of_10__K, v2: _of_10__V, k3: _of_10__K, v3: _of_10__V, k4: _of_10__K, v4: _of_10__V) -> 'ImmutableMultimap'[_of_10__K, _of_10__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_11__K, v: _of_11__V, k2: _of_11__K, v2: _of_11__V, k3: _of_11__K, v3: _of_11__V, k4: _of_11__K, v4: _of_11__V, k5: _of_11__K, v5: _of_11__V) -> 'ImmutableMultimap'[_of_11__K, _of_11__V]: ...
    def removeAll(self, object: typing.Any) -> ImmutableList[_ImmutableListMultimap__V]: ...
    def replaceValues(self, k: _ImmutableListMultimap__K, iterable: java.lang.Iterable[_ImmutableListMultimap__V]) -> ImmutableList[_ImmutableListMultimap__V]: ...
    _toImmutableListMultimap__T = typing.TypeVar('_toImmutableListMultimap__T')  # <T>
    _toImmutableListMultimap__K = typing.TypeVar('_toImmutableListMultimap__K')  # <K>
    _toImmutableListMultimap__V = typing.TypeVar('_toImmutableListMultimap__V')  # <V>
    @staticmethod
    def toImmutableListMultimap(function: typing.Union[java.util.function.Function[_toImmutableListMultimap__T, _toImmutableListMultimap__K], typing.Callable[[_toImmutableListMultimap__T], _toImmutableListMultimap__K]], function2: typing.Union[java.util.function.Function[_toImmutableListMultimap__T, _toImmutableListMultimap__V], typing.Callable[[_toImmutableListMultimap__T], _toImmutableListMultimap__V]]) -> java.util.stream.Collector[_toImmutableListMultimap__T, typing.Any, 'ImmutableListMultimap'[_toImmutableListMultimap__K, _toImmutableListMultimap__V]]: ...
    class Builder(com.google.common.collect.ImmutableMultimap.Builder[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V], typing.Generic[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]):
        def __init__(self): ...
        def build(self) -> 'ImmutableListMultimap'[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]: ...
        def orderKeysBy(self, comparator: typing.Union[java.util.Comparator[_ImmutableListMultimap__Builder__K], typing.Callable[[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__K], int]]) -> 'ImmutableListMultimap.Builder'[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]: ...
        def orderValuesBy(self, comparator: typing.Union[java.util.Comparator[_ImmutableListMultimap__Builder__V], typing.Callable[[_ImmutableListMultimap__Builder__V, _ImmutableListMultimap__Builder__V], int]]) -> 'ImmutableListMultimap.Builder'[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]: ...
        @typing.overload
        def put(self, k: _ImmutableListMultimap__Builder__K, v: _ImmutableListMultimap__Builder__V) -> 'ImmutableListMultimap.Builder'[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]: ...
        @typing.overload
        def put(self, entry: java.util.Map.Entry[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]) -> 'ImmutableListMultimap.Builder'[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, multimap: Multimap[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]) -> 'ImmutableListMultimap.Builder'[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, iterable: java.lang.Iterable[java.util.Map.Entry[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]]) -> 'ImmutableListMultimap.Builder'[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, k: _ImmutableListMultimap__Builder__K, iterable: java.lang.Iterable[_ImmutableListMultimap__Builder__V]) -> 'ImmutableListMultimap.Builder'[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, k: _ImmutableListMultimap__Builder__K, vArray: typing.List[_ImmutableListMultimap__Builder__V]) -> 'ImmutableListMultimap.Builder'[_ImmutableListMultimap__Builder__K, _ImmutableListMultimap__Builder__V]: ...

_ImmutableMultimap__Builder__K = typing.TypeVar('_ImmutableMultimap__Builder__K')  # <K>
_ImmutableMultimap__Builder__V = typing.TypeVar('_ImmutableMultimap__Builder__V')  # <V>
_ImmutableMultimap__K = typing.TypeVar('_ImmutableMultimap__K')  # <K>
_ImmutableMultimap__V = typing.TypeVar('_ImmutableMultimap__V')  # <V>
class ImmutableMultimap(com.google.common.collect.BaseImmutableMultimap[_ImmutableMultimap__K, _ImmutableMultimap__V], java.io.Serializable, typing.Generic[_ImmutableMultimap__K, _ImmutableMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<K,V> extends Object implements Serializable
    
        A :class:`~com.google.common.collect.Multimap` whose contents will never change, with many other important properties
        detailed at :class:`~com.google.common.collect.ImmutableCollection`.
    
        **Warning:** avoid *direct* usage of :class:`~com.google.common.collect.ImmutableMultimap` as a type (as with
        :class:`~com.google.common.collect.Multimap` itself). Prefer subtypes such as
        :class:`~com.google.common.collect.ImmutableSetMultimap` or :class:`~com.google.common.collect.ImmutableListMultimap`,
        which have well-defined :meth:`~com.google.common.collect.ImmutableMultimap.equals` semantics, thus avoiding a common
        source of bugs and confusion.
    
        **Note:** every :class:`~com.google.common.collect.ImmutableMultimap` offers an
        :meth:`~com.google.common.collect.ImmutableMultimap.inverse` view, so there is no need for a distinct
        :code:`ImmutableBiMultimap` type.
    
        :class:`~com.google.common.collect`
    
        **Key-grouped iteration.** All view collections follow the same iteration order. In all current implementations, the
        iteration order always keeps multiple entries with the same key together. Any creation method that would customarily
        respect insertion order (such as :meth:`~com.google.common.collect.ImmutableMultimap.copyOf`) instead preserves
        key-grouped order by inserting entries for an existing key immediately after the last entry having that key.
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def asMap(self) -> ImmutableMap[_ImmutableMultimap__K, java.util.Collection[_ImmutableMultimap__V]]: ...
    _builder__K = typing.TypeVar('_builder__K')  # <K>
    _builder__V = typing.TypeVar('_builder__V')  # <V>
    @staticmethod
    def builder() -> 'ImmutableMultimap.Builder'[_builder__K, _builder__V]: ...
    def clear(self) -> None: ...
    def containsKey(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    _copyOf_0__K = typing.TypeVar('_copyOf_0__K')  # <K>
    _copyOf_0__V = typing.TypeVar('_copyOf_0__V')  # <V>
    _copyOf_1__K = typing.TypeVar('_copyOf_1__K')  # <K>
    _copyOf_1__V = typing.TypeVar('_copyOf_1__V')  # <V>
    @typing.overload
    @staticmethod
    def copyOf(multimap: Multimap[_copyOf_0__K, _copyOf_0__V]) -> 'ImmutableMultimap'[_copyOf_0__K, _copyOf_0__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_1__K, _copyOf_1__V]]) -> 'ImmutableMultimap'[_copyOf_1__K, _copyOf_1__V]: ...
    def entries(self) -> ImmutableCollection[java.util.Map.Entry[_ImmutableMultimap__K, _ImmutableMultimap__V]]: ...
    def forEach(self, biConsumer: typing.Union[java.util.function.BiConsumer[_ImmutableMultimap__K, _ImmutableMultimap__V], typing.Callable[[_ImmutableMultimap__K, _ImmutableMultimap__V], None]]) -> None: ...
    def get(self, k: _ImmutableMultimap__K) -> ImmutableCollection[_ImmutableMultimap__V]: ...
    def inverse(self) -> 'ImmutableMultimap'[_ImmutableMultimap__V, _ImmutableMultimap__K]: ...
    def keySet(self) -> ImmutableSet[_ImmutableMultimap__K]: ...
    def keys(self) -> 'ImmutableMultiset'[_ImmutableMultimap__K]: ...
    _of_0__K = typing.TypeVar('_of_0__K')  # <K>
    _of_0__V = typing.TypeVar('_of_0__V')  # <V>
    _of_1__K = typing.TypeVar('_of_1__K')  # <K>
    _of_1__V = typing.TypeVar('_of_1__V')  # <V>
    _of_2__K = typing.TypeVar('_of_2__K')  # <K>
    _of_2__V = typing.TypeVar('_of_2__V')  # <V>
    _of_3__K = typing.TypeVar('_of_3__K')  # <K>
    _of_3__V = typing.TypeVar('_of_3__V')  # <V>
    _of_4__K = typing.TypeVar('_of_4__K')  # <K>
    _of_4__V = typing.TypeVar('_of_4__V')  # <V>
    _of_5__K = typing.TypeVar('_of_5__K')  # <K>
    _of_5__V = typing.TypeVar('_of_5__V')  # <V>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableMultimap'[_of_0__K, _of_0__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_1__K, v: _of_1__V) -> 'ImmutableMultimap'[_of_1__K, _of_1__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_2__K, v: _of_2__V, k2: _of_2__K, v2: _of_2__V) -> 'ImmutableMultimap'[_of_2__K, _of_2__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_3__K, v: _of_3__V, k2: _of_3__K, v2: _of_3__V, k3: _of_3__K, v3: _of_3__V) -> 'ImmutableMultimap'[_of_3__K, _of_3__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_4__K, v: _of_4__V, k2: _of_4__K, v2: _of_4__V, k3: _of_4__K, v3: _of_4__V, k4: _of_4__K, v4: _of_4__V) -> 'ImmutableMultimap'[_of_4__K, _of_4__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_5__K, v: _of_5__V, k2: _of_5__K, v2: _of_5__V, k3: _of_5__K, v3: _of_5__V, k4: _of_5__K, v4: _of_5__V, k5: _of_5__K, v5: _of_5__V) -> 'ImmutableMultimap'[_of_5__K, _of_5__V]: ...
    def put(self, k: _ImmutableMultimap__K, v: _ImmutableMultimap__V) -> bool: ...
    @typing.overload
    def putAll(self, multimap: Multimap[_ImmutableMultimap__K, _ImmutableMultimap__V]) -> bool: ...
    @typing.overload
    def putAll(self, k: _ImmutableMultimap__K, iterable: java.lang.Iterable[_ImmutableMultimap__V]) -> bool: ...
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...
    def removeAll(self, object: typing.Any) -> ImmutableCollection[_ImmutableMultimap__V]: ...
    def replaceValues(self, k: _ImmutableMultimap__K, iterable: java.lang.Iterable[_ImmutableMultimap__V]) -> ImmutableCollection[_ImmutableMultimap__V]: ...
    def size(self) -> int: ...
    def values(self) -> ImmutableCollection[_ImmutableMultimap__V]: ...
    class Builder(typing.Generic[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]):
        def __init__(self): ...
        def build(self) -> 'ImmutableMultimap'[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]: ...
        def orderKeysBy(self, comparator: typing.Union[java.util.Comparator[_ImmutableMultimap__Builder__K], typing.Callable[[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__K], int]]) -> 'ImmutableMultimap.Builder'[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]: ...
        def orderValuesBy(self, comparator: typing.Union[java.util.Comparator[_ImmutableMultimap__Builder__V], typing.Callable[[_ImmutableMultimap__Builder__V, _ImmutableMultimap__Builder__V], int]]) -> 'ImmutableMultimap.Builder'[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]: ...
        @typing.overload
        def put(self, k: _ImmutableMultimap__Builder__K, v: _ImmutableMultimap__Builder__V) -> 'ImmutableMultimap.Builder'[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]: ...
        @typing.overload
        def put(self, entry: java.util.Map.Entry[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]) -> 'ImmutableMultimap.Builder'[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, multimap: Multimap[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]) -> 'ImmutableMultimap.Builder'[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, iterable: java.lang.Iterable[java.util.Map.Entry[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]]) -> 'ImmutableMultimap.Builder'[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, k: _ImmutableMultimap__Builder__K, iterable: java.lang.Iterable[_ImmutableMultimap__Builder__V]) -> 'ImmutableMultimap.Builder'[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, k: _ImmutableMultimap__Builder__K, vArray: typing.List[_ImmutableMultimap__Builder__V]) -> 'ImmutableMultimap.Builder'[_ImmutableMultimap__Builder__K, _ImmutableMultimap__Builder__V]: ...

_ImmutableMultiset__Builder__E = typing.TypeVar('_ImmutableMultiset__Builder__E')  # <E>
_ImmutableMultiset__E = typing.TypeVar('_ImmutableMultiset__E')  # <E>
class ImmutableMultiset(com.google.common.collect.ImmutableMultisetGwtSerializationDependencies[_ImmutableMultiset__E], Multiset[_ImmutableMultiset__E], typing.Generic[_ImmutableMultiset__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ImmutableCollection`<E> implements :class:`~com.google.common.collect.Multiset`<E>
    
        A :class:`~com.google.common.collect.Multiset` whose contents will never change, with many other important properties
        detailed at :class:`~com.google.common.collect.ImmutableCollection`.
    
        **Grouped iteration.** In all current implementations, duplicate elements always appear consecutively when iterating.
        Elements iterate in order by the *first* appearance of that element when the multiset was created.
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def add(self, e: _ImmutableMultiset__E) -> bool: ...
    @typing.overload
    def add(self, e: _ImmutableMultiset__E, int: int) -> int: ...
    def asList(self) -> ImmutableList[_ImmutableMultiset__E]: ...
    _builder__E = typing.TypeVar('_builder__E')  # <E>
    @staticmethod
    def builder() -> 'ImmutableMultiset.Builder'[_builder__E]: ...
    def contains(self, object: typing.Any) -> bool: ...
    _copyOf_0__E = typing.TypeVar('_copyOf_0__E')  # <E>
    _copyOf_1__E = typing.TypeVar('_copyOf_1__E')  # <E>
    _copyOf_2__E = typing.TypeVar('_copyOf_2__E')  # <E>
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[_copyOf_0__E]) -> 'ImmutableMultiset'[_copyOf_0__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(eArray: typing.List[_copyOf_1__E]) -> 'ImmutableMultiset'[_copyOf_1__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterator: java.util.Iterator[_copyOf_2__E]) -> 'ImmutableMultiset'[_copyOf_2__E]: ...
    def elementSet(self) -> ImmutableSet[_ImmutableMultiset__E]: ...
    def entrySet(self) -> ImmutableSet[Multiset.Entry[_ImmutableMultiset__E]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def iterator(self) -> UnmodifiableIterator[_ImmutableMultiset__E]: ...
    _of_0__E = typing.TypeVar('_of_0__E')  # <E>
    _of_1__E = typing.TypeVar('_of_1__E')  # <E>
    _of_2__E = typing.TypeVar('_of_2__E')  # <E>
    _of_3__E = typing.TypeVar('_of_3__E')  # <E>
    _of_4__E = typing.TypeVar('_of_4__E')  # <E>
    _of_5__E = typing.TypeVar('_of_5__E')  # <E>
    _of_6__E = typing.TypeVar('_of_6__E')  # <E>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableMultiset'[_of_0__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_1__E) -> 'ImmutableMultiset'[_of_1__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_2__E, e2: _of_2__E) -> 'ImmutableMultiset'[_of_2__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_3__E, e2: _of_3__E, e3: _of_3__E) -> 'ImmutableMultiset'[_of_3__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_4__E, e2: _of_4__E, e3: _of_4__E, e4: _of_4__E) -> 'ImmutableMultiset'[_of_4__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_5__E, e2: _of_5__E, e3: _of_5__E, e4: _of_5__E, e5: _of_5__E) -> 'ImmutableMultiset'[_of_5__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_6__E, e2: _of_6__E, e3: _of_6__E, e4: _of_6__E, e5: _of_6__E, e6: _of_6__E, eArray: typing.List[_of_6__E]) -> 'ImmutableMultiset'[_of_6__E]: ...
    @typing.overload
    def remove(self, object: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any, int: int) -> int: ...
    @typing.overload
    def setCount(self, e: _ImmutableMultiset__E, int: int, int2: int) -> bool: ...
    @typing.overload
    def setCount(self, e: _ImmutableMultiset__E, int: int) -> int: ...
    _toImmutableMultiset_0__E = typing.TypeVar('_toImmutableMultiset_0__E')  # <E>
    _toImmutableMultiset_1__T = typing.TypeVar('_toImmutableMultiset_1__T')  # <T>
    _toImmutableMultiset_1__E = typing.TypeVar('_toImmutableMultiset_1__E')  # <E>
    @typing.overload
    @staticmethod
    def toImmutableMultiset() -> java.util.stream.Collector[_toImmutableMultiset_0__E, typing.Any, 'ImmutableMultiset'[_toImmutableMultiset_0__E]]: ...
    @typing.overload
    @staticmethod
    def toImmutableMultiset(function: typing.Union[java.util.function.Function[_toImmutableMultiset_1__T, _toImmutableMultiset_1__E], typing.Callable[[_toImmutableMultiset_1__T], _toImmutableMultiset_1__E]], toIntFunction: typing.Union[java.util.function.ToIntFunction[_toImmutableMultiset_1__T], typing.Callable[[_toImmutableMultiset_1__T], int]]) -> java.util.stream.Collector[_toImmutableMultiset_1__T, typing.Any, 'ImmutableMultiset'[_toImmutableMultiset_1__E]]: ...
    def toString(self) -> str: ...
    class Builder(ImmutableCollection.Builder[_ImmutableMultiset__Builder__E], typing.Generic[_ImmutableMultiset__Builder__E]):
        def __init__(self): ...
        @typing.overload
        def add(self, e: _ImmutableMultiset__Builder__E) -> 'ImmutableMultiset.Builder'[_ImmutableMultiset__Builder__E]: ...
        @typing.overload
        def add(self, eArray: typing.List[_ImmutableMultiset__Builder__E]) -> 'ImmutableMultiset.Builder'[_ImmutableMultiset__Builder__E]: ...
        @typing.overload
        def addAll(self, iterable: java.lang.Iterable[_ImmutableMultiset__Builder__E]) -> 'ImmutableMultiset.Builder'[_ImmutableMultiset__Builder__E]: ...
        @typing.overload
        def addAll(self, iterator: java.util.Iterator[_ImmutableMultiset__Builder__E]) -> 'ImmutableMultiset.Builder'[_ImmutableMultiset__Builder__E]: ...
        def addCopies(self, e: _ImmutableMultiset__Builder__E, int: int) -> 'ImmutableMultiset.Builder'[_ImmutableMultiset__Builder__E]: ...
        def build(self) -> 'ImmutableMultiset'[_ImmutableMultiset__Builder__E]: ...
        def setCount(self, e: _ImmutableMultiset__Builder__E, int: int) -> 'ImmutableMultiset.Builder'[_ImmutableMultiset__Builder__E]: ...

_ImmutableRangeSet__Builder__C = typing.TypeVar('_ImmutableRangeSet__Builder__C', bound=java.lang.Comparable)  # <C>
_ImmutableRangeSet__C = typing.TypeVar('_ImmutableRangeSet__C', bound=java.lang.Comparable)  # <C>
class ImmutableRangeSet(com.google.common.collect.AbstractRangeSet[_ImmutableRangeSet__C], java.io.Serializable, typing.Generic[_ImmutableRangeSet__C]):
    """
    :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtIncompatible` public final class :meth:`~src`<C extends Comparable> extends Object implements Serializable
    
        A :class:`~com.google.common.collect.RangeSet` whose contents will never change, with many other important properties
        detailed at :class:`~com.google.common.collect.ImmutableCollection`.
    
        Since:
            14.0
    
        Also see:
            :meth:`~serialized`
    """
    def add(self, range: 'Range'[_ImmutableRangeSet__C]) -> None: ...
    @typing.overload
    def addAll(self, rangeSet: RangeSet[_ImmutableRangeSet__C]) -> None: ...
    @typing.overload
    def addAll(self, iterable: java.lang.Iterable['Range'[_ImmutableRangeSet__C]]) -> None: ...
    def asDescendingSetOfRanges(self) -> ImmutableSet['Range'[_ImmutableRangeSet__C]]: ...
    def asRanges(self) -> ImmutableSet['Range'[_ImmutableRangeSet__C]]: ...
    def asSet(self, discreteDomain: DiscreteDomain[_ImmutableRangeSet__C]) -> 'ImmutableSortedSet'[_ImmutableRangeSet__C]: ...
    _builder__C = typing.TypeVar('_builder__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def builder() -> 'ImmutableRangeSet.Builder'[_builder__C]: ...
    def complement(self) -> 'ImmutableRangeSet'[_ImmutableRangeSet__C]: ...
    _copyOf_0__C = typing.TypeVar('_copyOf_0__C', bound=java.lang.Comparable)  # <C>
    _copyOf_1__C = typing.TypeVar('_copyOf_1__C', bound=java.lang.Comparable)  # <C>
    @typing.overload
    @staticmethod
    def copyOf(rangeSet: RangeSet[_copyOf_0__C]) -> 'ImmutableRangeSet'[_copyOf_0__C]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable['Range'[_copyOf_1__C]]) -> 'ImmutableRangeSet'[_copyOf_1__C]: ...
    def difference(self, rangeSet: RangeSet[_ImmutableRangeSet__C]) -> 'ImmutableRangeSet'[_ImmutableRangeSet__C]: ...
    def encloses(self, range: 'Range'[_ImmutableRangeSet__C]) -> bool: ...
    def enclosesAll(self, iterable: java.lang.Iterable['Range'[_ImmutableRangeSet__C]]) -> bool: ...
    def intersection(self, rangeSet: RangeSet[_ImmutableRangeSet__C]) -> 'ImmutableRangeSet'[_ImmutableRangeSet__C]: ...
    def intersects(self, range: 'Range'[_ImmutableRangeSet__C]) -> bool: ...
    def isEmpty(self) -> bool: ...
    _of_0__C = typing.TypeVar('_of_0__C', bound=java.lang.Comparable)  # <C>
    _of_1__C = typing.TypeVar('_of_1__C', bound=java.lang.Comparable)  # <C>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableRangeSet'[_of_0__C]: ...
    @typing.overload
    @staticmethod
    def of(range: 'Range'[_of_1__C]) -> 'ImmutableRangeSet'[_of_1__C]: ...
    def rangeContaining(self, c: _ImmutableRangeSet__C) -> 'Range'[_ImmutableRangeSet__C]: ...
    def remove(self, range: 'Range'[_ImmutableRangeSet__C]) -> None: ...
    @typing.overload
    def removeAll(self, rangeSet: RangeSet[_ImmutableRangeSet__C]) -> None: ...
    @typing.overload
    def removeAll(self, iterable: java.lang.Iterable['Range'[_ImmutableRangeSet__C]]) -> None: ...
    def span(self) -> 'Range'[_ImmutableRangeSet__C]: ...
    def subRangeSet(self, range: 'Range'[_ImmutableRangeSet__C]) -> 'ImmutableRangeSet'[_ImmutableRangeSet__C]: ...
    _toImmutableRangeSet__E = typing.TypeVar('_toImmutableRangeSet__E', bound=java.lang.Comparable)  # <E>
    @staticmethod
    def toImmutableRangeSet() -> java.util.stream.Collector['Range'[_toImmutableRangeSet__E], typing.Any, 'ImmutableRangeSet'[_toImmutableRangeSet__E]]: ...
    def union(self, rangeSet: RangeSet[_ImmutableRangeSet__C]) -> 'ImmutableRangeSet'[_ImmutableRangeSet__C]: ...
    _unionOf__C = typing.TypeVar('_unionOf__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def unionOf(iterable: java.lang.Iterable['Range'[_unionOf__C]]) -> 'ImmutableRangeSet'[_unionOf__C]: ...
    class Builder(typing.Generic[_ImmutableRangeSet__Builder__C]):
        def __init__(self): ...
        def add(self, range: 'Range'[_ImmutableRangeSet__Builder__C]) -> 'ImmutableRangeSet.Builder'[_ImmutableRangeSet__Builder__C]: ...
        @typing.overload
        def addAll(self, rangeSet: RangeSet[_ImmutableRangeSet__Builder__C]) -> 'ImmutableRangeSet.Builder'[_ImmutableRangeSet__Builder__C]: ...
        @typing.overload
        def addAll(self, iterable: java.lang.Iterable['Range'[_ImmutableRangeSet__Builder__C]]) -> 'ImmutableRangeSet.Builder'[_ImmutableRangeSet__Builder__C]: ...
        def build(self) -> 'ImmutableRangeSet'[_ImmutableRangeSet__Builder__C]: ...

_ImmutableSetMultimap__Builder__K = typing.TypeVar('_ImmutableSetMultimap__Builder__K')  # <K>
_ImmutableSetMultimap__Builder__V = typing.TypeVar('_ImmutableSetMultimap__Builder__V')  # <V>
_ImmutableSetMultimap__K = typing.TypeVar('_ImmutableSetMultimap__K')  # <K>
_ImmutableSetMultimap__V = typing.TypeVar('_ImmutableSetMultimap__V')  # <V>
class ImmutableSetMultimap(ImmutableMultimap[_ImmutableSetMultimap__K, _ImmutableSetMultimap__V], SetMultimap[_ImmutableSetMultimap__K, _ImmutableSetMultimap__V], typing.Generic[_ImmutableSetMultimap__K, _ImmutableSetMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ImmutableMultimap`<K,V> implements :class:`~com.google.common.collect.SetMultimap`<K,V>
    
        A :class:`~com.google.common.collect.SetMultimap` whose contents will never change, with many other important properties
        detailed at :class:`~com.google.common.collect.ImmutableCollection`.
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    _builder_0__K = typing.TypeVar('_builder_0__K')  # <K>
    _builder_0__V = typing.TypeVar('_builder_0__V')  # <V>
    _builder_1__K = typing.TypeVar('_builder_1__K')  # <K>
    _builder_1__V = typing.TypeVar('_builder_1__V')  # <V>
    @typing.overload
    @staticmethod
    def builder() -> ImmutableMultimap.Builder[_builder_0__K, _builder_0__V]: ...
    @typing.overload
    @staticmethod
    def builder() -> 'ImmutableSetMultimap.Builder'[_builder_1__K, _builder_1__V]: ...
    _copyOf_0__K = typing.TypeVar('_copyOf_0__K')  # <K>
    _copyOf_0__V = typing.TypeVar('_copyOf_0__V')  # <V>
    _copyOf_1__K = typing.TypeVar('_copyOf_1__K')  # <K>
    _copyOf_1__V = typing.TypeVar('_copyOf_1__V')  # <V>
    _copyOf_2__K = typing.TypeVar('_copyOf_2__K')  # <K>
    _copyOf_2__V = typing.TypeVar('_copyOf_2__V')  # <V>
    _copyOf_3__K = typing.TypeVar('_copyOf_3__K')  # <K>
    _copyOf_3__V = typing.TypeVar('_copyOf_3__V')  # <V>
    @typing.overload
    @staticmethod
    def copyOf(multimap: Multimap[_copyOf_0__K, _copyOf_0__V]) -> ImmutableMultimap[_copyOf_0__K, _copyOf_0__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_1__K, _copyOf_1__V]]) -> ImmutableMultimap[_copyOf_1__K, _copyOf_1__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(multimap: Multimap[_copyOf_2__K, _copyOf_2__V]) -> 'ImmutableSetMultimap'[_copyOf_2__K, _copyOf_2__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_3__K, _copyOf_3__V]]) -> 'ImmutableSetMultimap'[_copyOf_3__K, _copyOf_3__V]: ...
    def entries(self) -> ImmutableSet[java.util.Map.Entry[_ImmutableSetMultimap__K, _ImmutableSetMultimap__V]]: ...
    _flatteningToImmutableSetMultimap__T = typing.TypeVar('_flatteningToImmutableSetMultimap__T')  # <T>
    _flatteningToImmutableSetMultimap__K = typing.TypeVar('_flatteningToImmutableSetMultimap__K')  # <K>
    _flatteningToImmutableSetMultimap__V = typing.TypeVar('_flatteningToImmutableSetMultimap__V')  # <V>
    @staticmethod
    def flatteningToImmutableSetMultimap(function: typing.Union[java.util.function.Function[_flatteningToImmutableSetMultimap__T, _flatteningToImmutableSetMultimap__K], typing.Callable[[_flatteningToImmutableSetMultimap__T], _flatteningToImmutableSetMultimap__K]], function2: typing.Union[java.util.function.Function[_flatteningToImmutableSetMultimap__T, java.util.stream.Stream[_flatteningToImmutableSetMultimap__V]], typing.Callable[[_flatteningToImmutableSetMultimap__T], java.util.stream.Stream[_flatteningToImmutableSetMultimap__V]]]) -> java.util.stream.Collector[_flatteningToImmutableSetMultimap__T, typing.Any, 'ImmutableSetMultimap'[_flatteningToImmutableSetMultimap__K, _flatteningToImmutableSetMultimap__V]]: ...
    def get(self, k: _ImmutableSetMultimap__K) -> ImmutableSet[_ImmutableSetMultimap__V]: ...
    def inverse(self) -> 'ImmutableSetMultimap'[_ImmutableSetMultimap__V, _ImmutableSetMultimap__K]: ...
    _of_0__K = typing.TypeVar('_of_0__K')  # <K>
    _of_0__V = typing.TypeVar('_of_0__V')  # <V>
    _of_1__K = typing.TypeVar('_of_1__K')  # <K>
    _of_1__V = typing.TypeVar('_of_1__V')  # <V>
    _of_2__K = typing.TypeVar('_of_2__K')  # <K>
    _of_2__V = typing.TypeVar('_of_2__V')  # <V>
    _of_3__K = typing.TypeVar('_of_3__K')  # <K>
    _of_3__V = typing.TypeVar('_of_3__V')  # <V>
    _of_4__K = typing.TypeVar('_of_4__K')  # <K>
    _of_4__V = typing.TypeVar('_of_4__V')  # <V>
    _of_5__K = typing.TypeVar('_of_5__K')  # <K>
    _of_5__V = typing.TypeVar('_of_5__V')  # <V>
    _of_6__K = typing.TypeVar('_of_6__K')  # <K>
    _of_6__V = typing.TypeVar('_of_6__V')  # <V>
    _of_7__K = typing.TypeVar('_of_7__K')  # <K>
    _of_7__V = typing.TypeVar('_of_7__V')  # <V>
    _of_8__K = typing.TypeVar('_of_8__K')  # <K>
    _of_8__V = typing.TypeVar('_of_8__V')  # <V>
    _of_9__K = typing.TypeVar('_of_9__K')  # <K>
    _of_9__V = typing.TypeVar('_of_9__V')  # <V>
    _of_10__K = typing.TypeVar('_of_10__K')  # <K>
    _of_10__V = typing.TypeVar('_of_10__V')  # <V>
    _of_11__K = typing.TypeVar('_of_11__K')  # <K>
    _of_11__V = typing.TypeVar('_of_11__V')  # <V>
    @typing.overload
    @staticmethod
    def of() -> ImmutableMultimap[_of_0__K, _of_0__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_1__K, v: _of_1__V) -> ImmutableMultimap[_of_1__K, _of_1__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_2__K, v: _of_2__V, k2: _of_2__K, v2: _of_2__V) -> ImmutableMultimap[_of_2__K, _of_2__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_3__K, v: _of_3__V, k2: _of_3__K, v2: _of_3__V, k3: _of_3__K, v3: _of_3__V) -> ImmutableMultimap[_of_3__K, _of_3__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_4__K, v: _of_4__V, k2: _of_4__K, v2: _of_4__V, k3: _of_4__K, v3: _of_4__V, k4: _of_4__K, v4: _of_4__V) -> ImmutableMultimap[_of_4__K, _of_4__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_5__K, v: _of_5__V, k2: _of_5__K, v2: _of_5__V, k3: _of_5__K, v3: _of_5__V, k4: _of_5__K, v4: _of_5__V, k5: _of_5__K, v5: _of_5__V) -> ImmutableMultimap[_of_5__K, _of_5__V]: ...
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableSetMultimap'[_of_6__K, _of_6__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_7__K, v: _of_7__V) -> 'ImmutableSetMultimap'[_of_7__K, _of_7__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_8__K, v: _of_8__V, k2: _of_8__K, v2: _of_8__V) -> 'ImmutableSetMultimap'[_of_8__K, _of_8__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_9__K, v: _of_9__V, k2: _of_9__K, v2: _of_9__V, k3: _of_9__K, v3: _of_9__V) -> 'ImmutableSetMultimap'[_of_9__K, _of_9__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_10__K, v: _of_10__V, k2: _of_10__K, v2: _of_10__V, k3: _of_10__K, v3: _of_10__V, k4: _of_10__K, v4: _of_10__V) -> 'ImmutableSetMultimap'[_of_10__K, _of_10__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_11__K, v: _of_11__V, k2: _of_11__K, v2: _of_11__V, k3: _of_11__K, v3: _of_11__V, k4: _of_11__K, v4: _of_11__V, k5: _of_11__K, v5: _of_11__V) -> 'ImmutableSetMultimap'[_of_11__K, _of_11__V]: ...
    def removeAll(self, object: typing.Any) -> ImmutableSet[_ImmutableSetMultimap__V]: ...
    def replaceValues(self, k: _ImmutableSetMultimap__K, iterable: java.lang.Iterable[_ImmutableSetMultimap__V]) -> ImmutableSet[_ImmutableSetMultimap__V]: ...
    _toImmutableSetMultimap__T = typing.TypeVar('_toImmutableSetMultimap__T')  # <T>
    _toImmutableSetMultimap__K = typing.TypeVar('_toImmutableSetMultimap__K')  # <K>
    _toImmutableSetMultimap__V = typing.TypeVar('_toImmutableSetMultimap__V')  # <V>
    @staticmethod
    def toImmutableSetMultimap(function: typing.Union[java.util.function.Function[_toImmutableSetMultimap__T, _toImmutableSetMultimap__K], typing.Callable[[_toImmutableSetMultimap__T], _toImmutableSetMultimap__K]], function2: typing.Union[java.util.function.Function[_toImmutableSetMultimap__T, _toImmutableSetMultimap__V], typing.Callable[[_toImmutableSetMultimap__T], _toImmutableSetMultimap__V]]) -> java.util.stream.Collector[_toImmutableSetMultimap__T, typing.Any, 'ImmutableSetMultimap'[_toImmutableSetMultimap__K, _toImmutableSetMultimap__V]]: ...
    class Builder(ImmutableMultimap.Builder[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V], typing.Generic[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]):
        def __init__(self): ...
        def build(self) -> 'ImmutableSetMultimap'[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]: ...
        def orderKeysBy(self, comparator: typing.Union[java.util.Comparator[_ImmutableSetMultimap__Builder__K], typing.Callable[[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__K], int]]) -> 'ImmutableSetMultimap.Builder'[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]: ...
        def orderValuesBy(self, comparator: typing.Union[java.util.Comparator[_ImmutableSetMultimap__Builder__V], typing.Callable[[_ImmutableSetMultimap__Builder__V, _ImmutableSetMultimap__Builder__V], int]]) -> 'ImmutableSetMultimap.Builder'[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]: ...
        @typing.overload
        def put(self, k: _ImmutableSetMultimap__Builder__K, v: _ImmutableSetMultimap__Builder__V) -> 'ImmutableSetMultimap.Builder'[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]: ...
        @typing.overload
        def put(self, entry: java.util.Map.Entry[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]) -> 'ImmutableSetMultimap.Builder'[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, multimap: Multimap[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]) -> 'ImmutableSetMultimap.Builder'[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, iterable: java.lang.Iterable[java.util.Map.Entry[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]]) -> 'ImmutableSetMultimap.Builder'[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, k: _ImmutableSetMultimap__Builder__K, iterable: java.lang.Iterable[_ImmutableSetMultimap__Builder__V]) -> 'ImmutableSetMultimap.Builder'[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]: ...
        @typing.overload
        def putAll(self, k: _ImmutableSetMultimap__Builder__K, vArray: typing.List[_ImmutableSetMultimap__Builder__V]) -> 'ImmutableSetMultimap.Builder'[_ImmutableSetMultimap__Builder__K, _ImmutableSetMultimap__Builder__V]: ...

_ImmutableSortedMap__Builder__K = typing.TypeVar('_ImmutableSortedMap__Builder__K')  # <K>
_ImmutableSortedMap__Builder__V = typing.TypeVar('_ImmutableSortedMap__Builder__V')  # <V>
_ImmutableSortedMap__K = typing.TypeVar('_ImmutableSortedMap__K')  # <K>
_ImmutableSortedMap__V = typing.TypeVar('_ImmutableSortedMap__V')  # <V>
class ImmutableSortedMap(com.google.common.collect.ImmutableSortedMapFauxverideShim[_ImmutableSortedMap__K, _ImmutableSortedMap__V], java.util.NavigableMap[_ImmutableSortedMap__K, _ImmutableSortedMap__V], typing.Generic[_ImmutableSortedMap__K, _ImmutableSortedMap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<K,V> extends :class:`~com.google.common.collect.ImmutableMap`<K,V> implements NavigableMap<K,V>
    
        A null whose contents will never change, with many other important properties detailed at
        :class:`~com.google.common.collect.ImmutableCollection`.
    
        **Warning:** as with any sorted collection, you are strongly advised not to use a null or null type whose comparison
        behavior is *inconsistent with equals*. That is, :code:`a.compareTo(b)` or :code:`comparator.compare(a, b)` should equal
        zero *if and only if* :code:`a.equals(b)`. If this advice is not followed, the resulting map will not correctly obey its
        specification.
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            2.0 (implements :code:`NavigableMap` since 12.0)
    
        Also see:
            :meth:`~serialized`
    """
    def ceilingEntry(self, k: _ImmutableSortedMap__K) -> java.util.Map.Entry[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    def ceilingKey(self, k: _ImmutableSortedMap__K) -> _ImmutableSortedMap__K: ...
    def comparator(self) -> java.util.Comparator[_ImmutableSortedMap__K]: ...
    _copyOf_0__K = typing.TypeVar('_copyOf_0__K')  # <K>
    _copyOf_0__V = typing.TypeVar('_copyOf_0__V')  # <V>
    _copyOf_1__K = typing.TypeVar('_copyOf_1__K')  # <K>
    _copyOf_1__V = typing.TypeVar('_copyOf_1__V')  # <V>
    _copyOf_2__K = typing.TypeVar('_copyOf_2__K')  # <K>
    _copyOf_2__V = typing.TypeVar('_copyOf_2__V')  # <V>
    _copyOf_3__K = typing.TypeVar('_copyOf_3__K')  # <K>
    _copyOf_3__V = typing.TypeVar('_copyOf_3__V')  # <V>
    _copyOf_4__K = typing.TypeVar('_copyOf_4__K')  # <K>
    _copyOf_4__V = typing.TypeVar('_copyOf_4__V')  # <V>
    _copyOf_5__K = typing.TypeVar('_copyOf_5__K')  # <K>
    _copyOf_5__V = typing.TypeVar('_copyOf_5__V')  # <V>
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_0__K, _copyOf_0__V]]) -> ImmutableMap[_copyOf_0__K, _copyOf_0__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(map: typing.Union[java.util.Map[_copyOf_1__K, _copyOf_1__V], typing.Mapping[_copyOf_1__K, _copyOf_1__V]]) -> ImmutableMap[_copyOf_1__K, _copyOf_1__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_2__K, _copyOf_2__V]]) -> 'ImmutableSortedMap'[_copyOf_2__K, _copyOf_2__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[java.util.Map.Entry[_copyOf_3__K, _copyOf_3__V]], comparator: typing.Union[java.util.Comparator[_copyOf_3__K], typing.Callable[[_copyOf_3__K, _copyOf_3__K], int]]) -> 'ImmutableSortedMap'[_copyOf_3__K, _copyOf_3__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(map: typing.Union[java.util.Map[_copyOf_4__K, _copyOf_4__V], typing.Mapping[_copyOf_4__K, _copyOf_4__V]]) -> 'ImmutableSortedMap'[_copyOf_4__K, _copyOf_4__V]: ...
    @typing.overload
    @staticmethod
    def copyOf(map: typing.Union[java.util.Map[_copyOf_5__K, _copyOf_5__V], typing.Mapping[_copyOf_5__K, _copyOf_5__V]], comparator: typing.Union[java.util.Comparator[_copyOf_5__K], typing.Callable[[_copyOf_5__K, _copyOf_5__K], int]]) -> 'ImmutableSortedMap'[_copyOf_5__K, _copyOf_5__V]: ...
    _copyOfSorted__K = typing.TypeVar('_copyOfSorted__K')  # <K>
    _copyOfSorted__V = typing.TypeVar('_copyOfSorted__V')  # <V>
    @staticmethod
    def copyOfSorted(sortedMap: java.util.SortedMap[_copyOfSorted__K, _copyOfSorted__V]) -> 'ImmutableSortedMap'[_copyOfSorted__K, _copyOfSorted__V]: ...
    def descendingKeySet(self) -> 'ImmutableSortedSet'[_ImmutableSortedMap__K]: ...
    def descendingMap(self) -> 'ImmutableSortedMap'[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    def entrySet(self) -> ImmutableSet[java.util.Map.Entry[_ImmutableSortedMap__K, _ImmutableSortedMap__V]]: ...
    def firstEntry(self) -> java.util.Map.Entry[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    def firstKey(self) -> _ImmutableSortedMap__K: ...
    def floorEntry(self, k: _ImmutableSortedMap__K) -> java.util.Map.Entry[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    def floorKey(self, k: _ImmutableSortedMap__K) -> _ImmutableSortedMap__K: ...
    def forEach(self, biConsumer: typing.Union[java.util.function.BiConsumer[_ImmutableSortedMap__K, _ImmutableSortedMap__V], typing.Callable[[_ImmutableSortedMap__K, _ImmutableSortedMap__V], None]]) -> None: ...
    def get(self, object: typing.Any) -> _ImmutableSortedMap__V: ...
    @typing.overload
    def headMap(self, k: _ImmutableSortedMap__K) -> 'ImmutableSortedMap'[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    @typing.overload
    def headMap(self, k: _ImmutableSortedMap__K, boolean: bool) -> 'ImmutableSortedMap'[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    def higherEntry(self, k: _ImmutableSortedMap__K) -> java.util.Map.Entry[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    def higherKey(self, k: _ImmutableSortedMap__K) -> _ImmutableSortedMap__K: ...
    def keySet(self) -> 'ImmutableSortedSet'[_ImmutableSortedMap__K]: ...
    def lastEntry(self) -> java.util.Map.Entry[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    def lastKey(self) -> _ImmutableSortedMap__K: ...
    def lowerEntry(self, k: _ImmutableSortedMap__K) -> java.util.Map.Entry[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    def lowerKey(self, k: _ImmutableSortedMap__K) -> _ImmutableSortedMap__K: ...
    _naturalOrder__K = typing.TypeVar('_naturalOrder__K', bound=java.lang.Comparable)  # <K>
    _naturalOrder__V = typing.TypeVar('_naturalOrder__V')  # <V>
    @staticmethod
    def naturalOrder() -> 'ImmutableSortedMap.Builder'[_naturalOrder__K, _naturalOrder__V]: ...
    def navigableKeySet(self) -> 'ImmutableSortedSet'[_ImmutableSortedMap__K]: ...
    _of_0__K = typing.TypeVar('_of_0__K')  # <K>
    _of_0__V = typing.TypeVar('_of_0__V')  # <V>
    _of_1__K = typing.TypeVar('_of_1__K')  # <K>
    _of_1__V = typing.TypeVar('_of_1__V')  # <V>
    _of_2__K = typing.TypeVar('_of_2__K')  # <K>
    _of_2__V = typing.TypeVar('_of_2__V')  # <V>
    _of_3__K = typing.TypeVar('_of_3__K')  # <K>
    _of_3__V = typing.TypeVar('_of_3__V')  # <V>
    _of_4__K = typing.TypeVar('_of_4__K')  # <K>
    _of_4__V = typing.TypeVar('_of_4__V')  # <V>
    _of_5__K = typing.TypeVar('_of_5__K')  # <K>
    _of_5__V = typing.TypeVar('_of_5__V')  # <V>
    _of_6__K = typing.TypeVar('_of_6__K')  # <K>
    _of_6__V = typing.TypeVar('_of_6__V')  # <V>
    _of_7__K = typing.TypeVar('_of_7__K', bound=java.lang.Comparable)  # <K>
    _of_7__V = typing.TypeVar('_of_7__V')  # <V>
    _of_8__K = typing.TypeVar('_of_8__K', bound=java.lang.Comparable)  # <K>
    _of_8__V = typing.TypeVar('_of_8__V')  # <V>
    _of_9__K = typing.TypeVar('_of_9__K', bound=java.lang.Comparable)  # <K>
    _of_9__V = typing.TypeVar('_of_9__V')  # <V>
    _of_10__K = typing.TypeVar('_of_10__K', bound=java.lang.Comparable)  # <K>
    _of_10__V = typing.TypeVar('_of_10__V')  # <V>
    _of_11__K = typing.TypeVar('_of_11__K', bound=java.lang.Comparable)  # <K>
    _of_11__V = typing.TypeVar('_of_11__V')  # <V>
    _of_12__K = typing.TypeVar('_of_12__K')  # <K>
    _of_12__V = typing.TypeVar('_of_12__V')  # <V>
    _of_13__K = typing.TypeVar('_of_13__K')  # <K>
    _of_13__V = typing.TypeVar('_of_13__V')  # <V>
    _of_14__K = typing.TypeVar('_of_14__K')  # <K>
    _of_14__V = typing.TypeVar('_of_14__V')  # <V>
    _of_15__K = typing.TypeVar('_of_15__K')  # <K>
    _of_15__V = typing.TypeVar('_of_15__V')  # <V>
    _of_16__K = typing.TypeVar('_of_16__K')  # <K>
    _of_16__V = typing.TypeVar('_of_16__V')  # <V>
    @typing.overload
    @staticmethod
    def of() -> ImmutableMap[_of_0__K, _of_0__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_1__K, v: _of_1__V) -> ImmutableMap[_of_1__K, _of_1__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_2__K, v: _of_2__V, k2: _of_2__K, v2: _of_2__V) -> ImmutableMap[_of_2__K, _of_2__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_3__K, v: _of_3__V, k2: _of_3__K, v2: _of_3__V, k3: _of_3__K, v3: _of_3__V) -> ImmutableMap[_of_3__K, _of_3__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_4__K, v: _of_4__V, k2: _of_4__K, v2: _of_4__V, k3: _of_4__K, v3: _of_4__V, k4: _of_4__K, v4: _of_4__V) -> ImmutableMap[_of_4__K, _of_4__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_5__K, v: _of_5__V, k2: _of_5__K, v2: _of_5__V, k3: _of_5__K, v3: _of_5__V, k4: _of_5__K, v4: _of_5__V, k5: _of_5__K, v5: _of_5__V) -> ImmutableMap[_of_5__K, _of_5__V]: ...
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableSortedMap'[_of_6__K, _of_6__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_7__K, v: _of_7__V) -> 'ImmutableSortedMap'[_of_7__K, _of_7__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_8__K, v: _of_8__V, k2: _of_8__K, v2: _of_8__V) -> 'ImmutableSortedMap'[_of_8__K, _of_8__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_9__K, v: _of_9__V, k2: _of_9__K, v2: _of_9__V, k3: _of_9__K, v3: _of_9__V) -> 'ImmutableSortedMap'[_of_9__K, _of_9__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_10__K, v: _of_10__V, k2: _of_10__K, v2: _of_10__V, k3: _of_10__K, v3: _of_10__V, k4: _of_10__K, v4: _of_10__V) -> 'ImmutableSortedMap'[_of_10__K, _of_10__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_11__K, v: _of_11__V, k2: _of_11__K, v2: _of_11__V, k3: _of_11__K, v3: _of_11__V, k4: _of_11__K, v4: _of_11__V, k5: _of_11__K, v5: _of_11__V) -> 'ImmutableSortedMap'[_of_11__K, _of_11__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_12__K, v: _of_12__V) -> 'ImmutableSortedMap'[_of_12__K, _of_12__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_13__K, v: _of_13__V, k2: _of_13__K, v2: _of_13__V) -> 'ImmutableSortedMap'[_of_13__K, _of_13__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_14__K, v: _of_14__V, k2: _of_14__K, v2: _of_14__V, k3: _of_14__K, v3: _of_14__V) -> 'ImmutableSortedMap'[_of_14__K, _of_14__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_15__K, v: _of_15__V, k2: _of_15__K, v2: _of_15__V, k3: _of_15__K, v3: _of_15__V, k4: _of_15__K, v4: _of_15__V) -> 'ImmutableSortedMap'[_of_15__K, _of_15__V]: ...
    @typing.overload
    @staticmethod
    def of(k: _of_16__K, v: _of_16__V, k2: _of_16__K, v2: _of_16__V, k3: _of_16__K, v3: _of_16__V, k4: _of_16__K, v4: _of_16__V, k5: _of_16__K, v5: _of_16__V) -> 'ImmutableSortedMap'[_of_16__K, _of_16__V]: ...
    _orderedBy__K = typing.TypeVar('_orderedBy__K')  # <K>
    _orderedBy__V = typing.TypeVar('_orderedBy__V')  # <V>
    @staticmethod
    def orderedBy(comparator: typing.Union[java.util.Comparator[_orderedBy__K], typing.Callable[[_orderedBy__K, _orderedBy__K], int]]) -> 'ImmutableSortedMap.Builder'[_orderedBy__K, _orderedBy__V]: ...
    def pollFirstEntry(self) -> java.util.Map.Entry[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    def pollLastEntry(self) -> java.util.Map.Entry[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    _reverseOrder__K = typing.TypeVar('_reverseOrder__K', bound=java.lang.Comparable)  # <K>
    _reverseOrder__V = typing.TypeVar('_reverseOrder__V')  # <V>
    @staticmethod
    def reverseOrder() -> 'ImmutableSortedMap.Builder'[_reverseOrder__K, _reverseOrder__V]: ...
    def size(self) -> int: ...
    @typing.overload
    def subMap(self, k: _ImmutableSortedMap__K, boolean: bool, k2: _ImmutableSortedMap__K, boolean2: bool) -> 'ImmutableSortedMap'[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    @typing.overload
    def subMap(self, k: _ImmutableSortedMap__K, k2: _ImmutableSortedMap__K) -> 'ImmutableSortedMap'[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    @typing.overload
    def tailMap(self, k: _ImmutableSortedMap__K) -> 'ImmutableSortedMap'[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    @typing.overload
    def tailMap(self, k: _ImmutableSortedMap__K, boolean: bool) -> 'ImmutableSortedMap'[_ImmutableSortedMap__K, _ImmutableSortedMap__V]: ...
    _toImmutableSortedMap_0__T = typing.TypeVar('_toImmutableSortedMap_0__T')  # <T>
    _toImmutableSortedMap_0__K = typing.TypeVar('_toImmutableSortedMap_0__K')  # <K>
    _toImmutableSortedMap_0__V = typing.TypeVar('_toImmutableSortedMap_0__V')  # <V>
    _toImmutableSortedMap_1__T = typing.TypeVar('_toImmutableSortedMap_1__T')  # <T>
    _toImmutableSortedMap_1__K = typing.TypeVar('_toImmutableSortedMap_1__K')  # <K>
    _toImmutableSortedMap_1__V = typing.TypeVar('_toImmutableSortedMap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def toImmutableSortedMap(comparator: typing.Union[java.util.Comparator[_toImmutableSortedMap_0__K], typing.Callable[[_toImmutableSortedMap_0__K, _toImmutableSortedMap_0__K], int]], function: typing.Union[java.util.function.Function[_toImmutableSortedMap_0__T, _toImmutableSortedMap_0__K], typing.Callable[[_toImmutableSortedMap_0__T], _toImmutableSortedMap_0__K]], function2: typing.Union[java.util.function.Function[_toImmutableSortedMap_0__T, _toImmutableSortedMap_0__V], typing.Callable[[_toImmutableSortedMap_0__T], _toImmutableSortedMap_0__V]]) -> java.util.stream.Collector[_toImmutableSortedMap_0__T, typing.Any, 'ImmutableSortedMap'[_toImmutableSortedMap_0__K, _toImmutableSortedMap_0__V]]: ...
    @typing.overload
    @staticmethod
    def toImmutableSortedMap(comparator: typing.Union[java.util.Comparator[_toImmutableSortedMap_1__K], typing.Callable[[_toImmutableSortedMap_1__K, _toImmutableSortedMap_1__K], int]], function: typing.Union[java.util.function.Function[_toImmutableSortedMap_1__T, _toImmutableSortedMap_1__K], typing.Callable[[_toImmutableSortedMap_1__T], _toImmutableSortedMap_1__K]], function2: typing.Union[java.util.function.Function[_toImmutableSortedMap_1__T, _toImmutableSortedMap_1__V], typing.Callable[[_toImmutableSortedMap_1__T], _toImmutableSortedMap_1__V]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toImmutableSortedMap_1__V], typing.Callable]) -> java.util.stream.Collector[_toImmutableSortedMap_1__T, typing.Any, 'ImmutableSortedMap'[_toImmutableSortedMap_1__K, _toImmutableSortedMap_1__V]]: ...
    def values(self) -> ImmutableCollection[_ImmutableSortedMap__V]: ...
    class Builder(ImmutableMap.Builder[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V], typing.Generic[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V]):
        def __init__(self, comparator: typing.Union[java.util.Comparator[_ImmutableSortedMap__Builder__K], typing.Callable[[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__K], int]]): ...
        def build(self) -> 'ImmutableSortedMap'[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V]: ...
        def orderEntriesByValue(self, comparator: typing.Union[java.util.Comparator[_ImmutableSortedMap__Builder__V], typing.Callable[[_ImmutableSortedMap__Builder__V, _ImmutableSortedMap__Builder__V], int]]) -> 'ImmutableSortedMap.Builder'[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V]: ...
        @typing.overload
        def put(self, k: _ImmutableSortedMap__Builder__K, v: _ImmutableSortedMap__Builder__V) -> 'ImmutableSortedMap.Builder'[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V]: ...
        @typing.overload
        def put(self, entry: java.util.Map.Entry[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V]) -> 'ImmutableSortedMap.Builder'[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V]: ...
        @typing.overload
        def putAll(self, iterable: java.lang.Iterable[java.util.Map.Entry[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V]]) -> 'ImmutableSortedMap.Builder'[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V]: ...
        @typing.overload
        def putAll(self, map: typing.Union[java.util.Map[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V], typing.Mapping[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V]]) -> 'ImmutableSortedMap.Builder'[_ImmutableSortedMap__Builder__K, _ImmutableSortedMap__Builder__V]: ...

_ImmutableSortedMultiset__Builder__E = typing.TypeVar('_ImmutableSortedMultiset__Builder__E')  # <E>
_ImmutableSortedMultiset__E = typing.TypeVar('_ImmutableSortedMultiset__E')  # <E>
class ImmutableSortedMultiset(com.google.common.collect.ImmutableSortedMultisetFauxverideShim[_ImmutableSortedMultiset__E], com.google.common.collect.SortedMultiset[_ImmutableSortedMultiset__E], typing.Generic[_ImmutableSortedMultiset__E]):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ImmutableMultiset`<E> implements :class:`~com.google.common.collect.SortedMultiset`<E>
    
        A :class:`~com.google.common.collect.SortedMultiset` whose contents will never change, with many other important
        properties detailed at :class:`~com.google.common.collect.ImmutableCollection`.
    
        **Warning:** as with any sorted collection, you are strongly advised not to use a null or null type whose comparison
        behavior is *inconsistent with equals*. That is, :code:`a.compareTo(b)` or :code:`comparator.compare(a, b)` should equal
        zero *if and only if* :code:`a.equals(b)`. If this advice is not followed, the resulting collection will not correctly
        obey its specification.
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            12.0
    
        Also see:
            :meth:`~serialized`
    """
    def comparator(self) -> java.util.Comparator[_ImmutableSortedMultiset__E]: ...
    _copyOf_0__E = typing.TypeVar('_copyOf_0__E')  # <E>
    _copyOf_1__E = typing.TypeVar('_copyOf_1__E')  # <E>
    _copyOf_2__E = typing.TypeVar('_copyOf_2__E')  # <E>
    _copyOf_3__E = typing.TypeVar('_copyOf_3__E', bound=java.lang.Comparable)  # <E>
    _copyOf_4__E = typing.TypeVar('_copyOf_4__E')  # <E>
    _copyOf_5__E = typing.TypeVar('_copyOf_5__E')  # <E>
    _copyOf_6__E = typing.TypeVar('_copyOf_6__E')  # <E>
    _copyOf_7__E = typing.TypeVar('_copyOf_7__E')  # <E>
    _copyOf_8__E = typing.TypeVar('_copyOf_8__E')  # <E>
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[_copyOf_0__E]) -> ImmutableMultiset[_copyOf_0__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(eArray: typing.List[_copyOf_1__E]) -> ImmutableMultiset[_copyOf_1__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterator: java.util.Iterator[_copyOf_2__E]) -> ImmutableMultiset[_copyOf_2__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(eArray: typing.List[_copyOf_3__E]) -> 'ImmutableSortedMultiset'[_copyOf_3__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[_copyOf_4__E]) -> 'ImmutableSortedMultiset'[_copyOf_4__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(comparator: typing.Union[java.util.Comparator[_copyOf_5__E], typing.Callable[[_copyOf_5__E, _copyOf_5__E], int]], iterable: java.lang.Iterable[_copyOf_5__E]) -> 'ImmutableSortedMultiset'[_copyOf_5__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(comparator: typing.Union[java.util.Comparator[_copyOf_6__E], typing.Callable[[_copyOf_6__E, _copyOf_6__E], int]], iterator: java.util.Iterator[_copyOf_6__E]) -> 'ImmutableSortedMultiset'[_copyOf_6__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterator: java.util.Iterator[_copyOf_7__E]) -> 'ImmutableSortedMultiset'[_copyOf_7__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(eArray: typing.List[_copyOf_8__E]) -> 'ImmutableSortedMultiset'[_copyOf_8__E]: ...
    _copyOfSorted__E = typing.TypeVar('_copyOfSorted__E')  # <E>
    @staticmethod
    def copyOfSorted(sortedMultiset: 'SortedMultiset'[_copyOfSorted__E]) -> 'ImmutableSortedMultiset'[_copyOfSorted__E]: ...
    def descendingMultiset(self) -> 'ImmutableSortedMultiset'[_ImmutableSortedMultiset__E]: ...
    def elementSet(self) -> 'ImmutableSortedSet'[_ImmutableSortedMultiset__E]: ...
    def headMultiset(self, e: _ImmutableSortedMultiset__E, boundType: BoundType) -> 'ImmutableSortedMultiset'[_ImmutableSortedMultiset__E]: ...
    _naturalOrder__E = typing.TypeVar('_naturalOrder__E', bound=java.lang.Comparable)  # <E>
    @staticmethod
    def naturalOrder() -> 'ImmutableSortedMultiset.Builder'[_naturalOrder__E]: ...
    _of_0__E = typing.TypeVar('_of_0__E')  # <E>
    _of_1__E = typing.TypeVar('_of_1__E')  # <E>
    _of_2__E = typing.TypeVar('_of_2__E')  # <E>
    _of_3__E = typing.TypeVar('_of_3__E')  # <E>
    _of_4__E = typing.TypeVar('_of_4__E')  # <E>
    _of_5__E = typing.TypeVar('_of_5__E')  # <E>
    _of_6__E = typing.TypeVar('_of_6__E')  # <E>
    _of_7__E = typing.TypeVar('_of_7__E')  # <E>
    _of_8__E = typing.TypeVar('_of_8__E', bound=java.lang.Comparable)  # <E>
    _of_9__E = typing.TypeVar('_of_9__E', bound=java.lang.Comparable)  # <E>
    _of_10__E = typing.TypeVar('_of_10__E', bound=java.lang.Comparable)  # <E>
    _of_11__E = typing.TypeVar('_of_11__E', bound=java.lang.Comparable)  # <E>
    _of_12__E = typing.TypeVar('_of_12__E', bound=java.lang.Comparable)  # <E>
    _of_13__E = typing.TypeVar('_of_13__E', bound=java.lang.Comparable)  # <E>
    _of_14__E = typing.TypeVar('_of_14__E')  # <E>
    _of_15__E = typing.TypeVar('_of_15__E')  # <E>
    _of_16__E = typing.TypeVar('_of_16__E')  # <E>
    _of_17__E = typing.TypeVar('_of_17__E')  # <E>
    _of_18__E = typing.TypeVar('_of_18__E')  # <E>
    _of_19__E = typing.TypeVar('_of_19__E')  # <E>
    @typing.overload
    @staticmethod
    def of() -> ImmutableMultiset[_of_0__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_1__E) -> ImmutableMultiset[_of_1__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_2__E, e2: _of_2__E) -> ImmutableMultiset[_of_2__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_3__E, e2: _of_3__E, e3: _of_3__E) -> ImmutableMultiset[_of_3__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_4__E, e2: _of_4__E, e3: _of_4__E, e4: _of_4__E) -> ImmutableMultiset[_of_4__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_5__E, e2: _of_5__E, e3: _of_5__E, e4: _of_5__E, e5: _of_5__E) -> ImmutableMultiset[_of_5__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_6__E, e2: _of_6__E, e3: _of_6__E, e4: _of_6__E, e5: _of_6__E, e6: _of_6__E, eArray: typing.List[_of_6__E]) -> ImmutableMultiset[_of_6__E]: ...
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableSortedMultiset'[_of_7__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_8__E) -> 'ImmutableSortedMultiset'[_of_8__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_9__E, e2: _of_9__E) -> 'ImmutableSortedMultiset'[_of_9__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_10__E, e2: _of_10__E, e3: _of_10__E) -> 'ImmutableSortedMultiset'[_of_10__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_11__E, e2: _of_11__E, e3: _of_11__E, e4: _of_11__E) -> 'ImmutableSortedMultiset'[_of_11__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_12__E, e2: _of_12__E, e3: _of_12__E, e4: _of_12__E, e5: _of_12__E) -> 'ImmutableSortedMultiset'[_of_12__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_13__E, e2: _of_13__E, e3: _of_13__E, e4: _of_13__E, e5: _of_13__E, e6: _of_13__E, eArray: typing.List[_of_13__E]) -> 'ImmutableSortedMultiset'[_of_13__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_14__E) -> 'ImmutableSortedMultiset'[_of_14__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_15__E, e2: _of_15__E) -> 'ImmutableSortedMultiset'[_of_15__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_16__E, e2: _of_16__E, e3: _of_16__E) -> 'ImmutableSortedMultiset'[_of_16__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_17__E, e2: _of_17__E, e3: _of_17__E, e4: _of_17__E) -> 'ImmutableSortedMultiset'[_of_17__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_18__E, e2: _of_18__E, e3: _of_18__E, e4: _of_18__E, e5: _of_18__E) -> 'ImmutableSortedMultiset'[_of_18__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_19__E, e2: _of_19__E, e3: _of_19__E, e4: _of_19__E, e5: _of_19__E, e6: _of_19__E, eArray: typing.List[_of_19__E]) -> 'ImmutableSortedMultiset'[_of_19__E]: ...
    _orderedBy__E = typing.TypeVar('_orderedBy__E')  # <E>
    @staticmethod
    def orderedBy(comparator: typing.Union[java.util.Comparator[_orderedBy__E], typing.Callable[[_orderedBy__E, _orderedBy__E], int]]) -> 'ImmutableSortedMultiset.Builder'[_orderedBy__E]: ...
    def pollFirstEntry(self) -> Multiset.Entry[_ImmutableSortedMultiset__E]: ...
    def pollLastEntry(self) -> Multiset.Entry[_ImmutableSortedMultiset__E]: ...
    _reverseOrder__E = typing.TypeVar('_reverseOrder__E', bound=java.lang.Comparable)  # <E>
    @staticmethod
    def reverseOrder() -> 'ImmutableSortedMultiset.Builder'[_reverseOrder__E]: ...
    def subMultiset(self, e: _ImmutableSortedMultiset__E, boundType: BoundType, e2: _ImmutableSortedMultiset__E, boundType2: BoundType) -> 'ImmutableSortedMultiset'[_ImmutableSortedMultiset__E]: ...
    def tailMultiset(self, e: _ImmutableSortedMultiset__E, boundType: BoundType) -> 'ImmutableSortedMultiset'[_ImmutableSortedMultiset__E]: ...
    _toImmutableSortedMultiset_0__E = typing.TypeVar('_toImmutableSortedMultiset_0__E')  # <E>
    _toImmutableSortedMultiset_1__T = typing.TypeVar('_toImmutableSortedMultiset_1__T')  # <T>
    _toImmutableSortedMultiset_1__E = typing.TypeVar('_toImmutableSortedMultiset_1__E')  # <E>
    @typing.overload
    @staticmethod
    def toImmutableSortedMultiset(comparator: typing.Union[java.util.Comparator[_toImmutableSortedMultiset_0__E], typing.Callable[[_toImmutableSortedMultiset_0__E, _toImmutableSortedMultiset_0__E], int]]) -> java.util.stream.Collector[_toImmutableSortedMultiset_0__E, typing.Any, 'ImmutableSortedMultiset'[_toImmutableSortedMultiset_0__E]]: ...
    @typing.overload
    @staticmethod
    def toImmutableSortedMultiset(comparator: typing.Union[java.util.Comparator[_toImmutableSortedMultiset_1__E], typing.Callable[[_toImmutableSortedMultiset_1__E, _toImmutableSortedMultiset_1__E], int]], function: typing.Union[java.util.function.Function[_toImmutableSortedMultiset_1__T, _toImmutableSortedMultiset_1__E], typing.Callable[[_toImmutableSortedMultiset_1__T], _toImmutableSortedMultiset_1__E]], toIntFunction: typing.Union[java.util.function.ToIntFunction[_toImmutableSortedMultiset_1__T], typing.Callable[[_toImmutableSortedMultiset_1__T], int]]) -> java.util.stream.Collector[_toImmutableSortedMultiset_1__T, typing.Any, 'ImmutableSortedMultiset'[_toImmutableSortedMultiset_1__E]]: ...
    class Builder(ImmutableMultiset.Builder[_ImmutableSortedMultiset__Builder__E], typing.Generic[_ImmutableSortedMultiset__Builder__E]):
        def __init__(self, comparator: typing.Union[java.util.Comparator[_ImmutableSortedMultiset__Builder__E], typing.Callable[[_ImmutableSortedMultiset__Builder__E, _ImmutableSortedMultiset__Builder__E], int]]): ...
        @typing.overload
        def add(self, e: _ImmutableSortedMultiset__Builder__E) -> 'ImmutableSortedMultiset.Builder'[_ImmutableSortedMultiset__Builder__E]: ...
        @typing.overload
        def add(self, eArray: typing.List[_ImmutableSortedMultiset__Builder__E]) -> 'ImmutableSortedMultiset.Builder'[_ImmutableSortedMultiset__Builder__E]: ...
        @typing.overload
        def addAll(self, iterable: java.lang.Iterable[_ImmutableSortedMultiset__Builder__E]) -> 'ImmutableSortedMultiset.Builder'[_ImmutableSortedMultiset__Builder__E]: ...
        @typing.overload
        def addAll(self, iterator: java.util.Iterator[_ImmutableSortedMultiset__Builder__E]) -> 'ImmutableSortedMultiset.Builder'[_ImmutableSortedMultiset__Builder__E]: ...
        def addCopies(self, e: _ImmutableSortedMultiset__Builder__E, int: int) -> 'ImmutableSortedMultiset.Builder'[_ImmutableSortedMultiset__Builder__E]: ...
        def build(self) -> 'ImmutableSortedMultiset'[_ImmutableSortedMultiset__Builder__E]: ...
        def setCount(self, e: _ImmutableSortedMultiset__Builder__E, int: int) -> 'ImmutableSortedMultiset.Builder'[_ImmutableSortedMultiset__Builder__E]: ...

_ImmutableSortedSet__Builder__E = typing.TypeVar('_ImmutableSortedSet__Builder__E')  # <E>
_ImmutableSortedSet__E = typing.TypeVar('_ImmutableSortedSet__E')  # <E>
class ImmutableSortedSet(com.google.common.collect.ImmutableSortedSetFauxverideShim[_ImmutableSortedSet__E], java.util.NavigableSet[_ImmutableSortedSet__E], com.google.common.collect.SortedIterable[_ImmutableSortedSet__E], typing.Generic[_ImmutableSortedSet__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src`<E> extends :class:`~com.google.common.collect.ImmutableSet`<E> implements NavigableSet<E>
    
        A null whose contents will never change, with many other important properties detailed at
        :class:`~com.google.common.collect.ImmutableCollection`.
    
        **Warning:** as with any sorted collection, you are strongly advised not to use a null or null type whose comparison
        behavior is *inconsistent with equals*. That is, :code:`a.compareTo(b)` or :code:`comparator.compare(a, b)` should equal
        zero *if and only if* :code:`a.equals(b)`. If this advice is not followed, the resulting collection will not correctly
        obey its specification.
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            2.0 (implements :code:`NavigableSet` since 12.0)
    
        Also see:
            :meth:`~serialized`
    """
    def ceiling(self, e: _ImmutableSortedSet__E) -> _ImmutableSortedSet__E: ...
    def comparator(self) -> java.util.Comparator[_ImmutableSortedSet__E]: ...
    _copyOf_0__E = typing.TypeVar('_copyOf_0__E')  # <E>
    _copyOf_1__E = typing.TypeVar('_copyOf_1__E')  # <E>
    _copyOf_2__E = typing.TypeVar('_copyOf_2__E')  # <E>
    _copyOf_3__E = typing.TypeVar('_copyOf_3__E')  # <E>
    _copyOf_4__E = typing.TypeVar('_copyOf_4__E', bound=java.lang.Comparable)  # <E>
    _copyOf_5__E = typing.TypeVar('_copyOf_5__E')  # <E>
    _copyOf_6__E = typing.TypeVar('_copyOf_6__E')  # <E>
    _copyOf_7__E = typing.TypeVar('_copyOf_7__E')  # <E>
    _copyOf_8__E = typing.TypeVar('_copyOf_8__E')  # <E>
    _copyOf_9__E = typing.TypeVar('_copyOf_9__E')  # <E>
    _copyOf_10__E = typing.TypeVar('_copyOf_10__E')  # <E>
    _copyOf_11__E = typing.TypeVar('_copyOf_11__E')  # <E>
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[_copyOf_0__E]) -> ImmutableSet[_copyOf_0__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(eArray: typing.List[_copyOf_1__E]) -> ImmutableSet[_copyOf_1__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(collection: typing.Union[java.util.Collection[_copyOf_2__E], typing.Sequence[_copyOf_2__E]]) -> ImmutableSet[_copyOf_2__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterator: java.util.Iterator[_copyOf_3__E]) -> ImmutableSet[_copyOf_3__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(eArray: typing.List[_copyOf_4__E]) -> 'ImmutableSortedSet'[_copyOf_4__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterable: java.lang.Iterable[_copyOf_5__E]) -> 'ImmutableSortedSet'[_copyOf_5__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(collection: typing.Union[java.util.Collection[_copyOf_6__E], typing.Sequence[_copyOf_6__E]]) -> 'ImmutableSortedSet'[_copyOf_6__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(comparator: typing.Union[java.util.Comparator[_copyOf_7__E], typing.Callable[[_copyOf_7__E, _copyOf_7__E], int]], iterable: java.lang.Iterable[_copyOf_7__E]) -> 'ImmutableSortedSet'[_copyOf_7__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(comparator: typing.Union[java.util.Comparator[_copyOf_8__E], typing.Callable[[_copyOf_8__E, _copyOf_8__E], int]], collection: typing.Union[java.util.Collection[_copyOf_8__E], typing.Sequence[_copyOf_8__E]]) -> 'ImmutableSortedSet'[_copyOf_8__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(comparator: typing.Union[java.util.Comparator[_copyOf_9__E], typing.Callable[[_copyOf_9__E, _copyOf_9__E], int]], iterator: java.util.Iterator[_copyOf_9__E]) -> 'ImmutableSortedSet'[_copyOf_9__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(iterator: java.util.Iterator[_copyOf_10__E]) -> 'ImmutableSortedSet'[_copyOf_10__E]: ...
    @typing.overload
    @staticmethod
    def copyOf(eArray: typing.List[_copyOf_11__E]) -> 'ImmutableSortedSet'[_copyOf_11__E]: ...
    _copyOfSorted__E = typing.TypeVar('_copyOfSorted__E')  # <E>
    @staticmethod
    def copyOfSorted(sortedSet: java.util.SortedSet[_copyOfSorted__E]) -> 'ImmutableSortedSet'[_copyOfSorted__E]: ...
    def descendingIterator(self) -> UnmodifiableIterator[_ImmutableSortedSet__E]: ...
    def descendingSet(self) -> 'ImmutableSortedSet'[_ImmutableSortedSet__E]: ...
    def first(self) -> _ImmutableSortedSet__E: ...
    def floor(self, e: _ImmutableSortedSet__E) -> _ImmutableSortedSet__E: ...
    @typing.overload
    def headSet(self, e: _ImmutableSortedSet__E) -> 'ImmutableSortedSet'[_ImmutableSortedSet__E]: ...
    @typing.overload
    def headSet(self, e: _ImmutableSortedSet__E, boolean: bool) -> 'ImmutableSortedSet'[_ImmutableSortedSet__E]: ...
    def higher(self, e: _ImmutableSortedSet__E) -> _ImmutableSortedSet__E: ...
    def iterator(self) -> UnmodifiableIterator[_ImmutableSortedSet__E]: ...
    def last(self) -> _ImmutableSortedSet__E: ...
    def lower(self, e: _ImmutableSortedSet__E) -> _ImmutableSortedSet__E: ...
    _naturalOrder__E = typing.TypeVar('_naturalOrder__E', bound=java.lang.Comparable)  # <E>
    @staticmethod
    def naturalOrder() -> 'ImmutableSortedSet.Builder'[_naturalOrder__E]: ...
    _of_0__E = typing.TypeVar('_of_0__E')  # <E>
    _of_1__E = typing.TypeVar('_of_1__E')  # <E>
    _of_2__E = typing.TypeVar('_of_2__E')  # <E>
    _of_3__E = typing.TypeVar('_of_3__E')  # <E>
    _of_4__E = typing.TypeVar('_of_4__E')  # <E>
    _of_5__E = typing.TypeVar('_of_5__E')  # <E>
    _of_6__E = typing.TypeVar('_of_6__E')  # <E>
    _of_7__E = typing.TypeVar('_of_7__E')  # <E>
    _of_8__E = typing.TypeVar('_of_8__E', bound=java.lang.Comparable)  # <E>
    _of_9__E = typing.TypeVar('_of_9__E', bound=java.lang.Comparable)  # <E>
    _of_10__E = typing.TypeVar('_of_10__E', bound=java.lang.Comparable)  # <E>
    _of_11__E = typing.TypeVar('_of_11__E', bound=java.lang.Comparable)  # <E>
    _of_12__E = typing.TypeVar('_of_12__E', bound=java.lang.Comparable)  # <E>
    _of_13__E = typing.TypeVar('_of_13__E', bound=java.lang.Comparable)  # <E>
    _of_14__E = typing.TypeVar('_of_14__E')  # <E>
    _of_15__E = typing.TypeVar('_of_15__E')  # <E>
    _of_16__E = typing.TypeVar('_of_16__E')  # <E>
    _of_17__E = typing.TypeVar('_of_17__E')  # <E>
    _of_18__E = typing.TypeVar('_of_18__E')  # <E>
    _of_19__E = typing.TypeVar('_of_19__E')  # <E>
    @typing.overload
    @staticmethod
    def of() -> ImmutableSet[_of_0__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_1__E) -> ImmutableSet[_of_1__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_2__E, e2: _of_2__E) -> ImmutableSet[_of_2__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_3__E, e2: _of_3__E, e3: _of_3__E) -> ImmutableSet[_of_3__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_4__E, e2: _of_4__E, e3: _of_4__E, e4: _of_4__E) -> ImmutableSet[_of_4__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_5__E, e2: _of_5__E, e3: _of_5__E, e4: _of_5__E, e5: _of_5__E) -> ImmutableSet[_of_5__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_6__E, e2: _of_6__E, e3: _of_6__E, e4: _of_6__E, e5: _of_6__E, e6: _of_6__E, eArray: typing.List[_of_6__E]) -> ImmutableSet[_of_6__E]: ...
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableSortedSet'[_of_7__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_8__E) -> 'ImmutableSortedSet'[_of_8__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_9__E, e2: _of_9__E) -> 'ImmutableSortedSet'[_of_9__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_10__E, e2: _of_10__E, e3: _of_10__E) -> 'ImmutableSortedSet'[_of_10__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_11__E, e2: _of_11__E, e3: _of_11__E, e4: _of_11__E) -> 'ImmutableSortedSet'[_of_11__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_12__E, e2: _of_12__E, e3: _of_12__E, e4: _of_12__E, e5: _of_12__E) -> 'ImmutableSortedSet'[_of_12__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_13__E, e2: _of_13__E, e3: _of_13__E, e4: _of_13__E, e5: _of_13__E, e6: _of_13__E, eArray: typing.List[_of_13__E]) -> 'ImmutableSortedSet'[_of_13__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_14__E) -> 'ImmutableSortedSet'[_of_14__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_15__E, e2: _of_15__E) -> 'ImmutableSortedSet'[_of_15__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_16__E, e2: _of_16__E, e3: _of_16__E) -> 'ImmutableSortedSet'[_of_16__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_17__E, e2: _of_17__E, e3: _of_17__E, e4: _of_17__E) -> 'ImmutableSortedSet'[_of_17__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_18__E, e2: _of_18__E, e3: _of_18__E, e4: _of_18__E, e5: _of_18__E) -> 'ImmutableSortedSet'[_of_18__E]: ...
    @typing.overload
    @staticmethod
    def of(e: _of_19__E, e2: _of_19__E, e3: _of_19__E, e4: _of_19__E, e5: _of_19__E, e6: _of_19__E, eArray: typing.List[_of_19__E]) -> 'ImmutableSortedSet'[_of_19__E]: ...
    _orderedBy__E = typing.TypeVar('_orderedBy__E')  # <E>
    @staticmethod
    def orderedBy(comparator: typing.Union[java.util.Comparator[_orderedBy__E], typing.Callable[[_orderedBy__E, _orderedBy__E], int]]) -> 'ImmutableSortedSet.Builder'[_orderedBy__E]: ...
    def pollFirst(self) -> _ImmutableSortedSet__E: ...
    def pollLast(self) -> _ImmutableSortedSet__E: ...
    _reverseOrder__E = typing.TypeVar('_reverseOrder__E', bound=java.lang.Comparable)  # <E>
    @staticmethod
    def reverseOrder() -> 'ImmutableSortedSet.Builder'[_reverseOrder__E]: ...
    def spliterator(self) -> java.util.Spliterator[_ImmutableSortedSet__E]: ...
    @typing.overload
    def subSet(self, e: _ImmutableSortedSet__E, boolean: bool, e2: _ImmutableSortedSet__E, boolean2: bool) -> 'ImmutableSortedSet'[_ImmutableSortedSet__E]: ...
    @typing.overload
    def subSet(self, e: _ImmutableSortedSet__E, e2: _ImmutableSortedSet__E) -> 'ImmutableSortedSet'[_ImmutableSortedSet__E]: ...
    @typing.overload
    def tailSet(self, e: _ImmutableSortedSet__E) -> 'ImmutableSortedSet'[_ImmutableSortedSet__E]: ...
    @typing.overload
    def tailSet(self, e: _ImmutableSortedSet__E, boolean: bool) -> 'ImmutableSortedSet'[_ImmutableSortedSet__E]: ...
    _toImmutableSortedSet__E = typing.TypeVar('_toImmutableSortedSet__E')  # <E>
    @staticmethod
    def toImmutableSortedSet(comparator: typing.Union[java.util.Comparator[_toImmutableSortedSet__E], typing.Callable[[_toImmutableSortedSet__E, _toImmutableSortedSet__E], int]]) -> java.util.stream.Collector[_toImmutableSortedSet__E, typing.Any, 'ImmutableSortedSet'[_toImmutableSortedSet__E]]: ...
    class Builder(ImmutableSet.Builder[_ImmutableSortedSet__Builder__E], typing.Generic[_ImmutableSortedSet__Builder__E]):
        def __init__(self, comparator: typing.Union[java.util.Comparator[_ImmutableSortedSet__Builder__E], typing.Callable[[_ImmutableSortedSet__Builder__E, _ImmutableSortedSet__Builder__E], int]]): ...
        @typing.overload
        def add(self, e: _ImmutableSortedSet__Builder__E) -> 'ImmutableSortedSet.Builder'[_ImmutableSortedSet__Builder__E]: ...
        @typing.overload
        def add(self, eArray: typing.List[_ImmutableSortedSet__Builder__E]) -> 'ImmutableSortedSet.Builder'[_ImmutableSortedSet__Builder__E]: ...
        @typing.overload
        def addAll(self, iterable: java.lang.Iterable[_ImmutableSortedSet__Builder__E]) -> 'ImmutableSortedSet.Builder'[_ImmutableSortedSet__Builder__E]: ...
        @typing.overload
        def addAll(self, iterator: java.util.Iterator[_ImmutableSortedSet__Builder__E]) -> 'ImmutableSortedSet.Builder'[_ImmutableSortedSet__Builder__E]: ...
        def build(self) -> 'ImmutableSortedSet'[_ImmutableSortedSet__Builder__E]: ...

_ImmutableTable__Builder__R = typing.TypeVar('_ImmutableTable__Builder__R')  # <R>
_ImmutableTable__Builder__C = typing.TypeVar('_ImmutableTable__Builder__C')  # <C>
_ImmutableTable__Builder__V = typing.TypeVar('_ImmutableTable__Builder__V')  # <V>
_ImmutableTable__R = typing.TypeVar('_ImmutableTable__R')  # <R>
_ImmutableTable__C = typing.TypeVar('_ImmutableTable__C')  # <C>
_ImmutableTable__V = typing.TypeVar('_ImmutableTable__V')  # <V>
class ImmutableTable(com.google.common.collect.AbstractTable[_ImmutableTable__R, _ImmutableTable__C, _ImmutableTable__V], java.io.Serializable, typing.Generic[_ImmutableTable__R, _ImmutableTable__C, _ImmutableTable__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<R,C,V> extends Object implements Serializable
    
        A :class:`~com.google.common.collect.Table` whose contents will never change, with many other important properties
        detailed at :class:`~com.google.common.collect.ImmutableCollection`.
    
        See the Guava User Guide article on immutable collections.
    
        Since:
            11.0
    
        Also see:
            :meth:`~serialized`
    """
    _builder__R = typing.TypeVar('_builder__R')  # <R>
    _builder__C = typing.TypeVar('_builder__C')  # <C>
    _builder__V = typing.TypeVar('_builder__V')  # <V>
    @staticmethod
    def builder() -> 'ImmutableTable.Builder'[_builder__R, _builder__C, _builder__V]: ...
    def cellSet(self) -> ImmutableSet[Table.Cell[_ImmutableTable__R, _ImmutableTable__C, _ImmutableTable__V]]: ...
    def clear(self) -> None: ...
    def column(self, c: _ImmutableTable__C) -> ImmutableMap[_ImmutableTable__R, _ImmutableTable__V]: ...
    def columnKeySet(self) -> ImmutableSet[_ImmutableTable__C]: ...
    def columnMap(self) -> ImmutableMap[_ImmutableTable__C, java.util.Map[_ImmutableTable__R, _ImmutableTable__V]]: ...
    def contains(self, object: typing.Any, object2: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    _copyOf__R = typing.TypeVar('_copyOf__R')  # <R>
    _copyOf__C = typing.TypeVar('_copyOf__C')  # <C>
    _copyOf__V = typing.TypeVar('_copyOf__V')  # <V>
    @staticmethod
    def copyOf(table: Table[_copyOf__R, _copyOf__C, _copyOf__V]) -> 'ImmutableTable'[_copyOf__R, _copyOf__C, _copyOf__V]: ...
    _of_0__R = typing.TypeVar('_of_0__R')  # <R>
    _of_0__C = typing.TypeVar('_of_0__C')  # <C>
    _of_0__V = typing.TypeVar('_of_0__V')  # <V>
    _of_1__R = typing.TypeVar('_of_1__R')  # <R>
    _of_1__C = typing.TypeVar('_of_1__C')  # <C>
    _of_1__V = typing.TypeVar('_of_1__V')  # <V>
    @typing.overload
    @staticmethod
    def of() -> 'ImmutableTable'[_of_0__R, _of_0__C, _of_0__V]: ...
    @typing.overload
    @staticmethod
    def of(r: _of_1__R, c: _of_1__C, v: _of_1__V) -> 'ImmutableTable'[_of_1__R, _of_1__C, _of_1__V]: ...
    def put(self, r: _ImmutableTable__R, c: _ImmutableTable__C, v: _ImmutableTable__V) -> _ImmutableTable__V: ...
    def putAll(self, table: Table[_ImmutableTable__R, _ImmutableTable__C, _ImmutableTable__V]) -> None: ...
    def remove(self, object: typing.Any, object2: typing.Any) -> _ImmutableTable__V: ...
    def row(self, r: _ImmutableTable__R) -> ImmutableMap[_ImmutableTable__C, _ImmutableTable__V]: ...
    def rowKeySet(self) -> ImmutableSet[_ImmutableTable__R]: ...
    def rowMap(self) -> ImmutableMap[_ImmutableTable__R, java.util.Map[_ImmutableTable__C, _ImmutableTable__V]]: ...
    _toImmutableTable_0__T = typing.TypeVar('_toImmutableTable_0__T')  # <T>
    _toImmutableTable_0__R = typing.TypeVar('_toImmutableTable_0__R')  # <R>
    _toImmutableTable_0__C = typing.TypeVar('_toImmutableTable_0__C')  # <C>
    _toImmutableTable_0__V = typing.TypeVar('_toImmutableTable_0__V')  # <V>
    _toImmutableTable_1__T = typing.TypeVar('_toImmutableTable_1__T')  # <T>
    _toImmutableTable_1__R = typing.TypeVar('_toImmutableTable_1__R')  # <R>
    _toImmutableTable_1__C = typing.TypeVar('_toImmutableTable_1__C')  # <C>
    _toImmutableTable_1__V = typing.TypeVar('_toImmutableTable_1__V')  # <V>
    @typing.overload
    @staticmethod
    def toImmutableTable(function: typing.Union[java.util.function.Function[_toImmutableTable_0__T, _toImmutableTable_0__R], typing.Callable[[_toImmutableTable_0__T], _toImmutableTable_0__R]], function2: typing.Union[java.util.function.Function[_toImmutableTable_0__T, _toImmutableTable_0__C], typing.Callable[[_toImmutableTable_0__T], _toImmutableTable_0__C]], function3: typing.Union[java.util.function.Function[_toImmutableTable_0__T, _toImmutableTable_0__V], typing.Callable[[_toImmutableTable_0__T], _toImmutableTable_0__V]]) -> java.util.stream.Collector[_toImmutableTable_0__T, typing.Any, 'ImmutableTable'[_toImmutableTable_0__R, _toImmutableTable_0__C, _toImmutableTable_0__V]]: ...
    @typing.overload
    @staticmethod
    def toImmutableTable(function: typing.Union[java.util.function.Function[_toImmutableTable_1__T, _toImmutableTable_1__R], typing.Callable[[_toImmutableTable_1__T], _toImmutableTable_1__R]], function2: typing.Union[java.util.function.Function[_toImmutableTable_1__T, _toImmutableTable_1__C], typing.Callable[[_toImmutableTable_1__T], _toImmutableTable_1__C]], function3: typing.Union[java.util.function.Function[_toImmutableTable_1__T, _toImmutableTable_1__V], typing.Callable[[_toImmutableTable_1__T], _toImmutableTable_1__V]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toImmutableTable_1__V], typing.Callable]) -> java.util.stream.Collector[_toImmutableTable_1__T, typing.Any, 'ImmutableTable'[_toImmutableTable_1__R, _toImmutableTable_1__C, _toImmutableTable_1__V]]: ...
    def values(self) -> ImmutableCollection[_ImmutableTable__V]: ...
    class Builder(typing.Generic[_ImmutableTable__Builder__R, _ImmutableTable__Builder__C, _ImmutableTable__Builder__V]):
        def __init__(self): ...
        def build(self) -> 'ImmutableTable'[_ImmutableTable__Builder__R, _ImmutableTable__Builder__C, _ImmutableTable__Builder__V]: ...
        def orderColumnsBy(self, comparator: typing.Union[java.util.Comparator[_ImmutableTable__Builder__C], typing.Callable[[_ImmutableTable__Builder__C, _ImmutableTable__Builder__C], int]]) -> 'ImmutableTable.Builder'[_ImmutableTable__Builder__R, _ImmutableTable__Builder__C, _ImmutableTable__Builder__V]: ...
        def orderRowsBy(self, comparator: typing.Union[java.util.Comparator[_ImmutableTable__Builder__R], typing.Callable[[_ImmutableTable__Builder__R, _ImmutableTable__Builder__R], int]]) -> 'ImmutableTable.Builder'[_ImmutableTable__Builder__R, _ImmutableTable__Builder__C, _ImmutableTable__Builder__V]: ...
        @typing.overload
        def put(self, cell: Table.Cell[_ImmutableTable__Builder__R, _ImmutableTable__Builder__C, _ImmutableTable__Builder__V]) -> 'ImmutableTable.Builder'[_ImmutableTable__Builder__R, _ImmutableTable__Builder__C, _ImmutableTable__Builder__V]: ...
        @typing.overload
        def put(self, r: _ImmutableTable__Builder__R, c: _ImmutableTable__Builder__C, v: _ImmutableTable__Builder__V) -> 'ImmutableTable.Builder'[_ImmutableTable__Builder__R, _ImmutableTable__Builder__C, _ImmutableTable__Builder__V]: ...
        def putAll(self, table: Table[_ImmutableTable__Builder__R, _ImmutableTable__Builder__C, _ImmutableTable__Builder__V]) -> 'ImmutableTable.Builder'[_ImmutableTable__Builder__R, _ImmutableTable__Builder__C, _ImmutableTable__Builder__V]: ...

_LinkedHashMultimap__K = typing.TypeVar('_LinkedHashMultimap__K')  # <K>
_LinkedHashMultimap__V = typing.TypeVar('_LinkedHashMultimap__V')  # <V>
class LinkedHashMultimap(com.google.common.collect.LinkedHashMultimapGwtSerializationDependencies[_LinkedHashMultimap__K, _LinkedHashMultimap__V], typing.Generic[_LinkedHashMultimap__K, _LinkedHashMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<K,V> extends Object
    
        Implementation of :code:`Multimap` that does not allow duplicate key-value entries and that returns collections whose
        iterators follow the ordering in which the data was added to the multimap.
    
        The collections returned by :code:`keySet`, :code:`keys`, and :code:`asMap` iterate through the keys in the order they
        were first added to the multimap. Similarly, :code:`get`, :code:`removeAll`, and :code:`replaceValues` return
        collections that iterate through the values in the order they were added. The collections generated by :code:`entries`
        and :code:`values` iterate across the key-value mappings in the order they were added to the multimap.
    
        The iteration ordering of the collections generated by :code:`keySet`, :code:`keys`, and :code:`asMap` has a few
        subtleties. As long as the set of keys remains unchanged, adding or removing mappings does not affect the key iteration
        order. However, if you remove all values associated with a key and then add the key back to the multimap, that key will
        come last in the key iteration order.
    
        The multimap does not store duplicate key-value pairs. Adding a new key-value pair equal to an existing key-value pair
        has no effect.
    
        Keys and values may be null. All optional multimap methods are supported, and all returned views are modifiable.
    
        This class is not threadsafe when any concurrent operations update the multimap. Concurrent read operations will work
        correctly. To allow concurrent update operations, wrap your multimap with a call to
        :meth:`~com.google.common.collect.Multimaps.synchronizedSetMultimap`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def clear(self) -> None: ...
    _create_0__K = typing.TypeVar('_create_0__K')  # <K>
    _create_0__V = typing.TypeVar('_create_0__V')  # <V>
    _create_1__K = typing.TypeVar('_create_1__K')  # <K>
    _create_1__V = typing.TypeVar('_create_1__V')  # <V>
    _create_2__K = typing.TypeVar('_create_2__K')  # <K>
    _create_2__V = typing.TypeVar('_create_2__V')  # <V>
    @typing.overload
    @staticmethod
    def create() -> 'LinkedHashMultimap'[_create_0__K, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(multimap: Multimap[_create_1__K, _create_1__V]) -> 'LinkedHashMultimap'[_create_1__K, _create_1__V]: ...
    @typing.overload
    @staticmethod
    def create(int: int, int2: int) -> 'LinkedHashMultimap'[_create_2__K, _create_2__V]: ...
    def entries(self) -> java.util.Set[java.util.Map.Entry[_LinkedHashMultimap__K, _LinkedHashMultimap__V]]: ...
    def keySet(self) -> java.util.Set[_LinkedHashMultimap__K]: ...
    def replaceValues(self, k: _LinkedHashMultimap__K, iterable: java.lang.Iterable[_LinkedHashMultimap__V]) -> java.util.Set[_LinkedHashMultimap__V]: ...
    def values(self) -> java.util.Collection[_LinkedHashMultimap__V]: ...

_LinkedHashMultiset__E = typing.TypeVar('_LinkedHashMultiset__E')  # <E>
class LinkedHashMultiset(com.google.common.collect.AbstractMapBasedMultiset[_LinkedHashMultiset__E], typing.Generic[_LinkedHashMultiset__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<E> extends AbstractCollection<E>
    
        A :code:`Multiset` implementation with predictable iteration order. Its iterator orders elements according to when the
        first occurrence of the element was added. When the multiset contains multiple instances of an element, those instances
        are consecutive in the iteration order. If all occurrences of an element are removed, after which that element is added
        to the multiset, the element will appear at the end of the iteration.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def add(self, e: _LinkedHashMultiset__E) -> bool: ...
    _create_0__E = typing.TypeVar('_create_0__E')  # <E>
    _create_1__E = typing.TypeVar('_create_1__E')  # <E>
    _create_2__E = typing.TypeVar('_create_2__E')  # <E>
    @typing.overload
    @staticmethod
    def create() -> 'LinkedHashMultiset'[_create_0__E]: ...
    @typing.overload
    @staticmethod
    def create(int: int) -> 'LinkedHashMultiset'[_create_1__E]: ...
    @typing.overload
    @staticmethod
    def create(iterable: java.lang.Iterable[_create_2__E]) -> 'LinkedHashMultiset'[_create_2__E]: ...
    def remove(self, object: typing.Any) -> bool: ...

_LinkedListMultimap__K = typing.TypeVar('_LinkedListMultimap__K')  # <K>
_LinkedListMultimap__V = typing.TypeVar('_LinkedListMultimap__V')  # <V>
class LinkedListMultimap(com.google.common.collect.AbstractMultimap[_LinkedListMultimap__K, _LinkedListMultimap__V], ListMultimap[_LinkedListMultimap__K, _LinkedListMultimap__V], java.io.Serializable, typing.Generic[_LinkedListMultimap__K, _LinkedListMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public class :meth:`~src`<K,V> extends Object implements :class:`~com.google.common.collect.ListMultimap`<K,V>, Serializable
    
        An implementation of :code:`ListMultimap` that supports deterministic iteration order for both keys and values. The
        iteration order is preserved across non-distinct key values. For example, for the following multimap definition:
    
        .. code-block: java
        
         Multimap<K, V> multimap = LinkedListMultimap.create();
         multimap.put(key1, foo);
         multimap.put(key2, bar);
         multimap.put(key1, baz);
         
        ... the iteration order for :meth:`~com.google.common.collect.LinkedListMultimap.keys` is :code:`[key1, key2, key1]`,
        and similarly for :meth:`~com.google.common.collect.LinkedListMultimap.entries`. Unlike
        :class:`~com.google.common.collect.LinkedHashMultimap`, the iteration order is kept consistent between keys, entries and
        values. For example, calling:
    
        .. code-block: java
        
         multimap.remove(key1, foo);
         
    
        changes the entries iteration order to :code:`[key2=bar, key1=baz]` and the key iteration order to :code:`[key2, key1]`.
        The :meth:`~com.google.common.collect.LinkedListMultimap.entries` iterator returns mutable map entries, and
        :meth:`~com.google.common.collect.LinkedListMultimap.replaceValues` attempts to preserve iteration order as much as
        possible.
    
        The collections returned by :meth:`~com.google.common.collect.LinkedListMultimap.keySet` and
        :meth:`~com.google.common.collect.LinkedListMultimap.asMap` iterate through the keys in the order they were first added
        to the multimap. Similarly, :meth:`~com.google.common.collect.LinkedListMultimap.get`,
        :meth:`~com.google.common.collect.LinkedListMultimap.removeAll`, and
        :meth:`~com.google.common.collect.LinkedListMultimap.replaceValues` return collections that iterate through the values
        in the order they were added. The collections generated by
        :meth:`~com.google.common.collect.LinkedListMultimap.entries`,
        :meth:`~com.google.common.collect.LinkedListMultimap.keys`, and
        :meth:`~com.google.common.collect.LinkedListMultimap.values` iterate across the key-value mappings in the order they
        were added to the multimap.
    
        The :meth:`~com.google.common.collect.LinkedListMultimap.values` and
        :meth:`~com.google.common.collect.LinkedListMultimap.entries` methods both return a :code:`List`, instead of the
        :code:`Collection` specified by the :class:`~com.google.common.collect.ListMultimap` interface.
    
        The methods :meth:`~com.google.common.collect.LinkedListMultimap.get`,
        :meth:`~com.google.common.collect.LinkedListMultimap.keySet`,
        :meth:`~com.google.common.collect.LinkedListMultimap.keys`,
        :meth:`~com.google.common.collect.LinkedListMultimap.values`,
        :meth:`~com.google.common.collect.LinkedListMultimap.entries`, and
        :meth:`~com.google.common.collect.LinkedListMultimap.asMap` return collections that are views of the multimap. If the
        multimap is modified while an iteration over any of those collections is in progress, except through the iterator's
        methods, the results of the iteration are undefined.
    
        Keys and values may be null. All optional multimap methods are supported, and all returned views are modifiable.
    
        This class is not threadsafe when any concurrent operations update the multimap. Concurrent read operations will work
        correctly. To allow concurrent update operations, wrap your multimap with a call to
        :meth:`~com.google.common.collect.Multimaps.synchronizedListMultimap`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def clear(self) -> None: ...
    def containsKey(self, object: typing.Any) -> bool: ...
    def containsValue(self, object: typing.Any) -> bool: ...
    _create_0__K = typing.TypeVar('_create_0__K')  # <K>
    _create_0__V = typing.TypeVar('_create_0__V')  # <V>
    _create_1__K = typing.TypeVar('_create_1__K')  # <K>
    _create_1__V = typing.TypeVar('_create_1__V')  # <V>
    _create_2__K = typing.TypeVar('_create_2__K')  # <K>
    _create_2__V = typing.TypeVar('_create_2__V')  # <V>
    @typing.overload
    @staticmethod
    def create() -> 'LinkedListMultimap'[_create_0__K, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(multimap: Multimap[_create_1__K, _create_1__V]) -> 'LinkedListMultimap'[_create_1__K, _create_1__V]: ...
    @typing.overload
    @staticmethod
    def create(int: int) -> 'LinkedListMultimap'[_create_2__K, _create_2__V]: ...
    def entries(self) -> java.util.List[java.util.Map.Entry[_LinkedListMultimap__K, _LinkedListMultimap__V]]: ...
    def get(self, k: _LinkedListMultimap__K) -> java.util.List[_LinkedListMultimap__V]: ...
    def isEmpty(self) -> bool: ...
    def put(self, k: _LinkedListMultimap__K, v: _LinkedListMultimap__V) -> bool: ...
    def removeAll(self, object: typing.Any) -> java.util.List[_LinkedListMultimap__V]: ...
    def replaceValues(self, k: _LinkedListMultimap__K, iterable: java.lang.Iterable[_LinkedListMultimap__V]) -> java.util.List[_LinkedListMultimap__V]: ...
    def size(self) -> int: ...
    def values(self) -> java.util.List[_LinkedListMultimap__V]: ...

_MultimapBuilder__ListMultimapBuilder__K0 = typing.TypeVar('_MultimapBuilder__ListMultimapBuilder__K0')  # <K0>
_MultimapBuilder__ListMultimapBuilder__V0 = typing.TypeVar('_MultimapBuilder__ListMultimapBuilder__V0')  # <V0>
_MultimapBuilder__MultimapBuilderWithKeys__K0 = typing.TypeVar('_MultimapBuilder__MultimapBuilderWithKeys__K0')  # <K0>
_MultimapBuilder__SetMultimapBuilder__K0 = typing.TypeVar('_MultimapBuilder__SetMultimapBuilder__K0')  # <K0>
_MultimapBuilder__SetMultimapBuilder__V0 = typing.TypeVar('_MultimapBuilder__SetMultimapBuilder__V0')  # <V0>
_MultimapBuilder__SortedSetMultimapBuilder__K0 = typing.TypeVar('_MultimapBuilder__SortedSetMultimapBuilder__K0')  # <K0>
_MultimapBuilder__SortedSetMultimapBuilder__V0 = typing.TypeVar('_MultimapBuilder__SortedSetMultimapBuilder__V0')  # <V0>
_MultimapBuilder__K0 = typing.TypeVar('_MultimapBuilder__K0')  # <K0>
_MultimapBuilder__V0 = typing.TypeVar('_MultimapBuilder__V0')  # <V0>
class MultimapBuilder(typing.Generic[_MultimapBuilder__K0, _MultimapBuilder__V0]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<K0,V0> extends Object
    
        A builder for a multimap implementation that allows customization of the backing map and value collection
        implementations used in a particular multimap.
    
        This can be used to easily configure multimap data structure implementations not provided explicitly in
        :code:`com.google.common.collect`, for example:
    
        .. code-block: java
        
         ListMultimap<String, Integer> treeListMultimap =
             MultimapBuilder.treeKeys().arrayListValues().build();
         SetMultimap<Integer, MyEnum> hashEnumMultimap =
             MultimapBuilder.hashKeys().enumSetValues(MyEnum.class).build();
         
    
        :code:`MultimapBuilder` instances are immutable. Invoking a configuration method has no effect on the receiving
        instance; you must store and use the new builder instance it returns instead.
    
        The generated multimaps are serializable if the key and value types are serializable, unless stated otherwise in one of
        the configuration methods.
    
        Since:
            16.0
    """
    _build_0__K = typing.TypeVar('_build_0__K')  # <K>
    _build_0__V = typing.TypeVar('_build_0__V')  # <V>
    _build_1__K = typing.TypeVar('_build_1__K')  # <K>
    _build_1__V = typing.TypeVar('_build_1__V')  # <V>
    @typing.overload
    def build(self) -> Multimap[_build_0__K, _build_0__V]: ...
    @typing.overload
    def build(self, multimap: Multimap[_build_1__K, _build_1__V]) -> Multimap[_build_1__K, _build_1__V]: ...
    _enumKeys__K0 = typing.TypeVar('_enumKeys__K0', bound=java.lang.Enum)  # <K0>
    @staticmethod
    def enumKeys(class_: typing.Type[_enumKeys__K0]) -> 'MultimapBuilder.MultimapBuilderWithKeys'[_enumKeys__K0]: ...
    @typing.overload
    @staticmethod
    def hashKeys() -> 'MultimapBuilder.MultimapBuilderWithKeys'[typing.Any]: ...
    @typing.overload
    @staticmethod
    def hashKeys(int: int) -> 'MultimapBuilder.MultimapBuilderWithKeys'[typing.Any]: ...
    @typing.overload
    @staticmethod
    def linkedHashKeys() -> 'MultimapBuilder.MultimapBuilderWithKeys'[typing.Any]: ...
    @typing.overload
    @staticmethod
    def linkedHashKeys(int: int) -> 'MultimapBuilder.MultimapBuilderWithKeys'[typing.Any]: ...
    _treeKeys_1__K0 = typing.TypeVar('_treeKeys_1__K0')  # <K0>
    @typing.overload
    @staticmethod
    def treeKeys() -> 'MultimapBuilder.MultimapBuilderWithKeys'[java.lang.Comparable]: ...
    @typing.overload
    @staticmethod
    def treeKeys(comparator: typing.Union[java.util.Comparator[_treeKeys_1__K0], typing.Callable[[_treeKeys_1__K0, _treeKeys_1__K0], int]]) -> 'MultimapBuilder.MultimapBuilderWithKeys'[_treeKeys_1__K0]: ...
    class ListMultimapBuilder(com.google.common.collect.MultimapBuilder[_MultimapBuilder__ListMultimapBuilder__K0, _MultimapBuilder__ListMultimapBuilder__V0], typing.Generic[_MultimapBuilder__ListMultimapBuilder__K0, _MultimapBuilder__ListMultimapBuilder__V0]):
        _build_0__K = typing.TypeVar('_build_0__K')  # <K>
        _build_0__V = typing.TypeVar('_build_0__V')  # <V>
        _build_1__K = typing.TypeVar('_build_1__K')  # <K>
        _build_1__V = typing.TypeVar('_build_1__V')  # <V>
        @typing.overload
        def build(self) -> ListMultimap[_build_0__K, _build_0__V]: ...
        @typing.overload
        def build(self, multimap: Multimap[_build_1__K, _build_1__V]) -> ListMultimap[_build_1__K, _build_1__V]: ...
    class MultimapBuilderWithKeys(typing.Generic[_MultimapBuilder__MultimapBuilderWithKeys__K0]):
        @typing.overload
        def arrayListValues(self) -> 'MultimapBuilder.ListMultimapBuilder'[_MultimapBuilder__MultimapBuilderWithKeys__K0, typing.Any]: ...
        @typing.overload
        def arrayListValues(self, int: int) -> 'MultimapBuilder.ListMultimapBuilder'[_MultimapBuilder__MultimapBuilderWithKeys__K0, typing.Any]: ...
        _enumSetValues__V0 = typing.TypeVar('_enumSetValues__V0', bound=java.lang.Enum)  # <V0>
        def enumSetValues(self, class_: typing.Type[_enumSetValues__V0]) -> 'MultimapBuilder.SetMultimapBuilder'[_MultimapBuilder__MultimapBuilderWithKeys__K0, _enumSetValues__V0]: ...
        @typing.overload
        def hashSetValues(self) -> 'MultimapBuilder.SetMultimapBuilder'[_MultimapBuilder__MultimapBuilderWithKeys__K0, typing.Any]: ...
        @typing.overload
        def hashSetValues(self, int: int) -> 'MultimapBuilder.SetMultimapBuilder'[_MultimapBuilder__MultimapBuilderWithKeys__K0, typing.Any]: ...
        @typing.overload
        def linkedHashSetValues(self) -> 'MultimapBuilder.SetMultimapBuilder'[_MultimapBuilder__MultimapBuilderWithKeys__K0, typing.Any]: ...
        @typing.overload
        def linkedHashSetValues(self, int: int) -> 'MultimapBuilder.SetMultimapBuilder'[_MultimapBuilder__MultimapBuilderWithKeys__K0, typing.Any]: ...
        def linkedListValues(self) -> 'MultimapBuilder.ListMultimapBuilder'[_MultimapBuilder__MultimapBuilderWithKeys__K0, typing.Any]: ...
        _treeSetValues_1__V0 = typing.TypeVar('_treeSetValues_1__V0')  # <V0>
        @typing.overload
        def treeSetValues(self) -> 'MultimapBuilder.SortedSetMultimapBuilder'[_MultimapBuilder__MultimapBuilderWithKeys__K0, java.lang.Comparable]: ...
        @typing.overload
        def treeSetValues(self, comparator: typing.Union[java.util.Comparator[_treeSetValues_1__V0], typing.Callable[[_treeSetValues_1__V0, _treeSetValues_1__V0], int]]) -> 'MultimapBuilder.SortedSetMultimapBuilder'[_MultimapBuilder__MultimapBuilderWithKeys__K0, _treeSetValues_1__V0]: ...
    class SetMultimapBuilder(com.google.common.collect.MultimapBuilder[_MultimapBuilder__SetMultimapBuilder__K0, _MultimapBuilder__SetMultimapBuilder__V0], typing.Generic[_MultimapBuilder__SetMultimapBuilder__K0, _MultimapBuilder__SetMultimapBuilder__V0]):
        _build_0__K = typing.TypeVar('_build_0__K')  # <K>
        _build_0__V = typing.TypeVar('_build_0__V')  # <V>
        _build_1__K = typing.TypeVar('_build_1__K')  # <K>
        _build_1__V = typing.TypeVar('_build_1__V')  # <V>
        @typing.overload
        def build(self) -> SetMultimap[_build_0__K, _build_0__V]: ...
        @typing.overload
        def build(self, multimap: Multimap[_build_1__K, _build_1__V]) -> SetMultimap[_build_1__K, _build_1__V]: ...
    class SortedSetMultimapBuilder(com.google.common.collect.MultimapBuilder.SetMultimapBuilder[_MultimapBuilder__SortedSetMultimapBuilder__K0, _MultimapBuilder__SortedSetMultimapBuilder__V0], typing.Generic[_MultimapBuilder__SortedSetMultimapBuilder__K0, _MultimapBuilder__SortedSetMultimapBuilder__V0]):
        _build_0__K = typing.TypeVar('_build_0__K')  # <K>
        _build_0__V = typing.TypeVar('_build_0__V')  # <V>
        _build_1__K = typing.TypeVar('_build_1__K')  # <K>
        _build_1__V = typing.TypeVar('_build_1__V')  # <V>
        @typing.overload
        def build(self) -> SortedSetMultimap[_build_0__K, _build_0__V]: ...
        @typing.overload
        def build(self, multimap: Multimap[_build_1__K, _build_1__V]) -> SortedSetMultimap[_build_1__K, _build_1__V]: ...

_Range__C = typing.TypeVar('_Range__C', bound=java.lang.Comparable)  # <C>
class Range(com.google.common.collect.RangeGwtSerializationDependencies, com.google.common.base.Predicate[_Range__C], java.io.Serializable, typing.Generic[_Range__C]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src`<C extends Comparable> extends Object implements :class:`~com.google.common.base.Predicate`<C>, Serializable
    
        A range (or "interval") defines the *boundaries* around a contiguous span of values of some :code:`Comparable` type; for
        example, "integers from 1 to 100 inclusive." Note that it is not possible to *iterate* over these contained values. To
        do so, pass this range instance and an appropriate :class:`~com.google.common.collect.DiscreteDomain` to
        :meth:`~com.google.common.collect.ContiguousSet.create`.
    
        Types of ranges
    ---------------
    
    
        Each end of the range may be bounded or unbounded. If bounded, there is an associated *endpoint* value, and the range is
        considered to be either *open* (does not include the endpoint) or *closed* (includes the endpoint) on that side. With
        three possibilities on each side, this yields nine basic types of ranges, enumerated below. (Notation: a square bracket
        (:code:`[ ]`) indicates that the range is closed on that side; a parenthesis (:code:`( )`) means it is either open or
        unbounded. The construct :code:`{x | statement}` is read "the set of all *x* such that *statement*.")
    
        When both endpoints exist, the upper endpoint may not be less than the lower. The endpoints may be equal only if at
        least one of the bounds is closed:
    
          - :code:`[a..a]` : a singleton range
          - :code:`[a..a); (a..a]` : :meth:`~com.google.common.collect.Range.isEmpty` ranges; also valid
          - :code:`(a..a)` : **invalid**; an exception will be thrown
    
    
        Warnings
    --------
    
    
          - Use immutable value types only, if at all possible. If you must use a mutable type, **do not** allow the endpoint
            instances to mutate after the range is created!
          - Your value type's comparison method should be consistent with equals if at all possible. Otherwise, be aware that
            concepts used throughout this documentation such as "equal", "same", "unique" and so on actually refer to whether null
            returns zero, not whether null returns :code:`true`.
          - A class which implements :code:`Comparable<UnrelatedType>` is very broken, and will cause undefined horrible things to
            happen in :code:`Range`. For now, the Range API does not prevent its use, because this would also rule out all
            ungenerified (pre-JDK1.5) data types. **This may change in the future.**
    
    
        Other notes
    -----------
    
    
          - Instances of this type are obtained using the static factory methods in this class.
          - Ranges are *convex*: whenever two values are contained, all values in between them must also be contained. More
            formally, for any :code:`c1 <= c2 <= c3` of type :code:`C`, :code:`r.contains(c1) &&amp; r.contains(c3)` implies
            :code:`r.contains(c2)`). This means that a :code:`Range<Integer>` can never be used to represent, say, "all *prime*
            numbers from 1 to 100."
          - When evaluated as a :class:`~com.google.common.base.Predicate`, a range yields the same result as invoking
            :meth:`~com.google.common.collect.Range.contains`.
          - Terminology note: a range :code:`a` is said to be the *maximal* range having property *P* if, for all ranges :code:`b`
            also having property *P*, :code:`a.encloses(b)`. Likewise, :code:`a` is *minimal* when :code:`b.encloses(a)` for all
            :code:`b` having property *P*. See, for example, the definition of
            :meth:`~com.google.common.collect.Range.intersection`.
    
    
        Further reading
    ---------------
    
    
        See the Guava User Guide article on null.
    
        Since:
            10.0
    
        Also see:
            :meth:`~serialized`
    """
    _all__C = typing.TypeVar('_all__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def all() -> 'Range'[_all__C]: ...
    def apply(self, c: _Range__C) -> bool: ...
    _atLeast__C = typing.TypeVar('_atLeast__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def atLeast(c: _atLeast__C) -> 'Range'[_atLeast__C]: ...
    _atMost__C = typing.TypeVar('_atMost__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def atMost(c: _atMost__C) -> 'Range'[_atMost__C]: ...
    def canonical(self, discreteDomain: DiscreteDomain[_Range__C]) -> 'Range'[_Range__C]: ...
    _closed__C = typing.TypeVar('_closed__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def closed(c: _closed__C, c2: _closed__C) -> 'Range'[_closed__C]: ...
    _closedOpen__C = typing.TypeVar('_closedOpen__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def closedOpen(c: _closedOpen__C, c2: _closedOpen__C) -> 'Range'[_closedOpen__C]: ...
    def contains(self, c: _Range__C) -> bool: ...
    def containsAll(self, iterable: java.lang.Iterable[_Range__C]) -> bool: ...
    _downTo__C = typing.TypeVar('_downTo__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def downTo(c: _downTo__C, boundType: BoundType) -> 'Range'[_downTo__C]: ...
    _encloseAll__C = typing.TypeVar('_encloseAll__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def encloseAll(iterable: java.lang.Iterable[_encloseAll__C]) -> 'Range'[_encloseAll__C]: ...
    def encloses(self, range: 'Range'[_Range__C]) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def gap(self, range: 'Range'[_Range__C]) -> 'Range'[_Range__C]: ...
    _greaterThan__C = typing.TypeVar('_greaterThan__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def greaterThan(c: _greaterThan__C) -> 'Range'[_greaterThan__C]: ...
    def hasLowerBound(self) -> bool: ...
    def hasUpperBound(self) -> bool: ...
    def hashCode(self) -> int: ...
    def intersection(self, range: 'Range'[_Range__C]) -> 'Range'[_Range__C]: ...
    def isConnected(self, range: 'Range'[_Range__C]) -> bool: ...
    def isEmpty(self) -> bool: ...
    _lessThan__C = typing.TypeVar('_lessThan__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def lessThan(c: _lessThan__C) -> 'Range'[_lessThan__C]: ...
    def lowerBoundType(self) -> BoundType: ...
    def lowerEndpoint(self) -> _Range__C: ...
    _open__C = typing.TypeVar('_open__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def open(c: _open__C, c2: _open__C) -> 'Range'[_open__C]: ...
    _openClosed__C = typing.TypeVar('_openClosed__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def openClosed(c: _openClosed__C, c2: _openClosed__C) -> 'Range'[_openClosed__C]: ...
    _range__C = typing.TypeVar('_range__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def range(c: _range__C, boundType: BoundType, c2: _range__C, boundType2: BoundType) -> 'Range'[_range__C]: ...
    _singleton__C = typing.TypeVar('_singleton__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def singleton(c: _singleton__C) -> 'Range'[_singleton__C]: ...
    def span(self, range: 'Range'[_Range__C]) -> 'Range'[_Range__C]: ...
    def toString(self) -> str: ...
    _upTo__C = typing.TypeVar('_upTo__C', bound=java.lang.Comparable)  # <C>
    @staticmethod
    def upTo(c: _upTo__C, boundType: BoundType) -> 'Range'[_upTo__C]: ...
    def upperBoundType(self) -> BoundType: ...
    def upperEndpoint(self) -> _Range__C: ...

_SortedMultiset__E = typing.TypeVar('_SortedMultiset__E')  # <E>
class SortedMultiset(com.google.common.collect.SortedMultisetBridge[_SortedMultiset__E], com.google.common.collect.SortedIterable[_SortedMultiset__E], typing.Generic[_SortedMultiset__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public interface :meth:`~src`<E>
    
        A :class:`~com.google.common.collect.Multiset` which maintains the ordering of its elements, according to either their
        natural order or an explicit null. This order is reflected when iterating over the sorted multiset, either directly, or
        through its :code:`elementSet` or :code:`entrySet` views. In all cases, this implementation uses null or null instead of
        null to determine equivalence of instances.
    
        **Warning:** The comparison must be *consistent with equals* as explained by the null class specification. Otherwise,
        the resulting multiset will violate the null contract, which is specified in terms of null.
    
        See the Guava User Guide article on null.
    
        Since:
            11.0
    """
    def comparator(self) -> java.util.Comparator[_SortedMultiset__E]: ...
    def descendingMultiset(self) -> 'SortedMultiset'[_SortedMultiset__E]: ...
    def elementSet(self) -> java.util.NavigableSet[_SortedMultiset__E]: ...
    def entrySet(self) -> java.util.Set[Multiset.Entry[_SortedMultiset__E]]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def firstEntry(self) -> Multiset.Entry[_SortedMultiset__E]: ...
    def hashCode(self) -> int: ...
    def headMultiset(self, e: _SortedMultiset__E, boundType: BoundType) -> 'SortedMultiset'[_SortedMultiset__E]: ...
    def iterator(self) -> java.util.Iterator[_SortedMultiset__E]: ...
    def lastEntry(self) -> Multiset.Entry[_SortedMultiset__E]: ...
    def pollFirstEntry(self) -> Multiset.Entry[_SortedMultiset__E]: ...
    def pollLastEntry(self) -> Multiset.Entry[_SortedMultiset__E]: ...
    def subMultiset(self, e: _SortedMultiset__E, boundType: BoundType, e2: _SortedMultiset__E, boundType2: BoundType) -> 'SortedMultiset'[_SortedMultiset__E]: ...
    def tailMultiset(self, e: _SortedMultiset__E, boundType: BoundType) -> 'SortedMultiset'[_SortedMultiset__E]: ...
    def toString(self) -> str: ...

_TreeBasedTable__R = typing.TypeVar('_TreeBasedTable__R')  # <R>
_TreeBasedTable__C = typing.TypeVar('_TreeBasedTable__C')  # <C>
_TreeBasedTable__V = typing.TypeVar('_TreeBasedTable__V')  # <V>
class TreeBasedTable(com.google.common.collect.StandardRowSortedTable[_TreeBasedTable__R, _TreeBasedTable__C, _TreeBasedTable__V], typing.Generic[_TreeBasedTable__R, _TreeBasedTable__C, _TreeBasedTable__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true) public class :meth:`~src`<R,C,V> extends Object
    
        Implementation of :code:`Table` whose row keys and column keys are ordered by their natural ordering or by supplied
        comparators. When constructing a :code:`TreeBasedTable`, you may provide comparators for the row keys and the column
        keys, or you may use natural ordering for both.
    
        The :meth:`~com.google.common.collect.TreeBasedTable.rowKeySet` method returns a null and the
        :meth:`~com.google.common.collect.TreeBasedTable.rowMap` method returns a null, instead of the null and null specified
        by the :class:`~com.google.common.collect.Table` interface.
    
        The views returned by :meth:`~com.google.common.collect.TreeBasedTable.column`,
        :meth:`~com.google.common.collect.TreeBasedTable.columnKeySet`, and
        :meth:`~com.google.common.collect.TreeBasedTable.columnMap` have iterators that don't support :code:`remove()`.
        Otherwise, all optional operations are supported. Null row keys, columns keys, and values are not supported.
    
        Lookups by row key are often faster than lookups by column key, because the data is stored in a :code:`Map<R, Map<C,
        V>>`. A method call like :code:`column(columnKey).get(rowKey)` still runs quickly, since the row key is provided.
        However, :code:`column(columnKey).size()` takes longer, since an iteration across all row keys occurs.
    
        Because a :code:`TreeBasedTable` has unique sorted values for a given row, both :code:`row(rowKey)` and
        :code:`rowMap().get(rowKey)` are null instances, instead of the null specified in the
        :class:`~com.google.common.collect.Table` interface.
    
        Note that this implementation is not synchronized. If multiple threads access this table concurrently and one of the
        threads modifies the table, it must be synchronized externally.
    
        See the Guava User Guide article on null.
    
        Since:
            7.0
    
        Also see:
            :meth:`~serialized`
    """
    def columnComparator(self) -> java.util.Comparator[_TreeBasedTable__C]: ...
    _create_0__R = typing.TypeVar('_create_0__R', bound=java.lang.Comparable)  # <R>
    _create_0__C = typing.TypeVar('_create_0__C', bound=java.lang.Comparable)  # <C>
    _create_0__V = typing.TypeVar('_create_0__V')  # <V>
    _create_1__R = typing.TypeVar('_create_1__R')  # <R>
    _create_1__C = typing.TypeVar('_create_1__C')  # <C>
    _create_1__V = typing.TypeVar('_create_1__V')  # <V>
    _create_2__R = typing.TypeVar('_create_2__R')  # <R>
    _create_2__C = typing.TypeVar('_create_2__C')  # <C>
    _create_2__V = typing.TypeVar('_create_2__V')  # <V>
    @typing.overload
    @staticmethod
    def create() -> 'TreeBasedTable'[_create_0__R, _create_0__C, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(treeBasedTable: 'TreeBasedTable'[_create_1__R, _create_1__C, _create_1__V]) -> 'TreeBasedTable'[_create_1__R, _create_1__C, _create_1__V]: ...
    @typing.overload
    @staticmethod
    def create(comparator: typing.Union[java.util.Comparator[_create_2__R], typing.Callable[[_create_2__R, _create_2__R], int]], comparator2: typing.Union[java.util.Comparator[_create_2__C], typing.Callable[[_create_2__C, _create_2__C], int]]) -> 'TreeBasedTable'[_create_2__R, _create_2__C, _create_2__V]: ...
    def row(self, r: _TreeBasedTable__R) -> java.util.SortedMap[_TreeBasedTable__C, _TreeBasedTable__V]: ...
    def rowComparator(self) -> java.util.Comparator[_TreeBasedTable__R]: ...
    def rowKeySet(self) -> java.util.SortedSet[_TreeBasedTable__R]: ...
    def rowMap(self) -> java.util.SortedMap[_TreeBasedTable__R, java.util.Map[_TreeBasedTable__C, _TreeBasedTable__V]]: ...

_TreeMultimap__K = typing.TypeVar('_TreeMultimap__K')  # <K>
_TreeMultimap__V = typing.TypeVar('_TreeMultimap__V')  # <V>
class TreeMultimap(com.google.common.collect.AbstractSortedKeySortedSetMultimap[_TreeMultimap__K, _TreeMultimap__V], typing.Generic[_TreeMultimap__K, _TreeMultimap__V]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true, :meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public class :meth:`~src`<K,V> extends Object
    
        Implementation of :code:`Multimap` whose keys and values are ordered by their natural ordering or by supplied
        comparators. In all cases, this implementation uses null or null instead of null to determine equivalence of instances.
    
        **Warning:** The comparators or comparables used must be *consistent with equals* as explained by the null class
        specification. Otherwise, the resulting multiset will violate the general contract of
        :class:`~com.google.common.collect.SetMultimap`, which is specified in terms of null.
    
        The collections returned by :code:`keySet` and :code:`asMap` iterate through the keys according to the key comparator
        ordering or the natural ordering of the keys. Similarly, :code:`get`, :code:`removeAll`, and :code:`replaceValues`
        return collections that iterate through the values according to the value comparator ordering or the natural ordering of
        the values. The collections generated by :code:`entries`, :code:`keys`, and :code:`values` iterate across the keys
        according to the above key ordering, and for each key they iterate across the values according to the value ordering.
    
        The multimap does not store duplicate key-value pairs. Adding a new key-value pair equal to an existing key-value pair
        has no effect.
    
        Null keys and values are permitted (provided, of course, that the respective comparators support them). All optional
        multimap methods are supported, and all returned views are modifiable.
    
        This class is not threadsafe when any concurrent operations update the multimap. Concurrent read operations will work
        correctly. To allow concurrent update operations, wrap your multimap with a call to
        :meth:`~com.google.common.collect.Multimaps.synchronizedSortedSetMultimap`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    def asMap(self) -> java.util.NavigableMap[_TreeMultimap__K, java.util.Collection[_TreeMultimap__V]]: ...
    _create_0__K = typing.TypeVar('_create_0__K', bound=java.lang.Comparable)  # <K>
    _create_0__V = typing.TypeVar('_create_0__V', bound=java.lang.Comparable)  # <V>
    _create_1__K = typing.TypeVar('_create_1__K', bound=java.lang.Comparable)  # <K>
    _create_1__V = typing.TypeVar('_create_1__V', bound=java.lang.Comparable)  # <V>
    _create_2__K = typing.TypeVar('_create_2__K')  # <K>
    _create_2__V = typing.TypeVar('_create_2__V')  # <V>
    @typing.overload
    @staticmethod
    def create() -> 'TreeMultimap'[_create_0__K, _create_0__V]: ...
    @typing.overload
    @staticmethod
    def create(multimap: Multimap[_create_1__K, _create_1__V]) -> 'TreeMultimap'[_create_1__K, _create_1__V]: ...
    @typing.overload
    @staticmethod
    def create(comparator: typing.Union[java.util.Comparator[_create_2__K], typing.Callable[[_create_2__K, _create_2__K], int]], comparator2: typing.Union[java.util.Comparator[_create_2__V], typing.Callable[[_create_2__V, _create_2__V], int]]) -> 'TreeMultimap'[_create_2__K, _create_2__V]: ...
    def get(self, k: _TreeMultimap__K) -> java.util.NavigableSet[_TreeMultimap__V]: ...
    def keyComparator(self) -> java.util.Comparator[_TreeMultimap__K]: ...
    def keySet(self) -> java.util.NavigableSet[_TreeMultimap__K]: ...
    def valueComparator(self) -> java.util.Comparator[_TreeMultimap__V]: ...

_TreeMultiset__E = typing.TypeVar('_TreeMultiset__E')  # <E>
class TreeMultiset(com.google.common.collect.AbstractSortedMultiset[_TreeMultiset__E], java.io.Serializable, typing.Generic[_TreeMultiset__E]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src`<E> extends AbstractCollection<E> implements Serializable
    
        A multiset which maintains the ordering of its elements, according to either their natural order or an explicit null. In
        all cases, this implementation uses null or null instead of null to determine equivalence of instances.
    
        **Warning:** The comparison must be *consistent with equals* as explained by the null class specification. Otherwise,
        the resulting multiset will violate the null contract, which is specified in terms of null.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def add(self, e: _TreeMultiset__E) -> bool: ...
    @typing.overload
    def add(self, e: _TreeMultiset__E, int: int) -> int: ...
    def clear(self) -> None: ...
    def count(self, object: typing.Any) -> int: ...
    _create_0__E = typing.TypeVar('_create_0__E', bound=java.lang.Comparable)  # <E>
    _create_1__E = typing.TypeVar('_create_1__E', bound=java.lang.Comparable)  # <E>
    _create_2__E = typing.TypeVar('_create_2__E')  # <E>
    @typing.overload
    @staticmethod
    def create() -> 'TreeMultiset'[_create_0__E]: ...
    @typing.overload
    @staticmethod
    def create(iterable: java.lang.Iterable[_create_1__E]) -> 'TreeMultiset'[_create_1__E]: ...
    @typing.overload
    @staticmethod
    def create(comparator: typing.Union[java.util.Comparator[_create_2__E], typing.Callable[[_create_2__E, _create_2__E], int]]) -> 'TreeMultiset'[_create_2__E]: ...
    def forEachEntry(self, objIntConsumer: typing.Union[java.util.function.ObjIntConsumer[_TreeMultiset__E], typing.Callable[[_TreeMultiset__E, int], None]]) -> None: ...
    def headMultiset(self, e: _TreeMultiset__E, boundType: BoundType) -> SortedMultiset[_TreeMultiset__E]: ...
    def iterator(self) -> java.util.Iterator[_TreeMultiset__E]: ...
    @typing.overload
    def remove(self, object: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any, int: int) -> int: ...
    @typing.overload
    def setCount(self, e: _TreeMultiset__E, int: int, int2: int) -> bool: ...
    @typing.overload
    def setCount(self, e: _TreeMultiset__E, int: int) -> int: ...
    def size(self) -> int: ...
    def tailMultiset(self, e: _TreeMultiset__E, boundType: BoundType) -> SortedMultiset[_TreeMultiset__E]: ...

_TreeRangeSet__C = typing.TypeVar('_TreeRangeSet__C', bound=java.lang.Comparable)  # <C>
class TreeRangeSet(com.google.common.collect.AbstractRangeSet[_TreeRangeSet__C], java.io.Serializable, typing.Generic[_TreeRangeSet__C]):
    """
    :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtIncompatible` public class :meth:`~src`<C extends Comparable<?>> extends Object implements Serializable
    
        An implementation of :class:`~com.google.common.collect.RangeSet` backed by a null.
    
        Since:
            14.0
    
        Also see:
            :meth:`~serialized`
    """
    def add(self, range: Range[_TreeRangeSet__C]) -> None: ...
    def addAll(self, iterable: java.lang.Iterable[Range[_TreeRangeSet__C]]) -> None: ...
    def asDescendingSetOfRanges(self) -> java.util.Set[Range[_TreeRangeSet__C]]: ...
    def asRanges(self) -> java.util.Set[Range[_TreeRangeSet__C]]: ...
    def complement(self) -> RangeSet[_TreeRangeSet__C]: ...
    _create_0__C = typing.TypeVar('_create_0__C', bound=java.lang.Comparable)  # <C>
    _create_1__C = typing.TypeVar('_create_1__C', bound=java.lang.Comparable)  # <C>
    _create_2__C = typing.TypeVar('_create_2__C', bound=java.lang.Comparable)  # <C>
    @typing.overload
    @staticmethod
    def create() -> 'TreeRangeSet'[_create_0__C]: ...
    @typing.overload
    @staticmethod
    def create(rangeSet: RangeSet[_create_1__C]) -> 'TreeRangeSet'[_create_1__C]: ...
    @typing.overload
    @staticmethod
    def create(iterable: java.lang.Iterable[Range[_create_2__C]]) -> 'TreeRangeSet'[_create_2__C]: ...
    def encloses(self, range: Range[_TreeRangeSet__C]) -> bool: ...
    def enclosesAll(self, iterable: java.lang.Iterable[Range[_TreeRangeSet__C]]) -> bool: ...
    def intersects(self, range: Range[_TreeRangeSet__C]) -> bool: ...
    def rangeContaining(self, c: _TreeRangeSet__C) -> Range[_TreeRangeSet__C]: ...
    def remove(self, range: Range[_TreeRangeSet__C]) -> None: ...
    def removeAll(self, iterable: java.lang.Iterable[Range[_TreeRangeSet__C]]) -> None: ...
    def span(self) -> Range[_TreeRangeSet__C]: ...
    def subRangeSet(self, range: Range[_TreeRangeSet__C]) -> RangeSet[_TreeRangeSet__C]: ...

class AbstractBiMap: ...

class AbstractMapBasedMultiset: ...

class AbstractMultimap: ...

class AbstractMultiset: ...

class AbstractRangeSet: ...

class AbstractSortedKeySortedSetMultimap: ...

class AbstractSortedMultiset: ...

class AbstractTable: ...

class ArrayListMultimapGwtSerializationDependencies: ...

class BaseImmutableMultimap: ...

class HashMultimapGwtSerializationDependencies: ...

class ImmutableBiMapFauxverideShim: ...

class ImmutableMultisetGwtSerializationDependencies: ...

class ImmutableSortedMapFauxverideShim: ...

class ImmutableSortedMultisetFauxverideShim: ...

class ImmutableSortedSetFauxverideShim: ...

class LinkedHashMultimapGwtSerializationDependencies: ...

class RangeGwtSerializationDependencies: ...

class SortedIterable: ...

class SortedMultisetBridge: ...

class StandardRowSortedTable: ...

class StandardTable: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("com.google.common.collect")``.

    AbstractBiMap: typing.Type[AbstractBiMap]
    AbstractIterator: typing.Type[AbstractIterator]
    AbstractMapBasedMultiset: typing.Type[AbstractMapBasedMultiset]
    AbstractMultimap: typing.Type[AbstractMultimap]
    AbstractMultiset: typing.Type[AbstractMultiset]
    AbstractRangeSet: typing.Type[AbstractRangeSet]
    AbstractSequentialIterator: typing.Type[AbstractSequentialIterator]
    AbstractSortedKeySortedSetMultimap: typing.Type[AbstractSortedKeySortedSetMultimap]
    AbstractSortedMultiset: typing.Type[AbstractSortedMultiset]
    AbstractTable: typing.Type[AbstractTable]
    ArrayListMultimap: typing.Type[ArrayListMultimap]
    ArrayListMultimapGwtSerializationDependencies: typing.Type[ArrayListMultimapGwtSerializationDependencies]
    ArrayTable: typing.Type[ArrayTable]
    BaseImmutableMultimap: typing.Type[BaseImmutableMultimap]
    BiMap: typing.Type[BiMap]
    BoundType: typing.Type[BoundType]
    ClassToInstanceMap: typing.Type[ClassToInstanceMap]
    Collections2: typing.Type[Collections2]
    Comparators: typing.Type[Comparators]
    ComparisonChain: typing.Type[ComparisonChain]
    ComputationException: typing.Type[ComputationException]
    ConcurrentHashMultiset: typing.Type[ConcurrentHashMultiset]
    ContiguousSet: typing.Type[ContiguousSet]
    DiscreteDomain: typing.Type[DiscreteDomain]
    EnumBiMap: typing.Type[EnumBiMap]
    EnumHashBiMap: typing.Type[EnumHashBiMap]
    EnumMultiset: typing.Type[EnumMultiset]
    EvictingQueue: typing.Type[EvictingQueue]
    FluentIterable: typing.Type[FluentIterable]
    ForwardingBlockingDeque: typing.Type[ForwardingBlockingDeque]
    ForwardingCollection: typing.Type[ForwardingCollection]
    ForwardingConcurrentMap: typing.Type[ForwardingConcurrentMap]
    ForwardingDeque: typing.Type[ForwardingDeque]
    ForwardingIterator: typing.Type[ForwardingIterator]
    ForwardingList: typing.Type[ForwardingList]
    ForwardingListIterator: typing.Type[ForwardingListIterator]
    ForwardingListMultimap: typing.Type[ForwardingListMultimap]
    ForwardingMap: typing.Type[ForwardingMap]
    ForwardingMapEntry: typing.Type[ForwardingMapEntry]
    ForwardingMultimap: typing.Type[ForwardingMultimap]
    ForwardingMultiset: typing.Type[ForwardingMultiset]
    ForwardingNavigableMap: typing.Type[ForwardingNavigableMap]
    ForwardingNavigableSet: typing.Type[ForwardingNavigableSet]
    ForwardingObject: typing.Type[ForwardingObject]
    ForwardingQueue: typing.Type[ForwardingQueue]
    ForwardingSet: typing.Type[ForwardingSet]
    ForwardingSetMultimap: typing.Type[ForwardingSetMultimap]
    ForwardingSortedMap: typing.Type[ForwardingSortedMap]
    ForwardingSortedMultiset: typing.Type[ForwardingSortedMultiset]
    ForwardingSortedSet: typing.Type[ForwardingSortedSet]
    ForwardingSortedSetMultimap: typing.Type[ForwardingSortedSetMultimap]
    ForwardingTable: typing.Type[ForwardingTable]
    HashBasedTable: typing.Type[HashBasedTable]
    HashBiMap: typing.Type[HashBiMap]
    HashMultimap: typing.Type[HashMultimap]
    HashMultimapGwtSerializationDependencies: typing.Type[HashMultimapGwtSerializationDependencies]
    HashMultiset: typing.Type[HashMultiset]
    ImmutableBiMap: typing.Type[ImmutableBiMap]
    ImmutableBiMapFauxverideShim: typing.Type[ImmutableBiMapFauxverideShim]
    ImmutableClassToInstanceMap: typing.Type[ImmutableClassToInstanceMap]
    ImmutableCollection: typing.Type[ImmutableCollection]
    ImmutableList: typing.Type[ImmutableList]
    ImmutableListMultimap: typing.Type[ImmutableListMultimap]
    ImmutableMap: typing.Type[ImmutableMap]
    ImmutableMultimap: typing.Type[ImmutableMultimap]
    ImmutableMultiset: typing.Type[ImmutableMultiset]
    ImmutableMultisetGwtSerializationDependencies: typing.Type[ImmutableMultisetGwtSerializationDependencies]
    ImmutableRangeMap: typing.Type[ImmutableRangeMap]
    ImmutableRangeSet: typing.Type[ImmutableRangeSet]
    ImmutableSet: typing.Type[ImmutableSet]
    ImmutableSetMultimap: typing.Type[ImmutableSetMultimap]
    ImmutableSortedMap: typing.Type[ImmutableSortedMap]
    ImmutableSortedMapFauxverideShim: typing.Type[ImmutableSortedMapFauxverideShim]
    ImmutableSortedMultiset: typing.Type[ImmutableSortedMultiset]
    ImmutableSortedMultisetFauxverideShim: typing.Type[ImmutableSortedMultisetFauxverideShim]
    ImmutableSortedSet: typing.Type[ImmutableSortedSet]
    ImmutableSortedSetFauxverideShim: typing.Type[ImmutableSortedSetFauxverideShim]
    ImmutableTable: typing.Type[ImmutableTable]
    Interner: typing.Type[Interner]
    Interners: typing.Type[Interners]
    Iterables: typing.Type[Iterables]
    Iterators: typing.Type[Iterators]
    LinkedHashMultimap: typing.Type[LinkedHashMultimap]
    LinkedHashMultimapGwtSerializationDependencies: typing.Type[LinkedHashMultimapGwtSerializationDependencies]
    LinkedHashMultiset: typing.Type[LinkedHashMultiset]
    LinkedListMultimap: typing.Type[LinkedListMultimap]
    ListMultimap: typing.Type[ListMultimap]
    Lists: typing.Type[Lists]
    MapDifference: typing.Type[MapDifference]
    MapMaker: typing.Type[MapMaker]
    Maps: typing.Type[Maps]
    MinMaxPriorityQueue: typing.Type[MinMaxPriorityQueue]
    MoreCollectors: typing.Type[MoreCollectors]
    Multimap: typing.Type[Multimap]
    MultimapBuilder: typing.Type[MultimapBuilder]
    Multimaps: typing.Type[Multimaps]
    Multiset: typing.Type[Multiset]
    Multisets: typing.Type[Multisets]
    MutableClassToInstanceMap: typing.Type[MutableClassToInstanceMap]
    ObjectArrays: typing.Type[ObjectArrays]
    Ordering: typing.Type[Ordering]
    PeekingIterator: typing.Type[PeekingIterator]
    Queues: typing.Type[Queues]
    Range: typing.Type[Range]
    RangeGwtSerializationDependencies: typing.Type[RangeGwtSerializationDependencies]
    RangeMap: typing.Type[RangeMap]
    RangeSet: typing.Type[RangeSet]
    RowSortedTable: typing.Type[RowSortedTable]
    SetMultimap: typing.Type[SetMultimap]
    Sets: typing.Type[Sets]
    SortedIterable: typing.Type[SortedIterable]
    SortedMapDifference: typing.Type[SortedMapDifference]
    SortedMultiset: typing.Type[SortedMultiset]
    SortedMultisetBridge: typing.Type[SortedMultisetBridge]
    SortedSetMultimap: typing.Type[SortedSetMultimap]
    StandardRowSortedTable: typing.Type[StandardRowSortedTable]
    StandardTable: typing.Type[StandardTable]
    Streams: typing.Type[Streams]
    Table: typing.Type[Table]
    Tables: typing.Type[Tables]
    TreeBasedTable: typing.Type[TreeBasedTable]
    TreeMultimap: typing.Type[TreeMultimap]
    TreeMultiset: typing.Type[TreeMultiset]
    TreeRangeMap: typing.Type[TreeRangeMap]
    TreeRangeSet: typing.Type[TreeRangeSet]
    TreeTraverser: typing.Type[TreeTraverser]
    UnmodifiableIterator: typing.Type[UnmodifiableIterator]
    UnmodifiableListIterator: typing.Type[UnmodifiableListIterator]
