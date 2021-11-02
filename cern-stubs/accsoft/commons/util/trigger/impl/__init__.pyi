import cern.accsoft.commons.util.trigger
import datetime
import java.time
import java.util
import java.util.concurrent
import typing



_AbstractTrigger__E = typing.TypeVar('_AbstractTrigger__E', bound=cern.accsoft.commons.util.trigger.TriggerEvent)  # <E>
class AbstractTrigger(cern.accsoft.commons.util.trigger.Trigger[_AbstractTrigger__E], typing.Generic[_AbstractTrigger__E]):
    """
    public abstract class AbstractTrigger<E extends :class:`~cern.accsoft.commons.util.trigger.TriggerEvent`> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.trigger.Trigger`<E>
    """
    def __init__(self): ...
    def addTriggerListener(self, triggerListener: typing.Union[cern.accsoft.commons.util.trigger.TriggerListener[_AbstractTrigger__E], typing.Callable[[_AbstractTrigger__E], None]]) -> None: ...
    def removeTriggerListener(self, triggerListener: typing.Union[cern.accsoft.commons.util.trigger.TriggerListener[_AbstractTrigger__E], typing.Callable[[_AbstractTrigger__E], None]]) -> None: ...
    def setDispatchExecutor(self, executor: java.util.concurrent.Executor) -> None: ...
    def setTriggerListeners(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.util.trigger.TriggerListener[_AbstractTrigger__E]], typing.Sequence[cern.accsoft.commons.util.trigger.TriggerListener[_AbstractTrigger__E]]]) -> None: ...

class TriggerEventImpl(cern.accsoft.commons.util.trigger.TriggerEvent):
    """
    public class TriggerEventImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.trigger.TriggerEvent`
    """
    def __init__(self, instant: typing.Union[java.time.Instant, datetime.datetime]): ...
    def getTimestamp(self) -> java.time.Instant:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.trigger.TriggerEvent.getTimestamp`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.trigger.TriggerEvent`
        
            Returns:
                trigger timestamp
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_AbstractTimerTrigger__E = typing.TypeVar('_AbstractTimerTrigger__E', bound=cern.accsoft.commons.util.trigger.TriggerEvent)  # <E>
class AbstractTimerTrigger(AbstractTrigger[_AbstractTimerTrigger__E], typing.Generic[_AbstractTimerTrigger__E]):
    """
    public abstract class AbstractTimerTrigger<E extends :class:`~cern.accsoft.commons.util.trigger.TriggerEvent`> extends :class:`~cern.accsoft.commons.util.trigger.impl.AbstractTrigger`<E>
    
        Abstract :class:`~cern.accsoft.commons.util.trigger.Trigger` implementation based on timer.
    """
    def __init__(self, duration: java.time.Duration): ...
    def init(self) -> None:
        """
            Trigger initialization method.
        
        """
        ...
    def setTimerExecutorService(self, scheduledExecutorService: java.util.concurrent.ScheduledExecutorService) -> None:
        """
        
            Parameters:
                timerExecutorService (`ScheduledExecutorService <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/ScheduledExecutorService.html?is-external=true>`): `null
                    <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/ScheduledExecutorService.html?is-external=true>`
                    to use
        
        
        """
        ...

class DefaultTimerTrigger(AbstractTimerTrigger[TriggerEventImpl]):
    """
    public class DefaultTimerTrigger extends :class:`~cern.accsoft.commons.util.trigger.impl.AbstractTimerTrigger`<:class:`~cern.accsoft.commons.util.trigger.impl.TriggerEventImpl`>
    
        Default :class:`~cern.accsoft.commons.util.trigger.Trigger` implementation based on timer.
    """
    def __init__(self, duration: java.time.Duration): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.trigger.impl")``.

    AbstractTimerTrigger: typing.Type[AbstractTimerTrigger]
    AbstractTrigger: typing.Type[AbstractTrigger]
    DefaultTimerTrigger: typing.Type[DefaultTimerTrigger]
    TriggerEventImpl: typing.Type[TriggerEventImpl]
