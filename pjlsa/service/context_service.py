from datetime import datetime
from typing import Iterable, Union, Optional, List

from .. import _jpype as _jp
from .._util import *
from ..domain import *

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
            request.addAllBeamProcessNames(_jp.to_java_list(names))
        if ids is not None:
            request.addAllIds(_jp.to_java_list(ids))
        if accelerator is not None:
            request.accelerator(_jp.to_accelerator(accelerator))
        if resident is not None:
            request.resident(_jp.java.lang.Boolean(resident))
        if multiplexed is not None:
            request.multiplexed(_jp.java.lang.Boolean(multiplexed))
        contexts = self._lsa._contextService.findStandAloneBeamProcesses(request.build())
        return [ctx for ctx in contexts]

    def findStandAloneBeamProcess(self, name: Optional[str] = None, id: Optional[int] = None, *,
                                  accelerator: Union[str, CernAccelerator, None] = None,
                                  resident: Optional[bool] = None,
                                  multiplexed: Optional[bool] = None) -> Optional[StandAloneBeamProcess]:
        bps = self.findStandAloneBeamProcesses(names=name, ids=id, accelerator=accelerator,
                                               resident=resident, multiplexed=multiplexed)
        return only_element(bps)

    def findStandAloneCycles(self, names: Union[str, Iterable[str], None] = None, *,
                             ids: Union[int, Iterable[int], None] = None,
                             accelerator: Union[str, CernAccelerator, None] = None,
                             resident: Optional[bool] = None,
                             multiplexed: Optional[bool] = None) -> List[StandAloneCycle]:
        request = _jp.cern.lsa.domain.settings.StandAloneCyclesRequest.builder()
        if names is not None:
            request.addAllCycleNames(_jp.to_java_list(names))
        if ids is not None:
            request.addAllIds(_jp.to_java_list(ids))
        if accelerator is not None:
            request.accelerator(_jp.to_accelerator(accelerator))
        if resident is not None:
            request.resident(_jp.java.lang.Boolean(resident))
        if multiplexed is not None:
            request.multiplexed(_jp.java.lang.Boolean(multiplexed))
        contexts = self._lsa._contextService.findStandAloneCycles(request.build())
        return [ctx for ctx in contexts]

    def findStandAloneCycle(self, name: Optional[str] = None, *, id: Optional[int] = None,
                            accelerator: Union[str, CernAccelerator, None] = None,
                            resident: Optional[bool] = None,
                            multiplexed: Optional[bool] = None) -> Optional[StandAloneCycle]:
        cycles = self.findStandAloneCycles(names=name, ids=id, accelerator=accelerator,
                                           resident=resident, multiplexed=multiplexed)
        return only_element(cycles)

    def findUserContextMappingHistory(self, *, accelerator: Union[CernAccelerator, str],
                                      contextFamily: Union[str, ContextFamily],
                                      fromTime: Union[int, str, datetime],
                                      toTime: Union[int, str, datetime]) -> List[UserContextMapping]:
        mappings = self._lsa._contextService.findUserContextMappingHistory(_jp.to_accelerator(accelerator),
                                                                           _jp.to_java_enum(
                                                                               ContextFamily(contextFamily)),
                                                                           _jp.to_java_date(fromTime).getTime(),
                                                                           _jp.to_java_date(toTime).getTime())
        return [m for m in mappings]

    def findAcceleratorUsers(self, names: Union[str, Iterable[str], None] = None, *,
                             ids: Union[int, Iterable[int], None] = None,
                             accelerator: Union[str, CernAccelerator, None] = None,
                             userGroup: Optional[str] = None,
                             multiplexed: Optional[bool] = None) -> List[AcceleratorUser]:

        request = _jp.cern.lsa.domain.settings.AcceleratorUsersRequest.builder()
        if names is not None:
            request.addAllAcceleratorUserNames(_jp.to_java_list(names))
        if ids is not None:
            request.addAllIds(_jp.to_java_list(ids))
        if accelerator is not None:
            request.accelerator(_jp.to_accelerator(accelerator))
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
        return only_element(users)

    def updateContext(self, context: Context) -> None:
        self._lsa._contextService.updateContext(context)

    def findContextByAcceleratorUser(self, user: Union[AcceleratorUser, str]) -> StandAloneContext:
        return self._lsa._contextService.findStandAloneContextByAcceleratorUser(self._resolve_user(user))

    def saveContextToUserMapping(self, contexts: Iterable[Context]) -> None:
        self._lsa._contextService.saveContextToUserMapping(_jp.to_java_list(contexts))

    def findBeamProcessPurposes(self, accelerator: Union[str, CernAccelerator]) -> BeamProcessPurpose:
        purposes = self._lsa._contextService.findBeamProcessPurposes(_jp.to_accelerator(accelerator))
        return [p for p in purposes]

    def findDefaultBeamProcessPurpose(self, accelerator: Union[str, CernAccelerator]) -> BeamProcessPurpose:
        return self._lsa._contextService.findDefaultBeamProcessPurpose(_jp.to_accelerator(accelerator))

    def _resolve_user(self, user: Union[str, AcceleratorUser]):
        if isinstance(user, AcceleratorUser):
            return user
        acc_user = self.findAcceleratorUser(name=user)
        if acc_user is None:
            raise ValueError('User {0} not found.'.format(user))
        else:
            return acc_user

    def _resolve_contexts(self, ctxs: Union[str, Iterable[str], Context, Iterable[Context]]):
        if isinstance(ctxs, str) or isinstance(ctxs, Context):
            ctxs = [ctxs]
        ctx_objs = {p for p in ctxs if isinstance(p, Context)}
        ctx_names = {p for p in ctxs if not isinstance(p, Context)}
        found_bps = set(self.findStandAloneBeamProcesses(names=ctx_names)) if len(ctx_names) > 0 else set()
        found_cycles = set(self.findStandAloneCycles(names=ctx_names)) if len(ctx_names) > 0 else set()
        found_ctxs = found_cycles | found_bps
        if len(found_ctxs) < len(ctx_names):
            found_ctx_names = {p.name for p in found_ctxs}
            missing_ctx_names = ctx_names - found_ctx_names
            raise ValueError('Contexts [{0}] not found.'.format(','.join(missing_ctx_names)))
        ctx_objs.update(found_ctxs)
        return _jp.to_java_list(ctx_objs)

    def _resolve_context(self, ctx: Union[str, Context]):
        if isinstance(ctx, Context):
            return ctx
        else:
            cycle = self.findStandAloneCycle(ctx)
            bp = self.findStandAloneBeamProcess(ctx)
            if bp is None and cycle is None:
                raise ValueError('Context {0} not found.'.format(ctx))
            elif bp is not None:
                return bp
            else:
                return cycle