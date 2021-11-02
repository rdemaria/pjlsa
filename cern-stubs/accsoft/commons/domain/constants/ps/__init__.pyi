import typing



class PsConstants:
    """
    public class PsConstants extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Constants for PS.
    """
    PS_BENDING_RADIUS: typing.ClassVar[float] = ...
    """
    public static final double PS_BENDING_RADIUS
    
        The magnetic bending radius for the PS in meters
    
        Also see:
            :meth:`~constant`
    
    
    """
    PS_MACHINE_RADIUS: typing.ClassVar[float] = ...
    """
    public static final double PS_MACHINE_RADIUS
    
        The physical bending radius for the PS in meters
    
        Also see:
            :meth:`~constant`
    
    
    """
    PS_MACHINE_CIRCUMNFERENCE: typing.ClassVar[float] = ...
    """
    public static final double PS_MACHINE_CIRCUMNFERENCE
    
        The circumference of PS in meters
    
        Also see:
            :meth:`~constant`
    
    
    """
    PS_GAMMA_TRANSITION: typing.ClassVar[float] = ...
    """
    public static final double PS_GAMMA_TRANSITION
    
        Gamma transition for PS Proton
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.constants.ps")``.

    PsConstants: typing.Type[PsConstants]
