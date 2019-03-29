from typing import Iterable, Union, Optional, List, Mapping

from .. import _jpype as _jp
from .._util import *
from ..domain import *

__all__ = ['LsaParameterService']


class LsaParameterService(object):
    def __init__(self, lsa_client):
        self._lsa = lsa_client

    def findParameters(self, names: Union[str, Iterable[str], None] = None, *,
                       accelerator: Union[str, CernAccelerator, None] = None,
                       acceleratorZones: Union[
                           str, Iterable[str], AcceleratorZone, Iterable[AcceleratorZone], None] = None,
                       particleTransfers: Union[
                           str, Iterable[str], ParticleTransfer, Iterable[ParticleTransfer], None] = None,
                       parameterTypes: Union[str, Iterable[str], ParameterType, Iterable[ParameterType], None] = None,
                       parameterGroups: Union[
                           str, Iterable[str], ParameterGroup, Iterable[ParameterGroup], None] = None,
                       devices: Union[str, Iterable[str], None] = None,
                       properties: Union[str, Iterable[str], None] = None,
                       multiplexed: Optional[bool] = None,
                       virtual: Optional[bool] = None,
                       writable: Optional[bool] = None,
                       readable: Optional[bool] = None,
                       namePattern: Optional[str] = None,
                       critical: Optional[bool] = None) -> List[Parameter]:
        builder = _jp.cern.lsa.domain.settings.ParametersRequest.builder()
        if names is not None:
            builder.setParameterNames(_jp.to_java_list(names))
        if accelerator is not None:
            builder.setAccelerator(_jp.to_accelerator(accelerator))
        if acceleratorZones is not None:
            builder.setAcceleratorZones(_jp.to_java_list(acceleratorZones, converter=AcceleratorZone.of))
        if particleTransfers is not None:
            builder.setParticleTransfers(_jp.to_java_list(particleTransfers, converter=ParticleTransfer.of))
        if parameterTypes is not None:
            builder.setParameterTypeNames(_jp.to_java_list(parameterTypes, converter=str))
        if parameterGroups is not None:
            builder.setParameterGroups(_jp.to_java_list(parameterGroups, converter=str))
        if devices is not None:
            builder.setDeviceNames(_jp.to_java_list(devices))
        if properties is not None:
            builder.setPropertyNames(_jp.to_java_list(properties))
        if multiplexed is not None:
            builder.setMultiplexed(_jp.java.lang.Boolean(multiplexed))
        if virtual is not None:
            builder.setVirtual(_jp.java.lang.Boolean(virtual))
        if writable is not None:
            builder.setWritable(_jp.java.lang.Boolean(writable))
        if readable is not None:
            builder.setReadable(_jp.java.lang.Boolean(readable))
        if critical is not None:
            builder.setCritical(_jp.java.lang.Boolean(critical))
        if namePattern is not None:
            builder.setParameterNamePattern(namePattern)

        params = self._lsa._parameterService.findParameters(builder.build())
        return list(params)

    def findParameter(self, name: Optional[str] = None, *,
                      accelerator: Union[str, CernAccelerator, None] = None,
                      acceleratorZone: Union[str, AcceleratorZone, None] = None,
                      particleTransfer: Union[str, ParticleTransfer, None] = None,
                      parameterType: Union[str, ParameterType, None] = None,
                      parameterGroup: Optional[str] = None,
                      device: Optional[str] = None,
                      property: Optional[str] = None,
                      multiplexed: Optional[bool] = None,
                      virtual: Optional[bool] = None,
                      writable: Optional[bool] = None,
                      readable: Optional[bool] = None,
                      namePattern: Optional[str] = None,
                      critical: Optional[bool] = None) -> Optional[Parameter]:
        params = self.findParameters(names=name, accelerator=accelerator, acceleratorZones=acceleratorZone,
                                     particleTransfers=particleTransfer, parameterTypes=parameterType,
                                     parameterGroups=parameterGroup, devices=device, properties=property,
                                     multiplexed=multiplexed, virtual=virtual, writable=writable, readable=readable,
                                     namePattern=namePattern, critical=critical)
        return only_element(params)

    def findParametersForEditing(self, names: Union[str, Iterable[str], None] = None, *,
                                 accelerator: Union[str, CernAccelerator, None] = None,
                                 acceleratorZones: Union[
                                     str, Iterable[str], AcceleratorZone, Iterable[AcceleratorZone], None] = None,
                                 particleTransfers: Union[
                                     str, Iterable[str], ParticleTransfer, Iterable[ParticleTransfer], None] = None,
                                 parameterTypes: Union[
                                     str, Iterable[str], ParameterType, Iterable[ParameterType], None] = None,
                                 parameterGroups: Union[
                                     str, Iterable[str], ParameterGroup, Iterable[ParameterGroup], None] = None,
                                 devices: Union[str, Iterable[str], None] = None,
                                 properties: Union[str, Iterable[str], None] = None,
                                 multiplexed: Optional[bool] = None,
                                 virtual: Optional[bool] = None,
                                 writable: Optional[bool] = None,
                                 readable: Optional[bool] = None,
                                 namePattern: Optional[str] = None,
                                 critical: Optional[bool] = None) -> List[ParameterForEditing]:
        builder = _jp.cern.lsa.domain.settings.ParametersRequest.builder()
        if names is not None:
            builder.setParameterNames(_jp.to_java_list(names))
        if accelerator is not None:
            builder.setAccelerator(_jp.to_accelerator(accelerator))
        if acceleratorZones is not None:
            builder.setAcceleratorZones(_jp.to_java_list(acceleratorZones, converter=AcceleratorZone.of))
        if particleTransfers is not None:
            builder.setParticleTransfers(_jp.to_java_list(particleTransfers, converter=ParticleTransfer.of))
        if parameterTypes is not None:
            builder.setParameterTypeNames(_jp.to_java_list(parameterTypes, converter=str))
        if parameterGroups is not None:
            builder.setParameterGroups(_jp.to_java_list(parameterGroups, converter=str))
        if devices is not None:
            builder.setDeviceNames(_jp.to_java_list(devices))
        if properties is not None:
            builder.setPropertyNames(_jp.to_java_list(properties))
        if multiplexed is not None:
            builder.setMultiplexed(_jp.java.lang.Boolean(multiplexed))
        if virtual is not None:
            builder.setVirtual(_jp.java.lang.Boolean(virtual))
        if writable is not None:
            builder.setWritable(_jp.java.lang.Boolean(writable))
        if readable is not None:
            builder.setReadable(_jp.java.lang.Boolean(readable))
        if critical is not None:
            builder.setCritical(_jp.java.lang.Boolean(critical))
        if namePattern is not None:
            builder.setParameterNamePattern(namePattern)

        params = self._lsa._parameterService.findParametersForEditing(builder.build())
        return list(params)

    def findParameterTypes(self, names: Union[str, Iterable[str], None] = None, *,
                           deviceTypes: Union[str, Iterable[str], None] = None) -> List[ParameterType]:
        builder = _jp.cern.lsa.domain.settings.ParameterTypesRequest.builder()
        if names is None and deviceTypes is None:
            param_types = self._lsa._parameterService.findParameterTypes(builder.ALL_PARAMETER_TYPES)
        elif names is not None:
            builder.setParameterTypeNames(_jp.to_java_list(names))
            param_types = self._lsa._parameterService.findParameterTypes(builder.build())
        elif deviceTypes is not None:
            builder.setDeviceTypeNames(_jp.to_java_list(deviceTypes))
            param_types = self._lsa._parameterService.findParameterTypes(builder.build())
        else:
            raise ValueError("Invalid arguments")
        return list(param_types)

    def findParameterType(self, name: str) -> Optional[ParameterType]:
        return only_element(self.findParameterTypes(name))

    def findHierarchies(self, parameters: Union[str, Iterable[str], Parameter, Iterable[Parameter]]) -> List[str]:
        hierarchies = self._lsa._parameterService.findHierarchyNames(self._resolve_params(parameters))
        return list(hierarchies)

    def saveParameters(self, parameterAttributes: Union[ParameterAttributes, Iterable[ParameterAttributes]]) -> None:
        self._lsa._parameterService.saveParameters(_jp.to_java_list(parameterAttributes))

    def saveParameterRelations(self, relations: Mapping[Union[Parameter, str], Iterable[Union[Parameter, str]]], *,
                               hierarchy: str = 'DEFAULT') -> None:
        param_objs = {p for p in relations.keys() if isinstance(p, Parameter)}
        param_objs.update({p for pr in relations.values() for p in pr if isinstance(p, Parameter)})
        param_names = {p for p in relations.keys() if not isinstance(p, Parameter)}
        param_names.update({p for pr in relations.values() for p in pr if not isinstance(p, Parameter)})
        param_objs.update(self.findParameters(names=param_names))
        param_lookup = {p.name: p for p in param_objs}
        param_lookup.update({p: p for p in param_objs})
        resolved_relations = {param_lookup[p]: [param_lookup[dp] for dp in pr] for p, pr in relations.items()}
        self._lsa._parameterService.saveParameterRelations(_jp.python_to_java(resolved_relations), hierarchy)

    def saveParameterTypes(self, types: Union[ParameterType, Iterable[ParameterType]]) -> None:
        self._lsa._parameterService.saveParameterTypes(_jp.to_java_list(types))

    def deleteParameterTypes(self, types: Union[ParameterType, Iterable[ParameterType]]) -> None:
        self._lsa._parameterService.deleteParameterTypes(_jp.to_java_list(types))

    def deleteParameters(self, parameters: Union[Parameter, Iterable[Parameter]]) -> None:
        self._lsa._parameterService.deleteParameters(_jp.to_java_list(parameters))

    def findParameterGroups(self, accelerator: Union[str, CernAccelerator]) -> List[ParameterGroup]:
        param_groups = self._lsa._parameterService.findParameterGroupsByAccelerator(_jp.to_accelerator(accelerator))
        return list(param_groups)

    def saveParameterGroup(self, parameterGroup: ParameterGroup) -> None:
        self._lsa._parameterService.saveParameterGroup(parameterGroup)

    def deleteParameterGroup(self, parameterGroup: ParameterGroup) -> None:
        self._lsa._parameterService.deleteParameterGroup(parameterGroup.id)

    def addParametersToParameterGroup(self, parameterGroup: ParameterGroup,
                                      parameters: Union[str, Parameter, Iterable[Union[str, Parameter]]]) -> None:
        if isinstance(parameters, str) or isinstance(parameters, Parameter):
            parameters = [parameters]
        parameters = [p.name if isinstance(p, Parameter) else p for p in parameters]
        self._lsa._parameterService.addParametersToParameterGroup(parameterGroup, _jp.to_java_list(parameters))

    def removeParametersFromParameterGroup(self, parameterGroup: ParameterGroup,
                                           parameters: Union[str, Parameter, Iterable[Union[str, Parameter]]]) -> None:
        if isinstance(parameters, str) or isinstance(parameters, Parameter):
            parameters = [parameters]
        parameters = [p.name if isinstance(p, Parameter) else p for p in parameters]
        self._lsa._parameterService.removeParametersFromParameterGroup(parameterGroup, _jp.to_java_list(parameters))

    def findMakeRuleForParameterRelation(self, *, source: Union[str, Parameter],
                                         dependent: Union[str, Parameter]) -> MakeRuleForParameterRelation:
        builder = _jp.cern.lsa.domain.settings.parameter.relation.MakeRuleForParameterRelationRequest.builder()
        builder.sourceParameterName(source.name if isinstance(source, Parameter) else source)
        builder.dependentParameterName(dependent.name if isinstance(dependent, Parameter) else dependent)
        return self._lsa._parameterService.findMakeRuleForParameterRelation(builder.build())

    def findSourceParameterTree(self, parameter: Union[str, Parameter], *,
                                hierarchy: str = 'DEFAULT') -> List[ParameterTreeNode]:
        builder = _jp.cern.lsa.domain.settings.factory.ParameterTreesRequestBuilder
        param_name = parameter.name if isinstance(parameter, Parameter) else parameter
        req = builder.byParameterAndHierarchyFindSourceTrees(param_name, hierarchy)
        return only_element(list(self._lsa._parameterService.findParameterTrees(req)))

    def findDependentParameterTree(self, parameter=Union[str, Parameter],
                                   hierarchy: str = 'DEFAULT') -> List[ParameterTreeNode]:
        builder = _jp.cern.lsa.domain.settings.factory.ParameterTreesRequestBuilder
        param_name = parameter.name if isinstance(parameter, Parameter) else parameter
        req = builder.byParameterAndHierarchyFindDependentTrees(param_name, hierarchy)
        return only_element(list(self._lsa._parameterService.findParameterTrees(req)))

    def _resolve_params(self, parameters: Union[str, Iterable[str], Parameter, Iterable[Parameter]]):
        if isinstance(parameters, str) or isinstance(parameters, Parameter):
            parameters = [parameters]
        param_objs = {p for p in parameters if isinstance(p, Parameter)}
        param_names = {p for p in parameters if not isinstance(p, Parameter)}
        found_params = self.findParameters(names=param_names) if len(param_names) > 0 else []
        if len(found_params) < len(param_names):
            found_param_names = {p.name for p in found_params}
            missing_param_names = param_names - found_param_names
            raise ValueError('Parameters [{0}] not found.'.format(','.join(missing_param_names)))
        param_objs.update(found_params)
        return _jp.to_java_list(param_objs)

    def _resolve_param(self, parameter: Union[str, Parameter]):
        if isinstance(parameter, Parameter):
            return parameter
        else:
            param = self.findParameter(parameter)
            if param is None:
                raise ValueError('Parameter {0} not found.'.format(parameter))
            else:
                return param
