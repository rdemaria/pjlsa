import java.io
import typing



class RbaReflectiveInvoker:
    """
    Java class 'cern.accsoft.commons.util.rba.RbaReflectiveInvoker'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RbaReflectiveInvoker()
    
    """
    def __init__(self): ...
    def clearMiddleTierRbaToken(self) -> None: ...
    def findRbaToken(self) -> java.io.Serializable: ...
    def getHostName(self) -> str: ...
    def getUserName(self) -> str: ...
    def setMiddleTierRbaToken(self, serializable: java.io.Serializable) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.rba")``.

    RbaReflectiveInvoker: typing.Type[RbaReflectiveInvoker]
