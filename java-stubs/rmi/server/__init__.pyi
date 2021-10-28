import java.io
import java.lang
import java.lang.reflect
import java.net
import java.rmi
import typing



class ExportException(java.rmi.RemoteException):
    """
    Java class 'java.rmi.server.ExportException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * ExportException(java.lang.String)
        * ExportException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class LoaderHandler:
    """
    Java class 'java.rmi.server.LoaderHandler'
    
      Attributes:
        packagePrefix (java.lang.String): final static field
    
    """
    packagePrefix: typing.ClassVar[str] = ...
    def getSecurityContext(self, classLoader: java.lang.ClassLoader) -> typing.Any: ...
    @typing.overload
    def loadClass(self, string: str) -> typing.Type[typing.Any]: ...
    @typing.overload
    def loadClass(self, uRL: java.net.URL, string: str) -> typing.Type[typing.Any]: ...

class LogStream(java.io.PrintStream):
    """
    Java class 'java.rmi.server.LogStream'
    
        Extends:
            java.io.PrintStream
    
      Attributes:
        SILENT (int): final static field
        BRIEF (int): final static field
        VERBOSE (int): final static field
    
    """
    SILENT: typing.ClassVar[int] = ...
    BRIEF: typing.ClassVar[int] = ...
    VERBOSE: typing.ClassVar[int] = ...
    @staticmethod
    def getDefaultStream() -> java.io.PrintStream: ...
    def getOutputStream(self) -> java.io.OutputStream: ...
    @staticmethod
    def log(string: str) -> 'LogStream': ...
    @staticmethod
    def parseLevel(string: str) -> int: ...
    @staticmethod
    def setDefaultStream(printStream: java.io.PrintStream) -> None: ...
    def setOutputStream(self, outputStream: java.io.OutputStream) -> None: ...
    def toString(self) -> str: ...
    @typing.overload
    def write(self, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def write(self, byteArray: typing.List[int], int: int, int2: int) -> None: ...
    @typing.overload
    def write(self, int: int) -> None: ...

class ObjID(java.io.Serializable):
    """
    Java class 'java.rmi.server.ObjID'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * ObjID(int)
        * ObjID()
    
      Attributes:
        REGISTRY_ID (int): final static field
        ACTIVATOR_ID (int): final static field
        DGC_ID (int): final static field
    
    """
    REGISTRY_ID: typing.ClassVar[int] = ...
    ACTIVATOR_ID: typing.ClassVar[int] = ...
    DGC_ID: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def read(objectInput: java.io.ObjectInput) -> 'ObjID': ...
    def toString(self) -> str: ...
    def write(self, objectOutput: java.io.ObjectOutput) -> None: ...

class Operation:
    """
    Java class 'java.rmi.server.Operation'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Operation(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    def getOperation(self) -> str: ...
    def toString(self) -> str: ...

class RMIClassLoader:
    """
    Java class 'java.rmi.server.RMIClassLoader'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def getClassAnnotation(class_: typing.Type[typing.Any]) -> str: ...
    @staticmethod
    def getClassLoader(string: str) -> java.lang.ClassLoader: ...
    @staticmethod
    def getDefaultProviderInstance() -> 'RMIClassLoaderSpi': ...
    @staticmethod
    def getSecurityContext(classLoader: java.lang.ClassLoader) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def loadClass(string: str) -> typing.Type[typing.Any]: ...
    @typing.overload
    @staticmethod
    def loadClass(string: str, string2: str) -> typing.Type[typing.Any]: ...
    @typing.overload
    @staticmethod
    def loadClass(string: str, string2: str, classLoader: java.lang.ClassLoader) -> typing.Type[typing.Any]: ...
    @typing.overload
    @staticmethod
    def loadClass(uRL: java.net.URL, string: str) -> typing.Type[typing.Any]: ...
    @staticmethod
    def loadProxyClass(string: str, stringArray: typing.List[str], classLoader: java.lang.ClassLoader) -> typing.Type[typing.Any]: ...

class RMIClassLoaderSpi:
    """
    Java class 'java.rmi.server.RMIClassLoaderSpi'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RMIClassLoaderSpi()
    
    """
    def __init__(self): ...
    def getClassAnnotation(self, class_: typing.Type[typing.Any]) -> str: ...
    def getClassLoader(self, string: str) -> java.lang.ClassLoader: ...
    def loadClass(self, string: str, string2: str, classLoader: java.lang.ClassLoader) -> typing.Type[typing.Any]: ...
    def loadProxyClass(self, string: str, stringArray: typing.List[str], classLoader: java.lang.ClassLoader) -> typing.Type[typing.Any]: ...

class RMIClientSocketFactory:
    """
    Java class 'java.rmi.server.RMIClientSocketFactory'
    
    """
    def createSocket(self, string: str, int: int) -> java.net.Socket: ...

class RMIFailureHandler:
    """
    Java class 'java.rmi.server.RMIFailureHandler'
    
    """
    def failure(self, exception: java.lang.Exception) -> bool: ...

class RMIServerSocketFactory:
    """
    Java class 'java.rmi.server.RMIServerSocketFactory'
    
    """
    def createServerSocket(self, int: int) -> java.net.ServerSocket: ...

class RemoteCall:
    """
    Java class 'java.rmi.server.RemoteCall'
    
    """
    def done(self) -> None: ...
    def executeCall(self) -> None: ...
    def getInputStream(self) -> java.io.ObjectInput: ...
    def getOutputStream(self) -> java.io.ObjectOutput: ...
    def getResultStream(self, boolean: bool) -> java.io.ObjectOutput: ...
    def releaseInputStream(self) -> None: ...
    def releaseOutputStream(self) -> None: ...

class RemoteObject(java.rmi.Remote, java.io.Serializable):
    """
    Java class 'java.rmi.server.RemoteObject'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.rmi.Remote, java.io.Serializable
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getRef(self) -> 'RemoteRef': ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    @staticmethod
    def toStub(remote: java.rmi.Remote) -> java.rmi.Remote: ...

class RemoteRef(java.io.Externalizable):
    """
    Java class 'java.rmi.server.RemoteRef'
    
        Interfaces:
            java.io.Externalizable
    
      Attributes:
        serialVersionUID (long): final static field
        packagePrefix (java.lang.String): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    packagePrefix: typing.ClassVar[str] = ...
    def done(self, remoteCall: RemoteCall) -> None: ...
    def getRefClass(self, objectOutput: java.io.ObjectOutput) -> str: ...
    @typing.overload
    def invoke(self, remote: java.rmi.Remote, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any], long: int) -> typing.Any: ...
    @typing.overload
    def invoke(self, remoteCall: RemoteCall) -> None: ...
    def newCall(self, remoteObject: RemoteObject, operationArray: typing.List[Operation], int: int, long: int) -> RemoteCall: ...
    def remoteEquals(self, remoteRef: 'RemoteRef') -> bool: ...
    def remoteHashCode(self) -> int: ...
    def remoteToString(self) -> str: ...

class ServerCloneException(java.lang.CloneNotSupportedException):
    """
    Java class 'java.rmi.server.ServerCloneException'
    
        Extends:
            java.lang.CloneNotSupportedException
    
      Constructors:
        * ServerCloneException(java.lang.String)
        * ServerCloneException(java.lang.String, java.lang.Exception)
    
      Attributes:
        detail (java.lang.Exception): field
    
    """
    detail: java.lang.Exception = ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getMessage(self) -> str: ...

class ServerNotActiveException(java.lang.Exception):
    """
    Java class 'java.rmi.server.ServerNotActiveException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ServerNotActiveException()
        * ServerNotActiveException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class Skeleton:
    """
    Java class 'java.rmi.server.Skeleton'
    
    """
    def dispatch(self, remote: java.rmi.Remote, remoteCall: RemoteCall, int: int, long: int) -> None: ...
    def getOperations(self) -> typing.List[Operation]: ...

class SkeletonMismatchException(java.rmi.RemoteException):
    """
    Java class 'java.rmi.server.SkeletonMismatchException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * SkeletonMismatchException(java.lang.String)
    
    """
    def __init__(self, string: str): ...

class SkeletonNotFoundException(java.rmi.RemoteException):
    """
    Java class 'java.rmi.server.SkeletonNotFoundException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * SkeletonNotFoundException(java.lang.String)
        * SkeletonNotFoundException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class UID(java.io.Serializable):
    """
    Java class 'java.rmi.server.UID'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * UID(short)
        * UID()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, short: int): ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def read(dataInput: java.io.DataInput) -> 'UID': ...
    def toString(self) -> str: ...
    def write(self, dataOutput: java.io.DataOutput) -> None: ...

class Unreferenced:
    """
    Java class 'java.rmi.server.Unreferenced'
    
    """
    def unreferenced(self) -> None: ...

class RMISocketFactory(RMIClientSocketFactory, RMIServerSocketFactory):
    """
    Java class 'java.rmi.server.RMISocketFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.rmi.server.RMIClientSocketFactory,
            java.rmi.server.RMIServerSocketFactory
    
      Constructors:
        * RMISocketFactory()
    
    """
    def __init__(self): ...
    def createServerSocket(self, int: int) -> java.net.ServerSocket: ...
    def createSocket(self, string: str, int: int) -> java.net.Socket: ...
    @staticmethod
    def getDefaultSocketFactory() -> 'RMISocketFactory': ...
    @staticmethod
    def getFailureHandler() -> RMIFailureHandler: ...
    @staticmethod
    def getSocketFactory() -> 'RMISocketFactory': ...
    @staticmethod
    def setFailureHandler(rMIFailureHandler: RMIFailureHandler) -> None: ...
    @staticmethod
    def setSocketFactory(rMISocketFactory: 'RMISocketFactory') -> None: ...

class RemoteObjectInvocationHandler(RemoteObject, java.lang.reflect.InvocationHandler):
    """
    Java class 'java.rmi.server.RemoteObjectInvocationHandler'
    
        Extends:
            java.rmi.server.RemoteObject
    
        Interfaces:
            java.lang.reflect.InvocationHandler
    
      Constructors:
        * RemoteObjectInvocationHandler(java.rmi.server.RemoteRef)
    
    """
    def __init__(self, remoteRef: RemoteRef): ...
    def invoke(self, object: typing.Any, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any]) -> typing.Any: ...

class RemoteServer(RemoteObject):
    """
    Java class 'java.rmi.server.RemoteServer'
    
        Extends:
            java.rmi.server.RemoteObject
    
    """
    @staticmethod
    def getClientHost() -> str: ...
    @staticmethod
    def getLog() -> java.io.PrintStream: ...
    @staticmethod
    def setLog(outputStream: java.io.OutputStream) -> None: ...

class RemoteStub(RemoteObject): ...

class ServerRef(RemoteRef):
    """
    Java class 'java.rmi.server.ServerRef'
    
        Interfaces:
            java.rmi.server.RemoteRef
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    def exportObject(self, remote: java.rmi.Remote, object: typing.Any) -> RemoteStub: ...
    def getClientHost(self) -> str: ...

class SocketSecurityException(ExportException):
    """
    Java class 'java.rmi.server.SocketSecurityException'
    
        Extends:
            java.rmi.server.ExportException
    
      Constructors:
        * SocketSecurityException(java.lang.String)
        * SocketSecurityException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class UnicastRemoteObject(RemoteServer):
    """
    Java class 'java.rmi.server.UnicastRemoteObject'
    
        Extends:
            java.rmi.server.RemoteServer
    
    """
    def clone(self) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def exportObject(remote: java.rmi.Remote, int: int) -> java.rmi.Remote: ...
    @typing.overload
    @staticmethod
    def exportObject(remote: java.rmi.Remote, int: int, objectInputFilter: typing.Union[java.io.ObjectInputFilter, typing.Callable]) -> java.rmi.Remote: ...
    @typing.overload
    @staticmethod
    def exportObject(remote: java.rmi.Remote, int: int, rMIClientSocketFactory: RMIClientSocketFactory, rMIServerSocketFactory: RMIServerSocketFactory) -> java.rmi.Remote: ...
    @typing.overload
    @staticmethod
    def exportObject(remote: java.rmi.Remote, int: int, rMIClientSocketFactory: RMIClientSocketFactory, rMIServerSocketFactory: RMIServerSocketFactory, objectInputFilter: typing.Union[java.io.ObjectInputFilter, typing.Callable]) -> java.rmi.Remote: ...
    @typing.overload
    @staticmethod
    def exportObject(remote: java.rmi.Remote) -> RemoteStub: ...
    @staticmethod
    def unexportObject(remote: java.rmi.Remote, boolean: bool) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.rmi.server")``.

    ExportException: typing.Type[ExportException]
    LoaderHandler: typing.Type[LoaderHandler]
    LogStream: typing.Type[LogStream]
    ObjID: typing.Type[ObjID]
    Operation: typing.Type[Operation]
    RMIClassLoader: typing.Type[RMIClassLoader]
    RMIClassLoaderSpi: typing.Type[RMIClassLoaderSpi]
    RMIClientSocketFactory: typing.Type[RMIClientSocketFactory]
    RMIFailureHandler: typing.Type[RMIFailureHandler]
    RMIServerSocketFactory: typing.Type[RMIServerSocketFactory]
    RMISocketFactory: typing.Type[RMISocketFactory]
    RemoteCall: typing.Type[RemoteCall]
    RemoteObject: typing.Type[RemoteObject]
    RemoteObjectInvocationHandler: typing.Type[RemoteObjectInvocationHandler]
    RemoteRef: typing.Type[RemoteRef]
    RemoteServer: typing.Type[RemoteServer]
    RemoteStub: typing.Type[RemoteStub]
    ServerCloneException: typing.Type[ServerCloneException]
    ServerNotActiveException: typing.Type[ServerNotActiveException]
    ServerRef: typing.Type[ServerRef]
    Skeleton: typing.Type[Skeleton]
    SkeletonMismatchException: typing.Type[SkeletonMismatchException]
    SkeletonNotFoundException: typing.Type[SkeletonNotFoundException]
    SocketSecurityException: typing.Type[SocketSecurityException]
    UID: typing.Type[UID]
    UnicastRemoteObject: typing.Type[UnicastRemoteObject]
    Unreferenced: typing.Type[Unreferenced]
