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
