from typing import TypeVar as _py_TypeVar
from typing import Generic as _py_Generic
import java.time
import java.util


_Trigger__E = _py_TypeVar('_Trigger__E', bound='TriggerEvent')  # <E>
class Trigger(_py_Generic[_Trigger__E]):
    def addTriggerListener(self, triggerListener: 'TriggerListener'[_Trigger__E]) -> None: ...
    def removeTriggerListener(self, triggerListener: 'TriggerListener'[_Trigger__E]) -> None: ...
    def setTriggerListeners(self, collection: java.util.Collection['TriggerListener'[_Trigger__E]]) -> None: ...

class TriggerEvent:
    def getTimestamp(self) -> java.time.Instant: ...

_TriggerListener__E = _py_TypeVar('_TriggerListener__E', bound=TriggerEvent)  # <E>
class TriggerListener(_py_Generic[_TriggerListener__E]):
    def onTriggerEvent(self, e: _TriggerListener__E) -> None: ...
