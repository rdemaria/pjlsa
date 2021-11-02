import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.beams
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.commons.spi
import cern.lsa.domain.devices
import cern.lsa.domain.devices.spi
import cern.lsa.domain.optics
import cern.lsa.domain.settings.type
import com.google.common.collect
import java.io
import java.lang
import java.util
import typing



class CalibrationImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.optics.Calibration], cern.lsa.domain.optics.Calibration, java.io.Serializable):
    """
    public class CalibrationImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.optics.Calibration`> implements :class:`~cern.lsa.domain.optics.Calibration`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.optics.Calibration` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def addCalibrationFunctionForType(self, calibrationFunctionTypes: cern.lsa.domain.optics.CalibrationFunctionTypes, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> None:
        """
            Adds a new calibration curve to this calibration.
        
            Parameters:
                calibrationFunctionType (:class:`~cern.lsa.domain.optics.CalibrationFunctionTypes`): The type of the curve/function that should be added.
                calibrationFunction (cern.accsoft.commons.value.ImmutableDiscreteFunction): The function to add.
        
        
        """
        ...
    def getCalibrationFunctionByType(self, calibrationFunctionTypes: cern.lsa.domain.optics.CalibrationFunctionTypes) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Calibration.getCalibrationFunctionByType`
            Retrieves a function of the specified calibration function type for the current calibration.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Calibration.getCalibrationFunctionByType`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.Calibration`
        
            Parameters:
                calibrationFunctionType (:class:`~cern.lsa.domain.optics.CalibrationFunctionTypes`): the type of the calibration function that is needed (B_FIELD, SLOPE etc.)
        
            Returns:
                The function for the requested calibration function type or :code:`null` if it does not exist.
        
        
        """
        ...
    def getCalibrationFunctionMap(self) -> java.util.Map[cern.lsa.domain.optics.CalibrationFunctionTypes, cern.accsoft.commons.value.ImmutableDiscreteFunction]: ...
    def getCreationDate(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Calibration.getCreationDate`
            Returns the creation date of this calibration.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Calibration.getCreationDate` in interface :class:`~cern.lsa.domain.optics.Calibration`
        
            Returns:
                the creation date of this calibration.
        
        
        """
        ...
    def getFidelModelId(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Calibration.getFidelModelId`
            get the Fidel model ID
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Calibration.getFidelModelId` in interface :class:`~cern.lsa.domain.optics.Calibration`
        
            Returns:
        
        
        """
        ...
    def setCreationDate(self, date: java.util.Date) -> None:
        """
            Sets the :code:`creationDate` of this calibration.
        
            Parameters:
                creationDate (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): The :code:`creationDate` to set.
        
        
        """
        ...
    def setFidelModelId(self, long: int) -> None: ...

class ChromaticModelImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.optics.ChromaticModel], cern.lsa.domain.optics.ChromaticModel):
    """
    public class ChromaticModelImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.optics.ChromaticModel`> implements :class:`~cern.lsa.domain.optics.ChromaticModel`
    
        Default implementation of the :class:`~cern.lsa.domain.optics.ChromaticModel` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getAlphaH(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getAlphaH` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getAlphaV(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getAlphaV` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getBetaH(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getBetaH` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getBetaV(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getBetaV` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getBsedd(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getBsedd` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
            Returns:
                double
        
        
        """
        ...
    def getBsrem(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getBsrem` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getChcon(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getChcon` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getChedd(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getChedd` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getChrem(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getChrem` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getCvcon(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getCvcon` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getCvedd(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getCvedd` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getCvrem(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getCvrem` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getGammaH(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getGammaH` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getGammaV(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getGammaV` in interface :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def getLatticeChromaH(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getLatticeChromaH`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.ChromaticModel`
        
            Returns:
                double
        
        
        """
        ...
    def getLatticeChromaV(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ChromaticModel.getLatticeChromaV`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.ChromaticModel`
        
        
        """
        ...
    def setAlphaH(self, double: float) -> None:
        """
        
            Parameters:
                alphaH (double): 
        
        """
        ...
    def setAlphaV(self, double: float) -> None:
        """
        
            Parameters:
                alphaV (double): 
        
        """
        ...
    def setBetaH(self, double: float) -> None:
        """
        
            Parameters:
                betaH (double): 
        
        """
        ...
    def setBetaV(self, double: float) -> None:
        """
        
            Parameters:
                betaV (double): 
        
        """
        ...
    def setBsedd(self, double: float) -> None: ...
    def setBsrem(self, double: float) -> None:
        """
        
            Parameters:
                bsrem (double): 
        
        """
        ...
    def setChcon(self, double: float) -> None:
        """
        
            Parameters:
                chcon (double): 
        
        """
        ...
    def setChedd(self, double: float) -> None:
        """
        
            Parameters:
                chedd (double): 
        
        """
        ...
    def setChrem(self, double: float) -> None:
        """
        
            Parameters:
                chrem (double): 
        
        """
        ...
    def setCvcon(self, double: float) -> None:
        """
        
            Parameters:
                cvcon (double): 
        
        """
        ...
    def setCvedd(self, double: float) -> None:
        """
        
            Parameters:
                cvedd (double): 
        
        """
        ...
    def setCvrem(self, double: float) -> None:
        """
        
            Parameters:
                cvrem (double): the cvrem
        
        
        """
        ...
    def setGammaH(self, double: float) -> None:
        """
        
            Parameters:
                gammaH (double): 
        
        """
        ...
    def setGammaV(self, double: float) -> None:
        """
        
            Parameters:
                gammaV (double): 
        
        """
        ...
    def setLatticeChromaH(self, double: float) -> None:
        """
        
            Parameters:
                latticeChromaH (double): 
        
        """
        ...
    def setLatticeChromaV(self, double: float) -> None:
        """
        
            Parameters:
                latticeChromaV (double): 
        
        """
        ...

class ElementImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.optics.Element], cern.lsa.domain.optics.Element):
    """
    public class ElementImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.optics.Element`> implements :class:`~cern.lsa.domain.optics.Element`
    
        Default implementation of the :class:`~cern.lsa.domain.optics.Element` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def addLogicalHwName(self, string: str) -> None:
        """
        
            Parameters:
                logicalHwName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...
    def getAcceleratorZone(self) -> cern.accsoft.commons.domain.zones.AcceleratorZone:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.ElementBase.getAcceleratorZone`
            Returns the name of accelerator zone to which this element belongs to.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ElementBase.getAcceleratorZone`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.ElementBase`
        
            Returns:
                the name of accelerator zone to which this element belongs to.
        
        
        """
        ...
    def getAffectedRings(self) -> java.util.Set[cern.lsa.domain.optics.BeamEnum]: ...
    def getLength(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.ElementBase.getLength`
            Returns the length of this element. Greg: What is the unit here?
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ElementBase.getLength` in interface :class:`~cern.lsa.domain.optics.ElementBase`
        
            Returns:
                the length of this element
        
        
        """
        ...
    def getLogicalHwName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Element.getLogicalHwName`
            Returns the name of the first logical hardware (magnet string) associated with this element or :code:`null` if no
            logical hardware is associated with this element. This a convenience method that returns the first element of the array
            returned by :code:`getLogicalHwNames()` or null if the array is empty.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Element.getLogicalHwName` in interface :class:`~cern.lsa.domain.optics.Element`
        
            Returns:
                the name of the first logical hardware associated with this element or :code:`null`.
        
        
        """
        ...
    def getLogicalHwNames(self) -> java.util.Set[str]: ...
    def getMadParent(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.ElementBase.getMadParent`
            Returns the parent as defined in the MAD file of this element e.g. MB, MCS, MCD
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ElementBase.getMadParent` in interface :class:`~cern.lsa.domain.optics.ElementBase`
        
            Returns:
                the parent as defined in the MAD file of this element.
        
        
        """
        ...
    def getPlane(self) -> cern.lsa.domain.optics.ElementPlane:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ElementBase.getPlane` in interface :class:`~cern.lsa.domain.optics.ElementBase`
        
            Returns:
                the plane of this element
        
        
        """
        ...
    def getPosition(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.ElementBase.getPosition`
            Returns the position of this element. Greg: What is the unit here? what means the position?
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ElementBase.getPosition` in interface :class:`~cern.lsa.domain.optics.ElementBase`
        
            Returns:
                the position of this element
        
        
        """
        ...
    def getSteeringPlane(self) -> cern.lsa.domain.optics.ElementPlane:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Element.getSteeringPlane`
            get the steering plane to be used by the steering application for this element The steering plane value is
            ElementPlane.NONE when the element is not used by the steering
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Element.getSteeringPlane` in interface :class:`~cern.lsa.domain.optics.Element`
        
            Returns:
                ElementPlane
        
        
        """
        ...
    def getType(self) -> cern.lsa.domain.optics.ElementType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.ElementBase.getType`
            Returns the type of this element e.g. SBEND, QUADRUPOLE, VMONITOR, HKICKER.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ElementBase.getType` in interface :class:`~cern.lsa.domain.optics.ElementBase`
        
            Returns:
                the type of this element
        
        
        """
        ...
    def isObsolete(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Element.isObsolete`
            get the obsolete status of the element
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Element.isObsolete` in interface :class:`~cern.lsa.domain.optics.Element`
        
            Returns:
                true if the element is obsolete
        
        
        """
        ...
    def setAcceleratorZone(self, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> None:
        """
        
            Parameters:
                acceleratorZone (cern.accsoft.commons.domain.zones.AcceleratorZone): The :code:`acceleratorZone` to set.
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.ElementImpl.getAcceleratorZone`
        
        
        """
        ...
    def setAffectedRings(self, set: java.util.Set[cern.lsa.domain.optics.BeamEnum]) -> None: ...
    def setLength(self, double: float) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Element.setLength`
            set the length of the element
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Element.setLength` in interface :class:`~cern.lsa.domain.optics.Element`
        
            Parameters:
                length (double): The :code:`length` to set.
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.ElementImpl.getLength`
        
        
        """
        ...
    def setMadParent(self, string: str) -> None:
        """
        
            Parameters:
                madParent (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The :code:`madParent` to set.
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.ElementImpl.getMadParent`
        
        
        """
        ...
    def setObsolete(self, boolean: bool) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Element.setObsolete`
            set whereas the element is obsolete
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Element.setObsolete` in interface :class:`~cern.lsa.domain.optics.Element`
        
            Parameters:
                obsolete (boolean): : true if the element is obsolete
        
        
        """
        ...
    def setPlane(self, elementPlane: cern.lsa.domain.optics.ElementPlane) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Element.setPlane`
            Set the plane the element is acting on
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Element.setPlane` in interface :class:`~cern.lsa.domain.optics.Element`
        
            Parameters:
                plane (:class:`~cern.lsa.domain.optics.ElementPlane`): The :code:`plane` to set.
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.ElementImpl.getPlane`
        
        
        """
        ...
    def setPosition(self, double: float) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Element.setPosition`
            set the position of the element
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Element.setPosition` in interface :class:`~cern.lsa.domain.optics.Element`
        
            Parameters:
                position (double): The :code:`position` to set.
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.ElementImpl.getPosition`
        
        
        """
        ...
    def setSteeringPlane(self, elementPlane: cern.lsa.domain.optics.ElementPlane) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Element.setSteeringPlane`
            Set the plane to be used by the steering for this element The steering plane is set to ElementPlane.NONE when this
            element is not used by the steering application
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Element.setSteeringPlane` in interface :class:`~cern.lsa.domain.optics.Element`
        
            Parameters:
                steeringPlane (:class:`~cern.lsa.domain.optics.ElementPlane`): : the ElementPlane enum
        
        
        """
        ...
    def setType(self, elementType: cern.lsa.domain.optics.ElementType) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Element.setType`
            set the type of the element
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Element.setType` in interface :class:`~cern.lsa.domain.optics.Element`
        
            Parameters:
                type (:class:`~cern.lsa.domain.optics.ElementType`): The :code:`type` to set.
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.ElementImpl.getType`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.optics.Element`
        
        
        """
        ...

class ElementsRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.optics.ElementsRequest):
    """
    public class ElementsRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.optics.ElementsRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.optics.ElementsRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    ACCELERATOR_ZONE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ACCELERATOR_ZONE
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.ElementsRequestImpl.getAcceleratorZone`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARTICLE_TRANSFER: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARTICLE_TRANSFER
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.ElementsRequestImpl.getParticleTransfer`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ELEMENT_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ELEMENT_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.ElementsRequestImpl.getElementNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    LOGICAL_HW_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` LOGICAL_HW_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.ElementsRequestImpl.getLogicalHwNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TYPES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TYPES
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.ElementsRequestImpl.getTypes`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    STEERING: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` STEERING
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.ElementsRequestImpl.getSteering`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EXCLUDE_OBSOLETE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` EXCLUDE_OBSOLETE
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.ElementsRequestImpl.excludeObsolete`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def excludeObsolete(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.ElementsRequest.excludeObsolete`
            return :code:`true` if the Obsolete elements have to be excluded from the request
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ElementsRequest.excludeObsolete`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.ElementsRequest`
        
            Returns:
        
        
        """
        ...
    def getAcceleratorZone(self) -> cern.accsoft.commons.domain.zones.AcceleratorZone:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ElementsRequest.getAcceleratorZone`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.ElementsRequest`
        
            Returns:
                accelerator zone that the elements should belong to
        
        
        """
        ...
    def getElementNames(self) -> java.util.Set[str]: ...
    def getLogicalHwNames(self) -> java.util.Set[str]: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ElementsRequest.getParticleTransfer`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.ElementsRequest`
        
            Returns:
                particle transfer that the elements should belong to
        
        
        """
        ...
    def getSteering(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.ElementsRequest.getSteering`
            Returns :code:`true` if only steering elements are requested. Steering elements are monitors and correctors including
            :meth:`~cern.lsa.domain.optics.ElementType.MONITOR`, :meth:`~cern.lsa.domain.optics.ElementType.HMONITOR`,
            :meth:`~cern.lsa.domain.optics.ElementType.VMONITOR`, :meth:`~cern.lsa.domain.optics.ElementType.HKICKER`,
            :meth:`~cern.lsa.domain.optics.ElementType.VKICKER` that have a plane defined.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.ElementsRequest.getSteering`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.ElementsRequest`
        
            Returns:
                :code:`true` if only steering elements are requested
        
        
        """
        ...
    def getTypes(self) -> java.util.Set[cern.lsa.domain.optics.ElementType]: ...

class LogicalHardwareImpl(cern.lsa.domain.devices.spi.DeviceImpl, cern.lsa.domain.optics.LogicalHardware):
    """
    public class LogicalHardwareImpl extends :class:`~cern.lsa.domain.devices.spi.DeviceImpl` implements :class:`~cern.lsa.domain.optics.LogicalHardware`
    
        Default implementation of the :class:`~cern.lsa.domain.optics.LogicalHardware` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, device: cern.lsa.domain.devices.Device): ...
    @typing.overload
    def __init__(self, logicalHardware: cern.lsa.domain.optics.LogicalHardware): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...
    def getCalibrationName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getCalibrationName`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def getCalibrationSign(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getCalibrationSign`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def getLinkRuleName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getLinkRuleName`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.LogicalHardware`
        
            Returns:
                The name of the :code:`LinkRule` associated with the :class:`~cern.lsa.domain.devices.Device` the
                :code:`LogicalHardware` at hand describes, this is used in :code:`cern.lsa.core.trim.rules.linkrule.LinkRuleResolver`.
        
        
        """
        ...
    def getLtot(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getLtot` in interface :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def getMadStrengthName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getMadStrengthName`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def getMadStrengthType(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getMadStrengthType`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def getMagnetType(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getMagnetType`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def getMagneticLength(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getMagneticLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.LogicalHardware`
        
            Returns:
                the magnetic length or null if not defined
        
        
        """
        ...
    def getOpTemp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getOpTemp` in interface :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def getPlane(self) -> cern.lsa.domain.optics.ElementPlane:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getPlane` in interface :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def getRtot(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getRtot` in interface :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def getRtotMeasured(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getRtotMeasured`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def getTau(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.LogicalHardware.getTau` in interface :class:`~cern.lsa.domain.optics.LogicalHardware`
        
        
        """
        ...
    def setCalibrationName(self, string: str) -> None: ...
    def setCalibrationSign(self, int: int) -> None: ...
    def setLinkRuleName(self, string: str) -> None: ...
    def setLtot(self, double: float) -> None: ...
    def setMadStrengthName(self, string: str) -> None: ...
    def setMadStrengthType(self, string: str) -> None: ...
    def setMagnetType(self, string: str) -> None: ...
    def setMagneticLength(self, double: float) -> None: ...
    def setOpTemp(self, double: float) -> None: ...
    def setPlane(self, elementPlane: cern.lsa.domain.optics.ElementPlane) -> None: ...
    def setRtot(self, double: float) -> None: ...
    def setRtotMeasured(self, double: float) -> None: ...
    def setTau(self, double: float) -> None: ...

class MeasuredTwissImpl(cern.lsa.domain.optics.MeasuredTwiss, java.io.Serializable):
    """
    public class MeasuredTwissImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.optics.MeasuredTwiss`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default, immutable implementation of a measured twiss.
    
        Use the builder :code:`cern.lsa.domain.optics.factory.MeasuredTwissBuilder` in order to create instances of this class.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, twiss: cern.lsa.domain.optics.Twiss, double: float, date: java.util.Date, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, double13: float, double14: float, double15: float, double16: float, double17: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getAlfxError(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getAlfxError` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getAlfxMeas(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getAlfxMeas` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getAlfyError(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getAlfyError` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getAlfyMeas(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getAlfyMeas` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getBetxError(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getBetxError` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getBetxMeas(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getBetxMeas` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getBetyError(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getBetyError` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getBetyMeas(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getBetyMeas` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getDxError(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getDxError` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getDxMeas(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getDxMeas` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getDyError(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getDyError` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getDyMeas(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getDyMeas` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getEnergy(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getEnergy`
            Returns the energy at which the measurement was taken.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getEnergy` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
            Returns:
                energy of the measurement
        
        
        """
        ...
    def getMuxError(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getMuxError` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getMuxMeas(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getMuxMeas` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getMuyError(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getMuyError` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getMuyMeas(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getMuyMeas` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
        
        """
        ...
    def getTimestamp(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getTimestamp`
            Returns the UTC timestamp at which the measurement took place.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getTimestamp` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
            Returns:
                UTC timestamp of the measurement
        
        
        """
        ...
    def getTwiss(self) -> cern.lsa.domain.optics.Twiss:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getTwiss`
            Returns the twiss object associated to this measurement.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.MeasuredTwiss.getTwiss` in interface :class:`~cern.lsa.domain.optics.MeasuredTwiss`
        
            Returns:
                corresponding twiss paramters
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class OpticImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.optics.Optic], cern.lsa.domain.optics.Optic):
    """
    public class OpticImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.optics.Optic`> implements :class:`~cern.lsa.domain.optics.Optic`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.equals`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def getBaseStrengthFile(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Optic.getBaseStrengthFile`
            the madx file used as base for the optic strengths
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Optic.getBaseStrengthFile` in interface :class:`~cern.lsa.domain.optics.Optic`
        
            Returns:
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Optic.getCreationDate`
            the date the optic had been entered in LSA database
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Optic.getCreationDate` in interface :class:`~cern.lsa.domain.optics.Optic`
        
            Returns:
        
        
        """
        ...
    def getModelUri(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Optic.getModelUri` in interface :class:`~cern.lsa.domain.optics.Optic`
        
            Returns:
                the URI which can be passed to JMad to retrieve the model used to generate this optic
        
        
        """
        ...
    def getOpticParameters(self) -> java.util.Map[str, float]: ...
    def getOpticStrengths(self) -> java.util.List[cern.lsa.domain.optics.OpticStrength]: ...
    def getOverrideStrengthFile(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Optic.getOverrideStrengthFile`
            additional file for optic strength
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Optic.getOverrideStrengthFile` in interface :class:`~cern.lsa.domain.optics.Optic`
        
            Returns:
        
        
        """
        ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getParameterValue(self, string: str) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Optic.getParameterValue` in interface :class:`~cern.lsa.domain.optics.Optic`
        
            Returns:
                the value of the parameter of the given name
        
        
        """
        ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Optic.getParticleTransfer` in interface :class:`~cern.lsa.domain.optics.Optic`
        
            Returns:
                the particle transfer the optic applies for
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.hashCode`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def setBaseStrengthFile(self, string: str) -> None:
        """
        
            Parameters:
                baseStrengthFile (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): returns the name of the base strength file
        
        
        """
        ...
    def setCreationDate(self, date: java.util.Date) -> None:
        """
        
            Parameters:
                creationDate (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): The creationDate to set.
        
        
        """
        ...
    def setModelUri(self, string: str) -> None:
        """
        
            Parameters:
                modelUri (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The modelUri to set.
        
        
        """
        ...
    def setOpticParameters(self, map: typing.Union[java.util.Map[str, float], typing.Mapping[str, float]]) -> None: ...
    def setOpticStrengths(self, list: java.util.List[cern.lsa.domain.optics.OpticStrength]) -> None: ...
    def setOverrideStrengthFile(self, string: str) -> None:
        """
        
            Parameters:
                overrideStrengthFile (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): returns the name of the override strength file
        
        
        """
        ...
    def setParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> None:
        """
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): 
        
        """
        ...

class OpticStrengthImpl(cern.lsa.domain.optics.OpticStrength, java.io.Serializable):
    """
    public class OpticStrengthImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.optics.OpticStrength`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getBeam(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticStrength.getBeam`
            Returns the Beam or :code:`null` if it is not defined.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticStrength.getBeam` in interface :class:`~cern.lsa.domain.optics.OpticStrength`
        
            Returns:
                the Beam or :code:`null` if it is not defined.
        
        
        """
        ...
    def getLogicalHardwareName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticStrength.getLogicalHardwareName`
            Returns the name of a logical hardware this optic strength belongs to.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticStrength.getLogicalHardwareName`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.OpticStrength`
        
            Returns:
                the name of a logical hardware this optic strength belongs to.
        
        
        """
        ...
    def getStrength(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticStrength.getStrength` in interface :class:`~cern.lsa.domain.optics.OpticStrength`
        
            Returns:
                strength or 0 if not defined
        
        
        """
        ...
    def getStrengthL(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticStrength.getStrengthL` in interface :class:`~cern.lsa.domain.optics.OpticStrength`
        
            Returns:
                strengthL or 0 if not defined
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def setBeam(self, string: str) -> None: ...
    def setLogicalHWName(self, string: str) -> None: ...
    def setStrength(self, double: float) -> None: ...
    def setStrengthL(self, double: float) -> None: ...
    class Builder:
        def __init__(self): ...
        def beam(self, string: str) -> 'OpticStrengthImpl.Builder': ...
        def build(self) -> cern.lsa.domain.optics.OpticStrength: ...
        def logicalHWName(self, string: str) -> 'OpticStrengthImpl.Builder': ...
        def strength(self, double: float) -> 'OpticStrengthImpl.Builder': ...
        def strengthL(self, double: float) -> 'OpticStrengthImpl.Builder': ...

class OpticsRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.optics.OpticsRequest):
    """
    public class OpticsRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.optics.OpticsRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.optics.OpticsRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    ACCELERATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ACCELERATOR
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.OpticsRequestImpl.getAccelerator`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARTICLE_TRANSFER: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARTICLE_TRANSFER
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.OpticsRequestImpl.getParticleTransfer`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    BEAM_RPOCESS_TYPE_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` BEAM_RPOCESS_TYPE_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.OpticsRequestImpl.getBeamProcessTypeNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    OPTIC_IDS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` OPTIC_IDS
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.OpticsRequestImpl.getOpticIds`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsRequest.getAccelerator`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.OpticsRequest`
        
            Returns:
                accelerator the optic should belong to
        
        
        """
        ...
    def getBeamProcessTypeNames(self) -> java.util.Set[str]: ...
    def getOpticIds(self) -> java.util.Set[int]: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsRequest.getParticleTransfer`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.OpticsRequest`
        
            Returns:
                particle transfer the optic should belong to
        
            Also see:
                :meth:`~cern.lsa.domain.optics.Optic.getParticleTransfer`
        
        
        """
        ...

class OpticsTableImpl(cern.lsa.domain.optics.OpticsTable, java.io.Serializable):
    """
    public class OpticsTableImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.optics.OpticsTable`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of :class:`~cern.lsa.domain.optics.OpticsTable`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, opticsTable: cern.lsa.domain.optics.OpticsTable, list: java.util.List[cern.lsa.domain.optics.OpticsTableItem]): ...
    @typing.overload
    def __init__(self, beamProcessType: cern.lsa.domain.settings.type.BeamProcessType, list: java.util.List[cern.lsa.domain.optics.OpticsTableItem]): ...
    @typing.overload
    def __init__(self, string: str, int: int, list: java.util.List[cern.lsa.domain.optics.OpticsTableItem]): ...
    def getBeamProcessTypeName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTable.getBeamProcessTypeName`
            Returns name of the beam process type for which the optics table is defined.
        
            Note that in case when optics are defined per beam process rather than per beam process type, this method returns name
            of the corresponding beam process type.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTable.getBeamProcessTypeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.OpticsTable`
        
            Returns:
                name of the beam process type
        
        
        """
        ...
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def getLength(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTable.getLength`
            Returns the length of the table in ms, what is effectively the length of the beam process this table is for.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTable.getLength` in interface :class:`~cern.lsa.domain.optics.OpticsTable`
        
            Returns:
                length of the table in ms
        
        
        """
        ...
    def getOpticNames(self) -> java.util.List[str]: ...
    def getOpticsTableItemByIndex(self, int: int) -> cern.lsa.domain.optics.OpticsTableItem:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTable.getOpticsTableItemByIndex`
            Returns :class:`~cern.lsa.domain.optics.OpticsTableItem` at specified index.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTable.getOpticsTableItemByIndex`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.OpticsTable`
        
            Parameters:
                index (int): index of the :class:`~cern.lsa.domain.optics.OpticsTableItem` to be returned: from 0 to
                    :meth:`~cern.lsa.domain.optics.OpticsTable.getSize` - 1
        
            Returns:
                :class:`~cern.lsa.domain.optics.OpticsTableItem` at specified index
        
        
        """
        ...
    def getOpticsTableItemByTime(self, double: float) -> cern.lsa.domain.optics.OpticsTableItem:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTable.getOpticsTableItemByTime`
            Returns the :class:`~cern.lsa.domain.optics.OpticsTableItem` at the given time. The value returned is the
            :class:`~cern.lsa.domain.optics.OpticsTableItem` with the time closest to the given time and that is equal or inferior
            to the given time.
        
            The :class:`~cern.lsa.domain.optics.OpticsTableItem` is valid from the time it is defined till the next
            :class:`~cern.lsa.domain.optics.OpticsTableItem` or till the end of the beam process type. For instance if the last
            :class:`~cern.lsa.domain.optics.OpticsTableItem` is defined at time 1000ms and the length of beam process type is
            1200ms, then for any time from range [1000, 1200] the method returns this last
            :class:`~cern.lsa.domain.optics.OpticsTableItem` 1000ms.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTable.getOpticsTableItemByTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.OpticsTable`
        
            Parameters:
                timeInBeamProcessType (double): time within the beam process (type) for which :class:`~cern.lsa.domain.optics.OpticsTableItem` should be returned. Note
                    that in accelerators where we use a single beam process that covers the whole cycle - this is equivalent to the time
                    within the stand alone context (cycle).
        
            Returns:
                :class:`~cern.lsa.domain.optics.OpticsTableItem` for given time
        
        
        """
        ...
    def getOpticsTableItems(self) -> java.util.List[cern.lsa.domain.optics.OpticsTableItem]: ...
    def getSize(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTable.getSize`
            Returns number elements in the optics table.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTable.getSize` in interface :class:`~cern.lsa.domain.optics.OpticsTable`
        
            Returns:
                size of the optics table
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTable.isEmpty`
            Returns :code:`true` if the table doesn't contain any optic.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTable.isEmpty` in interface :class:`~cern.lsa.domain.optics.OpticsTable`
        
            Returns:
                :code:`true` if the table doesn't contain any optic
        
        
        """
        ...
    def isValid(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTable.isValid`
            Returns :code:`true` if the optics table is defined and is valid.
        
            The optic table might be not valid e.g. if the time coordinates are not strictly ascending or if the defined optic
            doesn't exist. In such case :meth:`~cern.lsa.domain.optics.OpticsTable.getErrorMessages` method can be used to get
            descriptions of the errors.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTable.isValid` in interface :class:`~cern.lsa.domain.optics.OpticsTable`
        
            Returns:
                :code:`true` if this optics table is valid, :code:`false` if it's not.
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator[cern.lsa.domain.optics.OpticsTableItem]: ...

class OpticsTableItemImpl(cern.lsa.domain.optics.OpticsTableItem, java.io.Serializable, java.lang.Cloneable):
    """
    public class OpticsTableItemImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.optics.OpticsTableItem`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.optics.OpticsTableItem` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, int: int, double: float, string2: str): ...
    @typing.overload
    def __init__(self, string: str, int: int, double: float, long: int, string2: str): ...
    def clone(self) -> cern.lsa.domain.optics.OpticsTableItem:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTableItem.clone`
            Returns copy of this OpticsTableItem.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTableItem.clone` in interface :class:`~cern.lsa.domain.optics.OpticsTableItem`
        
            Overrides:
                 in class 
        
            Returns:
                copy of this OpticsTableItem.
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getBeamProcessTypeName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTableItem.getBeamProcessTypeName`
            Returns name of the beam process type that this optics item belongs to.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTableItem.getBeamProcessTypeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.OpticsTableItem`
        
            Returns:
                name of the beam process type that this optics item belongs to.
        
        
        """
        ...
    def getEnergy(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTableItem.getEnergy`
            Returns energy of this optics item.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTableItem.getEnergy` in interface :class:`~cern.lsa.domain.optics.OpticsTableItem`
        
            Returns:
                energy of this optics item.
        
            Also see:
                :meth:`~cern.lsa.domain.optics.OpticsTableItem.getTime`
        
        
        """
        ...
    def getOpticId(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTableItem.getOpticId`
            Returns ID of related optic.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTableItem.getOpticId`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.OpticsTableItem`
        
            Returns:
                ID of related optic.
        
        
        """
        ...
    def getOpticName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTableItem.getOpticName`
            Returns name of related optic.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTableItem.getOpticName`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.OpticsTableItem`
        
            Returns:
                name of related optic.
        
        
        """
        ...
    def getTime(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.OpticsTableItem.getTime`
            Returns time (in the unit consistent with the accelerator - [s] for LHC, [ms] for all others) of this optics item within
            the beam process type.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.OpticsTableItem.getTime` in interface :class:`~cern.lsa.domain.optics.OpticsTableItem`
        
            Returns:
                time (in the unit consistent with the accelerator - [s] for LHC, [ms] for all others) of this optics item within the
                beam process type.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def setBeamProcessTypeName(self, string: str) -> None:
        """
            Assigns this item to the given beam process type.
        
            Parameters:
                beamProcessTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the beam process type for which the optic table is defined
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.OpticsTableItemImpl.getBeamProcessTypeName`
        
        
        """
        ...
    def setEnergy(self, double: float) -> None:
        """
            Sets the energy value at given time.
        
            Parameters:
                energy (double): energy at given time
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.OpticsTableItemImpl.getEnergy`
        
        
        """
        ...
    def setOpticId(self, long: int) -> None:
        """
            Sets the database ID of the associated optic.
        
            Parameters:
                opticId (long): the opticId to set
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.OpticsTableItemImpl.getOpticId`
        
        
        """
        ...
    def setOpticName(self, string: str) -> None:
        """
            Sets the name of optic to be used at given time.
        
            Parameters:
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of optic to be used at given time
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.OpticsTableItemImpl.getOpticName`
        
        
        """
        ...
    def setTime(self, int: int) -> None:
        """
            Sets the time coordinate.
        
            Parameters:
                time (int): time coordinate for the optic
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.OpticsTableItemImpl.getTime`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class PowerConverterInfoImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.optics.PowerConverterInfo], cern.lsa.domain.optics.PowerConverterInfo):
    """
    public class PowerConverterInfoImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.optics.PowerConverterInfo`> implements :class:`~cern.lsa.domain.optics.PowerConverterInfo`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, powerConverterInfo: cern.lsa.domain.optics.PowerConverterInfo): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...
    def getAccelerationLimit(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getAccelerationLimit`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the accelerationLimit
        
        
        """
        ...
    def getAdvance(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getAdvance`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the advance
        
        
        """
        ...
    def getBeam(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getBeam`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the beam
        
        
        """
        ...
    def getDecelerationLimit(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getDecelerationLimit`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the decelerationLimit
        
        
        """
        ...
    def getDidtMax(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getDidtMax`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the didtMax
        
        
        """
        ...
    def getDidtMin(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getDidtMin`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the didtMin
        
        
        """
        ...
    def getIMinOp(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getIMinOp`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the iMinOp
        
        
        """
        ...
    def getINom(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getINom`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the iNom
        
        
        """
        ...
    def getIPNo(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getIPNo`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the iPNo
        
        
        """
        ...
    def getIUlt(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getIUlt`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the iUlt
        
        
        """
        ...
    def getLastRefDatabaseUpdate(self) -> java.util.Date:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getLastRefDatabaseUpdate`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the lastRefDatabaseUpdate
        
        
        """
        ...
    def getPoweringSubsector(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.getPoweringSubsector`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the poweringSubsector
        
        
        """
        ...
    def isPolaritySwitch(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PowerConverterInfo.isPolaritySwitch`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
            Returns:
                the polaritySwitch
        
        
        """
        ...
    def setAccelerationLimit(self, double: float) -> None:
        """
        
            Parameters:
                accelerationLimit (double): the accelerationLimit to set
        
        
        """
        ...
    def setAdvance(self, double: float) -> None:
        """
        
            Parameters:
                advance (double): the advance to set
        
        
        """
        ...
    def setBeam(self, string: str) -> None:
        """
        
            Parameters:
                beam (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the beam to set
        
        
        """
        ...
    def setDecelerationLimit(self, double: float) -> None:
        """
        
            Parameters:
                decelerationLimit (double): the decelerationLimit to set
        
        
        """
        ...
    def setDidtMax(self, double: float) -> None:
        """
        
            Parameters:
                didtMax (double): the didtMax to set
        
        
        """
        ...
    def setDidtMin(self, double: float) -> None:
        """
        
            Parameters:
                didtMin (double): the didtMin to set
        
        
        """
        ...
    def setIMinOp(self, double: float) -> None:
        """
        
            Parameters:
                minOp (double): the iMinOp to set
        
        
        """
        ...
    def setINom(self, double: float) -> None:
        """
        
            Parameters:
                nom (double): the iNom to set
        
        
        """
        ...
    def setIPNo(self, double: float) -> None:
        """
        
            Parameters:
                nominalCurrent (double): the iPNo to set
        
        
        """
        ...
    def setIUlt(self, double: float) -> None:
        """
        
            Parameters:
                ult (double): the iUlt to set
        
        
        """
        ...
    def setLastRefDatabaseUpdate(self, date: java.util.Date) -> None:
        """
        
            Parameters:
                lastRefDatabaseUpdate (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): the lastRefDatabaseUpdate to set
        
        
        """
        ...
    def setPolaritySwitch(self, boolean: bool) -> None:
        """
        
            Parameters:
                polaritySwitch (boolean): the polaritySwitch to set
        
        
        """
        ...
    def setPoweringSubsector(self, string: str) -> None:
        """
        
            Parameters:
                poweringSubsector (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the poweringSubsector to set
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.optics.PowerConverterInfo`
        
        
        """
        ...

class PreCyclingPrescriptionImpl(cern.lsa.domain.optics.PreCyclingPrescription):
    """
    public class PreCyclingPrescriptionImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.optics.PreCyclingPrescription`
    """
    def __init__(self, string: str): ...
    def addAttribute(self, string: str, double: float) -> None: ...
    def getAttributeValue(self, string: str) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PreCyclingPrescription.getAttributeValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PreCyclingPrescription`
        
        
        """
        ...
    def getMagnetType(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PreCyclingPrescription.getMagnetType`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PreCyclingPrescription`
        
        
        """
        ...
    def getPrecyclingPrescriptionMode(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PreCyclingPrescription.getPrecyclingPrescriptionMode`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PreCyclingPrescription`
        
        
        """
        ...
    def getPrecyclingPrescriptionName(self) -> str: ...
    def getPrecyclingPrescriptionType(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.PreCyclingPrescription.getPrecyclingPrescriptionType`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.PreCyclingPrescription`
        
        
        """
        ...
    def setMagnetType(self, string: str) -> None:
        """
        
            Parameters:
                magnetType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the magnetType to set
        
        
        """
        ...
    def setPrecyclingPrescriptionMode(self, string: str) -> None:
        """
        
            Parameters:
                precyclingPrescriptionMode (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the precyclingPrescriptionMode to set
        
        
        """
        ...
    def setPrecyclingPrescriptionName(self, string: str) -> None: ...
    def setPrecyclingPrescriptionType(self, string: str) -> None:
        """
        
            Parameters:
                precyclingPrescriptionType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the precyclingPrescriptionType to set
        
        
        """
        ...

class RFCalibrationImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.optics.RFCalibration], cern.lsa.domain.optics.RFCalibration):
    """
    public class RFCalibrationImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.optics.RFCalibration`> implements :class:`~cern.lsa.domain.optics.RFCalibration`
    
        Default implementation of :class:`~cern.lsa.domain.optics.RFCalibration` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getCavityQ(self, double: float) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.RFCalibration.getCavityQ`
            Returns the interpolated cavityQ for the given couplerPosition
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.RFCalibration.getCavityQ` in interface :class:`~cern.lsa.domain.optics.RFCalibration`
        
            Parameters:
                couplerPos (double): coupler position
        
            Returns:
                a double representing the interpolated cavityQ
        
        
        """
        ...
    def getCavityQ2CouplerPosFunction(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.RFCalibration.getCavityQ2CouplerPosFunction`
            Returns the function current(cavityq) as defined by the CalibrationCurve items. The returned function can be used to
            interpolate the value of the current for the given value of bfield
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.RFCalibration.getCavityQ2CouplerPosFunction`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.RFCalibration`
        
            Returns:
                the function current(cavityq) as defined by the CalibrationCurve items.
        
        
        """
        ...
    def getCouplerPos(self, double: float) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.RFCalibration.getCouplerPos`
            Returns the interpolated couplerPos for given cavityQ in the current RFCalibration.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.RFCalibration.getCouplerPos` in interface :class:`~cern.lsa.domain.optics.RFCalibration`
        
            Returns:
                a double representing the interpolated coupler position.
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.RFCalibration.getCreationDate`
            Returns the creation date of this calibration.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.RFCalibration.getCreationDate`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.RFCalibration`
        
            Returns:
                the creation date of this calibration.
        
        
        """
        ...
    def getDeviceName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.RFCalibration.getDeviceName`
            Returns the device name associated to this calibration.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.RFCalibration.getDeviceName` in interface :class:`~cern.lsa.domain.optics.RFCalibration`
        
            Returns:
                the name of the device
        
        
        """
        ...
    def setCreationDate(self, date: java.util.Date) -> None:
        """
            Sets the :code:`creationDate` property.
        
            Parameters:
                creationDate (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): The :code:`creationDate` to set.
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.RFCalibrationImpl.getCreationDate`
        
        
        """
        ...
    def setDeviceName(self, string: str) -> None:
        """
            Sets name of device that this calibration is assigned to.
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the deviceName to set
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.RFCalibrationImpl.getDeviceName`
        
        
        """
        ...
    def setRFCalibrationFunction(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> None:
        """
            Sets the calibration function (cavity Q to coupler position).
        
            Parameters:
                calibrationFunction (cern.accsoft.commons.value.ImmutableDiscreteFunction): the calibration function
        
            Also see:
                :meth:`~cern.lsa.domain.optics.spi.RFCalibrationImpl.getCavityQ2CouplerPosFunction`
        
        
        """
        ...

class TwissImpl(cern.lsa.domain.optics.Twiss, java.io.Serializable):
    """
    public class TwissImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.optics.Twiss`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.optics.Twiss` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getAlfx(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getAlfx` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the correlation function Alfa x function at the element position
        
        
        """
        ...
    def getAlfy(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getAlfy` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the correlation function Alfa y function at the element position
        
        
        """
        ...
    def getBeam(self) -> cern.accsoft.commons.domain.beams.Beam:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getBeam` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the beam that this twiss is defined for
        
        
        """
        ...
    def getBetx(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getBetx` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the amplitude function Betax at the element position
        
        
        """
        ...
    def getBety(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getBety` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the amplitude function Betay at the element position
        
        
        """
        ...
    def getDpx(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getDpx` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the dispersion function Dpx = (delta px / delta PT) / ps at the element position with p= momentum and PT =
                Energy difference, divided by the reference momentum times the velocity of light
        
        
        """
        ...
    def getDpy(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getDpy` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the dispersion function Dpy = (delta py / delta PT) / ps at the element position with p= momentum and PT =
                Energy difference, divided by the reference momentum times the velocity of light
        
        
        """
        ...
    def getDx(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getDx` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the dispersion function Dx = delta x/PT at the element position PT = Energy difference, divided by the
                reference momentum times the velocity of light
        
        
        """
        ...
    def getDy(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getDy` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the dispersion function Dy = delta y/PT at the element position PT = Energy difference, divided by the
                reference momentum times the velocity of light
        
        
        """
        ...
    def getElement(self) -> cern.lsa.domain.optics.ElementBase:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Twiss.getElement`
            Returns element that this twiss is defined for.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getElement` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                element that this twiss is defined for
        
        
        """
        ...
    def getHkick(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getHkick` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the horizontal kick strength of orbit deflectors
        
        
        """
        ...
    def getK0l(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getK0l` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the strength at a dipole multiplied by the element length
        
        
        """
        ...
    def getK1Sl(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getK1Sl` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the strength at a sqew quadrupole element multiplied by the element length
        
        
        """
        ...
    def getK1l(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getK1l` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the strength at a quadrupole multiplied by the element length
        
        
        """
        ...
    def getK2Sl(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getK2Sl` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the strength at a sqew sextupole element multiplied by the element length
        
        
        """
        ...
    def getK2l(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getK2l` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the strength at sextupole multiplied by the element length
        
        
        """
        ...
    def getK3Sl(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getK3Sl` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the strength at a sqew octupole element multiplied by the element length
        
        
        """
        ...
    def getK3l(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getK3l` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the strength at a octupole element multiplied by the element length
        
        
        """
        ...
    def getK4l(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getK4l` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the strength at decapole elements
        
        
        """
        ...
    def getK5l(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getK5l` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the strength at duodecapole elements
        
        
        """
        ...
    def getMux(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getMux` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the horizontal phase function mux at the element position
        
        
        """
        ...
    def getMuy(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getMuy` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the vertical phase function muy at the element position
        
        
        """
        ...
    def getOpticName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Twiss.getOpticName`
            Returns name of optic that this twiss is defined for.
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getOpticName` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                name of optic that this twiss is defined for
        
        
        """
        ...
    def getPx(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getPx` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the momentum px of the orbit referred to the ideal orbit, divided by the reference momentum, at the element
                position
        
        
        """
        ...
    def getPy(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getPy` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the momentum py of the orbit referred to the ideal orbit, divided by the reference momentum, at the element
                position
        
        
        """
        ...
    def getVkick(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getVkick` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the vertical kick strength of orbit deflectors
        
        
        """
        ...
    def getX(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getX` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the Horizontal position x of the orbit, referred to the ideal orbit at the element longitudinal position
        
        
        """
        ...
    def getY(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.getY` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
            Returns:
                the value of the vertical position y of the orbit, referred to the ideal orbit at the element longitudinal position
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def setAlfx(self, double: float) -> None: ...
    def setAlfy(self, double: float) -> None: ...
    def setBeam(self, beam: cern.accsoft.commons.domain.beams.Beam) -> None: ...
    def setBetx(self, double: float) -> None: ...
    def setBety(self, double: float) -> None: ...
    def setDpx(self, double: float) -> None: ...
    def setDpy(self, double: float) -> None: ...
    def setDx(self, double: float) -> None: ...
    def setDy(self, double: float) -> None: ...
    def setElement(self, elementBase: cern.lsa.domain.optics.ElementBase) -> None: ...
    def setHkick(self, double: float) -> None: ...
    def setK0l(self, double: float) -> None: ...
    def setK1l(self, double: float) -> None: ...
    def setK1sl(self, double: float) -> None: ...
    def setK2l(self, double: float) -> None: ...
    def setK2sl(self, double: float) -> None: ...
    def setK3l(self, double: float) -> None: ...
    def setK3sl(self, double: float) -> None: ...
    def setK4l(self, double: float) -> None: ...
    def setK5l(self, double: float) -> None: ...
    def setMux(self, double: float) -> None: ...
    def setMuy(self, double: float) -> None: ...
    def setOpticName(self, string: str) -> None: ...
    def setPx(self, double: float) -> None: ...
    def setPy(self, double: float) -> None: ...
    def setVkick(self, double: float) -> None: ...
    def setX(self, double: float) -> None: ...
    def setY(self, double: float) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def updateOpticName(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.optics.Twiss.updateOpticName`
            This method updates the name of the optic the twiss is associated with
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.Twiss.updateOpticName` in interface :class:`~cern.lsa.domain.optics.Twiss`
        
        
        """
        ...

class TwissesRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.optics.TwissesRequest):
    """
    public class TwissesRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.optics.TwissesRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.optics.TwissesRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    OPTIC_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` OPTIC_NAME
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.TwissesRequestImpl.getOpticName`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    BEAM: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` BEAM
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.TwissesRequestImpl.getBeam`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ELEMENT_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ELEMENT_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.TwissesRequestImpl.getElementNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ELEMENT_TYPES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ELEMENT_TYPES
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.TwissesRequestImpl.getElementTypes`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ELEMENT_POSITION_RANGE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ELEMENT_POSITION_RANGE
    
        Attribute name for :meth:`~cern.lsa.domain.optics.spi.TwissesRequestImpl.getElementPositionRange`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getBeam(self) -> cern.accsoft.commons.domain.beams.Beam:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.TwissesRequest.getBeam` in interface :class:`~cern.lsa.domain.optics.TwissesRequest`
        
            Returns:
                beam name
        
            Also see:
                :meth:`~cern.lsa.domain.optics.Twiss.getBeam`
        
        
        """
        ...
    def getElementNames(self) -> java.util.Set[str]: ...
    def getElementPositionRange(self) -> com.google.common.collect.Range[float]: ...
    def getElementTypes(self) -> java.util.Set[cern.lsa.domain.optics.ElementType]: ...
    def getOpticName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.optics.TwissesRequest.getOpticName`Â in
                interfaceÂ :class:`~cern.lsa.domain.optics.TwissesRequest`
        
            Returns:
                optic name
        
            Also see:
                :meth:`~cern.lsa.domain.optics.Twiss.getOpticName`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.optics.spi")``.

    CalibrationImpl: typing.Type[CalibrationImpl]
    ChromaticModelImpl: typing.Type[ChromaticModelImpl]
    ElementImpl: typing.Type[ElementImpl]
    ElementsRequestImpl: typing.Type[ElementsRequestImpl]
    LogicalHardwareImpl: typing.Type[LogicalHardwareImpl]
    MeasuredTwissImpl: typing.Type[MeasuredTwissImpl]
    OpticImpl: typing.Type[OpticImpl]
    OpticStrengthImpl: typing.Type[OpticStrengthImpl]
    OpticsRequestImpl: typing.Type[OpticsRequestImpl]
    OpticsTableImpl: typing.Type[OpticsTableImpl]
    OpticsTableItemImpl: typing.Type[OpticsTableItemImpl]
    PowerConverterInfoImpl: typing.Type[PowerConverterInfoImpl]
    PreCyclingPrescriptionImpl: typing.Type[PreCyclingPrescriptionImpl]
    RFCalibrationImpl: typing.Type[RFCalibrationImpl]
    TwissImpl: typing.Type[TwissImpl]
    TwissesRequestImpl: typing.Type[TwissesRequestImpl]
