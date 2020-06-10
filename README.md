# pjlsa
A Python module providing access to the LSA API

## Low-Level access to the Java LSA API
Low-level access to the full Java LSA API is provided through the JPype import system.

The recommended way use it is to create a launcher module (e.g. `my_launcher.py`) which creates `LSAClient` and calls
 the `java_api()` context manager:
```python
import pjlsa
with pjlsa.LSAClient(server='sps').java_api():
    import my_main_module
```
This simple launcher will import the module `my_main_module.py` - which should contain your actual code entry point - 
with the JPype import system enabled.

In `my_main_module.py`, you can then use `import` statements to import LSA Java objects, e.g.:
```python
from cern.lsa.client import ServiceLocator, ParameterService

parameterService = ServiceLocator.getService(ParameterService)

parameter = parameterService.findParameterByName("SPSBEAM/MOMENTUM")
```

For your convenience, pjLSA ships with python type stubs for the commonly used Java APIs, which provide static type
checking and auto-completion in IDEs like PyCharm and VSCode.

### Examples
_The launcher code - see above - is omitted in the following examples._
#### Accessing Cycle settings
```python
from cern.lsa.client import ServiceLocator, ContextService, ParameterService, SettingService
from cern.lsa.domain.settings import ContextSettingsRequest, Settings
from java.util import Collections

contextService = ServiceLocator.getService(ContextService)
parameterService = ServiceLocator.getService(ParameterService)
settingService = ServiceLocator.getService(SettingService)

parameter = parameterService.findParameterByName("SPSBEAM/MOMENTUM")
cycle = contextService.findStandAloneCycle("SFT_PRO_MTE_L4780_2018_V1")
cycleSettings = settingService.findContextSettings(
    ContextSettingsRequest.byStandAloneContextAndParameters(cycle, Collections.singleton(parameter)))
function = Settings.getFunction(cycleSettings, parameter)
print(function)
```

#### Accessing Optics Information and Twiss Data
```python
from cern.lsa.client import ServiceLocator, ContextService, OpticService
from cern.accsoft.commons.domain.particletransfers import SpsParticleTransfer
from cern.lsa.domain.optics.factory import TwissesRequestBuilder

contextService = ServiceLocator.getService(ContextService)
opticService = ServiceLocator.getService(OpticService)

cycle = contextService.findStandAloneCycle("SFT_PRO_MTE_L4780_2018_V1")
spsFunctionBpType = cycle.getIntersections() \
    .getIntersectedFunctionBeamProcess(SpsParticleTransfer.SPSRING, 0.0) \
    .getBeamProcess().getTypeName()
opticsTables = opticService.findContextOpticsTables(cycle)
spsRingOpticTable = [ot for ot in opticsTables if ot.getBeamProcessTypeName() == spsFunctionBpType][0]


opticsTableItems = spsRingOpticTable.getOpticsTableItems()
firstOptic = opticsTableItems[0]
print(firstOptic)

twisses = opticService.findTwisses(TwissesRequestBuilder.byOpticName(firstOptic.getOpticName()))
print(twisses)
```

#### Performing a Trim
```python
from cern.lsa.client import ServiceLocator, ContextService, ParameterService, TrimService
from cern.accsoft.commons.value import ValueFactory
from cern.lsa.domain.settings import TrimRequest

trimService = ServiceLocator.getService(TrimService)
parameterService = ServiceLocator.getService(ParameterService)
contextService = ServiceLocator.getService(ContextService)

cycle = contextService.findStandAloneCycle("SFT_PRO_MTE_L4780_2018_test_Michi_V2")
parameter = parameterService.findParameterByName("logical.MDV.11705/K")
function = ValueFactory.createFunction(
    [0.0, 5000.0, 6000.0, 7000.0, 9240.0],
    [0.0, 0.0, 1e-5, -1e-5, 0.0]
)
trimRequest = TrimRequest.builder() \
    .setContext(cycle) \
    .addFunction(parameter, function) \
    .setDescription("Description for trim history") \
    .build()
trimService.trimSettings(trimRequest)
```

## High-Level python API (mostly for data analysis)
Limited use for the time being

Added methods: _getRawTrimHeadersByCycle, getTrimHeadersByCycle, getTrimsByCycle,
                getLastTrimByCycle, getLastTrimValue, getLastTrimValueByCycle

### Extract trims for a particular beamProcess, parameter, and time window
```python
import pjlsa
lsa = pjlsa.LSAClient()
t1='2015-11-22 00:00:00'
t2='2015-11-23 00:00:00'
trims = lsa.getTrims(parameter="LHCBEAM2/IP1_SEPSCAN_Y_MM",
                     beamprocess="PHYSICS-2.51TeV-4m-2015_V1@90_[END]",
                     start=t1, end=t2)
```

### Get optics tables
```
In [1]: ot = lsa.getOpticTable('RAMP-SQUEEZE-6.5TeV-ATS-1m-2017_V3_V1')

In [2]: ot
Out[2]: 
[OpticTableItem(time=0,    id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=30,   id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=60,   id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=120,  id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=200,  id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=300,  id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=400,  id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=452,  id=3795, name='R2017a_A970C970A10mL970'),
 OpticTableItem(time=491,  id=3791, name='R2017a_A920C920A10mL920'),
 OpticTableItem(time=536,  id=3802, name='R2017a_A850C850A10mL850'),
 OpticTableItem(time=595,  id=3797, name='R2017a_A740C740A10mL740'),
 OpticTableItem(time=669,  id=3794, name='R2017a_A630C630A10mL630'),
 OpticTableItem(time=768,  id=3792, name='R2017a_A530C530A10mL530'),
 OpticTableItem(time=842,  id=3787, name='R2017a_A440C440A10mL440'),
 OpticTableItem(time=882,  id=3799, name='R2017a_A360C360A10mL360'),
 OpticTableItem(time=931,  id=3796, name='R2017a_A310C310A10mL310'),
 OpticTableItem(time=971,  id=3803, name='R2017a_A230C230A10mL300'),
 OpticTableItem(time=1002, id=3807, name='R2017a_A180C180A10mL300'),
 OpticTableItem(time=1047, id=3804, name='R2017a_A135C135A10mL300'),
 OpticTableItem(time=1121, id=3788, name='R2017a_A100C100A10mL300'),
 OpticTableItem(time=1210, id=3788, name='R2017a_A100C100A10mL300')]

ts,(steps,val)=lsa.getLastTrim(parameter='LHCBEAM/MOMENTUM',
                               beamprocess='RAMP-SQUEEZE-6.5TeV-ATS-1m-2017_V3_V1')
 (1493433699L,
 array([[  0.00000000e+00,   1.00000000e+00,   2.00000000e+00, ...,
           1.20591610e+03,   1.20611610e+03,   1.21000000e+03],
        [  4.50000000e+02,   4.50010000e+02,   4.50040000e+02, ...,
           6.49999200e+03,   6.49999970e+03,   6.50000000e+03]]))
tvalue=[opt.time for opt in ot]
mom=np.interp(tvalue,steps,val)
for vv,opt in zip(mom,ot):
  print( "%7.1f %s"%(vv,opt.name) )

  450.0 R2017a_A11mC11mA10mL10m
  452.2 R2017a_A11mC11mA10mL10m
  459.0 R2017a_A11mC11mA10mL10m
  470.2 R2017a_A11mC11mA10mL10m
  486.0 R2017a_A11mC11mA10mL10m
  530.9 R2017a_A11mC11mA10mL10m
  593.9 R2017a_A11mC11mA10mL10m
  705.6 R2017a_A11mC11mA10mL10m
  843.5 R2017a_A11mC11mA10mL10m
 1054.3 R2017a_A11mC11mA10mL10m
 1317.6 R2017a_A11mC11mA10mL10m
 1607.1 R2017a_A11mC11mA10mL10m
 1694.0 R2017a_A11mC11mA10mL10m
 2197.8 R2017a_A970C970A10mL970
 2423.6 R2017a_A920C920A10mL920
 2684.2 R2017a_A850C850A10mL850
 3025.9 R2017a_A740C740A10mL740
 3454.4 R2017a_A630C630A10mL630
 4027.7 R2017a_A530C530A10mL530
 4456.2 R2017a_A440C440A10mL440
 4687.8 R2017a_A360C360A10mL360
 4971.6 R2017a_A310C310A10mL310
 5203.2 R2017a_A230C230A10mL300
 5382.7 R2017a_A180C180A10mL300
 5643.3 R2017a_A135C135A10mL300
 6071.8 R2017a_A100C100A10mL300
 6500.0 R2017a_A100C100A10mL300

```

### Get knob factors
```python
ot = lsa.getOpticTable('PHYSICS-2.51TeV-4m-2015_V1@90_[END]')
f = lsa.getKnobFactors('LHCBEAM2/IP1_SEPSCAN_Y_MM', ot[0])
```
```
{'RCBCV5.R1B2/KICK': -8.138696574e-05,
 'RCBCV6.L1B2/KICK': -3.353022415e-05,
 'RCBCV7.R1B2/KICK': 0.0,
 'RCBYV4.L1B2/KICK': 0.0,
 'RCBYVS4.L1B2/KICK': 5.584873181e-05,
 'RCBYVS4.R1B2/KICK': 0.0001292294752}
```

### search parameter names
```python
lsa.findParameterNames(deviceName='LHCBEAM',regexp=r'mom')
[u'LHCBEAM/MOMENTUM-TRIM', u'LHCBEAM/MOMENTUM']
lsa.findParameterNames(groupName='ALL MAGNETS',regexp=r'RQTL9\.L7.*/IREF')
[u'RPMBB.RR73.RQTL9.L7B1/IREF', u'RPMBB.RR73.RQTL9.L7B2/IREF']
```

```python
```
### PowerConverterInfo

```python
pcname=lsa.findPCNameByMadStrength('kq7.r5b1',full=True)
dev=lsa.deviceService.findPowerConverterInfo('RPHGA.RR57.RQ7.R5B1')
print(dev.getDidtMin())
print(dev.getInom())
```

### Get the parameter hierarchy tree for a parameter
```lsa.getParameterHierarchy('LHCBEAM1/IP1_SEPSCAN_X_MM')
{'I': ['RCBCH6.L1B1/I',
  'RCBYHS4.R1B1/I',
  'RCBYH4.L1B1/I',
  'RCBYHS4.L1B1/I',
  'RCBCH5.R1B1/I'],
 'IREF': ['RPLB.RR13.RCBCH6.L1B1/IREF',
  'RPLB.RR17.RCBYHS4.R1B1/IREF',
  'RPLB.RR13.RCBYH4.L1B1/IREF',
  'RPLB.RR13.RCBYHS4.L1B1/IREF',
  'RPLB.RR17.RCBCH5.R1B1/IREF'],
 'K': ['RCBCH6.L1B1/KICK',
  'RCBYHS4.R1B1/KICK',
  'RCBYH4.L1B1/KICK',
  'RCBYHS4.L1B1/KICK',
  'RCBCH5.R1B1/KICK'],
 'KNOB': ['LHCBEAM1/IP1_SEPSCAN_X_MM'],
 'K_SMOOTH': ['RCBCH6.L1B1/K_SMOOTH',
  'RCBYHS4.R1B1/K_SMOOTH',
  'RCBYH4.L1B1/K_SMOOTH',
  'RCBYHS4.L1B1/K_SMOOTH',
  'RCBCH5.R1B1/K_SMOOTH']}
```

