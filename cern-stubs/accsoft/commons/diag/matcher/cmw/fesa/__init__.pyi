import cern.accsoft.commons.diag.matcher.cmw
import java.lang
import typing



class AbstractFesaStringThrowableMatcher(cern.accsoft.commons.diag.matcher.cmw.AbstractCmwFEStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.AbstractCmwFEStringThrowableMatcher
    
      Attributes:
        FESA_PROBLEM_DOMAIN (java.lang.String): final static field
        FESA_HINT_STRING (java.lang.String): final static field
    
    """
    FESA_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    FESA_HINT_STRING: typing.ClassVar[str] = ...
    def checkMatching(self, throwable: java.lang.Throwable) -> java.lang.Throwable: ...

class FesaMuxWithAllStringThrowableMatcher(AbstractFesaStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.fesa.FesaMuxWithAllStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher
    
      Constructors:
        * FesaMuxWithAllStringThrowableMatcher()
    
      Attributes:
        CMW_IO_FESA_MUX_WITH_ALL_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_IO_FESA_MUX_WITH_ALL_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class FesaNoDataStringThrowableMatcher(AbstractFesaStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.fesa.FesaNoDataStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher
    
      Constructors:
        * FesaNoDataStringThrowableMatcher()
    
      Attributes:
        CMW_IO_FESA_NO_DATA_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_IO_FESA_NO_DATA_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class FesaOutOfRangeStringThrowableMatcher(AbstractFesaStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.fesa.FesaOutOfRangeStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher
    
      Constructors:
        * FesaOutOfRangeStringThrowableMatcher()
    
      Attributes:
        CMW_IO_FESA_OUT_OF_RANGE_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_IO_FESA_OUT_OF_RANGE_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class FesaStringThrowableMatcher(AbstractFesaStringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.cmw.fesa.FesaStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.cmw.fesa.AbstractFesaStringThrowableMatcher
    
      Constructors:
        * FesaStringThrowableMatcher()
    
      Attributes:
        CMW_IO_FESA_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_IO_FESA_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...
    def checkMatching(self, throwable: java.lang.Throwable) -> java.lang.Throwable: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher.cmw.fesa")``.

    AbstractFesaStringThrowableMatcher: typing.Type[AbstractFesaStringThrowableMatcher]
    FesaMuxWithAllStringThrowableMatcher: typing.Type[FesaMuxWithAllStringThrowableMatcher]
    FesaNoDataStringThrowableMatcher: typing.Type[FesaNoDataStringThrowableMatcher]
    FesaOutOfRangeStringThrowableMatcher: typing.Type[FesaOutOfRangeStringThrowableMatcher]
    FesaStringThrowableMatcher: typing.Type[FesaStringThrowableMatcher]
