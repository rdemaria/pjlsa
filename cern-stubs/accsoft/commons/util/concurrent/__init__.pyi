import java.lang
import java.util
import java.util.concurrent
import typing



class DefaultThreadFactory(java.util.concurrent.ThreadFactory):
    """
    public class DefaultThreadFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `ThreadFactory <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/ThreadFactory.html?is-external=true>`
    
        Thread factory to be used for executors instead of the default thread factory provided with `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/Executors.html?is-external=true#defaultThreadFactory()>`
        method. This class names the newly created threads with a prefix provided by the creator via constructor argument. For
        example, providing the :code:`threadNamePrefix` argument with the value of "MyExecutor-thread-" will result the newly
        created threads to be named "MyExecutor-thread-1", ..., "MyExecutor-thread-225", etc.
    
        The template is taken from `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/Executors.html?is-external=true>`
        DefaultThreadFactory inner class.
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    def newThread(self, runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> java.lang.Thread:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...

_ResourceSynchronizationHelper__Command__R = typing.TypeVar('_ResourceSynchronizationHelper__Command__R')  # <R>
_ResourceSynchronizationHelper__T = typing.TypeVar('_ResourceSynchronizationHelper__T')  # <T>
class ResourceSynchronizationHelper(typing.Generic[_ResourceSynchronizationHelper__T]):
    """
    public class ResourceSynchronizationHelper<T> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Synchronizes access to (potentially overlapping) sets of resources. Every resource must be identified with a unique ID.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, comparator: typing.Union[java.util.Comparator[_ResourceSynchronizationHelper__T], typing.Callable[[_ResourceSynchronizationHelper__T, _ResourceSynchronizationHelper__T], int]]): ...
    _executeCommand__R = typing.TypeVar('_executeCommand__R')  # <R>
    def executeCommand(self, collection: typing.Union[java.util.Collection[_ResourceSynchronizationHelper__T], typing.Sequence[_ResourceSynchronizationHelper__T]], command: 'ResourceSynchronizationHelper.Command'[_executeCommand__R]) -> _executeCommand__R: ...
    class Command(typing.Generic[_ResourceSynchronizationHelper__Command__R]):
        def execute(self) -> _ResourceSynchronizationHelper__Command__R: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.concurrent")``.

    DefaultThreadFactory: typing.Type[DefaultThreadFactory]
    ResourceSynchronizationHelper: typing.Type[ResourceSynchronizationHelper]
