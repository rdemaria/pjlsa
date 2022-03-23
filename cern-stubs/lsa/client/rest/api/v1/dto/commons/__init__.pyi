import cern.accsoft.commons.util
import cern.lsa.client.rest.api.v1.dto
import cern.lsa.domain.commons
import java.lang
import java.util
import typing



class AttributeDefinitionDto(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named):
    """
    @Immutable public interface AttributeDefinitionDto extends cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named
    """
    @staticmethod
    def builder() -> 'DefaultAttributeDefinitionDto.Builder': ...
    def getDefaultValue(self) -> str: ...
    def getDescription(self) -> str: ...
    def getEnumValues(self) -> java.util.Set[str]: ...
    def getUnits(self) -> str: ...
    def getValueType(self) -> cern.lsa.client.rest.api.v1.dto.TypeDto: ...

class AttributeDto(cern.accsoft.commons.util.Named):
    """
    @Immutable public interface AttributeDto extends cern.accsoft.commons.util.Named
    """
    @staticmethod
    def builder() -> 'DefaultAttributeDto.Builder': ...
    def getAttributeDefinition(self) -> AttributeDefinitionDto: ...
    def getValue(self) -> str: ...

class DefaultAttributeDefinitionDto(AttributeDefinitionDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultAttributeDefinitionDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto`.
    
        Use the builder to create immutable instances: :code:`DefaultAttributeDefinitionDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultAttributeDefinitionDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.commons.DefaultAttributeDefinitionDto`.
        
            .. code-block: java
            
             DefaultAttributeDefinitionDto.builder()
                .id(long) // required id
                .name(String) // required :code:`name`
                .valueType(cern.lsa.client.rest.api.v1.dto.TypeDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto.getValueType`
                .units(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto.getUnits`
                .enumValues(Set<String> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto.getEnumValues`
                .description(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto.getDescription`
                .defaultValue(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto.getDefaultValue`
                .build();
             
        
            Returns:
                A new DefaultAttributeDefinitionDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(attributeDefinitionDto: AttributeDefinitionDto) -> 'DefaultAttributeDefinitionDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto`): The instance to copy
        
            Returns:
                A copied immutable AttributeDefinitionDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDefaultValue(self) -> str: ...
    def getDescription(self) -> str: ...
    def getEnumValues(self) -> java.util.Set[str]: ...
    def getId(self) -> int:
        """
        
            Specified by:
                :code:`getId` in interface :code:`cern.lsa.domain.commons.IdentifiedEntity`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def getUnits(self) -> str: ...
    def getValueType(self) -> cern.lsa.client.rest.api.v1.dto.TypeDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto.getValueType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto`
        
            Returns:
                The value of the :code:`valueType` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`id`, :code:`name`, :code:`valueType`, :code:`units`, :code:`enumValues`,
            :code:`description`, :code:`defaultValue`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`AttributeDefinitionDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDefaultValue(self, string: str) -> 'DefaultAttributeDefinitionDto': ...
    def withDescription(self, string: str) -> 'DefaultAttributeDefinitionDto': ...
    @typing.overload
    def withEnumValues(self, iterable: java.lang.Iterable[str]) -> 'DefaultAttributeDefinitionDto': ...
    @typing.overload
    def withEnumValues(self, stringArray: typing.List[str]) -> 'DefaultAttributeDefinitionDto': ...
    def withId(self, long: int) -> 'DefaultAttributeDefinitionDto':
        """
            Copy the current immutable object by setting a value for the :code:`id` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultAttributeDefinitionDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withUnits(self, string: str) -> 'DefaultAttributeDefinitionDto': ...
    def withValueType(self, typeDto: cern.lsa.client.rest.api.v1.dto.TypeDto) -> 'DefaultAttributeDefinitionDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto.getValueType` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.TypeDto`): A new value for valueType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllEnumValues(self, iterable: java.lang.Iterable[str]) -> 'DefaultAttributeDefinitionDto.Builder': ...
        def addEnumValue(self, string: str) -> 'DefaultAttributeDefinitionDto.Builder': ...
        def addEnumValues(self, stringArray: typing.List[str]) -> 'DefaultAttributeDefinitionDto.Builder': ...
        def build(self) -> 'DefaultAttributeDefinitionDto': ...
        def defaultValue(self, string: str) -> 'DefaultAttributeDefinitionDto.Builder': ...
        def description(self, string: str) -> 'DefaultAttributeDefinitionDto.Builder': ...
        def enumValues(self, iterable: java.lang.Iterable[str]) -> 'DefaultAttributeDefinitionDto.Builder': ...
        def id(self, long: int) -> 'DefaultAttributeDefinitionDto.Builder': ...
        def name(self, string: str) -> 'DefaultAttributeDefinitionDto.Builder': ...
        def units(self, string: str) -> 'DefaultAttributeDefinitionDto.Builder': ...
        def valueType(self, typeDto: cern.lsa.client.rest.api.v1.dto.TypeDto) -> 'DefaultAttributeDefinitionDto.Builder': ...

class DefaultAttributeDto(AttributeDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultAttributeDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`.
    
        Use the builder to create immutable instances: :code:`DefaultAttributeDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultAttributeDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.commons.DefaultAttributeDto`.
        
            .. code-block: java
            
             DefaultAttributeDto.builder()
                .name(String) // required name
                .attributeDefinition(cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto.getAttributeDefinition`
                .value(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto.getValue`
                .build();
             
        
            Returns:
                A new DefaultAttributeDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(attributeDto: AttributeDto) -> 'DefaultAttributeDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`): The instance to copy
        
            Returns:
                A copied immutable AttributeDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAttributeDefinition(self) -> AttributeDefinitionDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto.getAttributeDefinition`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`
        
            Returns:
                The value of the :code:`attributeDefinition` attribute
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                The value of the :code:`name` attribute
        
        
        """
        ...
    def getValue(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto.getValue`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`
        
            Returns:
                The value of the :code:`value` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`, :code:`attributeDefinition`, :code:`value`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`AttributeDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAttributeDefinition(self, attributeDefinitionDto: AttributeDefinitionDto) -> 'DefaultAttributeDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto.getAttributeDefinition` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto`): A new value for attributeDefinition
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultAttributeDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withValue(self, string: str) -> 'DefaultAttributeDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto.getValue` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for value
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def attributeDefinition(self, attributeDefinitionDto: AttributeDefinitionDto) -> 'DefaultAttributeDto.Builder': ...
        def build(self) -> 'DefaultAttributeDto': ...
        def name(self, string: str) -> 'DefaultAttributeDto.Builder': ...
        def value(self, string: str) -> 'DefaultAttributeDto.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1.dto.commons")``.

    AttributeDefinitionDto: typing.Type[AttributeDefinitionDto]
    AttributeDto: typing.Type[AttributeDto]
    DefaultAttributeDefinitionDto: typing.Type[DefaultAttributeDefinitionDto]
    DefaultAttributeDto: typing.Type[DefaultAttributeDto]
