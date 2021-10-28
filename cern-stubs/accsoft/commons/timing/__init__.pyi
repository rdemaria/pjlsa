import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.modes
import cern.accsoft.commons.domain.util
import typing



class LhcAcceleratorModeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.modes.LhcAcceleratorMode]):
    """
    Java class 'cern.accsoft.commons.timing.LhcAcceleratorModeConverter'
    
        Extends:
            cern.accsoft.commons.domain.util.CodeEntityConverter
    
      Attributes:
        LHC_ACCELERATOR_MODE_CONVERTER (cern.accsoft.commons.timing.LhcAcceleratorModeConverter): final static field
    
    """
    LHC_ACCELERATOR_MODE_CONVERTER: typing.ClassVar['LhcAcceleratorModeConverter'] = ...

class LhcBeamModeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.modes.LhcBeamMode]):
    """
    Java class 'cern.accsoft.commons.timing.LhcBeamModeConverter'
    
        Extends:
            cern.accsoft.commons.domain.util.CodeEntityConverter
    
      Attributes:
        LHC_BEAM_MODE_CONVERTER (cern.accsoft.commons.timing.LhcBeamModeConverter): final static field
    
    """
    LHC_BEAM_MODE_CONVERTER: typing.ClassVar['LhcBeamModeConverter'] = ...

class LhcParticleTypeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.ParticleType]):
    """
    Java class 'cern.accsoft.commons.timing.LhcParticleTypeConverter'
    
        Extends:
            cern.accsoft.commons.domain.util.CodeEntityConverter
    
      Attributes:
        LHC_PARTICLE_TYPE_CONVERTER (cern.accsoft.commons.timing.LhcParticleTypeConverter): final static field
    
    """
    LHC_PARTICLE_TYPE_CONVERTER: typing.ClassVar['LhcParticleTypeConverter'] = ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.timing")``.

    LhcAcceleratorModeConverter: typing.Type[LhcAcceleratorModeConverter]
    LhcBeamModeConverter: typing.Type[LhcBeamModeConverter]
    LhcParticleTypeConverter: typing.Type[LhcParticleTypeConverter]
