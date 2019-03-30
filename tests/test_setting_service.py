from lsa_test_util import *
from jpype_test import *
from pjlsa.domain import *
import pytest
from datetime import datetime


def test_findContextSettings_byContextName_returns(lsa_client):
    ctxSet = JMock(ContextSettings)
    someBp = JMock(StandAloneBeamProcess)
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(returns={someBp})
    lsa_client.jmock_settingService.findContextSettings = JStub(returns=ctxSet)
    ret = lsa_client.settingService.findContextSettings('SomeBeamProcess')
    assert ret == ctxSet()
    bp_req_args = lsa_client.jmock_contextService.findStandAloneBeamProcesses.assert_called_once()
    assert bp_req_args[0].beamProcessNames == {'SomeBeamProcess'}
    java_args = lsa_client.jmock_settingService.findContextSettings.assert_called_once()
    assert java_args[0].context == someBp


def test_findContextSettings_byContexts_returns(lsa_client):
    ctxSet = JMock(ContextSettings)
    someCycle = JMock(StandAloneCycle)
    lsa_client.jmock_contextService.findStandAloneCycles = JStub(returns={someCycle})
    lsa_client.jmock_settingService.findContextSettings = JStub(returns=ctxSet)
    ret = lsa_client.settingService.findContextSettings(someCycle())
    assert ret == ctxSet()
    java_args = lsa_client.jmock_settingService.findContextSettings.assert_called_once()
    assert java_args[0].context == someCycle()


def test_findContextSettings_byContextNameThatDoesNotExist_throws(lsa_client):
    ctxSet = JMock(ContextSettings)
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(returns=set())
    lsa_client.jmock_settingService.findContextSettings = JStub(returns=ctxSet)
    with pytest.raises(ValueError) as error:
        lsa_client.settingService.findContextSettings('SomeBeamProcess')
    assert 'not found' in str(error)


def test_findNotIncorporatedParameters_byContextNames_returns(lsa_client):
    nip = JMock(NotIncorporatedParameters)
    bps = {'BP1': JMock(StandAloneBeamProcess), 'BP2': JMock(StandAloneBeamProcess)}
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(lambda r: {bps[list(r.beamProcessNames)[0]]()})
    lsa_client.jmock_settingService.findNotIncorporatedParameters = JStub(returns=nip)
    ret = lsa_client.settingService.findNotIncorporatedParameters(sourceBp='BP1', sourcePoint=42,
                                                                  destinationBp='BP2', destinationPoint=1)
    assert ret == nip()
    java_args = lsa_client.jmock_settingService.findNotIncorporatedParameters.assert_called_once()
    assert java_args[0] == bps['BP1']()
    assert java_args[1] == 42
    assert java_args[2] == bps['BP2']()
    assert java_args[3] == 1


def test_findNotIncorporatedParameters_byContexts_returns(lsa_client):
    nip = JMock(NotIncorporatedParameters)
    bp1, bp2 = JMock(StandAloneBeamProcess), JMock(StandAloneBeamProcess)
    lsa_client.jmock_settingService.findNotIncorporatedParameters = JStub(returns=nip)
    ret = lsa_client.settingService.findNotIncorporatedParameters(sourceBp=bp1(), sourcePoint=123,
                                                                  destinationBp=bp2())
    assert ret == nip()
    java_args = lsa_client.jmock_settingService.findNotIncorporatedParameters.assert_called_once()
    assert java_args[0] == bp1()
    assert java_args[1] == 123
    assert java_args[2] == bp2()
    assert java_args[3] == 0


def test_findNotIncorporatedParameters_byContextNameThatDoesNotExist_throws(lsa_client):
    nip = JMock(NotIncorporatedParameters)
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(returns=set())
    lsa_client.jmock_settingService.findNotIncorporatedParameters = JStub(returns=nip)
    with pytest.raises(ValueError) as error:
        lsa_client.settingService.findNotIncorporatedParameters(sourceBp='BP1', sourcePoint=42,
                                                                destinationBp='BP2', destinationPoint=0)
    assert 'not found' in str(error)
