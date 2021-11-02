import cern.accsoft.commons.domain
import cern.japc.core
import cern.japc.value
import cern.lsa.client.common.cache
import cern.lsa.client.common.japc
import cern.lsa.client.common.spi
import cern.lsa.client.common.test
import cern.lsa.domain
import cern.lsa.domain.commons
import cern.lsa.domain.devices
import cern.lsa.domain.devices.type
import cern.lsa.domain.exploitation
import cern.lsa.domain.exploitation.command
import cern.lsa.domain.generation
import cern.lsa.domain.optics
import cern.lsa.domain.settings
import cern.lsa.domain.settings.parameter.relation
import cern.lsa.domain.settings.parameter.type.relation
import cern.lsa.domain.settings.type
import cern.lsa.domain.trim.rules.makerule
import java.lang
import java.util
import typing



class ClientException(cern.lsa.domain.LsaException):
    """
    public class ClientException extends cern.lsa.domain.LsaException
    
        A general exception that is the root of all exceptions occuring in the business of the application.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class CommonAcceleratorService:
    """
    @Cacheable("clientCache") public interface CommonAcceleratorService
    
        Service for operations related to fetching and manipulating information about the accelerators (such as accelerator
        zones, particle transfers, ...).
    """
    def findAccelerator(self, string: str) -> cern.accsoft.commons.domain.Accelerator:
        """
            Returns accelerator with specified name.
        
            Parameters:
                acceleratorName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                :code:`Accelerator` or :code:`null` if it can't be found
        
        
        """
        ...
    def findAccelerators(self) -> java.util.Set[cern.accsoft.commons.domain.Accelerator]: ...

class CommonArchiveReferenceService:
    """
    public interface CommonArchiveReferenceService
    
        A service that allows retrieval, creation, modification and deletion of setting archives and retrieval and updates of
        setting reference values.
    
        Also see:
            :code:`Archive`
    """
    def createArchive(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext, string: str, string2: str) -> cern.lsa.domain.settings.Archive:
        """
            Creates a new archive for all parameters in the given stand-alone context, with given name, description and version =
            1.0.
        
            The created archive will contain all the active (current) settings of the specified context.
        
            Parameters:
                standAloneContext (cern.lsa.domain.settings.StandAloneContext): the non null context for which the archive should be created
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the non null name of the new archive
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the non null description of version 1.0 of the archive
        
            Returns:
                created archive
        
            Raises:
                : in case there are no settings associated with given context or there is already an archive with specified name (for this
                    context)
        
        
        """
        ...
    def createArchiveVersion(self, archive: cern.lsa.domain.settings.Archive, string: str, stringArray: typing.List[str]) -> cern.lsa.domain.settings.Archive: ...
    def deleteArchive(self, archive: cern.lsa.domain.settings.Archive) -> None:
        """
            Deletes the specified archive with all its versions.
        
            Parameters:
                archive (cern.lsa.domain.settings.Archive): the archive to be deleted
        
        
        """
        ...
    def deleteArchiveVersion(self, archiveVersion: cern.lsa.domain.settings.ArchiveVersion) -> cern.lsa.domain.settings.Archive:
        """
            Deletes the specified archive version.
        
            Parameters:
                archiveVersion (cern.lsa.domain.settings.ArchiveVersion): the non null archive version to be deleted
        
            Returns:
                the updated archive, not containing the specified archive version
        
            Raises:
                : in case the specified version can't be deleted as it is the last one of this archive. In such case
                    :meth:`~cern.lsa.client.common.CommonArchiveReferenceService.deleteArchive` method should be used instead.
        
        
        """
        ...
    def findArchiveById(self, long: int) -> cern.lsa.domain.settings.Archive:
        """
            Returns archive with given ID.
        
            Parameters:
                archiveId (long): the identifier of the archive
        
            Returns:
                archive with specified ID or :code:`null` if not found
        
            Also see:
                :code:`IdentifiedEntity.getId()`
        
        
        """
        ...
    @typing.overload
    def findArchiveSettings(self, archiveVersion: cern.lsa.domain.settings.ArchiveVersion) -> cern.lsa.domain.settings.CompositeContextSettings:
        """
            Returns an :code:`CompositeContextSettings` object for the given archive version and all parameters associated with it.
        
            Parameters:
                archiveVersion (cern.lsa.domain.settings.ArchiveVersion): the non null :code:`archiveVersion` of the considered archive
        
            Returns:
                :code:`CompositeContextSettings` for given version, containing settings for all or specified parameters
        
            Raises:
                cern.lsa.domain.settings.ParameterNotFoundException: if one or more of specified parameters is not defined in LSA
        
        
        """
        ...
    @typing.overload
    def findArchiveSettings(self, archiveVersion: cern.lsa.domain.settings.ArchiveVersion, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.settings.CompositeContextSettings: ...
    def findArchives(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> java.util.List[cern.lsa.domain.settings.Archive]: ...
    def findParametersWithoutSettings(self, archiveVersion: cern.lsa.domain.settings.ArchiveVersion, stringArray: typing.List[str]) -> java.util.Set[str]: ...
    @typing.overload
    def findReferenceValues(self, drivableContext: cern.lsa.domain.settings.DrivableContext) -> cern.lsa.domain.settings.CompositeContextSettings:
        """
            Returns a :code:`CompositeContextSettings` object with reference values for specified drivable context and all
            parameters associated with the particle transfers within this context
        
            Note that values for non-multiplexed parameters will be looked up in the associated non-multiplexed context.
        
            Parameters:
                drivableContext (cern.lsa.domain.settings.DrivableContext): the non null drivable context for which reference value should be returned
        
            Returns:
                :code:`CompositeContextSettings` object, containing settings for multiplexed and non-multiplexed parameters
        
        
        """
        ...
    @typing.overload
    def findReferenceValues(self, drivableContext: cern.lsa.domain.settings.DrivableContext, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.settings.CompositeContextSettings: ...
    def restoreArchive(self, archiveVersion: cern.lsa.domain.settings.ArchiveVersion, stringArray: typing.List[str]) -> cern.lsa.domain.settings.SettingsRestoreStatus: ...
    def restoreReferences(self, drivableContext: cern.lsa.domain.settings.DrivableContext, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.lsa.domain.settings.SettingsRestoreStatus: ...
    def saveReferenceValues(self, drivableContext: cern.lsa.domain.settings.DrivableContext, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[str]: ...
    def updateArchiveName(self, archive: cern.lsa.domain.settings.Archive, string: str) -> cern.lsa.domain.settings.Archive:
        """
            Updates name of the specified archive.
        
            Parameters:
                archive (cern.lsa.domain.settings.Archive): the non null archive to be updated
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the new (non null) name of the archive
        
            Returns:
                the updated (renamed) archive
        
            Raises:
                : in case there is already an archive with specified name (for this context)
        
            Also see:
                :code:`Named.getName()`
        
        
        """
        ...
    def updateArchiveVersionDescription(self, archiveVersion: cern.lsa.domain.settings.ArchiveVersion, string: str) -> cern.lsa.domain.settings.Archive:
        """
            Updates description of the specified archive version.
        
            Parameters:
                archiveVersion (cern.lsa.domain.settings.ArchiveVersion): the non null header of archive.
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the non null description of new archive
        
            Returns:
                the updated archive containing the version with the new description
        
            Also see:
                :code:`ArchiveVersion.getDescription()`
        
        
        """
        ...

class CommonCacheService:
    """
    public interface CommonCacheService
    
        A service that allows to clear all caches on the server-side.
    """
    def clearAll(self) -> None:
        """
            Clears all server caches.
        
        """
        ...

class CommonContextService:
    """
    @Cacheable("clientCache") public interface CommonContextService
    
        Service for context-related information: beam processes, cycles, hypercycles, cycle to user mappings...
    """
    def findAcceleratorUser(self, acceleratorUsersRequest: cern.lsa.domain.settings.AcceleratorUsersRequest) -> cern.lsa.domain.settings.AcceleratorUser: ...
    def findAcceleratorUsers(self, acceleratorUsersRequest: cern.lsa.domain.settings.AcceleratorUsersRequest) -> java.util.Set[cern.lsa.domain.settings.AcceleratorUser]: ...
    def findBeamProcessPurposes(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.settings.type.BeamProcessPurpose]: ...
    def findContextCategories(self) -> java.util.Set[cern.lsa.domain.settings.ContextCategory]: ...
    def findDefaultBeamProcessPurpose(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> cern.lsa.domain.settings.type.BeamProcessPurpose:
        """
            Returns default :code:`BeamProcessPurpose`.
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): The :code:`Accelerator` for which to fetch the default :code:`BeamProcessPurpose`. Must not be null.
        
            Returns:
                default :code:`BeamProcessPurpose`
        
        
        """
        ...
    def findDefaultContextCategory(self) -> cern.lsa.domain.settings.ContextCategory:
        """
            Returns default context category.
        
            Returns:
                default context category
        
        
        """
        ...
    def findDrivableContextByAcceleratorUser(self, acceleratorUser: cern.lsa.domain.settings.AcceleratorUser) -> cern.lsa.domain.settings.DrivableContext:
        """
            Retrieves :code:`DrivableContext` where this user name is assigned to.
        
            Parameters:
                acceleratorUser (cern.lsa.domain.settings.AcceleratorUser): acceleratorUser to search for
        
            Returns:
                DrivableContext
        
        
        """
        ...
    def findDrivableContextByUser(self, string: str) -> cern.lsa.domain.settings.DrivableContext: ...
    def findResidentContexts(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.settings.StandAloneContext]: ...
    def findResidentNonMultiplexedContext(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> cern.lsa.domain.settings.StandAloneContext:
        """
            Retrieves the non-multiplexed context that is resident for the given accelerator.
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): the accelerator
        
            Returns:
                resident non-multiplexed context for given accelerator or :code:`null` if not defined
        
            Also see:
                :code:`)`
        
        
        """
        ...
    def findStandAloneBeamProcess(self, string: str) -> cern.lsa.domain.settings.StandAloneBeamProcess:
        """
            Returns the stand-alone beam process with the given name, or :code:`null` if it doesn't exist.
        
            Parameters:
                beamProcessName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the beam process
        
            Returns:
                the beam process with given name or :code:`null`
        
        
        """
        ...
    @typing.overload
    def findStandAloneBeamProcesses(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.settings.StandAloneBeamProcess]: ...
    @typing.overload
    def findStandAloneBeamProcesses(self, standAloneBeamProcessesRequest: cern.lsa.domain.settings.StandAloneBeamProcessesRequest) -> java.util.Set[cern.lsa.domain.settings.StandAloneBeamProcess]: ...
    def findStandAloneContextByAcceleratorUser(self, acceleratorUser: cern.lsa.domain.settings.AcceleratorUser) -> cern.lsa.domain.settings.StandAloneContext: ...
    def findStandAloneContextByUser(self, string: str) -> cern.lsa.domain.settings.StandAloneContext: ...
    def findStandAloneContexts(self, standAloneContextsRequest: cern.lsa.domain.settings.StandAloneContextsRequest) -> java.util.Set[cern.lsa.domain.settings.StandAloneContext]: ...
    def findStandAloneCycle(self, string: str) -> cern.lsa.domain.settings.StandAloneCycle:
        """
            Returns the stand-alone cycle with the given name, or :code:`null` if it doesn't exist.
        
            Parameters:
                cycleName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the cycle
        
            Returns:
                the cycle of given name or :code:`null`
        
        
        """
        ...
    @typing.overload
    def findStandAloneCycles(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.settings.StandAloneCycle]: ...
    @typing.overload
    def findStandAloneCycles(self, standAloneCyclesRequest: cern.lsa.domain.settings.StandAloneCyclesRequest) -> java.util.Set[cern.lsa.domain.settings.StandAloneCycle]: ...
    def findUserContextMappingHistory(self, accelerator: cern.accsoft.commons.domain.Accelerator, contextFamily: cern.lsa.domain.settings.ContextFamily, long: int, long2: int) -> java.util.List[cern.lsa.domain.settings.UserContextMapping]: ...
    def findUsers(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[str]: ...
    def saveContextToUserMapping(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.StandAloneContext], typing.Sequence[cern.lsa.domain.settings.StandAloneContext]]) -> None: ...
    def updateContext(self, context: cern.lsa.domain.settings.Context) -> None: ...

class CommonDeviceService:
    """
    @Cacheable("clientCache") public interface CommonDeviceService
    
        Service to work with devices, device groups, etc.
    """
    def deleteDeviceGroups(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceGroup], typing.Sequence[cern.lsa.domain.devices.DeviceGroup]]) -> None: ...
    def findActualDevicesByLogicalHardwareName(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, java.util.Set[cern.lsa.domain.devices.Device]]: ...
    def findCalibration(self, calibrationsRequest: cern.lsa.domain.devices.CalibrationsRequest) -> cern.lsa.domain.optics.Calibration: ...
    def findCalibrations(self, calibrationsRequest: cern.lsa.domain.devices.CalibrationsRequest) -> java.util.Set[cern.lsa.domain.optics.Calibration]: ...
    def findDevice(self, string: str) -> cern.lsa.domain.devices.Device:
        """
            Finds device by its name.
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                the device or :code:`null` if it could not be found
        
        
        """
        ...
    def findDeviceGroupTypes(self) -> java.util.Set[cern.lsa.domain.devices.DeviceGroupType]: ...
    def findDeviceGroups(self, deviceGroupsRequest: cern.lsa.domain.devices.DeviceGroupsRequest) -> java.util.Set[cern.lsa.domain.devices.DeviceGroup]: ...
    def findDeviceType(self, string: str) -> cern.lsa.domain.devices.DeviceType:
        """
            Finds device type by its name.
        
            Parameters:
                deviceTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                device type with the specified name or :code:`null` if it can't be found
        
        
        """
        ...
    def findDeviceTypes(self, deviceTypesRequest: cern.lsa.domain.devices.DeviceTypesRequest) -> java.util.Set[cern.lsa.domain.devices.DeviceType]: ...
    def findDevices(self, devicesRequest: cern.lsa.domain.devices.DevicesRequest) -> java.util.Set[cern.lsa.domain.devices.Device]: ...
    def findDevicesByGroups(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceGroup], typing.Sequence[cern.lsa.domain.devices.DeviceGroup]]) -> java.util.Map[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]]: ...
    def findLogicalHardware(self, devicesRequest: cern.lsa.domain.devices.DevicesRequest) -> java.util.Set[cern.lsa.domain.optics.LogicalHardware]: ...
    def findLogicalHardwaresByActualDeviceNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, java.util.Set[cern.lsa.domain.optics.LogicalHardware]]: ...
    def findLogicalNamesByMadStrengthNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, str]: ...
    def findMadStrengthNamesByLogicalNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, str]: ...
    def findPowerConverterInfo(self, string: str) -> cern.lsa.domain.optics.PowerConverterInfo:
        """
            Finds the PowerConverter object identified by the given name.
        
            Parameters:
                powerConverterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the power converter to retrieve.
        
            Returns:
                the :code:`PowerConverterInfo`
        
        
        """
        ...
    def findPropertyFields(self, propertyFieldsRequest: cern.lsa.domain.devices.type.PropertyFieldsRequest) -> java.util.Set[cern.lsa.domain.devices.type.PropertyField]: ...
    def findPropertyVersions(self, propertyVersionsRequest: cern.lsa.domain.devices.type.PropertyVersionsRequest) -> java.util.SortedMap[cern.lsa.domain.devices.DeviceTypeVersion, java.util.Set[cern.lsa.domain.devices.type.PropertyVersion]]: ...
    def saveDeviceGroup(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup) -> None: ...
    def saveDeviceGroupDevices(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.Device], typing.Sequence[cern.lsa.domain.devices.Device]]) -> None: ...
    def saveLogicalHardware(self, logicalHardware: cern.lsa.domain.optics.LogicalHardware) -> None: ...
    def setActiveCalibration(self, string: str, string2: str) -> None: ...

class CommonExploitationService:
    """
    public interface CommonExploitationService
    
        Service to drive the hardware for which settings are stored in the setting management system.
    """
    def drive(self, driveRequest: cern.lsa.domain.exploitation.DriveRequest) -> cern.lsa.domain.exploitation.DriveResult:
        """
            Drives settings to the hardware. The request argument must be created using :code:`DriveRequestBuilder`. See JavaDoc of
            :code:`this class` for details of how to create a valid :code:`DriveRequest`.
        
        
        
        
            As of the refactoring of 2014, this method does not throw :code:`DriveException` anymore. To find out if there were
            errors during drive, check :code:`DriveResult.containsErrors()`.
        
            Parameters:
                request (cern.lsa.domain.exploitation.DriveRequest): Request containing all necessary information for the drive
        
            Returns:
                Status of the drive. If the drive is not allowed (i.e.: non-PRO database is used), the :code:`DriveResult` will contain
                an exception with a message that explains this error for every :code:`Parameter`.
        
        
        """
        ...
    def executeHwCommand(self, hwCommandExecutionRequest: cern.lsa.domain.exploitation.command.HwCommandExecutionRequest) -> cern.lsa.domain.exploitation.command.HwCommandExecutionResponse:
        """
            Executes the command identified in the request with the parameter value given along the request.
        
            Parameters:
                request (cern.lsa.domain.exploitation.command.HwCommandExecutionRequest): the request identifying the command to execute and providing the value of the command parameters.
        
            Returns:
                a response providing the result of the execution of the command.
        
        
        """
        ...
    def findHwCommands(self, hwCommandsRequest: cern.lsa.domain.exploitation.command.HwCommandsRequest) -> java.util.Set[cern.lsa.domain.exploitation.command.HwCommand]: ...
    def performSettingsCheck(self, settingsOnlineCheckRequest: cern.lsa.domain.exploitation.SettingsOnlineCheckRequest) -> java.util.List[cern.japc.core.FailSafeParameterValue]: ...
    def readHardwareValues(self, readHardwareRequest: cern.lsa.domain.exploitation.ReadHardwareRequest) -> java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.exploitation.FailSafeImmutableValue]: ...

class CommonGenerationService:
    """
    public interface CommonGenerationService
    
        Service for generation: cycle and beamprocess types creation and scheduling of beamprocess types.
    """
    def cloneStandAloneContext(self, standAloneContextCloneRequest: cern.lsa.domain.settings.StandAloneContextCloneRequest) -> cern.lsa.domain.settings.StandAloneContext: ...
    def createStandAloneContext(self, standAloneContextCreationRequest: cern.lsa.domain.settings.StandAloneContextCreationRequest) -> cern.lsa.domain.settings.StandAloneContext: ...
    def deleteContextType(self, contextType: cern.lsa.domain.settings.type.ContextType) -> None: ...
    def deleteStandAloneContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> None: ...
    def deleteValueGeneratorDefinitions(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.generation.ValueGeneratorDefinition], typing.Sequence[cern.lsa.domain.generation.ValueGeneratorDefinition]]) -> None: ...
    def findAllAvailableValueGenerators(self) -> java.util.Set[cern.lsa.domain.generation.ValueGeneratorInfo]: ...
    def findAllParticleTypes(self) -> java.util.Set[cern.accsoft.commons.domain.ParticleType]: ...
    def findBeamProcessType(self, string: str) -> cern.lsa.domain.settings.type.BeamProcessType: ...
    def findBeamProcessTypeAttributeDefinitions(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition]: ...
    def findBeamProcessTypeOpticTable(self, string: str) -> cern.lsa.domain.optics.OpticsTable: ...
    def findBeamProcessTypes(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.settings.type.BeamProcessType]: ...
    def findContextNamesByType(self, contextType: cern.lsa.domain.settings.type.ContextType) -> java.util.Set[str]: ...
    def findCycleType(self, string: str) -> cern.lsa.domain.settings.type.CycleType: ...
    def findCycleTypeAttributeDefinitions(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.commons.AttributeDefinition]: ...
    def findCycleTypes(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.settings.type.CycleType]: ...
    def findIncorporationRanges(self, string: str) -> java.util.List[cern.lsa.domain.settings.type.IncorporationRange]: ...
    def findIncorporationRules(self) -> java.util.List[cern.lsa.domain.settings.type.IncorporationRuleDescriptor]: ...
    def findStandAloneContexAttributeDefinitions(self, contextFamily: cern.lsa.domain.settings.ContextFamily, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.commons.AttributeDefinition]: ...
    def findValueGeneratorConfigInfo(self, parameter: cern.lsa.domain.settings.Parameter) -> cern.lsa.domain.generation.ValueGeneratorConfigInfo: ...
    def findValueGeneratorDefinitions(self, valueGeneratorDefinitionsRequest: cern.lsa.domain.generation.ValueGeneratorDefinitionsRequest) -> java.util.Set[cern.lsa.domain.generation.ValueGeneratorDefinition]: ...
    def generateActualBeamProcess(self, beamProcess: cern.lsa.domain.settings.BeamProcess, int: int) -> cern.lsa.domain.settings.StandAloneBeamProcess: ...
    def generateSettings(self, settingsGenerationRequest: cern.lsa.domain.settings.SettingsGenerationRequest) -> cern.lsa.domain.settings.TrimResponse: ...
    def regenerateActualBeamProcess(self, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess, string: str) -> None:
        """
            Regenerates settings of the given actual beam process.
        
            Parameters:
                actualBeamProcess (cern.lsa.domain.settings.StandAloneBeamProcess): the actual beam process to regenerate
                trimDescription (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): optional trim comment to be used for the trim entry that will be created. If not given, the method will use
                    '(Re)Generated from [sourceBeamProcessName]'
        
        
        """
        ...
    def saveBeamProcessType(self, beamProcessType: cern.lsa.domain.settings.type.BeamProcessType) -> None: ...
    def saveCycleType(self, cycleType: cern.lsa.domain.settings.type.CycleType) -> None: ...
    def saveIncorporationRanges(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.type.IncorporationRange], typing.Sequence[cern.lsa.domain.settings.type.IncorporationRange]], string: str) -> None: ...
    def saveOpticTable(self, opticsTable: cern.lsa.domain.optics.OpticsTable) -> None:
        """
            save the opticsTable items in the database
        
            Parameters:
                opticsTable (cern.lsa.domain.optics.OpticsTable): 
        
        """
        ...
    def saveValueGeneratorDefinitions(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.generation.ValueGeneratorDefinition], typing.Sequence[cern.lsa.domain.generation.ValueGeneratorDefinition]]) -> None: ...

class CommonJapcService:
    """
    public interface CommonJapcService
    
        Bridge between JAPC and LSA parameters.
    """
    def getValue(self, string: str, selector: cern.japc.core.Selector) -> cern.japc.core.AcquiredParameterValue: ...
    def getValues(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]], selector: cern.japc.core.Selector) -> java.util.List[cern.japc.core.FailSafeParameterValue]: ...
    def setValue(self, string: str, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue) -> None: ...

class CommonKnobService:
    """
    public interface CommonKnobService
    
        Service for knob related operations.
    """
    def deactivateKnob(self, string: str) -> None:
        """
            Deactivates a knob, i.e. it will be associated with the group "NOT_USED". The parameter itself and all settings continue
            to exist.
        
            Parameters:
                knobName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of knob to deactivate
        
        
        """
        ...
    def deleteKnob(self, string: str) -> None:
        """
            Deletes a knob. It removes all associated values (that is, all related entries in the *knobs* table), the corresponding
            parameter and parameter relations to its components, and all associated settings.
        
            Note that it does not delete the parameters that hold the related knob components.
        
            Parameters:
                knobName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the knob that is to be deleted
        
            Raises:
                : if the knob is not found
                : if the knob is protected or does not exist
        
        
        """
        ...
    def findKnob(self, string: str) -> cern.lsa.domain.settings.Knob:
        """
            Finds knob by its name.
        
            Parameters:
                knobName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                the knob or :code:`null` if it could not be found
        
        
        """
        ...
    def findKnobs(self, parametersRequest: cern.lsa.domain.settings.ParametersRequest) -> java.util.Set[cern.lsa.domain.settings.Knob]: ...
    def saveKnob(self, knob: cern.lsa.domain.settings.Knob) -> cern.lsa.domain.settings.Knob:
        """
            Saves the knob structure and values. This method can be used for both new knob creation and existing knob modification.
        
            Parameters:
                knob (cern.lsa.domain.settings.Knob): 
            Returns:
                the saved knob (to be used after new knob creation)
        
        
        """
        ...

class CommonOpticService:
    """
    @Cacheable("clientCache") public interface CommonOpticService
    
        Service for optics related operations.
    """
    def deleteMeasuredTwiss(self, measuredTwissArray: typing.List[cern.lsa.domain.optics.MeasuredTwiss]) -> int:
        """
            Deletes twiss measurements from the permanent storage.
        
            It is suggested to use the methods in the twiss finder, then filter the measurements that are to be deleted (with the
            appropriate helper methods, such as those in the :code:`TwissHelper`), and only then pass them as an array to this
            method for them to be deleted. That is, the selection of the twiss measurements to be deleted must be done before
            calling this method. Find some examples in the unit tests.
        
            *Javadoc copied from :code:`TwissPersister#deleteMeasuredTwiss(MeasuredTwiss...)`.*
        
            Parameters:
                measuredTwiss (cern.lsa.domain.optics.MeasuredTwiss...): one or several measurements for a twiss at a given energy
        
            Returns:
                number of twiss measurements that were deleted
        
        
        """
        ...
    def findElement(self, string: str) -> cern.lsa.domain.optics.Element:
        """
            Returns the element with the given name, or :code:`null` if it doesn't exist.
        
            Parameters:
                elementName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                element with specified name or :code:`null` if it can't be found
        
        
        """
        ...
    def findElements(self, elementsRequest: cern.lsa.domain.optics.ElementsRequest) -> java.util.Set[cern.lsa.domain.optics.Element]: ...
    @typing.overload
    def findMeasuredTwiss(self, twiss: cern.lsa.domain.optics.Twiss) -> java.util.List[cern.lsa.domain.optics.MeasuredTwiss]: ...
    @typing.overload
    def findMeasuredTwiss(self, string: str) -> java.util.List[cern.lsa.domain.optics.MeasuredTwiss]: ...
    def findOpticById(self, long: int) -> cern.lsa.domain.optics.Optic:
        """
            Returns the optic with the given ID, or :code:`null` if it doesn't exist.
        
            Parameters:
                opticId (long): the ID of the optic
        
            Returns:
                optic of the given ID or :code:`null`
        
        
        """
        ...
    def findOpticByName(self, string: str) -> cern.lsa.domain.optics.Optic:
        """
            Returns the optic with the given name, or :code:`null` if it doesn't exist.
        
            Parameters:
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the optic
        
            Returns:
                optic of the given name or :code:`null`
        
        
        """
        ...
    def findOpticInBeamProcessType(self, string: str, int: int) -> cern.lsa.domain.optics.Optic:
        """
            Finds the optic for a given beam process type name and a given point in time.
        
            Parameters:
                beamProcessTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the beam process type
                time (int): time in the range of beam process type
        
            Returns:
                optic configured for given beam process at specified time
        
        
        """
        ...
    def findOpticNames(self, opticsRequest: cern.lsa.domain.optics.OpticsRequest) -> java.util.Set[str]: ...
    def findOptics(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[cern.lsa.domain.optics.Optic]: ...
    def findOpticsTables(self, opticsTablesRequest: cern.lsa.domain.optics.OpticsTablesRequest) -> java.util.Map[str, cern.lsa.domain.optics.OpticsTable]: ...
    def findTwisses(self, twissesRequest: cern.lsa.domain.optics.TwissesRequest) -> java.util.Set[cern.lsa.domain.optics.Twiss]: ...
    def insertMeasuredTwiss(self, measuredTwissArray: typing.List[cern.lsa.domain.optics.MeasuredTwiss]) -> None:
        """
            Inserts a new twiss measurement into the permanent storage.
        
            *Javadoc copied from :code:`TwissPersister#insertMeasuredTwiss(MeasuredTwiss...)`.*
        
            Parameters:
                measuredTwiss (cern.lsa.domain.optics.MeasuredTwiss...): measurements for a twiss at a given energy
        
        
        """
        ...
    def renameOptic(self, string: str, string2: str) -> None: ...
    def saveElements(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.optics.Element], typing.Sequence[cern.lsa.domain.optics.Element]]) -> None: ...
    def setElementsObsolete(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.optics.Element], typing.Sequence[cern.lsa.domain.optics.Element]]) -> None: ...
    def updateElementName(self, string: str, string2: str) -> None:
        """
            update the name of an existing element with a new name
        
            Parameters:
                actualName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`):         newName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
        
        """
        ...
    def updateElements(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.optics.Element], typing.Sequence[cern.lsa.domain.optics.Element]]) -> None: ...

class CommonParameterService:
    """
    @Cacheable("clientCache") public interface CommonParameterService
    
        A class implementing this interface provides methods to retrieve parameters and their associated objects.
    
        Caches for this service should be reviewed after methods for knobs in the OpticService will be implemented properly
    """
    def addParametersToParameterGroup(self, parameterGroup: cern.lsa.domain.settings.ParameterGroup, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> None: ...
    def deleteCriticalProperty(self, propertyVersion: cern.lsa.domain.devices.type.PropertyVersion, device: cern.lsa.domain.devices.Device) -> None: ...
    def deleteParameterGroup(self, long: int) -> None: ...
    def deleteParameterRelations(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.parameter.relation.ParameterRelation], typing.Sequence[cern.lsa.domain.settings.parameter.relation.ParameterRelation]]) -> None: ...
    def deleteParameterTypeRelations(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation], typing.Sequence[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation]]) -> None: ...
    def deleteParameterTypes(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> None: ...
    def deleteParameters(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> None: ...
    def findAllAvailableMakerules(self) -> java.util.Set[cern.lsa.domain.trim.rules.makerule.MakeRuleInfo]: ...
    def findAllHierarchies(self) -> java.util.List[str]: ...
    def findAllParameterTypes(self) -> java.util.Set[cern.lsa.domain.settings.ParameterType]: ...
    def findCommonHierarchyNames(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> java.util.Set[str]: ...
    def findHierarchyNames(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> java.util.Set[str]: ...
    def findMakeRuleForParameterRelation(self, parameterRelation: cern.lsa.domain.settings.parameter.relation.ParameterRelation) -> cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo:
        """
            Finds the information about the makerule translating a setting from a given parameter to another parameter
        
            Parameters:
                parameterRelation (cern.lsa.domain.settings.parameter.relation.ParameterRelation): non-null parameter defining the searched makerule
        
            Returns:
                the non-null :code:`MakeRuleConfigInfo` containing the configuration status (
                :code:`MakeRuleConfigInfo.MakeRuleConfigStatus`).
        
        
        """
        ...
    def findParameterByName(self, string: str) -> cern.lsa.domain.settings.Parameter:
        """
            Returns the parameter object identified by the given name or null if no parameter of that name can be found
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the non null name of the parameter to retrieve
        
            Returns:
                the parameter identified by the name or null if the name does not match any existing parameter
        
        
        """
        ...
    def findParameterGroupsByAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.settings.ParameterGroup]: ...
    def findParameterRelationInfos(self, parameterRelationInfosRequest: cern.lsa.domain.settings.parameter.relation.ParameterRelationInfosRequest) -> java.util.Set[cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo]: ...
    def findParameterTrees(self, parameterTreesRequest: cern.lsa.domain.settings.ParameterTreesRequest) -> java.util.Set[cern.lsa.domain.settings.ParameterTreeNode]: ...
    def findParameterTypeRelationInfos(self, parameterTypeRelationInfosRequest: cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfosRequest) -> java.util.Set[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo]: ...
    def findParameterTypes(self, parameterTypesRequest: cern.lsa.domain.settings.ParameterTypesRequest) -> java.util.Set[cern.lsa.domain.settings.ParameterType]: ...
    def findParameters(self, parametersRequest: cern.lsa.domain.settings.ParametersRequest) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def findParametersByDeviceProperty(self, string: str) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def findParametersForEditing(self, parametersRequest: cern.lsa.domain.settings.ParametersRequest) -> java.util.Set[cern.lsa.domain.settings.ParameterForEditing]: ...
    def findParametersWithSettings(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def findParametersWithoutSettings(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getMaxDelta(self, parameter: cern.lsa.domain.settings.Parameter) -> float:
        """
            Returns the maximum change (delta) that can be applied to the parameter's value when it is trimmed.
        
            Returns:
                the maximum delta of parameter or :code:`NaN` if it's not defined
        
        
        """
        ...
    def removeParametersFromParameterGroup(self, parameterGroup: cern.lsa.domain.settings.ParameterGroup, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> None: ...
    def saveCriticalProperty(self, propertyVersion: cern.lsa.domain.devices.type.PropertyVersion, device: cern.lsa.domain.devices.Device) -> None: ...
    def saveParameterGroup(self, parameterGroup: cern.lsa.domain.settings.ParameterGroup) -> None: ...
    def saveParameterRelationInfos(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo], typing.Sequence[cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo]]) -> None: ...
    def saveParameterTypeRelationInfos(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo], typing.Sequence[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo]]) -> None: ...
    def saveParameterTypes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.ParameterType], typing.Sequence[cern.lsa.domain.settings.ParameterType]]) -> None: ...
    def saveParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.ParameterAttributes], typing.Sequence[cern.lsa.domain.settings.ParameterAttributes]]) -> None: ...

class CommonServiceLocator:
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class CommonServiceLocator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Deprecated.
        use :class:`~cern.lsa.client.common.LsaConfigurationConstants` instead
    """
    JDBC_PROPERTIES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JDBC_PROPERTIES
    
        Deprecated.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DATABASE_PROPERTY_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DATABASE_PROPERTY_NAME
    
        Deprecated.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SERVER_PROPERTIES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SERVER_PROPERTIES
    
        Deprecated.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SERVER_PROPERTY_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SERVER_PROPERTY_NAME
    
        Deprecated.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MODE_PROPERTY_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MODE_PROPERTY_NAME
    
        Deprecated.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def isTwoTier() -> bool:
        """
            Deprecated.
        
        """
        ...

class CommonSettingService:
    """
    public interface CommonSettingService
    
        Service allowing to fetch current and historical settings for specified context.
    """
    def deleteSettings(self, settingsDeletionRequest: cern.lsa.domain.settings.SettingsDeletionRequest) -> None:
        """
            Deletes settings for the given set of parameters in the given context(s).
        
            Parameters:
                settingsDeletionRequest (cern.lsa.domain.settings.SettingsDeletionRequest): object containing the description of the request
        
        
        """
        ...
    def findContextSettings(self, contextSettingsRequest: cern.lsa.domain.settings.ContextSettingsRequest) -> cern.lsa.domain.settings.ContextSettings:
        """
            Finds all the context settings associated to all beam processes corresponding to the given
            :code:`ContextSettingsRequest`.
        
        
            See also :code:`SettingFinder#findContextSettings(ContextSettingsRequest)`
        
            Parameters:
                contextSettingsRequest (cern.lsa.domain.settings.ContextSettingsRequest): the non :code:`null` contextSettingsRequest
        
            Returns:
                a non :code:`null` :code:`ContextSettings` object containing settings of all parameters
        
        
        """
        ...
    def findNotIncorporatedParameters(self, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess, int: int, beamProcess: cern.lsa.domain.settings.BeamProcess, int2: int) -> cern.lsa.domain.settings.NotIncorporatedParameters:
        """
            Finds and returns names of parameters that have different values in the source and destination beam process at specified
            points. For details see :code:`SettingFinder#findNotIncorporatedParameters(StandAloneBeamProcess, int,
            StandAloneBeamProcess, int)`.
        
        """
        ...

class CommonTimingService:
    """
    public interface CommonTimingService
    
        An object implementing this interface gives to the clients access to the timing services
    """
    ...

class CommonTrimService:
    """
    public interface CommonTrimService
    
        An object implementing this interface provides the implementation of the trim of a value.
    """
    def copySettings(self, copySettingsRequest: cern.lsa.domain.settings.CopySettingsRequest) -> cern.lsa.domain.settings.TrimResponse: ...
    def deleteTrimById(self, long: int) -> None: ...
    def findParametersAndParameterGroupsByBPsSinceTime(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.BeamProcess], typing.Sequence[cern.lsa.domain.settings.BeamProcess]], date: java.util.Date) -> java.util.Map[str, java.util.Set[str]]: ...
    def findTrimHeaders(self, trimHeadersRequest: cern.lsa.domain.settings.TrimHeadersRequest) -> java.util.List[cern.lsa.domain.settings.TrimHeader]: ...
    def findTrimmedParameters(self, long: int) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    @typing.overload
    def incorporate(self, beamProcessIncorporationRequest: cern.lsa.domain.settings.BeamProcessIncorporationRequest) -> cern.lsa.domain.settings.TrimResponse: ...
    @typing.overload
    def incorporate(self, incorporationRequest: cern.lsa.domain.settings.IncorporationRequest) -> cern.lsa.domain.settings.TrimResponse: ...
    @typing.overload
    def revertTrim(self, revertTrimRequest: cern.lsa.domain.settings.RevertTrimRequest) -> cern.lsa.domain.settings.TrimResponse: ...
    @typing.overload
    def revertTrim(self, list: java.util.List[cern.lsa.domain.settings.RevertTrimRequest]) -> java.util.List[cern.lsa.domain.settings.TrimResponse]: ...
    @typing.overload
    def trimSettings(self, trimRequest: cern.lsa.domain.settings.TrimRequest) -> cern.lsa.domain.settings.TrimResponse: ...
    @typing.overload
    def trimSettings(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.TrimRequest], typing.Sequence[cern.lsa.domain.settings.TrimRequest]]) -> java.util.List[cern.lsa.domain.settings.TrimResponse]: ...
    def updateTrimDescription(self, long: int, string: str) -> None:
        """
            Update the description of a trim identified by the given :code:`trimId`. If no trim with that id can be found, no update
            is performed.
        
            Parameters:
                trimId (long): the id of the trim to update
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the new description of the trim
        
        
        """
        ...

class LsaConfigurationConstants:
    """
    public class LsaConfigurationConstants extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    SYSPROP_DATABASE_PROPERTIES_FILENAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_DATABASE_PROPERTIES_FILENAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_DATABASE_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_DATABASE_NAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_SERVER_PROPERTIES_FILENAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_SERVER_PROPERTIES_FILENAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_SERVER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_SERVER_NAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_MODE_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_MODE_NAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    MODE_3_TIER: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MODE_3_TIER
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    MODE_2_TIER: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MODE_2_TIER
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_SERVER_SPRING_CACHE_ENABLED: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_SERVER_SPRING_CACHE_ENABLED
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class TransactionService:
    """
    public interface TransactionService
    
        Service that handles the generation of transaction ids used by the exploitation sub-system
    """
    def generateTransactionId(self) -> int:
        """
            Generates a transaction id that can be used by exploitation sub-system. This id can be set as an attribute in the
            :code:`TrimRequest` and :code:`DriveRequest`.
        
            Returns:
                the new transaction id
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.common")``.

    ClientException: typing.Type[ClientException]
    CommonAcceleratorService: typing.Type[CommonAcceleratorService]
    CommonArchiveReferenceService: typing.Type[CommonArchiveReferenceService]
    CommonCacheService: typing.Type[CommonCacheService]
    CommonContextService: typing.Type[CommonContextService]
    CommonDeviceService: typing.Type[CommonDeviceService]
    CommonExploitationService: typing.Type[CommonExploitationService]
    CommonGenerationService: typing.Type[CommonGenerationService]
    CommonJapcService: typing.Type[CommonJapcService]
    CommonKnobService: typing.Type[CommonKnobService]
    CommonOpticService: typing.Type[CommonOpticService]
    CommonParameterService: typing.Type[CommonParameterService]
    CommonServiceLocator: typing.Type[CommonServiceLocator]
    CommonSettingService: typing.Type[CommonSettingService]
    CommonTimingService: typing.Type[CommonTimingService]
    CommonTrimService: typing.Type[CommonTrimService]
    LsaConfigurationConstants: typing.Type[LsaConfigurationConstants]
    TransactionService: typing.Type[TransactionService]
    cache: cern.lsa.client.common.cache.__module_protocol__
    japc: cern.lsa.client.common.japc.__module_protocol__
    spi: cern.lsa.client.common.spi.__module_protocol__
    test: cern.lsa.client.common.test.__module_protocol__
