import cern.accsoft.commons.util.trigger
import datetime
import java.time
import java.util
import java.util.concurrent
import typing



_AbstractTrigger__E = typing.TypeVar('_AbstractTrigger__E', bound=cern.accsoft.commons.util.trigger.TriggerEvent)  # <E>
class AbstractTrigger(cern.accsoft.commons.util.trigger.Trigger[_AbstractTrigger__E], typing.Generic[_AbstractTrigger__E]):
    """
    Java class 'cern.accsoft.commons.util.trigger.impl.AbstractTrigger'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.trigger.Trigger
    
      Constructors:
        * AbstractTrigger()
    
    """
    def __init__(self): ...
    def addTriggerListener(self, triggerListener: typing.Union[cern.accsoft.commons.util.trigger.TriggerListener[_AbstractTrigger__E], typing.Callable[[_AbstractTrigger__E], None]]) -> None: ...
    def removeTriggerListener(self, triggerListener: typing.Union[cern.accsoft.commons.util.trigger.TriggerListener[_AbstractTrigger__E], typing.Callable[[_AbstractTrigger__E], None]]) -> None: ...
    def setDispatchExecutor(self, executor: java.util.concurrent.Executor) -> None: ...
    def setTriggerListeners(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.util.trigger.TriggerListener[_AbstractTrigger__E]], typing.Sequence[cern.accsoft.commons.util.trigger.TriggerListener[_AbstractTrigger__E]]]) -> None: ...

class TriggerEventImpl(cern.accsoft.commons.util.trigger.TriggerEvent):
    """
    Java class 'cern.accsoft.commons.util.trigger.impl.TriggerEventImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.trigger.TriggerEvent
    
      Constructors:
        * TriggerEventImpl(java.time.Instant)
    
    """
    def __init__(self, instant: typing.Union[java.time.Instant, datetime.datetime]): ...
    def getTimestamp(self) -> java.time.Instant: ...
    def toString(self) -> str: ...

_AbstractTimerTrigger__E = typing.TypeVar('_AbstractTimerTrigger__E', bound=cern.accsoft.commons.util.trigger.TriggerEvent)  # <E>
class AbstractTimerTrigger(AbstractTrigger[_AbstractTimerTrigger__E], typing.Generic[_AbstractTimerTrigger__E]):
    """
    Java class 'cern.accsoft.commons.util.trigger.impl.AbstractTimerTrigger'
    
        Extends:
            cern.accsoft.commons.util.trigger.impl.AbstractTrigger
    
      Constructors:
        * AbstractTimerTrigger(java.time.Duration)
    
    """
    def __init__(self, duration: java.time.Duration): ...
    def init(self) -> None: ...
    def setTimerExecutorService(self, scheduledExecutorService: java.util.concurrent.ScheduledExecutorService) -> None: ...

class DefaultTimerTrigger(AbstractTimerTrigger[TriggerEventImpl]):
    """
    Java class 'cern.accsoft.commons.util.trigger.impl.DefaultTimerTrigger'
    
        Extends:
            cern.accsoft.commons.util.trigger.impl.AbstractTimerTrigger
    
      Constructors:
        * DefaultTimerTrigger(java.time.Duration)
    
    """
    def __init__(self, duration: java.time.Duration): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.trigger.impl")``.

    AbstractTimerTrigger: typing.Type[AbstractTimerTrigger]
    AbstractTrigger: typing.Type[AbstractTrigger]
    DefaultTimerTrigger: typing.Type[DefaultTimerTrigger]
    TriggerEventImpl: typing.Type[TriggerEventImpl]
