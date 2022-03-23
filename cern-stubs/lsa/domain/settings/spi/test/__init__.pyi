import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.domain.zones
import cern.accsoft.commons.util.value
import cern.accsoft.commons.value
import cern.lsa.domain.devices
import cern.lsa.domain.exploitation
import cern.lsa.domain.exploitation.spi.results
import cern.lsa.domain.settings
import cern.lsa.domain.settings.factory
import cern.lsa.domain.settings.spi
import cern.lsa.domain.settings.type
import java.lang
import java.util
import typing



class DriveResultsTestUtils:
    """
    public class DriveResultsTestUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class to help creation of the JAPC, LSA drive results.
    """
    def __init__(self): ...
    @staticmethod
    def countJapcParameterDriveResults(driveResult: cern.lsa.domain.exploitation.DriveResult) -> int: ...
    @staticmethod
    def countSuccessfulJapcParameterDriveResults(driveResult: cern.lsa.domain.exploitation.DriveResult) -> int: ...
    @staticmethod
    def countSuccessfulLsaParameterDriveResults(driveResult: cern.lsa.domain.exploitation.DriveResult) -> int: ...
    @typing.overload
    @staticmethod
    def createLsaParameterDriveResult() -> cern.lsa.domain.exploitation.spi.results.LsaParameterDriveResult:
        """
        public static :class:`~cern.lsa.domain.exploitation.spi.results.LsaParameterDriveResult` createLsaParameterDriveResult (:class:`~cern.lsa.domain.settings.Parameter` parameter)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createLsaParameterDriveResult(parameter: cern.lsa.domain.settings.Parameter) -> cern.lsa.domain.exploitation.spi.results.LsaParameterDriveResult: ...
    @staticmethod
    def createLsaParameterDriveResults(int: int) -> java.util.Set[cern.lsa.domain.exploitation.spi.results.LsaParameterDriveResult]: ...
    @typing.overload
    @staticmethod
    def createSuccessfulContextDriveResult(drivableContext: cern.lsa.domain.settings.DrivableContext, int: int, int2: int) -> cern.lsa.domain.exploitation.spi.results.ContextDriveResult: ...
    @typing.overload
    @staticmethod
    def createSuccessfulContextDriveResult(int: int, int2: int) -> cern.lsa.domain.exploitation.spi.results.ContextDriveResult:
        """
        public static :class:`~cern.lsa.domain.exploitation.spi.results.ContextDriveResult` createSuccessfulContextDriveResult (:class:`~cern.lsa.domain.settings.DrivableContext` context, int numberOfLsaParameterDriveResults, int numberOfJapcParameterDriveResults)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createSuccessfulJapcParameterDriveResult() -> cern.lsa.domain.exploitation.spi.results.JapcParameterDriveResult:
        """
        public static :class:`~cern.lsa.domain.exploitation.spi.results.JapcParameterDriveResult` createSuccessfulJapcParameterDriveResult (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` japcParameterName)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createSuccessfulJapcParameterDriveResult(string: str) -> cern.lsa.domain.exploitation.spi.results.JapcParameterDriveResult: ...
    @staticmethod
    def createSuccessfulJapcParameterDriveResults(int: int) -> java.util.Set[cern.lsa.domain.exploitation.spi.results.JapcParameterDriveResult]: ...

class SettingsDomainUtils:
    """
    public abstract class SettingsDomainUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class with test values and method helping create test/mock objects. The class is here rather than in src/test to
        be visible from other products (not just lsa-domain).
    """
    BP_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int BP_LENGTH
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CONTEXT_CATEGORY_OPERATIONAL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CONTEXT_CATEGORY_OPERATIONAL
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    FUNC_0_0: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_0_0
    
    
    """
    FUNC_0_1: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_0_1
    
    
    """
    FUNC_1_0: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_1_0
    
    
    """
    FUNC_1_1: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_1_1
    
    
    """
    FUNC_1_2: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_1_2
    
    
    """
    FUNC_2_1: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_2_1
    
    
    """
    FUNC_2_2: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_2_2
    
    
    """
    FUNC_2_3: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_2_3
    
    
    """
    FUNC_3_3: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_3_3
    
    
    """
    FUNC_4_4: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_4_4
    
    
    """
    FUNC_5_5: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_5_5
    
    
    """
    FUNC_6_6: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_6_6
    
    
    """
    FUNC_0_1_0: typing.ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableDiscreteFunction FUNC_0_1_0
    
    
    """
    SCALAR_0: typing.ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableScalar SCALAR_0
    
    
    """
    SCALAR_1: typing.ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableScalar SCALAR_1
    
    
    """
    SCALAR_2: typing.ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableScalar SCALAR_2
    
    
    """
    SCALAR_3: typing.ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableScalar SCALAR_3
    
    
    """
    SCALAR_4: typing.ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableScalar SCALAR_4
    
    
    """
    SCALAR_5: typing.ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    """
    public static final cern.accsoft.commons.value.ImmutableScalar SCALAR_5
    
    
    """
    PARAMETER_TYPE_FUNCTION: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.test.SettingsDomainUtils.ParameterTypeStub` PARAMETER_TYPE_FUNCTION
    
    
    """
    PARAMETER_TYPE_FUNCTION_LIST: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.test.SettingsDomainUtils.ParameterTypeStub` PARAMETER_TYPE_FUNCTION_LIST
    
    
    """
    PARAMETER_TYPE_FUNCTIONS_ARRAY: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.test.SettingsDomainUtils.ParameterTypeStub` PARAMETER_TYPE_FUNCTIONS_ARRAY
    
    
    """
    PARAMETER_TYPE_DOUBLE: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.test.SettingsDomainUtils.ParameterTypeStub` PARAMETER_TYPE_DOUBLE
    
    
    """
    PARAMETER_TYPE_DOUBLE_ARRAY: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.test.SettingsDomainUtils.ParameterTypeStub` PARAMETER_TYPE_DOUBLE_ARRAY
    
    
    """
    PARAMETER_TYPE_SHORT_ARRAY: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.test.SettingsDomainUtils.ParameterTypeStub` PARAMETER_TYPE_SHORT_ARRAY
    
    
    """
    PARAMETER_TYPE_NON_MUX: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.test.SettingsDomainUtils.ParameterTypeStub` PARAMETER_TYPE_NON_MUX
    
    
    """
    PARAMETER_FUNCTION: typing.ClassVar[cern.lsa.domain.settings.Parameter] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.Parameter` PARAMETER_FUNCTION
    
    
    """
    PARAMETER_DOUBLE: typing.ClassVar[cern.lsa.domain.settings.Parameter] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.Parameter` PARAMETER_DOUBLE
    
    
    """
    PARAMETER_DOUBLE_ARRAY: typing.ClassVar[cern.lsa.domain.settings.Parameter] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.Parameter` PARAMETER_DOUBLE_ARRAY
    
    
    """
    PARAMETER_DOUBLE_FUNC_BP: typing.ClassVar[cern.lsa.domain.settings.Parameter] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.Parameter` PARAMETER_DOUBLE_FUNC_BP
    
    
    """
    PARAMETER_DOUBLE_ARRAY_FUNC_BP: typing.ClassVar[cern.lsa.domain.settings.Parameter] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.Parameter` PARAMETER_DOUBLE_ARRAY_FUNC_BP
    
    
    """
    PARAMETER_SHORT_ARRAY: typing.ClassVar[cern.lsa.domain.settings.Parameter] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.Parameter` PARAMETER_SHORT_ARRAY
    
    
    """
    BP_STAND_ALONE_DISCRETE: typing.ClassVar[cern.lsa.domain.settings.StandAloneBeamProcess] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.StandAloneBeamProcess` BP_STAND_ALONE_DISCRETE
    
    
    """
    BP_STAND_ALONE_DISCRETE_ARCHIVED: typing.ClassVar[cern.lsa.domain.settings.StandAloneBeamProcess] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.StandAloneBeamProcess` BP_STAND_ALONE_DISCRETE_ARCHIVED
    
    
    """
    BP_STAND_ALONE_FUNCTION: typing.ClassVar[cern.lsa.domain.settings.StandAloneBeamProcess] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.StandAloneBeamProcess` BP_STAND_ALONE_FUNCTION
    
    
    """
    BP_STAND_ALONE_ACTUAL: typing.ClassVar[cern.lsa.domain.settings.StandAloneBeamProcess] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.StandAloneBeamProcess` BP_STAND_ALONE_ACTUAL
    
    
    """
    BP_SPSRING_FUNCTION_INJ: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_SPSRING_FUNCTION_INJ
    
    
    """
    BP_SPSRING_FUNCTION_RAMP: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_SPSRING_FUNCTION_RAMP
    
    
    """
    BP_SPSRING_FUNCTION_FTOP: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_SPSRING_FUNCTION_FTOP
    
    
    """
    BP_SPSRING_FUNCTION_BEAM_OUT: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_SPSRING_FUNCTION_BEAM_OUT
    
    
    """
    BP_SPSRING_DISCRETE: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_SPSRING_DISCRETE
    
    
    """
    BP_SPS_CNGS_FUNCTION_BEAM_IN: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_SPS_CNGS_FUNCTION_BEAM_IN
    
    
    """
    BP_SPS_CNGS_FUNCTION_BEAM_OUT: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_SPS_CNGS_FUNCTION_BEAM_OUT
    
    
    """
    BP_SPS_INJ_FUNCTION_BEAM_IN: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_SPS_INJ_FUNCTION_BEAM_IN
    
    
    """
    BP_SPS_INJ_FUNCTION_BEAM_OUT: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_SPS_INJ_FUNCTION_BEAM_OUT
    
    
    """
    CYCLE_SPS: typing.ClassVar[cern.lsa.domain.settings.spi.StandAloneCycleImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.StandAloneCycleImpl` CYCLE_SPS
    
    
    """
    BP_PSRING_FUNCTION: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_PSRING_FUNCTION
    
    
    """
    BP_PSRING_DISCRETE: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_PSRING_DISCRETE
    
    
    """
    BP_PS_INJ_FUNCTION: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_PS_INJ_FUNCTION
    
    
    """
    CYCLE_PS: typing.ClassVar[cern.lsa.domain.settings.spi.StandAloneCycleImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.StandAloneCycleImpl` CYCLE_PS
    
    
    """
    BP_PS_NON_MULTIPLEXED: typing.ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.BeamProcessImpl` BP_PS_NON_MULTIPLEXED
    
    
    """
    CYCLE_PS_NON_MULTIPLEXED: typing.ClassVar[cern.lsa.domain.settings.spi.StandAloneCycleImpl] = ...
    """
    public static final :class:`~cern.lsa.domain.settings.spi.StandAloneCycleImpl` CYCLE_PS_NON_MULTIPLEXED
    
    
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def actualBeamProcess(string: str, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess, int: int, string2: str) -> cern.lsa.domain.settings.spi.BeamProcessImpl:
        """
        public static :class:`~cern.lsa.domain.settings.spi.StandAloneBeamProcessImpl` actualBeamProcess (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name, :class:`~cern.lsa.domain.settings.StandAloneBeamProcess` srcBeamProcess, int srcPoint)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def actualBeamProcess(string: str, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess, int: int) -> cern.lsa.domain.settings.spi.StandAloneBeamProcessImpl: ...
    @staticmethod
    def addSettings(contextSettingsImpl: cern.lsa.domain.settings.spi.ContextSettingsImpl, parameter: cern.lsa.domain.settings.Parameter, immutableValue: cern.accsoft.commons.value.ImmutableValue, beamProcessTypeCategoryArray: typing.List[cern.lsa.domain.settings.type.BeamProcessTypeCategory]) -> None: ...
    @staticmethod
    def beamProcess(string: str, int: int, int2: int, beamProcessTypeCategory: cern.lsa.domain.settings.type.BeamProcessTypeCategory, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> cern.lsa.domain.settings.spi.BeamProcessImpl: ...
    @staticmethod
    def createDevice(string: str, string2: str, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.devices.Device: ...
    @staticmethod
    def createDeviceTypeVersion(string: str, int: int, int2: int) -> cern.lsa.domain.devices.DeviceTypeVersion: ...
    @staticmethod
    def createNodes(set: java.util.Set[cern.lsa.domain.settings.Parameter]) -> java.util.List[cern.lsa.domain.settings.spi.ParameterTreeNodeImpl]: ...
    @staticmethod
    def createParameterAndTypeForTesting(string: str, string2: str) -> cern.accsoft.commons.util.value.Pair[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.ParameterType]: ...
    @staticmethod
    def createParameterAndTypeWithNameForTesting(string: str) -> cern.accsoft.commons.util.value.Pair[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.ParameterType]: ...
    @typing.overload
    @staticmethod
    def createParameterWithNameForTesting() -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def createParameterWithNameForTesting(string: str) -> cern.lsa.domain.settings.Parameter:
        """
        public static :class:`~cern.lsa.domain.settings.Parameter` createParameterWithNameForTesting()
        
        
        """
        ...
    @staticmethod
    def discreteBeamProcess(string: str, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, boolean: bool) -> cern.lsa.domain.settings.spi.BeamProcessImpl: ...
    @staticmethod
    def function(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> cern.accsoft.commons.value.DiscreteFunction: ...
    @staticmethod
    def functionBeamProcess(string: str, int: int, int2: int, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, boolean: bool) -> cern.lsa.domain.settings.spi.BeamProcessImpl: ...
    @staticmethod
    def newTrimRequestBuilder(standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> cern.lsa.domain.settings.factory.TrimRequestBuilder:
        """
            Creates new TrimRequestBuilder initializing it with given Context.
        
        """
        ...
    @typing.overload
    @staticmethod
    def parameter(string: str, parameterType: cern.lsa.domain.settings.ParameterType, boolean: bool, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone, type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.Parameter:
        """
        public static :class:`~cern.lsa.domain.settings.Parameter` parameter (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name, `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` parameterTypeName)
        
        """
        ...
    @typing.overload
    @staticmethod
    def parameter(string: str, parameterType: cern.lsa.domain.settings.ParameterType, boolean: bool, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone, type: cern.accsoft.commons.value.Type, boolean2: bool, boolean3: bool) -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def parameter(string: str, parameterType: cern.lsa.domain.settings.ParameterType, type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.Parameter:
        """
        public static :class:`~cern.lsa.domain.settings.Parameter` parameter (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name, :class:`~cern.lsa.domain.settings.spi.test.SettingsDomainUtils.ParameterTypeStub` marker)
        
        public static :class:`~cern.lsa.domain.settings.Parameter` parameter (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name, :class:`~cern.lsa.domain.settings.ParameterType` parameterType, cern.accsoft.commons.value.Type valueType, cern.accsoft.commons.domain.zones.AcceleratorZone acceleratorZone)
        
        public static :class:`~cern.lsa.domain.settings.Parameter` parameter (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name, :class:`~cern.lsa.domain.settings.ParameterType` parameterType, boolean belongsToFuncBP, cern.accsoft.commons.domain.zones.AcceleratorZone accZone, cern.accsoft.commons.value.Type valueType, boolean multiplexed, boolean lsaImplementation)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parameter(string: str, parameterType: cern.lsa.domain.settings.ParameterType, type: cern.accsoft.commons.value.Type, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def parameter(string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def parameter(string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub', boolean: bool, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def parameter(string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub', acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def parameter(string: str, string2: str) -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def parameterBuilder(string: str, type: cern.accsoft.commons.value.Type, parameterType: cern.lsa.domain.settings.ParameterType) -> cern.lsa.domain.settings.spi.ParameterBuilder.ParameterBuilderSteps:
        """
        public static :class:`~cern.lsa.domain.settings.spi.ParameterBuilder.ParameterBuilderSteps` parameterBuilder (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` parameterName, cern.accsoft.commons.value.Type valueType, :class:`~cern.lsa.domain.settings.ParameterType` parameterType)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parameterBuilder(string: str, type: cern.accsoft.commons.value.Type, parameterType: cern.lsa.domain.settings.ParameterType, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.spi.ParameterBuilder.ParameterBuilderSteps: ...
    @typing.overload
    @staticmethod
    def parameterBuilder(string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub', acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.spi.ParameterBuilder.ParameterBuilderSteps: ...
    @staticmethod
    def parameterBuilderLhc(string: str, type: cern.accsoft.commons.value.Type, parameterType: cern.lsa.domain.settings.ParameterType) -> cern.lsa.domain.settings.spi.ParameterBuilder.ParameterBuilderSteps: ...
    @typing.overload
    @staticmethod
    def parameterLhc(string: str, parameterType: cern.lsa.domain.settings.ParameterType, type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.Parameter:
        """
        public static :class:`~cern.lsa.domain.settings.Parameter` parameterLhc (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name, :class:`~cern.lsa.domain.settings.spi.test.SettingsDomainUtils.ParameterTypeStub` marker)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parameterLhc(string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def parameterLhc(string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub', boolean: bool) -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def parameterPsRing(string: str, parameterType: cern.lsa.domain.settings.ParameterType, type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.Parameter:
        """
        public static :class:`~cern.lsa.domain.settings.Parameter` parameterPsRing (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name, :class:`~cern.lsa.domain.settings.spi.test.SettingsDomainUtils.ParameterTypeStub` marker)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parameterPsRing(string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def parameterSpsRing(string: str, parameterType: cern.lsa.domain.settings.ParameterType, type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.Parameter: ...
    @typing.overload
    @staticmethod
    def parameterSpsRing(string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.Parameter:
        """
        public static :class:`~cern.lsa.domain.settings.Parameter` parameterSpsRing (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name, :class:`~cern.lsa.domain.settings.ParameterType` parameterType, cern.accsoft.commons.value.Type valueType)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def parameterType(parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.ParameterType:
        """
        public static :class:`~cern.lsa.domain.settings.ParameterType` parameterType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name)
        
        """
        ...
    @typing.overload
    @staticmethod
    def parameterType(string: str) -> cern.lsa.domain.settings.ParameterType: ...
    @typing.overload
    @staticmethod
    def parameterType(string: str, boolean: bool) -> cern.lsa.domain.settings.ParameterType: ...
    @typing.overload
    @staticmethod
    def parameterTypeBuilder(parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.spi.ParameterTypeBuilder.ParameterTypeStepBuilder:
        """
        public static :class:`~cern.lsa.domain.settings.spi.ParameterTypeBuilder.ParameterTypeStepBuilder` parameterTypeBuilder (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name)
        
        """
        ...
    @typing.overload
    @staticmethod
    def parameterTypeBuilder(string: str) -> cern.lsa.domain.settings.spi.ParameterTypeBuilder.ParameterTypeStepBuilder: ...
    @typing.overload
    @staticmethod
    def parameterTypeBuilder(string: str, boolean: bool) -> cern.lsa.domain.settings.spi.ParameterTypeBuilder.ParameterTypeStepBuilder: ...
    @staticmethod
    def randomId() -> int: ...
    @typing.overload
    @staticmethod
    def setting(beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, object: typing.Any) -> cern.lsa.domain.settings.Setting:
        """
        public static :class:`~cern.lsa.domain.settings.Setting` setting (:class:`~cern.lsa.domain.settings.BeamProcess` beamprocess, :class:`~cern.lsa.domain.settings.Parameter` param, `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` target, `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` correction)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def setting(beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, object: typing.Any, object2: typing.Any) -> cern.lsa.domain.settings.Setting: ...
    @typing.overload
    @staticmethod
    def standAloneBeamProcess(string: str, int: int, beamProcessTypeCategory: cern.lsa.domain.settings.type.BeamProcessTypeCategory, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> cern.lsa.domain.settings.spi.StandAloneBeamProcessImpl:
        """
        public static :class:`~cern.lsa.domain.settings.spi.StandAloneBeamProcessImpl` standAloneBeamProcess (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` name, int length, :class:`~cern.lsa.domain.settings.type.BeamProcessTypeCategory` category, cern.accsoft.commons.domain.particletransfers.ParticleTransfer particleTransfer)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def standAloneBeamProcess(string: str, int: int, beamProcessTypeCategory: cern.lsa.domain.settings.type.BeamProcessTypeCategory, string2: str) -> cern.lsa.domain.settings.spi.StandAloneBeamProcessImpl: ...
    @staticmethod
    def standAloneCycle(string: str, int: int, beamProcessImplArray: typing.List[cern.lsa.domain.settings.spi.BeamProcessImpl]) -> cern.lsa.domain.settings.spi.StandAloneCycleImpl: ...
    class ParameterTypeStub(java.lang.Enum['SettingsDomainUtils.ParameterTypeStub']):
        PARAMETER_TYPE_FUNCTION: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_FUNCTION_LIST: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_FUNCTIONS_ARRAY: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_DOUBLE: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_DOUBLE_ARRAY: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_SHORT_ARRAY: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_NON_MUX: typing.ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'SettingsDomainUtils.ParameterTypeStub': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['SettingsDomainUtils.ParameterTypeStub']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings.spi.test")``.

    DriveResultsTestUtils: typing.Type[DriveResultsTestUtils]
    SettingsDomainUtils: typing.Type[SettingsDomainUtils]
