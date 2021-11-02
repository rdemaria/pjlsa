import typing



class LhcConstants:
    """
    public class LhcConstants extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Constants for LHC.
    """
    BENDING_RADIUS_LHC: typing.ClassVar[float] = ...
    """
    public static final double BENDING_RADIUS_LHC
    
        The magnetic bending radius for the LHC in meters.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MACHINE_CIRCUMFERENCE_LHC: typing.ClassVar[float] = ...
    """
    public static final double MACHINE_CIRCUMFERENCE_LHC
    
        The LHC circumference in meters.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MACHINE_RADIUS_LHC: typing.ClassVar[float] = ...
    """
    public static final double MACHINE_RADIUS_LHC
    
        The LHC radius in meters
    
        Also see:
            :meth:`~constant`
    
    
    """
    GAMMA_TRANSITION_LHC: typing.ClassVar[float] = ...
    """
    public static final double GAMMA_TRANSITION_LHC
    
        Gamma transition for LHC Proton
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.constants.lhc")``.

    LhcConstants: typing.Type[LhcConstants]
