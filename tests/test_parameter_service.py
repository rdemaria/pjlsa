from lsa_test_util import *
from jpype_test import *
from pjlsa.domain import *
import pytest
import jpype as jp
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


def test_findParameter_findsNothing_returnsNone(lsa_client):
    lsa_client.jmock_parameterService.findParameters = JStub(returns=set())
    ret = lsa_client.parameterService.findParameter('Test/I_DONT_EXIST')
    assert ret is None
    java_args = lsa_client.jmock_parameterService.findParameters.assert_called_once()
    assert java_args[0].parameterNames == {'Test/I_DONT_EXIST'}


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


def test_findParameters_byMultipleCriteria_returns(lsa_client):
    param1, param2 = JMock(Parameter), JMock(Parameter)
    lsa_client.jmock_parameterService.findParameters = JStub(returns={param1, param2})
    ret = lsa_client.parameterService.findParameters(names=['Test1/P1', 'Test2/P2'], accelerator='LHC',
                                                     critical=False, multiplexed=True, virtual=False,
                                                     parameterGroups='Group', devices=['D1', 'D2'],
                                                     parameterTypes=['K'], particleTransfers='LHCRING',
                                                     acceleratorZones=['LHC'], namePattern='Test1/*')
    assert set(ret) == {param1(), param2()}
    java_args = lsa_client.jmock_parameterService.findParameters.assert_called_once()
    assert java_args[0].parameterNames == {'Test1/P1', 'Test2/P2'}
    assert java_args[0].accelerator == CernAccelerator.LHC
    assert java_args[0].critical == False
    assert java_args[0].multiplexed == True
    assert java_args[0].virtual == False
    assert java_args[0].parameterGroups == {'Group'}
    assert java_args[0].deviceNames == {'D1', 'D2'}
    assert java_args[0].parameterTypeNames == {'K'}
    assert java_args[0].particleTransfers == {LhcParticleTransfer.LHCRING}
    assert java_args[0].acceleratorZones == {LhcAcceleratorZone.LHC}
    assert java_args[0].parameterNamePattern == 'Test1/*'


def test_findParameters_findsNothing_returnsEmpty(lsa_client):
    lsa_client.jmock_parameterService.findParameters = JStub(returns=set())
    ret = lsa_client.parameterService.findParameters(names=['Test/I_DONT_EXIST'])
    assert ret == []
    java_args = lsa_client.jmock_parameterService.findParameters.assert_called_once()
    assert java_args[0].parameterNames == {'Test/I_DONT_EXIST'}


def test_findParametersForEditing_byMultipleCriteria_returns(lsa_client):
    param1, param2 = JMock(ParameterForEditing), JMock(ParameterForEditing)
    lsa_client.jmock_parameterService.findParametersForEditing = JStub(returns={param1, param2})
    ret = lsa_client.parameterService.findParametersForEditing(names=['Test1/P1', 'Test2/P2'], accelerator='AD',
                                                               critical=False, multiplexed=True, virtual=False,
                                                               parameterGroups='Group', devices=['D1', 'D2'],
                                                               parameterTypes=['K'], particleTransfers='ADRING',
                                                               acceleratorZones=['AD'], namePattern='*Test1*')
    assert set(ret) == {param1(), param2()}
    java_args = lsa_client.jmock_parameterService.findParametersForEditing.assert_called_once()
    assert java_args[0].parameterNames == {'Test1/P1', 'Test2/P2'}
    assert java_args[0].accelerator == CernAccelerator.AD
    assert java_args[0].critical == False
    assert java_args[0].multiplexed == True
    assert java_args[0].virtual == False
    assert java_args[0].parameterGroups == {'Group'}
    assert java_args[0].deviceNames == {'D1', 'D2'}
    assert java_args[0].parameterTypeNames == {'K'}
    assert java_args[0].particleTransfers == {AdParticleTransfer.ADRING}
    assert java_args[0].acceleratorZones == {AdAcceleratorZone.AD}
    assert java_args[0].parameterNamePattern == '*Test1*'


def test_findParametersForEditing_byMultipleCriteria_findsNothing_returnsEmpty(lsa_client):
    lsa_client.jmock_parameterService.findParametersForEditing = JStub(returns=set())
    ret = lsa_client.parameterService.findParametersForEditing(names=['Test/I_DONT_EXIST'])
    assert ret == []
    java_args = lsa_client.jmock_parameterService.findParametersForEditing.assert_called_once()
    assert java_args[0].parameterNames == {'Test/I_DONT_EXIST'}


def test_findParameterTypes_byNames_returns(lsa_client):
    pt1, pt2 = JMock(ParameterType), JMock(ParameterType)
    lsa_client.jmock_parameterService.findParameterTypes = JStub(returns={pt1, pt2})
    ret = lsa_client.parameterService.findParameterTypes(['K', 'I'])
    assert set(ret) == {pt1(), pt2()}
    java_args = lsa_client.jmock_parameterService.findParameterTypes.assert_called_once()
    assert java_args[0].parameterTypeNames == {'K', 'I'}


def test_findParameterTypes_byDeviceTypes_returns(lsa_client):
    pt1, pt2 = JMock(ParameterType), JMock(ParameterType)
    lsa_client.jmock_parameterService.findParameterTypes = JStub(returns={pt1, pt2})
    ret = lsa_client.parameterService.findParameterTypes(deviceTypes=['LHC.SomeDevice'])
    assert set(ret) == {pt1(), pt2()}
    java_args = lsa_client.jmock_parameterService.findParameterTypes.assert_called_once()
    assert java_args[0].deviceTypeNames == {'LHC.SomeDevice'}


def test_findParameterTypes_noArgument_requestsAll(lsa_client):
    pt1, pt2, pt3 = JMock(ParameterType), JMock(ParameterType), JMock(ParameterType)
    lsa_client.jmock_parameterService.findParameterTypes = JStub(returns={pt1, pt2, pt3})
    ret = lsa_client.parameterService.findParameterTypes()
    assert set(ret) == {pt1(), pt2(), pt3()}
    java_args = lsa_client.jmock_parameterService.findParameterTypes.assert_called_once()
    assert java_args[0] == jp.JClass('cern.lsa.domain.settings.ParameterTypesRequest').builder().ALL_PARAMETER_TYPES


def test_findParameterTypes_byNames_findsNothing_returnsEmpty(lsa_client):
    lsa_client.jmock_parameterService.findParameterTypes = JStub(returns=set())
    ret = lsa_client.parameterService.findParameterTypes(['FOOBAR'])
    assert ret == []
    java_args = lsa_client.jmock_parameterService.findParameterTypes.assert_called_once()
    assert java_args[0].parameterTypeNames == {'FOOBAR'}


def test_findParameterType_byNames_returns(lsa_client):
    pt = JMock(ParameterType)
    lsa_client.jmock_parameterService.findParameterTypes = JStub(returns={pt})
    ret = lsa_client.parameterService.findParameterType('K')
    assert ret == pt()
    java_args = lsa_client.jmock_parameterService.findParameterTypes.assert_called_once()
    assert java_args[0].parameterTypeNames == {'K'}


def test_findParameterTypes_byNames_findsNothing_returnsNone(lsa_client):
    lsa_client.jmock_parameterService.findParameterTypes = JStub(returns=set())
    ret = lsa_client.parameterService.findParameterType('FOOBAR')
    assert ret is None
    java_args = lsa_client.jmock_parameterService.findParameterTypes.assert_called_once()
    assert java_args[0].parameterTypeNames == {'FOOBAR'}


def test_findHierarchies_byParametersAndNames_returns(lsa_client):
    param, param_by_name = JMock(Parameter), JMock(Parameter)
    lsa_client.jmock_parameterService.findParameters = JStub(returns={param_by_name})
    lsa_client.jmock_parameterService.findHierarchyNames = JStub(returns={'DEFAULT'})
    ret = lsa_client.parameterService.findHierarchies(['FOOBAR', param()])
    assert ret == ['DEFAULT']
    param_lookup_args = lsa_client.jmock_parameterService.findParameters.assert_called_once()
    assert param_lookup_args[0].parameterNames == {'FOOBAR'}
    java_args = lsa_client.jmock_parameterService.findHierarchyNames.assert_called_once()
    assert java_args[0].containsAll(to_java([param_by_name(), param()]))


def test_saveParameters_delegates(lsa_client):
    pa = JMock(ParameterAttributes)
    lsa_client.jmock_parameterService.saveParameters = JStub()
    lsa_client.parameterService.saveParameters(pa())
    java_args = lsa_client.jmock_parameterService.saveParameters.assert_called_once()
    assert java_args[0] == to_java([pa()])


def test_saveParameterRelations_delegates(lsa_client):
    top_param1, dep_param1_by_name, dep_param1 = JMock(Parameter), JMock(Parameter), JMock(Parameter)
    dep_param1_by_name._getName = JStub(returns='DP1/byName')
    top_param2_by_name, dep_param2_by_name, dep_param2 = JMock(Parameter), JMock(Parameter), JMock(Parameter)
    top_param2_by_name._getName = JStub(returns='TP2/byName')
    dep_param2_by_name._getName = JStub(returns='DP2/byName')
    lsa_client.jmock_parameterService.findParameters = JStub(returns={dep_param1_by_name, top_param2_by_name,
                                                                      dep_param2_by_name})
    lsa_client.jmock_parameterService.saveParameterRelations = JStub()
    lsa_client.parameterService.saveParameterRelations({top_param1(): ['DP1/byName', dep_param1()],
                                                        'TP2/byName': ['DP2/byName', dep_param2()]})
    param_lookup_args = lsa_client.jmock_parameterService.findParameters.assert_called_once()
    assert param_lookup_args[0].parameterNames == {'TP2/byName', 'DP1/byName', 'DP2/byName'}
    java_args = lsa_client.jmock_parameterService.saveParameterRelations.assert_called_once()
    assert java_args[0].get(top_param1()).containsAll(to_java([dep_param1(), dep_param1_by_name()]))
    assert java_args[0].get(top_param2_by_name()).containsAll(to_java([dep_param2(), dep_param2_by_name()]))


def test_saveParameterTypes_delegates(lsa_client):
    pt1, pt2 = JMock(ParameterType), JMock(ParameterType)
    lsa_client.jmock_parameterService.saveParameterTypes = JStub()
    lsa_client.parameterService.saveParameterTypes([pt1(), pt2()])
    java_args = lsa_client.jmock_parameterService.saveParameterTypes.assert_called_once()
    assert java_args[0] == to_java([pt1(), pt2()])


def test_deleteParameterTypes_delegates(lsa_client):
    pt1, pt2 = JMock(ParameterType), JMock(ParameterType)
    lsa_client.jmock_parameterService.deleteParameterTypes = JStub()
    lsa_client.parameterService.deleteParameterTypes([pt1(), pt2()])
    java_args = lsa_client.jmock_parameterService.deleteParameterTypes.assert_called_once()
    assert java_args[0] == to_java([pt1(), pt2()])


def test_deleteParameters_delegates(lsa_client):
    p1, p2 = JMock(Parameter), JMock(Parameter)
    lsa_client.jmock_parameterService.deleteParameters = JStub()
    lsa_client.parameterService.deleteParameters([p1(), p2()])
    java_args = lsa_client.jmock_parameterService.deleteParameters.assert_called_once()
    assert java_args[0] == to_java([p1(), p2()])


def test_findParameterGroups_delegates(lsa_client):
    pg = JMock(ParameterGroup)
    lsa_client.jmock_parameterService.findParameterGroupsByAccelerator = JStub(returns={pg})
    lsa_client.parameterService.findParameterGroups('LHC')
    java_args = lsa_client.jmock_parameterService.findParameterGroupsByAccelerator.assert_called_once()
    assert java_args[0] == CernAccelerator.LHC


def test_saveParameterGroup_delegates(lsa_client):
    pg = JMock(ParameterGroup)
    lsa_client.jmock_parameterService.saveParameterGroup = JStub()
    lsa_client.parameterService.saveParameterGroup(pg())
    java_args = lsa_client.jmock_parameterService.saveParameterGroup.assert_called_once()
    assert java_args[0] == pg()


def test_deleteParameterGroup_delegates(lsa_client):
    pg = JMock(ParameterGroup)
    pg._getId = JStub(returns=42)
    lsa_client.jmock_parameterService.deleteParameterGroup = JStub()
    lsa_client.parameterService.deleteParameterGroup(pg())
    java_args = lsa_client.jmock_parameterService.deleteParameterGroup.assert_called_once()
    assert java_args[0] == 42


def test_addParametersToParameterGroup_delegates(lsa_client):
    pg = JMock(ParameterGroup)
    p1 = JMock(Parameter)
    p1._getName = JStub(returns='P1/Test')
    lsa_client.jmock_parameterService.addParametersToParameterGroup = JStub()
    lsa_client.parameterService.addParametersToParameterGroup(pg(), [p1(), 'P2/Test'])
    java_args = lsa_client.jmock_parameterService.addParametersToParameterGroup.assert_called_once()
    assert java_args[0] == pg()
    assert java_args[1] == to_java(['P1/Test', 'P2/Test'])


def test_removeParametersFromParameterGroup_delegates(lsa_client):
    pg = JMock(ParameterGroup)
    p1 = JMock(Parameter)
    p1._getName = JStub(returns='P1/Test')
    lsa_client.jmock_parameterService.removeParametersFromParameterGroup = JStub()
    lsa_client.parameterService.removeParametersFromParameterGroup(pg(), [p1(), 'P2/Test'])
    java_args = lsa_client.jmock_parameterService.removeParametersFromParameterGroup.assert_called_once()
    assert java_args[0] == pg()
    assert java_args[1] == to_java(['P1/Test', 'P2/Test'])


def test_findMakeRuleForParameterRelation_returns(lsa_client):
    sp = JMock(Parameter)
    sp._getName = JStub(returns='SP/Foo')
    mr = JMock(MakeRuleForParameterRelation)
    lsa_client.jmock_parameterService.findMakeRuleForParameterRelation = JStub(returns=mr())
    lsa_client.parameterService.findMakeRuleForParameterRelation(source=sp(), dependent='DP/Test')
    java_args = lsa_client.jmock_parameterService.findMakeRuleForParameterRelation.assert_called_once()
    assert java_args[0].sourceParameterName == 'SP/Foo'
    assert java_args[0].dependentParameterName == 'DP/Test'


def test_findSourceParameterTree_returns(lsa_client):
    ptn = JMock(ParameterTreeNode)
    lsa_client.jmock_parameterService.findParameterTrees = JStub(returns={ptn()})
    ret = lsa_client.parameterService.findSourceParameterTree(parameter='Test/Foo')
    assert ret == ptn
    java_args = lsa_client.jmock_parameterService.findParameterTrees.assert_called_once()
    assert java_args[0].parameterNames == {'Test/Foo'}
    assert str(java_args[0].treeDirection) == 'SOURCE_TREE'
    assert java_args[0].hierarchy == 'DEFAULT'


def test_findDependentParameterTree_returns(lsa_client):
    ptn = JMock(ParameterTreeNode)
    param = JMock(Parameter)
    param._getName = JStub(returns='Test/Param')
    lsa_client.jmock_parameterService.findParameterTrees = JStub(returns={ptn()})
    ret = lsa_client.parameterService.findDependentParameterTree(parameter=param(), hierarchy='NONDEFAULT')
    assert ret == ptn
    java_args = lsa_client.jmock_parameterService.findParameterTrees.assert_called_once()
    assert java_args[0].parameterNames == {'Test/Param'}
    assert str(java_args[0].treeDirection) == 'DEPENDENT_TREE'
    assert java_args[0].hierarchy == 'NONDEFAULT'
