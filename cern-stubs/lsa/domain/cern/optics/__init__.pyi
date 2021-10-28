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
    Java class 'cern.lsa.domain.cern.optics.FidelModel'
    
        Interfaces:
            cern.accsoft.commons.util.Named,
            cern.lsa.domain.commons.IdentifiedEntity
    
    """
    def findModelCoefficients(self, string: str) -> java.util.Map[str, float]: ...
    def getComponentsNames(self) -> java.util.Set[str]: ...
    def getModelId(self) -> int: ...
    def getModelName(self) -> str: ...

class FieldHarmonic(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.lsa.domain.cern.optics.FieldHarmonic'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getComponentName(self) -> str: ...
    def getCreationDate(self) -> java.util.Date: ...
    def getCurrent2CnFunction(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction: ...
    def getModelName(self) -> str: ...
    def getName(self) -> str: ...

class MasterControllerTimingEvent(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.lsa.domain.cern.optics.MasterControllerTimingEvent'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getTimingParameterName(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.optics")``.

    FidelModel: typing.Type[FidelModel]
    FieldHarmonic: typing.Type[FieldHarmonic]
    MasterControllerTimingEvent: typing.Type[MasterControllerTimingEvent]
    factory: cern.lsa.domain.cern.optics.factory.__module_protocol__
    ofb: cern.lsa.domain.cern.optics.ofb.__module_protocol__
    spi: cern.lsa.domain.cern.optics.spi.__module_protocol__
