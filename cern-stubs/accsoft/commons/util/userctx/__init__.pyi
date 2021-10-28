import java.io
import java.util
import org.aopalliance.intercept
import org.springframework.remoting.support
import typing



class ContextAwareRemoteInvocationExecutor(org.springframework.remoting.support.RemoteInvocationExecutor):
    """
    Java class 'cern.accsoft.commons.util.userctx.ContextAwareRemoteInvocationExecutor'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.springframework.remoting.support.RemoteInvocationExecutor
    
      Constructors:
        * ContextAwareRemoteInvocationExecutor()
    
    """
    def __init__(self): ...
    def invoke(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any) -> typing.Any: ...

class ContextAwareRemoteInvocationFactory(org.springframework.remoting.support.RemoteInvocationFactory):
    """
    Java class 'cern.accsoft.commons.util.userctx.ContextAwareRemoteInvocationFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.springframework.remoting.support.RemoteInvocationFactory
    
      Constructors:
        * ContextAwareRemoteInvocationFactory()
    
    """
    def __init__(self): ...
    def createRemoteInvocation(self, methodInvocation: org.aopalliance.intercept.MethodInvocation) -> org.springframework.remoting.support.RemoteInvocation: ...
    def getInvocationContextProviders(self) -> java.util.List['InvocationContextProvider']: ...
    def getStaticInvocationContext(self) -> java.util.Map[str, java.io.Serializable]: ...
    def setInvocationContextProviders(self, list: java.util.List['InvocationContextProvider']) -> None: ...
    def setStaticInvocationContext(self, map: typing.Union[java.util.Map[str, java.io.Serializable], typing.Mapping[str, java.io.Serializable]]) -> None: ...

class InvocationContextProvider:
    """
    Java class 'cern.accsoft.commons.util.userctx.InvocationContextProvider'
    
    """
    def getAttributeMap(self) -> java.util.Map[str, java.io.Serializable]: ...

class RemoteInvocationConstants:
    """
    Java class 'cern.accsoft.commons.util.userctx.RemoteInvocationConstants'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RemoteInvocationConstants()
    
      Attributes:
        CTX_CLIENT_ID (java.lang.String): final static field
        CTX_CLIENT_INFORMATION (java.lang.String): final static field
        CTX_RBA_TOKEN (java.lang.String): final static field
    
    """
    CTX_CLIENT_ID: typing.ClassVar[str] = ...
    CTX_CLIENT_INFORMATION: typing.ClassVar[str] = ...
    CTX_RBA_TOKEN: typing.ClassVar[str] = ...
    def __init__(self): ...

class ThreadLocalUserContext:
    """
    Java class 'cern.accsoft.commons.util.userctx.ThreadLocalUserContext'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ThreadLocalUserContext()
    
    """
    def __init__(self): ...
    @staticmethod
    def clear() -> None: ...
    @staticmethod
    def get(string: str) -> java.io.Serializable: ...
    @staticmethod
    def put(string: str, serializable: java.io.Serializable) -> None: ...
    @staticmethod
    def remove(string: str) -> java.io.Serializable: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.userctx")``.

    ContextAwareRemoteInvocationExecutor: typing.Type[ContextAwareRemoteInvocationExecutor]
    ContextAwareRemoteInvocationFactory: typing.Type[ContextAwareRemoteInvocationFactory]
    InvocationContextProvider: typing.Type[InvocationContextProvider]
    RemoteInvocationConstants: typing.Type[RemoteInvocationConstants]
    ThreadLocalUserContext: typing.Type[ThreadLocalUserContext]
