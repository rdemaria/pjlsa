import cern.accsoft.commons.diag
import cern.accsoft.commons.diag.matcher
import java.lang
import typing



class LsaDriveExceptionThrowableMatcher(cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher):
    """
    Java class 'cern.lsa.domain.cern.diag.LsaDriveExceptionThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher
    
      Constructors:
        * LsaDriveExceptionThrowableMatcher()
    
    """
    def __init__(self): ...

class LsaDriveProxyThrowableMatcher(cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher):
    """
    Java class 'cern.lsa.domain.cern.diag.LsaDriveProxyThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher
    
      Constructors:
        * LsaDriveProxyThrowableMatcher()
    
    """
    def __init__(self): ...

class LsaDriveStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.lsa.domain.cern.diag.LsaDriveStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Constructors:
        * LsaDriveStringThrowableMatcher()
    
    """
    def __init__(self): ...

class LsaDriveThrowableMessageComposer(cern.accsoft.commons.diag.DefaultThrowableMessageComposer):
    """
    Java class 'cern.lsa.domain.cern.diag.LsaDriveThrowableMessageComposer'
    
        Extends:
            cern.accsoft.commons.diag.DefaultThrowableMessageComposer
    
      Constructors:
        * LsaDriveThrowableMessageComposer()
    
    """
    def __init__(self): ...
    def composeMessage(self, throwable: java.lang.Throwable) -> str: ...

class LsaStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.lsa.domain.cern.diag.LsaStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Constructors:
        * LsaStringThrowableMatcher()
    
      Attributes:
        LSA_PROBLEM_DOMAIN (java.lang.String): final static field
    
    """
    LSA_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    def __init__(self): ...
    def buildThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor: ...

class LsaThrowableResolver(cern.accsoft.commons.diag.DefaultThrowableResolver):
    """
    Java class 'cern.lsa.domain.cern.diag.LsaThrowableResolver'
    
        Extends:
            cern.accsoft.commons.diag.DefaultThrowableResolver
    
    """
    @staticmethod
    def getInstance() -> 'LsaThrowableResolver': ...

class LsaTrimExceptionThrowableMatcher(cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher):
    """
    Java class 'cern.lsa.domain.cern.diag.LsaTrimExceptionThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher
    
      Constructors:
        * LsaTrimExceptionThrowableMatcher()
    
    """
    def __init__(self): ...

class LsaTrimProxyThrowableMatcher(cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher):
    """
    Java class 'cern.lsa.domain.cern.diag.LsaTrimProxyThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher
    
      Constructors:
        * LsaTrimProxyThrowableMatcher()
    
    """
    def __init__(self): ...

class LsaTrimStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.lsa.domain.cern.diag.LsaTrimStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Constructors:
        * LsaTrimStringThrowableMatcher()
    
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
