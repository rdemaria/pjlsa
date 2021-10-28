import cern.accsoft.commons.diag.matcher
import typing



class TgmThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.tgm.TgmThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Constructors:
        * TgmThrowableMatcher()
    
      Attributes:
        TGM_PROBLEM_DOMAIN (java.lang.String): final static field
    
    """
    TGM_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher.tgm")``.

    TgmThrowableMatcher: typing.Type[TgmThrowableMatcher]
