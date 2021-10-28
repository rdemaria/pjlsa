import java.lang.reflect
import java.util.concurrent
import typing



class MethodInvoker:
    """
    Java class 'cern.accsoft.commons.util.reflect.MethodInvoker'
    
    """
    def invoke(self, objectArray: typing.List[typing.Any], method: java.lang.reflect.Method, objectArray2: typing.List[typing.Any]) -> typing.List[typing.Any]: ...

class AbstractMethodInvoker(MethodInvoker):
    """
    Java class 'cern.accsoft.commons.util.reflect.AbstractMethodInvoker'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.reflect.MethodInvoker
    
      Constructors:
        * AbstractMethodInvoker()
    
    """
    def __init__(self): ...
    def invoke(self, objectArray: typing.List[typing.Any], method: java.lang.reflect.Method, objectArray2: typing.List[typing.Any]) -> typing.List[typing.Any]: ...

class ExecutorServiceMethodInvoker(AbstractMethodInvoker):
    """
    Java class 'cern.accsoft.commons.util.reflect.ExecutorServiceMethodInvoker'
    
        Extends:
            cern.accsoft.commons.util.reflect.AbstractMethodInvoker
    
      Constructors:
        * ExecutorServiceMethodInvoker()
        * ExecutorServiceMethodInvoker(java.util.concurrent.ExecutorService, long)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, executorService: java.util.concurrent.ExecutorService, long: int): ...
    def getExecutorService(self) -> java.util.concurrent.ExecutorService: ...
    def getMethodInvocationTimeout(self) -> int: ...

class SameThreadMethodInvoker(AbstractMethodInvoker):
    """
    Java class 'cern.accsoft.commons.util.reflect.SameThreadMethodInvoker'
    
        Extends:
            cern.accsoft.commons.util.reflect.AbstractMethodInvoker
    
      Constructors:
        * SameThreadMethodInvoker()
        * SameThreadMethodInvoker(boolean)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...

class SwingThreadMethodInvoker(AbstractMethodInvoker):
    """
    Java class 'cern.accsoft.commons.util.reflect.SwingThreadMethodInvoker'
    
        Extends:
            cern.accsoft.commons.util.reflect.AbstractMethodInvoker
    
      Constructors:
        * SwingThreadMethodInvoker()
    
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.reflect")``.

    AbstractMethodInvoker: typing.Type[AbstractMethodInvoker]
    ExecutorServiceMethodInvoker: typing.Type[ExecutorServiceMethodInvoker]
    MethodInvoker: typing.Type[MethodInvoker]
    SameThreadMethodInvoker: typing.Type[SameThreadMethodInvoker]
    SwingThreadMethodInvoker: typing.Type[SwingThreadMethodInvoker]
