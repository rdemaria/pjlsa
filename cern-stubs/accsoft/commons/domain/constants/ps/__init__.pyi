import typing



class PsConstants:
    """
    Java class 'cern.accsoft.commons.domain.constants.ps.PsConstants'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PsConstants()
    
      Attributes:
        PS_BENDING_RADIUS (double): final static field
        PS_MACHINE_RADIUS (double): final static field
        PS_MACHINE_CIRCUMNFERENCE (double): final static field
        PS_GAMMA_TRANSITION (double): final static field
    
    """
    PS_BENDING_RADIUS: typing.ClassVar[float] = ...
    PS_MACHINE_RADIUS: typing.ClassVar[float] = ...
    PS_MACHINE_CIRCUMNFERENCE: typing.ClassVar[float] = ...
    PS_GAMMA_TRANSITION: typing.ClassVar[float] = ...
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.constants.ps")``.

    PsConstants: typing.Type[PsConstants]
