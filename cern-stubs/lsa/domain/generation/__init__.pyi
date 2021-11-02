import cern.accsoft.commons.domain.particletransfers
import cern.lsa.domain.settings
import com.google.common.collect
import java.io
import java.lang
import java.util
import typing



class ValueGeneratorConfigInfo:
    """
    @Immutable public interface ValueGeneratorConfigInfo
    """
    @staticmethod
    def builder() -> 'DefaultValueGeneratorConfigInfo.Builder': ...
    def getValueGeneratorConfigStatus(self) -> 'ValueGeneratorConfigInfo.ValueGeneratorConfigStatus': ...
    def getValueGeneratorInfo(self) -> java.util.Optional['ValueGeneratorInfo']: ...
    @typing.overload
    @staticmethod
    def of(valueGeneratorConfigStatus: 'ValueGeneratorConfigInfo.ValueGeneratorConfigStatus') -> 'ValueGeneratorConfigInfo':
        """
        static :class:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo` of (:class:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo.ValueGeneratorConfigStatus` valueGeneratorConfigStatus)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(valueGeneratorConfigStatus: 'ValueGeneratorConfigInfo.ValueGeneratorConfigStatus', valueGeneratorInfo: 'ValueGeneratorInfo') -> 'ValueGeneratorConfigInfo': ...
    class ValueGeneratorConfigStatus(java.lang.Enum['ValueGeneratorConfigInfo.ValueGeneratorConfigStatus']):
        FULLY_CONFIGURED: typing.ClassVar['ValueGeneratorConfigInfo.ValueGeneratorConfigStatus'] = ...
        NOT_CONFIGURED: typing.ClassVar['ValueGeneratorConfigInfo.ValueGeneratorConfigStatus'] = ...
        BEAN_MISSING: typing.ClassVar['ValueGeneratorConfigInfo.ValueGeneratorConfigStatus'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ValueGeneratorConfigInfo.ValueGeneratorConfigStatus': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['ValueGeneratorConfigInfo.ValueGeneratorConfigStatus']: ...

class ValueGeneratorDefinition:
    """
    public interface ValueGeneratorDefinition
    """
    @staticmethod
    def builder() -> 'DefaultValueGeneratorDefinition.Builder': ...
    def getArguments(self) -> java.util.List[str]: ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def getParameterType(self) -> cern.lsa.domain.settings.ParameterType: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...
    def getValueGeneratorName(self) -> str: ...

class ValueGeneratorDefinitionsRequest:
    """
    @Immutable public interface ValueGeneratorDefinitionsRequest
    """
    @staticmethod
    def builder() -> 'DefaultValueGeneratorDefinitionsRequest.Builder': ...
    def getParameterTypes(self) -> java.util.Collection[cern.lsa.domain.settings.ParameterType]: ...
    def getParameters(self) -> java.util.Collection[cern.lsa.domain.settings.Parameter]: ...
    def getParticleTransfers(self) -> java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getValueGeneratorNames(self) -> java.util.Collection[str]: ...

class ValueGeneratorInfo:
    """
    @Immutable public interface ValueGeneratorInfo
    """
    @staticmethod
    def builder() -> 'DefaultValueGeneratorInfo.Builder': ...
    def getArguments(self) -> java.util.List[str]: ...
    def getValueGeneratorName(self) -> str: ...
    @staticmethod
    def of(string: str, list: java.util.List[str]) -> 'ValueGeneratorInfo': ...

class AbstractValueGeneratorDefinition(ValueGeneratorDefinition):
    """
    @Immutable public abstract class AbstractValueGeneratorDefinition extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.generation.ValueGeneratorDefinition`
    """
    def __init__(self): ...

class DefaultValueGeneratorConfigInfo(ValueGeneratorConfigInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultValueGeneratorConfigInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultValueGeneratorConfigInfo.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultValueGeneratorConfigInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.generation.DefaultValueGeneratorConfigInfo`.
        
            .. code-block: java
            
             DefaultValueGeneratorConfigInfo.builder()
                .valueGeneratorConfigStatus(cern.lsa.domain.generation.ValueGeneratorConfigInfo.ValueGeneratorConfigStatus) // required :meth:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo.getValueGeneratorConfigStatus`
                .valueGeneratorInfo(cern.lsa.domain.generation.ValueGeneratorInfo) // optional :meth:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo.getValueGeneratorInfo`
                .build();
             
        
            Returns:
                A new DefaultValueGeneratorConfigInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(valueGeneratorConfigInfo: ValueGeneratorConfigInfo) -> 'DefaultValueGeneratorConfigInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo`): The instance to copy
        
            Returns:
                A copied immutable ValueGeneratorConfigInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getValueGeneratorConfigStatus(self) -> ValueGeneratorConfigInfo.ValueGeneratorConfigStatus:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo.getValueGeneratorConfigStatus`Â in
                interfaceÂ :class:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo`
        
            Returns:
                The value of the :code:`valueGeneratorConfigStatus` attribute
        
        
        """
        ...
    def getValueGeneratorInfo(self) -> java.util.Optional[ValueGeneratorInfo]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`valueGeneratorConfigStatus`, :code:`valueGeneratorInfo`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ValueGeneratorConfigInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withValueGeneratorConfigStatus(self, valueGeneratorConfigStatus: ValueGeneratorConfigInfo.ValueGeneratorConfigStatus) -> 'DefaultValueGeneratorConfigInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo.getValueGeneratorConfigStatus` attribute. A value equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo.ValueGeneratorConfigStatus`): A new value for valueGeneratorConfigStatus
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withValueGeneratorInfo(self, valueGeneratorInfo: ValueGeneratorInfo) -> 'DefaultValueGeneratorConfigInfo':
        """
            Copy the current immutable object by setting a *present* value for the optional
            :meth:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo.getValueGeneratorInfo` attribute.
        
            Parameters:
                value (:class:`~cern.lsa.domain.generation.ValueGeneratorInfo`): The value for valueGeneratorInfo
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.domain.generation.DefaultValueGeneratorConfigInfo` withValueGeneratorInfo (`Optional <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Optional.html?is-external=true>`<? extends :class:`~cern.lsa.domain.generation.ValueGeneratorInfo`> optional)
        
            Copy the current immutable object by setting an optional value for the
            :meth:`~cern.lsa.domain.generation.ValueGeneratorConfigInfo.getValueGeneratorInfo` attribute. A shallow reference
            equality check is used on unboxed optional value to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                optional (`Optional <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Optional.html?is-external=true>`<? extends :class:`~cern.lsa.domain.generation.ValueGeneratorInfo`> optional): A value for valueGeneratorInfo
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withValueGeneratorInfo(self, optional: java.util.Optional[ValueGeneratorInfo]) -> 'DefaultValueGeneratorConfigInfo': ...
    class Builder:
        def build(self) -> 'DefaultValueGeneratorConfigInfo': ...
        def valueGeneratorConfigStatus(self, valueGeneratorConfigStatus: ValueGeneratorConfigInfo.ValueGeneratorConfigStatus) -> 'DefaultValueGeneratorConfigInfo.Builder': ...
        @typing.overload
        def valueGeneratorInfo(self, valueGeneratorInfo: ValueGeneratorInfo) -> 'DefaultValueGeneratorConfigInfo.Builder': ...
        @typing.overload
        def valueGeneratorInfo(self, optional: java.util.Optional[ValueGeneratorInfo]) -> 'DefaultValueGeneratorConfigInfo.Builder': ...

class DefaultValueGeneratorDefinitionsRequest(ValueGeneratorDefinitionsRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultValueGeneratorDefinitionsRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.generation.ValueGeneratorDefinitionsRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.generation.ValueGeneratorDefinitionsRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultValueGeneratorDefinitionsRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultValueGeneratorDefinitionsRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.generation.DefaultValueGeneratorDefinitionsRequest`.
        
            .. code-block: java
            
             DefaultValueGeneratorDefinitionsRequest.builder()
                .parameters(Collection<cern.lsa.domain.settings.Parameter> | null) // nullable :meth:`~cern.lsa.domain.generation.ValueGeneratorDefinitionsRequest.getParameters`
                .parameterTypes(Collection<cern.lsa.domain.settings.ParameterType> | null) // nullable :meth:`~cern.lsa.domain.generation.ValueGeneratorDefinitionsRequest.getParameterTypes`
                .particleTransfers(Collection<cern.accsoft.commons.domain.particletransfers.ParticleTransfer> | null) // nullable :meth:`~cern.lsa.domain.generation.ValueGeneratorDefinitionsRequest.getParticleTransfers`
                .valueGeneratorNames(Collection<String> | null) // nullable :meth:`~cern.lsa.domain.generation.ValueGeneratorDefinitionsRequest.getValueGeneratorNames`
                .build();
             
        
            Returns:
                A new DefaultValueGeneratorDefinitionsRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(valueGeneratorDefinitionsRequest: ValueGeneratorDefinitionsRequest) -> 'DefaultValueGeneratorDefinitionsRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.generation.ValueGeneratorDefinitionsRequest` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.generation.ValueGeneratorDefinitionsRequest`): The instance to copy
        
            Returns:
                A copied immutable ValueGeneratorDefinitionsRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getParameterTypes(self) -> java.util.Collection[cern.lsa.domain.settings.ParameterType]: ...
    def getParameters(self) -> java.util.Collection[cern.lsa.domain.settings.Parameter]: ...
    def getParticleTransfers(self) -> java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]: ...
    def getValueGeneratorNames(self) -> java.util.Collection[str]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`parameters`, :code:`parameterTypes`, :code:`particleTransfers`,
            :code:`valueGeneratorNames`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ValueGeneratorDefinitionsRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withParameterTypes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.ParameterType], typing.Sequence[cern.lsa.domain.settings.ParameterType]]) -> 'DefaultValueGeneratorDefinitionsRequest': ...
    def withParameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'DefaultValueGeneratorDefinitionsRequest': ...
    def withParticleTransfers(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]]) -> 'DefaultValueGeneratorDefinitionsRequest': ...
    def withValueGeneratorNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DefaultValueGeneratorDefinitionsRequest': ...
    class Builder:
        def build(self) -> 'DefaultValueGeneratorDefinitionsRequest': ...
        def parameterTypes(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.ParameterType], typing.Sequence[cern.lsa.domain.settings.ParameterType]]) -> 'DefaultValueGeneratorDefinitionsRequest.Builder': ...
        def parameters(self, collection: typing.Union[java.util.Collection[cern.lsa.domain.settings.Parameter], typing.Sequence[cern.lsa.domain.settings.Parameter]]) -> 'DefaultValueGeneratorDefinitionsRequest.Builder': ...
        def particleTransfers(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.domain.particletransfers.ParticleTransfer], typing.Sequence[cern.accsoft.commons.domain.particletransfers.ParticleTransfer]]) -> 'DefaultValueGeneratorDefinitionsRequest.Builder': ...
        def valueGeneratorNames(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'DefaultValueGeneratorDefinitionsRequest.Builder': ...

class DefaultValueGeneratorInfo(ValueGeneratorInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultValueGeneratorInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.generation.ValueGeneratorInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.generation.ValueGeneratorInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultValueGeneratorInfo.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultValueGeneratorInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.generation.DefaultValueGeneratorInfo`.
        
            .. code-block: java
            
             DefaultValueGeneratorInfo.builder()
                .valueGeneratorName(String) // required :meth:`~cern.lsa.domain.generation.ValueGeneratorInfo.getValueGeneratorName`
                .addArgument|addAllArguments(String) // :meth:`~cern.lsa.domain.generation.ValueGeneratorInfo.getArguments` elements
                .build();
             
        
            Returns:
                A new DefaultValueGeneratorInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(valueGeneratorInfo: ValueGeneratorInfo) -> 'DefaultValueGeneratorInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.generation.ValueGeneratorInfo` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.generation.ValueGeneratorInfo`): The instance to copy
        
            Returns:
                A copied immutable ValueGeneratorInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getArguments(self) -> com.google.common.collect.ImmutableList[str]: ...
    def getValueGeneratorName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.generation.ValueGeneratorInfo.getValueGeneratorName`Â in
                interfaceÂ :class:`~cern.lsa.domain.generation.ValueGeneratorInfo`
        
            Returns:
                The value of the :code:`valueGeneratorName` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`valueGeneratorName`, :code:`arguments`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ValueGeneratorInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withArguments(self, iterable: java.lang.Iterable[str]) -> 'DefaultValueGeneratorInfo': ...
    @typing.overload
    def withArguments(self, stringArray: typing.List[str]) -> 'DefaultValueGeneratorInfo': ...
    def withValueGeneratorName(self, string: str) -> 'DefaultValueGeneratorInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.generation.ValueGeneratorInfo.getValueGeneratorName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for valueGeneratorName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllArguments(self, iterable: java.lang.Iterable[str]) -> 'DefaultValueGeneratorInfo.Builder': ...
        def addArgument(self, string: str) -> 'DefaultValueGeneratorInfo.Builder': ...
        def addArguments(self, stringArray: typing.List[str]) -> 'DefaultValueGeneratorInfo.Builder': ...
        def arguments(self, iterable: java.lang.Iterable[str]) -> 'DefaultValueGeneratorInfo.Builder': ...
        def build(self) -> 'DefaultValueGeneratorInfo': ...
        def valueGeneratorName(self, string: str) -> 'DefaultValueGeneratorInfo.Builder': ...

class DefaultValueGeneratorDefinition(AbstractValueGeneratorDefinition):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultValueGeneratorDefinition extends :class:`~cern.lsa.domain.generation.AbstractValueGeneratorDefinition`
    
        Immutable implementation of :class:`~cern.lsa.domain.generation.AbstractValueGeneratorDefinition`.
    
        Use the builder to create immutable instances: :code:`DefaultValueGeneratorDefinition.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultValueGeneratorDefinition.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.generation.DefaultValueGeneratorDefinition`.
        
            .. code-block: java
            
             DefaultValueGeneratorDefinition.builder()
                .parameter(cern.lsa.domain.settings.Parameter | null) // nullable :meth:`~cern.lsa.domain.generation.ValueGeneratorDefinition.getParameter`
                .parameterType(cern.lsa.domain.settings.ParameterType | null) // nullable :meth:`~cern.lsa.domain.generation.ValueGeneratorDefinition.getParameterType`
                .particleTransfer(cern.accsoft.commons.domain.particletransfers.ParticleTransfer | null) // nullable :meth:`~cern.lsa.domain.generation.ValueGeneratorDefinition.getParticleTransfer`
                .valueGeneratorName(String) // required :meth:`~cern.lsa.domain.generation.ValueGeneratorDefinition.getValueGeneratorName`
                .addArgument|addAllArguments(String) // :meth:`~cern.lsa.domain.generation.ValueGeneratorDefinition.getArguments` elements
                .build();
             
        
            Returns:
                A new DefaultValueGeneratorDefinition builder
        
        
        """
        ...
    @staticmethod
    def copyOf(abstractValueGeneratorDefinition: AbstractValueGeneratorDefinition) -> 'DefaultValueGeneratorDefinition':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.generation.AbstractValueGeneratorDefinition` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.generation.AbstractValueGeneratorDefinition`): The instance to copy
        
            Returns:
                A copied immutable ValueGeneratorDefinition instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getArguments(self) -> com.google.common.collect.ImmutableList[str]: ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def getParameterType(self) -> cern.lsa.domain.settings.ParameterType: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...
    def getValueGeneratorName(self) -> str:
        """
        
            Returns:
                The value of the :code:`valueGeneratorName` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`parameter`, :code:`parameterType`, :code:`particleTransfer`,
            :code:`valueGeneratorName`, :code:`arguments`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ValueGeneratorDefinition` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withArguments(self, iterable: java.lang.Iterable[str]) -> 'DefaultValueGeneratorDefinition': ...
    @typing.overload
    def withArguments(self, stringArray: typing.List[str]) -> 'DefaultValueGeneratorDefinition': ...
    def withParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultValueGeneratorDefinition': ...
    def withParameterType(self, parameterType: cern.lsa.domain.settings.ParameterType) -> 'DefaultValueGeneratorDefinition': ...
    def withParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultValueGeneratorDefinition': ...
    def withValueGeneratorName(self, string: str) -> 'DefaultValueGeneratorDefinition':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.generation.ValueGeneratorDefinition.getValueGeneratorName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for valueGeneratorName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def addAllArguments(self, iterable: java.lang.Iterable[str]) -> 'DefaultValueGeneratorDefinition.Builder': ...
        def addArgument(self, string: str) -> 'DefaultValueGeneratorDefinition.Builder': ...
        def addArguments(self, stringArray: typing.List[str]) -> 'DefaultValueGeneratorDefinition.Builder': ...
        def arguments(self, iterable: java.lang.Iterable[str]) -> 'DefaultValueGeneratorDefinition.Builder': ...
        def build(self) -> 'DefaultValueGeneratorDefinition': ...
        def parameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultValueGeneratorDefinition.Builder': ...
        def parameterType(self, parameterType: cern.lsa.domain.settings.ParameterType) -> 'DefaultValueGeneratorDefinition.Builder': ...
        def particleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultValueGeneratorDefinition.Builder': ...
        def valueGeneratorName(self, string: str) -> 'DefaultValueGeneratorDefinition.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.generation")``.

    AbstractValueGeneratorDefinition: typing.Type[AbstractValueGeneratorDefinition]
    DefaultValueGeneratorConfigInfo: typing.Type[DefaultValueGeneratorConfigInfo]
    DefaultValueGeneratorDefinition: typing.Type[DefaultValueGeneratorDefinition]
    DefaultValueGeneratorDefinitionsRequest: typing.Type[DefaultValueGeneratorDefinitionsRequest]
    DefaultValueGeneratorInfo: typing.Type[DefaultValueGeneratorInfo]
    ValueGeneratorConfigInfo: typing.Type[ValueGeneratorConfigInfo]
    ValueGeneratorDefinition: typing.Type[ValueGeneratorDefinition]
    ValueGeneratorDefinitionsRequest: typing.Type[ValueGeneratorDefinitionsRequest]
    ValueGeneratorInfo: typing.Type[ValueGeneratorInfo]
