import cern.accsoft.commons.util.trigger
import cern.accsoft.commons.util.trigger.impl
import cern.japc.core.factory
import typing



_AbstractJapcTrigger__E = typing.TypeVar('_AbstractJapcTrigger__E', bound=cern.accsoft.commons.util.trigger.TriggerEvent)  # <E>
class AbstractJapcTrigger(cern.accsoft.commons.util.trigger.impl.AbstractTrigger[_AbstractJapcTrigger__E], typing.Generic[_AbstractJapcTrigger__E]):
    """
    public abstract class AbstractJapcTrigger<E extends cern.accsoft.commons.util.trigger.TriggerEvent> extends cern.accsoft.commons.util.trigger.impl.AbstractTrigger<E>
    
        Trigger implementation based on JAPC updates.
    """
    def __init__(self, string: str): ...
    def init(self) -> None: ...
    def setParameterFactory(self, parameterFactory: cern.japc.core.factory.ParameterFactory) -> None:
        """
        
            Parameters:
                parameterFactory (:class:`~cern.japc.core.factory.ParameterFactory`): :class:`~cern.japc.core.factory.ParameterFactory` to use
        
        
        """
        ...
    def setTriggerSelector(self, string: str) -> None:
        """
        
            Parameters:
                triggerSelector (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): JAPC selector for triggering parameter subscription
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.trigger")``.

    AbstractJapcTrigger: typing.Type[AbstractJapcTrigger]
