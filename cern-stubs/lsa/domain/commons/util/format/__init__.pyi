import java.util
import typing



class DefaultDateFormatter:
    """
    Java class 'cern.lsa.domain.commons.util.format.DefaultDateFormatter'
    
        Extends:
            java.lang.Object
    
      Attributes:
        FORMAT (java.lang.String): final static field
    
    """
    FORMAT: typing.ClassVar[str] = ...
    @staticmethod
    def format(date: java.util.Date) -> str: ...
    @staticmethod
    def parse(string: str) -> java.util.Date: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons.util.format")``.

    DefaultDateFormatter: typing.Type[DefaultDateFormatter]
