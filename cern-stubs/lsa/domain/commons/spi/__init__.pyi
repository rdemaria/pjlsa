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
    Java class 'cern.lsa.domain.commons.spi.AbstractIdentifiedEntity'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.commons.IdentifiedEntity,
            java.io.Serializable, java.lang.Comparable
    
    """
    def compareTo(self, i: _AbstractIdentifiedEntity__I) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getId(self) -> int: ...
    def hashCode(self) -> int: ...
    def setId(self, long: int) -> None: ...

_AbstractIdentifiedNamedEntity__E = typing.TypeVar('_AbstractIdentifiedNamedEntity__E', bound=cern.accsoft.commons.util.Named)  # <E>
class AbstractIdentifiedNamedEntity(cern.accsoft.commons.util.AbstractNamedSerializable[_AbstractIdentifiedNamedEntity__E], cern.lsa.domain.commons.IdentifiedEntity, typing.Generic[_AbstractIdentifiedNamedEntity__E]):
    """
    Java class 'cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity'
    
        Extends:
            cern.accsoft.commons.util.AbstractNamedSerializable
    
        Interfaces:
            cern.lsa.domain.commons.IdentifiedEntity
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getId(self) -> int: ...
    def hashCode(self) -> int: ...
    def setId(self, long: int) -> None: ...

_AbstractImmutableIdentifiedEntity__I = typing.TypeVar('_AbstractImmutableIdentifiedEntity__I', bound=cern.lsa.domain.commons.IdentifiedEntity)  # <I>
class AbstractImmutableIdentifiedEntity(cern.lsa.domain.commons.IdentifiedEntity, java.io.Serializable, java.lang.Comparable[_AbstractImmutableIdentifiedEntity__I], typing.Generic[_AbstractImmutableIdentifiedEntity__I]):
    """
    Java class 'cern.lsa.domain.commons.spi.AbstractImmutableIdentifiedEntity'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.commons.IdentifiedEntity,
            java.io.Serializable, java.lang.Comparable
    
    """
    def compareTo(self, i: _AbstractImmutableIdentifiedEntity__I) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getId(self) -> int: ...
    def hashCode(self) -> int: ...

_AbstractImmutableIdentifiedNamedEntity__E = typing.TypeVar('_AbstractImmutableIdentifiedNamedEntity__E', bound=cern.accsoft.commons.util.Named)  # <E>
class AbstractImmutableIdentifiedNamedEntity(cern.accsoft.commons.util.AbstractImmutableNamedSerializable[_AbstractImmutableIdentifiedNamedEntity__E], cern.lsa.domain.commons.IdentifiedEntity, typing.Generic[_AbstractImmutableIdentifiedNamedEntity__E]):
    """
    Java class 'cern.lsa.domain.commons.spi.AbstractImmutableIdentifiedNamedEntity'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
        Interfaces:
            cern.lsa.domain.commons.IdentifiedEntity
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getId(self) -> int: ...
    def hashCode(self) -> int: ...

class AbstractPropertiesHolder(java.io.Serializable):
    """
    Java class 'cern.lsa.domain.commons.spi.AbstractPropertiesHolder'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getProperties(self) -> java.util.Map[str, typing.Any]: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class AttributeImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.commons.Attribute], cern.lsa.domain.commons.Attribute):
    """
    Java class 'cern.lsa.domain.commons.spi.AttributeImpl'
    
        Extends:
            cern.accsoft.commons.util.AbstractNamedSerializable
    
        Interfaces:
            cern.lsa.domain.commons.Attribute
    
      Constructors:
        * AttributeImpl(cern.lsa.domain.commons.Attribute)
        * AttributeImpl(cern.lsa.domain.commons.AttributeDefinition, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, attribute: cern.lsa.domain.commons.Attribute): ...
    @typing.overload
    def __init__(self, attributeDefinition: cern.lsa.domain.commons.AttributeDefinition, string: str): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAttributeDefinition(self) -> cern.lsa.domain.commons.AttributeDefinition: ...
    def getBoolean(self) -> bool: ...
    def getDouble(self) -> float: ...
    def getInt(self) -> int: ...
    def getLong(self) -> int: ...
    def getName(self) -> str: ...
    def getValue(self) -> str: ...
    def hashCode(self) -> int: ...
    @typing.overload
    def setValue(self, boolean: bool) -> None: ...
    @typing.overload
    def setValue(self, double: float) -> None: ...
    @typing.overload
    def setValue(self, int: int) -> None: ...
    @typing.overload
    def setValue(self, string: str) -> None: ...
    @typing.overload
    def setValue(self, long: int) -> None: ...
    def toString(self) -> str: ...

class AttributeDefinitionImpl(AbstractIdentifiedNamedEntity[cern.lsa.domain.commons.AttributeDefinition], cern.lsa.domain.commons.AttributeDefinition):
    """
    Java class 'cern.lsa.domain.commons.spi.AttributeDefinitionImpl'
    
        Extends:
            cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity
    
        Interfaces:
            cern.lsa.domain.commons.AttributeDefinition
    
      Constructors:
        * AttributeDefinitionImpl(long, java.lang.String, java.lang.String, java.lang.String, cern.accsoft.commons.value.Type, java.util.Set, java.lang.String)
        * AttributeDefinitionImpl(cern.lsa.domain.commons.AttributeDefinition)
    
    """
    @typing.overload
    def __init__(self, attributeDefinition: cern.lsa.domain.commons.AttributeDefinition): ...
    @typing.overload
    def __init__(self, long: int, string: str, string2: str, string3: str, type: cern.accsoft.commons.value.Type, set: java.util.Set[str], string4: str): ...
    def getDefaultValue(self) -> str: ...
    def getDescription(self) -> str: ...
    def getEnumValues(self) -> java.util.Set[str]: ...
    def getUnits(self) -> str: ...
    def getValueType(self) -> cern.accsoft.commons.value.Type: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons.spi")``.

    AbstractIdentifiedEntity: typing.Type[AbstractIdentifiedEntity]
    AbstractIdentifiedNamedEntity: typing.Type[AbstractIdentifiedNamedEntity]
    AbstractImmutableIdentifiedEntity: typing.Type[AbstractImmutableIdentifiedEntity]
    AbstractImmutableIdentifiedNamedEntity: typing.Type[AbstractImmutableIdentifiedNamedEntity]
    AbstractPropertiesHolder: typing.Type[AbstractPropertiesHolder]
    AttributeDefinitionImpl: typing.Type[AttributeDefinitionImpl]
    AttributeImpl: typing.Type[AttributeImpl]
