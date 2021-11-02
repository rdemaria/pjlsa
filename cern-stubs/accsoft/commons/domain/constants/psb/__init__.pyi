import typing



class PsbConstants:
    """
    public class PsbConstants extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Constants for PSB.
    """
    PSB_BENDING_RADIUS: typing.ClassVar[float] = ...
    """
    public static final double PSB_BENDING_RADIUS
    
        The magnetic bending radius for the PSB in meters
    
        Also see:
            :meth:`~constant`
    
    
    """
    PSB_MACHINE_RADIUS: typing.ClassVar[float] = ...
    """
    public static final double PSB_MACHINE_RADIUS
    
        The physical bending radius for the PSB in meters
    
        Also see:
            :meth:`~constant`
    
    
    """
    PSB_MACHINE_CIRCUMFERENCE: typing.ClassVar[float] = ...
    """
    public static final double PSB_MACHINE_CIRCUMFERENCE
    
        The circumference of PSB in meters
    
        Also see:
            :meth:`~constant`
    
    
    """
    PSB_GAMMA_TRANSITION: typing.ClassVar[float] = ...
    """
    public static final double PSB_GAMMA_TRANSITION
    
        Gamma transition for PSB Proton
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.constants.psb")``.

    PsbConstants: typing.Type[PsbConstants]
