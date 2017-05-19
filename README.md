# pylsa
A Python wrapping of LSA API

Limited use for the time being

## Extract trims for a particular beamProcess, parameter, and time window
```python
import pylsa
lsaClient = pylsa.LSAClient()
t1='2015-11-22 00:00:00'
t2='2015-11-23 00:00:00'
trims = lsaClient.getTrims(beamprocess="PHYSICS-2.51TeV-4m-2015_V1@90_[END]", parameter="LHCBEAM2/IP1_SEPSCAN_Y_MM", start=t1, end=t2)
```

## Get optics tables
```
In [1]: ot = lsaClient.getOpticTable('RAMP-SQUEEZE-6.5TeV-ATS-1m-2017_V1')

In [2]: ot
Out[2]: 
[OpticTableItem(time=0, id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=30, id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=60, id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=120, id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=200, id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=300, id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=400, id=3789, name='R2017a_A11mC11mA10mL10m'),
 OpticTableItem(time=452, id=3795, name='R2017a_A970C970A10mL970'),
 OpticTableItem(time=491, id=3791, name='R2017a_A920C920A10mL920'),
 OpticTableItem(time=536, id=3802, name='R2017a_A850C850A10mL850'),
 OpticTableItem(time=595, id=3797, name='R2017a_A740C740A10mL740'),
 OpticTableItem(time=669, id=3794, name='R2017a_A630C630A10mL630'),
 OpticTableItem(time=768, id=3792, name='R2017a_A530C530A10mL530'),
 OpticTableItem(time=842, id=3787, name='R2017a_A440C440A10mL440'),
 OpticTableItem(time=882, id=3799, name='R2017a_A360C360A10mL360'),
 OpticTableItem(time=931, id=3796, name='R2017a_A310C310A10mL310'),
 OpticTableItem(time=971, id=3803, name='R2017a_A230C230A10mL300'),
 OpticTableItem(time=1002, id=3807, name='R2017a_A180C180A10mL300'),
 OpticTableItem(time=1047, id=3804, name='R2017a_A135C135A10mL300'),
 OpticTableItem(time=1121, id=3788, name='R2017a_A100C100A10mL300'),
 OpticTableItem(time=1210, id=3788, name='R2017a_A100C100A10mL300')]
```

## Get knob factors
```python
ot = lsaClient.getOpticTable('PHYSICS-2.51TeV-4m-2015_V1@90_[END]')
f = lsaClient.getKnobFactors('LHCBEAM2/IP1_SEPSCAN_Y_MM', ot[0])
```
```
{'RCBCV5.R1B2/KICK': -8.138696574e-05,
 'RCBCV6.L1B2/KICK': -3.353022415e-05,
 'RCBCV7.R1B2/KICK': 0.0,
 'RCBYV4.L1B2/KICK': 0.0,
 'RCBYVS4.L1B2/KICK': 5.584873181e-05,
 'RCBYVS4.R1B2/KICK': 0.0001292294752}
```

## Get parameter factors
```python
lsa.getParameterNames('LHCBEAM','mom')
[u'LHCBEAM/MOMENTUM-TRIM', u'LHCBEAM/MOMENTUM']
```

```python
lsa.getLastTrim('RAMP-SQUEEZE-6.5TeV-ATS-1m-2017_V3_V1','LHCBEAM/MOMENTUM')
(1493433699L,
 array([[  0.00000000e+00,   1.00000000e+00,   2.00000000e+00, ...,
           1.20591610e+03,   1.20611610e+03,   1.21000000e+03],
        [  4.50000000e+02,   4.50010000e+02,   4.50040000e+02, ...,
           6.49999200e+03,   6.49999970e+03,   6.50000000e+03]]))
```
