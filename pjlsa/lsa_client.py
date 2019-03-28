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

from . import _jpype as _jp
from . import service as _svc


class LsaClient(object):
    def __init__(self, server='gpn', logLevel='INFO'):
        _jp.System.setProperty('lsa.server', server)
        _jp.setup_log4j(logLevel)
        self._contextService = _jp.ServiceLocator.getService(_jp.ContextService)
        self._trimService = _jp.ServiceLocator.getService(_jp.TrimService)
        self._settingService = _jp.ServiceLocator.getService(_jp.SettingService)
        self._parameterService = _jp.ServiceLocator.getService(_jp.ParameterService)
        self._contextService = _jp.ServiceLocator.getService(_jp.ContextService)
        self._lhcService = _jp.ServiceLocator.getService(_jp.LhcService)
        self._hyperCycleService = _jp.ServiceLocator.getService(_jp.HyperCycleService)
        self._knobService = _jp.ServiceLocator.getService(_jp.KnobService)
        self._opticService = _jp.ServiceLocator.getService(_jp.OpticService)
        self._deviceService = _jp.ServiceLocator.getService(_jp.DeviceService)
        self._fidelService = _jp.ServiceLocator.getService(_jp.FidelService)

        self.contextService = _svc.LsaContextService(self)
        self.parameterService = _svc.LsaParameterService(self)
        self.settingService = _svc.LsaSettingService(self)
