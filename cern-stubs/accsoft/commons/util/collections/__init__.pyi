import cern.accsoft.commons.util.collections.tree
import java.util
import java.util.function
import typing



_CircularBuffer__E = typing.TypeVar('_CircularBuffer__E')  # <E>
class CircularBuffer(java.util.Queue[_CircularBuffer__E], typing.Generic[_CircularBuffer__E]):
    """
    Java class 'cern.accsoft.commons.util.collections.CircularBuffer'
    
        Interfaces:
            java.util.Queue
    
    """
    def add(self, e: _CircularBuffer__E) -> bool: ...
    def addAll(self, collection: typing.Union[java.util.Collection[_CircularBuffer__E], typing.Sequence[_CircularBuffer__E]]) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def offer(self, e: _CircularBuffer__E) -> bool: ...
    def peekLast(self) -> _CircularBuffer__E: ...

class CircularBuffers:
    """
    Java class 'cern.accsoft.commons.util.collections.CircularBuffers'
    
        Extends:
            java.lang.Object
    
    """
    _synchronizedCircularBuffer__T = typing.TypeVar('_synchronizedCircularBuffer__T')  # <T>
    @staticmethod
    def synchronizedCircularBuffer(circularBuffer: CircularBuffer[_synchronizedCircularBuffer__T]) -> CircularBuffer[_synchronizedCircularBuffer__T]: ...

_MultiValueMap__K = typing.TypeVar('_MultiValueMap__K')  # <K>
_MultiValueMap__V = typing.TypeVar('_MultiValueMap__V')  # <V>
class MultiValueMap(typing.Generic[_MultiValueMap__K, _MultiValueMap__V]):
    """
    Java class 'cern.accsoft.commons.util.collections.MultiValueMap'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MultiValueMap(java.lang.Class, boolean)
        * MultiValueMap(int)
        * MultiValueMap(int, java.lang.Class)
        * MultiValueMap(int, java.lang.Class, boolean)
        * MultiValueMap()
        * MultiValueMap(java.lang.Class)
        * MultiValueMap(boolean)
    
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
    def clear(self) -> None: ...
    def contains(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> bool: ...
    def containsAll(self, k: _MultiValueMap__K, collection: typing.Union[java.util.Collection[_MultiValueMap__V], typing.Sequence[_MultiValueMap__V]]) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getKeys(self) -> java.util.Set[_MultiValueMap__K]: ...
    def getValues(self, k: _MultiValueMap__K) -> java.util.Collection[_MultiValueMap__V]: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def put(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> None: ...
    @typing.overload
    def putAll(self, k: _MultiValueMap__K, collection: typing.Union[java.util.Collection[_MultiValueMap__V], typing.Sequence[_MultiValueMap__V]]) -> None: ...
    @typing.overload
    def putAll(self, map: typing.Union[java.util.Map[_MultiValueMap__K, _MultiValueMap__V], typing.Mapping[_MultiValueMap__K, _MultiValueMap__V]]) -> None: ...
    @typing.overload
    def remove(self, k: _MultiValueMap__K) -> bool: ...
    @typing.overload
    def remove(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> bool: ...
    def removeAll(self, k: _MultiValueMap__K, collection: typing.Union[java.util.Collection[_MultiValueMap__V], typing.Sequence[_MultiValueMap__V]]) -> bool: ...
    def size(self, k: _MultiValueMap__K) -> int: ...
    def toString(self) -> str: ...

_OrderedSet__E = typing.TypeVar('_OrderedSet__E')  # <E>
class OrderedSet(java.util.Set[_OrderedSet__E], typing.Generic[_OrderedSet__E]):
    """
    Java class 'cern.accsoft.commons.util.collections.OrderedSet'
    
        Interfaces:
            java.util.Set
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...

_ValueCollector__T = typing.TypeVar('_ValueCollector__T')  # <T>
class ValueCollector(typing.Generic[_ValueCollector__T]):
    """
    Java class 'cern.accsoft.commons.util.collections.ValueCollector'
    
    """
    def peek(self, valuePeekingStrategy: 'ValuePeekingStrategy'[_ValueCollector__T], long: int) -> java.util.Collection[_ValueCollector__T]: ...

_ValuePeekingStrategy__T = typing.TypeVar('_ValuePeekingStrategy__T')  # <T>
class ValuePeekingStrategy(typing.Generic[_ValuePeekingStrategy__T]):
    """
    Java class 'cern.accsoft.commons.util.collections.ValuePeekingStrategy'
    
    """
    def peek(self, circularBuffer: CircularBuffer[_ValuePeekingStrategy__T], boolean: bool) -> java.util.Collection[_ValuePeekingStrategy__T]: ...

_AbstractValueCollector__T = typing.TypeVar('_AbstractValueCollector__T')  # <T>
class AbstractValueCollector(ValueCollector[_AbstractValueCollector__T], typing.Generic[_AbstractValueCollector__T]):
    """
    Java class 'cern.accsoft.commons.util.collections.AbstractValueCollector'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.collections.ValueCollector
    
      Constructors:
        * AbstractValueCollector()
        * AbstractValueCollector(int)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    def peek(self, valuePeekingStrategy: ValuePeekingStrategy[_AbstractValueCollector__T], long: int) -> java.util.Collection[_AbstractValueCollector__T]: ...

_ArrayCircularBuffer__E = typing.TypeVar('_ArrayCircularBuffer__E')  # <E>
class ArrayCircularBuffer(CircularBuffer[_ArrayCircularBuffer__E], typing.Generic[_ArrayCircularBuffer__E]):
    """
    Java class 'cern.accsoft.commons.util.collections.ArrayCircularBuffer'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.collections.CircularBuffer
    
      Constructors:
        * ArrayCircularBuffer(int)
        * ArrayCircularBuffer(int, java.util.Collection)
    
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, collection: typing.Union[java.util.Collection[_ArrayCircularBuffer__E], typing.Sequence[_ArrayCircularBuffer__E]]): ...
    def add(self, e: _ArrayCircularBuffer__E) -> bool: ...
    def addAll(self, collection: typing.Union[java.util.Collection[_ArrayCircularBuffer__E], typing.Sequence[_ArrayCircularBuffer__E]]) -> bool: ...
    def clear(self) -> None: ...
    def contains(self, object: typing.Any) -> bool: ...
    def containsAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def element(self) -> _ArrayCircularBuffer__E: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> java.util.Iterator[_ArrayCircularBuffer__E]: ...
    def offer(self, e: _ArrayCircularBuffer__E) -> bool: ...
    def peek(self) -> _ArrayCircularBuffer__E: ...
    def peekLast(self) -> _ArrayCircularBuffer__E: ...
    def poll(self) -> _ArrayCircularBuffer__E: ...
    @typing.overload
    def remove(self, object: typing.Any) -> bool: ...
    @typing.overload
    def remove(self) -> _ArrayCircularBuffer__E: ...
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

_LastValuePeekingStrategy__T = typing.TypeVar('_LastValuePeekingStrategy__T')  # <T>
class LastValuePeekingStrategy(ValuePeekingStrategy[_LastValuePeekingStrategy__T], typing.Generic[_LastValuePeekingStrategy__T]):
    """
    Java class 'cern.accsoft.commons.util.collections.LastValuePeekingStrategy'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.collections.ValuePeekingStrategy
    
      Constructors:
        * LastValuePeekingStrategy()
    
    """
    def __init__(self): ...
    def peek(self, circularBuffer: CircularBuffer[_LastValuePeekingStrategy__T], boolean: bool) -> java.util.Collection[_LastValuePeekingStrategy__T]: ...

_OrderedHashSet__E = typing.TypeVar('_OrderedHashSet__E')  # <E>
class OrderedHashSet(java.util.LinkedHashSet[_OrderedHashSet__E], OrderedSet[_OrderedHashSet__E], typing.Generic[_OrderedHashSet__E]):
    """
    Java class 'cern.accsoft.commons.util.collections.OrderedHashSet'
    
        Extends:
            java.util.LinkedHashSet
    
        Interfaces:
            cern.accsoft.commons.util.collections.OrderedSet
    
      Constructors:
        * OrderedHashSet()
        * OrderedHashSet(java.util.Collection)
        * OrderedHashSet(int, float)
        * OrderedHashSet(int)
    
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
