import cern.accsoft.commons.domain.beamdestinations
import cern.accsoft.commons.domain.beams
import cern.accsoft.commons.domain.constants
import cern.accsoft.commons.domain.devicepropertymodel
import cern.accsoft.commons.domain.helper
import cern.accsoft.commons.domain.lhc
import cern.accsoft.commons.domain.modes
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.util
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.util
import java.util
import typing



class Accelerator(cern.accsoft.commons.util.Named):
    """
    public interface Accelerator extends cern.accsoft.commons.util.Named
    
        Accelerator.
    """
    def getAcceleratorModes(self) -> java.util.Set[cern.accsoft.commons.domain.modes.AcceleratorMode]: ...
    def getAcceleratorZones(self) -> java.util.Set[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getBeamDestinations(self) -> java.util.Set[cern.accsoft.commons.domain.beamdestinations.BeamDestination]: ...
    def getBeams(self) -> java.util.Set[cern.accsoft.commons.domain.beams.Beam]: ...
    def getCode(self) -> str: ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getTimingDomain(self) -> 'TimingDomain':
        """
        
            Returns:
                timing domain for this accelerator (never :code:`null`)
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Returns :code:`true` if the accelerator/facility is controlled in a multiplexed way, meaning that devices can have
            different settings for different timing users at the same time, ex. in PSB or SPS. On the other hand, ISOLDE, ADE and
            CTF are controlled in a non-multiplexed way, meaning that devices have single setting at a time. LHC is non-multiplexed
            machine at FE level.
        
            Returns:
                :code:`true` if the accelerator is controlled in a multiplexed way and :code:`false` otherwise
        
        
        """
        ...

class ParticleType(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['ParticleType']):
    """
    public class ParticleType extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.ParticleType`>
    
        Particle types.
    
        Also see:
            :meth:`~serialized`
    """
    ELECTRON: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` ELECTRON
    
        Electrons
    
    """
    PROTON: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` PROTON
    
        Protons
    
    """
    PBAR: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` PBAR
    
        Antiprotons
    
    """
    MUON: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` MUON
    
        Muons
    
    """
    PION_PLUS: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` PION_PLUS
    
        Pion+
    
    """
    PION_MINUS: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` PION_MINUS
    
        Pion-
    
    """
    KAON: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` KAON
    
        Kaon
    
    """
    PB54: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` PB54
    
        Lead 54+ ions
    
    """
    PB80: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` PB80
    
        Lead 80+ ions
    
    """
    PB81: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` PB81
    
        Lead 81+ ions
    
    """
    PB82: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` PB82
    
        Lead 82+ ions
    
    """
    XE39: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` XE39
    
        Xenon 39+ ions
    
    """
    XE54: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` XE54
    
        Xenon 54+ ions
    
    """
    AR11: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` AR11
    
        Argon 11+ ions
    
    """
    AR18: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` AR18
    
        Argon 18+ ions
    
    """
    HMINUS: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` HMINUS
    
        H-
    
    """
    O4: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` O4
    
        04
    
    """
    O8: typing.ClassVar['ParticleType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.ParticleType` O8
    
        08
    
    """
    def getNumberOfCharges(self) -> int:
        """
        
            Returns:
                the number of charges of the particle
        
        
        """
        ...
    def getRestMassEV(self) -> float:
        """
        
            Returns:
                the rest mass of the particle in eV/c^2
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'ParticleType': ...
    @staticmethod
    def values() -> typing.List['ParticleType']: ...

class TimingDomain(cern.accsoft.commons.util.Named):
    """
    public interface TimingDomain extends cern.accsoft.commons.util.Named
    
        Timing domain for accelerators.
    """
    def isCycling(self) -> bool:
        """
        
            Returns:
                :code:`true` if this timing domain is for cycling accelerators and facilities
        
        
        """
        ...
    def isMultiplexed(self) -> bool: ...

class CernAccelerator(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['CernAccelerator'], Accelerator):
    """
    public class CernAccelerator extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.CernAccelerator`> implements :class:`~cern.accsoft.commons.domain.Accelerator`
    
        CERN accelerators.
    
        Also see:
            :meth:`~serialized`
    """
    AD: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` AD
    
        AD
    
    """
    CTF: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` CTF
    
        CTF
    
    """
    ISOLDE: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` ISOLDE
    
        ISOLDE
    
    """
    LEIR: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` LEIR
    
        LEIR
    
    """
    LHC: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` LHC
    
        LHC
    
    """
    PS: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` PS
    
        PS
    
    """
    PSB: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` PSB
    
        PS Booster
    
    """
    SPS: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` SPS
    
        SPS
    
    """
    NORTH: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` NORTH
    
        North Experimental Area
    
    """
    PS_EAST: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` PS_EAST
    
        PS East Experimental Area
    
    """
    AWAKE: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` AWAKE
    
        AWAKE
    
    """
    ELENA: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` ELENA
    
        ELENA
    
    """
    LINAC3: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` LINAC3
    
        LINAC3
    
    """
    LINAC4: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` LINAC4
    
        LINAC4
    
    """
    REX: typing.ClassVar['CernAccelerator'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernAccelerator` REX
    
        REX
    
    """
    @staticmethod
    def byCcsName(string: str) -> 'CernAccelerator':
        """
        
            Parameters:
                ccsName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the CCS name of the accelerator
        
            Returns:
                accelerator by CCS name
        
        
        """
        ...
    @staticmethod
    def byCode(string: str) -> 'CernAccelerator': ...
    @staticmethod
    def fromNameOrCode(string: str) -> 'CernAccelerator': ...
    def getAcceleratorModes(self) -> java.util.Set[cern.accsoft.commons.domain.modes.AcceleratorMode]: ...
    def getAcceleratorZones(self) -> java.util.Set[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getBeamDestinations(self) -> java.util.Set[cern.accsoft.commons.domain.beamdestinations.BeamDestination]: ...
    def getBeams(self) -> java.util.Set[cern.accsoft.commons.domain.beams.Beam]: ...
    def getCcsName(self) -> str:
        """
        
            Returns:
                CCS name of this accelerator
        
        
        """
        ...
    def getCode(self) -> str: ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getTimingDomain(self) -> TimingDomain:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.Accelerator.getTimingDomain`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.Accelerator`
        
            Returns:
                timing domain for this accelerator (never :code:`null`)
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.domain.Accelerator.isMultiplexed`
            Returns :code:`true` if the accelerator/facility is controlled in a multiplexed way, meaning that devices can have
            different settings for different timing users at the same time, ex. in PSB or SPS. On the other hand, ISOLDE, ADE and
            CTF are controlled in a non-multiplexed way, meaning that devices have single setting at a time. LHC is non-multiplexed
            machine at FE level.
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.Accelerator.isMultiplexed`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.Accelerator`
        
            Returns:
                :code:`true` if the accelerator is controlled in a multiplexed way and :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'CernAccelerator': ...
    @staticmethod
    def values() -> typing.List['CernAccelerator']: ...

class CernTimingDomain(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['CernTimingDomain'], TimingDomain):
    """
    public class CernTimingDomain extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.CernTimingDomain`> implements :class:`~cern.accsoft.commons.domain.TimingDomain`
    
        Timing domain for CERN accelerators.
    
        Also see:
            :meth:`~serialized`
    """
    LHC: typing.ClassVar['CernTimingDomain'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernTimingDomain` LHC
    
        LHC timing domain
    
    """
    SPS: typing.ClassVar['CernTimingDomain'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernTimingDomain` SPS
    
        SPS timing domain
    
    """
    CPS: typing.ClassVar['CernTimingDomain'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernTimingDomain` CPS
    
        PS timing domain
    
    """
    PSB: typing.ClassVar['CernTimingDomain'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernTimingDomain` PSB
    
        PS Booster timing domain
    
    """
    LEI: typing.ClassVar['CernTimingDomain'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernTimingDomain` LEI
    
        LEIR timing domain
    
    """
    ADE: typing.ClassVar['CernTimingDomain'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernTimingDomain` ADE
    
        AD timing domain
    
    """
    SCT: typing.ClassVar['CernTimingDomain'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernTimingDomain` SCT
    
        CTF Slow Central Timing timing domain
    
    """
    LNA: typing.ClassVar['CernTimingDomain'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.CernTimingDomain` LNA
    
        ELENA timing domain
    
    """
    def isCycling(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.TimingDomain.isCycling`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.TimingDomain`
        
            Returns:
                :code:`true` if this timing domain is for cycling accelerators and facilities
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'CernTimingDomain': ...
    @staticmethod
    def values() -> typing.List['CernTimingDomain']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain")``.

    Accelerator: typing.Type[Accelerator]
    CernAccelerator: typing.Type[CernAccelerator]
    CernTimingDomain: typing.Type[CernTimingDomain]
    ParticleType: typing.Type[ParticleType]
    TimingDomain: typing.Type[TimingDomain]
    beamdestinations: cern.accsoft.commons.domain.beamdestinations.__module_protocol__
    beams: cern.accsoft.commons.domain.beams.__module_protocol__
    constants: cern.accsoft.commons.domain.constants.__module_protocol__
    devicepropertymodel: cern.accsoft.commons.domain.devicepropertymodel.__module_protocol__
    helper: cern.accsoft.commons.domain.helper.__module_protocol__
    lhc: cern.accsoft.commons.domain.lhc.__module_protocol__
    modes: cern.accsoft.commons.domain.modes.__module_protocol__
    particletransfers: cern.accsoft.commons.domain.particletransfers.__module_protocol__
    util: cern.accsoft.commons.domain.util.__module_protocol__
    zones: cern.accsoft.commons.domain.zones.__module_protocol__
