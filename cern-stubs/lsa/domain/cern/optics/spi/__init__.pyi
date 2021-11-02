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
    public class FidelModelImpl extends cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity<:class:`~cern.lsa.domain.cern.optics.FidelModel`> implements :class:`~cern.lsa.domain.cern.optics.FidelModel`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, long: int, string: str, string2: str): ...
    def addComponent(self, string: str) -> None: ...
    def findModelCoefficients(self, string: str) -> java.util.Map[str, float]: ...
    def getCoeffMap(self) -> java.util.Map[str, java.util.Map[str, float]]: ...
    def getComponentsNames(self) -> java.util.Set[str]: ...
    def getModelId(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.FidelModel.getModelId`
            Returns model ID
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.FidelModel.getModelId`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.FidelModel`
        
            Returns:
                model ID
        
        
        """
        ...
    def getModelName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.FidelModel.getModelName`
            Returns model name
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.FidelModel.getModelName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.FidelModel`
        
            Returns:
                model name; may not be null
        
        
        """
        ...
    def setCoeffMap(self, map: typing.Union[java.util.Map[str, typing.Union[java.util.Map[str, float], typing.Mapping[str, float]]], typing.Mapping[str, typing.Union[java.util.Map[str, float], typing.Mapping[str, float]]]]) -> None: ...

class FieldHarmonicImpl(cern.accsoft.commons.util.AbstractNamedSerializable, cern.lsa.domain.cern.optics.FieldHarmonic):
    """
    public class FieldHarmonicImpl extends cern.accsoft.commons.util.AbstractNamedSerializable implements :class:`~cern.lsa.domain.cern.optics.FieldHarmonic`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, date: java.util.Date, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction): ...
    def getComponentName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.FieldHarmonic.getComponentName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.FieldHarmonic`
        
            Returns:
        
        
        """
        ...
    def getCreationDate(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.FieldHarmonic.getCreationDate`
            Returns the creation date of this field harmonic.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.FieldHarmonic.getCreationDate`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.FieldHarmonic`
        
            Returns:
                the creation date of this field harmonic.
        
        
        """
        ...
    def getCurrent2CnFunction(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.optics.FieldHarmonic.getCurrent2CnFunction`
            Returns the function Cn(I) The returned function can be used to interpolate the value of the Cn for the given value of
            current
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.FieldHarmonic.getCurrent2CnFunction`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.FieldHarmonic`
        
            Returns:
                the function Cn(I)
        
        
        """
        ...
    def getModelName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.optics.FieldHarmonic.getModelName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.optics.FieldHarmonic`
        
            Returns:
        
        
        """
        ...
    def setComponentName(self, string: str) -> None: ...
    def setModelName(self, string: str) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.optics.spi")``.

    FidelModelImpl: typing.Type[FidelModelImpl]
    FieldHarmonicImpl: typing.Type[FieldHarmonicImpl]
    ofb: cern.lsa.domain.cern.optics.spi.ofb.__module_protocol__
