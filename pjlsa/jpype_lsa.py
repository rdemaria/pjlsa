import jpype

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