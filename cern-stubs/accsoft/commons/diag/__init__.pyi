from typing import TypeVar as _py_TypeVar
from typing import ClassVar as _py_ClassVar
from typing import Generic as _py_Generic
from typing import overload
import cern.accsoft.commons.diag.matcher
import cern.accsoft.commons.util
import java.io
import java.lang


_HierarchyImpl__T = _py_TypeVar('_HierarchyImpl__T', bound=cern.accsoft.commons.util.Named)  # <T>
class HierarchyImpl(_py_Generic[_HierarchyImpl__T]):
    def __init__(self): ...
    def addChildToEnd(self, t: _HierarchyImpl__T) -> None: ...
    def addChildToTop(self, t: _HierarchyImpl__T) -> None: ...

class ThrowableConstants:
    INDENTATION: _py_ClassVar[str] = ...
    BR: _py_ClassVar[str] = ...
    END: _py_ClassVar[str] = ...
    START_NAME: _py_ClassVar[str] = ...
    START_CHILDREN: _py_ClassVar[str] = ...

class ThrowableDescriptor(java.io.Serializable):
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
        @overload
        def __init__(self): ...
        @overload
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
    def composeMessage(self, throwable: java.lang.Throwable) -> str: ...

class ThrowableResolver:
    def resolve(self, throwable: java.lang.Throwable) -> ThrowableDescriptor: ...

class DefaultThrowableMessageComposer(ThrowableMessageComposer):
    def __init__(self): ...
    def composeMessage(self, throwable: java.lang.Throwable) -> str: ...

class EmptyThrowableResolver(cern.accsoft.commons.diag.matcher.ThrowableMatcherHierarchyImpl, ThrowableResolver):
    def __init__(self): ...
    def resolve(self, throwable: java.lang.Throwable) -> ThrowableDescriptor: ...
    def toString(self) -> str: ...

class DefaultThrowableResolver(EmptyThrowableResolver): ...