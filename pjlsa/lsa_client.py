# -*- coding: utf-8 -*-
'''
PJLSA -- A Python wrapping of Java LSA API

Copyright (c) CERN 2015-2019

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Authors:
    R. De Maria        <riccardo.de.maria@cern.ch>
    M. Hostettler      <michi.hostettler@cern.ch>
    V. Baggiolini      <vito.baggiolini@cern.ch>
    K. Shing Bruce Li  <kevin.shing.bruce.li@cern.ch>
    G. Trad            <georges.trad@cern.ch>
'''

from typing import Iterable, Union, Optional, List
from .util import *
from .jpype_lsa import *


class LsaClient(object):
    def __init__(self, server='gpn', logLevel='INFO'):
        System.setProperty('lsa.server', server)
        setupLog4j(logLevel)
        self._contextService = ServiceLocator.getService(ContextService)
        self._trimService = ServiceLocator.getService(TrimService)
        self._settingService = ServiceLocator.getService(SettingService)
        self._parameterService = ServiceLocator.getService(ParameterService)
        self._contextService = ServiceLocator.getService(ContextService)
        self._lhcService = ServiceLocator.getService(LhcService)
        self._hyperCycleService = ServiceLocator.getService(HyperCycleService)
        self._knobService = ServiceLocator.getService(KnobService)
        self._opticService = ServiceLocator.getService(OpticService)
        self._deviceService = ServiceLocator.getService(DeviceService)
        self._fidelService = ServiceLocator.getService(FidelService)

        self.contextService = LsaContextService(self)


class LsaContextService(object):
    def __init__(self, lsa_client):
        self._lsa = lsa_client

    def findStandAloneBeamProcesses(self, names: Union[str, Iterable[str], None] = None, *,
                                    ids: Union[int, Iterable[int], None] = None,
                                    accelerator: Optional[str] = None, resident: Optional[bool] = None,
                                    multiplexed: Optional[bool] = None) -> List[StandAloneBeamProcess]:
        request = cern.lsa.domain.settings.StandAloneBeamProcessesRequest.builder()
        if names is not None:
            request.addAllBeamProcessNames(toJavaList(names))
        if ids is not None:
            request.addAllIds(toJavaList(ids))
        if accelerator is not None:
            request.accelerator(toAccelerator(accelerator))
        if resident is not None:
            request.resident(java.lang.Boolean(resident))
        if multiplexed is not None:
            request.multiplexed(java.lang.Boolean(multiplexed))
        contexts = self._lsa._contextService.findStandAloneBeamProcesses(request.build())
        return [ctx for ctx in contexts]

    def findStandAloneBeamProcess(self, name: Optional[str] = None, id: Optional[int] = None, *,
                                  accelerator: Optional[str] = None, resident: Optional[bool] = None,
                                  multiplexed: Optional[bool] = None) -> StandAloneBeamProcess:
        bps = self.findStandAloneBeamProcesses(names=name, ids=id, accelerator=accelerator,
                                               resident=resident, multiplexed=multiplexed)
        return onlyElementOf(bps)

    def findStandAloneCycles(self, names: Union[str, Iterable[str], None] = None, *,
                             ids: Union[int, Iterable[int], None] = None,
                             accelerator: Optional[str] = None, resident: Optional[bool] = None,
                             multiplexed: Optional[bool] = None) -> List[StandAloneCycle]:
        request = cern.lsa.domain.settings.StandAloneCyclesRequest.builder()
        if names is not None:
            request.addAllCycleNames(toJavaList(names))
        if ids is not None:
            request.addAllIds(toJavaList(ids))
        if accelerator is not None:
            request.accelerator(toAccelerator(accelerator))
        if resident is not None:
            request.resident(java.lang.Boolean(resident))
        if multiplexed is not None:
            request.multiplexed(java.lang.Boolean(multiplexed))
        contexts = self._lsa._contextService.findStandAloneCycles(request.build())
        return [ctx for ctx in contexts]

    def findStandAloneCycle(self, name: Optional[str] = None, id: Optional[int] = None, *,
                            accelerator: Optional[str] = None, resident: Optional[bool] = None,
                            multiplexed: Optional[bool] = None) -> StandAloneCycle:
        cycles = self.findStandAloneCycles(names=name, ids=id, accelerator=accelerator,
                                           resident=resident, multiplexed=multiplexed)
        return onlyElementOf(cycles)

    def findStandAloneContexts(self, names: Union[str, Iterable[str], None] = None, *,
                               ids: Union[int, Iterable[int], None] = None,
                               accelerator: Optional[str] = None, resident: Optional[bool] = None,
                               multiplexed: Optional[bool] = None) -> List[StandAloneContext]:
        request = cern.lsa.domain.settings.StandAloneContextsRequest.builder()
        if names is not None:
            request.addAllContextNames(toJavaList(names))
        if ids is not None:
            request.addAllIds(toJavaList(ids))
        if accelerator is not None:
            request.accelerator(toAccelerator(accelerator))
        if resident is not None:
            request.resident(java.lang.Boolean(resident))
        if multiplexed is not None:
            request.multiplexed(java.lang.Boolean(multiplexed))
        contexts = self._lsa._contextService.findStandAloneContexts(request.build())
        return [ctx for ctx in contexts]

    def findResidentContexts(self, accelerator: str) -> List[StandAloneContext]:
        return self.findStandAloneContexts(accelerator=accelerator, resident=True)

    def findResidentNonMultiplexedContext(self, accelerator: str) -> StandAloneContext:
        return self._lsa._contextService.findResidentNonMultiplexedContext(toAccelerator(accelerator))

    def findUserContextMappingHistory(self, accelerator: str, contextFamily: str,
                                      fromTime: Union[int, str, datetime],
                                      toTime: Union[int, str, datetime]) -> List[UserContextMapping]:
        mappings = self._lsa._contextService.findUserContextMappingHistory(toAccelerator(accelerator),
                                                                           toEnum(contextFamily, ContextFamily),
                                                                           toJavaDate(fromTime).getTime(),
                                                                           toJavaDate(toTime).getTime())
        return [m for m in mappings]

    def findAcceleratorUsers(self, names: Union[str, Iterable[str], None] = None, *,
                             ids: Union[int, Iterable[int], None] = None,
                             accelerator: Optional[str] = None, userGroup: Optional[str] = None,
                             multiplexed: Optional[bool] = None) -> List[AcceleratorUser]:

        request = cern.lsa.domain.settings.AcceleratorUsersRequest.builder()
        if names is not None:
            request.addAllAcceleratorUserNames(toJavaList(names))
        if ids is not None:
            request.addAllIds(toJavaList(ids))
        if accelerator is not None:
            request.accelerator(toAccelerator(accelerator))
        if userGroup is not None:
            request.acceleratorUserGroupName(userGroup)
        if multiplexed is not None:
            request.multiplexed(java.lang.Boolean(multiplexed))
        users = self._lsa._contextService.findAcceleratorUsers(request.build())
        return [u for u in users]

    def findAcceleratorUser(self, name: Optional[str] = None, *, id: Optional[int] = None,
                            accelerator: Optional[str] = None, userGroup: Optional[str] = None,
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

    def saveContextToUserMapping(self, contexts: Iterable[Context]):
        pass

    def findContextCategories(self):
        pass

    def findDefaultContextCategory(self):
        pass

    def findBeamProcessPurposes(self, accelerator: str):
        pass

    def findDefaultBeamProcessPurpose(self, accelerator: str):
        pass
