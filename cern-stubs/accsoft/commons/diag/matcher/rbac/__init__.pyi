import cern.accsoft.commons.diag.matcher
import typing



class AbstractRbacStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public abstract class AbstractRbacStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher`
    
        Base RBAC exception string-based matcher.
    """
    RBAC_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RBAC_PROBLEM_DOMAIN
    
        RBAC problem domain
    
        Also see:
            :meth:`~constant`
    
    
    """

class RbacCmw3SecurityExceptionStringThrowableMatcher(AbstractRbacStringThrowableMatcher):
    """
    public class RbacCmw3SecurityExceptionStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.rbac.AbstractRbacStringThrowableMatcher`
    """
    RBAC_CMW_SECURITY_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RBAC_CMW_SECURITY_MATCHER_NAME
    
        RBAC "exception coming from CMW" matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class RbacStringThrowableMatcher(AbstractRbacStringThrowableMatcher):
    """
    public class RbacStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.rbac.AbstractRbacStringThrowableMatcher`
    
        RBAC exception string-based matcher.
    """
    RBAC_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RBAC_MATCHER_NAME
    
        RBAC exception matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher.rbac")``.

    AbstractRbacStringThrowableMatcher: typing.Type[AbstractRbacStringThrowableMatcher]
    RbacCmw3SecurityExceptionStringThrowableMatcher: typing.Type[RbacCmw3SecurityExceptionStringThrowableMatcher]
    RbacStringThrowableMatcher: typing.Type[RbacStringThrowableMatcher]
