import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.cern.optics
import cern.lsa.domain.cern.optics.spi.ofb
import cern.lsa.domain.commons.spi
import java.io
import java.util
import typing



class FidelModelImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.cern.optics.FidelModel], cern.lsa.domain.cern.optics.FidelModel, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.optics.spi.FidelModelImpl'
    
        Extends:
            cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity
    
        Interfaces:
            cern.lsa.domain.cern.optics.FidelModel, java.io.Serializable
    
      Constructors:
        * FidelModelImpl(long, java.lang.String, java.lang.String)
    
    """
    def __init__(self, long: int, string: str, string2: str): ...
    def addComponent(self, string: str) -> None: ...
    def findModelCoefficients(self, string: str) -> java.util.Map[str, float]: ...
    def getCoeffMap(self) -> java.util.Map[str, java.util.Map[str, float]]: ...
    def getComponentsNames(self) -> java.util.Set[str]: ...
    def getModelId(self) -> int: ...
    def getModelName(self) -> str: ...
    def setCoeffMap(self, map: typing.Union[java.util.Map[str, typing.Union[java.util.Map[str, float], typing.Mapping[str, float]]], typing.Mapping[str, typing.Union[java.util.Map[str, float], typing.Mapping[str, float]]]]) -> None: ...

class FieldHarmonicImpl(cern.accsoft.commons.util.AbstractNamedSerializable, cern.lsa.domain.cern.optics.FieldHarmonic):
    """
    Java class 'cern.lsa.domain.cern.optics.spi.FieldHarmonicImpl'
    
        Extends:
            cern.accsoft.commons.util.AbstractNamedSerializable
    
        Interfaces:
            cern.lsa.domain.cern.optics.FieldHarmonic
    
      Constructors:
        * FieldHarmonicImpl(java.lang.String, java.util.Date, cern.accsoft.commons.value.ImmutableDiscreteFunction)
    
    """
    def __init__(self, string: str, date: java.util.Date, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction): ...
    def getComponentName(self) -> str: ...
    def getCreationDate(self) -> java.util.Date: ...
    def getCurrent2CnFunction(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction: ...
    def getModelName(self) -> str: ...
    def setComponentName(self, string: str) -> None: ...
    def setModelName(self, string: str) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.optics.spi")``.

    FidelModelImpl: typing.Type[FidelModelImpl]
    FieldHarmonicImpl: typing.Type[FieldHarmonicImpl]
    ofb: cern.lsa.domain.cern.optics.spi.ofb.__module_protocol__
