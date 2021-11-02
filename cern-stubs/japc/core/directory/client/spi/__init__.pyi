import cern.cmw.directory.client
import java.util
import typing



class ServerInfoUtil:
    """
    public class ServerInfoUtil extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods to encode and decode the configuration of services into/from :code:`ServerInfo`.
    """
    MAX_SERVICE_URL_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int MAX_SERVICE_URL_LENGTH
    
        The maximum allowed service url length
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    @staticmethod
    def getProperties(serverInfo: cern.cmw.directory.client.ServerInfo) -> typing.List[java.util.Properties]: ...
    @staticmethod
    def getServerInfo(propertiesArray: typing.List[java.util.Properties]) -> cern.cmw.directory.client.ServerInfo: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.directory.client.spi")``.

    ServerInfoUtil: typing.Type[ServerInfoUtil]
