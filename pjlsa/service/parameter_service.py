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
            builder.parameterNames(_jp.toJavaList(names))
        if accelerator is not None:
            builder.accelerator(_jp.toAccelerator(accelerator))

        params = self._lsa._contextService.findParameters(builder.build)
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
        pass

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
        pass

    def findParameterTypes(self, names: Union[str, Iterable[str], None] = None, *,
                           deviceTypes: Union[str, Iterable[str], None] = None) -> List[ParameterType]:
        pass

    def findParameterType(self, name: str) -> Optional[ParameterType]:
        pass

    def findHierarchies(self, parameters: Union[str, Iterable[str], Parameter, Iterable[Parameter]]) -> str:
        pass

    def saveParameters(self, parameterAttributes: Union[ParameterAttributes, Iterable[ParameterAttributes]]) -> None:
        pass

    def saveParameterRelations(self, relations: Mapping[Union[Parameter, str], Iterable[Union[Parameter, str]]], *,
                               hierarchy: str = 'DEFAULT') -> None:
        pass

    def saveParameterTypes(self, types: Union[ParameterType, Iterable[ParameterType]]) -> None:
        pass

    def deleteParameterTypes(self, types: Union[ParameterType, Iterable[ParameterType]]) -> None:
        pass

    def deleteParameters(self, parameters: Union[Parameter, Iterable[Parameter]]) -> None:
        pass

    def findParameterGroups(self, accelerator: Union[str, CernAccelerator]) -> List[ParameterGroup]:
        pass

    def saveParameterGroup(self, parameterGroup: ParameterGroup) -> None:
        pass

    def deleteParameterGroup(self, parameterGroup: ParameterGroup) -> None:
        pass

    def addParametersToParameterGroup(self, parameterGroup: ParameterGroup,
                                      parameters=Union[str, Parameter, Iterable[Union[str, Parameter]]]) -> None:
        pass

    def removeParametersFromParameterGroup(self, parameterGroup: ParameterGroup,
                                           parameters=Union[str, Parameter, Iterable[Union[str, Parameter]]]) -> None:
        pass

    def findMakeRuleForParameterRelation(self, *, source=Union[str, Parameter],
                                         dependent=Union[str, Parameter]) -> MakeRuleConfigStatus:
        pass

    def findSourceParameterTree(self, parameter=Union[str, Parameter]) -> List[ParameterTreeNode]:
        pass

    def findDependentParameterTree(self, parameter=Union[str, Parameter]) -> List[ParameterTreeNode]:
        pass
