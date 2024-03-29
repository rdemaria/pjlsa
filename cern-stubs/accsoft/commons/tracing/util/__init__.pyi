from typing import Any as _py_Any
import cern.accsoft.commons.tracing.requests
import java.util


class ClientInfoUtils:
    def __init__(self): ...
    @classmethod
    def convertOfficialApplicationIdProperties(cls, string: str) -> java.util.Properties: ...
    @classmethod
    def getJSONRepresentation(cls, clientRequestInfo: cern.accsoft.commons.tracing.requests.ClientRequestInfo) -> str: ...
    @classmethod
    def getValidValue(cls, string: str, string2: str) -> str: ...

class JMXUtils:
    def __init__(self): ...
    @classmethod
    def registerMBean(cls, object: _py_Any, string: str, string2: str) -> None: ...
    @classmethod
    def unRegisterMBean(cls, string: str, string2: str) -> None: ...
