import os

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


BeamProcess          =cern.lsa.domain.settings.BeamProcess
ContextSettings      =cern.lsa.domain.settings.ContextSettings
HyperCycle           =cern.lsa.domain.settings.HyperCycle
Parameter            =cern.lsa.domain.settings.Parameter
ParameterSettings    =cern.lsa.domain.settings.ParameterSettings
Setting              =cern.lsa.domain.settings.Setting
StandAloneBeamProcess=cern.lsa.domain.settings.StandAloneBeamProcess
TrimHeader           =cern.lsa.domain.settings.TrimHeader

ParametersRequestBuilder = cern.lsa.domain.settings.factory.ParametersRequestBuilder
Device                   = cern.lsa.domain.devices.Device

CalibrationFunctionTypes=cern.lsa.domain.optics.CalibrationFunctionTypes;


class LSAClient(object):
    def __init__(self,server='lhc'):
        System.setProperty("lsa.server", server);
        System.setProperty("lsa.mode", "3");
        System.setProperty("accelerator", "LHC");
        self.trimService = ServiceLocator.getService(TrimService)
        self.settingService = ServiceLocator.getService(SettingService)
        self.parameterService = ServiceLocator.getService(ParameterService)
        self.contextService  = ServiceLocator.getService(ContextService)
        self.lhcService      = ServiceLocator.getService(LhcService)
        self.hyperCycleService = ServiceLocator.getService(HyperCycleService)
    def findHyperCycles(self):
        return map(str,self.hyperCycleService.findHyperCycles())
    def getHyperCycle(self,hypercycle=None):
        if hypercycle is None:
            return self.hyperCycleService.findActiveHyperCycle()
        else:
            return self.hyperCycleService.findHyperCycle(hypercycle)
    def getUsers(self,hypercycle=None):
        hp=self.getHyperCycle(hypercycle=hypercycle)
        return map(str,hp.getUsers())
    def getBeamProcess(self,hypercycle=None,user=None):
        hp=self.getHyperCycle(hypercycle=hypercycle)
        if user is None:
            return hp.getResidentBeamProcess()
        else:
            return hp.getBeamProcessByUser(user)
    def getParameterList(self,deviceName):
        req=ParametersRequestBuilder().setDeviceName(deviceName)
        lst=self.parameterService.findParameters(req.build())
        return lst
    def getParameterNames(self,deviceName):
        req=ParametersRequestBuilder().setDeviceName(deviceName)
        lst=self.parameterService.findParameters(req.build())
        return [pp.getName() for pp in lst]
    def getTrim(self,beamProcess,parameterName):
        parameter = self.parameterService.findParameterByName(parameterName)
        bpl=java.util.ArrayList(1)
        bpl.add(beamProcess)
        pl=java.util.ArrayList(1)
        pl.add(parameter)
        headers=self.trimService.findTrimHeaders(bpl,pl, None)
        return headers

class Fidel(object):
    def __init__(self,server='lhc'):
        System.setProperty("lsa.server", server);
        System.setProperty("lsa.mode", "3");
        System.setProperty("accelerator", "LHC");
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



