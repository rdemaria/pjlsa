import java.io
import java.lang
import org.slf4j
import typing



class InvocationIdHolder:
    """
    Java class 'cern.lsa.domain.commons.logging.InvocationIdHolder'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def getId() -> str: ...
    @staticmethod
    def setId(string: str) -> None: ...

class InvocationLogFactory:
    """
    Java class 'cern.lsa.domain.commons.logging.InvocationLogFactory'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * InvocationLogFactory()
    
    """
    def __init__(self): ...
    @staticmethod
    def getLogger() -> org.slf4j.Logger: ...

class LogMessage(java.io.Serializable):
    """
    Java class 'cern.lsa.domain.commons.logging.LogMessage'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * LogMessage(java.lang.String, int)
        * LogMessage(java.lang.String, java.lang.Throwable, int)
    
      Attributes:
        TRACE (int): final static field
        DEBUG (int): final static field
        INFO (int): final static field
        WARN (int): final static field
        ERROR (int): final static field
        FATAL (int): final static field
        IGNORED_EXCEPTION_PREFIX (java.lang.String): final static field
    
    """
    TRACE: typing.ClassVar[int] = ...
    DEBUG: typing.ClassVar[int] = ...
    INFO: typing.ClassVar[int] = ...
    WARN: typing.ClassVar[int] = ...
    ERROR: typing.ClassVar[int] = ...
    FATAL: typing.ClassVar[int] = ...
    IGNORED_EXCEPTION_PREFIX: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, string: str, int: int): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, int: int): ...
    def getDetails(self) -> java.lang.Throwable: ...
    def getLevel(self) -> int: ...
    def getMessage(self) -> str: ...
    def toString(self) -> str: ...

class ThreadLocalLogger:
    """
    Java class 'cern.lsa.domain.commons.logging.ThreadLocalLogger'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def clear() -> None: ...
    @typing.overload
    @staticmethod
    def debug(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def debug(string: str, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    @staticmethod
    def error(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def error(string: str, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    @staticmethod
    def fatal(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def fatal(string: str, throwable: java.lang.Throwable) -> None: ...
    @staticmethod
    def getLogMessages() -> typing.List[LogMessage]: ...
    @typing.overload
    @staticmethod
    def info(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def info(string: str, throwable: java.lang.Throwable) -> None: ...
    @staticmethod
    def log(logMessageArray: typing.List[LogMessage]) -> None: ...
    @typing.overload
    @staticmethod
    def trace(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def trace(string: str, throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    @staticmethod
    def warn(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def warn(string: str, throwable: java.lang.Throwable) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons.logging")``.

    InvocationIdHolder: typing.Type[InvocationIdHolder]
    InvocationLogFactory: typing.Type[InvocationLogFactory]
    LogMessage: typing.Type[LogMessage]
    ThreadLocalLogger: typing.Type[ThreadLocalLogger]
