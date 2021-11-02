import typing



class SpsConstants:
    """
    public class SpsConstants extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Constants for SPS.
    """
    SPS_BENDING_RADIUS: typing.ClassVar[float] = ...
    """
    public static final double SPS_BENDING_RADIUS
    
        The magnetic bending radius for the SPS in meters
    
        Also see:
            :meth:`~constant`
    
    
    """
    SPS_MACHINE_RADIUS: typing.ClassVar[float] = ...
    """
    public static final double SPS_MACHINE_RADIUS
    
        The physical bending radius for the SPS in meters
    
        Also see:
            :meth:`~constant`
    
    
    """
    SPS_MACHINE_CIRCUMFERENCE: typing.ClassVar[float] = ...
    """
    public static final double SPS_MACHINE_CIRCUMFERENCE
    
        The circumference of SPS in meters
    
        Also see:
            :meth:`~constant`
    
    
    """
    SPS_GAMMA_TRANSITION: typing.ClassVar[float] = ...
    """
    public static final double SPS_GAMMA_TRANSITION
    
        Gamma transition for SPS Proton
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.constants.sps")``.

    SpsConstants: typing.Type[SpsConstants]
