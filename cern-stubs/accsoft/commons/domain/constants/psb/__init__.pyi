import typing



class PsbConstants:
    """
    Java class 'cern.accsoft.commons.domain.constants.psb.PsbConstants'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PsbConstants()
    
      Attributes:
        PSB_BENDING_RADIUS (double): final static field
        PSB_MACHINE_RADIUS (double): final static field
        PSB_MACHINE_CIRCUMFERENCE (double): final static field
        PSB_GAMMA_TRANSITION (double): final static field
    
    """
    PSB_BENDING_RADIUS: typing.ClassVar[float] = ...
    PSB_MACHINE_RADIUS: typing.ClassVar[float] = ...
    PSB_MACHINE_CIRCUMFERENCE: typing.ClassVar[float] = ...
    PSB_GAMMA_TRANSITION: typing.ClassVar[float] = ...
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.constants.psb")``.

    PsbConstants: typing.Type[PsbConstants]
