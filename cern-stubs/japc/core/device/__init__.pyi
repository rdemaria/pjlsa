import cern.accsoft.commons.util
import cern.japc.core
import cern.japc.core.device.impl
import cern.japc.core.transaction
import java.util
import typing



class JapcDevice(cern.accsoft.commons.util.Named):
    """
    public interface JapcDevice extends cern.accsoft.commons.util.Named
    
        JAPC device which is represented as a collection of parameters corresponding to its properties.
    """
    def getImmutableParameter(self, string: str) -> cern.japc.core.ImmutableParameter:
        """
        
            Parameters:
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                the parameter
        
            Raises:
                : if the parameter is not found in the device
        
        
        """
        ...
    def getParameter(self, string: str) -> cern.japc.core.Parameter:
        """
        
            Parameters:
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                the parameter
        
            Raises:
                : if the parameter is not found in the device or is not writable
        
        
        """
        ...
    def getPropertyNames(self) -> java.util.Set[str]: ...
    def getTransactionalParameter(self, string: str) -> cern.japc.core.transaction.TransactionalParameter:
        """
        
            Parameters:
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                the parameter
        
            Raises:
                : if the parameter is not found in the device or is not transactional
        
        
        """
        ...
    def getWritablePropertyNames(self) -> java.util.Set[str]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.device")``.

    JapcDevice: typing.Type[JapcDevice]
    impl: cern.japc.core.device.impl.__module_protocol__
