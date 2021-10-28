import cern.accsoft.commons.diag
import cern.accsoft.commons.diag.matcher.ccdb
import cern.accsoft.commons.diag.matcher.cmw
import cern.accsoft.commons.diag.matcher.japc
import cern.accsoft.commons.diag.matcher.rbac
import cern.accsoft.commons.diag.matcher.tgm
import cern.accsoft.commons.util
import java.lang
import typing



class ThrowableMatcher(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.accsoft.commons.diag.matcher.ThrowableMatcher'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def findThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor: ...

class ThrowableMatcherHierarchyImpl(cern.accsoft.commons.diag.HierarchyImpl[ThrowableMatcher]):
    """
    Java class 'cern.accsoft.commons.diag.matcher.ThrowableMatcherHierarchyImpl'
    
        Extends:
            cern.accsoft.commons.diag.HierarchyImpl
    
      Constructors:
        * ThrowableMatcherHierarchyImpl()
    
    """
    def __init__(self): ...

class AbstractThrowableMatcher(ThrowableMatcherHierarchyImpl, ThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.AbstractThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.ThrowableMatcherHierarchyImpl
    
        Interfaces:
            cern.accsoft.commons.diag.matcher.ThrowableMatcher
    
      Constructors:
        * AbstractThrowableMatcher(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    @staticmethod
    def extractExceptionMessage(throwable: java.lang.Throwable, boolean: bool) -> str: ...
    def findThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor: ...
    def getName(self) -> str: ...
    def toString(self) -> str: ...

class ProxyThrowableMatcher(ThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.diag.matcher.ThrowableMatcher
    
      Constructors:
        * ProxyThrowableMatcher(java.lang.Class, cern.accsoft.commons.diag.matcher.ThrowableMatcher)
    
    """
    def __init__(self, class_: typing.Type[ThrowableMatcher], throwableMatcher: ThrowableMatcher): ...
    def findThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor: ...
    def getName(self) -> str: ...
    def toString(self) -> str: ...

class ThrowableMatcherDecoratorSupport(ThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.ThrowableMatcherDecoratorSupport'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.diag.matcher.ThrowableMatcher
    
      Constructors:
        * ThrowableMatcherDecoratorSupport(cern.accsoft.commons.diag.matcher.ThrowableMatcher)
    
    """
    def __init__(self, throwableMatcher: ThrowableMatcher): ...
    def findThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor: ...
    def getName(self) -> str: ...
    def toString(self) -> str: ...

class ExceptionClassThrowableMatcher(AbstractThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.AbstractThrowableMatcher
    
      Constructors:
        * ExceptionClassThrowableMatcher(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.Class, java.lang.String)
    
    """
    def __init__(self, string: str, string2: str, string3: str, string4: str, class_: typing.Type[java.lang.Throwable], string5: str): ...

class StringThrowableMatcher(AbstractThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.StringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.AbstractThrowableMatcher
    
      Constructors:
        * StringThrowableMatcher(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)
    
    """
    def __init__(self, string: str, string2: str, string3: str, string4: str, string5: str, string6: str): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher")``.

    AbstractThrowableMatcher: typing.Type[AbstractThrowableMatcher]
    ExceptionClassThrowableMatcher: typing.Type[ExceptionClassThrowableMatcher]
    ProxyThrowableMatcher: typing.Type[ProxyThrowableMatcher]
    StringThrowableMatcher: typing.Type[StringThrowableMatcher]
    ThrowableMatcher: typing.Type[ThrowableMatcher]
    ThrowableMatcherDecoratorSupport: typing.Type[ThrowableMatcherDecoratorSupport]
    ThrowableMatcherHierarchyImpl: typing.Type[ThrowableMatcherHierarchyImpl]
    ccdb: cern.accsoft.commons.diag.matcher.ccdb.__module_protocol__
    cmw: cern.accsoft.commons.diag.matcher.cmw.__module_protocol__
    japc: cern.accsoft.commons.diag.matcher.japc.__module_protocol__
    rbac: cern.accsoft.commons.diag.matcher.rbac.__module_protocol__
    tgm: cern.accsoft.commons.diag.matcher.tgm.__module_protocol__
