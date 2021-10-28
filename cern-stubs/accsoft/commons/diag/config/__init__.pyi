import cern.accsoft.commons.diag
import java.lang
import typing



class ReloadableThrowableResolver(cern.accsoft.commons.diag.ThrowableResolver):
    """
    Java class 'cern.accsoft.commons.diag.config.ReloadableThrowableResolver'
    
        Interfaces:
            cern.accsoft.commons.diag.ThrowableResolver
    
    """
    def reloadThrowableMatcherHierarchy(self) -> None: ...

class ThrowableMatcherException(java.lang.Exception):
    """
    Java class 'cern.accsoft.commons.diag.config.ThrowableMatcherException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ThrowableMatcherException(java.lang.String, java.lang.Throwable)
    
    """
    def __init__(self, string: str, throwable: java.lang.Throwable): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.config")``.

    ReloadableThrowableResolver: typing.Type[ReloadableThrowableResolver]
    ThrowableMatcherException: typing.Type[ThrowableMatcherException]
