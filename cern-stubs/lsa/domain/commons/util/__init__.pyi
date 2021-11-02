import cern.lsa.domain.commons
import cern.lsa.domain.commons.util.format
import cern.lsa.domain.settings
import datetime
import java.lang.reflect
import java.sql
import java.time
import java.util
import typing



class Attributes:
    """
    public final class Attributes extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Provides static utility methods to be used when working with :class:`~cern.lsa.domain.commons.Attribute`s
    
        Also see:
            Attributes documentation, `INCA-2836 <http://issues/browse/INCA-2836>`,
            :class:`~cern.lsa.domain.commons.AttributeDefinition`, :class:`~cern.lsa.domain.commons.Attribute`
    """
    MAX_ATTRIBUTE_VALUE_LENGTH: typing.ClassVar[int] = ...
    """
    public static final int MAX_ATTRIBUTE_VALUE_LENGTH
    
        This constant should indicate the maximum length of the string representation of an attribute value in the DB
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def assertCanWriteAttributes(object: typing.Any) -> cern.lsa.domain.commons.AttributeWritableAware:
        """
            Assures the given object might be decorated with attributes (implements
            :class:`~cern.lsa.domain.commons.AttributeWritableAware`)
        
            Parameters:
                entity (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): object instance to be checked
        
            Returns:
                entity reference casted to :class:`~cern.lsa.domain.commons.AttributeWritableAware`
        
        public static `Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<:class:`~cern.lsa.domain.commons.AttributeWritableAware`> assertCanWriteAttributes (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<?> entities)
        
            Assures the passed collection of objects might be decorated with attributes (all items implement
            :class:`~cern.lsa.domain.commons.AttributeWritableAware`)
        
            Parameters:
                entities (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<?> entities): entities to be checked
        
            Returns:
                Collection of references to the same objects as AttributeWritableAware
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def assertCanWriteAttributes(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> java.util.Collection[cern.lsa.domain.commons.AttributeWritableAware]: ...
    @staticmethod
    def assertCorrectlyConstructedAttribute(attribute: cern.lsa.domain.commons.Attribute) -> None:
        """
            Checks if the passed attribute has all necessary fields set and if they are in a proper format
        
        """
        ...
    @staticmethod
    def assertCorrectlyConstructedAttributes(collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.Attribute], typing.Sequence[cern.lsa.domain.commons.Attribute]]) -> None: ...
    @staticmethod
    def assertEntitiesHaveAllAttributes(collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.AttributeDefinition], typing.Sequence[cern.lsa.domain.commons.AttributeDefinition]], collection2: typing.Union[java.util.Collection[cern.lsa.domain.commons.AttributeAware], typing.Sequence[cern.lsa.domain.commons.AttributeAware]]) -> None: ...
    @staticmethod
    def assertValidAttributeValue(attributeDefinition: cern.lsa.domain.commons.AttributeDefinition, string: str) -> None:
        """
            Assures the attribute value is correct with respect to the
            :meth:`~cern.lsa.domain.commons.AttributeDefinition.getValueType`
        
            Raises:
                : if there is any problem with the arguments preventing from creating a valid :class:`~cern.lsa.domain.commons.Attribute`
                    out of them
        
            Also see:
                :meth:`~cern.lsa.domain.commons.util.Attributes.validateAttributeValue`
        
        
        """
        ...
    @staticmethod
    def getAttributeDefinitions(collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.Attribute], typing.Sequence[cern.lsa.domain.commons.Attribute]]) -> java.util.Set[cern.lsa.domain.commons.AttributeDefinition]: ...
    @staticmethod
    def getAttributesWithDefaultValues(collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.AttributeDefinition], typing.Sequence[cern.lsa.domain.commons.AttributeDefinition]]) -> java.util.Set[cern.lsa.domain.commons.Attribute]: ...
    _getValue__T = typing.TypeVar('_getValue__T')  # <T>
    @staticmethod
    def getValue(class_: typing.Type[_getValue__T], string: str) -> _getValue__T: ...
    @staticmethod
    def isAttributeAware(contextFamily: cern.lsa.domain.settings.ContextFamily) -> bool: ...
    @staticmethod
    def overrideAttributeValues(attributeWritableAware: cern.lsa.domain.commons.AttributeWritableAware, set: java.util.Set[cern.lsa.domain.commons.Attribute]) -> None: ...
    _overrideDefaultAttributeValues__T = typing.TypeVar('_overrideDefaultAttributeValues__T', bound=cern.lsa.domain.commons.AttributeWritableAware)  # <T>
    @staticmethod
    def overrideDefaultAttributeValues(collection: typing.Union[java.util.Collection[_overrideDefaultAttributeValues__T], typing.Sequence[_overrideDefaultAttributeValues__T]], map: typing.Union[java.util.Map[int, java.util.Set[cern.lsa.domain.commons.Attribute]], typing.Mapping[int, java.util.Set[cern.lsa.domain.commons.Attribute]]]) -> None: ...
    @staticmethod
    def validateAttributeValue(attributeDefinition: cern.lsa.domain.commons.AttributeDefinition, string: str) -> 'Attributes.AttributeValidationResult':
        """
            Validates the given :code:`attributeValue` according to the attribute specification contained in the
            :class:`~cern.lsa.domain.commons.AttributeDefinition`. It returns true if the given value conforms to the
            :class:`~cern.lsa.domain.commons.AttributeDefinition` and false if any error has been encountered.
        
            This method optionally accepts a collection of Strings in order to put there the error descriptions.
        
            Returns:
                true if attributeValue is correct, false otherwise
        
        
        """
        ...
    class AttributeValidationResult:
        def getErrorMessage(self) -> str: ...
        def isValid(self) -> bool: ...

class CacheUtil:
    """
    public class CacheUtil extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class providing common methods for caching.
    """
    def __init__(self): ...
    @staticmethod
    def generateCacheKey(object: typing.Any, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any]) -> str: ...

class TimeUtils:
    """
    public class TimeUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class containing helper methods related to time/date
    """
    @staticmethod
    def convertToTimestamp(instant: typing.Union[java.time.Instant, datetime.datetime]) -> java.sql.Timestamp: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons.util")``.

    Attributes: typing.Type[Attributes]
    CacheUtil: typing.Type[CacheUtil]
    TimeUtils: typing.Type[TimeUtils]
    format: cern.lsa.domain.commons.util.format.__module_protocol__
