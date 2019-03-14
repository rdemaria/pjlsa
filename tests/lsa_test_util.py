import pjlsa
import pytest
from jpype_test import *
from unittest.mock import Mock


@pytest.fixture
def lsa_client():
    pjlsa.lsa_client._jp.ServiceLocator = Mock()
    pjlsa.lsa_client._jp.ServiceLocator.getService = lambda jc: JMock(jc)
    lsa_client = pjlsa.LsaClient()
    for t in dir(lsa_client):
        mock = getattr(lsa_client, t)
        if isinstance(mock, JMock):
            setattr(lsa_client, t, mock())
            setattr(lsa_client, 'jmock' + t, mock)
    return lsa_client
