import cern.accsoft.commons.diag
import java.lang


class ReloadableThrowableResolver(cern.accsoft.commons.diag.ThrowableResolver):
    def reloadThrowableMatcherHierarchy(self) -> None: ...

class ThrowableMatcherException(java.lang.Exception):
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
