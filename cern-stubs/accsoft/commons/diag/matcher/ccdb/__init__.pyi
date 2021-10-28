import cern.accsoft.commons.diag.matcher
import typing



class CcdbThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.ccdb.CcdbThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Constructors:
        * CcdbThrowableMatcher()
    
      Attributes:
        CCDB_PROBLEM_DOMAIN (java.lang.String): final static field
    
    """
    CCDB_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher.ccdb")``.

    CcdbThrowableMatcher: typing.Type[CcdbThrowableMatcher]
