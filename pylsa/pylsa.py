import os

import jpype

import cmmnbuild_dep_manager

mgr = cmmnbuild_dep_manager.Manager()
jpype=mgr.start_jpype_jvm()


cern=jpype.JPackage('cern')
org=jpype.JPackage('org')
java=jpype.JPackage('java')
System=java.lang.System

null=org.apache.log4j.varia.NullAppender()
org.apache.log4j.BasicConfigurator.configure(null)

FidelService=cern.lsa.client.FidelService;
ServiceLocator=cern.lsa.client.ServiceLocator;
CalibrationFunctionTypes=cern.lsa.domain.optics.CalibrationFunctionTypes;


class Fidel(object):
    def __init__(self,server='lhc'):
        System.setProperty("lsa.server", "lhc");
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


