import cern
import cern.accsoft.commons.util.reflect
import java.awt.event
import java.beans
import java.lang
import java.util
import javax.swing.event
import typing



_EventListenerSupport__T = typing.TypeVar('_EventListenerSupport__T')  # <T>
class EventListenerSupport(typing.Generic[_EventListenerSupport__T]):
    @typing.overload
    def __init__(self, class_: typing.Type[_EventListenerSupport__T]): ...
    @typing.overload
    def __init__(self, class_: typing.Type[_EventListenerSupport__T], methodInvoker: cern.accsoft.commons.util.reflect.MethodInvoker): ...
    def add(self, t: _EventListenerSupport__T) -> None: ...
    def addAll(self, collection: typing.Union[java.util.Collection[_EventListenerSupport__T], typing.Sequence[_EventListenerSupport__T]]) -> None: ...
    def addAllWeakly(self, collection: typing.Union[java.util.Collection[_EventListenerSupport__T], typing.Sequence[_EventListenerSupport__T]]) -> None: ...
    def addWeakly(self, t: _EventListenerSupport__T) -> None: ...
    def clear(self) -> None: ...
    def getDispatcher(self) -> _EventListenerSupport__T: ...
    def getListenerInvoker(self) -> cern.accsoft.commons.util.reflect.MethodInvoker: ...
    def getListeners(self) -> java.util.List[_EventListenerSupport__T]: ...
    _newInstance__T = typing.TypeVar('_newInstance__T')  # <T>
    @staticmethod
    def newInstance(class_: typing.Type[_newInstance__T]) -> 'EventListenerSupport'[_newInstance__T]: ...
    def remove(self, t: _EventListenerSupport__T) -> None: ...
    def removeAll(self, collection: typing.Union[java.util.Collection[_EventListenerSupport__T], typing.Sequence[_EventListenerSupport__T]]) -> None: ...

class EventListeners:
    """
    public abstract class EventListeners extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class that allows creation of proxy objects for specified listener interface, that redirect method calls to
        given target object and method.
    
        The specified method in the target object should have no arguments or the argument list should match arguments of the
        listener method.
    
        If the target method is not public (default, private or protected) the proxy will try to make it accessible but whether
        this succeeds depends on the current Security Manager.
    
        **Use this class wisely (do not abuse it). Creating dynamic listeners by passing method name (as :code:`String` ) can be
        dangerous since the method might seem to be not used and can be changed or deleted accidentally. Thus if such method is
        only called from the dynamic event handler created by this class - it should be properly documented.**
    """
    def __init__(self): ...
    @staticmethod
    def actionListener(object: typing.Any, string: str) -> java.awt.event.ActionListener:
        """
            Creates an instance of :code:`ActionListener` that dispatches method call to the specified method.
        
            Parameters:
                target (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the target object
                methodName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the method to be called
        
            Returns:
                dynamic proxy that calls specified target method
        
        
        """
        ...
    @staticmethod
    def changeListener(object: typing.Any, string: str) -> javax.swing.event.ChangeListener:
        """
            Creates an instance of :code:`ChangeListener` that dispatches method call to the specified method.
        
            Parameters:
                target (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the target object
                methodName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the method to be called
        
            Returns:
                dynamic proxy that calls specified target method
        
        
        """
        ...
    _create_0__T = typing.TypeVar('_create_0__T')  # <T>
    _create_1__T = typing.TypeVar('_create_1__T')  # <T>
    @typing.overload
    @staticmethod
    def create(class_: typing.Type[_create_0__T], object: typing.Any, string: str) -> _create_0__T: ...
    @typing.overload
    @staticmethod
    def create(class_: typing.Type[_create_1__T], object: typing.Any, string: str, string2: str) -> _create_1__T: ...
    @staticmethod
    def listSelectionListener(object: typing.Any, string: str) -> javax.swing.event.ListSelectionListener:
        """
            Creates an instance of :code:`ListSelectionListener` that dispatches method call to the specified method.
        
            Parameters:
                target (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the target object
                methodName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the method to be called
        
            Returns:
                dynamic proxy that calls specified target method
        
        
        """
        ...
    @staticmethod
    def propertyChangeListener(object: typing.Any, string: str) -> java.beans.PropertyChangeListener:
        """
            Creates an instance of :code:`PropertyChangeListener` that dispatches method call to the specified method.
        
            Parameters:
                target (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the target object
                methodName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the method to be called
        
            Returns:
                dynamic proxy that calls specified target method
        
        
        """
        ...

_SyncEventListenerSupport__T = typing.TypeVar('_SyncEventListenerSupport__T')  # <T>
class SyncEventListenerSupport(EventListenerSupport[_SyncEventListenerSupport__T], typing.Generic[_SyncEventListenerSupport__T]):
    """
    public class SyncEventListenerSupport<T> extends :class:`~cern.accsoft.commons.util.event.EventListenerSupport`<T>
    
        Synchronized version of :class:`~cern.accsoft.commons.util.event.EventListenerSupport` which allows to add/remove
        listeners in a safe manner while the support is in use.
    """
    @typing.overload
    def __init__(self, class_: typing.Type[_SyncEventListenerSupport__T]): ...
    @typing.overload
    def __init__(self, class_: typing.Type[_SyncEventListenerSupport__T], methodInvoker: cern.accsoft.commons.util.reflect.MethodInvoker): ...
    def clear(self) -> None:
        """
            Description copied from class: :meth:`~cern.accsoft.commons.util.event.EventListenerSupport.clear`
            Removes all the listeners.
        
            Overrides:
                :meth:`~cern.accsoft.commons.util.event.EventListenerSupport.clear`Â in
                classÂ :class:`~cern.accsoft.commons.util.event.EventListenerSupport`
        
        
        """
        ...
    def getListeners(self) -> java.util.List[_SyncEventListenerSupport__T]: ...
    _newInstance_0__T = typing.TypeVar('_newInstance_0__T')  # <T>
    _newInstance_1__T = typing.TypeVar('_newInstance_1__T')  # <T>
    @typing.overload
    @staticmethod
    def newInstance(class_: typing.Type[_newInstance_0__T]) -> EventListenerSupport[_newInstance_0__T]: ...
    @typing.overload
    @staticmethod
    def newInstance(class_: typing.Type[_newInstance_1__T]) -> 'SyncEventListenerSupport'[_newInstance_1__T]: ...
    def remove(self, t: _SyncEventListenerSupport__T) -> None:
        """
            Description copied from class: :meth:`~cern.accsoft.commons.util.event.EventListenerSupport.remove`
            Removes specified listener.
        
            Overrides:
                :meth:`~cern.accsoft.commons.util.event.EventListenerSupport.remove`Â in
                classÂ :class:`~cern.accsoft.commons.util.event.EventListenerSupport`
        
            Parameters:
                listener (:class:`~cern.accsoft.commons.util.event.SyncEventListenerSupport`): listener to be removed
        
        
        """
        ...

class EventListenerSupportDemo:
    """
    public class EventListenerSupportDemo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Small demo class for :class:`~cern.accsoft.commons.util.event.EventListenerSupport`
    """
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    def updateListeners(self) -> None:
        """
            Hypothetical method that does some calculates and then updates the listeners using the proxy
        
        """
        ...
    class MyListenerImpl(cern.accsoft.commons.util.event.EventListenerSupportDemo.MyListener, cern.accsoft.commons.util.event.EventListenerSupportDemo.ParameterValueListener):
        def __init__(self, eventListenerSupportDemo: 'EventListenerSupportDemo', string: str): ...
        def exceptionOccured(self, string: str, exception: java.lang.Exception) -> None: ...
        def sendUpdate(self, long: int) -> None: ...
        def valueReceived(self, string: str) -> None: ...
    class MyListener: ...
    class ParameterValueListener: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.event")``.

    EventListenerSupport: typing.Type[EventListenerSupport]
    EventListenerSupportDemo: typing.Type[EventListenerSupportDemo]
    EventListeners: typing.Type[EventListeners]
    SyncEventListenerSupport: typing.Type[SyncEventListenerSupport]
