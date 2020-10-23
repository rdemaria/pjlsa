import cern.accsoft.commons.util
import cern.japc.core
import cern.japc.core.transaction
import java.util


class JapcDevice(cern.accsoft.commons.util.Named):
    def getImmutableParameter(self, string: str) -> cern.japc.core.ImmutableParameter: ...
    def getParameter(self, string: str) -> cern.japc.core.Parameter: ...
    def getPropertyNames(self) -> java.util.Set[str]: ...
    def getTransactionalParameter(self, string: str) -> cern.japc.core.transaction.TransactionalParameter: ...
    def getWritablePropertyNames(self) -> java.util.Set[str]: ...