import cern.accsoft.commons.util.userctx
import java.lang
import java.util
import org.springframework.remoting.support
import typing



class InstrumentationRemoteInvocationExecutor(cern.accsoft.commons.util.userctx.ContextAwareRemoteInvocationExecutor):
    """
    public class InstrumentationRemoteInvocationExecutor extends :class:`~cern.accsoft.commons.util.userctx.ContextAwareRemoteInvocationExecutor`
    
        A :code:`RemoteInvocationExecutor` that provides the ability to register instrumentations to be invoked during the
        processing of :code:`RemoteInvocation`.
    """
    def __init__(self, list: java.util.List['RemoteInvocationInstrumentation']): ...

class RemoteInstrumentationUtils:
    """
    public final class RemoteInstrumentationUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def getClassForLogging(object: typing.Any) -> typing.Type[typing.Any]: ...
    @staticmethod
    def getClientId(remoteInvocation: org.springframework.remoting.support.RemoteInvocation) -> str:
        """
            Gets the client id from this remote invocation if available otherwise returns an empty string.
        
            Parameters:
                remoteInvocation (org.springframework.remoting.support.RemoteInvocation): the remote invocation from which to extract the client id
        
            Returns:
                the client id or an empty string
        
        
        """
        ...
    @staticmethod
    def getRbacUser() -> str:
        """
        
            Returns:
                the RBAC username
        
        
        """
        ...

class RemoteInvocationInstrumentation:
    """
    public interface RemoteInvocationInstrumentation
    
        A remote invocation instrumentation used to perform action before and after each invocation.
    """
    def afterInvocationFailure(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any, exception: java.lang.Exception) -> None:
        """
            Invoked when the invocation is finished with exception.
        
            Parameters:
                invocation (org.springframework.remoting.support.RemoteInvocation): the invocation object
                targetObject (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the target object of the invocation
                exception (`Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`): the reason the invocation failed
        
        
        """
        ...
    def afterInvocationSuccess(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any, object2: typing.Any) -> None:
        """
            Invoked when the invocation is finished successfully.
        
            Parameters:
                invocation (org.springframework.remoting.support.RemoteInvocation): the invocation object
                targetObject (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the target object of the invocation
                result (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the result of the invocation
        
        
        """
        ...
    def beforeInvocation(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any) -> None:
        """
            Invoked before the actual invocation takes place.
        
            Parameters:
                invocation (org.springframework.remoting.support.RemoteInvocation): the invocation object
                targetObject (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the target object of the invocation
        
        
        """
        ...

class Slf4jRmiLogger(RemoteInvocationInstrumentation):
    """
    public class Slf4jRmiLogger extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation`
    
        Logs the service invocation together with its arguments, some process information and the rbac token
    """
    def __init__(self, string: str): ...
    def afterInvocationFailure(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any, exception: java.lang.Exception) -> None:
        """
            Description copied from
            interface:Â :meth:`~cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation.afterInvocationFailure`
            Invoked when the invocation is finished with exception.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation.afterInvocationFailure`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation`
        
            Parameters:
                invocation (org.springframework.remoting.support.RemoteInvocation): the invocation object
                targetObject (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the target object of the invocation
                exception (`Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`): the reason the invocation failed
        
        
        """
        ...
    def afterInvocationSuccess(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any, object2: typing.Any) -> None:
        """
            Description copied from
            interface:Â :meth:`~cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation.afterInvocationSuccess`
            Invoked when the invocation is finished successfully.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation.afterInvocationSuccess`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation`
        
            Parameters:
                invocation (org.springframework.remoting.support.RemoteInvocation): the invocation object
                targetObject (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the target object of the invocation
                result (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the result of the invocation
        
        
        """
        ...
    def beforeInvocation(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any) -> None:
        """
            Description copied from
            interface:Â :meth:`~cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation.beforeInvocation`
            Invoked before the actual invocation takes place.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation.beforeInvocation`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation`
        
            Parameters:
                invocation (org.springframework.remoting.support.RemoteInvocation): the invocation object
                targetObject (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the target object of the invocation
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.remoting.instrumentation")``.

    InstrumentationRemoteInvocationExecutor: typing.Type[InstrumentationRemoteInvocationExecutor]
    RemoteInstrumentationUtils: typing.Type[RemoteInstrumentationUtils]
    RemoteInvocationInstrumentation: typing.Type[RemoteInvocationInstrumentation]
    Slf4jRmiLogger: typing.Type[Slf4jRmiLogger]
