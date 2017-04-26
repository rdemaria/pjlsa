

from pylsa import *

import pylsa

#  %load_ext autoreload
#  %autoreload 2

lsa=pylsa.LSAClient()

lsa.findHyperCycles()

hp=lsa.getHyperCycle('6.5TeV_2017')

lsa.getUsers('6.5TeV_2017')

bp=lsa.getBeamProcess('6.5TeV_2017','LHC.USER.SQUEEZE6')

hp=lsa.getHyperCycle('6.5TeV_2017')

headers=lsa.getTrim(bp,'LHCBEAM2/IP1_SEPSCAN_Y_MM')

pl=lsa.getParameterList('LHCBEAM1')

pgl=list(lsa.parameterService.findParameterGroupsByAccelerator(bp.getAccelerator()))


t1='2015-11-22 00:00:00'
t2='2015-11-23 00:00:00'
trims = lsa.getTrims(beamprocess="PHYSICS-2.51TeV-4m-2015_V1@90_[END]", parameter="LHCBEAM2/IP1_SEPSCAN_Y_MM", start=t1, end=t2)


trims = lsa.getTrims(beamprocess="PHYSICS-2.51TeV-4m-2015_V1@90_[END]",        parameter="LHCBEAM2/IP1_SEPSCAN_Y_MM", start=t1, end=t2)

lsa.getOpticTable('RAMP-SQUEEZE-6.5TeV-ATS-1m-2017_V1')

ot = lsa.getOpticTable('PHYSICS-2.51TeV-4m-2015_V1@90_[END]')
f = lsa.getKnobFactors('LHCBEAM2/IP1_SEPSCAN_Y_MM', ot[0])


