import cern.accsoft.commons.util
import cern.japc.core
import cern.japc.core.device
import cern.japc.core.transaction
import java.util
import typing



class JapcDeviceImpl(cern.accsoft.commons.util.AbstractNamed[cern.japc.core.device.JapcDevice], cern.japc.core.device.JapcDevice):
    """
    public class JapcDeviceImpl extends cern.accsoft.commons.util.AbstractNamed<:class:`~cern.japc.core.device.JapcDevice`> implements :class:`~cern.japc.core.device.JapcDevice`
    
        Default implementation of :class:`~cern.japc.core.device.JapcDevice`.
    """
    def __init__(self, string: str): ...
    def addParameter(self, immutableParameter: cern.japc.core.ImmutableParameter) -> None:
        """
            Adds a parameter to this device.
        
            The device name of the parameter must correspond to the name of this device.
        
            For thread safety reasons, this method shall be called only in the beginning, when the
            :class:`~cern.japc.core.device.impl.JapcDeviceImpl` is being instantiated, and before other methods of this class are
            used
        
            Parameters:
                parameter (:class:`~cern.japc.core.ImmutableParameter`): parameter to be added (non-null)
        
            Raises:
                : if the parameter is :code:`null` or if the parameter's device name is not the same as the device name
        
        
        """
        ...
    def getImmutableParameter(self, string: str) -> cern.japc.core.ImmutableParameter:
        """
        
            Specified by:
                :meth:`~cern.japc.core.device.JapcDevice.getImmutableParameter` in interface :class:`~cern.japc.core.device.JapcDevice`
        
            Returns:
                the parameter
        
        
        """
        ...
    def getParameter(self, string: str) -> cern.japc.core.Parameter:
        """
        
            Specified by:
                :meth:`~cern.japc.core.device.JapcDevice.getParameter` in interface :class:`~cern.japc.core.device.JapcDevice`
        
            Returns:
                the parameter
        
        
        """
        ...
    def getPropertyNames(self) -> java.util.Set[str]: ...
    def getTransactionalParameter(self, string: str) -> cern.japc.core.transaction.TransactionalParameter:
        """
        
            Specified by:
                :meth:`~cern.japc.core.device.JapcDevice.getTransactionalParameter`Â in
                interfaceÂ :class:`~cern.japc.core.device.JapcDevice`
        
            Returns:
                the parameter
        
        
        """
        ...
    def getWritablePropertyNames(self) -> java.util.Set[str]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.device.impl")``.

    JapcDeviceImpl: typing.Type[JapcDeviceImpl]
