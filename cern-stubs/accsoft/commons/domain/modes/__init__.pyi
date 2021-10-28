import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import java.util
import typing



class AcceleratorMode(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.accsoft.commons.domain.modes.AcceleratorMode'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def isOperational(self) -> bool: ...

class BeamMode(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.accsoft.commons.domain.modes.BeamMode'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...

class LeirAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LeirAcceleratorMode'], AcceleratorMode):
    """
    Java class 'cern.accsoft.commons.domain.modes.LeirAcceleratorMode'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.modes.AcceleratorMode
    
      Attributes:
        ACCESS (cern.accsoft.commons.domain.modes.LeirAcceleratorMode): final static field
        BEAM_SETUP (cern.accsoft.commons.domain.modes.LeirAcceleratorMode): final static field
        ION_PHYSICS (cern.accsoft.commons.domain.modes.LeirAcceleratorMode): final static field
        MACHINE_DEVELOPMENT (cern.accsoft.commons.domain.modes.LeirAcceleratorMode): final static field
        SHUTDOWN (cern.accsoft.commons.domain.modes.LeirAcceleratorMode): final static field
    
    """
    ACCESS: typing.ClassVar['LeirAcceleratorMode'] = ...
    BEAM_SETUP: typing.ClassVar['LeirAcceleratorMode'] = ...
    ION_PHYSICS: typing.ClassVar['LeirAcceleratorMode'] = ...
    MACHINE_DEVELOPMENT: typing.ClassVar['LeirAcceleratorMode'] = ...
    SHUTDOWN: typing.ClassVar['LeirAcceleratorMode'] = ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def isOperational(self) -> bool: ...
    @staticmethod
    def valueOf(string: str) -> 'LeirAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['LeirAcceleratorMode']: ...

class LhcAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LhcAcceleratorMode'], AcceleratorMode):
    """
    Java class 'cern.accsoft.commons.domain.modes.LhcAcceleratorMode'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.modes.AcceleratorMode
    
      Attributes:
        ACCESS (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
        BEAM_SETUP (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
        ION_PHYSICS (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
        MACHINE_CHECKOUT (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
        MACHINE_DEVELOPMENT (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
        MACHINE_TEST (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
        NO_MODE (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
        PROTON_PHYSICS (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
        PROTON_NUCLEUS_PHYSICS (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
        SHUTDOWN (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
        SPECIAL_OPTICS_PHYSICS (cern.accsoft.commons.domain.modes.LhcAcceleratorMode): final static field
    
    """
    ACCESS: typing.ClassVar['LhcAcceleratorMode'] = ...
    BEAM_SETUP: typing.ClassVar['LhcAcceleratorMode'] = ...
    ION_PHYSICS: typing.ClassVar['LhcAcceleratorMode'] = ...
    MACHINE_CHECKOUT: typing.ClassVar['LhcAcceleratorMode'] = ...
    MACHINE_DEVELOPMENT: typing.ClassVar['LhcAcceleratorMode'] = ...
    MACHINE_TEST: typing.ClassVar['LhcAcceleratorMode'] = ...
    NO_MODE: typing.ClassVar['LhcAcceleratorMode'] = ...
    PROTON_PHYSICS: typing.ClassVar['LhcAcceleratorMode'] = ...
    PROTON_NUCLEUS_PHYSICS: typing.ClassVar['LhcAcceleratorMode'] = ...
    SHUTDOWN: typing.ClassVar['LhcAcceleratorMode'] = ...
    SPECIAL_OPTICS_PHYSICS: typing.ClassVar['LhcAcceleratorMode'] = ...
    @staticmethod
    def findByName(string: str) -> 'LhcAcceleratorMode': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    @staticmethod
    def getLhcSectorModes() -> java.util.Set['LhcAcceleratorMode']: ...
    def isApplicableToSectors(self) -> bool: ...
    def isOperational(self) -> bool: ...
    @staticmethod
    def valueOf(string: str) -> 'LhcAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['LhcAcceleratorMode']: ...

class LhcBeamMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LhcBeamMode'], BeamMode):
    """
    Java class 'cern.accsoft.commons.domain.modes.LhcBeamMode'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.modes.BeamMode
    
      Attributes:
        NO_MODE (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        SETUP (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        INJECTION_PROBE_BEAM (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        INJECTION_SETUP_BEAM (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        INJECTION_PHYSICS_BEAM (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        PREPARE_RAMP (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        RAMP (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        FLAT_TOP (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        SQUEEZE (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        ADJUST (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        STABLE_BEAMS (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        BEAM_DUMP (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        RAMP_DOWN (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        RECOVERY (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        CYCLING (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
        NO_BEAM (cern.accsoft.commons.domain.modes.LhcBeamMode): final static field
    
    """
    NO_MODE: typing.ClassVar['LhcBeamMode'] = ...
    SETUP: typing.ClassVar['LhcBeamMode'] = ...
    INJECTION_PROBE_BEAM: typing.ClassVar['LhcBeamMode'] = ...
    INJECTION_SETUP_BEAM: typing.ClassVar['LhcBeamMode'] = ...
    INJECTION_PHYSICS_BEAM: typing.ClassVar['LhcBeamMode'] = ...
    PREPARE_RAMP: typing.ClassVar['LhcBeamMode'] = ...
    RAMP: typing.ClassVar['LhcBeamMode'] = ...
    FLAT_TOP: typing.ClassVar['LhcBeamMode'] = ...
    SQUEEZE: typing.ClassVar['LhcBeamMode'] = ...
    ADJUST: typing.ClassVar['LhcBeamMode'] = ...
    STABLE_BEAMS: typing.ClassVar['LhcBeamMode'] = ...
    BEAM_DUMP: typing.ClassVar['LhcBeamMode'] = ...
    RAMP_DOWN: typing.ClassVar['LhcBeamMode'] = ...
    RECOVERY: typing.ClassVar['LhcBeamMode'] = ...
    CYCLING: typing.ClassVar['LhcBeamMode'] = ...
    NO_BEAM: typing.ClassVar['LhcBeamMode'] = ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    @staticmethod
    def valueOf(string: str) -> 'LhcBeamMode': ...
    @staticmethod
    def values() -> typing.List['LhcBeamMode']: ...

class PsAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsAcceleratorMode'], AcceleratorMode):
    """
    Java class 'cern.accsoft.commons.domain.modes.PsAcceleratorMode'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.modes.AcceleratorMode
    
      Attributes:
        SHUTDOWN (cern.accsoft.commons.domain.modes.PsAcceleratorMode): final static field
    
    """
    SHUTDOWN: typing.ClassVar['PsAcceleratorMode'] = ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def isOperational(self) -> bool: ...
    @staticmethod
    def valueOf(string: str) -> 'PsAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['PsAcceleratorMode']: ...

class PsbAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsbAcceleratorMode'], AcceleratorMode):
    """
    Java class 'cern.accsoft.commons.domain.modes.PsbAcceleratorMode'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.modes.AcceleratorMode
    
      Attributes:
        SHUTDOWN (cern.accsoft.commons.domain.modes.PsbAcceleratorMode): final static field
    
    """
    SHUTDOWN: typing.ClassVar['PsbAcceleratorMode'] = ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def isOperational(self) -> bool: ...
    @staticmethod
    def valueOf(string: str) -> 'PsbAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['PsbAcceleratorMode']: ...

class SpsAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsAcceleratorMode'], AcceleratorMode):
    """
    Java class 'cern.accsoft.commons.domain.modes.SpsAcceleratorMode'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.modes.AcceleratorMode
    
      Attributes:
        BEAM_OPERATION (cern.accsoft.commons.domain.modes.SpsAcceleratorMode): final static field
        SHUTDOWN (cern.accsoft.commons.domain.modes.SpsAcceleratorMode): final static field
    
    """
    BEAM_OPERATION: typing.ClassVar['SpsAcceleratorMode'] = ...
    SHUTDOWN: typing.ClassVar['SpsAcceleratorMode'] = ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def isOperational(self) -> bool: ...
    @staticmethod
    def valueOf(string: str) -> 'SpsAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['SpsAcceleratorMode']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.modes")``.

    AcceleratorMode: typing.Type[AcceleratorMode]
    BeamMode: typing.Type[BeamMode]
    LeirAcceleratorMode: typing.Type[LeirAcceleratorMode]
    LhcAcceleratorMode: typing.Type[LhcAcceleratorMode]
    LhcBeamMode: typing.Type[LhcBeamMode]
    PsAcceleratorMode: typing.Type[PsAcceleratorMode]
    PsbAcceleratorMode: typing.Type[PsbAcceleratorMode]
    SpsAcceleratorMode: typing.Type[SpsAcceleratorMode]
