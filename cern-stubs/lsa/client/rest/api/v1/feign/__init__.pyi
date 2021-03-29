import cern.lsa.client.rest.api.v1.dto
import cern.lsa.domain.cern.settings
import com.fasterxml.jackson.databind
import java.util
import typing


class FeignServiceLocator:
    @staticmethod
    def createObjectMapper() -> com.fasterxml.jackson.databind.ObjectMapper: ...
    @staticmethod
    def forHostAndPort(string: str, int: int) -> 'FeignServiceLocator': ...
    _getFeignService__T = typing.TypeVar('_getFeignService__T', bound='FeignService')  # <T>
    def getFeignService(self, class_: typing.Type[_getFeignService__T]) -> _getFeignService__T: ...

class FeignService: ...

class IncaFeignService(FeignService):
    def findIncaPropertyFieldInfos(self, incaPropertyFieldInfosRequestRest: cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestRest) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest]: ...
    def saveIncaPropertyFieldInfos(self, collection: typing.Union[java.util.Collection[cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest], typing.Sequence[cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoRest]]) -> None: ...
    class Urls:
        FIND_INCA_PROPERTY_FIELDS_INFO: typing.ClassVar[str] = ...
        SAVE_INCA_PROPERTY_FIELDS_INFO: typing.ClassVar[str] = ...

class ParameterFeignService(FeignService):
    def addParametersToParameterGroup(self, long: int, collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> None: ...
    def deleteCriticalProperty(self, long: int, string: str) -> None: ...
    def deleteParameterGroup(self, long: int) -> None: ...
    def deleteParameterTypes(self, collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> None: ...
    def deleteParameters(self, collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> None: ...
    def findAllHierarchies(self) -> java.util.List[str]: ...
    def findCommonHierarchyNames(self, list: java.util.List[int]) -> java.util.Set[str]: ...
    def findHierarchyNames(self, list: java.util.List[int]) -> java.util.Set[str]: ...
    def findMakeRuleForParameterRelation(self, long: int, long2: int) -> cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoRest: ...
    def findParameterGroupsByAccelerator(self, string: str) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterGroupRest]: ...
    def findParameterTrees(self, parameterTreesRequestRest: cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestRest) -> cern.lsa.client.rest.api.v1.dto.ParameterTreeDataRest: ...
    def findParameterTypes(self, parameterTypesRequestRest: cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestRest) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterTypeRest]: ...
    def findParameters(self, parametersRequestRest: cern.lsa.client.rest.api.v1.dto.ParametersRequestRest) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterRest]: ...
    def findParametersWithSettings(self, long: int, string: str) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterRest]: ...
    def findParametersWithoutSettings(self, long: int, string: str) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterRest]: ...
    def getMaxDelta(self, long: int) -> float: ...
    def removeParametersFromParameterGroup(self, long: int, collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> None: ...
    def saveCriticalProperty(self, propertyAndDeviceRest: cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceRest) -> None: ...
    def saveParameterGroup(self, parameterGroupRest: cern.lsa.client.rest.api.v1.dto.ParameterGroupRest) -> None: ...
    def saveParameterTypes(self, collection: typing.Union[java.util.Collection[cern.lsa.client.rest.api.v1.dto.ParameterTypeRest], typing.Sequence[cern.lsa.client.rest.api.v1.dto.ParameterTypeRest]]) -> None: ...
    def saveParameters(self, list: java.util.List[cern.lsa.client.rest.api.v1.dto.ParameterAttributesRest]) -> None: ...
    class Urls:
        FIND_PARAMETERS_URL: typing.ClassVar[str] = ...
        PARAMETERS_URL: typing.ClassVar[str] = ...
        PARAMETER_TYPES_URL: typing.ClassVar[str] = ...
        FIND_ALL_HIERARCHIES_URL: typing.ClassVar[str] = ...
        FIND_HIERARCHIES_BY_PARAMETERS_URL: typing.ClassVar[str] = ...
        FIND_COMMON_HIERARCHIES_BY_PARAMETERS_URL: typing.ClassVar[str] = ...
        SAVE_PARAMETER_RELATIONS: typing.ClassVar[str] = ...
        CRITICAL_PROPERTIES_URL: typing.ClassVar[str] = ...
        PARAMETER_GROUPS_URL: typing.ClassVar[str] = ...
        PARAMETER_GROUP_BY_ID_URL: typing.ClassVar[str] = ...
        PARAMETER_GROUP_PARAMETERS_URL: typing.ClassVar[str] = ...
        PARAMETER_RELATION_MAKE_RULE_URL: typing.ClassVar[str] = ...
        FIND_PARAMETER_TREES_URL: typing.ClassVar[str] = ...
        PARAMETERS_WITHOUT_SETTINGS_URL: typing.ClassVar[str] = ...
        PARAMETERS_WITH_SETTINGS_URL: typing.ClassVar[str] = ...
        PARAMETER_MAX_DELTA_URL: typing.ClassVar[str] = ...

class ReDriveSettingsFeignService(FeignService):
    def reDriveDeviceSettings(self, reDriveRequest: cern.lsa.domain.cern.settings.ReDriveRequest) -> cern.lsa.domain.cern.settings.ReDriveResponse: ...
    class Urls:
        REDRIVE_DEVICES: typing.ClassVar[str] = ...
