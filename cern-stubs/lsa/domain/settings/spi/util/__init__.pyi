import cern.accsoft.commons.value
import cern.lsa.domain.exploitation
import cern.lsa.domain.settings
import java.util
import typing



class SettingsCompareHelper:
    """
    Java class 'cern.lsa.domain.settings.spi.util.SettingsCompareHelper'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def prettyPrintInconsistentArrayValues(immutableScalarArray: cern.accsoft.commons.value.ImmutableScalarArray, immutableScalarArray2: cern.accsoft.commons.value.ImmutableScalarArray) -> str: ...
    @staticmethod
    def prettyPrintInconsistentValues(string: str, string2: str, immutableValue: cern.accsoft.commons.value.ImmutableValue, immutableValue2: cern.accsoft.commons.value.ImmutableValue) -> str: ...

class TrimHelper:
    """
    Java class 'cern.lsa.domain.settings.spi.util.TrimHelper'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * TrimHelper()
    
    """
    def __init__(self): ...
    @staticmethod
    def assertRequestContainsOnlySettingParameters(trimRequest: cern.lsa.domain.settings.TrimRequest) -> None: ...
    @staticmethod
    def canParameterAndItsParentHaveSettingsInBeamOut(parameter: cern.lsa.domain.settings.Parameter, parameter2: cern.lsa.domain.settings.Parameter) -> bool: ...
    @staticmethod
    def createAcquisitionTrimRequest(map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.exploitation.FailSafeImmutableValue], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.lsa.domain.exploitation.FailSafeImmutableValue]], drivableContext: cern.lsa.domain.settings.DrivableContext, string: str, boolean: bool) -> cern.lsa.domain.settings.TrimRequest: ...
    @staticmethod
    def extractParameters(collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.IncorporationSetting], typing.Sequence[cern.lsa.domain.settings.IncorporationSetting]]) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    @staticmethod
    def extractTrimmedParameters(trimRequest: cern.lsa.domain.settings.TrimRequest) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    @staticmethod
    def getParameterHierarchy(trimRequest: cern.lsa.domain.settings.TrimRequest) -> str: ...
    @staticmethod
    def hasDifferentLength(immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, int: int) -> bool: ...
    @staticmethod
    def hasSetting(beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool: ...
    @staticmethod
    def hasSettingInTrimRequest(beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, trimRequest: cern.lsa.domain.settings.TrimRequest) -> bool: ...
    @staticmethod
    def isSettingUpdated(beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool: ...
    @staticmethod
    def noParameterHasSetting(beamProcess: cern.lsa.domain.settings.BeamProcess, parameterArray: typing.List[cern.lsa.domain.settings.Parameter], contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool: ...
    @staticmethod
    def noParameterHasUpdatedSetting(beamProcess: cern.lsa.domain.settings.BeamProcess, parameterArray: typing.List[cern.lsa.domain.settings.Parameter], contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool: ...
    @staticmethod
    def parameterIsTrimmed(trimRequest: cern.lsa.domain.settings.TrimRequest, parameter: cern.lsa.domain.settings.Parameter) -> bool: ...
    @staticmethod
    def targetOrCorrectionHasLengthDifferentThanBeamProcess(setting: cern.lsa.domain.settings.Setting) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings.spi.util")``.

    SettingsCompareHelper: typing.Type[SettingsCompareHelper]
    TrimHelper: typing.Type[TrimHelper]
