import pjlsa
import numpy as np
import pytest

#  %load_ext autoreload
#  %autoreload 2

lsa = pjlsa.LSAClient()


def test_findHyperCycles():
    lst = lsa.findHyperCycles()
    assert len(lst) > 3


def test_findBeamProcesses():
    lst = lsa.findBeamProcesses()
    assert len(lst) > 3


def test_parameter():
    names = lsa.findParameterNames("LHCBEAM1")
    assert len(names) > 10


def test_trim():
    t1 = "2018-09-22 00:00:00"
    t2 = "2018-09-23 00:00:00"
    name = "LHCBEAM2/IP1_SEPSCAN_Y_MM"
    trims = lsa.getTrims(
        beamprocess="PHYSICS-6.5TeV-30cm-120s-2018_V1@120_[END]",
        parameter=name,
        start=t1,
        end=t2,
    )
    assert len(trims[name][1]) > 2


def test_trim_function():
    name = "RQ5.L1B1/I"
    trims = lsa.getTrims(
        beamprocess="PC_INTERLOCK_REF-SQUEEZE-6.5TeV-ATS-1m-30cm-2018_V1",
        parameter=name
    )
    func = trims[name].data
    assert len(func) > 0
    assert type(func[0]) is np.ndarray
    assert func[0].shape == (2, 329)


def test_optics():
    optics_list = lsa.getOpticTable("RAMP-SQUEEZE-6.5TeV-ATS-1m-2017_V1")
    assert len(optics_list) > 3


def test_factors():
    ot = lsa.getOpticTable("PHYSICS-6.5TeV-30cm-120s-2018_V1@120_[END]")
    f = lsa.getKnobFactors("LHCBEAM2/IP1_SEPSCAN_Y_MM", ot[0])
    assert len(f) > 3


def test_beamprocess():
    bp = lsa._getBeamProcess("PHYSICS-6.5TeV-30cm-120s-2018_V1@120_[END]")
    bp1 = lsa._getBeamProcessByUser("LHC.USER.PHYSICS", "6.5TeV_2018_PELP_RAMP")
    assert (bp == bp1) == 1


def test_users():
    users = lsa.getUsers("6.5TeV_2017")
    assert len(users) > 5


def test_device():
    devices = lsa._findDevices(deviceGroupName="COLLIMATORS")
    assert len(devices) > 1


def test_java_api():
    # assert jpype import system not available
    with pytest.raises(ImportError):
        from cern.lsa.client import ServiceLocator

    # assert LSA and JPype import system was loaded
    with lsa.java_api():
        from cern.lsa.client import ServiceLocator
        assert hasattr(ServiceLocator, 'getService')

    # assert clean-up happened
    with pytest.raises(ImportError):
        from cern.lsa.client import ServiceLocator
