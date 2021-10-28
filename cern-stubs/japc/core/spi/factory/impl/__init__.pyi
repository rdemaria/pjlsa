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
    Java class 'cern.japc.core.spi.factory.impl.CompositeParameterCreatorImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.factory.CompositeParameterCreator
    
      Constructors:
        * CompositeParameterCreatorImpl(java.util.Map)
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, 'CompositeParameterStructure'], typing.Mapping[str, 'CompositeParameterStructure']]): ...
    @typing.overload
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory, internalParameterCharacteristics: cern.japc.core.spi.factory.InternalParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    def isKnownCompositeParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> bool: ...

class CompositeParameterStructure:
    """
    Java class 'cern.japc.core.spi.factory.impl.CompositeParameterStructure'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * CompositeParameterStructure(java.lang.String[], java.lang.Object)
        * CompositeParameterStructure(java.lang.String[], java.lang.Object, cern.japc.core.spi.group.GroupSubscriptionStrategyFactory)
    
    """
    @typing.overload
    def __init__(self, stringArray: typing.List[str], object: typing.Any): ...
    @typing.overload
    def __init__(self, stringArray: typing.List[str], object: typing.Any, groupSubscriptionStrategyFactory: cern.japc.core.spi.group.GroupSubscriptionStrategyFactory): ...
    def getAdapter(self) -> typing.Any: ...
    def getComponents(self) -> typing.List[str]: ...
    def getGroupingStrategyFactory(self) -> cern.japc.core.spi.group.GroupSubscriptionStrategyFactory: ...
    def setGroupingStrategyFactory(self, groupSubscriptionStrategyFactory: cern.japc.core.spi.group.GroupSubscriptionStrategyFactory) -> None: ...

class ParameterCreatorConfigurationManager:
    """
    Java class 'cern.japc.core.spi.factory.impl.ParameterCreatorConfigurationManager'
    
    """
    def getConfig(self, parameterCreatorId: 'ParameterCreatorId') -> java.util.Properties: ...

class ParameterCreatorId(java.io.Serializable):
    """
    Java class 'cern.japc.core.spi.factory.impl.ParameterCreatorId'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * ParameterCreatorId(java.lang.String, java.lang.String)
    
    """
    def __init__(self, string: str, string2: str): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getProtocol(self) -> str: ...
    def getServiceName(self) -> str: ...
    def hashCode(self) -> int: ...
    def isProtocolDefined(self) -> bool: ...
    def toString(self) -> str: ...

class ParameterMetaFactory(cern.japc.core.factory.ParameterFactory, cern.japc.core.factory.ParameterMetaFactoryConstants):
    """
    Java class 'cern.japc.core.spi.factory.impl.ParameterMetaFactory'
    
        Extends:
            cern.japc.core.factory.ParameterFactory
    
        Interfaces:
            cern.japc.core.factory.ParameterMetaFactoryConstants
    
      Constructors:
        * ParameterMetaFactory(cern.japc.core.factory.ServiceNameResolver[], cern.japc.core.spi.factory.ServiceConfigLookup[], java.lang.String, java.lang.String)
        * ParameterMetaFactory(cern.japc.core.factory.ServiceNameResolver[], cern.japc.core.spi.factory.ServiceConfigLookup[])
        * ParameterMetaFactory()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, serviceNameResolverArray: typing.List[cern.japc.core.factory.ServiceNameResolver], serviceConfigLookupArray: typing.List[cern.japc.core.spi.factory.ServiceConfigLookup]): ...
    @typing.overload
    def __init__(self, serviceNameResolverArray: typing.List[cern.japc.core.factory.ServiceNameResolver], serviceConfigLookupArray: typing.List[cern.japc.core.spi.factory.ServiceConfigLookup], string: str, string2: str): ...
    def registerInParameterFactory(self) -> None: ...
    def setCompositeParameterCreator(self, compositeParameterCreator: cern.japc.core.spi.factory.CompositeParameterCreator) -> None: ...
    def setWildcardSelectorResolver(self, wildcardSelectorResolver: cern.japc.core.spi.subscription.WildcardSelectorResolver) -> None: ...

class ParameterCreatorConfigurationManagerImpl(ParameterCreatorConfigurationManager, cern.japc.core.spi.cache.JapcCache):
    """
    Java class 'cern.japc.core.spi.factory.impl.ParameterCreatorConfigurationManagerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.factory.impl.ParameterCreatorConfigurationM
            anager, cern.japc.core.spi.cache.JapcCache
    
      Constructors:
        * ParameterCreatorConfigurationManagerImpl(cern.japc.core.spi.factory.ServiceConfigLookup[])
    
    """
    def __init__(self, serviceConfigLookupArray: typing.List[cern.japc.core.spi.factory.ServiceConfigLookup]): ...
    def clearAll(self) -> None: ...
    def getConfig(self, parameterCreatorId: ParameterCreatorId) -> java.util.Properties: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.factory.impl")``.

    CompositeParameterCreatorImpl: typing.Type[CompositeParameterCreatorImpl]
    CompositeParameterStructure: typing.Type[CompositeParameterStructure]
    ParameterCreatorConfigurationManager: typing.Type[ParameterCreatorConfigurationManager]
    ParameterCreatorConfigurationManagerImpl: typing.Type[ParameterCreatorConfigurationManagerImpl]
    ParameterCreatorId: typing.Type[ParameterCreatorId]
    ParameterMetaFactory: typing.Type[ParameterMetaFactory]
