import cern.accsoft.commons.domain.constants.lhc
import cern.accsoft.commons.domain.constants.ps
import cern.accsoft.commons.domain.constants.psb
import cern.accsoft.commons.domain.constants.sps
import typing



class GlobalConstants:
    """
    Java class 'cern.accsoft.commons.domain.constants.GlobalConstants'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * GlobalConstants()
    
      Attributes:
        SPEED_OF_LIGHT (double): final static field
        UNIFIED_ATOMIC_MASS_UNIT (double): final static field
    
    """
    SPEED_OF_LIGHT: typing.ClassVar[float] = ...
    UNIFIED_ATOMIC_MASS_UNIT: typing.ClassVar[float] = ...
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.constants")``.

    GlobalConstants: typing.Type[GlobalConstants]
    lhc: cern.accsoft.commons.domain.constants.lhc.__module_protocol__
    ps: cern.accsoft.commons.domain.constants.ps.__module_protocol__
    psb: cern.accsoft.commons.domain.constants.psb.__module_protocol__
    sps: cern.accsoft.commons.domain.constants.sps.__module_protocol__
