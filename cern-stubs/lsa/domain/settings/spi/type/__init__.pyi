import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.particletransfers
import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.commons
import cern.lsa.domain.commons.spi
import cern.lsa.domain.settings.spi
import cern.lsa.domain.settings.type
import java.io
import java.lang
import java.util
import typing


class BeamProcessTypeSegmentAttributeDefinitionImpl(cern.lsa.domain.commons.spi.AttributeDefinitionImpl, cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition):
    @typing.overload
    def __init__(self, attributeDefinition: cern.lsa.domain.commons.AttributeDefinition, string: str, long: int): ...
    @typing.overload
    def __init__(self, beamProcessTypeSegmentAttributeDefinition: cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getSegmentId(self) -> int: ...
    def getSegmentName(self) -> str: ...
    def hashCode(self) -> int: ...
    def setSegmentName(self, string: str) -> None: ...

class BeamProcessTypeSegmentAttributeImpl(cern.lsa.domain.commons.spi.AttributeImpl, cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute):
    @typing.overload
    def __init__(self, beamProcessTypeSegmentAttribute: cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute): ...
    @typing.overload
    def __init__(self, beamProcessTypeSegmentAttributeDefinition: cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition, string: str, int: int): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAttributeDefinition(self) -> cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition: ...
    def getSegmentIndex(self) -> int: ...
    def hashCode(self) -> int: ...
    def setSegmentIndex(self, int: int) -> None: ...

class BeamProcessTypeSegmentsImpl(cern.lsa.domain.settings.type.BeamProcessTypeSegments, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, beamProcessTypeSegments: cern.lsa.domain.settings.type.BeamProcessTypeSegments): ...
    def addAttribute(self, beamProcessTypeSegmentAttribute: cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute) -> None: ...
    def getAttributeDoubleValue(self, int: int, string: str) -> float: ...
    def getAttributeDoubleValues(self, string: str) -> typing.List[float]: ...
    def getAttributeNames(self, int: int) -> java.util.Set[str]: ...
    def getAttributeStringValue(self, int: int, string: str) -> str: ...
    def getAttributes(self) -> java.util.List[cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute]: ...
    def getSegmentCount(self) -> int: ...
    def getSegmentName(self, int: int) -> str: ...
    def hasAttribute(self, int: int, string: str) -> bool: ...
    def setAttributes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute], typing.Sequence[cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute]]) -> None: ...
    def toString(self) -> str: ...

class ContextTypeImpl(cern.lsa.domain.settings.spi.ContextBase[cern.lsa.domain.settings.type.ContextType], cern.lsa.domain.settings.type.ContextType):
    @typing.overload
    def __init__(self, contextType: cern.lsa.domain.settings.type.ContextType): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...

class CycleTypeAttributeImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.settings.type.CycleTypeAttribute], cern.lsa.domain.settings.type.CycleTypeAttribute):
    @typing.overload
    def __init__(self, cycleTypeAttributeImpl: 'CycleTypeAttributeImpl'): ...
    @typing.overload
    def __init__(self, string: str, immutableScalar: cern.accsoft.commons.value.ImmutableScalar, string2: str): ...
    def getDescription(self) -> str: ...
    def getValue(self) -> cern.accsoft.commons.value.ImmutableScalar: ...
    @typing.overload
    def setValue(self, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None: ...
    @typing.overload
    def setValue(self, object: typing.Any) -> None: ...

class DefaultBeamProcessPurpose(cern.lsa.domain.settings.type.BeamProcessPurpose, java.io.Serializable):
    def __init__(self, string: str, boolean: bool): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def isDefault(self) -> bool: ...
    def toString(self) -> str: ...

class IncorporationRangeImpl(cern.lsa.domain.settings.type.IncorporationRange, java.io.Serializable, java.lang.Cloneable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, incorporationRange: cern.lsa.domain.settings.type.IncorporationRange): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, int: int, int2: int, string4: str, string5: str, string6: str, string7: str): ...
    def clone(self) -> 'IncorporationRangeImpl': ...
    def getBackwardIncorporationRule(self) -> str: ...
    def getBackwardIncorporationRuleParameter(self) -> str: ...
    def getBeamProcessTypeName(self) -> str: ...
    def getEndTime(self) -> int: ...
    def getForwardIncorporationRule(self) -> str: ...
    def getForwardIncorporationRuleParameter(self) -> str: ...
    def getParameterGroupName(self) -> str: ...
    def getParameterTypeName(self) -> str: ...
    def getStartTime(self) -> int: ...
    def setBackwardIncorporationRule(self, string: str) -> None: ...
    def setBackwardIncorporationRuleParameter(self, string: str) -> None: ...
    def setBeamProcessTypeName(self, string: str) -> None: ...
    def setEndTime(self, int: int) -> None: ...
    def setForwardIncorporationRule(self, string: str) -> None: ...
    def setForwardIncorporationRuleParameter(self, string: str) -> None: ...
    def setParameterGroupName(self, string: str) -> None: ...
    def setParameterTypeName(self, string: str) -> None: ...
    def setStartTime(self, int: int) -> None: ...
    def toString(self) -> str: ...

class IncorporationRuleDescriptorImpl(cern.lsa.domain.settings.type.IncorporationRuleDescriptor, java.io.Serializable):
    def __init__(self, string: str, boolean: bool): ...
    def getRuleName(self) -> str: ...
    def isParametrized(self) -> bool: ...

class TypeSchedulingItemImpl(cern.lsa.domain.settings.type.TypeSchedulingItem, java.io.Serializable):
    def equals(self, object: typing.Any) -> bool: ...
    def getScheduledType(self) -> cern.lsa.domain.settings.type.ContextType: ...
    def getStartTime(self) -> int: ...
    def hashCode(self) -> int: ...
    def setScheduledType(self, contextType: cern.lsa.domain.settings.type.ContextType) -> None: ...
    def setStartTime(self, int: int) -> None: ...
    def toString(self) -> str: ...

class BeamProcessTypeImpl(ContextTypeImpl, cern.lsa.domain.settings.type.BeamProcessType):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, beamProcessType: cern.lsa.domain.settings.type.BeamProcessType): ...
    @typing.overload
    def __init__(self, string: str): ...
    def getCategory(self) -> cern.lsa.domain.settings.type.BeamProcessTypeCategory: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...
    def getParticleType(self) -> cern.accsoft.commons.domain.ParticleType: ...
    def getPurpose(self) -> cern.lsa.domain.settings.type.BeamProcessPurpose: ...
    def getSegments(self) -> cern.lsa.domain.settings.type.BeamProcessTypeSegments: ...
    def getSegmentsImpl(self) -> BeamProcessTypeSegmentsImpl: ...
    def isExplicit(self) -> bool: ...
    def setCategory(self, beamProcessTypeCategory: cern.lsa.domain.settings.type.BeamProcessTypeCategory) -> None: ...
    def setExplicit(self, boolean: bool) -> None: ...
    def setParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> None: ...
    def setParticleType(self, particleType: cern.accsoft.commons.domain.ParticleType) -> None: ...
    def setPurpose(self, beamProcessPurpose: cern.lsa.domain.settings.type.BeamProcessPurpose) -> None: ...

class BeamProcessTypeScheduling(TypeSchedulingItemImpl):
    def __init__(self, int: int, contextType: cern.lsa.domain.settings.type.ContextType): ...

class TypeSchedulerImpl(ContextTypeImpl, cern.lsa.domain.settings.type.TypeScheduler):
    def addScheduling(self, typeSchedulingItem: cern.lsa.domain.settings.type.TypeSchedulingItem) -> None: ...
    def getSchedulings(self) -> java.util.List[cern.lsa.domain.settings.type.TypeSchedulingItem]: ...
    def setSchedulings(self, list: java.util.List[cern.lsa.domain.settings.type.TypeSchedulingItem]) -> None: ...

class CycleTypeImpl(TypeSchedulerImpl, cern.lsa.domain.settings.type.CycleType, cern.lsa.domain.commons.AttributeWritableAware):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, cycleTypeImpl: 'CycleTypeImpl'): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...
    def addAttribute(self, attribute: cern.lsa.domain.commons.Attribute) -> None: ...
    def getAttribute(self, string: str) -> cern.lsa.domain.commons.Attribute: ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getBeamProcessType(self, string: str) -> cern.lsa.domain.settings.type.BeamProcessType: ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def setAttributes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.Attribute], typing.Sequence[cern.lsa.domain.commons.Attribute]]) -> None: ...
