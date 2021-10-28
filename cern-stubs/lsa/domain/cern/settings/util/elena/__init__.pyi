import cern.lsa.domain.cern.settings.elena
import cern.lsa.domain.cern.settings.spi.elena
import java.time
import typing



class ElenaCycleUtils:
    """
    Java class 'cern.lsa.domain.cern.settings.util.elena.ElenaCycleUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ElenaCycleUtils()
    
      Attributes:
        TRIM_ATTR_OLD_ELENA_CYCLE_STRUCTURE (java.lang.String): final static field
        TRIM_ATTR_NEW_ELENA_CYCLE_STRUCTURE (java.lang.String): final static field
    
    """
    TRIM_ATTR_OLD_ELENA_CYCLE_STRUCTURE: typing.ClassVar[str] = ...
    TRIM_ATTR_NEW_ELENA_CYCLE_STRUCTURE: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def convertToElenaCycleStructure(string: str) -> cern.lsa.domain.cern.settings.spi.elena.ElenaCycleStructureImpl: ...
    @staticmethod
    def convertToXml(elenaCycleStructure: cern.lsa.domain.cern.settings.elena.ElenaCycleStructure) -> str: ...
    @staticmethod
    def getRealSegmentLength(elenaCycleSegment: cern.lsa.domain.cern.settings.elena.ElenaCycleSegment) -> java.time.Duration: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.settings.util.elena")``.

    ElenaCycleUtils: typing.Type[ElenaCycleUtils]
