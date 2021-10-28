import typing



class LhcConstants:
    """
    Java class 'cern.accsoft.commons.domain.constants.lhc.LhcConstants'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * LhcConstants()
    
      Attributes:
        BENDING_RADIUS_LHC (double): final static field
        MACHINE_CIRCUMFERENCE_LHC (double): final static field
        MACHINE_RADIUS_LHC (double): final static field
        GAMMA_TRANSITION_LHC (double): final static field
    
    """
    BENDING_RADIUS_LHC: typing.ClassVar[float] = ...
    MACHINE_CIRCUMFERENCE_LHC: typing.ClassVar[float] = ...
    MACHINE_RADIUS_LHC: typing.ClassVar[float] = ...
    GAMMA_TRANSITION_LHC: typing.ClassVar[float] = ...
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.constants.lhc")``.

    LhcConstants: typing.Type[LhcConstants]
