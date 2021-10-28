import typing



class SpsConstants:
    """
    Java class 'cern.accsoft.commons.domain.constants.sps.SpsConstants'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SpsConstants()
    
      Attributes:
        SPS_BENDING_RADIUS (double): final static field
        SPS_MACHINE_RADIUS (double): final static field
        SPS_MACHINE_CIRCUMFERENCE (double): final static field
        SPS_GAMMA_TRANSITION (double): final static field
    
    """
    SPS_BENDING_RADIUS: typing.ClassVar[float] = ...
    SPS_MACHINE_RADIUS: typing.ClassVar[float] = ...
    SPS_MACHINE_CIRCUMFERENCE: typing.ClassVar[float] = ...
    SPS_GAMMA_TRANSITION: typing.ClassVar[float] = ...
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.constants.sps")``.

    SpsConstants: typing.Type[SpsConstants]
