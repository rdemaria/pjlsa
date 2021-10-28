import cern.accsoft.commons.diag.matcher
import typing



class AbstractRbacStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.rbac.AbstractRbacStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Attributes:
        RBAC_PROBLEM_DOMAIN (java.lang.String): final static field
    
    """
    RBAC_PROBLEM_DOMAIN: typing.ClassVar[str] = ...

class RbacCmw3SecurityExceptionStringThrowableMatcher(AbstractRbacStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.rbac.RbacCmw3SecurityExceptionStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.rbac.AbstractRbacStringThrowableMatcher
    
      Constructors:
        * RbacCmw3SecurityExceptionStringThrowableMatcher()
    
      Attributes:
        RBAC_CMW_SECURITY_MATCHER_NAME (java.lang.String): final static field
    
    """
    RBAC_CMW_SECURITY_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class RbacStringThrowableMatcher(AbstractRbacStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.rbac.RbacStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.rbac.AbstractRbacStringThrowableMatcher
    
      Constructors:
        * RbacStringThrowableMatcher()
    
      Attributes:
        RBAC_MATCHER_NAME (java.lang.String): final static field
    
    """
    RBAC_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher.rbac")``.

    AbstractRbacStringThrowableMatcher: typing.Type[AbstractRbacStringThrowableMatcher]
    RbacCmw3SecurityExceptionStringThrowableMatcher: typing.Type[RbacCmw3SecurityExceptionStringThrowableMatcher]
    RbacStringThrowableMatcher: typing.Type[RbacStringThrowableMatcher]
