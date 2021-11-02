import cern.japc.core.spi.factory
import java.util
import typing



class LsaNonproEnvironmentServiceConfigLookup(cern.japc.core.spi.factory.ServiceConfigLookup):
    """
    public class LsaNonproEnvironmentServiceConfigLookup extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.japc.core.spi.factory.ServiceConfigLookup
    
        Should be used by both LSA server and clients to redirect japc operations to the a non-pro server.
    
    
        The standard JAPC system property :code:`metafactory.service.config.lookups` should be set before
        :code:`ParameterFactory` is initialized.
    """
    def __init__(self): ...
    def getConfig(self, string: str) -> typing.List[java.util.Properties]:
        """
        
            Specified by:
                :code:`getConfig` in interface :code:`cern.japc.core.spi.factory.ServiceConfigLookup`
        
        
        """
        ...
    @staticmethod
    def setServerPropertyFileName(string: str) -> None: ...

class NonproEnvironmentServiceConfigLookup(cern.japc.core.spi.factory.ServiceConfigLookup):
    """
    public class NonproEnvironmentServiceConfigLookup extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.japc.core.spi.factory.ServiceConfigLookup
    
        Should be used by both LSA server and clients to redirect japc operations to the a non-pro server.
    
    
        The standard JAPC system property :code:`metafactory.service.config.lookups` should be set before
        :code:`ParameterFactory` is initialized.
    """
    def __init__(self): ...
    def getConfig(self, string: str) -> typing.List[java.util.Properties]:
        """
        
            Specified by:
                :code:`getConfig` in interface :code:`cern.japc.core.spi.factory.ServiceConfigLookup`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.spi.japc")``.

    LsaNonproEnvironmentServiceConfigLookup: typing.Type[LsaNonproEnvironmentServiceConfigLookup]
    NonproEnvironmentServiceConfigLookup: typing.Type[NonproEnvironmentServiceConfigLookup]
