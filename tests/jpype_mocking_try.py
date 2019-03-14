import pjlsa
import jpype

org = jpype.JPackage('org')
java = jpype.JPackage('java')
Mockito = org.mockito.Mockito
ArgumentCaptor = org.mockito.ArgumentCaptor


class JavaMethodMock(object):
    def __init__(self, *, returns=None):
        self.return_value = returns
        self.object = None
        self.method_name = None
        self.overloads = None

    def calls(self):
        all_calls = []
        for method in self.overloads:
            param_types = method.getParameterTypes()
            captors = [ArgumentCaptor.forClass(p) for p in param_types]
            verifier = getattr(Mockito.verify(self.object._mock, Mockito.atLeast(0)), self.method_name)
            verifier(*[c.capture() for c in captors])
            all_calls.extend(zip(*[list(c.allValues) for c in captors]))
        return all_calls


class JavaClassMock(object):
    def __init__(self, jc):
        self._mock = Mockito.mock(jc)
        self._javaclass = jc

    def __setattr__(self, key, value):
        if isinstance(value, JavaMethodMock):
            self._stub(key, value)
        super().__setattr__(key, value)

    def _stub(self, method_name, mock):
        mock.object = self
        mock.method_name = method_name
        overloads = [m for m in jpype.reflect.getMethods(self._javaclass) if m.getName() == method_name]
        mock.overloads = overloads
        for method in overloads:
            param_types = method.getParameterTypes()
            stubber = getattr(Mockito.doReturn(mock.return_value, mock.return_value).when(self._mock), method_name)
            stubber(*[Mockito.any(t) for t in param_types])

    def __call__(self, *args, **kwargs):
        return self._mock


user = Mockito.mock(pjlsa.domain.AcceleratorUser)
hs = java.util.HashSet()
hs.add(user)

ctxSvcMock = JavaClassMock(pjlsa._jpype.ContextService)
ctxSvcMock.findAcceleratorUsers = JavaMethodMock(returns=hs)
ctxSvcMock.findLoggingHistory = JavaMethodMock(returns=java.util.Collections.singletonList('Hello'))

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
assert result[0] == user
calls = ctxSvcMock.findAcceleratorUsers.calls()
assert len(calls) == 1
assert calls[0][0].acceleratorUserNames == {'LHC.USER.ALL'}
