import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.modes
import cern.accsoft.commons.domain.util
import typing


class LhcAcceleratorModeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.modes.LhcAcceleratorMode]):
    LHC_ACCELERATOR_MODE_CONVERTER: typing.ClassVar['LhcAcceleratorModeConverter'] = ...

class LhcBeamModeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.modes.LhcBeamMode]):
    LHC_BEAM_MODE_CONVERTER: typing.ClassVar['LhcBeamModeConverter'] = ...

class LhcParticleTypeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.ParticleType]):
    LHC_PARTICLE_TYPE_CONVERTER: typing.ClassVar['LhcParticleTypeConverter'] = ...
