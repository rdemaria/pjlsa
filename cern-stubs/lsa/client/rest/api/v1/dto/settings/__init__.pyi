import cern.accsoft.commons.util
import cern.lsa.domain.commons
import java.lang
import java.util
import typing



class BeamProcessDto(cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity):
    """
    @Immutable public interface BeamProcessDto extends cern.accsoft.commons.util.Named, cern.lsa.domain.commons.IdentifiedEntity
    """
    @staticmethod
    def builder() -> 'DefaultBeamProcessDto.Builder': ...

class TrimHeaderDto(cern.lsa.domain.commons.IdentifiedEntity):
    """
    @Immutable public interface TrimHeaderDto extends cern.lsa.domain.commons.IdentifiedEntity
    """
    @staticmethod
    def builder() -> 'DefaultTrimHeaderDto.Builder': ...
    def getBeamProcessDtos(self) -> java.util.List[BeamProcessDto]: ...
    def getClientInfo(self) -> str: ...
    def getCreatedDate(self) -> java.util.Date: ...
    def getDescription(self) -> str: ...
    def isTag(self) -> bool: ...

class DefaultBeamProcessDto(BeamProcessDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultBeamProcessDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto`.
    
        Use the builder to create immutable instances: :code:`DefaultBeamProcessDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultBeamProcessDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.settings.DefaultBeamProcessDto`.
        
            .. code-block: java
            
             DefaultBeamProcessDto.builder()
                .name(String) // required name
                .id(long) // required :code:`id`
                .build();
             
        
            Returns:
                A new DefaultBeamProcessDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(beamProcessDto: BeamProcessDto) -> 'DefaultBeamProcessDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto` value. Uses accessors
            to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto`): The instance to copy
        
            Returns:
                A copied immutable BeamProcessDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
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
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`name`, :code:`id`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`BeamProcessDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultBeamProcessDto':
        """
            Copy the current immutable object by setting a value for the :code:`id` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withName(self, string: str) -> 'DefaultBeamProcessDto':
        """
            Copy the current immutable object by setting a value for the :code:`name` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for name
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultBeamProcessDto': ...
        def id(self, long: int) -> 'DefaultBeamProcessDto.Builder': ...
        def name(self, string: str) -> 'DefaultBeamProcessDto.Builder': ...

class DefaultTrimHeaderDto(TrimHeaderDto):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultTrimHeaderDto extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto`
    
        Immutable implementation of :class:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto`.
    
        Use the builder to create immutable instances: :code:`DefaultTrimHeaderDto.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultTrimHeaderDto.Builder':
        """
            Creates a builder for :class:`~cern.lsa.client.rest.api.v1.dto.settings.DefaultTrimHeaderDto`.
        
            .. code-block: java
            
             DefaultTrimHeaderDto.builder()
                .id(long) // required id
                .description(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getDescription`
                .addBeamProcessDto|addAllBeamProcessDtos(cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto) // :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getBeamProcessDtos` elements
                .createdDate(Date) // required :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getCreatedDate`
                .clientInfo(String) // required :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getClientInfo`
                .tag(boolean) // required :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.isTag`
                .build();
             
        
            Returns:
                A new DefaultTrimHeaderDto builder
        
        
        """
        ...
    @staticmethod
    def copyOf(trimHeaderDto: TrimHeaderDto) -> 'DefaultTrimHeaderDto':
        """
            Creates an immutable copy of a :class:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto`): The instance to copy
        
            Returns:
                A copied immutable TrimHeaderDto instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBeamProcessDtos(self) -> java.util.List[BeamProcessDto]: ...
    def getClientInfo(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getClientInfo`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto`
        
            Returns:
                The value of the :code:`clientInfo` attribute
        
        
        """
        ...
    def getCreatedDate(self) -> java.util.Date:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getCreatedDate`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto`
        
            Returns:
                The value of the :code:`createdDate` attribute
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto`
        
            Returns:
                The value of the :code:`description` attribute
        
        
        """
        ...
    def getId(self) -> int:
        """
        
            Specified by:
                :code:`getId` in interface :code:`cern.lsa.domain.commons.IdentifiedEntity`
        
            Returns:
                The value of the :code:`id` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`id`, :code:`description`, :code:`beamProcessDtos`, :code:`createdDate`,
            :code:`clientInfo`, :code:`tag`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isTag(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.isTag`Â in
                interfaceÂ :class:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto`
        
            Returns:
                The value of the :code:`tag` attribute
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`TrimHeaderDto` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withBeamProcessDtos(self, beamProcessDtoArray: typing.List[BeamProcessDto]) -> 'DefaultTrimHeaderDto':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getBeamProcessDtos`.
        
            Parameters:
                elements (:class:`~cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.client.rest.api.v1.dto.settings.DefaultTrimHeaderDto` withBeamProcessDtos (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getBeamProcessDtos`. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.client.rest.api.v1.dto.settings.BeamProcessDto`> elements): An iterable of beamProcessDtos elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withBeamProcessDtos(self, iterable: java.lang.Iterable[BeamProcessDto]) -> 'DefaultTrimHeaderDto': ...
    def withClientInfo(self, string: str) -> 'DefaultTrimHeaderDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getClientInfo` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for clientInfo
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withCreatedDate(self, date: java.util.Date) -> 'DefaultTrimHeaderDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getCreatedDate` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): A new value for createdDate
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withDescription(self, string: str) -> 'DefaultTrimHeaderDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.getDescription` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for description
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withId(self, long: int) -> 'DefaultTrimHeaderDto':
        """
            Copy the current immutable object by setting a value for the :code:`id` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (long): A new value for id
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTag(self, boolean: bool) -> 'DefaultTrimHeaderDto':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.client.rest.api.v1.dto.settings.TrimHeaderDto.isTag` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for tag
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllBeamProcessDtos(self, iterable: java.lang.Iterable[BeamProcessDto]) -> 'DefaultTrimHeaderDto.Builder': ...
        def addBeamProcessDto(self, beamProcessDto: BeamProcessDto) -> 'DefaultTrimHeaderDto.Builder': ...
        def addBeamProcessDtos(self, beamProcessDtoArray: typing.List[BeamProcessDto]) -> 'DefaultTrimHeaderDto.Builder': ...
        def beamProcessDtos(self, iterable: java.lang.Iterable[BeamProcessDto]) -> 'DefaultTrimHeaderDto.Builder': ...
        def build(self) -> 'DefaultTrimHeaderDto': ...
        def clientInfo(self, string: str) -> 'DefaultTrimHeaderDto.Builder': ...
        def createdDate(self, date: java.util.Date) -> 'DefaultTrimHeaderDto.Builder': ...
        def description(self, string: str) -> 'DefaultTrimHeaderDto.Builder': ...
        def id(self, long: int) -> 'DefaultTrimHeaderDto.Builder': ...
        def tag(self, boolean: bool) -> 'DefaultTrimHeaderDto.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1.dto.settings")``.

    BeamProcessDto: typing.Type[BeamProcessDto]
    DefaultBeamProcessDto: typing.Type[DefaultBeamProcessDto]
    DefaultTrimHeaderDto: typing.Type[DefaultTrimHeaderDto]
    TrimHeaderDto: typing.Type[TrimHeaderDto]
