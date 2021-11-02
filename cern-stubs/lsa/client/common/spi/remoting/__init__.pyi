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
    public class InvocationIdProvider extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.accsoft.commons.util.userctx.InvocationContextProvider
    
        Invocation context provider that returns a map with invocation ID that can be used to monitor progress of execution of
        certain operations performed on the LSA server.
    
        Also see:
            :code:`InvocationIdHolder`
    """
    def __init__(self): ...
    def getAttributeMap(self) -> java.util.Map[str, java.io.Serializable]: ...

class LSARemotingConstants:
    """
    public interface LSARemotingConstants
    """
    CLIENT_IP_ADDRESS: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CLIENT_IP_ADDRESS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CLIENT_USER_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CLIENT_USER_NAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CLIENT_HOST_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CLIENT_HOST_NAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CLIENT_METHOD: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CLIENT_METHOD
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    INVOCATION_ID: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` INVOCATION_ID
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CLIENT_INFO: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CLIENT_INFO
    
    
        Also see:
            :meth:`~constant`
    
    
    """

class LSAServiceAwareRmiProxyFactoryBean(org.springframework.remoting.rmi.RmiProxyFactoryBean, org.springframework.beans.factory.BeanNameAware):
    """
    public class LSAServiceAwareRmiProxyFactoryBean extends org.springframework.remoting.rmi.RmiProxyFactoryBean implements org.springframework.beans.factory.BeanNameAware
    """
    def __init__(self, string: str, int: int): ...
    def afterPropertiesSet(self) -> None:
        """
        
            Specified by:
                :code:`afterPropertiesSet` in interface :code:`org.springframework.beans.factory.InitializingBean`
        
            Overrides:
                :code:`afterPropertiesSet` in class :code:`org.springframework.remoting.rmi.RmiProxyFactoryBean`
        
        
        """
        ...
    def getObject(self) -> typing.Any:
        """
        
            Specified by:
                :code:`getObject` in interface 
        
            Overrides:
                :code:`getObject` in class :code:`org.springframework.remoting.rmi.RmiProxyFactoryBean`
        
        
        """
        ...
    def setBeanName(self, string: str) -> None:
        """
        
            Specified by:
                :code:`setBeanName` in interface :code:`org.springframework.beans.factory.BeanNameAware`
        
        
        """
        ...
    def setInterfaceClassName(self, string: str) -> None: ...
    def setLogicalInterfaceName(self, string: str) -> None: ...
    class FilteringStackTraceInvocationHandler(java.lang.reflect.InvocationHandler):
        PROPERTY_STACKTRACE_FILTER_DISABLED: typing.ClassVar[str] = ...
        PROPERTY_STACKTRACE_FILTER_PATTERNS: typing.ClassVar[str] = ...
        def invoke(self, object: typing.Any, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any]) -> typing.Any: ...

class LoggingAwareRemoteInvocationResult(org.springframework.remoting.support.RemoteInvocationResult):
    """
    public class LoggingAwareRemoteInvocationResult extends org.springframework.remoting.support.RemoteInvocationResult
    
        Invocation result which keeps array of :code:`LogMessage`s.
    
        Also see:
            :meth:`~serialized`
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
