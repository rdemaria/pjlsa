from lsa_test_util import *
from jpype_test import *
from pjlsa.domain import *


def test_basic(lsa_client):
    bp = JMock(StandAloneBeamProcess)
    lsa_client.mock_contextService.findStandAloneBeamProcesses = JStub(returns={bp})
    ret = lsa_client.contextService.findStandAloneBeamProcess('SomeBeamProcess')
    assert ret == bp()
    java_args = lsa_client.mock_contextService.findStandAloneBeamProcesses.assert_called_once()
    assert java_args[0].beamProcessNames == {'SomeBeamProcess'}
