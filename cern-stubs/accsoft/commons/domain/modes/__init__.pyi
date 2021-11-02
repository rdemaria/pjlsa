import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import java.util
import typing



class AcceleratorMode(cern.accsoft.commons.util.Named):
    """
    public interface AcceleratorMode extends cern.accsoft.commons.util.Named
    
        Accelerator mode.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                the accelerator this mode is for (never :code:`null`)
        
        
        """
        ...
    def isOperational(self) -> bool:
        """
            Specifies if the mode is operational. A mode is operational when is used during regular machine operations e.g. BEAM
            SETUP, MACHINE DEVELOPMENT. Whereas a non-operational mode typically doesn't involve beam operations e.g. SHUTDOWN,
            COOLDOWN.
        
            Returns:
                :code:`true` if the mode is operational, :code:`false` otherwise
        
        
        """
        ...

class BeamMode(cern.accsoft.commons.util.Named):
    """
    public interface BeamMode extends cern.accsoft.commons.util.Named
    
        Accelerator beam mode.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...

class LeirAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LeirAcceleratorMode'], AcceleratorMode):
    """
    public class LeirAcceleratorMode extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.modes.LeirAcceleratorMode`> implements :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
    
        LEIR accelerator modes.
    
        Also see:
            :meth:`~serialized`
    """
    ACCESS: typing.ClassVar['LeirAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LeirAcceleratorMode` ACCESS
    
        ACCESS mode
    
    """
    BEAM_SETUP: typing.ClassVar['LeirAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LeirAcceleratorMode` BEAM_SETUP
    
        BEAM SETUP mode
    
    """
    ION_PHYSICS: typing.ClassVar['LeirAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LeirAcceleratorMode` ION_PHYSICS
    
        ION PHYSICS mode
    
    """
    MACHINE_DEVELOPMENT: typing.ClassVar['LeirAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LeirAcceleratorMode` MACHINE_DEVELOPMENT
    
        MACHINE DEVELOPMENT mode
    
    """
    SHUTDOWN: typing.ClassVar['LeirAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LeirAcceleratorMode` SHUTDOWN
    
        SHUTDOWN mode
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
        
            Returns:
                the accelerator this mode is for (never :code:`null`)
        
        
        """
        ...
    def isOperational(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.isOperational`
            Specifies if the mode is operational. A mode is operational when is used during regular machine operations e.g. BEAM
            SETUP, MACHINE DEVELOPMENT. Whereas a non-operational mode typically doesn't involve beam operations e.g. SHUTDOWN,
            COOLDOWN.
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.isOperational`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
        
            Returns:
                :code:`true` if the mode is operational, :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'LeirAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['LeirAcceleratorMode']: ...

class LhcAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LhcAcceleratorMode'], AcceleratorMode):
    """
    public class LhcAcceleratorMode extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode`> implements :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
    
        LHC accelerator modes.
    
        Also see:
            :meth:`~serialized`
    """
    ACCESS: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` ACCESS
    
        ACCESS mode
    
    """
    BEAM_SETUP: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` BEAM_SETUP
    
        BEAM SETUP mode
    
    """
    ION_PHYSICS: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` ION_PHYSICS
    
        ION PHYSICS mode
    
    """
    MACHINE_CHECKOUT: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` MACHINE_CHECKOUT
    
        MACHINE CHECKOUT mode
    
    """
    MACHINE_DEVELOPMENT: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` MACHINE_DEVELOPMENT
    
        MACHINE DEVELOPMENT mode
    
    """
    MACHINE_TEST: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` MACHINE_TEST
    
        MACHINE TEST mode
    
    """
    NO_MODE: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` NO_MODE
    
        NOMODE mode
    
    """
    PROTON_PHYSICS: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` PROTON_PHYSICS
    
        PROTON PHYSICS mode
    
    """
    PROTON_NUCLEUS_PHYSICS: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` PROTON_NUCLEUS_PHYSICS
    
        PROTON NUCLEUS PHYSICS mode
    
    """
    SHUTDOWN: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` SHUTDOWN
    
        SHUTDOWN mode
    
    """
    SPECIAL_OPTICS_PHYSICS: typing.ClassVar['LhcAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcAcceleratorMode` SPECIAL_OPTICS_PHYSICS
    
        SPECIAL OPTICS PHYSICS mode
    
    """
    @staticmethod
    def findByName(string: str) -> 'LhcAcceleratorMode':
        """
        
            Parameters:
                lhcAcceleratorModeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the accelerator zone
        
            Returns:
                LHC accelerator mode
        
            Raises:
                : in case of unknown LHC accelerator mode name
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
        
            Returns:
                the accelerator this mode is for (never :code:`null`)
        
        
        """
        ...
    @staticmethod
    def getLhcSectorModes() -> java.util.Set['LhcAcceleratorMode']: ...
    def isApplicableToSectors(self) -> bool:
        """
        
            Returns:
                (@code true) if the mode is applicable to LHC sectors
        
        
        """
        ...
    def isOperational(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.isOperational`
            Specifies if the mode is operational. A mode is operational when is used during regular machine operations e.g. BEAM
            SETUP, MACHINE DEVELOPMENT. Whereas a non-operational mode typically doesn't involve beam operations e.g. SHUTDOWN,
            COOLDOWN.
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.isOperational`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
        
            Returns:
                :code:`true` if the mode is operational, :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'LhcAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['LhcAcceleratorMode']: ...

class LhcBeamMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LhcBeamMode'], BeamMode):
    """
    public class LhcBeamMode extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.modes.LhcBeamMode`> implements :class:`~cern.accsoft.commons.domain.modes.BeamMode`
    
        LHC beam modes.
    
        Also see:
            :meth:`~serialized`
    """
    NO_MODE: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` NO_MODE
    
        NO MODE mode
    
    """
    SETUP: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` SETUP
    
        SETUP mode
    
    """
    INJECTION_PROBE_BEAM: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` INJECTION_PROBE_BEAM
    
        INJECTION PROBE BEAM mode
    
    """
    INJECTION_SETUP_BEAM: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` INJECTION_SETUP_BEAM
    
        INJECTION SETUP BEAM mode
    
    """
    INJECTION_PHYSICS_BEAM: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` INJECTION_PHYSICS_BEAM
    
        INJECTION PHYSICS BEAM mode
    
    """
    PREPARE_RAMP: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` PREPARE_RAMP
    
        PREPARE RAMP mode
    
    """
    RAMP: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` RAMP
    
        RAMP mode
    
    """
    FLAT_TOP: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` FLAT_TOP
    
        FLAT TOP mode
    
    """
    SQUEEZE: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` SQUEEZE
    
        SQUEEZE mode
    
    """
    ADJUST: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` ADJUST
    
        ADJUST mode
    
    """
    STABLE_BEAMS: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` STABLE_BEAMS
    
        STABLE BEAMS mode
    
    """
    BEAM_DUMP: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` BEAM_DUMP
    
        BEAM DUMP mode
    
    """
    RAMP_DOWN: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` RAMP_DOWN
    
        RAMP DOWN mode
    
    """
    RECOVERY: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` RECOVERY
    
        RECOVERY mode
    
    """
    CYCLING: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` CYCLING
    
        CYCLING mode
    
    """
    NO_BEAM: typing.ClassVar['LhcBeamMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.LhcBeamMode` NO_BEAM
    
        NO BEAM mode
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.BeamMode.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.BeamMode`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'LhcBeamMode': ...
    @staticmethod
    def values() -> typing.List['LhcBeamMode']: ...

class PsAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsAcceleratorMode'], AcceleratorMode):
    """
    public class PsAcceleratorMode extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.modes.PsAcceleratorMode`> implements :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
    
        PS accelerator modes.
    
        Also see:
            :meth:`~serialized`
    """
    SHUTDOWN: typing.ClassVar['PsAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.PsAcceleratorMode` SHUTDOWN
    
        SHUTDOWN mode
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
        
            Returns:
                the accelerator this mode is for (never :code:`null`)
        
        
        """
        ...
    def isOperational(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.isOperational`
            Specifies if the mode is operational. A mode is operational when is used during regular machine operations e.g. BEAM
            SETUP, MACHINE DEVELOPMENT. Whereas a non-operational mode typically doesn't involve beam operations e.g. SHUTDOWN,
            COOLDOWN.
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.isOperational`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
        
            Returns:
                :code:`true` if the mode is operational, :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'PsAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['PsAcceleratorMode']: ...

class PsbAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsbAcceleratorMode'], AcceleratorMode):
    """
    public class PsbAcceleratorMode extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.modes.PsbAcceleratorMode`> implements :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
    
        PSB accelerator modes.
    
        Also see:
            :meth:`~serialized`
    """
    SHUTDOWN: typing.ClassVar['PsbAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.PsbAcceleratorMode` SHUTDOWN
    
        SHUTDOWN mode
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
        
            Returns:
                the accelerator this mode is for (never :code:`null`)
        
        
        """
        ...
    def isOperational(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.isOperational`
            Specifies if the mode is operational. A mode is operational when is used during regular machine operations e.g. BEAM
            SETUP, MACHINE DEVELOPMENT. Whereas a non-operational mode typically doesn't involve beam operations e.g. SHUTDOWN,
            COOLDOWN.
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.isOperational`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
        
            Returns:
                :code:`true` if the mode is operational, :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'PsbAcceleratorMode': ...
    @staticmethod
    def values() -> typing.List['PsbAcceleratorMode']: ...

class SpsAcceleratorMode(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsAcceleratorMode'], AcceleratorMode):
    """
    public class SpsAcceleratorMode extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.modes.SpsAcceleratorMode`> implements :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
    
        SPS accelerator modes.
    
        Also see:
            :meth:`~serialized`
    """
    BEAM_OPERATION: typing.ClassVar['SpsAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.SpsAcceleratorMode` BEAM_OPERATION
    
        BEAM-OPERATION mode
    
    """
    SHUTDOWN: typing.ClassVar['SpsAcceleratorMode'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.modes.SpsAcceleratorMode` SHUTDOWN
    
        SHUTDOWN mode
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
        
            Returns:
                the accelerator this mode is for (never :code:`null`)
        
        
        """
        ...
    def isOperational(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.isOperational`
            Specifies if the mode is operational. A mode is operational when is used during regular machine operations e.g. BEAM
            SETUP, MACHINE DEVELOPMENT. Whereas a non-operational mode typically doesn't involve beam operations e.g. SHUTDOWN,
            COOLDOWN.
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.modes.AcceleratorMode.isOperational`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.modes.AcceleratorMode`
        
            Returns:
                :code:`true` if the mode is operational, :code:`false` otherwise
        
        
        """
        ...
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
