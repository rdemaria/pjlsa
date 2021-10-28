import java.lang
import java.util.concurrent
import typing



class Cleaner:
    """
    Java class 'java.lang.ref.Cleaner'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    @staticmethod
    def create() -> 'Cleaner': ...
    @typing.overload
    @staticmethod
    def create(threadFactory: java.util.concurrent.ThreadFactory) -> 'Cleaner': ...
    def register(self, object: typing.Any, runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> 'Cleaner.Cleanable': ...
    class Cleanable:
        """
        Java class 'java.lang.ref.Cleaner$Cleanable'
        
        """
        def clean(self) -> None: ...

_Reference__T = typing.TypeVar('_Reference__T')  # <T>
class Reference(typing.Generic[_Reference__T]):
    """
    Java class 'java.lang.ref.Reference'
    
        Extends:
            java.lang.Object
    
    """
    def clear(self) -> None: ...
    def enqueue(self) -> bool: ...
    def get(self) -> _Reference__T: ...
    def isEnqueued(self) -> bool: ...
    @staticmethod
    def reachabilityFence(object: typing.Any) -> None: ...

_ReferenceQueue__T = typing.TypeVar('_ReferenceQueue__T')  # <T>
class ReferenceQueue(typing.Generic[_ReferenceQueue__T]):
    """
    Java class 'java.lang.ref.ReferenceQueue'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ReferenceQueue()
    
    """
    def __init__(self): ...
    def poll(self) -> Reference[_ReferenceQueue__T]: ...
    @typing.overload
    def remove(self) -> Reference[_ReferenceQueue__T]: ...
    @typing.overload
    def remove(self, long: int) -> Reference[_ReferenceQueue__T]: ...

_PhantomReference__T = typing.TypeVar('_PhantomReference__T')  # <T>
class PhantomReference(Reference[_PhantomReference__T], typing.Generic[_PhantomReference__T]):
    """
    Java class 'java.lang.ref.PhantomReference'
    
        Extends:
            java.lang.ref.Reference
    
      Constructors:
        * PhantomReference(java.lang.Object, java.lang.ref.ReferenceQueue)
    
    """
    def __init__(self, t: _PhantomReference__T, referenceQueue: ReferenceQueue[_PhantomReference__T]): ...
    def get(self) -> _PhantomReference__T: ...

_SoftReference__T = typing.TypeVar('_SoftReference__T')  # <T>
class SoftReference(Reference[_SoftReference__T], typing.Generic[_SoftReference__T]):
    """
    Java class 'java.lang.ref.SoftReference'
    
        Extends:
            java.lang.ref.Reference
    
      Constructors:
        * SoftReference(java.lang.Object)
        * SoftReference(java.lang.Object, java.lang.ref.ReferenceQueue)
    
    """
    @typing.overload
    def __init__(self, t: _SoftReference__T): ...
    @typing.overload
    def __init__(self, t: _SoftReference__T, referenceQueue: ReferenceQueue[_SoftReference__T]): ...
    def get(self) -> _SoftReference__T: ...

_WeakReference__T = typing.TypeVar('_WeakReference__T')  # <T>
class WeakReference(Reference[_WeakReference__T], typing.Generic[_WeakReference__T]):
    """
    Java class 'java.lang.ref.WeakReference'
    
        Extends:
            java.lang.ref.Reference
    
      Constructors:
        * WeakReference(java.lang.Object)
        * WeakReference(java.lang.Object, java.lang.ref.ReferenceQueue)
    
    """
    @typing.overload
    def __init__(self, t: _WeakReference__T): ...
    @typing.overload
    def __init__(self, t: _WeakReference__T, referenceQueue: ReferenceQueue[_WeakReference__T]): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.lang.ref")``.

    Cleaner: typing.Type[Cleaner]
    PhantomReference: typing.Type[PhantomReference]
    Reference: typing.Type[Reference]
    ReferenceQueue: typing.Type[ReferenceQueue]
    SoftReference: typing.Type[SoftReference]
    WeakReference: typing.Type[WeakReference]
