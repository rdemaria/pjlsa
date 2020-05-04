from typing import ClassVar as _py_ClassVar
import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.modes
import cern.accsoft.commons.domain.util


class LhcAcceleratorModeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.modes.LhcAcceleratorMode]):
    LHC_ACCELERATOR_MODE_CONVERTER: _py_ClassVar['LhcAcceleratorModeConverter'] = ...

class LhcBeamModeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.modes.LhcBeamMode]):
    LHC_BEAM_MODE_CONVERTER: _py_ClassVar['LhcBeamModeConverter'] = ...

class LhcParticleTypeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.ParticleType]):
    LHC_PARTICLE_TYPE_CONVERTER: _py_ClassVar['LhcParticleTypeConverter'] = ...
