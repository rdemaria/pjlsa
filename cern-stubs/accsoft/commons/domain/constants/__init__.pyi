import cern.accsoft.commons.domain.constants.lhc
import cern.accsoft.commons.domain.constants.ps
import cern.accsoft.commons.domain.constants.psb
import cern.accsoft.commons.domain.constants.sps
import typing



class GlobalConstants:
    """
    public class GlobalConstants extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Global world constants.
    """
    SPEED_OF_LIGHT: typing.ClassVar[float] = ...
    """
    public static final double SPEED_OF_LIGHT
    
        The speed of light in m/s.
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNIFIED_ATOMIC_MASS_UNIT: typing.ClassVar[float] = ...
    """
    public static final double UNIFIED_ATOMIC_MASS_UNIT
    
        Unified Atomic Mass Unit in MeV/c2
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.constants")``.

    GlobalConstants: typing.Type[GlobalConstants]
    lhc: cern.accsoft.commons.domain.constants.lhc.__module_protocol__
    ps: cern.accsoft.commons.domain.constants.ps.__module_protocol__
    psb: cern.accsoft.commons.domain.constants.psb.__module_protocol__
    sps: cern.accsoft.commons.domain.constants.sps.__module_protocol__
