from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
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


class DriveResultsTestUtils:
    def __init__(self): ...
    @classmethod
    def countJapcParameterDriveResults(cls, driveResult: cern.lsa.domain.exploitation.DriveResult) -> int: ...
    @classmethod
    def countSuccessfulJapcParameterDriveResults(cls, driveResult: cern.lsa.domain.exploitation.DriveResult) -> int: ...
    @classmethod
    def countSuccessfulLsaParameterDriveResults(cls, driveResult: cern.lsa.domain.exploitation.DriveResult) -> int: ...
    @classmethod
    @overload
    def createLsaParameterDriveResult(cls) -> cern.lsa.domain.exploitation.spi.results.LsaParameterDriveResult: ...
    @classmethod
    @overload
    def createLsaParameterDriveResult(cls, parameter: cern.lsa.domain.settings.Parameter) -> cern.lsa.domain.exploitation.spi.results.LsaParameterDriveResult: ...
    @classmethod
    def createLsaParameterDriveResults(cls, int: int) -> java.util.Set[cern.lsa.domain.exploitation.spi.results.LsaParameterDriveResult]: ...
    @classmethod
    @overload
    def createSuccessfulContextDriveResult(cls, drivableContext: cern.lsa.domain.settings.DrivableContext, int: int, int2: int) -> cern.lsa.domain.exploitation.spi.results.ContextDriveResult: ...
    @classmethod
    @overload
    def createSuccessfulContextDriveResult(cls, int: int, int2: int) -> cern.lsa.domain.exploitation.spi.results.ContextDriveResult: ...
    @classmethod
    @overload
    def createSuccessfulJapcParameterDriveResult(cls) -> cern.lsa.domain.exploitation.spi.results.JapcParameterDriveResult: ...
    @classmethod
    @overload
    def createSuccessfulJapcParameterDriveResult(cls, string: str) -> cern.lsa.domain.exploitation.spi.results.JapcParameterDriveResult: ...
    @classmethod
    def createSuccessfulJapcParameterDriveResults(cls, int: int) -> java.util.Set[cern.lsa.domain.exploitation.spi.results.JapcParameterDriveResult]: ...

class SettingsDomainUtils:
    BP_LENGTH: _py_ClassVar[int] = ...
    CONTEXT_CATEGORY_OPERATIONAL: _py_ClassVar[str] = ...
    FUNC_0_0: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_0_1: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_1_0: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_1_1: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_1_2: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_2_1: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_2_2: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_2_3: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_3_3: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_4_4: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_5_5: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_6_6: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    FUNC_0_1_0: _py_ClassVar[cern.accsoft.commons.value.ImmutableDiscreteFunction] = ...
    SCALAR_0: _py_ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    SCALAR_1: _py_ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    SCALAR_2: _py_ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    SCALAR_3: _py_ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    SCALAR_4: _py_ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    SCALAR_5: _py_ClassVar[cern.accsoft.commons.value.ImmutableScalar] = ...
    PARAMETER_TYPE_FUNCTION: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    PARAMETER_TYPE_FUNCTION_LIST: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    PARAMETER_TYPE_FUNCTIONS_ARRAY: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    PARAMETER_TYPE_DOUBLE: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    PARAMETER_TYPE_DOUBLE_ARRAY: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    PARAMETER_TYPE_SHORT_ARRAY: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    PARAMETER_TYPE_NON_MUX: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
    PARAMETER_FUNCTION: _py_ClassVar[cern.lsa.domain.settings.Parameter] = ...
    PARAMETER_DOUBLE: _py_ClassVar[cern.lsa.domain.settings.Parameter] = ...
    PARAMETER_DOUBLE_ARRAY: _py_ClassVar[cern.lsa.domain.settings.Parameter] = ...
    PARAMETER_DOUBLE_FUNC_BP: _py_ClassVar[cern.lsa.domain.settings.Parameter] = ...
    PARAMETER_DOUBLE_ARRAY_FUNC_BP: _py_ClassVar[cern.lsa.domain.settings.Parameter] = ...
    PARAMETER_SHORT_ARRAY: _py_ClassVar[cern.lsa.domain.settings.Parameter] = ...
    BP_STAND_ALONE_DISCRETE: _py_ClassVar[cern.lsa.domain.settings.StandAloneBeamProcess] = ...
    BP_STAND_ALONE_DISCRETE_ARCHIVED: _py_ClassVar[cern.lsa.domain.settings.StandAloneBeamProcess] = ...
    BP_STAND_ALONE_FUNCTION: _py_ClassVar[cern.lsa.domain.settings.StandAloneBeamProcess] = ...
    BP_STAND_ALONE_ACTUAL: _py_ClassVar[cern.lsa.domain.settings.StandAloneBeamProcess] = ...
    BP_SPSRING_FUNCTION_INJ: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    BP_SPSRING_FUNCTION_RAMP: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    BP_SPSRING_FUNCTION_FTOP: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    BP_SPSRING_FUNCTION_BEAM_OUT: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    BP_SPSRING_DISCRETE: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    BP_SPS_CNGS_FUNCTION_BEAM_IN: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    BP_SPS_CNGS_FUNCTION_BEAM_OUT: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    BP_SPS_INJ_FUNCTION_BEAM_IN: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    BP_SPS_INJ_FUNCTION_BEAM_OUT: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    CYCLE_SPS: _py_ClassVar[cern.lsa.domain.settings.spi.StandAloneCycleImpl] = ...
    BP_PSRING_FUNCTION: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    BP_PSRING_DISCRETE: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    BP_PS_INJ_FUNCTION: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    CYCLE_PS: _py_ClassVar[cern.lsa.domain.settings.spi.StandAloneCycleImpl] = ...
    BP_PS_NON_MULTIPLEXED: _py_ClassVar[cern.lsa.domain.settings.spi.BeamProcessImpl] = ...
    CYCLE_PS_NON_MULTIPLEXED: _py_ClassVar[cern.lsa.domain.settings.spi.StandAloneCycleImpl] = ...
    def __init__(self): ...
    @classmethod
    @overload
    def actualBeamProcess(cls, string: str, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess, int: int, string2: str) -> cern.lsa.domain.settings.spi.BeamProcessImpl: ...
    @classmethod
    @overload
    def actualBeamProcess(cls, string: str, standAloneBeamProcess: cern.lsa.domain.settings.StandAloneBeamProcess, int: int) -> cern.lsa.domain.settings.spi.StandAloneBeamProcessImpl: ...
    @classmethod
    def addSettings(cls, contextSettingsImpl: cern.lsa.domain.settings.spi.ContextSettingsImpl, parameter: cern.lsa.domain.settings.Parameter, immutableValue: cern.accsoft.commons.value.ImmutableValue, beamProcessTypeCategoryArray: _py_List[cern.lsa.domain.settings.type.BeamProcessTypeCategory]) -> None: ...
    @classmethod
    def beamProcess(cls, string: str, int: int, int2: int, beamProcessTypeCategory: cern.lsa.domain.settings.type.BeamProcessTypeCategory, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> cern.lsa.domain.settings.spi.BeamProcessImpl: ...
    @classmethod
    def createDevice(cls, string: str, string2: str, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.devices.Device: ...
    @classmethod
    def createDeviceTypeVersion(cls, string: str, int: int, int2: int) -> cern.lsa.domain.devices.DeviceTypeVersion: ...
    @classmethod
    def createNodes(cls, set: java.util.Set[cern.lsa.domain.settings.Parameter]) -> java.util.List[cern.lsa.domain.settings.spi.ParameterTreeNodeImpl]: ...
    @classmethod
    def createParameterAndTypeForTesting(cls, string: str, string2: str) -> cern.accsoft.commons.util.value.Pair[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.ParameterType]: ...
    @classmethod
    def createParameterAndTypeWithNameForTesting(cls, string: str) -> cern.accsoft.commons.util.value.Pair[cern.lsa.domain.settings.Parameter, cern.lsa.domain.settings.ParameterType]: ...
    @classmethod
    @overload
    def createParameterWithNameForTesting(cls) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def createParameterWithNameForTesting(cls, string: str) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    def discreteBeamProcess(cls, string: str, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, boolean: bool) -> cern.lsa.domain.settings.spi.BeamProcessImpl: ...
    @classmethod
    def function(cls, doubleArray: _py_List[float], doubleArray2: _py_List[float]) -> cern.accsoft.commons.value.DiscreteFunction: ...
    @classmethod
    def functionBeamProcess(cls, string: str, int: int, int2: int, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer, boolean: bool) -> cern.lsa.domain.settings.spi.BeamProcessImpl: ...
    @classmethod
    def newTrimRequestBuilder(cls, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> cern.lsa.domain.settings.factory.TrimRequestBuilder: ...
    @classmethod
    @overload
    def parameter(cls, string: str, parameterType: cern.lsa.domain.settings.ParameterType, boolean: bool, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone, type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameter(cls, string: str, parameterType: cern.lsa.domain.settings.ParameterType, boolean: bool, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone, type: cern.accsoft.commons.value.Type, boolean2: bool, boolean3: bool) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameter(cls, string: str, parameterType: cern.lsa.domain.settings.ParameterType, type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameter(cls, string: str, parameterType: cern.lsa.domain.settings.ParameterType, type: cern.accsoft.commons.value.Type, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameter(cls, string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameter(cls, string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub', boolean: bool, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameter(cls, string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub', acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameter(cls, string: str, string2: str) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameterBuilder(cls, string: str, type: cern.accsoft.commons.value.Type, parameterType: cern.lsa.domain.settings.ParameterType) -> cern.lsa.domain.settings.spi.ParameterBuilder.ParameterBuilderSteps: ...
    @classmethod
    @overload
    def parameterBuilder(cls, string: str, type: cern.accsoft.commons.value.Type, parameterType: cern.lsa.domain.settings.ParameterType, acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.spi.ParameterBuilder.ParameterBuilderSteps: ...
    @classmethod
    @overload
    def parameterBuilder(cls, string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub', acceleratorZone: cern.accsoft.commons.domain.zones.AcceleratorZone) -> cern.lsa.domain.settings.spi.ParameterBuilder.ParameterBuilderSteps: ...
    @classmethod
    def parameterBuilderLhc(cls, string: str, type: cern.accsoft.commons.value.Type, parameterType: cern.lsa.domain.settings.ParameterType) -> cern.lsa.domain.settings.spi.ParameterBuilder.ParameterBuilderSteps: ...
    @classmethod
    @overload
    def parameterLhc(cls, string: str, parameterType: cern.lsa.domain.settings.ParameterType, type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameterLhc(cls, string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameterLhc(cls, string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub', boolean: bool) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameterPsRing(cls, string: str, parameterType: cern.lsa.domain.settings.ParameterType, type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameterPsRing(cls, string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameterSpsRing(cls, string: str, parameterType: cern.lsa.domain.settings.ParameterType, type: cern.accsoft.commons.value.Type) -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameterSpsRing(cls, string: str, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.Parameter: ...
    @classmethod
    @overload
    def parameterType(cls, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.ParameterType: ...
    @classmethod
    @overload
    def parameterType(cls, string: str) -> cern.lsa.domain.settings.ParameterType: ...
    @classmethod
    @overload
    def parameterType(cls, string: str, boolean: bool) -> cern.lsa.domain.settings.ParameterType: ...
    @classmethod
    @overload
    def parameterTypeBuilder(cls, parameterTypeStub: 'SettingsDomainUtils.ParameterTypeStub') -> cern.lsa.domain.settings.spi.ParameterTypeBuilder.ParameterTypeStepBuilder: ...
    @classmethod
    @overload
    def parameterTypeBuilder(cls, string: str) -> cern.lsa.domain.settings.spi.ParameterTypeBuilder.ParameterTypeStepBuilder: ...
    @classmethod
    @overload
    def parameterTypeBuilder(cls, string: str, boolean: bool) -> cern.lsa.domain.settings.spi.ParameterTypeBuilder.ParameterTypeStepBuilder: ...
    @classmethod
    @overload
    def setting(cls, beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, object: _py_Any) -> cern.lsa.domain.settings.Setting: ...
    @classmethod
    @overload
    def setting(cls, beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, object: _py_Any, object2: _py_Any) -> cern.lsa.domain.settings.Setting: ...
    @classmethod
    @overload
    def standAloneBeamProcess(cls, string: str, int: int, beamProcessTypeCategory: cern.lsa.domain.settings.type.BeamProcessTypeCategory, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> cern.lsa.domain.settings.spi.StandAloneBeamProcessImpl: ...
    @classmethod
    @overload
    def standAloneBeamProcess(cls, string: str, int: int, beamProcessTypeCategory: cern.lsa.domain.settings.type.BeamProcessTypeCategory, string2: str) -> cern.lsa.domain.settings.spi.StandAloneBeamProcessImpl: ...
    @classmethod
    def standAloneCycle(cls, string: str, int: int, beamProcessImplArray: _py_List[cern.lsa.domain.settings.spi.BeamProcessImpl]) -> cern.lsa.domain.settings.spi.StandAloneCycleImpl: ...
    class ParameterTypeStub(java.lang.Enum['SettingsDomainUtils.ParameterTypeStub']):
        PARAMETER_TYPE_FUNCTION: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_FUNCTION_LIST: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_FUNCTIONS_ARRAY: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_DOUBLE: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_DOUBLE_ARRAY: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_SHORT_ARRAY: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        PARAMETER_TYPE_NON_MUX: _py_ClassVar['SettingsDomainUtils.ParameterTypeStub'] = ...
        @classmethod
        @overload
        def valueOf(cls, string: str) -> 'SettingsDomainUtils.ParameterTypeStub': ...
        _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @overload
        def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @classmethod
        def values(cls) -> _py_List['SettingsDomainUtils.ParameterTypeStub']: ...