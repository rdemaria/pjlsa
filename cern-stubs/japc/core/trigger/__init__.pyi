import cern.accsoft.commons.util.trigger
import cern.accsoft.commons.util.trigger.impl
import cern.japc.core.factory
import typing



_AbstractJapcTrigger__E = typing.TypeVar('_AbstractJapcTrigger__E', bound=cern.accsoft.commons.util.trigger.TriggerEvent)  # <E>
class AbstractJapcTrigger(cern.accsoft.commons.util.trigger.impl.AbstractTrigger[_AbstractJapcTrigger__E], typing.Generic[_AbstractJapcTrigger__E]):
    """
    Java class 'cern.japc.core.trigger.AbstractJapcTrigger'
    
        Extends:
            cern.accsoft.commons.util.trigger.impl.AbstractTrigger
    
      Constructors:
        * AbstractJapcTrigger(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    def init(self) -> None: ...
    def setParameterFactory(self, parameterFactory: cern.japc.core.factory.ParameterFactory) -> None: ...
    def setTriggerSelector(self, string: str) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.trigger")``.

    AbstractJapcTrigger: typing.Type[AbstractJapcTrigger]
