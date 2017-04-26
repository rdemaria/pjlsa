import pylsa

#  %load_ext autoreload
#  %autoreload 2

lsa=pylsa.LSAClient()

def test_hypercycle():
    hyperlist=lsa.findHyperCycles()
    assert len(hyperlist)>3

def test_parameter():
   names=lsa.getParameterNames('LHCBEAM1')
   assert len(names)>10

def test_trim():
    t1='2015-11-22 00:00:00'
    t2='2015-11-23 00:00:00'
    name="LHCBEAM2/IP1_SEPSCAN_Y_MM"
    trims = lsa.getTrims(beamprocess="PHYSICS-2.51TeV-4m-2015_V1@90_[END]",
            parameter=name, start=t1, end=t2)
    assert len(trims[name][1])>2

def test_optics():
   optics_list=lsa.getOpticTable('RAMP-SQUEEZE-6.5TeV-ATS-1m-2017_V1')
   assert len(optics_list)>3

def test_factors():
   ot = lsa.getOpticTable('PHYSICS-2.51TeV-4m-2015_V1@90_[END]')
   f = lsa.getKnobFactors('LHCBEAM2/IP1_SEPSCAN_Y_MM', ot[0])
   assert len(f)>3

def test_beamprocess():
  bp=lsa.getBeamProcess("PHYSICS-2.51TeV-4m-2015_V1@90_[END]")
  bp1=lsa.getBeamProcessByUser('LHC.USER.PHYSICS','2.51TeV_2015_CRS')
  assert (bp==bp1)==1

def test_users():
  users=lsa.getUsers('6.5TeV_2017')
  assert len(users)>5

