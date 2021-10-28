import cern.accsoft.commons.diag.matcher
import cern.accsoft.commons.diag.matcher.cmw.fesa
import java.lang
import typing



class AbstractCmwConfigStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.AbstractCmwConfigStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Attributes:
        CMW_CONFIG_DOMAIN (java.lang.String): final static field
        CMW_HINT_URL (java.lang.String): final static field
        CMW_CONTACT_URL (java.lang.String): final static field
    
    """
    CMW_CONFIG_DOMAIN: typing.ClassVar[str] = ...
    CMW_HINT_URL: typing.ClassVar[str] = ...
    CMW_CONTACT_URL: typing.ClassVar[str] = ...

class AbstractCmwFEStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.AbstractCmwFEStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Attributes:
        CMW_HW_PROBLEM_DOMAIN (java.lang.String): final static field
        CMW_HINT_STRING (java.lang.String): final static field
        CMW_HINT_URL (java.lang.String): final static field
        CMW_CONTACT_URL (java.lang.String): final static field
    
    """
    CMW_HW_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    CMW_HINT_STRING: typing.ClassVar[str] = ...
    CMW_HINT_URL: typing.ClassVar[str] = ...
    CMW_CONTACT_URL: typing.ClassVar[str] = ...

class AbstractCmwStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.AbstractCmwStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Attributes:
        CMW_PROBLEM_DOMAIN (java.lang.String): final static field
        CMW_HINT_URL (java.lang.String): final static field
        CMW_CONTACT_URL (java.lang.String): final static field
    
    """
    CMW_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    CMW_HINT_URL: typing.ClassVar[str] = ...
    CMW_CONTACT_URL: typing.ClassVar[str] = ...

class AbstractCmw3ServerExceptionStringThrowableMatcher(AbstractCmwFEStringThrowableMatcher): ...

class Cmw3InvalidArgumentStringThrowableMatcher(AbstractCmwConfigStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.Cmw3InvalidArgumentStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.AbstractCmwConfigStringThrowableMatcher
    
      Constructors:
        * Cmw3InvalidArgumentStringThrowableMatcher()
    
      Attributes:
        CMW_INVALID_ARGUMENT_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_INVALID_ARGUMENT_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class Cmw3NameServiceExceptionStringThrowableMatcher(AbstractCmwFEStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.Cmw3NameServiceExceptionStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.AbstractCmwFEStringThrowableMatcher
    
      Constructors:
        * Cmw3NameServiceExceptionStringThrowableMatcher()
    
      Attributes:
        CMW_NAME_SERVICE_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_NAME_SERVICE_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class Cmw3TransportExceptionStringThrowableMatcher(AbstractCmwFEStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.Cmw3TransportExceptionStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.AbstractCmwFEStringThrowableMatcher
    
      Constructors:
        * Cmw3TransportExceptionStringThrowableMatcher()
    
      Attributes:
        CMW_TRANSPORT_EXCEPTION_MATCHER_NAME (java.lang.String): final static field
        HINT_URL (java.lang.String): final static field
    
    """
    CMW_TRANSPORT_EXCEPTION_MATCHER_NAME: typing.ClassVar[str] = ...
    HINT_URL: typing.ClassVar[str] = ...
    def __init__(self): ...

class CmwNamingServerStringThrowableMatcher(AbstractCmwConfigStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.CmwNamingServerStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.AbstractCmwConfigStringThrowableMatcher
    
      Constructors:
        * CmwNamingServerStringThrowableMatcher()
    
      Attributes:
        CMW_NAMING_SERVE_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_NAMING_SERVE_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class CmwStringThrowableMatcher(AbstractCmwStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.CmwStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.AbstractCmwStringThrowableMatcher
    
      Constructors:
        * CmwStringThrowableMatcher()
    
      Attributes:
        CMW_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class Cmw3ServerExceptionStringThrowableMatcher(AbstractCmw3ServerExceptionStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.Cmw3ServerExceptionStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.AbstractCmw3ServerExceptionStringThrowableMatcher
    
      Constructors:
        * Cmw3ServerExceptionStringThrowableMatcher()
    
      Attributes:
        CMW_SERVER_EXCEPTION_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_SERVER_EXCEPTION_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...
    def checkMatching(self, throwable: java.lang.Throwable) -> java.lang.Throwable: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher.cmw")``.

    AbstractCmw3ServerExceptionStringThrowableMatcher: typing.Type[AbstractCmw3ServerExceptionStringThrowableMatcher]
    AbstractCmwConfigStringThrowableMatcher: typing.Type[AbstractCmwConfigStringThrowableMatcher]
    AbstractCmwFEStringThrowableMatcher: typing.Type[AbstractCmwFEStringThrowableMatcher]
    AbstractCmwStringThrowableMatcher: typing.Type[AbstractCmwStringThrowableMatcher]
    Cmw3InvalidArgumentStringThrowableMatcher: typing.Type[Cmw3InvalidArgumentStringThrowableMatcher]
    Cmw3NameServiceExceptionStringThrowableMatcher: typing.Type[Cmw3NameServiceExceptionStringThrowableMatcher]
    Cmw3ServerExceptionStringThrowableMatcher: typing.Type[Cmw3ServerExceptionStringThrowableMatcher]
    Cmw3TransportExceptionStringThrowableMatcher: typing.Type[Cmw3TransportExceptionStringThrowableMatcher]
    CmwNamingServerStringThrowableMatcher: typing.Type[CmwNamingServerStringThrowableMatcher]
    CmwStringThrowableMatcher: typing.Type[CmwStringThrowableMatcher]
    fesa: cern.accsoft.commons.diag.matcher.cmw.fesa.__module_protocol__
