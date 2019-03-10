import cmmnbuild_dep_manager

# ------ JPype SETUP ------
mgr = cmmnbuild_dep_manager.Manager('pjlsa')
jpype = mgr.start_jpype_jvm()


# Monkey-Patcher for LSA Java Domain Objects
class LsaCustomizer(jpype._jclass.JClassCustomizer):
    _PATCHES = {
        '__repr__': lambda self: self.__str__()
    }

    def canCustomize(self, name, jc):
        return name.startswith('cern.lsa.domain.') or name.startswith('cern.accsoft.commons.domain.')

    def customize(self, name, jc, bases, members, fields):
        members.update(LsaCustomizer._PATCHES)


jpype._jclass.registerClassCustomizer(LsaCustomizer())


# ------ IMPORTS ------
cern = jpype.JPackage('cern')
org = jpype.JPackage('org')
java = jpype.JPackage('java')

# General Java
System = java.lang.System

# LSA Services
ServiceLocator = cern.lsa.client.ServiceLocator

AcceleratorService = cern.lsa.client.AcceleratorService
AdService = cern.lsa.client.AdService
ArchiveReferenceService = cern.lsa.client.ArchiveReferenceService
CacheService = cern.lsa.client.CacheService
ContextService = cern.lsa.client.ContextService
DeviceService = cern.lsa.client.DeviceService
ElenaService = cern.lsa.client.ElenaService
ExploitationService = cern.lsa.client.ExploitationService
FidelService = cern.lsa.client.FidelService
GenerationService = cern.lsa.client.GenerationService
HyperCycleService = cern.lsa.client.HyperCycleService
JapcService = cern.lsa.client.JapcService
KnobService = cern.lsa.client.KnobService
LhcService = cern.lsa.client.LhcService
LktimService = cern.lsa.client.LktimService
OpticService = cern.lsa.client.OpticService
ParameterService = cern.lsa.client.ParameterService
SettingService = cern.lsa.client.SettingService
SpsService = cern.lsa.client.SpsService
TestService = cern.lsa.client.TestService
TimingService = cern.lsa.client.TimingService
TransactionService = cern.lsa.client.TransactionService
TrimService = cern.lsa.client.TrimService
WorkingSetService = cern.lsa.client.WorkingSetService

# Contexts
ContextFamily = cern.lsa.domain.settings.ContextFamily
Context = cern.lsa.domain.settings.Context
StandAloneBeamProcess = cern.lsa.domain.settings.StandAloneBeamProcess
StandAloneContext = cern.lsa.domain.settings.StandAloneContext
StandAloneCycle = cern.lsa.domain.settings.StandAloneCycle
BeamProcess = cern.lsa.domain.settings.BeamProcess
BeamProcessType = cern.lsa.domain.settings.type.BeamProcessType
BeamProcessPurpose = cern.lsa.domain.settings.type.BeamProcessPurpose
ActualBeamProcessInfo = cern.lsa.domain.settings.ActualBeamProcessInfo
UserContextMapping = cern.lsa.domain.settings.UserContextMapping
AcceleratorUser = cern.lsa.domain.settings.AcceleratorUser
AcceleratorUserGroup = cern.lsa.domain.settings.AcceleratorUserGroup
