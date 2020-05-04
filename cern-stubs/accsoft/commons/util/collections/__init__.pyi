from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import Generic as _py_Generic
from typing import overload
import java.util


_CircularBuffer__E = _py_TypeVar('_CircularBuffer__E')  # <E>
class CircularBuffer(java.util.Queue[_CircularBuffer__E], _py_Generic[_CircularBuffer__E]):
    def add(self, e: _CircularBuffer__E) -> bool: ...
    def addAll(self, collection: java.util.Collection[_CircularBuffer__E]) -> bool: ...
    def equals(self, object: _py_Any) -> bool: ...
    def hashCode(self) -> int: ...
    def offer(self, e: _CircularBuffer__E) -> bool: ...
    def peekLast(self) -> _CircularBuffer__E: ...

class CircularBuffers:
    _synchronizedCircularBuffer__T = _py_TypeVar('_synchronizedCircularBuffer__T')  # <T>
    @classmethod
    def synchronizedCircularBuffer(cls, circularBuffer: CircularBuffer[_synchronizedCircularBuffer__T]) -> CircularBuffer[_synchronizedCircularBuffer__T]: ...

_MultiValueMap__K = _py_TypeVar('_MultiValueMap__K')  # <K>
_MultiValueMap__V = _py_TypeVar('_MultiValueMap__V')  # <V>
class MultiValueMap(_py_Generic[_MultiValueMap__K, _MultiValueMap__V]):
    @overload
    def __init__(self, int: int, class_: _py_Type[java.util.Collection], boolean: bool): ...
    @overload
    def __init__(self, int: int, class_: _py_Type[java.util.Collection]): ...
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, class_: _py_Type[java.util.Collection]): ...
    @overload
    def __init__(self, boolean: bool): ...
    @overload
    def __init__(self, class_: _py_Type[java.util.Collection], boolean: bool): ...
    @overload
    def __init__(self, int: int): ...
    def asMap(self) -> java.util.Map[_MultiValueMap__K, java.util.Collection[_MultiValueMap__V]]: ...
    def clear(self) -> None: ...
    def contains(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> bool: ...
    def containsAll(self, k: _MultiValueMap__K, collection: java.util.Collection[_MultiValueMap__V]) -> bool: ...
    def equals(self, object: _py_Any) -> bool: ...
    def getKeys(self) -> java.util.Set[_MultiValueMap__K]: ...
    def getValues(self, k: _MultiValueMap__K) -> java.util.Collection[_MultiValueMap__V]: ...
    def hashCode(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def put(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> None: ...
    @overload
    def putAll(self, k: _MultiValueMap__K, collection: java.util.Collection[_MultiValueMap__V]) -> None: ...
    @overload
    def putAll(self, map: java.util.Map[_MultiValueMap__K, _MultiValueMap__V]) -> None: ...
    @overload
    def remove(self, k: _MultiValueMap__K) -> bool: ...
    @overload
    def remove(self, k: _MultiValueMap__K, v: _MultiValueMap__V) -> bool: ...
    def removeAll(self, k: _MultiValueMap__K, collection: java.util.Collection[_MultiValueMap__V]) -> bool: ...
    def size(self, k: _MultiValueMap__K) -> int: ...
    def toString(self) -> str: ...

_OrderedSet__E = _py_TypeVar('_OrderedSet__E')  # <E>
class OrderedSet(java.util.Set[_OrderedSet__E], _py_Generic[_OrderedSet__E]):
    def equals(self, object: _py_Any) -> bool: ...
    def hashCode(self) -> int: ...

_ValueCollector__T = _py_TypeVar('_ValueCollector__T')  # <T>
class ValueCollector(_py_Generic[_ValueCollector__T]):
    def peek(self, valuePeekingStrategy: 'ValuePeekingStrategy'[_ValueCollector__T], long: int) -> java.util.Collection[_ValueCollector__T]: ...

_ValuePeekingStrategy__T = _py_TypeVar('_ValuePeekingStrategy__T')  # <T>
class ValuePeekingStrategy(_py_Generic[_ValuePeekingStrategy__T]):
    def peek(self, circularBuffer: CircularBuffer[_ValuePeekingStrategy__T], boolean: bool) -> java.util.Collection[_ValuePeekingStrategy__T]: ...

_AbstractValueCollector__T = _py_TypeVar('_AbstractValueCollector__T')  # <T>
class AbstractValueCollector(ValueCollector[_AbstractValueCollector__T], _py_Generic[_AbstractValueCollector__T]):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, int: int): ...
    def peek(self, valuePeekingStrategy: ValuePeekingStrategy[_AbstractValueCollector__T], long: int) -> java.util.Collection[_AbstractValueCollector__T]: ...

_ArrayCircularBuffer__E = _py_TypeVar('_ArrayCircularBuffer__E')  # <E>
class ArrayCircularBuffer(CircularBuffer[_ArrayCircularBuffer__E], _py_Generic[_ArrayCircularBuffer__E]):
    @overload
    def __init__(self, int: int): ...
    @overload
    def __init__(self, int: int, collection: java.util.Collection[_ArrayCircularBuffer__E]): ...
    def add(self, e: _ArrayCircularBuffer__E) -> bool: ...
    def addAll(self, collection: java.util.Collection[_ArrayCircularBuffer__E]) -> bool: ...
    def clear(self) -> None: ...
    def contains(self, object: _py_Any) -> bool: ...
    def containsAll(self, collection: java.util.Collection[_py_Any]) -> bool: ...
    def element(self) -> _ArrayCircularBuffer__E: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> java.util.Iterator[_ArrayCircularBuffer__E]: ...
    def offer(self, e: _ArrayCircularBuffer__E) -> bool: ...
    def peek(self) -> _ArrayCircularBuffer__E: ...
    def peekLast(self) -> _ArrayCircularBuffer__E: ...
    def poll(self) -> _ArrayCircularBuffer__E: ...
    @overload
    def remove(self, object: _py_Any) -> bool: ...
    @overload
    def remove(self) -> _ArrayCircularBuffer__E: ...
    def removeAll(self, collection: java.util.Collection[_py_Any]) -> bool: ...
    def retainAll(self, collection: java.util.Collection[_py_Any]) -> bool: ...
    def size(self) -> int: ...
    @overload
    def toArray(self) -> _py_List[_py_Any]: ...
    _toArray_1__T = _py_TypeVar('_toArray_1__T')  # <T>
    @overload
    def toArray(self, tArray: _py_List[_toArray_1__T]) -> _py_List[_toArray_1__T]: ...

_LastValuePeekingStrategy__T = _py_TypeVar('_LastValuePeekingStrategy__T')  # <T>
class LastValuePeekingStrategy(ValuePeekingStrategy[_LastValuePeekingStrategy__T], _py_Generic[_LastValuePeekingStrategy__T]):
    def __init__(self): ...
    def peek(self, circularBuffer: CircularBuffer[_LastValuePeekingStrategy__T], boolean: bool) -> java.util.Collection[_LastValuePeekingStrategy__T]: ...

_OrderedHashSet__E = _py_TypeVar('_OrderedHashSet__E')  # <E>
class OrderedHashSet(java.util.LinkedHashSet[_OrderedHashSet__E], OrderedSet[_OrderedHashSet__E], _py_Generic[_OrderedHashSet__E]):
    @overload
    def __init__(self, collection: java.util.Collection[_OrderedHashSet__E]): ...
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, int: int): ...
    @overload
    def __init__(self, int: int, float: float): ...
    _asOrderedSet__T = _py_TypeVar('_asOrderedSet__T')  # <T>
    @classmethod
    def asOrderedSet(cls, tArray: _py_List[_asOrderedSet__T]) -> 'OrderedHashSet'[_asOrderedSet__T]: ...
