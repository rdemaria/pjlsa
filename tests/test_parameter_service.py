from lsa_test_util import *
from jpype_test import *
from pjlsa.domain import *
import pytest
from datetime import datetime


def test_findParameter_byName_returns(lsa_client):
    param = JMock(Parameter)
    lsa_client.jmock_parameterService.findParameters = JStub(returns={param})
    ret = lsa_client.parameterService.findParameter('Test/Property')
    assert ret == param()
    java_args = lsa_client.jmock_parameterService.findParameters.assert_called_once()
    assert java_args[0].parameterNames == {'Test/Property'}


def test_findParameter_byAcceleratorName_throwsDueToMultipleResults(lsa_client):
    param1, param2, param3 = JMock(Parameter), JMock(Parameter), JMock(Parameter)
    lsa_client.jmock_parameterService.findParameters = JStub(returns={param1, param2, param3})
    with pytest.raises(ValueError) as error:
        lsa_client.parameterService.findParameter(accelerator='SPS')
    assert 'Expected 1 matching' in str(error)
    java_args = lsa_client.jmock_parameterService.findParameters.assert_called_once()
    assert java_args[0].accelerator == CernAccelerator.SPS


def test_findParameters_byName_returns(lsa_client):
    param = JMock(Parameter)
    lsa_client.jmock_parameterService.findParameters = JStub(returns={param})
    ret = lsa_client.parameterService.findParameters('Test/Property')
    assert ret == [param()]
    java_args = lsa_client.jmock_parameterService.findParameters.assert_called_once()
    assert java_args[0].parameterNames == {'Test/Property'}


def test_findParameters_byAcceleratorName_returnsMultiple(lsa_client):
    param1, param2, param3 = JMock(Parameter), JMock(Parameter), JMock(Parameter)
    lsa_client.jmock_parameterService.findParameters = JStub(returns={param1, param2, param3})
    ret = lsa_client.parameterService.findParameters(accelerator='SPS')
    assert set(ret) == {param1(), param2(), param3()}
    java_args = lsa_client.jmock_parameterService.findParameters.assert_called_once()
    assert java_args[0].accelerator == CernAccelerator.SPS


def test_findParameters_byAccelerator_returnsMultiple(lsa_client):
    param1, param2, param3 = JMock(Parameter), JMock(Parameter), JMock(Parameter)
    lsa_client.jmock_parameterService.findParameters = JStub(returns={param1, param2, param3})
    ret = lsa_client.parameterService.findParameters(accelerator=CernAccelerator.SPS)
    assert set(ret) == {param1(), param2(), param3()}
    java_args = lsa_client.jmock_parameterService.findParameters.assert_called_once()
    assert java_args[0].accelerator == CernAccelerator.SPS
