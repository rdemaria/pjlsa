import cern.japc.core
import cern.japc.core.factory
import cern.japc.core.spi
import cern.japc.core.spi.factory.impl
import cern.japc.core.transaction
import cern.japc.value
import java.io
import java.util
import typing



class InternalParameterCharacteristics(cern.japc.core.factory.ParameterCharacteristicsImpl, cern.japc.core.ParameterCharacteristics, java.io.Serializable):
    """
    public class InternalParameterCharacteristics extends :class:`~cern.japc.core.factory.ParameterCharacteristicsImpl` implements :class:`~cern.japc.core.ParameterCharacteristics`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Helper class to keep track of parameter creation process. Must be used in a single thread.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, parameterCharacteristics: cern.japc.core.ParameterCharacteristics): ...
    def decreaseCreatingCompositeParameter(self) -> None:
        """
            Decreases the hierarchical level of composite parameter being created. Level of 0 means that ParameterFactory doesn't
            create a composite parameter at the moment.
        
        """
        ...
    def increaseCreatingCompositeParameter(self) -> None:
        """
            Increases the hierarchical level of composite parameter being created.
        
        """
        ...
    def isCreatingCompositeParameter(self) -> bool:
        """
            Returns true if composite parameter is being created and false otherwise.
        
            Returns:
                true if composite parameter is being created and false otherwise.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.japc.core.factory.ParameterCharacteristicsImpl.toString`Â in
                classÂ :class:`~cern.japc.core.factory.ParameterCharacteristicsImpl`
        
        
        """
        ...

class ParameterCreator:
    """
    public interface ParameterCreator
    
        The interface of a creator of different types of JAPC parameters
    """
    SERVICE_NAME_PROPERTY: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SERVICE_NAME_PROPERTY
    
        JAPC service configuration field to specify JAPC service name.
    
        Possible values: alpha-numeric strings with underscores.
    
        The information in the service configuration can NOT be overwritten.
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROTOCOL_PROPERTY: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROTOCOL_PROPERTY
    
        JAPC service configuration field to specify protocol for RPC.
    
        Possible values: either the same as service name or "no", "rmi", "http", "jms" (not used).
    
        The information in the service configuration can NOT be overwritten.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CREATOR_CLASS_PROPERTY: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CREATOR_CLASS_PROPERTY
    
        JAPC service configuration field to specify :class:`~cern.japc.core.spi.factory.ParameterCreator` implementation class.
    
        Possible values: fully qualified class name of :class:`~cern.japc.core.spi.factory.ParameterCreator` implementation.
    
        The information in the service configuration can NOT be overwritten.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_PROPERTY: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_PROPERTY
    
        JAPC service configuration field to specify if this service configuration is default in case when several service
        configurations (for different protocols) are available.
    
        Possible values: :code:`true`, :code:`false` (default :code:`false`).
    
        The information in the service configuration can NOT be overwritten.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory) -> cern.japc.core.transaction.TransactionalParameter: ...

class ServiceConfigLookup:
    """
    public interface ServiceConfigLookup
    
        This interface describes the functionality of a class which provides configurations for services.
    """
    def getConfig(self, string: str) -> typing.List[java.util.Properties]:
        """
            Returns an array of configurations for a service with the given name. Different configurations could come from that
            fact, that service could provide more than one way of connecting to it: http or JMS or something else.
        
            Parameters:
                serviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the service
        
            Returns:
                an array of properties containing configurations for a service. If no configurations found an empty array should be
                returned.
        
        
        """
        ...

class AdvancedParameterCreator(ParameterCreator):
    """
    public interface AdvancedParameterCreator extends :class:`~cern.japc.core.spi.factory.ParameterCreator`
    
        The interface of a creator of different types of JAPC parameters which can use
        :class:`~cern.japc.core.ParameterCharacteristics` object.
    """
    @typing.overload
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory, internalParameterCharacteristics: InternalParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def createParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor, parameterFactory: cern.japc.core.factory.ParameterFactory) -> cern.japc.core.transaction.TransactionalParameter: ...

class CompositeParameterCreator(AdvancedParameterCreator):
    """
    public interface CompositeParameterCreator extends :class:`~cern.japc.core.spi.factory.AdvancedParameterCreator`
    
        An interface for composite parameter creator (special creator).
    """
    def isKnownCompositeParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> bool:
        """
            Checks whether the paramter name is known composite parameter name
        
            Parameters:
                parameterUrl (:class:`~cern.japc.core.spi.ParameterUrl`): the URL of the parameter
        
            Returns:
                true in case of known composite parameter name
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.factory")``.

    AdvancedParameterCreator: typing.Type[AdvancedParameterCreator]
    CompositeParameterCreator: typing.Type[CompositeParameterCreator]
    InternalParameterCharacteristics: typing.Type[InternalParameterCharacteristics]
    ParameterCreator: typing.Type[ParameterCreator]
    ServiceConfigLookup: typing.Type[ServiceConfigLookup]
    impl: cern.japc.core.spi.factory.impl.__module_protocol__
