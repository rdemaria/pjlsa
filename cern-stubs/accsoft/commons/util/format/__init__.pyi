import java.util.concurrent
import typing



class TimeFormat:
    """
    Java class 'cern.accsoft.commons.util.format.TimeFormat'
    
    """
    def format(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> str: ...

class DefaultTimeFormat(TimeFormat):
    """
    Java class 'cern.accsoft.commons.util.format.DefaultTimeFormat'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.format.TimeFormat
    
      Constructors:
        * DefaultTimeFormat()
    
      Attributes:
        PLACEHOLDER (java.lang.String): final static field
        NO_TIME (java.lang.String): final static field
    
    """
    PLACEHOLDER: typing.ClassVar[str] = ...
    NO_TIME: typing.ClassVar[str] = ...
    def __init__(self): ...
    def format(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> str: ...
    def getDayFormat(self) -> str: ...
    def getHourFormat(self) -> str: ...
    def getMicrosecFormat(self) -> str: ...
    def getMillisecFormat(self) -> str: ...
    def getMinFormat(self) -> str: ...
    def getNanosecFormat(self) -> str: ...
    def getSecFormat(self) -> str: ...
    def getSeparator(self) -> str: ...
    def isSkipZeroValues(self) -> bool: ...
    def setDayFormat(self, string: str) -> None: ...
    def setHourFormat(self, string: str) -> None: ...
    def setMicrosecFormat(self, string: str) -> None: ...
    def setMillisecFormat(self, string: str) -> None: ...
    def setMinFormat(self, string: str) -> None: ...
    def setNanosecFormat(self, string: str) -> None: ...
    def setSecFormat(self, string: str) -> None: ...
    def setSeparator(self, string: str) -> None: ...
    def setSkipZeroValues(self, boolean: bool) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.format")``.

    DefaultTimeFormat: typing.Type[DefaultTimeFormat]
    TimeFormat: typing.Type[TimeFormat]
