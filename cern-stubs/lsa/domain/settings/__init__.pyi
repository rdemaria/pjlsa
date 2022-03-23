import cern
import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.util
import cern.accsoft.commons.util.value
import cern.accsoft.commons.value
import cern.lsa.domain
import cern.lsa.domain.commons
import cern.lsa.domain.devices
import cern.lsa.domain.devices.type
import cern.lsa.domain.exploitation
import cern.lsa.domain.optics
import cern.lsa.domain.settings.factory
import cern.lsa.domain.settings.parameter
import cern.lsa.domain.settings.spi
import cern.lsa.domain.settings.type
import cern.lsa.domain.trim.tag
import com.google.common.collect
import datetime
import java.io
import java.lang
import java.time
import java.util
import typing



class AcceleratorUser(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named):
    """
    @Immutable public interface AcceleratorUser extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`, cern.accsoft.commons.util.Named
    
        Usually, an :class:`~cern.lsa.domain.settings.AcceleratorUser` is used to tag
        :class:`~cern.lsa.domain.settings.DrivableContext`s to identify their settings so they can be played at a certain timing
        event on multiplexed hardware.
    
    
        In other cases, :class:`~cern.lsa.domain.settings.AcceleratorUser`s are used for different things, like logically
        grouping :class:`~cern.lsa.domain.settings.StandAloneBeamProcess`es utilizing
        :class:`~cern.lsa.domain.settings.AcceleratorUserGroup`s, as it is being done with
        :class:`~cern.lsa.domain.settings.HyperCycle`s for LHC and actual beam processes for SPS at CERN currently.
    """
    @staticmethod
    def builder() -> 'DefaultAcceleratorUser.Builder':
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.AcceleratorUser`
        
            Returns:
                the builder
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                The :code:`Accelerator` this :class:`~cern.lsa.domain.settings.AcceleratorUser` is associated with.
        
        
        """
        ...
    def getAcceleratorUserGroup(self) -> 'AcceleratorUserGroup':
        """
        
            Returns:
                The :class:`~cern.lsa.domain.settings.AcceleratorUserGroup` that this :class:`~cern.lsa.domain.settings.AcceleratorUser`
                belongs to.
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Indicates whether this user is used for multiplexed contexts or not.
        
            Returns:
                :code:`true` if user is for multiplexed contexts, :code:`false` otherwise
        
        
        """
        ...

class AcceleratorUserGroup(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named):
    """
    @Immutable public interface AcceleratorUserGroup extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`, cern.accsoft.commons.util.Named
    
        :class:`~cern.lsa.domain.settings.AcceleratorUserGroup`s are currently used for LHC at CERN to create logical groups of
        :class:`~cern.lsa.domain.settings.AcceleratorUser`s for the operators.
    """
    @staticmethod
    def builder() -> 'DefaultAcceleratorUserGroup.Builder':
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.AcceleratorUserGroup`
        
            Returns:
                the builder
        
        
        """
        ...
    def getDescription(self) -> str: ...

class AcceleratorUsersRequest:
    """
    @Immutable public interface AcceleratorUsersRequest
    
        Request object to find AcceleratorUser(s)
    """
    @staticmethod
    def builder() -> 'DefaultAcceleratorUsersRequest.Builder':
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.AcceleratorUsersRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    @staticmethod
    def byAccelerator(accelerator: cern.accsoft.commons.domain.Accelerator) -> 'AcceleratorUsersRequest':
        """
            Creates request by accelerator
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): the accelerator for which :class:`~cern.lsa.domain.settings.AcceleratorUser`s needs to be found
        
            Returns:
                the request
        
        
        """
        ...
    @staticmethod
    def byAcceleratorAndUserName(accelerator: cern.accsoft.commons.domain.Accelerator, string: str) -> 'AcceleratorUsersRequest':
        """
            Create request by user name
        
            Parameters:
                acceleratorUserName (cern.accsoft.commons.domain.Accelerator): the user name for which :class:`~cern.lsa.domain.settings.AcceleratorUser` needs to be found
        
            Returns:
                the request
        
        
        """
        ...
    @staticmethod
    def byUserName(string: str) -> 'AcceleratorUsersRequest':
        """
            Create request by user name
        
            Parameters:
                acceleratorUserName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the user name for which :class:`~cern.lsa.domain.settings.AcceleratorUser` needs to be found
        
            Returns:
                the request
        
        
        """
        ...
    @staticmethod
    def byUserNames(iterable: java.lang.Iterable[str]) -> 'AcceleratorUsersRequest': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getAcceleratorUserGroupName(self) -> str: ...
    def getAcceleratorUserNames(self) -> java.util.Set[str]: ...
    def getIds(self) -> java.util.Set[int]: ...
    def isMultiplexed(self) -> bool: ...

class ActualBeamProcessInfo:
    """
    public interface ActualBeamProcessInfo
    
        Info about actual beam process containing the source beam process and point from which the actual beam process was
        created.
    """
    def getSourceBeamProcess(self) -> 'BeamProcess':
        """
            Returns the source beam process from which this actual beam process was created.
        
            Returns:
                the source beamProcess this actual one was created from
        
        
        """
        ...
    def getSourcePoint(self) -> int:
        """
            Returns the point in time from which this actual beam process was created.
        
            Returns:
                the point in time from which this actual beam process was created
        
        
        """
        ...

class Archive(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named, java.lang.Comparable['Archive']):
    """
    public interface Archive extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`, cern.accsoft.commons.util.Named, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.settings.Archive`>
    
        Represents a versioned, coherent set of settings for a stand-alone context.
    """
    def getLatestVersion(self) -> 'ArchiveVersion':
        """
            Returns the latest version of this archive i.e. archive version with the highest version number.
        
            Returns:
                the latest archive version
        
        
        """
        ...
    def getStandAloneContext(self) -> 'StandAloneContext':
        """
            Returns the stand-alone context that the archive is created for.
        
            Returns:
                the stand-alone context that the archive is created for
        
        
        """
        ...
    def getVersion(self, double: float) -> 'ArchiveVersion':
        """
            Returns :code:`ArchiveVersion` with specified version number. If this archive doesn't contain specified version - the
            method returns :code:`null`.
        
            Parameters:
                version (double): requested archive version e.g. 1.2
        
            Returns:
                archive version or :code:`null`
        
        
        """
        ...
    def getVersions(self) -> java.util.SortedSet['ArchiveVersion']: ...

class ArchiveVersion(java.lang.Comparable['ArchiveVersion']):
    """
    public interface ArchiveVersion extends `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.settings.ArchiveVersion`>
    
        An :code:`ArchiveVersion` represents a single version of an archive.
    """
    def getArchive(self) -> Archive:
        """
            Returns archive that this version belongs to.
        
            Returns:
                archive that this version belongs to
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Returns the creation date of the archive version.
        
            Returns:
                the creation date of the archive version
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Returns the description of the archive version.
        
            Returns:
                the description of the archive version
        
        
        """
        ...
    def getSettingCount(self) -> int:
        """
            Returns count of created settings.
        
            Returns:
                count of created settings
        
        
        """
        ...
    def getVersion(self) -> float:
        """
            Returns the version of the archive.
        
            Returns:
                the version of the archive.
        
        
        """
        ...

class BeamProcessIncorporationRequest:
    """
    public interface BeamProcessIncorporationRequest
    
        Represents a request to incorporate settings from a source beam process into a destination beam process Instances of
        this interface should be created using
        :class:`~cern.lsa.domain.settings.factory.BeamProcessIncorporationRequestBuilder`.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    def getDescription(self) -> str:
        """
        
            Returns:
                description of the trim (comment).
        
        
        """
        ...
    def getDestBeamProcess(self) -> 'BeamProcess':
        """
        
            Returns:
                beam process to incorporate into
        
        
        """
        ...
    def getDestPointInTime(self) -> float:
        """
        
            Returns:
                the point in time of destination beam process to incorporate into
        
        
        """
        ...
    def getParameters(self) -> java.util.Set['Parameter']: ...
    def getSettingPart(self) -> 'SettingPartEnum':
        """
            Returns the setting part which should be used for the incorporation. Depending on the setting part the behavior is
            following:
        
              - :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE` - indicates that
                :meth:`~cern.lsa.domain.settings.Setting.getValue` of the setting present in the
                :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest` will be compared with the destination VALUE of the
                parameter and the difference will be incorporated in the :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` of
                the resulting setting, with target value unchanged.
              - :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET` - indicates that
                :meth:`~cern.lsa.domain.settings.Setting.getValue` of the setting present in the
                :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest` will be incorporated in the
                :meth:`~cern.lsa.domain.settings.Setting.getTargetValue` of the resulting setting, with correction value unchanged.
              - :meth:`~cern.lsa.domain.settings.SettingPartEnum.CORRECTION` - indicates that
                :meth:`~cern.lsa.domain.settings.Setting.getValue` of the setting present in the
                :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest` will be incorporated in the
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` of the resulting setting, with target value unchanged.
              - :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET_AND_CORRECTION` - indicates that target of the setting present
                in the :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest` will be incorporated in the target of the
                resulting setting, and correction will be incorporated in correction of the resulting setting.
        
        
            Returns:
                the setting part which should be used for the incorporation
        
        
        """
        ...
    def getSettingsSource(self) -> 'SettingsSource':
        """
        
            Returns:
                the settings source used to retrieve settings from the source beam process
        
        
        """
        ...
    def getSourceBeamProcess(self) -> 'BeamProcess':
        """
        
            Returns:
                beam process to incorporate from
        
        
        """
        ...
    def getSourcePointInTime(self) -> float:
        """
        
            Returns:
                the point in time of source beam process to incorporate from. If the source beam process is an
                :meth:`~cern.lsa.domain.settings.StandAloneBeamProcess.isActual` then the source point-in-time is ignored
        
        
        """
        ...
    def shouldDrive(self) -> bool:
        """
            Determines whether the incorporated settings should be driven to the hardware.
        
            Note that the new settings will be driven if the stand-alone context of the
            :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getDestBeamProcess` is
            :meth:`~cern.lsa.domain.settings.StandAloneContext.isResident`.
        
            Returns:
                :code:`true` if drive should be performed
        
        
        """
        ...
    def shouldIncorporateAllParameters(self) -> bool:
        """
        
            Returns:
                :code:`true` if settings for all parameters should be incorporated, otherwise parameters are taken from
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getParameters`.
        
        
        """
        ...

class BeamProcessIntersection:
    """
    public interface BeamProcessIntersection
    
        A class implementing this interface groups a beam process name and the x-coordinate of the intersection relative to this
        beam process.
    """
    def getBeamProcess(self) -> 'BeamProcess': ...
    def getIntersectionCoordinate(self) -> float: ...

class CompositeContextSettings:
    """
    public interface CompositeContextSettings
    
        The :code:`CompositeContextSettings` is a container for set of parameter settings in a multiplexed and in a
        non-multiplexed context.
    """
    def getContextSettings(self) -> 'ContextSettings':
        """
            Returns parameter settings for multiplexed parameters stored in this object. If this :code:`CompositeContextSettings`
            doesn't contain any multiplexed settings, this method returns an empty :code:`ContextSettings` object i.e. without any
            settings.
        
            Returns:
                parameter settings for multiplexed parameters stored in this object
        
        
        """
        ...
    def getNonMultiplexedSettings(self) -> 'ContextSettings':
        """
            Returns parameter settings for non-multiplexed parameters stored in this object. If this
            :code:`CompositeContextSettings` doesn't contain any non-multiplexed settings, this method returns an empty
            :code:`ContextSettings` object i.e. without any settings.
        
            Returns:
                parameter settings for non-multiplexed parameters stored in this object
        
        
        """
        ...
    def getParameters(self) -> java.util.Set['Parameter']: ...
    def getValue(self, drivableContext: 'DrivableContext', string: str) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Returns immutable value of specified parameter and drivable context. If there is no setting for specified parameter and
            context - the method returns :code:`null`.
        
            Note that non-multiplexed parameters have to be accessed using the non-multiplexed context.
        
            Parameters:
                drivableContext (:class:`~cern.lsa.domain.settings.DrivableContext`): drivable context for which value should be returned
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the parameter for which value should be returned
        
            Returns:
                immutable value of specified parameter and context or :code:`null`
        
        
        """
        ...

class Context(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named, java.lang.Comparable['Context']):
    """
    public interface Context extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`, cern.accsoft.commons.util.Named, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.settings.Context`>
    
        Represents a context. It's a base interface extended by all concrete contexts, defining common properties.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
            Returns accelerator that this contexts belongs to.
        
            Returns:
                associated accelerator
        
        
        """
        ...
    def getContextFamily(self) -> 'ContextFamily':
        """
            Returns the context family this context belongs to. E.g. if the context is a beam process and in addition it is a
            :code:`StandAloneBeamProcess` the method returns :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS`.
        
            Returns:
                context family that this context belongs to
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Returns creation date of this context.
        
            Returns:
                the date this context was created
        
        
        """
        ...
    def getCreatorName(self) -> str:
        """
        
            Returns:
                the NICE name of the creator of this context or null if it is unknown
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Description of the context entered by the creator.
        
            Returns:
                the description of this context
        
        
        """
        ...
    def getLength(self) -> int:
        """
            Returns length of the context in milliseconds.
        
            Returns:
                the length of this context
        
        
        """
        ...
    def getModificationDate(self) -> java.util.Date:
        """
        
            Returns:
                the date this context was modified for the last time
        
        
        """
        ...
    def getModifierName(self) -> str:
        """
        
            Returns:
                the NICE name of the modifier of this context or null if it is unknown
        
        
        """
        ...
    def getParent(self) -> 'Context':
        """
            Returns the parent :code:`Context` of this context or :code:`null` if this context has no parent. The possibility to
            nest some context into another is foreseen and this method returns the parent :code:`Context` if the context is a nested
            one or :code:`null` otherwise. This value is not necessarily the same as
            :meth:`~cern.lsa.domain.settings.Contexts.getStandAloneContext`.
        
            Depending on the type of the context the returned object may be different:
        
            :code:`BeamProcess` - may return :code:`StandAloneCycle`
        
        
            :class:`~cern.lsa.domain.settings.DrivableBeamProcess` - may return
            :class:`~cern.lsa.domain.settings.BeamProductionChain` or :class:`~cern.lsa.domain.settings.Pattern`
        
        
            :code:`Cycle` :class:`~cern.lsa.domain.settings.BeamProductionChain` - may return
            :class:`~cern.lsa.domain.settings.BeamProductionChain` (a chain can be nested into another chain) or
            :class:`~cern.lsa.domain.settings.Pattern`
        
        
        
            Stand-alone contexts like :code:`StandAloneCycle`, :code:`StandAloneBeamProcess` and :code:`Pattern` return
            :code:`null`.
        
        
            Returns:
                The parent :code:`Context` or :code:`null` if none exists.
        
        
        """
        ...
    def getTypeName(self) -> str:
        """
            Returns name of the context type, that this context instance has been created from. The type of the context holds common
            characteristics of the context.
        
            Returns:
                name of associated context type
        
            Also see:
                :class:`~cern.lsa.domain.settings.type.BeamProcessType`, :class:`~cern.lsa.domain.settings.type.CycleType`
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Indicates whether this context is multiplexed or not. Apart of special, dedicated contexts that are non-multiplexed, all
            the other contexts are multiplexed.
        
            Returns:
                :code:`true` if context is multiplexed, :code:`false` otherwise
        
        
        """
        ...
    def isStandAlone(self) -> bool:
        """
            Returns :code:`true` if this context is stand-alone, and :code:`false` if the context belongs to another context.
        
            In other words this method return :code:`true` if the context is a :code:`StandAloneCycle` or
            :code:`StandAloneBeamProcess`.
        
            Returns:
                :code:`true` if the context is stand-alone, :code:`false` otherwise
        
        
        """
        ...

class ContextCategory(cern.accsoft.commons.util.Named):
    """
    public interface ContextCategory extends cern.accsoft.commons.util.Named
    
        Context category such as OPERATIONAL, MD, TEST, OBSOLETE. It is used to categorize different contexts depending on their
        usage.
    """
    def isArchived(self) -> bool:
        """
        
            Returns:
                true if the category is archived
        
        
        """
        ...

class ContextFamily(java.lang.Enum['ContextFamily']):
    """
    public enum ContextFamily extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.settings.ContextFamily`>
    
        Represents a family of contexts. :code:`StandAloneBeamProcess` belongs to family
        :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS`, :code:`StandAloneCycle` and all
        :meth:`~cern.lsa.domain.settings.StandAloneContext.getBeamProcesses` belong to family
        :meth:`~cern.lsa.domain.settings.ContextFamily.CYCLE`. :code:`BeamProductionChain` and all
        :meth:`~cern.lsa.domain.settings.BeamProductionChain.getBeamProcesses` belong to family
        :meth:`~cern.lsa.domain.settings.ContextFamily.BEAM_PRODUCTION_CHAIN`. :code:`Pattern` and all
        :code:`Pattern#getChains() its beam production chains` and
        :meth:`~cern.lsa.domain.settings.BeamProductionChain.getBeamProcesses` belong to family
        :meth:`~cern.lsa.domain.settings.ContextFamily.PATTERN`.
    """
    CYCLE: typing.ClassVar['ContextFamily'] = ...
    BEAMPROCESS: typing.ClassVar['ContextFamily'] = ...
    BEAM_PRODUCTION_CHAIN: typing.ClassVar['ContextFamily'] = ...
    PATTERN: typing.ClassVar['ContextFamily'] = ...
    @staticmethod
    def getContextFamily(string: str) -> 'ContextFamily':
        """
            Resolves :code:`ContextFamily` by `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true#name()>` or
            :meth:`~cern.lsa.domain.settings.ContextFamily.getShortName`.
        
            Parameters:
                contextFamilyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the context. Either enum name or short name
        
            Returns:
                context family with specified name
        
        
        """
        ...
    def getDisplayName(self) -> str:
        """
            Returns a display name of this context family. Display names are defined as follows:
        
              - for :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS` returns :code:`"Beam Process"`
              - for :meth:`~cern.lsa.domain.settings.ContextFamily.CYCLE` returns :code:`"Cycle"`
              - for :meth:`~cern.lsa.domain.settings.ContextFamily.BEAM_PRODUCTION_CHAIN` returns :code:`"Beam Production Chain"`
              - for :meth:`~cern.lsa.domain.settings.ContextFamily.PATTERN` returns :code:`"Pattern"`
        
        
            The display name can be used in GUI components.
        
            Returns:
                display name of this context family
        
        
        """
        ...
    def getShortName(self) -> str:
        """
            Returns a short name of this context family. Short names are defined as follows:
        
              - for :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS` returns :code:`"BP"`
              - for :meth:`~cern.lsa.domain.settings.ContextFamily.CYCLE` returns :code:`"C"`
              - for :meth:`~cern.lsa.domain.settings.ContextFamily.BEAM_PRODUCTION_CHAIN` returns :code:`"BPC"`
              - for :meth:`~cern.lsa.domain.settings.ContextFamily.PATTERN` returns :code:`"P"`
        
        
            The short name is used (among others) in database tables to identify context family.
        
            Returns:
                short name of this context family: BP, C, BC or P
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ContextFamily':
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
    def values() -> typing.List['ContextFamily']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ContextFamily c : ContextFamily.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ContextIntersections:
    """
    public interface ContextIntersections
    
        Base intersections abstraction.
    """
    def getCycleBeamProcessIntersections(self) -> java.util.SortedSet['CycleBeamProcessIntersection']: ...

class ContextOptics:
    """
    public class ContextOptics extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A class holding the optic information for all beam processes of a :class:`~cern.lsa.domain.settings.StandAloneContext`
        together with the context itself. That way, the class can compute what is the optic at any time in the context.
    """
    def __init__(self, standAloneContext: 'StandAloneContext', collection: typing.Union[java.util.Collection[cern.lsa.domain.optics.OpticsTable], typing.Sequence[cern.lsa.domain.optics.OpticsTable]]): ...
    def getActiveOpticName(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, int: int) -> str:
        """
            Computes the optic of this CONTEXT for the given particle transfer and time. The particle transfer must exist in the
            context this object is referring to. The time must be relative to the context this object is referring to.
        
            If the time specified refers to point where two beam-in beam processes connect (one ends and next one starts) the
            function returns optic related to the next beam process (unless it is the last point or next beam process is beam-out).
        
        
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): the particle transfer in which the optic has to be found for
                time (int): the time in milliseconds in the context at which the optic has to be found. In case of actual beam process, the time
                    attribute is ignored
        
            Returns:
                the optic name or null if no optic was defined at that time for the given particle transfer
        
        
        """
        ...
    def getBeamProcessOpticsTable(self, beamProcess: 'BeamProcess') -> cern.lsa.domain.optics.OpticsTable:
        """
            Returns optics table for the specified beam process.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): 
            Returns:
                optics table for the specified beam process
        
        
        """
        ...
    def getContext(self) -> 'StandAloneContext':
        """
            Returns associated context.
        
        """
        ...
    def getContextName(self) -> str:
        """
            Returns the name of the context
        
            Returns:
                the name of the context
        
        
        """
        ...

class ContextSettings:
    """
    public interface ContextSettings
    
        A container for settings for many parameters for a given context (e.g. beam process, cycle).
    """
    def addAll(self, contextSettings: 'ContextSettings') -> None:
        """
            Adds to this object all the :class:`~cern.lsa.domain.settings.ParameterSettings` contained in the specified
            :code:`ContextSettings` that are not yet present in this :code:`ContextSettings`. In other words if this container
            contains :code:`ParameterSettings` for a given parameter - it won't be added from specified :code:`ContextSettings`.
        
            Parameters:
                ctxSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): settings to be added to this container
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def builder() -> cern.lsa.domain.settings.factory.ContextSettingsBuilder:
        """
        static :class:`~cern.lsa.domain.settings.factory.ContextSettingsBuilder` builder (:class:`~cern.lsa.domain.settings.ContextSettings` original)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def builder(contextSettings: 'ContextSettings') -> cern.lsa.domain.settings.factory.ContextSettingsBuilder: ...
    def getContext(self) -> 'StandAloneContext':
        """
            Returns the context these settings are for.
        
            Returns:
                the context these settings are for
        
        
        """
        ...
    def getCurrentBeamProcesses(self) -> java.util.Set['BeamProcess']: ...
    @typing.overload
    def getCurrentSetting(self, beamProcess: 'BeamProcess', parameter: 'Parameter') -> 'Setting':
        """
            Returns the current setting for the given beam process and parameter. The setting returned is always the current one,
            whether an updated value has been given or not.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to return the setting for
        
            Returns:
                the current setting for the given beam process and parameter or null if the given beam process has no setting for the
                parameter
        
            Returns the current setting for the given beam process and parameter. The setting returned is always the current one,
            whether an updated value has been given or not.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to return the setting for
        
            Returns:
                the current setting for the given beam process and parameter or null if the given beam process has no setting for the
                parameter
        
        
        """
        ...
    @typing.overload
    def getCurrentSetting(self, beamProcess: 'BeamProcess', string: str) -> 'Setting': ...
    def getCurrentSettings(self) -> java.util.Set['Setting']: ...
    @typing.overload
    def getParameterSettings(self, parameter: 'Parameter') -> 'ParameterSettings':
        """
            Returns the parameter settings for the given parameter or null if none has been registered.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to return the setting for
        
            Returns:
                the parameter setting for the given parameter name or null
        
            Returns the parameter settings for the given parameter or null if none has been registered.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to return the setting for
        
            Returns:
                the parameter setting for the given parameter or null if none has been found
        
        
        """
        ...
    @typing.overload
    def getParameterSettings(self, string: str) -> 'ParameterSettings': ...
    def getParameters(self) -> java.util.Set['Parameter']: ...
    @typing.overload
    def getSetting(self, beamProcess: 'BeamProcess', parameter: 'Parameter') -> 'Setting':
        """
            Returns either the current setting or the updated setting if one exist for the given beam process and parameter. The
            setting returned is always the updated one if it exist and the current one if no updated setting has been given for the
            given beam process.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to return the setting for
        
            Returns:
                the current or the updated setting for the given beam process and parameter.
        
            Returns either the current setting or the updated setting if one exist for the given beam process and parameter. The
            setting returned is always the updated one if it exist and the current one if no updated setting has been given for the
            given beam process.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to return the setting for
        
            Returns:
                the current or the updated setting for the given beam process and parameter
        
        
        """
        ...
    @typing.overload
    def getSetting(self, beamProcess: 'BeamProcess', string: str) -> 'Setting': ...
    def getSettings(self) -> java.util.Set['Setting']: ...
    def getUpdatedBeamProcesses(self) -> java.util.Set['BeamProcess']: ...
    def getUpdatedParameters(self) -> java.util.Set['Parameter']: ...
    @typing.overload
    def getUpdatedSetting(self, beamProcess: 'BeamProcess', parameter: 'Parameter') -> 'Setting':
        """
            Returns the updated setting for the given beam process and parameter. The setting returned is always the updated one, or
            null if no update has been set.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to return the setting for
        
            Returns:
                the updated setting for the given beam process and parameter or null if the given beam process has not been updated for
                the given parameter
        
            Returns the updated setting for the given beam process and parameter. The setting returned is always the updated one, or
            null if no update has been set.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to return the setting for
        
            Returns:
                the updated setting for the given beam process and parameter or null if the given beam process has not been updated for
                the given parameter
        
        
        """
        ...
    @typing.overload
    def getUpdatedSetting(self, beamProcess: 'BeamProcess', string: str) -> 'Setting': ...
    def getUpdatedSettings(self) -> java.util.Set['Setting']: ...
    def isEmpty(self) -> bool:
        """
        
            Returns:
                :code:`true` if :meth:`~cern.lsa.domain.settings.ContextSettings.size` is zero
        
        
        """
        ...
    @typing.overload
    def isUpdated(self, beamProcess: 'BeamProcess', parameter: 'Parameter') -> bool:
        """
            Returns :code:`true` if the setting for the given beam process and parameter has been updated, :code:`false` otherwise.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to check for update
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to check for update
        
            Returns:
                :code:`true` if the setting for the given beam process and parameter has been updated, :code:`false` otherwise.
        
            Returns :code:`true` if the setting for the given beam process and parameter has been updated, :code:`false` otherwise.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to check for update
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to check for update
        
            Returns:
                :code:`true` if the setting for the given beam process and parameter has been updated, :code:`false` otherwise.
        
        
        """
        ...
    @typing.overload
    def isUpdated(self, beamProcess: 'BeamProcess', string: str) -> bool: ...
    @typing.overload
    def isUpdated(self, parameter: 'Parameter') -> bool:
        """
            Returns :code:`true` if the setting for the given parameter has been updated, :code:`false` otherwise.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to check for update
        
            Returns:
                :code:`true` if the setting for the given parameter has been updated, :code:`false` otherwise.
        
            Returns :code:`true` if the setting for the given parameter has been updated, :code:`false` otherwise.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to check for update
        
            Returns:
                :code:`true` if the setting for the given parameter has been updated, :code:`false` otherwise.
        
        """
        ...
    @typing.overload
    def isUpdated(self, string: str) -> bool: ...
    def round(self) -> None:
        """
            Round all the settings that are part of this :code:`ContextSettings` object.
        
        """
        ...
    def size(self) -> int:
        """
        
            Returns:
                the number of parameter settings in this collection.
        
        
        """
        ...
    @typing.overload
    def updateSetting(self, beamProcess: 'BeamProcess', parameter: 'Parameter', immutableValue: cern.accsoft.commons.value.ImmutableValue, settingPartEnum: 'SettingPartEnum') -> None:
        """
            Updates the setting belonging to the given beam process for the given parameter with the given value. This method lookup
            the setting for the given beam process and the parameter. If no setting is associated to the beam process and parameter
            an exception is thrown. If a setting is found, then the updated setting is checked. If there is an existing updated
            setting, it is updated using the given value. If none exist, a new updated setting is created using the current one and
            it is updated with the given value. If the given value is null an updated setting will be created that is an exact copy
            of the current one.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process whose setting is to be updated
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to check for update
                updatedValue (cern.accsoft.commons.value.ImmutableValue): the possibly null value to use for the update
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the part of the setting to update
        
            Updates the setting belonging to the given beam process for the given parameter with the given value. This method lookup
            the setting for the given beam process and the parameter. If no setting is associated to the beam process and parameter
            an exception is thrown. If a setting is found, then the updated setting is checked. If there is an existing updated
            setting, it is updated using the given value. If none exist, a new updated setting is created using the current one and
            it is updated with the given value. If the given value is null an updated setting will be created that is an exact copy
            of the current one.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process whose setting is to be updated
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to check for update
                updatedValue (cern.accsoft.commons.value.ImmutableValue): the possibly null value to use for the update
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the part of the setting to update
        
        
        """
        ...
    @typing.overload
    def updateSetting(self, beamProcess: 'BeamProcess', string: str, immutableValue: cern.accsoft.commons.value.ImmutableValue, settingPartEnum: 'SettingPartEnum') -> None: ...

class ContextSettingsRequest(java.io.Serializable):
    """
    public class ContextSettingsRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Represents a request for obtaining context settings.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'ContextSettingsRequestBuilder':
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.ContextSettingsRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    @staticmethod
    def byStandAloneContext(standAloneContext: 'StandAloneContext') -> 'ContextSettingsRequest':
        """
            Creates an :class:`~cern.lsa.domain.settings.ContextSettingsRequest`
        
            Parameters:
                standAloneContext (:class:`~cern.lsa.domain.settings.StandAloneContext`): the non :code:`null` standAloneContext for which settings should be returned.
        
            Returns:
                the request
        
        
        """
        ...
    @staticmethod
    def byStandAloneContextAndAtInstant(standAloneContext: 'StandAloneContext', instant: typing.Union[java.time.Instant, datetime.datetime]) -> 'ContextSettingsRequest':
        """
            Creates an :class:`~cern.lsa.domain.settings.ContextSettingsRequest`
        
            Parameters:
                standAloneContext (:class:`~cern.lsa.domain.settings.StandAloneContext`): the non :code:`null` standAloneContext for which settings should be returned.
                atTimestamp (`Instant <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Instant.html?is-external=true>`): the possibly :code:`null` atTimestamp for which we want to see the active settings. If null no constraint of atTimestamp
                    is taken into account. Those settings represent the active settings at that time. Note that settings that have been
                    retired exactly at that date are not included. In other word, if the given date is the date a trim has been made, the
                    settings returned by this method are the settings as they were after the trim has been performed.
        
        
        
            Returns:
                the request
        
        
        """
        ...
    @staticmethod
    def byStandAloneContextAndParameters(standAloneContext: 'StandAloneContext', collection: typing.Union[java.util.Collection['Parameter'], typing.Sequence['Parameter']]) -> 'ContextSettingsRequest': ...
    def getAtTimestamp(self) -> java.time.Instant: ...
    def getContext(self) -> 'StandAloneContext': ...
    def getParameters(self) -> java.util.Collection['Parameter']: ...

class ContextSettingsRequestBuilder:
    """
    public class ContextSettingsRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self): ...
    def at(self, instant: typing.Union[java.time.Instant, datetime.datetime]) -> 'ContextSettingsRequestBuilder':
        """
        
            Parameters:
                atTimestamp (`Instant <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Instant.html?is-external=true>`): the possibly :code:`null` atTimestamp for which we want to see the active settings. If null no constraint of atTimestamp
                    is taken into account. Those settings represent the active settings at that time. Note that settings that have been
                    retired exactly at that date are not included. In other word, if the given date is the date a trim has been made, the
                    settings returned by this method are the settings as they were after the trim has been performed.
        
        
        
            Returns:
                object in creation
        
        
        """
        ...
    def build(self) -> ContextSettingsRequest: ...
    @staticmethod
    def byStandAloneContext(standAloneContext: 'StandAloneContext') -> ContextSettingsRequest: ...
    @staticmethod
    def byStandAloneContextAndAtInstant(standAloneContext: 'StandAloneContext', instant: typing.Union[java.time.Instant, datetime.datetime]) -> ContextSettingsRequest: ...
    @staticmethod
    def byStandAloneContextAndParameters(standAloneContext: 'StandAloneContext', collection: typing.Union[java.util.Collection['Parameter'], typing.Sequence['Parameter']]) -> ContextSettingsRequest: ...
    def parameters(self, collection: typing.Union[java.util.Collection['Parameter'], typing.Sequence['Parameter']]) -> 'ContextSettingsRequestBuilder': ...
    def standAloneContext(self, standAloneContext: 'StandAloneContext') -> 'ContextSettingsRequestBuilder':
        """
        
            Parameters:
                standAloneContext (:class:`~cern.lsa.domain.settings.StandAloneContext`): the non :code:`null` standAloneContext for which settings should be returned.
        
            Returns:
                object in creation
        
        
        """
        ...

class ContextTypeFilter(cern.accsoft.commons.util.Filters.Filter[cern.lsa.domain.settings.type.ContextType]):
    """
    public class ContextTypeFilter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.type.ContextType`>
    
        Simple :class:`~cern.lsa.domain.settings.type.ContextType` filter.
    """
    def __init__(self): ...
    def accepts(self, contextType: cern.lsa.domain.settings.type.ContextType) -> bool:
        """
        
            Specified by:
                :code:`accepts` in interface :class:`~cern.lsa.domain.settings.type.ContextType`
        
        
        """
        ...
    @staticmethod
    def categoryIn(collection: typing.Union[java.util.Collection[ContextCategory], typing.Sequence[ContextCategory]]) -> 'ContextTypeFilter': ...
    def setCategories(self, collection: typing.Union[java.util.Collection[ContextCategory], typing.Sequence[ContextCategory]]) -> 'ContextTypeFilter': ...

class ContextTypes:
    """
    public class ContextTypes extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A utility class that provides methods to manipulate LSA context types.
    """
    CATEGORIES: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.settings.type.ContextType`, :class:`~cern.lsa.domain.settings.ContextCategory`> CATEGORIES
    
        Mapper :class:`~cern.lsa.domain.settings.type.ContextType` to :class:`~cern.lsa.domain.settings.ContextCategory`
    
    """
    def __init__(self): ...
    _getCategories__T = typing.TypeVar('_getCategories__T', bound=cern.lsa.domain.settings.type.ContextType)  # <T>
    @staticmethod
    def getCategories(collection: typing.Union[java.util.Collection[_getCategories__T], typing.Sequence[_getCategories__T]]) -> java.util.Set[ContextCategory]: ...

class Contexts:
    """
    public class Contexts extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A utility class that provides methods to manipulate LSA contexts.
    """
    PARTICLE_TRANSFERS: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.settings.BeamProcess`, cern.accsoft.commons.domain.particletransfers.ParticleTransfer> PARTICLE_TRANSFERS
    
        Mapper :class:`~cern.lsa.domain.settings.BeamProcess` to :code:`ParticleTransfer`
    
    """
    CATEGORIES: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.settings.StandAloneContext`, :class:`~cern.lsa.domain.settings.ContextCategory`> CATEGORIES
    
        Mapper :class:`~cern.lsa.domain.settings.StandAloneContext` to :class:`~cern.lsa.domain.settings.ContextCategory`
    
    """
    SUBCONTEXT_START_TIME_COMPARATOR: typing.ClassVar[java.util.Comparator] = ...
    """
    public static final `Comparator <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Comparator.html?is-external=true>`<:class:`~cern.lsa.domain.settings.SubContext`> SUBCONTEXT_START_TIME_COMPARATOR
    
        A comparator that can be used to compare two sub contexts on their start time
    
    """
    @staticmethod
    def areResident(collection: typing.Union[java.util.Collection['DrivableContext'], typing.Sequence['DrivableContext']]) -> bool: ...
    @staticmethod
    def assertContextIsNonArchived(standAloneContext: 'StandAloneContext') -> None: ...
    @staticmethod
    def assertContextsAreNonArchived(collection: typing.Union[java.util.Collection['StandAloneContext'], typing.Sequence['StandAloneContext']]) -> None: ...
    @staticmethod
    def assertContextsBelongToSameStandAloneContext(collection: typing.Union[java.util.Collection[Context], typing.Sequence[Context]]) -> None: ...
    @staticmethod
    def belongSameStandAloneContext(collection: typing.Union[java.util.Collection[Context], typing.Sequence[Context]]) -> bool: ...
    @typing.overload
    @staticmethod
    def canBecomeResident(standAloneBeamProcess: 'StandAloneBeamProcess', hyperCycle: 'HyperCycle') -> bool:
        """
            Indicates if the specified beam process can become resident i.e. it is not yet resident, but belongs to an active hyper
            cycle and has a user mapped.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.StandAloneBeamProcess`): examined beam process
                activeHyperCycle (:class:`~cern.lsa.domain.settings.HyperCycle`): the currently active hyper cycle. If :code:`null` is passed the method treats it as there would be no active hyper cycle
                    (and returns :code:`false`)
        
            Returns:
                :code:`true` if the given beam process can become resident, :code:`false` otherwise
        
        """
        ...
    @typing.overload
    @staticmethod
    def canBecomeResident(standAloneContext: 'StandAloneContext') -> bool:
        """
            Indicates if the specified context can become resident i.e. it is not yet resident and has a user mapped (e.g. a beam
            process in the active hyper cycle) For beam processes, this is equivalent to
            :meth:`~cern.lsa.domain.settings.Contexts.canBecomeResident` for the active hyper cycle.
        
            Parameters:
                ctx (:class:`~cern.lsa.domain.settings.StandAloneContext`): examined context process
        
            Returns:
                :code:`true` if the given context can become resident, :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def cloneStandAloneContext(standAloneContext: 'StandAloneContext') -> 'StandAloneContext':
        """
            Utility method for cloning StandAloneContext instances. Uses the copy constructor of the appropriate class.
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.StandAloneContext`): the context to clone
        
            Returns:
                the clone
        
        
        """
        ...
    @staticmethod
    def contains(context: Context, int: int) -> bool:
        """
            Returns :code:`true` if the specified :code:`time` is within the given context i.e. :code:`time` in [startTime, endTime]
            (including first and last point). The method handles properly the case when contexts "wraps" around parent context e.g.
            beam processes on transfer lines which can start in the last cycle and end in the first cycle.
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.Context`): considered context
                time (int): checked time
        
            Returns:
                :code:`true` if the time belongs to the specified context
        
        
        """
        ...
    @staticmethod
    def containsSegmentWithName(beamProcessType: cern.lsa.domain.settings.type.BeamProcessType, string: str) -> bool:
        """
            Returns :code:`true` if the specified beam process type contains at least one segment with name matching given pattern
            i.e. if the segment name contains specified string.
        
            Parameters:
                bpType (:class:`~cern.lsa.domain.settings.type.BeamProcessType`): beam process type to be checked
                segmentNamePattern (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): regular expression pattern to be checked
        
            Returns:
                :code:`true` if the specified beam process type contains at least one segment with name matching given pattern.
        
        
        """
        ...
    @staticmethod
    def createActualBeamProcessName(beamProcess: 'BeamProcess', int: int) -> str:
        """
            Builds name of an actual beam process in the following format:
        
              - First point of source stand-alone context: SOURCE_CONTEXT_NAME@0_[START]
              - Last point of source stand-alone context: SOURCE_CONTEXT_NAME@XX_[END] where XX is the time in the context
              - Any other point: SOURCE_CONTEXT_NAME@XX where XX is the time in the context
        
        
            Parameters:
                srcBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the source beam process from which actual one is created
                timeInBeamProcess (int): point in time at which actual beam process is created
        
            Returns:
                the name of an actual beam process
        
        
        """
        ...
    _filterBeamProcesses_2__T = typing.TypeVar('_filterBeamProcesses_2__T', bound='BeamProcess')  # <T>
    _filterBeamProcesses_3__T = typing.TypeVar('_filterBeamProcesses_3__T', bound='BeamProcess')  # <T>
    @typing.overload
    @staticmethod
    def filterBeamProcesses(standAloneContext: 'StandAloneContext', particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, beamProcessTypeCategoryArray: typing.List[cern.lsa.domain.settings.type.BeamProcessTypeCategory]) -> java.util.List['BeamProcess']: ...
    @typing.overload
    @staticmethod
    def filterBeamProcesses(standAloneContext: 'StandAloneContext', particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.type.BeamProcessTypeCategory], typing.Sequence[cern.lsa.domain.settings.type.BeamProcessTypeCategory]]) -> java.util.List['BeamProcess']: ...
    @typing.overload
    @staticmethod
    def filterBeamProcesses(collection: typing.Union[java.util.Collection[_filterBeamProcesses_2__T], typing.Sequence[_filterBeamProcesses_2__T]], particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, beamProcessTypeCategoryArray: typing.List[cern.lsa.domain.settings.type.BeamProcessTypeCategory]) -> java.util.List[_filterBeamProcesses_2__T]: ...
    @typing.overload
    @staticmethod
    def filterBeamProcesses(collection: typing.Union[java.util.Collection[_filterBeamProcesses_3__T], typing.Sequence[_filterBeamProcesses_3__T]], particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, collection2: typing.Union[java.util.Collection[cern.lsa.domain.settings.type.BeamProcessTypeCategory], typing.Sequence[cern.lsa.domain.settings.type.BeamProcessTypeCategory]]) -> java.util.List[_filterBeamProcesses_3__T]: ...
    _filterBeamProcessesByParticleTransfers__T = typing.TypeVar('_filterBeamProcessesByParticleTransfers__T', bound='BeamProcess')  # <T>
    @staticmethod
    def filterBeamProcessesByParticleTransfers(collection: typing.Union[java.util.Collection[_filterBeamProcessesByParticleTransfers__T], typing.Sequence[_filterBeamProcessesByParticleTransfers__T]], collection2: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]]) -> java.util.List[_filterBeamProcessesByParticleTransfers__T]: ...
    _filterByCategories__T = typing.TypeVar('_filterByCategories__T', bound='StandAloneContext')  # <T>
    @staticmethod
    def filterByCategories(collection: typing.Union[java.util.Collection[_filterByCategories__T], typing.Sequence[_filterByCategories__T]], contextCategoryArray: typing.List[ContextCategory]) -> java.util.List[_filterByCategories__T]: ...
    _filterByMultiplexingCriteria__T = typing.TypeVar('_filterByMultiplexingCriteria__T', bound='StandAloneContext')  # <T>
    @staticmethod
    def filterByMultiplexingCriteria(collection: typing.Union[java.util.Collection[_filterByMultiplexingCriteria__T], typing.Sequence[_filterByMultiplexingCriteria__T]], boolean: bool) -> java.util.List[_filterByMultiplexingCriteria__T]: ...
    _filterCompatibleBeamProcesses__T = typing.TypeVar('_filterCompatibleBeamProcesses__T', bound='BeamProcess')  # <T>
    @staticmethod
    def filterCompatibleBeamProcesses(collection: typing.Union[java.util.Collection[_filterCompatibleBeamProcesses__T], typing.Sequence[_filterCompatibleBeamProcesses__T]], parameter: 'Parameter') -> java.util.List[_filterCompatibleBeamProcesses__T]: ...
    _filterDrivableContextsByUsers__T = typing.TypeVar('_filterDrivableContextsByUsers__T', bound='DrivableContext')  # <T>
    @staticmethod
    def filterDrivableContextsByUsers(collection: typing.Union[java.util.Collection[_filterDrivableContextsByUsers__T], typing.Sequence[_filterDrivableContextsByUsers__T]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[_filterDrivableContextsByUsers__T]: ...
    @staticmethod
    def filterFunctionBeamProcesses(standAloneContext: 'StandAloneContext', particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> java.util.List['BeamProcess']: ...
    _filterResidentContexts__T = typing.TypeVar('_filterResidentContexts__T', bound='StandAloneContext')  # <T>
    @staticmethod
    def filterResidentContexts(collection: typing.Union[java.util.Collection[_filterResidentContexts__T], typing.Sequence[_filterResidentContexts__T]], boolean: bool) -> java.util.List[_filterResidentContexts__T]: ...
    _filterStandAloneContextsByClass__T = typing.TypeVar('_filterStandAloneContextsByClass__T', bound='StandAloneContext')  # <T>
    @staticmethod
    def filterStandAloneContextsByClass(collection: typing.Union[java.util.Collection['StandAloneContext'], typing.Sequence['StandAloneContext']], class_: typing.Type[_filterStandAloneContextsByClass__T]) -> java.util.Set['StandAloneContext']: ...
    @staticmethod
    def getBeamProcessTypeCategories(collection: typing.Union[java.util.Collection['BeamProcess'], typing.Sequence['BeamProcess']]) -> java.util.Set[cern.lsa.domain.settings.type.BeamProcessTypeCategory]: ...
    @typing.overload
    @staticmethod
    def getBeamProcesses(standAloneContext: 'StandAloneContext', collection: typing.Union[java.util.Collection['SubContext'], typing.Sequence['SubContext']]) -> java.util.List['BeamProcess']: ...
    @typing.overload
    @staticmethod
    def getBeamProcesses(collection: typing.Union[java.util.Collection['DrivableContext'], typing.Sequence['DrivableContext']]) -> java.util.List['BeamProcess']: ...
    @staticmethod
    def getBeamProcessesAt(standAloneContext: 'StandAloneContext', collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]], double: float) -> java.util.List['BeamProcess']: ...
    _getCategories__T = typing.TypeVar('_getCategories__T', bound='StandAloneContext')  # <T>
    @staticmethod
    def getCategories(collection: typing.Union[java.util.Collection[_getCategories__T], typing.Sequence[_getCategories__T]]) -> java.util.Set[ContextCategory]: ...
    @staticmethod
    def getCompatibleBeamProcess(standAloneContext: 'StandAloneContext', parameter: 'Parameter') -> 'BeamProcess':
        """
            Returns a SINGLE beam process from given context that is :meth:`~cern.lsa.domain.settings.Contexts.isCompatible` with
            specified parameter. If there is none or more than one beam process that is compatible with given parameter - the method
            throws `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>`.
        
            Returns:
                the only beam process belonging to given context and compatible with specified parameter
        
            Raises:
                : if the context doesn't contain compatible beam process or there is more than one
        
        
        """
        ...
    @staticmethod
    def getCompatibleBeamProcesses(standAloneContext: 'StandAloneContext', parameter: 'Parameter') -> java.util.Set['BeamProcess']: ...
    @staticmethod
    def getCorrespondingBeamProcess(beamProcess: 'BeamProcess', parameter: 'Parameter') -> 'BeamProcess':
        """
            If the given beam process is :meth:`~cern.lsa.domain.settings.Contexts.isCompatible` with given parameter then the
            method returns directly the given beam process. Otherwise it returns compatible beam process overlapping with specified
            one.
        
            Typically this method can be used to find :meth:`~cern.lsa.domain.settings.BeamProcess.getCategory` beam process for
            corresponding discrete one or vice versa.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): checked beam process
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter for which compatible beam process should be returned
        
            Returns:
                the corresponding, compatible beam process
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Contexts.getCompatibleBeamProcesses`
        
        
        """
        ...
    @staticmethod
    def getCorrespondingBeamProcesses(beamProcess: 'BeamProcess', parameter: 'Parameter') -> java.util.List['BeamProcess']: ...
    @staticmethod
    def getCycle(beamProcess: 'BeamProcess') -> 'Cycle':
        """
            Returns cycle within which the given beam process starts or :code:`null` if the specified beam process is stand-alone.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): 
            Returns:
                cycle containing given beam process
        
        
        """
        ...
    @staticmethod
    def getDrivableContext(context: Context) -> 'DrivableContext':
        """
            Returns the drivable context from the given context.
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.Context`): given context
        
            Returns:
                all drivable contexts within the given context
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getDrivableContextByUser(standAloneContext: 'StandAloneContext', string: str) -> 'DrivableContext':
        """
            Returns the drivable context derived from the given stand alone context which is mapped to the given user
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.StandAloneContext`): given stand alone context
                user (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the user name used to check given contexts against
        
            Returns:
                drivable context derived from the given stand alone context which is mapped to the given user or null if there was no
                drivable withing given stand alone context
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getDrivableContextByUser(collection: typing.Union[java.util.Collection['StandAloneContext'], typing.Sequence['StandAloneContext']], string: str) -> 'DrivableContext': ...
    @typing.overload
    @staticmethod
    def getDrivableContexts(context: Context) -> java.util.Set['DrivableContext']: ...
    @typing.overload
    @staticmethod
    def getDrivableContexts(collection: typing.Union[java.util.Collection[Context], typing.Sequence[Context]]) -> java.util.Set['DrivableContext']: ...
    @staticmethod
    def getDrivableContextsByUsers(collection: typing.Union[java.util.Collection['StandAloneContext'], typing.Sequence['StandAloneContext']], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set['DrivableContext']: ...
    @staticmethod
    def getFollowingBeamProcess(beamProcess: 'BeamProcess') -> 'BeamProcess':
        """
            Returns a beam process that is scheduled after the given beam process in the same particle transfer. If the specified
            beam process is last - the method returns the first function beam process scheduled in the same particle transfer.
        
            Note that if a discrete beam process is passed to the method, it returns following discrete beam process. If a function
            beam process is passed, then the method returns the following function beam process.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the considered beam process
        
            Returns:
                the following beam process or :code:`null` if the given beam process is the only one in its particle transfer
        
        
        """
        ...
    @staticmethod
    def getFunctionBeamProcessAt(standAloneContext: 'StandAloneContext', particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, double: float) -> 'BeamProcess':
        """
            Retrieves the current function Beam Process for a given point in time for the given StandAloneContext
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.StandAloneContext`): surrounding standAloneContext to search the beamProcess in
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): given particleTransfer
                time (double): point in time
        
            Returns:
                beamProcess or :code:`null`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getIntersectedBeamProcesses(beamProcess: 'BeamProcess', collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]], beamProcessTypeCategoryArray: typing.List[cern.lsa.domain.settings.type.BeamProcessTypeCategory]) -> java.util.List['BeamProcess']: ...
    @typing.overload
    @staticmethod
    def getIntersectedBeamProcesses(context: Context) -> java.util.Set['BeamProcess']: ...
    @typing.overload
    @staticmethod
    def getIntersectedBeamProcesses(collection: typing.Union[java.util.Collection[Context], typing.Sequence[Context]]) -> java.util.Set['BeamProcess']: ...
    @staticmethod
    def getIntersectedCycles(collection: typing.Union[java.util.Collection['BeamProcess'], typing.Sequence['BeamProcess']]) -> java.util.Set['Cycle']: ...
    @staticmethod
    def getParticleTransfers(collection: typing.Union[java.util.Collection['StandAloneContext'], typing.Sequence['StandAloneContext']]) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def getParticleTransfersFromBeamProcesses(collection: typing.Union[java.util.Collection['BeamProcess'], typing.Sequence['BeamProcess']]) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def getPrecedingBeamProcess(beamProcess: 'BeamProcess') -> 'BeamProcess':
        """
            Returns a beam process that is scheduled before the given beam process in the same particle transfer. If the specified
            beam process is first - the method returns the last function beam process scheduled in the same particle transfer.
        
            Note that if a discrete beam process is passed to the method, it returns preceding discrete beam process. If a function
            beam process is passed, then the method returns the preceding function beam process.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the considered beam process
        
            Returns:
                the preceding beam process or :code:`null` if the given beam process is the only one in its particle transfer
        
        
        """
        ...
    @staticmethod
    def getStandAloneContext(context: Context) -> 'StandAloneContext':
        """
            Returns :code:`StandAloneContext` associated with specified context. If the given context is stand alone - it will be
            returned. If the given context is a sub-context - its stand-alone context will be returned. If the given context is a
            sub-context and not yet part of any standalone-context this method returns null (this is at the moment only the case for
            :code:`BeamProductionChain`).
        
            Returns:
                StandAloneContext associated with specified context.
        
        
        """
        ...
    @staticmethod
    def getStandAloneContexts(collection: typing.Union[java.util.Collection[Context], typing.Sequence[Context]]) -> java.util.Set['StandAloneContext']: ...
    @staticmethod
    def getTypeNames(collection: typing.Union[java.util.Collection[Context], typing.Sequence[Context]]) -> java.util.Set[str]: ...
    @staticmethod
    def getUsers(standAloneContext: 'StandAloneContext') -> java.util.Set[str]: ...
    @staticmethod
    def getUsersForContexts(collection: typing.Union[java.util.Collection[Context], typing.Sequence[Context]]) -> java.util.List[str]: ...
    @staticmethod
    def isActual(beamProcess: 'BeamProcess') -> bool:
        """
            Determines if the given beam process is actual.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): beam process to be check (cannot be null)
        
            Returns:
                :code:`true` if the given beam process is actual, :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def isActualBeamProcess(context: Context) -> bool:
        """
            Determines if the given context is an actual beam process i.e. if the associated
            :meth:`~cern.lsa.domain.settings.Context.getContextFamily` is
            :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS` and if it contains
            :meth:`~cern.lsa.domain.settings.StandAloneBeamProcess.getActualBeamProcessInfo`.
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.Context`): context to be checked
        
            Returns:
                :code:`true` if the given context is an actual beam process, :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def isCompatible(beamProcess: 'BeamProcess', parameter: 'Parameter') -> bool:
        """
            Returns :code:`true` if the given beam process can be used to store settings of the specified parameter. This method
            compares category of the beam process with value type of the parameter to verify if storing settings is possible. It
            also checks if particle transfer of the beam process matches particle transfers that given parameter belongs to.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): considered beam process
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): considered parameter
        
        
        """
        ...
    @staticmethod
    def isLastPoint(context: Context, int: int) -> bool:
        """
            Returns :code:`true` if the specified :code:`time` represents the last point of given context. The method handles
            properly the case when context "wraps" around its parent context.
        
            Parameters:
                context (:class:`~cern.lsa.domain.settings.Context`): considered context
                time (int): checked time
        
            Returns:
                :code:`true` if the :code:`time` is the last point of given context
        
        
        """
        ...
    _sortByStartTime__T = typing.TypeVar('_sortByStartTime__T', bound='SubContext')  # <T>
    @staticmethod
    def sortByStartTime(list: java.util.List[_sortByStartTime__T]) -> None: ...

class CycleBeamProcessIntersection:
    """
    public interface CycleBeamProcessIntersection
    
        Defines one intersection between a beam process and a cycle. This object represents one of these intersections. It
        contains the x-coordinates of the intersection locally in the beam process, locally in the cycle.
    """
    def getBeamProcess(self) -> 'BeamProcess':
        """
        
            Returns:
                Returns the beamProcess.
        
        
        """
        ...
    def getCycle(self) -> 'Cycle':
        """
        
            Returns:
                Returns the cycle.
        
        
        """
        ...
    def getEndInBeamProcess(self) -> int:
        """
        
            Returns:
                Returns the intersectionEndInBeamProcess.
        
        
        """
        ...
    def getEndInCycle(self) -> int:
        """
        
            Returns:
                Returns the intersectionEndInCycle.
        
        
        """
        ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
        
            Returns:
                Returns the particleTransfer.
        
        
        """
        ...
    def getStartInBeamProcess(self) -> int:
        """
        
            Returns:
                Returns the intersectionStartInBeamProcess.
        
        
        """
        ...
    def getStartInCycle(self) -> int:
        """
        
            Returns:
                Returns the intersectionStartInCycle.
        
        
        """
        ...

class DevicePropertyParameters:
    """
    public interface DevicePropertyParameters
    
        An utility structure used to keep set of parameters for the same device and property. Several utility methods are
        provided for easy retrieval of parameters including specialized methods for the signature parameter.
    """
    def getDeviceName(self) -> str:
        """
            Return the device name for which all related parameters are collected.
        
            Returns:
                the device name for which all related parameters are collected
        
        
        """
        ...
    def getDevicePropertyName(self) -> str:
        """
            Return the device name concatenated with property name for which all related parameters are collected.
        
            Returns:
                the device name concatenated with property name for which all related parameters are collected
        
        
        """
        ...
    @typing.overload
    def getFieldNames(self) -> java.util.SortedSet[str]: ...
    @typing.overload
    def getFieldNames(self, boolean: bool) -> java.util.SortedSet[str]: ...
    @typing.overload
    def getParameters(self) -> java.util.SortedSet['Parameter']: ...
    @typing.overload
    def getParameters(self, boolean: bool) -> java.util.SortedSet['Parameter']: ...
    def getPropertyName(self) -> str:
        """
            Return the property name for which all related parameters are collected.
        
            Returns:
                the property name for which all related parameters are collected
        
        
        """
        ...
    def getSignature(self) -> 'Parameter':
        """
            Return the signature parameter for the given device and property, or :code:`null` value if does not exist.
        
            For parameter device/property#field1 one would get a parameter called: device/property#signature
        
            Returns:
                the signature parameter for the given device and property or :code:`null` if none exists
        
        
        """
        ...
    def isCritical(self) -> bool:
        """
            Return :code:`true` if all parameters related to the given device and property are critical, otherwise :code:`false`.
        
            Returns:
                :code:`true` if all parameters related to the given device and property are critical, otherwise :code:`false`
        
        
        """
        ...

class ErrorsAwareContextSettings:
    """
    public class ErrorsAwareContextSettings extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A holder for :class:`~cern.lsa.domain.settings.ContextSettings` and exceptions that could occur when loading settings
        for the source and/or destination context from the hardware.
    """
    @typing.overload
    def __init__(self, contextSettings: ContextSettings): ...
    @typing.overload
    def __init__(self, contextSettings: ContextSettings, map: typing.Union[java.util.Map['Parameter', java.lang.Exception], typing.Mapping['Parameter', java.lang.Exception]]): ...
    def getContextSettings(self) -> ContextSettings:
        """
        
            Returns:
                context settings loaded from the database or from the hardware.
        
        
        """
        ...
    def getParameter2Exception(self) -> java.util.Map['Parameter', java.lang.Exception]: ...

class FailedParametersStatus:
    """
    public interface FailedParametersStatus
    
        Represents the status of any operation with parameters.
    """
    def containsFailedParameters(self) -> bool:
        """
            Returns :code:`true` if the status contains at least one failed parameter, :code:`false` otherwise.
        
            Returns:
                :code:`true` if the status contains at least one failed parameter, :code:`false` otherwise.
        
        
        """
        ...
    def getFailedContexts(self) -> java.util.Set[Context]: ...
    def getFailedParameters(self, context: Context) -> java.util.Map[str, java.lang.Exception]: ...

class GenerationException(cern.lsa.domain.LsaException):
    """
    public class GenerationException extends :class:`~cern.lsa.domain.LsaException`
    
        An exception thrown during settings generation, typically by :code:`ValueGenerator`s.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class HyperCycle(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity, java.lang.Comparable['HyperCycle']):
    """
    public interface HyperCycle extends cern.accsoft.commons.util.Named, :class:`~cern.lsa.domain.commons.IdentifiedEntity`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.settings.HyperCycle`>
    
        Hypercycle represents a series of BeamProcesses. It is necessary to provide information in which order the BeamProcesses
        will be played.
    """
    def getBeamProcessByUser(self, string: str) -> 'StandAloneBeamProcess':
        """
            Returns beam process which is mapped to the specified user.
        
            Parameters:
                userName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): LHC user name
        
            Returns:
                mapped beam process or :code:`null` if none beam process is mapped to the given user
        
        
        """
        ...
    def getBeamProcessPosition(self, string: str, standAloneBeamProcess: 'StandAloneBeamProcess') -> int:
        """
            Returns, for the given user category, the scheduled position of given beamprocess within the current HyperCycle.
        
            Returns:
                the beamprocess scheduled position or -1 (if, for the given category, no beamprocess equals to the given one is
                scheduled).
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Returns the description of this hypercycle
        
            Returns:
                the description of this hypercycle
        
        
        """
        ...
    def getFirstBeamProcess(self, string: str) -> 'StandAloneBeamProcess':
        """
            Returns the first beam process for the given category.
        
            Parameters:
                userCategory (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the category to consider
        
            Returns:
                the first beam process for :code:`userCategory` or :code:`null` if none or :code:`userCategory` does not exist.
        
        
        """
        ...
    def getLastBeamProcess(self, string: str) -> 'StandAloneBeamProcess':
        """
            Returns the last beam process for the given category
        
            Parameters:
                userCategory (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the category to consider
        
            Returns:
                the last beam process for :code:`userCategory` or :code:`null` if none or :code:`userCategory` does not exist.
        
        
        """
        ...
    def getNextBeamProcess(self, string: str) -> 'StandAloneBeamProcess':
        """
            Returns the beam process following another given one
        
            Parameters:
                beamProcessName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the beam process to consider as the current one
        
            Returns:
                the next beam process in relation to :code:`beamProcessName` or :code:`null` if none or :code:`beamProcessName` does not
                exist.
        
        
        """
        ...
    def getPreviousBeamProcess(self, string: str) -> 'StandAloneBeamProcess':
        """
            Returns the beam process preceding another given one
        
            Parameters:
                beamProcessName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the beam process to consider as the current one
        
            Returns:
                the previous beam process in relation to :code:`beamProcessName` or :code:`null` if none or :code:`beamProcessName` does
                not exist..
        
        
        """
        ...
    def getResidentBeamProcess(self, string: str) -> 'StandAloneBeamProcess':
        """
            Returns the resident beam processes for the given category.
        
            Parameters:
                userCategory (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the category to consider
        
            Returns:
                the resident beam processes for :code:`userCategory` or :code:`null` if there is no resident beam process in specified
                category
        
        
        """
        ...
    def getResidentBeamProcesses(self) -> java.util.Set['StandAloneBeamProcess']: ...
    @typing.overload
    def getScheduledBeamProcesses(self) -> java.util.List['StandAloneBeamProcess']: ...
    @typing.overload
    def getScheduledBeamProcesses(self, string: str) -> java.util.List['StandAloneBeamProcess']: ...
    def getUserCategories(self) -> java.util.SortedSet[str]: ...
    def getUserCategory(self, standAloneBeamProcess: 'StandAloneBeamProcess') -> str:
        """
            Returns a category to which the given user belongs.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.StandAloneBeamProcess`): considered beam process
        
            Returns:
                category name or :code:`null` if this beam process doesn't belong to this hyper cycle
        
        
        """
        ...
    def getUserForBeamProcess(self, standAloneBeamProcess: 'StandAloneBeamProcess') -> str:
        """
            Returns the user to which the specified beam process is mapped to.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.StandAloneBeamProcess`): the beam process
        
            Returns:
                mapped beam process or :code:`null` if none beam process is mapped to the given user
        
        
        """
        ...
    @typing.overload
    def getUsers(self, string: str) -> java.util.List[str]: ...
    @typing.overload
    def getUsers(self) -> java.util.Set[str]: ...
    def isActive(self) -> bool:
        """
            Indicates if this hyper cycle is active i.e. it is used in operation.
        
            At most one hyper cycle can be active at a time.
        
            Returns:
                if this hyper-cycle is active.
        
        
        """
        ...

class HyperCycleMapping:
    """
    @Immutable public interface HyperCycleMapping
    """
    @staticmethod
    def builder() -> 'DefaultHyperCycleMapping.Builder':
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.HyperCycleMapping`
        
            Returns:
                the builder
        
        
        """
        ...
    def getBeamProcess(self) -> 'StandAloneBeamProcess': ...
    def getUser(self) -> AcceleratorUser: ...

class IncorporationRanges:
    """
    public class IncorporationRanges extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods to deal with instances of :class:`~cern.lsa.domain.settings.type.IncorporationRange` instances.
    """
    def __init__(self): ...
    @staticmethod
    def assertRangesConsistentWithBeamProcessType(list: java.util.List[cern.lsa.domain.settings.type.IncorporationRange], beamProcessType: cern.lsa.domain.settings.type.BeamProcessType) -> None: ...
    @staticmethod
    def ensureConsistentRanges(collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.type.IncorporationRange], typing.Sequence[cern.lsa.domain.settings.type.IncorporationRange]]) -> None: ...

class IncorporationSetting(java.io.Serializable):
    """
    public class IncorporationSetting extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        :class:`~cern.lsa.domain.settings.Setting` with the point in time in the destination beam process to incorporate into.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, setting: 'Setting', double: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getPointInTime(self) -> float:
        """
        
            Returns:
                point-in-time inside destination beam process
        
        
        """
        ...
    def getSetting(self) -> 'Setting':
        """
        
            Returns:
                setting containing the destination beam process
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class Intersections:
    """
    public final class Intersections extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class with methods applying to intersections or used internally by implementations of different types (super
        cycle or cycle) of intersections.
    """
    TOLERANCE: typing.ClassVar[float] = ...
    """
    public static final double TOLERANCE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ERROR_MESSAGE_DISCONTINUITY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ERROR_MESSAGE_DISCONTINUITY
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    @staticmethod
    def computeBeamProcessFunction(standAloneContext: 'StandAloneContext', beamProcess: 'BeamProcess', immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> cern.accsoft.commons.value.DiscreteFunction:
        """
            Computes sub-function of specified function that intersects with given beam process.
        
            The specified function is expected to have X coordinates with respect to the :code:`StandAloneContext`. If the given
            function doesn't intersect with specified beam process - the method returns an empty function.
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeBeamProcessFunction(standAloneContext: 'StandAloneContext', beamProcess: 'BeamProcess', immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> cern.accsoft.commons.value.DiscreteFunctionsArray: ...
    @typing.overload
    @staticmethod
    def concatenateFunctions(discreteFunction: cern.accsoft.commons.value.DiscreteFunction, discreteFunction2: cern.accsoft.commons.value.DiscreteFunction, double: float) -> None:
        """
            Concatenates two functions arrays. Internally calls concatenate function for each function of the array.
        
            Parameters:
                dest (cern.accsoft.commons.value.DiscreteFunctionsArray): destination functions array
                src (cern.accsoft.commons.value.DiscreteFunctionsArray): source functions array
                xOffset (double): offset
        
            Concatenates two functions.
        
            Parameters:
                dest (cern.accsoft.commons.value.DiscreteFunction):         src (cern.accsoft.commons.value.DiscreteFunction):         xOffset (double): 
        
        """
        ...
    @typing.overload
    @staticmethod
    def concatenateFunctions(discreteFunctionsArray: cern.accsoft.commons.value.DiscreteFunctionsArray, discreteFunctionsArray2: cern.accsoft.commons.value.DiscreteFunctionsArray, double: float) -> None: ...
    @staticmethod
    def getCycleBeamProcessIntersections(standAloneContext: 'StandAloneContext') -> java.util.SortedSet[CycleBeamProcessIntersection]: ...
    @staticmethod
    def getPrecedingBeamProcess(standAloneContext: 'StandAloneContext', beamProcess: 'BeamProcess') -> 'BeamProcess': ...
    @typing.overload
    @staticmethod
    def insertNaN(discreteFunction: cern.accsoft.commons.value.DiscreteFunction, discreteFunction2: cern.accsoft.commons.value.DiscreteFunction, int: int) -> None:
        """
            Inserts a NaN value in the middle of the given interval. Always sets NaN to target and correction
        
            Parameters:
                target (cern.accsoft.commons.value.DiscreteFunction): Target Setting
                correction (cern.accsoft.commons.value.DiscreteFunction): Correction Setting
                start (int): Start of the interval
                end (int): End of the interval
        
            Inserts a NaN value exactly at the given point. Always sets NaN to target and correction
        
            Parameters:
                target (cern.accsoft.commons.value.DiscreteFunction): Target setting
                correction (cern.accsoft.commons.value.DiscreteFunction): Correction setting
                point (int): Point at which to insert the NaN
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def insertNaN(discreteFunction: cern.accsoft.commons.value.DiscreteFunction, discreteFunction2: cern.accsoft.commons.value.DiscreteFunction, int: int, int2: int) -> None: ...
    @typing.overload
    @staticmethod
    def insertNaN(discreteFunction: cern.accsoft.commons.value.DiscreteFunction, double: float, double2: float) -> None: ...
    @typing.overload
    @staticmethod
    def mergeFunctions(discreteFunction: cern.accsoft.commons.value.DiscreteFunction, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> None:
        """
            This method will merge a second functions array (src) into an existing one (dest). Internally it calls mergeFunctions
            for each function of the array
        
            Parameters:
                dest (cern.accsoft.commons.value.DiscreteFunctionsArray): destination functions array
                src (cern.accsoft.commons.value.DiscreteFunctionsArray): source functions array
        
            This method will merge a second function (src) into an existing one (dest). It is assumed, that not-NaN sections of the
            2 functions dont overlap. (It is used, if parameters belong to more than one particle transfer. If their non-NaN
            intervals overlap with different values, than an exception is thrown. In principal, this method takes the non-NaN
            intervals from the second function, inserts it into the first one, and then removes remaining obsolete NaNs for this
            interval from the first function.
        
            Parameters:
                dest (cern.accsoft.commons.value.DiscreteFunction): destination function to merge into
                src (cern.accsoft.commons.value.ImmutableDiscreteFunction): source function to take the non-NaN intervals from
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def mergeFunctions(discreteFunctionsArray: cern.accsoft.commons.value.DiscreteFunctionsArray, discreteFunctionsArray2: cern.accsoft.commons.value.DiscreteFunctionsArray) -> None: ...
    @staticmethod
    def mutateSettingPart(setting: 'Setting', settingPartEnum: 'SettingPartEnum') -> cern.accsoft.commons.value.DiscreteFunction: ...
    @staticmethod
    def toBeamProcessFunctionsArrayMap(standAloneContext: 'StandAloneContext', collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]], immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> java.util.Map['BeamProcess', cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray]: ...
    @staticmethod
    def toBeamProcessFunctionsMap(standAloneContext: 'StandAloneContext', collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]], immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> java.util.Map['BeamProcess', cern.accsoft.commons.value.ImmutableDiscreteFunction]: ...
    @staticmethod
    def updateFunctionSetting(standAloneContext: 'StandAloneContext', parameterSettings: 'ParameterSettings', immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, settingPartEnum: 'SettingPartEnum') -> None:
        """
            Updates given ParameterSettings with specified function that can span over several beam processes. The method "cuts" the
            given function into segments per beam process and updates settings of each affected/intersected beam process.
        
            Parameters:
                ctx (:class:`~cern.lsa.domain.settings.StandAloneContext`): the context on which the update is done
                settings (:class:`~cern.lsa.domain.settings.ParameterSettings`): parameter settings
                newFunction (cern.accsoft.commons.value.ImmutableDiscreteFunction): new function to be applied
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the setting part to be used for update
        
        
        """
        ...

class KnobFactor(java.io.Serializable):
    """
    public class KnobFactor extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Represents a triplet of knob component, optic and a factor associated to them.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, string2: str, double: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getComponentName(self) -> str: ...
    def getFactor(self) -> float: ...
    def getOpticName(self) -> str: ...
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

class KnobFactors:
    """
    public interface KnobFactors
    
        Container for the the multiplication factors of a knob for each combination of component and optic.
    
        Implementations must guarantee that each possible combination of component and optic has a factor defined.
    """
    def containsFactor(self, string: str, string2: str) -> bool:
        """
            Checks whether a multiplication factor is defined for the specified combination of the component and optic.
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of an optic
        
            Returns:
                :code:`true` if a multiplication factor is defined for the specified combination of the component and optic
        
        
        """
        ...
    def getComponentNames(self) -> java.util.Set[str]: ...
    def getFactor(self, string: str, string2: str) -> float:
        """
            Returns the multiplication factor for the specified combination of the component and optic.
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of an optic
        
            Returns:
                multiplication factor for the specified combination of the component and optic
        
            Raises:
                : if the knob component or the optic are not registered
        
        
        """
        ...
    def getFactors(self) -> java.util.Set[KnobFactor]: ...
    def getFactorsForComponent(self, string: str) -> java.util.Set[KnobFactor]: ...
    def getFactorsForOptic(self, string: str) -> java.util.Set[KnobFactor]: ...
    def getOpticNames(self) -> java.util.Set[str]: ...

class LinkRuleAttribute(java.lang.Enum['LinkRuleAttribute']):
    """
    public enum LinkRuleAttribute extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.settings.LinkRuleAttribute`>
    
        Enumeration listing all current attributes for linkrules together with their names in the DB
    """
    START_VALUE: typing.ClassVar['LinkRuleAttribute'] = ...
    STOP_VALUE: typing.ClassVar['LinkRuleAttribute'] = ...
    START_DELAY: typing.ClassVar['LinkRuleAttribute'] = ...
    STOP_DELAY: typing.ClassVar['LinkRuleAttribute'] = ...
    DEGAUSS_VALUE: typing.ClassVar['LinkRuleAttribute'] = ...
    START_ROUND: typing.ClassVar['LinkRuleAttribute'] = ...
    STOP_ROUND: typing.ClassVar['LinkRuleAttribute'] = ...
    RAMP_SPEED: typing.ClassVar['LinkRuleAttribute'] = ...
    TIME_UNIT: typing.ClassVar['LinkRuleAttribute'] = ...
    POINT_DIST: typing.ClassVar['LinkRuleAttribute'] = ...
    BTOM_AS_PERCENT_IMAX: typing.ClassVar['LinkRuleAttribute'] = ...
    KEEP_SIGN: typing.ClassVar['LinkRuleAttribute'] = ...
    LEIR_ETL_BHN10_MIN_PLATEAU_LENGTH: typing.ClassVar['LinkRuleAttribute'] = ...
    LEIR_ETL_BHN10_MIN_PLATEAU_I: typing.ClassVar['LinkRuleAttribute'] = ...
    LEIR_ETL_BHN10_MIN_STABILIZATION_LENGTH: typing.ClassVar['LinkRuleAttribute'] = ...
    LEIR_ETL_BHN10_START_END_CYCLE_I: typing.ClassVar['LinkRuleAttribute'] = ...
    def getAttributeName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LinkRuleAttribute':
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
    def values() -> typing.List['LinkRuleAttribute']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LinkRuleAttribute c : LinkRuleAttribute.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class MisconfiguredParameterException(cern.lsa.domain.LsaException):
    """
    public class MisconfiguredParameterException extends :class:`~cern.lsa.domain.LsaException`
    
        This exception is thrown when a parameter has settings for its stand-alone context, but they cannot be applied to the
        drivable context that actually gets driven. For example, this can happen when a scalar parameter has settings for a
        function beam process, but has the flag :code:`BELONGS_TO_FUNCTION_BPROC` set to false.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, parameter: 'Parameter', drivableContext: 'DrivableContext'): ...

class NotIncorporatedParameters:
    """
    public interface NotIncorporatedParameters
    
        Response object describing not incorporated parameters for source and destination beam processes in specified time.
    """
    def getNonCountinueParameters(self) -> java.util.Set[str]: ...
    def getParametersWithSettingsOnlyInFirstContext(self) -> java.util.Set[str]: ...

class Parameter(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity, java.lang.Comparable['Parameter']):
    """
    public interface Parameter extends cern.accsoft.commons.util.Named, :class:`~cern.lsa.domain.commons.IdentifiedEntity`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.settings.Parameter`>
    
        A parameter represents a measurable or settable entity of the system. It represent a property or property field on a
        given device.
    """
    def belongsToFunctionBeamProcess(self) -> bool:
        """
            Determines whether this parameter keeps value in a function beam process or in a discrete beam process - see
            :meth:`~cern.lsa.domain.settings.BeamProcess.getCategory`.
        
            This property is used by the Trim package to find out where given discrete parameter should store settings in case there
            are both function and discrete beam processes.
        
            Note that this flag is ignored for function parameters as they can keep settings only in function beam processes.
        
            Returns:
                :code:`true` if this parameter keeps settings in a function beam process
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameter.getValueDescriptor`,
                :meth:`~cern.lsa.domain.settings.BeamProcess.getCategory`
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                the accelerator to which this parameter belongs.
        
        
        """
        ...
    def getDefaultHierarchy(self) -> str:
        """
            Returns the default propagation hierarchy used by this parameter when translating its change to child parameters.
            Typically parameters have 'DEFAULT' as the default parameters hierarchy. In some cases, low level parameters have e.g.
            'UP' as the default hierarchy so that if they are trimmed - the change is propagated to high-level parameters.
        
            Returns:
                the default propagation hierarchy to be used
        
        
        """
        ...
    def getDevice(self) -> cern.lsa.domain.devices.Device:
        """
        
            Returns:
                the device this parameter belongs to.
        
        
        """
        ...
    def getParameterGroups(self) -> java.util.Set[str]: ...
    def getParameterType(self) -> 'ParameterType':
        """
            Returns the type of this parameter.
        
            Returns:
                the type of this parameter.
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getPropertyField(self) -> cern.lsa.domain.devices.type.PropertyField:
        """
            Returns the property/field design info for this parameter
        
            Returns:
                the property/field design info
        
        
        """
        ...
    def getValueDescriptor(self) -> cern.accsoft.commons.value.ValueDescriptor:
        """
            Returns the value descriptor for this parameter. ValueDescriptor object holds information about:
        
              - maximal, minimal parameter values
              - precision
              - enumeration of possible values
              - unit - any of methods: getYUnit(), getXUnit() can be used, because they will all return exactly same value. There is
                only 1 unit
              - array dimensions iff this is array parameter
        
        
            Returns:
                ValueDescriptor object for this parameter
        
        
        """
        ...
    def getValueType(self) -> cern.accsoft.commons.value.Type:
        """
            Returns value type of this parameter such as INT, DOUBLE, FLOAT_ARRAY, etc.
        
            Returns:
                the type of value the parameter can take.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Setting.getValueType`
        
        
        """
        ...
    def isCritical(self) -> bool:
        """
            Returns :code:`true` if this parameter is marked as critical. Critical parameters can be trimmed only by users who have
            a dedicated MCS RBAC role.
        
            The concept of critical parameters is part of the Machine Critical Settings infrastructure.
        
            Returns:
                :code:`true` if this parameter is marked as critical.
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
            Returns :code:`true` if this parameter is a cycle-bound acquisition parameter. More details can be found in "Device
            Property behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Returns:
                :code:`true` if this parameter is cycle-bound, :code:`false` otherwise.
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isCycleBound`, :meth:`~cern.lsa.domain.devices.Device.isCycleBound`
        
        
        """
        ...
    def isLsaImplementation(self) -> bool:
        """
            Return :code:`true`, if the parameter is implemented by LSA. This happens in the following scenarios: either the device
            server corresponds to LSA/InCA, either the corresponding property is added at the level of LSA and does not exists in
            the original class design.
        
            Returns:
                :code:`true`, if the parameter is implemented by LSA. :code:`false` otherwise.
        
        
        """
        ...
    def isMonitorable(self) -> bool:
        """
            Indicates if this type can be monitored.
        
            Returns:
                :code:`true` if this type is monitorable, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isMonitorable`
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Returns :code:`true` if this parameter is a multiplexed setting parameter. More details can be found in "Device Property
            behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Returns:
                :code:`true` if this parameter is multiplexed, :code:`false` otherwise.
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isMultiplexed`,
                :meth:`~cern.lsa.domain.devices.Device.isMultiplexed`
        
        
        """
        ...
    def isPropertySupportingPartialSet(self) -> bool:
        """
            Indicates if property associated with this parameter type supports partial set on the hardware i.e. if individual fields
            of this property can be set separately or all of them must be always set together.
        
            Returns:
                :code:`true` if the property supports partial set, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isSupportingPartialSet`
        
        
        """
        ...
    def isReadable(self) -> bool:
        """
            Indicates if this parameter is readable.
        
            Returns:
                :code:`true` if this parameter is readable, :code:`false` otherwise.
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isReadable`
        
        
        """
        ...
    def isReservedForOpExperts(self) -> bool:
        """
            Returns whether parameter is reserved for OP experts. In other words whether the parameter is representing a property of
            a device that is an expert property with restricted access.
        
            Returns:
                whether parameter is expert.
        
        
        """
        ...
    def isTrimable(self) -> bool:
        """
            Returns :code:`true` is the parameter is trimmable , :code:`false` otherwise.
        
            If parameter is marked as non-trimmable - it cannot be trimmed directly. Its setting can be only calculated by a make
            rule.
        
            Returns:
                :code:`true` is the parameter is trimmable, :code:`false` otherwise.
        
        
        """
        ...
    def isVirtual(self) -> bool: ...
    def isWritable(self) -> bool:
        """
            Indicates if this parameter is writable.
        
            Returns:
                :code:`true` if this parameter is writable, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isWritable`
        
        
        """
        ...

class ParameterAttributes(cern.accsoft.commons.util.Named, java.io.Serializable):
    """
    public interface ParameterAttributes extends cern.accsoft.commons.util.Named, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Provides attribute values to be updated on Parameter. :code:`null` value means that attribute has to be deleted.
    """
    def getAbsoluteTolerance(self) -> float:
        """
        
            Returns:
                :code:`null` to delete attribute or absoluteTolerance to set on Parameter
        
        
        """
        ...
    def getDefaultHierarchy(self) -> str: ...
    def getDevice(self) -> cern.lsa.domain.devices.Device: ...
    def getMaxValue(self) -> float:
        """
        
            Returns:
                :code:`null` to delete attribute or maxValue which overrides default maxValue coming from
                :meth:`~cern.lsa.domain.devices.type.PropertyFieldVersion.getValueDescriptor`
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
        
            Returns:
                :code:`null` to delete attribute or minValue which overrides default minValue coming from
                :meth:`~cern.lsa.domain.devices.type.PropertyFieldVersion.getValueDescriptor`
        
        
        """
        ...
    def getParameterId(self) -> int:
        """
        
            Returns:
                parameter id
        
        
        """
        ...
    def getParameterName(self) -> str: ...
    def getParameterType(self) -> 'ParameterType': ...
    def getPropertyField(self) -> cern.lsa.domain.devices.type.PropertyField: ...
    def getRelativeTolerance(self) -> float:
        """
        
            Returns:
                :code:`null` to delete attribute or relativeTolerance to set on Parameter
        
        
        """
        ...
    def getXPrecision(self) -> int:
        """
        
            Returns:
                :code:`null` to delete attribute or xPrecision to set on Parameter
        
        
        """
        ...
    def getYPrecision(self) -> int:
        """
        
            Returns:
                :code:`null` to delete attribute or yPrecision to set on Parameter
        
        
        """
        ...
    def isBelongsToFunctionBProc(self) -> bool: ...
    def isReservedForOpExperts(self) -> bool: ...
    def isTrimable(self) -> bool: ...
    def setAbsoluteTolerance(self, double: float) -> None: ...
    def setBelongsToFunctionBProc(self, boolean: bool) -> None: ...
    def setDefaultHierarchy(self, string: str) -> None: ...
    def setMaxValue(self, double: float) -> None: ...
    def setMinValue(self, double: float) -> None: ...
    def setParameterId(self, long: int) -> None: ...
    def setParameterName(self, string: str) -> None: ...
    def setRelativeTolerance(self, double: float) -> None: ...
    def setReservedForOpExperts(self, boolean: bool) -> None: ...
    def setTrimable(self, boolean: bool) -> None: ...
    def setXPrecision(self, integer: int) -> None: ...
    def setYPrecision(self, integer: int) -> None: ...

class ParameterForEditing(cern.accsoft.commons.util.Named, java.io.Serializable):
    """
    public class ParameterForEditing extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.accsoft.commons.util.Named, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, parameter: Parameter, parameterAttributes: ParameterAttributes): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def getParameter(self) -> Parameter: ...
    def getParameterAttributes(self) -> ParameterAttributes: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ParameterGroup(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface ParameterGroup extends cern.accsoft.commons.util.Named, :class:`~cern.lsa.domain.commons.IdentifiedEntity`
    
        Parameter group is used to group together parameters which have something in common. It is represented basically by it's
        name (e.g. MAGNETS, VIRTUAL DEVICES). Group can contain many parameters and one parameter can be in many groups. Each
        group is assigned to accelerator and all parameters in it must belong to the same accelerator.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                accelerator to which group belongs.
        
        
        """
        ...
    def getCreateDate(self) -> java.util.Date:
        """
        
            Returns:
                date when group was created
        
        
        """
        ...
    def getCreator(self) -> str:
        """
        
            Returns:
                identifier of a person who created this group.
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Returns:
                descriptions of group.
        
        
        """
        ...

class ParameterNotFoundException(java.lang.RuntimeException):
    """
    public class ParameterNotFoundException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
        Thrown when LSA parameter name is used for some operation but such parameter is not defined in LSA database.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]): ...
    def getParameterNames(self) -> java.util.SortedSet[str]: ...

class ParameterSettings:
    """
    public interface ParameterSettings
    
        A collection of settings for a parameter and for all beam processes.
    """
    def getCurrentBeamProcesses(self) -> java.util.Set['BeamProcess']: ...
    def getCurrentSetting(self, beamProcess: 'BeamProcess') -> 'Setting':
        """
            Returns the current setting for the given beam process. The setting returned is always the current one, whether an
            updated value has been given or not.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
        
            Returns:
                the current setting for the given beam process or null if the given beam process has no setting
        
        
        """
        ...
    def getCurrentSettings(self) -> java.util.Set['Setting']: ...
    def getParameter(self) -> Parameter:
        """
            Returns the name of the parameter these settings are for.
        
            Returns:
                the name of the parameter these settings are for
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getSetting(self, beamProcess: 'BeamProcess') -> 'Setting':
        """
            Returns either the current setting or the updated setting if one exist for the given beam process. The setting returned
            is always the updated one if it exist and the current one if no updated setting has been given for the given beam
            process.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
        
            Returns:
                the current or the updated setting for the given beam process
        
        
        """
        ...
    def getSettings(self) -> java.util.Set['Setting']: ...
    def getUpdatedBeamProcesses(self) -> java.util.Set['BeamProcess']: ...
    def getUpdatedSetting(self, beamProcess: 'BeamProcess') -> 'Setting':
        """
            Returns the updated setting for the given beam process. The setting returned is always the updated one, or null if no
            update has been set.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
        
            Returns:
                the updated setting for the given beam process or null if the given beam process has not been updated
        
        
        """
        ...
    def getUpdatedSettings(self) -> java.util.Set['Setting']: ...
    def getValueType(self) -> cern.accsoft.commons.value.Type:
        """
            Returns the type of the value of all settings in this collection.
        
            Returns:
                the type of the value of all settings in this collection
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Returns :code:`true` if there are no settings, neither current nor updated ones or :code:`false` when some settings are
            present.
        
            Returns:
                :code:`true` if there are no settings, :code:`false` when some settings are present
        
        
        """
        ...
    @typing.overload
    def isUpdated(self) -> bool:
        """
            Returns true if at least one setting has been updated, false else.
        
            Returns:
                true if at least one setting has been updated, false else.
        
        """
        ...
    @typing.overload
    def isUpdated(self, beamProcess: 'BeamProcess') -> bool:
        """
            Returns :code:`true` if the setting for the given beam process has been updated, otherwise :code:`false`.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to be checked for update
        
            Returns:
                :code:`true` if the setting for the given beam process has been updated, otherwise :code:`false`.
        
        
        """
        ...
    def round(self) -> None:
        """
            Round all the settings that are part of this :code:`ParameterSettings` object.
        
        """
        ...
    def size(self) -> int:
        """
            Returns the number of current settings independently of the updated ones.
        
            Returns:
                the number of current settings independently of the updated ones
        
        
        """
        ...
    @typing.overload
    def updateSetting(self, beamProcess: 'BeamProcess', immutableValue: cern.accsoft.commons.value.ImmutableValue, settingPartEnum: 'SettingPartEnum') -> None:
        """
            Updates the setting belonging to the given beam process with the given value.
        
            First, if there is no :meth:`~cern.lsa.domain.settings.ParameterSettings.getCurrentSetting`, the method initializes it
            with an :meth:`~cern.lsa.domain.settings.SettingFactory.newInitialSetting`. If there is already an
            :meth:`~cern.lsa.domain.settings.ParameterSettings.getUpdatedSetting` - the method just updates it with the given value.
            Otherwise it clones the current setting, updates it with the given value and sets it as
            :meth:`~cern.lsa.domain.settings.ParameterSettings.getUpdatedSetting`.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process whose setting is to be updated
                updatedValue (cern.accsoft.commons.value.ImmutableValue): the value to use for the update
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the part of the setting to update
        
        """
        ...
    @typing.overload
    def updateSetting(self, beamProcess: 'BeamProcess', setting: 'Setting') -> None:
        """
            Updates the setting belonging to the given beam process with the given value.
        
            First, if there is no :meth:`~cern.lsa.domain.settings.ParameterSettings.getCurrentSetting`, the method initializes it
            with an :meth:`~cern.lsa.domain.settings.SettingFactory.newInitialSetting`. If there is already an
            :meth:`~cern.lsa.domain.settings.ParameterSettings.getUpdatedSetting` - the method just updates it with the given value.
            Otherwise it clones the current setting, updates it with the given value and sets it as
            :meth:`~cern.lsa.domain.settings.ParameterSettings.getUpdatedSetting`.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process whose setting is to be updated
                updatedSetting (:class:`~cern.lsa.domain.settings.Setting`): the setting to use for the update of the destination setting
        
        
        """
        ...

class ParameterTreeNode(cern.accsoft.commons.util.Named):
    """
    public interface ParameterTreeNode extends cern.accsoft.commons.util.Named
    
        A class used to store a hierarchy of parameters in a form of a tree.
    
    
    
    
        All methods within this class handle cyclic relations correctly, i.e. they do not get stuck in an infinite recursion
        loop when they encounter a cyclic dependency.
    """
    def findNode(self, string: str) -> 'ParameterTreeNode': ...
    def getAllChildren(self) -> java.util.List['ParameterTreeNode']: ...
    def getAllParents(self) -> java.util.List['ParameterTreeNode']: ...
    def getChildren(self) -> java.util.List['ParameterTreeNode']: ...
    @typing.overload
    def getNodes(self) -> java.util.List['ParameterTreeNode']: ...
    @typing.overload
    def getNodes(self, boolean: bool) -> java.util.List['ParameterTreeNode']: ...
    def getParameter(self) -> Parameter:
        """
        
            Returns:
                The parameter of this node.
        
        
        """
        ...
    def getParameters(self) -> java.util.List[Parameter]: ...
    def getParametersFromThisNodeAndAllChildren(self) -> java.util.List[Parameter]: ...
    def getParametersFromThisNodeAndAllParents(self) -> java.util.List[Parameter]: ...
    def getParents(self) -> java.util.List['ParameterTreeNode']: ...
    def getThisNodeAndAllChildren(self) -> java.util.List['ParameterTreeNode']: ...
    def getThisNodeAndAllParents(self) -> java.util.List['ParameterTreeNode']: ...
    def isLeaf(self) -> bool:
        """
        
            Returns:
                True if this node does not have any children, otherwise false.
        
        
        """
        ...
    def isRoot(self) -> bool:
        """
        
            Returns:
                True if this node does not have any parents, otherwise false.
        
        
        """
        ...
    def isSource(self) -> bool:
        """
        
            Returns:
                True if this node was requested as a source for certain operations (e.g. trim), otherwise false.
        
        
        """
        ...

class ParameterTreesRequest:
    """
    public interface ParameterTreesRequest
    
        Describes criteria when searching for parameter trees. This object should be created using
        :code:`ParameterTreesRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> cern.lsa.domain.settings.factory.ParameterTreesRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.ParameterTreesRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getHierarchy(self) -> str:
        """
            Name of the hierarchy in which search for trees. If not provided than DEFAULT hierarchy will be used.
        
        """
        ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getParameters(self) -> java.util.Set[Parameter]: ...
    def getTreeDirection(self) -> 'ParameterTreesRequest.TreeDirection':
        """
            Specifies direction of trees from provided parameters. It can be
            :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.TreeDirection.SOURCE_TREE` to look for source trees (upward
            direction) or :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.TreeDirection.DEPENDENT_TREE` to look for dependent
            trees (downward direction).
        
        """
        ...
    class TreeDirection(java.lang.Enum['ParameterTreesRequest.TreeDirection']):
        SOURCE_TREE: typing.ClassVar['ParameterTreesRequest.TreeDirection'] = ...
        DEPENDENT_TREE: typing.ClassVar['ParameterTreesRequest.TreeDirection'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ParameterTreesRequest.TreeDirection': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['ParameterTreesRequest.TreeDirection']: ...

class ParameterType(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity, java.lang.Comparable['ParameterType']):
    """
    public interface ParameterType extends cern.accsoft.commons.util.Named, :class:`~cern.lsa.domain.commons.IdentifiedEntity`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.settings.ParameterType`>
    
        Represents the type of a :class:`~cern.lsa.domain.settings.Parameter`, typically the same property field belonging to
        the same device type. It holds common characteristics and meta-information about all parameters of this type.
    
        Parameter types are also used to configure things that are common to all or many parameters of given type (such as make
        rules, link rules, incorporation rules) and to configure layout and display of generic applications.
    """
    def getCategory(self) -> 'ParameterTypeCategory':
        """
        
            Returns:
                the category of this parameter type or :code:`null` if not defined.
        
        
        """
        ...
    def isLinkRuleApplicable(self) -> bool:
        """
        
            Returns:
                whether a linkrule can be applied for this parameter type.
        
        
        """
        ...

class ParameterTypeCategory(java.lang.Enum['ParameterTypeCategory']):
    """
    public enum ParameterTypeCategory extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.settings.ParameterTypeCategory`>
    
        Assigns ParameterType to broad category. Category is used for ordering of Parameters.
    """
    PHYSICS: typing.ClassVar['ParameterTypeCategory'] = ...
    HW_MAGNITUDE: typing.ClassVar['ParameterTypeCategory'] = ...
    HW_SETTINGS: typing.ClassVar['ParameterTypeCategory'] = ...
    HW_REFERENCE: typing.ClassVar['ParameterTypeCategory'] = ...
    def getCategoryOrder(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ParameterTypeCategory':
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
    def values() -> typing.List['ParameterTypeCategory']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ParameterTypeCategory c : ParameterTypeCategory.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ParameterTypeGroup(cern.accsoft.commons.util.Named):
    """
    public interface ParameterTypeGroup extends cern.accsoft.commons.util.Named
    
        Represents a group of parameter types. The :code:`ParameterTypeGroup` is typically created for a group of parameters
        that are very related e.g. have the same :meth:`~cern.lsa.domain.settings.Parameter.getValueType` and the same make rule
        is used to compute their values (in case the parameter belongs to a hierarchy and has parent parameters).
    """
    def getParameterTypes(self) -> java.util.Set[ParameterType]: ...

class ParameterTypes:
    """
    public final class ParameterTypes extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    PARAMETERS_WITH_META_DATA: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> PARAMETERS_WITH_META_DATA
    
        Filter for the :class:`~cern.lsa.domain.settings.Parameter`'s which could potentially have additional information
        attached to them
    
    """
    def __init__(self): ...
    @staticmethod
    def createParameterType(deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion, string: str, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]], collection2: typing.Union[java.util.Collection[cern.lsa.domain.devices.type.PropertyVersion], typing.Sequence[cern.lsa.domain.devices.type.PropertyVersion]]) -> java.util.List[ParameterType]: ...
    @staticmethod
    def generateParameterTypeName(string: str, string2: str, string3: str) -> str:
        """
            Creates a new Parameter Type name following fixed naming conventions for creating types out of device, property,
            property field
        
            Parameters:
                deviceType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`):         property (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`):         propField (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                the generated parameter name
        
        
        """
        ...

class ParameterTypesRequest:
    """
    public interface ParameterTypesRequest
    
        Describes criteria when searching for LSA parameter types. This object should be created using
        :code:`ParameterTypesRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> cern.lsa.domain.settings.factory.ParameterTypesRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.ParameterTypesRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getParameterTypeNames(self) -> java.util.Set[str]: ...
    def isAllParameterTypesRequested(self) -> bool: ...

class Parameters:
    """
    public final class Parameters extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class with methods applying to parameters.
    """
    DEFAULT_FIELD_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_FIELD_NAME
    
        Default representation in GUIs when a parameter does not belong to a parameter group.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_PARAMETER_HIERARCHY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_PARAMETER_HIERARCHY
    
        Default Hierarchy name
    
        Also see:
            :meth:`~constant`
    
    
    """
    NOT_SUPPORTING_PARTIAL_SET: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> NOT_SUPPORTING_PARTIAL_SET
    
        Filter accepting parameters that DON'T support partial set.
    
        Also see:
            :meth:`~cern.lsa.domain.settings.Parameter.isPropertySupportingPartialSet`
    
    
    """
    NON_LSA_IMPLEMENTATION: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> NON_LSA_IMPLEMENTATION
    
        Filter accepting non LSA implementation parameters.
    
    """
    LSA_IMPLEMENTATION: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> LSA_IMPLEMENTATION
    
        Filter accepting LSA implementation parameters.
    
    """
    SETTING: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> SETTING
    
        Filter accepting setting parameters.
    
    """
    CRITICAL: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> CRITICAL
    
        Filter accepting :meth:`~cern.lsa.domain.settings.Parameter.isCritical` parameters.
    
    """
    READABLE: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> READABLE
    
        Filter accepting :meth:`~cern.lsa.domain.settings.Parameter.isReadable` parameters.
    
    """
    WRITABLE: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> WRITABLE
    
        Filter accepting :meth:`~cern.lsa.domain.settings.Parameter.isWritable` parameters.
    
    """
    MONITORABLE: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> MONITORABLE
    
        Filter accepting :meth:`~cern.lsa.domain.settings.Parameter.isMonitorable` parameters.
    
    """
    READABLE_AND_WRITABLE: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> READABLE_AND_WRITABLE
    
        Filter accepting :meth:`~cern.lsa.domain.settings.Parameter.isReadable` and
        :meth:`~cern.lsa.domain.settings.Parameter.isWritable` parameters.
    
    """
    NON_MULTIPLEXED: typing.ClassVar[cern.accsoft.commons.util.Filters.Filter] = ...
    """
    public static final cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.Parameter`> NON_MULTIPLEXED
    
        Filter accepting non-multiplexed parameters.
    
    """
    FEC_NAME: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.settings.Parameter`, `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`> FEC_NAME
    
    
    """
    FIELD_NAME: typing.ClassVar[cern.accsoft.commons.util.Mappers.Mapper] = ...
    """
    public static final cern.accsoft.commons.util.Mappers.Mapper<:class:`~cern.lsa.domain.settings.Parameter`, `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`> FIELD_NAME
    
    
    """
    @staticmethod
    def assertParametersDefined(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> None: ...
    @staticmethod
    def atLeastOneIsMultiplexed(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> bool: ...
    @staticmethod
    def atLeastOneIsReadable(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> bool: ...
    @staticmethod
    def atLeastOneIsWritable(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> bool: ...
    @staticmethod
    def belongsToParticleTransfer(parameter: Parameter, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> bool:
        """
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): a non-null parameter to be checked
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): a non-null particle transfer name
        
            Returns:
                :code:`true` if the specified parameter belongs to given particle transfer, otherwise :code:`false`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameter.getParticleTransfers`
        
        
        """
        ...
    @staticmethod
    def constructParameterName(string: str, string2: str, string3: str) -> str:
        """
            Creates a new parameter name from device, property and fieldname
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`):         propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`):         fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
        
        
        """
        ...
    @staticmethod
    def containsField(string: str) -> bool:
        """
            Indicates if the given parameter name contains field name i.e. if the name is composed in the following way:
            deviceName/property#field. If :code:`null` is passed, the method returns :code:`false`.
        
            Returns:
                :code:`true` if the given parameter name contains field namae
        
        
        """
        ...
    @staticmethod
    def deviceIn(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.Device], typing.Sequence[cern.lsa.domain.devices.Device]]) -> cern.accsoft.commons.util.Filters.Filter[Parameter]: ...
    @staticmethod
    def deviceNameIn(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.accsoft.commons.util.Filters.Filter[Parameter]: ...
    @staticmethod
    def deviceTypeNameIn(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.accsoft.commons.util.Filters.Filter[Parameter]: ...
    @staticmethod
    def extractDefaultHierarchies(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[str]: ...
    @staticmethod
    def extractDeviceName(string: str) -> str:
        """
        
            Also see:
                :code:`Parameters.extractDeviceName(String)`
        
        
        """
        ...
    @staticmethod
    def extractDeviceNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[str]: ...
    @staticmethod
    def extractParameterName(string: str) -> str:
        """
        
            Also see:
                :code:`Parameters.extractDeviceAndProperty(String)`
        
        
        """
        ...
    @staticmethod
    def extractParameterNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[str]: ...
    @staticmethod
    def extractPropertyField(string: str) -> str:
        """
        
            Also see:
                :code:`Parameters.extractFieldName(String)`
        
        
        """
        ...
    @staticmethod
    def extractPropertyName(string: str) -> str:
        """
        
            Also see:
                :code:`Parameters.extractPropertyName(String)`
        
        
        """
        ...
    @staticmethod
    def extractPropertyNames(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[str]: ...
    @staticmethod
    def filterCriticalParameters(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterLeafNodes(collection: typing.Union[java.util.Collection[ParameterTreeNode], typing.Sequence[ParameterTreeNode]]) -> java.util.Set[ParameterTreeNode]: ...
    @staticmethod
    def filterLsaImplementationParameters(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterMonitorableParameters(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterNonLsaImplementationParameters(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterNonSignatureParameters(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByAccessMode(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], collection2: typing.Union[java.util.Collection['PropertyAccessMode'], typing.Sequence['PropertyAccessMode']]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByDeviceNames(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByDeviceProperties(set: java.util.Set[Parameter], set2: java.util.Set[str]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByDeviceTypeNames(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByDevices(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], collection2: typing.Union[java.util.Collection[cern.lsa.domain.devices.Device], typing.Sequence[cern.lsa.domain.devices.Device]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByImplementation(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], collection2: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceTypeImplementation], typing.Sequence[cern.lsa.domain.devices.DeviceTypeImplementation]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByMultiplexingCriteria(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], boolean: bool) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByParameterGroups(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByParticleTransfers(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], collection2: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByPropertyNames(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByTrimableCriteria(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], boolean: bool) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersByTypes(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterParametersNotBelongingToDeviceProperties(set: java.util.Set[Parameter], set2: java.util.Set[str]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterReadableParameters(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterRootNodes(collection: typing.Union[java.util.Collection[ParameterTreeNode], typing.Sequence[ParameterTreeNode]]) -> java.util.Set[ParameterTreeNode]: ...
    @staticmethod
    def filterSettingParameters(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def filterWritableParameters(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def getAllParameters(collection: typing.Union[java.util.Collection[ParameterTreeNode], typing.Sequence[ParameterTreeNode]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def getAncestors(collection: typing.Union[java.util.Collection[ParameterTreeNode], typing.Sequence[ParameterTreeNode]]) -> java.util.Set[ParameterTreeNode]: ...
    @staticmethod
    def getColumnCount(parameter: Parameter) -> int:
        """
            If the given parameter represents an array or array 2D, the method returns number of columns defined for given parameter
            (assuming that the parameter has :code:`ValueDescriptor`).
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): considered parameter
        
            Returns:
                number of columns (if relevant) or 0
        
        
        """
        ...
    @staticmethod
    def getDescendants(collection: typing.Union[java.util.Collection[ParameterTreeNode], typing.Sequence[ParameterTreeNode]]) -> java.util.Set[ParameterTreeNode]: ...
    @staticmethod
    def getDeviceNames(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[str]: ...
    @staticmethod
    def getDeviceProperties(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[str]: ...
    @staticmethod
    def getDeviceProperty(parameter: Parameter) -> str:
        """
            Constructs and returns JAPC-like parameter name (device/property). This method doesn't use parameter name to take the
            device name and property name but uses :meth:`~cern.lsa.domain.settings.Parameter.getDevice`.getName() and
            :meth:`~cern.lsa.domain.settings.Parameters.getPropertyName` methods. If the name of given parameter corresponds exactly
            to a real device and property, then the method behaves exactly like
            :meth:`~cern.lsa.domain.settings.Parameters.extractParameterName`.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): considered parameter
        
            Returns:
                JAPC-like parameter name with a real device and property
        
        
        """
        ...
    @staticmethod
    def getDeviceTypeNames(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[str]: ...
    @staticmethod
    def getDevices(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[cern.lsa.domain.devices.Device]: ...
    @staticmethod
    def getFieldName(parameter: Parameter) -> str:
        """
            The method returns property field name associated to this parameter.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): considered parameter
        
            Returns:
                name of associated property field
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameters.extractPropertyField`
        
        
        """
        ...
    @staticmethod
    def getFieldNames(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[str]: ...
    @staticmethod
    def getParameterByTypeName(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]], string: str) -> Parameter: ...
    @staticmethod
    def getParameterGroups(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[str]: ...
    @staticmethod
    def getParameterGroupsOrNoGroup(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[str]: ...
    @staticmethod
    def getParameterTypes(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[ParameterType]: ...
    @typing.overload
    @staticmethod
    def getParameters(collection: typing.Union[java.util.Collection[ParameterTreeNode], typing.Sequence[ParameterTreeNode]]) -> java.util.List[Parameter]: ...
    @typing.overload
    @staticmethod
    def getParameters(map: typing.Union[java.util.Map[str, DevicePropertyParameters], typing.Mapping[str, DevicePropertyParameters]]) -> java.util.Set[Parameter]: ...
    @staticmethod
    def getParticleTransfers(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    @staticmethod
    def getPropertyName(parameter: Parameter) -> str:
        """
            The method returns name of property associated to this parameter.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): considered parameter
        
            Returns:
                name of associated property
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameters.extractPropertyName`
        
        
        """
        ...
    @staticmethod
    def getPropertyNames(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Set[str]: ...
    @staticmethod
    def getRowCount(parameter: Parameter) -> int:
        """
            If the given parameter represents an array or array 2D, the method returns number of rows defined for given parameter
            (assuming that the parameter has :code:`ValueDescriptor`).
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): considered parameter
        
            Returns:
                number of rows (if relevant) or 0
        
        
        """
        ...
    @staticmethod
    def groupDevicePropertiesByDeviceType(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Map[str, java.util.Set[str]]: ...
    @staticmethod
    def groupParametersByDefaultHierarchy(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.SortedMap[str, java.util.Set[Parameter]]: ...
    @staticmethod
    def groupParametersByDeviceNames(set: java.util.Set[Parameter]) -> java.util.Map[str, java.util.Set[Parameter]]: ...
    @staticmethod
    def groupParametersByDeviceProperty(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Map[str, DevicePropertyParameters]: ...
    @staticmethod
    def groupParametersByDevices(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Map[cern.lsa.domain.devices.Device, java.util.Set[Parameter]]: ...
    @staticmethod
    def groupParametersByParticleTransfers(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Map[cern.accsoft.commons.domain.particletransfers.ParticleTransfer, java.util.Set[Parameter]]: ...
    @staticmethod
    def groupToParameterTypeGroups(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.List[ParameterTypeGroup]: ...
    @staticmethod
    def hasField(parameter: Parameter) -> bool:
        """
            Returns :code:`true` if given parameter represents a property field. This method simply checks if the parameter has an
            associated field name.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): considered parameter
        
            Returns:
                :code:`true` if the parameter represents a property field, :code:`false` if not
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameters.getFieldName`
        
        
        """
        ...
    @staticmethod
    def implementationIn(collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.DeviceTypeImplementation], typing.Sequence[cern.lsa.domain.devices.DeviceTypeImplementation]]) -> cern.accsoft.commons.util.Filters.Filter[Parameter]: ...
    @staticmethod
    def isCommandParameter(parameter: Parameter) -> bool:
        """
            Indicates if the given parameter is :meth:`~cern.lsa.domain.settings.Parameter.isWritable` and NOT
            :meth:`~cern.lsa.domain.settings.Parameter.isReadable`.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): checked parameter
        
            Returns:
                :code:`true` if the parameter is writable and non-readable, :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def isSettingParameter(parameter: Parameter) -> bool:
        """
            Indicates if the given parameter is :meth:`~cern.lsa.domain.settings.Parameter.isReadable` AND
            :meth:`~cern.lsa.domain.settings.Parameter.isWritable` i.e. it can have an associated setting.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): checked parameter
        
            Returns:
                :code:`true` if the parameter is readable AND writable, :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def isSignatureParameter(parameter: Parameter) -> bool:
        """
        
            Also see:
                :code:`Named.getName()`
        
        
        """
        ...
    @staticmethod
    def isSimpleProperty(set: java.util.Set[Parameter]) -> bool: ...
    @typing.overload
    @staticmethod
    def mapByDeviceName(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> java.util.Map[str, Parameter]: ...
    @typing.overload
    @staticmethod
    def mapByDeviceName(set: java.util.Set[Parameter]) -> java.util.Map[str, Parameter]: ...
    @staticmethod
    def mapByParameterTypeNames(set: java.util.Set[Parameter]) -> java.util.Map[str, Parameter]: ...
    @staticmethod
    def parameterTypeNameIn(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.accsoft.commons.util.Filters.Filter[Parameter]: ...
    @staticmethod
    def particleTransferIn(collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]]) -> cern.accsoft.commons.util.Filters.Filter[Parameter]: ...
    @staticmethod
    def propertyNameIn(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> cern.accsoft.commons.util.Filters.Filter[Parameter]: ...
    @staticmethod
    def toArray(collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> typing.List[Parameter]: ...

class ParametersRequest:
    """
    public interface ParametersRequest
    
        Describes criteria when searching for LSA parameters. This object should be created using
        :code:`ParametersRequestBuilder` and passed to appropriate finder method.
    
        If a criteria is not specified (should not be taken into account), the corresponding method returns :code:`null`. Be
        aware that specifying an empty collection (to a criteria accepting collection) means that this criteria **will** be
        taken into account (usually resulting in empty result of the invocation).
    """
    @staticmethod
    def builder() -> cern.lsa.domain.settings.factory.ParametersRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.ParametersRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                name of accelerator that the parameters should belong to.
        
        
        """
        ...
    def getAcceleratorZones(self) -> java.util.Set[cern.accsoft.commons.domain.zones.AcceleratorZone]: ...
    def getDeviceNames(self) -> java.util.Set[str]: ...
    def getDevices(self) -> java.util.Set[cern.lsa.domain.devices.Device]: ...
    def getParameterGroups(self) -> java.util.Set[str]: ...
    def getParameterNamePattern(self) -> str:
        """
        
            Returns:
                parameter name pattern which all parameter names should match. The pattern is a SQL pattern accepted by the :code:`LIKE`
                clause (containing **%** or **_** (underscore) characters). Matching is case insensitive.
        
        
        """
        ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getParameterTypeNames(self) -> java.util.Set[str]: ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getPropertyFields(self) -> java.util.Set[cern.lsa.domain.devices.type.PropertyField]: ...
    def getPropertyNames(self) -> java.util.Set[str]: ...
    def getValueTypes(self) -> java.util.Set[cern.accsoft.commons.value.Type]: ...
    def isCritical(self) -> bool:
        """
        
            Returns:
                whether only parameters marked as critical or non-critical should be returned.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameter.isCritical`
        
        
        """
        ...
    def isIncludeSignatures(self) -> bool:
        """
        
            Returns:
                TRUE to include the special LSA internal signature parameters for MCS properties.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameters.isSignatureParameter`
        
        
        """
        ...
    def isLsaImplementation(self) -> bool:
        """
            Determines whether only parameters with implementation LSA should be returned.
        
            Returns:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#TRUE>` if only LSA
                parameters should be returned, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#FALSE>` if only non-LSA
                should be returned, :code:`null` if both LSA and non-LSA should be returned
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameter.isLsaImplementation`
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Determines whether parameters to be returned should be multiplexed or not.
        
            Returns:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#TRUE>` if multiplexed
                parameters should be returned, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#FALSE>` if non-multiplexed,
                :code:`null` if both multiplexed and non-multiplexed should be returned
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameter.isMultiplexed`
        
        
        """
        ...
    def isReadable(self) -> bool:
        """
            Determines whether only readable or only non-readable parameters should be returned.
        
            Readable parameters are these whose corresponding property
            :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isReadable`. Non-readable parameters are typically command
            parameters that one can only SET.
        
            Returns:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#TRUE>` if only
                readable parameters should be returned, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#FALSE>` if only non-readable
                should be returned, :code:`null` if both readable and non-readable should be returned
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameter.isReadable`
        
        
        """
        ...
    def isWritable(self) -> bool:
        """
            Determines whether only writable or only non-writable parameters should be returned.
        
            Writable parameters are these whose corresponding property
            :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isWritable`. Non-writable parameters are typically acquisition
            parameters or configuration read-only parameters that should not be trimmed and/or sent to the hardware.
        
            **Note that if the :meth:`~cern.lsa.domain.settings.Parameter.getParameterType` is not linked to any property**
        
            Returns:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#TRUE>` if only
                writable parameters should be returned, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#FALSE>` if only non-writable
                should be returned, :code:`null` if both writable and non-writable should be returned
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isWritable`
        
        
        """
        ...

class PropertyAccessMode(java.lang.Enum['PropertyAccessMode']):
    """
    public enum PropertyAccessMode extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.settings.PropertyAccessMode`>
    
        Enum representing the property access mode (writable, readable, monitorable, multiplexed)
    """
    WRITABLE: typing.ClassVar['PropertyAccessMode'] = ...
    READABLE: typing.ClassVar['PropertyAccessMode'] = ...
    MONITORABLE: typing.ClassVar['PropertyAccessMode'] = ...
    MULTIPLEXED: typing.ClassVar['PropertyAccessMode'] = ...
    def hasTheSameAccessMode(self, parameter: Parameter) -> bool: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PropertyAccessMode':
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
    def values() -> typing.List['PropertyAccessMode']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (PropertyAccessMode c : PropertyAccessMode.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Setting(cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface Setting extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`
    
        Represents a setting which is a value of a parameter for a given beam process. The context holds two values : a target
        and a correction. Values can be of several type : scalar value : a simple double (Scalar) array of scalar values : an
        array of double values (ScalarArray) 2D array of scalar values : a function (ScalarArray2d) discrete function : a
        function (DiscreteFunction) string : a string (StringValue) string array : a string array (StringArray)
    """
    def clone(self) -> 'Setting':
        """
            Returns a deep copy of this Setting.
        
            Returns:
                a deep copy of this Setting
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def getArray2DValue(self) -> cern.accsoft.commons.value.ImmutableScalarArray2D:
        """
            Returns the value of this setting as an array2d. In case of an array2d there is no consideration of target and
            correction. An array2d setting can only have one value.
        
            Returns:
                the value of this setting as an array2d.
        
        
        """
        ...
    def getArrayValue(self) -> cern.accsoft.commons.value.ImmutableScalarArray:
        """
            Returns the value of this setting as an array. In case of an array there is no consideration of target and correction.
            An array setting can only have one value.
        
            Returns:
                the value of this setting as an array.
        
        
        """
        ...
    def getBeamProcess(self) -> 'BeamProcess':
        """
            Returns the beam process this setting is defined for
        
            Returns:
                the beam process this setting is defined for
        
        
        """
        ...
    def getCorrectionFunctionValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Returns the correction value of this setting as a Function
        
            Returns:
                the correction part of this setting as a function
        
        
        """
        ...
    def getCorrectionFunctionsArrayValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray:
        """
            Returns the correction value of this setting as functionsArray
        
            Returns:
                the correction part of this setting as functionsArray
        
        
        """
        ...
    def getCorrectionScalarValue(self) -> cern.accsoft.commons.value.ImmutableScalar:
        """
            Returns the correction value of this setting as a scalar
        
            Returns:
                the correction part of this setting as a scalar
        
        
        """
        ...
    def getCorrectionValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Returns the correction value of this setting. If the setting holds no correction value (correction is not defined) the
            value returned depends on its type.
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Returns the non null date this setting have been created.
        
            Returns:
                the non null date this setting have been created
        
        
        """
        ...
    def getFunctionValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two value is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned is an empty discrete function.
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def getFunctionsArrayValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray:
        """
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two values is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned is an empty discrete functions array.
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def getParameter(self) -> Parameter:
        """
            Returns the parameter this contextual value is for
        
            Returns:
                the parameter this contextual value is for
        
        
        """
        ...
    def getScalarValue(self) -> cern.accsoft.commons.value.ImmutableScalar:
        """
            Returns the value of this setting as an scalar. The value is made of the sum of target value and the correction value.
            If one of the two value is not defined only the value defined will be used. If the setting holds no value (both target
            and correction are not defined) the value returned is Double.NaN.
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def getTargetFunctionValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Returns the target value of this setting as a Function
        
            Returns:
                the target part of this setting as a function
        
        
        """
        ...
    def getTargetFunctionsArrayValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray:
        """
            Returns the target value of this setting as functionsArray
        
            Returns:
                the target part of this setting as functionsArray
        
        
        """
        ...
    def getTargetScalarValue(self) -> cern.accsoft.commons.value.ImmutableScalar:
        """
            Returns the target value of this setting as a scalar
        
            Returns:
                the target part of this setting as a scalar
        
        
        """
        ...
    def getTargetValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Returns the target value of this setting. If the setting holds no target value (target is not defined) the value
            returned depends of its type.
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getTrimId(self) -> int:
        """
            Returns the trim id this setting is for
        
            Returns:
                the trim id this setting is for
        
        
        """
        ...
    def getValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two value is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned depends of its type.
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def getValueType(self) -> cern.accsoft.commons.value.Type:
        """
            Returns the type of the value holds by this setting.
        
            Returns:
                the type of the value holds by this setting.
        
            Also see:
                :code:`Type`
        
        
        """
        ...
    @typing.overload
    def updateValue(self, immutableValue: cern.accsoft.commons.value.ImmutableValue, settingPartEnum: 'SettingPartEnum') -> None:
        """
            Updates the target or the correction value of this setting depending of the given setting part. If the given part is
            VALUE, the correction value will be updated by substracting the target value to the given value. The target part will
            remain untouched unless the given value is null or the target part itself is null. If the given value is null and the
            part is VALUE, both, the target and the correction will be set to null. If the given part is CORRECTION, the correction
            value will be updated directly with the given value not affecting the target If the given part is TARGET, the target
            value will be updated directly with the given value not affecting the correction.
        
            Parameters:
                value (cern.accsoft.commons.value.ImmutableValue): the possibly null new value of the given part
                part (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the part of the setting to update
        
        """
        ...
    @typing.overload
    def updateValue(self, setting: 'Setting') -> None:
        """
            Updates the target and the correction value of this setting with the processed value of the target and the correction of
            the given setting. This only overwrites actual values, no additional processing is performed. If the given setting is
            null nothing will be updated.
        
            Parameters:
                sourceSetting (:class:`~cern.lsa.domain.settings.Setting`): the source setting from which the values of the target and the correction will be copied to this setting
        
        
        """
        ...

class SettingComparisonParameterResult:
    """
    public interface SettingComparisonParameterResult
    
        Result of the comparison between settings of various source and destination beam processes, for a given parameter. The
        number of the source and destination beam processes is the same and the comparison is performed one-to-one, considering
        the ordering of the beam processes as they have been set in the request.
    """
    def getDestinationBeamProcesses(self) -> java.util.List['BeamProcess']: ...
    def getDestinationDetailedException(self, beamProcess: 'BeamProcess') -> java.lang.Exception:
        """
            Returns the exception occurred when comparing the destination beam process.
        
            Parameters:
                destinationBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the destination beam process involved in the comparison operation.
        
            Returns:
                the exception occurred, if specified, when comparing the destination beam process; :code:`null` otherwise.
        
        
        """
        ...
    def getDestinationException(self) -> java.lang.Exception:
        """
            Returns exception, if defined, about the destination (e.g.: error occurred when loading destination settings).
        
            Returns:
                exception or :code:`null`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.ERROR`
        
        
        """
        ...
    def getDestinationSettings(self) -> ParameterSettings:
        """
            Settings of the parameter in the context(s) designated as *destination*. It may be null, depending on the type of the
            comparison result, and the configuration of the comparison request. It might not contain settings for all the
            destination beam processes.
        
            Returns:
                settings of the parameter in the destination context
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getResultType`,
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDestinationBeamProcesses`
        
        
        """
        ...
    def getDetailedResultType(self, beamProcess: 'BeamProcess', beamProcess2: 'BeamProcess') -> 'SettingComparisonResultType':
        """
            Returns the detailed result type of the comparison between settings of the source and destination beam process. If
            specified for some input beam processes, this result must be considered as a comparison result type of those beam
            processes. If it is not specified, the overall result type is considered as a comparison result type for the input beam
            processes.
        
            Parameters:
                sourceBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the source beam process involved in the comparison
                destBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the destination beam process involved in the comparison
        
            Returns:
                the detailed result type of the comparison between settings of the source and destination beam processes. It returns
                :code:`null` if not specified.
        
        
        """
        ...
    def getDetailedResultTypes(self) -> java.util.Map[cern.accsoft.commons.util.value.Pair['BeamProcess', 'BeamProcess'], 'SettingComparisonResultType']: ...
    def getParameter(self) -> Parameter:
        """
            Returns the parameter involved in the comparison.
        
            Returns:
                the parameter involved in the comparison. It is never :code:`null`.
        
        
        """
        ...
    def getResultType(self) -> 'SettingComparisonResultType':
        """
            The overall result type of the comparison between source and destination parameters' settings. Depending on this value,
            it may or may not make sense to check the values of the parameters and even the detailed result type: they might not be
            present.
        
        
            In general this result type is applicable to all the couple (source and destination beam process) compared. Eventually,
            for some of them there might be a detailed result type which overrides this one.
        
            Returns:
                the overall result type of the comparison
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDetailedResultType`
        
        
        """
        ...
    def getSourceBeamProcesses(self) -> java.util.List['BeamProcess']: ...
    def getSourceDetailedException(self, beamProcess: 'BeamProcess') -> java.lang.Exception:
        """
            Returns the exception occurred when comparing the source beam process.
        
            Parameters:
                sourceBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the source beam process involved in the comparison operation.
        
            Returns:
                the exception occurred, if specified, when comparing the source beam process; :code:`null` otherwise.
        
        
        """
        ...
    def getSourceException(self) -> java.lang.Exception:
        """
            Returns exception, if defined, about the source (e.g: error occurred when loading source settings).
        
            Returns:
                exception or :code:`null`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.ERROR`
        
        
        """
        ...
    def getSourceSettings(self) -> ParameterSettings:
        """
            Settings of the parameter in the context(s) designated as *source*. It may be null, depending on the type of the
            comparison result, and the configuration of the comparison request. It might not contain settings for all the source
            beam processes.
        
            Returns:
                settings of the parameter in the source context
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getResultType`,
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getSourceBeamProcesses`
        
        
        """
        ...

class SettingComparisonRequest:
    """
    public interface SettingComparisonRequest
    
        Request for a comparison between settings of parameters for different contexts.
    
        It is recommended to use the provided builder in order to create new comparison request instances.
    """
    def compareAllParameters(self) -> bool:
        """
            Returns :code:`true` if all settings should be compared between source and destination contexts; returns :code:`false`
            if only :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getParameters` parameters should be compared.
        
        """
        ...
    def getDestinationBeamProcesses(self) -> java.util.List['BeamProcess']: ...
    def getDestinationSettingsSource(self) -> 'SettingsSource':
        """
            Returns settings source of the destination context.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getDestinationBeamProcesses`
        
        
        """
        ...
    def getParameters(self) -> java.util.Set[Parameter]: ...
    def getPointInDestFunction(self) -> int:
        """
            Returns the point in time, in X, for the function of the destination parameter at which the comparison is to be made.
        
            Returns:
                point in the function for the destination parameter
        
        
        """
        ...
    def getPointInSourceFunction(self) -> int:
        """
            Returns the point in time, in X, for the function of the source parameter at which the comparison is to be made.
        
            Returns:
                point in the function for the source parameter
        
        
        """
        ...
    def getSourceBeamProcesses(self) -> java.util.List['BeamProcess']: ...
    def getSourceSettingsSource(self) -> 'SettingsSource':
        """
            Returns settings source of the source context.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getSourceBeamProcesses`
        
        
        """
        ...
    def ignoreFlatFunctionsLength(self) -> bool:
        """
            Returns :code:`true` if length should be ignored when comparing two flat functions i.e. if two flat functions have the
            same value but different length - they will be treated as the same.
        
            Returns:
                :code:`true` to treat two flat functions of the same value as the same even if their lengths are different
        
        
        """
        ...

class SettingComparisonResponse:
    """
    public interface SettingComparisonResponse
    
        The response of the setting comparison request.
    """
    def getSettingComparisonRequest(self) -> SettingComparisonRequest:
        """
            Returns the original comparison request which generated this response
        
            Returns:
                the original comparison request
        
        
        """
        ...
    def getSettingComparisonResult(self) -> 'SettingComparisonResult':
        """
            Returns the result of the comparison operation
        
            Returns:
                the result of the comparison operation
        
        
        """
        ...

class SettingComparisonResult:
    """
    public interface SettingComparisonResult
    
        The result of the comparison operation. For each parameter compared, this result contains detailed information of the
        comparison operation.
    """
    def getComparedParameters(self) -> java.util.Set[Parameter]: ...
    def getSettingComparisonParameterResult(self, parameter: Parameter) -> SettingComparisonParameterResult:
        """
            Returns the comparison result for the given compared parameter.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter the comparison result has to be retrieved
        
            Returns:
                Returns the comparison result for the given compared parameter. It returns :code:`null` if the parameter was not
                involved in the comparison operation.
        
        
        """
        ...
    def getSettingComparisonParameterResults(self) -> java.util.Map[Parameter, SettingComparisonParameterResult]: ...

class SettingComparisonResultType(java.lang.Enum['SettingComparisonResultType']):
    """
    public enum SettingComparisonResultType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.settings.SettingComparisonResultType`>
    
        Result of a comparison of settings of parameters in different contexts.
    """
    MATCH: typing.ClassVar['SettingComparisonResultType'] = ...
    MISMATCH: typing.ClassVar['SettingComparisonResultType'] = ...
    NO_SETTINGS: typing.ClassVar['SettingComparisonResultType'] = ...
    NO_SETTINGS_IN_SOURCE: typing.ClassVar['SettingComparisonResultType'] = ...
    NO_SETTINGS_IN_DEST: typing.ClassVar['SettingComparisonResultType'] = ...
    NOT_COMPARABLE: typing.ClassVar['SettingComparisonResultType'] = ...
    ERROR: typing.ClassVar['SettingComparisonResultType'] = ...
    FILTERED_OUT: typing.ClassVar['SettingComparisonResultType'] = ...
    UNDEFINED: typing.ClassVar['SettingComparisonResultType'] = ...
    @staticmethod
    def mostRepresentative(settingComparisonResultType: 'SettingComparisonResultType', settingComparisonResultType2: 'SettingComparisonResultType') -> 'SettingComparisonResultType':
        """
            Returns the most representative result type, between the results of the comparison of the settings of a given parameter
            in two different pairs of beam processes. The *priority scale* is:
            :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.ERROR` >
            :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.UNDEFINED` >
            :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.FILTERED_OUT` >
            :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.NOT_COMPARABLE` >
            :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.NO_SETTINGS` >
            :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.NO_SETTINGS_IN_SOURCE` >
            :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.NO_SETTINGS_IN_DEST` >
            :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.MISMATCH` >
            :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.MATCH`.
        
            Parameters:
                resultType1 (:class:`~cern.lsa.domain.settings.SettingComparisonResultType`): first result type
                resultType2 (:class:`~cern.lsa.domain.settings.SettingComparisonResultType`): second result type
        
            Returns:
                most restrictive result type
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SettingComparisonResultType':
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
    def values() -> typing.List['SettingComparisonResultType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SettingComparisonResultType c : SettingComparisonResultType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SettingFactory:
    """
    public class SettingFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory class that should be used to create instances of :code:`Setting` interface corresponding to the given beam
        process and parameter.
    """
    @typing.overload
    @staticmethod
    def newInitialSetting(beamProcess: 'BeamProcess', parameter: Parameter) -> Setting:
        """
            Creates an initial setting for given beam process and parameter.
        
        
            The value that is created depends on the parameter's :code:`value type`:
        
              - :code:`Type.FUNCTION` - a function with two points (0, 0) and (beamProcessLength, 0)
              - :code:`Type.FUNCTION_LIST` - a list with single function with two points (0, 0) and (beamProcessLength, 0)
              - :code:`Type.BOOLEAN` - :code:`false`
              - :code:`Type.STRING` - "" (empty string)
              - :code:`Type.ENUM` - the first enum value as registered in :code:`EnumType`
              - Numeric scalars (byte, int, double, ..) - 0
              - Arrays and Arrays 2D of any type - empty array
        
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): beam process for which setting should be created
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter for which setting should be created
        
            Returns:
                the setting with initial (default) value
        
            Creates an initial setting for given beam process and parameter.
        
        
            The value that is created depends on the requested :code:`value type`:
        
              - :code:`Type.FUNCTION` - a function with two points (0, 0) and (beamProcessLength, 0)
              - :code:`Type.FUNCTION_LIST` - a list with single function with two points (0, 0) and (beamProcessLength, 0)
              - :code:`Type.BOOLEAN` - :code:`false`
              - :code:`Type.STRING` - "" (empty string)
              - :code:`Type.ENUM` - the first enum value as registered in :code:`EnumType`
              - Numeric scalars (byte, int, double, ..) - 0
              - Arrays and Arrays 2D of any type - empty array
        
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): beam process for which setting should be created
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter for which setting should be created
                requestedValueType (cern.accsoft.commons.value.Type): requested value type of the setting
        
            Returns:
                the setting with initial (default) value
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newInitialSetting(beamProcess: 'BeamProcess', parameter: Parameter, type: cern.accsoft.commons.value.Type) -> Setting: ...
    @typing.overload
    @staticmethod
    def newSetting(beamProcess: 'BeamProcess', parameter: Parameter) -> Setting:
        """
            Creates a new setting for the given beam process and parameter. The specified value is set as a
            :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET` in the returned setting.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): beam process
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to create a setting for
                targetValue (cern.accsoft.commons.value.ImmutableValue): the value that goes to :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET` setting part
        
            Returns:
                the setting
        
            Creates a new setting for the given beam process and parameter.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): beam process
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to create a setting for
                targetValue (cern.accsoft.commons.value.ImmutableValue): the value that goes to :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET` setting part
                correctionValue (cern.accsoft.commons.value.ImmutableValue): the value that goes to :meth:`~cern.lsa.domain.settings.SettingPartEnum.CORRECTION` setting part
        
            Returns:
                the setting
        
            Creates a new empty setting for specified beam process and parameter
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): beam process
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): 
            Returns:
                new Setting
        
            Creates a new Setting.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): beam process
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter (not null)
                valueType (cern.accsoft.commons.value.Type): value type of the setting to be created
        
            Returns:
        
        """
        ...
    @typing.overload
    @staticmethod
    def newSetting(beamProcess: 'BeamProcess', parameter: Parameter, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> Setting: ...
    @typing.overload
    @staticmethod
    def newSetting(beamProcess: 'BeamProcess', parameter: Parameter, immutableValue: cern.accsoft.commons.value.ImmutableValue, immutableValue2: cern.accsoft.commons.value.ImmutableValue) -> Setting: ...
    @typing.overload
    @staticmethod
    def newSetting(beamProcess: 'BeamProcess', parameter: Parameter, type: cern.accsoft.commons.value.Type) -> Setting: ...
    @typing.overload
    @staticmethod
    def newSetting(type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.spi.AbstractSetting: ...

class SettingPartEnum(java.lang.Enum['SettingPartEnum']):
    """
    public enum SettingPartEnum extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.settings.SettingPartEnum`>
    
        A SettingPartEnum represents the information what part of a setting is affected by an action.
    """
    NONE: typing.ClassVar['SettingPartEnum'] = ...
    CORRECTION: typing.ClassVar['SettingPartEnum'] = ...
    TARGET: typing.ClassVar['SettingPartEnum'] = ...
    VALUE: typing.ClassVar['SettingPartEnum'] = ...
    UPDATE_TARGET_NO_CORRECTION: typing.ClassVar['SettingPartEnum'] = ...
    TARGET_AND_CORRECTION: typing.ClassVar['SettingPartEnum'] = ...
    UPDATE_VALUE_ON_TARGET: typing.ClassVar['SettingPartEnum'] = ...
    def getTypeName(self) -> str:
        """
            Returns a descriptive String for this constant.
        
            Returns:
                The content of :code:`typeName` that contains a :code:`String` that describes this type
        
        
        """
        ...
    def getValue(self) -> int:
        """
            Returns the integer value of that represents this setting part constant (this must be equal to the numbers in Setting
            e.g. Setting.CORRECTION).
        
            Returns:
                the integer value corresponding to this setting part constant.
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns the name of this enum.
        
            Overrides:
                 in class 
        
            Returns:
                the name of this enum
        
        
        """
        ...
    _valueOf_2__T = typing.TypeVar('_valueOf_2__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(int: int) -> 'SettingPartEnum':
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
        
            Returns a setting part enum constant constructed from the old constants of the Setting class (@see
            cern.lsa.settings.domain.Setting).
        
            Parameters:
                settingPart (int): one of the values Setting.CORRECTION, Setting.TARGET, Setting.VALUE, Setting.UPDATE_TARGET_NO_CORRECTION,
                    Setting.UPDATE_VALUE_ON_TARGET.
        
            Returns:
                the corresponding SettingPartEnum constant.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SettingPartEnum': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_2__T], string: str) -> _valueOf_2__T: ...
    @staticmethod
    def values() -> typing.List['SettingPartEnum']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SettingPartEnum c : SettingPartEnum.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Settings:
    """
    public class Settings extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class with settings-related methods.
    """
    @staticmethod
    def computeContextBeamInValue(standAloneContext: 'StandAloneContext', parameterSettings: ParameterSettings, settingPartEnum: SettingPartEnum) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Calculates value for the beam-in part of the context. The method returns also a correct value for scalar parameters.
        
            Parameters:
                ctx (:class:`~cern.lsa.domain.settings.StandAloneContext`): :class:`~cern.lsa.domain.settings.StandAloneContext` for which the values shall be calculated
                settings (:class:`~cern.lsa.domain.settings.ParameterSettings`): :class:`~cern.lsa.domain.settings.ParameterSettings` to calculate the values from
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the desired setting part
        
            Returns:
                beam-in value or :code:`null`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeContextValue(context: Context, parameterSettings: ParameterSettings) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Calls :meth:`~cern.lsa.domain.settings.Settings.computeContextValue` passing
            :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE` as the setting part.
        
            Parameters:
                ctx (:class:`~cern.lsa.domain.settings.Context`): context for which value should be computed, can be :code:`Cycle` or :code:`BeamProcess`
                settings (:class:`~cern.lsa.domain.settings.ParameterSettings`): parameter settings
        
            Returns:
                parameter value for given context
        
            Computes parameter value for specified context.
        
            Calls :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`, passing given context as a single element array.
        
            Parameters:
                ctx (:class:`~cern.lsa.domain.settings.Context`): context for which value should be computed, can be :code:`Cycle` or :code:`BeamProcess`
                settings (:class:`~cern.lsa.domain.settings.ParameterSettings`): parameter settings
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): setting part to be calculated
        
            Returns:
                parameter value for given context
        
        public static cern.accsoft.commons.value.ImmutableValue computeContextValue (:class:`~cern.lsa.domain.settings.StandAloneContext` ctx, `Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<? extends :class:`~cern.lsa.domain.settings.Context`> subCtx, :class:`~cern.lsa.domain.settings.ParameterSettings` settings, :class:`~cern.lsa.domain.settings.SettingPartEnum` settingPart)
        
            Convenience method that calls :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`. This method is meant to be
            used when we have stand alone context and sub contexts selected from a :code:`ContextSelector`. When we work with stand
            alone cycles - we can simply use selected sub-contexts. However when we select a StandAloneBeamProcess - the the list of
            sub-contexts is empty and :meth:`~cern.lsa.domain.settings.Settings.computeContextValue` would throw an exception.
        
            This method checks context family of the given :code:`StandAloneContext`. If it is a :code:`StandAloneBeamProcess` - it
            passes it to the method mentioned above, otherwise it passes the given collection of sub contexts.
        
            Parameters:
                ctx (:class:`~cern.lsa.domain.settings.StandAloneContext`): selected :code:`StandAloneContext`
                subCtx (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<? extends :class:`~cern.lsa.domain.settings.Context`> subCtx): list of sub-contexts
                settings (:class:`~cern.lsa.domain.settings.ParameterSettings`): parameter settings
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the setting part to be calculated
        
            Returns:
                parameter value for specified contexts
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`,
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`
        
        public static cern.accsoft.commons.value.ImmutableValue computeContextValue (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<? extends :class:`~cern.lsa.domain.settings.Context`> ctx, :class:`~cern.lsa.domain.settings.ParameterSettings` settings, :class:`~cern.lsa.domain.settings.SettingPartEnum` settingPart)
        
            Calculates parameter value for given collection of contexts.
        
            For discrete parameters the method returns value for the first compatible beam process i.e. if the parameter keeps
            settings in a discrete beam process - the method returns value of given parameter from the first discrete beam process
            intersected by specified contexts. The method behaves in the same way for discrete parameters that keep settings in the
            function beam processes, except that it returns value of the first matching function beam process.
        
        
            Note that if there is no setting for the first matching beam process, the method will check the following matching beam
            process, until it finds one with a setting. If there is no setting for none of the matching beam process - the method
            returns :code:`null`.
        
            For function parameters, the method concatenates function slices of all intersections between cycles and beam processes
            and returns result with X coordinate relative to the parent stand alone context. If there are any gaps in the computed
            function (e.g. when there is no setting for one beam process) these gaps are marked with a NaN number in the middle of
            the gap. If the gap is at the beginning or end of the returned function - it contains in addition NaN value at the
            beginning or end (respectively).
        
            If the specified collection of contexts is :code:`null` or empty - this method returns :code:`null`.
        
            Parameters:
                ctx (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<? extends :class:`~cern.lsa.domain.settings.Context`> ctx): contexts for which value should be computed. that can be either a :code:`StandAloneContext`, collection of
                    :code:`Cycle`s or collection of :code:`BeamProcess`es
                settings (:class:`~cern.lsa.domain.settings.ParameterSettings`): parameter settings
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the setting part to be calculated
        
            Returns:
                parameter value for specified contexts
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`,
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeContextValue(context: Context, parameterSettings: ParameterSettings, settingPartEnum: SettingPartEnum) -> cern.accsoft.commons.value.ImmutableValue: ...
    @typing.overload
    @staticmethod
    def computeContextValue(standAloneContext: 'StandAloneContext', collection: typing.Union[java.util.Collection[Context], typing.Sequence[Context]], parameterSettings: ParameterSettings, settingPartEnum: SettingPartEnum) -> cern.accsoft.commons.value.ImmutableValue: ...
    @typing.overload
    @staticmethod
    def computeContextValue(collection: typing.Union[java.util.Collection[Context], typing.Sequence[Context]], parameterSettings: ParameterSettings, settingPartEnum: SettingPartEnum) -> cern.accsoft.commons.value.ImmutableValue: ...
    @staticmethod
    def filterNonCommandSettings(collection: typing.Union[java.util.Collection[Setting], typing.Sequence[Setting]]) -> java.util.List[Setting]: ...
    @staticmethod
    def filterNonSignatureSettings(collection: typing.Union[java.util.Collection[Setting], typing.Sequence[Setting]]) -> java.util.Set[Setting]: ...
    @staticmethod
    def filterSignatureSettings(collection: typing.Union[java.util.Collection[Setting], typing.Sequence[Setting]]) -> java.util.Set[Setting]: ...
    @staticmethod
    def getBeamProcesses(collection: typing.Union[java.util.Collection[Setting], typing.Sequence[Setting]]) -> java.util.Set['BeamProcess']: ...
    @staticmethod
    def getFunction(contextSettings: ContextSettings, parameter: Parameter) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Extracts :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE` of given parameter from specified
            :code:`ContextSettings`.
        
            Parameters:
                ctxSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): context settings to extract the value from
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter for which value should be returned
        
            Returns:
                value of the parameter or :code:`null` if setting of given parameter is not present in the given :code:`ContextSettings`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`,
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`
        
        
        """
        ...
    @staticmethod
    def getFunctionList(contextSettings: ContextSettings, parameter: Parameter) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionList:
        """
            Extracts :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE` of given parameter from specified
            :code:`ContextSettings`.
        
            Parameters:
                ctxSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): context settings to extract the value from
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter for which value should be returned
        
            Returns:
                value of the parameter or :code:`null` if setting of given parameter is not present in the given :code:`ContextSettings`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`,
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`
        
        
        """
        ...
    @staticmethod
    def getFunctionValue(setting: Setting, settingPartEnum: SettingPartEnum) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Returns result of :meth:`~cern.lsa.domain.settings.Settings.getValue` cast to :code:`ImmutableScalar`.
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): setting from which appropriate setting part value should be extracted
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the requested setting part
        
            Returns:
                the corresponding value
        
        
        """
        ...
    @staticmethod
    def getFunctionsArrayValue(setting: Setting, settingPartEnum: SettingPartEnum) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray:
        """
            Returns result of :meth:`~cern.lsa.domain.settings.Settings.getValue` cast to :code:`ImmutableDiscreteFunctionsArray`.
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): setting from which appropriate setting part value should be extracted
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the requested setting part
        
            Returns:
                the corresponding value
        
        
        """
        ...
    @staticmethod
    def getPolynomialValue(setting: Setting, settingPartEnum: SettingPartEnum) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Returns a PolynomialFunction converted to an ImmutableDiscreteFunction.
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): setting from which appropriate setting part value should be extracted
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the requested setting part
        
            Returns:
                the corresponding value
        
        
        """
        ...
    @staticmethod
    def getScalar(contextSettings: ContextSettings, parameter: Parameter) -> cern.accsoft.commons.value.ImmutableScalar:
        """
            Extracts :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE` of given parameter from specified
            :code:`ContextSettings`.
        
            Parameters:
                ctxSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): context settings to extract the value from
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter for which value should be returned
        
            Returns:
                value of the parameter or :code:`null` if setting of given parameter is not present in the given :code:`ContextSettings`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`,
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`
        
        
        """
        ...
    @staticmethod
    def getScalarArray(contextSettings: ContextSettings, parameter: Parameter) -> cern.accsoft.commons.value.ImmutableScalarArray:
        """
            Extracts :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE` of given parameter from specified
            :code:`ContextSettings`.
        
            Parameters:
                ctxSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): context settings to extract the value from
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter for which value should be returned
        
            Returns:
                value of the parameter or :code:`null` if setting of given parameter is not present in the given :code:`ContextSettings`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`,
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`
        
        
        """
        ...
    @staticmethod
    def getScalarArray2D(contextSettings: ContextSettings, parameter: Parameter) -> cern.accsoft.commons.value.ImmutableScalarArray2D:
        """
            Extracts :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE` of given parameter from specified
            :code:`ContextSettings`.
        
            Parameters:
                ctxSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): context settings to extract the value from
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): parameter for which value should be returned
        
            Returns:
                value of the parameter or :code:`null` if setting of given parameter is not present in the given :code:`ContextSettings`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`,
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`
        
        
        """
        ...
    @staticmethod
    def getScalarValue(setting: Setting, settingPartEnum: SettingPartEnum) -> cern.accsoft.commons.value.ImmutableScalar:
        """
            Returns result of :meth:`~cern.lsa.domain.settings.Settings.getValue` cast to :code:`ImmutableScalar`.
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): setting from which appropriate setting part value should be extracted
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the requested setting part
        
            Returns:
                the corresponding value
        
        
        """
        ...
    @staticmethod
    def getUpdatedDrivableContexts(contextSettings: ContextSettings) -> java.util.Set['DrivableContext']: ...
    @typing.overload
    @staticmethod
    def getValue(contextSettings: ContextSettings, parameter: Parameter) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Extracts the setting's value of the specified :class:`~cern.lsa.domain.settings.Parameter` from the specified
            :class:`~cern.lsa.domain.settings.ContextSettings` for :meth:`~cern.lsa.domain.settings.ContextSettings.getContext`.
            Internally calls :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`.
        
            Parameters:
                ctxSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): :class:`~cern.lsa.domain.settings.ContextSettings` that contain the value to be extracted (or calculated, if necessary)
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): The :class:`~cern.lsa.domain.settings.Parameter` to return the setting's value for
        
            Returns:
                The value of the setting for the specified :class:`~cern.lsa.domain.settings.Parameter` from the specified
                :class:`~cern.lsa.domain.settings.ContextSettings` for :meth:`~cern.lsa.domain.settings.ContextSettings.getContext`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Settings.computeContextValue`, :meth:`~cern.lsa.domain.settings.Settings.getValue`
        
            Returns value of the given setting for specified setting part.
        
            For :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET` - the method returns
            :meth:`~cern.lsa.domain.settings.Setting.getTargetValue`, for
            :meth:`~cern.lsa.domain.settings.SettingPartEnum.CORRECTION` - the method returns
            :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` and for any other setting part - the method returns
            :meth:`~cern.lsa.domain.settings.Setting.getValue`.
        
            If the given setting is :code:`null`, the method returns :code:`null`.
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): setting from which appropriate setting part value should be extracted
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the requested setting part
        
            Returns:
                the corresponding value or :code:`null`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getValue(setting: Setting, settingPartEnum: SettingPartEnum) -> cern.accsoft.commons.value.ImmutableValue: ...
    @staticmethod
    def groupSettingsByValueType(collection: typing.Union[java.util.Collection[Setting], typing.Sequence[Setting]]) -> java.util.Map[cern.accsoft.commons.value.Type, java.util.List[Setting]]: ...
    @staticmethod
    def hasCorrectLength(setting: Setting) -> bool:
        """
            Checks the length of the setting. Especially for functions it checks, if their length matches the beamProcess length.
        
            Parameters:
                setting (:class:`~cern.lsa.domain.settings.Setting`): the setting to check
        
            Returns:
                true, if the length is correct
        
        
        """
        ...
    @staticmethod
    def hasUpdatedSetting(contextSettings: ContextSettings, set: java.util.Set[Parameter], beamProcess: 'BeamProcess') -> bool: ...
    @typing.overload
    @staticmethod
    def isContinue(immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, immutableDiscreteFunction2: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> bool:
        """
            Indicates if the given {code firstSetting} is continuous with the given :code:`secondSetting`. Continuity is checked
            separately on target and correction and if one of them is not continuous (or missing), the method returns :code:`false`.
        
            Parameters:
                firstSetting (:class:`~cern.lsa.domain.settings.Setting`): The :class:`~cern.lsa.domain.settings.Setting` which shall have its last value checked for continuity with the first
                    value from :code:`secondSetting`
                secondSetting (:class:`~cern.lsa.domain.settings.Setting`): The :class:`~cern.lsa.domain.settings.Setting` which shall have its first value checked for continuity with the last
                    value from :code:`firstSetting`
        
            Returns:
                True if both target and correction are continuous (or both are :code:`null`), otherwise false
        
            Verifies if the target function is continue with the next function. If both functions :code:`are empty` - the method
            returns :code:`true`. If only one of them is empty - the method returns :code:`false` otherwise the method returns
            result of the :code:`DiscreteFunctions.isContinueWith(ImmutableDiscreteFunction, ImmutableDiscreteFunction, double)`.
        
            Parameters:
                target (cern.accsoft.commons.value.ImmutableDiscreteFunction): the target function whose last point is checked versus first point of the next function
                next (cern.accsoft.commons.value.ImmutableDiscreteFunction): the following function whose first point is checked for continuity
        
            Returns:
                :code:`true` if functions are continue, :code:`false` otherwise
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def isContinue(setting: Setting, setting2: Setting) -> bool: ...
    @staticmethod
    def isInLimits(immutableValue: cern.accsoft.commons.value.ImmutableValue) -> bool:
        """
            Checks whether the value is within the limits defined by the value descriptor. More specifically,
            :code:`value.getValueDescriptor().getMin() < value < value.getValueDescriptor().getMax()` must hold true.
        
            For :code:`ScalarArray`s and :code:`ScalarArray2D`s, every element of the array is checked. For :code:`Function` s, all
            its values on the Y axis are checked.
        
            If there is no value descriptor, or if the minimum and maximum values are not defined, it returns :code:`true`.
        
            Parameters:
                value (cern.accsoft.commons.value.ImmutableValue): The :code:`ImmutableValue` to be checked
        
            Returns:
                True if the value is within its valid range, otherwise false
        
            Raises:
                : if the value is :code:`null`
        
            Also see:
                :code:`ImmutableValue.getValueDescriptor()`
        
        
        """
        ...
    @staticmethod
    def updateScalar(immutableScalar: cern.accsoft.commons.value.ImmutableScalar, immutableScalar2: cern.accsoft.commons.value.ImmutableScalar, boolean: bool) -> cern.accsoft.commons.util.value.Pair[bool, cern.accsoft.commons.value.ImmutableScalar]: ...
    @staticmethod
    def valuesAreEqual(immutableValue: cern.accsoft.commons.value.ImmutableValue, immutableValue2: cern.accsoft.commons.value.ImmutableValue) -> bool:
        """
            Compares two ImmutableValues for equality.
        
            Parameters:
                valueOne (cern.accsoft.commons.value.ImmutableValue): the first value to compare.
                valueTwo (cern.accsoft.commons.value.ImmutableValue): the second value to compare.
        
            Returns:
                :code:`true` - if the values are equal or both are null
        
        
                :code:`false` - if the values are not equal or only one of them is null
        
        
        """
        ...

class SettingsDeletionRequest:
    """
    @Immutable public interface SettingsDeletionRequest
    """
    @staticmethod
    def builder() -> 'DefaultSettingsDeletionRequest.Builder': ...
    @staticmethod
    def byStandAloneContextAndParameters(standAloneContext: 'StandAloneContext', collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> 'SettingsDeletionRequest': ...
    def getContext(self) -> 'StandAloneContext': ...
    def getParameters(self) -> java.util.Set[Parameter]: ...

class SettingsSource(java.io.Serializable):
    """
    public class SettingsSource extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Defines source of settings for a predefined context i.e. how settings of certain parameters should be retrieved from a
        given context e.g. current settings, historical settings or an archive.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def forArchiveVersionSettings(archiveVersion: ArchiveVersion) -> 'SettingsSource': ...
    @staticmethod
    def forCurrentSettings() -> 'SettingsSource': ...
    @staticmethod
    def forHardwareSettings() -> 'SettingsSource': ...
    @staticmethod
    def forHistoricalSettings(date: java.util.Date) -> 'SettingsSource': ...
    @staticmethod
    def forReferenceSettings() -> 'SettingsSource': ...
    @staticmethod
    def forTrimSettings(trimHeader: 'TrimHeader') -> 'SettingsSource': ...
    @staticmethod
    def forTrimTagSettingsOfAllParameters(trimTag: cern.lsa.domain.trim.tag.TrimTag) -> 'SettingsSource': ...
    @staticmethod
    def forTrimTagSettingsOfTaggedParameters(trimTag: cern.lsa.domain.trim.tag.TrimTag) -> 'SettingsSource': ...
    def getArchiveVersion(self) -> ArchiveVersion: ...
    def getDate(self) -> java.util.Date: ...
    def getTrimHeader(self) -> 'TrimHeader': ...
    def getType(self) -> 'SettingsSource.SettingsSourceType': ...
    def isTrimmedParametersOnly(self) -> bool: ...
    def isValid(self) -> bool:
        """
            Indicates if the source is valid i.e. if contains the source object e.g. if the
            :meth:`~cern.lsa.domain.settings.SettingsSource.getType` is
            :meth:`~cern.lsa.domain.settings.SettingsSource.SettingsSourceType.TRIM`, the method returns :code:`true` if the object
            contains the corresponding :meth:`~cern.lsa.domain.settings.SettingsSource.getTrimHeader`.
        
            If the type is :meth:`~cern.lsa.domain.settings.SettingsSource.SettingsSourceType.CURRENT_SETTINGS` then the method
            always returns :code:`true`.
        
            Returns:
                :code:`true` if the object is valid and contains all information, :code:`false` otherwise
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    class SettingsSourceType(java.lang.Enum['SettingsSource.SettingsSourceType']):
        CURRENT_SETTINGS: typing.ClassVar['SettingsSource.SettingsSourceType'] = ...
        HISTORICAL_SETTINGS: typing.ClassVar['SettingsSource.SettingsSourceType'] = ...
        TRIM: typing.ClassVar['SettingsSource.SettingsSourceType'] = ...
        TRIM_TAG: typing.ClassVar['SettingsSource.SettingsSourceType'] = ...
        ARCHIVE_VERSION: typing.ClassVar['SettingsSource.SettingsSourceType'] = ...
        REFERENCE: typing.ClassVar['SettingsSource.SettingsSourceType'] = ...
        HARDWARE: typing.ClassVar['SettingsSource.SettingsSourceType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'SettingsSource.SettingsSourceType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['SettingsSource.SettingsSourceType']: ...

class StandAloneContextCloneRequest:
    """
    public interface StandAloneContextCloneRequest
    
        Describes criteria when cloning :class:`~cern.lsa.domain.settings.StandAloneContext`s. Objects of this class should be
        created using :class:`~cern.lsa.domain.settings.factory.StandAloneContextCloneRequestBuilder` and passed to appropriate
        service (GenerationService).
    
        If a criteria is not specified the corresponding method returns an empty collection (in case the result type is a
        collection) or :code:`null` (in any other case).
    
        Also see:
            :class:`~cern.lsa.domain.settings.factory.StandAloneContextCloneRequestBuilder`
    """
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getCloneName(self) -> str:
        """
        
            Returns:
                name of the clone
        
        
        """
        ...
    def getContextCategory(self) -> ContextCategory:
        """
        
            Returns:
                category of the clone context
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Returns:
                description of the clone
        
        
        """
        ...
    def getHistoryCutOff(self) -> java.time.Instant:
        """
        
            Returns:
                the date from which the settings history will start if such a date was set, null otherwise
        
        
        """
        ...
    def getSource(self) -> 'StandAloneContext':
        """
        
            Returns:
                the source StandAloneContext to clone from
        
        
        """
        ...
    def shouldCloneType(self) -> bool:
        """
        
            Returns:
                weather we should also clone the type of the given standalone context all it's sub-contexts
        
        
        """
        ...
    def withHistory(self) -> bool:
        """
        
            Returns:
                flag deciding if the settings history should be also cloned
        
        
        """
        ...

class StandAloneContextCreationRequest:
    """
    public interface StandAloneContextCreationRequest
    
        Describes criteria when creating :class:`~cern.lsa.domain.settings.StandAloneContext`s. Objects of this class should be
        created using :class:`~cern.lsa.domain.settings.factory.StandAloneContextCreationRequestBuilder` and passed to
        appropriate service (GenerationService).
    
        If a criteria is not specified the corresponding method returns an empty collection (in case the result type is a
        collection) or :code:`null` (in any other case).
    
        Also see:
            :class:`~cern.lsa.domain.settings.factory.StandAloneContextCreationRequestBuilder`
    """
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getContextCategory(self) -> ContextCategory:
        """
        
            Returns:
                the context category to which the newly created context should belong
        
        
        """
        ...
    def getContextType(self) -> cern.lsa.domain.settings.type.ContextType:
        """
        
            Returns:
                The ContextType, which should serve as a pattern for the created :class:`~cern.lsa.domain.settings.StandAloneContext`
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Returns:
                description of the :class:`~cern.lsa.domain.settings.StandAloneContext` to be created
        
        
        """
        ...
    def getLength(self) -> int:
        """
        
            Returns:
                the requested length of the created context
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Returns:
                name of the to-be-created :class:`~cern.lsa.domain.settings.StandAloneContext`
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
        
            Returns:
                the multiplexity of the created context
        
        
        """
        ...

class StandAloneContextFilter(cern.accsoft.commons.util.Filters.Filter['StandAloneContext']):
    """
    public class StandAloneContextFilter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.accsoft.commons.util.Filters.Filter<:class:`~cern.lsa.domain.settings.StandAloneContext`>
    
        Simple :class:`~cern.lsa.domain.settings.StandAloneContext` filter.
    """
    def __init__(self): ...
    def accepts(self, standAloneContext: 'StandAloneContext') -> bool:
        """
        
            Specified by:
                :code:`accepts` in interface :class:`~cern.lsa.domain.settings.StandAloneContext`
        
        
        """
        ...
    @staticmethod
    def categoryIn(collection: typing.Union[java.util.Collection[ContextCategory], typing.Sequence[ContextCategory]]) -> 'StandAloneContextFilter': ...
    def setCategories(self, collection: typing.Union[java.util.Collection[ContextCategory], typing.Sequence[ContextCategory]]) -> 'StandAloneContextFilter': ...

class TrimException(cern.lsa.domain.LsaException):
    """
    public class TrimException extends :class:`~cern.lsa.domain.LsaException`
    
        An exception thrown when a trim related operation fails such as execution of a make rule, incorporation rule or link
        rule.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class TrimHeader(cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface TrimHeader extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`
    
        An TrimHeader represents the information about trim without the associated settings.
    """
    def getBeamProcesses(self) -> java.util.List['BeamProcess']: ...
    def getClientInfo(self) -> str:
        """
            Returns the information on the client who made the trim (app, user, host)
        
            Returns:
                the information on the client who made the trim (app, user, host)
        
        
        """
        ...
    def getCreatedDate(self) -> java.util.Date:
        """
            Returns the date at which this archive has been created.
        
            Returns:
                the date at which this archive has been created.
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Returns the description associated with this trim.
        
            Returns:
                the description associated with this trim.
        
        
        """
        ...
    def isTag(self) -> bool:
        """
            Returns true if the trim is a tag, false otherwise
        
            Returns:
                true if the trim is a tag, false otherwise
        
        
        """
        ...

class TrimHeadersRequest(java.io.Serializable):
    """
    public class TrimHeadersRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Represents a request to obtain trim headers.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'TrimHeadersRequestBuilder':
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.TrimHeadersRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    @staticmethod
    def byBeamProcessesAndParameters(collection: typing.Union[java.util.Collection['BeamProcess'], typing.Sequence['BeamProcess']], collection2: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> 'TrimHeadersRequest': ...
    def getBeamProcesses(self) -> java.util.Collection['BeamProcess']: ...
    def getMaxLastTrimsNumber(self) -> int:
        """
        
            Returns:
                a possibly :code:`null` maximum number of latest trim headers to return. If :code:`null` no constraint of maximum number
                is taken into account.
        
        
        """
        ...
    def getParameters(self) -> java.util.Collection[Parameter]: ...
    def getStartingFrom(self) -> java.time.Instant:
        """
        
            Returns:
                a possibly :code:`null` timestamp from which on to find the trims performed. If :code:`null` no constraint of timestamp
                is taken into account.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class TrimHeadersRequestBuilder:
    """
    public class TrimHeadersRequestBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self): ...
    def beamProcesses(self, collection: typing.Union[java.util.Collection['BeamProcess'], typing.Sequence['BeamProcess']]) -> 'TrimHeadersRequestBuilder': ...
    def build(self) -> TrimHeadersRequest: ...
    @staticmethod
    def byBeamProcessesAndParameters(collection: typing.Union[java.util.Collection['BeamProcess'], typing.Sequence['BeamProcess']], collection2: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> TrimHeadersRequest: ...
    def maxLastTrimsNumber(self, integer: int) -> 'TrimHeadersRequestBuilder':
        """
        
            Parameters:
                maxLastTrimsNumber (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): a possibly :code:`null` maximum number of latest trim headers to return. If :code:`null` no constraint of maximum number
                    is taken into account.
        
            Returns:
                object in creation
        
        
        """
        ...
    def parameters(self, collection: typing.Union[java.util.Collection[Parameter], typing.Sequence[Parameter]]) -> 'TrimHeadersRequestBuilder': ...
    def startingFrom(self, instant: typing.Union[java.time.Instant, datetime.datetime]) -> 'TrimHeadersRequestBuilder':
        """
        
            Parameters:
                instant (`Instant <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/time/Instant.html?is-external=true>`): a possibly :code:`null` timestamp from which on to find the trims performed. If :code:`null` no constraint of timestamp
                    is taken into account.
        
            Returns:
                object in creation
        
        
        """
        ...

class TrimRequest:
    """
    public interface TrimRequest
    
        Represents a request to trim (to modify) settings of certain parameters. This interface describes all the
        characteristics of the trim that should be performed like :code:`StandAloneContext`, parameters, setting part etc.
    
        Instances of this interface should be created using :class:`~cern.lsa.domain.settings.factory.TrimRequestBuilder`.
    """
    @typing.overload
    @staticmethod
    def builder() -> cern.lsa.domain.settings.factory.TrimRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                the builder
        
        """
        ...
    @typing.overload
    @staticmethod
    def builder(trimRequest: 'TrimRequest') -> cern.lsa.domain.settings.factory.TrimRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getAttribute(self, string: str) -> typing.Any:
        """
            Returns a custom attribute associated with this request.
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
        
            Returns:
                attribute value
        
        
        """
        ...
    def getAttributes(self) -> java.util.Map[str, typing.Any]: ...
    def getChildSettingPart(self) -> SettingPartEnum:
        """
            Returns the setting part which should be used to update the children within the trim. Default value is
            :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET`.
        
        """
        ...
    def getContext(self) -> 'StandAloneContext':
        """
            Returns the :code:`StandAloneContext` on which the trim should be performed.
        
        """
        ...
    def getContextSettings(self) -> ContextSettings:
        """
            Returns :code:`ContextSettings` containing new setting values.
        
        """
        ...
    def getCustomSettingPart(self, parameter: Parameter) -> SettingPartEnum:
        """
            Returns the custom setting part to be used by the trim to update the setting for the given parameters. If no custom
            setting part is specified, this method returns null. (Typically then either the setting part for source parameters or
            the child setting part will be taken as default.)
        
        
        """
        ...
    def getCustomSettingPartMap(self) -> java.util.Map[Parameter, SettingPartEnum]: ...
    def getDescription(self) -> str:
        """
            Returns description of the trim (comment).
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimHeader.getDescription`
        
        
        """
        ...
    def getParameters(self) -> java.util.Set[Parameter]: ...
    def getSettingPart(self) -> SettingPartEnum:
        """
            Returns the setting part which should be used for the trim. Depending on the setting part the behavior is following:
        
              - :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE` - indicates that
                :meth:`~cern.lsa.domain.settings.Setting.getValue` of the setting present in the TrimRequest will be compared with the
                current VALUE of the parameter and the difference will be put in the
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` of the resulting setting, with target value unchanged.
              - :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET` - indicates that
                :meth:`~cern.lsa.domain.settings.Setting.getValue` of the setting present in the TrimRequest will be put in the
                :meth:`~cern.lsa.domain.settings.Setting.getTargetValue` of the resulting setting, with correction value unchanged.
              - :meth:`~cern.lsa.domain.settings.SettingPartEnum.CORRECTION` - indicates that
                :meth:`~cern.lsa.domain.settings.Setting.getValue` of the setting present in the TrimRequest will be put in the
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` of the resulting setting, with target value unchanged.
              - :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET_AND_CORRECTION` - indicates that target of the setting present
                in the TrimRequest will be put in the target of the resulting setting, and correction will be put in correction of the
                resulting setting.
              - :meth:`~cern.lsa.domain.settings.SettingPartEnum.UPDATE_TARGET_NO_CORRECTION` - indicates that
                :meth:`~cern.lsa.domain.settings.Setting.getValue` of the setting present in the TrimRequest will be put in the
                :meth:`~cern.lsa.domain.settings.Setting.getTargetValue` of the resulting setting, with correction value set to ZERO or
                :code:`null` (in case the value type doesn't support correction).
        
            Note that for settings that don't support correction part e.g. BOOLEAN, STRING or arrays - the correction part won't be
            set even if setting part indicates so. In other words if one makes a trim on many parameters and uses
            :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET_AND_CORRECTION` - the correction will be ignored for such
            parameters.
        
        """
        ...
    def getTransactionId(self) -> int: ...
    def isCommit(self) -> bool:
        """
            Determines whether the trimmed settings should be committed after driven to the hardware.
        
            Returns:
                :code:`true` if commit should be performed after drive
        
        
        """
        ...
    def isDrive(self) -> bool:
        """
            Determines whether the trimmed settings should be driven to the hardware.
        
            Note that trim will attempt to drive settings only if the associated
            :meth:`~cern.lsa.domain.settings.TrimRequest.getContext` is
            :meth:`~cern.lsa.domain.settings.StandAloneContext.isResident`.
        
            Returns:
                :code:`true` if drive should be performed
        
        
        """
        ...
    def isForceDrive(self) -> bool:
        """
            Determines whether the trimmed settings should be driven to the hardware even if they have not changed.
        
        
            Returns:
                :code:`true` if drive should be performed even though there are no changes
        
        
        """
        ...
    def isForceProcessing(self) -> bool:
        """
            Determines if all rules should be executed even if by default it's not necessary. With such policy even if trimmed
            settings are the same as the current ones in the database - they will be marked as updated and propagated down in the
            hierarchy (all make rules will be executed). Also link rules and incorporation rules will be executed even if functions
            are continue.
        
            The only case when make rules won't be executed even with this policy is when the
            :meth:`~cern.lsa.domain.settings.TrimRequest.isPropagateToChildren` flag is set to :code:`false`.
        
            This property is meant for settings (re)generation when we want everything to be recalculated, taking into account
            possible change of configuration in the database or change of implementation of certain rules.
        
            Returns:
                :code:`true` if settings should be updated though there are no changes
        
        
        """
        ...
    def isIgnoreErrors(self) -> bool:
        """
            Determines if trim should continue if an error occurs or the :class:`~cern.lsa.domain.settings.TrimException` should be
            thrown.
        
            If this method returns :code:`true` - all exceptions that occurred during trim can be retrieved from
            :meth:`~cern.lsa.domain.settings.TrimResult.getWarnings`.
        
        """
        ...
    def isLenientDrive(self) -> bool:
        """
            The flag determines the trim and drive behavior in case when drive exceptions are encountered (ex. an equipment refused
            settings).
        
            This flag is taken into account only if the trim is performed on a resident context, the
            :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive` has been requested and when drive problems have been encountered.
            If the flag is :code:`false` (default) - drive transaction (if transactional parameters are part of the operation) will
            be rolled back, the trimmed settings will not be persisted and a :code:`DriveException` will be thrown. If the flag is
            :code:`true`, drive problems will be ignored and commit will be still issued both for drive transaction (if
            transactional parameters are part of the operation) and settings persistency.
        
            Returns:
                :code:`true` if the drive should be lenient (drive exceptions are ignored and drive transaction is committed and
                settings persisted)
        
        
        """
        ...
    def isPersistSettings(self) -> bool:
        """
            Determines if settings should be persisted in the database.
        
            This flag can be used to perform trim simulation.
        
            Returns:
                if :code:`true` settings will be persisted
        
        
        """
        ...
    def isPropagateToChildren(self) -> bool:
        """
            Determines whether trim made on given parameters should be propagated to all their dependent parameters.
        
            In most of situations this flag should be set to :code:`true` to keep settings within parameter trees consistent.
            However in some situations we might want not to propagate the change downwards the hierarchy e.g. when we trim a
            MOMENTUM parameter.
        
            Returns:
                if :code:`true` the change will be propagated to all dependent parameters (and their dependents)
        
        
        """
        ...
    def isRelative(self) -> bool:
        """
            Determines if values from the request should be treated as relative (delta) values (:code:`true`) or as absolute values
            (:code:`false`).
        
            Returns:
                :code:`true` if the request contains relative (delta) values
        
        
        """
        ...
    def isReturnSettings(self) -> bool:
        """
            Determines if after the trim operation the returned :class:`~cern.lsa.domain.settings.TrimResult` should contain
            :meth:`~cern.lsa.domain.settings.TrimResult.getContextSettings` object with current and updated settings of parameters
            affected by the trim.
        
            The flag should be set to :code:`true` only if the application calling the trim API is interested in affected parameters
            and/or affected settings. Otherwise this flag should be set to :code:`false`.
        
            Returns:
                :code:`true` if the ContextSettings object used by trim should be returned to the client within
                :class:`~cern.lsa.domain.settings.TrimResult`; :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimResult.getContextSettings`
        
        
        """
        ...
    def isSkipProcessing(self) -> bool:
        """
            Determines whether the trim should skip processing the settings i.e. run make rules, incorporation rules, link rules
            etc. This flag might be useful if one wants just to persist settings without any further processing.
        
            Returns:
                :code:`true` if settings should be processed by the trim or not
        
        
        """
        ...
    def setAttribute(self, string: str, object: typing.Any) -> None:
        """
            Sets a custom attribute for this request.
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
                attrValue (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): value of the attribute
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getAttribute`, :meth:`~cern.lsa.domain.settings.TrimRequest.getAttributes`
        
        
        """
        ...
    def setSettingPart(self, settingPartEnum: SettingPartEnum) -> None:
        """
            Allows to change the setting part to be used by the trim.
        
            Parameters:
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): setting part to be used by the trim
        
        
        """
        ...

class TrimResponse:
    """
    public interface TrimResponse
    
        Response of the trim operation that may optionally involve also driving settings to the hardware.
    """
    def getDriveResult(self) -> cern.lsa.domain.exploitation.DriveResult:
        """
            Result of the drive operation. This method returns :code:`null` if the trim didn't involve driving settings to the
            hardware. This may happen if the trimmed context is not resident or the drive was not requested in the
            :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive`.
        
            Returns:
                result of the drive operation
        
        
        """
        ...
    def getTrimResult(self) -> 'TrimResult':
        """
            Returns result of the trim operation.
        
            Returns:
                result of the trim operation
        
        
        """
        ...
    def isDrivePerformed(self) -> bool:
        """
            Returns :code:`true` if settings were driven to the hardware after trim operation. In other words it returns
            :code:`true` if the :meth:`~cern.lsa.domain.settings.TrimResponse.getDriveResult` is not :code:`null` and there was at
            least one parameter successfully driven to the hardware.
        
            Returns:
                :code:`true` if drive was performed, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimResponse.getDriveResult`
        
        
        """
        ...

class TrimResult:
    """
    public interface TrimResult
    
        Result of a trim operation, that provides access to the affected context, parameters, exceptions, etc.
    """
    def getAttribute(self, string: str) -> java.io.Serializable:
        """
            Returns value of a custom attribute that might have been set during :code:`trim` or :code:`drive` operations.
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the custom attribute
        
            Returns:
                attribute value or :code:`null` if the attribute was not set
        
        
        """
        ...
    def getContext(self) -> 'StandAloneContext':
        """
            Returns the :code:`StandAloneContext` on which the trim operation has been performed.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getContext`, :meth:`~cern.lsa.domain.settings.TrimResult.getTrimRequest`
        
        
        """
        ...
    def getContextSettings(self) -> ContextSettings:
        """
            Returns settings of all parameters loaded and calculated by the Trim. The object contains not only calculated settings
            but also settings of parameters that might have been used for calculations i.e. parent parameters.
        
            The method returns an object only if :meth:`~cern.lsa.domain.settings.TrimRequest.isReturnSettings` is set to
            :code:`true` (which is the default value).
        
        """
        ...
    def getTrimHeader(self) -> TrimHeader:
        """
            Return the :class:`~cern.lsa.domain.settings.TrimHeader` of the trim persisted following the
            :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                the :class:`~cern.lsa.domain.settings.TrimHeader` or null, if nothing was persisted
        
        
        """
        ...
    def getTrimRequest(self) -> TrimRequest:
        """
            Returns the request that was used to perform the trim operation.
        
            Returns:
                the original :code:`TrimRequest` object
        
        
        """
        ...
    def getWarnings(self) -> java.util.List[cern.accsoft.commons.util.value.Pair[str, java.lang.Throwable]]: ...

class UserContextMapping:
    """
    public interface UserContextMapping
    
        Mapping of a user to a drivable context. It provides information about when a user
        (:meth:`~cern.lsa.domain.settings.UserContextMapping.getUser`) and context (
        :meth:`~cern.lsa.domain.settings.UserContextMapping.getContextName` were mapped
        (:meth:`~cern.lsa.domain.settings.UserContextMapping.getMappingTimestamp`).
    """
    def equalByName(self, userContextMapping: 'UserContextMapping') -> bool:
        """
        
            Returns:
                true when given :class:`~cern.lsa.domain.settings.UserContextMapping` has the same name, the same parent's name
        
        
        """
        ...
    def getContextName(self) -> str:
        """
        
            Returns:
                name of the context for this mapping
        
        
        """
        ...
    def getContextParent(self) -> str:
        """
        
            Returns:
                name of the context containing this context
        
        
        """
        ...
    def getMappingTimestamp(self) -> int:
        """
        
            Returns:
                timestamp in which this mapping was established
        
        
        """
        ...
    def getOperationType(self) -> 'UserContextMapping.OperationType':
        """
        
            Returns:
                type of the operation
        
        
        """
        ...
    def getUser(self) -> str:
        """
        
            Returns:
                name of the user for this mapping
        
        
        """
        ...
    def isResident(self) -> bool:
        """
        
            Returns:
                true if context is resident
        
        
        """
        ...
    class OperationType(java.lang.Enum['UserContextMapping.OperationType']):
        INSERT: typing.ClassVar['UserContextMapping.OperationType'] = ...
        DELETE: typing.ClassVar['UserContextMapping.OperationType'] = ...
        UPDATE: typing.ClassVar['UserContextMapping.OperationType'] = ...
        @staticmethod
        def fromString(string: str) -> 'UserContextMapping.OperationType': ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'UserContextMapping.OperationType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['UserContextMapping.OperationType']: ...

class CopySettingsRequest(TrimRequest):
    """
    public interface CopySettingsRequest extends :class:`~cern.lsa.domain.settings.TrimRequest`
    
        Represents a request to copy settings from specified source contexts to given destination contexts.
    
        Instances of this interface should be created using
        :class:`~cern.lsa.domain.settings.factory.CopySettingsRequestBuilder`.
    """
    @staticmethod
    def builder() -> cern.lsa.domain.settings.factory.CopySettingsRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.CopySettingsRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getDestinationContexts(self) -> java.util.List[Context]: ...
    def getDestinationParameters(self) -> java.util.Set[Parameter]: ...
    def getSettingsSource(self) -> SettingsSource:
        """
            Descriptor of how source settings should be retrieved.
        
        """
        ...
    def getSourceContexts(self) -> java.util.List[Context]: ...

class CriticalParameterException(TrimException):
    """
    public class CriticalParameterException extends :class:`~cern.lsa.domain.settings.TrimException`
    
        Exception indicates that there was an error during processing of a critical parameter.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class CycleIntersections(ContextIntersections):
    """
    public interface CycleIntersections extends :class:`~cern.lsa.domain.settings.ContextIntersections`
    
        A collection of all settings for a given cycle and parameter. The collection keeps two versions of each setting, the
        current one and the updated one. The updated one can be null until an update is performed.
    """
    def getBeamProcesses(self) -> java.util.Set['BeamProcess']: ...
    def getCycleName(self) -> str:
        """
            Returns the cycle name this intersection is for
        
            Returns:
                the cycle name this intersection is for
        
        
        """
        ...
    def getFollowingBeamProcess(self, beamProcess: 'BeamProcess') -> 'BeamProcess':
        """
            Returns the FUNCTION beam process object following the FUNCTION one whose name is given, it returns the following for
            the SAME particle transfer. If there is no following, it returns null.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process from which to find the following
        
            Returns:
                the non null beam process object following the one whose name is given
        
        
        """
        ...
    def getIntersectedBeamProcesses(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> java.util.Set['BeamProcess']: ...
    def getIntersectedFunctionBeamProcess(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, double: float) -> BeamProcessIntersection:
        """
            Return the beam process that intersects the given x-coordinate. The given xCoordinate must be relative to the CYCLE. If
            no beam process is defined at that xCoordinate, null is returned. If a beam process is defined at that xCoordinate, it
            is returned. Together with the beam process name the x-coordinate of the intersection relative to the beam process is
            returned. That x-coordinate is the one matching the given x-coordinate (relative to the CYCLE) but inside the beam
            process and relative to that beam process.
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): the particle transfer in which to consider the intersection
                xCoordinate (double): the xCoordinate at which to find the intersecting beam process
        
            Returns:
                the intersecting beam process together with the x-coordinate of the intersection or null
        
        
        """
        ...
    def getIntersectedFunctionBeamProcesses(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, double: float) -> java.util.List[BeamProcessIntersection]: ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getPrecedingBeamProcess(self, beamProcess: 'BeamProcess') -> 'BeamProcess':
        """
            Returns the FUNCTION beam process object preceding the FUNCTION one whose name is given for the SAME particle transfer.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process from which to find the preceding
        
            Returns:
                the non null beam process object preceding the one whose name is given
        
        
        """
        ...
    def size(self) -> int:
        """
            Return the number of intersections in this collection
        
            Returns:
                the number of intersections in this collection
        
        
        """
        ...

class DefaultAcceleratorUser(AcceleratorUser, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultAcceleratorUser extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.AcceleratorUser`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.AcceleratorUser`.
    
        Use the builder to create immutable instances: :code:`DefaultAcceleratorUser.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultAcceleratorUser.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.DefaultAcceleratorUser`.
        
            .. code-block: java
            
             DefaultAcceleratorUser.builder()
                .id(long) // required :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId`
                .name(String) // required name
                .accelerator(cern.accsoft.commons.domain.Accelerator) // required :meth:`~cern.lsa.domain.settings.AcceleratorUser.getAccelerator`
                .acceleratorUserGroup(cern.lsa.domain.settings.AcceleratorUserGroup) // required :meth:`~cern.lsa.domain.settings.AcceleratorUser.getAcceleratorUserGroup`
                .multiplexed(boolean) // required :meth:`~cern.lsa.domain.settings.AcceleratorUser.isMultiplexed`
                .build();
             
        
            Returns:
                A new DefaultAcceleratorUser builder
        
        
        """
        ...
    @staticmethod
    def copyOf(acceleratorUser: AcceleratorUser) -> 'DefaultAcceleratorUser':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.AcceleratorUser` value. Uses accessors to get values to
            initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.AcceleratorUser`): The instance to copy
        
            Returns:
                A copied immutable AcceleratorUser instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.AcceleratorUser.getAccelerator`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.AcceleratorUser`
        
            Returns:
                The :code:`Accelerator` this :class:`~cern.lsa.domain.settings.AcceleratorUser` is associated with.
        
        
        """
        ...
    def getAcceleratorUserGroup(self) -> AcceleratorUserGroup:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.AcceleratorUser.getAcceleratorUserGroup`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.AcceleratorUser`
        
            Returns:
                The :class:`~cern.lsa.domain.settings.AcceleratorUserGroup` that this :class:`~cern.lsa.domain.settings.AcceleratorUser`
                belongs to.
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId` in interface :class:`~cern.lsa.domain.commons.IdentifiedEntity`
        
            Returns:
                identifier of this entity, any long number - positive, negative or 0
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`id`, :code:`name`, :code:`accelerator`, :code:`acceleratorUserGroup`,
            :code:`multiplexed`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Indicates whether this user is used for multiplexed contexts or not.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.AcceleratorUser.isMultiplexed`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.AcceleratorUser`
        
            Returns:
                :code:`true` if user is for multiplexed contexts, :code:`false` otherwise
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`AcceleratorUser` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DefaultAcceleratorUser':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.AcceleratorUser.getAccelerator` attribute. A shallow reference equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (cern.accsoft.commons.domain.Accelerator): A new value for accelerator
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withAcceleratorUserGroup(self, acceleratorUserGroup: AcceleratorUserGroup) -> 'DefaultAcceleratorUser':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.AcceleratorUser.getAcceleratorUserGroup` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.AcceleratorUserGroup`): A new value for acceleratorUserGroup
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultAcceleratorUser':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId`
            attribute. A value equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultAcceleratorUser':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.AcceleratorUser.isMultiplexed` attribute. A value equality check is used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for multiplexed
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultAcceleratorUser':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def accelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DefaultAcceleratorUser.Builder': ...
        def acceleratorUserGroup(self, acceleratorUserGroup: AcceleratorUserGroup) -> 'DefaultAcceleratorUser.Builder': ...
        def build(self) -> 'DefaultAcceleratorUser': ...
        def id(self, long: int) -> 'DefaultAcceleratorUser.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultAcceleratorUser.Builder': ...
        def name(self, string: str) -> 'DefaultAcceleratorUser.Builder': ...

class DefaultAcceleratorUserGroup(AcceleratorUserGroup, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultAcceleratorUserGroup extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.AcceleratorUserGroup`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.AcceleratorUserGroup`.
    
        Use the builder to create immutable instances: :code:`DefaultAcceleratorUserGroup.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultAcceleratorUserGroup.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.DefaultAcceleratorUserGroup`.
        
            .. code-block: java
            
             DefaultAcceleratorUserGroup.builder()
                .id(long) // required :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId`
                .name(String) // required name
                .description(String | null) // nullable :meth:`~cern.lsa.domain.settings.AcceleratorUserGroup.getDescription`
                .build();
             
        
            Returns:
                A new DefaultAcceleratorUserGroup builder
        
        
        """
        ...
    @staticmethod
    def copyOf(acceleratorUserGroup: AcceleratorUserGroup) -> 'DefaultAcceleratorUserGroup':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.AcceleratorUserGroup` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.AcceleratorUserGroup`): The instance to copy
        
            Returns:
                A copied immutable AcceleratorUserGroup instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDescription(self) -> str: ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId` in interface :class:`~cern.lsa.domain.commons.IdentifiedEntity`
        
            Returns:
                identifier of this entity, any long number - positive, negative or 0
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`id`, :code:`name`, :code:`description`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`AcceleratorUserGroup` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDescription(self, string: str) -> 'DefaultAcceleratorUserGroup': ...
    def withId(self, long: int) -> 'DefaultAcceleratorUserGroup':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId`
            attribute. A value equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultAcceleratorUserGroup':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultAcceleratorUserGroup': ...
        def description(self, string: str) -> 'DefaultAcceleratorUserGroup.Builder': ...
        def id(self, long: int) -> 'DefaultAcceleratorUserGroup.Builder': ...
        def name(self, string: str) -> 'DefaultAcceleratorUserGroup.Builder': ...

class DefaultAcceleratorUsersRequest(AcceleratorUsersRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultAcceleratorUsersRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.AcceleratorUsersRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.AcceleratorUsersRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultAcceleratorUsersRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultAcceleratorUsersRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.DefaultAcceleratorUsersRequest`.
        
            .. code-block: java
            
             DefaultAcceleratorUsersRequest.builder()
                .ids(Set<Long> | null) // nullable :meth:`~cern.lsa.domain.settings.AcceleratorUsersRequest.getIds`
                .accelerator(cern.accsoft.commons.domain.Accelerator | null) // nullable :meth:`~cern.lsa.domain.settings.AcceleratorUsersRequest.getAccelerator`
                .acceleratorUserNames(Set<String> | null) // nullable :meth:`~cern.lsa.domain.settings.AcceleratorUsersRequest.getAcceleratorUserNames`
                .multiplexed(Boolean | null) // nullable :meth:`~cern.lsa.domain.settings.AcceleratorUsersRequest.isMultiplexed`
                .acceleratorUserGroupName(String | null) // nullable :meth:`~cern.lsa.domain.settings.AcceleratorUsersRequest.getAcceleratorUserGroupName`
                .build();
             
        
            Returns:
                A new DefaultAcceleratorUsersRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(acceleratorUsersRequest: AcceleratorUsersRequest) -> 'DefaultAcceleratorUsersRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.AcceleratorUsersRequest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.AcceleratorUsersRequest`): The instance to copy
        
            Returns:
                A copied immutable AcceleratorUsersRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getAcceleratorUserGroupName(self) -> str: ...
    def getAcceleratorUserNames(self) -> com.google.common.collect.ImmutableSet[str]: ...
    def getIds(self) -> com.google.common.collect.ImmutableSet[int]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`ids`, :code:`accelerator`, :code:`acceleratorUserNames`,
            :code:`multiplexed`, :code:`acceleratorUserGroupName`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isMultiplexed(self) -> bool: ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`AcceleratorUsersRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DefaultAcceleratorUsersRequest': ...
    def withAcceleratorUserGroupName(self, string: str) -> 'DefaultAcceleratorUsersRequest': ...
    @typing.overload
    def withAcceleratorUserNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultAcceleratorUsersRequest': ...
    @typing.overload
    def withAcceleratorUserNames(self, stringArray: typing.List[str]) -> 'DefaultAcceleratorUsersRequest': ...
    @typing.overload
    def withIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultAcceleratorUsersRequest': ...
    @typing.overload
    def withIds(self, longArray: typing.List[int]) -> 'DefaultAcceleratorUsersRequest': ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultAcceleratorUsersRequest': ...
    class Builder:
        def accelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DefaultAcceleratorUsersRequest.Builder': ...
        def acceleratorUserGroupName(self, string: str) -> 'DefaultAcceleratorUsersRequest.Builder': ...
        def acceleratorUserNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultAcceleratorUsersRequest.Builder': ...
        def addAcceleratorUserName(self, string: str) -> 'DefaultAcceleratorUsersRequest.Builder': ...
        def addAcceleratorUserNames(self, stringArray: typing.List[str]) -> 'DefaultAcceleratorUsersRequest.Builder': ...
        def addAllAcceleratorUserNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultAcceleratorUsersRequest.Builder': ...
        def addAllIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultAcceleratorUsersRequest.Builder': ...
        def addId(self, long: int) -> 'DefaultAcceleratorUsersRequest.Builder': ...
        def addIds(self, longArray: typing.List[int]) -> 'DefaultAcceleratorUsersRequest.Builder': ...
        def build(self) -> 'DefaultAcceleratorUsersRequest': ...
        def ids(self, iterable: java.lang.Iterable[int]) -> 'DefaultAcceleratorUsersRequest.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultAcceleratorUsersRequest.Builder': ...

class DefaultHyperCycleMapping(HyperCycleMapping, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultHyperCycleMapping extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.HyperCycleMapping`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.HyperCycleMapping`.
    
        Use the builder to create immutable instances: :code:`DefaultHyperCycleMapping.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultHyperCycleMapping.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.DefaultHyperCycleMapping`.
        
            .. code-block: java
            
             DefaultHyperCycleMapping.builder()
                .user(cern.lsa.domain.settings.AcceleratorUser) // required :meth:`~cern.lsa.domain.settings.HyperCycleMapping.getUser`
                .beamProcess(cern.lsa.domain.settings.StandAloneBeamProcess) // required :meth:`~cern.lsa.domain.settings.HyperCycleMapping.getBeamProcess`
                .build();
             
        
            Returns:
                A new DefaultHyperCycleMapping builder
        
        
        """
        ...
    @staticmethod
    def copyOf(hyperCycleMapping: HyperCycleMapping) -> 'DefaultHyperCycleMapping':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.HyperCycleMapping` value. Uses accessors to get values
            to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.HyperCycleMapping`): The instance to copy
        
            Returns:
                A copied immutable HyperCycleMapping instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBeamProcess(self) -> 'StandAloneBeamProcess':
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycleMapping.getBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.HyperCycleMapping`
        
            Returns:
                The value of the :code:`beamProcess` attribute
        
        
        """
        ...
    def getUser(self) -> AcceleratorUser:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycleMapping.getUser`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.HyperCycleMapping`
        
            Returns:
                The value of the :code:`user` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`user`, :code:`beamProcess`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`HyperCycleMapping` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withBeamProcess(self, standAloneBeamProcess: 'StandAloneBeamProcess') -> 'DefaultHyperCycleMapping':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.HyperCycleMapping.getBeamProcess` attribute. A shallow reference equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.StandAloneBeamProcess`): A new value for beamProcess
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withUser(self, acceleratorUser: AcceleratorUser) -> 'DefaultHyperCycleMapping':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.domain.settings.HyperCycleMapping.getUser`
            attribute. A shallow reference equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.AcceleratorUser`): A new value for user
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def beamProcess(self, standAloneBeamProcess: 'StandAloneBeamProcess') -> 'DefaultHyperCycleMapping.Builder': ...
        def build(self) -> 'DefaultHyperCycleMapping': ...
        def user(self, acceleratorUser: AcceleratorUser) -> 'DefaultHyperCycleMapping.Builder': ...

class DefaultSettingsDeletionRequest(SettingsDeletionRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultSettingsDeletionRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.SettingsDeletionRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.SettingsDeletionRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultSettingsDeletionRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultSettingsDeletionRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.DefaultSettingsDeletionRequest`.
        
            .. code-block: java
            
             DefaultSettingsDeletionRequest.builder()
                .context(cern.lsa.domain.settings.StandAloneContext) // required :meth:`~cern.lsa.domain.settings.SettingsDeletionRequest.getContext`
                .addParameter|addAllParameters(cern.lsa.domain.settings.Parameter) // :meth:`~cern.lsa.domain.settings.SettingsDeletionRequest.getParameters` elements
                .build();
             
        
            Returns:
                A new DefaultSettingsDeletionRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(settingsDeletionRequest: SettingsDeletionRequest) -> 'DefaultSettingsDeletionRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.SettingsDeletionRequest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.SettingsDeletionRequest`): The instance to copy
        
            Returns:
                A copied immutable SettingsDeletionRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getContext(self) -> 'StandAloneContext':
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingsDeletionRequest.getContext`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingsDeletionRequest`
        
            Returns:
                The value of the :code:`context` attribute
        
        
        """
        ...
    def getParameters(self) -> com.google.common.collect.ImmutableSet[Parameter]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`context`, :code:`parameters`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`SettingsDeletionRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withContext(self, standAloneContext: 'StandAloneContext') -> 'DefaultSettingsDeletionRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.SettingsDeletionRequest.getContext` attribute. A shallow reference equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.StandAloneContext`): A new value for context
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameters(self, parameterArray: typing.List[Parameter]) -> 'DefaultSettingsDeletionRequest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.settings.SettingsDeletionRequest.getParameters`.
        
            Parameters:
                elements (:class:`~cern.lsa.domain.settings.Parameter`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.domain.settings.DefaultSettingsDeletionRequest` withParameters (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.settings.Parameter`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.settings.SettingsDeletionRequest.getParameters`. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.settings.Parameter`> elements): An iterable of parameters elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameters(self, iterable: java.lang.Iterable[Parameter]) -> 'DefaultSettingsDeletionRequest': ...
    class Builder:
        def addAllParameters(self, iterable: java.lang.Iterable[Parameter]) -> 'DefaultSettingsDeletionRequest.Builder': ...
        def addParameter(self, parameter: Parameter) -> 'DefaultSettingsDeletionRequest.Builder': ...
        def addParameters(self, parameterArray: typing.List[Parameter]) -> 'DefaultSettingsDeletionRequest.Builder': ...
        def build(self) -> 'DefaultSettingsDeletionRequest': ...
        def context(self, standAloneContext: 'StandAloneContext') -> 'DefaultSettingsDeletionRequest.Builder': ...
        def parameters(self, iterable: java.lang.Iterable[Parameter]) -> 'DefaultSettingsDeletionRequest.Builder': ...

class DrivableContext(Context):
    """
    public interface DrivableContext extends :class:`~cern.lsa.domain.settings.Context`
    
        This interface is implemented by contexts which can be driven to the hardware. It extends base context with certain
        information which is necessary during drive operation.
    """
    def getUser(self) -> str:
        """
            Returns name of accelerator user associated with this context.
        
            Returns:
                accelerator user mapped to this context or :code:`null` if there is no user mapped
        
        
        """
        ...

class IncorporationRequest(TrimRequest):
    """
    public interface IncorporationRequest extends :class:`~cern.lsa.domain.settings.TrimRequest`
    
        Represents a request to incorporate settings from given source beam process to a beam process specified in
        :class:`~cern.lsa.domain.settings.TrimRequest`.
    
        Instances of this interface should be created using
        :class:`~cern.lsa.domain.settings.factory.IncorporationRequestBuilder`.
    """
    @staticmethod
    def builder() -> cern.lsa.domain.settings.factory.IncorporationRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.IncorporationRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getIncorporationSettings(self) -> java.util.Set[IncorporationSetting]: ...
    def shouldIncorporate(self, parameter: Parameter) -> bool:
        """
            Since in one incorporation request it is possible to mix parameter settings to trim and parameter settings to
            incorporate this method checks whether for specified parameter the setting should be incorporated.
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): 
            Returns:
                :code:`true` if for specified parameter the settings should be incorporated, :code:`false` if the settings should be
                trimmed
        
        
        """
        ...

class Knob(Parameter):
    """
    public interface Knob extends :class:`~cern.lsa.domain.settings.Parameter`
    
        Knob parameter. A knob is a high-level (LSA implementation) parameter that is defined for one or several optics and has
        one or several dependent parameters aka components.
    
        For each pair of optic and component knob has a :code:`value` associated, aka multiplication factors. The new values of
        the components for each optic are calculated using the delta of the knob parameter and the corresponding multiplication
        factors.
    """
    def getComponentNames(self) -> java.util.Set[str]: ...
    def getKnobFactors(self) -> KnobFactors:
        """
        
            Returns:
                all the multiplication factors
        
        
        """
        ...
    def getOpticNames(self) -> java.util.Set[str]: ...

class RevertTrimRequest(TrimRequest):
    """
    public interface RevertTrimRequest extends :class:`~cern.lsa.domain.settings.TrimRequest`
    
        Represents a request to revert settings of specified beam processes and parameters to the time determined by
        :code:`TrimHeader`.
    
        Instances of this interface should be created using :class:`~cern.lsa.domain.settings.factory.RevertTrimRequestBuilder`.
    """
    @staticmethod
    def builder() -> cern.lsa.domain.settings.factory.RevertTrimRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.RevertTrimRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getBeamProcesses(self) -> java.util.Set['BeamProcess']: ...
    def getTrimHeader(self) -> TrimHeader:
        """
            Trim to be reverted determining moment in time - see :meth:`~cern.lsa.domain.settings.TrimHeader.getCreatedDate`
        
        """
        ...

class SettingsGenerationRequest(TrimRequest):
    """
    public interface SettingsGenerationRequest extends :class:`~cern.lsa.domain.settings.TrimRequest`
    
        Represents a request to generate settings of certain parameters.
    
        This interface describes all the characteristics of the trim that should be performed like :code:`StandAloneContext`,
        parameters etc. It extends the trim request, since generation will internally perform a trim after generation has been
        performed.
    
        Instances of this interface should be created using
        :class:`~cern.lsa.domain.settings.factory.SettingsGenerationRequestBuilder`.
    """
    @staticmethod
    def builder() -> cern.lsa.domain.settings.factory.SettingsGenerationRequestBuilder:
        """
            Creates builder to build :class:`~cern.lsa.domain.settings.SettingsGenerationRequest`
        
            Returns:
                the builder
        
        
        """
        ...
    def getSubContexts(self) -> java.util.Set['SubContext']: ...
    def isGenerateZeroSettings(self) -> bool:
        """
            Determines whether generation shall generate zero settings for the given parameters.
        
            The value of the ZERO setting depends on the parameter's value type and is generated using
            :meth:`~cern.lsa.domain.settings.SettingFactory.newInitialSetting` method. See JavaDoc of this method to find out what
            value is generated for each value type.
        
            Returns:
                :code:`true` to generate ZERO settings, :code:`false` to use the default generation procedure
        
        
        """
        ...

class SettingsRestoreStatus(FailedParametersStatus):
    """
    public interface SettingsRestoreStatus extends :class:`~cern.lsa.domain.settings.FailedParametersStatus`
    
        Represents the status of a settings restore operation.
    """
    def getSettings(self) -> CompositeContextSettings:
        """
            Returns settings that were restored.
        
            Returns:
                settings that were restored
        
        
        """
        ...

class StandAloneContext(Context, cern.lsa.domain.commons.AttributeAware):
    """
    public interface StandAloneContext extends :class:`~cern.lsa.domain.settings.Context`, :class:`~cern.lsa.domain.commons.AttributeAware`
    
        Represents a stand-alone context i.e. a context that does not belong to any other parent context and exists by its own.
    """
    def getBeamProcesses(self) -> java.util.List['BeamProcess']: ...
    def getContextCategory(self) -> ContextCategory:
        """
            Returns the context category that this context belongs to.
        
            Returns:
                the context category that this context belongs to
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def isResident(self) -> bool:
        """
            Returns :code:`true` if this context is **resident**. A :code:`StandAloneContext` is resident if all
            :code:`DrivableContext`s that are part of it, have an accelerator user assigned. The
            :class:`~cern.lsa.domain.settings.StandAloneCycle` and :class:`~cern.lsa.domain.settings.StandAloneBeamProcess` are
            directly implementing :class:`~cern.lsa.domain.settings.DrivableContext` so there might be at most one accelerator user
            assigned to them.
        
            Marking a :code:`StandAloneContext` as resident means that settings associated with the context can be written and read
            from the hardware, however it doesn't mean that the hardware actually uses these settings. A multiplexed device has
            several memory "slots" labeled with the timing user, where settings can be stored. Whenever settings of a resident
            context are sent to the hardware - they are stored in a corresponding "slot". However what timing users are currently
            played and what settings (from what slots) are actually used depends on how the timing system has been programmed.
        
            Returns:
                :code:`true` if this context is **resident**, :code:`false` otherwise
        
        
        """
        ...

class SubContext(Context):
    """
    public interface SubContext extends :class:`~cern.lsa.domain.settings.Context`
    
        Represents a sub context of another (parent) context. Example of a sub context are cycle and beam process.
    """
    def getStartTime(self) -> int:
        """
            Returns the start time of this context in its parent context. The unit of the time is the same as the unit of context
            length returned by :meth:`~cern.lsa.domain.settings.Context.getLength` method.
        
            Returns:
                the start time of this context
        
        
        """
        ...

class BeamProcess(SubContext):
    """
    public interface BeamProcess extends :class:`~cern.lsa.domain.settings.SubContext`
    
        Defines a generic beam process. A beam process defines a specific process (injection, extraction) in the cycle for a
        given domain (Main Ring, Transfer Line, etc.).
    
        Beam process is the "smallest" context and it is a building block for cycles.
    
        Every parameter value is assigned to a beam process, defining a setting.
    
        Also see:
            :class:`~cern.lsa.domain.settings.Setting`
    """
    def getCategory(self) -> cern.lsa.domain.settings.type.BeamProcessTypeCategory:
        """
            Returns the category of this beam process.
        
            Returns:
                the category of this beam process
        
        
        """
        ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
            Returns the name of the particle transfer that this beam process has been created for.
        
            Returns:
                the name of the particle transfer this beam process belongs to
        
        
        """
        ...
    def getPurpose(self) -> cern.lsa.domain.settings.type.BeamProcessPurpose:
        """
            Returns the purpose of this beam process.
        
            Returns:
                the purpose of this beam process
        
        
        """
        ...

class BeamProductionChain(SubContext):
    """
    public interface BeamProductionChain extends :class:`~cern.lsa.domain.settings.SubContext`
    
        A :code:`BeamProductionChain` is a sequence of :code:`BeamProcess` or another nested :code:`BeamProductionChain`.
    
        It usually describes the production of a specific particle from the source to the target even across different
        accelerators. The nesting is used to repeat specific processes. Like defining a booster :code:`BeamProductionChain` and
        using it several times or in several places.
    """
    def getBeamProcesses(self) -> java.util.List['DrivableBeamProcess']: ...

class Cycle(SubContext, DrivableContext):
    """
    public interface Cycle extends :class:`~cern.lsa.domain.settings.SubContext`, :class:`~cern.lsa.domain.settings.DrivableContext`
    
        A cycle defines the lifespan of the beam (from injection to extraction) and beam out. A cycle holds the characteristics
        of the beam and represents a window of time that is related to the timing system.
    """
    ...

class Pattern(StandAloneContext):
    """
    public interface Pattern extends :class:`~cern.lsa.domain.settings.StandAloneContext`
    
        A relative scheduling of :code:`BeamProductionChain` and :code:`BeamProcess`. Basically several BeamProductionChains can
        be placed in an order and are connected by Beam-Out BeamProcesses.
    """
    def getDrivableBeamProcesses(self) -> java.util.List['DrivableBeamProcess']: ...

class DrivableBeamProcess(BeamProcess, DrivableContext):
    """
    public interface DrivableBeamProcess extends :class:`~cern.lsa.domain.settings.BeamProcess`, :class:`~cern.lsa.domain.settings.DrivableContext`
    
        Defines a generic BeamProcess. A beam process defines a specific process (injection, extraction) in the cycle for a
        given domain (Main Ring, Transfer Lines).
    
        In addition to the :code:`BeamProcess` the :code:`DrivableBeamProcess` also implements the :code:`DrivableContext`
        interface and provides information for driving to the hardware.
    """
    ...

class StandAloneCycle(StandAloneContext, Cycle):
    """
    public interface StandAloneCycle extends :class:`~cern.lsa.domain.settings.StandAloneContext`, :class:`~cern.lsa.domain.settings.Cycle`
    
        A cycle defines the lifespan of the beam (from injection to extraction) and beam out. A cycle holds the characteristics
        of the beam and represents a window of time that is related to the timing system.
    """
    def getIntersections(self) -> CycleIntersections:
        """
        
            Returns:
                intersections
        
        
        """
        ...

class StandAloneBeamProcess(StandAloneContext, DrivableBeamProcess):
    """
    public interface StandAloneBeamProcess extends :class:`~cern.lsa.domain.settings.StandAloneContext`, :class:`~cern.lsa.domain.settings.DrivableBeamProcess`
    
        Defines a generic BeamProcess. A beam process defines a specific process (injection, extraction) in the cycle for a
        given domain (Main Ring, Transfer Lines).
    """
    def getActualBeamProcessInfo(self) -> ActualBeamProcessInfo:
        """
            If the given BeamProcess is actual, this information contains all actual information like source point and a reference
            to the source BP
        
            Returns:
                actual information or null, if the BP is not actual
        
        
        """
        ...
    def isActual(self) -> bool:
        """
            Marks, if a specific BeamProcess is actual
        
            Returns:
                true, if it is an actual BeamProcess
        
        
        """
        ...

class DefaultStandAloneBeamProcessesRequest(cern.lsa.domain.settings.StandAloneBeamProcessesRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultStandAloneBeamProcessesRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.StandAloneBeamProcessesRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.StandAloneBeamProcessesRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultStandAloneBeamProcessesRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultStandAloneBeamProcessesRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.DefaultStandAloneBeamProcessesRequest`.
        
            .. code-block: java
            
             DefaultStandAloneBeamProcessesRequest.builder()
                .ids(Set<Long> | null) // nullable ids
                .accelerator(cern.accsoft.commons.domain.Accelerator | null) // nullable :code:`accelerator`
                .resident(Boolean | null) // nullable :code:`resident`
                .multiplexed(Boolean | null) // nullable :code:`multiplexed`
                .beamProcessNames(Set<String> | null) // nullable :meth:`~cern.lsa.domain.settings.StandAloneBeamProcessesRequest.getBeamProcessNames`
                .build();
             
        
            Returns:
                A new DefaultStandAloneBeamProcessesRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(standAloneBeamProcessesRequest: 'StandAloneBeamProcessesRequest') -> 'DefaultStandAloneBeamProcessesRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.StandAloneBeamProcessesRequest` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.StandAloneBeamProcessesRequest`): The instance to copy
        
            Returns:
                A copied immutable StandAloneBeamProcessesRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getBeamProcessNames(self) -> com.google.common.collect.ImmutableSet[str]: ...
    def getIds(self) -> com.google.common.collect.ImmutableSet[int]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`ids`, :code:`accelerator`, :code:`resident`, :code:`multiplexed`,
            :code:`beamProcessNames`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isMultiplexed(self) -> bool: ...
    def isResident(self) -> bool: ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`StandAloneBeamProcessesRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DefaultStandAloneBeamProcessesRequest': ...
    @typing.overload
    def withBeamProcessNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultStandAloneBeamProcessesRequest': ...
    @typing.overload
    def withBeamProcessNames(self, stringArray: typing.List[str]) -> 'DefaultStandAloneBeamProcessesRequest': ...
    @typing.overload
    def withIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultStandAloneBeamProcessesRequest': ...
    @typing.overload
    def withIds(self, longArray: typing.List[int]) -> 'DefaultStandAloneBeamProcessesRequest': ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultStandAloneBeamProcessesRequest': ...
    def withResident(self, boolean: bool) -> 'DefaultStandAloneBeamProcessesRequest': ...
    class Builder:
        def accelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...
        def addAllBeamProcessNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...
        def addAllIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...
        def addBeamProcessName(self, string: str) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...
        def addBeamProcessNames(self, stringArray: typing.List[str]) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...
        def addId(self, long: int) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...
        def addIds(self, longArray: typing.List[int]) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...
        def beamProcessNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...
        def build(self) -> 'DefaultStandAloneBeamProcessesRequest': ...
        def ids(self, iterable: java.lang.Iterable[int]) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...
        def resident(self, boolean: bool) -> 'DefaultStandAloneBeamProcessesRequest.Builder': ...

class DefaultStandAloneContextsRequest(cern.lsa.domain.settings.StandAloneContextsRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultStandAloneContextsRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.StandAloneContextsRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.StandAloneContextsRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultStandAloneContextsRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultStandAloneContextsRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.DefaultStandAloneContextsRequest`.
        
            .. code-block: java
            
             DefaultStandAloneContextsRequest.builder()
                .ids(Set<Long> | null) // nullable ids
                .accelerator(cern.accsoft.commons.domain.Accelerator | null) // nullable :code:`accelerator`
                .resident(Boolean | null) // nullable :code:`resident`
                .multiplexed(Boolean | null) // nullable :code:`multiplexed`
                .contextNames(Set<String> | null) // nullable :meth:`~cern.lsa.domain.settings.StandAloneContextsRequest.getContextNames`
                .build();
             
        
            Returns:
                A new DefaultStandAloneContextsRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(standAloneContextsRequest: 'StandAloneContextsRequest') -> 'DefaultStandAloneContextsRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.StandAloneContextsRequest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.StandAloneContextsRequest`): The instance to copy
        
            Returns:
                A copied immutable StandAloneContextsRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getContextNames(self) -> com.google.common.collect.ImmutableSet[str]: ...
    def getIds(self) -> com.google.common.collect.ImmutableSet[int]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`ids`, :code:`accelerator`, :code:`resident`, :code:`multiplexed`,
            :code:`contextNames`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isMultiplexed(self) -> bool: ...
    def isResident(self) -> bool: ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`StandAloneContextsRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DefaultStandAloneContextsRequest': ...
    @typing.overload
    def withContextNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultStandAloneContextsRequest': ...
    @typing.overload
    def withContextNames(self, stringArray: typing.List[str]) -> 'DefaultStandAloneContextsRequest': ...
    @typing.overload
    def withIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultStandAloneContextsRequest': ...
    @typing.overload
    def withIds(self, longArray: typing.List[int]) -> 'DefaultStandAloneContextsRequest': ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultStandAloneContextsRequest': ...
    def withResident(self, boolean: bool) -> 'DefaultStandAloneContextsRequest': ...
    class Builder:
        def accelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DefaultStandAloneContextsRequest.Builder': ...
        def addAllContextNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultStandAloneContextsRequest.Builder': ...
        def addAllIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultStandAloneContextsRequest.Builder': ...
        def addContextName(self, string: str) -> 'DefaultStandAloneContextsRequest.Builder': ...
        def addContextNames(self, stringArray: typing.List[str]) -> 'DefaultStandAloneContextsRequest.Builder': ...
        def addId(self, long: int) -> 'DefaultStandAloneContextsRequest.Builder': ...
        def addIds(self, longArray: typing.List[int]) -> 'DefaultStandAloneContextsRequest.Builder': ...
        def build(self) -> 'DefaultStandAloneContextsRequest': ...
        def contextNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultStandAloneContextsRequest.Builder': ...
        def ids(self, iterable: java.lang.Iterable[int]) -> 'DefaultStandAloneContextsRequest.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultStandAloneContextsRequest.Builder': ...
        def resident(self, boolean: bool) -> 'DefaultStandAloneContextsRequest.Builder': ...

class DefaultStandAloneCyclesRequest(cern.lsa.domain.settings.StandAloneCyclesRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultStandAloneCyclesRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.StandAloneCyclesRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.StandAloneCyclesRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultStandAloneCyclesRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultStandAloneCyclesRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.DefaultStandAloneCyclesRequest`.
        
            .. code-block: java
            
             DefaultStandAloneCyclesRequest.builder()
                .ids(Set<Long> | null) // nullable ids
                .accelerator(cern.accsoft.commons.domain.Accelerator | null) // nullable :code:`accelerator`
                .resident(Boolean | null) // nullable :code:`resident`
                .multiplexed(Boolean | null) // nullable :code:`multiplexed`
                .cycleNames(Set<String> | null) // nullable :meth:`~cern.lsa.domain.settings.StandAloneCyclesRequest.getCycleNames`
                .build();
             
        
            Returns:
                A new DefaultStandAloneCyclesRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(standAloneCyclesRequest: 'StandAloneCyclesRequest') -> 'DefaultStandAloneCyclesRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.StandAloneCyclesRequest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.StandAloneCyclesRequest`): The instance to copy
        
            Returns:
                A copied immutable StandAloneCyclesRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getCycleNames(self) -> com.google.common.collect.ImmutableSet[str]: ...
    def getIds(self) -> com.google.common.collect.ImmutableSet[int]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`ids`, :code:`accelerator`, :code:`resident`, :code:`multiplexed`,
            :code:`cycleNames`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isMultiplexed(self) -> bool: ...
    def isResident(self) -> bool: ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`StandAloneCyclesRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DefaultStandAloneCyclesRequest': ...
    @typing.overload
    def withCycleNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultStandAloneCyclesRequest': ...
    @typing.overload
    def withCycleNames(self, stringArray: typing.List[str]) -> 'DefaultStandAloneCyclesRequest': ...
    @typing.overload
    def withIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultStandAloneCyclesRequest': ...
    @typing.overload
    def withIds(self, longArray: typing.List[int]) -> 'DefaultStandAloneCyclesRequest': ...
    def withMultiplexed(self, boolean: bool) -> 'DefaultStandAloneCyclesRequest': ...
    def withResident(self, boolean: bool) -> 'DefaultStandAloneCyclesRequest': ...
    class Builder:
        def accelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> 'DefaultStandAloneCyclesRequest.Builder': ...
        def addAllCycleNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultStandAloneCyclesRequest.Builder': ...
        def addAllIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultStandAloneCyclesRequest.Builder': ...
        def addCycleName(self, string: str) -> 'DefaultStandAloneCyclesRequest.Builder': ...
        def addCycleNames(self, stringArray: typing.List[str]) -> 'DefaultStandAloneCyclesRequest.Builder': ...
        def addId(self, long: int) -> 'DefaultStandAloneCyclesRequest.Builder': ...
        def addIds(self, longArray: typing.List[int]) -> 'DefaultStandAloneCyclesRequest.Builder': ...
        def build(self) -> 'DefaultStandAloneCyclesRequest': ...
        def cycleNames(self, iterable: java.lang.Iterable[str]) -> 'DefaultStandAloneCyclesRequest.Builder': ...
        def ids(self, iterable: java.lang.Iterable[int]) -> 'DefaultStandAloneCyclesRequest.Builder': ...
        def multiplexed(self, boolean: bool) -> 'DefaultStandAloneCyclesRequest.Builder': ...
        def resident(self, boolean: bool) -> 'DefaultStandAloneCyclesRequest.Builder': ...

class StandAloneBeamProcessesRequest(cern.lsa.domain.settings.BaseStandAloneContextsRequest):
    """
    @Immutable public interface StandAloneBeamProcessesRequest
    
        Describes criteria when searching for LSA stand alone beam process contexts. This object should be created using
        :code:`StandAloneBeamProcessesRequestBuilder` or factory methods present in this interface and passed to appropriate
        finder methods.
    """
    @staticmethod
    def builder() -> DefaultStandAloneBeamProcessesRequest.Builder:
        """
            Create a builder for a request object to search for all :class:`~cern.lsa.domain.settings.StandAloneBeamProcess`
            matching provided criterion
        
            Returns:
                a builder for :class:`~cern.lsa.domain.settings.StandAloneBeamProcessesRequest`
        
        
        """
        ...
    @staticmethod
    def byAccelerator(accelerator: cern.accsoft.commons.domain.Accelerator) -> 'StandAloneBeamProcessesRequest':
        """
            Create a request object to search for all :class:`~cern.lsa.domain.settings.StandAloneBeamProcess` belonging to the
            provided :code:`Accelerator`
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): the accelerator for which we want to retrieve :class:`~cern.lsa.domain.settings.StandAloneBeamProcess`s
        
            Returns:
                :class:`~cern.lsa.domain.settings.StandAloneBeamProcessesRequest` to find by accelerator
        
        
        """
        ...
    @staticmethod
    def byBeamProcessName(string: str) -> 'StandAloneBeamProcessesRequest':
        """
            Create a request object to search for all :class:`~cern.lsa.domain.settings.StandAloneBeamProcess` with name provided.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the context
        
            Returns:
                :class:`~cern.lsa.domain.settings.StandAloneBeamProcessesRequest` to find by name
        
        
        """
        ...
    def getBeamProcessNames(self) -> java.util.Set[str]: ...

class StandAloneContextsRequest(cern.lsa.domain.settings.BaseStandAloneContextsRequest):
    """
    @Immutable public interface StandAloneContextsRequest
    
        Describes criteria when searching for LSA stand alone beam process or cycles contexts. This object should be created
        using :code:`cern.lsa.domain.settings.StandAloneContextsRequestBuilder` or factory methods present in this interface and
        passed to appropriate finder methods.
    """
    @staticmethod
    def builder() -> DefaultStandAloneContextsRequest.Builder:
        """
            Create a builder for a request object to search for all :class:`~cern.lsa.domain.settings.StandAloneContext` matching
            provided criterion
        
            Returns:
                a builder for :class:`~cern.lsa.domain.settings.StandAloneContextsRequest`
        
        
        """
        ...
    @staticmethod
    def byAccelerator(accelerator: cern.accsoft.commons.domain.Accelerator) -> 'StandAloneContextsRequest':
        """
            Create a request object to search for all :class:`~cern.lsa.domain.settings.StandAloneContextsRequest` belonging to the
            provided :code:`Accelerator`
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): the accelerator for which we want to retrieve :class:`~cern.lsa.domain.settings.StandAloneContext`s
        
            Returns:
                :class:`~cern.lsa.domain.settings.StandAloneContextsRequest` to find by accelerator
        
        
        """
        ...
    @staticmethod
    def byContextName(string: str) -> 'StandAloneContextsRequest':
        """
            Create a request object to search for all :class:`~cern.lsa.domain.settings.StandAloneContext` with name provided.
        
            Parameters:
                contextName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the context
        
            Returns:
                :class:`~cern.lsa.domain.settings.StandAloneContextsRequest` to find by name
        
        
        """
        ...
    def getContextNames(self) -> java.util.Set[str]: ...

class StandAloneCyclesRequest(cern.lsa.domain.settings.BaseStandAloneContextsRequest):
    """
    @Immutable public interface StandAloneCyclesRequest
    
        Describes criteria when searching for LSA stand alone beam process contexts. This object should be created using
        :code:`StandAloneBeamCyclesRequestBuilder` or factory methods present in this interface and passed to appropriate finder
        methods.
    """
    @staticmethod
    def builder() -> DefaultStandAloneCyclesRequest.Builder:
        """
            Create a builder for a request object to search for all :class:`~cern.lsa.domain.settings.StandAloneCycle` matching
            provided criterion
        
            Returns:
                a builder for :class:`~cern.lsa.domain.settings.StandAloneCyclesRequest`
        
        
        """
        ...
    @staticmethod
    def byAccelerator(accelerator: cern.accsoft.commons.domain.Accelerator) -> 'StandAloneCyclesRequest':
        """
            Create a request object to search for all :class:`~cern.lsa.domain.settings.StandAloneCycle` belonging to the provided
            :code:`Accelerator`
        
            Parameters:
                accelerator (cern.accsoft.commons.domain.Accelerator): the accelerator for which we want to retrieve :class:`~cern.lsa.domain.settings.StandAloneCycle`s
        
            Returns:
                :class:`~cern.lsa.domain.settings.StandAloneCyclesRequest` to find by accelerator
        
        
        """
        ...
    @staticmethod
    def byCycleName(string: str) -> 'StandAloneCyclesRequest':
        """
            Create a request object to search for all :class:`~cern.lsa.domain.settings.StandAloneCycle` with name provided.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the context
        
            Returns:
                :class:`~cern.lsa.domain.settings.StandAloneCyclesRequest` to find by name
        
        
        """
        ...
    def getCycleNames(self) -> java.util.Set[str]: ...

class BaseStandAloneContextsRequest: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings")``.

    AcceleratorUser: typing.Type[AcceleratorUser]
    AcceleratorUserGroup: typing.Type[AcceleratorUserGroup]
    AcceleratorUsersRequest: typing.Type[AcceleratorUsersRequest]
    ActualBeamProcessInfo: typing.Type[ActualBeamProcessInfo]
    Archive: typing.Type[Archive]
    ArchiveVersion: typing.Type[ArchiveVersion]
    BaseStandAloneContextsRequest: typing.Type[BaseStandAloneContextsRequest]
    BeamProcess: typing.Type[BeamProcess]
    BeamProcessIncorporationRequest: typing.Type[BeamProcessIncorporationRequest]
    BeamProcessIntersection: typing.Type[BeamProcessIntersection]
    BeamProductionChain: typing.Type[BeamProductionChain]
    CompositeContextSettings: typing.Type[CompositeContextSettings]
    Context: typing.Type[Context]
    ContextCategory: typing.Type[ContextCategory]
    ContextFamily: typing.Type[ContextFamily]
    ContextIntersections: typing.Type[ContextIntersections]
    ContextOptics: typing.Type[ContextOptics]
    ContextSettings: typing.Type[ContextSettings]
    ContextSettingsRequest: typing.Type[ContextSettingsRequest]
    ContextSettingsRequestBuilder: typing.Type[ContextSettingsRequestBuilder]
    ContextTypeFilter: typing.Type[ContextTypeFilter]
    ContextTypes: typing.Type[ContextTypes]
    Contexts: typing.Type[Contexts]
    CopySettingsRequest: typing.Type[CopySettingsRequest]
    CriticalParameterException: typing.Type[CriticalParameterException]
    Cycle: typing.Type[Cycle]
    CycleBeamProcessIntersection: typing.Type[CycleBeamProcessIntersection]
    CycleIntersections: typing.Type[CycleIntersections]
    DefaultAcceleratorUser: typing.Type[DefaultAcceleratorUser]
    DefaultAcceleratorUserGroup: typing.Type[DefaultAcceleratorUserGroup]
    DefaultAcceleratorUsersRequest: typing.Type[DefaultAcceleratorUsersRequest]
    DefaultHyperCycleMapping: typing.Type[DefaultHyperCycleMapping]
    DefaultSettingsDeletionRequest: typing.Type[DefaultSettingsDeletionRequest]
    DefaultStandAloneBeamProcessesRequest: typing.Type[DefaultStandAloneBeamProcessesRequest]
    DefaultStandAloneContextsRequest: typing.Type[DefaultStandAloneContextsRequest]
    DefaultStandAloneCyclesRequest: typing.Type[DefaultStandAloneCyclesRequest]
    DevicePropertyParameters: typing.Type[DevicePropertyParameters]
    DrivableBeamProcess: typing.Type[DrivableBeamProcess]
    DrivableContext: typing.Type[DrivableContext]
    ErrorsAwareContextSettings: typing.Type[ErrorsAwareContextSettings]
    FailedParametersStatus: typing.Type[FailedParametersStatus]
    GenerationException: typing.Type[GenerationException]
    HyperCycle: typing.Type[HyperCycle]
    HyperCycleMapping: typing.Type[HyperCycleMapping]
    IncorporationRanges: typing.Type[IncorporationRanges]
    IncorporationRequest: typing.Type[IncorporationRequest]
    IncorporationSetting: typing.Type[IncorporationSetting]
    Intersections: typing.Type[Intersections]
    Knob: typing.Type[Knob]
    KnobFactor: typing.Type[KnobFactor]
    KnobFactors: typing.Type[KnobFactors]
    LinkRuleAttribute: typing.Type[LinkRuleAttribute]
    MisconfiguredParameterException: typing.Type[MisconfiguredParameterException]
    NotIncorporatedParameters: typing.Type[NotIncorporatedParameters]
    Parameter: typing.Type[Parameter]
    ParameterAttributes: typing.Type[ParameterAttributes]
    ParameterForEditing: typing.Type[ParameterForEditing]
    ParameterGroup: typing.Type[ParameterGroup]
    ParameterNotFoundException: typing.Type[ParameterNotFoundException]
    ParameterSettings: typing.Type[ParameterSettings]
    ParameterTreeNode: typing.Type[ParameterTreeNode]
    ParameterTreesRequest: typing.Type[ParameterTreesRequest]
    ParameterType: typing.Type[ParameterType]
    ParameterTypeCategory: typing.Type[ParameterTypeCategory]
    ParameterTypeGroup: typing.Type[ParameterTypeGroup]
    ParameterTypes: typing.Type[ParameterTypes]
    ParameterTypesRequest: typing.Type[ParameterTypesRequest]
    Parameters: typing.Type[Parameters]
    ParametersRequest: typing.Type[ParametersRequest]
    Pattern: typing.Type[Pattern]
    PropertyAccessMode: typing.Type[PropertyAccessMode]
    RevertTrimRequest: typing.Type[RevertTrimRequest]
    Setting: typing.Type[Setting]
    SettingComparisonParameterResult: typing.Type[SettingComparisonParameterResult]
    SettingComparisonRequest: typing.Type[SettingComparisonRequest]
    SettingComparisonResponse: typing.Type[SettingComparisonResponse]
    SettingComparisonResult: typing.Type[SettingComparisonResult]
    SettingComparisonResultType: typing.Type[SettingComparisonResultType]
    SettingFactory: typing.Type[SettingFactory]
    SettingPartEnum: typing.Type[SettingPartEnum]
    Settings: typing.Type[Settings]
    SettingsDeletionRequest: typing.Type[SettingsDeletionRequest]
    SettingsGenerationRequest: typing.Type[SettingsGenerationRequest]
    SettingsRestoreStatus: typing.Type[SettingsRestoreStatus]
    SettingsSource: typing.Type[SettingsSource]
    StandAloneBeamProcess: typing.Type[StandAloneBeamProcess]
    StandAloneBeamProcessesRequest: typing.Type[StandAloneBeamProcessesRequest]
    StandAloneContext: typing.Type[StandAloneContext]
    StandAloneContextCloneRequest: typing.Type[StandAloneContextCloneRequest]
    StandAloneContextCreationRequest: typing.Type[StandAloneContextCreationRequest]
    StandAloneContextFilter: typing.Type[StandAloneContextFilter]
    StandAloneContextsRequest: typing.Type[StandAloneContextsRequest]
    StandAloneCycle: typing.Type[StandAloneCycle]
    StandAloneCyclesRequest: typing.Type[StandAloneCyclesRequest]
    SubContext: typing.Type[SubContext]
    TrimException: typing.Type[TrimException]
    TrimHeader: typing.Type[TrimHeader]
    TrimHeadersRequest: typing.Type[TrimHeadersRequest]
    TrimHeadersRequestBuilder: typing.Type[TrimHeadersRequestBuilder]
    TrimRequest: typing.Type[TrimRequest]
    TrimResponse: typing.Type[TrimResponse]
    TrimResult: typing.Type[TrimResult]
    UserContextMapping: typing.Type[UserContextMapping]
    factory: cern.lsa.domain.settings.factory.__module_protocol__
    parameter: cern.lsa.domain.settings.parameter.__module_protocol__
    spi: cern.lsa.domain.settings.spi.__module_protocol__
    type: cern.lsa.domain.settings.type.__module_protocol__
