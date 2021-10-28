import java.lang
import java.util.concurrent
import typing



class DefaultThreadFactory(java.util.concurrent.ThreadFactory):
    """
    Java class 'cern.accsoft.commons.util.concurrent.DefaultThreadFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.util.concurrent.ThreadFactory
    
      Constructors:
        * DefaultThreadFactory(java.lang.String)
        * DefaultThreadFactory(java.lang.String, boolean)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, boolean: bool): ...
    def newThread(self, runnable: typing.Union[java.lang.Runnable, typing.Callable]) -> java.lang.Thread: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.concurrent")``.

    DefaultThreadFactory: typing.Type[DefaultThreadFactory]
