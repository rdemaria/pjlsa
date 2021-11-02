import cern.accsoft.commons.util.trigger.impl
import java.time
import java.util
import typing



_Trigger__E = typing.TypeVar('_Trigger__E', bound='TriggerEvent')  # <E>
class Trigger(typing.Generic[_Trigger__E]):
    """
    public interface Trigger<E extends :class:`~cern.accsoft.commons.util.trigger.TriggerEvent`>
    
        Interface for a component triggering actions.
    """
    def addTriggerListener(self, triggerListener: typing.Union['TriggerListener'[_Trigger__E], typing.Callable[[_Trigger__E], None]]) -> None: ...
    def removeTriggerListener(self, triggerListener: typing.Union['TriggerListener'[_Trigger__E], typing.Callable[[_Trigger__E], None]]) -> None: ...
    def setTriggerListeners(self, collection: typing.Union[java.util.Collection['TriggerListener'[_Trigger__E]], typing.Sequence['TriggerListener'[_Trigger__E]]]) -> None: ...

class TriggerEvent:
    """
    public interface TriggerEvent
    
        Information about triggered event.
    """
    def getTimestamp(self) -> java.time.Instant:
        """
        
            Returns:
                trigger timestamp
        
        
        """
        ...

_TriggerListener__E = typing.TypeVar('_TriggerListener__E', bound=TriggerEvent)  # <E>
class TriggerListener(typing.Generic[_TriggerListener__E]):
    """
    `@FunctionalInterface <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/FunctionalInterface.html?is-external=true>` public interface TriggerListener<E extends :class:`~cern.accsoft.commons.util.trigger.TriggerEvent`>
    
        Listener for trigger events.
    """
    def onTriggerEvent(self, e: _TriggerListener__E) -> None:
        """
            Callback on the trigger event.
        
            Parameters:
                triggerEvent (:class:`~cern.accsoft.commons.util.trigger.TriggerListener`): the triggered event information
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.trigger")``.

    Trigger: typing.Type[Trigger]
    TriggerEvent: typing.Type[TriggerEvent]
    TriggerListener: typing.Type[TriggerListener]
    impl: cern.accsoft.commons.util.trigger.impl.__module_protocol__
