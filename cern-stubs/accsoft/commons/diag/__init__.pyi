import cern.accsoft.commons.diag.config
import cern.accsoft.commons.diag.matcher
import cern.accsoft.commons.util
import java.io
import java.lang
import typing



class ApplicationThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public class ApplicationThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher`
    """
    APPLICATION_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` APPLICATION_PROBLEM_DOMAIN
    
        InCA problem domain
    
        Also see:
            :meth:`~constant`
    
    
    """
    APPLICATION_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` APPLICATION_MATCHER_NAME
    
        InCA matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def buildThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> 'ThrowableDescriptor':
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.diag.matcher.AbstractThrowableMatcher.buildThrowableDescriptor`Â in
                classÂ :class:`~cern.accsoft.commons.diag.matcher.AbstractThrowableMatcher`
        
        
        """
        ...

_HierarchyImpl__T = typing.TypeVar('_HierarchyImpl__T', bound=cern.accsoft.commons.util.Named)  # <T>
class HierarchyImpl(typing.Generic[_HierarchyImpl__T]):
    """
    public abstract class HierarchyImpl<T extends cern.accsoft.commons.util.Named> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        General implementation of a container for objects respecting their order.
    """
    def __init__(self): ...
    def addChildToEnd(self, t: _HierarchyImpl__T) -> None: ...
    def addChildToTop(self, t: _HierarchyImpl__T) -> None: ...

class ThrowableConstants:
    """
    public interface ThrowableConstants
    """
    INDENTATION: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` INDENTATION
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    BR: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` BR
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    END: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` END
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    START_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` START_NAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    START_CHILDREN: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` START_CHILDREN
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    RESOLVER: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RESOLVER
    
    
        Also see:
            :meth:`~constant`
    
    
    """

class ThrowableDescriptor(java.io.Serializable):
    """
    public class ThrowableDescriptor extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Descriptor for a `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`.
    
        Also see:
            :meth:`~serialized`
    """
    def getContactUrl(self) -> str: ...
    def getFullThrowableStackTrace(self) -> str: ...
    def getHintString(self) -> str: ...
    def getHintUrl(self) -> str: ...
    def getMatchedThrowableStackTrace(self) -> str: ...
    def getMatcherName(self) -> str: ...
    def getMessage(self) -> str: ...
    def getProblemDomain(self) -> str: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    class ThrowableDescriptorBuilder:
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
    public interface ThrowableMessageComposer
    
        Composes a message describing a `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`.
    """
    def composeMessage(self, throwable: java.lang.Throwable) -> str:
        """
        
            Parameters:
                throwable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): 
            Returns:
                message describing a `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
        
        
        """
        ...

class ThrowableResolver:
    """
    public interface ThrowableResolver
    
        Resolver for throwables.
    """
    def resolve(self, throwable: java.lang.Throwable) -> ThrowableDescriptor:
        """
        
            Parameters:
                throwable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): 
            Returns:
                the `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`'s description
        
        
        """
        ...

class DefaultThrowableMessageComposer(ThrowableMessageComposer):
    """
    public class DefaultThrowableMessageComposer extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.diag.ThrowableMessageComposer`
    
        Basic implementation of :class:`~cern.accsoft.commons.diag.ThrowableMessageComposer`.
    """
    def __init__(self): ...
    def composeMessage(self, throwable: java.lang.Throwable) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.diag.ThrowableMessageComposer.composeMessage`Â in
                interfaceÂ :class:`~cern.accsoft.commons.diag.ThrowableMessageComposer`
        
            Returns:
                message describing a `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
        
        
        """
        ...

class EmptyThrowableResolver(cern.accsoft.commons.diag.matcher.ThrowableMatcherHierarchyImpl, ThrowableResolver):
    """
    public abstract class EmptyThrowableResolver extends :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcherHierarchyImpl` implements :class:`~cern.accsoft.commons.diag.ThrowableResolver`
    
        :class:`~cern.accsoft.commons.diag.ThrowableResolver` which does not contain any matcher by default.
    
        Matchers can be added manually via :code:`#addChildToTop(ThrowableMatcher)` and
        :code:`#addChildToEnd(ThrowableMatcher)`.
    """
    def __init__(self): ...
    def resolve(self, throwable: java.lang.Throwable) -> ThrowableDescriptor:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.diag.ThrowableResolver.resolve`Â in
                interfaceÂ :class:`~cern.accsoft.commons.diag.ThrowableResolver`
        
            Returns:
                the `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`'s description
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class DefaultThrowableResolver(EmptyThrowableResolver):
    """
    public abstract class DefaultThrowableResolver extends :class:`~cern.accsoft.commons.diag.EmptyThrowableResolver`
    
        :class:`~cern.accsoft.commons.diag.ThrowableResolver` with some default matchers recognizing problems related to RBAC,
        CMW, TGM, CCDB and JAPC.
    """
    ...


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
