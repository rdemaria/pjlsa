import java.io
import java.lang
import java.rmi
import java.rmi.server
import java.util
import typing



class Activatable(java.rmi.server.RemoteServer):
    """
    Java class 'java.rmi.activation.Activatable'
    
        Extends:
            java.rmi.server.RemoteServer
    
    """
    @typing.overload
    @staticmethod
    def exportObject(remote: java.rmi.Remote, activationID: 'ActivationID', int: int) -> java.rmi.Remote: ...
    @typing.overload
    @staticmethod
    def exportObject(remote: java.rmi.Remote, activationID: 'ActivationID', int: int, rMIClientSocketFactory: java.rmi.server.RMIClientSocketFactory, rMIServerSocketFactory: java.rmi.server.RMIServerSocketFactory) -> java.rmi.Remote: ...
    @typing.overload
    @staticmethod
    def exportObject(remote: java.rmi.Remote, string: str, marshalledObject: java.rmi.MarshalledObject[typing.Any], boolean: bool, int: int) -> 'ActivationID': ...
    @typing.overload
    @staticmethod
    def exportObject(remote: java.rmi.Remote, string: str, marshalledObject: java.rmi.MarshalledObject[typing.Any], boolean: bool, int: int, rMIClientSocketFactory: java.rmi.server.RMIClientSocketFactory, rMIServerSocketFactory: java.rmi.server.RMIServerSocketFactory) -> 'ActivationID': ...
    @staticmethod
    def inactive(activationID: 'ActivationID') -> bool: ...
    @staticmethod
    def register(activationDesc: 'ActivationDesc') -> java.rmi.Remote: ...
    @staticmethod
    def unexportObject(remote: java.rmi.Remote, boolean: bool) -> bool: ...
    @staticmethod
    def unregister(activationID: 'ActivationID') -> None: ...

class ActivateFailedException(java.rmi.RemoteException):
    """
    Java class 'java.rmi.activation.ActivateFailedException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * ActivateFailedException(java.lang.String)
        * ActivateFailedException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ActivationDesc(java.io.Serializable):
    """
    Java class 'java.rmi.activation.ActivationDesc'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * ActivationDesc(java.rmi.activation.ActivationGroupID, java.lang.String, java.lang.String, java.rmi.MarshalledObject, boolean)
        * ActivationDesc(java.rmi.activation.ActivationGroupID, java.lang.String, java.lang.String, java.rmi.MarshalledObject)
        * ActivationDesc(java.lang.String, java.lang.String, java.rmi.MarshalledObject, boolean)
        * ActivationDesc(java.lang.String, java.lang.String, java.rmi.MarshalledObject)
    
      Raises:
        java.rmi.activation.ActivationException: from java
    
    """
    @typing.overload
    def __init__(self, string: str, string2: str, marshalledObject: java.rmi.MarshalledObject[typing.Any]): ...
    @typing.overload
    def __init__(self, string: str, string2: str, marshalledObject: java.rmi.MarshalledObject[typing.Any], boolean: bool): ...
    @typing.overload
    def __init__(self, activationGroupID: 'ActivationGroupID', string: str, string2: str, marshalledObject: java.rmi.MarshalledObject[typing.Any]): ...
    @typing.overload
    def __init__(self, activationGroupID: 'ActivationGroupID', string: str, string2: str, marshalledObject: java.rmi.MarshalledObject[typing.Any], boolean: bool): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getClassName(self) -> str: ...
    def getData(self) -> java.rmi.MarshalledObject[typing.Any]: ...
    def getGroupID(self) -> 'ActivationGroupID': ...
    def getLocation(self) -> str: ...
    def getRestartMode(self) -> bool: ...
    def hashCode(self) -> int: ...

class ActivationException(java.lang.Exception):
    """
    Java class 'java.rmi.activation.ActivationException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ActivationException(java.lang.String, java.lang.Throwable)
        * ActivationException(java.lang.String)
        * ActivationException()
    
      Attributes:
        detail (java.lang.Throwable): field
    
    """
    detail: java.lang.Throwable = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getMessage(self) -> str: ...

class ActivationGroupDesc(java.io.Serializable):
    """
    Java class 'java.rmi.activation.ActivationGroupDesc'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * ActivationGroupDesc(java.util.Properties, java.rmi.activation.ActivationGroupDesc.CommandEnvironment)
        * ActivationGroupDesc(java.lang.String, java.lang.String, java.rmi.MarshalledObject, java.util.Properties, java.rmi.activation.ActivationGroupDesc.CommandEnvironment)
    
    """
    @typing.overload
    def __init__(self, string: str, string2: str, marshalledObject: java.rmi.MarshalledObject[typing.Any], properties: java.util.Properties, commandEnvironment: 'ActivationGroupDesc.CommandEnvironment'): ...
    @typing.overload
    def __init__(self, properties: java.util.Properties, commandEnvironment: 'ActivationGroupDesc.CommandEnvironment'): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getClassName(self) -> str: ...
    def getCommandEnvironment(self) -> 'ActivationGroupDesc.CommandEnvironment': ...
    def getData(self) -> java.rmi.MarshalledObject[typing.Any]: ...
    def getLocation(self) -> str: ...
    def getPropertyOverrides(self) -> java.util.Properties: ...
    def hashCode(self) -> int: ...
    class CommandEnvironment(java.io.Serializable):
        """
        Java class 'java.rmi.activation.ActivationGroupDesc$CommandEnvironment'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.io.Serializable
        
          Constructors:
            * CommandEnvironment(java.lang.String, java.lang.String[])
        
        """
        def __init__(self, string: str, stringArray: typing.List[str]): ...
        def equals(self, object: typing.Any) -> bool: ...
        def getCommandOptions(self) -> typing.List[str]: ...
        def getCommandPath(self) -> str: ...
        def hashCode(self) -> int: ...

class ActivationGroupID(java.io.Serializable):
    """
    Java class 'java.rmi.activation.ActivationGroupID'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * ActivationGroupID(java.rmi.activation.ActivationSystem)
    
    """
    def __init__(self, activationSystem: 'ActivationSystem'): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getSystem(self) -> 'ActivationSystem': ...
    def hashCode(self) -> int: ...

class ActivationID(java.io.Serializable):
    """
    Java class 'java.rmi.activation.ActivationID'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * ActivationID(java.rmi.activation.Activator)
    
    """
    def __init__(self, activator: 'Activator'): ...
    def activate(self, boolean: bool) -> java.rmi.Remote: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...

class ActivationInstantiator(java.rmi.Remote):
    """
    Java class 'java.rmi.activation.ActivationInstantiator'
    
        Interfaces:
            java.rmi.Remote
    
    """
    def newInstance(self, activationID: ActivationID, activationDesc: ActivationDesc) -> java.rmi.MarshalledObject[java.rmi.Remote]: ...

class ActivationMonitor(java.rmi.Remote):
    """
    Java class 'java.rmi.activation.ActivationMonitor'
    
        Interfaces:
            java.rmi.Remote
    
    """
    def activeObject(self, activationID: ActivationID, marshalledObject: java.rmi.MarshalledObject[java.rmi.Remote]) -> None: ...
    def inactiveGroup(self, activationGroupID: ActivationGroupID, long: int) -> None: ...
    def inactiveObject(self, activationID: ActivationID) -> None: ...

class ActivationSystem(java.rmi.Remote):
    """
    Java class 'java.rmi.activation.ActivationSystem'
    
        Interfaces:
            java.rmi.Remote
    
      Attributes:
        SYSTEM_PORT (int): final static field
    
    """
    SYSTEM_PORT: typing.ClassVar[int] = ...
    def activeGroup(self, activationGroupID: ActivationGroupID, activationInstantiator: ActivationInstantiator, long: int) -> ActivationMonitor: ...
    def getActivationDesc(self, activationID: ActivationID) -> ActivationDesc: ...
    def getActivationGroupDesc(self, activationGroupID: ActivationGroupID) -> ActivationGroupDesc: ...
    def registerGroup(self, activationGroupDesc: ActivationGroupDesc) -> ActivationGroupID: ...
    def registerObject(self, activationDesc: ActivationDesc) -> ActivationID: ...
    def setActivationDesc(self, activationID: ActivationID, activationDesc: ActivationDesc) -> ActivationDesc: ...
    def setActivationGroupDesc(self, activationGroupID: ActivationGroupID, activationGroupDesc: ActivationGroupDesc) -> ActivationGroupDesc: ...
    def shutdown(self) -> None: ...
    def unregisterGroup(self, activationGroupID: ActivationGroupID) -> None: ...
    def unregisterObject(self, activationID: ActivationID) -> None: ...

class Activator(java.rmi.Remote):
    """
    Java class 'java.rmi.activation.Activator'
    
        Interfaces:
            java.rmi.Remote
    
    """
    def activate(self, activationID: ActivationID, boolean: bool) -> java.rmi.MarshalledObject[java.rmi.Remote]: ...

class ActivationGroup(java.rmi.server.UnicastRemoteObject, ActivationInstantiator):
    """
    Java class 'java.rmi.activation.ActivationGroup'
    
        Extends:
            java.rmi.server.UnicastRemoteObject
    
        Interfaces:
            java.rmi.activation.ActivationInstantiator
    
    """
    def activeObject(self, activationID: ActivationID, remote: java.rmi.Remote) -> None: ...
    @staticmethod
    def createGroup(activationGroupID: ActivationGroupID, activationGroupDesc: ActivationGroupDesc, long: int) -> 'ActivationGroup': ...
    @staticmethod
    def currentGroupID() -> ActivationGroupID: ...
    @staticmethod
    def getSystem() -> ActivationSystem: ...
    def inactiveObject(self, activationID: ActivationID) -> bool: ...
    @staticmethod
    def setSystem(activationSystem: ActivationSystem) -> None: ...

class ActivationGroup_Stub(java.rmi.server.RemoteStub, ActivationInstantiator, java.rmi.Remote):
    """
    Java class 'java.rmi.activation.ActivationGroup_Stub'
    
        Extends:
            java.rmi.server.RemoteStub
    
        Interfaces:
            java.rmi.activation.ActivationInstantiator, java.rmi.Remote
    
      Constructors:
        * ActivationGroup_Stub(java.rmi.server.RemoteRef)
    
    """
    def __init__(self, remoteRef: java.rmi.server.RemoteRef): ...
    def newInstance(self, activationID: ActivationID, activationDesc: ActivationDesc) -> java.rmi.MarshalledObject: ...

class UnknownGroupException(ActivationException):
    """
    Java class 'java.rmi.activation.UnknownGroupException'
    
        Extends:
            java.rmi.activation.ActivationException
    
      Constructors:
        * UnknownGroupException(java.lang.String)
    
    """
    def __init__(self, string: str): ...

class UnknownObjectException(ActivationException):
    """
    Java class 'java.rmi.activation.UnknownObjectException'
    
        Extends:
            java.rmi.activation.ActivationException
    
      Constructors:
        * UnknownObjectException(java.lang.String)
    
    """
    def __init__(self, string: str): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.rmi.activation")``.

    Activatable: typing.Type[Activatable]
    ActivateFailedException: typing.Type[ActivateFailedException]
    ActivationDesc: typing.Type[ActivationDesc]
    ActivationException: typing.Type[ActivationException]
    ActivationGroup: typing.Type[ActivationGroup]
    ActivationGroupDesc: typing.Type[ActivationGroupDesc]
    ActivationGroupID: typing.Type[ActivationGroupID]
    ActivationGroup_Stub: typing.Type[ActivationGroup_Stub]
    ActivationID: typing.Type[ActivationID]
    ActivationInstantiator: typing.Type[ActivationInstantiator]
    ActivationMonitor: typing.Type[ActivationMonitor]
    ActivationSystem: typing.Type[ActivationSystem]
    Activator: typing.Type[Activator]
    UnknownGroupException: typing.Type[UnknownGroupException]
    UnknownObjectException: typing.Type[UnknownObjectException]
