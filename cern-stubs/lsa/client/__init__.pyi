import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.beamdestinations
import cern.accsoft.commons.domain.beams
import cern.accsoft.commons.domain.lhc
import cern.accsoft.commons.domain.modes
import cern.accsoft.commons.util.value
import cern.accsoft.commons.value
import cern.lsa.client.common
import cern.lsa.client.reference
import cern.lsa.client.rest
import cern.lsa.client.spi
import cern.lsa.client.test
import cern.lsa.domain.cern.devices
import cern.lsa.domain.cern.exploitation
import cern.lsa.domain.cern.optics
import cern.lsa.domain.cern.optics.ofb
import cern.lsa.domain.cern.settings
import cern.lsa.domain.cern.settings.ad
import cern.lsa.domain.cern.settings.elena
import cern.lsa.domain.cern.settings.lktim
import cern.lsa.domain.cern.timing
import cern.lsa.domain.cern.timing.enums
import cern.lsa.domain.devices
import cern.lsa.domain.devices.inca
import cern.lsa.domain.optics
import cern.lsa.domain.settings
import cern.lsa.domain.settings.type
import java.lang
import java.time
import java.util
import typing



class AcceleratorService(cern.lsa.client.common.CommonAcceleratorService):
    """
    @Cacheable("clientCache") public interface AcceleratorService extends cern.lsa.client.common.CommonAcceleratorService
    
        Service for operations related to fetching and manipulating information about the accelerators (such as accelerator
        zones, particle transfers, ...).
    """
    def findActiveAcceleratorMode(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> cern.accsoft.commons.domain.modes.AcceleratorMode: ...
    def findActiveBeamDestinationEndPoint(self, beamDestination: cern.accsoft.commons.domain.beamdestinations.BeamDestination) -> cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint: ...
    def findOpConfigs(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[str]: ...
    def setActiveAcceleratorMode(self, accelerator: cern.accsoft.commons.domain.Accelerator, acceleratorMode: cern.accsoft.commons.domain.modes.AcceleratorMode) -> None: ...
    def setActiveBeamDestinationEndPoint(self, beamDestination: cern.accsoft.commons.domain.beamdestinations.BeamDestination, beamDestinationEndPoint: cern.accsoft.commons.domain.beamdestinations.BeamDestinationEndPoint) -> None: ...

class AdService:
    """
    public interface AdService
    
        Service with methods specific to the AD accelerator. It allows retrieve and save AD cycle structure and related timing
        information.
    """
    @typing.overload
    def convertCycleTimeToKTime(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle, duration: java.time.Duration) -> java.time.Duration:
        """
            Converts the cycle time to k time. Both times are in milli-seconds.
        
            Parameters:
                lsaCycle (cern.lsa.domain.settings.StandAloneCycle): LSA cycle
                cycleTime (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>`): the cycle time to convert
        
            Returns:
                the k time
        
        `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` `Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>` convertCycleTimeToKTime (`Duration <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Duration.html?is-external=true>` cycleTime)
        
            Deprecated.
            use :meth:`~cern.lsa.client.AdService.convertCycleTimeToKTime`
        
        """
        ...
    @typing.overload
    def convertCycleTimeToKTime(self, duration: java.time.Duration) -> java.time.Duration: ...
    @typing.overload
    def findCycleStructure(self) -> cern.lsa.domain.cern.settings.ad.AdCycleStructure: ...
    @typing.overload
    def findCycleStructure(self, adCycleStructure: cern.lsa.domain.cern.settings.ad.AdCycleStructure, trimHeader: cern.lsa.domain.settings.TrimHeader) -> cern.lsa.domain.cern.settings.ad.AdCycleStructure:
        """
            Returns cycle structure of the AD cycle as it was at the moment represented by given trim header.
        
            Parameters:
                lsaCycle (cern.lsa.domain.settings.StandAloneCycle): LSA cycle
                trimHeader (cern.lsa.domain.settings.TrimHeader): non-null trim header for which cycle structure should be returned
        
            Returns:
                the corresponding cycle structure
        
        `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` cern.lsa.domain.cern.settings.ad.AdCycleStructure findCycleStructure()
        
            Deprecated.
            use :meth:`~cern.lsa.client.AdService.findCycleStructure`
        `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` cern.lsa.domain.cern.settings.ad.AdCycleStructure findCycleStructure (cern.lsa.domain.cern.settings.ad.AdCycleStructure adCycle, cern.lsa.domain.settings.TrimHeader trimHeader)
        
            Deprecated.
            use :meth:`~cern.lsa.client.AdService.findCycleStructure`
        
        """
        ...
    @typing.overload
    def findCycleStructure(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle) -> cern.lsa.domain.cern.settings.ad.AdCycleStructure:
        """
            Returns the current structure of an AD cycle.
        
            Parameters:
                lsaCycle (cern.lsa.domain.settings.StandAloneCycle): LSA cycle
        
            Returns:
                current structure of an AD cycle
        
            Raises:
                : if the AD cycle structure settings are not defined in the database or the format is corrupted.
        
        """
        ...
    @typing.overload
    def findCycleStructure(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle, trimHeader: cern.lsa.domain.settings.TrimHeader) -> cern.lsa.domain.cern.settings.ad.AdCycleStructure: ...
    @typing.overload
    def findCycleStructureTrims(self, adCycleStructure: cern.lsa.domain.cern.settings.ad.AdCycleStructure) -> java.util.List[cern.lsa.domain.settings.TrimHeader]: ...
    @typing.overload
    def findCycleStructureTrims(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle) -> java.util.List[cern.lsa.domain.settings.TrimHeader]: ...
    def findEltagNames(self) -> java.util.Set[str]: ...
    @typing.overload
    def findFlatTopTimeByEltag(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle, string: str) -> int:
        """
            Method meant for YASP. For a given ELTAG name, the method returns time at which the corresponding flat segment starts.
            The time is calculated by taking real RAMP segment length (length including flat parts and rounding time) and ignoring
            length of flat tops (as there are internal stops in the corresponding CGAFG function.
        
            Parameters:
                lsaCycle (cern.lsa.domain.settings.StandAloneCycle): LSA cycle
                eltag (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): ELTAG name
        
            Returns:
                time coordinate of the flat top in the cycle
        
            Raises:
                : if the given ELTAG is not assigned to any flat segment of the cycle
        
        `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` int findFlatTopTimeByEltag (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` eltag)
        
            Deprecated.
            use :meth:`~cern.lsa.client.AdService.findFlatTopTimeByEltag`
        
        """
        ...
    @typing.overload
    def findFlatTopTimeByEltag(self, string: str) -> int: ...
    def findTestCycleStructure(self) -> cern.lsa.domain.cern.settings.ad.AdCycleStructure: ...
    def findTimingProcesses(self) -> java.util.Set[cern.lsa.domain.cern.timing.TimingProcess]: ...
    def saveCycleSettings(self, trimRequest: cern.lsa.domain.settings.TrimRequest, adCycleStructure: cern.lsa.domain.cern.settings.ad.AdCycleStructure) -> cern.lsa.domain.settings.TrimResponse: ...
    def saveCycleStructure(self, adCycleStructure: cern.lsa.domain.cern.settings.ad.AdCycleStructure, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunctionList], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.accsoft.commons.value.ImmutableDiscreteFunctionList]], string: str) -> cern.lsa.domain.settings.TrimResponse: ...

class ArchiveReferenceService(cern.lsa.client.common.CommonArchiveReferenceService):
    """
    public interface ArchiveReferenceService extends cern.lsa.client.common.CommonArchiveReferenceService
    
        A service that allows retrieval, creation, modification and deletion of setting archives and retrieval and updates of
        setting reference values.
    
        Also see:
            :code:`Archive`
    """
    ...

class CacheService(cern.lsa.client.common.CommonCacheService):
    """
    public interface CacheService extends cern.lsa.client.common.CommonCacheService
    
        A service that allows to clear all caches on the server-side, and get related stats.
    """
    ...

class ClientApplicationConfig:
    """
    @Configuration public class ClientApplicationConfig extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Main LSA Services, ready to be imported into application specific's Spring contexts In order to grab a reference to any
        of LSA public services, you can do: AnnotationConfigApplicationContext applicationContext = new
        AnnotationConfigApplicationContext( ClientApplicationConfig.class); OpticService opticService =
        applicationContext.getBean(OpticService.class); Which is exactly equivalent to
        ServiceLocator.getService(OpticService.class);
    """
    def __init__(self): ...
    def acceleratorService(self) -> AcceleratorService: ...
    def archiveReferenceService(self) -> ArchiveReferenceService: ...
    def cacheService(self) -> CacheService: ...
    def contextService(self) -> 'ContextService': ...
    def exploitationService(self) -> 'ExploitationService': ...
    def fidelService(self) -> 'FidelService': ...
    def generationService(self) -> 'GenerationService': ...
    def hyperCycleService(self) -> 'HyperCycleService': ...
    def japcService(self) -> 'JapcService': ...
    def knobService(self) -> 'KnobService': ...
    def lhcService(self) -> 'LhcService': ...
    def opticService(self) -> 'OpticService': ...
    def parameterService(self) -> 'ParameterService': ...
    def settingService(self) -> 'SettingService': ...
    def spsService(self) -> 'SpsService': ...
    def timingService(self) -> 'TimingService': ...
    def transactionService(self) -> cern.lsa.client.common.TransactionService: ...
    def trimService(self) -> 'TrimService': ...

class ContextService(cern.lsa.client.common.CommonContextService):
    """
    @Cacheable("clientCache") public interface ContextService extends cern.lsa.client.common.CommonContextService
    
        Service for context-related information: beam processes, cycles, hyper-cycles, cycle to user mappings...
    """
    def findActiveContexts(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.settings.StandAloneContext]: ...
    def findActiveTimingUsers(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> cern.lsa.domain.cern.timing.ActiveTimingUsers:
        """
            Returns active users currently played by the timing system.
        
            The returned object contains list of normal and spare users, in the order as they are played by the timing system.
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): accelerator
        
            Returns:
                object containing current normal and spare users
        
            Raises:
                : in case there is a problem accessing TGM telegram for given accelerator
        
        
        """
        ...
    def findLoggingHistory(self, long: int, long2: int, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.List[cern.lsa.domain.settings.UserContextMapping]: ...

class DeviceService(cern.lsa.client.common.CommonDeviceService):
    """
    @Cacheable("clientCache") public interface DeviceService extends cern.lsa.client.common.CommonDeviceService
    
        Service to work with devices, device groups, etc.
    """
    def findPowerConverterInfosByDeviceIds(self, collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> java.util.Set[cern.lsa.domain.optics.PowerConverterInfo]: ...
    def findPowerConverterNestedCircuitInfos(self, powerConverterNestedCircuitInfosRequest: cern.lsa.domain.devices.PowerConverterNestedCircuitInfosRequest) -> java.util.Set[cern.lsa.domain.devices.PowerConverterNestedCircuitInfo]: ...

class ElenaService:
    """
    public interface ElenaService
    
        Service with methods specific to the ELENA accelerator. It allows retrieve and save ELENA cycle structure and related
        timing information.
    """
    @typing.overload
    def findCycleStructure(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle) -> cern.lsa.domain.cern.settings.elena.ElenaCycleStructure:
        """
            Returns the current structure of the ELENA cycle.
        
            Parameters:
                lsaCycle (cern.lsa.domain.settings.StandAloneCycle): LSA cycle
        
            Returns:
                current structure of the ELENA cycle
        
            Raises:
                : if the ELENA cycle structure settings are not defined in the database or the format is corrupted.
        
            Returns cycle structure of the ELENA cycle as it was at the moment represented by given trim header.
        
            Parameters:
                lsaCycle (cern.lsa.domain.settings.StandAloneCycle): LSA cycle
                trimHeader (cern.lsa.domain.settings.TrimHeader): non-null trim header for which cycle structure should be returned
        
            Returns:
                the corresponding cycle structure
        
        
        """
        ...
    @typing.overload
    def findCycleStructure(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle, trimHeader: cern.lsa.domain.settings.TrimHeader) -> cern.lsa.domain.cern.settings.elena.ElenaCycleStructure: ...
    def findCycleStructureTrims(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle) -> java.util.List[cern.lsa.domain.settings.TrimHeader]: ...
    def findFlatTopTimeByEltag(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle, eLTAG: cern.lsa.domain.cern.settings.elena.ELTAG) -> java.time.Duration:
        """
            Method meant for YASP. For a given ELTAG, the method returns time at which the corresponding flat segment starts. The
            time is calculated by taking real RAMP segment length (length including flat parts and rounding time) and ignoring
            length of flat tops.
        
            Parameters:
                lsaCycle (cern.lsa.domain.settings.StandAloneCycle): LSA cycle
                eltag (cern.lsa.domain.cern.settings.elena.ELTAG): ELTAG
        
            Returns:
                offset from the cycle start to the start of a flat top identified with :code:`ELTAG`
        
            Raises:
                : if the given ELTAG is not assigned to any flat segment of the cycle
        
        
        """
        ...
    def findTimingProcesses(self) -> java.util.Set[cern.lsa.domain.cern.timing.TimingProcess]: ...
    def saveCycleSettings(self, trimRequest: cern.lsa.domain.settings.TrimRequest, elenaCycleStructure: cern.lsa.domain.cern.settings.elena.ElenaCycleStructure) -> cern.lsa.domain.settings.TrimResponse: ...

class ExploitationService(cern.lsa.client.common.CommonExploitationService):
    """
    public interface ExploitationService extends cern.lsa.client.common.CommonExploitationService
    
        Service to drive the hardware for which settings are stored in the setting management system.
    """
    def calculateTimeToReachNewValues(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> cern.lsa.domain.cern.exploitation.TimeToReachNewValues:
        """
            Calculate the longest time needed to perform the value changes specified in the given context settings
        
            Parameters:
                contextSettings (cern.lsa.domain.settings.ContextSettings): the settings for which to calculate the longest duration
        
            Returns:
                the calculation result
        
        
        """
        ...

class FidelService:
    """
    public interface FidelService
    
        An interface to deal with FiDeL models: finding model's component for given devices, generating calibration curves based
        on a model
    """
    def findAllCalibrations(self) -> typing.List[cern.lsa.domain.optics.Calibration]: ...
    def findAllHarmonics(self) -> typing.List[cern.lsa.domain.cern.optics.FieldHarmonic]:
        """
            Find all existing harmonics
        
            Returns:
                harmonics array, empty if no harmonics found
        
        
        """
        ...
    def findCalibrationByLogicalHardware(self, string: str) -> cern.lsa.domain.optics.Calibration: ...
    @typing.overload
    def findComponentsNames(self, string: str) -> typing.List[str]: ...
    @typing.overload
    def findComponentsNames(self, long: int) -> typing.List[str]: ...
    def findFidelModels(self) -> typing.List[cern.lsa.domain.cern.optics.FidelModel]:
        """
            Finds all existing FiDeL models (if any)
        
            Returns:
                Fidel model array, not null, empty if no model found
        
        
        """
        ...
    def findHarmonics(self, string: str, string2: str) -> typing.List[cern.lsa.domain.cern.optics.FieldHarmonic]:
        """
            Finds all harmonics components for the given device; if component is null - finds all harmonics for the given device
        
            Parameters:
                device (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the device, not null
                component (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the harmonic component, may be null
        
            Returns:
                harmonics array, empty if no harmonics found
        
        
        """
        ...
    @typing.overload
    def findModel(self, string: str) -> cern.lsa.domain.cern.optics.FidelModel:
        """
            Finds a defined model (if any) for a given device identified by its ID
        
            Parameters:
                deviceId (long): device ID
        
            Returns:
                Fidel model or null if not found
        
        cern.lsa.domain.cern.optics.FidelModel findModel (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` deviceName) throws cern.lsa.client.common.ClientException
        
            Finds a defined model (if any) for a given device
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): device ID
        
            Returns:
                Fidel model or null if not found
        
            Raises:
                cern.lsa.client.common.ClientException: 
        
        """
        ...
    @typing.overload
    def findModel(self, long: int) -> cern.lsa.domain.cern.optics.FidelModel: ...
    def generateHarmonics(self, string: str, string2: str, string3: str) -> cern.lsa.domain.cern.optics.FieldHarmonic: ...
    def generateMainCalibration(self, string: str, string2: str, calibrationFunctionTypes: cern.lsa.domain.optics.CalibrationFunctionTypes) -> cern.lsa.domain.optics.Calibration: ...
    def setActiveModel(self, stringArray: typing.List[str], long: int) -> None: ...
    def updateFieldHarmonic(self, fieldHarmonic: cern.lsa.domain.cern.optics.FieldHarmonic) -> None:
        """
        
            Parameters:
                fieldHarmonicToSave (cern.lsa.domain.cern.optics.FieldHarmonic): 
        
        """
        ...
    def updateMainCalibration(self, calibration: cern.lsa.domain.optics.Calibration) -> None:
        """
            update the main calibration curves as defined in the calibrationToSave
        
            Parameters:
                calibrationToSave (cern.lsa.domain.optics.Calibration): 
        
        """
        ...

class GenerationService(cern.lsa.client.common.CommonGenerationService):
    """
    public interface GenerationService extends cern.lsa.client.common.CommonGenerationService
    
        Service for generation: cycle and beamprocess types creation and scheduling of beamprocess types and cycle types.
    """
    @typing.overload
    def findIncorporationRanges(self, string: str, string2: str) -> java.util.List[cern.lsa.domain.settings.type.IncorporationRange]: ...
    @typing.overload
    def findIncorporationRanges(self, string: str) -> java.util.List[cern.lsa.domain.settings.type.IncorporationRange]: ...
    def previewEnergy(self, beamProcessType: cern.lsa.domain.settings.type.BeamProcessType) -> cern.accsoft.commons.value.DiscreteFunction: ...

class HyperCycleService:
    """
    @Cacheable("clientCache") public interface HyperCycleService
    
        Service for hyper-cycle and lhc-user related information
    """
    def findActiveHyperCycle(self) -> cern.lsa.domain.settings.HyperCycle:
        """
            Returns the :code:`active` hypercycle.
        
            Returns:
                the active hypercycle or :code:`null`.
        
        
        """
        ...
    def findHyperCycle(self, string: str) -> cern.lsa.domain.settings.HyperCycle:
        """
            Returns the hyper cycle with the given name, or :code:`null` if it doesn't exist.
        
            Parameters:
                hyperCycleName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the hyper cycle
        
            Returns:
                the hyper cycle of given name or :code:`null`
        
        
        """
        ...
    def findHyperCycles(self) -> java.util.Set[cern.lsa.domain.settings.HyperCycle]: ...
    def makeHyperCycleActive(self, string: str) -> None: ...
    def removeHyperCycle(self, hyperCycle: cern.lsa.domain.settings.HyperCycle) -> None: ...
    def saveHyperCycle(self, hyperCycle: cern.lsa.domain.settings.HyperCycle) -> None: ...

class IncaService:
    """
    public interface IncaService
    
        Service to expose INCA-specific information.
    """
    def findIncaPropertyFieldInfos(self, incaPropertyFieldInfosRequest: cern.lsa.domain.devices.inca.IncaPropertyFieldInfosRequest) -> java.util.Set[cern.lsa.domain.devices.inca.IncaPropertyFieldInfo]: ...
    def saveIncaPropertyFieldInfos(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.inca.IncaPropertyFieldInfo], typing.Sequence[cern.lsa.domain.devices.inca.IncaPropertyFieldInfo]]) -> None: ...

class JapcService(cern.lsa.client.common.CommonJapcService):
    """
    public interface JapcService extends cern.lsa.client.common.CommonJapcService
    
        Bridge between JAPC and LSA parameters.
    """
    ...

class KnobService(cern.lsa.client.common.CommonKnobService):
    """
    public interface KnobService extends cern.lsa.client.common.CommonKnobService
    
        Service for knob related operations.
    """
    ...

class LhcService:
    """
    public interface LhcService
    
        Dedicated to services which are LHC specific.
    """
    def calculateKfromIREF(self, map: typing.Union[java.util.Map[str, float], typing.Mapping[str, float]], double: float) -> java.util.Map[str, float]: ...
    def createFillDirectory(self, int: int) -> None: ...
    def deleteOrbit(self, ofbOrbit: cern.lsa.domain.cern.optics.ofb.OfbOrbit) -> None:
        """
            Deletes orbit form the database with corresponding overlays, but without deleting reading sets.
        
            Parameters:
                ofbOrbit (cern.lsa.domain.cern.optics.ofb.OfbOrbit): orbit to be deleted
        
        
        """
        ...
    def deleteReadingSet(self, ofbReadingSet: cern.lsa.domain.cern.optics.ofb.OfbReadingSet) -> None: ...
    def findAcceleratorModeTimingEvents(self) -> java.util.Map[cern.accsoft.commons.domain.modes.LhcAcceleratorMode, int]: ...
    def findActiveBeamMode(self) -> cern.accsoft.commons.domain.modes.LhcBeamMode: ...
    def findActiveLhcSectorMode(self, lhcSector: cern.accsoft.commons.domain.lhc.LhcSector) -> cern.accsoft.commons.domain.modes.LhcAcceleratorMode: ...
    def findActiveLhcSectorModes(self) -> java.util.Map[cern.accsoft.commons.domain.lhc.LhcSector, cern.accsoft.commons.domain.modes.LhcAcceleratorMode]: ...
    def findActiveParticleTypeRing1(self) -> cern.accsoft.commons.domain.ParticleType:
        """
            Finds the current particle type in ring 1.
        
            Returns:
                current particle type in ring 1
        
        
        """
        ...
    def findActiveParticleTypeRing2(self) -> cern.accsoft.commons.domain.ParticleType:
        """
            Finds the current particle type in ring 2.
        
            Returns:
                current particle type in ring 2
        
        
        """
        ...
    def findAllCalibrationsByDevices(self) -> java.util.Map[str, cern.lsa.domain.optics.RFCalibration]: ...
    def findBeamModeTimingEvents(self) -> java.util.Map[cern.accsoft.commons.domain.modes.LhcBeamMode, int]: ...
    def findBlmAppliedThresholds(self, string: str) -> java.util.Map[str, cern.lsa.domain.cern.devices.ThresholdsAwareBlmInfo]: ...
    def findBlmCrateInfos(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.lsa.domain.cern.devices.BlmCrateInfo]: ...
    def findBlmFamilies(self) -> java.util.Set[cern.lsa.domain.cern.devices.BlmFamily]: ...
    def findBlmInfos(self) -> java.util.Map[str, cern.lsa.domain.cern.devices.BlmInfo]: ...
    def findBlmInfosByCrate(self, string: str) -> java.util.Map[str, cern.lsa.domain.cern.devices.BlmInfo]: ...
    def findBlmRSTimes(self) -> typing.List[int]: ...
    def findCollimatorAlignmentHistory(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]], string: str, date: java.util.Date, date2: java.util.Date) -> java.util.Map[str, java.util.List[cern.lsa.domain.cern.devices.CollimatorAlignment]]: ...
    def findCollimatorAlignments(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]], string: str) -> java.util.Map[str, cern.lsa.domain.cern.devices.CollimatorAlignment]: ...
    def findCurrentFillNumber(self) -> int:
        """
            Find current LHC fill number.
        
            Returns:
                current LHC fill number
        
        
        """
        ...
    def findCurrentLhcBeamLossMap(self) -> cern.lsa.domain.cern.devices.LhcBeamLossMap: ...
    def findLHCHandShakes(self) -> java.util.Map[str, str]: ...
    def findLhcBeamLossMapBeamModeCategories(self) -> java.util.Set[str]: ...
    def findLhcBeamLossMapConfigTypes(self) -> java.util.Set[str]: ...
    def findLhcBeamLossMapHistory(self) -> java.util.List[cern.lsa.domain.cern.devices.LhcBeamLossMap.LhcBeamLossMapEntry]: ...
    def findLhcBlmExpertNamesByType(self) -> java.util.Map[str, java.util.List[str]]: ...
    def findLhcCollimatorInfos(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.lsa.domain.cern.devices.LhcCollimatorInfo]: ...
    def findMinimalBeamProcessTime(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.util.value.Pair[str, float]], typing.Sequence[cern.accsoft.commons.util.value.Pair[str, float]]]) -> java.util.List[cern.lsa.domain.cern.settings.BeamProcessTypeOpticTransitionInfo]: ...
    def findOfbOpticsTableInfo(self, opticsTable: cern.lsa.domain.optics.OpticsTable) -> cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo: ...
    def findOrbits(self) -> java.util.Set[cern.lsa.domain.cern.optics.ofb.OfbOrbit]: ...
    def findParabolicFractions(self, string: str) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Loads from database the parabolic fraction function: x - absolute time in the beam process type were an optic X starts,
            y - parabolic fraction of the function starting from optic X and finishing with the next optic..
        
        
            Returns :code:`null` if beam process type not found or had no parabolic fractions.
        
            Parameters:
                beamProcessTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of considered beam process type
        
            Returns:
                parabolic fraction function
        
        
        """
        ...
    @typing.overload
    def findReadingSets(self) -> java.util.Set[cern.lsa.domain.cern.optics.ofb.OfbReadingSet]: ...
    @typing.overload
    def findReadingSets(self, ofbReadingSetType: cern.lsa.domain.cern.optics.ofb.OfbReadingSetType) -> java.util.Set[cern.lsa.domain.cern.optics.ofb.OfbReadingSet]: ...
    def findReadingSetsWithReadings(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.cern.optics.ofb.OfbReadingSet], typing.Sequence[cern.lsa.domain.cern.optics.ofb.OfbReadingSet]]) -> java.util.Set[cern.lsa.domain.cern.optics.ofb.OfbReadingSet]: ...
    @typing.overload
    def findResidentStandAloneBeamProcessesByTime(self, long: int) -> java.util.Map[str, cern.lsa.domain.settings.StandAloneBeamProcess]: ...
    @typing.overload
    def findResidentStandAloneBeamProcessesByTime(self, long: int, long2: int) -> java.util.Map[str, java.util.Set[cern.lsa.domain.settings.StandAloneBeamProcess]]: ...
    def getRfFgcChannelMap(self) -> java.util.Map[str, cern.lsa.domain.cern.devices.RfFgcChannel]: ...
    def incrementFillNumber(self) -> int:
        """
            Increment the LHC fill number.
        
            Returns:
                new, incremented value of fill number
        
        
        """
        ...
    def makeLHCUserResident(self, string: str) -> None: ...
    def saveCollimatorAlignments(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.cern.devices.CollimatorAlignment], typing.Sequence[cern.lsa.domain.cern.devices.CollimatorAlignment]]) -> None: ...
    def saveOfbOpticsTableInfo(self, ofbOpticsTableInfo: cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo) -> None:
        """
            Update the OFB information attached to a particular optics table in persistent storage.
        
            Parameters:
                ofbOpticsTableInfos (cern.lsa.domain.cern.optics.ofb.OfbOpticsTableInfo): collection of :code:`OfbOpticsTableItemInfo`
        
            Also see:
                :code:`CommonGenerationService.saveOpticTable(OpticsTable)`
        
        
        """
        ...
    def saveOrbit(self, ofbOrbit: cern.lsa.domain.cern.optics.ofb.OfbOrbit) -> None:
        """
            Saves or updates given orbit. If the orbit is new, the method inserts new orbit and related reading sets and overlays.
            If the orbit already exists, the method will update it's attributes and will update (or create) corresponding overlays
            and reading sets using :meth:`~cern.lsa.client.LhcService.saveReadingSet`.
        
            Parameters:
                ofbOrbit (cern.lsa.domain.cern.optics.ofb.OfbOrbit): orbit to be saved or updated
        
        
        """
        ...
    def saveParabolicFractions(self, string: str, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> None:
        """
            Saves or updates in database, for the given beam process type, the given parabolic fraction function (x->time,
            y->fraction).
        
            Parameters:
                beamProcessTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of considered beam process type
                parabolicFractionsFunction (cern.accsoft.commons.value.ImmutableDiscreteFunction): 
        
        """
        ...
    def saveReadingSet(self, ofbReadingSet: cern.lsa.domain.cern.optics.ofb.OfbReadingSet) -> None: ...
    def setActiveBeamMode(self, lhcBeamMode: cern.accsoft.commons.domain.modes.LhcBeamMode) -> None: ...
    def setActiveLhcSectorMode(self, lhcSector: cern.accsoft.commons.domain.lhc.LhcSector, lhcAcceleratorMode: cern.accsoft.commons.domain.modes.LhcAcceleratorMode) -> None: ...
    def setActiveParticleTypeRing1(self, particleType: cern.accsoft.commons.domain.ParticleType) -> None:
        """
            Sets value of the current particle type for ring 1.
        
            Parameters:
                particleType (cern.accsoft.commons.domain.ParticleType): particle type value to be set for ring 1
        
        
        """
        ...
    def setActiveParticleTypeRing2(self, particleType: cern.accsoft.commons.domain.ParticleType) -> None:
        """
            Sets value of the current particle type for ring 2.
        
            Parameters:
                particleType (cern.accsoft.commons.domain.ParticleType): particle type value to be set for ring 2
        
        
        """
        ...
    def setHandshakeProperty(self, string: str, string2: str) -> None:
        """
            Set value of the given LHC handshake property.
        
            Parameters:
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): property name which should be updated
                propertyValue (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): property value to be set
        
        
        """
        ...
    def updateBeamLossMap(self, lhcBeam: cern.accsoft.commons.domain.beams.LhcBeam, string: str, string2: str, long: int, long2: int) -> None:
        """
            Updates validity period for the specified beam loss map.
        
            Parameters:
                beam (cern.accsoft.commons.domain.beams.LhcBeam): LHC beam
                configType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the type of the configuration for this beam loss map: :code:`BETATRON_HOR`, :code:`BETATRON_VER`,
                    :code:`OFFMOMENTUM_POS_DP`, :code:`OFFMOMENTUM_NEG_DP`, ...
                beamModeCategory (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the category of the beam mode, such as :code:`INJECTION`, :code:`FLATTOP`, :code:`SQUEEZED` or :code:`PHYSICS`
                validFrom (long): UTC timestamp that indicates the start of the time range for the validity of this beam loss map
                validTo (long): UTC timestamp that indicates the end of the time range for the validity of this beam loss map
        
            Raises:
                : if the specified configuration type is not defined for given beam or if the specified beam mode category is not defined
                    in the database
        
            Also see:
                :code:`BlmPersister#updateBeamLossMap(LhcBeam, String, String, long, long)`
        
        
        """
        ...

class LktimService:
    def canAddDeviceToTree(self, string: str, lktimTree: cern.lsa.domain.cern.settings.lktim.LktimTree) -> cern.lsa.domain.cern.settings.lktim.NodeAdditionCheckResult: ...
    def createNode(self, string: str) -> cern.lsa.domain.cern.settings.lktim.LktimTreeNode: ...
    def createTree(self, string: str) -> cern.lsa.domain.cern.settings.lktim.LktimTree: ...
    def deleteTree(self, lktimTree: cern.lsa.domain.cern.settings.lktim.LktimTree) -> None: ...
    def findOverlappingTreeNames(self, string: str) -> java.util.Set[str]: ...
    def findReferenceSettings(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle, lktimTree: cern.lsa.domain.cern.settings.lktim.LktimTree) -> cern.lsa.domain.cern.settings.lktim.LktimTreeSettings: ...
    def findSettings(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle, lktimTree: cern.lsa.domain.cern.settings.lktim.LktimTree) -> cern.lsa.domain.cern.settings.lktim.LktimTreeSettings: ...
    def findStatus(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.lsa.domain.cern.settings.lktim.LktimTreeStatus]: ...
    def findTimingDevices(self) -> java.util.Set[cern.lsa.domain.devices.Device]: ...
    def findTree(self, string: str) -> cern.lsa.domain.cern.settings.lktim.LktimTree: ...
    def findTreeFromHistory(self, string: str, date: java.util.Date) -> cern.lsa.domain.cern.settings.lktim.LktimTree: ...
    def findTreeNames(self) -> java.util.Set[str]: ...
    def findTreesByDeviceNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]], date: java.util.Date) -> java.util.Map[str, java.util.Set[str]]: ...
    def isTreeExisting(self, string: str) -> bool: ...
    def saveReferenceSettings(self, standAloneCycle: cern.lsa.domain.settings.StandAloneCycle, lktimTree: cern.lsa.domain.cern.settings.lktim.LktimTree) -> None: ...
    def saveSettings(self, lktimTreeSettings: cern.lsa.domain.cern.settings.lktim.LktimTreeSettings) -> None: ...
    def saveTree(self, lktimTree: cern.lsa.domain.cern.settings.lktim.LktimTree) -> cern.lsa.domain.cern.settings.lktim.LktimTree: ...

class LsaServiceLocator:
    """
    public class LsaServiceLocator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        In this version static method takes care of the configuration aspect of the system properties while builder takes care
        of overding aspect. The bad thing is that system properties are read several times.
    """
    @staticmethod
    def builder() -> 'LsaServiceLocator.LsaServiceLocatorBuilder': ...
    _get__T = typing.TypeVar('_get__T')  # <T>
    def get(self, class_: typing.Type[_get__T]) -> _get__T: ...
    def getDatabaseName(self) -> str: ...
    @staticmethod
    def getLsaServiceLocator() -> 'LsaServiceLocator': ...
    def getServerName(self) -> str: ...
    _getService__T = typing.TypeVar('_getService__T')  # <T>
    @staticmethod
    def getService(class_: typing.Type[_getService__T]) -> _getService__T: ...
    def isRbacEnabled(self) -> bool: ...
    def isTwoTier(self) -> bool: ...
    class LsaServer(java.lang.Enum['LsaServiceLocator.LsaServer']):
        AD: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        CTF: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        ISOLDE: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        SPS: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        LHC: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        PS: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        PSB: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        LEIR: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        GPN: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        ELENA: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        AWAKE: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        TESTBED: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        NEXT: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        NEXT_INCA: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        NEXT_INCA_PSB: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        NEXT_INCA_PS: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        INTEGRATION: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        DEV: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        LOCAL: typing.ClassVar['LsaServiceLocator.LsaServer'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'LsaServiceLocator.LsaServer': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['LsaServiceLocator.LsaServer']: ...
    class LsaServiceLocatorBuilder:
        def __init__(self): ...
        def accelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'LsaServiceLocator.LsaServiceLocatorBuilder': ...
        def build(self) -> 'LsaServiceLocator': ...
        def clientCacheEnabled(self, boolean: bool) -> 'LsaServiceLocator.LsaServiceLocatorBuilder': ...
        def lsaServer(self, lsaServer: 'LsaServiceLocator.LsaServer') -> 'LsaServiceLocator.LsaServiceLocatorBuilder': ...

class OpticService(cern.lsa.client.common.CommonOpticService):
    """
    @Cacheable("clientCache") public interface OpticService extends cern.lsa.client.common.CommonOpticService
    
        Service for optics related operations.
    """
    def deleteOptic(self, optic: cern.lsa.domain.optics.Optic) -> None:
        """
            Delete the specified optic (incl. optic parametrs, twisses, strengths) If the optic is still referenced (e.g. in optic
            table) the exception is thrown
        
            Parameters:
                optic (cern.lsa.domain.optics.Optic): 
        
        """
        ...
    def findConfigurationParameters(self, string: str) -> java.util.Map[str, str]: ...
    def findContextOpticsTables(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> java.util.Collection[cern.lsa.domain.optics.OpticsTable]: ...
    def saveOptic(self, optic: cern.lsa.domain.optics.Optic) -> None:
        """
            Saves a new optic into the persistent storage. The twisses for this optic have to be saved with the saveTwisses
        
            Parameters:
                newOptic (cern.lsa.domain.optics.Optic): the new optic to persist
        
            Raises:
                : if the optic already exists
        
        
        """
        ...
    def saveTwisses(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.optics.Twiss], typing.Sequence[cern.lsa.domain.optics.Twiss]]) -> None: ...
    def updateOptic(self, optic: cern.lsa.domain.optics.Optic) -> None:
        """
            Updates an optic in the persistent storage. The optic (by ID) must already exist, or an IllegalArgumentException is
            thrown. The twisses have to be updated with the updateOpticTwisses method
        
            Parameters:
                newOptic (cern.lsa.domain.optics.Optic): the new optic to persist
        
            Raises:
                : if the optic does not exist
        
        
        """
        ...
    def updateOpticForActualBeamProcess(self, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess, string: str) -> None: ...
    def updateTwisses(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.optics.Twiss], typing.Sequence[cern.lsa.domain.optics.Twiss]]) -> None: ...

class ParameterService(cern.lsa.client.common.CommonParameterService):
    """
    @Cacheable("clientCache") public interface ParameterService extends cern.lsa.client.common.CommonParameterService
    
        A class implementing this interface provides methods to retrieve parameters and their associated objects.
    
        Caches for this service should be reviewed after methods for knobs in the OpticService will be implemented properly
    """
    def findParametersInKnobs(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[str]: ...
    def findParametersInWorkingSets(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[str]: ...

class ServiceLocator:
    """
    public class ServiceLocator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A :code:`Service Locator` pattern implementation allowing to access all LSA services via appropriate LSA service
        interface.
    
        All LSA services are available via interfaces whose name follow the convention: :code:`[Function]Service`, where the
        [Function] corresponds to area of functionality provided by this service e.g. :code:`ContextService` can be used to find
        LSA contexts, to modify them or to delete them.
    
        Depending on the running mode (2-tier or 3-tier) the :meth:`~cern.lsa.client.ServiceLocator.getService` method returns
        either directly an implementing class (2-tier mode) or a remote proxy which forwards all method calls to the LSA server.
        Every application should specify in which running mode it would like to use LSA. This can be done via JVM property:
        :meth:`~cern.lsa.client.ServiceLocator.MODE_PROPERTY_NAME` (:code:`lsa.mode`).
    
    
    
    
        **Running in 2-tier mode**
    
    
        JVM properties required:
    
          - :code:`lsa.mode=2`
          - :code:`lsa.database={pro, dev, test, next}`
    
        The default value for :meth:`~cern.lsa.client.ServiceLocator.MODE_PROPERTY_NAME`
        :meth:`~cern.lsa.client.ServiceLocator.MODE_DEFAULT` (from Jan 2011 it is "3"). The :code:`lsa.database` property
        specifies which LSA database should be used - production, development, test. Value of this property should be set to one
        of values specified above. The default value for :code:`lsa.database` property is :code:`dev` (if this property is not
        set - the development database will be used).
    
    
    
    
        **Running in 3-tier mode**
    
    
        JVM properties required:
    
          - :code:`lsa.server={lhc, sps, leir, cps, psb, next, dev, gpn}`
    
        The :code:`lsa.server` *required* property specifies which LSA server should be used. For :code:`lhc, sps, leir, cps,
        psb, gpn`, the :code:`pro` database is used, for :code:`next` the :code:`next` database, and for :code:`dev` the
        :code:`dev` dababase.
    """
    JDBC_PROPERTIES: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JDBC_PROPERTIES
    
        Deprecated.
        use constants in :code:`LsaConfigurationConstants` instead
    
        Also see:
            :meth:`~constant`
    
    
    """
    DATABASE_PROPERTY_NAME: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DATABASE_PROPERTY_NAME
    
        Deprecated.
        use constants in :code:`LsaConfigurationConstants` instead
    
        Also see:
            :meth:`~constant`
    
    
    """
    SERVER_PROPERTIES: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SERVER_PROPERTIES
    
        Deprecated.
        use constants in :code:`LsaConfigurationConstants` instead
    
        Also see:
            :meth:`~constant`
    
    
    """
    SERVER_PROPERTY_NAME: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SERVER_PROPERTY_NAME
    
        Deprecated.
        use constants in :code:`LsaConfigurationConstants` instead
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROTOCOL_PROPERTY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROTOCOL_PROPERTY
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    MODE_PROPERTY_NAME: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MODE_PROPERTY_NAME
    
        Deprecated.
        use constants in :code:`LsaConfigurationConstants` instead
    
        Also see:
            :meth:`~constant`
    
    
    """
    MODE_3_TIER: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MODE_3_TIER
    
        Deprecated.
        use constants in :code:`LsaConfigurationConstants` instead
    
        Also see:
            :meth:`~constant`
    
    
    """
    MODE_2_TIER: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MODE_2_TIER
    
        Deprecated.
        use constants in :code:`LsaConfigurationConstants` instead
    
        Also see:
            :meth:`~constant`
    
    
    """
    MODE_DEFAULT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MODE_DEFAULT
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    _getService_0__T = typing.TypeVar('_getService_0__T')  # <T>
    @typing.overload
    @staticmethod
    def getService(class_: typing.Type[_getService_0__T]) -> _getService_0__T: ...
    @typing.overload
    @staticmethod
    def getService(string: str) -> typing.Any:
        """
            Returns implementation of LSA client service interface by interface name. The name may or may not contain package name
            (both ways are supported) e.g.
        
        
            :code:`ContextService contextController = (ContextService) ServiceLocator.getService("ContextService"); ParameterService
            parameterController = (ParameterService) ServiceLocator.getService("cern.lsa.client.common.ParameterService");`
        
            Parameters:
                interfaceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of LSA client controller interface
        
            Returns:
                implementation of the controller interface
        
        public static <T> T getService (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`<T> interfaceClass)
        
            Returns implementation of LSA client service interface by interface class.
        
        
            Examples: :code:`ContextService contextController = ServiceLocator.getService(ContextService.class); ParameterService
            parameterController = ServiceLocator.getService(ParameterService.class);`
        
            Parameters:
                interfaceClass (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`<T> interfaceClass): class of the LSA client controller interface
        
            Returns:
                implementation of the controller interface
        
        
        """
        ...
    @staticmethod
    def isTwoTier() -> bool: ...

class SettingService(cern.lsa.client.common.CommonSettingService):
    """
    public interface SettingService extends cern.lsa.client.common.CommonSettingService
    
        Service allowing to fetch current and historical settings for specified context.
    """
    def compareSettings(self, settingComparisonRequest: cern.lsa.domain.settings.SettingComparisonRequest) -> cern.lsa.domain.settings.SettingComparisonResponse:
        """
            Compares settings for parameters between contexts, archive versions, acquired settings and others.
        
            More specifically, it compares settings for parameters in:
        
              - Contexts
        
                  - Two beam processes
                  - Two cycles
        
              - Archive versions
              - Context to archive version
              - Context to references
              - Context to acquired settings
              - Context to acquisition parameter values
        
        
            By default, it compares the full values of the active settings for the supplied parameters. But further customization is
            possible:
        
        
              - Choose non-active settings: to compare current with last week's
              - For functions, pick a specific point in time to compare: to compare an actual beam process to a function beam process
              - Provide the exact list of parameters to compare, or just compare all the related parameters
        
        
            Find more information about the specific types of comparable contexts in the documentation of the builder of
            :code:`SettingComparisonRequest`s.
        
            As output, it produces :code:`SettingComparisonResponse`.
        
            *Javadoc copied from :code:`cern.lsa.settings.SettingFinder` on Oct 19, 2010. It may be out of sync.*
        
            Parameters:
                comparisonRequest (cern.lsa.domain.settings.SettingComparisonRequest): request for a setting comparison
        
            Returns:
                result of the comparison for every of the provided parameters
        
        
        """
        ...

class SettingsComparator:
    """
    public interface SettingsComparator
    
        Performs the settings comparison.
    """
    def compare(self, settingComparisonRequest: cern.lsa.domain.settings.SettingComparisonRequest, errorsAwareContextSettings: cern.lsa.domain.settings.ErrorsAwareContextSettings, errorsAwareContextSettings2: cern.lsa.domain.settings.ErrorsAwareContextSettings, parameterArray: typing.List[cern.lsa.domain.settings.Parameter]) -> java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingComparisonParameterResult]: ...

class SettingsLoader:
    """
    public interface SettingsLoader
    
        Responsible for loading settings from the database for given contexts, settings sources and parameters. The interface
        exists there (instead of class) to be able to mock it.
    """
    def loadSettings(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext, settingsSource: cern.lsa.domain.settings.SettingsSource, standAloneContext2: cern.lsa.domain.settings.StandAloneContext, settingsSource2: cern.lsa.domain.settings.SettingsSource, parameterArray: typing.List[cern.lsa.domain.settings.Parameter]) -> cern.accsoft.commons.util.value.Pair[cern.lsa.domain.settings.ErrorsAwareContextSettings, cern.lsa.domain.settings.ErrorsAwareContextSettings]:
        """
            Loads settings for the given contexts and parameters.
        
            Parameters:
                params (cern.lsa.domain.settings.StandAloneContext): if :code:`null` is passed - the method will load all settings for given contexts
        
            Returns:
                a pair of settings where the first element contains settings of the source context and the second element contains
                settings of the destination context
        
        
        """
        ...

class SpsService:
    """
    public interface SpsService
    
        Dedicated to expose SPS-specific functionalities.
    
        Also see:
            INCA-3551, JMON-875, BCT Markers in LSA documentation
    """
    def findBctMarkers(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> java.util.Set[cern.lsa.domain.cern.exploitation.BctMarker]: ...
    def findBctMarkersForActiveContexts(self) -> java.util.Map[str, java.util.Set[cern.lsa.domain.cern.exploitation.BctMarker]]: ...
    def findBctMarkersForResidentContexts(self) -> java.util.Map[str, java.util.Set[cern.lsa.domain.cern.exploitation.BctMarker]]: ...
    def findBctMarkersForTimingUsers(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, java.util.Set[cern.lsa.domain.cern.exploitation.BctMarker]]: ...

class TimingService(cern.lsa.client.common.CommonTimingService):
    def abortEventTable(self, eventTable: cern.lsa.domain.cern.timing.EventTable) -> None: ...
    def clearCirculatingBunchConfig(self, lhcBeam: cern.accsoft.commons.domain.beams.LhcBeam) -> None: ...
    def clearSequencerReservation(self) -> None: ...
    def continueEventTable(self, eventTable: cern.lsa.domain.cern.timing.EventTable) -> None: ...
    def deleteEventTable(self, eventTable: cern.lsa.domain.cern.timing.EventTable) -> None: ...
    def deleteInjectionBunchConfig(self, string: str) -> None: ...
    def deleteInjectionRequest(self, string: str) -> None: ...
    def deleteInjectionScheme(self, string: str) -> None: ...
    def deleteOneBunchFromCirculatingBunchConfig(self, int: int, lhcBeam: cern.accsoft.commons.domain.beams.LhcBeam) -> None: ...
    def findActiveInjectionRequest(self) -> cern.lsa.domain.cern.timing.LhcInjection: ...
    def findActiveInjectionScheme(self) -> cern.lsa.domain.cern.timing.LhcInjectionScheme: ...
    def findAllBunchPatterns(self) -> typing.List[cern.lsa.domain.cern.timing.BunchPattern]: ...
    def findAllEventTables(self) -> java.util.List[cern.lsa.domain.cern.timing.EventTable]: ...
    def findAllEventTypes(self) -> java.util.List[cern.lsa.domain.cern.timing.EventType]: ...
    def findAllInjectionBunchConfiguration(self) -> typing.List[cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration]: ...
    def findAllInjectionSchemeOnlyHeaders(self) -> java.util.List[cern.lsa.domain.cern.timing.LhcInjectionScheme]: ...
    def findAllInjectionSchemes(self) -> java.util.List[cern.lsa.domain.cern.timing.LhcInjectionScheme]: ...
    def findAllInjections(self) -> java.util.List[cern.lsa.domain.cern.timing.LhcInjection]: ...
    def findAllSchemeGroups(self) -> java.util.List[str]: ...
    def findCirculatingBunchConfiguration(self, lhcBeam: cern.accsoft.commons.domain.beams.LhcBeam) -> cern.lsa.domain.cern.timing.LhcCirculatingBunchConfiguration: ...
    def findEventTableByName(self, string: str) -> cern.lsa.domain.cern.timing.EventTable: ...
    def findEventTypeByName(self, string: str) -> cern.lsa.domain.cern.timing.EventType: ...
    def findInjectionByName(self, string: str) -> cern.lsa.domain.cern.timing.LhcInjection: ...
    def findInjectionSchemeByName(self, string: str) -> cern.lsa.domain.cern.timing.LhcInjectionScheme: ...
    def findSequencerReservation(self) -> str: ...
    def getLhcCirculatingBunchConfiguration(self, lhcBeam: cern.accsoft.commons.domain.beams.LhcBeam) -> cern.lsa.domain.cern.timing.LhcCirculatingBunchConfiguration: ...
    def getLoadedEventTableList(self) -> java.util.List[str]: ...
    def getLoadedEventTables(self) -> typing.List[cern.lsa.domain.cern.timing.LoadedEventTable]: ...
    def getReservedEventNames(self) -> typing.List[str]: ...
    def getTelegramGroupValue(self, string: str) -> int: ...
    def insertNewInjectionIntoCiculatingBunchConfig(self, lhcInjection: cern.lsa.domain.cern.timing.LhcInjection) -> None: ...
    def isInjectionConfigUsed(self, string: str) -> bool: ...
    def isInjectionRequestUsed(self, string: str) -> bool: ...
    def isSchemeExisting(self, string: str) -> bool: ...
    @typing.overload
    def loadEventTable(self, eventTable: cern.lsa.domain.cern.timing.EventTable) -> None: ...
    @typing.overload
    def loadEventTable(self, string: str) -> None: ...
    def replaceBucketsIntoCirculatingBunchConfig(self, intArray: typing.List[int], lhcBeam: cern.accsoft.commons.domain.beams.LhcBeam) -> None: ...
    def reserveSequencer(self, string: str) -> None: ...
    def saveBunchPattern(self, bunchPattern: cern.lsa.domain.cern.timing.BunchPattern) -> None: ...
    def saveEventTable(self, eventTable: cern.lsa.domain.cern.timing.EventTable) -> None: ...
    def saveInjectionBunchConfiguration(self, lhcInjectionBunchConfiguration: cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration) -> None: ...
    def saveInjectionRequest(self, lhcInjection: cern.lsa.domain.cern.timing.LhcInjection) -> None: ...
    def saveInjectionScheme(self, lhcInjectionScheme: cern.lsa.domain.cern.timing.LhcInjectionScheme) -> None: ...
    def sendEvent(self, event: cern.lsa.domain.cern.timing.Event, int: int) -> None: ...
    def sendEvents(self, set: java.util.Set[cern.lsa.domain.cern.timing.Event], int: int) -> None: ...
    def setActiveInjectionRequest(self, string: str) -> None: ...
    def setActiveInjectionScheme(self, string: str) -> None: ...
    def setTelegramGroup(self, string: str, int: int) -> None: ...
    @typing.overload
    def stopEventTable(self, eventTable: cern.lsa.domain.cern.timing.EventTable) -> None: ...
    @typing.overload
    def stopEventTable(self, string: str) -> None: ...
    @typing.overload
    def unloadEventTable(self, eventTable: cern.lsa.domain.cern.timing.EventTable) -> None: ...
    @typing.overload
    def unloadEventTable(self, string: str) -> None: ...
    def unreserveSequencer(self, string: str) -> None: ...
    def updateEventTable(self, eventTable: cern.lsa.domain.cern.timing.EventTable) -> None: ...
    def updateInjectionBunchCongig(self, lhcInjectionBunchConfiguration: cern.lsa.domain.cern.timing.LhcInjectionBunchConfiguration) -> None: ...
    def updateInjectionRequestBeamType(self, string: str, bEAM_TYPE: cern.lsa.domain.cern.timing.enums.BEAM_TYPE) -> None: ...
    def updateStartConditionOnLoadedTable(self, string: str, string2: str, int: int, int2: int) -> None: ...

class TrimService(cern.lsa.client.common.CommonTrimService):
    """
    public interface TrimService extends cern.lsa.client.common.CommonTrimService
    
        An object implementing this interface provides the implementation of the trim of a value.
    """
    ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client")``.

    AcceleratorService: typing.Type[AcceleratorService]
    AdService: typing.Type[AdService]
    ArchiveReferenceService: typing.Type[ArchiveReferenceService]
    CacheService: typing.Type[CacheService]
    ClientApplicationConfig: typing.Type[ClientApplicationConfig]
    ContextService: typing.Type[ContextService]
    DeviceService: typing.Type[DeviceService]
    ElenaService: typing.Type[ElenaService]
    ExploitationService: typing.Type[ExploitationService]
    FidelService: typing.Type[FidelService]
    GenerationService: typing.Type[GenerationService]
    HyperCycleService: typing.Type[HyperCycleService]
    IncaService: typing.Type[IncaService]
    JapcService: typing.Type[JapcService]
    KnobService: typing.Type[KnobService]
    LhcService: typing.Type[LhcService]
    LktimService: typing.Type[LktimService]
    LsaServiceLocator: typing.Type[LsaServiceLocator]
    OpticService: typing.Type[OpticService]
    ParameterService: typing.Type[ParameterService]
    ServiceLocator: typing.Type[ServiceLocator]
    SettingService: typing.Type[SettingService]
    SettingsComparator: typing.Type[SettingsComparator]
    SettingsLoader: typing.Type[SettingsLoader]
    SpsService: typing.Type[SpsService]
    TimingService: typing.Type[TimingService]
    TrimService: typing.Type[TrimService]
    common: cern.lsa.client.common.__module_protocol__
    reference: cern.lsa.client.reference.__module_protocol__
    rest: cern.lsa.client.rest.__module_protocol__
    spi: cern.lsa.client.spi.__module_protocol__
    test: cern.lsa.client.test.__module_protocol__
