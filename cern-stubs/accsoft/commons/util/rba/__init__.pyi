import java.io
import typing



class RbaReflectiveInvoker:
    """
    public class RbaReflectiveInvoker extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A helper class that uses reflection to call RBAC methods without having compile-time dependencies on the RBAC jars.
    """
    def __init__(self): ...
    def clearMiddleTierRbaToken(self) -> None:
        """
            Reflective invocation of :code:`MiddleTierRBATokenHolder.clear();`. Clears the token if RBA libraries can be found, else
            does nothing.
        
        """
        ...
    def findRbaToken(self) -> java.io.Serializable:
        """
            If the class RbaTokenLookup can be found, invokes the RbaTokenLookup.findRbaToken() method and returns the result as a
            serializable, else returns :code:`null`
        
            Returns:
                the RbaToken object or :code:`null`
        
        
        """
        ...
    def getHostName(self) -> str:
        """
            Reflective invocation of :code:`RbaUtils.getHostName()`
        
            Returns:
                the host name or :code:`null` if RBAC code is not there or cannot be invoked
        
        
        """
        ...
    def getUserName(self) -> str:
        """
            Reflective invocation of :code:`RbaUtils.getUserName()`
        
            Returns:
                the user name or :code:`null` if RBAC code is not there or cannot be invoked
        
        
        """
        ...
    def setMiddleTierRbaToken(self, serializable: java.io.Serializable) -> None:
        """
            Reflective invocation of :code:`MiddleTierRBATokenHolder.set(token);`. Sets the token if RBA libraries can be found,
            else does nothing. If RBAC token from client is :code:`null` then empty token is set.
        
            Parameters:
                token (`Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`): 
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.rba")``.

    RbaReflectiveInvoker: typing.Type[RbaReflectiveInvoker]
