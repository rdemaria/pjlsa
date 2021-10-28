import java.io
import java.rmi
import java.rmi.server
import typing



class DGC(java.rmi.Remote):
    """
    Java class 'java.rmi.dgc.DGC'
    
        Interfaces:
            java.rmi.Remote
    
    """
    def clean(self, objIDArray: typing.List[java.rmi.server.ObjID], long: int, vMID: 'VMID', boolean: bool) -> None: ...
    def dirty(self, objIDArray: typing.List[java.rmi.server.ObjID], long: int, lease: 'Lease') -> 'Lease': ...

class Lease(java.io.Serializable):
    """
    Java class 'java.rmi.dgc.Lease'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * Lease(java.rmi.dgc.VMID, long)
    
    """
    def __init__(self, vMID: 'VMID', long: int): ...
    def getVMID(self) -> 'VMID': ...
    def getValue(self) -> int: ...

class VMID(java.io.Serializable):
    """
    Java class 'java.rmi.dgc.VMID'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * VMID()
    
    """
    def __init__(self): ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def isUnique() -> bool: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.rmi.dgc")``.

    DGC: typing.Type[DGC]
    Lease: typing.Type[Lease]
    VMID: typing.Type[VMID]
