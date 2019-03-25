from typing import Iterable, Union, Optional, List, Mapping
from ..util import *
from .. import _jpype as _jp
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
            builder.setParameterNames(_jp.toJavaList(names))
        if accelerator is not None:
            builder.setAccelerator(_jp.toAccelerator(accelerator))
        if acceleratorZones is not None:
            builder.setAcceleratorZones(_jp.toJavaList(acceleratorZones, converter=AcceleratorZone.of))
        if particleTransfers is not None:
            builder.setParticleTransfers(_jp.toJavaList(particleTransfers, converter=ParticleTransfer.of))
        if parameterTypes is not None:
            builder.setParameterTypes(_jp.toJavaList(parameterTypes, converter=str))
        if parameterGroups is not None:
            builder.setParameterGroups(_jp.toJavaList(parameterGroups, converter=str))
        if devices is not None:
            builder.setDeviceNames(_jp.toJavaList(devices))
        if properties is not None:
            builder.setPropertyNames(_jp.toJavaList(properties))
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
        return onlyElementOf(params)

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
            builder.setParameterNames(_jp.toJavaList(names))
        if accelerator is not None:
            builder.setAccelerator(_jp.toAccelerator(accelerator))
        if acceleratorZones is not None:
            builder.setAcceleratorZones(_jp.toJavaList(acceleratorZones, converter=AcceleratorZone.of))
        if particleTransfers is not None:
            builder.setParticleTransfers(_jp.toJavaList(particleTransfers, converter=ParticleTransfer.of))
        if parameterTypes is not None:
            builder.setParameterTypes(_jp.toJavaList(parameterTypes, converter=str))
        if parameterGroups is not None:
            builder.setParameterGroups(_jp.toJavaList(parameterGroups, converter=str))
        if devices is not None:
            builder.setDeviceNames(_jp.toJavaList(devices))
        if properties is not None:
            builder.setPropertyNames(_jp.toJavaList(properties))
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
            builder.setAllParameterTypesRequested(True)
        if names is not None:
            builder.setParameterTypeNames(_jp.toJavaList(names))
        if names is not None:
            builder.setDeviceTypeNames(_jp.toJavaList(deviceTypes))
        param_types = self._lsa._parameterService.findParameterTypes(builder.build())
        return list(param_types)

    def findParameterType(self, name: str) -> Optional[ParameterType]:
        return onlyElementOf(self.findParameterTypes(name))

    def findHierarchies(self, parameters: Union[str, Iterable[str], Parameter, Iterable[Parameter]]) -> List[str]:
        if isinstance(parameters, str) or isinstance(parameters, Parameter):
            parameters = [parameters]
        parameters = set(parameters)
        param_names = {p for p in parameters if not isinstance(p, Parameter)}
        parameters -= param_names
        found_params = self.findParameterTypes(names=param_names)
        parameters.update(found_params)
        hierarchies = self._lsa._parameterService.findHierarchyNames(_jp.toJavaList(parameters))
        return list(hierarchies)

    def saveParameters(self, parameterAttributes: Union[ParameterAttributes, Iterable[ParameterAttributes]]) -> None:
        self._lsa.saveParameters(_jp.toJavaList(parameterAttributes))

    def saveParameterRelations(self, relations: Mapping[Union[Parameter, str], Iterable[Union[Parameter, str]]], *,
                               hierarchy: str = 'DEFAULT') -> None:
        resolved_params = {p for p in relations.keys() if isinstance(p, Parameter)}
        resolved_params.update({p for pr in relations.values() for p in pr if isinstance(p, Parameter)})
        unresolved_params = {p for p in relations.keys() if not isinstance(p, Parameter)}
        unresolved_params.update({p for pr in relations.values() for p in pr if not isinstance(p, Parameter)})
        resolved_params.update(self.findParameterTypes(names=unresolved_params))
        param_lookup = {p.name: p for p in resolved_params}
        param_lookup.update({p: p for p in resolved_params})
        resolved_relations = {param_lookup[p]: [param_lookup[dp] for dp in pr] for p, pr in relations}
        self._lsa._parameterService.saveParameterRelations(_jp.pythonToJava(resolved_relations), hierarchy)

    def saveParameterTypes(self, types: Union[ParameterType, Iterable[ParameterType]]) -> None:
        self._lsa._parameterService.saveParameterTypes(_jp.toJavaList(types))

    def deleteParameterTypes(self, types: Union[ParameterType, Iterable[ParameterType]]) -> None:
        self._lsa._parameterService.deleteParameterTypes(_jp.toJavaList(types))

    def deleteParameters(self, parameters: Union[Parameter, Iterable[Parameter]]) -> None:
        self._lsa._parameterService.deleteParameters(_jp.toJavaList(parameters))

    def findParameterGroups(self, accelerator: Union[str, CernAccelerator]) -> List[ParameterGroup]:
        param_groups = self._lsa._parameterService.findParameterGroups(_jp.toAccelerator(accelerator))
        return list(param_groups)

    def saveParameterGroup(self, parameterGroup: ParameterGroup) -> None:
        self._lsa.saveParameterGroup(parameterGroup)

    def deleteParameterGroup(self, parameterGroup: ParameterGroup) -> None:
        self._lsa.deleteParameterGroup(parameterGroup)

    def addParametersToParameterGroup(self, parameterGroup: ParameterGroup,
                                      parameters: Union[str, Parameter, Iterable[Union[str, Parameter]]]) -> None:
        pass

    def removeParametersFromParameterGroup(self, parameterGroup: ParameterGroup,
                                           parameters: Union[str, Parameter, Iterable[Union[str, Parameter]]]) -> None:
        pass

    def findMakeRuleForParameterRelation(self, *, source: Union[str, Parameter],
                                         dependent: Union[str, Parameter]) -> MakeRuleConfigStatus:
        pass

    def findSourceParameterTree(self, parameter: Union[str, Parameter]) -> List[ParameterTreeNode]:
        pass

    def findDependentParameterTree(self, parameter=Union[str, Parameter]) -> List[ParameterTreeNode]:
        pass
