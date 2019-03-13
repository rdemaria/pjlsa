import pjlsa
import jpype

org = jpype.JPackage('org')
java = jpype.JPackage('java')
Mockito = org.mockito.Mockito
ArgumentCaptor = org.mockito.ArgumentCaptor

lsa = pjlsa.LsaClient()
lsa._contextService = Mockito.mock(pjlsa._jpype.ContextService)
user = Mockito.mock(pjlsa.domain.AcceleratorUser)
hs = java.util.HashSet()
hs.add(user)
Mockito.doReturn(hs, None).when(lsa._contextService).findAcceleratorUsers(Mockito.any())

result = lsa.contextService.findAcceleratorUsers('LHC.USER.ALL')
print(result)
print(user)
assert len(result) == 1
assert result[0] == user
Mockito.verify(lsa._contextService).findAcceleratorUser(Mockito.any())