import cern.accsoft.commons.util
import cern.japc.core
import cern.japc.core.device.impl
import cern.japc.core.transaction
import java.util
import typing



class JapcDevice(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.japc.core.device.JapcDevice'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getImmutableParameter(self, string: str) -> cern.japc.core.ImmutableParameter: ...
    def getParameter(self, string: str) -> cern.japc.core.Parameter: ...
    def getPropertyNames(self) -> java.util.Set[str]: ...
    def getTransactionalParameter(self, string: str) -> cern.japc.core.transaction.TransactionalParameter: ...
    def getWritablePropertyNames(self) -> java.util.Set[str]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.device")``.

    JapcDevice: typing.Type[JapcDevice]
    impl: cern.japc.core.device.impl.__module_protocol__
