import java.lang
import java.lang.reflect
import typing



class Annotation:
    """
    Java class 'java.lang.annotation.Annotation'
    
    """
    def annotationType(self) -> typing.Type['Annotation']: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class AnnotationFormatError(java.lang.Error):
    """
    Java class 'java.lang.annotation.AnnotationFormatError'
    
        Extends:
            java.lang.Error
    
      Constructors:
        * AnnotationFormatError(java.lang.String)
        * AnnotationFormatError(java.lang.String, java.lang.Throwable)
        * AnnotationFormatError(java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class AnnotationTypeMismatchException(java.lang.RuntimeException):
    """
    Java class 'java.lang.annotation.AnnotationTypeMismatchException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * AnnotationTypeMismatchException(java.lang.reflect.Method, java.lang.String)
    
    """
    def __init__(self, method: java.lang.reflect.Method, string: str): ...
    def element(self) -> java.lang.reflect.Method: ...
    def foundType(self) -> str: ...

class ElementType(java.lang.Enum['ElementType']):
    """
    Java class 'java.lang.annotation.ElementType'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        TYPE (java.lang.annotation.ElementType): final static enum constant
        FIELD (java.lang.annotation.ElementType): final static enum constant
        METHOD (java.lang.annotation.ElementType): final static enum constant
        PARAMETER (java.lang.annotation.ElementType): final static enum constant
        CONSTRUCTOR (java.lang.annotation.ElementType): final static enum constant
        LOCAL_VARIABLE (java.lang.annotation.ElementType): final static enum constant
        ANNOTATION_TYPE (java.lang.annotation.ElementType): final static enum constant
        PACKAGE (java.lang.annotation.ElementType): final static enum constant
        TYPE_PARAMETER (java.lang.annotation.ElementType): final static enum constant
        TYPE_USE (java.lang.annotation.ElementType): final static enum constant
        MODULE (java.lang.annotation.ElementType): final static enum constant
    
    """
    TYPE: typing.ClassVar['ElementType'] = ...
    FIELD: typing.ClassVar['ElementType'] = ...
    METHOD: typing.ClassVar['ElementType'] = ...
    PARAMETER: typing.ClassVar['ElementType'] = ...
    CONSTRUCTOR: typing.ClassVar['ElementType'] = ...
    LOCAL_VARIABLE: typing.ClassVar['ElementType'] = ...
    ANNOTATION_TYPE: typing.ClassVar['ElementType'] = ...
    PACKAGE: typing.ClassVar['ElementType'] = ...
    TYPE_PARAMETER: typing.ClassVar['ElementType'] = ...
    TYPE_USE: typing.ClassVar['ElementType'] = ...
    MODULE: typing.ClassVar['ElementType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ElementType': ...
    @staticmethod
    def values() -> typing.List['ElementType']: ...

class IncompleteAnnotationException(java.lang.RuntimeException):
    """
    Java class 'java.lang.annotation.IncompleteAnnotationException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * IncompleteAnnotationException(java.lang.Class, java.lang.String)
    
    """
    def __init__(self, class_: typing.Type[Annotation], string: str): ...
    def annotationType(self) -> typing.Type[Annotation]: ...
    def elementName(self) -> str: ...

class RetentionPolicy(java.lang.Enum['RetentionPolicy']):
    """
    Java class 'java.lang.annotation.RetentionPolicy'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        SOURCE (java.lang.annotation.RetentionPolicy): final static enum constant
        CLASS (java.lang.annotation.RetentionPolicy): final static enum constant
        RUNTIME (java.lang.annotation.RetentionPolicy): final static enum constant
    
    """
    SOURCE: typing.ClassVar['RetentionPolicy'] = ...
    CLASS: typing.ClassVar['RetentionPolicy'] = ...
    RUNTIME: typing.ClassVar['RetentionPolicy'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RetentionPolicy': ...
    @staticmethod
    def values() -> typing.List['RetentionPolicy']: ...

class Documented(Annotation):
    """
    Java class 'java.lang.annotation.Documented'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class Inherited(Annotation):
    """
    Java class 'java.lang.annotation.Inherited'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class Native(Annotation):
    """
    Java class 'java.lang.annotation.Native'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class Repeatable(Annotation):
    """
    Java class 'java.lang.annotation.Repeatable'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def value(self) -> typing.Type[Annotation]: ...

class Retention(Annotation):
    """
    Java class 'java.lang.annotation.Retention'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def value(self) -> RetentionPolicy: ...

class Target(Annotation):
    """
    Java class 'java.lang.annotation.Target'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def value(self) -> typing.List[ElementType]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.lang.annotation")``.

    Annotation: typing.Type[Annotation]
    AnnotationFormatError: typing.Type[AnnotationFormatError]
    AnnotationTypeMismatchException: typing.Type[AnnotationTypeMismatchException]
    Documented: typing.Type[Documented]
    ElementType: typing.Type[ElementType]
    IncompleteAnnotationException: typing.Type[IncompleteAnnotationException]
    Inherited: typing.Type[Inherited]
    Native: typing.Type[Native]
    Repeatable: typing.Type[Repeatable]
    Retention: typing.Type[Retention]
    RetentionPolicy: typing.Type[RetentionPolicy]
    Target: typing.Type[Target]
