import cern.accsoft.commons.diag
import cern.accsoft.commons.diag.matcher
import java.lang
import typing



class LsaDriveExceptionThrowableMatcher(cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher):
    """
    public class LsaDriveExceptionThrowableMatcher extends cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher
    """
    def __init__(self): ...

class LsaDriveProxyThrowableMatcher(cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher):
    """
    public class LsaDriveProxyThrowableMatcher extends cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher
    """
    def __init__(self): ...

class LsaDriveStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public class LsaDriveStringThrowableMatcher extends cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    """
    def __init__(self): ...

class LsaDriveThrowableMessageComposer(cern.accsoft.commons.diag.DefaultThrowableMessageComposer):
    """
    public class LsaDriveThrowableMessageComposer extends cern.accsoft.commons.diag.DefaultThrowableMessageComposer
    """
    def __init__(self): ...
    def composeMessage(self, throwable: java.lang.Throwable) -> str:
        """
        
            Specified by:
                :code:`composeMessage` in interface :code:`cern.accsoft.commons.diag.ThrowableMessageComposer`
        
            Overrides:
                :code:`composeMessage` in class :code:`cern.accsoft.commons.diag.DefaultThrowableMessageComposer`
        
        
        """
        ...

class LsaStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public class LsaStringThrowableMatcher extends cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    """
    LSA_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` LSA_PROBLEM_DOMAIN
    
        LSA problem domain
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def buildThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor:
        """
        
            Overrides:
                :code:`buildThrowableDescriptor` in class :code:`cern.accsoft.commons.diag.matcher.AbstractThrowableMatcher`
        
        
        """
        ...

class LsaThrowableResolver(cern.accsoft.commons.diag.DefaultThrowableResolver):
    """
    public class LsaThrowableResolver extends cern.accsoft.commons.diag.DefaultThrowableResolver
    """
    @staticmethod
    def getInstance() -> 'LsaThrowableResolver': ...

class LsaTrimExceptionThrowableMatcher(cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher):
    """
    public class LsaTrimExceptionThrowableMatcher extends cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher
    """
    def __init__(self): ...

class LsaTrimProxyThrowableMatcher(cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher):
    """
    public class LsaTrimProxyThrowableMatcher extends cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher
    """
    def __init__(self): ...

class LsaTrimStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public class LsaTrimStringThrowableMatcher extends cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.diag")``.

    LsaDriveExceptionThrowableMatcher: typing.Type[LsaDriveExceptionThrowableMatcher]
    LsaDriveProxyThrowableMatcher: typing.Type[LsaDriveProxyThrowableMatcher]
    LsaDriveStringThrowableMatcher: typing.Type[LsaDriveStringThrowableMatcher]
    LsaDriveThrowableMessageComposer: typing.Type[LsaDriveThrowableMessageComposer]
    LsaStringThrowableMatcher: typing.Type[LsaStringThrowableMatcher]
    LsaThrowableResolver: typing.Type[LsaThrowableResolver]
    LsaTrimExceptionThrowableMatcher: typing.Type[LsaTrimExceptionThrowableMatcher]
    LsaTrimProxyThrowableMatcher: typing.Type[LsaTrimProxyThrowableMatcher]
    LsaTrimStringThrowableMatcher: typing.Type[LsaTrimStringThrowableMatcher]
