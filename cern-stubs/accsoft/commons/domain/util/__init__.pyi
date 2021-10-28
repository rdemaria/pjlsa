import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.beamdestinations
import cern.accsoft.commons.domain.beams
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.util
import java.util
import typing



class AccsoftDomainUtil:
    """
    Java class 'cern.accsoft.commons.domain.util.AccsoftDomainUtil'
    
        Extends:
            java.lang.Object
    
    """
    _findAcceleratorZone__T = typing.TypeVar('_findAcceleratorZone__T', bound=cern.accsoft.commons.domain.Accelerator)  # <T>
    @staticmethod
    def findAcceleratorZone(class_: typing.Type[_findAcceleratorZone__T], string: str) -> cern.accsoft.commons.domain.zones.AcceleratorZone: ...
    @staticmethod
    def findBeam(accelerator: cern.accsoft.commons.domain.Accelerator, string: str) -> cern.accsoft.commons.domain.beams.Beam: ...
    @staticmethod
    def findBeamDestinationEndPoint(beamDestination: cern.accsoft.commons.domain.beamdestinations.BeamDestination, string: str) -> cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint: ...
    _findNamedEnumValue__T = typing.TypeVar('_findNamedEnumValue__T', bound=cern.accsoft.commons.util.Named)  # <T>
    @staticmethod
    def findNamedEnumValue(class_: typing.Type[_findNamedEnumValue__T], string: str) -> _findNamedEnumValue__T: ...
    _findParticleTransfer__T = typing.TypeVar('_findParticleTransfer__T', bound=cern.accsoft.commons.domain.Accelerator)  # <T>
    @staticmethod
    def findParticleTransfer(class_: typing.Type[_findParticleTransfer__T], string: str) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...

_CodeEntityConverter__E = typing.TypeVar('_CodeEntityConverter__E')  # <E>
class CodeEntityConverter(typing.Generic[_CodeEntityConverter__E]):
    """
    Java class 'cern.accsoft.commons.domain.util.CodeEntityConverter'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    def fromCode(self, int: int) -> _CodeEntityConverter__E: ...
    @typing.overload
    def fromCode(self, long: int) -> _CodeEntityConverter__E: ...
    def getFromCodeMap(self) -> java.util.Map[int, _CodeEntityConverter__E]: ...
    def getToCodeMap(self) -> java.util.Map[_CodeEntityConverter__E, int]: ...
    def toCode(self, e: _CodeEntityConverter__E) -> int: ...

class EnumEmulationUtils:
    """
    Java class 'cern.accsoft.commons.domain.util.EnumEmulationUtils'
    
        Extends:
            java.lang.Object
    
    """
    _getEnumConstants__T = typing.TypeVar('_getEnumConstants__T')  # <T>
    @staticmethod
    def getEnumConstants(class_: typing.Type[_getEnumConstants__T]) -> typing.List[_getEnumConstants__T]: ...
    _getEnumConstantsMap__T = typing.TypeVar('_getEnumConstantsMap__T')  # <T>
    @staticmethod
    def getEnumConstantsMap(class_: typing.Type[_getEnumConstantsMap__T]) -> java.util.Map[str, _getEnumConstantsMap__T]: ...
    _valueOf__T = typing.TypeVar('_valueOf__T')  # <T>
    @staticmethod
    def valueOf(string: str, class_: typing.Type[_valueOf__T]) -> _valueOf__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.util")``.

    AccsoftDomainUtil: typing.Type[AccsoftDomainUtil]
    CodeEntityConverter: typing.Type[CodeEntityConverter]
    EnumEmulationUtils: typing.Type[EnumEmulationUtils]
