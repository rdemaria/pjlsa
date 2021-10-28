import cern.cmw.directory.client
import cern.japc.core
import cern.japc.core.directory.client.services
import cern.japc.core.directory.client.spi
import cern.japc.core.factory
import cern.japc.core.spi.factory
import java.util
import typing



class CcdbServiceConfigLookup(cern.japc.core.spi.factory.ServiceConfigLookup):
    """
    Java class 'cern.japc.core.directory.client.CcdbServiceConfigLookup'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.factory.ServiceConfigLookup
    
      Constructors:
        * CcdbServiceConfigLookup()
    
    """
    def __init__(self): ...
    def getConfig(self, string: str) -> typing.List[java.util.Properties]: ...

class CcdbServiceNameResolver(cern.japc.core.factory.ServiceNameResolver):
    """
    Java class 'cern.japc.core.directory.client.CcdbServiceNameResolver'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.factory.ServiceNameResolver
    
      Constructors:
        * CcdbServiceNameResolver()
    
      Attributes:
        SYSPROP_JAPC_CCDB_SERVICE_NAME_RESOLVER_DISABLED (java.lang.String): final static field
    
    """
    SYSPROP_JAPC_CCDB_SERVICE_NAME_RESOLVER_DISABLED: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getServiceName(self, string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> str: ...

class DirectoryLocator:
    """
    Java class 'cern.japc.core.directory.client.DirectoryLocator'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * DirectoryLocator()
    
    """
    def __init__(self): ...
    @staticmethod
    def get() -> cern.cmw.directory.client.DirectoryClient: ...

class ServiceBinder:
    """
    Java class 'cern.japc.core.directory.client.ServiceBinder'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ServiceBinder()
    
    """
    def __init__(self): ...
    @staticmethod
    def bind(properties: java.util.Properties) -> None: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    @staticmethod
    def update(serverInfo: cern.cmw.directory.client.ServerInfo) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.directory.client")``.

    CcdbServiceConfigLookup: typing.Type[CcdbServiceConfigLookup]
    CcdbServiceNameResolver: typing.Type[CcdbServiceNameResolver]
    DirectoryLocator: typing.Type[DirectoryLocator]
    ServiceBinder: typing.Type[ServiceBinder]
    services: cern.japc.core.directory.client.services.__module_protocol__
    spi: cern.japc.core.directory.client.spi.__module_protocol__
