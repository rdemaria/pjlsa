import cern
import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.util
import cern.accsoft.commons.util.value
import cern.accsoft.commons.value
import cern.lsa.domain.commons
import cern.lsa.domain.commons.spi
import cern.lsa.domain.devices
import cern.lsa.domain.devices.type
import cern.lsa.domain.exploitation
import cern.lsa.domain.settings
import cern.lsa.domain.settings.spi.test
import cern.lsa.domain.settings.spi.type
import cern.lsa.domain.settings.spi.util
import cern.lsa.domain.settings.type
import java.io
import java.lang
import java.time
import java.util
import typing



class AbstractSetting(cern.lsa.domain.commons.spi.AbstractIdentifiedEntity[cern.lsa.domain.settings.Setting], cern.lsa.domain.settings.Setting, java.lang.Cloneable):
    """
    public abstract class AbstractSetting extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity`<:class:`~cern.lsa.domain.settings.Setting`> implements :class:`~cern.lsa.domain.settings.Setting`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        An abstract implementation of the :class:`~cern.lsa.domain.settings.Setting` interface containing common properties and
        methods.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def checkReadSettingPart(settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> None:
        """
            Checks if the specified setting part can be used to read setting.
        
            Parameters:
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): 
            Raises:
                : if the specified setting part is not one of: :meth:`~cern.lsa.domain.settings.SettingPartEnum.CORRECTION`,
                    :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET`, :meth:`~cern.lsa.domain.settings.SettingPartEnum.VALUE`.
        
        
        """
        ...
    def clone(self) -> 'AbstractSetting':
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.clone`
            Returns a deep copy of this Setting.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.clone` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Overrides:
                 in class 
        
            Returns:
                a deep copy of this Setting
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Description copied from class: :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.equals`
            Returns :code:`true` if the given object is of the same class and has the same ID.
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.equals`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity`
        
            Also see:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.getId`
        
        
        """
        ...
    def getArray2DValue(self) -> cern.accsoft.commons.value.ImmutableScalarArray2D:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getArray2DValue`
            Returns the value of this setting as an array2d. In case of an array2d there is no consideration of target and
            correction. An array2d setting can only have one value.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getArray2DValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the value of this setting as an array2d.
        
        
        """
        ...
    def getArrayValue(self) -> cern.accsoft.commons.value.ImmutableScalarArray:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getArrayValue`
            Returns the value of this setting as an array. In case of an array there is no consideration of target and correction.
            An array setting can only have one value.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getArrayValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the value of this setting as an array.
        
        
        """
        ...
    def getBeamProcess(self) -> cern.lsa.domain.settings.BeamProcess:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getBeamProcess`
            Returns the beam process this setting is defined for
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getBeamProcess` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the beam process this setting is defined for
        
        
        """
        ...
    def getCorrectionFunctionValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCorrectionFunctionValue`
            Returns the correction value of this setting as a Function
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionFunctionValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the correction part of this setting as a function
        
        
        """
        ...
    def getCorrectionFunctionsArrayValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCorrectionFunctionsArrayValue`
            Returns the correction value of this setting as functionsArray
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionFunctionsArrayValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the correction part of this setting as functionsArray
        
        
        """
        ...
    def getCorrectionScalarValue(self) -> cern.accsoft.commons.value.ImmutableScalar:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCorrectionScalarValue`
            Returns the correction value of this setting as a scalar
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionScalarValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the correction part of this setting as a scalar
        
        
        """
        ...
    def getCorrectionValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue`
            Returns the correction value of this setting. If the setting holds no correction value (correction is not defined) the
            value returned depends on its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCreationDate`
            Returns the non null date this setting have been created.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCreationDate` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the non null date this setting have been created
        
        
        """
        ...
    def getFunctionValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getFunctionValue`
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two value is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned is an empty discrete function.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getFunctionValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def getFunctionsArrayValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getFunctionsArrayValue`
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two values is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned is an empty discrete functions array.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getFunctionsArrayValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getParameter`
            Returns the parameter this contextual value is for
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getParameter` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the parameter this contextual value is for
        
        
        """
        ...
    def getScalarValue(self) -> cern.accsoft.commons.value.ImmutableScalar:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getScalarValue`
            Returns the value of this setting as an scalar. The value is made of the sum of target value and the correction value.
            If one of the two value is not defined only the value defined will be used. If the setting holds no value (both target
            and correction are not defined) the value returned is Double.NaN.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getScalarValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def getTargetFunctionValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getTargetFunctionValue`
            Returns the target value of this setting as a Function
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getTargetFunctionValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the target part of this setting as a function
        
        
        """
        ...
    def getTargetFunctionsArrayValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getTargetFunctionsArrayValue`
            Returns the target value of this setting as functionsArray
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getTargetFunctionsArrayValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the target part of this setting as functionsArray
        
        
        """
        ...
    def getTargetScalarValue(self) -> cern.accsoft.commons.value.ImmutableScalar:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getTargetScalarValue`
            Returns the target value of this setting as a scalar
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getTargetScalarValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the target part of this setting as a scalar
        
        
        """
        ...
    def getTargetValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getTargetValue`
            Returns the target value of this setting. If the setting holds no target value (target is not defined) the value
            returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getTargetValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getTrimId(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getTrimId`
            Returns the trim id this setting is for
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getTrimId` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the trim id this setting is for
        
        
        """
        ...
    def getValueType(self) -> cern.accsoft.commons.value.Type:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getValueType`
            Returns the type of the value holds by this setting.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getValueType` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the type of the value holds by this setting.
        
            Also see:
                :code:`Type`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Description copied from class: :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.hashCode`
            Redefines equals in term of the name
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.hashCode`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity`
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#hashCode()>`
        
        
        """
        ...
    def setBeamProcess(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> None:
        """
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): The beamProcessName to set.
        
        
        """
        ...
    def setCreationDate(self, date: java.util.Date) -> None:
        """
        
            Parameters:
                creationDate (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): The retirementDate to set.
        
        
        """
        ...
    def setParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> None:
        """
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): The parameterName to set.
        
        
        """
        ...
    def setTrimId(self, long: int) -> None:
        """
        
            Parameters:
                trimId (long): The trimId to set.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def updateValue(self, immutableValue: cern.accsoft.commons.value.ImmutableValue, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.updateValue`
            Updates the target or the correction value of this setting depending of the given setting part. If the given part is
            VALUE, the correction value will be updated by substracting the target value to the given value. The target part will
            remain untouched unless the given value is null or the target part itself is null. If the given value is null and the
            part is VALUE, both, the target and the correction will be set to null. If the given part is CORRECTION, the correction
            value will be updated directly with the given value not affecting the target If the given part is TARGET, the target
            value will be updated directly with the given value not affecting the correction.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.updateValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Parameters:
                value (cern.accsoft.commons.value.ImmutableValue): the possibly null new value of the given part
                part (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the part of the setting to update
        
        """
        ...
    @typing.overload
    def updateValue(self, setting: cern.lsa.domain.settings.Setting) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.updateValue`
            Updates the target and the correction value of this setting with the processed value of the target and the correction of
            the given setting. This only overwrites actual values, no additional processing is performed. If the given setting is
            null nothing will be updated.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.updateValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Parameters:
                sourceSetting (:class:`~cern.lsa.domain.settings.Setting`): the source setting from which the values of the target and the correction will be copied to this setting
        
        
        """
        ...

class ActualBeamProcessInfoImpl(cern.lsa.domain.settings.ActualBeamProcessInfo, java.io.Serializable):
    """
    public class ActualBeamProcessInfoImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.ActualBeamProcessInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of :class:`~cern.lsa.domain.settings.ActualBeamProcessInfo` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, beamProcess: cern.lsa.domain.settings.BeamProcess, int: int): ...
    def getSourceBeamProcess(self) -> cern.lsa.domain.settings.BeamProcess:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ActualBeamProcessInfo.getSourceBeamProcess`
            Returns the source beam process from which this actual beam process was created.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ActualBeamProcessInfo.getSourceBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ActualBeamProcessInfo`
        
            Returns:
                the source beamProcess this actual one was created from
        
        
        """
        ...
    def getSourcePoint(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ActualBeamProcessInfo.getSourcePoint`
            Returns the point in time from which this actual beam process was created.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ActualBeamProcessInfo.getSourcePoint`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ActualBeamProcessInfo`
        
            Returns:
                the point in time from which this actual beam process was created
        
        
        """
        ...
    def setSourceBeamProcess(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> None:
        """
            Sets :code:`sourceBeamProcess` property.
        
            Parameters:
                sourceBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the :code:`sourceBeamProcess` to set
        
        
        """
        ...

class ArchiveImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.settings.Archive], cern.lsa.domain.settings.Archive):
    """
    public class ArchiveImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.settings.Archive`> implements :class:`~cern.lsa.domain.settings.Archive`
    
        Default implementation of the :code:`Archive` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, long: int, string: str, standAloneContext: cern.lsa.domain.settings.StandAloneContext): ...
    def addArchiveVersion(self, archiveVersion: cern.lsa.domain.settings.ArchiveVersion) -> None:
        """
            Adds an archive version to this archive. **This method should be only used by DAO layer when Archive object is loaded
            from the database.**
        
            Parameters:
                archiveVersion (:class:`~cern.lsa.domain.settings.ArchiveVersion`): archive version to be added
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.equals`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def getLatestVersion(self) -> cern.lsa.domain.settings.ArchiveVersion:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Archive.getLatestVersion`
            Returns the latest version of this archive i.e. archive version with the highest version number.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Archive.getLatestVersion` in interface :class:`~cern.lsa.domain.settings.Archive`
        
            Returns:
                the latest archive version
        
        
        """
        ...
    def getStandAloneContext(self) -> cern.lsa.domain.settings.StandAloneContext:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Archive.getStandAloneContext`
            Returns the stand-alone context that the archive is created for.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Archive.getStandAloneContext` in interface :class:`~cern.lsa.domain.settings.Archive`
        
            Returns:
                the stand-alone context that the archive is created for
        
        
        """
        ...
    def getVersion(self, double: float) -> cern.lsa.domain.settings.ArchiveVersion:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Archive.getVersion`
            Returns :code:`ArchiveVersion` with specified version number. If this archive doesn't contain specified version - the
            method returns :code:`null`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Archive.getVersion` in interface :class:`~cern.lsa.domain.settings.Archive`
        
            Parameters:
                version (double): requested archive version e.g. 1.2
        
            Returns:
                archive version or :code:`null`
        
        
        """
        ...
    def getVersions(self) -> java.util.SortedSet[cern.lsa.domain.settings.ArchiveVersion]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.hashCode`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.settings.Archive`
        
        
        """
        ...

class ArchiveVersionImpl(cern.lsa.domain.settings.ArchiveVersion, java.io.Serializable):
    """
    public class ArchiveVersionImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.ArchiveVersion`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :code:`ArchiveVersion` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, archive: cern.lsa.domain.settings.Archive, double: float, date: java.util.Date, string: str, int: int): ...
    def compareTo(self, archiveVersion: cern.lsa.domain.settings.ArchiveVersion) -> int:
        """
            Compares this archive version to the specified one using version number.
        
            Specified by:
                 in interface 
        
            Raises:
                : if the specified archive version does not belong to the same archive
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ArchiveVersionImpl.getVersion`,
                :meth:`~cern.lsa.domain.settings.spi.ArchiveVersionImpl.getArchive`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getArchive(self) -> cern.lsa.domain.settings.Archive:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ArchiveVersion.getArchive`
            Returns archive that this version belongs to.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ArchiveVersion.getArchive`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ArchiveVersion`
        
            Returns:
                archive that this version belongs to
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ArchiveVersion.getCreationDate`
            Returns the creation date of the archive version.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ArchiveVersion.getCreationDate`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ArchiveVersion`
        
            Returns:
                the creation date of the archive version
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ArchiveVersion.getDescription`
            Returns the description of the archive version.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ArchiveVersion.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ArchiveVersion`
        
            Returns:
                the description of the archive version
        
        
        """
        ...
    def getSettingCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ArchiveVersion.getSettingCount`
            Returns count of created settings.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ArchiveVersion.getSettingCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ArchiveVersion`
        
            Returns:
                count of created settings
        
        
        """
        ...
    def getVersion(self) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ArchiveVersion.getVersion`
            Returns the version of the archive.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ArchiveVersion.getVersion`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ArchiveVersion`
        
            Returns:
                the version of the archive.
        
        
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

class BeamProcessIncorporationRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.settings.BeamProcessIncorporationRequest):
    """
    public class BeamProcessIncorporationRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
    
        Incorporation request describing the incorporation from a point in a beam process.
    
        Also see:
            :meth:`~serialized`
    """
    SOURCE_BEAM_PROCESS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SOURCE_BEAM_PROCESS
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.BeamProcessIncorporationRequestImpl.getSourceBeamProcess`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SETTINGS_SOURCE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SETTINGS_SOURCE
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.BeamProcessIncorporationRequestImpl.getSettingsSource`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEST_BEAM_PROCESS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEST_BEAM_PROCESS
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.BeamProcessIncorporationRequestImpl.getDestBeamProcess`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SOURCE_POINT_IN_TIME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SOURCE_POINT_IN_TIME
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.BeamProcessIncorporationRequestImpl.getSourcePointInTime`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEST_POINT_IN_TIME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEST_POINT_IN_TIME
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.BeamProcessIncorporationRequestImpl.getDestPointInTime`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SHOULD_INCORPORATE_ALL_PARAMETERS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SHOULD_INCORPORATE_ALL_PARAMETERS
    
        Attribute name for
        :meth:`~cern.lsa.domain.settings.spi.BeamProcessIncorporationRequestImpl.shouldIncorporateAllParameters` specifying if
        the settings for all the parameter should be incorporated.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARAMETERS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETERS
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.BeamProcessIncorporationRequestImpl.getParameters`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SETTING_PART: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SETTING_PART
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.BeamProcessIncorporationRequestImpl.getSettingPart`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DRIVE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DRIVE
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.BeamProcessIncorporationRequestImpl.shouldDrive` indicating that
        the incorporated settings should be driven to HW.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DESCRIPTION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DESCRIPTION
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.BeamProcessIncorporationRequestImpl.getDescription`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
        
            Returns:
                description of the trim (comment).
        
        
        """
        ...
    def getDestBeamProcess(self) -> cern.lsa.domain.settings.BeamProcess:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getDestBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
        
            Returns:
                beam process to incorporate into
        
        
        """
        ...
    def getDestPointInTime(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getDestPointInTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
        
            Returns:
                the point in time of destination beam process to incorporate into
        
        
        """
        ...
    def getParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getSettingPart(self) -> cern.lsa.domain.settings.SettingPartEnum:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getSettingPart`
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
        
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getSettingPart`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
        
            Returns:
                the setting part which should be used for the incorporation
        
        
        """
        ...
    def getSettingsSource(self) -> cern.lsa.domain.settings.SettingsSource:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getSettingsSource`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
        
            Returns:
                the settings source used to retrieve settings from the source beam process
        
        
        """
        ...
    def getSourceBeamProcess(self) -> cern.lsa.domain.settings.BeamProcess:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getSourceBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
        
            Returns:
                beam process to incorporate from
        
        
        """
        ...
    def getSourcePointInTime(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getSourcePointInTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
        
            Returns:
                the point in time of source beam process to incorporate from. If the source beam process is an
                :meth:`~cern.lsa.domain.settings.StandAloneBeamProcess.isActual` then the source point-in-time is ignored
        
        
        """
        ...
    def shouldDrive(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.shouldDrive`
            Determines whether the incorporated settings should be driven to the hardware.
        
            Note that the new settings will be driven if the stand-alone context of the
            :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getDestBeamProcess` is
            :meth:`~cern.lsa.domain.settings.StandAloneContext.isResident`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.shouldDrive`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
        
            Returns:
                :code:`true` if drive should be performed
        
        
        """
        ...
    def shouldIncorporateAllParameters(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.shouldIncorporateAllParameters`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest`
        
            Returns:
                :code:`true` if settings for all parameters should be incorporated, otherwise parameters are taken from
                :meth:`~cern.lsa.domain.settings.BeamProcessIncorporationRequest.getParameters`.
        
        
        """
        ...

class CompositeContextSettingsImpl(cern.lsa.domain.settings.CompositeContextSettings, java.io.Serializable):
    """
    public class CompositeContextSettingsImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.CompositeContextSettings`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :code:`CompositeContextSettings` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, contextSettings: cern.lsa.domain.settings.ContextSettings, contextSettings2: cern.lsa.domain.settings.ContextSettings): ...
    def getContextSettings(self) -> cern.lsa.domain.settings.ContextSettings:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.CompositeContextSettings.getContextSettings`
            Returns parameter settings for multiplexed parameters stored in this object. If this :code:`CompositeContextSettings`
            doesn't contain any multiplexed settings, this method returns an empty :code:`ContextSettings` object i.e. without any
            settings.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CompositeContextSettings.getContextSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CompositeContextSettings`
        
            Returns:
                parameter settings for multiplexed parameters stored in this object
        
        
        """
        ...
    def getNonMultiplexedSettings(self) -> cern.lsa.domain.settings.ContextSettings:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.CompositeContextSettings.getNonMultiplexedSettings`
            Returns parameter settings for non-multiplexed parameters stored in this object. If this
            :code:`CompositeContextSettings` doesn't contain any non-multiplexed settings, this method returns an empty
            :code:`ContextSettings` object i.e. without any settings.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CompositeContextSettings.getNonMultiplexedSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CompositeContextSettings`
        
            Returns:
                parameter settings for non-multiplexed parameters stored in this object
        
        
        """
        ...
    def getParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getValue(self, drivableContext: cern.lsa.domain.settings.DrivableContext, string: str) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.CompositeContextSettings.getValue`
            Returns immutable value of specified parameter and drivable context. If there is no setting for specified parameter and
            context - the method returns :code:`null`.
        
            Note that non-multiplexed parameters have to be accessed using the non-multiplexed context.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CompositeContextSettings.getValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CompositeContextSettings`
        
            Parameters:
                drivableContext (:class:`~cern.lsa.domain.settings.DrivableContext`): drivable context for which value should be returned
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the parameter for which value should be returned
        
            Returns:
                immutable value of specified parameter and context or :code:`null`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_ContextBase__C = typing.TypeVar('_ContextBase__C', bound=cern.accsoft.commons.util.Named)  # <C>
class ContextBase(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[_ContextBase__C], typing.Generic[_ContextBase__C]):
    """
    public abstract class ContextBase<C extends cern.accsoft.commons.util.Named & :class:`~cern.lsa.domain.commons.IdentifiedEntity`> extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<C>
    
        A base class to be extended by all context and context type implementations. A holder for common attributes.
    
        This class should NOT be used directly (as variable type) by any code. It is only meant for inheritance.
    
        The class doesn't define :code:`equals(..)` or :code:`hashCode()` methods since every context is uniquely identified by
        its ID and name, so implementations of these two methods in the :code:`AbstractIdentifiedNamedEntity` class are valid.
    
        Also see:
            :meth:`~serialized`
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                accelerator the context belongs to
        
        
        """
        ...
    def getContextCategory(self) -> cern.lsa.domain.settings.ContextCategory:
        """
        
            Returns:
                the name of context category
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
        
            Returns:
                date when the context was created or :code:`null` if date was not provided
        
        
        """
        ...
    def getCreatorName(self) -> str:
        """
        
            Returns:
                NICE name of the context creator
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Returns:
                description of the context
        
        
        """
        ...
    def getLength(self) -> int:
        """
        
            Returns:
                length of the context
        
        
        """
        ...
    def getModificationDate(self) -> java.util.Date:
        """
        
            Returns:
                date when the context was created or :code:`null` if date was not provided
        
        
        """
        ...
    def getModifierName(self) -> str:
        """
        
            Returns:
                NICE name of the context modifier
        
        
        """
        ...
    def setAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ContextBase.getAccelerator`
        
        
        """
        ...
    def setContextCategory(self, contextCategory: cern.lsa.domain.settings.ContextCategory) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ContextBase.getContextCategory`
        
        
        """
        ...
    def setCreationDate(self, date: java.util.Date) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ContextBase.getCreationDate`
        
        
        """
        ...
    def setCreatorName(self, string: str) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ContextBase.getCreatorName`
        
        
        """
        ...
    def setDescription(self, string: str) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ContextBase.getDescription`
        
        
        """
        ...
    @typing.overload
    def setLength(self, int: int) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ContextBase.getLength`
        
        
        """
        ...
    @typing.overload
    def setLength(self, string: str) -> None: ...
    def setModificationDate(self, date: java.util.Date) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ContextBase.getCreationDate`
        
        
        """
        ...
    def setModifierName(self, string: str) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ContextBase.getModifierName`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.settings.spi.ContextBase`
        
        
        """
        ...

class ContextSettingsImpl(cern.lsa.domain.settings.ContextSettings, java.io.Serializable):
    """
    public class ContextSettingsImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.ContextSettings`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.ContextSettings` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, contextSettings: cern.lsa.domain.settings.ContextSettings): ...
    @typing.overload
    def __init__(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext): ...
    @typing.overload
    def __init__(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext, map: typing.Union[java.util.Map[str, 'ParameterSettingsImpl'], typing.Mapping[str, 'ParameterSettingsImpl']]): ...
    def addAll(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.addAll`
            Adds to this object all the :class:`~cern.lsa.domain.settings.ParameterSettings` contained in the specified
            :code:`ContextSettings` that are not yet present in this :code:`ContextSettings`. In other words if this container
            contains :code:`ParameterSettings` for a given parameter - it won't be added from specified :code:`ContextSettings`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.addAll`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                ctxSettings (:class:`~cern.lsa.domain.settings.ContextSettings`): settings to be added to this container
        
        
        """
        ...
    def addCurrentSetting(self, setting: cern.lsa.domain.settings.Setting) -> None: ...
    def addParameterSettings(self, parameterSettings: cern.lsa.domain.settings.ParameterSettings) -> None:
        """
            Adds new :class:`~cern.lsa.domain.settings.ParameterSettings` instance to the current
            :class:`~cern.lsa.domain.settings.ContextSettings` object.
        
            Parameters:
                parameterSettings (:class:`~cern.lsa.domain.settings.ParameterSettings`): settings which are about to be added to the current object
        
        
        """
        ...
    def addUpdatedSetting(self, setting: cern.lsa.domain.settings.Setting) -> None: ...
    def getContext(self) -> cern.lsa.domain.settings.StandAloneContext:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.getContext`
            Returns the context these settings are for.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.getContext`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Returns:
                the context these settings are for
        
        
        """
        ...
    def getCurrentBeamProcesses(self) -> java.util.Set[cern.lsa.domain.settings.BeamProcess]: ...
    @typing.overload
    def getCurrentSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter) -> cern.lsa.domain.settings.Setting:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.getCurrentSetting`
            Returns the current setting for the given beam process and parameter. The setting returned is always the current one,
            whether an updated value has been given or not.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.getCurrentSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to return the setting for
        
            Returns:
                the current setting for the given beam process and parameter or null if the given beam process has no setting for the
                parameter
        
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.getCurrentSetting`
            Returns the current setting for the given beam process and parameter. The setting returned is always the current one,
            whether an updated value has been given or not.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.getCurrentSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to return the setting for
        
            Returns:
                the current setting for the given beam process and parameter or null if the given beam process has no setting for the
                parameter
        
        
        """
        ...
    @typing.overload
    def getCurrentSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess, string: str) -> cern.lsa.domain.settings.Setting: ...
    def getCurrentSettings(self) -> java.util.Set[cern.lsa.domain.settings.Setting]: ...
    def getParameterSettingMap(self) -> java.util.Map[str, 'ParameterSettingsImpl']: ...
    @typing.overload
    def getParameterSettings(self, parameter: cern.lsa.domain.settings.Parameter) -> cern.lsa.domain.settings.ParameterSettings:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.getParameterSettings`
            Returns the parameter settings for the given parameter or null if none has been registered.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.getParameterSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to return the setting for
        
            Returns:
                the parameter setting for the given parameter name or null
        
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.getParameterSettings`
            Returns the parameter settings for the given parameter or null if none has been registered.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.getParameterSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to return the setting for
        
            Returns:
                the parameter setting for the given parameter or null if none has been found
        
        
        """
        ...
    @typing.overload
    def getParameterSettings(self, string: str) -> cern.lsa.domain.settings.ParameterSettings: ...
    def getParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    @typing.overload
    def getSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter) -> cern.lsa.domain.settings.Setting:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.getSetting`
            Returns either the current setting or the updated setting if one exist for the given beam process and parameter. The
            setting returned is always the updated one if it exist and the current one if no updated setting has been given for the
            given beam process.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.getSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to return the setting for
        
            Returns:
                the current or the updated setting for the given beam process and parameter.
        
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.getSetting`
            Returns either the current setting or the updated setting if one exist for the given beam process and parameter. The
            setting returned is always the updated one if it exist and the current one if no updated setting has been given for the
            given beam process.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.getSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to return the setting for
        
            Returns:
                the current or the updated setting for the given beam process and parameter
        
        
        """
        ...
    @typing.overload
    def getSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess, string: str) -> cern.lsa.domain.settings.Setting: ...
    def getSettings(self) -> java.util.Set[cern.lsa.domain.settings.Setting]: ...
    def getUpdatedBeamProcesses(self) -> java.util.Set[cern.lsa.domain.settings.BeamProcess]: ...
    def getUpdatedParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    @typing.overload
    def getUpdatedSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter) -> cern.lsa.domain.settings.Setting:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.getUpdatedSetting`
            Returns the updated setting for the given beam process and parameter. The setting returned is always the updated one, or
            null if no update has been set.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.getUpdatedSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to return the setting for
        
            Returns:
                the updated setting for the given beam process and parameter or null if the given beam process has not been updated for
                the given parameter
        
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.getUpdatedSetting`
            Returns the updated setting for the given beam process and parameter. The setting returned is always the updated one, or
            null if no update has been set.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.getUpdatedSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to return the setting for
        
            Returns:
                the updated setting for the given beam process and parameter or null if the given beam process has not been updated for
                the given parameter
        
        
        """
        ...
    @typing.overload
    def getUpdatedSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess, string: str) -> cern.lsa.domain.settings.Setting: ...
    def getUpdatedSettings(self) -> java.util.Set[cern.lsa.domain.settings.Setting]: ...
    def isEmpty(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.isEmpty`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Returns:
                :code:`true` if :meth:`~cern.lsa.domain.settings.ContextSettings.size` is zero
        
        
        """
        ...
    @typing.overload
    def isUpdated(self, beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.isUpdated`
            Returns :code:`true` if the setting for the given beam process and parameter has been updated, :code:`false` otherwise.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.isUpdated`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to check for update
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to check for update
        
            Returns:
                :code:`true` if the setting for the given beam process and parameter has been updated, :code:`false` otherwise.
        
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.isUpdated`
            Returns :code:`true` if the setting for the given beam process and parameter has been updated, :code:`false` otherwise.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.isUpdated`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to check for update
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to check for update
        
            Returns:
                :code:`true` if the setting for the given beam process and parameter has been updated, :code:`false` otherwise.
        
        
        """
        ...
    @typing.overload
    def isUpdated(self, beamProcess: cern.lsa.domain.settings.BeamProcess, string: str) -> bool: ...
    @typing.overload
    def isUpdated(self, parameter: cern.lsa.domain.settings.Parameter) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.isUpdated`
            Returns :code:`true` if the setting for the given parameter has been updated, :code:`false` otherwise.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.isUpdated`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to check for update
        
            Returns:
                :code:`true` if the setting for the given parameter has been updated, :code:`false` otherwise.
        
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.isUpdated`
            Returns :code:`true` if the setting for the given parameter has been updated, :code:`false` otherwise.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.isUpdated`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
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
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.round`
            Round all the settings that are part of this :code:`ContextSettings` object.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.round` in interface :class:`~cern.lsa.domain.settings.ContextSettings`
        
        
        """
        ...
    def size(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.size` in interface :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Returns:
                the number of parameter settings in this collection.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def updateSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, immutableValue: cern.accsoft.commons.value.ImmutableValue, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.updateSetting`
            Updates the setting belonging to the given beam process for the given parameter with the given value. This method lookup
            the setting for the given beam process and the parameter. If no setting is associated to the beam process and parameter
            an exception is thrown. If a setting is found, then the updated setting is checked. If there is an existing updated
            setting, it is updated using the given value. If none exist, a new updated setting is created using the current one and
            it is updated with the given value. If the given value is null an updated setting will be created that is an exact copy
            of the current one.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.updateSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process whose setting is to be updated
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to check for update
                updatedValue (cern.accsoft.commons.value.ImmutableValue): the possibly null value to use for the update
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the part of the setting to update
        
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ContextSettings.updateSetting`
            Updates the setting belonging to the given beam process for the given parameter with the given value. This method lookup
            the setting for the given beam process and the parameter. If no setting is associated to the beam process and parameter
            an exception is thrown. If a setting is found, then the updated setting is checked. If there is an existing updated
            setting, it is updated using the given value. If none exist, a new updated setting is created using the current one and
            it is updated with the given value. If the given value is null an updated setting will be created that is an exact copy
            of the current one.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ContextSettings.updateSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ContextSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process whose setting is to be updated
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter to check for update
                updatedValue (cern.accsoft.commons.value.ImmutableValue): the possibly null value to use for the update
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the part of the setting to update
        
        
        """
        ...
    @typing.overload
    def updateSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess, string: str, immutableValue: cern.accsoft.commons.value.ImmutableValue, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> None: ...

class CycleBeamProcessIntersectionImpl(cern.lsa.domain.settings.CycleBeamProcessIntersection, java.io.Serializable):
    """
    public class CycleBeamProcessIntersectionImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.CycleBeamProcessIntersection`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
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
    def getBeamProcess(self) -> cern.lsa.domain.settings.BeamProcess:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CycleBeamProcessIntersection.getBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CycleBeamProcessIntersection`
        
            Returns:
                Returns the beamProcess.
        
        
        """
        ...
    def getCycle(self) -> cern.lsa.domain.settings.Cycle:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CycleBeamProcessIntersection.getCycle`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CycleBeamProcessIntersection`
        
            Returns:
                Returns the cycle.
        
        
        """
        ...
    def getEndInBeamProcess(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CycleBeamProcessIntersection.getEndInBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CycleBeamProcessIntersection`
        
            Returns:
                Returns the intersectionEndInBeamProcess.
        
        
        """
        ...
    def getEndInCycle(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CycleBeamProcessIntersection.getEndInCycle`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CycleBeamProcessIntersection`
        
            Returns:
                Returns the intersectionEndInCycle.
        
        
        """
        ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CycleBeamProcessIntersection.getParticleTransfer`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CycleBeamProcessIntersection`
        
            Returns:
                Returns the particleTransfer.
        
        
        """
        ...
    def getStartInBeamProcess(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CycleBeamProcessIntersection.getStartInBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CycleBeamProcessIntersection`
        
            Returns:
                Returns the intersectionStartInBeamProcess.
        
        
        """
        ...
    def getStartInCycle(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CycleBeamProcessIntersection.getStartInCycle`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CycleBeamProcessIntersection`
        
            Returns:
                Returns the intersectionStartInCycle.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def setBeamProcess(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> None:
        """
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): The beamProcess to set.
        
        
        """
        ...
    def setCycle(self, cycle: cern.lsa.domain.settings.Cycle) -> None:
        """
        
            Parameters:
                cycle (:class:`~cern.lsa.domain.settings.Cycle`): The :class:`~cern.lsa.domain.settings.Cycle` to set.
        
        
        """
        ...
    def setIntersectionEndInBeamProcess(self, int: int) -> None:
        """
        
            Parameters:
                intersectionEndInBeamProcess (int): The intersectionEndInBeamProcess to set.
        
        
        """
        ...
    def setIntersectionEndInCycle(self, int: int) -> None:
        """
        
            Parameters:
                intersectionEndInCycle (int): The intersectionEndInCycle to set.
        
        
        """
        ...
    def setIntersectionStartInBeamProcess(self, int: int) -> None:
        """
        
            Parameters:
                intersectionStartInBeamProcess (int): The intersectionStartInBeamProcess to set.
        
        
        """
        ...
    def setIntersectionStartInCycle(self, int: int) -> None:
        """
        
            Parameters:
                intersectionStartInCycle (int): The intersectionStartInCycle to set.
        
        
        """
        ...
    def setParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> None:
        """
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): The particleTransfer to set.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class DevicePropertyParametersImpl(cern.lsa.domain.settings.DevicePropertyParameters, java.io.Serializable):
    """
    public class DevicePropertyParametersImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.DevicePropertyParameters`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.DevicePropertyParameters` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, set: java.util.Set[cern.lsa.domain.settings.Parameter]): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getDeviceName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.DevicePropertyParameters.getDeviceName`
            Return the device name for which all related parameters are collected.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.DevicePropertyParameters.getDeviceName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.DevicePropertyParameters`
        
            Returns:
                the device name for which all related parameters are collected
        
        
        """
        ...
    def getDevicePropertyName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.DevicePropertyParameters.getDevicePropertyName`
            Return the device name concatenated with property name for which all related parameters are collected.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.DevicePropertyParameters.getDevicePropertyName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.DevicePropertyParameters`
        
            Returns:
                the device name concatenated with property name for which all related parameters are collected
        
        
        """
        ...
    @typing.overload
    def getFieldNames(self) -> java.util.SortedSet[str]: ...
    @typing.overload
    def getFieldNames(self, boolean: bool) -> java.util.SortedSet[str]: ...
    @typing.overload
    def getParameters(self) -> java.util.SortedSet[cern.lsa.domain.settings.Parameter]: ...
    @typing.overload
    def getParameters(self, boolean: bool) -> java.util.SortedSet[cern.lsa.domain.settings.Parameter]: ...
    def getPropertyName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.DevicePropertyParameters.getPropertyName`
            Return the property name for which all related parameters are collected.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.DevicePropertyParameters.getPropertyName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.DevicePropertyParameters`
        
            Returns:
                the property name for which all related parameters are collected
        
        
        """
        ...
    def getSignature(self) -> cern.lsa.domain.settings.Parameter:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.DevicePropertyParameters.getSignature`
            Return the signature parameter for the given device and property, or :code:`null` value if does not exist.
        
            For parameter device/property#field1 one would get a parameter called: device/property#signature
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.DevicePropertyParameters.getSignature`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.DevicePropertyParameters`
        
            Returns:
                the signature parameter for the given device and property or :code:`null` if none exists
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isCritical(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.DevicePropertyParameters.isCritical`
            Return :code:`true` if all parameters related to the given device and property are critical, otherwise :code:`false`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.DevicePropertyParameters.isCritical`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.DevicePropertyParameters`
        
            Returns:
                :code:`true` if all parameters related to the given device and property are critical, otherwise :code:`false`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class FailedParametersStatusImpl(cern.lsa.domain.settings.FailedParametersStatus, java.io.Serializable):
    """
    public class FailedParametersStatusImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.FailedParametersStatus`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def addFailedParameters(self, context: cern.lsa.domain.settings.Context, map: typing.Union[java.util.Map[str, java.lang.Exception], typing.Mapping[str, java.lang.Exception]]) -> None: ...
    def containsFailedParameters(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.FailedParametersStatus.containsFailedParameters`
            Returns :code:`true` if the status contains at least one failed parameter, :code:`false` otherwise.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.FailedParametersStatus.containsFailedParameters`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.FailedParametersStatus`
        
            Returns:
                :code:`true` if the status contains at least one failed parameter, :code:`false` otherwise.
        
        
        """
        ...
    def getFailedContexts(self) -> java.util.Set[cern.lsa.domain.settings.Context]: ...
    def getFailedParameters(self, context: cern.lsa.domain.settings.Context) -> java.util.Map[str, java.lang.Exception]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class HyperCycleImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.settings.HyperCycle], cern.lsa.domain.settings.HyperCycle, java.lang.Cloneable):
    """
    public class HyperCycleImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.settings.HyperCycle`> implements :class:`~cern.lsa.domain.settings.HyperCycle`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Hypercycle represents a series of beamprocesses. It is necessary to provide information in which order the beamprocesses
        will be played.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...
    @typing.overload
    def add(self, acceleratorUser: cern.lsa.domain.settings.AcceleratorUser, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess) -> None:
        """
            Appends the given :code:`beamProcess` to the end of the hypercycle scheduling for the given :code:`userCategory`.
        
            Parameters:
                acceleratorUser (:class:`~cern.lsa.domain.settings.AcceleratorUser`): the user to map the beam process to
                beamProcess (:class:`~cern.lsa.domain.settings.StandAloneBeamProcess`): the beam process to append to the hypercycle scheduling.
        
            Adds the given :code:`beamProcess` into the given position in the hypercycle's schedule for the given
            :code:`userCategory`.
        
            Parameters:
                acceleratorUser (:class:`~cern.lsa.domain.settings.AcceleratorUser`): the user to map the beam process to
                beamProcess (:class:`~cern.lsa.domain.settings.StandAloneBeamProcess`): the beam process to append to the hypercycle scheduling.
                position (int): where to insert the beam process. If the position was already occupied, the schedule will be shifted as needed. First
                    position has value 1.
        
        
        """
        ...
    @typing.overload
    def add(self, acceleratorUser: cern.lsa.domain.settings.AcceleratorUser, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess, int: int) -> None: ...
    def clone(self) -> typing.Any: ...
    def contains(self, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess) -> bool:
        """
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.StandAloneBeamProcess`): the beam process
        
            Returns:
                true if the beam process is contained in this hyper cycle
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.equals`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def getBeamProcessByUser(self, string: str) -> cern.lsa.domain.settings.StandAloneBeamProcess:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.getBeamProcessByUser`
            Returns beam process which is mapped to the specified user.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.getBeamProcessByUser`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.HyperCycle`
        
            Parameters:
                userName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): LHC user name
        
            Returns:
                mapped beam process or :code:`null` if none beam process is mapped to the given user
        
        
        """
        ...
    def getBeamProcessPosition(self, string: str, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.getBeamProcessPosition`
            Returns, for the given user category, the scheduled position of given beamprocess within the current HyperCycle.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.getBeamProcessPosition`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.HyperCycle`
        
            Returns:
                the beamprocess scheduled position or -1 (if, for the given category, no beamprocess equals to the given one is
                scheduled).
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.getDescription`
            Returns the description of this hypercycle
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.getDescription` in interface :class:`~cern.lsa.domain.settings.HyperCycle`
        
            Returns:
                the description of this hypercycle
        
        
        """
        ...
    def getFirstBeamProcess(self, string: str) -> cern.lsa.domain.settings.StandAloneBeamProcess:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.getFirstBeamProcess`
            Returns the first beam process for the given category.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.getFirstBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.HyperCycle`
        
            Parameters:
                userCategory (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the category to consider
        
            Returns:
                the first beam process for :code:`userCategory` or :code:`null` if none or :code:`userCategory` does not exist.
        
        
        """
        ...
    def getLastBeamProcess(self, string: str) -> cern.lsa.domain.settings.StandAloneBeamProcess:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.getLastBeamProcess`
            Returns the last beam process for the given category
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.getLastBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.HyperCycle`
        
            Parameters:
                userCategory (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the category to consider
        
            Returns:
                the last beam process for :code:`userCategory` or :code:`null` if none or :code:`userCategory` does not exist.
        
        
        """
        ...
    def getNextBeamProcess(self, string: str) -> cern.lsa.domain.settings.StandAloneBeamProcess:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.getNextBeamProcess`
            Returns the beam process following another given one
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.getNextBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.HyperCycle`
        
            Parameters:
                beamProcessName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the beam process to consider as the current one
        
            Returns:
                the next beam process in relation to :code:`beamProcessName` or :code:`null` if none or :code:`beamProcessName` does not
                exist.
        
        
        """
        ...
    def getPreviousBeamProcess(self, string: str) -> cern.lsa.domain.settings.StandAloneBeamProcess:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.getPreviousBeamProcess`
            Returns the beam process preceding another given one
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.getPreviousBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.HyperCycle`
        
            Parameters:
                beamProcessName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the beam process to consider as the current one
        
            Returns:
                the previous beam process in relation to :code:`beamProcessName` or :code:`null` if none or :code:`beamProcessName` does
                not exist..
        
        
        """
        ...
    def getResidentBeamProcess(self, string: str) -> cern.lsa.domain.settings.StandAloneBeamProcess:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.getResidentBeamProcess`
            Returns the resident beam processes for the given category.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.getResidentBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.HyperCycle`
        
            Parameters:
                userCategory (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the category to consider
        
            Returns:
                the resident beam processes for :code:`userCategory` or :code:`null` if there is no resident beam process in specified
                category
        
        
        """
        ...
    def getResidentBeamProcesses(self) -> java.util.Set[cern.lsa.domain.settings.StandAloneBeamProcess]: ...
    @typing.overload
    def getScheduledBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.StandAloneBeamProcess]: ...
    @typing.overload
    def getScheduledBeamProcesses(self, string: str) -> java.util.List[cern.lsa.domain.settings.StandAloneBeamProcess]: ...
    def getUserCategories(self) -> java.util.SortedSet[str]: ...
    def getUserCategory(self, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.getUserCategory`
            Returns a category to which the given user belongs.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.getUserCategory` in interface :class:`~cern.lsa.domain.settings.HyperCycle`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.StandAloneBeamProcess`): considered beam process
        
            Returns:
                category name or :code:`null` if this beam process doesn't belong to this hyper cycle
        
        
        """
        ...
    def getUserForBeamProcess(self, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.getUserForBeamProcess`
            Returns the user to which the specified beam process is mapped to.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.getUserForBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.HyperCycle`
        
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
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.hashCode`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def isActive(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.HyperCycle.isActive`
            Indicates if this hyper cycle is active i.e. it is used in operation.
        
            At most one hyper cycle can be active at a time.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.HyperCycle.isActive` in interface :class:`~cern.lsa.domain.settings.HyperCycle`
        
            Returns:
                if this hyper-cycle is active.
        
        
        """
        ...
    def remove(self, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess) -> None:
        """
            Removes :code:`beamProcess` from the hypercycle scheduling. This beam process must **not** be active. This method
            removes the given beam process from all the users categories where it is found.
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.StandAloneBeamProcess`): the beam process to remove from the hypercycle scheduling.
        
        
        """
        ...
    def setActive(self, boolean: bool) -> None:
        """
            Marks this hypercycle as active.
        
            Parameters:
                active (boolean): the active to set
        
        
        """
        ...
    def setDescription(self, string: str) -> None: ...
    def swap(self, string: str, int: int, int2: int) -> None: ...

class KnobFactorsBuilder:
    """
    public class KnobFactorsBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder for :class:`~cern.lsa.domain.settings.KnobFactors`.
    
        It can be used for to create a new :class:`~cern.lsa.domain.settings.KnobFactors` from scratch or basing on an existing
        one.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, knobFactors: cern.lsa.domain.settings.KnobFactors): ...
    @typing.overload
    def addFactor(self, knobFactor: cern.lsa.domain.settings.KnobFactor) -> 'KnobFactorsBuilder':
        """
            Adds a knob factor.
        
            Parameters:
                knobFactor (:class:`~cern.lsa.domain.settings.KnobFactor`): factor for a component-optic pair
        
            Returns:
                this builder for chaining
        
            Raises:
                : if a factor is already defined for this component-optic pair
        
        
        """
        ...
    @typing.overload
    def addFactor(self, string: str, string2: str, double: float) -> 'KnobFactorsBuilder':
        """
            Adds a knob factor.
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): optic name of an optic
                factor (double): factor for this component-optic pair
        
            Returns:
                this builder for chaining
        
            Raises:
                : if a factor is already defined for this component-optic pair
        
        """
        ...
    @typing.overload
    def addOrUpdateFactor(self, knobFactor: cern.lsa.domain.settings.KnobFactor) -> 'KnobFactorsBuilder':
        """
            Adds or updates a knob factor.
        
            This methods adds a factor if it is not defined yet or updates an existing one.
        
            Parameters:
                knobFactor (:class:`~cern.lsa.domain.settings.KnobFactor`): factor for a component-optic pair
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    @typing.overload
    def addOrUpdateFactor(self, string: str, string2: str, double: float) -> 'KnobFactorsBuilder':
        """
            Adds or updates a knob factor.
        
            This methods adds a factor if it is not defined yet or updates an existing one.
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): optic name of an optic
                factor (double): factor for this component-optic pair
        
            Returns:
                this builder for chaining
        
        """
        ...
    def build(self) -> cern.lsa.domain.settings.KnobFactors:
        """
            Builds the :class:`~cern.lsa.domain.settings.KnobFactors`.
        
            Returns:
                new :class:`~cern.lsa.domain.settings.KnobFactors`
        
            Raises:
                : if there is no factor defined for some combination of knob component and optic
        
        
        """
        ...
    def clear(self) -> 'KnobFactorsBuilder':
        """
            Cleans all the factors.
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def removeFactor(self, string: str, string2: str) -> 'KnobFactorsBuilder':
        """
            Cleans a knob factor.
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): optic name of an optic
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    @typing.overload
    def updateFactor(self, knobFactor: cern.lsa.domain.settings.KnobFactor) -> 'KnobFactorsBuilder':
        """
            Updates a knob factor.
        
            Parameters:
                knobFactor (:class:`~cern.lsa.domain.settings.KnobFactor`): factor for a component-optic pair
        
            Returns:
                this builder for chaining
        
            Raises:
                : if a factor is not yet defined for this component-optic pair
        
        
        """
        ...
    @typing.overload
    def updateFactor(self, string: str, string2: str, double: float) -> 'KnobFactorsBuilder':
        """
            Updates a knob factor.
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): optic name of an optic
                factor (double): factor for this component-optic pair
        
            Returns:
                this builder for chaining
        
            Raises:
                : if a factor is not yet defined for this component-optic pair
        
        """
        ...

class KnobFactorsImpl(cern.lsa.domain.settings.KnobFactors, java.io.Serializable):
    """
    public class KnobFactorsImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.KnobFactors`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.KnobFactors`.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, set: java.util.Set[cern.lsa.domain.settings.KnobFactor]): ...
    @staticmethod
    def buildFactorsMap(set: java.util.Set[cern.lsa.domain.settings.KnobFactor]) -> java.util.Map[cern.accsoft.commons.util.value.Pair[str, str], cern.lsa.domain.settings.KnobFactor]: ...
    def containsFactor(self, string: str, string2: str) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.KnobFactors.containsFactor`
            Checks whether a multiplication factor is defined for the specified combination of the component and optic.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.KnobFactors.containsFactor`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.KnobFactors`
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of an optic
        
            Returns:
                :code:`true` if a multiplication factor is defined for the specified combination of the component and optic
        
        
        """
        ...
    @staticmethod
    def extractComponents(collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.KnobFactor], typing.Sequence[cern.lsa.domain.settings.KnobFactor]]) -> java.util.Set[str]: ...
    @staticmethod
    def extractOptics(collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.KnobFactor], typing.Sequence[cern.lsa.domain.settings.KnobFactor]]) -> java.util.Set[str]: ...
    def getComponentNames(self) -> java.util.Set[str]: ...
    def getFactor(self, string: str, string2: str) -> float:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.KnobFactors.getFactor`
            Returns the multiplication factor for the specified combination of the component and optic.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.KnobFactors.getFactor` in interface :class:`~cern.lsa.domain.settings.KnobFactors`
        
            Parameters:
                componentName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of a knob component
                opticName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of an optic
        
            Returns:
                multiplication factor for the specified combination of the component and optic
        
        
        """
        ...
    def getFactors(self) -> java.util.Set[cern.lsa.domain.settings.KnobFactor]: ...
    def getFactorsForComponent(self, string: str) -> java.util.Set[cern.lsa.domain.settings.KnobFactor]: ...
    def getFactorsForOptic(self, string: str) -> java.util.Set[cern.lsa.domain.settings.KnobFactor]: ...
    def getOpticNames(self) -> java.util.Set[str]: ...

class NotIncorporatedParametersImpl(cern.lsa.domain.settings.NotIncorporatedParameters, java.io.Serializable):
    """
    public class NotIncorporatedParametersImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.NotIncorporatedParameters`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, set: java.util.Set[str], set2: java.util.Set[str]): ...
    def getNonCountinueParameters(self) -> java.util.Set[str]: ...
    def getParametersWithSettingsOnlyInFirstContext(self) -> java.util.Set[str]: ...

class ParameterAttributesImpl(cern.lsa.domain.settings.ParameterAttributes):
    """
    public class ParameterAttributesImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.ParameterAttributes`
    
        Mutable object for creation or updating :class:`~cern.lsa.domain.settings.Parameter`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, parameterAttributes: cern.lsa.domain.settings.ParameterAttributes): ...
    @typing.overload
    def __init__(self, long: int, string: str, device: cern.lsa.domain.devices.Device, parameterType: cern.lsa.domain.settings.ParameterType, propertyField: cern.lsa.domain.devices.type.PropertyField, double: float, double2: float, integer: int, integer2: int, double3: float, double4: float, boolean: bool, string2: str, boolean2: bool, boolean3: bool): ...
    @typing.overload
    def __init__(self, string: str, device: cern.lsa.domain.devices.Device, parameterType: cern.lsa.domain.settings.ParameterType, propertyField: cern.lsa.domain.devices.type.PropertyField): ...
    @staticmethod
    def asNew(parameterAttributes: cern.lsa.domain.settings.ParameterAttributes) -> cern.lsa.domain.settings.ParameterAttributes: ...
    @staticmethod
    def baseFromParameter(parameter: cern.lsa.domain.settings.Parameter) -> cern.lsa.domain.settings.ParameterAttributes: ...
    def getAbsoluteTolerance(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getAbsoluteTolerance`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
            Returns:
                :code:`null` to delete attribute or absoluteTolerance to set on Parameter
        
        
        """
        ...
    def getDefaultHierarchy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getDefaultHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def getDevice(self) -> cern.lsa.domain.devices.Device:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getDevice`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def getMaxValue(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getMaxValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
            Returns:
                :code:`null` to delete attribute or maxValue which overrides default maxValue coming from
                :meth:`~cern.lsa.domain.devices.type.PropertyFieldVersion.getValueDescriptor`
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getMinValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
            Returns:
                :code:`null` to delete attribute or minValue which overrides default minValue coming from
                :meth:`~cern.lsa.domain.devices.type.PropertyFieldVersion.getValueDescriptor`
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def getParameterId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getParameterId`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
            Returns:
                parameter id
        
        
        """
        ...
    def getParameterName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getParameterName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def getParameterType(self) -> cern.lsa.domain.settings.ParameterType:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getParameterType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def getPropertyField(self) -> cern.lsa.domain.devices.type.PropertyField:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getPropertyField`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def getRelativeTolerance(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getRelativeTolerance`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
            Returns:
                :code:`null` to delete attribute or relativeTolerance to set on Parameter
        
        
        """
        ...
    def getXPrecision(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getXPrecision`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
            Returns:
                :code:`null` to delete attribute or xPrecision to set on Parameter
        
        
        """
        ...
    def getYPrecision(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.getYPrecision`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
            Returns:
                :code:`null` to delete attribute or yPrecision to set on Parameter
        
        
        """
        ...
    def isBelongsToFunctionBProc(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.isBelongsToFunctionBProc`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def isReservedForOpExperts(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.isReservedForOpExperts`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def isTrimable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.isTrimable`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setAbsoluteTolerance(self, double: float) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setAbsoluteTolerance`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setBelongsToFunctionBProc(self, boolean: bool) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setBelongsToFunctionBProc`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setDefaultHierarchy(self, string: str) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setDefaultHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setMaxValue(self, double: float) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setMaxValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setMinValue(self, double: float) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setMinValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setParameterId(self, long: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setParameterId`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setParameterName(self, string: str) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setParameterName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setRelativeTolerance(self, double: float) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setRelativeTolerance`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setReservedForOpExperts(self, boolean: bool) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setReservedForOpExperts`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setTrimable(self, boolean: bool) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setTrimable`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setXPrecision(self, integer: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setXPrecision`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def setYPrecision(self, integer: int) -> None:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterAttributes.setYPrecision`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterAttributes`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ParameterImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.settings.Parameter], cern.lsa.domain.settings.Parameter, java.lang.Cloneable):
    """
    public class ParameterImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.settings.Parameter`> implements :class:`~cern.lsa.domain.settings.Parameter`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Implementation of a Parameter that represents a property or a property field on a given device.
    
        Also see:
            :meth:`~serialized`
    """
    def belongsToFunctionBeamProcess(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.belongsToFunctionBeamProcess`
            Determines whether this parameter keeps value in a function beam process or in a discrete beam process - see
            :meth:`~cern.lsa.domain.settings.BeamProcess.getCategory`.
        
            This property is used by the Trim package to find out where given discrete parameter should store settings in case there
            are both function and discrete beam processes.
        
            Note that this flag is ignored for function parameters as they can keep settings only in function beam processes.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.belongsToFunctionBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                :code:`true` if this parameter keeps settings in a function beam process
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameter.getValueDescriptor`,
                :meth:`~cern.lsa.domain.settings.BeamProcess.getCategory`
        
        
        """
        ...
    def clone(self) -> 'ParameterImpl':
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.equals`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.getAccelerator` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                the accelerator to which this parameter belongs.
        
        
        """
        ...
    def getDefaultHierarchy(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.getDefaultHierarchy`
            Returns the default propagation hierarchy used by this parameter when translating its change to child parameters.
            Typically parameters have 'DEFAULT' as the default parameters hierarchy. In some cases, low level parameters have e.g.
            'UP' as the default hierarchy so that if they are trimmed - the change is propagated to high-level parameters.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.getDefaultHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                the default propagation hierarchy to be used
        
        
        """
        ...
    def getDevice(self) -> cern.lsa.domain.devices.Device:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.getDevice` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                the device this parameter belongs to.
        
        
        """
        ...
    def getParameterGroups(self) -> java.util.Set[str]: ...
    def getParameterType(self) -> cern.lsa.domain.settings.ParameterType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.getParameterType`
            Returns the type of this parameter.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.getParameterType` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                the type of this parameter.
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getPropertyField(self) -> cern.lsa.domain.devices.type.PropertyField:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.getPropertyField`
            Returns the property/field design info for this parameter
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.getPropertyField` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                the property/field design info
        
        
        """
        ...
    def getValueDescriptor(self) -> cern.accsoft.commons.value.ValueDescriptor:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.getValueDescriptor`
            Returns the value descriptor for this parameter. ValueDescriptor object holds information about:
        
              - maximal, minimal parameter values
              - precision
              - enumeration of possible values
              - unit - any of methods: getYUnit(), getXUnit() can be used, because they will all return exactly same value. There is
                only 1 unit
              - array dimensions iff this is array parameter
        
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.getValueDescriptor`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                ValueDescriptor object for this parameter
        
        
        """
        ...
    def getValueType(self) -> cern.accsoft.commons.value.Type:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.getValueType`
            Returns value type of this parameter such as INT, DOUBLE, FLOAT_ARRAY, etc.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.getValueType` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                the type of value the parameter can take.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Setting.getValueType`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Just name is taken into account.
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.hashCode`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def isCritical(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isCritical`
            Returns :code:`true` if this parameter is marked as critical. Critical parameters can be trimmed only by users who have
            a dedicated MCS RBAC role.
        
            The concept of critical parameters is part of the Machine Critical Settings infrastructure.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isCritical` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                :code:`true` if this parameter is marked as critical.
        
        
        """
        ...
    def isCycleBound(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isCycleBound`
            Returns :code:`true` if this parameter is a cycle-bound acquisition parameter. More details can be found in "Device
            Property behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isCycleBound` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                :code:`true` if this parameter is cycle-bound, :code:`false` otherwise.
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isCycleBound`, :meth:`~cern.lsa.domain.devices.Device.isCycleBound`
        
        
        """
        ...
    def isLsaImplementation(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isLsaImplementation`
            Return :code:`true`, if the parameter is implemented by LSA. This happens in the following scenarios: either the device
            server corresponds to LSA/InCA, either the corresponding property is added at the level of LSA and does not exists in
            the original class design.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isLsaImplementation`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                :code:`true`, if the parameter is implemented by LSA. :code:`false` otherwise.
        
        
        """
        ...
    def isMonitorable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isMonitorable`
            Indicates if this type can be monitored.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isMonitorable` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                :code:`true` if this type is monitorable, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isMonitorable`
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isMultiplexed`
            Returns :code:`true` if this parameter is a multiplexed setting parameter. More details can be found in "Device Property
            behaviour and contextual data" EDMS document:
            [https://edms.cern.ch/ui/#!master/navigator/document?D:100135354:100135354:subDocs]
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isMultiplexed` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                :code:`true` if this parameter is multiplexed, :code:`false` otherwise.
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isMultiplexed`,
                :meth:`~cern.lsa.domain.devices.Device.isMultiplexed`
        
        
        """
        ...
    def isPropertySupportingPartialSet(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isPropertySupportingPartialSet`
            Indicates if property associated with this parameter type supports partial set on the hardware i.e. if individual fields
            of this property can be set separately or all of them must be always set together.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isPropertySupportingPartialSet`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                :code:`true` if the property supports partial set, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isSupportingPartialSet`
        
        
        """
        ...
    def isReadable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isReadable`
            Indicates if this parameter is readable.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isReadable` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                :code:`true` if this parameter is readable, :code:`false` otherwise.
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isReadable`
        
        
        """
        ...
    def isReservedForOpExperts(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isReservedForOpExperts`
            Returns whether parameter is reserved for OP experts. In other words whether the parameter is representing a property of
            a device that is an expert property with restricted access.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isReservedForOpExperts`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                whether parameter is expert.
        
        
        """
        ...
    def isTrimable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isTrimable`
            Returns :code:`true` is the parameter is trimmable , :code:`false` otherwise.
        
            If parameter is marked as non-trimmable - it cannot be trimmed directly. Its setting can be only calculated by a make
            rule.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isTrimable` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                :code:`true` is the parameter is trimmable, :code:`false` otherwise.
        
        
        """
        ...
    def isVirtual(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isVirtual`
            Returns whether parameter is virtual. In other words whether the parameter is representing a property field of a
            hardware device that is addressable. Virtual parameters cannot be used to drive the hardware.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isVirtual` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                whether parameter is virtual.
        
        
        """
        ...
    def isWritable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Parameter.isWritable`
            Indicates if this parameter is writable.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Parameter.isWritable` in interface :class:`~cern.lsa.domain.settings.Parameter`
        
            Returns:
                :code:`true` if this parameter is writable, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isWritable`
        
        
        """
        ...

class ParameterSettingsImpl(cern.lsa.domain.settings.ParameterSettings, java.io.Serializable, java.lang.Cloneable):
    """
    public class ParameterSettingsImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.ParameterSettings`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.ParameterSettings` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, parameter: cern.lsa.domain.settings.Parameter): ...
    @typing.overload
    def __init__(self, parameter: cern.lsa.domain.settings.Parameter, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer): ...
    @typing.overload
    def __init__(self, parameter: cern.lsa.domain.settings.Parameter, collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]]): ...
    @typing.overload
    def __init__(self, parameterSettings: cern.lsa.domain.settings.ParameterSettings): ...
    def addCurrentSetting(self, setting: cern.lsa.domain.settings.Setting) -> None: ...
    def addUpdatedSetting(self, setting: cern.lsa.domain.settings.Setting) -> None: ...
    def getCurrentBeamProcesses(self) -> java.util.Set[cern.lsa.domain.settings.BeamProcess]: ...
    def getCurrentSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> cern.lsa.domain.settings.Setting:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.getCurrentSetting`
            Returns the current setting for the given beam process. The setting returned is always the current one, whether an
            updated value has been given or not.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.getCurrentSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
        
            Returns:
                the current setting for the given beam process or null if the given beam process has no setting
        
        
        """
        ...
    def getCurrentSettings(self) -> java.util.Set[cern.lsa.domain.settings.Setting]: ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.getParameter`
            Returns the name of the parameter these settings are for.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.getParameter`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Returns:
                the name of the parameter these settings are for
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> cern.lsa.domain.settings.Setting:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.getSetting`
            Returns either the current setting or the updated setting if one exist for the given beam process. The setting returned
            is always the updated one if it exist and the current one if no updated setting has been given for the given beam
            process.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.getSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
        
            Returns:
                the current or the updated setting for the given beam process
        
        
        """
        ...
    def getSettings(self) -> java.util.Set[cern.lsa.domain.settings.Setting]: ...
    def getUpdatedBeamProcesses(self) -> java.util.Set[cern.lsa.domain.settings.BeamProcess]: ...
    def getUpdatedSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> cern.lsa.domain.settings.Setting:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.getUpdatedSetting`
            Returns the updated setting for the given beam process. The setting returned is always the updated one, or null if no
            update has been set.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.getUpdatedSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to return the setting for
        
            Returns:
                the updated setting for the given beam process or null if the given beam process has not been updated
        
        
        """
        ...
    def getUpdatedSettings(self) -> java.util.Set[cern.lsa.domain.settings.Setting]: ...
    def getValueType(self) -> cern.accsoft.commons.value.Type:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.getValueType`
            Returns the type of the value of all settings in this collection.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.getValueType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Returns:
                the type of the value of all settings in this collection
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.isEmpty`
            Returns :code:`true` if there are no settings, neither current nor updated ones or :code:`false` when some settings are
            present.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.isEmpty`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Returns:
                :code:`true` if there are no settings, :code:`false` when some settings are present
        
        
        """
        ...
    @typing.overload
    def isUpdated(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.isUpdated`
            Returns true if at least one setting has been updated, false else.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.isUpdated`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Returns:
                true if at least one setting has been updated, false else.
        
        """
        ...
    @typing.overload
    def isUpdated(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.isUpdated`
            Returns :code:`true` if the setting for the given beam process has been updated, otherwise :code:`false`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.isUpdated`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process to be checked for update
        
            Returns:
                :code:`true` if the setting for the given beam process has been updated, otherwise :code:`false`.
        
        
        """
        ...
    def round(self) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.round`
            Round all the settings that are part of this :code:`ParameterSettings` object.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.round`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
        
        """
        ...
    def size(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.size`
            Returns the number of current settings independently of the updated ones.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.size`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Returns:
                the number of current settings independently of the updated ones
        
        
        """
        ...
    @typing.overload
    def updateSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess, immutableValue: cern.accsoft.commons.value.ImmutableValue, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.updateSetting`
            Updates the setting belonging to the given beam process with the given value.
        
            First, if there is no :meth:`~cern.lsa.domain.settings.ParameterSettings.getCurrentSetting`, the method initializes it
            with an :meth:`~cern.lsa.domain.settings.SettingFactory.newInitialSetting`. If there is already an
            :meth:`~cern.lsa.domain.settings.ParameterSettings.getUpdatedSetting` - the method just updates it with the given value.
            Otherwise it clones the current setting, updates it with the given value and sets it as
            :meth:`~cern.lsa.domain.settings.ParameterSettings.getUpdatedSetting`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.updateSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process whose setting is to be updated
                updatedValue (cern.accsoft.commons.value.ImmutableValue): the value to use for the update
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): the part of the setting to update
        
        
        """
        ...
    @typing.overload
    def updateSetting(self, beamProcess: cern.lsa.domain.settings.BeamProcess, setting: cern.lsa.domain.settings.Setting) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterSettings.updateSetting`
            Updates the setting belonging to the given beam process with the given value.
        
            First, if there is no :meth:`~cern.lsa.domain.settings.ParameterSettings.getCurrentSetting`, the method initializes it
            with an :meth:`~cern.lsa.domain.settings.SettingFactory.newInitialSetting`. If there is already an
            :meth:`~cern.lsa.domain.settings.ParameterSettings.getUpdatedSetting` - the method just updates it with the given value.
            Otherwise it clones the current setting, updates it with the given value and sets it as
            :meth:`~cern.lsa.domain.settings.ParameterSettings.getUpdatedSetting`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterSettings.updateSetting`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterSettings`
        
            Parameters:
                beamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the beam process whose setting is to be updated
                srcSetting (:class:`~cern.lsa.domain.settings.Setting`): the setting to use for the update of the destination setting
        
        """
        ...

class ParameterTreeNodeImpl(cern.lsa.domain.settings.ParameterTreeNode, java.lang.Comparable[cern.lsa.domain.settings.ParameterTreeNode], java.io.Serializable):
    """
    public class ParameterTreeNodeImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.ParameterTreeNode`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.lsa.domain.settings.ParameterTreeNode`>, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.ParameterTreeNode` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, parameter: cern.lsa.domain.settings.Parameter, boolean: bool): ...
    def addChild(self, parameterTreeNodeImpl: 'ParameterTreeNodeImpl') -> None:
        """
            Add a child to this node. This also adds :code:`this` as the parent of the child.
        
            Parameters:
                child (:class:`~cern.lsa.domain.settings.spi.ParameterTreeNodeImpl`): the child to be added
        
        
        """
        ...
    def compareTo(self, parameterTreeNode: cern.lsa.domain.settings.ParameterTreeNode) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def findNode(self, string: str) -> cern.lsa.domain.settings.ParameterTreeNode: ...
    def getAllChildren(self) -> java.util.List[cern.lsa.domain.settings.ParameterTreeNode]: ...
    def getAllParents(self) -> java.util.List[cern.lsa.domain.settings.ParameterTreeNode]: ...
    def getChildren(self) -> java.util.List[cern.lsa.domain.settings.ParameterTreeNode]: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    @typing.overload
    def getNodes(self) -> java.util.List[cern.lsa.domain.settings.ParameterTreeNode]: ...
    @typing.overload
    def getNodes(self, boolean: bool) -> java.util.List[cern.lsa.domain.settings.ParameterTreeNode]: ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterTreeNode.getParameter`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterTreeNode`
        
            Returns:
                The parameter of this node.
        
        
        """
        ...
    def getParameters(self) -> java.util.List[cern.lsa.domain.settings.Parameter]: ...
    def getParametersFromThisNodeAndAllChildren(self) -> java.util.List[cern.lsa.domain.settings.Parameter]: ...
    def getParametersFromThisNodeAndAllParents(self) -> java.util.List[cern.lsa.domain.settings.Parameter]: ...
    def getParents(self) -> java.util.List[cern.lsa.domain.settings.ParameterTreeNode]: ...
    def getThisNodeAndAllChildren(self) -> java.util.List[cern.lsa.domain.settings.ParameterTreeNode]: ...
    def getThisNodeAndAllParents(self) -> java.util.List[cern.lsa.domain.settings.ParameterTreeNode]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isLeaf(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterTreeNode.isLeaf`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterTreeNode`
        
            Returns:
                True if this node does not have any children, otherwise false.
        
        
        """
        ...
    def isRoot(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterTreeNode.isRoot`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterTreeNode`
        
            Returns:
                True if this node does not have any parents, otherwise false.
        
        
        """
        ...
    def isSource(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterTreeNode.isSource`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterTreeNode`
        
            Returns:
                True if this node was requested as a source for certain operations (e.g. trim), otherwise false.
        
        
        """
        ...
    def setIsSource(self, boolean: bool) -> None:
        """
        
            Parameters:
                isSource (boolean): If true, the node will be marked as being a source parameter which contains meaningful information for e.g. trim.
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns a string representation of the node printing its children as well. Please not that this method is cycle-proof by
            marking visited nodes.
        
            Overrides:
                 in class 
        
        
        """
        ...

class ParameterTreesRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.settings.ParameterTreesRequest):
    """
    public class ParameterTreesRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.settings.ParameterTreesRequest`
    
    
        Also see:
            :meth:`~serialized`
    """
    PARAMETER_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETER_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParameterTreesRequestImpl.getParameterNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARAMETERS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETERS
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParameterTreesRequestImpl.getParameters`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    HIERARCHY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` HIERARCHY
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParameterTreesRequestImpl.getHierarchy`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TREE_DIRECTION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TREE_DIRECTION
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParameterTreesRequestImpl.getTreeDirection`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getHierarchy(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.getHierarchy`
            Name of the hierarchy in which search for trees. If not provided than DEFAULT hierarchy will be used.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.getHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterTreesRequest`
        
        
        """
        ...
    def getParameterNames(self) -> java.util.Set[str]: ...
    def getParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getTreeDirection(self) -> cern.lsa.domain.settings.ParameterTreesRequest.TreeDirection:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.getTreeDirection`
            Specifies direction of trees from provided parameters. It can be
            :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.TreeDirection.SOURCE_TREE` to look for source trees (upward
            direction) or :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.TreeDirection.DEPENDENT_TREE` to look for dependent
            trees (downward direction).
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterTreesRequest.getTreeDirection`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterTreesRequest`
        
        
        """
        ...

class ParameterTypeGroupImpl(cern.accsoft.commons.util.AbstractNamed[cern.lsa.domain.settings.ParameterTypeGroup], cern.lsa.domain.settings.ParameterTypeGroup, java.io.Serializable):
    """
    public class ParameterTypeGroupImpl extends cern.accsoft.commons.util.AbstractNamed<:class:`~cern.lsa.domain.settings.ParameterTypeGroup`> implements :class:`~cern.lsa.domain.settings.ParameterTypeGroup`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, parameterTypeCategory: cern.lsa.domain.settings.ParameterTypeCategory): ...
    def addParameterType(self, parameterType: cern.lsa.domain.settings.ParameterType) -> None: ...
    def compareTo(self, parameterTypeGroup: cern.lsa.domain.settings.ParameterTypeGroup) -> int:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                :code:`compareTo` in class :class:`~cern.lsa.domain.settings.ParameterTypeGroup`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :code:`equals` in class :class:`~cern.lsa.domain.settings.ParameterTypeGroup`
        
        
        """
        ...
    def getParameterTypes(self) -> java.util.Set[cern.lsa.domain.settings.ParameterType]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :code:`hashCode` in class :class:`~cern.lsa.domain.settings.ParameterTypeGroup`
        
        
        """
        ...

class ParameterTypeImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.settings.ParameterType], cern.lsa.domain.settings.ParameterType, java.lang.Cloneable):
    """
    public class ParameterTypeImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.settings.ParameterType`> implements :class:`~cern.lsa.domain.settings.ParameterType`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        A ParameterType object defines a type of parameter. A type of parameter groups parameters that have the same
        characteristics and the same sensitivity to the context.
    
        A type of parameter can be context sensitive which means that the value of the parameters of that type changes with the
        context of what is running in the accelarator or context insensitive which means that the value of the parameters of
        that type is unique for the accelerator.
    
        Also see:
            :class:`~cern.lsa.domain.settings.ParameterType`, :meth:`~serialized`
    """
    def clone(self) -> 'ParameterTypeImpl':
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def compareTo(self, parameterType: cern.lsa.domain.settings.ParameterType) -> int:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                :code:`compareTo` in class :class:`~cern.lsa.domain.settings.ParameterType`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Just name is taken into account.
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.equals`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def getCategory(self) -> cern.lsa.domain.settings.ParameterTypeCategory:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterType.getCategory`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterType`
        
            Returns:
                the category of this parameter type or :code:`null` if not defined.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.hashCode`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def isLinkRuleApplicable(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterType.isLinkRuleApplicable`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterType`
        
            Returns:
                whether a linkrule can be applied for this parameter type.
        
        
        """
        ...

class ParameterTypesRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.settings.ParameterTypesRequest):
    """
    public class ParameterTypesRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.settings.ParameterTypesRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.ParameterTypesRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    PARAMETER_TYPE_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETER_TYPE_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParameterTypesRequestImpl.getParameterTypeNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ALL_PARAMETER_TYPES_REQUESTED: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ALL_PARAMETER_TYPES_REQUESTED
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getParameterTypeNames(self) -> java.util.Set[str]: ...
    def isAllParameterTypesRequested(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParameterTypesRequest.isAllParameterTypesRequested`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParameterTypesRequest`
        
        
        """
        ...

class ParametersRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.settings.ParametersRequest):
    """
    public class ParametersRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.settings.ParametersRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.ParametersRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    ACCELERATOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ACCELERATOR
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getAccelerator`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ACCELERATOR_ZONES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ACCELERATOR_ZONES
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getAcceleratorZones`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARTICLE_TRANSFERS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARTICLE_TRANSFERS
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getParticleTransfers`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARAMETER_GROUPS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETER_GROUPS
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getParameterGroups`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARAMETER_TYPE_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETER_TYPE_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getParameterTypeNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROPERTY_FIELDS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPERTY_FIELDS
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getPropertyFields`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROPERTY_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPERTY_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getPropertyNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARAMETER_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETER_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getParameterNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getDeviceNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICES
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getDevices`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MULTIPLEXED: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MULTIPLEXED
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.isMultiplexed` flag.
    
        Also see:
            :meth:`~constant`
    
    
    """
    LSA_IMPLEMENTATION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` LSA_IMPLEMENTATION
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.isLsaImplementation` flag.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VIRTUAL: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` VIRTUAL
    
        Deprecated.
        use LSA instead, following INCA-6038, this should be cleaned up when all clients use the new LSA attribute.
        Attribute name for legacy #isVirtual() flag.
    
        Also see:
            :meth:`~constant`
    
    
    """
    WRITABLE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` WRITABLE
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.isWritable` flag.
    
        Also see:
            :meth:`~constant`
    
    
    """
    READABLE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` READABLE
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.isReadable` flag.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARAMETER_NAME_PATTERN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETER_NAME_PATTERN
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getParameterNamePattern`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CRITICAL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CRITICAL
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.isCritical` flag.
    
        Also see:
            :meth:`~constant`
    
    
    """
    INCLUDE_SIGNATURES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` INCLUDE_SIGNATURES
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.isIncludeSignatures` flag.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VALUE_TYPES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` VALUE_TYPES
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.ParametersRequestImpl.getValueTypes`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getAccelerator`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParametersRequest`
        
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
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.getParameterNamePattern`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParametersRequest`
        
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
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isCritical`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParametersRequest`
        
            Returns:
                whether only parameters marked as critical or non-critical should be returned.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameter.isCritical`
        
        
        """
        ...
    def isIncludeSignatures(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isIncludeSignatures`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParametersRequest`
        
            Returns:
                TRUE to include the special LSA internal signature parameters for MCS properties.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Parameters.isSignatureParameter`
        
        
        """
        ...
    def isLsaImplementation(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParametersRequest.isLsaImplementation`
            Determines whether only parameters with implementation LSA should be returned.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isLsaImplementation`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParametersRequest`
        
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
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParametersRequest.isMultiplexed`
            Determines whether parameters to be returned should be multiplexed or not.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isMultiplexed`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParametersRequest`
        
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
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParametersRequest.isReadable`
            Determines whether only readable or only non-readable parameters should be returned.
        
            Readable parameters are these whose corresponding property
            :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isReadable`. Non-readable parameters are typically command
            parameters that one can only SET.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isReadable`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParametersRequest`
        
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
            Description copied from interface: :meth:`~cern.lsa.domain.settings.ParametersRequest.isWritable`
            Determines whether only writable or only non-writable parameters should be returned.
        
            Writable parameters are these whose corresponding property
            :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isWritable`. Non-writable parameters are typically acquisition
            parameters or configuration read-only parameters that should not be trimmed and/or sent to the hardware.
        
            **Note that if the :meth:`~cern.lsa.domain.settings.Parameter.getParameterType` is not linked to any property**
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.ParametersRequest.isWritable`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.ParametersRequest`
        
            Returns:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#TRUE>` if only
                writable parameters should be returned, `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Boolean.html?is-external=true#FALSE>` if only non-writable
                should be returned, :code:`null` if both writable and non-writable should be returned
        
            Also see:
                :meth:`~cern.lsa.domain.devices.type.PropertyVersion.isWritable`
        
        
        """
        ...

class SettingComparisonParameterResultImpl(cern.lsa.domain.settings.SettingComparisonParameterResult, java.io.Serializable):
    """
    public class SettingComparisonParameterResultImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, parameter: cern.lsa.domain.settings.Parameter, list: java.util.List[cern.lsa.domain.settings.BeamProcess], list2: java.util.List[cern.lsa.domain.settings.BeamProcess]): ...
    def addDetailedResultType(self, beamProcess: cern.lsa.domain.settings.BeamProcess, beamProcess2: cern.lsa.domain.settings.BeamProcess, settingComparisonResultType: cern.lsa.domain.settings.SettingComparisonResultType) -> None:
        """
            Adds the detailed result type of the comparison between the settings of the source and destination beam process.
        
            Parameters:
                sourceBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the source beam process involved in the comparison
                destinationBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the destination beam process involved in the comparison
                parameterResultType (:class:`~cern.lsa.domain.settings.SettingComparisonResultType`): the result type of the comparison
        
        
        """
        ...
    def getDestinationBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.BeamProcess]: ...
    def getDestinationDetailedException(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> java.lang.Exception:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDestinationDetailedException`
            Returns the exception occurred when comparing the destination beam process.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDestinationDetailedException`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult`
        
            Parameters:
                destinationBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the destination beam process involved in the comparison operation.
        
            Returns:
                the exception occurred, if specified, when comparing the destination beam process; :code:`null` otherwise.
        
        
        """
        ...
    def getDestinationException(self) -> java.lang.Exception:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDestinationException`
            Returns exception, if defined, about the destination (e.g.: error occurred when loading destination settings).
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDestinationException`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult`
        
            Returns:
                exception or :code:`null`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.ERROR`
        
        
        """
        ...
    def getDestinationSettings(self) -> cern.lsa.domain.settings.ParameterSettings:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDestinationSettings`
            Settings of the parameter in the context(s) designated as *destination*. It may be null, depending on the type of the
            comparison result, and the configuration of the comparison request. It might not contain settings for all the
            destination beam processes.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDestinationSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult`
        
            Returns:
                settings of the parameter in the destination context
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getResultType`,
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDestinationBeamProcesses`
        
        
        """
        ...
    def getDetailedResultType(self, beamProcess: cern.lsa.domain.settings.BeamProcess, beamProcess2: cern.lsa.domain.settings.BeamProcess) -> cern.lsa.domain.settings.SettingComparisonResultType:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDetailedResultType`
            Returns the detailed result type of the comparison between settings of the source and destination beam process. If
            specified for some input beam processes, this result must be considered as a comparison result type of those beam
            processes. If it is not specified, the overall result type is considered as a comparison result type for the input beam
            processes.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDetailedResultType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult`
        
            Parameters:
                sourceBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the source beam process involved in the comparison
                destinationBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the destination beam process involved in the comparison
        
            Returns:
                the detailed result type of the comparison between settings of the source and destination beam processes. It returns
                :code:`null` if not specified.
        
        
        """
        ...
    def getDetailedResultTypes(self) -> java.util.Map[cern.accsoft.commons.util.value.Pair[cern.lsa.domain.settings.BeamProcess, cern.lsa.domain.settings.BeamProcess], cern.lsa.domain.settings.SettingComparisonResultType]: ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getParameter`
            Returns the parameter involved in the comparison.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getParameter`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult`
        
            Returns:
                the parameter involved in the comparison. It is never :code:`null`.
        
        
        """
        ...
    def getResultType(self) -> cern.lsa.domain.settings.SettingComparisonResultType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getResultType`
            The overall result type of the comparison between source and destination parameters' settings. Depending on this value,
            it may or may not make sense to check the values of the parameters and even the detailed result type: they might not be
            present.
        
        
            In general this result type is applicable to all the couple (source and destination beam process) compared. Eventually,
            for some of them there might be a detailed result type which overrides this one.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getResultType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult`
        
            Returns:
                the overall result type of the comparison
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getDetailedResultType`
        
        
        """
        ...
    def getSourceBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.BeamProcess]: ...
    def getSourceDetailedException(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> java.lang.Exception:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getSourceDetailedException`
            Returns the exception occurred when comparing the source beam process.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getSourceDetailedException`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult`
        
            Parameters:
                sourceBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the source beam process involved in the comparison operation.
        
            Returns:
                the exception occurred, if specified, when comparing the source beam process; :code:`null` otherwise.
        
        
        """
        ...
    def getSourceException(self) -> java.lang.Exception:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getSourceException`
            Returns exception, if defined, about the source (e.g: error occurred when loading source settings).
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getSourceException`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult`
        
            Returns:
                exception or :code:`null`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonResultType.ERROR`
        
        
        """
        ...
    def getSourceSettings(self) -> cern.lsa.domain.settings.ParameterSettings:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getSourceSettings`
            Settings of the parameter in the context(s) designated as *source*. It may be null, depending on the type of the
            comparison result, and the configuration of the comparison request. It might not contain settings for all the source
            beam processes.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getSourceSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonParameterResult`
        
            Returns:
                settings of the parameter in the source context
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getResultType`,
                :meth:`~cern.lsa.domain.settings.SettingComparisonParameterResult.getSourceBeamProcesses`
        
        
        """
        ...
    def setDestinationDetailedException(self, beamProcess: cern.lsa.domain.settings.BeamProcess, exception: java.lang.Exception) -> None:
        """
            Sets the detailed exception related to the comparison of the destination beam process.
        
            Parameters:
                destinationBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the destination beam process the exception is occurred
                exception (`Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`): the exception occurred
        
        
        """
        ...
    def setDestinationException(self, exception: java.lang.Exception) -> None:
        """
            Sets the exception about the destination settings (e.g.: if it hasn't been possible to retrieve settings from hardware).
            If this is set, :meth:`~cern.lsa.domain.settings.spi.SettingComparisonParameterResultImpl.getDestinationSettings` might
            be null.
        
            Parameters:
                exception (`Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`): the exception to be set
        
        
        """
        ...
    def setDestinationSettings(self, parameterSettings: cern.lsa.domain.settings.ParameterSettings) -> None:
        """
            Sets the settings to be considered as destination. The parameter of :code:`settings` must be same of the one set in this
            result object.
        
            Parameters:
                settings (:class:`~cern.lsa.domain.settings.ParameterSettings`): the source settings
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.SettingComparisonParameterResultImpl.getParameter`,
                :meth:`~cern.lsa.domain.settings.ParameterSettings.getParameter`
        
        
        """
        ...
    def setDetailedResultTypes(self, map: typing.Union[java.util.Map[cern.accsoft.commons.util.value.Pair[cern.lsa.domain.settings.BeamProcess, cern.lsa.domain.settings.BeamProcess], cern.lsa.domain.settings.SettingComparisonResultType], typing.Mapping[cern.accsoft.commons.util.value.Pair[cern.lsa.domain.settings.BeamProcess, cern.lsa.domain.settings.BeamProcess], cern.lsa.domain.settings.SettingComparisonResultType]]) -> None: ...
    def setResultType(self, settingComparisonResultType: cern.lsa.domain.settings.SettingComparisonResultType) -> None:
        """
            Sets the overall result of the comparison operation involving the parameter this result object has been created for.
        
            Parameters:
                resultType (:class:`~cern.lsa.domain.settings.SettingComparisonResultType`): the result type
        
        
        """
        ...
    def setSourceDetailedException(self, beamProcess: cern.lsa.domain.settings.BeamProcess, exception: java.lang.Exception) -> None:
        """
            Sets the detailed exception related to the comparison of the source beam process.
        
            Parameters:
                sourceBeamProcess (:class:`~cern.lsa.domain.settings.BeamProcess`): the source beam process the exception is occurred
                exception (`Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`): the exception occurred
        
        
        """
        ...
    def setSourceException(self, exception: java.lang.Exception) -> None:
        """
            Sets the exception about the source settings (e.g.: if it hasn't been possible to retrieve settings from hardware). If
            this is set, :meth:`~cern.lsa.domain.settings.spi.SettingComparisonParameterResultImpl.getSourceSettings` might be null.
        
            Parameters:
                exception (`Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`): the exception to be set
        
        
        """
        ...
    def setSourceSettings(self, parameterSettings: cern.lsa.domain.settings.ParameterSettings) -> None:
        """
            Sets the settings to be considered as source. The parameter of :code:`settings` must be same of the one set in this
            result object.
        
            Parameters:
                settings (:class:`~cern.lsa.domain.settings.ParameterSettings`): the source settings
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.SettingComparisonParameterResultImpl.getParameter`,
                :meth:`~cern.lsa.domain.settings.ParameterSettings.getParameter`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class SettingComparisonRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.settings.SettingComparisonRequest):
    """
    public class SettingComparisonRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.settings.SettingComparisonRequest`
    
        Immutable implementation for a setting comparison request.
    
        Clients are expected to use a builder, provided by this package, rather than constructing instances of this object
        themselves.
    
        Also see:
            :meth:`~serialized`
    """
    POINT_IN_SRC_FUNCTION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` POINT_IN_SRC_FUNCTION
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    POINT_IN_DEST_FUNCTION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` POINT_IN_DEST_FUNCTION
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SRC_SETTINGS_SOURCE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SRC_SETTINGS_SOURCE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEST_SETTINGS_SOURCE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEST_SETTINGS_SOURCE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARAMETERS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETERS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    COMPARE_ALL_PARAMETERS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` COMPARE_ALL_PARAMETERS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SRC_BEAMPROCESSES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SRC_BEAMPROCESSES
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEST_BEAMPROCESSES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEST_BEAMPROCESSES
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    IGNORE_FLAT_FUNCTION_LENGTH: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` IGNORE_FLAT_FUNCTION_LENGTH
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def compareAllParameters(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.compareAllParameters`
            Returns :code:`true` if all settings should be compared between source and destination contexts; returns :code:`false`
            if only :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getParameters` parameters should be compared.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.compareAllParameters`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonRequest`
        
        
        """
        ...
    def getDestinationBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.BeamProcess]: ...
    def getDestinationSettingsSource(self) -> cern.lsa.domain.settings.SettingsSource:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getDestinationSettingsSource`
            Returns settings source of the destination context.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getDestinationSettingsSource`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonRequest`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getDestinationBeamProcesses`
        
        
        """
        ...
    def getParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getPointInDestFunction(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getPointInDestFunction`
            Returns the point in time, in X, for the function of the destination parameter at which the comparison is to be made.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getPointInDestFunction`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonRequest`
        
            Returns:
                point in the function for the destination parameter
        
        
        """
        ...
    def getPointInSourceFunction(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getPointInSourceFunction`
            Returns the point in time, in X, for the function of the source parameter at which the comparison is to be made.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getPointInSourceFunction`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonRequest`
        
            Returns:
                point in the function for the source parameter
        
        
        """
        ...
    def getSourceBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.BeamProcess]: ...
    def getSourceSettingsSource(self) -> cern.lsa.domain.settings.SettingsSource:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getSourceSettingsSource`
            Returns settings source of the source context.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getSourceSettingsSource`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonRequest`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.getSourceBeamProcesses`
        
        
        """
        ...
    def ignoreFlatFunctionsLength(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.ignoreFlatFunctionsLength`
            Returns :code:`true` if length should be ignored when comparing two flat functions i.e. if two flat functions have the
            same value but different length - they will be treated as the same.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonRequest.ignoreFlatFunctionsLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonRequest`
        
            Returns:
                :code:`true` to treat two flat functions of the same value as the same even if their lengths are different
        
        
        """
        ...

class SettingComparisonResponseImpl(cern.lsa.domain.settings.SettingComparisonResponse, java.io.Serializable):
    """
    public class SettingComparisonResponseImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.SettingComparisonResponse`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        The implementation of the :class:`~cern.lsa.domain.settings.SettingComparisonResponse` interface
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, settingComparisonRequest: cern.lsa.domain.settings.SettingComparisonRequest, settingComparisonResult: cern.lsa.domain.settings.SettingComparisonResult): ...
    def getSettingComparisonRequest(self) -> cern.lsa.domain.settings.SettingComparisonRequest:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.SettingComparisonResponse.getSettingComparisonRequest`
            Returns the original comparison request which generated this response
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonResponse.getSettingComparisonRequest`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonResponse`
        
            Returns:
                the original comparison request
        
        
        """
        ...
    def getSettingComparisonResult(self) -> cern.lsa.domain.settings.SettingComparisonResult:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.SettingComparisonResponse.getSettingComparisonResult`
            Returns the result of the comparison operation
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonResponse.getSettingComparisonResult`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonResponse`
        
            Returns:
                the result of the comparison operation
        
        
        """
        ...

class SettingComparisonResultImpl(cern.lsa.domain.settings.SettingComparisonResult, java.io.Serializable):
    """
    public class SettingComparisonResultImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.SettingComparisonResult`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Implementation of the :class:`~cern.lsa.domain.settings.SettingComparisonResult` interface
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingComparisonParameterResult], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingComparisonParameterResult]]): ...
    def getComparedParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getSettingComparisonParameterResult(self, parameter: cern.lsa.domain.settings.Parameter) -> cern.lsa.domain.settings.SettingComparisonParameterResult:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.SettingComparisonResult.getSettingComparisonParameterResult`
            Returns the comparison result for the given compared parameter.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingComparisonResult.getSettingComparisonParameterResult`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingComparisonResult`
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): the parameter the comparison result has to be retrieved
        
            Returns:
                Returns the comparison result for the given compared parameter. It returns :code:`null` if the parameter was not
                involved in the comparison operation.
        
        
        """
        ...
    def getSettingComparisonParameterResults(self) -> java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingComparisonParameterResult]: ...

class StandAloneContextCloneRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.settings.StandAloneContextCloneRequest):
    """
    public class StandAloneContextCloneRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.settings.StandAloneContextCloneRequest`
    
        Default implementation of the :code:`StandAloneContextCloneRequest` interface
    
        Also see:
            :meth:`~serialized`
    """
    CLONE_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CLONE_NAME
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCloneRequestImpl.getCloneName`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DESCRIPTION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DESCRIPTION
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCloneRequestImpl.getDescription`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ATTRIBUTES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ATTRIBUTES
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCloneRequestImpl.getAttributes`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SOURCE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SOURCE
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCloneRequestImpl.getSource`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    WITH_HISTORY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` WITH_HISTORY
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCloneRequestImpl.withHistory`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    HISTORY_CUT_OFF_DATE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` HISTORY_CUT_OFF_DATE
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCloneRequestImpl.getHistoryCutOff`)}.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CONTEXT_CATEGORY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CONTEXT_CATEGORY
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCloneRequestImpl.getContextCategory`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CLONE_TYPE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CLONE_TYPE
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCloneRequestImpl.shouldCloneType`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getCloneName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCloneRequest.getCloneName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCloneRequest`
        
            Returns:
                name of the clone
        
        
        """
        ...
    def getContextCategory(self) -> cern.lsa.domain.settings.ContextCategory:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCloneRequest.getContextCategory`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCloneRequest`
        
            Returns:
                category of the clone context
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCloneRequest.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCloneRequest`
        
            Returns:
                description of the clone
        
        
        """
        ...
    def getHistoryCutOff(self) -> java.time.Instant:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCloneRequest.getHistoryCutOff`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCloneRequest`
        
            Returns:
                the date from which the settings history will start if such a date was set, null otherwise
        
        
        """
        ...
    def getSource(self) -> cern.lsa.domain.settings.StandAloneContext:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCloneRequest.getSource`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCloneRequest`
        
            Returns:
                the source StandAloneContext to clone from
        
        
        """
        ...
    def shouldCloneType(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCloneRequest.shouldCloneType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCloneRequest`
        
            Returns:
                weather we should also clone the type of the given standalone context all it's sub-contexts
        
        
        """
        ...
    def withHistory(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCloneRequest.withHistory`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCloneRequest`
        
            Returns:
                flag deciding if the settings history should be also cloned
        
        
        """
        ...

class StandAloneContextCreationRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.settings.StandAloneContextCreationRequest):
    """
    public class StandAloneContextCreationRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.settings.StandAloneContextCreationRequest`
    
        Default implementation of the :code:`StandAloneContextCreationRequest` interface
    
        Also see:
            :meth:`~serialized`
    """
    NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` NAME
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCreationRequestImpl.getName`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DESCRIPTION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DESCRIPTION
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCreationRequestImpl.getDescription`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CONTEXT_TYPE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CONTEXT_TYPE
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCreationRequestImpl.getContextType`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CONTEXT_CATEGORY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CONTEXT_CATEGORY
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCreationRequestImpl.getContextCategory`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ATTRIBUTES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ATTRIBUTES
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCreationRequestImpl.getAttributes`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    LENGTH: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` LENGTH
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCreationRequestImpl.getLength`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MULTIPLEXITY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MULTIPLEXITY
    
        Property name for :meth:`~cern.lsa.domain.settings.spi.StandAloneContextCreationRequestImpl.isMultiplexed` }.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getContextCategory(self) -> cern.lsa.domain.settings.ContextCategory:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCreationRequest.getContextCategory`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCreationRequest`
        
            Returns:
                the context category to which the newly created context should belong
        
        
        """
        ...
    def getContextType(self) -> cern.lsa.domain.settings.type.ContextType:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCreationRequest.getContextType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCreationRequest`
        
            Returns:
                The ContextType, which should serve as a pattern for the created :class:`~cern.lsa.domain.settings.StandAloneContext`
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCreationRequest.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCreationRequest`
        
            Returns:
                description of the :class:`~cern.lsa.domain.settings.StandAloneContext` to be created
        
        
        """
        ...
    def getLength(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCreationRequest.getLength`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCreationRequest`
        
            Returns:
                the requested length of the created context
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCreationRequest.getName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCreationRequest`
        
            Returns:
                name of the to-be-created :class:`~cern.lsa.domain.settings.StandAloneContext`
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContextCreationRequest.isMultiplexed`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContextCreationRequest`
        
            Returns:
                the multiplexity of the created context
        
        
        """
        ...

class TrimHeaderImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedEntity[cern.lsa.domain.settings.TrimHeader], cern.lsa.domain.settings.TrimHeader, java.io.Serializable):
    """
    public class TrimHeaderImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity`<:class:`~cern.lsa.domain.settings.TrimHeader`> implements :class:`~cern.lsa.domain.settings.TrimHeader`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of :class:`~cern.lsa.domain.settings.TrimHeader`.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.BeamProcess]: ...
    def getClientInfo(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimHeader.getClientInfo`
            Returns the information on the client who made the trim (app, user, host)
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimHeader.getClientInfo` in interface :class:`~cern.lsa.domain.settings.TrimHeader`
        
            Returns:
                the information on the client who made the trim (app, user, host)
        
        
        """
        ...
    def getCreatedDate(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimHeader.getCreatedDate`
            Returns the date at which this archive has been created.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimHeader.getCreatedDate` in interface :class:`~cern.lsa.domain.settings.TrimHeader`
        
            Returns:
                the date at which this archive has been created.
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimHeader.getDescription`
            Returns the description associated with this trim.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimHeader.getDescription` in interface :class:`~cern.lsa.domain.settings.TrimHeader`
        
            Returns:
                the description associated with this trim.
        
        
        """
        ...
    def isTag(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimHeader.isTag`
            Returns true if the trim is a tag, false otherwise
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimHeader.isTag` in interface :class:`~cern.lsa.domain.settings.TrimHeader`
        
            Returns:
                true if the trim is a tag, false otherwise
        
        
        """
        ...
    def setBeamProcesses(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.BeamProcess], typing.Sequence[cern.lsa.domain.settings.BeamProcess]]) -> None: ...
    def setClientInfo(self, string: str) -> None: ...
    def setCreatedDate(self, date: java.util.Date) -> None: ...
    def setDescription(self, string: str) -> None: ...
    def setTag(self, boolean: bool) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class TrimRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.settings.TrimRequest):
    """
    public class TrimRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.settings.TrimRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.TrimRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    IS_GENERATION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` IS_GENERATION
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SETTING_PART: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SETTING_PART
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CHILD_SETTING_PART: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CHILD_SETTING_PART
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CUSTOM_SETTING_PART_MAP: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CUSTOM_SETTING_PART_MAP
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CONTEXT_SETTINGS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CONTEXT_SETTINGS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    PARAMETERS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PARAMETERS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    IGNORE_ERRORS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` IGNORE_ERRORS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    LENIENT_DRIVE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` LENIENT_DRIVE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROPAGATE_TO_CHILDREN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPAGATE_TO_CHILDREN
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    RELATIVE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RELATIVE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    PERSIST_SETTINGS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PERSIST_SETTINGS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    RETURN_SETTINGS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RETURN_SETTINGS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DRIVE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DRIVE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DESCRIPTION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DESCRIPTION
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    FORCE_DRIVE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` FORCE_DRIVE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SKIP_PROCESSING: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SKIP_PROCESSING
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    FORCE_PROCESSING: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` FORCE_PROCESSING
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SKIP_DRIVING_SOURCE_PARAMETERS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SKIP_DRIVING_SOURCE_PARAMETERS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    COMMIT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` COMMIT
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRANSACTION_ID: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TRANSACTION_ID
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]], map2: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getAttribute(self, string: str) -> typing.Any:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.getAttribute`
            Returns a custom attribute associated with this request.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getAttribute` in interface :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
        
            Returns:
                attribute value
        
        
        """
        ...
    def getAttributes(self) -> java.util.Map[str, typing.Any]: ...
    def getChildSettingPart(self) -> cern.lsa.domain.settings.SettingPartEnum:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.getChildSettingPart`
            Returns the setting part which should be used to update the children within the trim. Default value is
            :meth:`~cern.lsa.domain.settings.SettingPartEnum.TARGET`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getChildSettingPart`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
        
        """
        ...
    def getContext(self) -> cern.lsa.domain.settings.StandAloneContext:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.getContext`
            Returns the :code:`StandAloneContext` on which the trim should be performed.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getContext` in interface :class:`~cern.lsa.domain.settings.TrimRequest`
        
        
        """
        ...
    def getContextSettings(self) -> cern.lsa.domain.settings.ContextSettings:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.getContextSettings`
            Returns :code:`ContextSettings` containing new setting values.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getContextSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
        
        """
        ...
    def getCustomSettingPart(self, parameter: cern.lsa.domain.settings.Parameter) -> cern.lsa.domain.settings.SettingPartEnum:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.getCustomSettingPart`
            Returns the custom setting part to be used by the trim to update the setting for the given parameters. If no custom
            setting part is specified, this method returns null. (Typically then either the setting part for source parameters or
            the child setting part will be taken as default.)
        
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getCustomSettingPart`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
        
        """
        ...
    def getCustomSettingPartMap(self) -> java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.SettingPartEnum]: ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.getDescription`
            Returns description of the trim (comment).
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimHeader.getDescription`
        
        
        """
        ...
    def getParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getSettingPart(self) -> cern.lsa.domain.settings.SettingPartEnum:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.getSettingPart`
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
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getSettingPart`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
        
        """
        ...
    def getTransactionId(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.getTransactionId`
            Returns the custom transaction ID to be used for driving transactional parameters, if set. Otherwise, returns null. If
            no transaction ID is set, one will be generated automatically if it is required.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getTransactionId`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                the transaction ID, or null if not set
        
        
        """
        ...
    def isCommit(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isCommit`
            Determines whether the trimmed settings should be committed after driven to the hardware.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isCommit` in interface :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                :code:`true` if commit should be performed after drive
        
        
        """
        ...
    def isDrive(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive`
            Determines whether the trimmed settings should be driven to the hardware.
        
            Note that trim will attempt to drive settings only if the associated
            :meth:`~cern.lsa.domain.settings.TrimRequest.getContext` is
            :meth:`~cern.lsa.domain.settings.StandAloneContext.isResident`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive` in interface :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                :code:`true` if drive should be performed
        
        
        """
        ...
    def isForceDrive(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isForceDrive`
            Determines whether the trimmed settings should be driven to the hardware even if they have not changed.
        
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isForceDrive` in interface :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                :code:`true` if drive should be performed even though there are no changes
        
        
        """
        ...
    def isForceProcessing(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isForceProcessing`
            Determines if all rules should be executed even if by default it's not necessary. With such policy even if trimmed
            settings are the same as the current ones in the database - they will be marked as updated and propagated down in the
            hierarchy (all make rules will be executed). Also link rules and incorporation rules will be executed even if functions
            are continue.
        
            The only case when make rules won't be executed even with this policy is when the
            :meth:`~cern.lsa.domain.settings.TrimRequest.isPropagateToChildren` flag is set to :code:`false`.
        
            This property is meant for settings (re)generation when we want everything to be recalculated, taking into account
            possible change of configuration in the database or change of implementation of certain rules.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isForceProcessing`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                :code:`true` if settings should be updated though there are no changes
        
        
        """
        ...
    def isIgnoreErrors(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isIgnoreErrors`
            Determines if trim should continue if an error occurs or the :class:`~cern.lsa.domain.settings.TrimException` should be
            thrown.
        
            If this method returns :code:`true` - all exceptions that occurred during trim can be retrieved from
            :meth:`~cern.lsa.domain.settings.TrimResult.getWarnings`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isIgnoreErrors`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
        
        """
        ...
    def isLenientDrive(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isLenientDrive`
            The flag determines the trim and drive behavior in case when drive exceptions are encountered (ex. an equipment refused
            settings).
        
            This flag is taken into account only if the trim is performed on a resident context, the
            :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive` has been requested and when drive problems have been encountered.
            If the flag is :code:`false` (default) - drive transaction (if transactional parameters are part of the operation) will
            be rolled back, the trimmed settings will not be persisted and a :code:`DriveException` will be thrown. If the flag is
            :code:`true`, drive problems will be ignored and commit will be still issued both for drive transaction (if
            transactional parameters are part of the operation) and settings persistency.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isLenientDrive`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                :code:`true` if the drive should be lenient (drive exceptions are ignored and drive transaction is committed and
                settings persisted)
        
        
        """
        ...
    def isPersistSettings(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isPersistSettings`
            Determines if settings should be persisted in the database.
        
            This flag can be used to perform trim simulation.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPersistSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                if :code:`true` settings will be persisted
        
        
        """
        ...
    def isPropagateToChildren(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isPropagateToChildren`
            Determines whether trim made on given parameters should be propagated to all their dependent parameters.
        
            In most of situations this flag should be set to :code:`true` to keep settings within parameter trees consistent.
            However in some situations we might want not to propagate the change downwards the hierarchy e.g. when we trim a
            MOMENTUM parameter.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isPropagateToChildren`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                if :code:`true` the change will be propagated to all dependent parameters (and their dependents)
        
        
        """
        ...
    def isRelative(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isRelative`
            Determines if values from the request should be treated as relative (delta) values (:code:`true`) or as absolute values
            (:code:`false`).
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isRelative` in interface :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                :code:`true` if the request contains relative (delta) values
        
        
        """
        ...
    def isReturnSettings(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isReturnSettings`
            Determines if after the trim operation the returned :class:`~cern.lsa.domain.settings.TrimResult` should contain
            :meth:`~cern.lsa.domain.settings.TrimResult.getContextSettings` object with current and updated settings of parameters
            affected by the trim.
        
            The flag should be set to :code:`true` only if the application calling the trim API is interested in affected parameters
            and/or affected settings. Otherwise this flag should be set to :code:`false`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isReturnSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                :code:`true` if the ContextSettings object used by trim should be returned to the client within
                :class:`~cern.lsa.domain.settings.TrimResult`; :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimResult.getContextSettings`
        
        
        """
        ...
    def isSkipProcessing(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.isSkipProcessing`
            Determines whether the trim should skip processing the settings i.e. run make rules, incorporation rules, link rules
            etc. This flag might be useful if one wants just to persist settings without any further processing.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.isSkipProcessing`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Returns:
                :code:`true` if settings should be processed by the trim or not
        
        
        """
        ...
    def setAttribute(self, string: str, object: typing.Any) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.setAttribute`
            Sets a custom attribute for this request.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.setAttribute` in interface :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
                attrValue (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): value of the attribute
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getAttribute`, :meth:`~cern.lsa.domain.settings.TrimRequest.getAttributes`
        
        
        """
        ...
    def setSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimRequest.setSettingPart`
            Allows to change the setting part to be used by the trim.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimRequest.setSettingPart`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Parameters:
                settingPart (:class:`~cern.lsa.domain.settings.SettingPartEnum`): setting part to be used by the trim
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder.toString`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder`
        
        
        """
        ...

class TrimResponseImpl(cern.lsa.domain.settings.TrimResponse, java.io.Serializable):
    """
    public class TrimResponseImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.TrimResponse`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of :class:`~cern.lsa.domain.settings.TrimResponse` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, trimResult: cern.lsa.domain.settings.TrimResult, driveResult: cern.lsa.domain.exploitation.DriveResult): ...
    def getDriveResult(self) -> cern.lsa.domain.exploitation.DriveResult:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimResponse.getDriveResult`
            Result of the drive operation. This method returns :code:`null` if the trim didn't involve driving settings to the
            hardware. This may happen if the trimmed context is not resident or the drive was not requested in the
            :meth:`~cern.lsa.domain.settings.TrimRequest.isDrive`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimResponse.getDriveResult`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimResponse`
        
            Returns:
                result of the drive operation
        
        
        """
        ...
    def getTrimResult(self) -> cern.lsa.domain.settings.TrimResult:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimResponse.getTrimResult`
            Returns result of the trim operation.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimResponse.getTrimResult`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimResponse`
        
            Returns:
                result of the trim operation
        
        
        """
        ...
    def isDrivePerformed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimResponse.isDrivePerformed`
            Returns :code:`true` if settings were driven to the hardware after trim operation. In other words it returns
            :code:`true` if the :meth:`~cern.lsa.domain.settings.TrimResponse.getDriveResult` is not :code:`null` and there was at
            least one parameter successfully driven to the hardware.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimResponse.isDrivePerformed`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimResponse`
        
            Returns:
                :code:`true` if drive was performed, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimResponse.getDriveResult`
        
        
        """
        ...

class TrimResultImpl(cern.lsa.domain.settings.TrimResult, java.io.Serializable):
    """
    public class TrimResultImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.TrimResult`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.TrimResult` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, trimRequest: cern.lsa.domain.settings.TrimRequest, contextSettings: cern.lsa.domain.settings.ContextSettings): ...
    @typing.overload
    def __init__(self, trimRequest: cern.lsa.domain.settings.TrimRequest, trimHeader: cern.lsa.domain.settings.TrimHeader, contextSettings: cern.lsa.domain.settings.ContextSettings, list: java.util.List[cern.accsoft.commons.util.value.Pair[str, java.lang.Throwable]]): ...
    def getAttribute(self, string: str) -> java.io.Serializable:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimResult.getAttribute`
            Returns value of a custom attribute that might have been set during :code:`trim` or :code:`drive` operations.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimResult.getAttribute` in interface :class:`~cern.lsa.domain.settings.TrimResult`
        
            Parameters:
                attrName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the custom attribute
        
            Returns:
                attribute value or :code:`null` if the attribute was not set
        
        
        """
        ...
    def getContext(self) -> cern.lsa.domain.settings.StandAloneContext:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimResult.getContext`
            Returns the :code:`StandAloneContext` on which the trim operation has been performed.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimResult.getContext` in interface :class:`~cern.lsa.domain.settings.TrimResult`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getContext`, :meth:`~cern.lsa.domain.settings.TrimResult.getTrimRequest`
        
        
        """
        ...
    def getContextSettings(self) -> cern.lsa.domain.settings.ContextSettings:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimResult.getContextSettings`
            Returns settings of all parameters loaded and calculated by the Trim. The object contains not only calculated settings
            but also settings of parameters that might have been used for calculations i.e. parent parameters.
        
            The method returns an object only if :meth:`~cern.lsa.domain.settings.TrimRequest.isReturnSettings` is set to
            :code:`true` (which is the default value).
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimResult.getContextSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.TrimResult`
        
        
        """
        ...
    def getTrimHeader(self) -> cern.lsa.domain.settings.TrimHeader:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimResult.getTrimHeader`
            Return the :class:`~cern.lsa.domain.settings.TrimHeader` of the trim persisted following the
            :class:`~cern.lsa.domain.settings.TrimRequest`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimResult.getTrimHeader` in interface :class:`~cern.lsa.domain.settings.TrimResult`
        
            Returns:
                the :class:`~cern.lsa.domain.settings.TrimHeader` or null, if nothing was persisted
        
        
        """
        ...
    def getTrimRequest(self) -> cern.lsa.domain.settings.TrimRequest:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.TrimResult.getTrimRequest`
            Returns the request that was used to perform the trim operation.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.TrimResult.getTrimRequest` in interface :class:`~cern.lsa.domain.settings.TrimResult`
        
            Returns:
                the original :code:`TrimRequest` object
        
        
        """
        ...
    def getWarnings(self) -> java.util.List[cern.accsoft.commons.util.value.Pair[str, java.lang.Throwable]]: ...
    def putAttributes(self, map: typing.Union[java.util.Map[str, java.io.Serializable], typing.Mapping[str, java.io.Serializable]]) -> None: ...
    def setAttribute(self, string: str, serializable: java.io.Serializable) -> None: ...

class UserContextMappingImpl(cern.lsa.domain.settings.UserContextMapping, java.io.Serializable):
    """
    public class UserContextMappingImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.UserContextMapping`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation for a user to context mapping entry.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, string2: str, long: int, operationType: cern.lsa.domain.settings.UserContextMapping.OperationType, string3: str, boolean: bool): ...
    def equalByName(self, userContextMapping: cern.lsa.domain.settings.UserContextMapping) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.UserContextMapping.equalByName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.UserContextMapping`
        
            Returns:
                true when given :class:`~cern.lsa.domain.settings.UserContextMapping` has the same name, the same parent's name
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getContextName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.UserContextMapping.getContextName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.UserContextMapping`
        
            Returns:
                name of the context for this mapping
        
        
        """
        ...
    def getContextParent(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.UserContextMapping.getContextParent`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.UserContextMapping`
        
            Returns:
                name of the context containing this context
        
        
        """
        ...
    def getMappingTimestamp(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.UserContextMapping.getMappingTimestamp`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.UserContextMapping`
        
            Returns:
                timestamp in which this mapping was established
        
        
        """
        ...
    def getOperationType(self) -> cern.lsa.domain.settings.UserContextMapping.OperationType:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.UserContextMapping.getOperationType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.UserContextMapping`
        
            Returns:
                type of the operation
        
        
        """
        ...
    def getUser(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.UserContextMapping.getUser`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.UserContextMapping`
        
            Returns:
                name of the user for this mapping
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isResident(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.UserContextMapping.isResident`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.UserContextMapping`
        
            Returns:
                true if context is resident
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class BoundedPolynomialSequenceSetting(AbstractSetting):
    """
    public class BoundedPolynomialSequenceSetting extends :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getCorrectionValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue`
            Returns the correction value of this setting. If the setting holds no correction value (correction is not defined) the
            value returned depends on its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.getCorrectionValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getTargetValue(self) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getTargetValue`
            Returns the target value of this setting. If the setting holds no target value (target is not defined) the value
            returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getTargetValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.getTargetValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getValue(self) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getValue`
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two value is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned depends of its type.
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    @typing.overload
    def setValue(self, boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence) -> None:
        """
        public void setValue (cern.accsoft.commons.value.ScalarArray2D value)
        
        
        """
        ...
    @typing.overload
    def setValue(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D) -> None: ...

class ContextImpl(ContextBase[cern.lsa.domain.settings.Context], cern.lsa.domain.settings.Context):
    """
    public abstract class ContextImpl extends :class:`~cern.lsa.domain.settings.spi.ContextBase`<:class:`~cern.lsa.domain.settings.Context`> implements :class:`~cern.lsa.domain.settings.Context`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.Context` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.getDescription`
            Description of the context entered by the creator.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.getDescription` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.ContextBase.getDescription`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.ContextBase`
        
            Returns:
                description of the context
        
        
        """
        ...
    def getParent(self) -> cern.lsa.domain.settings.Context:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.getParent`
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
        
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.getParent` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Returns:
                The parent :code:`Context` or :code:`null` if none exists.
        
        
        """
        ...
    def getTypeName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.getTypeName`
            Returns name of the context type, that this context instance has been created from. The type of the context holds common
            characteristics of the context.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.getTypeName` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Returns:
                name of associated context type
        
            Also see:
                :class:`~cern.lsa.domain.settings.type.BeamProcessType`, :class:`~cern.lsa.domain.settings.type.CycleType`
        
        
        """
        ...
    def isMultiplexed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.isMultiplexed`
            Indicates whether this context is multiplexed or not. Apart of special, dedicated contexts that are non-multiplexed, all
            the other contexts are multiplexed.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.isMultiplexed` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Returns:
                :code:`true` if context is multiplexed, :code:`false` otherwise
        
        
        """
        ...
    def isStandAlone(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.isStandAlone`
            Returns :code:`true` if this context is stand-alone, and :code:`false` if the context belongs to another context.
        
            In other words this method return :code:`true` if the context is a :code:`StandAloneCycle` or
            :code:`StandAloneBeamProcess`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.isStandAlone` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Returns:
                :code:`true` if the context is stand-alone, :code:`false` otherwise
        
        
        """
        ...
    def setMultiplexed(self, boolean: bool) -> None: ...
    def setParent(self, context: cern.lsa.domain.settings.Context) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ContextImpl.getParent`
        
        
        """
        ...
    def setTypeName(self, string: str) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.ContextImpl.getTypeName`
        
        
        """
        ...

class CopySettingsRequestImpl(TrimRequestImpl, cern.lsa.domain.settings.CopySettingsRequest):
    """
    public class CopySettingsRequestImpl extends :class:`~cern.lsa.domain.settings.spi.TrimRequestImpl` implements :class:`~cern.lsa.domain.settings.CopySettingsRequest`
    
    
        Also see:
            :meth:`~serialized`
    """
    SETTINGS_SOURCE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SETTINGS_SOURCE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SOURCE_CONTEXTS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SOURCE_CONTEXTS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DESTINATION_CONTEXTS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DESTINATION_CONTEXTS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DESTINATION_PARAMETERS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DESTINATION_PARAMETERS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]], map2: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getDestinationContexts(self) -> java.util.List[cern.lsa.domain.settings.Context]: ...
    def getDestinationParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getSettingsSource(self) -> cern.lsa.domain.settings.SettingsSource:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.CopySettingsRequest.getSettingsSource`
            Descriptor of how source settings should be retrieved.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CopySettingsRequest.getSettingsSource`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CopySettingsRequest`
        
        
        """
        ...
    def getSourceContexts(self) -> java.util.List[cern.lsa.domain.settings.Context]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.TrimRequestImpl.toString`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.TrimRequestImpl`
        
        
        """
        ...

class FunctionSetting(AbstractSetting, java.io.Serializable, java.lang.Cloneable):
    """
    public class FunctionSetting extends :class:`~cern.lsa.domain.settings.spi.AbstractSetting` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        :class:`~cern.lsa.domain.settings.Setting` implementation dedicated for functions and function lists.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, type: cern.accsoft.commons.value.Type): ...
    def clone(self) -> 'FunctionSetting':
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.clone`
            Returns a deep copy of this Setting.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.clone` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.clone`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                a deep copy of this Setting
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def getCorrectionValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue`
            Returns the correction value of this setting. If the setting holds no correction value (correction is not defined) the
            value returned depends on its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.getCorrectionValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getTargetValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getTargetValue`
            Returns the target value of this setting. If the setting holds no target value (target is not defined) the value
            returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getTargetValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.getTargetValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getValue`
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two value is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def setCorrectionValue(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> None:
        """
            Sets the correction points of this Setting. The current correction points are discarded and replaced by new ones based
            on the given discreteFunction.
        
            Parameters:
                discreteFunction (cern.accsoft.commons.value.ImmutableDiscreteFunction): the possibly :code:`null` new value of the correction value
        
        
        """
        ...
    def setTargetValue(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction) -> None:
        """
            Sets the target points of this Setting. The current target points are discarded and replaced by new ones based on the
            given discreteFunction.
        
            Parameters:
                discreteFunction (cern.accsoft.commons.value.ImmutableDiscreteFunction): the possibly :code:`null` new value of the target value
        
        
        """
        ...

class FunctionsArraySetting(AbstractSetting, java.io.Serializable, java.lang.Cloneable):
    """
    public class FunctionsArraySetting extends :class:`~cern.lsa.domain.settings.spi.AbstractSetting` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        :class:`~cern.lsa.domain.settings.Setting` implementation dedicated for functionsArray.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, type: cern.accsoft.commons.value.Type): ...
    def clone(self) -> 'FunctionsArraySetting':
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.clone`
            Returns a deep copy of this Setting.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.clone` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.clone`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                a deep copy of this Setting
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def getCorrectionValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue`
            Returns the correction value of this setting. If the setting holds no correction value (correction is not defined) the
            value returned depends on its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.getCorrectionValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getTargetValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getTargetValue`
            Returns the target value of this setting. If the setting holds no target value (target is not defined) the value
            returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getTargetValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.getTargetValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getValue`
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two value is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def setCorrectionValue(self, immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> None:
        """
            Sets the correction functions of this Setting. The current correction functions are discarded and replaced by new ones
            based on the given discreteFunction.
        
            Parameters:
                discreteFunctionsArray (cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray): the possibly :code:`null` new value of the correction value
        
        
        """
        ...
    def setTargetValue(self, immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> None:
        """
            Sets the target functions of this Setting. The current target functions are discarded and replaced by new ones based on
            the given discreteFunction.
        
            Parameters:
                discreteFunctionsArray (cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray): the possibly :code:`null` new value of the target value
        
        
        """
        ...

class IncorporationRequestImpl(TrimRequestImpl, cern.lsa.domain.settings.IncorporationRequest):
    """
    public class IncorporationRequestImpl extends :class:`~cern.lsa.domain.settings.spi.TrimRequestImpl` implements :class:`~cern.lsa.domain.settings.IncorporationRequest`
    
        Default implementation of :class:`~cern.lsa.domain.settings.IncorporationRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    INCORPORATION_SETTINGS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` INCORPORATION_SETTINGS
    
        Attribute name for :meth:`~cern.lsa.domain.settings.spi.IncorporationRequestImpl.getIncorporationSettings`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]], map2: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getIncorporationSettings(self) -> java.util.Set[cern.lsa.domain.settings.IncorporationSetting]: ...
    def shouldIncorporate(self, parameter: cern.lsa.domain.settings.Parameter) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.IncorporationRequest.shouldIncorporate`
            Since in one incorporation request it is possible to mix parameter settings to trim and parameter settings to
            incorporate this method checks whether for specified parameter the setting should be incorporated.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.IncorporationRequest.shouldIncorporate`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.IncorporationRequest`
        
            Returns:
                :code:`true` if for specified parameter the settings should be incorporated, :code:`false` if the settings should be
                trimmed
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.TrimRequestImpl.toString`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.TrimRequestImpl`
        
        
        """
        ...

class RevertTrimRequestImpl(TrimRequestImpl, cern.lsa.domain.settings.RevertTrimRequest):
    """
    public class RevertTrimRequestImpl extends :class:`~cern.lsa.domain.settings.spi.TrimRequestImpl` implements :class:`~cern.lsa.domain.settings.RevertTrimRequest`
    
        Default implementation of :class:`~cern.lsa.domain.settings.RevertTrimRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    TRIM_HEADER: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TRIM_HEADER
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    BEAM_PROCESSES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` BEAM_PROCESSES
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]], map2: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getBeamProcesses(self) -> java.util.Set[cern.lsa.domain.settings.BeamProcess]: ...
    def getTrimHeader(self) -> cern.lsa.domain.settings.TrimHeader:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.RevertTrimRequest.getTrimHeader`
            Trim to be reverted determining moment in time - see :meth:`~cern.lsa.domain.settings.TrimHeader.getCreatedDate`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.RevertTrimRequest.getTrimHeader`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.RevertTrimRequest`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.TrimRequestImpl.toString`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.TrimRequestImpl`
        
        
        """
        ...

class ScalarSetting(AbstractSetting, java.io.Serializable, java.lang.Cloneable):
    """
    public class ScalarSetting extends :class:`~cern.lsa.domain.settings.spi.AbstractSetting` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Represents a setting which is a value of a parameter for a given context. The context holds two values : a target and a
        correction.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, type: cern.accsoft.commons.value.Type): ...
    def clone(self) -> 'ScalarSetting':
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.clone`
            Returns a deep copy of this Setting.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.clone` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.clone`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                a deep copy of this Setting
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def getCorrectionValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue`
            Returns the correction value of this setting. If the setting holds no correction value (correction is not defined) the
            value returned depends on its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.getCorrectionValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getTargetValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getTargetValue`
            Returns the target value of this setting. If the setting holds no target value (target is not defined) the value
            returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getTargetValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.AbstractSetting.getTargetValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.AbstractSetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getValue`
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two value is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def setCorrectionValue(self, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None:
        """
            Sets the correction value of this Setting. The current correction value is discarded and replaced by new ones based on
            the given scalar value.
        
            Parameters:
                scalar (cern.accsoft.commons.value.ImmutableScalar): the possibly null new value of the correction value
        
        
        """
        ...
    def setTargetValue(self, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None:
        """
            Sets the target value of this Setting. The current target value is discarded and replaced by new ones based on the given
            scalar value.
        
            Parameters:
                scalar (cern.accsoft.commons.value.ImmutableScalar): the possibly null new value of the target value
        
        
        """
        ...

class SettingsGenerationRequestImpl(TrimRequestImpl, cern.lsa.domain.settings.SettingsGenerationRequest):
    """
    public class SettingsGenerationRequestImpl extends :class:`~cern.lsa.domain.settings.spi.TrimRequestImpl` implements :class:`~cern.lsa.domain.settings.SettingsGenerationRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.SettingsGenerationRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    SUBCONTEXTS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SUBCONTEXTS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    GENERATE_ZERO_SETTINGS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` GENERATE_ZERO_SETTINGS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]], map2: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getSubContexts(self) -> java.util.Set[cern.lsa.domain.settings.SubContext]: ...
    def isGenerateZeroSettings(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SettingsGenerationRequest.isGenerateZeroSettings`
            Determines whether generation shall generate zero settings for the given parameters.
        
            The value of the ZERO setting depends on the parameter's value type and is generated using
            :meth:`~cern.lsa.domain.settings.SettingFactory.newInitialSetting` method. See JavaDoc of this method to find out what
            value is generated for each value type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingsGenerationRequest.isGenerateZeroSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingsGenerationRequest`
        
            Returns:
                :code:`true` to generate ZERO settings, :code:`false` to use the default generation procedure
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.TrimRequestImpl.toString`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.TrimRequestImpl`
        
        
        """
        ...

class SettingsRestoreStatusImpl(FailedParametersStatusImpl, cern.lsa.domain.settings.SettingsRestoreStatus, java.io.Serializable):
    """
    public class SettingsRestoreStatusImpl extends :class:`~cern.lsa.domain.settings.spi.FailedParametersStatusImpl` implements :class:`~cern.lsa.domain.settings.SettingsRestoreStatus`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :code:`ArchiveRestoreStatus` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, compositeContextSettings: cern.lsa.domain.settings.CompositeContextSettings): ...
    def getSettings(self) -> cern.lsa.domain.settings.CompositeContextSettings:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SettingsRestoreStatus.getSettings`
            Returns settings that were restored.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SettingsRestoreStatus.getSettings`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.SettingsRestoreStatus`
        
            Returns:
                settings that were restored
        
        
        """
        ...

class CorrectionMissingSetting(ScalarSetting):
    """
    public abstract class CorrectionMissingSetting extends :class:`~cern.lsa.domain.settings.spi.ScalarSetting`
    
        Base abstract class for settings which don't have correction part.
    
        Also see:
            :meth:`~serialized`
    """
    def getCorrectionValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue`
            Returns the correction value of this setting. If the setting holds no correction value (correction is not defined) the
            value returned depends on its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.ScalarSetting.getCorrectionValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.ScalarSetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getValue(self) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getValue`
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two value is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.ScalarSetting.getValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.ScalarSetting`
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def setCorrectionValue(self, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None:
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.spi.ScalarSetting.setCorrectionValue`
            Sets the correction value of this Setting. The current correction value is discarded and replaced by new ones based on
            the given scalar value.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.ScalarSetting.setCorrectionValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.ScalarSetting`
        
            Parameters:
                scalar (cern.accsoft.commons.value.ImmutableScalar): the possibly null new value of the correction value
        
        
        """
        ...
    def setValue(self, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None: ...

class IncorporationFunctionsArraySetting(FunctionsArraySetting):
    """
    public class IncorporationFunctionsArraySetting extends :class:`~cern.lsa.domain.settings.spi.FunctionsArraySetting`
    
        :class:`~cern.lsa.domain.settings.spi.FunctionsArraySetting` implementation for incorporation: it defines one single
        target and correction value to be incorporated for each function in a function array.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    def getCorrectionValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue`
            Returns the correction value of this setting. If the setting holds no correction value (correction is not defined) the
            value returned depends on its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getCorrectionValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.FunctionsArraySetting.getCorrectionValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.FunctionsArraySetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getTargetValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getTargetValue`
            Returns the target value of this setting. If the setting holds no target value (target is not defined) the value
            returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getTargetValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.FunctionsArraySetting.getTargetValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.FunctionsArraySetting`
        
            Returns:
                the value (target) of this setting. The value returned can be null.
        
        
        """
        ...
    def getValue(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Setting.getValue`
            Returns the value of this setting. The value is made of the sum of target value and the correction value. If one of the
            two value is not defined only the value defined will be used. If the setting holds no value (both target and correction
            are not defined) the value returned depends of its type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Setting.getValue` in interface :class:`~cern.lsa.domain.settings.Setting`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.FunctionsArraySetting.getValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.FunctionsArraySetting`
        
            Returns:
                the value (target+correction) of this setting. The value returned cannot be null.
        
        
        """
        ...
    def setCorrectionValue(self, immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> None:
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.spi.FunctionsArraySetting.setCorrectionValue`
            Sets the correction functions of this Setting. The current correction functions are discarded and replaced by new ones
            based on the given discreteFunction.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.FunctionsArraySetting.setCorrectionValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.FunctionsArraySetting`
        
            Parameters:
                discreteFunctionsArray (cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray): the possibly :code:`null` new value of the correction value
        
        
        """
        ...
    def setTargetValue(self, immutableDiscreteFunctionsArray: cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray) -> None:
        """
            Description copied from class: :meth:`~cern.lsa.domain.settings.spi.FunctionsArraySetting.setTargetValue`
            Sets the target functions of this Setting. The current target functions are discarded and replaced by new ones based on
            the given discreteFunction.
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.FunctionsArraySetting.setTargetValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.FunctionsArraySetting`
        
            Parameters:
                discreteFunctionsArray (cern.accsoft.commons.value.ImmutableDiscreteFunctionsArray): the possibly :code:`null` new value of the target value
        
        
        """
        ...

class PatternImpl(ContextImpl, cern.lsa.domain.settings.Pattern):
    """
    public class PatternImpl extends :class:`~cern.lsa.domain.settings.spi.ContextImpl` implements :class:`~cern.lsa.domain.settings.Pattern`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.Pattern` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getAttribute(self, string: str) -> cern.lsa.domain.commons.Attribute:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeAware.getAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeAware`
        
            Parameters:
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
        
            Returns:
                Retrieves the attribute with the given name, or null if such attribute name is not bound to this object.
        
        
        """
        ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.BeamProcess]: ...
    def getContextFamily(self) -> cern.lsa.domain.settings.ContextFamily:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.getContextFamily`
            Returns the context family this context belongs to. E.g. if the context is a beam process and in addition it is a
            :code:`StandAloneBeamProcess` the method returns :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.getContextFamily` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Returns:
                context family that this context belongs to
        
        
        """
        ...
    def getDrivableBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.DrivableBeamProcess]: ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def isMultiplexed(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.isMultiplexed`
            Indicates whether this context is multiplexed or not. Apart of special, dedicated contexts that are non-multiplexed, all
            the other contexts are multiplexed.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.isMultiplexed` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.ContextImpl.isMultiplexed`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.ContextImpl`
        
            Returns:
                :code:`true` if context is multiplexed, :code:`false` otherwise
        
        
        """
        ...
    def isResident(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.StandAloneContext.isResident`
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
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContext.isResident`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContext`
        
            Returns:
                :code:`true` if this context is **resident**, :code:`false` otherwise
        
        
        """
        ...
    def setMultiplexed(self, boolean: bool) -> None:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.ContextImpl.setMultiplexed`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.ContextImpl`
        
        
        """
        ...
    def setResident(self, boolean: bool) -> None: ...
    def setSubContexts(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.SubContext], typing.Sequence[cern.lsa.domain.settings.SubContext]]) -> None: ...

class SubContextImpl(ContextImpl, cern.lsa.domain.settings.SubContext):
    """
    public abstract class SubContextImpl extends :class:`~cern.lsa.domain.settings.spi.ContextImpl` implements :class:`~cern.lsa.domain.settings.SubContext`
    
        Implements a sub context.
    
        Also see:
            :class:`~cern.lsa.domain.settings.SubContext`, :meth:`~serialized`
    """
    def getStartTime(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.SubContext.getStartTime`
            Returns the start time of this context in its parent context. The unit of the time is the same as the unit of context
            length returned by :meth:`~cern.lsa.domain.settings.Context.getLength` method.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.SubContext.getStartTime` in interface :class:`~cern.lsa.domain.settings.SubContext`
        
            Returns:
                the start time of this context
        
        
        """
        ...
    def getUser(self) -> str:
        """
        
            Returns:
                user assigned to this context
        
        
        """
        ...
    def setStartTime(self, int: int) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.SubContextImpl.getStartTime`
        
        
        """
        ...
    def setUser(self, string: str) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.SubContextImpl.getUser`
        
        
        """
        ...

class Array2DSetting(CorrectionMissingSetting):
    """
    public class Array2DSetting extends :class:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting`
    
        A :class:`~cern.lsa.domain.settings.Setting` implementation dedicated for arrays 2D. The setting keeps only target
        (correction is meaningless).
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, type: cern.accsoft.commons.value.Type): ...
    def setValue(self, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None:
        """
            Sets the value of this Setting. The current value is discarded and replaced by new ones based on the given array2d.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting.setValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting`
        
            Parameters:
                value (cern.accsoft.commons.value.ImmutableScalar): the possibly null new scalarArray2d value of this setting
        
        
        """
        ...

class ArraySetting(CorrectionMissingSetting):
    """
    public class ArraySetting extends :class:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting`
    
        A :class:`~cern.lsa.domain.settings.Setting` implementation dedicated for single dimension arrays. The setting keeps
        only target (correction is meaningless).
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, type: cern.accsoft.commons.value.Type): ...
    def setValue(self, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None:
        """
            Sets the value of this Setting. The current value is discarded and replaced by new ones based on the given array.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting.setValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting`
        
            Parameters:
                value (cern.accsoft.commons.value.ImmutableScalar): the (possibly null) new scalarArray value of this setting
        
        
        """
        ...

class BeamProcessImpl(SubContextImpl, cern.lsa.domain.settings.BeamProcess):
    """
    public class BeamProcessImpl extends :class:`~cern.lsa.domain.settings.spi.SubContextImpl` implements :class:`~cern.lsa.domain.settings.BeamProcess`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.BeamProcess` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, beamProcessImpl: 'BeamProcessImpl'): ...
    @typing.overload
    def __init__(self, string: str): ...
    def getCategory(self) -> cern.lsa.domain.settings.type.BeamProcessTypeCategory:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.BeamProcess.getCategory`
            Returns the category of this beam process.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcess.getCategory` in interface :class:`~cern.lsa.domain.settings.BeamProcess`
        
            Returns:
                the category of this beam process
        
        
        """
        ...
    def getContextFamily(self) -> cern.lsa.domain.settings.ContextFamily:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.getContextFamily`
            Returns the context family this context belongs to. E.g. if the context is a beam process and in addition it is a
            :code:`StandAloneBeamProcess` the method returns :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.getContextFamily` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Returns:
                context family that this context belongs to
        
        
        """
        ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.BeamProcess.getParticleTransfer`
            Returns the name of the particle transfer that this beam process has been created for.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcess.getParticleTransfer`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.BeamProcess`
        
            Returns:
                the name of the particle transfer this beam process belongs to
        
        
        """
        ...
    def getPurpose(self) -> cern.lsa.domain.settings.type.BeamProcessPurpose:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.BeamProcess.getPurpose`
            Returns the purpose of this beam process.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.BeamProcess.getPurpose` in interface :class:`~cern.lsa.domain.settings.BeamProcess`
        
            Returns:
                the purpose of this beam process
        
        
        """
        ...
    def setCategory(self, beamProcessTypeCategory: cern.lsa.domain.settings.type.BeamProcessTypeCategory) -> None: ...
    def setParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> None: ...
    def setPurpose(self, beamProcessPurpose: cern.lsa.domain.settings.type.BeamProcessPurpose) -> None: ...

class BeamProductionChainImpl(SubContextImpl, cern.lsa.domain.settings.BeamProductionChain):
    """
    public class BeamProductionChainImpl extends :class:`~cern.lsa.domain.settings.spi.SubContextImpl` implements :class:`~cern.lsa.domain.settings.BeamProductionChain`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.BeamProductionChain` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, beamProductionChainImpl: 'BeamProductionChainImpl'): ...
    @typing.overload
    def __init__(self, string: str): ...
    def getBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.DrivableBeamProcess]: ...
    def getContextFamily(self) -> cern.lsa.domain.settings.ContextFamily:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.getContextFamily`
            Returns the context family this context belongs to. E.g. if the context is a beam process and in addition it is a
            :code:`StandAloneBeamProcess` the method returns :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.getContextFamily` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Returns:
                context family that this context belongs to
        
        
        """
        ...
    def setBeamProcesses(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.DrivableBeamProcess], typing.Sequence[cern.lsa.domain.settings.DrivableBeamProcess]]) -> None: ...

class BooleanSetting(CorrectionMissingSetting):
    """
    public class BooleanSetting extends :class:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting`
    
        Represents a setting which is a value of a parameter for a given context. This setting is a boolean and there is only
        one single value (only target)
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def setValue(self, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None:
        """
            Sets the value of this Setting. The current value is discarded and replaced by the new one.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting.setValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting`
        
            Parameters:
                value (cern.accsoft.commons.value.ImmutableScalar): the possibly null new value of the target value
        
        
        """
        ...

class CycleImpl(SubContextImpl, cern.lsa.domain.settings.Cycle):
    """
    public class CycleImpl extends :class:`~cern.lsa.domain.settings.spi.SubContextImpl` implements :class:`~cern.lsa.domain.settings.Cycle`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.Cycle` and
        :class:`~cern.lsa.domain.settings.StandAloneCycle` interfaces.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, cycleImpl: 'CycleImpl'): ...
    @typing.overload
    def __init__(self, string: str): ...
    def getContextFamily(self) -> cern.lsa.domain.settings.ContextFamily:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.getContextFamily`
            Returns the context family this context belongs to. E.g. if the context is a beam process and in addition it is a
            :code:`StandAloneBeamProcess` the method returns :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.getContextFamily` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Returns:
                context family that this context belongs to
        
        
        """
        ...

class StringSetting(CorrectionMissingSetting):
    """
    public class StringSetting extends :class:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting`
    
        Represents setting of type :code:`Type.STRING` or :code:`Type.ENUM`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, type: cern.accsoft.commons.value.Type): ...
    def setValue(self, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None:
        """
            Sets the value of this Setting. The current value is discarded and replaced by the new one.
        
            If the setting keeps :code:`Type.ENUM` value and the given value is not of type enum (but e.g. STRING or INT), the
            method converts it to the corresponding enum value using :code:`EnumType.valueOf(long)` or
            :code:`EnumType.valueOf(String)` method.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting.setValue`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.CorrectionMissingSetting`
        
            Parameters:
                value (cern.accsoft.commons.value.ImmutableScalar): the possibly null new value of the target value
        
        
        """
        ...

class StandAloneBeamProcessImpl(BeamProcessImpl, cern.lsa.domain.settings.StandAloneBeamProcess, cern.lsa.domain.commons.AttributeWritableAware):
    """
    public class StandAloneBeamProcessImpl extends :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` implements :class:`~cern.lsa.domain.settings.StandAloneBeamProcess`, :class:`~cern.lsa.domain.commons.AttributeWritableAware`
    
        Implementation of a stand alone beam process.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, standAloneBeamProcessImpl: 'StandAloneBeamProcessImpl'): ...
    @typing.overload
    def __init__(self, string: str): ...
    def addAttribute(self, attribute: cern.lsa.domain.commons.Attribute) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.commons.AttributeWritableAware.addAttribute`
            Adds the given attribute to the set of attributes already assigned to this object. If an attribute with the same
            :class:`~cern.lsa.domain.commons.AttributeDefinition` has been already assigned to this entity, it is overridden with
            the given attribute.
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeWritableAware.addAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeWritableAware`
        
            Parameters:
                attribute (:class:`~cern.lsa.domain.commons.Attribute`): attribute to be added.
        
        
        """
        ...
    def getActualBeamProcessInfo(self) -> cern.lsa.domain.settings.ActualBeamProcessInfo:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.StandAloneBeamProcess.getActualBeamProcessInfo`
            If the given BeamProcess is actual, this information contains all actual information like source point and a reference
            to the source BP
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneBeamProcess.getActualBeamProcessInfo`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneBeamProcess`
        
            Returns:
                actual information or null, if the BP is not actual
        
        
        """
        ...
    def getAttribute(self, string: str) -> cern.lsa.domain.commons.Attribute:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeAware.getAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeAware`
        
            Parameters:
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
        
            Returns:
                Retrieves the attribute with the given name, or null if such attribute name is not bound to this object.
        
        
        """
        ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.BeamProcess]: ...
    def getContextFamily(self) -> cern.lsa.domain.settings.ContextFamily:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.getContextFamily`
            Returns the context family this context belongs to. E.g. if the context is a beam process and in addition it is a
            :code:`StandAloneBeamProcess` the method returns :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.getContextFamily` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.BeamProcessImpl.getContextFamily`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl`
        
            Returns:
                context family that this context belongs to
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def isActual(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.StandAloneBeamProcess.isActual`
            Marks, if a specific BeamProcess is actual
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneBeamProcess.isActual`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneBeamProcess`
        
            Returns:
                true, if it is an actual BeamProcess
        
        
        """
        ...
    def isResident(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.StandAloneContext.isResident`
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
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContext.isResident`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContext`
        
            Returns:
                :code:`true` if this context is **resident**, :code:`false` otherwise
        
        
        """
        ...
    def setActualBeamProcessInfo(self, actualBeamProcessInfo: cern.lsa.domain.settings.ActualBeamProcessInfo) -> None: ...
    def setAttributes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.Attribute], typing.Sequence[cern.lsa.domain.commons.Attribute]]) -> None: ...
    def setResident(self, boolean: bool) -> None: ...

class StandAloneCycleImpl(CycleImpl, cern.lsa.domain.settings.StandAloneCycle, cern.lsa.domain.commons.AttributeWritableAware):
    """
    public class StandAloneCycleImpl extends :class:`~cern.lsa.domain.settings.spi.CycleImpl` implements :class:`~cern.lsa.domain.settings.StandAloneCycle`, :class:`~cern.lsa.domain.commons.AttributeWritableAware`
    
        Implementation of a stand alone cycle.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, standAloneCycleImpl: 'StandAloneCycleImpl'): ...
    @typing.overload
    def __init__(self, string: str): ...
    def addAttribute(self, attribute: cern.lsa.domain.commons.Attribute) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.commons.AttributeWritableAware.addAttribute`
            Adds the given attribute to the set of attributes already assigned to this object. If an attribute with the same
            :class:`~cern.lsa.domain.commons.AttributeDefinition` has been already assigned to this entity, it is overridden with
            the given attribute.
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeWritableAware.addAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeWritableAware`
        
            Parameters:
                attribute (:class:`~cern.lsa.domain.commons.Attribute`): attribute to be added.
        
        
        """
        ...
    def clearIntersections(self) -> None:
        """
            Method, that allows clearing the intersections at runtime. Temporary method, necessary e.g. for tests with flexible
            length.
        
        """
        ...
    def getAttribute(self, string: str) -> cern.lsa.domain.commons.Attribute:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeAware.getAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeAware`
        
            Parameters:
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
        
            Returns:
                Retrieves the attribute with the given name, or null if such attribute name is not bound to this object.
        
        
        """
        ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getBeamProcesses(self) -> java.util.List[cern.lsa.domain.settings.BeamProcess]: ...
    def getContextFamily(self) -> cern.lsa.domain.settings.ContextFamily:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.Context.getContextFamily`
            Returns the context family this context belongs to. E.g. if the context is a beam process and in addition it is a
            :code:`StandAloneBeamProcess` the method returns :meth:`~cern.lsa.domain.settings.ContextFamily.BEAMPROCESS`.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Context.getContextFamily` in interface :class:`~cern.lsa.domain.settings.Context`
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.CycleImpl.getContextFamily`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.CycleImpl`
        
            Returns:
                context family that this context belongs to
        
        
        """
        ...
    def getIntersections(self) -> cern.lsa.domain.settings.CycleIntersections:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneCycle.getIntersections`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneCycle`
        
            Returns:
                intersections
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def isResident(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.StandAloneContext.isResident`
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
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.StandAloneContext.isResident`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.StandAloneContext`
        
            Returns:
                :code:`true` if this context is **resident**, :code:`false` otherwise
        
        
        """
        ...
    def setAttributes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.Attribute], typing.Sequence[cern.lsa.domain.commons.Attribute]]) -> None: ...
    def setBeamProcesses(self, collection: typing.Union[java.util.Collection[BeamProcessImpl], typing.Sequence[BeamProcessImpl]]) -> None: ...
    def setResident(self, boolean: bool) -> None: ...
    def setStartTime(self, int: int) -> None:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.settings.spi.SubContextImpl.setStartTime`Â in
                classÂ :class:`~cern.lsa.domain.settings.spi.SubContextImpl`
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.SubContextImpl.getStartTime`
        
        
        """
        ...

class CycleIntersectionsImpl(cern.lsa.domain.settings.spi.AbstractContextIntersectionsImpl, cern.lsa.domain.settings.CycleIntersections, java.io.Serializable):
    """
    public class CycleIntersectionsImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.CycleIntersections`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...
    def getBeamProcesses(self) -> java.util.Set[cern.lsa.domain.settings.BeamProcess]: ...
    def getCycleName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.CycleIntersections.getCycleName`
            Returns the cycle name this intersection is for
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CycleIntersections.getCycleName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CycleIntersections`
        
            Returns:
                the cycle name this intersection is for
        
        
        """
        ...
    def getIntersectedBeamProcesses(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> java.util.Set[cern.lsa.domain.settings.BeamProcess]: ...
    def getIntersectedFunctionBeamProcess(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, double: float) -> cern.lsa.domain.settings.BeamProcessIntersection:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.CycleIntersections.getIntersectedFunctionBeamProcess`
            Return the beam process that intersects the given x-coordinate. The given xCoordinate must be relative to the CYCLE. If
            no beam process is defined at that xCoordinate, null is returned. If a beam process is defined at that xCoordinate, it
            is returned. Together with the beam process name the x-coordinate of the intersection relative to the beam process is
            returned. That x-coordinate is the one matching the given x-coordinate (relative to the CYCLE) but inside the beam
            process and relative to that beam process.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.CycleIntersections.getIntersectedFunctionBeamProcess`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.CycleIntersections`
        
            Parameters:
                particleTransfer (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): the particle transfer in which to consider the intersection
                xCoordinate (double): the xCoordinate at which to find the intersecting beam process
        
            Returns:
                the intersecting beam process together with the x-coordinate of the intersection or null
        
        
        """
        ...
    def getIntersectedFunctionBeamProcesses(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, double: float) -> java.util.List[cern.lsa.domain.settings.BeamProcessIntersection]: ...

class KnobImpl(cern.lsa.domain.settings.spi.ParameterDecorator, cern.lsa.domain.settings.Knob):
    """
    public class KnobImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.Knob`
    
        Default implementation of :class:`~cern.lsa.domain.settings.Knob`.
    
        Use the builder :class:`~cern.lsa.domain.settings.factory.KnobCreationBuilder` to create new knob instances.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, parameter: cern.lsa.domain.settings.Parameter, knobFactors: cern.lsa.domain.settings.KnobFactors): ...
    def getComponentNames(self) -> java.util.Set[str]: ...
    def getKnobFactors(self) -> cern.lsa.domain.settings.KnobFactors:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.Knob.getKnobFactors` in interface :class:`~cern.lsa.domain.settings.Knob`
        
            Returns:
                all the multiplication factors
        
        
        """
        ...
    def getOpticNames(self) -> java.util.Set[str]: ...
    def toString(self) -> str: ...

class ParameterBuilder:
    """
    public class ParameterBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def newBuilder(parameter: cern.lsa.domain.settings.Parameter) -> 'ParameterBuilder.ParameterBuilderSteps': ...
    @typing.overload
    @staticmethod
    def newBuilder() -> 'ParameterBuilder.SetIdParameterBuilder':
        """
        public static :class:`~cern.lsa.domain.settings.spi.ParameterBuilder.ParameterBuilderSteps` newBuilder (:class:`~cern.lsa.domain.settings.Parameter` parameter)
        
        
            Parameters:
                parameter (:class:`~cern.lsa.domain.settings.Parameter`): to modify
        
            Returns:
                builder that allows to change any property of parameter.
        
        
        """
        ...
    class BuildParameterBuilder:
        def build(self) -> cern.lsa.domain.settings.Parameter: ...
    class ParameterBuilderSteps(cern.lsa.domain.settings.spi.ParameterBuilder.SetIdParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetDeviceParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetParameterTypeParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetPropertyFieldParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetValueDescriptorParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetMultiplexedParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetTrimableParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetCriticalParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetDefaultHierarchyParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetBelongsToFunctionBeamProcessParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetReservedForOpExpertsParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetParameterGroupsParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetPropertySupportingPartialSetParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetLsaImplementationParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetMonitorableParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetWritableParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetReadableParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetValueTypeParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.BuildParameterBuilder, cern.lsa.domain.settings.spi.ParameterBuilder.SetCycleBoundParameterBuilder):
        def addParameterGroup(self, string: str) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def addParameterGroups(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def build(self) -> cern.lsa.domain.settings.Parameter: ...
        def setBelongsToFunctionBeamProcess(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setCritical(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setCycleBound(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        @typing.overload
        def setDefaultHierarchy(self) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        @typing.overload
        def setDefaultHierarchy(self, string: str) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setDevice(self, device: cern.lsa.domain.devices.Device) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setLsaImplementation(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setMonitorable(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setMultiplexed(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setParameterGroups(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setParameterName(self, string: str) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setParameterNameAndId(self, long: int, string: str) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setParameterType(self, parameterType: cern.lsa.domain.settings.ParameterType) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setPropertyField(self, propertyField: cern.lsa.domain.devices.type.PropertyField) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setReadable(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setReservedForOpExperts(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setSupportingPartialSet(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setTrimable(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setValueDescriptor(self, valueDescriptor: cern.accsoft.commons.value.ValueDescriptor) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setValueType(self, type: cern.accsoft.commons.value.Type) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def setWritable(self, boolean: bool) -> 'ParameterBuilder.ParameterBuilderSteps': ...
        def withNoGroups(self) -> 'ParameterBuilder.ParameterBuilderSteps': ...
    class SetBelongsToFunctionBeamProcessParameterBuilder:
        def setBelongsToFunctionBeamProcess(self, boolean: bool) -> 'ParameterBuilder.SetReadableParameterBuilder': ...
    class SetCriticalParameterBuilder:
        def setCritical(self, boolean: bool) -> 'ParameterBuilder.SetReservedForOpExpertsParameterBuilder': ...
    class SetCycleBoundParameterBuilder:
        def setCycleBound(self, boolean: bool) -> 'ParameterBuilder.SetTrimableParameterBuilder': ...
    class SetDefaultHierarchyParameterBuilder:
        @typing.overload
        def setDefaultHierarchy(self) -> 'ParameterBuilder.SetPropertySupportingPartialSetParameterBuilder': ...
        @typing.overload
        def setDefaultHierarchy(self, string: str) -> 'ParameterBuilder.SetPropertySupportingPartialSetParameterBuilder': ...
    class SetDeviceParameterBuilder:
        def setDevice(self, device: cern.lsa.domain.devices.Device) -> 'ParameterBuilder.SetParameterTypeParameterBuilder': ...
    class SetIdParameterBuilder:
        def setParameterName(self, string: str) -> 'ParameterBuilder.SetDeviceParameterBuilder': ...
        def setParameterNameAndId(self, long: int, string: str) -> 'ParameterBuilder.SetDeviceParameterBuilder': ...
    class SetLsaImplementationParameterBuilder:
        def setLsaImplementation(self, boolean: bool) -> 'ParameterBuilder.SetCriticalParameterBuilder': ...
    class SetMonitorableParameterBuilder:
        def setMonitorable(self, boolean: bool) -> 'ParameterBuilder.SetLsaImplementationParameterBuilder': ...
    class SetMultiplexedParameterBuilder:
        def setMultiplexed(self, boolean: bool) -> 'ParameterBuilder.SetCycleBoundParameterBuilder': ...
    class SetParameterGroupsParameterBuilder:
        def setParameterGroups(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'ParameterBuilder.BuildParameterBuilder': ...
        def withNoGroups(self) -> 'ParameterBuilder.BuildParameterBuilder': ...
    class SetParameterTypeParameterBuilder:
        def setParameterType(self, parameterType: cern.lsa.domain.settings.ParameterType) -> 'ParameterBuilder.SetPropertyFieldParameterBuilder': ...
    class SetPropertyFieldParameterBuilder:
        def setPropertyField(self, propertyField: cern.lsa.domain.devices.type.PropertyField) -> 'ParameterBuilder.SetValueTypeParameterBuilder': ...
    class SetPropertySupportingPartialSetParameterBuilder:
        def setSupportingPartialSet(self, boolean: bool) -> 'ParameterBuilder.SetParameterGroupsParameterBuilder': ...
    class SetReadableParameterBuilder:
        def setReadable(self, boolean: bool) -> 'ParameterBuilder.SetWritableParameterBuilder': ...
    class SetReservedForOpExpertsParameterBuilder:
        def setReservedForOpExperts(self, boolean: bool) -> 'ParameterBuilder.SetDefaultHierarchyParameterBuilder': ...
    class SetTrimableParameterBuilder:
        def setTrimable(self, boolean: bool) -> 'ParameterBuilder.SetBelongsToFunctionBeamProcessParameterBuilder': ...
    class SetValueDescriptorParameterBuilder:
        def setValueDescriptor(self, valueDescriptor: cern.accsoft.commons.value.ValueDescriptor) -> 'ParameterBuilder.SetMultiplexedParameterBuilder': ...
    class SetValueTypeParameterBuilder:
        def setValueType(self, type: cern.accsoft.commons.value.Type) -> 'ParameterBuilder.SetValueDescriptorParameterBuilder': ...
    class SetWritableParameterBuilder:
        def setWritable(self, boolean: bool) -> 'ParameterBuilder.SetMonitorableParameterBuilder': ...

class ParameterTypeBuilder:
    """
    public class ParameterTypeBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def newBuilder(parameterType: cern.lsa.domain.settings.ParameterType) -> 'ParameterTypeBuilder.ParameterTypeStepBuilder': ...
    @typing.overload
    @staticmethod
    def newBuilder() -> 'ParameterTypeBuilder.SetNameAndIdParameterTypeBuilder':
        """
        public static :class:`~cern.lsa.domain.settings.spi.ParameterTypeBuilder.ParameterTypeStepBuilder` newBuilder (:class:`~cern.lsa.domain.settings.ParameterType` parameterType)
        
        
        """
        ...
    class BuildParameterType:
        def build(self) -> cern.lsa.domain.settings.ParameterType: ...
    class ParameterTypeStepBuilder(cern.lsa.domain.settings.spi.ParameterTypeBuilder.SetNameAndIdParameterTypeBuilder, cern.lsa.domain.settings.spi.ParameterTypeBuilder.SetLinkRuleApplicableParameterTypeBuilder, cern.lsa.domain.settings.spi.ParameterTypeBuilder.SetParameterTypeCategoryBuilder, cern.lsa.domain.settings.spi.ParameterTypeBuilder.BuildParameterType):
        def build(self) -> cern.lsa.domain.settings.ParameterType: ...
        def setCategoryType(self, parameterTypeCategory: cern.lsa.domain.settings.ParameterTypeCategory) -> 'ParameterTypeBuilder.ParameterTypeStepBuilder': ...
        def setDefaultCategoryType(self) -> 'ParameterTypeBuilder.ParameterTypeStepBuilder': ...
        def setIdAndName(self, long: int, string: str) -> 'ParameterTypeBuilder.ParameterTypeStepBuilder': ...
        def setLinkRuleApplicable(self, boolean: bool) -> 'ParameterTypeBuilder.ParameterTypeStepBuilder': ...
        def setName(self, string: str) -> 'ParameterTypeBuilder.ParameterTypeStepBuilder': ...
    class SetLinkRuleApplicableParameterTypeBuilder:
        def setLinkRuleApplicable(self, boolean: bool) -> 'ParameterTypeBuilder.SetParameterTypeCategoryBuilder': ...
    class SetNameAndIdParameterTypeBuilder:
        def setIdAndName(self, long: int, string: str) -> 'ParameterTypeBuilder.SetLinkRuleApplicableParameterTypeBuilder': ...
        def setName(self, string: str) -> 'ParameterTypeBuilder.SetLinkRuleApplicableParameterTypeBuilder': ...
    class SetParameterTypeCategoryBuilder:
        def setCategoryType(self, parameterTypeCategory: cern.lsa.domain.settings.ParameterTypeCategory) -> 'ParameterTypeBuilder.BuildParameterType': ...
        def setDefaultCategoryType(self) -> 'ParameterTypeBuilder.BuildParameterType': ...

class AbstractContextIntersectionsImpl: ...

class ParameterDecorator: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings.spi")``.

    AbstractContextIntersectionsImpl: typing.Type[AbstractContextIntersectionsImpl]
    AbstractSetting: typing.Type[AbstractSetting]
    ActualBeamProcessInfoImpl: typing.Type[ActualBeamProcessInfoImpl]
    ArchiveImpl: typing.Type[ArchiveImpl]
    ArchiveVersionImpl: typing.Type[ArchiveVersionImpl]
    Array2DSetting: typing.Type[Array2DSetting]
    ArraySetting: typing.Type[ArraySetting]
    BeamProcessImpl: typing.Type[BeamProcessImpl]
    BeamProcessIncorporationRequestImpl: typing.Type[BeamProcessIncorporationRequestImpl]
    BeamProductionChainImpl: typing.Type[BeamProductionChainImpl]
    BooleanSetting: typing.Type[BooleanSetting]
    BoundedPolynomialSequenceSetting: typing.Type[BoundedPolynomialSequenceSetting]
    CompositeContextSettingsImpl: typing.Type[CompositeContextSettingsImpl]
    ContextBase: typing.Type[ContextBase]
    ContextImpl: typing.Type[ContextImpl]
    ContextSettingsImpl: typing.Type[ContextSettingsImpl]
    CopySettingsRequestImpl: typing.Type[CopySettingsRequestImpl]
    CorrectionMissingSetting: typing.Type[CorrectionMissingSetting]
    CycleBeamProcessIntersectionImpl: typing.Type[CycleBeamProcessIntersectionImpl]
    CycleImpl: typing.Type[CycleImpl]
    CycleIntersectionsImpl: typing.Type[CycleIntersectionsImpl]
    DevicePropertyParametersImpl: typing.Type[DevicePropertyParametersImpl]
    FailedParametersStatusImpl: typing.Type[FailedParametersStatusImpl]
    FunctionSetting: typing.Type[FunctionSetting]
    FunctionsArraySetting: typing.Type[FunctionsArraySetting]
    HyperCycleImpl: typing.Type[HyperCycleImpl]
    IncorporationFunctionsArraySetting: typing.Type[IncorporationFunctionsArraySetting]
    IncorporationRequestImpl: typing.Type[IncorporationRequestImpl]
    KnobFactorsBuilder: typing.Type[KnobFactorsBuilder]
    KnobFactorsImpl: typing.Type[KnobFactorsImpl]
    KnobImpl: typing.Type[KnobImpl]
    NotIncorporatedParametersImpl: typing.Type[NotIncorporatedParametersImpl]
    ParameterAttributesImpl: typing.Type[ParameterAttributesImpl]
    ParameterBuilder: typing.Type[ParameterBuilder]
    ParameterDecorator: typing.Type[ParameterDecorator]
    ParameterImpl: typing.Type[ParameterImpl]
    ParameterSettingsImpl: typing.Type[ParameterSettingsImpl]
    ParameterTreeNodeImpl: typing.Type[ParameterTreeNodeImpl]
    ParameterTreesRequestImpl: typing.Type[ParameterTreesRequestImpl]
    ParameterTypeBuilder: typing.Type[ParameterTypeBuilder]
    ParameterTypeGroupImpl: typing.Type[ParameterTypeGroupImpl]
    ParameterTypeImpl: typing.Type[ParameterTypeImpl]
    ParameterTypesRequestImpl: typing.Type[ParameterTypesRequestImpl]
    ParametersRequestImpl: typing.Type[ParametersRequestImpl]
    PatternImpl: typing.Type[PatternImpl]
    RevertTrimRequestImpl: typing.Type[RevertTrimRequestImpl]
    ScalarSetting: typing.Type[ScalarSetting]
    SettingComparisonParameterResultImpl: typing.Type[SettingComparisonParameterResultImpl]
    SettingComparisonRequestImpl: typing.Type[SettingComparisonRequestImpl]
    SettingComparisonResponseImpl: typing.Type[SettingComparisonResponseImpl]
    SettingComparisonResultImpl: typing.Type[SettingComparisonResultImpl]
    SettingsGenerationRequestImpl: typing.Type[SettingsGenerationRequestImpl]
    SettingsRestoreStatusImpl: typing.Type[SettingsRestoreStatusImpl]
    StandAloneBeamProcessImpl: typing.Type[StandAloneBeamProcessImpl]
    StandAloneContextCloneRequestImpl: typing.Type[StandAloneContextCloneRequestImpl]
    StandAloneContextCreationRequestImpl: typing.Type[StandAloneContextCreationRequestImpl]
    StandAloneCycleImpl: typing.Type[StandAloneCycleImpl]
    StringSetting: typing.Type[StringSetting]
    SubContextImpl: typing.Type[SubContextImpl]
    TrimHeaderImpl: typing.Type[TrimHeaderImpl]
    TrimRequestImpl: typing.Type[TrimRequestImpl]
    TrimResponseImpl: typing.Type[TrimResponseImpl]
    TrimResultImpl: typing.Type[TrimResultImpl]
    UserContextMappingImpl: typing.Type[UserContextMappingImpl]
    test: cern.lsa.domain.settings.spi.test.__module_protocol__
    type: cern.lsa.domain.settings.spi.type.__module_protocol__
    util: cern.lsa.domain.settings.spi.util.__module_protocol__
