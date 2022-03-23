import cern.accsoft.ccs.ccda.client.core
import cern.accsoft.ccs.ccda.client.hardware
import cern.accsoft.ccs.ccda.client.model.device
import cern.accsoft.ccs.ccm.client
import cern.accsoft.ccs.ccm.client.model
import cern.accsoft.ccs.ccm.client.model.enums
import cern.accsoft.ccs.ccm.client.service
import cern.accsoft.commons.domain
import cern.accsoft.commons.util
import cern.japc.value
import java.lang
import java.util
import typing



class AcceleratorInfo(cern.accsoft.commons.util.Named):
    """
    public final class :meth:`~src` extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.accsoft.commons.util.Named
    
        This class provides utility methods to handle AcceleratorInfo device information such as:
    
          - The accelerator.INFO device name.
          - The accelerator.INFO associated :code:`CernAccelerator`.
          - The accelerator.INFO associated lsaAccelerator name.
          - The accelerator.INFO associated ccdbAccelerator name.
          - The accelerator.INFO associated tgmMachine name.
          - The accelerator.INFO associated non Multiplexed Context name.
          - The accelerator.INFO associated lsaAccelerator name.
    
        More details can be found here: https://wikis.cern.ch/display/InCA/LsaContextMappingMonitor+marked+as+deprecated
    """
    def __init__(self, device: cern.accsoft.ccs.ccda.client.model.device.Device): ...
    @staticmethod
    def ccdbTolsaAccelerator(string: str) -> str: ...
    @staticmethod
    def getAcceleratorFromSystemProperty() -> cern.accsoft.commons.domain.CernAccelerator: ...
    @staticmethod
    def getAcceleratorInfoForCernAccelerator(cernAccelerator: cern.accsoft.commons.domain.CernAccelerator) -> 'AcceleratorInfo': ...
    def getCcdbAccelerator(self) -> str: ...
    @staticmethod
    def getCcdbAcceleratorForOpConfig(string: str) -> str: ...
    def getCernAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    @staticmethod
    def getCernAcceleratorForName(string: str) -> cern.accsoft.commons.domain.CernAccelerator: ...
    @staticmethod
    def getCernAcceleratorForOpConfig(string: str) -> cern.accsoft.commons.domain.CernAccelerator: ...
    @staticmethod
    def getCernAcceleratorForTgm(string: str) -> cern.accsoft.commons.domain.CernAccelerator: ...
    @staticmethod
    def getDefaultCernAccelerator() -> cern.accsoft.commons.domain.CernAccelerator: ...
    @staticmethod
    def getInfoDeviceForCernAccelerator(cernAccelerator: cern.accsoft.commons.domain.CernAccelerator) -> str: ...
    @staticmethod
    def getInfoDeviceForLsaAcceleratorName(string: str) -> str: ...
    def getLsaAccelerator(self) -> str: ...
    @staticmethod
    def getLsaAcceleratorForCernAccelerator(cernAccelerator: cern.accsoft.commons.domain.CernAccelerator) -> str: ...
    @staticmethod
    def getLsaAcceleratorForOpConfig(string: str) -> str: ...
    def getName(self) -> str: ...
    @staticmethod
    def getNonMultiplexContextNameForAccelerator(string: str) -> str: ...
    def getNonMultiplexedContext(self) -> str: ...
    @staticmethod
    def getOpConfig() -> str: ...
    def getOpConfigs(self) -> java.util.List[str]: ...
    def getTgmMachine(self) -> str: ...
    @staticmethod
    def getTgmMachineNameForOpConfig(string: str) -> str: ...
    @staticmethod
    def isCcdbAcceleratorName(string: str) -> bool: ...
    @staticmethod
    def isLsaAcceleratorName(string: str) -> bool: ...
    @staticmethod
    def isPseudoNonMultiplexedAccelerator(cernAccelerator: cern.accsoft.commons.domain.CernAccelerator) -> bool: ...
    @staticmethod
    def isTgmMachineNameForOpConfigExisting(string: str) -> bool: ...
    @staticmethod
    def lsaToCcdbAccelerator(string: str) -> str: ...
    def toString(self) -> str: ...
    @staticmethod
    def values() -> java.util.Collection['AcceleratorInfo']: ...

class CcdaAccess:
    """
    public final class :meth:`~src` extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Provide access to the default :code:`CcdaClient` Object used in this product for the :code:`Environment` specified by
        the "cern.cdda.environment" system property or :code:`Environment.PRO` if no system property is defined.
    """
    SYSPROP_CCDA_ENVIRONMENT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
        The :code:`"cern.cdda.environment"` system property used to select the :code:`CcdaClient` :code:`Environment`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def getCcdaClient() -> cern.accsoft.ccs.ccda.client.core.CcdaClient: ...
    @staticmethod
    def getDefaultCcdaEnvironment() -> cern.accsoft.ccs.ccda.client.core.Environment: ...
    @staticmethod
    def getEnvironmentFromSystemProperty() -> cern.accsoft.ccs.ccda.client.core.Environment: ...

class CcdaUtils:
    """
    public class :meth:`~src` extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    DEFAULT_VALUE_FIELD: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNDEFINED: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
        Default value when there is no CCS value defined.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_DIMENSION: typing.ClassVar[int] = ...
    """
    public static final int :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def calculateFormatPattern(simpleDescriptor: cern.japc.value.SimpleDescriptor) -> str: ...
    @staticmethod
    def createBooleanType(string: str, propertyFieldBooleanMeaning: cern.accsoft.ccs.ccda.client.model.device.PropertyFieldBooleanMeaning) -> cern.japc.value.BooleanType: ...
    @staticmethod
    def createEnumOrBooleanTypeName(device: cern.accsoft.ccs.ccda.client.model.device.Device, deviceClassProperty: cern.accsoft.ccs.ccda.client.model.device.DeviceClassProperty, propertyField: cern.accsoft.ccs.ccda.client.model.device.PropertyField) -> str: ...
    @staticmethod
    def createEnumType(string: str, valueType: cern.japc.value.ValueType, propertyField: cern.accsoft.ccs.ccda.client.model.device.PropertyField) -> cern.japc.value.EnumType: ...
    @staticmethod
    def getAcceleratorNames() -> java.util.Set[str]: ...
    @staticmethod
    def getColumnCount(propertyField: cern.accsoft.ccs.ccda.client.model.device.PropertyField) -> int: ...
    @staticmethod
    def getComputer(string: str) -> cern.accsoft.ccs.ccda.client.hardware.Computer: ...
    @staticmethod
    def getDevice(string: str) -> cern.accsoft.ccs.ccda.client.model.device.Device: ...
    @staticmethod
    def getDeviceAcceleratorName(string: str) -> str: ...
    @staticmethod
    def getDeviceClassForDevice(string: str) -> cern.accsoft.ccs.ccda.client.model.device.DeviceClass: ...
    @staticmethod
    def getDeviceClassNamesByAccelerator(string: str) -> java.util.Set[str]: ...
    @staticmethod
    def getDeviceClassNamesByAcceleratorAndFrontEnds(string: str, stringArray: typing.List[str]) -> java.util.Set[str]: ...
    @staticmethod
    def getDeviceClassNamesByFrontEnd(string: str) -> java.util.Set[str]: ...
    @staticmethod
    def getDeviceNamesByClassNameFrontEndsAndAccelerators(string: str, stringArray: typing.List[str], stringArray2: typing.List[str]) -> java.util.Set[str]: ...
    @staticmethod
    def getDeviceNamesByClassNamesAndAccelerators(stringArray: typing.List[str], stringArray2: typing.List[str]) -> java.util.Set[str]: ...
    @staticmethod
    def getDeviceVersion(string: str) -> str: ...
    @staticmethod
    def getFieldOfSimpleProperty(deviceClassProperty: cern.accsoft.ccs.ccda.client.model.device.DeviceClassProperty) -> cern.accsoft.ccs.ccda.client.model.device.PropertyField: ...
    @staticmethod
    def getFieldsForDeviceProperty(string: str, string2: str) -> java.util.Set[str]: ...
    @staticmethod
    def getFilterFieldsForDeviceProperty(string: str, string2: str) -> java.util.Set[str]: ...
    @staticmethod
    def getFilterFieldsForFesaDeviceProperty(string: str, string2: str) -> java.util.Set[str]: ...
    @staticmethod
    def getFrontEndNamesForAccelerator(string: str) -> java.util.Set[str]: ...
    @staticmethod
    def getPropertiesForDevice(string: str) -> java.util.Set[str]: ...
    @staticmethod
    def getRealColumnCount(propertyField: cern.accsoft.ccs.ccda.client.model.device.PropertyField) -> int: ...
    @staticmethod
    def getRealRowCount(propertyField: cern.accsoft.ccs.ccda.client.model.device.PropertyField) -> int: ...
    @staticmethod
    def getRowCount(propertyField: cern.accsoft.ccs.ccda.client.model.device.PropertyField) -> int: ...
    @staticmethod
    def isDeviceValid(string: str) -> bool: ...
    @staticmethod
    def isParameterValid(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isSimpleParameter(device: cern.accsoft.ccs.ccda.client.model.device.Device, deviceClassProperty: cern.accsoft.ccs.ccda.client.model.device.DeviceClassProperty) -> bool: ...
    @typing.overload
    @staticmethod
    def isSimpleParameter(device: cern.accsoft.ccs.ccda.client.model.device.Device, deviceClassProperty: cern.accsoft.ccs.ccda.client.model.device.DeviceClassProperty, boolean: bool) -> bool: ...
    @staticmethod
    def toStringArray(stringArray: typing.List[str]) -> typing.List[str]: ...

class CcmCcsAccess:
    """
    public final class :meth:`~src` extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Provide access to the default :code:`CcmConfigurationService` Object used in this product for the
        :code:`CCMServiceLocator.Environment` specified by the "cern.ccm.useccdb" system property or
        :code:`CCMServiceLocator.Environment.PRO` if no system property is defined.
    """
    SYSPROP_CCM_CCS_ENVIRONMENT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
        The :code:`"cern.ccm.useccdb"` system property used to select the CCDB server :code:`CCMServiceLocator.Environment`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def getCcmConfigurationService() -> cern.accsoft.ccs.ccm.client.service.CcmConfigurationService: ...
    @staticmethod
    def getDefaultCcdaEnvironment() -> cern.accsoft.ccs.ccm.client.CCMServiceLocator.Environment: ...
    @staticmethod
    def getEnvironmentFromSystemProperty() -> cern.accsoft.ccs.ccm.client.CCMServiceLocator.Environment: ...
    @staticmethod
    def isCcdbEnvironmentDev() -> bool: ...
    @staticmethod
    def isCcdbEnvironmentPro() -> bool: ...

class CcmCcsUtils:
    """
    public class :meth:`~src` extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    DEFAULT_INDENT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def dumpApplicWindow(applicWindow: cern.accsoft.ccs.ccm.client.model.ApplicWindow) -> str: ...
    @staticmethod
    def dumpApplicWindowList(list: java.util.List[cern.accsoft.ccs.ccm.client.model.ApplicWindow]) -> str: ...
    @staticmethod
    def dumpApplication(application: cern.accsoft.ccs.ccm.client.model.Application, string: str, boolean: bool) -> str: ...
    @typing.overload
    @staticmethod
    def dumpCcdbModel(identifiable: cern.accsoft.ccs.ccm.client.service.Identifiable) -> str: ...
    @typing.overload
    @staticmethod
    def dumpCcdbModel(identifiable: cern.accsoft.ccs.ccm.client.service.Identifiable, string: str, boolean: bool) -> str: ...
    @staticmethod
    def dumpConsoleMenu(consoleMenu: cern.accsoft.ccs.ccm.client.model.ConsoleMenu, string: str, boolean: bool) -> str: ...
    @staticmethod
    def dumpConsolemenuTree(string: str, consoleMenu: cern.accsoft.ccs.ccm.client.model.ConsoleMenu, stringBuilder: java.lang.StringBuilder) -> str: ...
    @staticmethod
    def dumpOpconfig(opConfig: cern.accsoft.ccs.ccm.client.model.OpConfig, string: str, boolean: bool) -> str: ...
    @staticmethod
    def dumpOsCommand(osName: cern.accsoft.ccs.ccm.client.model.enums.OsName, string: str) -> str: ...
    @staticmethod
    def dumpOsCommands(string: str, list: java.util.List[cern.accsoft.ccs.ccm.client.model.OsCommand]) -> str: ...
    @staticmethod
    def dumpSubstitutionEntity(substitutionEntity: cern.accsoft.ccs.ccm.client.model.SubstitutionEntity, string: str, boolean: bool) -> str: ...
    @staticmethod
    def dumpTool(tool: cern.accsoft.ccs.ccm.client.model.Tool, string: str, boolean: bool) -> str: ...
    @staticmethod
    def getAccelerator(string: str) -> cern.accsoft.ccs.ccm.client.model.Accelerator: ...
    @staticmethod
    def getAcceleratorNames() -> java.util.List[str]: ...
    @staticmethod
    def getApplicationById(long: int) -> cern.accsoft.ccs.ccm.client.model.Application: ...
    @staticmethod
    def getApplicationDependencies(application: cern.accsoft.ccs.ccm.client.model.Application) -> java.util.List[str]: ...
    @staticmethod
    def getApplications() -> java.util.List[cern.accsoft.ccs.ccm.client.model.Application]: ...
    @staticmethod
    def getApplicationsForOpConfig(string: str) -> java.util.List[cern.accsoft.ccs.ccm.client.model.Application]: ...
    @staticmethod
    def getConsoleMenuById(long: int) -> cern.accsoft.ccs.ccm.client.model.ConsoleMenu: ...
    @staticmethod
    def getDefaultOpConfig() -> str: ...
    @staticmethod
    def getDeviceClasses() -> java.util.List[cern.accsoft.ccs.ccm.client.model.DeviceClass]: ...
    @staticmethod
    def getMatchingNamedResponsibles(string: str) -> java.util.List[cern.accsoft.commons.util.Named]: ...
    @staticmethod
    def getNamedResponsibles(set: java.util.Set[str]) -> java.util.List[cern.accsoft.commons.util.Named]: ...
    @staticmethod
    def getOpConfig(string: str) -> cern.accsoft.ccs.ccm.client.model.OpConfig: ...
    @staticmethod
    def getOpConfigNames() -> java.util.List[str]: ...
    @staticmethod
    def getOpConfigs() -> java.util.List[cern.accsoft.ccs.ccm.client.model.OpConfig]: ...
    @staticmethod
    def getRbacRoleForOpConfigName(string: str) -> str: ...
    @staticmethod
    def getRbacRoles() -> java.util.List[str]: ...
    @staticmethod
    def getRootConsoleMenuForOpConfig(string: str) -> cern.accsoft.ccs.ccm.client.model.ConsoleMenu: ...
    @staticmethod
    def getSubstitutionDependencies(substitutionEntity: cern.accsoft.ccs.ccm.client.model.SubstitutionEntity) -> java.util.List[str]: ...
    @staticmethod
    def getSubstitutionEntities() -> java.util.List[cern.accsoft.ccs.ccm.client.model.SubstitutionEntity]: ...
    @staticmethod
    def getSubstitutionEntityById(long: int) -> cern.accsoft.ccs.ccm.client.model.SubstitutionEntity: ...
    @staticmethod
    def getToolById(long: int) -> cern.accsoft.ccs.ccm.client.model.Tool: ...
    @staticmethod
    def getToolDependencies(tool: cern.accsoft.ccs.ccm.client.model.Tool) -> java.util.List[str]: ...
    @staticmethod
    def getTools() -> java.util.List[cern.accsoft.ccs.ccm.client.model.Tool]: ...
    @staticmethod
    def isValidOpConfig(string: str) -> bool: ...

class ConvertCcsToJapcMeaning:
    """
    public final class :meth:`~src` extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Convert CCS :code:`FieldValueMeaning` to a JAPC :code:`SimpleValueStandardMeaning`.
    """
    @staticmethod
    def ccsToJapcMeaning(fieldValueMeaning: cern.accsoft.ccs.ccda.client.model.device.FieldValueMeaning) -> cern.japc.value.SimpleValueStandardMeaning: ...

class ConvertCcsToJapcValueType:
    """
    public final class :meth:`~src` extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Convert CCS type and primitive data type pair Strings to proper JAPC :code:`ValueType`.
    
    
        Please see https://issues.cern.ch/browse/CCS-9354 for more details.
    """
    SCALAR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ARRAY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ARRAY2D: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ENUM: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ENUM_ARRAY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ENUM_ARRAY2D: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    BIT_ENUM: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    BIT_ENUM_ARRAY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    BIT_ENUM_ARRAY2D: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DIAG_FWK_TOPIC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DIAG_CUSTOM_TOPIC: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    NOTIFICATION_UPDATE_ENUM: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CUSTOM_TYPE_SCALAR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    FAULT_SEVERITY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CONST_UINT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` :meth:`~src`
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def ccsToJapcType(string: str, primitiveDataType: cern.accsoft.ccs.ccda.client.model.device.PrimitiveDataType) -> cern.japc.value.ValueType: ...

class ConvertPrimitiveDataTypeTypeToEnumTypeBitSize:
    """
    public final class :meth:`~src` extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Convert the given :code:`ValueType` to a :code:`EnumTypeBitSize`
    """
    @staticmethod
    def primitiveDataTypeToEnumTypeBitSize(primitiveDataType: cern.accsoft.ccs.ccda.client.model.device.PrimitiveDataType) -> cern.japc.value.EnumTypeBitSize: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.ccs")``.

    AcceleratorInfo: typing.Type[AcceleratorInfo]
    CcdaAccess: typing.Type[CcdaAccess]
    CcdaUtils: typing.Type[CcdaUtils]
    CcmCcsAccess: typing.Type[CcmCcsAccess]
    CcmCcsUtils: typing.Type[CcmCcsUtils]
    ConvertCcsToJapcMeaning: typing.Type[ConvertCcsToJapcMeaning]
    ConvertCcsToJapcValueType: typing.Type[ConvertCcsToJapcValueType]
    ConvertPrimitiveDataTypeTypeToEnumTypeBitSize: typing.Type[ConvertPrimitiveDataTypeTypeToEnumTypeBitSize]
