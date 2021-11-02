import cern.accsoft.commons.diag.matcher
import cern.accsoft.commons.diag.matcher.cmw.fesa
import java.lang
import typing



class AbstractCmwConfigStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public abstract class AbstractCmwConfigStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher`
    
        Base CMW exception string-based matcher.
    """
    CMW_CONFIG_DOMAIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_CONFIG_DOMAIN
    
        CMW problem domain
    
        Also see:
            :meth:`~constant`
    
    
    """
    CMW_HINT_URL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_HINT_URL
    
        CMW hint URL
    
        Also see:
            :meth:`~constant`
    
    
    """
    CMW_CONTACT_URL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_CONTACT_URL
    
        CMW contact URL
    
        Also see:
            :meth:`~constant`
    
    
    """

class AbstractCmwFEStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public abstract class AbstractCmwFEStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher`
    
        Base CMW exception string-based matcher.
    """
    CMW_HW_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_HW_PROBLEM_DOMAIN
    
        CMW problem domain
    
        Also see:
            :meth:`~constant`
    
    
    """
    CMW_HINT_STRING: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_HINT_STRING
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    CMW_HINT_URL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_HINT_URL
    
        CMW hint URL
    
        Also see:
            :meth:`~constant`
    
    
    """
    CMW_CONTACT_URL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_CONTACT_URL
    
        CMW contact URL
    
        Also see:
            :meth:`~constant`
    
    
    """

class AbstractCmwStringThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public abstract class AbstractCmwStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher`
    
        Base CMW exception string-based matcher.
    """
    CMW_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_PROBLEM_DOMAIN
    
        CMW problem domain
    
        Also see:
            :meth:`~constant`
    
    
    """
    CMW_HINT_URL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_HINT_URL
    
        CMW hint URL
    
        Also see:
            :meth:`~constant`
    
    
    """
    CMW_CONTACT_URL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_CONTACT_URL
    
        CMW contact URL
    
        Also see:
            :meth:`~constant`
    
    
    """

class AbstractCmw3ServerExceptionStringThrowableMatcher(AbstractCmwFEStringThrowableMatcher):
    """
    public abstract class AbstractCmw3ServerExceptionStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.AbstractCmwFEStringThrowableMatcher`
    
        Base CMW IO exception string-based matcher.
    """
    ...

class Cmw3InvalidArgumentStringThrowableMatcher(AbstractCmwConfigStringThrowableMatcher):
    """
    public class Cmw3InvalidArgumentStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.AbstractCmwConfigStringThrowableMatcher`
    """
    CMW_INVALID_ARGUMENT_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_INVALID_ARGUMENT_MATCHER_NAME
    
        CMW BadParameter matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class Cmw3NameServiceExceptionStringThrowableMatcher(AbstractCmwFEStringThrowableMatcher):
    """
    public class Cmw3NameServiceExceptionStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.AbstractCmwFEStringThrowableMatcher`
    """
    CMW_NAME_SERVICE_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_NAME_SERVICE_MATCHER_NAME
    
        CMW BadParameter matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class Cmw3TransportExceptionStringThrowableMatcher(AbstractCmwFEStringThrowableMatcher):
    """
    public class Cmw3TransportExceptionStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.AbstractCmwFEStringThrowableMatcher`
    """
    CMW_TRANSPORT_EXCEPTION_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_TRANSPORT_EXCEPTION_MATCHER_NAME
    
        CMW TransportException matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    HINT_URL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` HINT_URL
    
        CMW hint URL
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class CmwNamingServerStringThrowableMatcher(AbstractCmwConfigStringThrowableMatcher):
    """
    public class CmwNamingServerStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.AbstractCmwConfigStringThrowableMatcher`
    """
    CMW_NAMING_SERVE_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_NAMING_SERVE_MATCHER_NAME
    
        CMW BadParameter matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class CmwStringThrowableMatcher(AbstractCmwStringThrowableMatcher):
    """
    public class CmwStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.AbstractCmwStringThrowableMatcher`
    
        CMW exception general string-based matcher.
    """
    CMW_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_MATCHER_NAME
    
        CMW exception matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class Cmw3ServerExceptionStringThrowableMatcher(AbstractCmw3ServerExceptionStringThrowableMatcher):
    """
    public class Cmw3ServerExceptionStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.AbstractCmw3ServerExceptionStringThrowableMatcher`
    
        CMW IO exception general string-based matcher.
    """
    CMW_SERVER_EXCEPTION_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_SERVER_EXCEPTION_MATCHER_NAME
    
        CMW IO error matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def checkMatching(self, throwable: java.lang.Throwable) -> java.lang.Throwable:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher.checkMatching`Â in
                classÂ :class:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher`
        
        
        """
        ...


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
