import cern.accsoft.commons.util.executor
import java.nio.charset
import java.util
import typing



class TraceIdContextForwarder(cern.accsoft.commons.util.executor.ContextForwarder):
    """
    Java class 'cern.accsoft.commons.util.traceid.TraceIdContextForwarder'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.executor.ContextForwarder
    
      Constructors:
        * TraceIdContextForwarder()
    
    """
    def __init__(self): ...
    def clearContext(self) -> None: ...
    def setContext(self) -> None: ...

class TraceIds:
    """
    Java class 'cern.accsoft.commons.util.traceid.TraceIds'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * TraceIds()
    
      Attributes:
        TRACE_ID (java.lang.String): final static field
        TRACE_ID_CONTEXT_DEFINITION (cern.accsoft.commons.util.executor.ContextDefinition): final static field
        TRACE_ID_EXECUTORS (cern.accsoft.commons.util.executor.ContextAwareExecutors): final static field
    
    """
    TRACE_ID: typing.ClassVar[str] = ...
    TRACE_ID_CONTEXT_DEFINITION: typing.ClassVar[cern.accsoft.commons.util.executor.ContextDefinition] = ...
    TRACE_ID_EXECUTORS: typing.ClassVar[cern.accsoft.commons.util.executor.ContextAwareExecutors] = ...
    def __init__(self): ...
    @staticmethod
    def clearTraceId() -> None: ...
    @staticmethod
    def generateUniqueId() -> str: ...
    @staticmethod
    def getTraceId() -> str: ...
    @staticmethod
    def setNewTraceId() -> str: ...
    @staticmethod
    def setNewTraceIdIfMissing() -> str: ...
    @staticmethod
    def setTraceId(string: str) -> None: ...

class UUIDs:
    """
    Java class 'cern.accsoft.commons.util.traceid.UUIDs'
    
        Extends:
            java.lang.Object
    
      Attributes:
        UTF_8 (java.nio.charset.Charset): final static field
    
    """
    UTF_8: typing.ClassVar[java.nio.charset.Charset] = ...
    @staticmethod
    def endOf(long: int) -> java.util.UUID: ...
    @staticmethod
    def random() -> java.util.UUID: ...
    @staticmethod
    def startOf(long: int) -> java.util.UUID: ...
    @staticmethod
    def timeBased() -> java.util.UUID: ...
    @staticmethod
    def unixTimestamp(uUID: java.util.UUID) -> int: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.traceid")``.

    TraceIdContextForwarder: typing.Type[TraceIdContextForwarder]
    TraceIds: typing.Type[TraceIds]
    UUIDs: typing.Type[UUIDs]
