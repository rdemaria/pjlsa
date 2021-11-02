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
    """
    public class BeamProcessTypeSegmentAttributeDefinitionImpl extends :class:`~cern.lsa.domain.commons.spi.AttributeDefinitionImpl` implements :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition`
    
        Default implementation of the :code:`BeamProcessTypeSegmentAttributeDefinition` interface
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, attributeDefinition: cern.lsa.domain.commons.AttributeDefinition, string: str, long: int): ...
    @typing.overload
    def __init__(self, beamProcessTypeSegmentAttributeDefinition: cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.equals`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def getSegmentId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition.getSegmentId`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition`
        
            Returns:
                returns the ID of the beam process type segment as stored in the DB
        
        
        """
        ...
    def getSegmentName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition.getSegmentName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition`
        
            Returns:
                Retrieves beam process type segment name this attribute definition is defined for
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity.hashCode`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def setSegmentName(self, string: str) -> None: ...

class BeamProcessTypeSegmentAttributeImpl(cern.lsa.domain.commons.spi.AttributeImpl, cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute):
    """
    public class BeamProcessTypeSegmentAttributeImpl extends :class:`~cern.lsa.domain.commons.spi.AttributeImpl` implements :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute` interface
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, beamProcessTypeSegmentAttribute: cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute): ...
    @typing.overload
    def __init__(self, beamProcessTypeSegmentAttributeDefinition: cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition, string: str, int: int): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AttributeImpl.equals` in class :class:`~cern.lsa.domain.commons.spi.AttributeImpl`
        
        
        """
        ...
    def getAttributeDefinition(self) -> cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttributeDefinition:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute.getAttributeDefinition`
            Gets extended attribute definition
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.Attribute.getAttributeDefinition`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.Attribute`
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute.getAttributeDefinition`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute`
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AttributeImpl.getAttributeDefinition`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AttributeImpl`
        
            Returns:
                definition of the associated attribute
        
        
        """
        ...
    def getSegmentIndex(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute.getSegmentIndex`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute`
        
            Returns:
                segment number in which this value is defined within a beam process type
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.lsa.domain.commons.spi.AttributeImpl.hashCode`Â in
                classÂ :class:`~cern.lsa.domain.commons.spi.AttributeImpl`
        
        
        """
        ...
    def setSegmentIndex(self, int: int) -> None: ...

class BeamProcessTypeSegmentsImpl(cern.lsa.domain.settings.type.BeamProcessTypeSegments, java.io.Serializable):
    """
    public class BeamProcessTypeSegmentsImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the :code:`BeamProcessTypeSegments` interface
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, beamProcessTypeSegments: cern.lsa.domain.settings.type.BeamProcessTypeSegments): ...
    def addAttribute(self, beamProcessTypeSegmentAttribute: cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute) -> None: ...
    def getAttributeDoubleValue(self, int: int, string: str) -> float:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.getAttributeDoubleValue`
            Returns the matching attribute value of this beam process type or NaN if no attribute of that name and index is found.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.getAttributeDoubleValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments`
        
            Parameters:
                segmentIndex (int): the index of the segment where to look for the attribute
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the attribute to return
        
            Returns:
                the matching attribute or null
        
        
        """
        ...
    def getAttributeDoubleValues(self, string: str) -> typing.List[float]:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.getAttributeDoubleValues`
            Returns the value of the matching attribute for all segments. If the attribute name if not defined for one or more
            segment(s), Double.NaN will be found in the resulting array. The resulting array is guaranted to be non null and of same
            size as the number of segments
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.getAttributeDoubleValues`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments`
        
            Parameters:
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the attribute to return
        
            Returns:
                the array of values for the attribute of given name for all segments
        
        
        """
        ...
    def getAttributeNames(self, int: int) -> java.util.Set[str]: ...
    def getAttributeStringValue(self, int: int, string: str) -> str:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.getAttributeStringValue`
            Returns the matching attribute value of this beam process type or null if no attribute of that name and index is found.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.getAttributeStringValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments`
        
            Parameters:
                segmentIndex (int): the index of the segment where to look for the attribute
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the attribute to return
        
            Returns:
                the matching attribute or null
        
        
        """
        ...
    def getAttributes(self) -> java.util.List[cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute]: ...
    def getSegmentCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.getSegmentCount`
            Returns the number of segment in that beam process type. A segment represents a period of time over the beam process
            type duration where parameters have the same value
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.getSegmentCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments`
        
            Returns:
                the number of segment in that beam process type
        
        
        """
        ...
    def getSegmentName(self, int: int) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.getSegmentName`
            Returns the name of the segment at index segmentIndex
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.getSegmentName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments`
        
            Parameters:
                segmentIndex (int): the index of the segment where to look for the attribute
        
            Returns:
                the name of the segment at index segmentIndex
        
        
        """
        ...
    def hasAttribute(self, int: int, string: str) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.hasAttribute`
            Returns true if the attribute of given name exists for the given segment
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments.hasAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessTypeSegments`
        
            Parameters:
                segmentIndex (int): the index of the segment where to look for the attribute
                attributeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the attribute to return
        
            Returns:
                true if the attribute of given name exists for the given segment
        
        
        """
        ...
    def setAttributes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute], typing.Sequence[cern.lsa.domain.settings.type.BeamProcessTypeSegmentAttribute]]) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ContextTypeImpl(cern.lsa.domain.settings.spi.ContextBase[cern.lsa.domain.settings.type.ContextType], cern.lsa.domain.settings.type.ContextType):
    """
    public abstract class ContextTypeImpl extends :class:`~cern.lsa.domain.settings.spi.ContextBase`<:class:`~cern.lsa.domain.settings.type.ContextType`> implements :class:`~cern.lsa.domain.settings.type.ContextType`
    
        Base class extended by all other context type implementations.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, contextType: cern.lsa.domain.settings.type.ContextType): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...

class CycleTypeAttributeImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.settings.type.CycleTypeAttribute], cern.lsa.domain.settings.type.CycleTypeAttribute):
    """
    public class CycleTypeAttributeImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.settings.type.CycleTypeAttribute`> implements :class:`~cern.lsa.domain.settings.type.CycleTypeAttribute`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.type.CycleTypeAttribute` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, cycleTypeAttributeImpl: 'CycleTypeAttributeImpl'): ...
    @typing.overload
    def __init__(self, string: str, immutableScalar: cern.accsoft.commons.value.ImmutableScalar, string2: str): ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.CycleTypeAttribute.getDescription`
            Returns optional description of the attribute.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.CycleTypeAttribute.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.CycleTypeAttribute`
        
            Returns:
                description
        
        
        """
        ...
    def getValue(self) -> cern.accsoft.commons.value.ImmutableScalar:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.CycleTypeAttribute.getValue`
            Returns value of the attribute.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.CycleTypeAttribute.getValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.CycleTypeAttribute`
        
            Returns:
                value of the attribute
        
        
        """
        ...
    @typing.overload
    def setValue(self, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None:
        """
        public void setValue (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` value)
        
        
        """
        ...
    @typing.overload
    def setValue(self, object: typing.Any) -> None: ...

class DefaultBeamProcessPurpose(cern.lsa.domain.settings.type.BeamProcessPurpose, java.io.Serializable):
    """
    public class DefaultBeamProcessPurpose extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.type.BeamProcessPurpose`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        A default POJO based implementation of BeamProcessPurpose
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, boolean: bool): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isDefault(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessPurpose.isDefault`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessPurpose`
        
            Returns:
                true if this :class:`~cern.lsa.domain.settings.type.BeamProcessPurpose` is default, false otherwise
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class IncorporationRangeImpl(cern.lsa.domain.settings.type.IncorporationRange, java.io.Serializable, java.lang.Cloneable):
    """
    public class IncorporationRangeImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.type.IncorporationRange`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, incorporationRange: cern.lsa.domain.settings.type.IncorporationRange): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, int: int, int2: int, string4: str, string5: str, string6: str, string7: str): ...
    def clone(self) -> 'IncorporationRangeImpl':
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.IncorporationRange.clone`
            Returns clone of this object.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.clone`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getBackwardIncorporationRule(self) -> str:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getBackwardIncorporationRule`
            Returns the name of the incorporation rule to apply in this incorporation range to incorporate a point in the function
            for the part of the function before the moved point.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getBackwardIncorporationRule`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Returns:
                the name of the incorporation rule to apply to incorporate the moved point before
        
        
        """
        ...
    def getBackwardIncorporationRuleParameter(self) -> str:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getBackwardIncorporationRuleParameter`
            Returns an optional parameter to the backward incorporation rule.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getBackwardIncorporationRuleParameter`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Returns:
                the optional parameter to the backward incorporation rule or null.
        
        
        """
        ...
    def getBeamProcessTypeName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getBeamProcessTypeName`
            Returns the beam process type name
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getBeamProcessTypeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Returns:
                the beam process type name
        
        
        """
        ...
    def getEndTime(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getEndTime`
            Returns the end time of this incorporation range in ms
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getEndTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Returns:
                the end time of this incorporation range in ms
        
        
        """
        ...
    def getForwardIncorporationRule(self) -> str:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getForwardIncorporationRule`
            Returns the name of the incorporation rule to apply in this incorporation range to incorporate a point in the function
            for the part of the function after the moved point.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getForwardIncorporationRule`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Returns:
                the name of the incorporation rule to apply to incorporate the moved point after
        
        
        """
        ...
    def getForwardIncorporationRuleParameter(self) -> str:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getForwardIncorporationRuleParameter`
            Returns an optional parameter to the forward incorporation rule.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getForwardIncorporationRuleParameter`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Returns:
                the optional parameter to the forward incorporation rule or null.
        
        
        """
        ...
    def getParameterGroupName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getParameterGroupName`
            Returns the parameter group name associated to this incorporation range. If it's null, it means this incorporation range
            isn't linked to a specific group.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getParameterGroupName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Returns:
        
        
        """
        ...
    def getParameterTypeName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getParameterTypeName`
            Returns parameter type name
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getParameterTypeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Returns:
                parameter type name
        
        
        """
        ...
    def getStartTime(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getStartTime`
            Returns the start time of this incorporation range in ms
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.getStartTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Returns:
                the start time of this incorporation range in ms
        
        
        """
        ...
    def setBackwardIncorporationRule(self, string: str) -> None:
        """
        
            Parameters:
                incorporationRuleIn (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The incorporationRuleIn to set.
        
        
        """
        ...
    def setBackwardIncorporationRuleParameter(self, string: str) -> None:
        """
        
            Parameters:
                incorporationRuleInParameter (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The incorporationRuleInParameter to set.
        
        
        """
        ...
    def setBeamProcessTypeName(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.IncorporationRange.setBeamProcessTypeName`
            Sets the beam process type name
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRange.setBeamProcessTypeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRange`
        
            Parameters:
                beamProcessTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The beamProcessTypeName to set.
        
        
        """
        ...
    def setEndTime(self, int: int) -> None:
        """
        
            Parameters:
                endTime (int): The endTime to set.
        
        
        """
        ...
    def setForwardIncorporationRule(self, string: str) -> None:
        """
        
            Parameters:
                incorporationRuleOut (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The incorporationRuleOut to set.
        
        
        """
        ...
    def setForwardIncorporationRuleParameter(self, string: str) -> None:
        """
        
            Parameters:
                incorporationRuleOutParameter (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The incorporationRuleOutParameter to set.
        
        
        """
        ...
    def setParameterGroupName(self, string: str) -> None:
        """
        
            Parameters:
                parameterGroupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the parameterGroupName to set
        
        
        """
        ...
    def setParameterTypeName(self, string: str) -> None:
        """
        
            Parameters:
                parameterTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The parameterTypeName to set.
        
        
        """
        ...
    def setStartTime(self, int: int) -> None:
        """
        
            Parameters:
                startTime (int): The startTime to set.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class IncorporationRuleDescriptorImpl(cern.lsa.domain.settings.type.IncorporationRuleDescriptor, java.io.Serializable):
    """
    public class IncorporationRuleDescriptorImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.type.IncorporationRuleDescriptor`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Implementation of the :class:`~cern.lsa.domain.settings.type.IncorporationRuleDescriptor`
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, boolean: bool): ...
    def getRuleName(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.IncorporationRuleDescriptor.getRuleName`
            Returns the name of the rule
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRuleDescriptor.getRuleName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRuleDescriptor`
        
            Returns:
                the name of the rule
        
        
        """
        ...
    def isParametrized(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.IncorporationRuleDescriptor.isParametrized`
            Returns true if rule has parameters
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.IncorporationRuleDescriptor.isParametrized`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.IncorporationRuleDescriptor`
        
            Returns:
                true if rule has parameters
        
        
        """
        ...

class TypeSchedulingItemImpl(cern.lsa.domain.settings.type.TypeSchedulingItem, java.io.Serializable):
    """
    public abstract class TypeSchedulingItemImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.type.TypeSchedulingItem`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Provides a way to schedule an entity identified by an id at a given time.
    
        Greg: This class should be made concrete and CycleTypeScheduling and BeamProcessTypeScheduling should be eradicated as
        they don't bring anything.
    
        Also see:
            :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getScheduledType(self) -> cern.lsa.domain.settings.type.ContextType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.TypeSchedulingItem.getScheduledType`
            Returns the scheduled type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.TypeSchedulingItem.getScheduledType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.TypeSchedulingItem`
        
            Returns:
                the scheduled type
        
        
        """
        ...
    def getStartTime(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.TypeSchedulingItem.getStartTime`
            Returns the start time for a scheduled type in the scheduling type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.TypeSchedulingItem.getStartTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.TypeSchedulingItem`
        
            Returns:
                the start time
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def setScheduledType(self, contextType: cern.lsa.domain.settings.type.ContextType) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.type.TypeSchedulingItemImpl.getScheduledType`
        
        
        """
        ...
    def setStartTime(self, int: int) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.type.TypeSchedulingItemImpl.getStartTime`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class BeamProcessTypeImpl(ContextTypeImpl, cern.lsa.domain.settings.type.BeamProcessType):
    """
    public class BeamProcessTypeImpl extends :class:`~cern.lsa.domain.settings.spi.type.ContextTypeImpl` implements :class:`~cern.lsa.domain.settings.type.BeamProcessType`
    
        Default implementation of the :class:`~cern.lsa.domain.settings.type.BeamProcessType` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, beamProcessType: cern.lsa.domain.settings.type.BeamProcessType): ...
    @typing.overload
    def __init__(self, string: str): ...
    def getCategory(self) -> cern.lsa.domain.settings.type.BeamProcessTypeCategory:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getCategory`
            Returns the non null category of this beam process type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getCategory`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessType`
        
            Returns:
                the non null category of this beam process type.
        
        
        """
        ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getParticleTransfer`
            Returns the name of the particle transfer this type is associated with
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getParticleTransfer`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessType`
        
            Returns:
                the name of the particle transfer this type is associated with
        
        
        """
        ...
    def getParticleType(self) -> cern.accsoft.commons.domain.ParticleType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getParticleType`
            Returns particle type associated with this beam process type.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getParticleType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessType`
        
            Returns:
                the particle type attached to this beam process type
        
        
        """
        ...
    def getPurpose(self) -> cern.lsa.domain.settings.type.BeamProcessPurpose:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getPurpose`
            Returns the beamProcess purpose, defining e.g. if it is a RAMP, FLATTOP, etc.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getPurpose`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessType`
        
            Returns:
                the beamProcess purpose
        
        
        """
        ...
    def getSegments(self) -> cern.lsa.domain.settings.type.BeamProcessTypeSegments:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getSegments`
            Returns the collection of segments defined for this beam process type
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessType.getSegments`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessType`
        
            Returns:
                the collection of segments defined for this beam process type
        
        
        """
        ...
    def getSegmentsImpl(self) -> BeamProcessTypeSegmentsImpl: ...
    def isExplicit(self) -> bool:
        """
            Returns true, if a BP type was created explicitly (default). Only certain system-generated beamout types will have
            explicitily == false Used by GSI.
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.BeamProcessType.isExplicit`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.BeamProcessType`
        
        
        """
        ...
    def setCategory(self, beamProcessTypeCategory: cern.lsa.domain.settings.type.BeamProcessTypeCategory) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.type.BeamProcessTypeImpl.getCategory`
        
        
        """
        ...
    def setExplicit(self, boolean: bool) -> None:
        """
            Set to true, if the BP was created explicitly. Set to true per default. However, within the generation, certain beamout
            BPs will be of a type with explicit == false, which means, the type will be actually created for them.
        
            Parameters:
                explicit (boolean): typically true
        
        
        """
        ...
    def setParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.type.BeamProcessTypeImpl.getParticleTransfer`
        
        
        """
        ...
    def setParticleType(self, particleType: cern.accsoft.commons.domain.ParticleType) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.type.BeamProcessTypeImpl.getParticleType`
        
        
        """
        ...
    def setPurpose(self, beamProcessPurpose: cern.lsa.domain.settings.type.BeamProcessPurpose) -> None:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.settings.spi.type.BeamProcessTypeImpl.getPurpose`
        
        
        """
        ...

class BeamProcessTypeScheduling(TypeSchedulingItemImpl):
    """
    public class BeamProcessTypeScheduling extends :class:`~cern.lsa.domain.settings.spi.type.TypeSchedulingItemImpl`
    
        A class to hold the scheduling of the different beam process types in a cycle.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, int: int, contextType: cern.lsa.domain.settings.type.ContextType): ...

class TypeSchedulerImpl(ContextTypeImpl, cern.lsa.domain.settings.type.TypeScheduler):
    """
    public abstract class TypeSchedulerImpl extends :class:`~cern.lsa.domain.settings.spi.type.ContextTypeImpl` implements :class:`~cern.lsa.domain.settings.type.TypeScheduler`
    
        This is the base type for classes wanting to schedule other classes of type BaseType.
    
        Also see:
            :meth:`~serialized`
    """
    def addScheduling(self, typeSchedulingItem: cern.lsa.domain.settings.type.TypeSchedulingItem) -> None:
        """
        
            Parameters:
                newScheduling (:class:`~cern.lsa.domain.settings.type.TypeSchedulingItem`): 
        
        """
        ...
    def getSchedulings(self) -> java.util.List[cern.lsa.domain.settings.type.TypeSchedulingItem]: ...
    def setSchedulings(self, list: java.util.List[cern.lsa.domain.settings.type.TypeSchedulingItem]) -> None: ...

class CycleTypeImpl(TypeSchedulerImpl, cern.lsa.domain.settings.type.CycleType, cern.lsa.domain.commons.AttributeWritableAware):
    """
    public class CycleTypeImpl extends :class:`~cern.lsa.domain.settings.spi.type.TypeSchedulerImpl` implements :class:`~cern.lsa.domain.settings.type.CycleType`, :class:`~cern.lsa.domain.commons.AttributeWritableAware`
    
        This implementation holds the information associated to a cycle. A cycle type holds beam process types that are
        scheduled with a given start time.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, cycleTypeImpl: 'CycleTypeImpl'): ...
    @typing.overload
    def __init__(self, long: int, string: str): ...
    def addAttribute(self, attribute: cern.lsa.domain.commons.Attribute) -> None:
        """
            Adds cycle type attribute to this cycle type.
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeWritableAware.addAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeWritableAware`
        
            Parameters:
                attribute (:class:`~cern.lsa.domain.commons.Attribute`): attribute
        
        
        """
        ...
    def getAttribute(self, string: str) -> cern.lsa.domain.commons.Attribute:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeAware.getAttribute`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeAware`
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the attribute
        
            Returns:
                Retrieves the attribute with the given name, or null if such attribute name is not bound to this object.
        
        
        """
        ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getBeamProcessType(self, string: str) -> cern.lsa.domain.settings.type.BeamProcessType:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.settings.type.CycleType.getBeamProcessType`
            Finds the beam process type of given name amongst those that are scheduled
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.type.CycleType.getBeamProcessType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.type.CycleType`
        
            Parameters:
                beamProcessTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the beam process type to find
        
            Returns:
                the beam process type of that name or null if none is found
        
        
        """
        ...
    def getParticleTransfers(self) -> java.util.Set[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def setAttributes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.Attribute], typing.Sequence[cern.lsa.domain.commons.Attribute]]) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings.spi.type")``.

    BeamProcessTypeImpl: typing.Type[BeamProcessTypeImpl]
    BeamProcessTypeScheduling: typing.Type[BeamProcessTypeScheduling]
    BeamProcessTypeSegmentAttributeDefinitionImpl: typing.Type[BeamProcessTypeSegmentAttributeDefinitionImpl]
    BeamProcessTypeSegmentAttributeImpl: typing.Type[BeamProcessTypeSegmentAttributeImpl]
    BeamProcessTypeSegmentsImpl: typing.Type[BeamProcessTypeSegmentsImpl]
    ContextTypeImpl: typing.Type[ContextTypeImpl]
    CycleTypeAttributeImpl: typing.Type[CycleTypeAttributeImpl]
    CycleTypeImpl: typing.Type[CycleTypeImpl]
    DefaultBeamProcessPurpose: typing.Type[DefaultBeamProcessPurpose]
    IncorporationRangeImpl: typing.Type[IncorporationRangeImpl]
    IncorporationRuleDescriptorImpl: typing.Type[IncorporationRuleDescriptorImpl]
    TypeSchedulerImpl: typing.Type[TypeSchedulerImpl]
    TypeSchedulingItemImpl: typing.Type[TypeSchedulingItemImpl]
