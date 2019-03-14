from lsa_test_util import *
from jpype_test import *
from pjlsa.domain import *
import pytest


def test_findStandAloneBeamProcess_byName_returns(lsa_client):
    bp = JMock(StandAloneBeamProcess)
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(returns={bp})
    ret = lsa_client.contextService.findStandAloneBeamProcess('SomeBeamProcess')
    assert ret == bp()
    java_args = lsa_client.jmock_contextService.findStandAloneBeamProcesses.assert_called_once()
    assert java_args[0].beamProcessNames == {'SomeBeamProcess'}


def test_findStandAloneBeamProcess_findingMultipleBps_throws(lsa_client):
    bp1, bp2 = JMock(StandAloneBeamProcess), JMock(StandAloneBeamProcess)
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(returns={bp1, bp2})
    with pytest.raises(ValueError) as error:
        lsa_client.contextService.findStandAloneBeamProcess(accelerator=CernAccelerator.LHC)
    assert 'Expected 1 matching' in str(error)
    java_args = lsa_client.jmock_contextService.findStandAloneBeamProcesses.assert_called_once()
    assert java_args[0].accelerator == CernAccelerator.LHC


def test_findStandAloneBeamProcesses_byAccelerator_returns(lsa_client):
    bp1, bp2 = JMock(StandAloneBeamProcess), JMock(StandAloneBeamProcess)
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(returns={bp1, bp2})
    ret = lsa_client.contextService.findStandAloneBeamProcesses(accelerator=CernAccelerator.LHC)
    assert set(ret) == {bp1(), bp2()}
    java_args = lsa_client.jmock_contextService.findStandAloneBeamProcesses.assert_called_once()
    assert java_args[0].accelerator == CernAccelerator.LHC


def test_findStandAloneBeamProcesses_byAcceleratorAndMultiplexityAndResidency_returns(lsa_client):
    bp = JMock(StandAloneBeamProcess)
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(returns={bp})
    ret = lsa_client.contextService.findStandAloneBeamProcesses(accelerator=CernAccelerator.LHC, multiplexed=False,
                                                                resident=True)
    assert ret == [bp()]
    java_args = lsa_client.jmock_contextService.findStandAloneBeamProcesses.assert_called_once()
    assert java_args[0].accelerator == CernAccelerator.LHC
    assert java_args[0].multiplexed == False
    assert java_args[0].resident == True


def test_findStandAloneBeamProcesses_findsNothing_returns(lsa_client):
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(returns=set())
    ret = lsa_client.contextService.findStandAloneBeamProcesses('SomethingThatDoesNotExist')
    assert ret == []
    java_args = lsa_client.jmock_contextService.findStandAloneBeamProcesses.assert_called_once()
    assert java_args[0].beamProcessNames == {'SomethingThatDoesNotExist'}


def test_findStandAloneBeamProcesses_multipleNames_returns(lsa_client):
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(returns=set())
    ret = lsa_client.contextService.findStandAloneBeamProcesses(names=['BP1', 'BP2'])
    assert ret == []
    java_args = lsa_client.jmock_contextService.findStandAloneBeamProcesses.assert_called_once()
    assert java_args[0].beamProcessNames == {'BP1', 'BP2'}


def test_findStandAloneCycle_byName_returns(lsa_client):
    cyc = JMock(StandAloneCycle)
    lsa_client.jmock_contextService.findStandAloneCycles = JStub(returns={cyc})
    ret = lsa_client.contextService.findStandAloneCycle('SomeCycle')
    assert ret == cyc()
    java_args = lsa_client.jmock_contextService.findStandAloneCycles.assert_called_once()
    assert java_args[0].cycleNames == {'SomeCycle'}


def test_findStandAloneCycle_findingMultipleCycs_throws(lsa_client):
    cyc1, cyc2 = JMock(StandAloneCycle), JMock(StandAloneCycle)
    lsa_client.jmock_contextService.findStandAloneCycles = JStub(returns={cyc1, cyc2})
    with pytest.raises(ValueError) as error:
        lsa_client.contextService.findStandAloneCycle(accelerator=CernAccelerator.SPS)
    assert 'Expected 1 matching' in str(error)
    java_args = lsa_client.jmock_contextService.findStandAloneCycles.assert_called_once()
    assert java_args[0].accelerator == CernAccelerator.SPS


def test_findStandAloneCycles_byAccelerator_returns(lsa_client):
    cyc1, cyc2 = JMock(StandAloneCycle), JMock(StandAloneCycle)
    lsa_client.jmock_contextService.findStandAloneCycles = JStub(returns={cyc1, cyc2})
    ret = lsa_client.contextService.findStandAloneCycles(accelerator=CernAccelerator.AD)
    assert set(ret) == {cyc1(), cyc2()}
    java_args = lsa_client.jmock_contextService.findStandAloneCycles.assert_called_once()
    assert java_args[0].accelerator == CernAccelerator.AD


def test_findStandAloneCycles_byAcceleratorAndMultiplexityAndResidency_returns(lsa_client):
    cyc = JMock(StandAloneCycle)
    lsa_client.jmock_contextService.findStandAloneCycles = JStub(returns={cyc})
    ret = lsa_client.contextService.findStandAloneCycles(accelerator=CernAccelerator.PSB, multiplexed=False,
                                                         resident=True)
    assert ret == [cyc()]
    java_args = lsa_client.jmock_contextService.findStandAloneCycles.assert_called_once()
    assert java_args[0].accelerator == CernAccelerator.PSB
    assert java_args[0].multiplexed == False
    assert java_args[0].resident == True


def test_findStandAloneCycles_findsNothing_returns(lsa_client):
    lsa_client.jmock_contextService.findStandAloneCycles = JStub(returns=set())
    ret = lsa_client.contextService.findStandAloneCycles('SomethingThatDoesNotExist')
    assert ret == []
    java_args = lsa_client.jmock_contextService.findStandAloneCycles.assert_called_once()
    assert java_args[0].cycleNames == {'SomethingThatDoesNotExist'}


def test_findStandAloneCycles_multipleNames_returns(lsa_client):
    lsa_client.jmock_contextService.findStandAloneCycles = JStub(returns=set())
    ret = lsa_client.contextService.findStandAloneCycles(names=['CYC1', 'CYC2'])
    assert ret == []
    java_args = lsa_client.jmock_contextService.findStandAloneCycles.assert_called_once()
    assert java_args[0].cycleNames == {'CYC1', 'CYC2'}
