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


def test_findContextSettings_byContextNameThatDoesNotExist_throws(lsa_client):
    ctxSet = JMock(ContextSettings)
    lsa_client.jmock_contextService.findStandAloneBeamProcesses = JStub(returns=set())
    lsa_client.jmock_settingService.findContextSettings = JStub(returns=ctxSet)
    with pytest.raises(ValueError) as error:
        lsa_client.settingService.findContextSettings('SomeBeamProcess')
    assert 'not found' in str(error)
