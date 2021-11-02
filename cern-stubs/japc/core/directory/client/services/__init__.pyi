import java.util
import typing



class BindInstance:
    """
    public abstract class BindInstance extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    globalList: typing.ClassVar[java.util.HashMap] = ...
    """
    public static `HashMap <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/HashMap.html?is-external=true>`<`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`, :class:`~cern.japc.core.directory.client.services.BindInstance`> globalList
    
    
    """
    def __init__(self): ...
    def checkExisting(self) -> bool: ...
    def getServerInfo(self) -> java.util.Properties: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.directory.client.services")``.

    BindInstance: typing.Type[BindInstance]
