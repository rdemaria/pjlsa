import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.util
import java.util
import typing



class AcceleratorZone(cern.accsoft.commons.util.Named):
    """
    public interface AcceleratorZone extends cern.accsoft.commons.util.Named
    
        Accelerator zones.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...

class AdAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['AdAcceleratorZone'], AcceleratorZone):
    """
    public class AdAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.AdAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        AD accelerator zones.
    
        Also see:
            :meth:`~serialized`
    """
    AD: typing.ClassVar['AdAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.AdAcceleratorZone` AD
    
        AD ring
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'AdAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['AdAcceleratorZone']: ...

class AwakeAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['AwakeAcceleratorZone'], AcceleratorZone):
    """
    public class AwakeAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.AwakeAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        AWAKE accelerator zones.
    
        Also see:
            :meth:`~serialized`
    """
    AWAKE: typing.ClassVar['AwakeAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.AwakeAcceleratorZone` AWAKE
    
        AWAKE Experiment
    
    """
    TT43: typing.ClassVar['AwakeAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.AwakeAcceleratorZone` TT43
    
        AWAKE electron line
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'AwakeAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['AwakeAcceleratorZone']: ...

class CtfAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['CtfAcceleratorZone'], AcceleratorZone):
    """
    public class CtfAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.CtfAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        CTF accelerator zones.
    
        Also see:
            :meth:`~serialized`
    """
    CTF: typing.ClassVar['CtfAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.CtfAcceleratorZone` CTF
    
        CTF
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'CtfAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['CtfAcceleratorZone']: ...

class ElenaAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['ElenaAcceleratorZone'], AcceleratorZone):
    """
    public class ElenaAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        ELENA accelerator zones.
    
        Also see:
            :meth:`~serialized`
    """
    ELENA: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` ELENA
    
        ELENA
    
    """
    LNE00: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE00
    
        LNE00
    
    """
    LNE01A: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE01A
    
        LNE01A
    
    """
    LNE01B: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE01B
    
        LNE01B
    
    """
    LNE01C: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE01C
    
        LNE01C
    
    """
    LNE03A: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE03A
    
        LNE03A
    
    """
    LNE01D: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE01D
    
        LNE01D
    
    """
    LNE02: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE02
    
        LNE02
    
    """
    LNE03B: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE03B
    
        LNE03B
    
    """
    LNE04: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE04
    
        LNE04
    
    """
    LNE06A: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE06A
    
        LNE06A
    
    """
    LNE05: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE05
    
        LNE05
    
    """
    LNE06B: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE06B
    
        LNE06B
    
    """
    LNE07: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE07
    
        LNE07
    
    """
    LNE50: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE50
    
        LNE50
    
    """
    LNE51: typing.ClassVar['ElenaAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.ElenaAcceleratorZone` LNE51
    
        LNE51
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'ElenaAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['ElenaAcceleratorZone']: ...

class IsoldeAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['IsoldeAcceleratorZone'], AcceleratorZone):
    """
    public class IsoldeAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.IsoldeAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        ISOLDE accelerator zones.
    
        Also see:
            :meth:`~serialized`
    """
    ISOLDE: typing.ClassVar['IsoldeAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.IsoldeAcceleratorZone` ISOLDE
    
        ISOLDE
    
    """
    HIE: typing.ClassVar['IsoldeAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.IsoldeAcceleratorZone` HIE
    
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'IsoldeAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['IsoldeAcceleratorZone']: ...

class LeirAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LeirAcceleratorZone'], AcceleratorZone):
    """
    public class LeirAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        LEIR accelerator zones.
    
        Also see:
            :meth:`~serialized`
    """
    LEIR: typing.ClassVar['LeirAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone` LEIR
    
        LEIR
    
    """
    LINAC3: typing.ClassVar['LeirAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone` LINAC3
    
        LINAC3
    
    """
    ETL: typing.ClassVar['LeirAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone` ETL
    
        ETL
    
    """
    ITE: typing.ClassVar['LeirAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone` ITE
    
        ITE
    
    """
    ETP: typing.ClassVar['LeirAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone` ETP
    
        ETP
    
    """
    ITH: typing.ClassVar['LeirAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone` ITH
    
        ITH
    
    """
    ETL_INJ: typing.ClassVar['LeirAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone` ETL_INJ
    
        ETL_INJ
    
    """
    ETL_EJ: typing.ClassVar['LeirAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone` ETL_EJ
    
        ETL_EJ
    
    """
    EI: typing.ClassVar['LeirAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone` EI
    
        EI
    
    """
    EE: typing.ClassVar['LeirAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LeirAcceleratorZone` EE
    
        EE
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'LeirAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['LeirAcceleratorZone']: ...

class LhcAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LhcAcceleratorZone'], AcceleratorZone):
    """
    public class LhcAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.LhcAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        LHC accelerator zones.
    
        Also see:
            :meth:`~serialized`
    """
    LHC: typing.ClassVar['LhcAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.LhcAcceleratorZone` LHC
    
        LHC ring
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'LhcAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['LhcAcceleratorZone']: ...

class NorthAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['NorthAcceleratorZone'], AcceleratorZone):
    """
    public class NorthAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        North Experimental Area zones.
    
        Also see:
            :meth:`~serialized`
    """
    H2Z: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H2Z
    
        H2Z Experimental zone
    
    """
    H2A: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H2A
    
        H2A Experimental zone
    
    """
    H2B: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H2B
    
        H2B Experimental zone
    
    """
    H4Z: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H4Z
    
        H4Z Experimental zone
    
    """
    H4A: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H4A
    
        H4A Experimental zone
    
    """
    H4B: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H4B
    
        H4B Experimental zone
    
    """
    H4C: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H4C
    
        H4C Experimental zone
    
    """
    H6Z: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H6Z
    
        H6Z Experimental zone
    
    """
    H6A: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H6A
    
        H6A Experimental zone
    
    """
    H6B: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H6B
    
        H6B Experimental zone
    
    """
    H6C: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H6C
    
        H6C Experimental zone
    
    """
    H8Z: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H8Z
    
        H8Z Experimental zone
    
    """
    H8A: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H8A
    
        H8A Experimental zone
    
    """
    H8B: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H8B
    
        H8B Experimental zone
    
    """
    H8C: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` H8C
    
        H8C Experimental zone
    
    """
    K12A: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` K12A
    
        K12A Experimental zone
    
    """
    M2A: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` M2A
    
        M2A Experimental zone
    
    """
    T2A: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` T2A
    
        T2A Experimental zone
    
    """
    T4A: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` T4A
    
        T4A Experimental zone
    
    """
    T6A: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` T6A
    
        T6A Experimental zone
    
    """
    T10A: typing.ClassVar['NorthAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.NorthAcceleratorZone` T10A
    
        T10A Experimental zone
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'NorthAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['NorthAcceleratorZone']: ...

class PsAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsAcceleratorZone'], AcceleratorZone):
    """
    public class PsAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.PsAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        PS accelerator zones.
    
        Also see:
            :meth:`~serialized`
    """
    PS: typing.ClassVar['PsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsAcceleratorZone` PS
    
        PS
    
    """
    F16: typing.ClassVar['PsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsAcceleratorZone` F16
    
        F16
    
    """
    F61: typing.ClassVar['PsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsAcceleratorZone` F61
    
        F61
    
    """
    T08: typing.ClassVar['PsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsAcceleratorZone` T08
    
        T08
    
    """
    F62_1: typing.ClassVar['PsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsAcceleratorZone` F62_1
    
        F62_1
    
    """
    F62_2: typing.ClassVar['PsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsAcceleratorZone` F62_2
    
        F62_2
    
    """
    F63: typing.ClassVar['PsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsAcceleratorZone` F63
    
        F63
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'PsAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['PsAcceleratorZone']: ...

class PsEastAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsEastAcceleratorZone'], AcceleratorZone):
    """
    public class PsEastAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.PsEastAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        PS East Experimental Area zones.
    
        Also see:
            :meth:`~serialized`
    """
    PS_EAST: typing.ClassVar['PsEastAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsEastAcceleratorZone` PS_EAST
    
        PS_EAST Experimental zone
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'PsEastAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['PsEastAcceleratorZone']: ...

class PsbAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['PsbAcceleratorZone'], AcceleratorZone):
    """
    public class PsbAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        PS booster accelerator zones.
    
        Also see:
            :meth:`~serialized`
    """
    LINAC4: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` LINAC4
    
        LINAC4
    
    """
    L4T: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` L4T
    
        L4T
    
    """
    LT: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` LT
    
        LT
    
    """
    LTB: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` LTB
    
        LTB
    
    """
    LBE: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` LBE
    
        LBE
    
    """
    BI: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` BI
    
        BI
    
    """
    PSB: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` PSB
    
        PSB
    
    """
    BE_BT: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` BE_BT
    
        BE_BT
    
    """
    BTP: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` BTP
    
        BTP
    
    """
    BTM: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` BTM
    
        Deprecated.
        BTM
    
    """
    BTY: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` BTY
    
        Deprecated.
        BTY
    
    """
    BTM_BTY: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` BTM_BTY
    
        BTM_BTY
    
    """
    BTY_GPS: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` BTY_GPS
    
        BTY_GPS
    
    """
    BTY_HRS: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` BTY_HRS
    
        BTY_HRS
    
    """
    BT_DUMP: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` BT_DUMP
    
        BT_DUMP
    
    """
    BTM_DUMP: typing.ClassVar['PsbAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.PsbAcceleratorZone` BTM_DUMP
    
        BTM_DUMP
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'PsbAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['PsbAcceleratorZone']: ...

class SpsAcceleratorZone(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsAcceleratorZone'], AcceleratorZone):
    """
    public class SpsAcceleratorZone extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone`> implements :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
    
        SPS accelerator zones.
    
        Also see:
            :meth:`~serialized`
    """
    SPS: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` SPS
    
        SPS
    
    """
    TT40: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT40
    
        TT40
    
    """
    TI8: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TI8
    
        TI8
    
    """
    TT41: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT41
    
        TT41
    
    """
    TT10: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT10
    
        TT10
    
    """
    TT21: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT21
    
        TT21
    
    """
    TT22: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT22
    
        TT22
    
    """
    TT23: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT23
    
        TT23
    
    """
    TT24: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT24
    
        TT24
    
    """
    TT25: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT25
    
        TT25
    
    """
    TT60: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT60
    
        TT60
    
    """
    TI2: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TI2
    
        TI2
    
    """
    NORTH_EXTRACTION: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` NORTH_EXTRACTION
    
        NORTH_EXTRACTION
    
    """
    WEST_EXTRACTION: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` WEST_EXTRACTION
    
        WEST_EXTRACTION
    
    """
    EAST_EXTRACTION: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` EAST_EXTRACTION
    
        EAST_EXTRACTION
    
    """
    TT2: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT2
    
        TT2
    
    """
    TT66: typing.ClassVar['SpsAcceleratorZone'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.zones.SpsAcceleratorZone` TT66
    
        TT66
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.zones.AcceleratorZone.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.zones.AcceleratorZone`
        
            Returns:
                the accelerator this beam mode is for (never :code:`null`)
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def valueOf(string: str) -> 'SpsAcceleratorZone': ...
    @staticmethod
    def values() -> typing.List['SpsAcceleratorZone']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.zones")``.

    AcceleratorZone: typing.Type[AcceleratorZone]
    AdAcceleratorZone: typing.Type[AdAcceleratorZone]
    AwakeAcceleratorZone: typing.Type[AwakeAcceleratorZone]
    CtfAcceleratorZone: typing.Type[CtfAcceleratorZone]
    ElenaAcceleratorZone: typing.Type[ElenaAcceleratorZone]
    IsoldeAcceleratorZone: typing.Type[IsoldeAcceleratorZone]
    LeirAcceleratorZone: typing.Type[LeirAcceleratorZone]
    LhcAcceleratorZone: typing.Type[LhcAcceleratorZone]
    NorthAcceleratorZone: typing.Type[NorthAcceleratorZone]
    PsAcceleratorZone: typing.Type[PsAcceleratorZone]
    PsEastAcceleratorZone: typing.Type[PsEastAcceleratorZone]
    PsbAcceleratorZone: typing.Type[PsbAcceleratorZone]
    SpsAcceleratorZone: typing.Type[SpsAcceleratorZone]
