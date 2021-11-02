import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.cern.optics.factory
import cern.lsa.domain.cern.optics.ofb
import cern.lsa.domain.cern.optics.spi
import cern.lsa.domain.commons
import java.util
import typing



class FidelModel(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity):
    """
    public interface FidelModel extends cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity
    
        Represents a LHC FIDEL model.
    """
    def findModelCoefficients(self, string: str) -> java.util.Map[str, float]: ...
    def getComponentsNames(self) -> java.util.Set[str]: ...
    def getModelId(self) -> int:
        """
            Returns model ID
        
            Returns:
                model ID
        
        
        """
        ...
    def getModelName(self) -> str:
        """
            Returns model name
        
            Returns:
                model name; may not be null
        
        
        """
        ...

class FieldHarmonic(cern.accsoft.commons.util.Named):
    """
    public interface FieldHarmonic extends cern.accsoft.commons.util.Named
    """
    def getComponentName(self) -> str:
        """
        
            Returns:
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Returns the creation date of this field harmonic.
        
            Returns:
                the creation date of this field harmonic.
        
        
        """
        ...
    def getCurrent2CnFunction(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Returns the function Cn(I) The returned function can be used to interpolate the value of the Cn for the given value of
            current
        
            Returns:
                the function Cn(I)
        
        
        """
        ...
    def getModelName(self) -> str:
        """
        
            Returns:
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns the name of this field harmonic.
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                the name of this field harmonic.
        
        
        """
        ...

class MasterControllerTimingEvent(cern.accsoft.commons.util.Named):
    """
    public interface MasterControllerTimingEvent extends cern.accsoft.commons.util.Named
    
        Represents Master Controller timing events. In PS and PSB this corresponds to CTIMA devices. Each event has it's name
        (label) and corresponding LSA parameter name that contains time (within the cycle) when the event is fired.
    
        At the moment 5 different events are supported (the list may be different from accelerator to accelerator):
    
          - Inj-1 - first injection
          - Inj-2 - second injection
          - Trans - transition
          - Ej-1 - first ejection
          - Ej-2 - second ejection
    
        The principle use of this class are trims on the OPTICS/OpticsFunction parameters that define optics function as
        setting. See OpticsMakeRule JavaDoc for details.
    """
    def getTimingParameterName(self) -> str:
        """
            Returns name of the corresponding timing parameter (as defined in LSA database).
        
            Returns:
                name of the timing parameter e.g. PIX.MC-CTM/CCV#value
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.optics")``.

    FidelModel: typing.Type[FidelModel]
    FieldHarmonic: typing.Type[FieldHarmonic]
    MasterControllerTimingEvent: typing.Type[MasterControllerTimingEvent]
    factory: cern.lsa.domain.cern.optics.factory.__module_protocol__
    ofb: cern.lsa.domain.cern.optics.ofb.__module_protocol__
    spi: cern.lsa.domain.cern.optics.spi.__module_protocol__
