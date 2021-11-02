import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.modes
import cern.accsoft.commons.domain.util
import typing



class LhcAcceleratorModeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.modes.LhcAcceleratorMode]):
    """
    public class LhcAcceleratorModeConverter extends :class:`~cern.accsoft.commons.domain.util.CodeEntityConverter`<:class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode`>
    
        Converter between :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` and corresponding timing codes.
    """
    LHC_ACCELERATOR_MODE_CONVERTER: typing.ClassVar['LhcAcceleratorModeConverter'] = ...
    """
    public static final :class:`~cern.accsoft.commons.timing.LhcAcceleratorModeConverter` LHC_ACCELERATOR_MODE_CONVERTER
    
        LHC Accelerator Mode converter singleton
    
    """

class LhcBeamModeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.modes.LhcBeamMode]):
    """
    public class LhcBeamModeConverter extends :class:`~cern.accsoft.commons.domain.util.CodeEntityConverter`<:class:`~cern.accsoft.commons.domain.modes.LhcBeamMode`>
    
        Converter between :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` and corresponding timing codes.
    """
    LHC_BEAM_MODE_CONVERTER: typing.ClassVar['LhcBeamModeConverter'] = ...
    """
    public static final :class:`~cern.accsoft.commons.timing.LhcBeamModeConverter` LHC_BEAM_MODE_CONVERTER
    
        LHC Beam Mode converter singleton
    
    """

class LhcParticleTypeConverter(cern.accsoft.commons.domain.util.CodeEntityConverter[cern.accsoft.commons.domain.ParticleType]):
    """
    public class LhcParticleTypeConverter extends :class:`~cern.accsoft.commons.domain.util.CodeEntityConverter`<:class:`~cern.accsoft.commons.domain.ParticleType`>
    
        Converter between :class:`~cern.accsoft.commons.domain.ParticleType` and corresponding timing codes.
    """
    LHC_PARTICLE_TYPE_CONVERTER: typing.ClassVar['LhcParticleTypeConverter'] = ...
    """
    public static final :class:`~cern.accsoft.commons.timing.LhcParticleTypeConverter` LHC_PARTICLE_TYPE_CONVERTER
    
        LHC Particle Type converter singleton
    
    """


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.timing")``.

    LhcAcceleratorModeConverter: typing.Type[LhcAcceleratorModeConverter]
    LhcBeamModeConverter: typing.Type[LhcBeamModeConverter]
    LhcParticleTypeConverter: typing.Type[LhcParticleTypeConverter]
