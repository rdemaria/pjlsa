import cern.accsoft.commons.util.userctx
import java.lang
import java.util
import org.springframework.remoting.support
import typing



class InstrumentationRemoteInvocationExecutor(cern.accsoft.commons.util.userctx.ContextAwareRemoteInvocationExecutor):
    """
    Java class 'cern.accsoft.commons.util.remoting.instrumentation.InstrumentationRemoteInvocationExecutor'
    
        Extends:
            cern.accsoft.commons.util.userctx.ContextAwareRemoteInvocationExecutor
    
      Constructors:
        * InstrumentationRemoteInvocationExecutor(java.util.List)
    
    """
    def __init__(self, list: java.util.List['RemoteInvocationInstrumentation']): ...

class RemoteInstrumentationUtils:
    """
    Java class 'cern.accsoft.commons.util.remoting.instrumentation.RemoteInstrumentationUtils'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def getClassForLogging(object: typing.Any) -> typing.Type[typing.Any]: ...
    @staticmethod
    def getClientId(remoteInvocation: org.springframework.remoting.support.RemoteInvocation) -> str: ...
    @staticmethod
    def getRbacUser() -> str: ...

class RemoteInvocationInstrumentation:
    """
    Java class 'cern.accsoft.commons.util.remoting.instrumentation.RemoteInvocationInstrumentation'
    
    """
    def afterInvocationFailure(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any, exception: java.lang.Exception) -> None: ...
    def afterInvocationSuccess(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any, object2: typing.Any) -> None: ...
    def beforeInvocation(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any) -> None: ...

class Slf4jRmiLogger(RemoteInvocationInstrumentation):
    """
    Java class 'cern.accsoft.commons.util.remoting.instrumentation.Slf4jRmiLogger'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.remoting.instrumentation.RemoteInvoc
            ationInstrumentation
    
      Constructors:
        * Slf4jRmiLogger(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    def afterInvocationFailure(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any, exception: java.lang.Exception) -> None: ...
    def afterInvocationSuccess(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any, object2: typing.Any) -> None: ...
    def beforeInvocation(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.remoting.instrumentation")``.

    InstrumentationRemoteInvocationExecutor: typing.Type[InstrumentationRemoteInvocationExecutor]
    RemoteInstrumentationUtils: typing.Type[RemoteInstrumentationUtils]
    RemoteInvocationInstrumentation: typing.Type[RemoteInvocationInstrumentation]
    Slf4jRmiLogger: typing.Type[Slf4jRmiLogger]
