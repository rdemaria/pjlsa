import java.io
import java.lang
import org.slf4j
import typing



class InvocationIdHolder:
    """
    public class InvocationIdHolder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Holder which keeps current invocation ID.
    """
    @staticmethod
    def getId() -> str:
        """
            Returns invocation ID. If there is no value for the id, it generates a new one.
        
            Returns:
                invocation id
        
        
        """
        ...
    @staticmethod
    def setId(string: str) -> None:
        """
            Sets user defined invocation id.
        
            Parameters:
                id (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): user defined id
        
        
        """
        ...

class InvocationLogFactory:
    """
    public class InvocationLogFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory which returns current invocation log (to publish info for clients)
    """
    def __init__(self): ...
    @staticmethod
    def getLogger() -> org.slf4j.Logger:
        """
            Returns current invocation logger.
        
            Returns:
                current invocation logger
        
        
        """
        ...

class LogMessage(java.io.Serializable):
    """
    public class LogMessage extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        A bean used to store a single log message.
    
        Also see:
            :class:`~cern.lsa.domain.commons.logging.ThreadLocalLogger`, :meth:`~serialized`
    """
    TRACE: typing.ClassVar[int] = ...
    """
    public static final int TRACE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEBUG: typing.ClassVar[int] = ...
    """
    public static final int DEBUG
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    INFO: typing.ClassVar[int] = ...
    """
    public static final int INFO
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    WARN: typing.ClassVar[int] = ...
    """
    public static final int WARN
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ERROR: typing.ClassVar[int] = ...
    """
    public static final int ERROR
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    FATAL: typing.ClassVar[int] = ...
    """
    public static final int FATAL
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    IGNORED_EXCEPTION_PREFIX: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` IGNORED_EXCEPTION_PREFIX
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str, int: int): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable, int: int): ...
    def getDetails(self) -> java.lang.Throwable:
        """
            Returns :code:`details`.
        
            Returns:
                the :code:`details`
        
        
        """
        ...
    def getLevel(self) -> int:
        """
            Returns :code:`level`.
        
            Returns:
                the :code:`level`
        
        
        """
        ...
    def getMessage(self) -> str:
        """
            Returns :code:`message`.
        
            Returns:
                the :code:`message`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ThreadLocalLogger:
    """
    public final class ThreadLocalLogger extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Logger class which can be used to log and keep messages for the current thread. Messages are not redirected anywhere but
        only kept in a thread local variable. In order to display messages logged using this logger it is necessary to retrieve
        messages using :meth:`~cern.lsa.domain.commons.logging.ThreadLocalLogger.getLogMessages` method.
    
        This class is foreseen mainly to gather log messages on the server side and display them in client applications.
    """
    @staticmethod
    def clear() -> None:
        """
            Removes all messages logged in the current thread.
        
        """
        ...
    @typing.overload
    @staticmethod
    def debug(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def debug(string: str, throwable: java.lang.Throwable) -> None:
        """
        public static void debug (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` msg)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def error(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def error(string: str, throwable: java.lang.Throwable) -> None:
        """
        public static void error (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` msg)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def fatal(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def fatal(string: str, throwable: java.lang.Throwable) -> None:
        """
        public static void fatal (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` msg)
        
        
        """
        ...
    @staticmethod
    def getLogMessages() -> typing.List[LogMessage]:
        """
            Returns all messages logged so far in the current thread.
        
            Returns:
                a non-null array of messages
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def info(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def info(string: str, throwable: java.lang.Throwable) -> None:
        """
        public static void info (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` msg)
        
        
        """
        ...
    @staticmethod
    def log(logMessageArray: typing.List[LogMessage]) -> None:
        """
            Appends specified Logs to the current list of messages (of the current thread).
        
        """
        ...
    @typing.overload
    @staticmethod
    def trace(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def trace(string: str, throwable: java.lang.Throwable) -> None:
        """
        public static void trace (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` msg)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def warn(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def warn(string: str, throwable: java.lang.Throwable) -> None:
        """
        public static void warn (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` msg)
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons.logging")``.

    InvocationIdHolder: typing.Type[InvocationIdHolder]
    InvocationLogFactory: typing.Type[InvocationLogFactory]
    LogMessage: typing.Type[LogMessage]
    ThreadLocalLogger: typing.Type[ThreadLocalLogger]
