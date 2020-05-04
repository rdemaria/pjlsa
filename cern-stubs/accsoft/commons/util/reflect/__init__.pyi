from typing import Any as _py_Any
from typing import List as _py_List
from typing import overload
import java.lang.reflect
import java.util.concurrent


class MethodInvoker:
    def invoke(self, objectArray: _py_List[_py_Any], method: java.lang.reflect.Method, objectArray2: _py_List[_py_Any]) -> _py_List[_py_Any]: ...

class AbstractMethodInvoker(MethodInvoker):
    def __init__(self): ...
    def invoke(self, objectArray: _py_List[_py_Any], method: java.lang.reflect.Method, objectArray2: _py_List[_py_Any]) -> _py_List[_py_Any]: ...

class ExecutorServiceMethodInvoker(AbstractMethodInvoker):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, executorService: java.util.concurrent.ExecutorService, long: int): ...
    def getExecutorService(self) -> java.util.concurrent.ExecutorService: ...
    def getMethodInvocationTimeout(self) -> int: ...

class SameThreadMethodInvoker(AbstractMethodInvoker):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, boolean: bool): ...

class SwingThreadMethodInvoker(AbstractMethodInvoker):
    def __init__(self): ...
