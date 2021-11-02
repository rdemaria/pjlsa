import cern.lsa.domain.cern.settings.elena
import cern.lsa.domain.cern.settings.spi.elena
import java.time
import typing



class ElenaCycleUtils:
    """
    public final class ElenaCycleUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    TRIM_ATTR_OLD_ELENA_CYCLE_STRUCTURE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TRIM_ATTR_OLD_ELENA_CYCLE_STRUCTURE
    
        Name of a custom :code:`TrimRequest` attribute for the current ELENA cycle structure
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRIM_ATTR_NEW_ELENA_CYCLE_STRUCTURE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TRIM_ATTR_NEW_ELENA_CYCLE_STRUCTURE
    
        Name of a custom :code:`TrimRequest` attribute for the new ELENA cycle structure
    
        Also see:
            :meth:`~constant`
    
    
    """
    ELENA_FUNCTION_CORRECTIONS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ELENA_FUNCTION_CORRECTIONS
    
        Name of a custom :code:`TrimRequest` attribute for the function corrections
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    @staticmethod
    def convertToElenaCycleStructure(string: str) -> cern.lsa.domain.cern.settings.spi.elena.ElenaCycleStructureImpl: ...
    @staticmethod
    def convertToXml(elenaCycleStructure: cern.lsa.domain.cern.settings.elena.ElenaCycleStructure) -> str: ...
    @staticmethod
    def getRealSegmentLength(elenaCycleSegment: cern.lsa.domain.cern.settings.elena.ElenaCycleSegment) -> java.time.Duration:
        """
            For ramp segments, we have to calculate and return the real length that takes into account flat part section and
            rounding section. See specification of the ELENA cycle for details.
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.settings.util.elena")``.

    ElenaCycleUtils: typing.Type[ElenaCycleUtils]
