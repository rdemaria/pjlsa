import cern.accsoft.commons.domain.particletransfers
import cern.lsa.domain.settings
import java.io
import typing



class ParameterRelation:
    """
    @Immutable public interface ParameterRelation
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelation.Builder': ...
    def getDependentParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def getHierarchy(self) -> str: ...
    def getSourceParameter(self) -> cern.lsa.domain.settings.Parameter: ...

class ParameterRelationInfo:
    """
    @Immutable public interface ParameterRelationInfo
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelationInfo.Builder': ...
    def getParameterRelation(self) -> ParameterRelation: ...
    def getParameterSpecificMakeRuleName(self) -> str: ...

class ParameterRelationInfosRequest:
    """
    @Immutable public interface ParameterRelationInfosRequest
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelationInfosRequest.Builder': ...
    @staticmethod
    def byParticleTransfer(particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'ParameterRelationInfosRequest': ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...

class DefaultParameterRelation(ParameterRelation, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterRelation extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterRelation.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelation.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.parameter.relation.DefaultParameterRelation`.
        
            .. code-block: java
            
             DefaultParameterRelation.builder()
                .sourceParameter(cern.lsa.domain.settings.Parameter) // required :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation.getSourceParameter`
                .dependentParameter(cern.lsa.domain.settings.Parameter) // required :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation.getDependentParameter`
                .hierarchy(String) // optional :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation.getHierarchy`
                .build();
             
        
            Returns:
                A new DefaultParameterRelation builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterRelation: ParameterRelation) -> 'DefaultParameterRelation':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation`): The instance to copy
        
            Returns:
                A copied immutable ParameterRelation instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDependentParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation.getDependentParameter`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation`
        
            Returns:
                The value of the :code:`dependentParameter` attribute
        
        
        """
        ...
    def getHierarchy(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation.getHierarchy`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation`
        
            Returns:
                The value of the :code:`hierarchy` attribute
        
        
        """
        ...
    def getSourceParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation.getSourceParameter`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation`
        
            Returns:
                The value of the :code:`sourceParameter` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`sourceParameter`, :code:`dependentParameter`, :code:`hierarchy`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterRelation` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDependentParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation.getDependentParameter` attribute. A shallow
            reference equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.Parameter`): A new value for dependentParameter
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withHierarchy(self, string: str) -> 'DefaultParameterRelation':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation.getHierarchy` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for hierarchy
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withSourceParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation.getSourceParameter` attribute. A shallow reference
            equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.Parameter`): A new value for sourceParameter
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultParameterRelation': ...
        def dependentParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation.Builder': ...
        def hierarchy(self, string: str) -> 'DefaultParameterRelation.Builder': ...
        def sourceParameter(self, parameter: cern.lsa.domain.settings.Parameter) -> 'DefaultParameterRelation.Builder': ...

class DefaultParameterRelationInfo(ParameterRelationInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterRelationInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterRelationInfo.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelationInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.parameter.relation.DefaultParameterRelationInfo`.
        
            .. code-block: java
            
             DefaultParameterRelationInfo.builder()
                .parameterRelation(cern.lsa.domain.settings.parameter.relation.ParameterRelation) // required :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo.getParameterRelation`
                .parameterSpecificMakeRuleName(String | null) // nullable :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo.getParameterSpecificMakeRuleName`
                .build();
             
        
            Returns:
                A new DefaultParameterRelationInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterRelationInfo: ParameterRelationInfo) -> 'DefaultParameterRelationInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo`): The instance to copy
        
            Returns:
                A copied immutable ParameterRelationInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getParameterRelation(self) -> ParameterRelation:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo.getParameterRelation`Â in
                interfaceÂ :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo`
        
            Returns:
                The value of the :code:`parameterRelation` attribute
        
        
        """
        ...
    def getParameterSpecificMakeRuleName(self) -> str: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`parameterRelation`, :code:`parameterSpecificMakeRuleName`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterRelationInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withParameterRelation(self, parameterRelation: ParameterRelation) -> 'DefaultParameterRelationInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfo.getParameterRelation` attribute. A shallow
            reference equality check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelation`): A new value for parameterRelation
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParameterSpecificMakeRuleName(self, string: str) -> 'DefaultParameterRelationInfo': ...
    class Builder:
        def build(self) -> 'DefaultParameterRelationInfo': ...
        def parameterRelation(self, parameterRelation: ParameterRelation) -> 'DefaultParameterRelationInfo.Builder': ...
        def parameterSpecificMakeRuleName(self, string: str) -> 'DefaultParameterRelationInfo.Builder': ...

class DefaultParameterRelationInfosRequest(ParameterRelationInfosRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterRelationInfosRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfosRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfosRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterRelationInfosRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultParameterRelationInfosRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.settings.parameter.relation.DefaultParameterRelationInfosRequest`.
        
            .. code-block: java
            
             DefaultParameterRelationInfosRequest.builder()
                .particleTransfer(cern.accsoft.commons.domain.particletransfers.ParticleTransfer | null) // nullable :meth:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfosRequest.getParticleTransfer`
                .build();
             
        
            Returns:
                A new DefaultParameterRelationInfosRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterRelationInfosRequest: ParameterRelationInfosRequest) -> 'DefaultParameterRelationInfosRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfosRequest`
            value. Uses accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is
            returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.settings.parameter.relation.ParameterRelationInfosRequest`): The instance to copy
        
            Returns:
                A copied immutable ParameterRelationInfosRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getParticleTransfer(self) -> cern.accsoft.commons.domain.particletransfers.ParticleTransfer: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`particleTransfer`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterRelationInfosRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withParticleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultParameterRelationInfosRequest': ...
    class Builder:
        def build(self) -> 'DefaultParameterRelationInfosRequest': ...
        def particleTransfer(self, particleTransfer: cern.accsoft.commons.domain.particletransfers.ParticleTransfer) -> 'DefaultParameterRelationInfosRequest.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.settings.parameter.relation")``.

    DefaultParameterRelation: typing.Type[DefaultParameterRelation]
    DefaultParameterRelationInfo: typing.Type[DefaultParameterRelationInfo]
    DefaultParameterRelationInfosRequest: typing.Type[DefaultParameterRelationInfosRequest]
    ParameterRelation: typing.Type[ParameterRelation]
    ParameterRelationInfo: typing.Type[ParameterRelationInfo]
    ParameterRelationInfosRequest: typing.Type[ParameterRelationInfosRequest]
