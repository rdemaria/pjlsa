import cern.accsoft.commons.diag
import java.lang
import typing



class ReloadableThrowableResolver(cern.accsoft.commons.diag.ThrowableResolver):
    """
    public interface ReloadableThrowableResolver extends :class:`~cern.accsoft.commons.diag.ThrowableResolver`
    """
    def reloadThrowableMatcherHierarchy(self) -> None: ...

class ThrowableMatcherException(java.lang.Exception):
    """
    public class ThrowableMatcherException extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, throwable: java.lang.Throwable): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.config")``.

    ReloadableThrowableResolver: typing.Type[ReloadableThrowableResolver]
    ThrowableMatcherException: typing.Type[ThrowableMatcherException]
