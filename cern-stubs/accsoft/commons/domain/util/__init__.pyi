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
    public class AccsoftDomainUtil extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods to be used by clients.
    """
    _findAcceleratorZone__T = typing.TypeVar('_findAcceleratorZone__T', bound=cern.accsoft.commons.domain.Accelerator)  # <T>
    @staticmethod
    def findAcceleratorZone(class_: typing.Type[_findAcceleratorZone__T], string: str) -> cern.accsoft.commons.domain.zones.AcceleratorZone: ...
    @staticmethod
    def findBeam(accelerator: cern.accsoft.commons.domain.Accelerator, string: str) -> cern.accsoft.commons.domain.beams.Beam:
        """
            Finds accelerator beam.
        
            Parameters:
                accelerator (:class:`~cern.accsoft.commons.domain.Accelerator`): accelerator
                beamName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): beam name
        
            Returns:
                :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Raises:
                : if beam doesn't exist
        
        
        """
        ...
    @staticmethod
    def findBeamDestinationEndPoint(beamDestination: cern.accsoft.commons.domain.beamdestinations.BeamDestination, string: str) -> cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint:
        """
            Finds beam destination end point by name.
        
            Parameters:
                beamDestination (:class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestination`):         endPointName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                :class:`~cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint`
        
            Raises:
                : if end point doesn't exist
        
        
        """
        ...
    _findNamedEnumValue__T = typing.TypeVar('_findNamedEnumValue__T', bound=cern.accsoft.commons.util.Named)  # <T>
    @staticmethod
    def findNamedEnumValue(class_: typing.Type[_findNamedEnumValue__T], string: str) -> _findNamedEnumValue__T: ...
    _findParticleTransfer__T = typing.TypeVar('_findParticleTransfer__T', bound=cern.accsoft.commons.domain.Accelerator)  # <T>
    @staticmethod
    def findParticleTransfer(class_: typing.Type[_findParticleTransfer__T], string: str) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...

_CodeEntityConverter__E = typing.TypeVar('_CodeEntityConverter__E')  # <E>
class CodeEntityConverter(typing.Generic[_CodeEntityConverter__E]):
    """
    public class CodeEntityConverter<E> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Generic class to convert between codes and corresponding entities.
    """
    @typing.overload
    def fromCode(self, int: int) -> _CodeEntityConverter__E:
        """
        
            Parameters:
                code (long): code
        
            Returns:
                corresponding entity
        
        
            Parameters:
                code (int): code
        
            Returns:
                corresponding entity
        
        
        """
        ...
    @typing.overload
    def fromCode(self, long: int) -> _CodeEntityConverter__E: ...
    def getFromCodeMap(self) -> java.util.Map[int, _CodeEntityConverter__E]: ...
    def getToCodeMap(self) -> java.util.Map[_CodeEntityConverter__E, int]: ...
    def toCode(self, e: _CodeEntityConverter__E) -> int:
        """
        
            Parameters:
                entity (:class:`~cern.accsoft.commons.domain.util.CodeEntityConverter`): entity
        
            Returns:
                corresponding code
        
        
        """
        ...

class EnumEmulationUtils:
    """
    public class EnumEmulationUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
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
