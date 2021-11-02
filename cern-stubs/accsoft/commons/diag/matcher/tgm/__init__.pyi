import cern.accsoft.commons.diag.matcher
import typing



class TgmThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public class TgmThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher`
    
        TGM exception string-based matcher.
    """
    TGM_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TGM_PROBLEM_DOMAIN
    
        TGM problem domain
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher.tgm")``.

    TgmThrowableMatcher: typing.Type[TgmThrowableMatcher]
