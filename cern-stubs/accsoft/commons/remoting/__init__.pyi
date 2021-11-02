import java.lang.reflect
import java.util
import org.springframework.beans.factory
import org.springframework.beans.factory.support
import org.springframework.context
import org.springframework.remoting.rmi
import typing



class BusinessService:
    """
    public interface BusinessService
    
        Marker interface.
    """
    ...

class RemoteServiceLookupBeanFactory(org.springframework.beans.factory.FactoryBean[java.util.List[org.springframework.remoting.rmi.RmiProxyFactoryBean]], org.springframework.beans.factory.BeanFactoryAware):
    """
    public class RemoteServiceLookupBeanFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements org.springframework.beans.factory.FactoryBean<`List <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/List.html?is-external=true>`<org.springframework.remoting.rmi.RmiProxyFactoryBean>>, org.springframework.beans.factory.BeanFactoryAware
    
        Remote services factory. It produces raw references to the remote services.
    """
    def __init__(self): ...
    def getObject(self) -> java.util.List[org.springframework.remoting.rmi.RmiProxyFactoryBean]: ...
    def getObjectType(self) -> typing.Type[typing.Any]: ...
    def isSingleton(self) -> bool:
        """
        
            Specified by:
                :code:`isSingleton` in interface 
        
        
        """
        ...
    def setBeanFactory(self, beanFactory: org.springframework.beans.factory.BeanFactory) -> None: ...
    def setBeansProvider(self, serviceBeansProvider: 'ServiceBeansProvider') -> None: ...

class ServerManager:
    """
    public interface ServerManager
    
        Manages remote servers. A remote server contains a set of business services that can be used by end clients.
    """
    def createRemoteServerFor(self, string: str, list: java.util.List['BusinessServiceDescriptor']) -> 'RemoteServer': ...

class ServerRegistry:
    """
    public interface ServerRegistry
    
        Represents registry of remote servers. A remote server contains a set of (default) remote business services that might
        be used by clients. One service might be hosted by many servers.
    """
    _getAllServices__T = typing.TypeVar('_getAllServices__T', bound=BusinessService)  # <T>
    def getAllServices(self, class_: typing.Type[_getAllServices__T]) -> java.util.List[_getAllServices__T]: ...
    _getServiceFor__T = typing.TypeVar('_getServiceFor__T', bound=BusinessService)  # <T>
    def getServiceFor(self, class_: typing.Type[_getServiceFor__T]) -> _getServiceFor__T: ...
    _registerServicesFor__T = typing.TypeVar('_registerServicesFor__T', bound=BusinessService)  # <T>
    def registerServicesFor(self, string: str) -> None:
        """
            Registers new set of default services for the given server's location.
        
            Parameters:
                url (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): server's location
        
        
        """
        ...

class ServerScheduler:
    """
    public interface ServerScheduler
    
        Represents servers scheduling contract. From a given collection of remote servers each of them containing set of
        business services it shall be possible to select appropriate server based on some criteria. Such criteria shall be
        defined by the implementation.
    """
    _getServiceFrom__T = typing.TypeVar('_getServiceFrom__T', bound=BusinessService)  # <T>
    def getServiceFrom(self, set: java.util.Set['RemoteServer'], class_: typing.Type[_getServiceFrom__T]) -> _getServiceFrom__T: ...
    def lockServer(self, remoteServer: 'RemoteServer') -> None:
        """
            Locks the given server (for instance in case when a server is down)
        
        """
        ...
    def markServerAsUsed(self, remoteServer: 'RemoteServer') -> None:
        """
            Informs scheduler that given server is being used.
        
        """
        ...
    def releaseCurrentlyUsedServers(self) -> None:
        """
            Informs scheduler that all servers that have been used by the current thread can be released (whatever it means).
        
        """
        ...

class ServiceBeanReplacer(org.springframework.beans.factory.support.MethodReplacer, org.springframework.context.ApplicationContextAware):
    """
    public abstract class ServiceBeanReplacer extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements org.springframework.beans.factory.support.MethodReplacer, org.springframework.context.ApplicationContextAware
    
        The intention of this class is to transform raw (rmi) remote services into business services.
    
        It is used by the "Method replacement" injection feature in Spring.
    """
    def __init__(self): ...
    def getServiceRegistry(self) -> 'ServiceRegistry': ...
    def reimplement(self, object: typing.Any, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def setApplicationContext(self, applicationContext: org.springframework.context.ApplicationContext) -> None: ...

class ServiceBeansProvider:
    """
    public interface ServiceBeansProvider
    
        Provides information about remote servers's locations as well as referenced business services proxies (in a form of
        their Spring beans' names)
    """
    def getBeanNames(self) -> java.util.List[str]: ...
    def getServers(self) -> java.util.List[str]: ...

class ServiceRegistry:
    """
    public abstract class ServiceRegistry extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Simple container for remote services. This class is a part of the framework and has no business meaning.
    """
    def __init__(self): ...
    def getRawServices(self) -> java.util.List[org.springframework.remoting.rmi.RmiProxyFactoryBean]: ...

class BusinessServiceDescriptor: ...

class RemoteServer: ...

class DefaultServiceBeansProvider(ServiceBeansProvider):
    """
    public class DefaultServiceBeansProvider extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.remoting.ServiceBeansProvider`
    """
    def __init__(self, list: java.util.List[str], list2: java.util.List[str]): ...
    def getBeanNames(self) -> java.util.List[str]: ...
    def getServers(self) -> java.util.List[str]: ...

class ServerRegistryImpl(ServerRegistry):
    """
    public abstract class ServerRegistryImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.remoting.ServerRegistry`
    
        An implementation of the ServerRegistry interface. It holds a collection of remote servers each of them containing a set
        of remote business services.
    
        It's possible to add a remote server with a predefined set of services. Each remote service is wrapped in a proxy that
        handles sort of fail over defined as retrying method execution on another remote service.
    
        The order in which a service for a given class is returned to end client is delegated to the serverScheduler instance.
    """
    def __init__(self, serviceBeansProvider: ServiceBeansProvider, serverScheduler: ServerScheduler): ...
    _getAllServices__T = typing.TypeVar('_getAllServices__T', bound=BusinessService)  # <T>
    def getAllServices(self, class_: typing.Type[_getAllServices__T]) -> java.util.List[_getAllServices__T]: ...
    def getServerServices(self, string: str) -> java.util.List[BusinessServiceDescriptor]: ...
    _getServiceFor__T = typing.TypeVar('_getServiceFor__T', bound=BusinessService)  # <T>
    def getServiceFor(self, class_: typing.Type[_getServiceFor__T]) -> _getServiceFor__T: ...
    def init(self) -> None: ...
    _registerServicesFor__T = typing.TypeVar('_registerServicesFor__T', bound=BusinessService)  # <T>
    def registerServicesFor(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.remoting.ServerRegistry.registerServicesFor`
            Registers new set of default services for the given server's location.
        
            Specified by:
                :meth:`~cern.accsoft.commons.remoting.ServerRegistry.registerServicesFor`Â in
                interfaceÂ :class:`~cern.accsoft.commons.remoting.ServerRegistry`
        
            Parameters:
                url (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): server's location
        
        
        """
        ...

class SimpleServerScheduler(ServerScheduler):
    """
    public class SimpleServerScheduler extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.remoting.ServerScheduler`
    
        Uses cyclic buffer as a server selection algorithm. The algorithm is applied within the same thread in order to avoid
        thread starvation in case of service fail over.
    
        This implementation assumes that every RemoteServer contains the same set of services. In case if there's no server that
        can handle given service the NoServersFoundException is thrown.
    """
    def __init__(self): ...
    _getServiceFrom__T = typing.TypeVar('_getServiceFrom__T', bound=BusinessService)  # <T>
    def getServiceFrom(self, set: java.util.Set[RemoteServer], class_: typing.Type[_getServiceFrom__T]) -> _getServiceFrom__T: ...
    def lockServer(self, remoteServer: RemoteServer) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.remoting.ServerScheduler.lockServer`
            Locks the given server (for instance in case when a server is down)
        
            Specified by:
                :meth:`~cern.accsoft.commons.remoting.ServerScheduler.lockServer`Â in
                interfaceÂ :class:`~cern.accsoft.commons.remoting.ServerScheduler`
        
        
        """
        ...
    def markServerAsUsed(self, remoteServer: RemoteServer) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.remoting.ServerScheduler.markServerAsUsed`
            Informs scheduler that given server is being used.
        
            Specified by:
                :meth:`~cern.accsoft.commons.remoting.ServerScheduler.markServerAsUsed`Â in
                interfaceÂ :class:`~cern.accsoft.commons.remoting.ServerScheduler`
        
        
        """
        ...
    def releaseCurrentlyUsedServers(self) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.remoting.ServerScheduler.releaseCurrentlyUsedServers`
            Informs scheduler that all servers that have been used by the current thread can be released (whatever it means).
        
            Specified by:
                :meth:`~cern.accsoft.commons.remoting.ServerScheduler.releaseCurrentlyUsedServers`Â in
                interfaceÂ :class:`~cern.accsoft.commons.remoting.ServerScheduler`
        
        
        """
        ...
    def setLockedTimeSeconds(self, int: int) -> None: ...
    def setNumberOfAttemptsBeforeLock(self, int: int) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.remoting")``.

    BusinessService: typing.Type[BusinessService]
    BusinessServiceDescriptor: typing.Type[BusinessServiceDescriptor]
    DefaultServiceBeansProvider: typing.Type[DefaultServiceBeansProvider]
    RemoteServer: typing.Type[RemoteServer]
    RemoteServiceLookupBeanFactory: typing.Type[RemoteServiceLookupBeanFactory]
    ServerManager: typing.Type[ServerManager]
    ServerRegistry: typing.Type[ServerRegistry]
    ServerRegistryImpl: typing.Type[ServerRegistryImpl]
    ServerScheduler: typing.Type[ServerScheduler]
    ServiceBeanReplacer: typing.Type[ServiceBeanReplacer]
    ServiceBeansProvider: typing.Type[ServiceBeansProvider]
    ServiceRegistry: typing.Type[ServiceRegistry]
    SimpleServerScheduler: typing.Type[SimpleServerScheduler]
