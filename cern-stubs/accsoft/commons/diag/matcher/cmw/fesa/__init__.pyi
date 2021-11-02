import cern.accsoft.commons.diag.matcher.cmw
import java.lang
import typing



class AbstractFesaStringThrowableMatcher(cern.accsoft.commons.diag.matcher.cmw.AbstractCmwFEStringThrowableMatcher):
    """
    public abstract class AbstractFesaStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.AbstractCmwFEStringThrowableMatcher`
    
        Base CMW IO FESA exception string-based matcher.
    """
    FESA_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` FESA_PROBLEM_DOMAIN
    
        FESA problem domain
    
        Also see:
            :meth:`~constant`
    
    
    """
    FESA_HINT_STRING: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` FESA_HINT_STRING
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def checkMatching(self, throwable: java.lang.Throwable) -> java.lang.Throwable:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher.checkMatching`Â in
                classÂ :class:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher`
        
        
        """
        ...

class FesaMuxWithAllStringThrowableMatcher(AbstractFesaStringThrowableMatcher):
    """
    public class FesaMuxWithAllStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher`
    """
    CMW_IO_FESA_MUX_WITH_ALL_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_IO_FESA_MUX_WITH_ALL_MATCHER_NAME
    
        CMW-FESA "mux property accessed with ALL selector" exception matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class FesaNoDataStringThrowableMatcher(AbstractFesaStringThrowableMatcher):
    """
    public class FesaNoDataStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher`
    """
    CMW_IO_FESA_NO_DATA_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_IO_FESA_NO_DATA_MATCHER_NAME
    
        CMW-FESA "no data" exception matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class FesaOutOfRangeStringThrowableMatcher(AbstractFesaStringThrowableMatcher):
    """
    public class FesaOutOfRangeStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher`
    """
    CMW_IO_FESA_OUT_OF_RANGE_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_IO_FESA_OUT_OF_RANGE_MATCHER_NAME
    
        CMW-FESA "class-specific" exception matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class FesaStringThrowableMatcher(AbstractFesaStringThrowableMatcher):
    """
    public class FesaStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher`
    """
    CMW_IO_FESA_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_IO_FESA_MATCHER_NAME
    
        CMW-FESA exception matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def checkMatching(self, throwable: java.lang.Throwable) -> java.lang.Throwable:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher.checkMatching`Â in
                classÂ :class:`~cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher.cmw.fesa")``.

    AbstractFesaStringThrowableMatcher: typing.Type[AbstractFesaStringThrowableMatcher]
    FesaMuxWithAllStringThrowableMatcher: typing.Type[FesaMuxWithAllStringThrowableMatcher]
    FesaNoDataStringThrowableMatcher: typing.Type[FesaNoDataStringThrowableMatcher]
    FesaOutOfRangeStringThrowableMatcher: typing.Type[FesaOutOfRangeStringThrowableMatcher]
    FesaStringThrowableMatcher: typing.Type[FesaStringThrowableMatcher]
