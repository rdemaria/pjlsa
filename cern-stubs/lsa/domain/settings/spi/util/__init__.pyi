import cern.accsoft.commons.value
import cern.lsa.domain.exploitation
import cern.lsa.domain.settings
import java.util
import typing



class SettingsCompareHelper:
    """
    public class SettingsCompareHelper extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def prettyPrintInconsistentArrayValues(immutableScalarArray: cern.accsoft.commons.value.ImmutableScalarArray, immutableScalarArray2: cern.accsoft.commons.value.ImmutableScalarArray) -> str: ...
    @staticmethod
    def prettyPrintInconsistentValues(string: str, string2: str, immutableValue: cern.accsoft.commons.value.ImmutableValue, immutableValue2: cern.accsoft.commons.value.ImmutableValue) -> str: ...

class TrimHelper:
    """
    public class TrimHelper extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Helper class with methods used by the trim core.
    """
    def __init__(self): ...
    @staticmethod
    def assertRequestContainsOnlySettingParameters(trimRequest: cern.lsa.domain.settings.TrimRequest) -> None: ...
    @staticmethod
    def canParameterAndItsParentHaveSettingsInBeamOut(parameter: cern.lsa.domain.settings.Parameter, parameter2: cern.lsa.domain.settings.Parameter) -> bool:
        """
            The method returns :code:`true` if the specified parameter and all its parents are
            :meth:`~cern.lsa.domain.settings.ParameterType.isLinkRuleApplicable` parameters so that they can have settings in the
            beam-out. This is basically to verify if setting of given parameter can be calculated for the beam out from its parents.
        
            There might be a case that one of the parents is a scalar parameter that keeps settings in a discrete beam process (and
            not in beam-out). In such case the the method also returns :code:`true` as the setting of child can be calculated.
        
            If parameter has no parents (the specified array is empty) - the method returns :code:`false`.
        
        """
        ...
    @staticmethod
    def createAcquisitionTrimRequest(map: typing.Union[java.util.Map[cern.lsa.domain.settings.Parameter, cern.lsa.domain.exploitation.FailSafeImmutableValue], typing.Mapping[cern.lsa.domain.settings.Parameter, cern.lsa.domain.exploitation.FailSafeImmutableValue]], drivableContext: cern.lsa.domain.settings.DrivableContext, string: str, boolean: bool) -> cern.lsa.domain.settings.TrimRequest: ...
    @staticmethod
    def extractParameters(collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.IncorporationSetting], typing.Sequence[cern.lsa.domain.settings.IncorporationSetting]]) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    @staticmethod
    def extractTrimmedParameters(trimRequest: cern.lsa.domain.settings.TrimRequest) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    @staticmethod
    def getParameterHierarchy(trimRequest: cern.lsa.domain.settings.TrimRequest) -> str:
        """
        
            Parameters:
                request (:class:`~cern.lsa.domain.settings.TrimRequest`): 
            Returns:
                parameter hierarchy to be used
        
        
        """
        ...
    @staticmethod
    def hasDifferentLength(immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, int: int) -> bool: ...
    @staticmethod
    def hasSetting(beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool:
        """
            Indicates if the given ContextSettings contains setting for specified parameter and beam process.
        
        """
        ...
    @staticmethod
    def hasSettingInTrimRequest(beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, trimRequest: cern.lsa.domain.settings.TrimRequest) -> bool:
        """
            Indicates if the TrimRequest contains setting for specified parameter and beam process.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.TrimRequest.getContextSettings`
        
        
        """
        ...
    @staticmethod
    def isSettingUpdated(beamProcess: cern.lsa.domain.settings.BeamProcess, parameter: cern.lsa.domain.settings.Parameter, contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool:
        """
            Indicates if setting of specified parameter in specified beam process has been
            :meth:`~cern.lsa.domain.settings.ParameterSettings.isUpdated`. The method handles properly the case when parameter is
            not compatible with specified beam process. In such case the method looks for
            :meth:`~cern.lsa.domain.settings.Contexts.isCompatible` beam processes and checks if settings were updated on at least
            one of them.
        
            Also see:
                :meth:`~cern.lsa.domain.settings.Contexts.getCorrespondingBeamProcesses`,
                :meth:`~cern.lsa.domain.settings.spi.util.TrimHelper.isSettingUpdatedInAtLeastOneBeamProcess`
        
        
        """
        ...
    @staticmethod
    def noParameterHasSetting(beamProcess: cern.lsa.domain.settings.BeamProcess, parameterArray: typing.List[cern.lsa.domain.settings.Parameter], contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool:
        """
            Indicates if the given ContextSettings contains setting for at least one parameter from the specified ones and beam
            process.
        
        """
        ...
    @staticmethod
    def noParameterHasUpdatedSetting(beamProcess: cern.lsa.domain.settings.BeamProcess, parameterArray: typing.List[cern.lsa.domain.settings.Parameter], contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool:
        """
            Indicates if the given ContextSettings contains setting for all parent but none of them is updated
        
        """
        ...
    @staticmethod
    def parameterIsTrimmed(trimRequest: cern.lsa.domain.settings.TrimRequest, parameter: cern.lsa.domain.settings.Parameter) -> bool:
        """
        
            Parameters:
                request (:class:`~cern.lsa.domain.settings.TrimRequest`):         parameter (:class:`~cern.lsa.domain.settings.Parameter`): 
            Returns:
                :code:`true` if the parameter is requested to be trimmed or incorporated
        
        
        """
        ...
    @staticmethod
    def targetOrCorrectionHasLengthDifferentThanBeamProcess(setting: cern.lsa.domain.settings.Setting) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings.spi.util")``.

    SettingsCompareHelper: typing.Type[SettingsCompareHelper]
    TrimHelper: typing.Type[TrimHelper]
