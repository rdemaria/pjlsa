import java.io
import java.lang
import java.util
import typing



class MakeRuleClassInfo:
    """
    @Immutable public interface MakeRuleClassInfo
    
        Holds information about an implementation of a makerule
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleClassInfo.Builder':
        """
            Creates builder to build :class:`~cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleClassInfo`
        
            Returns:
                the builder
        
        
        """
        ...
    def getClassName(self) -> str:
        """
        
            Returns:
                the full class name of the makerule
        
        
        """
        ...
    def getProductName(self) -> str:
        """
        
            Returns:
                the name of the product containing the makerule
        
        
        """
        ...
    def getVersion(self) -> str:
        """
        
            Returns:
                the version of the package containing the class
        
        
        """
        ...

class MakeRuleConfigInfo:
    """
    @Immutable public interface MakeRuleConfigInfo
    
        Object containing informations defining a makerule
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigInfo.Builder':
        """
            Creates builder to build :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo`
        
            Returns:
                the builder
        
        
        """
        ...
    def getMakeRuleConfigStatus(self) -> 'MakeRuleConfigInfo.MakeRuleConfigStatus':
        """
        
            Returns:
                the status of the makerule's configuration
        
        
        """
        ...
    def getMakeRuleInfo(self) -> java.util.Optional['MakeRuleInfo']: ...
    class MakeRuleConfigStatus(java.lang.Enum['MakeRuleConfigInfo.MakeRuleConfigStatus']):
        FULLY_CONFIGURED: typing.ClassVar['MakeRuleConfigInfo.MakeRuleConfigStatus'] = ...
        NOT_CONFIGURED: typing.ClassVar['MakeRuleConfigInfo.MakeRuleConfigStatus'] = ...
        BEAN_MISSING: typing.ClassVar['MakeRuleConfigInfo.MakeRuleConfigStatus'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'MakeRuleConfigInfo.MakeRuleConfigStatus': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['MakeRuleConfigInfo.MakeRuleConfigStatus']: ...

class MakeRuleInfo:
    """
    @Immutable public interface MakeRuleInfo
    
        Object containing informations defining a makerule
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleInfo.Builder':
        """
            Creates builder to build :class:`~cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleInfo`
        
            Returns:
                the builder
        
        
        """
        ...
    def getMakeRuleClassInfo(self) -> java.util.Optional[MakeRuleClassInfo]: ...
    def getMakeRuleName(self) -> str: ...

class DefaultMakeRuleClassInfo(MakeRuleClassInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleClassInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleClassInfo.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleClassInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleClassInfo`.
        
            .. code-block: java
            
             DefaultMakeRuleClassInfo.builder()
                .className(String) // required :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo.getClassName`
                .productName(String) // required :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo.getProductName`
                .version(String) // required :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo.getVersion`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleClassInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleClassInfo: MakeRuleClassInfo) -> 'DefaultMakeRuleClassInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleClassInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getClassName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo.getClassName`Â in
                interfaceÂ :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo`
        
            Returns:
                the full class name of the makerule
        
        
        """
        ...
    def getProductName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo.getProductName`Â in
                interfaceÂ :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo`
        
            Returns:
                the name of the product containing the makerule
        
        
        """
        ...
    def getVersion(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo.getVersion`Â in
                interfaceÂ :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo`
        
            Returns:
                the version of the package containing the class
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`className`, :code:`productName`, :code:`version`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`MakeRuleClassInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withClassName(self, string: str) -> 'DefaultMakeRuleClassInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo.getClassName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for className
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withProductName(self, string: str) -> 'DefaultMakeRuleClassInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo.getProductName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for productName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withVersion(self, string: str) -> 'DefaultMakeRuleClassInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo.getVersion` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for version
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleClassInfo': ...
        def className(self, string: str) -> 'DefaultMakeRuleClassInfo.Builder': ...
        def productName(self, string: str) -> 'DefaultMakeRuleClassInfo.Builder': ...
        def version(self, string: str) -> 'DefaultMakeRuleClassInfo.Builder': ...

class DefaultMakeRuleConfigInfo(MakeRuleConfigInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleConfigInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleConfigInfo.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleConfigInfo`.
        
            .. code-block: java
            
             DefaultMakeRuleConfigInfo.builder()
                .makeRuleConfigStatus(cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo.MakeRuleConfigStatus) // required :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo.getMakeRuleConfigStatus`
                .makeRuleInfo(cern.lsa.domain.trim.rules.makerule.MakeRuleInfo) // optional :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo.getMakeRuleInfo`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleConfigInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleConfigInfo: MakeRuleConfigInfo) -> 'DefaultMakeRuleConfigInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleConfigInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMakeRuleConfigStatus(self) -> MakeRuleConfigInfo.MakeRuleConfigStatus:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo.getMakeRuleConfigStatus`Â in
                interfaceÂ :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo`
        
            Returns:
                the status of the makerule's configuration
        
        
        """
        ...
    def getMakeRuleInfo(self) -> java.util.Optional[MakeRuleInfo]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`makeRuleConfigStatus`, :code:`makeRuleInfo`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`MakeRuleConfigInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withMakeRuleConfigStatus(self, makeRuleConfigStatus: MakeRuleConfigInfo.MakeRuleConfigStatus) -> 'DefaultMakeRuleConfigInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo.getMakeRuleConfigStatus` attribute. A value equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo.MakeRuleConfigStatus`): A new value for makeRuleConfigStatus
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withMakeRuleInfo(self, makeRuleInfo: MakeRuleInfo) -> 'DefaultMakeRuleConfigInfo':
        """
            Copy the current immutable object by setting a *present* value for the optional
            :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo.getMakeRuleInfo` attribute.
        
            Parameters:
                value (:class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo`): The value for makeRuleInfo
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleConfigInfo` withMakeRuleInfo (`Optional <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Optional.html?is-external=true>`<? extends :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo`> optional)
        
            Copy the current immutable object by setting an optional value for the
            :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo.getMakeRuleInfo` attribute. A shallow reference equality
            check is used on unboxed optional value to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                optional (`Optional <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Optional.html?is-external=true>`<? extends :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo`> optional): A value for makeRuleInfo
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withMakeRuleInfo(self, optional: java.util.Optional[MakeRuleInfo]) -> 'DefaultMakeRuleConfigInfo': ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleConfigInfo': ...
        def makeRuleConfigStatus(self, makeRuleConfigStatus: MakeRuleConfigInfo.MakeRuleConfigStatus) -> 'DefaultMakeRuleConfigInfo.Builder': ...
        @typing.overload
        def makeRuleInfo(self, makeRuleInfo: MakeRuleInfo) -> 'DefaultMakeRuleConfigInfo.Builder': ...
        @typing.overload
        def makeRuleInfo(self, optional: java.util.Optional[MakeRuleInfo]) -> 'DefaultMakeRuleConfigInfo.Builder': ...

class DefaultMakeRuleInfo(MakeRuleInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultMakeRuleInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultMakeRuleInfo.builder()`. Use the static factory method to
        create immutable instances: :code:`DefaultMakeRuleInfo.of()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleInfo`.
        
            .. code-block: java
            
             DefaultMakeRuleInfo.builder()
                .makeRuleName(String) // required :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo.getMakeRuleName`
                .makeRuleClassInfo(cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo) // optional :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo.getMakeRuleClassInfo`
                .build();
             
        
            Returns:
                A new DefaultMakeRuleInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(makeRuleInfo: MakeRuleInfo) -> 'DefaultMakeRuleInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo`): The instance to copy
        
            Returns:
                A copied immutable MakeRuleInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMakeRuleClassInfo(self) -> java.util.Optional[MakeRuleClassInfo]: ...
    def getMakeRuleName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo.getMakeRuleName`Â in
                interfaceÂ :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo`
        
            Returns:
                the makerule name in the DB
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`makeRuleName`, :code:`makeRuleClassInfo`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    @staticmethod
    def of(string: str) -> 'DefaultMakeRuleInfo':
        """
            Construct a new immutable :code:`MakeRuleInfo` instance.
        
            Parameters:
                makeRuleName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The value for the :code:`makeRuleName` attribute
        
            Returns:
                An immutable MakeRuleInfo instance
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`MakeRuleInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withMakeRuleClassInfo(self, makeRuleClassInfo: MakeRuleClassInfo) -> 'DefaultMakeRuleInfo':
        """
            Copy the current immutable object by setting a *present* value for the optional
            :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo.getMakeRuleClassInfo` attribute.
        
            Parameters:
                value (:class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo`): The value for makeRuleClassInfo
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleInfo` withMakeRuleClassInfo (`Optional <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Optional.html?is-external=true>`<? extends :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo`> optional)
        
            Copy the current immutable object by setting an optional value for the
            :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo.getMakeRuleClassInfo` attribute. A shallow reference equality
            check is used on unboxed optional value to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                optional (`Optional <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Optional.html?is-external=true>`<? extends :class:`~cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo`> optional): A value for makeRuleClassInfo
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withMakeRuleClassInfo(self, optional: java.util.Optional[MakeRuleClassInfo]) -> 'DefaultMakeRuleInfo': ...
    def withMakeRuleName(self, string: str) -> 'DefaultMakeRuleInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.trim.rules.makerule.MakeRuleInfo.getMakeRuleName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for makeRuleName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleInfo': ...
        @typing.overload
        def makeRuleClassInfo(self, makeRuleClassInfo: MakeRuleClassInfo) -> 'DefaultMakeRuleInfo.Builder': ...
        @typing.overload
        def makeRuleClassInfo(self, optional: java.util.Optional[MakeRuleClassInfo]) -> 'DefaultMakeRuleInfo.Builder': ...
        def makeRuleName(self, string: str) -> 'DefaultMakeRuleInfo.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.trim.rules.makerule")``.

    DefaultMakeRuleClassInfo: typing.Type[DefaultMakeRuleClassInfo]
    DefaultMakeRuleConfigInfo: typing.Type[DefaultMakeRuleConfigInfo]
    DefaultMakeRuleInfo: typing.Type[DefaultMakeRuleInfo]
    MakeRuleClassInfo: typing.Type[MakeRuleClassInfo]
    MakeRuleConfigInfo: typing.Type[MakeRuleConfigInfo]
    MakeRuleInfo: typing.Type[MakeRuleInfo]
