from typing import ClassVar as _py_ClassVar
import cern.accsoft.commons.diag
import cern.accsoft.commons.diag.matcher
import java.lang


class LsaDriveExceptionThrowableMatcher(cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher):
    def __init__(self): ...

class LsaDriveProxyThrowableMatcher(cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher):
    def __init__(self): ...

class LsaDriveStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    def __init__(self): ...

class LsaDriveThrowableMessageComposer(cern.accsoft.commons.diag.DefaultThrowableMessageComposer):
    def __init__(self): ...
    def composeMessage(self, throwable: java.lang.Throwable) -> str: ...

class LsaStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    LSA_PROBLEM_DOMAIN: _py_ClassVar[str] = ...
    def __init__(self): ...
    def buildThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor: ...

class LsaThrowableResolver(cern.accsoft.commons.diag.DefaultThrowableResolver):
    @classmethod
    def getInstance(cls) -> 'LsaThrowableResolver': ...

class LsaTrimExceptionThrowableMatcher(cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher):
    def __init__(self): ...

class LsaTrimProxyThrowableMatcher(cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher):
    def __init__(self): ...

class LsaTrimStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    def __init__(self): ...
