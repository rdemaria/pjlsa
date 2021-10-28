import cern.cmw.directory.client
import java.util
import typing



class ServerInfoUtil:
    """
    Java class 'cern.japc.core.directory.client.spi.ServerInfoUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ServerInfoUtil()
    
      Attributes:
        MAX_SERVICE_URL_LENGTH (int): final static field
    
    """
    MAX_SERVICE_URL_LENGTH: typing.ClassVar[int] = ...
    def __init__(self): ...
    @staticmethod
    def getProperties(serverInfo: cern.cmw.directory.client.ServerInfo) -> typing.List[java.util.Properties]: ...
    @staticmethod
    def getServerInfo(propertiesArray: typing.List[java.util.Properties]) -> cern.cmw.directory.client.ServerInfo: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.directory.client.spi")``.

    ServerInfoUtil: typing.Type[ServerInfoUtil]
