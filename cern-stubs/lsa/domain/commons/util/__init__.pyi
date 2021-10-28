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
    Java class 'cern.lsa.domain.commons.util.Attributes'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Attributes()
    
      Attributes:
        MAX_ATTRIBUTE_VALUE_LENGTH (int): final static field
    
    """
    MAX_ATTRIBUTE_VALUE_LENGTH: typing.ClassVar[int] = ...
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def assertCanWriteAttributes(object: typing.Any) -> cern.lsa.domain.commons.AttributeWritableAware: ...
    @typing.overload
    @staticmethod
    def assertCanWriteAttributes(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> java.util.Collection[cern.lsa.domain.commons.AttributeWritableAware]: ...
    @staticmethod
    def assertCorrectlyConstructedAttribute(attribute: cern.lsa.domain.commons.Attribute) -> None: ...
    @staticmethod
    def assertCorrectlyConstructedAttributes(collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.Attribute], typing.Sequence[cern.lsa.domain.commons.Attribute]]) -> None: ...
    @staticmethod
    def assertEntitiesHaveAllAttributes(collection: typing.Union[java.util.Collection[cern.lsa.domain.commons.AttributeDefinition], typing.Sequence[cern.lsa.domain.commons.AttributeDefinition]], collection2: typing.Union[java.util.Collection[cern.lsa.domain.commons.AttributeAware], typing.Sequence[cern.lsa.domain.commons.AttributeAware]]) -> None: ...
    @staticmethod
    def assertValidAttributeValue(attributeDefinition: cern.lsa.domain.commons.AttributeDefinition, string: str) -> None: ...
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
    def validateAttributeValue(attributeDefinition: cern.lsa.domain.commons.AttributeDefinition, string: str) -> 'Attributes.AttributeValidationResult': ...
    class AttributeValidationResult:
        """
        Java class 'cern.lsa.domain.commons.util.Attributes$AttributeValidationResult'
        
            Extends:
                java.lang.Object
        
        """
        def getErrorMessage(self) -> str: ...
        def isValid(self) -> bool: ...

class CacheUtil:
    """
    Java class 'cern.lsa.domain.commons.util.CacheUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * CacheUtil()
    
    """
    def __init__(self): ...
    @staticmethod
    def generateCacheKey(object: typing.Any, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any]) -> str: ...

class TimeUtils:
    """
    Java class 'cern.lsa.domain.commons.util.TimeUtils'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def convertToTimestamp(instant: typing.Union[java.time.Instant, datetime.datetime]) -> java.sql.Timestamp: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons.util")``.

    Attributes: typing.Type[Attributes]
    CacheUtil: typing.Type[CacheUtil]
    TimeUtils: typing.Type[TimeUtils]
    format: cern.lsa.domain.commons.util.format.__module_protocol__
