import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.beams
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.commons
import cern.lsa.domain.devices
import cern.lsa.domain.optics.factory
import cern.lsa.domain.optics.spi
import cern.lsa.domain.settings
import cern.lsa.domain.settings.type
import com.google.common.collect
import java.io
import java.lang
import java.util
import typing



class BeamEnum(java.lang.Enum['BeamEnum']):
    """
    public enum BeamEnum extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.optics.BeamEnum`>
    
        A ring in the machine, also known as *beam*. For instance, the LHC has two rings, that correspond to the two beams,
        whereas the Booster has four.
    
        This identifier can be typically used to mark whether certain entities are defined, belong or work on specific rings in
        an accelerator.
    """
    B1: typing.ClassVar['BeamEnum'] = ...
    B2: typing.ClassVar['BeamEnum'] = ...
    B3: typing.ClassVar['BeamEnum'] = ...
    B4: typing.ClassVar['BeamEnum'] = ...
    @staticmethod
    def toBeamEnum(string: str) -> 'BeamEnum':
        """
            Converts given string to an element of the :class:`~cern.lsa.domain.optics.BeamEnum` enum. The specified string is
            expected to be a digit (from 1 to 4) optionally prefixed by letter "B" or "b" e.g. "2", "b2" and "B2" represent
            :meth:`~cern.lsa.domain.optics.BeamEnum.B2`.
        
            Parameters:
                beam (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): string representation of the beam
        
            Returns:
                bean identifier represented by given string
        
            Raises:
                : if the string can't be parsed to a :class:`~cern.lsa.domain.optics.BeamEnum` or is :code:`null`
        
            Also see:
                :meth:`~cern.lsa.domain.optics.BeamEnum.valueOf`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'BeamEnum':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['BeamEnum']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (BeamEnum c : BeamEnum.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Calibration(cern.accsoft.commons.util.Named):
    """
    public interface Calibration extends cern.accsoft.commons.util.Named
    
        Represents calibration function that translates certain physical parameter into another e.g. B field that can be
        produced by a magnet into the magnet current that is necessary to produce such field.
    
        Calibrations are based on measurements made on specific devices (e.g. on magnets) and stored in LSA database.
    
        Calibrations are typically used in :code:`ValueGenerator`s and :code:`MakeRule`s when calculating values of certain
        parameters out of other parameters e.g. when translating magnetic field (B) to magnet current (I).
    """
    def getCalibrationFunctionByType(self, calibrationFunctionTypes: 'CalibrationFunctionTypes') -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Retrieves a function of the specified calibration function type for the current calibration.
        
            Parameters:
                calibrationFunctionType (:class:`~cern.lsa.domain.optics.CalibrationFunctionTypes`): the type of the calibration function that is needed (B_FIELD, SLOPE etc.)
        
            Returns:
                The function for the requested calibration function type or :code:`null` if it does not exist.
        
        
        """
        ...
    def getCalibrationFunctionMap(self) -> java.util.Map['CalibrationFunctionTypes', cern.accsoft.commons.value.ImmutableDiscreteFunction]: ...
    def getCreationDate(self) -> java.util.Date:
        """
            Returns the creation date of this calibration.
        
            Returns:
                the creation date of this calibration.
        
        
        """
        ...
    def getFidelModelId(self) -> int:
        """
            get the Fidel model ID
        
            Returns:
        
        
        """
        ...

class CalibrationException(java.lang.Exception):
    """
    public class CalibrationException extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`
    
        Exception to be used for calibration curves generation and model handling.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...

class CalibrationFunctionTypes(java.lang.Enum['CalibrationFunctionTypes']):
    """
    public enum CalibrationFunctionTypes extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.optics.CalibrationFunctionTypes`>
    
        Enumeration with possible calibration function types.
    
        Also see:
            :class:`~cern.lsa.domain.optics.Calibration`
    """
    B_FIELD: typing.ClassVar['CalibrationFunctionTypes'] = ...
    BL_FIELD: typing.ClassVar['CalibrationFunctionTypes'] = ...
    SLOPE: typing.ClassVar['CalibrationFunctionTypes'] = ...
    CURRENT2INDUCTANCE: typing.ClassVar['CalibrationFunctionTypes'] = ...
    CURRENT2COUPLING_INDUCTANCE: typing.ClassVar['CalibrationFunctionTypes'] = ...
    MAG_INTFIELD2CURRENT: typing.ClassVar['CalibrationFunctionTypes'] = ...
    EL_INTFIELD2VOLTAGE: typing.ClassVar['CalibrationFunctionTypes'] = ...
    LOCAL_FIELD2CURRENT: typing.ClassVar['CalibrationFunctionTypes'] = ...
    CURRENT2HALL_VOLTAGE: typing.ClassVar['CalibrationFunctionTypes'] = ...
    B_FIELD_RDOWN: typing.ClassVar['CalibrationFunctionTypes'] = ...
    MAG_INTFIELD2VOLTAGE: typing.ClassVar['CalibrationFunctionTypes'] = ...
    BL_FIELD_RDOWN: typing.ClassVar['CalibrationFunctionTypes'] = ...
    def getFunctionTypeName(self) -> str:
        """
            Returns corresponding function type name that is stored in CALIBRATION_FUNCTION_TYPES database table.
        
            Returns:
                name of function type stored in database
        
        
        """
        ...
    @staticmethod
    def getTypeForName(string: str) -> 'CalibrationFunctionTypes':
        """
            Returns calibration type for given :meth:`~cern.lsa.domain.optics.CalibrationFunctionTypes.getFunctionTypeName`.
        
            Parameters:
                calibrationFunctionTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the calibration function type
        
            Returns:
                the corresponding enum value or :code:`null`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CalibrationFunctionTypes':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['CalibrationFunctionTypes']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (CalibrationFunctionTypes c : CalibrationFunctionTypes.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ChromaticModel(cern.accsoft.commons.util.Named):
    """
    public interface ChromaticModel extends cern.accsoft.commons.util.Named
    
        Represents a model of chromaticity i.e. a set of physical attributes that allow to calculate chromatic effects and
        correct them.
    
        For details about specific attributes of this entity, please see with Lasse Normann.
    
        Note: At the moment this class is not used however we keep it (together with DB table) for a while in case SPS guys
        decide to use it again for generation of Chromaticity settings.
    """
    def getAlphaH(self) -> float: ...
    def getAlphaV(self) -> float: ...
    def getBetaH(self) -> float: ...
    def getBetaV(self) -> float: ...
    def getBsedd(self) -> float: ...
    def getBsrem(self) -> float: ...
    def getChcon(self) -> float: ...
    def getChedd(self) -> float: ...
    def getChrem(self) -> float: ...
    def getCvcon(self) -> float: ...
    def getCvedd(self) -> float: ...
    def getCvrem(self) -> float: ...
    def getGammaH(self) -> float: ...
    def getGammaV(self) -> float: ...
    def getLatticeChromaH(self) -> float: ...
    def getLatticeChromaV(self) -> float: ...

class ElementBase(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface ElementBase extends cern.accsoft.commons.util.Named, :class:`~cern.lsa.domain.commons.IdentifiedEntity`
    
        Represents a magnet element like bending magnet, quadrupole or sextupole, with it's position in the accelerator and
        length.
    
        Certain elements (e.g. quadrupoles) can have associated :meth:`~cern.lsa.domain.optics.ElementBase.getPlane` (e.g.
        HORIZONTAL or VERTICAL).
    
        Elements are defined in :code:`ELEMENTS` table in the database.
    """
    def getAcceleratorZone(self) -> cern.accsoft.commons.domain.zones.AcceleratorZone:
        """
            Returns the name of accelerator zone to which this element belongs to.
        
            Returns:
                the name of accelerator zone to which this element belongs to.
        
        
        """
        ...
    def getLength(self) -> float:
        """
            Returns the length of this element. Greg: What is the unit here?
        
            Returns:
                the length of this element
        
        
        """
        ...
    def getMadParent(self) -> str:
        """
            Returns the parent as defined in the MAD file of this element e.g. MB, MCS, MCD
        
            Returns:
                the parent as defined in the MAD file of this element.
        
        
        """
        ...
    def getPlane(self) -> 'ElementPlane':
        """
        
            Returns:
                the plane of this element
        
        
        """
        ...
    def getPosition(self) -> float:
        """
            Returns the position of this element. Greg: What is the unit here? what means the position?
        
            Returns:
                the position of this element
        
        
        """
        ...
    def getType(self) -> 'ElementType':
        """
            Returns the type of this element e.g. SBEND, QUADRUPOLE, VMONITOR, HKICKER.
        
            Returns:
                the type of this element
        
        
        """
        ...

class ElementPlane(java.lang.Enum['ElementPlane'], cern.accsoft.commons.util.Named):
    """
    public enum ElementPlane extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.optics.ElementPlane`> implements cern.accsoft.commons.util.Named
    
        Element planes.
    """
    VERTICAL: typing.ClassVar['ElementPlane'] = ...
    HORIZONTAL: typing.ClassVar['ElementPlane'] = ...
    BOTH: typing.ClassVar['ElementPlane'] = ...
    NONE: typing.ClassVar['ElementPlane'] = ...
    @staticmethod
    def findPlaneBySymbol(char: str) -> 'ElementPlane':
        """
        
            Parameters:
                symbol (char): 
            Returns:
                :class:`~cern.lsa.domain.optics.ElementPlane` corresponding to the symbol
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def getSymbol(self) -> str:
        """
        
            Returns:
                the symbol representing the plane.
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ElementPlane':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['ElementPlane']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ElementPlane c : ElementPlane.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ElementType(java.lang.Enum['ElementType'], cern.accsoft.commons.util.Named):
    """
    public enum ElementType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.optics.ElementType`> implements cern.accsoft.commons.util.Named
    
        Magnetic element types.
    """
    DRIFT: typing.ClassVar['ElementType'] = ...
    HKICKER: typing.ClassVar['ElementType'] = ...
    HMONITOR: typing.ClassVar['ElementType'] = ...
    INSTRUMENT: typing.ClassVar['ElementType'] = ...
    IP: typing.ClassVar['ElementType'] = ...
    KICKER: typing.ClassVar['ElementType'] = ...
    MARKER: typing.ClassVar['ElementType'] = ...
    PLACEHOLDER: typing.ClassVar['ElementType'] = ...
    MONITOR: typing.ClassVar['ElementType'] = ...
    MULTIPOLE: typing.ClassVar['ElementType'] = ...
    OCTUPOLE: typing.ClassVar['ElementType'] = ...
    QUADRUPOLE: typing.ClassVar['ElementType'] = ...
    RBEND: typing.ClassVar['ElementType'] = ...
    RCOLLIMATOR: typing.ClassVar['ElementType'] = ...
    RFCAVITY: typing.ClassVar['ElementType'] = ...
    SBEND: typing.ClassVar['ElementType'] = ...
    SEXTUPOLE: typing.ClassVar['ElementType'] = ...
    SOLENOID: typing.ClassVar['ElementType'] = ...
    TKICKER: typing.ClassVar['ElementType'] = ...
    VKICKER: typing.ClassVar['ElementType'] = ...
    VMONITOR: typing.ClassVar['ElementType'] = ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ElementType':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['ElementType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ElementType c : ElementType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ElementsRequest:
    """
    public interface ElementsRequest
    
        Describes criteria when searching for LSA elements. This object should be created using
        :class:`~cern.lsa.domain.optics.factory.ElementsRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> cern.lsa.domain.optics.factory.ElementsRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.optics.ElementsRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def excludeObsolete(self) -> bool:
        """
            return :code:`true` if the Obsolete elements have to be excluded from the request
        
            Returns:
        
        
        """
        ...
    def getAcceleratorZone(self) -> cern.accsoft.commons.domain.zones.AcceleratorZone:
        """
        
            Returns:
                accelerator zone that the elements should belong to
        
        
        """
        ...
    def getElementNames(self) -> java.util.Set[str]: ...
    def getLogicalHwNames(self) -> java.util.Set[str]: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
        
            Returns:
                particle transfer that the elements should belong to
        
        
        """
        ...
    def getSteering(self) -> bool:
        """
            Returns :code:`true` if only steering elements are requested. Steering elements are monitors and correctors including
            :meth:`~cern.lsa.domain.optics.ElementType.MONITOR`, :meth:`~cern.lsa.domain.optics.ElementType.HMONITOR`,
            :meth:`~cern.lsa.domain.optics.ElementType.VMONITOR`, :meth:`~cern.lsa.domain.optics.ElementType.HKICKER`,
            :meth:`~cern.lsa.domain.optics.ElementType.VKICKER` that have a plane defined.
        
            Returns:
                :code:`true` if only steering elements are requested
        
        
        """
        ...
    def getTypes(self) -> java.util.Set[ElementType]: ...

class LogicalHardware(cern.lsa.domain.devices.Device):
    """
    public interface LogicalHardware extends :class:`~cern.lsa.domain.devices.Device`
    
        A :code:`LogicalHardware` is a specialized :class:`~cern.lsa.domain.devices.Device` that holds additional information
        specific to either :class:`~cern.lsa.domain.devices.DeviceType`s with a meta type of 'L' (logic) or other
        :code:`Devices` for which the information contained within this class is required.
    
        Also see:
            :class:`~cern.lsa.domain.devices.Device`, :class:`~cern.lsa.domain.devices.DeviceType`,
            :meth:`~cern.lsa.domain.devices.DeviceType.getMetaType`
    """
    def getCalibrationName(self) -> str: ...
    def getCalibrationSign(self) -> int: ...
    def getLinkRuleName(self) -> str: ...
    def getLtot(self) -> float: ...
    def getMadStrengthName(self) -> str: ...
    def getMadStrengthType(self) -> str: ...
    def getMagnetType(self) -> str: ...
    def getMagneticLength(self) -> float: ...
    def getOpTemp(self) -> float: ...
    def getPlane(self) -> ElementPlane: ...
    def getRtot(self) -> float: ...
    def getRtotMeasured(self) -> float: ...
    def getTau(self) -> float: ...

class MeasuredTwiss:
    """
    public interface MeasuredTwiss
    
        Represents the twiss parameters recorded during a measurement. The static twiss parameters are provided by the
        associated twiss object, :class:`~cern.lsa.domain.optics.Twiss`.
    
        A twiss measurement is identified by :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getTwiss`,
        :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getEnergy` and :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getTimestamp`,
        which are guaranteed to be non-null. As for the other parameters, they can hold a :code:`Double.NaN` value, which means
        there is no measurement for it.
    """
    def getAlfxError(self) -> float: ...
    def getAlfxMeas(self) -> float: ...
    def getAlfyError(self) -> float: ...
    def getAlfyMeas(self) -> float: ...
    def getBetxError(self) -> float: ...
    def getBetxMeas(self) -> float: ...
    def getBetyError(self) -> float: ...
    def getBetyMeas(self) -> float: ...
    def getDxError(self) -> float: ...
    def getDxMeas(self) -> float: ...
    def getDyError(self) -> float: ...
    def getDyMeas(self) -> float: ...
    def getEnergy(self) -> float:
        """
            Returns the energy at which the measurement was taken.
        
            Returns:
                energy of the measurement
        
        
        """
        ...
    def getMuxError(self) -> float: ...
    def getMuxMeas(self) -> float: ...
    def getMuyError(self) -> float: ...
    def getMuyMeas(self) -> float: ...
    def getTimestamp(self) -> java.util.Date:
        """
            Returns the UTC timestamp at which the measurement took place.
        
            Returns:
                UTC timestamp of the measurement
        
        
        """
        ...
    def getTwiss(self) -> 'Twiss':
        """
            Returns the twiss object associated to this measurement.
        
            Returns:
                corresponding twiss paramters
        
        
        """
        ...

class Optic(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface Optic extends cern.accsoft.commons.util.Named, :class:`~cern.lsa.domain.commons.IdentifiedEntity`
    """
    def getBaseStrengthFile(self) -> str:
        """
            the madx file used as base for the optic strengths
        
            Returns:
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            the date the optic had been entered in LSA database
        
            Returns:
        
        
        """
        ...
    def getModelUri(self) -> str:
        """
        
            Returns:
                the URI which can be passed to JMad to retrieve the model used to generate this optic
        
        
        """
        ...
    def getOpticParameters(self) -> java.util.Map[str, float]: ...
    def getOpticStrengths(self) -> java.util.List['OpticStrength']: ...
    def getOverrideStrengthFile(self) -> str:
        """
            additional file for optic strength
        
            Returns:
        
        
        """
        ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getParameterValue(self, string: str) -> float:
        """
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                the value of the parameter of the given name
        
        
        """
        ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
        
            Returns:
                the particle transfer the optic applies for
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Set the name of the optic
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...

class OpticStrength:
    """
    public interface OpticStrength
    
        Magnet strength for a given logical hardware and optic.
    """
    @staticmethod
    def builder() -> cern.lsa.domain.optics.spi.OpticStrengthImpl.Builder: ...
    def getBeam(self) -> str:
        """
            Returns the Beam or :code:`null` if it is not defined.
        
            Returns:
                the Beam or :code:`null` if it is not defined.
        
        
        """
        ...
    def getLogicalHardwareName(self) -> str:
        """
            Returns the name of a logical hardware this optic strength belongs to.
        
            Returns:
                the name of a logical hardware this optic strength belongs to.
        
        
        """
        ...
    def getStrength(self) -> float:
        """
        
            Returns:
                strength or 0 if not defined
        
        
        """
        ...
    def getStrengthL(self) -> float:
        """
        
            Returns:
                strengthL or 0 if not defined
        
        
        """
        ...

class Optics(java.io.Serializable):
    """
    public class Optics extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Optics store information about many optics and their strengh. It offers method to get directly the various pieces of
        information hold by the optics.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, set: java.util.Set[Optic]): ...
    def getBeam(self, stringArray: typing.List[str], string2: str) -> typing.List[str]:
        """
            Each optic may have from zero to many OpticStrengths. Each OpticStrength is for a given logical hardware. This method
            returns the value of the parameter beam of the OpticStrength for the given logical hardware and for the given array of
            opticNames. In the returned array, the value at index i is the value of beam for the optic at index i in the given array
            of optic names and the given logicalHardware. If one optic has no strength defined for the given logicalHardware, null
            will be found in the returned array of values at the corresponding index.
        
            Parameters:
                opticNames (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the array of optic names to retrieve the strength parameter value for
                logicalHardwareName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the logical hardware to get the value for
        
            Returns:
                the array of value for the given optics and strength parameter for the given logical hardware.
        
        
        """
        ...
    def getOptic(self, string: str) -> Optic:
        """
            Returns the optics of given name or null if that optic if not found
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the optic to retrieve
        
            Returns:
                the optics of given name or null if that optic if not found
        
        
        """
        ...
    def getOpticNames(self) -> java.util.Set[str]: ...
    def getOpticParameterValues(self, list: java.util.List[str], string: str) -> typing.List[float]: ...
    def getStrength(self, list: java.util.List[str], string: str) -> typing.List[float]: ...
    def getStrengthL(self, list: java.util.List[str], string: str) -> typing.List[float]: ...
    def isParameterDefined(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]], string: str) -> bool: ...
    def size(self) -> int:
        """
            Returns the number of optics stored in this object
        
            Returns:
                the number of optics stored in this object
        
        
        """
        ...

class OpticsRequest:
    """
    public interface OpticsRequest
    
        Describes criteria when searching for optics. This object should be created using
        :class:`~cern.lsa.domain.optics.factory.OpticsRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> cern.lsa.domain.optics.factory.OpticsRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.optics.OpticsRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                accelerator the optic should belong to
        
        
        """
        ...
    def getBeamProcessTypeNames(self) -> java.util.Set[str]: ...
    def getOpticIds(self) -> java.util.Set[int]: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
        
            Returns:
                particle transfer the optic should belong to
        
            Also see:
                :meth:`~cern.lsa.domain.optics.Optic.getParticleTransfer`
        
        
        """
        ...

class OpticsTable(java.lang.Iterable['OpticsTableItem']):
    """
    public interface OpticsTable extends `Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<:class:`~cern.lsa.domain.optics.OpticsTableItem`>
    
        Represents a table of optic names at specific times within the corresponding beam process type.
    """
    def getBeamProcessTypeName(self) -> str:
        """
            Returns name of the beam process type for which the optics table is defined.
        
            Note that in case when optics are defined per beam process rather than per beam process type, this method returns name
            of the corresponding beam process type.
        
            Returns:
                name of the beam process type
        
        
        """
        ...
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def getLength(self) -> int:
        """
            Returns the length of the table in ms, what is effectively the length of the beam process this table is for.
        
            Returns:
                length of the table in ms
        
        
        """
        ...
    def getOpticNames(self) -> java.util.List[str]: ...
    def getOpticsTableItemByIndex(self, int: int) -> 'OpticsTableItem':
        """
            Returns :class:`~cern.lsa.domain.optics.OpticsTableItem` at specified index.
        
            Parameters:
                index (int): index of the :class:`~cern.lsa.domain.optics.OpticsTableItem` to be returned: from 0 to
                    :meth:`~cern.lsa.domain.optics.OpticsTable.getSize` - 1
        
            Returns:
                :class:`~cern.lsa.domain.optics.OpticsTableItem` at specified index
        
            Raises:
                : if the index is outside the range from 0 to :meth:`~cern.lsa.domain.optics.OpticsTable.getSize` - 1
        
        
        """
        ...
    def getOpticsTableItemByTime(self, double: float) -> 'OpticsTableItem':
        """
            Returns the :class:`~cern.lsa.domain.optics.OpticsTableItem` at the given time. The value returned is the
            :class:`~cern.lsa.domain.optics.OpticsTableItem` with the time closest to the given time and that is equal or inferior
            to the given time.
        
            The :class:`~cern.lsa.domain.optics.OpticsTableItem` is valid from the time it is defined till the next
            :class:`~cern.lsa.domain.optics.OpticsTableItem` or till the end of the beam process type. For instance if the last
            :class:`~cern.lsa.domain.optics.OpticsTableItem` is defined at time 1000ms and the length of beam process type is
            1200ms, then for any time from range [1000, 1200] the method returns this last
            :class:`~cern.lsa.domain.optics.OpticsTableItem` 1000ms.
        
            Parameters:
                timeInBeamProcessType (double): time within the beam process (type) for which :class:`~cern.lsa.domain.optics.OpticsTableItem` should be returned. Note
                    that in accelerators where we use a single beam process that covers the whole cycle - this is equivalent to the time
                    within the stand alone context (cycle).
        
            Returns:
                :class:`~cern.lsa.domain.optics.OpticsTableItem` for given time
        
            Raises:
                : if the specified time is negative or is greater than the length of the corresponding beam process type
        
        
        """
        ...
    def getOpticsTableItems(self) -> java.util.List['OpticsTableItem']: ...
    def getSize(self) -> int:
        """
            Returns number elements in the optics table.
        
            Returns:
                size of the optics table
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Returns :code:`true` if the table doesn't contain any optic.
        
            Returns:
                :code:`true` if the table doesn't contain any optic
        
        
        """
        ...
    def isValid(self) -> bool:
        """
            Returns :code:`true` if the optics table is defined and is valid.
        
            The optic table might be not valid e.g. if the time coordinates are not strictly ascending or if the defined optic
            doesn't exist. In such case :meth:`~cern.lsa.domain.optics.OpticsTable.getErrorMessages` method can be used to get
            descriptions of the errors.
        
            Returns:
                :code:`true` if this optics table is valid, :code:`false` if it's not.
        
        
        """
        ...

class OpticsTableItem:
    """
    public interface OpticsTableItem
    
        Represents a single point of an optic function defined for a beam process type.
    
        Also see:
            :class:`~cern.lsa.domain.optics.OpticsTable`
    """
    def clone(self) -> 'OpticsTableItem':
        """
            Returns copy of this OpticsTableItem.
        
            Returns:
                copy of this OpticsTableItem.
        
        
        """
        ...
    def getBeamProcessTypeName(self) -> str:
        """
            Returns name of the beam process type that this optics item belongs to.
        
            Returns:
                name of the beam process type that this optics item belongs to.
        
        
        """
        ...
    def getEnergy(self) -> float:
        """
            Returns energy of this optics item.
        
            Returns:
                energy of this optics item.
        
            Also see:
                :meth:`~cern.lsa.domain.optics.OpticsTableItem.getTime`
        
        
        """
        ...
    def getOpticId(self) -> int:
        """
            Returns ID of related optic.
        
            Returns:
                ID of related optic.
        
        
        """
        ...
    def getOpticName(self) -> str:
        """
            Returns name of related optic.
        
            Returns:
                name of related optic.
        
        
        """
        ...
    def getTime(self) -> int:
        """
            Returns time (in the unit consistent with the accelerator - [s] for LHC, [ms] for all others) of this optics item within
            the beam process type.
        
            Returns:
                time (in the unit consistent with the accelerator - [s] for LHC, [ms] for all others) of this optics item within the
                beam process type.
        
        
        """
        ...

class OpticsTables:
    """
    public class OpticsTables extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods dealing with :class:`~cern.lsa.domain.optics.OpticsTable` instances.
    """
    def __init__(self): ...
    @staticmethod
    def getEnergyFunction(opticsTable: OpticsTable) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Returns the energy as a function of time for the given :class:`~cern.lsa.domain.optics.OpticsTable`.
        
            Parameters:
                opticsTable (:class:`~cern.lsa.domain.optics.OpticsTable`): 
            Returns:
                energy as a function of time
        
        
        """
        ...
    @staticmethod
    def getOpticTimesCoordinates(opticsTable: OpticsTable) -> typing.List[float]:
        """
            Returns an array of optic times from the optics table.
        
            Parameters:
                opticsTable (:class:`~cern.lsa.domain.optics.OpticsTable`): 
            Returns:
                array of optic times from the optics table
        
        
        """
        ...

class OpticsTablesRequest:
    """
    @Immutable public interface OpticsTablesRequest
    
        Request object to search for OpticsTables Warning: one and only one criterion must be specified
    """
    @staticmethod
    def builder() -> 'DefaultOpticsTablesRequest.Builder': ...
    @staticmethod
    def byBeamProcess(beamProcess: cern.lsa.domain.settings.BeamProcess) -> 'OpticsTablesRequest': ...
    @staticmethod
    def byBeamProcessType(beamProcessType: cern.lsa.domain.settings.type.BeamProcessType) -> 'OpticsTablesRequest': ...
    @staticmethod
    def byBeamProcessTypeName(string: str) -> 'OpticsTablesRequest': ...
    @staticmethod
    def byBeamProcessTypeNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'OpticsTablesRequest': ...
    @staticmethod
    def byBeamProcessTypes(collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.type.BeamProcessType], typing.Sequence[cern.lsa.domain.settings.type.BeamProcessType]]) -> 'OpticsTablesRequest': ...
    @staticmethod
    def byBeamProcesses(collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.BeamProcess], typing.Sequence[cern.lsa.domain.settings.BeamProcess]]) -> 'OpticsTablesRequest': ...
    @staticmethod
    def byOptic(optic: Optic) -> 'OpticsTablesRequest': ...
    @staticmethod
    def byOptics(collection: typing.Union[java.util.Collection[Optic], typing.Sequence[Optic]]) -> 'OpticsTablesRequest': ...
    @staticmethod
    def byStandAloneContext(standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'OpticsTablesRequest': ...
    @staticmethod
    def byStandAloneContexts(collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.StandAloneContext], typing.Sequence[cern.lsa.domain.settings.StandAloneContext]]) -> 'OpticsTablesRequest': ...
    def check(self) -> None: ...
    def getBeamProcessTypeNames(self) -> java.util.Set[str]: ...
    def getOptics(self) -> java.util.Set[Optic]: ...
    def getStandAloneContexts(self) -> java.util.Set[cern.lsa.domain.settings.StandAloneContext]: ...

class PowerConverterInfo(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface PowerConverterInfo extends cern.accsoft.commons.util.Named, :class:`~cern.lsa.domain.commons.IdentifiedEntity`
    
        Provide information about power converter.
    """
    def getAccelerationLimit(self) -> float:
        """
        
            Returns:
                acceleration limit
        
        
        """
        ...
    def getAdvance(self) -> float:
        """
        
            Returns:
        
        
        """
        ...
    def getBeam(self) -> str: ...
    def getDecelerationLimit(self) -> float:
        """
        
            Returns:
                deceleration limit
        
        
        """
        ...
    def getDidtMax(self) -> float:
        """
        
            Returns:
        
        
        """
        ...
    def getDidtMin(self) -> float:
        """
        
            Returns:
        
        
        """
        ...
    def getIMinOp(self) -> float:
        """
        
            Returns:
        
        
        """
        ...
    def getINom(self) -> float:
        """
        
            Returns:
        
        
        """
        ...
    def getIPNo(self) -> float:
        """
        
            Returns:
                the iPNO
        
        
        """
        ...
    def getIUlt(self) -> float:
        """
        
            Returns:
                the iUlt
        
        
        """
        ...
    def getLastRefDatabaseUpdate(self) -> java.util.Date:
        """
        
            Returns:
        
        
        """
        ...
    def getPoweringSubsector(self) -> str:
        """
        
            Returns:
        
        
        """
        ...
    def isPolaritySwitch(self) -> bool:
        """
        
            Returns:
                the polaritySwitch
        
        
        """
        ...

class PreCyclingPrescription:
    """
    public interface PreCyclingPrescription
    """
    def getAttributeValue(self, string: str) -> float: ...
    def getMagnetType(self) -> str: ...
    def getPrecyclingPrescriptionMode(self) -> str: ...
    def getPrecyclingPrescriptionType(self) -> str: ...

class RFCalibration(cern.accsoft.commons.util.Named):
    """
    public interface RFCalibration extends cern.accsoft.commons.util.Named
    
        Represents a calibration function for an RF device.
    """
    def getCavityQ(self, double: float) -> float:
        """
            Returns the interpolated cavityQ for the given couplerPosition
        
            Parameters:
                couplerPos (double): coupler position
        
            Returns:
                a double representing the interpolated cavityQ
        
        
        """
        ...
    def getCavityQ2CouplerPosFunction(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Returns the function current(cavityq) as defined by the CalibrationCurve items. The returned function can be used to
            interpolate the value of the current for the given value of bfield
        
            Returns:
                the function current(cavityq) as defined by the CalibrationCurve items.
        
        
        """
        ...
    def getCouplerPos(self, double: float) -> float:
        """
            Returns the interpolated couplerPos for given cavityQ in the current RFCalibration.
        
            Parameters:
                cavityQ (double): 
            Returns:
                a double representing the interpolated coupler position.
        
            Raises:
                : if the given cavityQ doesn't permit to interpolate the couplerPosition
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Returns the creation date of this calibration.
        
            Returns:
                the creation date of this calibration.
        
        
        """
        ...
    def getDeviceName(self) -> str:
        """
            Returns the device name associated to this calibration.
        
            Returns:
                the name of the device
        
        
        """
        ...

class Twiss:
    """
    public interface Twiss
    
        Represents a set of twiss parameters for a given optic, element and beam.
    """
    def getAlfx(self) -> float:
        """
        
            Returns:
                the value of the correlation function Alfa x function at the element position
        
        
        """
        ...
    def getAlfy(self) -> float:
        """
        
            Returns:
                the value of the correlation function Alfa y function at the element position
        
        
        """
        ...
    def getBeam(self) -> cern.accsoft.commons.domain.beams.Beam:
        """
        
            Returns:
                the beam that this twiss is defined for
        
        
        """
        ...
    def getBetx(self) -> float:
        """
        
            Returns:
                the value of the amplitude function Betax at the element position
        
        
        """
        ...
    def getBety(self) -> float:
        """
        
            Returns:
                the value of the amplitude function Betay at the element position
        
        
        """
        ...
    def getDpx(self) -> float:
        """
        
            Returns:
                the value of the dispersion function Dpx = (delta px / delta PT) / ps at the element position with p= momentum and PT =
                Energy difference, divided by the reference momentum times the velocity of light
        
        
        """
        ...
    def getDpy(self) -> float:
        """
        
            Returns:
                the value of the dispersion function Dpy = (delta py / delta PT) / ps at the element position with p= momentum and PT =
                Energy difference, divided by the reference momentum times the velocity of light
        
        
        """
        ...
    def getDx(self) -> float:
        """
        
            Returns:
                the value of the dispersion function Dx = delta x/PT at the element position PT = Energy difference, divided by the
                reference momentum times the velocity of light
        
        
        """
        ...
    def getDy(self) -> float:
        """
        
            Returns:
                the value of the dispersion function Dy = delta y/PT at the element position PT = Energy difference, divided by the
                reference momentum times the velocity of light
        
        
        """
        ...
    def getElement(self) -> ElementBase:
        """
            Returns element that this twiss is defined for.
        
            Returns:
                element that this twiss is defined for
        
        
        """
        ...
    def getHkick(self) -> float:
        """
        
            Returns:
                the horizontal kick strength of orbit deflectors
        
        
        """
        ...
    def getK0l(self) -> float:
        """
        
            Returns:
                the strength at a dipole multiplied by the element length
        
        
        """
        ...
    def getK1Sl(self) -> float:
        """
        
            Returns:
                the strength at a sqew quadrupole element multiplied by the element length
        
        
        """
        ...
    def getK1l(self) -> float:
        """
        
            Returns:
                the strength at a quadrupole multiplied by the element length
        
        
        """
        ...
    def getK2Sl(self) -> float:
        """
        
            Returns:
                the strength at a sqew sextupole element multiplied by the element length
        
        
        """
        ...
    def getK2l(self) -> float:
        """
        
            Returns:
                the strength at sextupole multiplied by the element length
        
        
        """
        ...
    def getK3Sl(self) -> float:
        """
        
            Returns:
                the strength at a sqew octupole element multiplied by the element length
        
        
        """
        ...
    def getK3l(self) -> float:
        """
        
            Returns:
                the strength at a octupole element multiplied by the element length
        
        
        """
        ...
    def getK4l(self) -> float:
        """
        
            Returns:
                the strength at decapole elements
        
        
        """
        ...
    def getK5l(self) -> float:
        """
        
            Returns:
                the strength at duodecapole elements
        
        
        """
        ...
    def getMux(self) -> float:
        """
        
            Returns:
                the value of the horizontal phase function mux at the element position
        
        
        """
        ...
    def getMuy(self) -> float:
        """
        
            Returns:
                the value of the vertical phase function muy at the element position
        
        
        """
        ...
    def getOpticName(self) -> str:
        """
            Returns name of optic that this twiss is defined for.
        
            Returns:
                name of optic that this twiss is defined for
        
        
        """
        ...
    def getPx(self) -> float:
        """
        
            Returns:
                the value of the momentum px of the orbit referred to the ideal orbit, divided by the reference momentum, at the element
                position
        
        
        """
        ...
    def getPy(self) -> float:
        """
        
            Returns:
                the value of the momentum py of the orbit referred to the ideal orbit, divided by the reference momentum, at the element
                position
        
        
        """
        ...
    def getVkick(self) -> float:
        """
        
            Returns:
                the vertical kick strength of orbit deflectors
        
        
        """
        ...
    def getX(self) -> float:
        """
        
            Returns:
                the value of the Horizontal position x of the orbit, referred to the ideal orbit at the element longitudinal position
        
        
        """
        ...
    def getY(self) -> float:
        """
        
            Returns:
                the value of the vertical position y of the orbit, referred to the ideal orbit at the element longitudinal position
        
        
        """
        ...
    def updateOpticName(self, string: str) -> None:
        """
            This method updates the name of the optic the twiss is associated with
        
            Parameters:
                newOpticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...

class TwissFilter(cern.accsoft.commons.util.Filters.Filter[Twiss]):
    """
    public class TwissFilter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.optics.Twiss`>
    
        Simple :class:`~cern.lsa.domain.optics.Twiss` filter.
    """
    def __init__(self): ...
    def accepts(self, twiss: Twiss) -> bool:
        """
        
            Specified by:
                :code:`accepts` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
        
        """
        ...
    @staticmethod
    def beam(beam: cern.accsoft.commons.domain.beams.Beam) -> 'TwissFilter':
        """
        
            Parameters:
                beam (cern.accsoft.commons.domain.beams.Beam): 
            Returns:
                the filter
        
        
        """
        ...
    @staticmethod
    def elementTypeIn(collection: typing.Union[java.util.Collection[ElementType], typing.Sequence[ElementType]]) -> 'TwissFilter': ...
    def setBeam(self, beam: cern.accsoft.commons.domain.beams.Beam) -> 'TwissFilter':
        """
        
            Parameters:
                beam (cern.accsoft.commons.domain.beams.Beam): 
            Returns:
                this instance for chaining
        
        
        """
        ...
    def setElementTypes(self, collection: typing.Union[java.util.Collection[ElementType], typing.Sequence[ElementType]]) -> 'TwissFilter': ...

class TwissHelper:
    """
    public final class TwissHelper extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Helper methods to read information out of twiss and twiss measurements.
    """
    def __init__(self): ...
    @staticmethod
    def mapByDate(collection: typing.Union[java.util.Collection[MeasuredTwiss], typing.Sequence[MeasuredTwiss]]) -> java.util.Map[java.util.Date, java.util.Set[MeasuredTwiss]]: ...
    @staticmethod
    def mapByEnergy(collection: typing.Union[java.util.Collection[MeasuredTwiss], typing.Sequence[MeasuredTwiss]]) -> java.util.Map[float, java.util.Set[MeasuredTwiss]]: ...
    @staticmethod
    def mapByOpticName(collection: typing.Union[java.util.Collection[MeasuredTwiss], typing.Sequence[MeasuredTwiss]]) -> java.util.Map[str, java.util.Set[MeasuredTwiss]]: ...
    @staticmethod
    def mapByTwiss(collection: typing.Union[java.util.Collection[MeasuredTwiss], typing.Sequence[MeasuredTwiss]]) -> java.util.Map[Twiss, java.util.Set[MeasuredTwiss]]: ...

class Twisses:
    """
    public class Twisses extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods for :class:`~cern.lsa.domain.optics.Twiss` objects.
    """
    BEAMS: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.optics.Twiss`, cern.accsoft.commons.domain.beams.Beam> BEAMS
    
        Twiss mapper to beam name
    
    """
    ELEMENT_TYPES: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.optics.Twiss`, :class:`~cern.lsa.domain.optics.ElementType`> ELEMENT_TYPES
    
        Twiss mapper to element type
    
    """
    ELEMENT_NAMES: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.optics.Twiss`, `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`> ELEMENT_NAMES
    
        Twiss mapper to element name
    
    """
    def __init__(self): ...
    @staticmethod
    def getBeams(collection: typing.Union[java.util.Collection[Twiss], typing.Sequence[Twiss]]) -> java.util.Set[cern.accsoft.commons.domain.beams.Beam]: ...
    @staticmethod
    def getElementTypes(collection: typing.Union[java.util.Collection[Twiss], typing.Sequence[Twiss]]) -> java.util.Set[ElementType]: ...
    @staticmethod
    def toElementNamesMap(collection: typing.Union[java.util.Collection[Twiss], typing.Sequence[Twiss]]) -> java.util.Map[str, Twiss]: ...

class TwissesRequest:
    """
    public interface TwissesRequest
    
        Describes criteria when searching for LSA twisses. This object should be created using
        :class:`~cern.lsa.domain.optics.factory.TwissesRequestBuilder` and passed to appropriate finder method. *
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> cern.lsa.domain.optics.factory.TwissesRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.optics.TwissesRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getBeam(self) -> cern.accsoft.commons.domain.beams.Beam:
        """
        
            Returns:
                beam name
        
            Also see:
                :meth:`~cern.lsa.domain.optics.Twiss.getBeam`
        
        
        """
        ...
    def getElementNames(self) -> java.util.Set[str]: ...
    def getElementPositionRange(self) -> com.google.common.collect.Range[float]: ...
    def getElementTypes(self) -> java.util.Set[ElementType]: ...
    def getOpticName(self) -> str:
        """
        
            Returns:
                optic name
        
            Also see:
                :meth:`~cern.lsa.domain.optics.Twiss.getOpticName`
        
        
        """
        ...

class DefaultOpticsTablesRequest(OpticsTablesRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultOpticsTablesRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.optics.OpticsTablesRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.optics.OpticsTablesRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultOpticsTablesRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultOpticsTablesRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.optics.DefaultOpticsTablesRequest`.
        
            .. code-block: java
            
             DefaultOpticsTablesRequest.builder()
                .optics(Set<cern.lsa.domain.optics.Optic> | null) // nullable :meth:`~cern.lsa.domain.optics.OpticsTablesRequest.getOptics`
                .standAloneContexts(Set<cern.lsa.domain.settings.StandAloneContext> | null) // nullable :meth:`~cern.lsa.domain.optics.OpticsTablesRequest.getStandAloneContexts`
                .beamProcessTypeNames(Set<String> | null) // nullable :meth:`~cern.lsa.domain.optics.OpticsTablesRequest.getBeamProcessTypeNames`
                .build();
             
        
            Returns:
                A new DefaultOpticsTablesRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(opticsTablesRequest: OpticsTablesRequest) -> 'DefaultOpticsTablesRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.optics.OpticsTablesRequest` value. Uses accessors to get values
            to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.optics.OpticsTablesRequest`): The instance to copy
        
            Returns:
                A copied immutable OpticsTablesRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBeamProcessTypeNames(self) -> java.util.Set[str]: ...
    def getOptics(self) -> java.util.Set[Optic]: ...
    def getStandAloneContexts(self) -> java.util.Set[cern.lsa.domain.settings.StandAloneContext]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`optics`, :code:`standAloneContexts`, :code:`beamProcessTypeNames`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`OpticsTablesRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withBeamProcessTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultOpticsTablesRequest': ...
    @typing.overload
    def withBeamProcessTypeNames(self, stringArray: typing.List[str]) -> 'DefaultOpticsTablesRequest': ...
    @typing.overload
    def withOptics(self, opticArray: typing.List[Optic]) -> 'DefaultOpticsTablesRequest': ...
    @typing.overload
    def withOptics(self, iterable: java.lang.Iterable[Optic]) -> 'DefaultOpticsTablesRequest': ...
    @typing.overload
    def withStandAloneContexts(self, standAloneContextArray: typing.List[cern.lsa.domain.settings.StandAloneContext]) -> 'DefaultOpticsTablesRequest': ...
    @typing.overload
    def withStandAloneContexts(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.StandAloneContext]) -> 'DefaultOpticsTablesRequest': ...
    class Builder:
        def addAllBeamProcessTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultOpticsTablesRequest.Builder': ...
        def addAllOptics(self, iterable: java.lang.Iterable[Optic]) -> 'DefaultOpticsTablesRequest.Builder': ...
        def addAllStandAloneContexts(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.StandAloneContext]) -> 'DefaultOpticsTablesRequest.Builder': ...
        def addBeamProcessTypeName(self, string: str) -> 'DefaultOpticsTablesRequest.Builder': ...
        def addBeamProcessTypeNames(self, stringArray: typing.List[str]) -> 'DefaultOpticsTablesRequest.Builder': ...
        def addOptic(self, optic: Optic) -> 'DefaultOpticsTablesRequest.Builder': ...
        def addOptics(self, opticArray: typing.List[Optic]) -> 'DefaultOpticsTablesRequest.Builder': ...
        def addStandAloneContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'DefaultOpticsTablesRequest.Builder': ...
        def addStandAloneContexts(self, standAloneContextArray: typing.List[cern.lsa.domain.settings.StandAloneContext]) -> 'DefaultOpticsTablesRequest.Builder': ...
        def beamProcessTypeNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultOpticsTablesRequest.Builder': ...
        def build(self) -> 'DefaultOpticsTablesRequest': ...
        def optics(self, iterable: java.lang.Iterable[Optic]) -> 'DefaultOpticsTablesRequest.Builder': ...
        def standAloneContexts(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.StandAloneContext]) -> 'DefaultOpticsTablesRequest.Builder': ...

class Element(ElementBase):
    """
    public interface Element extends :class:`~cern.lsa.domain.optics.ElementBase`
    
        Element entity that contains information about logical devices associated with this element.
    """
    def getAffectedRings(self) -> java.util.Set[BeamEnum]: ...
    def getLogicalHwName(self) -> str: ...
    def getLogicalHwNames(self) -> java.util.Set[str]: ...
    def getSteeringPlane(self) -> ElementPlane:
        """
            get the steering plane to be used by the steering application for this element The steering plane value is
            ElementPlane.NONE when the element is not used by the steering
        
            Returns:
                ElementPlane
        
        
        """
        ...
    def isObsolete(self) -> bool:
        """
            get the obsolete status of the element
        
            Returns:
                true if the element is obsolete
        
        
        """
        ...
    def setAffectedRings(self, set: java.util.Set[BeamEnum]) -> None: ...
    def setLength(self, double: float) -> None:
        """
            set the length of the element
        
            Parameters:
                elementLength (double): 
        
        """
        ...
    def setObsolete(self, boolean: bool) -> None:
        """
            set whereas the element is obsolete
        
            Parameters:
                obsolete (boolean): : true if the element is obsolete
        
        
        """
        ...
    def setPlane(self, elementPlane: ElementPlane) -> None:
        """
            Set the plane the element is acting on
        
            Parameters:
                plane (:class:`~cern.lsa.domain.optics.ElementPlane`): 
        
        """
        ...
    def setPosition(self, double: float) -> None:
        """
            set the position of the element
        
            Parameters:
                elementPosition (double): 
        
        """
        ...
    def setSteeringPlane(self, elementPlane: ElementPlane) -> None:
        """
            Set the plane to be used by the steering for this element The steering plane is set to ElementPlane.NONE when this
            element is not used by the steering application
        
            Parameters:
                plane (:class:`~cern.lsa.domain.optics.ElementPlane`): : the ElementPlane enum
        
        
        """
        ...
    def setType(self, elementType: ElementType) -> None:
        """
            set the type of the element
        
            Parameters:
                type (:class:`~cern.lsa.domain.optics.ElementType`): 
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.optics")``.

    BeamEnum: typing.Type[BeamEnum]
    Calibration: typing.Type[Calibration]
    CalibrationException: typing.Type[CalibrationException]
    CalibrationFunctionTypes: typing.Type[CalibrationFunctionTypes]
    ChromaticModel: typing.Type[ChromaticModel]
    DefaultOpticsTablesRequest: typing.Type[DefaultOpticsTablesRequest]
    Element: typing.Type[Element]
    ElementBase: typing.Type[ElementBase]
    ElementPlane: typing.Type[ElementPlane]
    ElementType: typing.Type[ElementType]
    ElementsRequest: typing.Type[ElementsRequest]
    LogicalHardware: typing.Type[LogicalHardware]
    MeasuredTwiss: typing.Type[MeasuredTwiss]
    Optic: typing.Type[Optic]
    OpticStrength: typing.Type[OpticStrength]
    Optics: typing.Type[Optics]
    OpticsRequest: typing.Type[OpticsRequest]
    OpticsTable: typing.Type[OpticsTable]
    OpticsTableItem: typing.Type[OpticsTableItem]
    OpticsTables: typing.Type[OpticsTables]
    OpticsTablesRequest: typing.Type[OpticsTablesRequest]
    PowerConverterInfo: typing.Type[PowerConverterInfo]
    PreCyclingPrescription: typing.Type[PreCyclingPrescription]
    RFCalibration: typing.Type[RFCalibration]
    Twiss: typing.Type[Twiss]
    TwissFilter: typing.Type[TwissFilter]
    TwissHelper: typing.Type[TwissHelper]
    Twisses: typing.Type[Twisses]
    TwissesRequest: typing.Type[TwissesRequest]
    factory: cern.lsa.domain.optics.factory.__module_protocol__
    spi: cern.lsa.domain.optics.spi.__module_protocol__
