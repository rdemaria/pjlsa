import cern.accsoft.commons.domain.particletransfers
import cern.lsa.domain.settings
import java.io
import typing



class ParameterTypeRelation:
    """
    @Immutable public interface ParameterTypeRelation
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeRelation.Builder': ...
    def getDependentParameterType(self) -> cern.lsa.domain.settings.ParameterType: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...
    def getSourceParameterType(self) -> cern.lsa.domain.settings.ParameterType: ...

class ParameterTypeRelationInfo:
    """
    @Immutable public interface ParameterTypeRelationInfo
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeRelationInfo.Builder': ...
    def getMakeRuleName(self) -> str: ...
    def getParameterTypeRelation(self) -> ParameterTypeRelation: ...

class ParameterTypeRelationInfosRequest:
    """
    @Immutable public interface ParameterTypeRelationInfosRequest
    """
    @staticmethod
    def all() -> 'ParameterTypeRelationInfosRequest': ...
    @staticmethod
    def builder() -> 'DefaultParameterTypeRelationInfosRequest.Builder': ...
    @staticmethod
    def byMakeRuleName(string: str) -> 'ParameterTypeRelationInfosRequest': ...
    @staticmethod
    def byParticleTransfer(particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'ParameterTypeRelationInfosRequest': ...
    def getMakeRuleName(self) -> str: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...

class DefaultParameterTypeRelation(ParameterTypeRelation, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTypeRelation extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTypeRelation.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeRelation.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.parameter.type.relation.DefaultParameterTypeRelation`.
        
            .. code-block: java
            
             DefaultParameterTypeRelation.builder()
                .sourceParameterType(cern.lsa.domain.settings.ParameterType) // required :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation.getSourceParameterType`
                .dependentParameterType(cern.lsa.domain.settings.ParameterType) // required :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation.getDependentParameterType`
                .particleTransfer(cern.accsoft.commons.domain.particletransfers.ParticleTransfer) // required :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation.getParticleTransfer`
                .build();
             
        
            Returns:
                A new DefaultParameterTypeRelation builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTypeRelation: ParameterTypeRelation) -> 'DefaultParameterTypeRelation':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation` value.
            Uses accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is
            returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation`): The instance to copy
        
            Returns:
                A copied immutable ParameterTypeRelation instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDependentParameterType(self) -> cern.lsa.domain.settings.ParameterType:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation.getDependentParameterType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation`
        
            Returns:
                The value of the :code:`dependentParameterType` attribute
        
        
        """
        ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation.getParticleTransfer`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation`
        
            Returns:
                The value of the :code:`particleTransfer` attribute
        
        
        """
        ...
    def getSourceParameterType(self) -> cern.lsa.domain.settings.ParameterType:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation.getSourceParameterType`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation`
        
            Returns:
                The value of the :code:`sourceParameterType` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`sourceParameterType`, :code:`dependentParameterType`,
            :code:`particleTransfer`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTypeRelation` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDependentParameterType(self, parameterType: cern.lsa.domain.settings.ParameterType) -> 'DefaultParameterTypeRelation':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation.getDependentParameterType` attribute. A
            shallow reference equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.ParameterType`): A new value for dependentParameterType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultParameterTypeRelation':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation.getParticleTransfer` attribute. A shallow
            reference equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (cern.accsoft.commons.domain.particletransfers.ParticleTransfer): A new value for particleTransfer
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withSourceParameterType(self, parameterType: cern.lsa.domain.settings.ParameterType) -> 'DefaultParameterTypeRelation':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation.getSourceParameterType` attribute. A
            shallow reference equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.ParameterType`): A new value for sourceParameterType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultParameterTypeRelation': ...
        def dependentParameterType(self, parameterType: cern.lsa.domain.settings.ParameterType) -> 'DefaultParameterTypeRelation.Builder': ...
        def particleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultParameterTypeRelation.Builder': ...
        def sourceParameterType(self, parameterType: cern.lsa.domain.settings.ParameterType) -> 'DefaultParameterTypeRelation.Builder': ...

class DefaultParameterTypeRelationInfo(ParameterTypeRelationInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTypeRelationInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTypeRelationInfo.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeRelationInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.parameter.type.relation.DefaultParameterTypeRelationInfo`.
        
            .. code-block: java
            
             DefaultParameterTypeRelationInfo.builder()
                .parameterTypeRelation(cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation) // required :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo.getParameterTypeRelation`
                .makeRuleName(String) // required :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo.getMakeRuleName`
                .build();
             
        
            Returns:
                A new DefaultParameterTypeRelationInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTypeRelationInfo: ParameterTypeRelationInfo) -> 'DefaultParameterTypeRelationInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo`
            value. Uses accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is
            returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo`): The instance to copy
        
            Returns:
                A copied immutable ParameterTypeRelationInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMakeRuleName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo.getMakeRuleName`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo`
        
            Returns:
                The value of the :code:`makeRuleName` attribute
        
        
        """
        ...
    def getParameterTypeRelation(self) -> ParameterTypeRelation:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo.getParameterTypeRelation`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo`
        
            Returns:
                The value of the :code:`parameterTypeRelation` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`parameterTypeRelation`, :code:`makeRuleName`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTypeRelationInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withMakeRuleName(self, string: str) -> 'DefaultParameterTypeRelationInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo.getMakeRuleName` attribute. An equals
            check used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for makeRuleName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParameterTypeRelation(self, parameterTypeRelation: ParameterTypeRelation) -> 'DefaultParameterTypeRelationInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfo.getParameterTypeRelation` attribute.
            A shallow reference equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelation`): A new value for parameterTypeRelation
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultParameterTypeRelationInfo': ...
        def makeRuleName(self, string: str) -> 'DefaultParameterTypeRelationInfo.Builder': ...
        def parameterTypeRelation(self, parameterTypeRelation: ParameterTypeRelation) -> 'DefaultParameterTypeRelationInfo.Builder': ...

class DefaultParameterTypeRelationInfosRequest(ParameterTypeRelationInfosRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterTypeRelationInfosRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfosRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of
        :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfosRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterTypeRelationInfosRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultParameterTypeRelationInfosRequest.Builder':
        """
            Creates a builder for
            :class:`~cern.lsa.domain.settings.parameter.type.relation.DefaultParameterTypeRelationInfosRequest`.
        
            .. code-block: java
            
             DefaultParameterTypeRelationInfosRequest.builder()
                .particleTransfer(cern.accsoft.commons.domain.particletransfers.ParticleTransfer | null) // nullable :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfosRequest.getParticleTransfer`
                .makeRuleName(String | null) // nullable :meth:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfosRequest.getMakeRuleName`
                .build();
             
        
            Returns:
                A new DefaultParameterTypeRelationInfosRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterTypeRelationInfosRequest: ParameterTypeRelationInfosRequest) -> 'DefaultParameterTypeRelationInfosRequest':
        """
            Creates an immutable copy of a
            :class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfosRequest` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.parameter.type.relation.ParameterTypeRelationInfosRequest`): The instance to copy
        
            Returns:
                A copied immutable ParameterTypeRelationInfosRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMakeRuleName(self) -> str: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`particleTransfer`, :code:`makeRuleName`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterTypeRelationInfosRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withMakeRuleName(self, string: str) -> 'DefaultParameterTypeRelationInfosRequest': ...
    def withParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultParameterTypeRelationInfosRequest': ...
    class Builder:
        def build(self) -> 'DefaultParameterTypeRelationInfosRequest': ...
        def makeRuleName(self, string: str) -> 'DefaultParameterTypeRelationInfosRequest.Builder': ...
        def particleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultParameterTypeRelationInfosRequest.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings.parameter.type.relation")``.

    DefaultParameterTypeRelation: typing.Type[DefaultParameterTypeRelation]
    DefaultParameterTypeRelationInfo: typing.Type[DefaultParameterTypeRelationInfo]
    DefaultParameterTypeRelationInfosRequest: typing.Type[DefaultParameterTypeRelationInfosRequest]
    ParameterTypeRelation: typing.Type[ParameterTypeRelation]
    ParameterTypeRelationInfo: typing.Type[ParameterTypeRelationInfo]
    ParameterTypeRelationInfosRequest: typing.Type[ParameterTypeRelationInfosRequest]
