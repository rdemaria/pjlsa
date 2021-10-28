import cern.japc.core.spi.factory
import java.util
import typing



class LsaNonproEnvironmentServiceConfigLookup(cern.japc.core.spi.factory.ServiceConfigLookup):
    """
    Java class 'cern.lsa.client.spi.japc.LsaNonproEnvironmentServiceConfigLookup'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.factory.ServiceConfigLookup
    
      Constructors:
        * LsaNonproEnvironmentServiceConfigLookup()
    
    """
    def __init__(self): ...
    def getConfig(self, string: str) -> typing.List[java.util.Properties]: ...
    @staticmethod
    def setServerPropertyFileName(string: str) -> None: ...

class NonproEnvironmentServiceConfigLookup(cern.japc.core.spi.factory.ServiceConfigLookup):
    """
    Java class 'cern.lsa.client.spi.japc.NonproEnvironmentServiceConfigLookup'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.factory.ServiceConfigLookup
    
      Constructors:
        * NonproEnvironmentServiceConfigLookup()
    
    """
    def __init__(self): ...
    def getConfig(self, string: str) -> typing.List[java.util.Properties]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.spi.japc")``.

    LsaNonproEnvironmentServiceConfigLookup: typing.Type[LsaNonproEnvironmentServiceConfigLookup]
    NonproEnvironmentServiceConfigLookup: typing.Type[NonproEnvironmentServiceConfigLookup]
