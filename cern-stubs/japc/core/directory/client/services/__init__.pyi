import java.util
import typing



class BindInstance:
    """
    Java class 'cern.japc.core.directory.client.services.BindInstance'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * BindInstance()
    
      Attributes:
        globalList (java.util.HashMap): static field
    
    """
    globalList: typing.ClassVar[java.util.HashMap] = ...
    def __init__(self): ...
    def checkExisting(self) -> bool: ...
    def getServerInfo(self) -> java.util.Properties: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.directory.client.services")``.

    BindInstance: typing.Type[BindInstance]
