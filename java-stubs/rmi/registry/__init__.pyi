import java.rmi
import java.rmi.server
import typing



class LocateRegistry:
    """
    Java class 'java.rmi.registry.LocateRegistry'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    @staticmethod
    def createRegistry(int: int) -> 'Registry': ...
    @typing.overload
    @staticmethod
    def createRegistry(int: int, rMIClientSocketFactory: java.rmi.server.RMIClientSocketFactory, rMIServerSocketFactory: java.rmi.server.RMIServerSocketFactory) -> 'Registry': ...
    @typing.overload
    @staticmethod
    def getRegistry() -> 'Registry': ...
    @typing.overload
    @staticmethod
    def getRegistry(int: int) -> 'Registry': ...
    @typing.overload
    @staticmethod
    def getRegistry(string: str) -> 'Registry': ...
    @typing.overload
    @staticmethod
    def getRegistry(string: str, int: int) -> 'Registry': ...
    @typing.overload
    @staticmethod
    def getRegistry(string: str, int: int, rMIClientSocketFactory: java.rmi.server.RMIClientSocketFactory) -> 'Registry': ...

class Registry(java.rmi.Remote):
    """
    Java class 'java.rmi.registry.Registry'
    
        Interfaces:
            java.rmi.Remote
    
      Attributes:
        REGISTRY_PORT (int): final static field
    
    """
    REGISTRY_PORT: typing.ClassVar[int] = ...
    def bind(self, string: str, remote: java.rmi.Remote) -> None: ...
    def list(self) -> typing.List[str]: ...
    def lookup(self, string: str) -> java.rmi.Remote: ...
    def rebind(self, string: str, remote: java.rmi.Remote) -> None: ...
    def unbind(self, string: str) -> None: ...

class RegistryHandler:
    """
    Java class 'java.rmi.registry.RegistryHandler'
    
    """
    def registryImpl(self, int: int) -> Registry: ...
    def registryStub(self, string: str, int: int) -> Registry: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.rmi.registry")``.

    LocateRegistry: typing.Type[LocateRegistry]
    Registry: typing.Type[Registry]
    RegistryHandler: typing.Type[RegistryHandler]
