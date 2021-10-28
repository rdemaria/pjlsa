import cern.accsoft.commons.util.trigger.impl
import java.time
import java.util
import typing



_Trigger__E = typing.TypeVar('_Trigger__E', bound='TriggerEvent')  # <E>
class Trigger(typing.Generic[_Trigger__E]):
    """
    Java class 'cern.accsoft.commons.util.trigger.Trigger'
    
    """
    def addTriggerListener(self, triggerListener: typing.Union['TriggerListener'[_Trigger__E], typing.Callable[[_Trigger__E], None]]) -> None: ...
    def removeTriggerListener(self, triggerListener: typing.Union['TriggerListener'[_Trigger__E], typing.Callable[[_Trigger__E], None]]) -> None: ...
    def setTriggerListeners(self, collection: typing.Union[java.util.Collection['TriggerListener'[_Trigger__E]], typing.Sequence['TriggerListener'[_Trigger__E]]]) -> None: ...

class TriggerEvent:
    """
    Java class 'cern.accsoft.commons.util.trigger.TriggerEvent'
    
    """
    def getTimestamp(self) -> java.time.Instant: ...

_TriggerListener__E = typing.TypeVar('_TriggerListener__E', bound=TriggerEvent)  # <E>
class TriggerListener(typing.Generic[_TriggerListener__E]):
    """
    Java class 'cern.accsoft.commons.util.trigger.TriggerListener'
    
    """
    def onTriggerEvent(self, e: _TriggerListener__E) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.trigger")``.

    Trigger: typing.Type[Trigger]
    TriggerEvent: typing.Type[TriggerEvent]
    TriggerListener: typing.Type[TriggerListener]
    impl: cern.accsoft.commons.util.trigger.impl.__module_protocol__
