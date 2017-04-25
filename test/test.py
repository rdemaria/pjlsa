

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



