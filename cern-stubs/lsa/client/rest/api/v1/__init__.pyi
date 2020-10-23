import cern.accsoft.commons.domain
import cern.lsa.client
import cern.lsa.client.rest.api.v1.feign
import cern.lsa.client.rest.api.v1.mapper
import cern.lsa.domain.devices
import cern.lsa.domain.devices.inca
import cern.lsa.domain.devices.type
import cern.lsa.domain.settings
import cern.lsa.domain.settings.parameter.relation
import cern.lsa.domain.settings.parameter.type.relation
import cern.lsa.domain.trim.rules.makerule
import java.util


class ClientRestConfig:
    def __init__(self): ...
    def feignServiceLocator(self) -> cern.lsa.client.rest.api.v1.feign.FeignServiceLocator: ...
    def fromRest(self) -> cern.lsa.client.rest.api.v1.mapper.FromRest: ...
    def incaFeignService(self) -> cern.lsa.client.rest.api.v1.feign.IncaFeignService: ...
    def incaServiceRest(self) -> cern.lsa.client.IncaService: ...
    def toRest(self) -> cern.lsa.client.rest.api.v1.mapper.ToRest: ...

class ClientRestIncaService(cern.lsa.client.IncaService):
    def __init__(self, incaFeignService: cern.lsa.client.rest.api.v1.feign.IncaFeignService, toRest: cern.lsa.client.rest.api.v1.mapper.ToRest, fromRest: cern.lsa.client.rest.api.v1.mapper.FromRest): ...
    def findIncaPropertyFieldInfos(self, incaPropertyFieldInfosRequest: cern.lsa.domain.devices.inca.IncaPropertyFieldInfosRequest) -> java.util.Set[cern.lsa.domain.devices.inca.IncaPropertyFieldInfo]: ...
    def saveIncaPropertyFieldInfos(self, collection: java.util.Collection[cern.lsa.domain.devices.inca.IncaPropertyFieldInfo]) -> None: ...

class ClientRestParameterService(cern.lsa.client.ParameterService):
    def __init__(self, parameterFeignService: cern.lsa.client.rest.api.v1.feign.ParameterFeignService, toRest: cern.lsa.client.rest.api.v1.mapper.ToRest, fromRest: cern.lsa.client.rest.api.v1.mapper.FromRest): ...
    def addParametersToParameterGroup(self, parameterGroup: cern.lsa.domain.settings.ParameterGroup, collection: java.util.Collection[str]) -> None: ...
    def deleteCriticalProperty(self, propertyVersion: cern.lsa.domain.devices.type.PropertyVersion, device: cern.lsa.domain.devices.Device) -> None: ...
    def deleteParameterGroup(self, long: int) -> None: ...
    def deleteParameterRelations(self, collection: java.util.Collection[cern.lsa.domain.settings.parameter.relation.ParameterRelation]) -> None: ...
    def deleteParameterTypeRelations(self, collection: java.util.Collection[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation]) -> None: ...
    def deleteParameterTypes(self, collection: java.util.Collection[str]) -> None: ...
    def deleteParameters(self, collection: java.util.Collection[str]) -> None: ...
    def findAllAvailableMakerules(self) -> java.util.Set[cern.lsa.domain.trim.rules.makerule.MakeRuleInfo]: ...
    def findAllHierarchies(self) -> java.util.List[str]: ...
    def findAllParameterTypes(self) -> java.util.Set[cern.lsa.domain.settings.ParameterType]: ...
    def findCommonHierarchyNames(self, collection: java.util.Collection[cern.lsa.domain.settings.Parameter]) -> java.util.Set[str]: ...
    def findHierarchyNames(self, collection: java.util.Collection[cern.lsa.domain.settings.Parameter]) -> java.util.Set[str]: ...
    def findMakeRuleForParameterRelation(self, parameterRelation: cern.lsa.domain.settings.parameter.relation.ParameterRelation) -> cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo: ...
    def findParameterByName(self, string: str) -> cern.lsa.domain.settings.Parameter: ...
    def findParameterGroupsByAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.settings.ParameterGroup]: ...
    def findParameterRelationInfos(self, parameterRelationInfosRequest: cern.lsa.domain.settings.parameter.relation.ParameterRelationInfosRequest) -> java.util.Set[cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo]: ...
    def findParameterTrees(self, parameterTreesRequest: cern.lsa.domain.settings.ParameterTreesRequest) -> java.util.Set[cern.lsa.domain.settings.ParameterTreeNode]: ...
    def findParameterTypeRelationInfos(self, parameterTypeRelationInfosRequest: cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfosRequest) -> java.util.Set[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo]: ...
    def findParameterTypes(self, parameterTypesRequest: cern.lsa.domain.settings.ParameterTypesRequest) -> java.util.Set[cern.lsa.domain.settings.ParameterType]: ...
    def findParameters(self, parametersRequest: cern.lsa.domain.settings.ParametersRequest) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def findParametersByDeviceProperty(self, string: str) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def findParametersForEditing(self, parametersRequest: cern.lsa.domain.settings.ParametersRequest) -> java.util.Set[cern.lsa.domain.settings.ParameterForEditing]: ...
    def findParametersInKnobs(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[str]: ...
    def findParametersInWorkingSets(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[str]: ...
    def findParametersWithSettings(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def findParametersWithoutSettings(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getMaxDelta(self, parameter: cern.lsa.domain.settings.Parameter) -> float: ...
    def removeParametersFromParameterGroup(self, parameterGroup: cern.lsa.domain.settings.ParameterGroup, collection: java.util.Collection[str]) -> None: ...
    def saveCriticalProperty(self, propertyVersion: cern.lsa.domain.devices.type.PropertyVersion, device: cern.lsa.domain.devices.Device) -> None: ...
    def saveParameterGroup(self, parameterGroup: cern.lsa.domain.settings.ParameterGroup) -> None: ...
    def saveParameterRelationInfos(self, collection: java.util.Collection[cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo]) -> None: ...
    def saveParameterTypeRelationInfos(self, collection: java.util.Collection[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo]) -> None: ...
    def saveParameterTypes(self, collection: java.util.Collection[cern.lsa.domain.settings.ParameterType]) -> None: ...
    def saveParameters(self, collection: java.util.Collection[cern.lsa.domain.settings.ParameterAttributes]) -> None: ...