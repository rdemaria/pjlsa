import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.commons
import java.io
import java.lang
import java.util
import typing



_AbstractIdentifiedEntity__I = typing.TypeVar('_AbstractIdentifiedEntity__I', bound=cern.lsa.domain.commons.IdentifiedEntity)  # <I>
class AbstractIdentifiedEntity(cern.lsa.domain.commons.IdentifiedEntity, java.io.Serializable, java.lang.Comparable[_AbstractIdentifiedEntity__I], typing.Generic[_AbstractIdentifiedEntity__I]):
    """
    public abstract class AbstractIdentifiedEntity<I extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.commons.IdentifiedEntity`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<I>
    
        An abstract implementation of the :class:`~cern.lsa.domain.commons.IdentifiedEntity` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def compareTo(self, i: _AbstractIdentifiedEntity__I) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Returns :code:`true` if the given object is of the same class and has the same ID.
        
            Overrides:
                 in class 
        
            Also see:
                :meth:`~cern.lsa.domain.commons.spi.AbstractIdentifiedEntity.getId`
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId` in interface :class:`~cern.lsa.domain.commons.IdentifiedEntity`
        
            Returns:
                identifier of this entity, any long number - positive, negative or 0
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Redefines equals in term of the name
        
            Overrides:
                 in class 
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#hashCode()>`
        
        
        """
        ...
    def setId(self, long: int) -> None:
        """
            Changes identifier of this object to the specified one.
        
            Parameters:
                id (long): new ID of this object
        
        
        """
        ...

_AbstractIdentifiedNamedEntity__E = typing.TypeVar('_AbstractIdentifiedNamedEntity__E', bound=cern.accsoft.commons.util.Named)  # <E>
class AbstractIdentifiedNamedEntity(cern.accsoft.commons.util.AbstractNamedSerializable[_AbstractIdentifiedNamedEntity__E], cern.lsa.domain.commons.IdentifiedEntity, typing.Generic[_AbstractIdentifiedNamedEntity__E]):
    """
    public abstract class AbstractIdentifiedNamedEntity<E extends cern.accsoft.commons.util.Named & :class:`~cern.lsa.domain.commons.IdentifiedEntity`> extends cern.accsoft.commons.util.AbstractNamedSerializable<E> implements :class:`~cern.lsa.domain.commons.IdentifiedEntity`
    
        An abstract implementation of :code:`Named` and :class:`~cern.lsa.domain.commons.IdentifiedEntity` interfaces.
    
        Also see:
            :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :code:`equals` in class :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId` in interface :class:`~cern.lsa.domain.commons.IdentifiedEntity`
        
            Returns:
                identifier of this entity, any long number - positive, negative or 0
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :code:`hashCode` in class :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`
        
        
        """
        ...
    def setId(self, long: int) -> None:
        """
        
            Parameters:
                id (long): new ID of this object
        
        
        """
        ...

_AbstractImmutableIdentifiedEntity__I = typing.TypeVar('_AbstractImmutableIdentifiedEntity__I', bound=cern.lsa.domain.commons.IdentifiedEntity)  # <I>
class AbstractImmutableIdentifiedEntity(cern.lsa.domain.commons.IdentifiedEntity, java.io.Serializable, java.lang.Comparable[_AbstractImmutableIdentifiedEntity__I], typing.Generic[_AbstractImmutableIdentifiedEntity__I]):
    """
    public abstract class AbstractImmutableIdentifiedEntity<I extends :class:`~cern.lsa.domain.commons.IdentifiedEntity`> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.commons.IdentifiedEntity`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<I>
    
        An abstract implementation of the :class:`~cern.lsa.domain.commons.IdentifiedEntity` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def compareTo(self, i: _AbstractImmutableIdentifiedEntity__I) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Returns :code:`true` if the given object is of the same class and has the same ID.
        
            Overrides:
                 in class 
        
            Also see:
                :meth:`~cern.lsa.domain.commons.spi.AbstractImmutableIdentifiedEntity.getId`
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId` in interface :class:`~cern.lsa.domain.commons.IdentifiedEntity`
        
            Returns:
                identifier of this entity, any long number - positive, negative or 0
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Redefines equals in term of the name
        
            Overrides:
                 in class 
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#hashCode()>`
        
        
        """
        ...

_AbstractImmutableIdentifiedNamedEntity__E = typing.TypeVar('_AbstractImmutableIdentifiedNamedEntity__E', bound=cern.accsoft.commons.util.Named)  # <E>
class AbstractImmutableIdentifiedNamedEntity(cern.accsoft.commons.util.AbstractImmutableNamedSerializable[_AbstractImmutableIdentifiedNamedEntity__E], cern.lsa.domain.commons.IdentifiedEntity, typing.Generic[_AbstractImmutableIdentifiedNamedEntity__E]):
    """
    public abstract class AbstractImmutableIdentifiedNamedEntity<E extends cern.accsoft.commons.util.Named & :class:`~cern.lsa.domain.commons.IdentifiedEntity`> extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<E> implements :class:`~cern.lsa.domain.commons.IdentifiedEntity`
    
        An abstract implementation of :code:`Named` and :class:`~cern.lsa.domain.commons.IdentifiedEntity` interfaces.
    
        Also see:
            :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :code:`equals` in class :class:`~cern.lsa.domain.commons.spi.AbstractImmutableIdentifiedNamedEntity`
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.IdentifiedEntity.getId` in interface :class:`~cern.lsa.domain.commons.IdentifiedEntity`
        
            Returns:
                identifier of this entity, any long number - positive, negative or 0
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :code:`hashCode` in class :class:`~cern.lsa.domain.commons.spi.AbstractImmutableIdentifiedNamedEntity`
        
        
        """
        ...

class AbstractPropertiesHolder(java.io.Serializable):
    """
    public abstract class AbstractPropertiesHolder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        General container for attributes.
    
        Also see:
            :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getProperties(self) -> java.util.Map[str, typing.Any]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class AttributeImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.commons.Attribute], cern.lsa.domain.commons.Attribute):
    """
    public class AttributeImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.commons.Attribute`> implements :class:`~cern.lsa.domain.commons.Attribute`
    
        Default implementation of the :class:`~cern.lsa.domain.commons.Attribute` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, attribute: cern.lsa.domain.commons.Attribute): ...
    @typing.overload
    def __init__(self, attributeDefinition: cern.lsa.domain.commons.AttributeDefinition, string: str): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :code:`equals` in class :class:`~cern.lsa.domain.commons.Attribute`
        
        
        """
        ...
    def getAttributeDefinition(self) -> cern.lsa.domain.commons.AttributeDefinition:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.Attribute.getAttributeDefinition`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.Attribute`
        
            Returns:
                definition of the associated attribute
        
        
        """
        ...
    def getBoolean(self) -> bool: ...
    def getDouble(self) -> float: ...
    def getInt(self) -> int: ...
    def getLong(self) -> int: ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Overrides:
                :code:`getName` in class :class:`~cern.lsa.domain.commons.Attribute`
        
        
        """
        ...
    def getValue(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.commons.Attribute.getValue`
            This method returns the value of this attribute as a String, which is the raw format stored in the DB
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.Attribute.getValue` in interface :class:`~cern.lsa.domain.commons.Attribute`
        
            Returns:
                value of the attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :code:`hashCode` in class :class:`~cern.lsa.domain.commons.Attribute`
        
        
        """
        ...
    @typing.overload
    def setValue(self, boolean: bool) -> None:
        """
        public void setValue (double newValue)
        
        public void setValue (long newValue)
        
        
        """
        ...
    @typing.overload
    def setValue(self, double: float) -> None: ...
    @typing.overload
    def setValue(self, int: int) -> None: ...
    @typing.overload
    def setValue(self, string: str) -> None: ...
    @typing.overload
    def setValue(self, long: int) -> None: ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.commons.Attribute`
        
        
        """
        ...

class AttributeDefinitionImpl(AbstractIdentifiedNamedEntity[cern.lsa.domain.commons.AttributeDefinition], cern.lsa.domain.commons.AttributeDefinition):
    """
    public class AttributeDefinitionImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity`<:class:`~cern.lsa.domain.commons.AttributeDefinition`> implements :class:`~cern.lsa.domain.commons.AttributeDefinition`
    
        Default implementation of the :class:`~cern.lsa.domain.commons.AttributeDefinition` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, attributeDefinition: cern.lsa.domain.commons.AttributeDefinition): ...
    @typing.overload
    def __init__(self, long: int, string: str, string2: str, string3: str, type: cern.accsoft.commons.value.Type, set: java.util.Set[str], string4: str): ...
    def getDefaultValue(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.commons.AttributeDefinition.getDefaultValue`
            Retrieves the default value of this attribute.
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeDefinition.getDefaultValue`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeDefinition`
        
            Returns:
                default value of the attribute or :code:`null`, if this attribute value needs to be set explicitly by an operator
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeDefinition.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeDefinition`
        
            Returns:
                attribute's description, :code:`null` if not specified
        
        
        """
        ...
    def getEnumValues(self) -> java.util.Set[str]: ...
    def getUnits(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeDefinition.getUnits`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeDefinition`
        
            Returns:
                units of the value, :code:`null` if not specified
        
        
        """
        ...
    def getValueType(self) -> cern.accsoft.commons.value.Type:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.commons.AttributeDefinition.getValueType`Â in
                interfaceÂ :class:`~cern.lsa.domain.commons.AttributeDefinition`
        
            Returns:
                attribute's value type
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.commons.AttributeDefinition`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons.spi")``.

    AbstractIdentifiedEntity: typing.Type[AbstractIdentifiedEntity]
    AbstractIdentifiedNamedEntity: typing.Type[AbstractIdentifiedNamedEntity]
    AbstractImmutableIdentifiedEntity: typing.Type[AbstractImmutableIdentifiedEntity]
    AbstractImmutableIdentifiedNamedEntity: typing.Type[AbstractImmutableIdentifiedNamedEntity]
    AbstractPropertiesHolder: typing.Type[AbstractPropertiesHolder]
    AttributeDefinitionImpl: typing.Type[AttributeDefinitionImpl]
    AttributeImpl: typing.Type[AttributeImpl]
