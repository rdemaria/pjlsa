import cern.accsoft.commons.diag.config
import cern.accsoft.commons.diag.matcher
import cern.accsoft.commons.util
import java.io
import java.lang
import typing



class ApplicationThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.ApplicationThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Constructors:
        * ApplicationThrowableMatcher()
    
      Attributes:
        APPLICATION_PROBLEM_DOMAIN (java.lang.String): final static field
        APPLICATION_MATCHER_NAME (java.lang.String): final static field
    
    """
    APPLICATION_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    APPLICATION_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...
    def buildThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> 'ThrowableDescriptor': ...

_HierarchyImpl__T = typing.TypeVar('_HierarchyImpl__T', bound=cern.accsoft.commons.util.Named)  # <T>
class HierarchyImpl(typing.Generic[_HierarchyImpl__T]):
    """
    Java class 'cern.accsoft.commons.diag.HierarchyImpl'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * HierarchyImpl()
    
    """
    def __init__(self): ...
    def addChildToEnd(self, t: _HierarchyImpl__T) -> None: ...
    def addChildToTop(self, t: _HierarchyImpl__T) -> None: ...

class ThrowableConstants:
    """
    Java class 'cern.accsoft.commons.diag.ThrowableConstants'
    
      Attributes:
        INDENTATION (java.lang.String): final static field
        BR (java.lang.String): final static field
        END (java.lang.String): final static field
        START_NAME (java.lang.String): final static field
        START_CHILDREN (java.lang.String): final static field
        RESOLVER (java.lang.String): final static field
    
    """
    INDENTATION: typing.ClassVar[str] = ...
    BR: typing.ClassVar[str] = ...
    END: typing.ClassVar[str] = ...
    START_NAME: typing.ClassVar[str] = ...
    START_CHILDREN: typing.ClassVar[str] = ...
    RESOLVER: typing.ClassVar[str] = ...

class ThrowableDescriptor(java.io.Serializable):
    """
    Java class 'cern.accsoft.commons.diag.ThrowableDescriptor'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
    """
    def getContactUrl(self) -> str: ...
    def getFullThrowableStackTrace(self) -> str: ...
    def getHintString(self) -> str: ...
    def getHintUrl(self) -> str: ...
    def getMatchedThrowableStackTrace(self) -> str: ...
    def getMatcherName(self) -> str: ...
    def getMessage(self) -> str: ...
    def getProblemDomain(self) -> str: ...
    def toString(self) -> str: ...
    class ThrowableDescriptorBuilder:
        """
        Java class 'cern.accsoft.commons.diag.ThrowableDescriptor$ThrowableDescriptorBuilder'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * ThrowableDescriptorBuilder()
            * ThrowableDescriptorBuilder(cern.accsoft.commons.diag.ThrowableDescriptor)
        
        """
        @typing.overload
        def __init__(self): ...
        @typing.overload
        def __init__(self, throwableDescriptor: 'ThrowableDescriptor'): ...
        def build(self) -> 'ThrowableDescriptor': ...
        def contactUrl(self, string: str) -> 'ThrowableDescriptor.ThrowableDescriptorBuilder': ...
        def fullThrowableStackTrace(self, string: str) -> 'ThrowableDescriptor.ThrowableDescriptorBuilder': ...
        def hintString(self, string: str) -> 'ThrowableDescriptor.ThrowableDescriptorBuilder': ...
        def hintUrl(self, string: str) -> 'ThrowableDescriptor.ThrowableDescriptorBuilder': ...
        def matchedThrowableStackTrace(self, string: str) -> 'ThrowableDescriptor.ThrowableDescriptorBuilder': ...
        def matcherName(self, string: str) -> 'ThrowableDescriptor.ThrowableDescriptorBuilder': ...
        def message(self, string: str) -> 'ThrowableDescriptor.ThrowableDescriptorBuilder': ...
        def problemDomain(self, string: str) -> 'ThrowableDescriptor.ThrowableDescriptorBuilder': ...

class ThrowableMessageComposer:
    """
    Java class 'cern.accsoft.commons.diag.ThrowableMessageComposer'
    
    """
    def composeMessage(self, throwable: java.lang.Throwable) -> str: ...

class ThrowableResolver:
    """
    Java class 'cern.accsoft.commons.diag.ThrowableResolver'
    
    """
    def resolve(self, throwable: java.lang.Throwable) -> ThrowableDescriptor: ...

class DefaultThrowableMessageComposer(ThrowableMessageComposer):
    """
    Java class 'cern.accsoft.commons.diag.DefaultThrowableMessageComposer'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.diag.ThrowableMessageComposer
    
      Constructors:
        * DefaultThrowableMessageComposer()
    
    """
    def __init__(self): ...
    def composeMessage(self, throwable: java.lang.Throwable) -> str: ...

class EmptyThrowableResolver(cern.accsoft.commons.diag.matcher.ThrowableMatcherHierarchyImpl, ThrowableResolver):
    """
    Java class 'cern.accsoft.commons.diag.EmptyThrowableResolver'
    
        Extends:
            cern.accsoft.commons.diag.matcher.ThrowableMatcherHierarchyImpl
    
        Interfaces:
            cern.accsoft.commons.diag.ThrowableResolver
    
      Constructors:
        * EmptyThrowableResolver()
    
    """
    def __init__(self): ...
    def resolve(self, throwable: java.lang.Throwable) -> ThrowableDescriptor: ...
    def toString(self) -> str: ...

class DefaultThrowableResolver(EmptyThrowableResolver): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag")``.

    ApplicationThrowableMatcher: typing.Type[ApplicationThrowableMatcher]
    DefaultThrowableMessageComposer: typing.Type[DefaultThrowableMessageComposer]
    DefaultThrowableResolver: typing.Type[DefaultThrowableResolver]
    EmptyThrowableResolver: typing.Type[EmptyThrowableResolver]
    HierarchyImpl: typing.Type[HierarchyImpl]
    ThrowableConstants: typing.Type[ThrowableConstants]
    ThrowableDescriptor: typing.Type[ThrowableDescriptor]
    ThrowableMessageComposer: typing.Type[ThrowableMessageComposer]
    ThrowableResolver: typing.Type[ThrowableResolver]
    config: cern.accsoft.commons.diag.config.__module_protocol__
    matcher: cern.accsoft.commons.diag.matcher.__module_protocol__
