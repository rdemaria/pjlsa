import cern.lsa.client.rest.api.v1.dto
import cern.lsa.client.rest.api.v1.dto.commons
import cern.lsa.client.rest.api.v1.dto.settings
import java.lang
import java.util
import typing



class TrimTagCreationRequestDto:
    """
    @Immutable public interface TrimTagCreationRequestDto
    """
    @staticmethod
    def builder() -> 'DefaultTrimTagCreationRequestDto.Builder': ...
    def getAttributes(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]: ...
    def getComment(self) -> str: ...
    def getCreatedBy(self) -> str: ...
    def getParameters(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterDto]: ...
    def getSettingsDate(self) -> java.util.Date: ...
    def getStandAloneContextId(self) -> int: ...
    def getTitle(self) -> str: ...
    def getType(self) -> str: ...

class TrimTagDto:
    """
    @Immutable public interface TrimTagDto
    """
    @staticmethod
    def builder() -> 'DefaultTrimTagDto.Builder': ...
    def getAttributes(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]: ...
    def getComment(self) -> str: ...
    def getCreatedBy(self) -> str: ...
    def getStandAloneContextId(self) -> int: ...
    def getTrimHeaderDto(self) -> cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto: ...
    def getTypeName(self) -> str: ...

class TrimTagsRequestDto:
    """
    @Immutable public interface TrimTagsRequestDto
    """
    @staticmethod
    def builder() -> 'DefaultTrimTagsRequestDto.Builder': ...
    def check(self) -> None: ...
    def getBeamProcesses(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto]: ...
    def getCreatedBy(self) -> str: ...
    def getParameters(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterDto]: ...
    def getStandAloneContextIds(self) -> java.util.Set[int]: ...
    def getTitle(self) -> str: ...
    def getTrimHeaders(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto]: ...
    def getTrimTagType(self) -> str: ...

class DefaultTrimTagCreationRequestDto(TrimTagCreationRequestDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultTrimTagCreationRequestDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto`.
    
        Use the builder to create immutable instances: :code:`DefaultTrimTagCreationRequestDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultTrimTagCreationRequestDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.DefaultTrimTagCreationRequestDto`.
        
            .. code-block: java
            
             DefaultTrimTagCreationRequestDto.builder()
                .settingsDate(Date) // required :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getSettingsDate`
                .standAloneContextId(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getStandAloneContextId`
                .createdBy(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getCreatedBy`
                .type(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getType`
                .addParameter|addAllParameters(cern.lsa.client.rest.api.v1.dto.ParameterDto) // :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getParameters` elements
                .addAttribute|addAllAttributes(cern.lsa.client.rest.api.v1.dto.commons.AttributeDto) // :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getAttributes` elements
                .title(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getTitle`
                .comment(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getComment`
                .build();
             
        
            Returns:
                A new DefaultTrimTagCreationRequestDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(trimTagCreationRequestDto: TrimTagCreationRequestDto) -> 'DefaultTrimTagCreationRequestDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto`): The instance to copy
        
            Returns:
                A copied immutable TrimTagCreationRequestDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAttributes(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]: ...
    def getComment(self) -> str: ...
    def getCreatedBy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getCreatedBy`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto`
        
            Returns:
                The value of the :code:`createdBy` attribute
        
        
        """
        ...
    def getParameters(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterDto]: ...
    def getSettingsDate(self) -> java.util.Date:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getSettingsDate`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto`
        
            Returns:
                The value of the :code:`settingsDate` attribute
        
        
        """
        ...
    def getStandAloneContextId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getStandAloneContextId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto`
        
            Returns:
                The value of the :code:`standAloneContextId` attribute
        
        
        """
        ...
    def getTitle(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getTitle`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto`
        
            Returns:
                The value of the :code:`title` attribute
        
        
        """
        ...
    def getType(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getType`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto`
        
            Returns:
                The value of the :code:`type` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`settingsDate`, :code:`standAloneContextId`, :code:`createdBy`,
            :code:`type`, :code:`parameters`, :code:`attributes`, :code:`title`, :code:`comment`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`TrimTagCreationRequestDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withAttributes(self, attributeDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]) -> 'DefaultTrimTagCreationRequestDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getAttributes`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.DefaultTrimTagCreationRequestDto` withAttributes (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getAttributes`. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`> elements): An iterable of attributes elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withAttributes(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]) -> 'DefaultTrimTagCreationRequestDto': ...
    def withComment(self, string: str) -> 'DefaultTrimTagCreationRequestDto': ...
    def withCreatedBy(self, string: str) -> 'DefaultTrimTagCreationRequestDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getCreatedBy` attribute. An equals check used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for createdBy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameters(self, parameterDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.ParameterDto]) -> 'DefaultTrimTagCreationRequestDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getParameters`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.DefaultTrimTagCreationRequestDto` withParameters (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getParameters`. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.ParameterDto`> elements): An iterable of parameters elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameters(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.ParameterDto]) -> 'DefaultTrimTagCreationRequestDto': ...
    def withSettingsDate(self, date: java.util.Date) -> 'DefaultTrimTagCreationRequestDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getSettingsDate` attribute. A shallow
            reference equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): A new value for settingsDate
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withStandAloneContextId(self, long: int) -> 'DefaultTrimTagCreationRequestDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getStandAloneContextId` attribute. A value
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for standAloneContextId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTitle(self, string: str) -> 'DefaultTrimTagCreationRequestDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getTitle` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for title
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withType(self, string: str) -> 'DefaultTrimTagCreationRequestDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto.getType` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for type
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllAttributes(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def addAllParameters(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.ParameterDto]) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def addAttribute(self, attributeDto: cern.lsa.client.rest.api.v1.dto.commons.AttributeDto) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def addAttributes(self, attributeDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def addParameter(self, parameterDto: cern.lsa.client.rest.api.v1.dto.ParameterDto) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def addParameters(self, parameterDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.ParameterDto]) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def attributes(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def build(self) -> 'DefaultTrimTagCreationRequestDto': ...
        def comment(self, string: str) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def createdBy(self, string: str) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def parameters(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.ParameterDto]) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def settingsDate(self, date: java.util.Date) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def standAloneContextId(self, long: int) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def title(self, string: str) -> 'DefaultTrimTagCreationRequestDto.Builder': ...
        def type(self, string: str) -> 'DefaultTrimTagCreationRequestDto.Builder': ...

class DefaultTrimTagDto(TrimTagDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultTrimTagDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto`.
    
        Use the builder to create immutable instances: :code:`DefaultTrimTagDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultTrimTagDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.DefaultTrimTagDto`.
        
            .. code-block: java
            
             DefaultTrimTagDto.builder()
                .trimHeaderDto(cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto) // required :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getTrimHeaderDto`
                .standAloneContextId(long) // required :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getStandAloneContextId`
                .createdBy(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getCreatedBy`
                .comment(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getComment`
                .typeName(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getTypeName`
                .addAttribute|addAllAttributes(cern.lsa.client.rest.api.v1.dto.commons.AttributeDto) // :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getAttributes` elements
                .build();
             
        
            Returns:
                A new DefaultTrimTagDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(trimTagDto: TrimTagDto) -> 'DefaultTrimTagDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto`): The instance to copy
        
            Returns:
                A copied immutable TrimTagDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAttributes(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]: ...
    def getComment(self) -> str: ...
    def getCreatedBy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getCreatedBy`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto`
        
            Returns:
                The value of the :code:`createdBy` attribute
        
        
        """
        ...
    def getStandAloneContextId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getStandAloneContextId`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto`
        
            Returns:
                The value of the :code:`standAloneContextId` attribute
        
        
        """
        ...
    def getTrimHeaderDto(self) -> cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getTrimHeaderDto`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto`
        
            Returns:
                The value of the :code:`trimHeaderDto` attribute
        
        
        """
        ...
    def getTypeName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getTypeName`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto`
        
            Returns:
                The value of the :code:`typeName` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`trimHeaderDto`, :code:`standAloneContextId`, :code:`createdBy`,
            :code:`comment`, :code:`typeName`, :code:`attributes`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`TrimTagDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withAttributes(self, attributeDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]) -> 'DefaultTrimTagDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getAttributes`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.DefaultTrimTagDto` withAttributes (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getAttributes`. A shallow reference equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.commons.AttributeDto`> elements): An iterable of attributes elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withAttributes(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]) -> 'DefaultTrimTagDto': ...
    def withComment(self, string: str) -> 'DefaultTrimTagDto': ...
    def withCreatedBy(self, string: str) -> 'DefaultTrimTagDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getCreatedBy` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for createdBy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withStandAloneContextId(self, long: int) -> 'DefaultTrimTagDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getStandAloneContextId` attribute. A value equality check is
            used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for standAloneContextId
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTrimHeaderDto(self, trimHeaderDto: cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto) -> 'DefaultTrimTagDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getTrimHeaderDto` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto`): A new value for trimHeaderDto
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTypeName(self, string: str) -> 'DefaultTrimTagDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto.getTypeName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for typeName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllAttributes(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]) -> 'DefaultTrimTagDto.Builder': ...
        def addAttribute(self, attributeDto: cern.lsa.client.rest.api.v1.dto.commons.AttributeDto) -> 'DefaultTrimTagDto.Builder': ...
        def addAttributes(self, attributeDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]) -> 'DefaultTrimTagDto.Builder': ...
        def attributes(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.commons.AttributeDto]) -> 'DefaultTrimTagDto.Builder': ...
        def build(self) -> 'DefaultTrimTagDto': ...
        def comment(self, string: str) -> 'DefaultTrimTagDto.Builder': ...
        def createdBy(self, string: str) -> 'DefaultTrimTagDto.Builder': ...
        def standAloneContextId(self, long: int) -> 'DefaultTrimTagDto.Builder': ...
        def trimHeaderDto(self, trimHeaderDto: cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto) -> 'DefaultTrimTagDto.Builder': ...
        def typeName(self, string: str) -> 'DefaultTrimTagDto.Builder': ...

class DefaultTrimTagsRequestDto(TrimTagsRequestDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultTrimTagsRequestDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto`.
    
        Use the builder to create immutable instances: :code:`DefaultTrimTagsRequestDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultTrimTagsRequestDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.DefaultTrimTagsRequestDto`.
        
            .. code-block: java
            
             DefaultTrimTagsRequestDto.builder()
                .addStandAloneContextId|addAllStandAloneContextIds(long) // :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto.getStandAloneContextIds` elements
                .trimHeaders(Set<cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto.getTrimHeaders`
                .beamProcesses(Set<cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto.getBeamProcesses`
                .parameters(Set<cern.lsa.client.rest.api.v1.dto.ParameterDto> | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto.getParameters`
                .title(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto.getTitle`
                .createdBy(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto.getCreatedBy`
                .trimTagType(String | null) // nullable :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto.getTrimTagType`
                .build();
             
        
            Returns:
                A new DefaultTrimTagsRequestDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(trimTagsRequestDto: TrimTagsRequestDto) -> 'DefaultTrimTagsRequestDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto`): The instance to copy
        
            Returns:
                A copied immutable TrimTagsRequestDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBeamProcesses(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto]: ...
    def getCreatedBy(self) -> str: ...
    def getParameters(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.ParameterDto]: ...
    def getStandAloneContextIds(self) -> java.util.Set[int]: ...
    def getTitle(self) -> str: ...
    def getTrimHeaders(self) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto]: ...
    def getTrimTagType(self) -> str: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`standAloneContextIds`, :code:`trimHeaders`, :code:`beamProcesses`,
            :code:`parameters`, :code:`title`, :code:`createdBy`, :code:`trimTagType`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`TrimTagsRequestDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withBeamProcesses(self, beamProcessDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto]) -> 'DefaultTrimTagsRequestDto': ...
    @typing.overload
    def withBeamProcesses(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto]) -> 'DefaultTrimTagsRequestDto': ...
    def withCreatedBy(self, string: str) -> 'DefaultTrimTagsRequestDto': ...
    @typing.overload
    def withParameters(self, parameterDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.ParameterDto]) -> 'DefaultTrimTagsRequestDto': ...
    @typing.overload
    def withParameters(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.ParameterDto]) -> 'DefaultTrimTagsRequestDto': ...
    @typing.overload
    def withStandAloneContextIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultTrimTagsRequestDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto.getStandAloneContextIds`.
        
            Parameters:
                elements (long...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.trim.tag.DefaultTrimTagsRequestDto` withStandAloneContextIds (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto.getStandAloneContextIds`. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<`Long <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Long.html?is-external=true>`> elements): An iterable of standAloneContextIds elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withStandAloneContextIds(self, longArray: typing.List[int]) -> 'DefaultTrimTagsRequestDto': ...
    def withTitle(self, string: str) -> 'DefaultTrimTagsRequestDto': ...
    @typing.overload
    def withTrimHeaders(self, trimHeaderDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto]) -> 'DefaultTrimTagsRequestDto': ...
    @typing.overload
    def withTrimHeaders(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto]) -> 'DefaultTrimTagsRequestDto': ...
    def withTrimTagType(self, string: str) -> 'DefaultTrimTagsRequestDto': ...
    class Builder:
        def addAllBeamProcesses(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addAllParameters(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.ParameterDto]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addAllStandAloneContextIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addAllTrimHeaders(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addBeamProcess(self, beamProcessDto: cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addBeamProcesses(self, beamProcessDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addParameter(self, parameterDto: cern.lsa.client.rest.api.v1.dto.ParameterDto) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addParameters(self, parameterDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.ParameterDto]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addStandAloneContextId(self, long: int) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addStandAloneContextIds(self, longArray: typing.List[int]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addTrimHeader(self, trimHeaderDto: cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def addTrimHeaders(self, trimHeaderDtoArray: typing.List[cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def beamProcesses(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def build(self) -> 'DefaultTrimTagsRequestDto': ...
        def createdBy(self, string: str) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def parameters(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.ParameterDto]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def standAloneContextIds(self, iterable: java.lang.Iterable[int]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def title(self, string: str) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def trimHeaders(self, iterable: java.lang.Iterable[cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto]) -> 'DefaultTrimTagsRequestDto.Builder': ...
        def trimTagType(self, string: str) -> 'DefaultTrimTagsRequestDto.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1.dto.trim.tag")``.

    DefaultTrimTagCreationRequestDto: typing.Type[DefaultTrimTagCreationRequestDto]
    DefaultTrimTagDto: typing.Type[DefaultTrimTagDto]
    DefaultTrimTagsRequestDto: typing.Type[DefaultTrimTagsRequestDto]
    TrimTagCreationRequestDto: typing.Type[TrimTagCreationRequestDto]
    TrimTagDto: typing.Type[TrimTagDto]
    TrimTagsRequestDto: typing.Type[TrimTagsRequestDto]
