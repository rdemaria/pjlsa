import cern.accsoft.commons.util.collections.tree
import java.util
import java.util.function
import typing



_CircularBuffer__E = typing.TypeVar('_CircularBuffer__E')  # <E>
class CircularBuffer(java.util.Queue[_CircularBuffer__E], typing.Generic[_CircularBuffer__E]):
    """
    public interface CircularBuffer<E> extends `Queue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Queue.html?is-external=true>`<E>
    
        A collection that can contain a maximum amount of elements. If an element is added when the buffer is full, then the
        oldest element is removed. With respect to a `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Queue.html?is-external=true>` a circular buffer has
        modified behaviour for the methods related to adding elements
        (:meth:`~cern.accsoft.commons.util.collections.CircularBuffer.add`,:meth:`~cern.accsoft.commons.util.collections.CircularBuffer.addAll`
        , :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.offer`).
    """
    def add(self, e: _CircularBuffer__E) -> bool:
        """
            Inserts the specified element into this buffer. If the capacity of the buffer is reached, then the head-element from the
            buffer is removed prior to adding the new element. The difference to the
            :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.offer` method is, that this method throws an `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalStateException.html?is-external=true>`, if the
            element can not be added.
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Parameters:
                e (:class:`~cern.accsoft.commons.util.collections.CircularBuffer`): the element to add
        
            Returns:
                ``true`` (as specified by `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true#add(E)>`)
        
            Raises:
                : if the element cannot be added at this time due to capacity restrictions
                : if the class of the specified element prevents it from being added to this bugger
                : if the specified element is null and this buffer does not permit null elements
                : if some property of this element prevents it from being added to this buffer
        
        
        """
        ...
    def addAll(self, collection: typing.Union[java.util.Collection[_CircularBuffer__E], typing.Sequence[_CircularBuffer__E]]) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def offer(self, e: _CircularBuffer__E) -> bool:
        """
            Inserts the specified element into this buffer. If the capacity of the buffer is reached, then the head-element from the
            buffer is removed prior to adding the new element. The difference to the
            :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.add` method is, that this method does not throw an
            exception, if the element can not be added, instead it returns :code:`false`.
        
            Specified by:
                 in interface 
        
            Parameters:
                e (:class:`~cern.accsoft.commons.util.collections.CircularBuffer`): the element to add
        
            Returns:
                :code:`true` if the element was added, :code:`false` otherwise
        
            Raises:
                : if the class of the specified element prevents it from being added to this buffer
                : if the specified element is null and this buffer does not permit null elements
                : if some property of this element prevents it from being added to this buffer
        
        
        """
        ...
    def peekLast(self) -> _CircularBuffer__E:
        """
            Retrieves, but does not remove, the tail of this buffer, or returns :code:`null` if this buffer is empty.
        
            Returns:
                the last added element (tail) of the buffer.
        
        
        """
        ...

class CircularBuffers:
    """
    public class CircularBuffers extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Contains static helper methods related to :class:`~cern.accsoft.commons.util.collections.CircularBuffer`s.
    """
    _synchronizedCircularBuffer__T = typing.TypeVar('_synchronizedCircularBuffer__T')  # <T>
    @staticmethod
    def synchronizedCircularBuffer(circularBuffer: CircularBuffer[_synchronizedCircularBuffer__T]) -> CircularBuffer[_synchronizedCircularBuffer__T]:
        """
            Returns a synchronized (thread-safe) circular buffer backed by the specified circular buffer. In order to guarantee
            serial access, it is critical that **all** access to the backing set is accomplished through the returned set.
        
            It is imperative that the user manually synchronize on the returned circular buffer when iterating over it:
        
            .. code-block: java
            
              CircularBuffer cb = CircularBuffers.synchronizedCircularBuffer(new CircularBufferImpl());
                  ...
              synchronized(cb) {
                  Iterator i = cb.iterator(); // Must be in the synchronized block
                  while (cb.hasNext())
                      foo(cb.next());
              }
             
            Failure to follow this advice may result in non-deterministic behavior.
        
            The returned circular buffer will be serializable if the specified set is serializable.
        
            Parameters:
                circularBuffer (:class:`~cern.accsoft.commons.util.collections.CircularBuffer`<T> circularBuffer): the circular buffer to wrap
        
            Returns:
                a synchronized view of the specified circular buffer.
        
        
        """
        ...

_MultiValueMap__K = typing.TypeVar('_MultiValueMap__K')  # <K>
_MultiValueMap__V = typing.TypeVar('_MultiValueMap__V')  # <V>
class MultiValueMap(typing.Generic[_MultiValueMap__K, _MultiValueMap__V]):
    """
    public class MultiValueMap<K, V> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A map that can contain for each key multiple values.
    
        Key is mapped to a collection of values.
    
        Internally this map can use any type of collection to keep the values (lists, sets). By default a `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/LinkedList.html?is-external=true>` is used.
    
        This class also supports the behavior of `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/WeakHashMap.html?is-external=true>`: an entry in a
        ``MultiValueMap`` will automatically be removed when its key is no longer in ordinary use.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, class_: typing.Type[java.util.Collection]): ...
    @typing.overload
    def __init__(self, int: int, class_: typing.Type[java.util.Collection], boolean: bool): ...
    @typing.overload
    def __init__(self, class_: typing.Type[java.util.Collection]): ...
    @typing.overload
    def __init__(self, class_: typing.Type[java.util.Collection], boolean: bool): ...
    def asMap(self) -> java.util.Map[_MultiValueMap__K, java.util.Collection[_MultiValueMap__V]]: ...
    def clear(self) -> None:
        """
            Clears the whole map.
        
        """
        ...
    def contains(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> bool:
        """
            Checks whether the key-value pair is stored in this MultiValueMap.
        
            Parameters:
                key (:class:`~cern.accsoft.commons.util.collections.MultiValueMap`): the key (must be non-null)
                value (:class:`~cern.accsoft.commons.util.collections.MultiValueMap`): the value (must be non-null)
        
            Returns:
                true if the key-value pair is stored in this MultiValueMap
        
        
        """
        ...
    def containsAll(self, k: _MultiValueMap__K, collection: typing.Union[java.util.Collection[_MultiValueMap__V], typing.Sequence[_MultiValueMap__V]]) -> bool: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getKeys(self) -> java.util.Set[_MultiValueMap__K]: ...
    def getValues(self, k: _MultiValueMap__K) -> java.util.Collection[_MultiValueMap__V]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Checks whether the map is empty.
        
            Returns:
                true if the map is empty and false otherwise.
        
        
        """
        ...
    def put(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> None:
        """
            Adds the key-value pair to this MultiValueMap.
        
            Parameters:
                key (:class:`~cern.accsoft.commons.util.collections.MultiValueMap`): the key (must be non-null)
                value (:class:`~cern.accsoft.commons.util.collections.MultiValueMap`): the value (must be non-null)
        
        
        """
        ...
    @typing.overload
    def putAll(self, k: _MultiValueMap__K, collection: typing.Union[java.util.Collection[_MultiValueMap__V], typing.Sequence[_MultiValueMap__V]]) -> None: ...
    @typing.overload
    def putAll(self, map: typing.Union[java.util.Map[_MultiValueMap__K, _MultiValueMap__V], typing.Mapping[_MultiValueMap__K, _MultiValueMap__V]]) -> None: ...
    @typing.overload
    def remove(self, k: _MultiValueMap__K) -> bool:
        """
            Removes all the values for particular key.
        
            Parameters:
                key (:class:`~cern.accsoft.commons.util.collections.MultiValueMap`): the key (must be non-null)
        
            Returns:
                true if it was successfully removed
        
            Removes the key-value pair from this MultiValueMap.
        
            Parameters:
                key (:class:`~cern.accsoft.commons.util.collections.MultiValueMap`): the key (must be non-null)
                value (:class:`~cern.accsoft.commons.util.collections.MultiValueMap`): the value (must be non-null)
        
            Returns:
                true if it was successfully removed
        
        
        """
        ...
    @typing.overload
    def remove(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> bool: ...
    def removeAll(self, k: _MultiValueMap__K, collection: typing.Union[java.util.Collection[_MultiValueMap__V], typing.Sequence[_MultiValueMap__V]]) -> bool: ...
    def size(self, k: _MultiValueMap__K) -> int:
        """
            Returns the number of elements stored with the key.
        
            Parameters:
                key (:class:`~cern.accsoft.commons.util.collections.MultiValueMap`): the key (must be non-null)
        
            Returns:
                the number of elements stored with the key.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_OrderedSet__E = typing.TypeVar('_OrderedSet__E')  # <E>
class OrderedSet(java.util.Set[_OrderedSet__E], typing.Generic[_OrderedSet__E]):
    """
    public interface OrderedSet<E> extends `Set <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Set.html?is-external=true>`<E>
    
        Represents a set keeping the insertion order.
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...

_ValueCollector__T = typing.TypeVar('_ValueCollector__T')  # <T>
class ValueCollector(typing.Generic[_ValueCollector__T]):
    """
    public interface ValueCollector<T>
    
        Interface represents a collector for values of certain type.
    
        Collector is a class which keeps a buffer of values and allows to retrieve the values with certain timeout and different
        strategies described by the interface :class:`~cern.accsoft.commons.util.collections.ValuePeekingStrategy`.
    
        The collector notifies the strategy each time a new value or exception has arrived within the specified timeout. The
        strategy can choose some values or continue to wait. Once a strategy has chosen some values those values are returned to
        the client. When timeout expires the collector notifies the strategy the last time with the :code:`timeoutExpired` flag
        set to let the strategy the last chance to choose values.
    """
    def peek(self, valuePeekingStrategy: 'ValuePeekingStrategy'[_ValueCollector__T], long: int) -> java.util.Collection[_ValueCollector__T]: ...

_ValuePeekingStrategy__T = typing.TypeVar('_ValuePeekingStrategy__T')  # <T>
class ValuePeekingStrategy(typing.Generic[_ValuePeekingStrategy__T]):
    """
    public interface ValuePeekingStrategy<T>
    
        Interface describing a strategy which chooses the values from
        :class:`~cern.accsoft.commons.util.collections.ValueCollector`.
    """
    def peek(self, circularBuffer: CircularBuffer[_ValuePeekingStrategy__T], boolean: bool) -> java.util.Collection[_ValuePeekingStrategy__T]: ...

_AbstractValueCollector__T = typing.TypeVar('_AbstractValueCollector__T')  # <T>
class AbstractValueCollector(ValueCollector[_AbstractValueCollector__T], typing.Generic[_AbstractValueCollector__T]):
    """
    public abstract class AbstractValueCollector<T> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.collections.ValueCollector`<T>
    
        Abstract implementation of :class:`~cern.accsoft.commons.util.collections.ValueCollector`.
    
        Since every collector has its own way of receiving the values the implementations should implement the receiving
        functionality accordingly and use :meth:`~cern.accsoft.commons.util.collections.AbstractValueCollector.doAddValue`
        method to add the received value to the collector.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    def peek(self, valuePeekingStrategy: ValuePeekingStrategy[_AbstractValueCollector__T], long: int) -> java.util.Collection[_AbstractValueCollector__T]: ...

_ArrayCircularBuffer__E = typing.TypeVar('_ArrayCircularBuffer__E')  # <E>
class ArrayCircularBuffer(CircularBuffer[_ArrayCircularBuffer__E], typing.Generic[_ArrayCircularBuffer__E]):
    """
    public class ArrayCircularBuffer<E> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.collections.CircularBuffer`<E>
    
        The implementation of a circular buffer, backed by an `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/ArrayBlockingQueue.html?is-external=true>`.
        This class implements the methods with modified behaviour with respect to `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Queue.html?is-external=true>` as defined in
        :class:`~cern.accsoft.commons.util.collections.CircularBuffer`. The rest of the method calls are delegated to the
        backing queue. Since array blocking queue does not accept null elements, this implementation also does not.
    
        This class is not thread save.
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, collection: typing.Union[java.util.Collection[_ArrayCircularBuffer__E], typing.Sequence[_ArrayCircularBuffer__E]]): ...
    def add(self, e: _ArrayCircularBuffer__E) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.add`
            Inserts the specified element into this buffer. If the capacity of the buffer is reached, then the head-element from the
            buffer is removed prior to adding the new element. The difference to the
            :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.offer` method is, that this method throws an `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalStateException.html?is-external=true>`, if the
            element can not be added.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.add`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.collections.CircularBuffer`
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Parameters:
                element (:class:`~cern.accsoft.commons.util.collections.ArrayCircularBuffer`): the element to add
        
            Returns:
                ``true`` (as specified by `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true#add(E)>`)
        
        
        """
        ...
    def addAll(self, collection: typing.Union[java.util.Collection[_ArrayCircularBuffer__E], typing.Sequence[_ArrayCircularBuffer__E]]) -> bool: ...
    def clear(self) -> None:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def contains(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def containsAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def element(self) -> _ArrayCircularBuffer__E:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator[_ArrayCircularBuffer__E]: ...
    def offer(self, e: _ArrayCircularBuffer__E) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.offer`
            Inserts the specified element into this buffer. If the capacity of the buffer is reached, then the head-element from the
            buffer is removed prior to adding the new element. The difference to the
            :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.add` method is, that this method does not throw an
            exception, if the element can not be added, instead it returns :code:`false`.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.offer`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.collections.CircularBuffer`
        
            Specified by:
                 in interface 
        
            Parameters:
                element (:class:`~cern.accsoft.commons.util.collections.ArrayCircularBuffer`): the element to add
        
            Returns:
                :code:`true` if the element was added, :code:`false` otherwise
        
        
        """
        ...
    def peek(self) -> _ArrayCircularBuffer__E:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def peekLast(self) -> _ArrayCircularBuffer__E:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.peekLast`
            Retrieves, but does not remove, the tail of this buffer, or returns :code:`null` if this buffer is empty.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.collections.CircularBuffer.peekLast`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.collections.CircularBuffer`
        
            Returns:
                the last added element (tail) of the buffer.
        
        
        """
        ...
    def poll(self) -> _ArrayCircularBuffer__E:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    @typing.overload
    def remove(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    @typing.overload
    def remove(self) -> _ArrayCircularBuffer__E:
        """
        
            Specified by:
                 in interface 
        
        """
        ...
    def removeAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def retainAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def size(self) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    _toArray_0__T = typing.TypeVar('_toArray_0__T')  # <T>
    _toArray_2__T = typing.TypeVar('_toArray_2__T')  # <T>
    @typing.overload
    def toArray(self, intFunction: typing.Union[java.util.function.IntFunction[typing.List[_toArray_0__T]], typing.Callable[[int], typing.List[_toArray_0__T]]]) -> typing.List[_toArray_0__T]:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    @typing.overload
    def toArray(self) -> typing.List[typing.Any]:
        """
        
            Specified by:
                 in interface 
        
        """
        ...
    @typing.overload
    def toArray(self, tArray: typing.List[_toArray_2__T]) -> typing.List[_toArray_2__T]: ...

_LastValuePeekingStrategy__T = typing.TypeVar('_LastValuePeekingStrategy__T')  # <T>
class LastValuePeekingStrategy(ValuePeekingStrategy[_LastValuePeekingStrategy__T], typing.Generic[_LastValuePeekingStrategy__T]):
    """
    public class LastValuePeekingStrategy<T> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.collections.ValuePeekingStrategy`<T>
    
        Implementation of :class:`~cern.accsoft.commons.util.collections.ValuePeekingStrategy` which chooses the latest value
        from the buffer within timeout.
    
        Basically this implementation always returns no value until timeout expires and the strategy gets its last chance to
        peek a value. Then it peeks the latest value.
    """
    def __init__(self): ...
    def peek(self, circularBuffer: CircularBuffer[_LastValuePeekingStrategy__T], boolean: bool) -> java.util.Collection[_LastValuePeekingStrategy__T]: ...

_OrderedHashSet__E = typing.TypeVar('_OrderedHashSet__E')  # <E>
class OrderedHashSet(java.util.LinkedHashSet[_OrderedHashSet__E], OrderedSet[_OrderedHashSet__E], typing.Generic[_OrderedHashSet__E]):
    """
    public class OrderedHashSet<E> extends `LinkedHashSet <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/LinkedHashSet.html?is-external=true>`<E> implements :class:`~cern.accsoft.commons.util.collections.OrderedSet`<E>
    
        Default :class:`~cern.accsoft.commons.util.collections.OrderedSet` implementation based on `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/LinkedHashSet.html?is-external=true>`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, float: float): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[_OrderedHashSet__E], typing.Sequence[_OrderedHashSet__E]]): ...
    _asOrderedSet__T = typing.TypeVar('_asOrderedSet__T')  # <T>
    @staticmethod
    def asOrderedSet(tArray: typing.List[_asOrderedSet__T]) -> 'OrderedHashSet'[_asOrderedSet__T]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.collections")``.

    AbstractValueCollector: typing.Type[AbstractValueCollector]
    ArrayCircularBuffer: typing.Type[ArrayCircularBuffer]
    CircularBuffer: typing.Type[CircularBuffer]
    CircularBuffers: typing.Type[CircularBuffers]
    LastValuePeekingStrategy: typing.Type[LastValuePeekingStrategy]
    MultiValueMap: typing.Type[MultiValueMap]
    OrderedHashSet: typing.Type[OrderedHashSet]
    OrderedSet: typing.Type[OrderedSet]
    ValueCollector: typing.Type[ValueCollector]
    ValuePeekingStrategy: typing.Type[ValuePeekingStrategy]
    tree: cern.accsoft.commons.util.collections.tree.__module_protocol__
