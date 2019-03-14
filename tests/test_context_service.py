from lsa_test_util import *
from jpype_test import *
from pjlsa.domain import *
import pytest
from datetime import datetime


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
        lsa_client.contextService.findStandAloneBeamProcess(accelerator='LHC')
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
    ret = lsa_client.contextService.findStandAloneBeamProcesses(accelerator='LHC', multiplexed=False,
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
    ret = lsa_client.contextService.findStandAloneCycles(accelerator='PSB', multiplexed=False,
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


def test_findUserContextMappingHistory_withStrings_returns(lsa_client):
    ucm1, ucm2 = JMock(UserContextMapping), JMock(UserContextMapping)
    lsa_client.jmock_contextService.findUserContextMappingHistory = JStub(returns=[ucm1, ucm2])
    ret = lsa_client.contextService.findUserContextMappingHistory(accelerator='SPS',
                                                                  contextFamily='CYCLE',
                                                                  fromTime='2018-08-01 00:00:00',
                                                                  toTime='2018-09-10 00:00:00')
    assert ret == [ucm1(), ucm2()]
    java_args = lsa_client.jmock_contextService.findUserContextMappingHistory.assert_called_once()
    assert java_args == (CernAccelerator.SPS.__javavalue__, ContextFamily.CYCLE.__javavalue__,
                         datetime(2018, 8, 1, 0, 0, 0).timestamp() * 1000,
                         datetime(2018, 9, 10, 0, 0, 0).timestamp() * 1000)


def test_findUserContextMappingHistory_withObjects_returns(lsa_client):
    ucm1, ucm2 = JMock(UserContextMapping), JMock(UserContextMapping)
    from_time = datetime(2018, 5, 1, 0, 0, 42)
    to_time = datetime(2018, 5, 23, 0, 0, 42)
    lsa_client.jmock_contextService.findUserContextMappingHistory = JStub(returns=[ucm1, ucm2])
    ret = lsa_client.contextService.findUserContextMappingHistory(accelerator=CernAccelerator.PSB,
                                                                  contextFamily=ContextFamily.CYCLE,
                                                                  fromTime=from_time,
                                                                  toTime=to_time)
    assert ret == [ucm1(), ucm2()]
    java_args = lsa_client.jmock_contextService.findUserContextMappingHistory.assert_called_once()
    assert java_args == (CernAccelerator.PSB.__javavalue__, ContextFamily.CYCLE.__javavalue__,
                         from_time.timestamp() * 1000,
                         to_time.timestamp() * 1000)
