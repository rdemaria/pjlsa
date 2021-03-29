import java.time
import java.util
import typing


_Trigger__E = typing.TypeVar('_Trigger__E', bound='TriggerEvent')  # <E>
class Trigger(typing.Generic[_Trigger__E]):
    def addTriggerListener(self, triggerListener: typing.Union['TriggerListener'[_Trigger__E], typing.Callable[[_Trigger__E], None]]) -> None: ...
    def removeTriggerListener(self, triggerListener: typing.Union['TriggerListener'[_Trigger__E], typing.Callable[[_Trigger__E], None]]) -> None: ...
    def setTriggerListeners(self, collection: typing.Union[java.util.Collection['TriggerListener'[_Trigger__E]], typing.Sequence['TriggerListener'[_Trigger__E]]]) -> None: ...

class TriggerEvent:
    def getTimestamp(self) -> java.time.Instant: ...

_TriggerListener__E = typing.TypeVar('_TriggerListener__E', bound=TriggerEvent)  # <E>
class TriggerListener(typing.Generic[_TriggerListener__E]):
    def onTriggerEvent(self, e: _TriggerListener__E) -> None: ...
