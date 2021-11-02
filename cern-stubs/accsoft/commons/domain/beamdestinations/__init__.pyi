import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import java.util
import typing



class BeamDestination(cern.accsoft.commons.util.Named):
    """
    public interface BeamDestination extends cern.accsoft.commons.util.Named
    
        Accelerator beam destination.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                the accelerator this beam destination belongs to (never :code:`null`)
        
        
        """
        ...
    def getEndPoints(self) -> java.util.Set['BeamDestinationEndPoint']: ...

class BeamDestinationEndPoint(cern.accsoft.commons.util.Named):
    """
    public interface BeamDestinationEndPoint extends cern.accsoft.commons.util.Named
    
        Accelerator beam destination end point.
    """
    def getBeamDestination(self) -> BeamDestination:
        """
        
            Returns:
                the beam destination this end point belongs to (never :code:`null`)
        
        
        """
        ...

class SpsAwakeEndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsAwakeEndPoint'], BeamDestinationEndPoint):
    """
    public class SpsAwakeEndPoint extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.beamdestinations.SpsAwakeEndPoint`> implements :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
    
        SPS AWAKE end points.
    
        Also see:
            :meth:`~serialized`
    """
    NO_EXTRACTION: typing.ClassVar['SpsAwakeEndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsAwakeEndPoint` NO_EXTRACTION
    
        NO EXTRACTION
    
    """
    T40: typing.ClassVar['SpsAwakeEndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsAwakeEndPoint` T40
    
        T40
    
    """
    TT40_TED: typing.ClassVar['SpsAwakeEndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsAwakeEndPoint` TT40_TED
    
        TT40 TED
    
    """
    def getBeamDestination(self) -> 'SpsBeamDestination':
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint.getBeamDestination`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
        
            Returns:
                the beam destination this end point belongs to (never :code:`null`)
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'SpsAwakeEndPoint': ...
    @staticmethod
    def values() -> typing.List['SpsAwakeEndPoint']: ...

class SpsBeamDestination(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsBeamDestination'], BeamDestination):
    """
    public class SpsBeamDestination extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination`> implements :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestination`
    
        SPS beam destinations.
    
        Also see:
            :meth:`~serialized`
    """
    AWAKE: typing.ClassVar['SpsBeamDestination'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination` AWAKE
    
        AWAKE
    
    """
    FTARGET: typing.ClassVar['SpsBeamDestination'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination` FTARGET
    
        Fixed Target
    
    """
    HIRADMAT: typing.ClassVar['SpsBeamDestination'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination` HIRADMAT
    
        HIRADMAT
    
    """
    LHC_B1: typing.ClassVar['SpsBeamDestination'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination` LHC_B1
    
        LHC B1
    
    """
    LHC_B2: typing.ClassVar['SpsBeamDestination'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination` LHC_B2
    
        LHC B2
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beamdestinations.BeamDestination.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestination`
        
            Returns:
                the accelerator this beam destination belongs to (never :code:`null`)
        
        
        """
        ...
    def getEndPoints(self) -> java.util.Set[BeamDestinationEndPoint]: ...
    @staticmethod
    def valueOf(string: str) -> 'SpsBeamDestination': ...
    @staticmethod
    def values() -> typing.List['SpsBeamDestination']: ...

class SpsFTargetEndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsFTargetEndPoint'], BeamDestinationEndPoint):
    """
    public class SpsFTargetEndPoint extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint`> implements :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
    
        SPS FTARGET end points.
    
        Also see:
            :meth:`~serialized`
    """
    NO_EXTRACTION: typing.ClassVar['SpsFTargetEndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint` NO_EXTRACTION
    
        NO EXTRACTION
    
    """
    T2_T4_T6: typing.ClassVar['SpsFTargetEndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint` T2_T4_T6
    
        T2 T4 T6
    
    """
    T2_T4_T6_T10: typing.ClassVar['SpsFTargetEndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint` T2_T4_T6_T10
    
        T2 T4 T6 T10
    
    """
    TT20_TED: typing.ClassVar['SpsFTargetEndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint` TT20_TED
    
        TT20 TED
    
    """
    def getBeamDestination(self) -> SpsBeamDestination:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint.getBeamDestination`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
        
            Returns:
                the beam destination this end point belongs to (never :code:`null`)
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'SpsFTargetEndPoint': ...
    @staticmethod
    def values() -> typing.List['SpsFTargetEndPoint']: ...

class SpsHiradmatEndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsHiradmatEndPoint'], BeamDestinationEndPoint):
    """
    public class SpsHiradmatEndPoint extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.beamdestinations.SpsHiradmatEndPoint`> implements :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
    
        SPS HIRADMAT end points.
    
        Also see:
            :meth:`~serialized`
    """
    NO_EXTRACTION: typing.ClassVar['SpsHiradmatEndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsHiradmatEndPoint` NO_EXTRACTION
    
        NO EXTRACTION
    
    """
    TT60_TED: typing.ClassVar['SpsHiradmatEndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsHiradmatEndPoint` TT60_TED
    
        TT60 TED
    
    """
    TEST_BENCH: typing.ClassVar['SpsHiradmatEndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsHiradmatEndPoint` TEST_BENCH
    
        TEST BEANCH
    
    """
    def getBeamDestination(self) -> SpsBeamDestination:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint.getBeamDestination`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
        
            Returns:
                the beam destination this end point belongs to (never :code:`null`)
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'SpsHiradmatEndPoint': ...
    @staticmethod
    def values() -> typing.List['SpsHiradmatEndPoint']: ...

class SpsLhcB1EndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsLhcB1EndPoint'], BeamDestinationEndPoint):
    """
    public class SpsLhcB1EndPoint extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint`> implements :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
    
        SPS LHC B1 end points.
    
        Also see:
            :meth:`~serialized`
    """
    NO_EXTRACTION: typing.ClassVar['SpsLhcB1EndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint` NO_EXTRACTION
    
        NO EXTRACTION
    
    """
    LHC_RING1: typing.ClassVar['SpsLhcB1EndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint` LHC_RING1
    
        LHC RING1
    
    """
    TI2_TED: typing.ClassVar['SpsLhcB1EndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint` TI2_TED
    
        TI2 TED
    
    """
    TT60_TED: typing.ClassVar['SpsLhcB1EndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint` TT60_TED
    
        TT60 TED
    
    """
    def getBeamDestination(self) -> SpsBeamDestination:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint.getBeamDestination`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
        
            Returns:
                the beam destination this end point belongs to (never :code:`null`)
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'SpsLhcB1EndPoint': ...
    @staticmethod
    def values() -> typing.List['SpsLhcB1EndPoint']: ...

class SpsLhcB2EndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsLhcB2EndPoint'], BeamDestinationEndPoint):
    """
    public class SpsLhcB2EndPoint extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint`> implements :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
    
        SPS LHC B2 end points.
    
        Also see:
            :meth:`~serialized`
    """
    NO_EXTRACTION: typing.ClassVar['SpsLhcB2EndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint` NO_EXTRACTION
    
        NO EXTRACTION
    
    """
    LHC_RING2: typing.ClassVar['SpsLhcB2EndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint` LHC_RING2
    
        LHC RING2
    
    """
    TI8_TED: typing.ClassVar['SpsLhcB2EndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint` TI8_TED
    
        TI8 TED
    
    """
    TT40_TED: typing.ClassVar['SpsLhcB2EndPoint'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint` TT40_TED
    
        TT40 TED
    
    """
    def getBeamDestination(self) -> SpsBeamDestination:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint.getBeamDestination`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
        
            Returns:
                the beam destination this end point belongs to (never :code:`null`)
        
        
        """
        ...
    @staticmethod
    def valueOf(string: str) -> 'SpsLhcB2EndPoint': ...
    @staticmethod
    def values() -> typing.List['SpsLhcB2EndPoint']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.beamdestinations")``.

    BeamDestination: typing.Type[BeamDestination]
    BeamDestinationEndPoint: typing.Type[BeamDestinationEndPoint]
    SpsAwakeEndPoint: typing.Type[SpsAwakeEndPoint]
    SpsBeamDestination: typing.Type[SpsBeamDestination]
    SpsFTargetEndPoint: typing.Type[SpsFTargetEndPoint]
    SpsHiradmatEndPoint: typing.Type[SpsHiradmatEndPoint]
    SpsLhcB1EndPoint: typing.Type[SpsLhcB1EndPoint]
    SpsLhcB2EndPoint: typing.Type[SpsLhcB2EndPoint]
