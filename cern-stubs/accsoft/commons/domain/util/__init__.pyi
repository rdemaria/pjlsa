from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import Generic as _py_Generic
from typing import overload
import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.beamdestinations
import cern.accsoft.commons.domain.beams
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.util
import java.util


class AccsoftDomainUtil:
    _findAcceleratorZone__T = _py_TypeVar('_findAcceleratorZone__T', bound=cern.accsoft.commons.domain.Accelerator)  # <T>
    @classmethod
    def findAcceleratorZone(cls, class_: _py_Type[_findAcceleratorZone__T], string: str) -> cern.accsoft.commons.domain.zones.AcceleratorZone: ...
    @classmethod
    def findBeam(cls, accelerator: cern.accsoft.commons.domain.Accelerator, string: str) -> cern.accsoft.commons.domain.beams.Beam: ...
    @classmethod
    def findBeamDestinationEndPoint(cls, beamDestination: cern.accsoft.commons.domain.beamdestinations.BeamDestination, string: str) -> cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint: ...
    _findNamedEnumValue__T = _py_TypeVar('_findNamedEnumValue__T', bound=cern.accsoft.commons.util.Named)  # <T>
    @classmethod
    def findNamedEnumValue(cls, class_: _py_Type[_findNamedEnumValue__T], string: str) -> _findNamedEnumValue__T: ...
    _findParticleTransfer__T = _py_TypeVar('_findParticleTransfer__T', bound=cern.accsoft.commons.domain.Accelerator)  # <T>
    @classmethod
    def findParticleTransfer(cls, class_: _py_Type[_findParticleTransfer__T], string: str) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...

_CodeEntityConverter__E = _py_TypeVar('_CodeEntityConverter__E')  # <E>
class CodeEntityConverter(_py_Generic[_CodeEntityConverter__E]):
    @overload
    def fromCode(self, long: int) -> _CodeEntityConverter__E: ...
    @overload
    def fromCode(self, int: int) -> _CodeEntityConverter__E: ...
    def getFromCodeMap(self) -> java.util.Map[int, _CodeEntityConverter__E]: ...
    def getToCodeMap(self) -> java.util.Map[_CodeEntityConverter__E, int]: ...
    def toCode(self, e: _CodeEntityConverter__E) -> int: ...

class EnumEmulationUtils:
    _getEnumConstants__T = _py_TypeVar('_getEnumConstants__T')  # <T>
    @classmethod
    def getEnumConstants(cls, class_: _py_Type[_getEnumConstants__T]) -> _py_List[_getEnumConstants__T]: ...
    _getEnumConstantsMap__T = _py_TypeVar('_getEnumConstantsMap__T')  # <T>
    @classmethod
    def getEnumConstantsMap(cls, class_: _py_Type[_getEnumConstantsMap__T]) -> java.util.Map[str, _getEnumConstantsMap__T]: ...
    _valueOf__T = _py_TypeVar('_valueOf__T')  # <T>
    @classmethod
    def valueOf(cls, string: str, class_: _py_Type[_valueOf__T]) -> _valueOf__T: ...
