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
    """
    Java class 'cern.accsoft.commons.util.event.EventListenerSupport'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * EventListenerSupport(java.lang.Class)
        * EventListenerSupport(java.lang.Class, cern.accsoft.commons.util.reflect.MethodInvoker)
    
    """
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
    Java class 'cern.accsoft.commons.util.event.EventListeners'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * EventListeners()
    
    """
    def __init__(self): ...
    @staticmethod
    def actionListener(object: typing.Any, string: str) -> java.awt.event.ActionListener: ...
    @staticmethod
    def changeListener(object: typing.Any, string: str) -> javax.swing.event.ChangeListener: ...
    _create_0__T = typing.TypeVar('_create_0__T')  # <T>
    _create_1__T = typing.TypeVar('_create_1__T')  # <T>
    @typing.overload
    @staticmethod
    def create(class_: typing.Type[_create_0__T], object: typing.Any, string: str) -> _create_0__T: ...
    @typing.overload
    @staticmethod
    def create(class_: typing.Type[_create_1__T], object: typing.Any, string: str, string2: str) -> _create_1__T: ...
    @staticmethod
    def listSelectionListener(object: typing.Any, string: str) -> javax.swing.event.ListSelectionListener: ...
    @staticmethod
    def propertyChangeListener(object: typing.Any, string: str) -> java.beans.PropertyChangeListener: ...

_SyncEventListenerSupport__T = typing.TypeVar('_SyncEventListenerSupport__T')  # <T>
class SyncEventListenerSupport(EventListenerSupport[_SyncEventListenerSupport__T], typing.Generic[_SyncEventListenerSupport__T]):
    """
    Java class 'cern.accsoft.commons.util.event.SyncEventListenerSupport'
    
        Extends:
            cern.accsoft.commons.util.event.EventListenerSupport
    
      Constructors:
        * SyncEventListenerSupport(java.lang.Class)
        * SyncEventListenerSupport(java.lang.Class, cern.accsoft.commons.util.reflect.MethodInvoker)
    
    """
    @typing.overload
    def __init__(self, class_: typing.Type[_SyncEventListenerSupport__T]): ...
    @typing.overload
    def __init__(self, class_: typing.Type[_SyncEventListenerSupport__T], methodInvoker: cern.accsoft.commons.util.reflect.MethodInvoker): ...
    def clear(self) -> None: ...
    def getListeners(self) -> java.util.List[_SyncEventListenerSupport__T]: ...
    _newInstance_0__T = typing.TypeVar('_newInstance_0__T')  # <T>
    _newInstance_1__T = typing.TypeVar('_newInstance_1__T')  # <T>
    @typing.overload
    @staticmethod
    def newInstance(class_: typing.Type[_newInstance_0__T]) -> EventListenerSupport[_newInstance_0__T]: ...
    @typing.overload
    @staticmethod
    def newInstance(class_: typing.Type[_newInstance_1__T]) -> 'SyncEventListenerSupport'[_newInstance_1__T]: ...
    def remove(self, t: _SyncEventListenerSupport__T) -> None: ...

class EventListenerSupportDemo:
    """
    Java class 'cern.accsoft.commons.util.event.EventListenerSupportDemo'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * EventListenerSupportDemo()
    
    """
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    def updateListeners(self) -> None: ...
    class MyListenerImpl(cern.accsoft.commons.util.event.EventListenerSupportDemo.MyListener, cern.accsoft.commons.util.event.EventListenerSupportDemo.ParameterValueListener):
        """
        Java class 'cern.accsoft.commons.util.event.EventListenerSupportDemo$MyListenerImpl'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                cern.accsoft.commons.util.event.EventListenerSupportDemo.MyLis
                tener, cern.accsoft.commons.util.event.EventListenerSupportDem
                o.ParameterValueListener
        
          Constructors:
            * MyListenerImpl(cern.accsoft.commons.util.event.EventListenerSupportDemo, java.lang.String)
        
        """
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
