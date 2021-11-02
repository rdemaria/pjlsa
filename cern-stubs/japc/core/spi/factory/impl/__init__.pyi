import cern.japc.core
import cern.japc.core.factory
import cern.japc.core.spi
import cern.japc.core.spi.cache
import cern.japc.core.spi.factory
import cern.japc.core.spi.group
import cern.japc.core.spi.subscription
import cern.japc.core.transaction
import cern.japc.value
import java.io
import java.util
import typing



class CompositeParameterCreatorImpl(cern.japc.core.spi.factory.CompositeParameterCreator):
    """
    public class CompositeParameterCreatorImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.factory.CompositeParameterCreator`
    
        This class creates GroupBasedParameters. The description of GroupBasedParameters (adapter class and components) is
        injected by Spring as a map of :class:`~cern.japc.core.spi.factory.impl.CompositeParameterStructure`.
    """
    def __init__(self, map: typing.Union[java.util.Map[str, 'CompositeParameterStructure'], typing.Mapping[str, 'CompositeParameterStructure']]): ...
    @typing.overload
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory, internalParameterCharacteristics: cern.japc.core.spi.factory.InternalParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    def isKnownCompositeParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> bool:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.spi.factory.CompositeParameterCreator.isKnownCompositeParameter`
            Checks whether the paramter name is known composite parameter name
        
            Specified by:
                :meth:`~cern.japc.core.spi.factory.CompositeParameterCreator.isKnownCompositeParameter`Â in
                interfaceÂ :class:`~cern.japc.core.spi.factory.CompositeParameterCreator`
        
            Parameters:
                parameterUrl (:class:`~cern.japc.core.spi.ParameterUrl`): the URL of the parameter
        
            Returns:
                true in case of known composite parameter name
        
        
        """
        ...

class CompositeParameterStructure:
    """
    public class CompositeParameterStructure extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class is a storage of a configuration of a single GroupBasedParameter.
    """
    @typing.overload
    def __init__(self, stringArray: typing.List[str], object: typing.Any): ...
    @typing.overload
    def __init__(self, stringArray: typing.List[str], object: typing.Any, groupSubscriptionStrategyFactory: cern.japc.core.spi.group.GroupSubscriptionStrategyFactory): ...
    def getAdapter(self) -> typing.Any:
        """
            Getter for adapter.
        
        
            Returns:
                adapter used for composing the result value.
        
        
        """
        ...
    def getComponents(self) -> typing.List[str]:
        """
            Getter for components.
        
        
            Returns:
                components parameters which the result value is composed from.
        
        
        """
        ...
    def getGroupingStrategyFactory(self) -> cern.japc.core.spi.group.GroupSubscriptionStrategyFactory:
        """
            Getter for grouping strategy class.
        
        
            Returns:
                class of grouping strategy.
        
        
        """
        ...
    def setGroupingStrategyFactory(self, groupSubscriptionStrategyFactory: cern.japc.core.spi.group.GroupSubscriptionStrategyFactory) -> None:
        """
            Setter for grouping strategy class name.
        
        
            Parameters:
                groupingStrategyFactory (:class:`~cern.japc.core.spi.group.GroupSubscriptionStrategyFactory`): a factory for grouping strategies (can be null)
        
        
        """
        ...

class ParameterCreatorConfigurationManager:
    """
    public interface ParameterCreatorConfigurationManager
    
        This interface deals with all the configurations of ParameterCreators. The goal of the implementations is to return a
        service configuration corresponding to a requested :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId`, taking
        into account that there could be multiple configurations for the same service (for different protocols, for example) and
        one or several can be marked as default.
    """
    def getConfig(self, parameterCreatorId: 'ParameterCreatorId') -> java.util.Properties:
        """
            Returns the config corresponding to passed :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId`.
            :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId` could contain protocol or not. If the protocol isn't
            specified and more than 1 configurations available then the first default configuration will be taken. If no default
            configurations provided then just the first configuration will be taken.
        
            Parameters:
                pcid (:class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId`): passed :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId`
        
            Returns:
                the config corresponding to passed :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId` or null if no
                configuration found.
        
        
        """
        ...

class ParameterCreatorId(java.io.Serializable):
    """
    public class ParameterCreatorId extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Identifier of parameter creator. Contains protocol and the name of a service.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, string2: str): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getProtocol(self) -> str:
        """
            Getter for protocol name.
        
            Returns:
                protocol name
        
        
        """
        ...
    def getServiceName(self) -> str:
        """
            Getter for service name.
        
            Returns:
                service name
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isProtocolDefined(self) -> bool:
        """
            Checks whether a protocol is defined.
        
            Returns:
                true if protocol is defined and false otherwise.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ParameterMetaFactory(cern.japc.core.factory.ParameterFactory, cern.japc.core.factory.ParameterMetaFactoryConstants):
    """
    public class ParameterMetaFactory extends :class:`~cern.japc.core.factory.ParameterFactory` implements :class:`~cern.japc.core.factory.ParameterMetaFactoryConstants`
    
        This is a meta-factory for parameters.
    
        This factory is able to create parameters of different services/types (RDAParameter, RemoteParameter, TGMParameter, etc)
        following some rules described in details on :class:`~cern.japc.core.spi.factory.impl`.
    
        By default to get the configuration for a service the factory reads CERN local repository (project japc-svc-lookup). But
        it is possible to provide an array of your own implementations of
        :class:`~cern.japc.core.spi.factory.ServiceConfigLookup` to the Factory using a constructor argument. In this case your
        implementations will be asked first (in the order they are in array) about the configuration of a service, and if none
        of your :class:`~cern.japc.core.spi.factory.ServiceConfigLookup` implementations can provide the information then the
        factory will go to the default one.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, serviceNameResolverArray: typing.List[cern.japc.core.factory.ServiceNameResolver], serviceConfigLookupArray: typing.List[cern.japc.core.spi.factory.ServiceConfigLookup]): ...
    @typing.overload
    def __init__(self, serviceNameResolverArray: typing.List[cern.japc.core.factory.ServiceNameResolver], serviceConfigLookupArray: typing.List[cern.japc.core.spi.factory.ServiceConfigLookup], string: str, string2: str): ...
    def registerInParameterFactory(self) -> None:
        """
            This method registers an instance of ParameterMetaFactory in the ParameterFactory map of instantiated parameter
            factories. This method should be used as post-creation method when ParameterMetaFactory is created inside Spring context
            to make sure that the instance returned from Spring is the same which returned via
            :meth:`~cern.japc.core.factory.ParameterFactory.newInstance` or
            :meth:`~cern.japc.core.factory.ParameterFactory.newInstance`.
        
        """
        ...
    def setCompositeParameterCreator(self, compositeParameterCreator: cern.japc.core.spi.factory.CompositeParameterCreator) -> None:
        """
        
            Parameters:
                compositeParameterCreator (:class:`~cern.japc.core.spi.factory.CompositeParameterCreator`): 
        
        """
        ...
    def setWildcardSelectorResolver(self, wildcardSelectorResolver: cern.japc.core.spi.subscription.WildcardSelectorResolver) -> None:
        """
        
            Parameters:
                wildcardSelectorResolver (:class:`~cern.japc.core.spi.subscription.WildcardSelectorResolver`): 
        
        """
        ...

class ParameterCreatorConfigurationManagerImpl(ParameterCreatorConfigurationManager, cern.japc.core.spi.cache.JapcCache):
    """
    public class ParameterCreatorConfigurationManagerImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorConfigurationManager`, :class:`~cern.japc.core.spi.cache.JapcCache`
    
        Default implementation of :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorConfigurationManager`.
    
        This class deals with all the configurations of ParameterCreators. The goal of this class is to return a configuration
        corresponding to a requested :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId`, taking into account that
        fact, that any :class:`~cern.japc.core.spi.factory.ServiceConfigLookup` returns the whole set of configurations (for
        different protocols, for example) for the certain service. One of this configurations is really needed, but others
        should be nevertheless stored locally to not search for them again when/if they will be needed.
    """
    def __init__(self, serviceConfigLookupArray: typing.List[cern.japc.core.spi.factory.ServiceConfigLookup]): ...
    def clearAll(self) -> None: ...
    def getConfig(self, parameterCreatorId: ParameterCreatorId) -> java.util.Properties:
        """
            Description copied from
            interface:Â :meth:`~cern.japc.core.spi.factory.impl.ParameterCreatorConfigurationManager.getConfig`
            Returns the config corresponding to passed :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId`.
            :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId` could contain protocol or not. If the protocol isn't
            specified and more than 1 configurations available then the first default configuration will be taken. If no default
            configurations provided then just the first configuration will be taken.
        
            Specified by:
                :meth:`~cern.japc.core.spi.factory.impl.ParameterCreatorConfigurationManager.getConfig`Â in
                interfaceÂ :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorConfigurationManager`
        
            Parameters:
                pcid (:class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId`): passed :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId`
        
            Returns:
                the config corresponding to passed :class:`~cern.japc.core.spi.factory.impl.ParameterCreatorId` or null if no
                configuration found.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.factory.impl")``.

    CompositeParameterCreatorImpl: typing.Type[CompositeParameterCreatorImpl]
    CompositeParameterStructure: typing.Type[CompositeParameterStructure]
    ParameterCreatorConfigurationManager: typing.Type[ParameterCreatorConfigurationManager]
    ParameterCreatorConfigurationManagerImpl: typing.Type[ParameterCreatorConfigurationManagerImpl]
    ParameterCreatorId: typing.Type[ParameterCreatorId]
    ParameterMetaFactory: typing.Type[ParameterMetaFactory]
