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
    public interface ThrowableMatcher extends cern.accsoft.commons.util.Named
    
        Matcher recognizing a certain group of `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`'s.
    """
    def findThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor:
        """
        
            Parameters:
                potentialyMatchingThrowable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): a `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>` to check for
                    matching
                fullThrowable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): full original `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
                    containing :code:`potentialyMatchingThrowable`
        
            Returns:
                descriptor of the `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
                if it is recognized and :code:`null` otherwise
        
        
        """
        ...

class ThrowableMatcherHierarchyImpl(cern.accsoft.commons.diag.HierarchyImpl[ThrowableMatcher]):
    """
    public abstract class ThrowableMatcherHierarchyImpl extends :class:`~cern.accsoft.commons.diag.HierarchyImpl`<:class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher`>
    
        Container for :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher`'s.
    
        Contains reusable methods for real implementations.
    """
    def __init__(self): ...

class AbstractThrowableMatcher(ThrowableMatcherHierarchyImpl, ThrowableMatcher):
    """
    public abstract class AbstractThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcherHierarchyImpl` implements :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher`
    
        Base class for all the :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher` implementations.
    """
    def __init__(self, string: str): ...
    @staticmethod
    def extractExceptionMessage(throwable: java.lang.Throwable, boolean: bool) -> str:
        """
            Extracts a nice message describing exceptions, causes and messages they contain.
        
            For instance:
        
            .. code-block: java
            
             extractExceptionMessage(new RuntimeException("message", new IllegalArgumentException("cause")));
             
            returns the String
        
            .. code-block: java
            
             "RuntimeException [message] caused by: IllegalArgumentException [cause]"
             
        
            Parameters:
                exception (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): the exception
                shouldPrintInSeparateLines (boolean): specifies if each cause in the stack trace should be printed in separate lines.
        
            Returns:
                the message String extracted from the exception
        
        
        """
        ...
    def findThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher.findThrowableDescriptor`Â in
                interfaceÂ :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher`
        
            Overrides:
                :meth:`~cern.accsoft.commons.diag.matcher.ThrowableMatcherHierarchyImpl.findThrowableDescriptor`Â in
                classÂ :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcherHierarchyImpl`
        
            Parameters:
                potentialyMatchingThrowable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): a `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>` to check for
                    matching
                fullThrowable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): full original `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
                    containing :code:`potentialyMatchingThrowable`
        
            Returns:
                descriptor of the `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
                if it is recognized and :code:`null` otherwise
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ProxyThrowableMatcher(ThrowableMatcher):
    """
    public class ProxyThrowableMatcher extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher`
    
        :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher` implementation deciding at runtime if it should use a
        string-based actual matcher implementation or a class-based.
    """
    def __init__(self, class_: typing.Type[ThrowableMatcher], throwableMatcher: ThrowableMatcher): ...
    def findThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher.findThrowableDescriptor`Â in
                interfaceÂ :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher`
        
            Parameters:
                throwable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): a `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>` to check for
                    matching
                fullThrowable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): full original `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
                    containing :code:`potentialyMatchingThrowable`
        
            Returns:
                descriptor of the `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
                if it is recognized and :code:`null` otherwise
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ThrowableMatcherDecoratorSupport(ThrowableMatcher):
    """
    public abstract class ThrowableMatcherDecoratorSupport extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher`
    
        Base class providing the possibility to modify the descriptors on-the-fly.
    
        Useful to modify the information provided by original :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher` in
        different contexts (ex. LSA, InCA, CESAR, etc.)
    """
    def __init__(self, throwableMatcher: ThrowableMatcher): ...
    def findThrowableDescriptor(self, throwable: java.lang.Throwable, throwable2: java.lang.Throwable) -> cern.accsoft.commons.diag.ThrowableDescriptor:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher.findThrowableDescriptor`Â in
                interfaceÂ :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher`
        
            Parameters:
                potentialyMatchingThrowable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): a `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>` to check for
                    matching
                fullThrowable (`Throwable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`): full original `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
                    containing :code:`potentialyMatchingThrowable`
        
            Returns:
                descriptor of the `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
                if it is recognized and :code:`null` otherwise
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ExceptionClassThrowableMatcher(AbstractThrowableMatcher):
    """
    public class ExceptionClassThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.AbstractThrowableMatcher`
    
        Basic :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher` based on exception classes.
    
        It allows to specify :code:`root throwable` and :code:`throwable message pattern` and only if both are satisfied the
        matcher is considered matching a throwable. At least one matching criterion must be specified otherwise the matcher is
        ignored. Non-specified matching criteria are ignored.
    """
    def __init__(self, string: str, string2: str, string3: str, string4: str, class_: typing.Type[java.lang.Throwable], string5: str): ...

class StringThrowableMatcher(AbstractThrowableMatcher):
    """
    public class StringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.AbstractThrowableMatcher`
    
        Basic :class:`~cern.accsoft.commons.diag.matcher.ThrowableMatcher` based on strings.
    
        It allows to specify :code:`throwable class name pattern` and :code:`throwable message pattern` and only if both are
        satisfied the matcher is considered matching a throwable. At least one matching criterion must be specified otherwise
        the matcher is ignored. Non-specified matching criteria are ignored.
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
