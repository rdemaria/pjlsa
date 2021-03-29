import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import java.util
import typing


class AcceleratorMode(cern.accsoft.commons.util.Named):
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def isOperational(self) -> bool: ...

class BeamMode(cern.accsoft.commons.util.Named):
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...

class LeirAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LeirAcceleratorMode'], AcceleratorMode):
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
    PO_PHASE_1: typing.ClassVar['LhcAcceleratorMode'] = ...
    PO_PHASE_2: typing.ClassVar['LhcAcceleratorMode'] = ...
    CSCM_TEST: typing.ClassVar['LhcAcceleratorMode'] = ...
    COLD: typing.ClassVar['LhcAcceleratorMode'] = ...
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
    SHUTDOWN: typing.ClassVar['PsAcceleratorMode'] = ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def isOperational(self) -> bool: ...
    @staticmethod
    def valueOf(string: str) -> 'PsAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['PsAcceleratorMode']: ...

class PsbAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsbAcceleratorMode'], AcceleratorMode):
    SHUTDOWN: typing.ClassVar['PsbAcceleratorMode'] = ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def isOperational(self) -> bool: ...
    @staticmethod
    def valueOf(string: str) -> 'PsbAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['PsbAcceleratorMode']: ...

class SpsAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsAcceleratorMode'], AcceleratorMode):
    BEAM_OPERATION: typing.ClassVar['SpsAcceleratorMode'] = ...
    SHUTDOWN: typing.ClassVar['SpsAcceleratorMode'] = ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def isOperational(self) -> bool: ...
    @staticmethod
    def valueOf(string: str) -> 'SpsAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['SpsAcceleratorMode']: ...
