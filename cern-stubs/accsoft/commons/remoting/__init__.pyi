import java.lang.reflect
import java.util
import org.springframework.beans.factory
import org.springframework.beans.factory.support
import org.springframework.context
import org.springframework.remoting.rmi
import typing



class BusinessService: ...

class RemoteServiceLookupBeanFactory(org.springframework.beans.factory.FactoryBean[java.util.List[org.springframework.remoting.rmi.RmiProxyFactoryBean]], org.springframework.beans.factory.BeanFactoryAware):
    """
    Java class 'cern.accsoft.commons.remoting.RemoteServiceLookupBeanFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.springframework.beans.factory.FactoryBean,
            org.springframework.beans.factory.BeanFactoryAware
    
      Constructors:
        * RemoteServiceLookupBeanFactory()
    
    """
    def __init__(self): ...
    def getObject(self) -> java.util.List[org.springframework.remoting.rmi.RmiProxyFactoryBean]: ...
    def getObjectType(self) -> typing.Type[typing.Any]: ...
    def isSingleton(self) -> bool: ...
    def setBeanFactory(self, beanFactory: org.springframework.beans.factory.BeanFactory) -> None: ...
    def setBeansProvider(self, serviceBeansProvider: 'ServiceBeansProvider') -> None: ...

class ServerManager:
    """
    Java class 'cern.accsoft.commons.remoting.ServerManager'
    
    """
    def createRemoteServerFor(self, string: str, list: java.util.List['BusinessServiceDescriptor']) -> 'RemoteServer': ...

class ServerRegistry:
    """
    Java class 'cern.accsoft.commons.remoting.ServerRegistry'
    
    """
    _getAllServices__T = typing.TypeVar('_getAllServices__T', bound=BusinessService)  # <T>
    def getAllServices(self, class_: typing.Type[_getAllServices__T]) -> java.util.List[_getAllServices__T]: ...
    _getServiceFor__T = typing.TypeVar('_getServiceFor__T', bound=BusinessService)  # <T>
    def getServiceFor(self, class_: typing.Type[_getServiceFor__T]) -> _getServiceFor__T: ...
    _registerServicesFor__T = typing.TypeVar('_registerServicesFor__T', bound=BusinessService)  # <T>
    def registerServicesFor(self, string: str) -> None: ...

class ServerScheduler:
    """
    Java class 'cern.accsoft.commons.remoting.ServerScheduler'
    
    """
    _getServiceFrom__T = typing.TypeVar('_getServiceFrom__T', bound=BusinessService)  # <T>
    def getServiceFrom(self, set: java.util.Set['RemoteServer'], class_: typing.Type[_getServiceFrom__T]) -> _getServiceFrom__T: ...
    def lockServer(self, remoteServer: 'RemoteServer') -> None: ...
    def markServerAsUsed(self, remoteServer: 'RemoteServer') -> None: ...
    def releaseCurrentlyUsedServers(self) -> None: ...

class ServiceBeanReplacer(org.springframework.beans.factory.support.MethodReplacer, org.springframework.context.ApplicationContextAware):
    """
    Java class 'cern.accsoft.commons.remoting.ServiceBeanReplacer'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.springframework.beans.factory.support.MethodReplacer,
            org.springframework.context.ApplicationContextAware
    
      Constructors:
        * ServiceBeanReplacer()
    
    """
    def __init__(self): ...
    def getServiceRegistry(self) -> 'ServiceRegistry': ...
    def reimplement(self, object: typing.Any, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    def setApplicationContext(self, applicationContext: org.springframework.context.ApplicationContext) -> None: ...

class ServiceBeansProvider:
    """
    Java class 'cern.accsoft.commons.remoting.ServiceBeansProvider'
    
    """
    def getBeanNames(self) -> java.util.List[str]: ...
    def getServers(self) -> java.util.List[str]: ...

class ServiceRegistry:
    """
    Java class 'cern.accsoft.commons.remoting.ServiceRegistry'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ServiceRegistry()
    
    """
    def __init__(self): ...
    def getRawServices(self) -> java.util.List[org.springframework.remoting.rmi.RmiProxyFactoryBean]: ...

class BusinessServiceDescriptor: ...

class RemoteServer: ...

class DefaultServiceBeansProvider(ServiceBeansProvider):
    """
    Java class 'cern.accsoft.commons.remoting.DefaultServiceBeansProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.remoting.ServiceBeansProvider
    
      Constructors:
        * DefaultServiceBeansProvider(java.util.List, java.util.List)
    
    """
    def __init__(self, list: java.util.List[str], list2: java.util.List[str]): ...
    def getBeanNames(self) -> java.util.List[str]: ...
    def getServers(self) -> java.util.List[str]: ...

class ServerRegistryImpl(ServerRegistry):
    """
    Java class 'cern.accsoft.commons.remoting.ServerRegistryImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.remoting.ServerRegistry
    
      Constructors:
        * ServerRegistryImpl(cern.accsoft.commons.remoting.ServiceBeansProvider, cern.accsoft.commons.remoting.ServerScheduler)
    
    """
    def __init__(self, serviceBeansProvider: ServiceBeansProvider, serverScheduler: ServerScheduler): ...
    _getAllServices__T = typing.TypeVar('_getAllServices__T', bound=BusinessService)  # <T>
    def getAllServices(self, class_: typing.Type[_getAllServices__T]) -> java.util.List[_getAllServices__T]: ...
    def getServerServices(self, string: str) -> java.util.List[BusinessServiceDescriptor]: ...
    _getServiceFor__T = typing.TypeVar('_getServiceFor__T', bound=BusinessService)  # <T>
    def getServiceFor(self, class_: typing.Type[_getServiceFor__T]) -> _getServiceFor__T: ...
    def init(self) -> None: ...
    _registerServicesFor__T = typing.TypeVar('_registerServicesFor__T', bound=BusinessService)  # <T>
    def registerServicesFor(self, string: str) -> None: ...

class SimpleServerScheduler(ServerScheduler):
    """
    Java class 'cern.accsoft.commons.remoting.SimpleServerScheduler'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.remoting.ServerScheduler
    
      Constructors:
        * SimpleServerScheduler()
    
    """
    def __init__(self): ...
    _getServiceFrom__T = typing.TypeVar('_getServiceFrom__T', bound=BusinessService)  # <T>
    def getServiceFrom(self, set: java.util.Set[RemoteServer], class_: typing.Type[_getServiceFrom__T]) -> _getServiceFrom__T: ...
    def lockServer(self, remoteServer: RemoteServer) -> None: ...
    def markServerAsUsed(self, remoteServer: RemoteServer) -> None: ...
    def releaseCurrentlyUsedServers(self) -> None: ...
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
