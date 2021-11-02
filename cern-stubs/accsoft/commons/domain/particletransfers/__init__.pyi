import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.util
import java.util
import typing



class ParticleTransfer(cern.accsoft.commons.util.Named):
    """
    public interface ParticleTransfer extends cern.accsoft.commons.util.Named
    
        Particle transfers.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> 'ParticleTransferType':
        """
        
            Returns:
                the type of particle transfer
        
        
        """
        ...

class ParticleTransferType(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['ParticleTransferType']):
    """
    public class ParticleTransferType extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransferType`>
    
        Type of particle transfer. Used to e.g. distinguish the handling of rings and tranfer lines.
    
        Also see:
            :meth:`~serialized`
    """
    RING: typing.ClassVar['ParticleTransferType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransferType` RING
    
        Ring
    
    """
    TRANSFER: typing.ClassVar['ParticleTransferType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransferType` TRANSFER
    
        Transfer line
    
    """
    SOURCE: typing.ClassVar['ParticleTransferType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransferType` SOURCE
    
        Ion Source
    
    """
    EXPERIMENT: typing.ClassVar['ParticleTransferType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransferType` EXPERIMENT
    
        Experiment
    
    """
    COOLER: typing.ClassVar['ParticleTransferType'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransferType` COOLER
    
        Cooler
    
    """
    @staticmethod
    def valueOf(string: str) -> 'ParticleTransferType': ...
    @staticmethod
    def values() -> typing.List['ParticleTransferType']: ...

class AdParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['AdParticleTransfer'], ParticleTransfer):
    """
    public class AdParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.AdParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        AD particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    ADRING: typing.ClassVar['AdParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.AdParticleTransfer` ADRING
    
        AD ring
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'AdParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['AdParticleTransfer']: ...

class AwakeParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['AwakeParticleTransfer'], ParticleTransfer):
    """
    public class AwakeParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.AwakeParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        AWAKE particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    AWAKE: typing.ClassVar['AwakeParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.AwakeParticleTransfer` AWAKE
    
        AWAKE Experiment
    
    """
    AWAKEElectronTransfer: typing.ClassVar['AwakeParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.AwakeParticleTransfer` AWAKEElectronTransfer
    
        AWAKETransfer
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'AwakeParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['AwakeParticleTransfer']: ...

class CtfParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['CtfParticleTransfer'], ParticleTransfer):
    """
    public class CtfParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.CtfParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        CTF particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    CTF: typing.ClassVar['CtfParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.CtfParticleTransfer` CTF
    
        CTF
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'CtfParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['CtfParticleTransfer']: ...

class ElenaParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['ElenaParticleTransfer'], ParticleTransfer):
    """
    public class ElenaParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        ELENA particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    ELENA: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` ELENA
    
        ELENA
    
    """
    ElenaLNE00Extraction: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` ElenaLNE00Extraction
    
        ElenaLNE00Extraction
    
    """
    LNE01Transfer: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` LNE01Transfer
    
        LNE01Transfer
    
    """
    LNE02Transfer: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` LNE02Transfer
    
        LNE02Transfer
    
    """
    LNE03Transfer: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` LNE03Transfer
    
        LNE03Transfer
    
    """
    LNE04Transfer: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` LNE04Transfer
    
        LNE04Transfer
    
    """
    LNE05Transfer: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` LNE05Transfer
    
        LNE05Transfer
    
    """
    LNE06Transfer: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` LNE06Transfer
    
        LNE06Transfer
    
    """
    LNE07Transfer: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` LNE07Transfer
    
        LNE07Transfer
    
    """
    LNE50Transfer: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` LNE50Transfer
    
        LNE50Transfer
    
    """
    LNE51Transfer: typing.ClassVar['ElenaParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.ElenaParticleTransfer` LNE51Transfer
    
        LNE51Transfer
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'ElenaParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['ElenaParticleTransfer']: ...

class IsoldeParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['IsoldeParticleTransfer'], ParticleTransfer):
    """
    public class IsoldeParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.IsoldeParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        ISOLDE particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    ISOLDE: typing.ClassVar['IsoldeParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.IsoldeParticleTransfer` ISOLDE
    
        ISOLDE
    
    """
    HIE: typing.ClassVar['IsoldeParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.IsoldeParticleTransfer` HIE
    
        HIE
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'IsoldeParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['IsoldeParticleTransfer']: ...

class LeirParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LeirParticleTransfer'], ParticleTransfer):
    """
    public class LeirParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.LeirParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        LEIR particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    LEIRRING: typing.ClassVar['LeirParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.LeirParticleTransfer` LEIRRING
    
        LEIRRING
    
    """
    LINAC3: typing.ClassVar['LeirParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.LeirParticleTransfer` LINAC3
    
        LINAC3
    
    """
    LEIRInjection: typing.ClassVar['LeirParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.LeirParticleTransfer` LEIRInjection
    
        LEIRInjection
    
    """
    LEIREjection: typing.ClassVar['LeirParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.LeirParticleTransfer` LEIREjection
    
        LEIREjection
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'LeirParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['LeirParticleTransfer']: ...

class LhcParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LhcParticleTransfer'], ParticleTransfer):
    """
    public class LhcParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.LhcParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        LHC particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    LHCRING: typing.ClassVar['LhcParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.LhcParticleTransfer` LHCRING
    
        LHCRING
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'LhcParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['LhcParticleTransfer']: ...

class NorthParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['NorthParticleTransfer'], ParticleTransfer):
    """
    public class NorthParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        North Experimental Area particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    H2: typing.ClassVar['NorthParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer` H2
    
        H2
    
    """
    H4: typing.ClassVar['NorthParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer` H4
    
        H4
    
    """
    H6: typing.ClassVar['NorthParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer` H6
    
        H6
    
    """
    H8: typing.ClassVar['NorthParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer` H8
    
        H8
    
    """
    K12: typing.ClassVar['NorthParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer` K12
    
        K12
    
    """
    M2: typing.ClassVar['NorthParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer` M2
    
        M2
    
    """
    T2: typing.ClassVar['NorthParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer` T2
    
        T2
    
    """
    T4: typing.ClassVar['NorthParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer` T4
    
        T4
    
    """
    T6: typing.ClassVar['NorthParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer` T6
    
        T6
    
    """
    T10: typing.ClassVar['NorthParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.NorthParticleTransfer` T10
    
        T10
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'NorthParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['NorthParticleTransfer']: ...

class PsEastParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsEastParticleTransfer'], ParticleTransfer):
    """
    public class PsEastParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.PsEastParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        PS East Experimental Area particle transfers. (no tused for the moment - put here to be included into codebase of
        re-released applications to smothen the future modelling)
    
        Also see:
            :meth:`~serialized`
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'PsEastParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['PsEastParticleTransfer']: ...

class PsParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsParticleTransfer'], ParticleTransfer):
    """
    public class PsParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.PsParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        PS particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    PSRING: typing.ClassVar['PsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsParticleTransfer` PSRING
    
        PSRING
    
    """
    PSExtractionTT2: typing.ClassVar['PsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsParticleTransfer` PSExtractionTT2
    
        PSExtractionTT2
    
    """
    T08Transfer: typing.ClassVar['PsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsParticleTransfer` T08Transfer
    
        T08Transfer
    
    """
    T09Transfer: typing.ClassVar['PsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsParticleTransfer` T09Transfer
    
        T09Transfer
    
    """
    T11Transfer: typing.ClassVar['PsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsParticleTransfer` T11Transfer
    
        T11Transfer
    
    """
    PSExtractionEast: typing.ClassVar['PsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsParticleTransfer` PSExtractionEast
    
        PSExtractionEast
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'PsParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['PsParticleTransfer']: ...

class PsbParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsbParticleTransfer'], ParticleTransfer):
    """
    public class PsbParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        PSB particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    LINAC4: typing.ClassVar['PsbParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer` LINAC4
    
        LINAC4
    
    """
    PSBInjection: typing.ClassVar['PsbParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer` PSBInjection
    
        PSBInjection
    
    """
    PSBRING: typing.ClassVar['PsbParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer` PSBRING
    
        PSBRING
    
    """
    PSBExtraction: typing.ClassVar['PsbParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer` PSBExtraction
    
        PSBExtraction
    
    """
    PSTransfer: typing.ClassVar['PsbParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer` PSTransfer
    
        PSTransfer
    
    """
    GPSTransfer: typing.ClassVar['PsbParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer` GPSTransfer
    
        GPSTransfer
    
    """
    HRSTransfer: typing.ClassVar['PsbParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer` HRSTransfer
    
        HRSTransfer
    
    """
    PSBDumpTransfer: typing.ClassVar['PsbParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.PsbParticleTransfer` PSBDumpTransfer
    
        PSBDumpTransfer
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'PsbParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['PsbParticleTransfer']: ...

class SpsParticleTransfer(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsParticleTransfer'], ParticleTransfer):
    """
    public class SpsParticleTransfer extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer`> implements :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
    
        SPS particle transfers.
    
        Also see:
            :meth:`~serialized`
    """
    AWAKETransfer: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` AWAKETransfer
    
        AWAKETransfer
    
    """
    EastExtraction: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` EastExtraction
    
        EastExtraction
    
    """
    HiRadMatTransfer: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` HiRadMatTransfer
    
        HiRadMatTransfer
    
    """
    LHCB1Transfer: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` LHCB1Transfer
    
        LHCB1Transfer
    
    """
    LHCB2Transfer: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` LHCB2Transfer
    
        LHCB2Transfer
    
    """
    NorthExtraction: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` NorthExtraction
    
        NorthExtraction
    
    """
    SPSInjection: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` SPSInjection
    
        SPSInjection
    
    """
    SPSRING: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` SPSRING
    
        SPSRING
    
    """
    T2Transfer: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` T2Transfer
    
        T2Transfer
    
    """
    T4Transfer: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` T4Transfer
    
        T4Transfer
    
    """
    T6Transfer: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` T6Transfer
    
        T6Transfer
    
    """
    WestExtraction: typing.ClassVar['SpsParticleTransfer'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.particletransfers.SpsParticleTransfer` WestExtraction
    
        WestExtraction
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.List[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getDescription`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                particle transfer description (can be :code:`null`)
        
        
        """
        ...
    def getParticleTransferType(self) -> ParticleTransferType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer.getParticleTransferType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.particletransfers.ParticleTransfer`
        
            Returns:
                the type of particle transfer
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'SpsParticleTransfer': ...
    @staticmethod
    def values() -> typing.List['SpsParticleTransfer']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.particletransfers")``.

    AdParticleTransfer: typing.Type[AdParticleTransfer]
    AwakeParticleTransfer: typing.Type[AwakeParticleTransfer]
    CtfParticleTransfer: typing.Type[CtfParticleTransfer]
    ElenaParticleTransfer: typing.Type[ElenaParticleTransfer]
    IsoldeParticleTransfer: typing.Type[IsoldeParticleTransfer]
    LeirParticleTransfer: typing.Type[LeirParticleTransfer]
    LhcParticleTransfer: typing.Type[LhcParticleTransfer]
    NorthParticleTransfer: typing.Type[NorthParticleTransfer]
    ParticleTransfer: typing.Type[ParticleTransfer]
    ParticleTransferType: typing.Type[ParticleTransferType]
    PsEastParticleTransfer: typing.Type[PsEastParticleTransfer]
    PsParticleTransfer: typing.Type[PsParticleTransfer]
    PsbParticleTransfer: typing.Type[PsbParticleTransfer]
    SpsParticleTransfer: typing.Type[SpsParticleTransfer]
