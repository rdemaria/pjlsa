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
    public class CcdbServiceConfigLookup extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.factory.ServiceConfigLookup`
    
        :class:`~cern.japc.core.spi.factory.ServiceConfigLookup` implementation which uses CCDB as a source.
    """
    def __init__(self): ...
    def getConfig(self, string: str) -> typing.List[java.util.Properties]:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.factory.ServiceConfigLookup.getConfig`
            Returns an array of configurations for a service with the given name. Different configurations could come from that
            fact, that service could provide more than one way of connecting to it: http or JMS or something else.
        
            Specified by:
                :meth:`~cern.japc.core.spi.factory.ServiceConfigLookup.getConfig`Â in
                interfaceÂ :class:`~cern.japc.core.spi.factory.ServiceConfigLookup`
        
            Parameters:
                serviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the service
        
            Returns:
                an array of properties containing configurations for a service. If no configurations found an empty array should be
                returned.
        
        
        """
        ...

class CcdbServiceNameResolver(cern.japc.core.factory.ServiceNameResolver):
    """
    public class CcdbServiceNameResolver extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.factory.ServiceNameResolver`
    
        :class:`~cern.japc.core.factory.ServiceNameResolver` implementation which uses CCDB as a source.
    """
    SYSPROP_JAPC_CCDB_SERVICE_NAME_RESOLVER_DISABLED: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_JAPC_CCDB_SERVICE_NAME_RESOLVER_DISABLED
    
        System property to disable JAPC CCDB service name resolver
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def getServiceName(self, string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.core.factory.ServiceNameResolver.getServiceName`
            This method returns the name of the service to use for parameter or null if this parameter name is unknown to this
            resolver.
        
            Specified by:
                :meth:`~cern.japc.core.factory.ServiceNameResolver.getServiceName`Â in
                interfaceÂ :class:`~cern.japc.core.factory.ServiceNameResolver`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter
                parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`): the descriptor of the parameter
        
            Returns:
                the name of the creator to use or :code:`null` if this parameter name is unknown to this resolver
        
        
        """
        ...

class DirectoryLocator:
    """
    public abstract class DirectoryLocator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self): ...
    @staticmethod
    def get() -> cern.cmw.directory.client.DirectoryClient: ...

class ServiceBinder:
    """
    public class ServiceBinder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class is used to bind a new service to the CCDB directory.
    
        Essentially, this class is just a script to send the information about a new service (or an update) to the CMW
        Directory.
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
