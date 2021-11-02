import cern.accsoft.commons.diag.matcher
import typing



class CcdbThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public class CcdbThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher`
    
        CCDB exception string-based matcher.
    """
    CCDB_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CCDB_PROBLEM_DOMAIN
    
        CCDB problem domain
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher.ccdb")``.

    CcdbThrowableMatcher: typing.Type[CcdbThrowableMatcher]
