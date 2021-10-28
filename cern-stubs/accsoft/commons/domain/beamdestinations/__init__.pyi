import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import java.util
import typing



class BeamDestination(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.accsoft.commons.domain.beamdestinations.BeamDestination'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getEndPoints(self) -> java.util.Set['BeamDestinationEndPoint']: ...

class BeamDestinationEndPoint(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getBeamDestination(self) -> BeamDestination: ...

class SpsAwakeEndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsAwakeEndPoint'], BeamDestinationEndPoint):
    """
    Java class 'cern.accsoft.commons.domain.beamdestinations.SpsAwakeEndPoint'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.beamdestinations.BeamDestinationEn
            dPoint
    
      Attributes:
        NO_EXTRACTION (cern.accsoft.commons.domain.beamdestinations.SpsAwakeEndPoint): final static field
        T40 (cern.accsoft.commons.domain.beamdestinations.SpsAwakeEndPoint): final static field
        TT40_TED (cern.accsoft.commons.domain.beamdestinations.SpsAwakeEndPoint): final static field
    
    """
    NO_EXTRACTION: typing.ClassVar['SpsAwakeEndPoint'] = ...
    T40: typing.ClassVar['SpsAwakeEndPoint'] = ...
    TT40_TED: typing.ClassVar['SpsAwakeEndPoint'] = ...
    def getBeamDestination(self) -> 'SpsBeamDestination': ...
    @staticmethod
    def valueOf(string: str) -> 'SpsAwakeEndPoint': ...
    @staticmethod
    def values() -> typing.List['SpsAwakeEndPoint']: ...

class SpsBeamDestination(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsBeamDestination'], BeamDestination):
    """
    Java class 'cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.beamdestinations.BeamDestination
    
      Attributes:
        AWAKE (cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination): final static field
        FTARGET (cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination): final static field
        HIRADMAT (cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination): final static field
        LHC_B1 (cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination): final static field
        LHC_B2 (cern.accsoft.commons.domain.beamdestinations.SpsBeamDestination): final static field
    
    """
    AWAKE: typing.ClassVar['SpsBeamDestination'] = ...
    FTARGET: typing.ClassVar['SpsBeamDestination'] = ...
    HIRADMAT: typing.ClassVar['SpsBeamDestination'] = ...
    LHC_B1: typing.ClassVar['SpsBeamDestination'] = ...
    LHC_B2: typing.ClassVar['SpsBeamDestination'] = ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getEndPoints(self) -> java.util.Set[BeamDestinationEndPoint]: ...
    @staticmethod
    def valueOf(string: str) -> 'SpsBeamDestination': ...
    @staticmethod
    def values() -> typing.List['SpsBeamDestination']: ...

class SpsFTargetEndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsFTargetEndPoint'], BeamDestinationEndPoint):
    """
    Java class 'cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.beamdestinations.BeamDestinationEn
            dPoint
    
      Attributes:
        NO_EXTRACTION (cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint): final static field
        T2_T4_T6 (cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint): final static field
        T2_T4_T6_T10 (cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint): final static field
        TT20_TED (cern.accsoft.commons.domain.beamdestinations.SpsFTargetEndPoint): final static field
    
    """
    NO_EXTRACTION: typing.ClassVar['SpsFTargetEndPoint'] = ...
    T2_T4_T6: typing.ClassVar['SpsFTargetEndPoint'] = ...
    T2_T4_T6_T10: typing.ClassVar['SpsFTargetEndPoint'] = ...
    TT20_TED: typing.ClassVar['SpsFTargetEndPoint'] = ...
    def getBeamDestination(self) -> SpsBeamDestination: ...
    @staticmethod
    def valueOf(string: str) -> 'SpsFTargetEndPoint': ...
    @staticmethod
    def values() -> typing.List['SpsFTargetEndPoint']: ...

class SpsHiradmatEndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsHiradmatEndPoint'], BeamDestinationEndPoint):
    """
    Java class 'cern.accsoft.commons.domain.beamdestinations.SpsHiradmatEndPoint'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.beamdestinations.BeamDestinationEn
            dPoint
    
      Attributes:
        NO_EXTRACTION (cern.accsoft.commons.domain.beamdestinations.SpsHiradmatEndPoint): final static field
        TT60_TED (cern.accsoft.commons.domain.beamdestinations.SpsHiradmatEndPoint): final static field
        TEST_BENCH (cern.accsoft.commons.domain.beamdestinations.SpsHiradmatEndPoint): final static field
    
    """
    NO_EXTRACTION: typing.ClassVar['SpsHiradmatEndPoint'] = ...
    TT60_TED: typing.ClassVar['SpsHiradmatEndPoint'] = ...
    TEST_BENCH: typing.ClassVar['SpsHiradmatEndPoint'] = ...
    def getBeamDestination(self) -> SpsBeamDestination: ...
    @staticmethod
    def valueOf(string: str) -> 'SpsHiradmatEndPoint': ...
    @staticmethod
    def values() -> typing.List['SpsHiradmatEndPoint']: ...

class SpsLhcB1EndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsLhcB1EndPoint'], BeamDestinationEndPoint):
    """
    Java class 'cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.beamdestinations.BeamDestinationEn
            dPoint
    
      Attributes:
        NO_EXTRACTION (cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint): final static field
        LHC_RING1 (cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint): final static field
        TI2_TED (cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint): final static field
        TT60_TED (cern.accsoft.commons.domain.beamdestinations.SpsLhcB1EndPoint): final static field
    
    """
    NO_EXTRACTION: typing.ClassVar['SpsLhcB1EndPoint'] = ...
    LHC_RING1: typing.ClassVar['SpsLhcB1EndPoint'] = ...
    TI2_TED: typing.ClassVar['SpsLhcB1EndPoint'] = ...
    TT60_TED: typing.ClassVar['SpsLhcB1EndPoint'] = ...
    def getBeamDestination(self) -> SpsBeamDestination: ...
    @staticmethod
    def valueOf(string: str) -> 'SpsLhcB1EndPoint': ...
    @staticmethod
    def values() -> typing.List['SpsLhcB1EndPoint']: ...

class SpsLhcB2EndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsLhcB2EndPoint'], BeamDestinationEndPoint):
    """
    Java class 'cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.accsoft.commons.domain.beamdestinations.BeamDestinationEn
            dPoint
    
      Attributes:
        NO_EXTRACTION (cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint): final static field
        LHC_RING2 (cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint): final static field
        TI8_TED (cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint): final static field
        TT40_TED (cern.accsoft.commons.domain.beamdestinations.SpsLhcB2EndPoint): final static field
    
    """
    NO_EXTRACTION: typing.ClassVar['SpsLhcB2EndPoint'] = ...
    LHC_RING2: typing.ClassVar['SpsLhcB2EndPoint'] = ...
    TI8_TED: typing.ClassVar['SpsLhcB2EndPoint'] = ...
    TT40_TED: typing.ClassVar['SpsLhcB2EndPoint'] = ...
    def getBeamDestination(self) -> SpsBeamDestination: ...
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
