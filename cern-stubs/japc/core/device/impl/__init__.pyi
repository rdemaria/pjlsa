import cern.accsoft.commons.util
import cern.japc.core
import cern.japc.core.device
import cern.japc.core.transaction
import java.util
import typing



class JapcDeviceImpl(cern.accsoft.commons.util.AbstractNamed[cern.japc.core.device.JapcDevice], cern.japc.core.device.JapcDevice):
    """
    Java class 'cern.japc.core.device.impl.JapcDeviceImpl'
    
        Extends:
            cern.accsoft.commons.util.AbstractNamed
    
        Interfaces:
            cern.japc.core.device.JapcDevice
    
      Constructors:
        * JapcDeviceImpl(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    def addParameter(self, immutableParameter: cern.japc.core.ImmutableParameter) -> None: ...
    def getImmutableParameter(self, string: str) -> cern.japc.core.ImmutableParameter: ...
    def getName(self) -> str: ...
    def getParameter(self, string: str) -> cern.japc.core.Parameter: ...
    def getPropertyNames(self) -> java.util.Set[str]: ...
    def getTransactionalParameter(self, string: str) -> cern.japc.core.transaction.TransactionalParameter: ...
    def getWritablePropertyNames(self) -> java.util.Set[str]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.device.impl")``.

    JapcDeviceImpl: typing.Type[JapcDeviceImpl]
