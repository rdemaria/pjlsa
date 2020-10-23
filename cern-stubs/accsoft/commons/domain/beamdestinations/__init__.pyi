from typing import List as _py_List
from typing import ClassVar as _py_ClassVar
from typing import overload
import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import java.util


class BeamDestination(cern.accsoft.commons.util.Named):
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getEndPoints(self) -> java.util.Set['BeamDestinationEndPoint']: ...

class BeamDestinationEndPoint(cern.accsoft.commons.util.Named):
    def getBeamDestination(self) -> BeamDestination: ...

class SpsAwakeEndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsAwakeEndPoint'], BeamDestinationEndPoint):
    NO_EXTRACTION: _py_ClassVar['SpsAwakeEndPoint'] = ...
    T40: _py_ClassVar['SpsAwakeEndPoint'] = ...
    TT40_TED: _py_ClassVar['SpsAwakeEndPoint'] = ...
    @overload
    def getBeamDestination(self) -> BeamDestination: ...
    @overload
    def getBeamDestination(self) -> 'SpsBeamDestination': ...
    @classmethod
    def valueOf(cls, string: str) -> 'SpsAwakeEndPoint': ...
    @classmethod
    def values(cls) -> _py_List['SpsAwakeEndPoint']: ...

class SpsBeamDestination(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsBeamDestination'], BeamDestination):
    AWAKE: _py_ClassVar['SpsBeamDestination'] = ...
    FTARGET: _py_ClassVar['SpsBeamDestination'] = ...
    HIRADMAT: _py_ClassVar['SpsBeamDestination'] = ...
    LHC_B1: _py_ClassVar['SpsBeamDestination'] = ...
    LHC_B2: _py_ClassVar['SpsBeamDestination'] = ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getEndPoints(self) -> java.util.Set[BeamDestinationEndPoint]: ...
    @classmethod
    def valueOf(cls, string: str) -> 'SpsBeamDestination': ...
    @classmethod
    def values(cls) -> _py_List['SpsBeamDestination']: ...

class SpsFTargetEndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsFTargetEndPoint'], BeamDestinationEndPoint):
    NO_EXTRACTION: _py_ClassVar['SpsFTargetEndPoint'] = ...
    T2_T4_T6: _py_ClassVar['SpsFTargetEndPoint'] = ...
    T2_T4_T6_T10: _py_ClassVar['SpsFTargetEndPoint'] = ...
    TT20_TED: _py_ClassVar['SpsFTargetEndPoint'] = ...
    @overload
    def getBeamDestination(self) -> BeamDestination: ...
    @overload
    def getBeamDestination(self) -> SpsBeamDestination: ...
    @classmethod
    def valueOf(cls, string: str) -> 'SpsFTargetEndPoint': ...
    @classmethod
    def values(cls) -> _py_List['SpsFTargetEndPoint']: ...

class SpsHiradmatEndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsHiradmatEndPoint'], BeamDestinationEndPoint):
    NO_EXTRACTION: _py_ClassVar['SpsHiradmatEndPoint'] = ...
    TT60_TED: _py_ClassVar['SpsHiradmatEndPoint'] = ...
    TEST_BENCH: _py_ClassVar['SpsHiradmatEndPoint'] = ...
    @overload
    def getBeamDestination(self) -> BeamDestination: ...
    @overload
    def getBeamDestination(self) -> SpsBeamDestination: ...
    @classmethod
    def valueOf(cls, string: str) -> 'SpsHiradmatEndPoint': ...
    @classmethod
    def values(cls) -> _py_List['SpsHiradmatEndPoint']: ...

class SpsLhcB1EndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsLhcB1EndPoint'], BeamDestinationEndPoint):
    NO_EXTRACTION: _py_ClassVar['SpsLhcB1EndPoint'] = ...
    LHC_RING1: _py_ClassVar['SpsLhcB1EndPoint'] = ...
    TI2_TED: _py_ClassVar['SpsLhcB1EndPoint'] = ...
    TT60_TED: _py_ClassVar['SpsLhcB1EndPoint'] = ...
    @overload
    def getBeamDestination(self) -> BeamDestination: ...
    @overload
    def getBeamDestination(self) -> SpsBeamDestination: ...
    @classmethod
    def valueOf(cls, string: str) -> 'SpsLhcB1EndPoint': ...
    @classmethod
    def values(cls) -> _py_List['SpsLhcB1EndPoint']: ...

class SpsLhcB2EndPoint(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['SpsLhcB2EndPoint'], BeamDestinationEndPoint):
    NO_EXTRACTION: _py_ClassVar['SpsLhcB2EndPoint'] = ...
    LHC_RING2: _py_ClassVar['SpsLhcB2EndPoint'] = ...
    TI8_TED: _py_ClassVar['SpsLhcB2EndPoint'] = ...
    TT40_TED: _py_ClassVar['SpsLhcB2EndPoint'] = ...
    @overload
    def getBeamDestination(self) -> BeamDestination: ...
    @overload
    def getBeamDestination(self) -> SpsBeamDestination: ...
    @classmethod
    def valueOf(cls, string: str) -> 'SpsLhcB2EndPoint': ...
    @classmethod
    def values(cls) -> _py_List['SpsLhcB2EndPoint']: ...