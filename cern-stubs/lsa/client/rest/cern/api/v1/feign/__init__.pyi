import cern.lsa.client.rest.api.v1.dto
import cern.lsa.client.rest.api.v1.feign
import cern.lsa.domain.cern.settings
import java.util
import typing



class IncaFeignService(cern.lsa.client.rest.api.v1.feign.FeignService):
    """
    public interface IncaFeignService extends cern.lsa.client.rest.api.v1.feign.FeignService
    """
    def findIncaPropertyFieldInfos(self, incaPropertyFieldInfosRequestDto: cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfosRequestDto) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto]: ...
    def saveIncaPropertyFieldInfos(self, collection: typing.Union[java.util.Collection[cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto], typing.Sequence[cern.lsa.client.rest.api.v1.dto.IncaPropertyFieldInfoDto]]) -> None: ...
    class Urls:
        FIND_INCA_PROPERTY_FIELDS_INFO: typing.ClassVar[str] = ...
        SAVE_INCA_PROPERTY_FIELDS_INFO: typing.ClassVar[str] = ...

class ParameterFeignService(cern.lsa.client.rest.api.v1.feign.FeignService):
    """
    public interface ParameterFeignService extends cern.lsa.client.rest.api.v1.feign.FeignService
    """
    def addParametersToParameterGroup(self, long: int, collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> None: ...
    def deleteCriticalProperty(self, long: int, string: str) -> None: ...
    def deleteParameterGroup(self, long: int) -> None: ...
    def deleteParameterTypes(self, collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> None: ...
    def deleteParameters(self, collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> None: ...
    def findAllHierarchies(self) -> java.util.List[str]: ...
    def findCommonHierarchyNames(self, list: java.util.List[int]) -> java.util.Set[str]: ...
    def findHierarchyNames(self, list: java.util.List[int]) -> java.util.Set[str]: ...
    def findMakeRuleForParameterRelation(self, long: int, long2: int) -> cern.lsa.client.rest.api.v1.dto.MakeRuleConfigInfoDto: ...
    def findParameterGroupsByAccelerator(self, string: str) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterGroupDto]: ...
    def findParameterTrees(self, parameterTreesRequestDto: cern.lsa.client.rest.api.v1.dto.ParameterTreesRequestDto) -> cern.lsa.client.rest.api.v1.dto.ParameterTreeDataDto: ...
    def findParameterTypes(self, parameterTypesRequestDto: cern.lsa.client.rest.api.v1.dto.ParameterTypesRequestDto) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterTypeDto]: ...
    def findParameters(self, parametersRequestDto: cern.lsa.client.rest.api.v1.dto.ParametersRequestDto) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterDto]: ...
    def findParametersWithSettings(self, long: int, string: str) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterDto]: ...
    def findParametersWithoutSettings(self, long: int, string: str) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterDto]: ...
    def getMaxDelta(self, long: int) -> float: ...
    def removeParametersFromParameterGroup(self, long: int, collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> None: ...
    def saveCriticalProperty(self, propertyAndDeviceDto: cern.lsa.client.rest.api.v1.dto.PropertyAndDeviceDto) -> None: ...
    def saveParameterGroup(self, parameterGroupDto: cern.lsa.client.rest.api.v1.dto.ParameterGroupDto) -> None: ...
    def saveParameterTypes(self, collection: typing.Union[java.util.Collection[cern.lsa.client.rest.api.v1.dto.ParameterTypeDto], typing.Sequence[cern.lsa.client.rest.api.v1.dto.ParameterTypeDto]]) -> None: ...
    def saveParameters(self, list: java.util.List[cern.lsa.client.rest.api.v1.dto.ParameterAttributesDto]) -> None: ...
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

class ReDriveSettingsFeignService(cern.lsa.client.rest.api.v1.feign.FeignService):
    """
    public interface ReDriveSettingsFeignService extends cern.lsa.client.rest.api.v1.feign.FeignService
    """
    def reDriveDeviceSettings(self, reDriveRequest: cern.lsa.domain.cern.settings.ReDriveRequest) -> cern.lsa.domain.cern.settings.ReDriveResponse: ...
    class Urls:
        REDRIVE_DEVICES: typing.ClassVar[str] = ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.cern.api.v1.feign")``.

    IncaFeignService: typing.Type[IncaFeignService]
    ParameterFeignService: typing.Type[ParameterFeignService]
    ReDriveSettingsFeignService: typing.Type[ReDriveSettingsFeignService]
