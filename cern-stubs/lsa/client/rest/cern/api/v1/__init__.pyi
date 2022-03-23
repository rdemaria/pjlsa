import cern.accsoft.commons.domain
import cern.lsa.client
import cern.lsa.client.rest.api.v1
import cern.lsa.client.rest.api.v1.mapper
import cern.lsa.client.rest.cern.api.v1.feign
import cern.lsa.domain.devices
import cern.lsa.domain.devices.inca
import cern.lsa.domain.devices.type
import cern.lsa.domain.settings
import cern.lsa.domain.settings.parameter.relation
import cern.lsa.domain.settings.parameter.type.relation
import cern.lsa.domain.trim.rules.makerule
import java.util
import typing



class CernClientRestConfig(cern.lsa.client.rest.api.v1.AbstractClientRestConfig):
    """
    @Configuration @PropertySource(value="classpath:${lsa.server.properties}", ignoreResourceNotFound=true) public class CernClientRestConfig extends cern.lsa.client.rest.api.v1.AbstractClientRestConfig
    """
    def __init__(self): ...

class ClientRestIncaService(cern.lsa.client.IncaService):
    """
    public class ClientRestIncaService extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.lsa.client.IncaService
    """
    def __init__(self, incaFeignService: cern.lsa.client.rest.cern.api.v1.feign.IncaFeignService, toDto: cern.lsa.client.rest.api.v1.mapper.ToDto, fromDto: cern.lsa.client.rest.api.v1.mapper.FromDto): ...
    def findIncaPropertyFieldInfos(self, incaPropertyFieldInfosRequest: cern.lsa.domain.devices.inca.IncaPropertyFieldInfosRequest) -> java.util.Set[cern.lsa.domain.devices.inca.IncaPropertyFieldInfo]: ...
    def saveIncaPropertyFieldInfos(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.devices.inca.IncaPropertyFieldInfo], typing.Sequence[cern.lsa.domain.devices.inca.IncaPropertyFieldInfo]]) -> None: ...

class ClientRestParameterService(cern.lsa.client.ParameterService):
    """
    public class ClientRestParameterService extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.lsa.client.ParameterService
    """
    def __init__(self, parameterFeignService: cern.lsa.client.rest.cern.api.v1.feign.ParameterFeignService, toDto: cern.lsa.client.rest.api.v1.mapper.ToDto, fromDto: cern.lsa.client.rest.api.v1.mapper.FromDto): ...
    def addParametersToParameterGroup(self, parameterGroup: cern.lsa.domain.settings.ParameterGroup, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> None: ...
    def deleteCriticalProperty(self, propertyVersion: cern.lsa.domain.devices.type.PropertyVersion, device: cern.lsa.domain.devices.Device) -> None:
        """
        
            Specified by:
                :code:`deleteCriticalProperty` in interface :code:`cern.lsa.client.common.CommonParameterService`
        
        
        """
        ...
    def deleteParameterGroup(self, long: int) -> None:
        """
        
            Specified by:
                :code:`deleteParameterGroup` in interface :code:`cern.lsa.client.common.CommonParameterService`
        
        
        """
        ...
    def deleteParameterRelations(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.parameter.relation.ParameterRelation], typing.Sequence[cern.lsa.domain.settings.parameter.relation.ParameterRelation]]) -> None: ...
    def deleteParameterTypeRelations(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation], typing.Sequence[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation]]) -> None: ...
    def deleteParameterTypes(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> None: ...
    def deleteParameters(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> None: ...
    def findAllAvailableMakerules(self) -> java.util.Set[cern.lsa.domain.trim.rules.makerule.MakeRuleInfo]: ...
    def findAllHierarchies(self) -> java.util.List[str]: ...
    def findAllParameterTypes(self) -> java.util.Set[cern.lsa.domain.settings.ParameterType]: ...
    def findCommonHierarchyNames(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> java.util.Set[str]: ...
    def findHierarchyNames(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> java.util.Set[str]: ...
    def findMakeRuleForParameterRelation(self, parameterRelation: cern.lsa.domain.settings.parameter.relation.ParameterRelation) -> cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo:
        """
        
            Specified by:
                :code:`findMakeRuleForParameterRelation` in interface :code:`cern.lsa.client.common.CommonParameterService`
        
        
        """
        ...
    def findParameterByName(self, string: str) -> cern.lsa.domain.settings.Parameter:
        """
        
            Specified by:
                :code:`findParameterByName` in interface :code:`cern.lsa.client.common.CommonParameterService`
        
        
        """
        ...
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
    def getMaxDelta(self, parameter: cern.lsa.domain.settings.Parameter) -> float:
        """
        
            Specified by:
                :code:`getMaxDelta` in interface :code:`cern.lsa.client.common.CommonParameterService`
        
        
        """
        ...
    def removeParametersFromParameterGroup(self, parameterGroup: cern.lsa.domain.settings.ParameterGroup, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> None: ...
    def saveCriticalProperty(self, propertyVersion: cern.lsa.domain.devices.type.PropertyVersion, device: cern.lsa.domain.devices.Device) -> None:
        """
        
            Specified by:
                :code:`saveCriticalProperty` in interface :code:`cern.lsa.client.common.CommonParameterService`
        
        
        """
        ...
    def saveParameterGroup(self, parameterGroup: cern.lsa.domain.settings.ParameterGroup) -> None:
        """
        
            Specified by:
                :code:`saveParameterGroup` in interface :code:`cern.lsa.client.common.CommonParameterService`
        
        
        """
        ...
    def saveParameterRelationInfos(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo], typing.Sequence[cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo]]) -> None: ...
    def saveParameterTypeRelationInfos(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo], typing.Sequence[cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo]]) -> None: ...
    def saveParameterTypes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.ParameterType], typing.Sequence[cern.lsa.domain.settings.ParameterType]]) -> None: ...
    def saveParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.ParameterAttributes], typing.Sequence[cern.lsa.domain.settings.ParameterAttributes]]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.cern.api.v1")``.

    CernClientRestConfig: typing.Type[CernClientRestConfig]
    ClientRestIncaService: typing.Type[ClientRestIncaService]
    ClientRestParameterService: typing.Type[ClientRestParameterService]
    feign: cern.lsa.client.rest.cern.api.v1.feign.__module_protocol__
