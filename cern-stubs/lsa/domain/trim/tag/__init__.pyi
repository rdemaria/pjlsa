import cern.accsoft.commons.util
import cern.lsa.domain.commons
import cern.lsa.domain.settings
import java.io
import java.lang
import java.util
import typing



class TrimTag:
    """
    @Immutable public interface TrimTag
    """
    @staticmethod
    def builder() -> 'DefaultTrimTag.Builder': ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getComment(self) -> str: ...
    def getCreatedBy(self) -> str: ...
    def getStandAloneContext(self) -> cern.lsa.domain.settings.StandAloneContext: ...
    def getTrimHeader(self) -> cern.lsa.domain.settings.TrimHeader: ...
    def getType(self) -> 'TrimTagType': ...

class TrimTagCreationRequest:
    """
    @Immutable public interface TrimTagCreationRequest
    """
    @staticmethod
    def builder() -> 'DefaultTrimTagCreationRequest.Builder': ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getComment(self) -> str: ...
    def getCreatedBy(self) -> str: ...
    def getParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getSettingsSource(self) -> cern.lsa.domain.settings.SettingsSource: ...
    def getStandAloneContext(self) -> cern.lsa.domain.settings.StandAloneContext: ...
    def getTitle(self) -> str: ...
    def getType(self) -> 'TrimTagType': ...

class TrimTagType(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['TrimTagType']):
    """
    public class TrimTagType extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.lsa.domain.trim.tag.TrimTagType`>
    
    
        Also see:
            :meth:`~serialized`
    """
    MD: typing.ClassVar['TrimTagType'] = ...
    """
    public static final :class:`~cern.lsa.domain.trim.tag.TrimTagType` MD
    
    
    """
    GOLDEN: typing.ClassVar['TrimTagType'] = ...
    """
    public static final :class:`~cern.lsa.domain.trim.tag.TrimTagType` GOLDEN
    
    
    """
    SNAPSHOT: typing.ClassVar['TrimTagType'] = ...
    """
    public static final :class:`~cern.lsa.domain.trim.tag.TrimTagType` SNAPSHOT
    
    
    """
    @staticmethod
    def valueOf(string: str) -> 'TrimTagType': ...
    @staticmethod
    def values() -> typing.List['TrimTagType']: ...

class TrimTagsRequest:
    """
    @Immutable public interface TrimTagsRequest
    """
    @staticmethod
    def builder() -> 'DefaultTrimTagsRequest.Builder': ...
    @staticmethod
    def byBeamProcess(beamProcess: cern.lsa.domain.settings.BeamProcess) -> 'DefaultTrimTagsRequest': ...
    @staticmethod
    def byBeamProcesses(collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.BeamProcess], typing.Sequence[cern.lsa.domain.settings.BeamProcess]]) -> 'DefaultTrimTagsRequest': ...
    @staticmethod
    def byTrimHeader(trimHeader: cern.lsa.domain.settings.TrimHeader) -> 'DefaultTrimTagsRequest': ...
    def check(self) -> None: ...
    def getBeamProcesses(self) -> java.util.Set[cern.lsa.domain.settings.BeamProcess]: ...
    def getCreatedBy(self) -> str: ...
    def getParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getTitle(self) -> str: ...
    def getTrimHeaders(self) -> java.util.Set[cern.lsa.domain.settings.TrimHeader]: ...
    def getTrimTagType(self) -> TrimTagType: ...

class DefaultTrimTag(TrimTag, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultTrimTag extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.trim.tag.TrimTag`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.trim.tag.TrimTag`.
    
        Use the builder to create immutable instances: :code:`DefaultTrimTag.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultTrimTag.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.trim.tag.DefaultTrimTag`.
        
            .. code-block: java
            
             DefaultTrimTag.builder()
                .trimHeader(cern.lsa.domain.settings.TrimHeader) // required :meth:`~cern.lsa.domain.trim.tag.TrimTag.getTrimHeader`
                .standAloneContext(cern.lsa.domain.settings.StandAloneContext) // required :meth:`~cern.lsa.domain.trim.tag.TrimTag.getStandAloneContext`
                .createdBy(String) // required :meth:`~cern.lsa.domain.trim.tag.TrimTag.getCreatedBy`
                .comment(String | null) // nullable :meth:`~cern.lsa.domain.trim.tag.TrimTag.getComment`
                .type(cern.lsa.domain.trim.tag.TrimTagType) // required :meth:`~cern.lsa.domain.trim.tag.TrimTag.getType`
                .addAttribute|addAllAttributes(cern.lsa.domain.commons.Attribute) // :meth:`~cern.lsa.domain.trim.tag.TrimTag.getAttributes` elements
                .build();
             
        
            Returns:
                A new DefaultTrimTag builder
        
        
        """
        ...
    @staticmethod
    def copyOf(trimTag: TrimTag) -> 'DefaultTrimTag':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.trim.tag.TrimTag` value. Uses accessors to get values to
            initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.trim.tag.TrimTag`): The instance to copy
        
            Returns:
                A copied immutable TrimTag instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getComment(self) -> str: ...
    def getCreatedBy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.tag.TrimTag.getCreatedBy` in interface :class:`~cern.lsa.domain.trim.tag.TrimTag`
        
            Returns:
                The value of the :code:`createdBy` attribute
        
        
        """
        ...
    def getStandAloneContext(self) -> cern.lsa.domain.settings.StandAloneContext:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.tag.TrimTag.getStandAloneContext` in interface :class:`~cern.lsa.domain.trim.tag.TrimTag`
        
            Returns:
                The value of the :code:`standAloneContext` attribute
        
        
        """
        ...
    def getTrimHeader(self) -> cern.lsa.domain.settings.TrimHeader:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.tag.TrimTag.getTrimHeader` in interface :class:`~cern.lsa.domain.trim.tag.TrimTag`
        
            Returns:
                The value of the :code:`trimHeader` attribute
        
        
        """
        ...
    def getType(self) -> TrimTagType:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.tag.TrimTag.getType` in interface :class:`~cern.lsa.domain.trim.tag.TrimTag`
        
            Returns:
                The value of the :code:`type` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`trimHeader`, :code:`standAloneContext`, :code:`createdBy`, :code:`comment`,
            :code:`type`, :code:`attributes`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`TrimTag` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withAttributes(self, attributeArray: typing.List[cern.lsa.domain.commons.Attribute]) -> 'DefaultTrimTag':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.trim.tag.TrimTag.getAttributes`.
        
            Parameters:
                elements (:class:`~cern.lsa.domain.commons.Attribute`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.domain.trim.tag.DefaultTrimTag` withAttributes (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.commons.Attribute`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.trim.tag.TrimTag.getAttributes`. A shallow reference equality check is used to prevent copying
            of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.commons.Attribute`> elements): An iterable of attributes elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withAttributes(self, iterable: java.lang.Iterable[cern.lsa.domain.commons.Attribute]) -> 'DefaultTrimTag': ...
    def withComment(self, string: str) -> 'DefaultTrimTag': ...
    def withCreatedBy(self, string: str) -> 'DefaultTrimTag':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.domain.trim.tag.TrimTag.getCreatedBy`
            attribute. An equals check used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for createdBy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withStandAloneContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'DefaultTrimTag':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.tag.TrimTag.getStandAloneContext` attribute. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.StandAloneContext`): A new value for standAloneContext
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTrimHeader(self, trimHeader: cern.lsa.domain.settings.TrimHeader) -> 'DefaultTrimTag':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.domain.trim.tag.TrimTag.getTrimHeader`
            attribute. A shallow reference equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.TrimHeader`): A new value for trimHeader
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withType(self, trimTagType: TrimTagType) -> 'DefaultTrimTag':
        """
            Copy the current immutable object by setting a value for the :meth:`~cern.lsa.domain.trim.tag.TrimTag.getType`
            attribute. A shallow reference equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.trim.tag.TrimTagType`): A new value for type
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllAttributes(self, iterable: java.lang.Iterable[cern.lsa.domain.commons.Attribute]) -> 'DefaultTrimTag.Builder': ...
        def addAttribute(self, attribute: cern.lsa.domain.commons.Attribute) -> 'DefaultTrimTag.Builder': ...
        def addAttributes(self, attributeArray: typing.List[cern.lsa.domain.commons.Attribute]) -> 'DefaultTrimTag.Builder': ...
        def attributes(self, iterable: java.lang.Iterable[cern.lsa.domain.commons.Attribute]) -> 'DefaultTrimTag.Builder': ...
        def build(self) -> 'DefaultTrimTag': ...
        def comment(self, string: str) -> 'DefaultTrimTag.Builder': ...
        def createdBy(self, string: str) -> 'DefaultTrimTag.Builder': ...
        def standAloneContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'DefaultTrimTag.Builder': ...
        def trimHeader(self, trimHeader: cern.lsa.domain.settings.TrimHeader) -> 'DefaultTrimTag.Builder': ...
        def type(self, trimTagType: TrimTagType) -> 'DefaultTrimTag.Builder': ...

class DefaultTrimTagCreationRequest(TrimTagCreationRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultTrimTagCreationRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultTrimTagCreationRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultTrimTagCreationRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.trim.tag.DefaultTrimTagCreationRequest`.
        
            .. code-block: java
            
             DefaultTrimTagCreationRequest.builder()
                .settingsSource(cern.lsa.domain.settings.SettingsSource) // required :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getSettingsSource`
                .standAloneContext(cern.lsa.domain.settings.StandAloneContext) // required :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getStandAloneContext`
                .createdBy(String) // required :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getCreatedBy`
                .type(cern.lsa.domain.trim.tag.TrimTagType) // required :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getType`
                .addParameter|addAllParameters(cern.lsa.domain.settings.Parameter) // :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getParameters` elements
                .addAttribute|addAllAttributes(cern.lsa.domain.commons.Attribute) // :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getAttributes` elements
                .title(String) // required :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getTitle`
                .comment(String | null) // nullable :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getComment`
                .build();
             
        
            Returns:
                A new DefaultTrimTagCreationRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(trimTagCreationRequest: TrimTagCreationRequest) -> 'DefaultTrimTagCreationRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest`): The instance to copy
        
            Returns:
                A copied immutable TrimTagCreationRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAttributes(self) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    def getComment(self) -> str: ...
    def getCreatedBy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getCreatedBy`Â in
                interfaceÂ :class:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest`
        
            Returns:
                The value of the :code:`createdBy` attribute
        
        
        """
        ...
    def getParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getSettingsSource(self) -> cern.lsa.domain.settings.SettingsSource:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getSettingsSource`Â in
                interfaceÂ :class:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest`
        
            Returns:
                The value of the :code:`settingsSource` attribute
        
        
        """
        ...
    def getStandAloneContext(self) -> cern.lsa.domain.settings.StandAloneContext:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getStandAloneContext`Â in
                interfaceÂ :class:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest`
        
            Returns:
                The value of the :code:`standAloneContext` attribute
        
        
        """
        ...
    def getTitle(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getTitle`Â in
                interfaceÂ :class:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest`
        
            Returns:
                The value of the :code:`title` attribute
        
        
        """
        ...
    def getType(self) -> TrimTagType:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getType`Â in
                interfaceÂ :class:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest`
        
            Returns:
                The value of the :code:`type` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`settingsSource`, :code:`standAloneContext`, :code:`createdBy`,
            :code:`type`, :code:`parameters`, :code:`attributes`, :code:`title`, :code:`comment`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`TrimTagCreationRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withAttributes(self, attributeArray: typing.List[cern.lsa.domain.commons.Attribute]) -> 'DefaultTrimTagCreationRequest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getAttributes`.
        
            Parameters:
                elements (:class:`~cern.lsa.domain.commons.Attribute`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.domain.trim.tag.DefaultTrimTagCreationRequest` withAttributes (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.commons.Attribute`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getAttributes`. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.commons.Attribute`> elements): An iterable of attributes elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withAttributes(self, iterable: java.lang.Iterable[cern.lsa.domain.commons.Attribute]) -> 'DefaultTrimTagCreationRequest': ...
    def withComment(self, string: str) -> 'DefaultTrimTagCreationRequest': ...
    def withCreatedBy(self, string: str) -> 'DefaultTrimTagCreationRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getCreatedBy` attribute. An equals check used to prevent copying
            of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for createdBy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameters(self, parameterArray: typing.List[cern.lsa.domain.settings.Parameter]) -> 'DefaultTrimTagCreationRequest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getParameters`.
        
            Parameters:
                elements (:class:`~cern.lsa.domain.settings.Parameter`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.domain.trim.tag.DefaultTrimTagCreationRequest` withParameters (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.settings.Parameter`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getParameters`. A shallow reference equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.settings.Parameter`> elements): An iterable of parameters elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameters(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.Parameter]) -> 'DefaultTrimTagCreationRequest': ...
    def withSettingsSource(self, settingsSource: cern.lsa.domain.settings.SettingsSource) -> 'DefaultTrimTagCreationRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getSettingsSource` attribute. A shallow reference equality check
            is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.SettingsSource`): A new value for settingsSource
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withStandAloneContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'DefaultTrimTagCreationRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getStandAloneContext` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.StandAloneContext`): A new value for standAloneContext
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withTitle(self, string: str) -> 'DefaultTrimTagCreationRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getTitle` attribute. An equals check used to prevent copying of
            the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for title
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withType(self, trimTagType: TrimTagType) -> 'DefaultTrimTagCreationRequest':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.tag.TrimTagCreationRequest.getType` attribute. A shallow reference equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.trim.tag.TrimTagType`): A new value for type
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllAttributes(self, iterable: java.lang.Iterable[cern.lsa.domain.commons.Attribute]) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def addAllParameters(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.Parameter]) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def addAttribute(self, attribute: cern.lsa.domain.commons.Attribute) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def addAttributes(self, attributeArray: typing.List[cern.lsa.domain.commons.Attribute]) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def addParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def addParameters(self, parameterArray: typing.List[cern.lsa.domain.settings.Parameter]) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def attributes(self, iterable: java.lang.Iterable[cern.lsa.domain.commons.Attribute]) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def build(self) -> 'DefaultTrimTagCreationRequest': ...
        def comment(self, string: str) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def createdBy(self, string: str) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def parameters(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.Parameter]) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def settingsSource(self, settingsSource: cern.lsa.domain.settings.SettingsSource) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def standAloneContext(self, standAloneContext: cern.lsa.domain.settings.StandAloneContext) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def title(self, string: str) -> 'DefaultTrimTagCreationRequest.Builder': ...
        def type(self, trimTagType: TrimTagType) -> 'DefaultTrimTagCreationRequest.Builder': ...

class DefaultTrimTagsRequest(TrimTagsRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultTrimTagsRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.trim.tag.TrimTagsRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.trim.tag.TrimTagsRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultTrimTagsRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultTrimTagsRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.trim.tag.DefaultTrimTagsRequest`.
        
            .. code-block: java
            
             DefaultTrimTagsRequest.builder()
                .trimHeaders(Set<cern.lsa.domain.settings.TrimHeader> | null) // nullable :meth:`~cern.lsa.domain.trim.tag.TrimTagsRequest.getTrimHeaders`
                .beamProcesses(Set<cern.lsa.domain.settings.BeamProcess> | null) // nullable :meth:`~cern.lsa.domain.trim.tag.TrimTagsRequest.getBeamProcesses`
                .parameters(Set<cern.lsa.domain.settings.Parameter> | null) // nullable :meth:`~cern.lsa.domain.trim.tag.TrimTagsRequest.getParameters`
                .title(String | null) // nullable :meth:`~cern.lsa.domain.trim.tag.TrimTagsRequest.getTitle`
                .createdBy(String | null) // nullable :meth:`~cern.lsa.domain.trim.tag.TrimTagsRequest.getCreatedBy`
                .trimTagType(cern.lsa.domain.trim.tag.TrimTagType | null) // nullable :meth:`~cern.lsa.domain.trim.tag.TrimTagsRequest.getTrimTagType`
                .build();
             
        
            Returns:
                A new DefaultTrimTagsRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(trimTagsRequest: TrimTagsRequest) -> 'DefaultTrimTagsRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.trim.tag.TrimTagsRequest` value. Uses accessors to get values to
            initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.trim.tag.TrimTagsRequest`): The instance to copy
        
            Returns:
                A copied immutable TrimTagsRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getBeamProcesses(self) -> java.util.Set[cern.lsa.domain.settings.BeamProcess]: ...
    def getCreatedBy(self) -> str: ...
    def getParameters(self) -> java.util.Set[cern.lsa.domain.settings.Parameter]: ...
    def getTitle(self) -> str: ...
    def getTrimHeaders(self) -> java.util.Set[cern.lsa.domain.settings.TrimHeader]: ...
    def getTrimTagType(self) -> TrimTagType: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`trimHeaders`, :code:`beamProcesses`, :code:`parameters`, :code:`title`,
            :code:`createdBy`, :code:`trimTagType`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`TrimTagsRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withBeamProcesses(self, beamProcessArray: typing.List[cern.lsa.domain.settings.BeamProcess]) -> 'DefaultTrimTagsRequest': ...
    @typing.overload
    def withBeamProcesses(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.BeamProcess]) -> 'DefaultTrimTagsRequest': ...
    def withCreatedBy(self, string: str) -> 'DefaultTrimTagsRequest': ...
    @typing.overload
    def withParameters(self, parameterArray: typing.List[cern.lsa.domain.settings.Parameter]) -> 'DefaultTrimTagsRequest': ...
    @typing.overload
    def withParameters(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.Parameter]) -> 'DefaultTrimTagsRequest': ...
    def withTitle(self, string: str) -> 'DefaultTrimTagsRequest': ...
    @typing.overload
    def withTrimHeaders(self, trimHeaderArray: typing.List[cern.lsa.domain.settings.TrimHeader]) -> 'DefaultTrimTagsRequest': ...
    @typing.overload
    def withTrimHeaders(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.TrimHeader]) -> 'DefaultTrimTagsRequest': ...
    def withTrimTagType(self, trimTagType: TrimTagType) -> 'DefaultTrimTagsRequest': ...
    class Builder:
        def addAllBeamProcesses(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.BeamProcess]) -> 'DefaultTrimTagsRequest.Builder': ...
        def addAllParameters(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.Parameter]) -> 'DefaultTrimTagsRequest.Builder': ...
        def addAllTrimHeaders(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.TrimHeader]) -> 'DefaultTrimTagsRequest.Builder': ...
        def addBeamProcess(self, beamProcess: cern.lsa.domain.settings.BeamProcess) -> 'DefaultTrimTagsRequest.Builder': ...
        def addBeamProcesses(self, beamProcessArray: typing.List[cern.lsa.domain.settings.BeamProcess]) -> 'DefaultTrimTagsRequest.Builder': ...
        def addParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultTrimTagsRequest.Builder': ...
        def addParameters(self, parameterArray: typing.List[cern.lsa.domain.settings.Parameter]) -> 'DefaultTrimTagsRequest.Builder': ...
        def addTrimHeader(self, trimHeader: cern.lsa.domain.settings.TrimHeader) -> 'DefaultTrimTagsRequest.Builder': ...
        def addTrimHeaders(self, trimHeaderArray: typing.List[cern.lsa.domain.settings.TrimHeader]) -> 'DefaultTrimTagsRequest.Builder': ...
        def beamProcesses(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.BeamProcess]) -> 'DefaultTrimTagsRequest.Builder': ...
        def build(self) -> 'DefaultTrimTagsRequest': ...
        def createdBy(self, string: str) -> 'DefaultTrimTagsRequest.Builder': ...
        def parameters(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.Parameter]) -> 'DefaultTrimTagsRequest.Builder': ...
        def title(self, string: str) -> 'DefaultTrimTagsRequest.Builder': ...
        def trimHeaders(self, iterable: java.lang.Iterable[cern.lsa.domain.settings.TrimHeader]) -> 'DefaultTrimTagsRequest.Builder': ...
        def trimTagType(self, trimTagType: TrimTagType) -> 'DefaultTrimTagsRequest.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.trim.tag")``.

    DefaultTrimTag: typing.Type[DefaultTrimTag]
    DefaultTrimTagCreationRequest: typing.Type[DefaultTrimTagCreationRequest]
    DefaultTrimTagsRequest: typing.Type[DefaultTrimTagsRequest]
    TrimTag: typing.Type[TrimTag]
    TrimTagCreationRequest: typing.Type[TrimTagCreationRequest]
    TrimTagType: typing.Type[TrimTagType]
    TrimTagsRequest: typing.Type[TrimTagsRequest]
