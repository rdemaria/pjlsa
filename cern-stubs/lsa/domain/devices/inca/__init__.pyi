import cern.lsa.domain.devices.type
import java.io
import java.lang
import java.util
import typing



class IncaPropertyFieldInfo:
    """
    @Immutable public interface IncaPropertyFieldInfo
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfo.Builder': ...
    def getAssociatedPropertyField(self) -> cern.lsa.domain.devices.type.PropertyField: ...
    def getControlWarningMessage(self) -> str: ...
    def getDisplayFormat(self) -> str: ...
    def getDisplayName(self) -> str: ...
    def getParameterValueCompareType(self) -> 'IncaPropertyFieldInfo.ValueCompareType':
        """
            Returns the comparison type that should be applied for this parameter type when calculating value status.
        
            Returns:
                type of parameter value comparison
        
        
        """
        ...
    def getPropertyField(self) -> cern.lsa.domain.devices.type.PropertyField:
        """
        
            Returns:
                property-field this info is attached to
        
        
        """
        ...
    def isMainStatus(self) -> bool:
        """
            Indicates if this parameter type represents the main status property for given device type. The main status property
            typically indicates if the device is enabled, disabled or in a faulty state. It's value type is either an enumeration or
            boolean. Note that for a given device type, only a single parameter type can represent the main status.
        
            Returns:
                :code:`true` if this parameter type represents the main status property field
        
        
        """
        ...
    class ValueCompareType(java.lang.Enum['IncaPropertyFieldInfo.ValueCompareType']):
        EXACT_MEANING: typing.ClassVar['IncaPropertyFieldInfo.ValueCompareType'] = ...
        TOL_REL: typing.ClassVar['IncaPropertyFieldInfo.ValueCompareType'] = ...
        TOL_ABS: typing.ClassVar['IncaPropertyFieldInfo.ValueCompareType'] = ...
        EXACT: typing.ClassVar['IncaPropertyFieldInfo.ValueCompareType'] = ...
        TOL_ABS_REL: typing.ClassVar['IncaPropertyFieldInfo.ValueCompareType'] = ...
        TOL_ABS_MOD360: typing.ClassVar['IncaPropertyFieldInfo.ValueCompareType'] = ...
        NONE: typing.ClassVar['IncaPropertyFieldInfo.ValueCompareType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'IncaPropertyFieldInfo.ValueCompareType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['IncaPropertyFieldInfo.ValueCompareType']: ...

class IncaPropertyFieldInfosRequest:
    """
    @Immutable public interface IncaPropertyFieldInfosRequest
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfosRequest.Builder': ...
    @staticmethod
    def byPropertyField(propertyField: cern.lsa.domain.devices.type.PropertyField) -> 'IncaPropertyFieldInfosRequest': ...
    @staticmethod
    def byPropertyFields(set: java.util.Set[cern.lsa.domain.devices.type.PropertyField]) -> 'IncaPropertyFieldInfosRequest': ...
    def getPropertyFields(self) -> java.util.Set[cern.lsa.domain.devices.type.PropertyField]: ...

class DefaultIncaPropertyFieldInfo(IncaPropertyFieldInfo, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultIncaPropertyFieldInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo`.
    
        Use the builder to create immutable instances: :code:`DefaultIncaPropertyFieldInfo.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfo.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.devices.inca.DefaultIncaPropertyFieldInfo`.
        
            .. code-block: java
            
             DefaultIncaPropertyFieldInfo.builder()
                .propertyField(cern.lsa.domain.devices.type.PropertyField) // required :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.getPropertyField`
                .displayName(String | null) // nullable :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.getDisplayName`
                .mainStatus(boolean) // required :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.isMainStatus`
                .associatedPropertyField(cern.lsa.domain.devices.type.PropertyField | null) // nullable :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.getAssociatedPropertyField`
                .controlWarningMessage(String | null) // nullable :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.getControlWarningMessage`
                .parameterValueCompareType(cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.ValueCompareType) // required :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.getParameterValueCompareType`
                .displayFormat(String | null) // nullable :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.getDisplayFormat`
                .build();
             
        
            Returns:
                A new DefaultIncaPropertyFieldInfo builder
        
        
        """
        ...
    @staticmethod
    def copyOf(incaPropertyFieldInfo: IncaPropertyFieldInfo) -> 'DefaultIncaPropertyFieldInfo':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo` value. Uses accessors to get
            values to initialize the new immutable instance. If an instance is already immutable, it is returned as is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo`): The instance to copy
        
            Returns:
                A copied immutable IncaPropertyFieldInfo instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAssociatedPropertyField(self) -> cern.lsa.domain.devices.type.PropertyField: ...
    def getControlWarningMessage(self) -> str: ...
    def getDisplayFormat(self) -> str: ...
    def getDisplayName(self) -> str: ...
    def getParameterValueCompareType(self) -> IncaPropertyFieldInfo.ValueCompareType:
        """
            Returns the comparison type that should be applied for this parameter type when calculating value status.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.getParameterValueCompareType`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo`
        
            Returns:
                type of parameter value comparison
        
        
        """
        ...
    def getPropertyField(self) -> cern.lsa.domain.devices.type.PropertyField:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.getPropertyField`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo`
        
            Returns:
                property-field this info is attached to
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`propertyField`, :code:`displayName`, :code:`mainStatus`,
            :code:`associatedPropertyField`, :code:`controlWarningMessage`, :code:`parameterValueCompareType`,
            :code:`displayFormat`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def isMainStatus(self) -> bool:
        """
            Indicates if this parameter type represents the main status property for given device type. The main status property
            typically indicates if the device is enabled, disabled or in a faulty state. It's value type is either an enumeration or
            boolean. Note that for a given device type, only a single parameter type can represent the main status.
        
            Specified by:
                :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.isMainStatus`Â in
                interfaceÂ :class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo`
        
            Returns:
                :code:`true` if this parameter type represents the main status property field
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`IncaPropertyFieldInfo` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    def withAssociatedPropertyField(self, propertyField: cern.lsa.domain.devices.type.PropertyField) -> 'DefaultIncaPropertyFieldInfo': ...
    def withControlWarningMessage(self, string: str) -> 'DefaultIncaPropertyFieldInfo': ...
    def withDisplayFormat(self, string: str) -> 'DefaultIncaPropertyFieldInfo': ...
    def withDisplayName(self, string: str) -> 'DefaultIncaPropertyFieldInfo': ...
    def withMainStatus(self, boolean: bool) -> 'DefaultIncaPropertyFieldInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.isMainStatus` attribute. A value equality check is used to
            prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (boolean): A new value for mainStatus
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withParameterValueCompareType(self, valueCompareType: IncaPropertyFieldInfo.ValueCompareType) -> 'DefaultIncaPropertyFieldInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.getParameterValueCompareType` attribute. A value equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.ValueCompareType`): A new value for parameterValueCompareType
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    def withPropertyField(self, propertyField: cern.lsa.domain.devices.type.PropertyField) -> 'DefaultIncaPropertyFieldInfo':
        """
            Copy the current immutable object by setting a value for the
            :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfo.getPropertyField` attribute. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                value (:class:`~cern.lsa.domain.devices.type.PropertyField`): A new value for propertyField
        
            Returns:
                A modified copy of the :code:`this` object
        
        
        """
        ...
    class Builder:
        def associatedPropertyField(self, propertyField: cern.lsa.domain.devices.type.PropertyField) -> 'DefaultIncaPropertyFieldInfo.Builder': ...
        def build(self) -> 'DefaultIncaPropertyFieldInfo': ...
        def controlWarningMessage(self, string: str) -> 'DefaultIncaPropertyFieldInfo.Builder': ...
        def displayFormat(self, string: str) -> 'DefaultIncaPropertyFieldInfo.Builder': ...
        def displayName(self, string: str) -> 'DefaultIncaPropertyFieldInfo.Builder': ...
        def mainStatus(self, boolean: bool) -> 'DefaultIncaPropertyFieldInfo.Builder': ...
        def parameterValueCompareType(self, valueCompareType: IncaPropertyFieldInfo.ValueCompareType) -> 'DefaultIncaPropertyFieldInfo.Builder': ...
        def propertyField(self, propertyField: cern.lsa.domain.devices.type.PropertyField) -> 'DefaultIncaPropertyFieldInfo.Builder': ...

class DefaultIncaPropertyFieldInfosRequest(IncaPropertyFieldInfosRequest, java.io.Serializable):
    """
    `@ParametersAreNonnullByDefault <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/ParametersAreNonnullByDefault.html?is-external=true>` `@Generated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Generated.html?is-external=true>`("org.immutables.processor.ProxyProcessor") @Immutable `@CheckReturnValue <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/CheckReturnValue.html?is-external=true>` public final class DefaultIncaPropertyFieldInfosRequest extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfosRequest`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Immutable implementation of :class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfosRequest`.
    
        Use the builder to create immutable instances: :code:`DefaultIncaPropertyFieldInfosRequest.builder()`.
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'DefaultIncaPropertyFieldInfosRequest.Builder':
        """
            Creates a builder for :class:`~cern.lsa.domain.devices.inca.DefaultIncaPropertyFieldInfosRequest`.
        
            .. code-block: java
            
             DefaultIncaPropertyFieldInfosRequest.builder()
                .addPropertyField|addAllPropertyFields(cern.lsa.domain.devices.type.PropertyField) // :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfosRequest.getPropertyFields` elements
                .build();
             
        
            Returns:
                A new DefaultIncaPropertyFieldInfosRequest builder
        
        
        """
        ...
    @staticmethod
    def copyOf(incaPropertyFieldInfosRequest: IncaPropertyFieldInfosRequest) -> 'DefaultIncaPropertyFieldInfosRequest':
        """
            Creates an immutable copy of a :class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfosRequest` value. Uses
            accessors to get values to initialize the new immutable instance. If an instance is already immutable, it is returned as
            is.
        
            Parameters:
                instance (:class:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfosRequest`): The instance to copy
        
            Returns:
                A copied immutable IncaPropertyFieldInfosRequest instance
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool: ...
    def getPropertyFields(self) -> java.util.Set[cern.lsa.domain.devices.type.PropertyField]: ...
    def hashCode(self) -> int:
        """
            Computes a hash code from attributes: :code:`propertyFields`.
        
            Overrides:
                 in class 
        
            Returns:
                hashCode value
        
        
        """
        ...
    def toString(self) -> str:
        """
            Prints the immutable value :code:`IncaPropertyFieldInfosRequest` with attribute values.
        
            Overrides:
                 in class 
        
            Returns:
                A string representation of the value
        
        
        """
        ...
    @typing.overload
    def withPropertyFields(self, propertyFieldArray: typing.List[cern.lsa.domain.devices.type.PropertyField]) -> 'DefaultIncaPropertyFieldInfosRequest':
        """
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfosRequest.getPropertyFields`.
        
            Parameters:
                elements (:class:`~cern.lsa.domain.devices.type.PropertyField`...): The elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        public final :class:`~cern.lsa.domain.devices.inca.DefaultIncaPropertyFieldInfosRequest` withPropertyFields (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.devices.type.PropertyField`> elements)
        
            Copy the current immutable object with elements that replace the content of
            :meth:`~cern.lsa.domain.devices.inca.IncaPropertyFieldInfosRequest.getPropertyFields`. A shallow reference equality
            check is used to prevent copying of the same value by returning :code:`this`.
        
            Parameters:
                elements (`Iterable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Iterable.html?is-external=true>`<? extends :class:`~cern.lsa.domain.devices.type.PropertyField`> elements): An iterable of propertyFields elements to set
        
            Returns:
                A modified copy of :code:`this` object
        
        
        """
        ...
    @typing.overload
    def withPropertyFields(self, iterable: java.lang.Iterable[cern.lsa.domain.devices.type.PropertyField]) -> 'DefaultIncaPropertyFieldInfosRequest': ...
    class Builder:
        def addAllPropertyFields(self, iterable: java.lang.Iterable[cern.lsa.domain.devices.type.PropertyField]) -> 'DefaultIncaPropertyFieldInfosRequest.Builder': ...
        def addPropertyField(self, propertyField: cern.lsa.domain.devices.type.PropertyField) -> 'DefaultIncaPropertyFieldInfosRequest.Builder': ...
        def addPropertyFields(self, propertyFieldArray: typing.List[cern.lsa.domain.devices.type.PropertyField]) -> 'DefaultIncaPropertyFieldInfosRequest.Builder': ...
        def build(self) -> 'DefaultIncaPropertyFieldInfosRequest': ...
        def propertyFields(self, iterable: java.lang.Iterable[cern.lsa.domain.devices.type.PropertyField]) -> 'DefaultIncaPropertyFieldInfosRequest.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.devices.inca")``.

    DefaultIncaPropertyFieldInfo: typing.Type[DefaultIncaPropertyFieldInfo]
    DefaultIncaPropertyFieldInfosRequest: typing.Type[DefaultIncaPropertyFieldInfosRequest]
    IncaPropertyFieldInfo: typing.Type[IncaPropertyFieldInfo]
    IncaPropertyFieldInfosRequest: typing.Type[IncaPropertyFieldInfosRequest]
