# -*- coding: utf-8 -*-
"""
PJLSA -- A Python wrapping of Java LSA API

Copyright (c) CERN 2015-2017

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
R. De Maria     <riccardo.de.maria@cern.ch>
M. Hostettler   <michi.hostettler@cern.ch>
V. Baggiolini   <vito.baggiolini@cern.ch>


Code conventions:
*   methods uses camelCase
*   Classes uses Capital

*   _<method> returns java types and return java types
*   <method> take python types or java types and return python types
"""

import os
import re
from collections import namedtuple
import datetime
from contextlib import contextmanager

import numpy as np
import six
import jpype

import cmmnbuild_dep_manager

# Python data descriptors
TrimHeader = namedtuple(
    "TrimHeader", ["id", "beamProcesses", "createdDate", "description", "clientInfo"],
)
OpticTableItem = namedtuple("OpticTableItem", ["time", "id", "name"])
TrimTuple = namedtuple("TrimTuple", ["time", "data"])
Calibration = namedtuple("Calibration", ["field", "current", "fieldtype", "name"])
PCInfo = namedtuple(
    "PCInfo",
    [
        "accelerationLimit",
        "decelerationLimit",
        "didtMin",
        "didtMax",
        "iMinOp",
        "iNom",
        "iPNo",
        "iUlt",
        "polaritySwitch",
    ],
)

Context = namedtuple("Context", ["timestamp", "name", "user"])


def _build_TrimHeader(th):
    return TrimHeader(
        id=th.getId(),
        beamProcesses=[str(bp) for bp in th.getBeamProcesses()],
        createdDate=datetime.datetime.fromtimestamp(
            th.getCreatedDate().getTime() / 1000
        ),
        description=th.getDescription(),
        clientInfo=th.getClientInfo(),
    )


def _toJavaDate(t):
    """Date from string, datetime, unixtimestamp to java date
    """
    Date = jpype.java.util.Date
    if isinstance(t, six.string_types):
        return jpype.java.sql.Timestamp.valueOf(t)
    elif isinstance(t, datetime.datetime):
        return jpype.java.sql.Timestamp.valueOf(t.strftime("%Y-%m-%d %H:%M:%S.%f"))
    elif t is None:
        return None
    elif isinstance(t, Date):
        return t
    else:
        return Date(int(t * 1000))


def _toJavaList(lst):
    res = jpype.java.util.LinkedList()
    for ii in lst:
        res.add(ii)
    return res


class LSAClient(object):
    def __init__(self, server="gpn"):
        self._mgr = cmmnbuild_dep_manager.Manager("pjlsa")
        self._jpype = self._mgr.start_jpype_jvm()

        # basic Java packages
        self._cern = jpype.JPackage("cern")
        self._org = jpype.JPackage("org")
        self._java = jpype.JPackage("java")
        self._System = self._java.lang.System

        null = self._org.apache.log4j.varia.NullAppender()
        self._org.apache.log4j.BasicConfigurator.configure(null)

        # System.setProperty("lsa.mode", "3")

        self._lsa = self._cern.lsa
        self._client = self._lsa.client
        self._domain = self._lsa.domain

        # Java classes
        self._ContextService = self._client.ContextService
        self._HyperCycleService = self._client.HyperCycleService
        self._ParameterService = self._client.ParameterService
        self._ServiceLocator = self._client.ServiceLocator
        self._SettingService = self._client.SettingService
        self._TrimService = self._client.TrimService
        self._LhcService = self._client.LhcService
        self._FidelService = self._client.FidelService
        self._KnobService = self._client.KnobService
        self._OpticService = self._client.OpticService
        self._DeviceService = self._client.DeviceService

        self._BeamProcess = self._domain.settings.BeamProcess
        self._Cycle = self._domain.settings.Cycle
        self._ContextSettings = self._domain.settings.ContextSettings
        self._ContextFamily = self._domain.settings.ContextFamily
        self._HyperCycle = self._domain.settings.HyperCycle
        self._Parameter = self._domain.settings.Parameter
        self._ParameterSettings = self._domain.settings.ParameterSettings
        self._Setting = self._domain.settings.Setting
        self._StandAloneBeamProcess = self._domain.settings.StandAloneBeamProcess
        self._Knob = self._domain.settings.Knob
        self._FunctionSetting = self._domain.settings.spi.FunctionSetting
        self._ScalarSetting = self._domain.settings.spi.ScalarSetting

        self._ParametersRequestBuilder = (
            self._domain.settings.factory.ParametersRequestBuilder
        )
        self._Device = self._domain.devices.Device
        self._DeviceRequestBuilder = self._domain.devices.factory.DevicesRequestBuilder

        self._ParameterTreesRequestBuilder = (
            self._domain.settings.factory.ParameterTreesRequestBuilder
        )
        self._ParameterTreesRequest = self._domain.settings.ParameterTreesRequest
        self._ParameterTreesRequestTreeDirection = (
            self._ParameterTreesRequest.TreeDirection
        )

        self._CalibrationFunctionTypes = self._domain.optics.CalibrationFunctionTypes

        # non lsa classes

        self._CernAccelerator = self._cern.accsoft.commons.domain.CernAccelerator

        # starting services
        self._System.setProperty("lsa.server", server)

        self._contextService = self._ServiceLocator.getService(self._ContextService)
        self._trimService = self._ServiceLocator.getService(self._TrimService)
        self._settingService = self._ServiceLocator.getService(self._SettingService)
        self._parameterService = self._ServiceLocator.getService(self._ParameterService)
        self._contextService = self._ServiceLocator.getService(self._ContextService)
        self._lhcService = self._ServiceLocator.getService(self._LhcService)
        self._hyperCycleService = self._ServiceLocator.getService(
            self._HyperCycleService
        )
        self._knobService = self._ServiceLocator.getService(self._KnobService)
        self._opticService = self._ServiceLocator.getService(self._OpticService)
        self._deviceService = self._ServiceLocator.getService(self._DeviceService)
        self._fidelService = self._ServiceLocator.getService(self._FidelService)

    @contextmanager
    def java_api(self):
        """Run code with the access to the LSA Java universe through JPype imports.
        After the import/execution returns, the original python import behavior is restored.

        This method is typically called from a launcher module, e.g.:
            `with pjlsa.LSAClient(server=...).java_api(): import my_main_module`
        """
        with self._mgr.imports():
            # work-around to fire up JPypes forward converters - TODO: remove me in JPype 0.8!
            from java.util import HashSet, HashMap, ArrayList, Date
            ArrayList()
            HashMap()
            HashSet()
            Date()
            yield

    def _getContextFamily(self, name):
        if isinstance(name, str):
            return getattr(self._ContextFamily, name.upper())
        else:
            return name

    def _getAccelerator(self, name):
        if isinstance(name, str):
            return getattr(self._CernAccelerator, name.upper())
        else:
            return name

    def _findHyperCycles(self):
        return list(self._hyperCycleService.findHyperCycles())

    def findHyperCycles(self):
        return [str(c) for c in self._findHyperCycles()]

    def _getHyperCycle(self, hypercycle=None):
        if hypercycle is None:
            return self._hyperCycleService.findActiveHyperCycle()
        else:
            return self._hyperCycleService.findHyperCycle(hypercycle)

    def findOperationalContexts(self, accelerator: str = 'sps'):
        accelerator = self._getAccelerator(accelerator)
        cycles = self._contextService.findStandAloneCycles(accelerator)
        cycles = filter(lambda cyc: str(cyc.getContextCategory) == 'OPERATIONAL', cycles)

        return sorted(map(str, cycles))

    def findResidentContexts(self, accelerator: str = 'sps'):
        accelerator = self._getAccelerator(accelerator)
        cycles = self._contextService.findResidentContexts(accelerator)

        return sorted(map(str, cycles))

    def findActiveContexts(self, accelerator: str = 'sps'):
        accelerator = self._getAccelerator(accelerator)
        cycles = self._contextService.findActiveContexts(accelerator)

        return sorted(map(str, cycles))

    def getUsers(self, hypercycle=None):
        hp = self._getHyperCycle(hypercycle=hypercycle)

        return sorted([str(u) for u in hp.getUsers()])

    def findParameterGroups(self, regexp="", accelerator="lhc"):
        acc = self._getAccelerator(accelerator)
        find = self._parameterService.findParameterGroupsByAccelerator
        grps = [grp.getName() for grp in find(acc)]
        reg = re.compile(regexp, re.IGNORECASE)
        return sorted(filter(reg.search, [str(grp) for grp in grps]))

    def findBeamProcesses(self, regexp="", accelerator="lhc"):
        acc = self._getAccelerator(accelerator)
        bps = self._contextService.findStandAloneBeamProcesses(acc)
        reg = re.compile(regexp, re.IGNORECASE)
        return sorted(filter(reg.search, [str(bp) for bp in bps]))

    def _getBeamProcess(self, bp):
        if isinstance(bp, self._BeamProcess):
            return bp
        else:
            return self._contextService.findStandAloneBeamProcess(bp)

    def _getCycle(self, cy):
        if isinstance(cy, self._Cycle):
            return cy
        else:
            return self._contextService.findStandAloneCycle(cy)

    def _getBeamProcessByUser(self, user, hypercycle=None):
        hp = self._getHyperCycle(hypercycle=hypercycle)
        return hp.getBeamProcessByUser(user)

    def getResidentBeamProcess(self, category):
        return str(self._getHyperCycle().getResidentBeamProcess(category))

    def getResidentBeamProcesses(self):
        return [str(p) for p in list(self._getHyperCycle().getResidentBeamProcesses())]

    def findParameterNames(self, deviceName=None, groupName=None, regexp=""):
        req = self._ParametersRequestBuilder()
        if deviceName is not None:
            req.setDeviceName(deviceName)
        if groupName is not None:
            req.setParameterGroup(groupName)
        lst = self._parameterService.findParameters(req.build())
        reg = re.compile(regexp, re.IGNORECASE)
        return sorted(filter(reg.search, [pp.getName() for pp in lst]))

    def _findDevices(self, deviceGroupName=None):
        builder = self._DeviceRequestBuilder()
        if deviceGroupName is not None:
            builder.setDeviceGroupName(deviceGroupName)
        req = builder.build()
        deviceList = self._deviceService.findDevices(req)
        return list(deviceList)

    def findDevices(self, deviceGroupName=None):
        deviceList = self._findDevices(deviceGroupName=deviceGroupName)
        return list(map(str, deviceList))

    def findUserContextMappingHistory(
            self, t1, t2, accelerator="lhc", contextFamily="beamprocess"
    ):
        acc = self._getAccelerator(accelerator)
        contextFamily = self._getContextFamily(contextFamily)
        t1 = _toJavaDate(t1).getTime()
        t2 = _toJavaDate(t2).getTime()
        res = self._contextService.findUserContextMappingHistory(
            acc, contextFamily, t1, t2
        )
        out = [
            (ct.getMappingTimestamp() / 1000.0, ct.getContextName(), ct.getUser())
            for ct in res
        ]
        return Context(*map(np.array, zip(*out)))

    def findBeamProcessHistory(self, t1, t2, accelerator="lhc"):
        cts = self.findUserContextMappingHistory(t1, t2, accelerator=accelerator)
        import pytimber

        db = pytimber.LoggingDB()
        fillnts, fillnv = db.get("HX:FILLN", t1, t2)["HX:FILLN"]
        fills = {}
        for ts, name in zip(cts.timestamp, cts.name):
            idx = fillnts.searchsorted(ts) - 1
            filln = int(fillnv[idx])
            fills.setdefault(filln, []).insert(0, (ts, name))
            # print(filln,len(fills[filln]))
        return fills

    def _getParameter(self, param):
        if isinstance(param, self._Parameter):
            return param
        else:
            return self._parameterService.findParameterByName(param)

    def _getParameterList(self, deviceName):
        req = self._ParametersRequestBuilder().setDeviceName(deviceName)
        lst = self._parameterService.findParameters(req.build())
        return lst

    def _getRawTrimHeadersByBeamprocess(self, param, beamprocess, start=None, end=None):
        bp = self._getBeamProcess(beamprocess)
        thrb = self._cern.lsa.domain.settings.TrimHeadersRequestBuilder()
        thrb.beamProcesses(self._java.util.Collections.singleton(bp))
        thrb.parameters(param)
        if start is not None:
            thrb.startingFrom(_toJavaDate(start).toInstant())
        trimHeadersRequest = thrb.build()
        raw_headers = self._trimService.findTrimHeaders(trimHeadersRequest)
        raw_headers = list(raw_headers)
        if start is not None:
            raw_headers = [
                th
                for th in raw_headers
                if not th.getCreatedDate().before(_toJavaDate(start))
            ]
        if end is not None:
            raw_headers = [
                th
                for th in raw_headers
                if not th.getCreatedDate().after(_toJavaDate(end))
            ]
        return raw_headers

    def _getRawTrimHeadersByCycle(self, param, cycle, start=None, end=None):
        cy = self._getCycle(cycle)
        thrb = self._cern.lsa.domain.settings.TrimHeadersRequestBuilder()
        thrb.beamProcesses(cy.getBeamProcesses())
        thrb.parameters(param)
        if start is not None:
            thrb.startingFrom(_toJavaDate(start).toInstant())
        trimHeadersRequest = thrb.build()
        raw_headers = self._trimService.findTrimHeaders(trimHeadersRequest)
        raw_headers = list(raw_headers)
        if start is not None:
            raw_headers = [
                th
                for th in raw_headers
                if not th.getCreatedDate().before(_toJavaDate(start))
            ]
        if end is not None:
            raw_headers = [
                th
                for th in raw_headers
                if not th.getCreatedDate().after(_toJavaDate(end))
            ]
        return raw_headers

    def _buildParameterList(self, parameter):
        if type(parameter) in [str, self._BeamProcess]:
            param = self._getParameter(parameter)
            param = self._java.util.Collections.singleton(param)
        else:
            param = self._java.util.LinkedList()
            for pp in parameter:
                param.add(self._getParameter(pp))
        return param

    def _getTrimHeadersByBeamprocess(self, parameter, beamprocess, start=None, end=None):
        return [
            _build_TrimHeader(th)
            for th in self._getRawTrimHeadersByBeamprocess(
                self._buildParameterList(parameter), beamprocess, start, end
            )
        ]

    def _getTrimHeadersByCycle(self, parameter, cycle, start=None, end=None):
        return [
            _build_TrimHeader(th)
            for th in self._getRawTrimHeadersByCycle(
                self._buildParameterList(parameter), cycle, start, end
            )
        ]

    def getTrimHeaders(
            self, parameter, beamprocess=None, cycle=None, start=None, end=None
    ):
        if beamprocess is not None:
            return self._getTrimHeadersByBeamprocess(parameter,
                                                     beamprocess=beamprocess,
                                                     start=start, end=end)
        else:
            return self._getTrimHeadersByCycle(parameter,
                                               cycle=cycle,
                                               start=start, end=end)

    def _getTrimsByBeamprocess(
            self, parameter, beamprocess, start=None, end=None, part="value"
    ):
        parameterList = self._buildParameterList(parameter)
        bp = self._getBeamProcess(beamprocess)

        timestamps = {}
        values = {}
        for th in self._getRawTrimHeadersByBeamprocess(parameterList, bp, start, end):
            csrb = (
                self._cern.lsa.domain.settings.ContextSettingsRequestBuilder()
            )
            csrb.standAloneContext(bp)
            csrb.parameters(parameterList)
            csrb.at(th.getCreatedDate().toInstant())
            contextSettings = self._settingService.findContextSettings(csrb.build())
            for pp in parameterList:
                parameterSetting = contextSettings.getParameterSettings(pp)
                if parameterSetting is None:
                    continue

                setting = parameterSetting.getSetting(bp)
                value = setting
                if part is not None:
                    if type(setting) is self._ScalarSetting:
                        if part == "value":
                            value = setting.getScalarValue().getDouble()
                        elif part == "target":
                            value = setting.getTargetScalarValue().getDouble()
                        elif part == "correction":
                            value = setting.getCorrectionScalarValue().getDouble()
                        else:
                            raise ValueError("Invalid Setting Part: " + part)
                    elif type(setting) is self._FunctionSetting:
                        if part == "value":
                            df = setting.getFunctionValue()
                        elif part == "target":
                            df = setting.getTargetFunctionValue()
                        elif part == "correction":
                            df = setting.getCorrectionFunctionValue()
                        else:
                            raise ValueError("Invalid Setting Part: " + part)
                        value = np.array([df.toXArray()[:], df.toYArray()[:]])
                    else:
                        # for now, return the java type (to be extended)
                        value = setting

                timestamps.setdefault(pp.getName(), []).append(
                    th.getCreatedDate().getTime() / 1000
                )
                values.setdefault(pp.getName(), []).append(value)
        out = {}
        for name in values:
            out[name] = TrimTuple(time=timestamps[name], data=values[name])
        return out

    def _getTrimsByCycle(
            self, parameter, cycle, start=None, end=None, part="value"
    ):
        parameterList = self._buildParameterList(parameter)
        cy = self._getCycle(cycle)

        timestamps = {}
        values = {}
        for th in self._getRawTrimHeadersByCycle(
                parameterList, cy, start, end
        ):
            csrb = self._domain.settings.ContextSettingsRequestBuilder()
            csrb.standAloneContext(cy)
            csrb.parameters(parameterList)
            csrb.at(th.getCreatedDate().toInstant())
            contextSettings = self._settingService.findContextSettings(csrb.build())
            for pp in parameterList:
                parameterSetting = contextSettings.getParameterSettings(pp)
                if parameterSetting is None:
                    continue
                settingIterator = parameterSetting.getSettings().iterator()
                setting = []
                while settingIterator.hasNext():
                    setting.append(settingIterator.next())
                if len(setting) == 1:
                    setting = setting[0]
                value = setting
                if part is not None:
                    if type(setting) is self._ScalarSetting:
                        if part == "value":
                            value = setting.getScalarValue().getDouble()
                        elif part == "target":
                            value = setting.getTargetScalarValue().getDouble()
                        elif part == "correction":
                            value = setting.getCorrectionScalarValue().getDouble()
                        else:
                            raise ValueError("Invalid Setting Part: " + part)
                    elif type(setting) is self._FunctionSetting:
                        if part == "value":
                            df = setting.getFunctionValue()
                        elif part == "target":
                            df = setting.getTargetFunctionValue()
                        elif part == "correction":
                            df = setting.getCorrectionFunctionValue()
                        else:
                            raise ValueError("Invalid Setting Part: " + part)
                        value = np.array([df.toXArray()[:], df.toYArray()[:]])
                    else:
                        # for now, return the java type (to be extended)
                        value = setting

                timestamps.setdefault(pp.getName(), []).append(
                    th.getCreatedDate().getTime() / 1000
                )
                values.setdefault(pp.getName(), []).append(value)
        out = {}
        for name in values:
            out[name] = TrimTuple(time=timestamps[name], data=values[name])
        return out

    def getTrims(
            self, parameter, beamprocess=None, cycle=None, start=None, end=None, part="value"
    ):
        if beamprocess is not None:
            return self._getTrimsByBeamprocess(parameter,
                                               beamprocess=beamprocess,
                                               start=start, end=end,
                                               part=part)
        else:
            return self._getTrimsByCycle(parameter,
                                         cycle=cycle,
                                         start=start, end=end,
                                         part=part)

    def _getLastTrimByBeamprocess(self, parameter, beamprocess, part="value"):
        th = self._getTrimHeadersByBeamprocess(parameter, beamprocess)[-1]
        res = self._getTrimsByBeamprocess(
            parameter, beamprocess, part=part, start=th.createdDate
        )[parameter]
        return TrimTuple(res.time[-1], res.data[-1])

    def _getLastTrimByCycle(self, parameter, cycle, part="value"):
        th = self._getTrimHeadersByCycle(parameter, cycle)[-1]
        res = self._getTrimsByCycle(
            parameter, cycle, part=part, start=th.createdDate
        )[parameter]
        return TrimTuple(res.time[-1], res.data[-1])

    def getLastTrim(
            self, parameter, beamprocess=None, cycle=None, part="value"
    ):
        if beamprocess is not None:
            return self._getLastTrimByBeamprocess(parameter,
                                                  beamprocess=beamprocess,
                                                  part=part)
        else:
            return self._getLastTrimByCycle(parameter,
                                            cycle=cycle,
                                            part=part)

    def _getLastTrimValueByBeamprocess(self, parameter, beamprocess, part="value"):
        th = self._getTrimHeadersByBeamprocess(parameter, beamprocess)[-1]
        res = self._getTrimsByBeamprocess(
            parameter, beamprocess, part=part, start=th.createdDate
        )[parameter]
        return res.data[-1]

    def _getLastTrimValueByCycle(self, parameter, cycle, part="value"):
        th = self._getTrimHeadersByCycle(parameter, cycle)[-1]
        res = self._getTrimsByCycle(
            parameter, cycle, part=part, start=th.createdDate
        )[parameter]
        return res.data[-1]

    def getLastTrimValue(
            self, parameter, beamprocess=None, cycle=None, part="value"
    ):
        if beamprocess is not None:
            return self._getLastTrimValueByBeamprocess(parameter,
                                                       beamprocess=beamprocess,
                                                       part=part)
        else:
            return self._getLastTrimValueByCycle(parameter,
                                                 cycle=cycle,
                                                 part=part)

    def getOpticTable(self, beamprocess):
        bp = self._getBeamProcess(beamprocess)
        if bp is None:
            raise ValueError("Beamprocess '%s' not found" % beamprocess)
        opticTable = list(self._opticService.findContextOpticsTables(bp))[
            0
        ].getOpticsTableItems()
        return [
            OpticTableItem(time=o.getTime(), id=o.getOpticId(), name=o.getOpticName())
            for o in opticTable
        ]

    def getKnobFactors(self, knob, optic):
        if isinstance(optic, OpticTableItem):
            optic = optic.name
        k = self._knobService.findKnob(knob)
        factors = list(k.getKnobFactors().getFactorsForOptic(optic))
        return {f.getComponentName(): f.getFactor() for f in factors}

    def getParameterHierarchy(self, parameter, direction="dependent"):
        req = self._ParameterTreesRequestBuilder()
        if direction == "dependent":
            req.setTreeDirection(
                self._ParameterTreesRequestTreeDirection.DEPENDENT_TREE
            )
        elif direction == "source":
            req.setTreeDirection(self._ParameterTreesRequestTreeDirection.SOURCE_TREE)
        else:
            raise ValueError('invalid direction, expecting "dependent" or "source"')
        req.setParameter(self._getParameter(parameter))
        tree = self._parameterService.findParameterTrees(req.build())
        params = {}
        for t in tree:
            for p in t.getParameters():
                params.setdefault(str(p.getParameterType()), []).append(str(p))
        return params

    def getOpticStrength(self, optic):
        if not hasattr(optic, "name"):
            optic = self._opticService.findOpticByName(optic)
        out = [(st.logicalHWName, st.strength) for st in optic.getOpticStrengths()]
        return dict(out)

    def _getOptics(self, name):
        return self._opticService.findOpticByName(name)

    def interpolateOpticsParameters(self, beamprocess, parameters):
        ot = self.getOpticTable(beamprocess)
        tvalue = [opt.time for opt in ot]
        pv = {}
        for pn in parameters:
            try:
                ts, (steps, val) = self.getLastTrim(beamprocess, pn)
                pv[pn] = np.interp(tvalue, steps, val)
            except ValueError as ex:
                print("Error extracting parameter '%s': %s" % (pn, ex))
            except IndexError as ex:
                print("Error extracting parameter '%s': %s" % (pn, ex))
            except jpype.JException as ex:
                print("Error extracting parameter '%s': %s" % (pn, ex))
        return pv

    def findPCNameByMadStrength(self, madname, full=False):
        nl = self._java.util.Collections.singleton(madname)
        pcs = self._deviceService.findLogicalNamesByMadStrengthNames(nl)
        pcname = pcs[madname]
        if full is True:
            nl = self._java.util.Collections.singleton(pcname)
            pcs = self._deviceService.findActualDevicesByLogicalHardwareName(nl)
            pcname = list(pcs[pcname])[0].toString()
        return pcname

    def findMadStrengthNameByPCName(self, pcname, full=False):
        if full is True:
            nl = self._java.util.Collections.singleton(pcname)
            pcs = self._deviceService.findLogicalHardwaresByActualDeviceNames(nl)
            pcname = list(pcs[pcname])[0].toString()
        nl = self._java.util.Collections.singleton(pcname)
        madnames = self._deviceService.findMadStrengthNamesByLogicalNames(nl)
        madname = madnames[pcname]
        return madname

    def getCalibration(self, pcname, fieldtype="B_FIELD"):
        jfieldtype = getattr(self._CalibrationFunctionTypes, fieldtype)
        cal = self._fidelService.findCalibrationByLogicalHardware(pcname)
        ff = cal.getCalibrationFunctionByType(jfieldtype)
        if ff is not None:
            field = list(ff.toXArray())
            current = list(ff.toYArray())
            return Calibration(
                current=current, field=field, fieldtype=fieldtype, name=pcname
            )

    def _get_calibration(self):
        cals = self._fidelService.findAllCalibrations()
        return dict((cc.getName(), cc) for cc in cals)

    def dump_calibrations(self, outdir="calib"):
        """ Dump all calibration in directory <outdir>
        """
        os.mkdir(outdir)
        for name, cc in self._get_calibrations():
            ff = cc.getCalibrationFunctionByType(self._CalibrationFunctionTypes.B_FIELD)
            if ff is not None:
                field = ff.toXArray()
                current = ff.toYArray()
                fn = os.path.join(outdir, "%s.txt" % name)
                print(fn)
                fh = open(fn, "w")
                fh.write("\n".join(["%s %s" % (i, f) for i, f in zip(current, field)]))
                fh.close()

    def getPCInfo(self, pcname):
        pc = self._deviceService.findPowerConverterInfo(pcname)
        info = PCInfo(*(getattr(pc, nn) for nn in PCInfo._fields))
        return info
