from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import Generic as _py_Generic
from typing import overload
import java.io
import java.lang
import java.lang.annotation
import java.security
import java.util.function
import sun.reflect


class AnnotatedElement:
    _getAnnotation__T = _py_TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: _py_Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getAnnotations(self) -> _py_List[java.lang.annotation.Annotation]: ...
    _getAnnotationsByType__T = _py_TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: _py_Type[_getAnnotationsByType__T]) -> _py_List[_getAnnotationsByType__T]: ...
    _getDeclaredAnnotation__T = _py_TypeVar('_getDeclaredAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotation(self, class_: _py_Type[_getDeclaredAnnotation__T]) -> _getDeclaredAnnotation__T: ...
    def getDeclaredAnnotations(self) -> _py_List[java.lang.annotation.Annotation]: ...
    _getDeclaredAnnotationsByType__T = _py_TypeVar('_getDeclaredAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotationsByType(self, class_: _py_Type[_getDeclaredAnnotationsByType__T]) -> _py_List[_getDeclaredAnnotationsByType__T]: ...
    def isAnnotationPresent(self, class_: _py_Type[java.lang.annotation.Annotation]) -> bool: ...

class Array:
    @classmethod
    def get(cls, object: _py_Any, int: int) -> _py_Any: ...
    @classmethod
    def getBoolean(cls, object: _py_Any, int: int) -> bool: ...
    @classmethod
    def getByte(cls, object: _py_Any, int: int) -> int: ...
    @classmethod
    def getChar(cls, object: _py_Any, int: int) -> str: ...
    @classmethod
    def getDouble(cls, object: _py_Any, int: int) -> float: ...
    @classmethod
    def getFloat(cls, object: _py_Any, int: int) -> float: ...
    @classmethod
    def getInt(cls, object: _py_Any, int: int) -> int: ...
    @classmethod
    def getLength(cls, object: _py_Any) -> int: ...
    @classmethod
    def getLong(cls, object: _py_Any, int: int) -> int: ...
    @classmethod
    def getShort(cls, object: _py_Any, int: int) -> int: ...
    @classmethod
    @overload
    def newInstance(cls, class_: _py_Type[_py_Any], int: int) -> _py_Any: ...
    @classmethod
    @overload
    def newInstance(cls, class_: _py_Type[_py_Any], intArray: _py_List[int]) -> _py_Any: ...
    @classmethod
    def set(cls, object: _py_Any, int: int, object2: _py_Any) -> None: ...
    @classmethod
    def setBoolean(cls, object: _py_Any, int: int, boolean: bool) -> None: ...
    @classmethod
    def setByte(cls, object: _py_Any, int: int, byte: int) -> None: ...
    @classmethod
    def setChar(cls, object: _py_Any, int: int, char: str) -> None: ...
    @classmethod
    def setDouble(cls, object: _py_Any, int: int, double: float) -> None: ...
    @classmethod
    def setFloat(cls, object: _py_Any, int: int, float: float) -> None: ...
    @classmethod
    def setInt(cls, object: _py_Any, int: int, int2: int) -> None: ...
    @classmethod
    def setLong(cls, object: _py_Any, int: int, long: int) -> None: ...
    @classmethod
    def setShort(cls, object: _py_Any, int: int, short: int) -> None: ...

class GenericSignatureFormatError(java.lang.ClassFormatError):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, string: str): ...

class InvocationHandler:
    def invoke(self, object: _py_Any, method: 'Method', objectArray: _py_List[_py_Any]) -> _py_Any: ...

class InvocationTargetException(java.lang.ReflectiveOperationException):
    @overload
    def __init__(self, throwable: java.lang.Throwable): ...
    @overload
    def __init__(self, throwable: java.lang.Throwable, string: str): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getTargetException(self) -> java.lang.Throwable: ...

class MalformedParameterizedTypeException(java.lang.RuntimeException):
    def __init__(self): ...

class MalformedParametersException(java.lang.RuntimeException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, string: str): ...

class Member:
    PUBLIC: _py_ClassVar[int] = ...
    DECLARED: _py_ClassVar[int] = ...
    def getDeclaringClass(self) -> _py_Type[_py_Any]: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def isSynthetic(self) -> bool: ...

class Modifier:
    PUBLIC: _py_ClassVar[int] = ...
    PRIVATE: _py_ClassVar[int] = ...
    PROTECTED: _py_ClassVar[int] = ...
    STATIC: _py_ClassVar[int] = ...
    FINAL: _py_ClassVar[int] = ...
    SYNCHRONIZED: _py_ClassVar[int] = ...
    VOLATILE: _py_ClassVar[int] = ...
    TRANSIENT: _py_ClassVar[int] = ...
    NATIVE: _py_ClassVar[int] = ...
    INTERFACE: _py_ClassVar[int] = ...
    ABSTRACT: _py_ClassVar[int] = ...
    STRICT: _py_ClassVar[int] = ...
    def __init__(self): ...
    @classmethod
    def classModifiers(cls) -> int: ...
    @classmethod
    def constructorModifiers(cls) -> int: ...
    @classmethod
    def fieldModifiers(cls) -> int: ...
    @classmethod
    def interfaceModifiers(cls) -> int: ...
    @classmethod
    def isAbstract(cls, int: int) -> bool: ...
    @classmethod
    def isFinal(cls, int: int) -> bool: ...
    @classmethod
    def isInterface(cls, int: int) -> bool: ...
    @classmethod
    def isNative(cls, int: int) -> bool: ...
    @classmethod
    def isPrivate(cls, int: int) -> bool: ...
    @classmethod
    def isProtected(cls, int: int) -> bool: ...
    @classmethod
    def isPublic(cls, int: int) -> bool: ...
    @classmethod
    def isStatic(cls, int: int) -> bool: ...
    @classmethod
    def isStrict(cls, int: int) -> bool: ...
    @classmethod
    def isSynchronized(cls, int: int) -> bool: ...
    @classmethod
    def isTransient(cls, int: int) -> bool: ...
    @classmethod
    def isVolatile(cls, int: int) -> bool: ...
    @classmethod
    def methodModifiers(cls) -> int: ...
    @classmethod
    def parameterModifiers(cls) -> int: ...
    @overload
    def toString(self) -> str: ...
    @classmethod
    @overload
    def toString(cls, int: int) -> str: ...

class Proxy(java.io.Serializable):
    @classmethod
    def getInvocationHandler(cls, object: _py_Any) -> InvocationHandler: ...
    @classmethod
    def getProxyClass(cls, classLoader: java.lang.ClassLoader, classArray: _py_List[_py_Type[_py_Any]]) -> _py_Type[_py_Any]: ...
    @classmethod
    def isProxyClass(cls, class_: _py_Type[_py_Any]) -> bool: ...
    @classmethod
    def newProxyInstance(cls, classLoader: java.lang.ClassLoader, classArray: _py_List[_py_Type[_py_Any]], invocationHandler: InvocationHandler) -> _py_Any: ...

class ReflectAccess(sun.reflect.LangReflectAccess):
    _copyConstructor__T = _py_TypeVar('_copyConstructor__T')  # <T>
    def copyConstructor(self, constructor: 'Constructor'[_copyConstructor__T]) -> 'Constructor'[_copyConstructor__T]: ...
    def copyField(self, field: 'Field') -> 'Field': ...
    def copyMethod(self, method: 'Method') -> 'Method': ...
    def getConstructorAccessor(self, constructor: 'Constructor'[_py_Any]) -> sun.reflect.ConstructorAccessor: ...
    def getConstructorAnnotations(self, constructor: 'Constructor'[_py_Any]) -> _py_List[int]: ...
    def getConstructorParameterAnnotations(self, constructor: 'Constructor'[_py_Any]) -> _py_List[int]: ...
    def getConstructorSignature(self, constructor: 'Constructor'[_py_Any]) -> str: ...
    def getConstructorSlot(self, constructor: 'Constructor'[_py_Any]) -> int: ...
    def getExecutableTypeAnnotationBytes(self, executable: 'Executable') -> _py_List[int]: ...
    def getMethodAccessor(self, method: 'Method') -> sun.reflect.MethodAccessor: ...
    _newConstructor__T = _py_TypeVar('_newConstructor__T')  # <T>
    def newConstructor(self, class_: _py_Type[_newConstructor__T], classArray: _py_List[_py_Type[_py_Any]], classArray2: _py_List[_py_Type[_py_Any]], int: int, int2: int, string: str, byteArray: _py_List[int], byteArray2: _py_List[int]) -> 'Constructor'[_newConstructor__T]: ...
    def newField(self, class_: _py_Type[_py_Any], string: str, class2: _py_Type[_py_Any], int: int, int2: int, string2: str, byteArray: _py_List[int]) -> 'Field': ...
    def newMethod(self, class_: _py_Type[_py_Any], string: str, classArray: _py_List[_py_Type[_py_Any]], class3: _py_Type[_py_Any], classArray2: _py_List[_py_Type[_py_Any]], int: int, int2: int, string2: str, byteArray: _py_List[int], byteArray2: _py_List[int], byteArray3: _py_List[int]) -> 'Method': ...
    def setConstructorAccessor(self, constructor: 'Constructor'[_py_Any], constructorAccessor: sun.reflect.ConstructorAccessor) -> None: ...
    def setMethodAccessor(self, method: 'Method', methodAccessor: sun.reflect.MethodAccessor) -> None: ...

class ReflectPermission(java.security.BasicPermission):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, string2: str): ...

class Type:
    def getTypeName(self) -> str: ...

class UndeclaredThrowableException(java.lang.RuntimeException):
    @overload
    def __init__(self, throwable: java.lang.Throwable): ...
    @overload
    def __init__(self, throwable: java.lang.Throwable, string: str): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getUndeclaredThrowable(self) -> java.lang.Throwable: ...

_WeakCache__K = _py_TypeVar('_WeakCache__K')  # <K>
_WeakCache__P = _py_TypeVar('_WeakCache__P')  # <P>
_WeakCache__V = _py_TypeVar('_WeakCache__V')  # <V>
class WeakCache(_py_Generic[_WeakCache__K, _WeakCache__P, _WeakCache__V]):
    def __init__(self, biFunction: java.util.function.BiFunction[_WeakCache__K, _WeakCache__P, _py_Any], biFunction2: java.util.function.BiFunction[_WeakCache__K, _WeakCache__P, _WeakCache__V]): ...
    def containsValue(self, v: _WeakCache__V) -> bool: ...
    def get(self, k: _WeakCache__K, p: _WeakCache__P) -> _WeakCache__V: ...
    def size(self) -> int: ...

class AccessibleObject(AnnotatedElement):
    _getAnnotation__T = _py_TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: _py_Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getAnnotations(self) -> _py_List[java.lang.annotation.Annotation]: ...
    _getAnnotationsByType__T = _py_TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: _py_Type[_getAnnotationsByType__T]) -> _py_List[_getAnnotationsByType__T]: ...
    _getDeclaredAnnotation__T = _py_TypeVar('_getDeclaredAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotation(self, class_: _py_Type[_getDeclaredAnnotation__T]) -> _getDeclaredAnnotation__T: ...
    def getDeclaredAnnotations(self) -> _py_List[java.lang.annotation.Annotation]: ...
    _getDeclaredAnnotationsByType__T = _py_TypeVar('_getDeclaredAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotationsByType(self, class_: _py_Type[_getDeclaredAnnotationsByType__T]) -> _py_List[_getDeclaredAnnotationsByType__T]: ...
    def isAccessible(self) -> bool: ...
    def isAnnotationPresent(self, class_: _py_Type[java.lang.annotation.Annotation]) -> bool: ...
    @classmethod
    @overload
    def setAccessible(cls, accessibleObjectArray: _py_List['AccessibleObject'], boolean: bool) -> None: ...
    @overload
    def setAccessible(self, boolean: bool) -> None: ...

class AnnotatedType(AnnotatedElement):
    def getType(self) -> Type: ...

class GenericArrayType(Type):
    def getGenericComponentType(self) -> Type: ...

class GenericDeclaration(AnnotatedElement):
    def getTypeParameters(self) -> _py_List['TypeVariable'[_py_Any]]: ...

class Parameter(AnnotatedElement):
    def equals(self, object: _py_Any) -> bool: ...
    def getAnnotatedType(self) -> AnnotatedType: ...
    _getAnnotation__T = _py_TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: _py_Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getAnnotations(self) -> _py_List[java.lang.annotation.Annotation]: ...
    _getAnnotationsByType__T = _py_TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: _py_Type[_getAnnotationsByType__T]) -> _py_List[_getAnnotationsByType__T]: ...
    _getDeclaredAnnotation__T = _py_TypeVar('_getDeclaredAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotation(self, class_: _py_Type[_getDeclaredAnnotation__T]) -> _getDeclaredAnnotation__T: ...
    def getDeclaredAnnotations(self) -> _py_List[java.lang.annotation.Annotation]: ...
    _getDeclaredAnnotationsByType__T = _py_TypeVar('_getDeclaredAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotationsByType(self, class_: _py_Type[_getDeclaredAnnotationsByType__T]) -> _py_List[_getDeclaredAnnotationsByType__T]: ...
    def getDeclaringExecutable(self) -> 'Executable': ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getParameterizedType(self) -> Type: ...
    def getType(self) -> _py_Type[_py_Any]: ...
    def hashCode(self) -> int: ...
    def isImplicit(self) -> bool: ...
    def isNamePresent(self) -> bool: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    def toString(self) -> str: ...

class ParameterizedType(Type):
    def getActualTypeArguments(self) -> _py_List[Type]: ...
    def getOwnerType(self) -> Type: ...
    def getRawType(self) -> Type: ...

_TypeVariable__D = _py_TypeVar('_TypeVariable__D', bound=GenericDeclaration)  # <D>
class TypeVariable(Type, AnnotatedElement, _py_Generic[_TypeVariable__D]):
    def getAnnotatedBounds(self) -> _py_List[AnnotatedType]: ...
    def getBounds(self) -> _py_List[Type]: ...
    def getGenericDeclaration(self) -> _TypeVariable__D: ...
    def getName(self) -> str: ...

class WildcardType(Type):
    def getLowerBounds(self) -> _py_List[Type]: ...
    def getUpperBounds(self) -> _py_List[Type]: ...

class AnnotatedArrayType(AnnotatedType):
    def getAnnotatedGenericComponentType(self) -> AnnotatedType: ...

class AnnotatedParameterizedType(AnnotatedType):
    def getAnnotatedActualTypeArguments(self) -> _py_List[AnnotatedType]: ...

class AnnotatedTypeVariable(AnnotatedType):
    def getAnnotatedBounds(self) -> _py_List[AnnotatedType]: ...

class AnnotatedWildcardType(AnnotatedType):
    def getAnnotatedLowerBounds(self) -> _py_List[AnnotatedType]: ...
    def getAnnotatedUpperBounds(self) -> _py_List[AnnotatedType]: ...

class Executable(AccessibleObject, Member, GenericDeclaration):
    def getAnnotatedExceptionTypes(self) -> _py_List[AnnotatedType]: ...
    def getAnnotatedParameterTypes(self) -> _py_List[AnnotatedType]: ...
    def getAnnotatedReceiverType(self) -> AnnotatedType: ...
    def getAnnotatedReturnType(self) -> AnnotatedType: ...
    _getAnnotation__T = _py_TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: _py_Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    _getAnnotationsByType__T = _py_TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: _py_Type[_getAnnotationsByType__T]) -> _py_List[_getAnnotationsByType__T]: ...
    def getDeclaredAnnotations(self) -> _py_List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> _py_Type[_py_Any]: ...
    def getExceptionTypes(self) -> _py_List[_py_Type[_py_Any]]: ...
    def getGenericExceptionTypes(self) -> _py_List[Type]: ...
    def getGenericParameterTypes(self) -> _py_List[Type]: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getParameterAnnotations(self) -> _py_List[_py_List[java.lang.annotation.Annotation]]: ...
    def getParameterCount(self) -> int: ...
    def getParameterTypes(self) -> _py_List[_py_Type[_py_Any]]: ...
    def getParameters(self) -> _py_List[Parameter]: ...
    def getTypeParameters(self) -> _py_List[TypeVariable[_py_Any]]: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    def toGenericString(self) -> str: ...

class Field(AccessibleObject, Member):
    def equals(self, object: _py_Any) -> bool: ...
    def get(self, object: _py_Any) -> _py_Any: ...
    def getAnnotatedType(self) -> AnnotatedType: ...
    _getAnnotation__T = _py_TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: _py_Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    _getAnnotationsByType__T = _py_TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: _py_Type[_getAnnotationsByType__T]) -> _py_List[_getAnnotationsByType__T]: ...
    def getBoolean(self, object: _py_Any) -> bool: ...
    def getByte(self, object: _py_Any) -> int: ...
    def getChar(self, object: _py_Any) -> str: ...
    def getDeclaredAnnotations(self) -> _py_List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> _py_Type[_py_Any]: ...
    def getDouble(self, object: _py_Any) -> float: ...
    def getFloat(self, object: _py_Any) -> float: ...
    def getGenericType(self) -> Type: ...
    def getInt(self, object: _py_Any) -> int: ...
    def getLong(self, object: _py_Any) -> int: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getShort(self, object: _py_Any) -> int: ...
    def getType(self) -> _py_Type[_py_Any]: ...
    def hashCode(self) -> int: ...
    def isEnumConstant(self) -> bool: ...
    def isSynthetic(self) -> bool: ...
    def set(self, object: _py_Any, object2: _py_Any) -> None: ...
    def setBoolean(self, object: _py_Any, boolean: bool) -> None: ...
    def setByte(self, object: _py_Any, byte: int) -> None: ...
    def setChar(self, object: _py_Any, char: str) -> None: ...
    def setDouble(self, object: _py_Any, double: float) -> None: ...
    def setFloat(self, object: _py_Any, float: float) -> None: ...
    def setInt(self, object: _py_Any, int: int) -> None: ...
    def setLong(self, object: _py_Any, long: int) -> None: ...
    def setShort(self, object: _py_Any, short: int) -> None: ...
    def toGenericString(self) -> str: ...
    def toString(self) -> str: ...

_Constructor__T = _py_TypeVar('_Constructor__T')  # <T>
class Constructor(Executable, _py_Generic[_Constructor__T]):
    def equals(self, object: _py_Any) -> bool: ...
    def getAnnotatedReceiverType(self) -> AnnotatedType: ...
    def getAnnotatedReturnType(self) -> AnnotatedType: ...
    _getAnnotation__T = _py_TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: _py_Type[java.lang.annotation.Annotation]) -> java.lang.annotation.Annotation: ...
    def getDeclaredAnnotations(self) -> _py_List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> _py_Type[_Constructor__T]: ...
    def getExceptionTypes(self) -> _py_List[_py_Type[_py_Any]]: ...
    def getGenericExceptionTypes(self) -> _py_List[Type]: ...
    def getGenericParameterTypes(self) -> _py_List[Type]: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getParameterAnnotations(self) -> _py_List[_py_List[java.lang.annotation.Annotation]]: ...
    def getParameterCount(self) -> int: ...
    def getParameterTypes(self) -> _py_List[_py_Type[_py_Any]]: ...
    def getTypeParameters(self) -> _py_List[TypeVariable['Constructor'[_Constructor__T]]]: ...
    def hashCode(self) -> int: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    def newInstance(self, objectArray: _py_List[_py_Any]) -> _Constructor__T: ...
    def toGenericString(self) -> str: ...
    def toString(self) -> str: ...

class Method(Executable):
    def equals(self, object: _py_Any) -> bool: ...
    def getAnnotatedReturnType(self) -> AnnotatedType: ...
    _getAnnotation__T = _py_TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: _py_Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getDeclaredAnnotations(self) -> _py_List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> _py_Type[_py_Any]: ...
    def getDefaultValue(self) -> _py_Any: ...
    def getExceptionTypes(self) -> _py_List[_py_Type[_py_Any]]: ...
    def getGenericExceptionTypes(self) -> _py_List[Type]: ...
    def getGenericParameterTypes(self) -> _py_List[Type]: ...
    def getGenericReturnType(self) -> Type: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getParameterAnnotations(self) -> _py_List[_py_List[java.lang.annotation.Annotation]]: ...
    def getParameterCount(self) -> int: ...
    def getParameterTypes(self) -> _py_List[_py_Type[_py_Any]]: ...
    def getReturnType(self) -> _py_Type[_py_Any]: ...
    def getTypeParameters(self) -> _py_List[TypeVariable['Method']]: ...
    def hashCode(self) -> int: ...
    def invoke(self, object: _py_Any, objectArray: _py_List[_py_Any]) -> _py_Any: ...
    def isBridge(self) -> bool: ...
    def isDefault(self) -> bool: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    def toGenericString(self) -> str: ...
    def toString(self) -> str: ...