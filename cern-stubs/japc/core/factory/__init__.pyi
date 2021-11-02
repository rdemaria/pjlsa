import cern.japc.core
import cern.japc.core.spi
import cern.japc.core.spi.provider
import cern.japc.core.transaction
import cern.japc.value
import java.io
import java.lang
import java.util
import typing



class AcquiredParameterValueFactory:
    """
    public class AcquiredParameterValueFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory to create :class:`~cern.japc.core.AcquiredParameterValue`s.
    """
    @typing.overload
    @staticmethod
    def newAcquiredParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, valueHeader: cern.japc.core.ValueHeader) -> cern.japc.core.AcquiredParameterValue:
        """
            Creates a new :class:`~cern.japc.core.AcquiredParameterValue` based on the given parameter name,
            :class:`~cern.japc.core.ValueHeader` and :code:`ParameterValue`.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                header (:class:`~cern.japc.core.ValueHeader`): value header
                value (cern.japc.value.ParameterValue): parameter value
        
            Returns:
                a new acquired parameter value with the provided properties
        
            Creates a new :class:`~cern.japc.core.AcquiredParameterValue` based on the given
            :class:`~cern.japc.core.AcquiredParameterValue` and the new :class:`~cern.japc.core.ValueHeader`.
        
            Parameters:
                originalValue (:class:`~cern.japc.core.AcquiredParameterValue`): original :class:`~cern.japc.core.AcquiredParameterValue`
                newHeader (:class:`~cern.japc.core.ValueHeader`): new value header
        
            Returns:
                a new acquired parameter value with the provided properties
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newAcquiredParameterValue(string: str, valueHeader: cern.japc.core.ValueHeader, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.AcquiredParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue, valueHeader: cern.japc.core.ValueHeader) -> cern.japc.core.AcquiredParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(string: str, valueHeader: cern.japc.core.ValueHeader, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.AcquiredParameterValue: ...

class FactoryConfigurationError(java.lang.Error):
    """
    public class FactoryConfigurationError extends `Error <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Error.html?is-external=true>`
    
        Thrown when a problem with configuration of the Factories exists. This error will typically be thrown when the class of
        a factory specified in the system properties cannot be found or instantiated.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class FailSafeParameterValueFactory:
    """
    public class FailSafeParameterValueFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory to create :class:`~cern.japc.core.FailSafeParameterValue`s.
    """
    @typing.overload
    @staticmethod
    def newFailSafeParameterValue(acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> cern.japc.core.FailSafeParameterValue:
        """
            Creates a new :class:`~cern.japc.core.FailSafeParameterValue` based on the given
            :class:`~cern.japc.core.AcquiredParameterValue`.
        
            Parameters:
                acquiredParameterValue (:class:`~cern.japc.core.AcquiredParameterValue`): :class:`~cern.japc.core.AcquiredParameterValue`
        
            Returns:
                a new fail-safe parameter value with the provided properties
        
        """
        ...
    @typing.overload
    @staticmethod
    def newFailSafeParameterValue(string: str, parameterException: cern.japc.core.ParameterException) -> cern.japc.core.FailSafeParameterValue:
        """
            Creates a new :class:`~cern.japc.core.FailSafeParameterValue` based on the given parameter name,
            :class:`~cern.japc.core.ValueHeader` and :code:`ParameterValue`.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                header (:class:`~cern.japc.core.ValueHeader`): value header
                value (cern.japc.value.ParameterValue): parameter value
        
            Returns:
                a new fail-safe parameter value with the provided properties
        
            Creates a new :class:`~cern.japc.core.FailSafeParameterValue` based on the given parameter name and
            :class:`~cern.japc.core.ParameterException`.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter to create value for
                parameterException (:class:`~cern.japc.core.ParameterException`): the exception to set in the created parameter
        
            Returns:
                a new fail-safe parameter value with the provided properties
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newFailSafeParameterValue(string: str, valueHeader: cern.japc.core.ValueHeader, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.FailSafeParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(string: str, parameterException: cern.japc.core.ParameterException) -> cern.japc.core.FailSafeParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(string: str, valueHeader: cern.japc.core.ValueHeader, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.FailSafeParameterValue: ...

class IParameterFactory:
    """
    public interface IParameterFactory
    
        Interface for a factory for JAPC parameters.
    """
    @typing.overload
    def newParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterCharacteristics: cern.japc.core.ParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str, parameterCharacteristics: cern.japc.core.ParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str, string2: str) -> cern.japc.core.transaction.TransactionalParameter: ...

class MapParameterValueFactory:
    """
    public class MapParameterValueFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory to create :code:`MapParameterValue`s.
    """
    @typing.overload
    @staticmethod
    def newMapParameterValue() -> cern.japc.value.MapParameterValue:
        """
            Creates a new empty :code:`MapParameterValue`.
        
            The value can be filled in afterwards with values.
        
            Returns:
                a new empty :code:`MapParameterValue`
        
        """
        ...
    @typing.overload
    @staticmethod
    def newMapParameterValue(immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.MapParameterValue:
        """
            Creates a new :code:`MapParameterValue` based on the given descriptor.
        
            If the descriptor is not provided then the call is equivalent to
            :meth:`~cern.japc.core.factory.MapParameterValueFactory.newMapParameterValue`.
        
            Parameters:
                mapDescriptor (cern.japc.value.MapDescriptor): the :code:`MapDescriptor` for the parameter value to create or :code:`null`
        
            Returns:
                a new :code:`MapParameterValue`
        
            Creates a new :code:`MapParameterValue` for the given parameter.
        
            The new value is based on the value descriptor of the provided parameter.
        
            Parameters:
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`MapParameterValue`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newMapParameterValue(mapDescriptor: cern.japc.value.MapDescriptor) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newMapParameterValue(stringArray: typing.List[str], simpleParameterValueArray: typing.List[cern.japc.value.SimpleParameterValue]) -> cern.japc.value.MapParameterValue:
        """
            Creates a new :code:`MapParameterValue` based on the given field names and :code:`SimpleParameterValue`s.
        
            Parameters:
                fieldNames (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the field names
                values (cern.japc.value.SimpleParameterValue[]): :code:`SimpleParameterValue`s
        
            Returns:
                a new :code:`MapParameterValue` based on the given field names and :code:`SimpleParameterValue`s
        
        public static cern.japc.value.MapParameterValue newMapParameterValue (`Map <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Map.html?is-external=true>`<`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`, cern.japc.value.SimpleParameterValue> namesAndValues)
        
            Creates a new :code:`MapParameterValue` based on the given field names and :code:`SimpleParameterValue`s.
        
            Parameters:
                namesAndValues (`Map <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Map.html?is-external=true>`<`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`, cern.japc.value.SimpleParameterValue> namesAndValues): the field names pointing to :code:`SimpleParameterValue`s
        
            Returns:
                a new :code:`MapParameterValue` based on the given field names and :code:`SimpleParameterValue`s
        
        """
        ...
    @typing.overload
    @staticmethod
    def newMapParameterValue(map: typing.Union[java.util.Map[str, cern.japc.value.SimpleParameterValue], typing.Mapping[str, cern.japc.value.SimpleParameterValue]]) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue() -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(mapDescriptor: cern.japc.value.MapDescriptor) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(stringArray: typing.List[str], simpleParameterValueArray: typing.List[cern.japc.value.SimpleParameterValue]) -> cern.japc.value.MapParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(map: typing.Union[java.util.Map[str, cern.japc.value.SimpleParameterValue], typing.Mapping[str, cern.japc.value.SimpleParameterValue]]) -> cern.japc.value.MapParameterValue: ...

class ObjectParameterValueFactory:
    """
    public class ObjectParameterValueFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory to create :class:`~cern.japc.core.ObjectParameterValue`s.
    """
    @staticmethod
    def newObjectParameterValue(object: typing.Any) -> cern.japc.core.ObjectParameterValue:
        """
            Creates a new :class:`~cern.japc.core.ObjectParameterValue` based on the given object.
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value to be held by the new :class:`~cern.japc.core.ObjectParameterValue`
        
            Returns:
                a new :class:`~cern.japc.core.ObjectParameterValue` holding the given object value
        
        
        """
        ...
    @staticmethod
    def newValue(object: typing.Any) -> cern.japc.core.ObjectParameterValue: ...

class ParameterCharacteristicsFactory:
    """
    public class ParameterCharacteristicsFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory class to create different :class:`~cern.japc.core.factory.ParameterCharacteristicsImpl` objects.
    """
    def __init__(self): ...
    @staticmethod
    def getNormalCharacteristics() -> cern.japc.core.ParameterCharacteristics:
        """
            Returns :class:`~cern.japc.core.factory.ParameterCharacteristicsImpl` to create usual parameter.
        
            Returns:
                :class:`~cern.japc.core.factory.ParameterCharacteristicsImpl` to create usual parameter.
        
        
        """
        ...
    @staticmethod
    def getParameterCharacteristics(boolean: bool, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]) -> cern.japc.core.ParameterCharacteristics: ...
    @staticmethod
    def getWildcardCharacteristics() -> cern.japc.core.ParameterCharacteristics:
        """
            Returns :class:`~cern.japc.core.factory.ParameterCharacteristicsImpl` to create parameter with wildcard selector
            functionality.
        
            Returns:
                :class:`~cern.japc.core.factory.ParameterCharacteristicsImpl` to create parameter with wildcard selector functionality.
        
        
        """
        ...

class ParameterCharacteristicsImpl(cern.japc.core.ParameterCharacteristics, java.io.Serializable):
    """
    public class ParameterCharacteristicsImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.ParameterCharacteristics`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class contains information about special parameter characteristics which is pre-defined by user:
    
    
    
          - If parameter must use wildcard functionality or not
    
        It also has a general purpose `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Map.html?is-external=true>` to pass/keep additional
        extention-specific information.
    
    
        The instance of the class can be used in multi-threaded environment. But care must be taken when using
        additionalInformation Map: class keeps a copy of Map passed by user, but the contents are not copied - only references
        are copied (shallow copy). User must use immutable objects as keys and values of the additionalInformation Map.
    
        Also see:
            :meth:`~serialized`
    """
    CHARACHTERISTICS_N: typing.ClassVar[cern.japc.core.ParameterCharacteristics] = ...
    """
    public static final :class:`~cern.japc.core.ParameterCharacteristics` CHARACHTERISTICS_N
    
        Characteristics of a normal parameter
    
    """
    CHARACHTERISTICS_W: typing.ClassVar[cern.japc.core.ParameterCharacteristics] = ...
    """
    public static final :class:`~cern.japc.core.ParameterCharacteristics` CHARACHTERISTICS_W
    
        Characteristic of a parameter with wildcard subscription functionality
    
    """
    def getAdditionalInformation(self) -> java.util.Map[str, typing.Any]: ...
    def isWildcardSubscriptionParameter(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.ParameterCharacteristics.isWildcardSubscriptionParameter`
            Returns true if wildcard functionality must be available for a parameter
        
            Specified by:
                :meth:`~cern.japc.core.ParameterCharacteristics.isWildcardSubscriptionParameter`Â in
                interfaceÂ :class:`~cern.japc.core.ParameterCharacteristics`
        
            Returns:
                true if wildcard functionality must be available for a parameter
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ParameterExceptionFactory:
    """
    public class ParameterExceptionFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory to create :class:`~cern.japc.core.ParameterException`s.
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def newException(exception: java.lang.Exception, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> cern.japc.core.ParameterException:
        """
            Creates a new :class:`~cern.japc.core.ParameterException` based on the original exception and the value which caused the
            original exception.
        
            Parameters:
                exception (`Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`): original exception
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the value caused the original exception
        
            Returns:
                a new :class:`~cern.japc.core.ParameterException`
        
        """
        ...
    @typing.overload
    @staticmethod
    def newException(string: str, exception: java.lang.Exception, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> cern.japc.core.ParameterException:
        """
            Creates a new :class:`~cern.japc.core.ParameterException` based on the given message, original exception and the value
            which caused the original exception.
        
            Parameters:
                message (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the message for the exception
                exception (`Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`): original exception
                value (:class:`~cern.japc.core.AcquiredParameterValue`): the value caused the original exception
        
            Returns:
                a new :class:`~cern.japc.core.ParameterException`
        
        
        """
        ...

class ParameterMetaFactoryConstants:
    """
    public interface ParameterMetaFactoryConstants
    
        Constants for JAPC Meta Factory
    """
    RDA_SERVICE_NAME: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RDA_SERVICE_NAME
    
        Deprecated.
        RDA service name
    
        Also see:
            :meth:`~constant`
    
    
    """
    RDA3_SERVICE_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RDA3_SERVICE_NAME
    
        RDA3 service name
    
        Also see:
            :meth:`~constant`
    
    
    """
    TGM_SERVICE_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TGM_SERVICE_NAME
    
        TGM service name
    
        Also see:
            :meth:`~constant`
    
    
    """
    SNMP_SERVICE_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SNMP_SERVICE_NAME
    
        SNMP protocol is used to access SNMP devices
    
        Also see:
            :meth:`~constant`
    
    
    """
    RMI_SERVICE_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RMI_SERVICE_NAME
    
        RMI protocol is used to access RMI devices
    
        Also see:
            :meth:`~constant`
    
    
    """
    RDA_PROTOCOL: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RDA_PROTOCOL
    
        Deprecated.
        RDA protocol name
    
        Also see:
            :meth:`~constant`
    
    
    """
    RDA3_PROTOCOL: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RDA3_PROTOCOL
    
        RDA3 protocol name
    
        Also see:
            :meth:`~constant`
    
    
    """
    TGM_PROTOCOL: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TGM_PROTOCOL
    
        TGM protocol name
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_DEFAULT_SERVICE_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_DEFAULT_SERVICE_NAME
    
        System property to specify default service name
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_DEFAULT_PROTOCOL_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_DEFAULT_PROTOCOL_NAME
    
        System property to specify default protocol name
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_SERVICE_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_SERVICE_NAME
    
        Default service name
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_PROTOCOL_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_PROTOCOL_NAME
    
        Default protocol name
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_SERVICE_NAME_RESOLVERS: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_SERVICE_NAME_RESOLVERS
    
        System property to specify service name resolvers (comma separated)
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_SERVICE_CONFIG_LOOKUPS: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_SERVICE_CONFIG_LOOKUPS
    
        System property to specify service configuration lookups (comma separated)
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_WILDCARD_SELECTOR_RESOLVER: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_WILDCARD_SELECTOR_RESOLVER
    
        System property to specify wildcard selector resolver
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_DEFAULT_WILDCARD_SUBSCRIPTION_ON: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_DEFAULT_WILDCARD_SUBSCRIPTION_ON
    
        System property to specify usage of wildcard functionality by default for all the parameters
    
        Also see:
            :meth:`~constant`
    
    
    """

class SelectorFactory:
    """
    public class SelectorFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory to create :class:`~cern.japc.core.Selector`s.
    """
    @typing.overload
    @staticmethod
    def newSelector(parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.Selector:
        """
            Creates a new :class:`~cern.japc.core.Selector`.
        
            The new :class:`~cern.japc.core.Selector` has no data filter.
        
            Parameters:
                id (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the ID of the selector to create (cannot be :code:`null`)
        
            Returns:
                a new :class:`~cern.japc.core.Selector`
        
            Creates a new no-selector with data filter.
        
            Parameters:
                dataFilter (cern.japc.value.ParameterValue): a filter for the data to request
        
            Returns:
                a new :class:`~cern.japc.core.Selector`
        
        """
        ...
    @typing.overload
    @staticmethod
    def newSelector(string: str) -> cern.japc.core.Selector: ...
    @typing.overload
    @staticmethod
    def newSelector(string: str, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.core.Selector:
        """
            Creates a new :class:`~cern.japc.core.Selector`.
        
            Parameters:
                id (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the ID of the selector to create (cannot be :code:`null`)
                dataFilter (cern.japc.value.ParameterValue): a filter for the data to request
        
            Returns:
                a new :class:`~cern.japc.core.Selector`
        
        
        """
        ...

class ServiceNameResolver:
    """
    public interface ServiceNameResolver
    
        The interface of a class which returns the name of the service associated with a ParameterCreator which should be used
        to create a JAPC parameter with certain name
    """
    def getServiceName(self, string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> str:
        """
            This method returns the name of the service to use for parameter or null if this parameter name is unknown to this
            resolver.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the parameter
                parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`): the descriptor of the parameter
        
            Returns:
                the name of the creator to use or :code:`null` if this parameter name is unknown to this resolver
        
        
        """
        ...

class SimpleParameterValueFactory:
    """
    public class SimpleParameterValueFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory to create :code:`SimpleParameterValue`s.
    """
    @typing.overload
    @staticmethod
    def newSimpleParameterValue() -> cern.japc.value.SimpleParameterValue:
        """
            Creates a new empty :code:`SimpleParameterValue`.
        
            Returns:
                a new empty :code:`SimpleParameterValue`
        
        """
        ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(boolean: bool) -> cern.japc.value.SimpleParameterValue:
        """
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (boolean): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (byte): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (double): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (float): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (int): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (long): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (short): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.EnumItem): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.EnumItemSet): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.DiscreteFunction): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.DiscreteFunctionList): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (boolean[]): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (byte[]): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (double[]): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (float[]): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (int[]): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (long[]): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (short[]): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new parameter value based on the given value
        
            Parameters:
                value (cern.japc.value.EnumItem[]): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new parameter value based on the given value
        
            Parameters:
                value (cern.japc.value.EnumItemSet[]): the value to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            The given value must be one of the supported types:
        
              - primitive wrappers and Strings
              - arrays or :code:`Array2D` of primitives and Strings
              - :code:`EnumItem` and :code:`EnumItemSet`
              - arrays or :code:`Array2D` of :code:`EnumItem` and :code:`EnumItemSet`
              - :code:`DiscreteFunction`
              - :code:`DiscreteFunctionList`
        
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): value of supported type (not :code:`null`) to create the :code:`SimpleParameterValue` with
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given :code:`ValueType`.
        
            Parameters:
                valueType (cern.japc.value.ValueType): the type of the parameter value to create
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new enum-based :code:`SimpleParameterValue`.
        
            Parameters:
                valueType (cern.japc.value.ValueType): the type of the :code:`SimpleParameterValue` to create
                enumType (cern.japc.value.EnumType): the enumeration type
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given :code:`SimpleDescriptor`.
        
            If the descriptor is not provided then the call is equivalent to
            :meth:`~cern.japc.core.factory.SimpleParameterValueFactory.newSimpleParameterValue`.
        
            Parameters:
                simpleDescriptor (cern.japc.value.SimpleDescriptor): the :code:`SimpleDescriptor` for the parameter value to create or :code:`null`
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` for the given parameter.
        
            The new value is based on the value descriptor of the provided parameter.
        
            Parameters:
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` for the given parameter.
        
            The new value is based on the value descriptor of the provided parameter.
        
            Parameters:
                value (boolean): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (byte): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (double): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (float): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (int): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (long): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (short): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.EnumItem): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.EnumItemSet): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.DiscreteFunction): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.DiscreteFunctionList): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
        """
        ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(boolean: bool, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue:
        """
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (boolean[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (byte[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (double[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (float[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (int[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (long[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (short[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the Value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.EnumItem[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the Value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.EnumItemSet[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the Value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` (supposed to be 2d-array) based on the given value and dimensions.
        
            The given value must be an array of the supported types:
        
              - primitive wrappers and Strings
              - :code:`EnumItem` and :code:`EnumItemSet`
        
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): value of supported type (not :code:`null`) to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the Value (rowCount, columnCount)
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (boolean[]): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (byte[]): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (double[]): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (float[]): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (int[]): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (long[]): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (short[]): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new parameter value based on the given value
        
            Parameters:
                value (cern.japc.value.EnumItem[]): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new parameter value based on the given value
        
            Parameters:
                value (cern.japc.value.EnumItemSet[]): the value to create the :code:`SimpleParameterValue` with
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` for :code:`parameter` based on the given :code:`value`.
        
            The given value must be one of the supported types:
        
              - primitive wrappers and Strings
              - arrays or :code:`Array2D` of primitives and Strings
              - :code:`EnumItem` and :code:`EnumItemSet`
              - arrays or :code:`Array2D` of :code:`EnumItem` and :code:`EnumItemSet`
              - :code:`DiscreteFunction`
              - :code:`DiscreteFunctionList`
        
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): value of supported type (should not be :code:`null`)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
        """
        ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(booleanArray: typing.List[bool]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(booleanArray: typing.List[bool], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(booleanArray: typing.List[bool], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(booleanArray: typing.List[bool], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue:
        """
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (boolean[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (byte[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (double[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (float[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (int[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (long[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (short[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the Value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.EnumItem[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the Value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` based on the given value.
        
            Parameters:
                value (cern.japc.value.EnumItemSet[]): the value to create the :code:`SimpleParameterValue` with
                dimensions (int[]): the dimensions of the Value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
            Creates a new :code:`SimpleParameterValue` (supposed to be 2d-array) based on the given :code:`value` and
            :code:`dimensions` for :code:`parameter`.
        
            The given value must be an array of the supported types:
        
              - primitive wrappers and Strings
              - :code:`EnumItem` and :code:`EnumItemSet`
        
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): value of supported type (should not be :code:`null`)
                dimensions (int[]): the dimensions of the Value (rowCount, columnCount)
                parameter (:class:`~cern.japc.core.ImmutableParameter`): :class:`~cern.japc.core.ImmutableParameter` to create value for
        
            Returns:
                a new :code:`SimpleParameterValue`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byte: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byte: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byteArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byteArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byteArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(byteArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(discreteFunction: cern.japc.value.DiscreteFunction) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(discreteFunction: cern.japc.value.DiscreteFunction, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(discreteFunctionList: cern.japc.value.DiscreteFunctionList, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItem: cern.japc.value.EnumItem) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItem: cern.japc.value.EnumItem, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSet: cern.japc.value.EnumItemSet) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSet: cern.japc.value.EnumItemSet, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemArray: typing.List[cern.japc.value.EnumItem]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemArray: typing.List[cern.japc.value.EnumItem], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(simpleDescriptor: cern.japc.value.SimpleDescriptor) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(valueType: cern.japc.value.ValueType) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(valueType: cern.japc.value.ValueType, enumType: cern.japc.value.EnumType) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(double: float) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(double: float, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(doubleArray: typing.List[float]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(doubleArray: typing.List[float], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(doubleArray: typing.List[float], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(doubleArray: typing.List[float], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(float: float) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(float: float, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(floatArray: typing.List[float]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(floatArray: typing.List[float], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(floatArray: typing.List[float], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(floatArray: typing.List[float], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(int: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(int: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(intArray: typing.List[int], intArray2: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(intArray: typing.List[int], intArray2: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(object: typing.Any) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(object: typing.Any, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(object: typing.Any, intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(object: typing.Any, intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(string: str) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(string: str, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(stringArray: typing.List[str]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(stringArray: typing.List[str], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(stringArray: typing.List[str], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(stringArray: typing.List[str], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(long: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(long: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(longArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(longArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(longArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(longArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(short: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(short: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(shortArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(shortArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(shortArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newSimpleParameterValue(shortArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue() -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(boolean: bool) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(boolean: bool, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(booleanArray: typing.List[bool]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(booleanArray: typing.List[bool], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(booleanArray: typing.List[bool], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(booleanArray: typing.List[bool], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byte: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byte: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byteArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byteArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byteArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(byteArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(discreteFunction: cern.japc.value.DiscreteFunction) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(discreteFunction: cern.japc.value.DiscreteFunction, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(discreteFunctionList: cern.japc.value.DiscreteFunctionList, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItem: cern.japc.value.EnumItem) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItem: cern.japc.value.EnumItem, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSet: cern.japc.value.EnumItemSet) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSet: cern.japc.value.EnumItemSet, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemArray: typing.List[cern.japc.value.EnumItem]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemArray: typing.List[cern.japc.value.EnumItem], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(simpleDescriptor: cern.japc.value.SimpleDescriptor) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(valueType: cern.japc.value.ValueType) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(valueType: cern.japc.value.ValueType, enumType: cern.japc.value.EnumType) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(double: float) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(double: float, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(doubleArray: typing.List[float]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(doubleArray: typing.List[float], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(doubleArray: typing.List[float], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(doubleArray: typing.List[float], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(float: float) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(float: float, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(floatArray: typing.List[float]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(floatArray: typing.List[float], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(floatArray: typing.List[float], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(floatArray: typing.List[float], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(int: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(int: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(intArray: typing.List[int], intArray2: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(intArray: typing.List[int], intArray2: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(object: typing.Any) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(object: typing.Any, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(object: typing.Any, intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(object: typing.Any, intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(string: str) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(string: str, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(stringArray: typing.List[str]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(stringArray: typing.List[str], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(stringArray: typing.List[str], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(stringArray: typing.List[str], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(long: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(long: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(longArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(longArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(longArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(longArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(short: int) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(short: int, immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(shortArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(shortArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(shortArray: typing.List[int], intArray: typing.List[int]) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    @staticmethod
    def newValue(shortArray: typing.List[int], intArray: typing.List[int], immutableParameter: cern.japc.core.ImmutableParameter) -> cern.japc.value.SimpleParameterValue: ...

class TransactionFactory:
    """
    public class TransactionFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory to build CompositeTransaction.
    """
    @staticmethod
    def newCompositeTransaction() -> cern.japc.core.transaction.CompositeTransaction:
        """
            Creates a new Transaction.
        
            Returns:
                the instance of Parameter for the given parameter.
        
        
        """
        ...

class ValueHeaderFactory:
    """
    public class ValueHeaderFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory to create :class:`~cern.japc.core.ValueHeader`s.
    """
    NO_CYCLE_STAMP: typing.ClassVar[int] = ...
    """
    public static final long NO_CYCLE_STAMP
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    NO_SET_STAMP: typing.ClassVar[int] = ...
    """
    public static final long NO_SET_STAMP
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    @staticmethod
    def newAcquisitionFirstUpdateHeader(long: int, long2: int, selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader:
        """
            Create a :class:`~cern.japc.core.ValueHeader` for first updates of acquisition parameters.
        
            Parameters:
                acqStamp (long): acquisition timestamp in nanos
                cycleStamp (long): cycle stamp in nanos
                selector (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
            Create a :class:`~cern.japc.core.ValueHeader` for first updates of acquisition parameters.
        
            Parameters:
                acqStamp (long): acquisition timestamp in nanos
                cycleStamp (long): cycle stamp in nanos
                selector (:class:`~cern.japc.core.Selector`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newAcquisitionFirstUpdateHeader(long: int, long2: int, string: str) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newAcquisitionRegularUpdateHeader(long: int, long2: int, selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader:
        """
            Create a :class:`~cern.japc.core.ValueHeader` for regular updates of acquisition parameters.
        
            Parameters:
                acqStamp (long): acquisition timestamp in nanos
                cycleStamp (long): cycle stamp in nanos
                selector (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
            Create a :class:`~cern.japc.core.ValueHeader` for regular updates of acquisition parameters.
        
            Parameters:
                acqStamp (long): acquisition timestamp in nanos
                cycleStamp (long): cycle stamp in nanos
                selector (:class:`~cern.japc.core.Selector`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newAcquisitionRegularUpdateHeader(long: int, long2: int, string: str) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingFirstUpdateHeader(long: int, long2: int, selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader:
        """
            Create a :class:`~cern.japc.core.ValueHeader` for first updates of setting parameters.
        
            Parameters:
                acqStamp (long): acquisition timestamp in nanos
                setStamp (long): set stamp in nanos
                selector (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
            Create a :class:`~cern.japc.core.ValueHeader` for first updates of setting parameters.
        
            Parameters:
                acqStamp (long): acquisition timestamp in nanos
                setStamp (long): set stamp in nanos
                selector (:class:`~cern.japc.core.Selector`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newSettingFirstUpdateHeader(long: int, long2: int, string: str) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingImmediateUpdateHeader(selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader:
        """
            Create a :class:`~cern.japc.core.ValueHeader` for immediate updates of setting parameters.
        
            Parameters:
                acqStamp (long): acquisition timestamp in nanos
                setStamp (long): set stamp in nanos
                selector (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
            Create a :class:`~cern.japc.core.ValueHeader` for immediate updates of setting parameters.
        
            Parameters:
                acqStamp (long): acquisition timestamp in nanos
                setStamp (long): set stamp in nanos
                selector (:class:`~cern.japc.core.Selector`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
            Create a :class:`~cern.japc.core.ValueHeader` for immediate updates of setting parameters.**** Both acquisition
            timestamp (acqStamp) and set timestamp (setStamp) will be initialized to current time.
        
            Parameters:
                selector (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
            Create a :class:`~cern.japc.core.ValueHeader` for immediate updates of setting parameters.**** * Both acquisition
            timestamp (acqStamp) and set timestamp (setStamp) will be initialized to current time.
        
            Parameters:
                selector (:class:`~cern.japc.core.Selector`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newSettingImmediateUpdateHeader(string: str) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingImmediateUpdateHeader(long: int, long2: int, selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingImmediateUpdateHeader(long: int, long2: int, string: str) -> cern.japc.core.ValueHeader: ...
    @typing.overload
    @staticmethod
    def newSettingRegularUpdateHeader(long: int, long2: int, selector: cern.japc.core.Selector) -> cern.japc.core.ValueHeader:
        """
            Create a :class:`~cern.japc.core.ValueHeader` for regular updates of setting parameters.
        
            Parameters:
                acqStamp (long): acquisition timestamp in nanos
                setStamp (long): set stamp in nanos
                selector (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
            Create a :class:`~cern.japc.core.ValueHeader` for regular updates of setting parameters.
        
            Parameters:
                acqStamp (long): acquisition timestamp in nanos
                setStamp (long): set stamp in nanos
                selector (:class:`~cern.japc.core.Selector`): selector
        
            Returns:
                new :class:`~cern.japc.core.ValueHeader`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newSettingRegularUpdateHeader(long: int, long2: int, string: str) -> cern.japc.core.ValueHeader: ...
    @staticmethod
    def toFirstUpdateHeader(valueHeader: cern.japc.core.ValueHeader) -> cern.japc.core.ValueHeader:
        """
            Converts value header to be first-update value header.
        
            Parameters:
                header (:class:`~cern.japc.core.ValueHeader`): original value header
        
            Returns:
                first-update value header
        
        
        """
        ...
    @staticmethod
    def toImmediateUpdateHeader(valueHeader: cern.japc.core.ValueHeader) -> cern.japc.core.ValueHeader:
        """
            Converts value header to be immediate-update value header.
        
            Parameters:
                header (:class:`~cern.japc.core.ValueHeader`): original value header
        
            Returns:
                immediate-update value header
        
        
        """
        ...
    @staticmethod
    def toRegularUpdateHeader(valueHeader: cern.japc.core.ValueHeader) -> cern.japc.core.ValueHeader:
        """
            Converts value header to be regular value header.
        
            Parameters:
                header (:class:`~cern.japc.core.ValueHeader`): original value header
        
            Returns:
                regular value header
        
        
        """
        ...

class ParameterFactory(IParameterFactory):
    """
    public abstract class ParameterFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.factory.IParameterFactory`
    
        Defines a factory API that enables to configure and obtains :code:`Parameter`s. The concrete implementation of the
        factories returned by the :code:`newInstance` method will be determined at runtime based on properties.
    
    
    
        **Since :class:`~cern.japc.core.spi.factory.impl.ParameterMetaFactory` is implemented the information in italic below is
        still valid, but not recommended to use for creating different factories for different types of parameters.
        :class:`~cern.japc.core.spi.factory.impl.ParameterMetaFactory` can create any type of parameters itself. The only thing
        you need to do is to obtain an instance of :class:`~cern.japc.core.spi.factory.impl.ParameterMetaFactory` via
        :meth:`~cern.japc.core.factory.ParameterFactory.newInstance` method.** *The system property :code:`FACTORY_ID` will be
        looked-up in order to find the string giving the fully qualified name of the factory class to instantiate. It is
        possible to start a java program and specifying the factory to use by providing the following property on the java
        command : -Dcern.japc.factory.ParameterFactory=[the fully qualified name of the factory class] It is also possible to
        set the factory directly from java by using : System.setProperty(ParameterFactory.FACTORY_ID, "[the fully qualified name
        of the factory class]"); Last it is also possible to request directly a specific factory by using : ParameterFactory
        factory = ParameterFactory.newInstance("[the fully qualified name of the factory class]");*
    
        The system property :code:`DESCRIPTOR_PROVIDER_ID` will be looked-up in order to find the string given the fully
        qualified name of the provider class to instantiate. The provider class is the class providing the factory with the
        parameter descriptor, the value descriptor and the device descriptor.
    
        It is possible to start a java program and specifying the descriptor provider to use by providing the following property
        on the java command :
    
        .. code-block: java
        
          -Dcern.japc.spi.provider.DescriptorProvider=[the fully qualified name of the provider class]
         
        It is also possible to set the factory directly from java by using :
    
        .. code-block: java
        
         System.setProperty(ParameterFactory.DESCRIPTOR_PROVIDER_ID, "[the fully qualified name of the provider class]");
         
    
        The concrete implementation of :code:`ParameterFactory` returned by the method :code:`newIntance()` creates JAPC
        parameters tailored for a given transport and a given domain. Using the instance of parameter factory, it is possible to
        create parameters by calling
    
        .. code-block: java
        
          Parameter parameter = parameterFactory.newParameter(...)
         
    
        The implementors of a concrete implementation of :code:`ParameterFactory` must override the abstract protected methods :
    
        .. code-block: java
        
          protected TransactionalParameter newParameterImpl(...)
         
        That method is called whenever a parameter is created. The method is given a :code:`ParameterDescriptor` and a
        :code:`ValueDescriptor` in order to create the parameter, plus :code:`InternalParameterCharacteristics` object to keep
        track on parameter creation process. The :code:`ParameterDescriptor` and the :code:`ValueDescriptor` are obtained from
        the :code:`DescriptorProvider` associated with the factory. In order to get the :code:`DescriptorProvider`, the
        ParameterFactory will call the protected method :code:`getDescriptorProvider()`. There are two ways of setting a
        :code:`DescriptorProvider` for a factory. By default this factory will use a System property to get the class of the
        :code:`DescriptorProvider` to use. The other way is to override the method :code:`getDescriptorProvider()` of this
        factory and to provide directly an implementation. The :code:`InternalParameterCharacteristics` are derived from
        :code:`ParameterCharacteristicsImpl` passed from client via :code:`newParameter(...)` method.
    
        An implementation of the ParameterFactory class is NOT guaranteed to be thread safe. It is up to the user of the factory
        to make sure that the ParameterFactory is not used by more than one thread. An application can use the same instance of
        the factory to obtain one or more instances of Parameter provided the instance of the factory isn't being used in more
        than one thread at a time.
    """
    FACTORY_ID: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` FACTORY_ID
    
        the default ID used to lookup in the system properties the class name to instantiate for a concrete implementation of
        this factory
    
        Also see:
            :meth:`~constant`
    
    
    """
    DESCRIPTOR_PROVIDER_ID: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DESCRIPTOR_PROVIDER_ID
    
        the default ID used to lookup in the system properties the class name to instantiate for a concrete implementation of
        the descriptor provider used by this factory.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_JAPC_DIRSERVICE_PROVIDER_ENABLED: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_JAPC_DIRSERVICE_PROVIDER_ENABLED
    
        Deprecated.
        Please use :meth:`~cern.japc.core.factory.ParameterFactory.SYSPROP_JAPC_CCS_DESCRIPTORS_ENABLED` instead.
    
    
        (And replace the obsolete japc-ext-dirservice dependency by japc-svc-ccs in your product.xml)
        System property to enable Directory Service pre-defined descriptor provider
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_JAPC_CCS_DESCRIPTORS_ENABLED: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_JAPC_CCS_DESCRIPTORS_ENABLED
    
        System property to enable CCS descriptors
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_JAPC_IGNORE_SET: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_JAPC_IGNORE_SET
    
        System property defining if all set operations are ignored on JAPC parameters
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def addAllDescriptors(string: str, deviceDescriptor: cern.japc.core.DeviceDescriptor, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor) -> None:
        """
            Adds a device descriptor into the list of known devices
        
        
            Adds a parameter descriptor into the list of known parameters
        
        
            Adds a value descriptor into the list of known parameter values
        
        
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The full name of the device could be used, for example MAGEA_900/Acquisition, or only a device class name, for example
                    MAGEA/Acquisition.
                deviceDescriptor (:class:`~cern.japc.core.DeviceDescriptor`):         parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`):         valueDescriptor (cern.japc.value.ValueDescriptor): 
        
        """
        ...
    @staticmethod
    def addDeviceDescriptor(string: str, deviceDescriptor: cern.japc.core.DeviceDescriptor) -> None:
        """
            Adds a device descriptor into the list of known devices
        
        
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): It could be the full name of the device, for example MAGEA_900, or only a device class name, for example MAGEA.
                deviceDescriptor (:class:`~cern.japc.core.DeviceDescriptor`): 
        
        """
        ...
    @staticmethod
    def addParameterAndValueDescriptor(string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor) -> None:
        """
            Adds a parameter descriptor into the list of known parameters
        
        
            Adds a value descriptor into the list of known parameter values
        
        
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The full name of the device could be used, for example MAGEA_900/Acquisition, or only a device class name, for example
                    MAGEA/Acquisition.
                parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`):         valueDescriptor (cern.japc.value.ValueDescriptor): 
        
        """
        ...
    @staticmethod
    def addParameterDescriptor(string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> None:
        """
            Adds a parameter descriptor into the list of known parameters
        
        
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The full name of the device could be used, for example MAGEA_900/Acquisition, or only a device class name, for example
                    MAGEA/Acquisition.
                parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`): 
        
        """
        ...
    @staticmethod
    def addValueDescriptor(string: str, valueDescriptor: cern.japc.value.ValueDescriptor) -> None:
        """
            Adds a value descriptor into the list of known parameter values
        
        
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The full name of the device could be used, for example MAGEA_900/Acquisition, or only a device class name, for example
                    MAGEA/Acquisition.
                valueDescriptor (cern.japc.value.ValueDescriptor): 
        
        """
        ...
    def getDescriptorProvider(self) -> cern.japc.core.spi.provider.DescriptorProvider:
        """
            Returns the DescriptorProvider used to provide parameter descriptors and value descriptors for this factory. This method
            is called each time the descriptor provider is used. The default implementation will try to load the descriptor provider
            based on the system properties and cache it. If the descriptor provider is not given in the system properties a default
            provider will be used. The default provider returns always a null value descriptor, a null device descriptor and a
            parameter descriptor allowing read/write/monitor.
        
            This method is synchronized to avoid creating 2 descriptor provider structures in parallel if in very beginning (when
            the structure isn't instantiated yet) several request for parameter creation come at the same time.
        
            Returns:
                the provider for this factory
        
        
        """
        ...
    def getDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor:
        """
            Gets the descriptor of the device of given name. If no device of that name can be found or if there is no descriptor for
            the device null is returned.
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the device to get the descriptor for
        
            Returns:
                the descriptor of the device of given name or null.
        
        
        """
        ...
    def getDeviceDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    @typing.overload
    def getParameterDescriptor(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> cern.japc.core.ParameterDescriptor: ...
    @typing.overload
    def getParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def getParameterDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def getParameterDescriptorsFromUrls(self, collection: typing.Union[java.util.Collection[cern.japc.core.spi.ParameterUrl], typing.Sequence[cern.japc.core.spi.ParameterUrl]]) -> java.util.Map[cern.japc.core.spi.ParameterUrl, cern.japc.core.ParameterDescriptor]: ...
    @typing.overload
    def getValueDescriptor(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> cern.japc.value.ValueDescriptor: ...
    @typing.overload
    def getValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def getValueDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...
    def getValueDescriptorsFromUrls(self, collection: typing.Union[java.util.Collection[cern.japc.core.spi.ParameterUrl], typing.Sequence[cern.japc.core.spi.ParameterUrl]]) -> java.util.Map[cern.japc.core.spi.ParameterUrl, cern.japc.value.ValueDescriptor]: ...
    def isUnknownParameterSupported(self) -> bool:
        """
            Returns whether parameters not found by the descriptor provider fail or succeed with a default descriptor
        
            Returns:
                whether parameters not found by the descriptor provider fail or succeed with a default descriptor
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newInstance() -> 'ParameterFactory':
        """
            Obtains a new instance of a ParameterFactory. This static method creates a new factory instance and uses the
            cern.japc.core.factory.ParameterFactory system property to find the fqn of the class to instantiate. Once an application
            has obtained a reference on a ParameterFactory it can use it to configure and obtain Parameter instances.
        
            Note that the ClassLoader used to load the concrete factory class dynamically is the one obtained from
            :code:`Thread.currentThread().getContextClassLoader()`. In some context, when the class loader of this factory is not
            the same as the one that loaded the class using the factory and holding the concrete factory, you may have to set the
            context class loader of the current thread by doing :code:`Thread.currentThread().setContextClassLoader()` just to make
            sure that JAPC will find the class to load.
            In case when ParameterMetaFactory used with Spring some actions should be done to make sure that the instance of
            ParameterMetaFactory returned from this method is the same which is created by Spring:
        
        
            1. Spring context should be initialized before any call to this method.
        
        
            2. In Spring the post-creation method
            :meth:`~cern.japc.core.spi.factory.impl.ParameterMetaFactory.registerInParameterFactory` should be used for
            ParameterMetaFactory class.
        
        
        
            Returns:
                a non null instance of ParameterFactory
        
            Raises:
                :class:`~cern.japc.core.factory.FactoryConfigurationError`: is the instance of the factory cannot be created.
        
        """
        ...
    @typing.overload
    @staticmethod
    def newInstance(string: str) -> 'ParameterFactory':
        """
            Obtains a new instance of a ParameterFactory. This static method creates a new factory instance and uses the given
            factoryId as a system property to find the fqn of the class to instantiate. Once an application has obtained a reference
            to a ParameterFactory it can use the factory to configure and obtain Parameter instances.
        
            Note that the ClassLoader used to load the concrete factory class dynamically is the one obtained from
            :code:`Thread.currentThread().getContextClassLoader()`. In some context, when the class loader of this factory is not
            the same as the one that loaded the class using the factory and holding the concrete factory, you may have to set the
            context class loader of the current thread by doing :code:`Thread.currentThread().setContextClassLoader()` just to make
            sure that JAPC will find the class to load.
        
            Parameters:
                factoryId (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the id of the factory to instantiate
        
            Returns:
                a non null instance of ParameterFactory
        
            Raises:
                :class:`~cern.japc.core.factory.FactoryConfigurationError`: is the instance of the factory cannot be created.
        
        
        """
        ...
    @typing.overload
    def newParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, parameterUrl: cern.japc.core.spi.ParameterUrl, parameterCharacteristics: cern.japc.core.ParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str, parameterCharacteristics: cern.japc.core.ParameterCharacteristics) -> cern.japc.core.transaction.TransactionalParameter: ...
    @typing.overload
    def newParameter(self, string: str, string2: str) -> cern.japc.core.transaction.TransactionalParameter: ...
    def newParameterExplorer(self) -> cern.japc.core.ParameterExplorer:
        """
            Creates a new :code:`ParameterExplorer`. The parameter explorer is an optional component the factory can provide to
            explore the parameters it can create. With a parameter explorer it is possible to browse the parameters and their
            relationships.
        
            The default implementation returns null
        
            Returns:
                a new instance of :code:`ParameterExplorer` if supported or null if not supported.
        
        
        """
        ...
    def setUnknownParameterSupported(self, boolean: bool) -> None:
        """
            When a parameter is created, the factory is looking for a parameter descriptor and for a value descriptor. If the
            descriptor provider does not know about a given parameter it will return no parameter descriptor. This factory can have
            two behavior. Fail and throw an exception warning the parameter hasn't been found. Create a default parameter descriptor
            allowing read/write and monitor access. If set with false the first behavior (fail first) is enabled. If set with true
            the second behavior (default descriptor) is enabled. The default behavior is to default descriptor.
        
            Parameters:
                unknownParameterSupported (boolean): true for default descriptor, false for fail first
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.factory")``.

    AcquiredParameterValueFactory: typing.Type[AcquiredParameterValueFactory]
    FactoryConfigurationError: typing.Type[FactoryConfigurationError]
    FailSafeParameterValueFactory: typing.Type[FailSafeParameterValueFactory]
    IParameterFactory: typing.Type[IParameterFactory]
    MapParameterValueFactory: typing.Type[MapParameterValueFactory]
    ObjectParameterValueFactory: typing.Type[ObjectParameterValueFactory]
    ParameterCharacteristicsFactory: typing.Type[ParameterCharacteristicsFactory]
    ParameterCharacteristicsImpl: typing.Type[ParameterCharacteristicsImpl]
    ParameterExceptionFactory: typing.Type[ParameterExceptionFactory]
    ParameterFactory: typing.Type[ParameterFactory]
    ParameterMetaFactoryConstants: typing.Type[ParameterMetaFactoryConstants]
    SelectorFactory: typing.Type[SelectorFactory]
    ServiceNameResolver: typing.Type[ServiceNameResolver]
    SimpleParameterValueFactory: typing.Type[SimpleParameterValueFactory]
    TransactionFactory: typing.Type[TransactionFactory]
    ValueHeaderFactory: typing.Type[ValueHeaderFactory]
