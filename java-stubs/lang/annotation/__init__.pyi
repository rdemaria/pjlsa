import java.lang
import java.lang.reflect
import typing


class Annotation:
    def annotationType(self) -> typing.Type['Annotation']: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class AnnotationFormatError(java.lang.Error):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class AnnotationTypeMismatchException(java.lang.RuntimeException):
    def __init__(self, method: java.lang.reflect.Method, string: str): ...
    def element(self) -> java.lang.reflect.Method: ...
    def foundType(self) -> str: ...

class ElementType(java.lang.Enum['ElementType']):
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
    def __init__(self, class_: typing.Type[Annotation], string: str): ...
    def annotationType(self) -> typing.Type[Annotation]: ...
    def elementName(self) -> str: ...

class RetentionPolicy(java.lang.Enum['RetentionPolicy']):
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
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class Inherited(Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class Native(Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class Repeatable(Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def value(self) -> typing.Type[Annotation]: ...

class Retention(Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def value(self) -> RetentionPolicy: ...

class Target(Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def value(self) -> typing.List[ElementType]: ...
