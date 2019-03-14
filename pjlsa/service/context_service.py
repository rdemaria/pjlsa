from typing import Iterable, Union, Optional, List
from ..util import *
from .. import _jpype as _jp
from ..domain import *
from datetime import datetime

__all__ = ['LsaContextService']


class LsaContextService(object):
    def __init__(self, lsa_client):
        self._lsa = lsa_client

    def findStandAloneBeamProcesses(self, names: Union[str, Iterable[str], None] = None, *,
                                    ids: Union[int, Iterable[int], None] = None,
                                    accelerator: Union[str, CernAccelerator, None] = None,
                                    resident: Optional[bool] = None,
                                    multiplexed: Optional[bool] = None) -> List[StandAloneBeamProcess]:
        request = _jp.cern.lsa.domain.settings.StandAloneBeamProcessesRequest.builder()
        if names is not None:
            request.addAllBeamProcessNames(_jp.toJavaList(names))
        if ids is not None:
            request.addAllIds(_jp.toJavaList(ids))
        if accelerator is not None:
            request.accelerator(_jp.toAccelerator(accelerator))
        if resident is not None:
            request.resident(_jp.java.lang.Boolean(resident))
        if multiplexed is not None:
            request.multiplexed(_jp.java.lang.Boolean(multiplexed))
        contexts = self._lsa._contextService.findStandAloneBeamProcesses(request.build())
        return [ctx for ctx in contexts]

    def findStandAloneBeamProcess(self, name: Optional[str] = None, id: Optional[int] = None, *,
                                  accelerator: Union[str, CernAccelerator, None] = None,
                                  resident: Optional[bool] = None,
                                  multiplexed: Optional[bool] = None) -> StandAloneBeamProcess:
        bps = self.findStandAloneBeamProcesses(names=name, ids=id, accelerator=accelerator,
                                               resident=resident, multiplexed=multiplexed)
        return onlyElementOf(bps)

    def findStandAloneCycles(self, names: Union[str, Iterable[str], None] = None, *,
                             ids: Union[int, Iterable[int], None] = None,
                             accelerator: Union[str, CernAccelerator, None] = None,
                             resident: Optional[bool] = None,
                             multiplexed: Optional[bool] = None) -> List[StandAloneCycle]:
        request = _jp.cern.lsa.domain.settings.StandAloneCyclesRequest.builder()
        if names is not None:
            request.addAllCycleNames(_jp.toJavaList(names))
        if ids is not None:
            request.addAllIds(_jp.toJavaList(ids))
        if accelerator is not None:
            request.accelerator(_jp.toAccelerator(accelerator))
        if resident is not None:
            request.resident(_jp.java.lang.Boolean(resident))
        if multiplexed is not None:
            request.multiplexed(_jp.java.lang.Boolean(multiplexed))
        contexts = self._lsa._contextService.findStandAloneCycles(request.build())
        return [ctx for ctx in contexts]

    def findStandAloneCycle(self, name: Optional[str] = None, *, id: Optional[int] = None,
                            accelerator: Union[str, CernAccelerator, None] = None,
                            resident: Optional[bool] = None,
                            multiplexed: Optional[bool] = None) -> StandAloneCycle:
        cycles = self.findStandAloneCycles(names=name, ids=id, accelerator=accelerator,
                                           resident=resident, multiplexed=multiplexed)
        return onlyElementOf(cycles)

    def findUserContextMappingHistory(self, *, accelerator: Union[CernAccelerator, str],
                                      contextFamily: Union[str, ContextFamily],
                                      fromTime: Union[int, str, datetime],
                                      toTime: Union[int, str, datetime]) -> List[UserContextMapping]:
        mappings = self._lsa._contextService.findUserContextMappingHistory(_jp.toAccelerator(accelerator),
                                                                           _jp.toJavaEnum(ContextFamily(contextFamily)),
                                                                           _jp.toJavaDate(fromTime).getTime(),
                                                                           _jp.toJavaDate(toTime).getTime())
        return [m for m in mappings]

    def findAcceleratorUsers(self, names: Union[str, Iterable[str], None] = None, *,
                             ids: Union[int, Iterable[int], None] = None,
                             accelerator: Union[str, CernAccelerator, None] = None,
                             userGroup: Optional[str] = None,
                             multiplexed: Optional[bool] = None) -> List[AcceleratorUser]:

        request = _jp.cern.lsa.domain.settings.AcceleratorUsersRequest.builder()
        if names is not None:
            request.addAllAcceleratorUserNames(_jp.toJavaList(names))
        if ids is not None:
            request.addAllIds(_jp.toJavaList(ids))
        if accelerator is not None:
            request.accelerator(_jp.toAccelerator(accelerator))
        if userGroup is not None:
            request.acceleratorUserGroupName(userGroup)
        if multiplexed is not None:
            request.multiplexed(_jp.java.lang.Boolean(multiplexed))
        users = self._lsa._contextService.findAcceleratorUsers(request.build())
        return [u for u in users]

    def findAcceleratorUser(self, name: Optional[str] = None, *, id: Optional[int] = None,
                            accelerator: Union[str, CernAccelerator, None] = None,
                            userGroup: Optional[str] = None,
                            multiplexed: Optional[bool] = None) -> AcceleratorUser:
        users = self.findAcceleratorUsers(names=name, ids=id, accelerator=accelerator, userGroup=userGroup,
                                          multiplexed=multiplexed)
        return onlyElementOf(users)

    def updateContext(self, context: Context) -> None:
        self._lsa._contextService.updateContext(context)

    def findContextByAcceleratorUser(self, user: Union[AcceleratorUser, str]) -> StandAloneContext:
        if isinstance(user, str):
            user = self.findAcceleratorUser(name=user)
        return self._lsa._contextService.findStandAloneContextByAcceleratorUser(user)

    def saveContextToUserMapping(self, contexts: Iterable[Context]) -> None:
        self._lsa._contextService.saveContextToUserMapping(_jp.toJavaList(contexts))

    def findBeamProcessPurposes(self, accelerator: Union[str, CernAccelerator]) -> BeamProcessPurpose:
        purposes = self._lsa._contextService.findBeamProcessPurposes(_jp.toAccelerator(accelerator))
        return [p for p in purposes]

    def findDefaultBeamProcessPurpose(self, accelerator: Union[str, CernAccelerator]) -> BeamProcessPurpose:
        return self._lsa._contextService.findDefaultBeamProcessPurpose(_jp.toAccelerator(accelerator))
