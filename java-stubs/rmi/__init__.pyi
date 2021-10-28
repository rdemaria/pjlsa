import java.io
import java.lang
import java.rmi.activation
import java.rmi.dgc
import java.rmi.registry
import java.rmi.server
import typing



class AlreadyBoundException(java.lang.Exception):
    """
    Java class 'java.rmi.AlreadyBoundException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * AlreadyBoundException()
        * AlreadyBoundException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

_MarshalledObject__T = typing.TypeVar('_MarshalledObject__T')  # <T>
class MarshalledObject(java.io.Serializable, typing.Generic[_MarshalledObject__T]):
    """
    Java class 'java.rmi.MarshalledObject'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * MarshalledObject(java.lang.Object)
    
      Raises:
        java.io.IOException: from java
    
    """
    def __init__(self, t: _MarshalledObject__T): ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self) -> _MarshalledObject__T: ...
    def hashCode(self) -> int: ...

class Naming:
    """
    Java class 'java.rmi.Naming'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def bind(string: str, remote: 'Remote') -> None: ...
    @staticmethod
    def list(string: str) -> typing.List[str]: ...
    @staticmethod
    def lookup(string: str) -> 'Remote': ...
    @staticmethod
    def rebind(string: str, remote: 'Remote') -> None: ...
    @staticmethod
    def unbind(string: str) -> None: ...

class NotBoundException(java.lang.Exception):
    """
    Java class 'java.rmi.NotBoundException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * NotBoundException()
        * NotBoundException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class RMISecurityException(java.lang.SecurityException):
    """
    Java class 'java.rmi.RMISecurityException'
    
        Extends:
            java.lang.SecurityException
    
      Constructors:
        * RMISecurityException(java.lang.String)
        * RMISecurityException(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...

class RMISecurityManager(java.lang.SecurityManager):
    """
    Java class 'java.rmi.RMISecurityManager'
    
        Extends:
            java.lang.SecurityManager
    
      Constructors:
        * RMISecurityManager()
    
    """
    def __init__(self): ...

class Remote: ...

class RemoteException(java.io.IOException):
    """
    Java class 'java.rmi.RemoteException'
    
        Extends:
            java.io.IOException
    
      Constructors:
        * RemoteException(java.lang.String, java.lang.Throwable)
        * RemoteException(java.lang.String)
        * RemoteException()
    
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

class AccessException(RemoteException):
    """
    Java class 'java.rmi.AccessException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * AccessException(java.lang.String)
        * AccessException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ConnectException(RemoteException):
    """
    Java class 'java.rmi.ConnectException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * ConnectException(java.lang.String)
        * ConnectException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ConnectIOException(RemoteException):
    """
    Java class 'java.rmi.ConnectIOException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * ConnectIOException(java.lang.String)
        * ConnectIOException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class MarshalException(RemoteException):
    """
    Java class 'java.rmi.MarshalException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * MarshalException(java.lang.String)
        * MarshalException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class NoSuchObjectException(RemoteException):
    """
    Java class 'java.rmi.NoSuchObjectException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * NoSuchObjectException(java.lang.String)
    
    """
    def __init__(self, string: str): ...

class ServerError(RemoteException):
    """
    Java class 'java.rmi.ServerError'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * ServerError(java.lang.String, java.lang.Error)
    
    """
    def __init__(self, string: str, error: java.lang.Error): ...

class ServerException(RemoteException):
    """
    Java class 'java.rmi.ServerException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * ServerException(java.lang.String)
        * ServerException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ServerRuntimeException(RemoteException):
    """
    Java class 'java.rmi.ServerRuntimeException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * ServerRuntimeException(java.lang.String, java.lang.Exception)
    
    """
    def __init__(self, string: str, exception: java.lang.Exception): ...

class StubNotFoundException(RemoteException):
    """
    Java class 'java.rmi.StubNotFoundException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * StubNotFoundException(java.lang.String)
        * StubNotFoundException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class UnexpectedException(RemoteException):
    """
    Java class 'java.rmi.UnexpectedException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * UnexpectedException(java.lang.String)
        * UnexpectedException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class UnknownHostException(RemoteException):
    """
    Java class 'java.rmi.UnknownHostException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * UnknownHostException(java.lang.String)
        * UnknownHostException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class UnmarshalException(RemoteException):
    """
    Java class 'java.rmi.UnmarshalException'
    
        Extends:
            java.rmi.RemoteException
    
      Constructors:
        * UnmarshalException(java.lang.String)
        * UnmarshalException(java.lang.String, java.lang.Exception)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.rmi")``.

    AccessException: typing.Type[AccessException]
    AlreadyBoundException: typing.Type[AlreadyBoundException]
    ConnectException: typing.Type[ConnectException]
    ConnectIOException: typing.Type[ConnectIOException]
    MarshalException: typing.Type[MarshalException]
    MarshalledObject: typing.Type[MarshalledObject]
    Naming: typing.Type[Naming]
    NoSuchObjectException: typing.Type[NoSuchObjectException]
    NotBoundException: typing.Type[NotBoundException]
    RMISecurityException: typing.Type[RMISecurityException]
    RMISecurityManager: typing.Type[RMISecurityManager]
    Remote: typing.Type[Remote]
    RemoteException: typing.Type[RemoteException]
    ServerError: typing.Type[ServerError]
    ServerException: typing.Type[ServerException]
    ServerRuntimeException: typing.Type[ServerRuntimeException]
    StubNotFoundException: typing.Type[StubNotFoundException]
    UnexpectedException: typing.Type[UnexpectedException]
    UnknownHostException: typing.Type[UnknownHostException]
    UnmarshalException: typing.Type[UnmarshalException]
    activation: java.rmi.activation.__module_protocol__
    dgc: java.rmi.dgc.__module_protocol__
    registry: java.rmi.registry.__module_protocol__
    server: java.rmi.server.__module_protocol__
