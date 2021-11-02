import java.io
import java.util
import org.aopalliance.intercept
import org.springframework.remoting.support
import typing



class ContextAwareRemoteInvocationExecutor(org.springframework.remoting.support.RemoteInvocationExecutor):
    """
    public class ContextAwareRemoteInvocationExecutor extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements org.springframework.remoting.support.RemoteInvocationExecutor
    
        RemoteInvocationExecutor that extracts all client context attributes from the :code:`RemoteInvocation` object.
    
        It puts the client context attributes into the :class:`~cern.accsoft.commons.util.userctx.ThreadLocalUserContext` and
        RBA Token into the :code:`cern.rba.util.holder.MiddleTierRBATokenHolder`. Then it invokes the server-side method, and
        then it clears the client context attributes again from the thread local storage.
    
        This class can be extended to further customize the behavior by overriding the protected methods
        :code:`#beforeInvoke(RemoteInvocation, Object)`, :code:`#afterInvoke(Object)` and :code:`#onException(Throwable)` which
        are called immediately before and after the invocation of the server-side method.
    """
    def __init__(self): ...
    def invoke(self, remoteInvocation: org.springframework.remoting.support.RemoteInvocation, object: typing.Any) -> typing.Any: ...

class ContextAwareRemoteInvocationFactory(org.springframework.remoting.support.RemoteInvocationFactory):
    """
    public class ContextAwareRemoteInvocationFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements org.springframework.remoting.support.RemoteInvocationFactory
    
        Called by a client-side instance of :code:`org.springframework.remoting.rmi.RmiProxyFactoryBean`,
        :code:`org.springframework.remoting.httpinvoker.HttpInvokerProxyFactoryBean` or any other
        :code:`org.springframework.remoting.support.RemoteInvocationBasedAccessor` when it creates a remote invocation.
    
        Set an instance of this bean against the above class' :code:`remoteInvocationFactory` property.
        In practice, create the Factory as a bean in your client-side Spring application context:
    
        .. code-block: java
        
         
         <bean id="remoteInvocationFactory" class="cern.accsoft.commons.util.userctx.ContextAwareRemoteInvocationFactory"/>
         
         
        and then inject it into the :code:`RemoteInvocationBasedAccessor.setRemoteInvocationFactory(RemoteInvocationFactory)`
        with:
    
        .. code-block: java
        
         
          <property name="remoteInvocationFactory">
              <ref local="remoteInvocationFactory" />
          </property>
    """
    def __init__(self): ...
    def createRemoteInvocation(self, methodInvocation: org.aopalliance.intercept.MethodInvocation) -> org.springframework.remoting.support.RemoteInvocation:
        """
        
            Specified by:
                :code:`createRemoteInvocation` in interface :code:`org.springframework.remoting.support.RemoteInvocationFactory`
        
        
        """
        ...
    def getInvocationContextProviders(self) -> java.util.List['InvocationContextProvider']: ...
    def getStaticInvocationContext(self) -> java.util.Map[str, java.io.Serializable]: ...
    def setInvocationContextProviders(self, list: java.util.List['InvocationContextProvider']) -> None: ...
    def setStaticInvocationContext(self, map: typing.Union[java.util.Map[str, java.io.Serializable], typing.Mapping[str, java.io.Serializable]]) -> None: ...

class InvocationContextProvider:
    """
    public interface InvocationContextProvider
    
        Implementations of this interface can provide named attributes to be passed using the
        :code:`RemoteInvocation.addAttribute(String, Serializable)`;
    """
    def getAttributeMap(self) -> java.util.Map[str, java.io.Serializable]: ...

class RemoteInvocationConstants:
    """
    public class RemoteInvocationConstants extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Constants related for Remote Invocation and user context
    """
    CTX_CLIENT_ID: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CTX_CLIENT_ID
    
        Key under which the client ID is stored in the ThreadLocal context - use
        :meth:`~cern.accsoft.commons.util.userctx.ThreadLocalUserContext.get` to access it
    
        Also see:
            :meth:`~constant`
    
    
    """
    CTX_CLIENT_INFORMATION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CTX_CLIENT_INFORMATION
    
        Key under which the :class:`~cern.accsoft.commons.util.userinfo.ClientInformation` is stored in the ThreadLocal context
        - use :meth:`~cern.accsoft.commons.util.userctx.ThreadLocalUserContext.get` to access it
    
        Also see:
            :meth:`~constant`
    
    
    """
    CTX_RBA_TOKEN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CTX_RBA_TOKEN
    
        Key under which the RBAC token is stored in the ThreadLocal context - use
        :meth:`~cern.accsoft.commons.util.userctx.ThreadLocalUserContext.get` to access it
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class ThreadLocalUserContext:
    """
    public class ThreadLocalUserContext extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        An object to keep user context (typically coming from the a client) in thread local storage
    """
    def __init__(self): ...
    @staticmethod
    def clear() -> None:
        """
            Clears all values in this context
        
        """
        ...
    @staticmethod
    def get(string: str) -> java.io.Serializable:
        """
            Returns the context object corresponding to the specified key
        
            Parameters:
                key (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the key, e.g. :code:`ContextSendingRemoteInvocation#wait(long, int)`
        
            Returns:
                the context object corresponding to the specified key
        
        
        """
        ...
    @staticmethod
    def put(string: str, serializable: java.io.Serializable) -> None:
        """
            Sets the context value for the specified key
        
            Parameters:
                key (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the key, e.g. :code:`ContextSendingRemoteInvocation#wait(long, int)`
                value (`Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`): the value to store
        
        
        """
        ...
    @staticmethod
    def remove(string: str) -> java.io.Serializable:
        """
            Removes and returns the context object corresponding to the specified key
        
            Parameters:
                key (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the key, e.g. :code:`ContextSendingRemoteInvocation#wait(long, int)`
        
            Returns:
                the context object corresponding to the specified key
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.userctx")``.

    ContextAwareRemoteInvocationExecutor: typing.Type[ContextAwareRemoteInvocationExecutor]
    ContextAwareRemoteInvocationFactory: typing.Type[ContextAwareRemoteInvocationFactory]
    InvocationContextProvider: typing.Type[InvocationContextProvider]
    RemoteInvocationConstants: typing.Type[RemoteInvocationConstants]
    ThreadLocalUserContext: typing.Type[ThreadLocalUserContext]
