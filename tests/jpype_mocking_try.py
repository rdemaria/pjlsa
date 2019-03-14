import pjlsa
from jpype_test import *

user = JMock(pjlsa.domain.AcceleratorUser)
ctxSvcMock = JMock(pjlsa._jpype.ContextService)
ctxSvcMock.findAcceleratorUsers = JStub(returns={user})
ctxSvcMock.findLoggingHistory = JStub(returns=['Hello'])

lsa = pjlsa.LsaClient()
lsa._contextService = ctxSvcMock()

print(ctxSvcMock().findLoggingHistory(1, 1, pjlsa.domain.CernAccelerator.LHC.__javavalue__))
print(ctxSvcMock().findLoggingHistory(2, 2, pjlsa.domain.CernAccelerator.SPS.__javavalue__))
print(ctxSvcMock().findLoggingHistory(7, 5, pjlsa.domain.CernAccelerator.AD.__javavalue__))

result = lsa.contextService.findAcceleratorUsers('LHC.USER.ALL')
print(result)
print(user)
print(ctxSvcMock.findAcceleratorUsers.calls())
print(ctxSvcMock.findLoggingHistory.calls())

assert len(result) == 1
assert result[0] == user()
calls = ctxSvcMock.findAcceleratorUsers.calls()
assert len(calls) == 1
assert calls[0][0].acceleratorUserNames == {'LHC.USER.ALL'}
