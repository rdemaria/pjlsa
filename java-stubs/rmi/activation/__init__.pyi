from typing import Any as _py_Any
from typing import List as _py_List
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.io
import java.lang
import java.rmi
import java.rmi.server
import java.util


class Activatable(java.rmi.server.RemoteServer):
    @classmethod
    @overload
    def exportObject(cls, remote: java.rmi.Remote, activationID: 'ActivationID', int: int) -> java.rmi.Remote: ...
    @classmethod
    @overload
    def exportObject(cls, remote: java.rmi.Remote, activationID: 'ActivationID', int: int, rMIClientSocketFactory: java.rmi.server.RMIClientSocketFactory, rMIServerSocketFactory: java.rmi.server.RMIServerSocketFactory) -> java.rmi.Remote: ...
    @classmethod
    @overload
    def exportObject(cls, remote: java.rmi.Remote, string: str, marshalledObject: java.rmi.MarshalledObject[_py_Any], boolean: bool, int: int) -> 'ActivationID': ...
    @classmethod
    @overload
    def exportObject(cls, remote: java.rmi.Remote, string: str, marshalledObject: java.rmi.MarshalledObject[_py_Any], boolean: bool, int: int, rMIClientSocketFactory: java.rmi.server.RMIClientSocketFactory, rMIServerSocketFactory: java.rmi.server.RMIServerSocketFactory) -> 'ActivationID': ...
    @classmethod
    def inactive(cls, activationID: 'ActivationID') -> bool: ...
    @classmethod
    def register(cls, activationDesc: 'ActivationDesc') -> java.rmi.Remote: ...
    @classmethod
    def unexportObject(cls, remote: java.rmi.Remote, boolean: bool) -> bool: ...
    @classmethod
    def unregister(cls, activationID: 'ActivationID') -> None: ...

class ActivateFailedException(java.rmi.RemoteException):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ActivationDesc(java.io.Serializable):
    @overload
    def __init__(self, string: str, string2: str, marshalledObject: java.rmi.MarshalledObject[_py_Any]): ...
    @overload
    def __init__(self, string: str, string2: str, marshalledObject: java.rmi.MarshalledObject[_py_Any], boolean: bool): ...
    @overload
    def __init__(self, activationGroupID: 'ActivationGroupID', string: str, string2: str, marshalledObject: java.rmi.MarshalledObject[_py_Any]): ...
    @overload
    def __init__(self, activationGroupID: 'ActivationGroupID', string: str, string2: str, marshalledObject: java.rmi.MarshalledObject[_py_Any], boolean: bool): ...
    def equals(self, object: _py_Any) -> bool: ...
    def getClassName(self) -> str: ...
    def getData(self) -> java.rmi.MarshalledObject[_py_Any]: ...
    def getGroupID(self) -> 'ActivationGroupID': ...
    def getLocation(self) -> str: ...
    def getRestartMode(self) -> bool: ...
    def hashCode(self) -> int: ...

class ActivationException(java.lang.Exception):
    detail: java.lang.Throwable = ...
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getMessage(self) -> str: ...

class ActivationGroupDesc(java.io.Serializable):
    @overload
    def __init__(self, string: str, string2: str, marshalledObject: java.rmi.MarshalledObject[_py_Any], properties: java.util.Properties, commandEnvironment: 'ActivationGroupDesc.CommandEnvironment'): ...
    @overload
    def __init__(self, properties: java.util.Properties, commandEnvironment: 'ActivationGroupDesc.CommandEnvironment'): ...
    def equals(self, object: _py_Any) -> bool: ...
    def getClassName(self) -> str: ...
    def getCommandEnvironment(self) -> 'ActivationGroupDesc.CommandEnvironment': ...
    def getData(self) -> java.rmi.MarshalledObject[_py_Any]: ...
    def getLocation(self) -> str: ...
    def getPropertyOverrides(self) -> java.util.Properties: ...
    def hashCode(self) -> int: ...
    class CommandEnvironment(java.io.Serializable):
        def __init__(self, string: str, stringArray: _py_List[str]): ...
        def equals(self, object: _py_Any) -> bool: ...
        def getCommandOptions(self) -> _py_List[str]: ...
        def getCommandPath(self) -> str: ...
        def hashCode(self) -> int: ...

class ActivationGroupID(java.io.Serializable):
    def __init__(self, activationSystem: 'ActivationSystem'): ...
    def equals(self, object: _py_Any) -> bool: ...
    def getSystem(self) -> 'ActivationSystem': ...
    def hashCode(self) -> int: ...

class ActivationID(java.io.Serializable):
    def __init__(self, activator: 'Activator'): ...
    def activate(self, boolean: bool) -> java.rmi.Remote: ...
    def equals(self, object: _py_Any) -> bool: ...
    def hashCode(self) -> int: ...

class ActivationInstantiator(java.rmi.Remote):
    def newInstance(self, activationID: ActivationID, activationDesc: ActivationDesc) -> java.rmi.MarshalledObject[java.rmi.Remote]: ...

class ActivationMonitor(java.rmi.Remote):
    def activeObject(self, activationID: ActivationID, marshalledObject: java.rmi.MarshalledObject[java.rmi.Remote]) -> None: ...
    def inactiveGroup(self, activationGroupID: ActivationGroupID, long: int) -> None: ...
    def inactiveObject(self, activationID: ActivationID) -> None: ...

class ActivationSystem(java.rmi.Remote):
    SYSTEM_PORT: _py_ClassVar[int] = ...
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
    def activate(self, activationID: ActivationID, boolean: bool) -> java.rmi.MarshalledObject[java.rmi.Remote]: ...

class ActivationGroup(java.rmi.server.UnicastRemoteObject, ActivationInstantiator):
    def activeObject(self, activationID: ActivationID, remote: java.rmi.Remote) -> None: ...
    @classmethod
    def createGroup(cls, activationGroupID: ActivationGroupID, activationGroupDesc: ActivationGroupDesc, long: int) -> 'ActivationGroup': ...
    @classmethod
    def currentGroupID(cls) -> ActivationGroupID: ...
    @classmethod
    def getSystem(cls) -> ActivationSystem: ...
    def inactiveObject(self, activationID: ActivationID) -> bool: ...
    @classmethod
    def setSystem(cls, activationSystem: ActivationSystem) -> None: ...

class ActivationGroup_Stub(java.rmi.server.RemoteStub, ActivationInstantiator, java.rmi.Remote):
    def __init__(self, remoteRef: java.rmi.server.RemoteRef): ...
    def newInstance(self, activationID: ActivationID, activationDesc: ActivationDesc) -> java.rmi.MarshalledObject: ...

class UnknownGroupException(ActivationException):
    def __init__(self, string: str): ...

class UnknownObjectException(ActivationException):
    def __init__(self, string: str): ...