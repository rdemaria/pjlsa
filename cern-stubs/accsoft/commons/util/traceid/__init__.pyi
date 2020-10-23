from typing import ClassVar as _py_ClassVar
import cern.accsoft.commons.util.executor
import java.nio.charset
import java.util


class TraceIdContextForwarder(cern.accsoft.commons.util.executor.ContextForwarder):
    def __init__(self): ...
    def clearContext(self) -> None: ...
    def setContext(self) -> None: ...

class TraceIds:
    TRACE_ID: _py_ClassVar[str] = ...
    TRACE_ID_CONTEXT_DEFINITION: _py_ClassVar[cern.accsoft.commons.util.executor.ContextDefinition] = ...
    TRACE_ID_EXECUTORS: _py_ClassVar[cern.accsoft.commons.util.executor.ContextAwareExecutors] = ...
    def __init__(self): ...
    @classmethod
    def clearTraceId(cls) -> None: ...
    @classmethod
    def generateUniqueId(cls) -> str: ...
    @classmethod
    def getTraceId(cls) -> str: ...
    @classmethod
    def setNewTraceId(cls) -> str: ...
    @classmethod
    def setNewTraceIdIfMissing(cls) -> str: ...
    @classmethod
    def setTraceId(cls, string: str) -> None: ...

class UUIDs:
    UTF_8: _py_ClassVar[java.nio.charset.Charset] = ...
    @classmethod
    def endOf(cls, long: int) -> java.util.UUID: ...
    @classmethod
    def random(cls) -> java.util.UUID: ...
    @classmethod
    def startOf(cls, long: int) -> java.util.UUID: ...
    @classmethod
    def timeBased(cls) -> java.util.UUID: ...
    @classmethod
    def unixTimestamp(cls, uUID: java.util.UUID) -> int: ...