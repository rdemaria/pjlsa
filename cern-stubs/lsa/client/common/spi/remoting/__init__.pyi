import cern.accsoft.commons.util.userctx
import cern.lsa.domain.commons.logging
import java.io
import java.lang
import java.lang.reflect
import java.util
import org.springframework.beans.factory
import org.springframework.remoting.rmi
import org.springframework.remoting.support
import typing



class InvocationIdProvider(cern.accsoft.commons.util.userctx.InvocationContextProvider):
    """
    Java class 'cern.lsa.client.common.spi.remoting.InvocationIdProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.userctx.InvocationContextProvider
    
      Constructors:
        * InvocationIdProvider()
    
    """
    def __init__(self): ...
    def getAttributeMap(self) -> java.util.Map[str, java.io.Serializable]: ...

class LSARemotingConstants:
    """
    Java class 'cern.lsa.client.common.spi.remoting.LSARemotingConstants'
    
      Attributes:
        CLIENT_IP_ADDRESS (java.lang.String): final static field
        CLIENT_USER_NAME (java.lang.String): final static field
        CLIENT_HOST_NAME (java.lang.String): final static field
        CLIENT_METHOD (java.lang.String): final static field
        INVOCATION_ID (java.lang.String): final static field
        CLIENT_INFO (java.lang.String): final static field
    
    """
    CLIENT_IP_ADDRESS: typing.ClassVar[str] = ...
    CLIENT_USER_NAME: typing.ClassVar[str] = ...
    CLIENT_HOST_NAME: typing.ClassVar[str] = ...
    CLIENT_METHOD: typing.ClassVar[str] = ...
    INVOCATION_ID: typing.ClassVar[str] = ...
    CLIENT_INFO: typing.ClassVar[str] = ...

class LSAServiceAwareRmiProxyFactoryBean(org.springframework.remoting.rmi.RmiProxyFactoryBean, org.springframework.beans.factory.BeanNameAware):
    """
    Java class 'cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean'
    
        Extends:
            org.springframework.remoting.rmi.RmiProxyFactoryBean
    
        Interfaces:
            org.springframework.beans.factory.BeanNameAware
    
      Constructors:
        * LSAServiceAwareRmiProxyFactoryBean(java.lang.String, int)
    
    """
    def __init__(self, string: str, int: int): ...
    def afterPropertiesSet(self) -> None: ...
    def getObject(self) -> typing.Any: ...
    def setBeanName(self, string: str) -> None: ...
    def setInterfaceClassName(self, string: str) -> None: ...
    def setLogicalInterfaceName(self, string: str) -> None: ...
    class FilteringStackTraceInvocationHandler(java.lang.reflect.InvocationHandler):
        """
        Java class 'cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean$FilteringStackTraceInvocationHandler'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.lang.reflect.InvocationHandler
        
          Attributes:
            PROPERTY_STACKTRACE_FILTER_DISABLED (java.lang.String): final static field
            PROPERTY_STACKTRACE_FILTER_PATTERNS (java.lang.String): final static field
        
        """
        PROPERTY_STACKTRACE_FILTER_DISABLED: typing.ClassVar[str] = ...
        PROPERTY_STACKTRACE_FILTER_PATTERNS: typing.ClassVar[str] = ...
        def invoke(self, object: typing.Any, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any]) -> typing.Any: ...

class LoggingAwareRemoteInvocationResult(org.springframework.remoting.support.RemoteInvocationResult):
    """
    Java class 'cern.lsa.client.common.spi.remoting.LoggingAwareRemoteInvocationResult'
    
        Extends:
            org.springframework.remoting.support.RemoteInvocationResult
    
      Constructors:
        * LoggingAwareRemoteInvocationResult(java.lang.Object)
        * LoggingAwareRemoteInvocationResult(java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, object: typing.Any): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    def getMiddleTierLogs(self) -> typing.List[cern.lsa.domain.commons.logging.LogMessage]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.common.spi.remoting")``.

    InvocationIdProvider: typing.Type[InvocationIdProvider]
    LSARemotingConstants: typing.Type[LSARemotingConstants]
    LSAServiceAwareRmiProxyFactoryBean: typing.Type[LSAServiceAwareRmiProxyFactoryBean]
    LoggingAwareRemoteInvocationResult: typing.Type[LoggingAwareRemoteInvocationResult]
