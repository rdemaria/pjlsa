# -*- coding: utf-8 -*-
import os, re
from collections import namedtuple
import datetime

import numpy as np
import six

import cmmnbuild_dep_manager


# Use mgr.class_hints('LhcService')
# put deps in __init__.py
mgr = cmmnbuild_dep_manager.Manager('pylsa')
jpype=mgr.start_jpype_jvm()

cern=jpype.JPackage('cern')
org=jpype.JPackage('org')
java=jpype.JPackage('java')
System=java.lang.System

null=org.apache.log4j.varia.NullAppender()
org.apache.log4j.BasicConfigurator.configure(null)

ContextService   =cern.lsa.client.ContextService
HyperCycleService=cern.lsa.client.HyperCycleService
ParameterService =cern.lsa.client.ParameterService
ServiceLocator   =cern.lsa.client.ServiceLocator
SettingService   =cern.lsa.client.SettingService
TrimService      =cern.lsa.client.TrimService
LhcService       =cern.lsa.client.LhcService
FidelService     =cern.lsa.client.FidelService
KnobService      =cern.lsa.client.KnobService
OpticService     =cern.lsa.client.OpticService
DeviceService    =cern.lsa.client.DeviceService

BeamProcess          =cern.lsa.domain.settings.BeamProcess
ContextSettings      =cern.lsa.domain.settings.ContextSettings
HyperCycle           =cern.lsa.domain.settings.HyperCycle
Parameter            =cern.lsa.domain.settings.Parameter
ParameterSettings    =cern.lsa.domain.settings.ParameterSettings
Setting              =cern.lsa.domain.settings.Setting
StandAloneBeamProcess=cern.lsa.domain.settings.StandAloneBeamProcess
Knob                 =cern.lsa.domain.settings.Knob
FunctionSetting      =cern.lsa.domain.settings.spi.FunctionSetting
ScalarSetting        =cern.lsa.domain.settings.spi.ScalarSetting

ParametersRequestBuilder = cern.lsa.domain.settings.factory.ParametersRequestBuilder
Device                   = cern.lsa.domain.devices.Device

CalibrationFunctionTypes=cern.lsa.domain.optics.CalibrationFunctionTypes

TrimHeader = namedtuple('TrimHeader',
           ['id','beamProcesses','createdDate','description','clientInfo'])

def _build_TrimHeader(th):
    return TrimHeader(
            id = th.id,
            beamProcesses = [str(bp) for bp in th.beamProcesses],
            createdDate = datetime.datetime.fromtimestamp(
                              th.createdDate.getTime()/1000),
            description = th.description,
            clientInfo = th.clientInfo )
OpticTableItem = namedtuple('OpticTableItem', ['time', 'id', 'name'])

TrimTuple = namedtuple('TrimTuple', ['time', 'data'])

def _toJavaDate(t):
    Date = java.util.Date
    if isinstance(t, six.string_types):
        return java.sql.Timestamp.valueOf(t)
    elif isinstance(t, datetime.datetime):
        return java.sql.Timestamp.valueOf(t.strftime('%Y-%m-%d %H:%M:%S.%f'))
    elif t is None:
        return None
    elif isinstance(t,Date):
        return t
    else:
        return Date(int(t*1000))

accelerators={
        'lhc': cern.accsoft.commons.domain.CernAccelerator.LHC,
        }

class LSAClient(object):
    def __init__(self,server='lhc',accelerator="LHC"):
        System.setProperty("lsa.server", server)
        System.setProperty("lsa.mode", "3")
        System.setProperty("accelerator", accelerator)
        self.contextService = ServiceLocator.getService(ContextService)
        self.trimService = ServiceLocator.getService(TrimService)
        self.settingService = ServiceLocator.getService(SettingService)
        self.parameterService = ServiceLocator.getService(ParameterService)
        self.contextService = ServiceLocator.getService(ContextService)
        self.lhcService = ServiceLocator.getService(LhcService)
        self.hyperCycleService = ServiceLocator.getService(HyperCycleService)
        self.knobService = ServiceLocator.getService(KnobService)
        self.opticService = ServiceLocator.getService(OpticService)
        self.deviceService = ServiceLocator.getService(DeviceService)

    def findHyperCycles(self):
        return [str(c) for c in self.contextService.findHyperCycles()]

    def findBeamProcesses(self,regexp='',accelerator='lhc'):
        acc=accelerators.get(accelerator,accelerator)
        bps = self.contextService.findStandAloneBeamProcesses(acc)
        reg=re.compile(regexp,re.IGNORECASE)
        return filter(reg.search,[str(bp) for bp in bps])

    def getHyperCycle(self,hypercycle=None):
        if hypercycle is None:
            return self.hyperCycleService.findActiveHyperCycle()
        else:
            return self.hyperCycleService.findHyperCycle(hypercycle)

    def getUsers(self,hypercycle=None):
        hp=self.getHyperCycle(hypercycle=hypercycle)
        return [str(u) for u in hp.getUsers()]

    def getBeamProcess(self, bp):
        if isinstance(bp, BeamProcess):
            return bp
        else:
            return self.contextService.findStandAloneBeamProcess(bp)

    def getParameter(self, param):
        if isinstance(param, Parameter):
            return param
        else:
            return self.parameterService.findParameterByName(param)

    def getBeamProcessByUser(self,user, hypercycle=None):
        hp=self.getHyperCycle(hypercycle=hypercycle)
        return hp.getBeamProcessByUser(user)

    def getResidentBeamProcess(self, category):
        return str(self.getHyperCycle().getResidentBeamProcess(category))

    def getResidentBeamProcesses(self):
        return [str(p) for p in list(self.getHyperCycle().getResidentBeamProcesses())]

    def _getRawTrimHeaders(self, beamprocess, param, start=None, end=None):
        bp = self.getBeamProcess(beamprocess)
        raw_headers = self.trimService.findTrimHeaders(java.util.Collections.singleton(bp),
                                                       param,
                                                       _toJavaDate(start))
        raw_headers = list(raw_headers)
        if start is not None:
            raw_headers = [th for th in raw_headers if th.createdDate.after(_toJavaDate(start))]
        if end is not None:
            raw_headers = [th for th in raw_headers if th.createdDate.before(_toJavaDate(end))]
        return raw_headers

    def _buildParameterList(self, parameter):
        if type(parameter) in [str,BeamProcess]:
            param = self.getParameter(parameter)
            param = java.util.Collections.singleton(param)
        else:
            param = java.util.LinkedList()
            for pp in parameter:
                param.add(self.getParameter(pp))
        return param

    def getTrimHeaders(self, beamprocess, parameter, start=None, end=None):
        return [_build_TrimHeader(th) for th in
                   self._getRawTrimHeaders(
                            beamprocess,
                            self._buildParameterList(parameter), start, end)]

    def getTrims(self, beamprocess, parameter, start=None, end=None, part='value'):
        parameterList = self._buildParameterList(parameter)
        bp = self.getBeamProcess(beamprocess)

        timestamps = {}
        values = {}
        for th in self._getRawTrimHeaders(bp, parameterList, start, end):
            contextSettings =  \
                    self.settingService.findContextSettings(bp,
                            parameterList, th.createdDate)
            for pp in parameterList:
              parameterSetting = contextSettings.getParameterSettings(pp)
              if parameterSetting is None:
                continue

              setting = parameterSetting.getSetting(bp)
              value = setting
              if part is not None:
                if type(setting) is ScalarSetting:
                  if part == 'value':
                    value = setting.getScalarValue().getDouble()
                  elif part == 'target':
                    value = setting.getTargetScalarValue().getDouble()
                  elif part == 'correction':
                    value = setting.getCorrectionScalarValue().getDouble()
                  else:
                    raise ValueError('Invalid Setting Part: ' + part)
                elif type(setting) is FunctionSetting:
                  if part == 'value':
                    df = setting.getFunctionValue()
                  elif part == 'target':
                    df = setting.getTargetFunctionValue()
                  elif part == 'correction':
                    df = setting.getCorrectionFunctionValue()
                  else:
                    raise ValueError('Invalid Setting Part: ' + part)
                  value = np.array([df.toXArray()[:], df.toYArray()[:]])
                else:
                  # for now, return the java type (to be extended)
                  value = setting

              timestamps.setdefault(pp.getName(),[]).append(
                                          th.createdDate.getTime()/1000)
              values.setdefault(pp.getName(),[]).append(value)
        out={ }
        for name in values:
            out[name]=TrimTuple(time=timestamps[name], data=values[name])
        return out
    def getLastTrim(self,beamprocess, parameter, part='value'):
        res=self.getTrims(beamprocess,parameter,part=part)[parameter]
        return res.time[-1],res.data[-1]

    def getOpticTable(self, beamprocess):
        bp = self.getBeamProcess(beamprocess)
        opticTable = list(self.opticService.findContextOpticsTables(bp))[0].getOpticsTableItems()
        return [ OpticTableItem(time=o.getTime(),
                 id=o.getOpticId(),
                 name=o.getOpticName()) for o in opticTable ]

    def getKnobFactors(self, knob, optic):
        if isinstance(optic, OpticTableItem):
            optic = optic.name
        k = self.knobService.findKnob(knob)
        factors = list(k.getKnobFactors().getFactorsForOptic(optic))
        return { f.getComponentName(): f.getFactor() for f in factors }

    def getOpticStrength(self,optic):
        if not hasattr(optic,'name'):
           optic=self.opticService.findOpticByName(optic)
        out=  [ (st.logicalHWName,st.strength)
                for st in optic.getOpticStrengths() ]
        return dict(out)

    def getOptics(self,name):
        return self.opticService.findOpticByName(name)

    def getParameterList(self,deviceName):
        req=ParametersRequestBuilder().setDeviceName(deviceName)
        lst=self.parameterService.findParameters(req.build())
        return lst

    def getParameterNames(self,deviceName,regexp=''):
        req=ParametersRequestBuilder().setDeviceName(deviceName)
        lst=self.parameterService.findParameters(req.build())
        reg=re.compile(regexp,re.IGNORECASE)
        return filter(reg.search,[pp.getName() for pp in lst ])

class Fidel(object):
    def __init__(self,server='lhc',accelerator="LHC"):
        System.setProperty("lsa.server", server)
        System.setProperty("lsa.mode", "3")
        System.setProperty("accelerator", accelerator)
        self.fidelService = ServiceLocator.getService(FidelService)
    def dump_calibrations(outdir='calib'):
        os.mkdir(outdir)
        cals=fidelService.findAllCalibrations();
        for cc in cals:
          name=cc.getName()
          ff=cc.getCalibrationFunctionByType(CalibrationFunctionTypes.B_FIELD)
          if ff is not None:
             field=ff.toXArray()
             current=ff.toYArray()
             fn=os.path.join(outdir,'%s.txt'%name)
             print(fn)
             fh=open(fn,'w')
             fh.write('\n'.join(["%s %s"%(i,f) for i,f in zip(current,field)]))
             fh.close()

