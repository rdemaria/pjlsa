import cern.lsa.domain.cern.settings.ad
import cern.lsa.domain.cern.settings.elena
import cern.lsa.domain.cern.settings.lktim
import cern.lsa.domain.cern.settings.spi
import cern.lsa.domain.cern.settings.util
import cern.lsa.domain.settings
import com.google.common.collect
import java.io
import java.lang
import java.util
import typing



class BeamProcessTypeOpticTransitionInfo(java.io.Serializable):
    """
    public class BeamProcessTypeOpticTransitionInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Information about transition between 2 optics in a beam process type.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float, string: str, string2: str, double2: float, double3: float): ...
    def getDuration(self) -> float:
        """
        
            Returns:
                transition duration
        
        
        """
        ...
    def getEndOptic(self) -> str:
        """
        
            Returns:
                optic to end with
        
        
        """
        ...
    def getParabolicFraction(self) -> float:
        """
        
            Returns:
                the fraction of transition time spent in parabola
        
        
        """
        ...
    def getStartOptic(self) -> str:
        """
        
            Returns:
                optic to start from
        
        
        """
        ...
    def getStartTime(self) -> float:
        """
        
            Returns:
                start time within beam process type
        
        
        """
        ...

class CernContextCategory(java.lang.Enum['CernContextCategory'], cern.lsa.domain.settings.ContextCategory):
    """
    public enum CernContextCategory extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.CernContextCategory`> implements cern.lsa.domain.settings.ContextCategory
    
        CERN context categories.
    """
    MD: typing.ClassVar['CernContextCategory'] = ...
    OBSOLETE: typing.ClassVar['CernContextCategory'] = ...
    OPERATIONAL: typing.ClassVar['CernContextCategory'] = ...
    TEST: typing.ClassVar['CernContextCategory'] = ...
    REFERENCE: typing.ClassVar['CernContextCategory'] = ...
    ARCHIVED: typing.ClassVar['CernContextCategory'] = ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def isArchived(self) -> bool:
        """
        
            Specified by:
                :code:`isArchived` in interface :code:`cern.lsa.domain.settings.ContextCategory`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CernContextCategory':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['CernContextCategory']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (CernContextCategory c : CernContextCategory.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class DeviceReDriveResponse:
    """
    @Immutable public interface DeviceReDriveResponse
    """
    def getDeviceName(self) -> str: ...
    def getParameterReDriveResponses(self) -> java.util.Set['ParameterReDriveResponse']: ...

class ParameterReDriveResponse:
    """
    @Immutable public interface ParameterReDriveResponse
    """
    def containsError(self) -> bool: ...
    def getContextName(self) -> str: ...
    def getJapcParameterNameToExceptionMessage(self) -> java.util.Map[str, str]: ...
    def getLsaExceptionMessage(self) -> str: ...
    def getParameterName(self) -> str: ...

class ReDriveRequest:
    """
    @Immutable public interface ReDriveRequest
    """
    def getDeviceNamesToReDrive(self) -> java.util.Set[str]: ...

class ReDriveResponse:
    """
    @Immutable public interface ReDriveResponse
    """
    def getDeviceReDriveResponses(self) -> java.util.Collection[DeviceReDriveResponse]: ...

class DefaultDeviceReDriveResponse(DeviceReDriveResponse):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultDeviceReDriveResponse extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse`
    
        Immutable implementation of :class:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse`.
    
        Use the builder to create immutable instances: :code:`DefaultDeviceReDriveResponse.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultDeviceReDriveResponse.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.cern.settings.DefaultDeviceReDriveResponse`.
        
            .. code-block: java
            
             DefaultDeviceReDriveResponse.builder()
                .deviceName(String) // required :meth:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse.getDeviceName`
                .addParameterReDriveResponse|addAllParameterReDriveResponses(cern.lsa.domain.cern.settings.ParameterReDriveResponse) // :meth:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse.getParameterReDriveResponses` elements
                .build();
             
        
            Returns:
                A new DefaultDeviceReDriveResponse builder
        
        
        """
        ...
    @staticmethod
    def copyOf(deviceReDriveResponse: DeviceReDriveResponse) -> 'DefaultDeviceReDriveResponse':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse`): The instance to copy
        
            Returns:
                A copied immutable DeviceReDriveResponse instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDeviceName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse.getDeviceName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse`
        
            Returns:
                The value of the :code:`deviceName` attribute
        
        
        """
        ...
    def getParameterReDriveResponses(self) -> com.google.common.collect.ImmutableSet[ParameterReDriveResponse]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`deviceName`, :code:`parameterReDriveResponses`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`DeviceReDriveResponse` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDeviceName(self, string: str) -> 'DefaultDeviceReDriveResponse':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse.getDeviceName` attribute. An equals check used to prevent
            copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for deviceName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameterReDriveResponses(self, parameterReDriveResponseArray: typing.List[ParameterReDriveResponse]) -> 'DefaultDeviceReDriveResponse':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse.getParameterReDriveResponses`.
        
            Parameters:
                elements (:class:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.domain.cern.settings.DefaultDeviceReDriveResponse` withParameterReDriveResponses (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.cern.settings.DeviceReDriveResponse.getParameterReDriveResponses`. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse`> elements): An iterable of parameterReDriveResponses elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withParameterReDriveResponses(self, iterable: java.lang.Iterable[ParameterReDriveResponse]) -> 'DefaultDeviceReDriveResponse': ...
    class Builder:
        def addAllParameterReDriveResponses(self, iterable: java.lang.Iterable[ParameterReDriveResponse]) -> 'DefaultDeviceReDriveResponse.Builder': ...
        def addParameterReDriveResponse(self, parameterReDriveResponse: ParameterReDriveResponse) -> 'DefaultDeviceReDriveResponse.Builder': ...
        def addParameterReDriveResponses(self, parameterReDriveResponseArray: typing.List[ParameterReDriveResponse]) -> 'DefaultDeviceReDriveResponse.Builder': ...
        def build(self) -> 'DefaultDeviceReDriveResponse': ...
        def deviceName(self, string: str) -> 'DefaultDeviceReDriveResponse.Builder': ...
        def parameterReDriveResponses(self, iterable: java.lang.Iterable[ParameterReDriveResponse]) -> 'DefaultDeviceReDriveResponse.Builder': ...

class DefaultParameterReDriveResponse(ParameterReDriveResponse):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultParameterReDriveResponse extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse`
    
        Immutable implementation of :class:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse`.
    
        Use the builder to create immutable instances: :code:`DefaultParameterReDriveResponse.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultParameterReDriveResponse.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.cern.settings.DefaultParameterReDriveResponse`.
        
            .. code-block: java
            
             DefaultParameterReDriveResponse.builder()
                .contextName(String) // required :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.getContextName`
                .parameterName(String) // required :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.getParameterName`
                .containsError(boolean) // required :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.containsError`
                .lsaExceptionMessage(String | null) // nullable :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.getLsaExceptionMessage`
                .putJapcParameterNameToExceptionMessage|putAllJapcParameterNameToExceptionMessage(String => String) // :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.getJapcParameterNameToExceptionMessage` mappings
                .build();
             
        
            Returns:
                A new DefaultParameterReDriveResponse builder
        
        
        """
        ...
    def containsError(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.containsError`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse`
        
            Returns:
                The value of the :code:`containsError` attribute
        
        
        """
        ...
    @staticmethod
    def copyOf(parameterReDriveResponse: ParameterReDriveResponse) -> 'DefaultParameterReDriveResponse':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse` value. Uses accessors to
            get values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse`): The instance to copy
        
            Returns:
                A copied immutable ParameterReDriveResponse instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getContextName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.getContextName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse`
        
            Returns:
                The value of the :code:`contextName` attribute
        
        
        """
        ...
    def getJapcParameterNameToExceptionMessage(self) -> com.google.common.collect.ImmutableMap[str, str]: ...
    def getLsaExceptionMessage(self) -> str: ...
    def getParameterName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.getParameterName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse`
        
            Returns:
                The value of the :code:`parameterName` attribute
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`contextName`, :code:`parameterName`, :code:`containsError`,
            :code:`lsaExceptionMessage`, :code:`japcParameterNameToExceptionMessage`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ParameterReDriveResponse` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withContainsError(self, boolean: bool) -> 'DefaultParameterReDriveResponse':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.containsError` attribute. A value equality check is used
            to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for containsError
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withContextName(self, string: str) -> 'DefaultParameterReDriveResponse':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.getContextName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for contextName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withJapcParameterNameToExceptionMessage(self, map: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]]) -> 'DefaultParameterReDriveResponse': ...
    def withLsaExceptionMessage(self, string: str) -> 'DefaultParameterReDriveResponse': ...
    def withParameterName(self, string: str) -> 'DefaultParameterReDriveResponse':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.cern.settings.ParameterReDriveResponse.getParameterName` attribute. An equals check used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): A new value for parameterName
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def build(self) -> 'DefaultParameterReDriveResponse': ...
        def containsError(self, boolean: bool) -> 'DefaultParameterReDriveResponse.Builder': ...
        def contextName(self, string: str) -> 'DefaultParameterReDriveResponse.Builder': ...
        def japcParameterNameToExceptionMessage(self, map: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]]) -> 'DefaultParameterReDriveResponse.Builder': ...
        def lsaExceptionMessage(self, string: str) -> 'DefaultParameterReDriveResponse.Builder': ...
        def parameterName(self, string: str) -> 'DefaultParameterReDriveResponse.Builder': ...
        def putAllJapcParameterNameToExceptionMessage(self, map: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]]) -> 'DefaultParameterReDriveResponse.Builder': ...
        @typing.overload
        def putJapcParameterNameToExceptionMessage(self, string: str, string2: str) -> 'DefaultParameterReDriveResponse.Builder': ...
        @typing.overload
        def putJapcParameterNameToExceptionMessage(self, entry: java.util.Map.Entry[str, str]) -> 'DefaultParameterReDriveResponse.Builder': ...

class DefaultReDriveRequest(ReDriveRequest):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultReDriveRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.settings.ReDriveRequest`
    
        Immutable implementation of :class:`~cern.lsa.domain.cern.settings.ReDriveRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultReDriveRequest.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultReDriveRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.cern.settings.DefaultReDriveRequest`.
        
            .. code-block: java
            
             DefaultReDriveRequest.builder()
                .addDeviceNamesToReDrive|addAllDeviceNamesToReDrive(String) // :meth:`~cern.lsa.domain.cern.settings.ReDriveRequest.getDeviceNamesToReDrive` elements
                .build();
             
        
            Returns:
                A new DefaultReDriveRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(reDriveRequest: ReDriveRequest) -> 'DefaultReDriveRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.cern.settings.ReDriveRequest` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.cern.settings.ReDriveRequest`): The instance to copy
        
            Returns:
                A copied immutable ReDriveRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDeviceNamesToReDrive(self) -> com.google.common.collect.ImmutableSet[str]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`deviceNamesToReDrive`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ReDriveRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withDeviceNamesToReDrive(self, iterable: java.lang.Iterable[str]) -> 'DefaultReDriveRequest': ...
    @typing.overload
    def withDeviceNamesToReDrive(self, stringArray: typing.List[str]) -> 'DefaultReDriveRequest': ...
    class Builder:
        def addAllDeviceNamesToReDrive(self, iterable: java.lang.Iterable[str]) -> 'DefaultReDriveRequest.Builder': ...
        @typing.overload
        def addDeviceNamesToReDrive(self, string: str) -> 'DefaultReDriveRequest.Builder': ...
        @typing.overload
        def addDeviceNamesToReDrive(self, stringArray: typing.List[str]) -> 'DefaultReDriveRequest.Builder': ...
        def build(self) -> 'DefaultReDriveRequest': ...
        def deviceNamesToReDrive(self, iterable: java.lang.Iterable[str]) -> 'DefaultReDriveRequest.Builder': ...

class DefaultReDriveResponse(ReDriveResponse):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultReDriveResponse extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.settings.ReDriveResponse`
    
        Immutable implementation of :class:`~cern.lsa.domain.cern.settings.ReDriveResponse`.
    
        Use the builder to create immutable instances: :code:`DefaultReDriveResponse.builder()`.
    """
    @staticmethod
    def builder() -> 'DefaultReDriveResponse.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.cern.settings.DefaultReDriveResponse`.
        
            .. code-block: java
            
             DefaultReDriveResponse.builder()
                .deviceReDriveResponses(Collection<cern.lsa.domain.cern.settings.DeviceReDriveResponse>) // required :meth:`~cern.lsa.domain.cern.settings.ReDriveResponse.getDeviceReDriveResponses`
                .build();
             
        
            Returns:
                A new DefaultReDriveResponse builder
        
        
        """
        ...
    @staticmethod
    def copyOf(reDriveResponse: ReDriveResponse) -> 'DefaultReDriveResponse':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.cern.settings.ReDriveResponse` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.cern.settings.ReDriveResponse`): The instance to copy
        
            Returns:
                A copied immutable ReDriveResponse instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDeviceReDriveResponses(self) -> java.util.Collection[DeviceReDriveResponse]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`deviceReDriveResponses`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`ReDriveResponse` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withDeviceReDriveResponses(self, collection: typing.Union[java.util.Collection[DeviceReDriveResponse], typing.Sequence[DeviceReDriveResponse]]) -> 'DefaultReDriveResponse': ...
    class Builder:
        def build(self) -> 'DefaultReDriveResponse': ...
        def deviceReDriveResponses(self, collection: typing.Union[java.util.Collection[DeviceReDriveResponse], typing.Sequence[DeviceReDriveResponse]]) -> 'DefaultReDriveResponse.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.settings")``.

    BeamProcessTypeOpticTransitionInfo: typing.Type[BeamProcessTypeOpticTransitionInfo]
    CernContextCategory: typing.Type[CernContextCategory]
    DefaultDeviceReDriveResponse: typing.Type[DefaultDeviceReDriveResponse]
    DefaultParameterReDriveResponse: typing.Type[DefaultParameterReDriveResponse]
    DefaultReDriveRequest: typing.Type[DefaultReDriveRequest]
    DefaultReDriveResponse: typing.Type[DefaultReDriveResponse]
    DeviceReDriveResponse: typing.Type[DeviceReDriveResponse]
    ParameterReDriveResponse: typing.Type[ParameterReDriveResponse]
    ReDriveRequest: typing.Type[ReDriveRequest]
    ReDriveResponse: typing.Type[ReDriveResponse]
    ad: cern.lsa.domain.cern.settings.ad.__module_protocol__
    elena: cern.lsa.domain.cern.settings.elena.__module_protocol__
    lktim: cern.lsa.domain.cern.settings.lktim.__module_protocol__
    spi: cern.lsa.domain.cern.settings.spi.__module_protocol__
    util: cern.lsa.domain.cern.settings.util.__module_protocol__
