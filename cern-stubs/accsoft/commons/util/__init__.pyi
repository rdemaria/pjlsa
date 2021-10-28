import _jpype
import cern
import cern.accsoft.commons.util.annotation
import cern.accsoft.commons.util.collections
import cern.accsoft.commons.util.concurrent
import cern.accsoft.commons.util.enums
import cern.accsoft.commons.util.event
import cern.accsoft.commons.util.executor
import cern.accsoft.commons.util.format
import cern.accsoft.commons.util.jmx
import cern.accsoft.commons.util.mail
import cern.accsoft.commons.util.marker
import cern.accsoft.commons.util.metric
import cern.accsoft.commons.util.proc
import cern.accsoft.commons.util.rba
import cern.accsoft.commons.util.reflect
import cern.accsoft.commons.util.regexp
import cern.accsoft.commons.util.remoting
import cern.accsoft.commons.util.traceid
import cern.accsoft.commons.util.trigger
import cern.accsoft.commons.util.userctx
import cern.accsoft.commons.util.userinfo
import cern.accsoft.commons.util.value
import cern.accsoft.commons.util.xml
import java.awt
import java.beans
import java.io
import java.lang
import java.lang.reflect
import java.net
import java.nio.file
import java.text
import java.util
import java.util.stream
import jpype.protocol
import typing



class AppLauncher:
    """
    Java class 'cern.accsoft.commons.util.AppLauncher'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def launch(stringArray: typing.List[str]) -> None: ...

class ArrayUtils:
    """
    Java class 'cern.accsoft.commons.util.ArrayUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ArrayUtils()
    
    """
    def __init__(self): ...
    @staticmethod
    def addObjectToArray(objectArray: typing.List[typing.Any], object2: typing.Any) -> typing.List[typing.Any]: ...
    _concatenateArrays__T = typing.TypeVar('_concatenateArrays__T')  # <T>
    @staticmethod
    def concatenateArrays(tArray: typing.List[_concatenateArrays__T], tArray2: typing.List[_concatenateArrays__T]) -> typing.List[_concatenateArrays__T]: ...
    @staticmethod
    def isEmpty(objectArray: typing.List[typing.Any]) -> bool: ...
    _toArray__T = typing.TypeVar('_toArray__T')  # <T>
    @staticmethod
    def toArray(collection: typing.Union[java.util.Collection[_toArray__T], typing.Sequence[_toArray__T]], class_: typing.Type[_toArray__T]) -> typing.List[_toArray__T]: ...
    @staticmethod
    def toDoubleArray(collection: typing.Union[java.util.Collection[float], typing.Sequence[float]]) -> typing.List[float]: ...
    @staticmethod
    def toFloatArray(collection: typing.Union[java.util.Collection[float], typing.Sequence[float]]) -> typing.List[float]: ...
    @staticmethod
    def toLongArray(collection: typing.Union[java.util.Collection[int], typing.Sequence[int]]) -> typing.List[int]: ...
    @staticmethod
    def toObjectArray(object: typing.Any) -> typing.List[typing.Any]: ...
    @staticmethod
    def toStringArray(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> typing.List[str]: ...

class Assert:
    """
    Java class 'cern.accsoft.commons.util.Assert'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Assert()
    
    """
    def __init__(self): ...
    @staticmethod
    def argHasText(string: str, string2: str) -> None: ...
    @staticmethod
    def argIsNumber(double: float, string: str) -> None: ...
    @staticmethod
    def argNotNull(object: typing.Any, string: str) -> None: ...
    @typing.overload
    @staticmethod
    def doesNotContain(string: str, string2: str) -> None: ...
    @typing.overload
    @staticmethod
    def doesNotContain(string: str, string2: str, string3: str) -> None: ...
    @typing.overload
    @staticmethod
    def hasLength(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def hasLength(string: str, string2: str) -> None: ...
    @typing.overload
    @staticmethod
    def hasText(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def hasText(string: str, string2: str) -> None: ...
    @typing.overload
    @staticmethod
    def isAssignable(class_: typing.Type, class2: typing.Type) -> None: ...
    @typing.overload
    @staticmethod
    def isAssignable(class_: typing.Type, class2: typing.Type, string: str) -> None: ...
    @typing.overload
    @staticmethod
    def isInstanceOf(class_: typing.Type, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def isInstanceOf(class_: typing.Type, object: typing.Any, string: str) -> None: ...
    @typing.overload
    @staticmethod
    def isNull(object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def isNull(object: typing.Any, string: str) -> None: ...
    @staticmethod
    def isNumber(double: float, string: str) -> None: ...
    @typing.overload
    @staticmethod
    def isTrue(boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def isTrue(boolean: bool, string: str) -> None: ...
    @typing.overload
    @staticmethod
    def notEmpty(objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    @staticmethod
    def notEmpty(objectArray: typing.List[typing.Any], string: str) -> None: ...
    @typing.overload
    @staticmethod
    def notEmpty(collection: typing.Union[java.util.Collection, typing.Sequence]) -> None: ...
    @typing.overload
    @staticmethod
    def notEmpty(collection: typing.Union[java.util.Collection, typing.Sequence], string: str) -> None: ...
    @typing.overload
    @staticmethod
    def notEmpty(map: typing.Union[java.util.Map, typing.Mapping]) -> None: ...
    @typing.overload
    @staticmethod
    def notEmpty(map: typing.Union[java.util.Map, typing.Mapping], string: str) -> None: ...
    @typing.overload
    @staticmethod
    def notNull(object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def notNull(object: typing.Any, string: str) -> None: ...
    @typing.overload
    @staticmethod
    def notNullElements(objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    @staticmethod
    def notNullElements(objectArray: typing.List[typing.Any], string: str) -> None: ...
    @typing.overload
    @staticmethod
    def notNullElements(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]], string: str) -> None: ...
    @typing.overload
    @staticmethod
    def state(boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def state(boolean: bool, string: str) -> None: ...

class BeanSupport:
    """
    Java class 'cern.accsoft.commons.util.BeanSupport'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * BeanSupport(java.lang.Object)
    
    """
    def __init__(self, object: typing.Any): ...
    @typing.overload
    def addPropertyChangeListener(self, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    @typing.overload
    def addPropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    @typing.overload
    def removePropertyChangeListener(self, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    @typing.overload
    def removePropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...

class BeanUtils:
    """
    Java class 'cern.accsoft.commons.util.BeanUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * BeanUtils()
    
    """
    def __init__(self): ...
    @staticmethod
    def findDeclaredMethod(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> java.lang.reflect.Method: ...
    @staticmethod
    def findDeclaredMethodWithMinimalParameters(class_: typing.Type, string: str) -> java.lang.reflect.Method: ...
    @staticmethod
    def findMethod(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> java.lang.reflect.Method: ...
    @staticmethod
    def findMethodWithMinimalParameters(class_: typing.Type, string: str) -> java.lang.reflect.Method: ...
    @staticmethod
    def getNames(objectArray: typing.List[typing.Any]) -> typing.List[str]: ...
    @staticmethod
    def getPropertyType(class_: typing.Type, string: str) -> typing.Type: ...
    @staticmethod
    def getPropertyValue(object: typing.Any, string: str) -> typing.Any: ...
    @staticmethod
    def isSimpleProperty(class_: typing.Type) -> bool: ...
    @staticmethod
    def resolveSignature(string: str, class_: typing.Type) -> java.lang.reflect.Method: ...
    @staticmethod
    def toPropertyValues(objectArray: typing.List[typing.Any], string: str, class_: typing.Type) -> typing.List[typing.Any]: ...

class ClassLoaderJarInfo:
    """
    Java class 'cern.accsoft.commons.util.ClassLoaderJarInfo'
    
        Extends:
            java.lang.Object
    
      Attributes:
        JAR_EXT (java.lang.String): final static field
    
    """
    JAR_EXT: typing.ClassVar[str] = ...
    @typing.overload
    @staticmethod
    def getJarInfo(string: str) -> 'JarInfo': ...
    @typing.overload
    @staticmethod
    def getJarInfo(string: str, object: typing.Any) -> 'JarInfo': ...
    @typing.overload
    @staticmethod
    def getLoadedJarInfo() -> java.util.HashMap[str, 'JarInfo']: ...
    @typing.overload
    @staticmethod
    def getLoadedJarInfo(object: typing.Any) -> java.util.HashMap[str, 'JarInfo']: ...

class ClassLoaderUtils:
    """
    Java class 'cern.accsoft.commons.util.ClassLoaderUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ClassLoaderUtils()
    
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def showClassLoaderHierarchy(classLoader: java.lang.ClassLoader) -> str: ...
    @typing.overload
    @staticmethod
    def showClassLoaderHierarchy(classLoader: java.lang.ClassLoader, string: str, string2: str) -> str: ...
    @typing.overload
    @staticmethod
    def showClassLoaderHierarchy(object: typing.Any, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def showClassLoaderHierarchy(object: typing.Any, string: str, string2: str, string3: str) -> str: ...

class ClassUtils:
    """
    Java class 'cern.accsoft.commons.util.ClassUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ClassUtils()
    
      Attributes:
        ARRAY_SUFFIX (java.lang.String): final static field
    
    """
    ARRAY_SUFFIX: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def addResourcePathToPackagePath(class_: typing.Type, string: str) -> str: ...
    @typing.overload
    @staticmethod
    def classNamesToString(classArray: typing.List[typing.Type]) -> str: ...
    @typing.overload
    @staticmethod
    def classNamesToString(collection: typing.Union[java.util.Collection, typing.Sequence]) -> str: ...
    @staticmethod
    def classPackageAsResourcePath(class_: typing.Type) -> str: ...
    @staticmethod
    def createCompositeInterface(classArray: typing.List[typing.Type], classLoader: java.lang.ClassLoader) -> typing.Type: ...
    @staticmethod
    def findClassVersion(class_: typing.Type[typing.Any]) -> str: ...
    @typing.overload
    @staticmethod
    def forName(string: str) -> typing.Type: ...
    @typing.overload
    @staticmethod
    def forName(string: str, classLoader: java.lang.ClassLoader) -> typing.Type: ...
    @staticmethod
    def getAllInterfaces(object: typing.Any) -> typing.List[typing.Type]: ...
    @staticmethod
    def getAllInterfacesAsSet(object: typing.Any) -> java.util.Set: ...
    @staticmethod
    def getAllInterfacesForClass(class_: typing.Type) -> typing.List[typing.Type]: ...
    @staticmethod
    def getAllInterfacesForClassAsSet(class_: typing.Type) -> java.util.Set: ...
    @staticmethod
    def getClassFileName(class_: typing.Type) -> str: ...
    @staticmethod
    def getConstructorIfAvailable(class_: typing.Type, classArray: typing.List[typing.Type]) -> java.lang.reflect.Constructor: ...
    @staticmethod
    def getDefaultClassLoader() -> java.lang.ClassLoader: ...
    @staticmethod
    def getMethodCountForName(class_: typing.Type, string: str) -> int: ...
    @staticmethod
    def getMethodIfAvailable(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> java.lang.reflect.Method: ...
    @staticmethod
    def getQualifiedMethodName(method: java.lang.reflect.Method) -> str: ...
    @staticmethod
    def getQualifiedName(class_: typing.Type) -> str: ...
    @typing.overload
    @staticmethod
    def getShortName(class_: typing.Type) -> str: ...
    @typing.overload
    @staticmethod
    def getShortName(string: str) -> str: ...
    @staticmethod
    def getShortNameAsProperty(class_: typing.Type) -> str: ...
    @staticmethod
    def getStaticMethod(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> java.lang.reflect.Method: ...
    @typing.overload
    @staticmethod
    def getUserClass(class_: typing.Type) -> typing.Type: ...
    @typing.overload
    @staticmethod
    def getUserClass(object: typing.Any) -> typing.Type: ...
    @staticmethod
    def hasAtLeastOneMethodWithName(class_: typing.Type, string: str) -> bool: ...
    @staticmethod
    def hasConstructor(class_: typing.Type, classArray: typing.List[typing.Type]) -> bool: ...
    @staticmethod
    def hasMethod(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> bool: ...
    @staticmethod
    def isAssignable(class_: typing.Type, class2: typing.Type) -> bool: ...
    @staticmethod
    def isAssignableValue(class_: typing.Type, object: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def isPresent(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def isPresent(string: str, classLoader: java.lang.ClassLoader) -> bool: ...
    @staticmethod
    def isPrimitiveArray(class_: typing.Type) -> bool: ...
    @staticmethod
    def isPrimitiveOrWrapper(class_: typing.Type) -> bool: ...
    @staticmethod
    def isPrimitiveWrapper(class_: typing.Type) -> bool: ...
    @staticmethod
    def isPrimitiveWrapperArray(class_: typing.Type) -> bool: ...
    @staticmethod
    def resolveClassName(string: str, classLoader: java.lang.ClassLoader) -> typing.Type: ...
    @staticmethod
    def resolvePrimitiveClassName(string: str) -> typing.Type: ...

class ClasspathUtils:
    """
    Java class 'cern.accsoft.commons.util.ClasspathUtils'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def findSubClassesInPackage(class_: typing.Type[typing.Any], string: str, boolean: bool) -> java.util.Set[typing.Type[typing.Any]]: ...

class Cleanable:
    """
    Java class 'cern.accsoft.commons.util.Cleanable'
    
    """
    def cleanup(self) -> None: ...
    def isCleaning(self) -> bool: ...

class CleanableUtil:
    """
    Java class 'cern.accsoft.commons.util.CleanableUtil'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def cleanupContainer(container: java.awt.Container) -> None: ...

class CollectionUtils:
    """
    Java class 'cern.accsoft.commons.util.CollectionUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * CollectionUtils()
    
    """
    def __init__(self): ...
    @staticmethod
    def arrayToList(object: typing.Any) -> java.util.List: ...
    @typing.overload
    @staticmethod
    def contains(enumeration: java.util.Enumeration, object: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def contains(iterator: java.util.Iterator, object: typing.Any) -> bool: ...
    @staticmethod
    def containsAny(collection: typing.Union[java.util.Collection, typing.Sequence], collection2: typing.Union[java.util.Collection, typing.Sequence]) -> bool: ...
    @staticmethod
    def containsInstance(collection: typing.Union[java.util.Collection, typing.Sequence], object: typing.Any) -> bool: ...
    @staticmethod
    def findFirstMatch(collection: typing.Union[java.util.Collection, typing.Sequence], collection2: typing.Union[java.util.Collection, typing.Sequence]) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def findValueOfType(collection: typing.Union[java.util.Collection, typing.Sequence], class_: typing.Type) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def findValueOfType(collection: typing.Union[java.util.Collection, typing.Sequence], classArray: typing.List[typing.Type]) -> typing.Any: ...
    _flatten__C = typing.TypeVar('_flatten__C', bound=java.util.Collection)  # <C>
    _flatten__T = typing.TypeVar('_flatten__T')  # <T>
    @staticmethod
    def flatten(collection: typing.Union[java.util.Collection[java.util.Collection[_flatten__T]], typing.Sequence[java.util.Collection[_flatten__T]]], collector: java.util.stream.Collector[_flatten__T, typing.Any, _flatten__C]) -> _flatten__C: ...
    _flattenToList__T = typing.TypeVar('_flattenToList__T')  # <T>
    @staticmethod
    def flattenToList(collection: typing.Union[java.util.Collection[java.util.Collection[_flattenToList__T]], typing.Sequence[java.util.Collection[_flattenToList__T]]]) -> java.util.List[_flattenToList__T]: ...
    _flattenToSet__T = typing.TypeVar('_flattenToSet__T')  # <T>
    @staticmethod
    def flattenToSet(collection: typing.Union[java.util.Collection[java.util.Collection[_flattenToSet__T]], typing.Sequence[java.util.Collection[_flattenToSet__T]]]) -> java.util.Set[_flattenToSet__T]: ...
    @staticmethod
    def hasUniqueObject(collection: typing.Union[java.util.Collection, typing.Sequence]) -> bool: ...
    @typing.overload
    @staticmethod
    def isEmpty(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    @typing.overload
    @staticmethod
    def isEmpty(map: typing.Union[java.util.Map[typing.Any, typing.Any], typing.Mapping[typing.Any, typing.Any]]) -> bool: ...
    @staticmethod
    def mergeArrayIntoCollection(object: typing.Any, collection: typing.Union[java.util.Collection, typing.Sequence]) -> None: ...
    @staticmethod
    def mergePropertiesIntoMap(properties: java.util.Properties, map: typing.Union[java.util.Map, typing.Mapping]) -> None: ...
    _toSet__E = typing.TypeVar('_toSet__E')  # <E>
    @staticmethod
    def toSet(eArray: typing.List[_toSet__E]) -> java.util.Set[_toSet__E]: ...
    _toSortedList__T = typing.TypeVar('_toSortedList__T')  # <T>
    @staticmethod
    def toSortedList(collection: typing.Union[java.util.Collection[_toSortedList__T], typing.Sequence[_toSortedList__T]]) -> java.util.List[_toSortedList__T]: ...

class ExceptionUtils:
    """
    Java class 'cern.accsoft.commons.util.ExceptionUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ExceptionUtils()
    
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def extractExceptionMessage(throwable: java.lang.Throwable) -> str: ...
    @typing.overload
    @staticmethod
    def extractExceptionMessage(throwable: java.lang.Throwable, boolean: bool) -> str: ...
    @staticmethod
    def filterStackTrace(throwable: java.lang.Throwable, string: str) -> None: ...
    @staticmethod
    def getCondensedStackTrace(throwable: java.lang.Throwable, int: int) -> str: ...
    @staticmethod
    def getRootCause(throwable: java.lang.Throwable) -> java.lang.Throwable: ...
    @staticmethod
    def getStackTraceAsString(throwable: java.lang.Throwable) -> str: ...

class FileCopyUtils:
    """
    Java class 'cern.accsoft.commons.util.FileCopyUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * FileCopyUtils()
    
      Attributes:
        BUFFER_SIZE (int): final static field
    
    """
    BUFFER_SIZE: typing.ClassVar[int] = ...
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def copy(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], file2: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> int: ...
    @typing.overload
    @staticmethod
    def copy(inputStream: java.io.InputStream, outputStream: java.io.OutputStream) -> int: ...
    @typing.overload
    @staticmethod
    def copy(reader: java.io.Reader, writer: java.io.Writer) -> int: ...
    @typing.overload
    @staticmethod
    def copy(byteArray: typing.List[int], file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None: ...
    @typing.overload
    @staticmethod
    def copy(byteArray: typing.List[int], outputStream: java.io.OutputStream) -> None: ...
    @typing.overload
    @staticmethod
    def copy(string: str, writer: java.io.Writer) -> None: ...
    @typing.overload
    @staticmethod
    def copyToByteArray(file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> typing.List[int]: ...
    @typing.overload
    @staticmethod
    def copyToByteArray(inputStream: java.io.InputStream) -> typing.List[int]: ...
    @staticmethod
    def copyToString(reader: java.io.Reader) -> str: ...

class FileUtils:
    """
    Java class 'cern.accsoft.commons.util.FileUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * FileUtils()
    
      Attributes:
        FS (java.lang.String): final static field
        DATA_URL (java.lang.String): final static field
        DATA_PATH (java.lang.String): final static field
        FILE_BY_DATE_COMPARATOR (java.util.Comparator): final static field
    
    """
    FS: typing.ClassVar[str] = ...
    DATA_URL: typing.ClassVar[str] = ...
    DATA_PATH: typing.ClassVar[str] = ...
    FILE_BY_DATE_COMPARATOR: typing.ClassVar[java.util.Comparator] = ...
    def __init__(self): ...
    @staticmethod
    def createFilenameFilter(string: str) -> java.io.FilenameFilter: ...
    @typing.overload
    @staticmethod
    def findFiles(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], filenameFilter: typing.Union[java.io.FilenameFilter, typing.Callable]) -> java.util.List[java.io.File]: ...
    @typing.overload
    @staticmethod
    def findFiles(string: str, string2: str) -> java.util.List[str]: ...
    @staticmethod
    def getTempDir() -> java.io.File: ...
    @typing.overload
    @staticmethod
    def readAllLines(inputStream: java.io.InputStream) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def readAllLines(string: str) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def readAllText(inputStream: java.io.InputStream) -> str: ...
    @typing.overload
    @staticmethod
    def readAllText(string: str) -> str: ...

class JarInfo:
    """
    Java class 'cern.accsoft.commons.util.JarInfo'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * JarInfo()
    
      Attributes:
        classLoaderName (java.lang.String): field
        cbngJarName (java.lang.String): field
        jarName (java.lang.String): field
        vendor (java.lang.String): field
        version (java.lang.String): field
        version2 (java.lang.String): field
        jarPath (java.lang.String): field
    
    """
    classLoaderName: str = ...
    cbngJarName: str = ...
    jarName: str = ...
    vendor: str = ...
    version: str = ...
    version2: str = ...
    jarPath: str = ...
    def __init__(self): ...
    def toString(self) -> str: ...

class JdkUtils:
    """
    Java class 'cern.accsoft.commons.util.JdkUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * JdkUtils()
    
      Attributes:
        JDK_VERSION (java.lang.String): final static field
        JDK_PATH_DEFAULT (java.lang.String): final static field
    
    """
    JDK_VERSION: typing.ClassVar[str] = ...
    JDK_PATH_DEFAULT: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def findCurrentJdkDir() -> str: ...
    @staticmethod
    def findCurrentJvmPath() -> java.nio.file.Path: ...
    @staticmethod
    def findJdkDirsUnder(string: str) -> java.util.List[str]: ...
    @staticmethod
    def findStandardJdkDirs() -> java.util.List[str]: ...
    @staticmethod
    def getPidLinux() -> int: ...

class MapUtils:
    """
    Java class 'cern.accsoft.commons.util.MapUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MapUtils()
    
    """
    def __init__(self): ...
    _extractValues__K = typing.TypeVar('_extractValues__K')  # <K>
    _extractValues__V = typing.TypeVar('_extractValues__V')  # <V>
    _extractValues__C = typing.TypeVar('_extractValues__C', bound=java.util.Collection)  # <C>
    @staticmethod
    def extractValues(map: typing.Union[java.util.Map[_extractValues__K, _extractValues__C], typing.Mapping[_extractValues__K, _extractValues__C]]) -> java.util.Set[_extractValues__V]: ...
    _findMatchingValues__T = typing.TypeVar('_findMatchingValues__T')  # <T>
    @staticmethod
    def findMatchingValues(map: typing.Union[java.util.Map[str, _findMatchingValues__T], typing.Mapping[str, _findMatchingValues__T]], string: str, matchType: 'MapUtils.MatchType') -> java.util.Map[str, _findMatchingValues__T]: ...
    _getKeyByValue__T = typing.TypeVar('_getKeyByValue__T')  # <T>
    _getKeyByValue__E = typing.TypeVar('_getKeyByValue__E')  # <E>
    @staticmethod
    def getKeyByValue(map: typing.Union[java.util.Map[_getKeyByValue__T, _getKeyByValue__E], typing.Mapping[_getKeyByValue__T, _getKeyByValue__E]], e: _getKeyByValue__E) -> _getKeyByValue__T: ...
    _getKeysByValue__T = typing.TypeVar('_getKeysByValue__T')  # <T>
    _getKeysByValue__E = typing.TypeVar('_getKeysByValue__E')  # <E>
    @staticmethod
    def getKeysByValue(map: typing.Union[java.util.Map[_getKeysByValue__T, _getKeysByValue__E], typing.Mapping[_getKeysByValue__T, _getKeysByValue__E]], e: _getKeysByValue__E) -> java.util.Set[_getKeysByValue__T]: ...
    _indexBy__T = typing.TypeVar('_indexBy__T')  # <T>
    @staticmethod
    def indexBy(tArray: typing.List[_indexBy__T], string: str, objectArray: typing.List[typing.Any]) -> java.util.Map[str, _indexBy__T]: ...
    _indexByName__T = typing.TypeVar('_indexByName__T')  # <T>
    @staticmethod
    def indexByName(tArray: typing.List[_indexByName__T]) -> java.util.Map[str, _indexByName__T]: ...
    _valuesIntersection__K = typing.TypeVar('_valuesIntersection__K')  # <K>
    _valuesIntersection__V = typing.TypeVar('_valuesIntersection__V')  # <V>
    _valuesIntersection__C = typing.TypeVar('_valuesIntersection__C', bound=java.util.Collection)  # <C>
    @staticmethod
    def valuesIntersection(map: typing.Union[java.util.Map[_valuesIntersection__K, _valuesIntersection__C], typing.Mapping[_valuesIntersection__K, _valuesIntersection__C]]) -> java.util.Set[_valuesIntersection__V]: ...
    class MatchType(java.lang.Enum['MapUtils.MatchType']):
        """
        Java class 'cern.accsoft.commons.util.MapUtils$MatchType'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            STARTS_WITH (cern.accsoft.commons.util.MapUtils$MatchType): final static enum constant
            CONTAINS (cern.accsoft.commons.util.MapUtils$MatchType): final static enum constant
            ENDS_WITH (cern.accsoft.commons.util.MapUtils$MatchType): final static enum constant
            REGEXP (cern.accsoft.commons.util.MapUtils$MatchType): final static enum constant
        
        """
        STARTS_WITH: typing.ClassVar['MapUtils.MatchType'] = ...
        CONTAINS: typing.ClassVar['MapUtils.MatchType'] = ...
        ENDS_WITH: typing.ClassVar['MapUtils.MatchType'] = ...
        REGEXP: typing.ClassVar['MapUtils.MatchType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'MapUtils.MatchType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['MapUtils.MatchType']: ...

class MockitoUtil:
    """
    Java class 'cern.accsoft.commons.util.MockitoUtil'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MockitoUtil()
    
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def wireWithMocks(object: typing.Any) -> java.util.Map[str, typing.Any]: ...
    @typing.overload
    @staticmethod
    def wireWithMocks(object: typing.Any, class_: typing.Type[typing.Any]) -> java.util.Map[str, typing.Any]: ...

class Named:
    """
    Java class 'cern.accsoft.commons.util.Named'
    
    """
    def getName(self) -> str: ...

class Nameds:
    """
    Java class 'cern.accsoft.commons.util.Nameds'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Nameds()
    
      Attributes:
        NAMED_MAPPER (cern.accsoft.commons.util.Mappers$Mapper): final static field
        NAMED_COMPARATOR (java.util.Comparator): final static field
    
    """
    NAMED_MAPPER: typing.ClassVar['Mappers.Mapper'] = ...
    NAMED_COMPARATOR: typing.ClassVar[java.util.Comparator] = ...
    def __init__(self): ...
    _containsByName__T = typing.TypeVar('_containsByName__T', bound=Named)  # <T>
    @staticmethod
    def containsByName(collection: typing.Union[java.util.Collection[_containsByName__T], typing.Sequence[_containsByName__T]], string: str) -> bool: ...
    _filterByNames_0__T = typing.TypeVar('_filterByNames_0__T', bound=Named)  # <T>
    _filterByNames_1__T = typing.TypeVar('_filterByNames_1__T', bound=Named)  # <T>
    _filterByNames_2__T = typing.TypeVar('_filterByNames_2__T', bound=Named)  # <T>
    @typing.overload
    @staticmethod
    def filterByNames(collection: typing.Union[java.util.Collection[_filterByNames_0__T], typing.Sequence[_filterByNames_0__T]], collection2: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Collection[_filterByNames_0__T]: ...
    @typing.overload
    @staticmethod
    def filterByNames(list: java.util.List[_filterByNames_1__T], collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.List[_filterByNames_1__T]: ...
    @typing.overload
    @staticmethod
    def filterByNames(set: java.util.Set[_filterByNames_2__T], collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Set[_filterByNames_2__T]: ...
    _findByName_0__T = typing.TypeVar('_findByName_0__T', bound=Named)  # <T>
    _findByName_1__T = typing.TypeVar('_findByName_1__T', bound=Named)  # <T>
    @typing.overload
    @staticmethod
    def findByName(tArray: typing.List[_findByName_0__T], string: str) -> _findByName_0__T: ...
    @typing.overload
    @staticmethod
    def findByName(collection: typing.Union[java.util.Collection[_findByName_1__T], typing.Sequence[_findByName_1__T]], string: str) -> _findByName_1__T: ...
    @typing.overload
    @staticmethod
    def getNames(collection: typing.Union[java.util.Collection[Named], typing.Sequence[Named]]) -> java.util.Collection[str]: ...
    @typing.overload
    @staticmethod
    def getNames(namedArray: typing.List[Named]) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def getNames(list: java.util.List[Named]) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def getNames(set: java.util.Set[Named]) -> java.util.Set[str]: ...
    @staticmethod
    def getNamesList(collection: typing.Union[java.util.Collection[Named], typing.Sequence[Named]]) -> java.util.List[str]: ...
    @staticmethod
    def getNamesSet(collection: typing.Union[java.util.Collection[Named], typing.Sequence[Named]]) -> java.util.Set[str]: ...
    @typing.overload
    @staticmethod
    def getSortedNames(collection: typing.Union[java.util.Collection[Named], typing.Sequence[Named]]) -> java.util.Collection[str]: ...
    @typing.overload
    @staticmethod
    def getSortedNames(namedArray: typing.List[Named]) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def getSortedNames(list: java.util.List[Named]) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def getSortedNames(set: java.util.Set[Named]) -> java.util.Set[str]: ...
    _mapByName_0__T = typing.TypeVar('_mapByName_0__T', bound=Named)  # <T>
    _mapByName_1__T = typing.TypeVar('_mapByName_1__T', bound=Named)  # <T>
    @typing.overload
    @staticmethod
    def mapByName(tArray: typing.List[_mapByName_0__T]) -> java.util.Map[str, _mapByName_0__T]: ...
    @typing.overload
    @staticmethod
    def mapByName(collection: typing.Union[java.util.Collection[_mapByName_1__T], typing.Sequence[_mapByName_1__T]]) -> java.util.Map[str, _mapByName_1__T]: ...
    _sortByName_0__T = typing.TypeVar('_sortByName_0__T', bound=Named)  # <T>
    _sortByName_1__T = typing.TypeVar('_sortByName_1__T', bound=Named)  # <T>
    @typing.overload
    @staticmethod
    def sortByName(list: java.util.List[_sortByName_0__T]) -> java.util.List[_sortByName_0__T]: ...
    @typing.overload
    @staticmethod
    def sortByName(set: java.util.Set[_sortByName_1__T]) -> java.util.Set[_sortByName_1__T]: ...
    _sortByNameToList__T = typing.TypeVar('_sortByNameToList__T', bound=Named)  # <T>
    @staticmethod
    def sortByNameToList(collection: typing.Union[java.util.Collection[_sortByNameToList__T], typing.Sequence[_sortByNameToList__T]]) -> java.util.List[_sortByNameToList__T]: ...
    _sortByNameToSet__T = typing.TypeVar('_sortByNameToSet__T', bound=Named)  # <T>
    @staticmethod
    def sortByNameToSet(collection: typing.Union[java.util.Collection[_sortByNameToSet__T], typing.Sequence[_sortByNameToSet__T]]) -> java.util.Set[_sortByNameToSet__T]: ...

class NumberUtils:
    """
    Java class 'cern.accsoft.commons.util.NumberUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * NumberUtils()
    
      Attributes:
        HEXADECIMAL_FORMAT_PREFIX (java.lang.String): final static field
        HEXADECIMAL_FORMAT_RADIX (int): final static field
        BINARY_FORMAT_PREFIX (java.lang.String): final static field
        BINARY_FORMAT_RADIX (int): final static field
    
    """
    HEXADECIMAL_FORMAT_PREFIX: typing.ClassVar[str] = ...
    HEXADECIMAL_FORMAT_RADIX: typing.ClassVar[int] = ...
    BINARY_FORMAT_PREFIX: typing.ClassVar[str] = ...
    BINARY_FORMAT_RADIX: typing.ClassVar[int] = ...
    def __init__(self): ...
    @staticmethod
    def convertNumberToTargetClass(number: typing.Union[_jpype._JNumberLong, _jpype._JNumberFloat, typing.SupportsIndex, typing.SupportsFloat], class_: typing.Type) -> java.lang.Number: ...
    @typing.overload
    @staticmethod
    def parseNumber(string: str, class_: typing.Type) -> java.lang.Number: ...
    @typing.overload
    @staticmethod
    def parseNumber(string: str, class_: typing.Type, numberFormat: java.text.NumberFormat) -> java.lang.Number: ...

class OSUtils:
    """
    Java class 'cern.accsoft.commons.util.OSUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * OSUtils()
    
      Attributes:
        IS_WINDOWS (boolean): final static field
        IS_LINUX (boolean): final static field
    
    """
    IS_WINDOWS: typing.ClassVar[bool] = ...
    IS_LINUX: typing.ClassVar[bool] = ...
    def __init__(self): ...

class ObjectUtils:
    """
    Java class 'cern.accsoft.commons.util.ObjectUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ObjectUtils()
    
    """
    def __init__(self): ...
    @staticmethod
    def getDisplayString(object: typing.Any) -> str: ...
    @staticmethod
    def getIdentityHexString(object: typing.Any) -> str: ...
    @typing.overload
    def hashCode(self) -> int: ...
    @typing.overload
    @staticmethod
    def hashCode(boolean: bool) -> int: ...
    @typing.overload
    @staticmethod
    def hashCode(double: float) -> int: ...
    @typing.overload
    @staticmethod
    def hashCode(float: float) -> int: ...
    @typing.overload
    @staticmethod
    def hashCode(long: int) -> int: ...
    @staticmethod
    def identityToString(object: typing.Any) -> str: ...
    @staticmethod
    def isCheckedException(throwable: java.lang.Throwable) -> bool: ...
    @staticmethod
    def isCompatibleWithThrowsClause(throwable: java.lang.Throwable, classArray: typing.List[typing.Type]) -> bool: ...
    @staticmethod
    def nullSafeClassName(object: typing.Any) -> str: ...
    @staticmethod
    def nullSafeEquals(object: typing.Any, object2: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(booleanArray: typing.List[bool]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(byteArray: typing.List[int]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(charArray: typing.List[str]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(doubleArray: typing.List[float]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(floatArray: typing.List[float]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(intArray: typing.List[int]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(object: typing.Any) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(objectArray: typing.List[typing.Any]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(longArray: typing.List[int]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeHashCode(shortArray: typing.List[int]) -> int: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(booleanArray: typing.List[bool]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(byteArray: typing.List[int]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(charArray: typing.List[str]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(doubleArray: typing.List[float]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(floatArray: typing.List[float]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(intArray: typing.List[int]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(object: typing.Any) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(objectArray: typing.List[typing.Any]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(longArray: typing.List[int]) -> str: ...
    @typing.overload
    @staticmethod
    def nullSafeToString(shortArray: typing.List[int]) -> str: ...

class PcropsRepositoryDownloader:
    """
    Java class 'cern.accsoft.commons.util.PcropsRepositoryDownloader'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PcropsRepositoryDownloader()
    
    """
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class PcropsRepositoryJnlpSearcher:
    """
    Java class 'cern.accsoft.commons.util.PcropsRepositoryJnlpSearcher'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PcropsRepositoryJnlpSearcher()
    
    """
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class PcropsRepositoryProductUsageSearcher:
    """
    Java class 'cern.accsoft.commons.util.PcropsRepositoryProductUsageSearcher'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PcropsRepositoryProductUsageSearcher()
    
    """
    def __init__(self): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...

class ProcessUtils:
    """
    Java class 'cern.accsoft.commons.util.ProcessUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ProcessUtils()
    
    """
    def __init__(self): ...
    @staticmethod
    def getMyPid() -> int: ...
    @staticmethod
    def getMyProcessName() -> str: ...
    @staticmethod
    def getMyShortProcessName() -> str: ...

class ReflectionUtils:
    """
    Java class 'cern.accsoft.commons.util.ReflectionUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ReflectionUtils()
    
      Attributes:
        COPYABLE_FIELDS (cern.accsoft.commons.util.ReflectionUtils$FieldFilter): static field
    
    """
    COPYABLE_FIELDS: typing.ClassVar['ReflectionUtils.FieldFilter'] = ...
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def doWithFields(class_: typing.Type, fieldCallback: 'ReflectionUtils.FieldCallback') -> None: ...
    @typing.overload
    @staticmethod
    def doWithFields(class_: typing.Type, fieldCallback: 'ReflectionUtils.FieldCallback', fieldFilter: 'ReflectionUtils.FieldFilter') -> None: ...
    @typing.overload
    @staticmethod
    def doWithMethods(class_: typing.Type, methodCallback: 'ReflectionUtils.MethodCallback') -> None: ...
    @typing.overload
    @staticmethod
    def doWithMethods(class_: typing.Type, methodCallback: 'ReflectionUtils.MethodCallback', methodFilter: 'ReflectionUtils.MethodFilter') -> None: ...
    @staticmethod
    def findAncestors(class_: typing.Type[typing.Any], list: java.util.List[typing.Type[typing.Any]]) -> None: ...
    @staticmethod
    def findMethod(class_: typing.Type, string: str, classArray: typing.List[typing.Type]) -> java.lang.reflect.Method: ...
    @staticmethod
    def getAllDeclaredMethods(class_: typing.Type) -> typing.List[java.lang.reflect.Method]: ...
    @staticmethod
    def getPropertyValue(object: typing.Any, string: str) -> typing.Any: ...
    @staticmethod
    def handleInvocationTargetException(invocationTargetException: java.lang.reflect.InvocationTargetException) -> None: ...
    @staticmethod
    def handleReflectionException(exception: java.lang.Exception) -> None: ...
    @typing.overload
    @staticmethod
    def invokeMethod(method: java.lang.reflect.Method, object: typing.Any) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def invokeMethod(method: java.lang.reflect.Method, object: typing.Any, objectArray: typing.List[typing.Any]) -> typing.Any: ...
    @staticmethod
    def isFoundOnClassPath(string: str) -> bool: ...
    @staticmethod
    def isPublicStaticFinal(field: java.lang.reflect.Field) -> bool: ...
    @staticmethod
    def makeAccessible(field: java.lang.reflect.Field) -> None: ...
    @staticmethod
    def shallowCopyFieldState(object: typing.Any, object2: typing.Any) -> None: ...
    class FieldCallback:
        """
        Java class 'cern.accsoft.commons.util.ReflectionUtils$FieldCallback'
        
        """
        def doWith(self, field: java.lang.reflect.Field) -> None: ...
    class FieldFilter:
        """
        Java class 'cern.accsoft.commons.util.ReflectionUtils$FieldFilter'
        
        """
        def matches(self, field: java.lang.reflect.Field) -> bool: ...
    class MethodCallback:
        """
        Java class 'cern.accsoft.commons.util.ReflectionUtils$MethodCallback'
        
        """
        def doWith(self, method: java.lang.reflect.Method) -> None: ...
    class MethodFilter:
        """
        Java class 'cern.accsoft.commons.util.ReflectionUtils$MethodFilter'
        
        """
        def matches(self, method: java.lang.reflect.Method) -> bool: ...

class ResourceUtils:
    """
    Java class 'cern.accsoft.commons.util.ResourceUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ResourceUtils()
    
      Attributes:
        CLASSPATH_URL_PREFIX (java.lang.String): final static field
        FILE_URL_PREFIX (java.lang.String): final static field
        URL_PROTOCOL_FILE (java.lang.String): final static field
        URL_PROTOCOL_JAR (java.lang.String): final static field
        URL_PROTOCOL_ZIP (java.lang.String): final static field
        URL_PROTOCOL_WSJAR (java.lang.String): final static field
        JAR_URL_SEPARATOR (java.lang.String): final static field
    
    """
    CLASSPATH_URL_PREFIX: typing.ClassVar[str] = ...
    FILE_URL_PREFIX: typing.ClassVar[str] = ...
    URL_PROTOCOL_FILE: typing.ClassVar[str] = ...
    URL_PROTOCOL_JAR: typing.ClassVar[str] = ...
    URL_PROTOCOL_ZIP: typing.ClassVar[str] = ...
    URL_PROTOCOL_WSJAR: typing.ClassVar[str] = ...
    JAR_URL_SEPARATOR: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def extractJarFileURL(uRL: java.net.URL) -> java.net.URL: ...
    @typing.overload
    @staticmethod
    def getFile(string: str) -> java.io.File: ...
    @typing.overload
    @staticmethod
    def getFile(uRL: java.net.URL) -> java.io.File: ...
    @typing.overload
    @staticmethod
    def getFile(uRL: java.net.URL, string: str) -> java.io.File: ...
    @staticmethod
    def getURL(string: str) -> java.net.URL: ...
    @staticmethod
    def isJarURL(uRL: java.net.URL) -> bool: ...
    @staticmethod
    def isUrl(string: str) -> bool: ...

class SerializationObjectCloner:
    """
    Java class 'cern.accsoft.commons.util.SerializationObjectCloner'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SerializationObjectCloner()
    
    """
    def __init__(self): ...
    _deepCopy__T = typing.TypeVar('_deepCopy__T', bound=java.io.Serializable)  # <T>
    @staticmethod
    def deepCopy(t: _deepCopy__T) -> _deepCopy__T: ...

class StringUtils:
    """
    Java class 'cern.accsoft.commons.util.StringUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * StringUtils()
    
      Attributes:
        EMPTY_STRING (java.lang.String): final static field
        EMPTY_STRING_ARRAY ([Ljava.lang.String;): final static field
        EMPTY_STRING_ARRAY2D ([[Ljava.lang.String;): final static field
    
    """
    EMPTY_STRING: typing.ClassVar[str] = ...
    EMPTY_STRING_ARRAY: typing.ClassVar[typing.List[str]] = ...
    EMPTY_STRING_ARRAY2D: typing.ClassVar[typing.List[typing.List[str]]] = ...
    def __init__(self): ...
    @staticmethod
    def addStringToArray(stringArray: typing.List[str], string2: str) -> typing.List[str]: ...
    @staticmethod
    def applyRelativePath(string: str, string2: str) -> str: ...
    @staticmethod
    def arrayToCommaDelimitedString(objectArray: typing.List[typing.Any]) -> str: ...
    @staticmethod
    def arrayToDelimitedString(objectArray: typing.List[typing.Any], string: str) -> str: ...
    @staticmethod
    def capitalize(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def center(string: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def center(string: str, int: int, char: str) -> str: ...
    @staticmethod
    def cleanPath(string: str) -> str: ...
    @staticmethod
    def collectionToCommaDelimitedString(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> str: ...
    @typing.overload
    @staticmethod
    def collectionToDelimitedString(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]], string: str) -> str: ...
    @typing.overload
    @staticmethod
    def collectionToDelimitedString(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]], string: str, string2: str, string3: str) -> str: ...
    @staticmethod
    def commaDelimitedListToSet(string: str) -> java.util.Set[str]: ...
    @staticmethod
    def commaDelimitedListToStringArray(string: str) -> typing.List[str]: ...
    @staticmethod
    def concatenateStringArrays(stringArray: typing.List[str], stringArray2: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def containsAnySubstring(string: str, stringArray: typing.List[str]) -> bool: ...
    @staticmethod
    def containsWhitespace(string: str) -> bool: ...
    @staticmethod
    def countOccurrencesOf(string: str, string2: str) -> int: ...
    @staticmethod
    def delete(string: str, string2: str) -> str: ...
    @staticmethod
    def deleteAny(string: str, string2: str) -> str: ...
    @staticmethod
    def delimitedListToStringArray(string: str, string2: str) -> typing.List[str]: ...
    @staticmethod
    def emptyStringToNull(string: str) -> str: ...
    @staticmethod
    def endsWithIgnoreCase(string: str, string2: str) -> bool: ...
    @staticmethod
    def getFilename(string: str) -> str: ...
    @staticmethod
    def getFilenameExtension(string: str) -> str: ...
    @staticmethod
    def hasLength(string: str) -> bool: ...
    @staticmethod
    def hasText(string: str) -> bool: ...
    @staticmethod
    def mergeStringArrays(stringArray: typing.List[str], stringArray2: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def nullToEmptyString(string: str) -> str: ...
    @staticmethod
    def parseLocaleString(string: str) -> java.util.Locale: ...
    @staticmethod
    def pathEquals(string: str, string2: str) -> bool: ...
    @staticmethod
    def quote(string: str) -> str: ...
    @staticmethod
    def quoteIfString(object: typing.Any) -> typing.Any: ...
    @staticmethod
    def removeDuplicateStrings(stringArray: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def repeatChar(char: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def replace(string: str, string2: str, string3: str) -> str: ...
    @typing.overload
    @staticmethod
    def replace(stringBuilder: java.lang.StringBuilder, string2: str, string3: str, boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def setStringLength(string: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def setStringLength(string: str, int: int, char: str) -> str: ...
    @staticmethod
    def sortStringArray(stringArray: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def split(string: str, string2: str) -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def splitArrayElementsIntoProperties(stringArray: typing.List[str], string2: str) -> java.util.Properties: ...
    @typing.overload
    @staticmethod
    def splitArrayElementsIntoProperties(stringArray: typing.List[str], string2: str, string3: str) -> java.util.Properties: ...
    @staticmethod
    def splitHTMLSentence(string: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def splitSentence(string: str, int: int) -> str: ...
    @typing.overload
    @staticmethod
    def splitSentence(string: str, string2: str, int: int) -> str: ...
    @staticmethod
    def startsWithIgnoreCase(string: str, string2: str) -> bool: ...
    @staticmethod
    def stripFilenameExtension(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def toCamelCase(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def toCamelCase(string: str, firstLetterCapitalization: 'StringUtils.FirstLetterCapitalization') -> str: ...
    @staticmethod
    def toNotNullTrimmedString(string: str) -> str: ...
    @staticmethod
    def toStringArray(collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def tokenizeToStringArray(string: str, string2: str) -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def tokenizeToStringArray(string: str, string2: str, boolean: bool, boolean2: bool) -> typing.List[str]: ...
    @staticmethod
    def trimAllWhitespace(string: str) -> str: ...
    @staticmethod
    def trimLeadingWhitespace(string: str) -> str: ...
    @staticmethod
    def trimTrailingWhitespace(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def trimWhitespace(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def trimWhitespace(stringArray: typing.List[str]) -> typing.List[str]: ...
    @staticmethod
    def uncapitalize(string: str) -> str: ...
    @staticmethod
    def underscoreName(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def unqualify(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def unqualify(string: str, char: str) -> str: ...
    class FirstLetterCapitalization(java.lang.Enum['StringUtils.FirstLetterCapitalization']):
        """
        Java class 'cern.accsoft.commons.util.StringUtils$FirstLetterCapitalization'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            CAPITALIZE_FIRST_LETTER (cern.accsoft.commons.util.StringUtils$FirstLetterCapitalization): final static enum constant
            UNCAPITALIZE_FIRST_LETTER (cern.accsoft.commons.util.StringUtils$FirstLetterCapitalization): final static enum constant
            DO_NOT_CHANGE_FIRST_LETTER (cern.accsoft.commons.util.StringUtils$FirstLetterCapitalization): final static enum constant
        
        """
        CAPITALIZE_FIRST_LETTER: typing.ClassVar['StringUtils.FirstLetterCapitalization'] = ...
        UNCAPITALIZE_FIRST_LETTER: typing.ClassVar['StringUtils.FirstLetterCapitalization'] = ...
        DO_NOT_CHANGE_FIRST_LETTER: typing.ClassVar['StringUtils.FirstLetterCapitalization'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'StringUtils.FirstLetterCapitalization': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['StringUtils.FirstLetterCapitalization']: ...

class SystemPropertyUtils:
    """
    Java class 'cern.accsoft.commons.util.SystemPropertyUtils'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SystemPropertyUtils()
    
      Attributes:
        PLACEHOLDER_PREFIX (java.lang.String): final static field
        PLACEHOLDER_SUFFIX (java.lang.String): final static field
    
    """
    PLACEHOLDER_PREFIX: typing.ClassVar[str] = ...
    PLACEHOLDER_SUFFIX: typing.ClassVar[str] = ...
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def getBooleanSystemPropertyValue(string: str) -> bool: ...
    @typing.overload
    @staticmethod
    def getBooleanSystemPropertyValue(string: str, boolean: bool) -> bool: ...
    @staticmethod
    def getProperty(stringArray: typing.List[str], string2: str) -> str: ...
    @staticmethod
    def parseBooleanSystemPropertyValue(string: str) -> bool: ...
    @staticmethod
    def resolvePlaceholders(string: str) -> str: ...

class Trace:
    """
    Java class 'cern.accsoft.commons.util.Trace'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    def dumpMeasurement(self, outputStream: java.io.OutputStream) -> None: ...
    @typing.overload
    def dumpMeasurement(self, string: str, outputStream: java.io.OutputStream) -> None: ...
    @staticmethod
    def dumpMeasurements(outputStream: java.io.OutputStream) -> None: ...
    @staticmethod
    def getHumanReadableTime(long: int) -> str: ...
    @staticmethod
    def getInstance(string: str) -> 'Trace': ...
    def getName(self) -> str: ...
    @staticmethod
    def isTraceEnabled() -> bool: ...
    @staticmethod
    def printArray(objectArray: typing.List[typing.Any]) -> None: ...
    def printMeasurement(self, boolean: bool, string: str, string2: str, string3: str) -> int: ...
    def printMessage(self, boolean: bool, string: str, string2: str) -> None: ...
    def resetMeasurement(self) -> None: ...
    @staticmethod
    def resetMeasurements() -> None: ...
    @staticmethod
    def setStringLength(string: str, int: int) -> str: ...
    @staticmethod
    def setTraceEnabled(boolean: bool) -> None: ...
    def startMeasurement(self, boolean: bool, string: str, string2: str) -> None: ...

class UnitExponents:
    """
    Java class 'cern.accsoft.commons.util.UnitExponents'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def getUnit(string: str, int: int) -> str: ...

_AbstractImmutableNamed__N = typing.TypeVar('_AbstractImmutableNamed__N', bound=Named)  # <N>
class AbstractImmutableNamed(Named, java.lang.Comparable[_AbstractImmutableNamed__N], typing.Generic[_AbstractImmutableNamed__N]):
    """
    Java class 'cern.accsoft.commons.util.AbstractImmutableNamed'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.Named, java.lang.Comparable
    
    """
    def compareTo(self, n: _AbstractImmutableNamed__N) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

_AbstractImmutableNamedSerializable__N = typing.TypeVar('_AbstractImmutableNamedSerializable__N', bound=Named)  # <N>
class AbstractImmutableNamedSerializable(Named, java.lang.Comparable[_AbstractImmutableNamedSerializable__N], java.io.Serializable, typing.Generic[_AbstractImmutableNamedSerializable__N]):
    """
    Java class 'cern.accsoft.commons.util.AbstractImmutableNamedSerializable'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.Named, java.lang.Comparable,
            java.io.Serializable
    
    """
    def compareTo(self, n: _AbstractImmutableNamedSerializable__N) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

_AbstractNamed__N = typing.TypeVar('_AbstractNamed__N', bound=Named)  # <N>
class AbstractNamed(Named, java.lang.Comparable[_AbstractNamed__N], typing.Generic[_AbstractNamed__N]):
    """
    Java class 'cern.accsoft.commons.util.AbstractNamed'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.Named, java.lang.Comparable
    
    """
    def compareTo(self, n: _AbstractNamed__N) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def setName(self, string: str) -> None: ...
    def toString(self) -> str: ...

_AbstractNamedSerializable__N = typing.TypeVar('_AbstractNamedSerializable__N', bound=Named)  # <N>
class AbstractNamedSerializable(Named, java.lang.Comparable[_AbstractNamedSerializable__N], java.io.Serializable, typing.Generic[_AbstractNamedSerializable__N]):
    """
    Java class 'cern.accsoft.commons.util.AbstractNamedSerializable'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.Named, java.lang.Comparable,
            java.io.Serializable
    
    """
    def compareTo(self, n: _AbstractNamedSerializable__N) -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def setName(self, string: str) -> None: ...
    def toString(self) -> str: ...

_Filters__Filter__T = typing.TypeVar('_Filters__Filter__T')  # <T>
_Filters__FilterSourceAndDestCollectionHolder__T = typing.TypeVar('_Filters__FilterSourceAndDestCollectionHolder__T')  # <T>
_Filters__FilterSourceAndDestCollectionHolder__D = typing.TypeVar('_Filters__FilterSourceAndDestCollectionHolder__D', bound=java.util.Collection)  # <D>
_Filters__FilterSourceCollectionHolder__T = typing.TypeVar('_Filters__FilterSourceCollectionHolder__T')  # <T>
_Filters__FilterSourceCollectionHolder__C = typing.TypeVar('_Filters__FilterSourceCollectionHolder__C', bound=java.util.Collection)  # <C>
class Filters:
    """
    Java class 'cern.accsoft.commons.util.Filters'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Filters()
    
    """
    def __init__(self): ...
    _filter_0__T = typing.TypeVar('_filter_0__T')  # <T>
    _filter_1__T = typing.TypeVar('_filter_1__T')  # <T>
    _filter_2__T = typing.TypeVar('_filter_2__T')  # <T>
    @typing.overload
    @staticmethod
    def filter(collection: typing.Union[java.util.Collection[_filter_0__T], typing.Sequence[_filter_0__T]]) -> 'Filters.FilterSourceCollectionHolder'[_filter_0__T, java.util.Collection[_filter_0__T]]: ...
    @typing.overload
    @staticmethod
    def filter(list: java.util.List[_filter_1__T]) -> 'Filters.FilterSourceCollectionHolder'[_filter_1__T, java.util.List[_filter_1__T]]: ...
    @typing.overload
    @staticmethod
    def filter(set: java.util.Set[_filter_2__T]) -> 'Filters.FilterSourceCollectionHolder'[_filter_2__T, java.util.Set[_filter_2__T]]: ...
    class Filter(typing.Generic[_Filters__Filter__T]):
        """
        Java class 'cern.accsoft.commons.util.Filters$Filter'
        
        """
        def accepts(self, t: _Filters__Filter__T) -> bool: ...
    class FilterSourceAndDestCollectionHolder(cern.accsoft.commons.util.Filters.FilterCollectionHolder[_Filters__FilterSourceAndDestCollectionHolder__T, java.util.Collection[_Filters__FilterSourceAndDestCollectionHolder__T], _Filters__FilterSourceAndDestCollectionHolder__D], typing.Generic[_Filters__FilterSourceAndDestCollectionHolder__T, _Filters__FilterSourceAndDestCollectionHolder__D]): ...
    class FilterSourceCollectionHolder(cern.accsoft.commons.util.Filters.FilterCollectionHolder[_Filters__FilterSourceCollectionHolder__T, _Filters__FilterSourceCollectionHolder__C, _Filters__FilterSourceCollectionHolder__C], typing.Generic[_Filters__FilterSourceCollectionHolder__T, _Filters__FilterSourceCollectionHolder__C]):
        """
        Java class 'cern.accsoft.commons.util.Filters$FilterSourceCollectionHolder'
        
            Extends:
                cern.accsoft.commons.util.Filters$FilterCollectionHolder
        
        """
        _to__D = typing.TypeVar('_to__D', bound=java.util.Collection)  # <D>
        def to(self, d: _to__D) -> 'Filters.FilterSourceAndDestCollectionHolder'[_Filters__FilterSourceCollectionHolder__T, _to__D]: ...
    class FilterCollectionHolder: ...

_Mappers__FlatMapSourceAndDestCollectionHolder__S = typing.TypeVar('_Mappers__FlatMapSourceAndDestCollectionHolder__S')  # <S>
_Mappers__FlatMapSourceAndDestCollectionHolder__D = typing.TypeVar('_Mappers__FlatMapSourceAndDestCollectionHolder__D')  # <D>
_Mappers__FlatMapSourceAndDestCollectionHolder__C = typing.TypeVar('_Mappers__FlatMapSourceAndDestCollectionHolder__C', bound=java.util.Collection)  # <C>
_Mappers__FlatMapSourceCollectionHolder__S = typing.TypeVar('_Mappers__FlatMapSourceCollectionHolder__S')  # <S>
_Mappers__GroupSourceCollectionHolder__S = typing.TypeVar('_Mappers__GroupSourceCollectionHolder__S')  # <S>
_Mappers__GroupSourceCollectionHolder__C = typing.TypeVar('_Mappers__GroupSourceCollectionHolder__C', bound=java.util.Collection)  # <C>
_Mappers__MapBySourceAndDestCollectionHolder__S = typing.TypeVar('_Mappers__MapBySourceAndDestCollectionHolder__S')  # <S>
_Mappers__MapBySourceAndDestCollectionHolder__D = typing.TypeVar('_Mappers__MapBySourceAndDestCollectionHolder__D')  # <D>
_Mappers__MapBySourceAndDestCollectionHolder__M = typing.TypeVar('_Mappers__MapBySourceAndDestCollectionHolder__M', bound=java.util.Map)  # <M>
_Mappers__MapSourceCollectionHolder__S = typing.TypeVar('_Mappers__MapSourceCollectionHolder__S')  # <S>
_Mappers__MapToSourceAndDestCollectionHolder__S = typing.TypeVar('_Mappers__MapToSourceAndDestCollectionHolder__S')  # <S>
_Mappers__MapToSourceAndDestCollectionHolder__D = typing.TypeVar('_Mappers__MapToSourceAndDestCollectionHolder__D')  # <D>
_Mappers__MapToSourceAndDestCollectionHolder__C = typing.TypeVar('_Mappers__MapToSourceAndDestCollectionHolder__C', bound=java.util.Collection)  # <C>
_Mappers__Mapper__S = typing.TypeVar('_Mappers__Mapper__S')  # <S>
_Mappers__Mapper__D = typing.TypeVar('_Mappers__Mapper__D')  # <D>
class Mappers:
    """
    Java class 'cern.accsoft.commons.util.Mappers'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Mappers()
    
    """
    def __init__(self): ...
    _flatMap__S = typing.TypeVar('_flatMap__S')  # <S>
    @staticmethod
    def flatMap(collection: typing.Union[java.util.Collection[_flatMap__S], typing.Sequence[_flatMap__S]]) -> 'Mappers.FlatMapSourceCollectionHolder'[_flatMap__S]: ...
    _group_0__S = typing.TypeVar('_group_0__S')  # <S>
    _group_1__S = typing.TypeVar('_group_1__S')  # <S>
    _group_2__S = typing.TypeVar('_group_2__S')  # <S>
    @typing.overload
    @staticmethod
    def group(collection: typing.Union[java.util.Collection[_group_0__S], typing.Sequence[_group_0__S]]) -> 'Mappers.GroupSourceCollectionHolder'[_group_0__S, java.util.Collection[_group_0__S]]: ...
    @typing.overload
    @staticmethod
    def group(list: java.util.List[_group_1__S]) -> 'Mappers.GroupSourceCollectionHolder'[_group_1__S, java.util.List[_group_1__S]]: ...
    @typing.overload
    @staticmethod
    def group(set: java.util.Set[_group_2__S]) -> 'Mappers.GroupSourceCollectionHolder'[_group_2__S, java.util.Set[_group_2__S]]: ...
    _map__S = typing.TypeVar('_map__S')  # <S>
    @staticmethod
    def map(collection: typing.Union[java.util.Collection[_map__S], typing.Sequence[_map__S]]) -> 'Mappers.MapSourceCollectionHolder'[_map__S]: ...
    class FlatMapSourceAndDestCollectionHolder(cern.accsoft.commons.util.Mappers.SourceCollectionHolder[_Mappers__FlatMapSourceAndDestCollectionHolder__S], typing.Generic[_Mappers__FlatMapSourceAndDestCollectionHolder__S, _Mappers__FlatMapSourceAndDestCollectionHolder__D, _Mappers__FlatMapSourceAndDestCollectionHolder__C]):
        """
        Java class 'cern.accsoft.commons.util.Mappers$FlatMapSourceAndDestCollectionHolder'
        
            Extends:
                cern.accsoft.commons.util.Mappers$SourceCollectionHolder
        
        """
        def of(self, mapper: 'Mappers.Mapper'[_Mappers__FlatMapSourceAndDestCollectionHolder__S, typing.Union[java.util.Collection[_Mappers__FlatMapSourceAndDestCollectionHolder__D], typing.Sequence[_Mappers__FlatMapSourceAndDestCollectionHolder__D]]]) -> _Mappers__FlatMapSourceAndDestCollectionHolder__C: ...
    class FlatMapSourceCollectionHolder(cern.accsoft.commons.util.Mappers.SourceCollectionHolder[_Mappers__FlatMapSourceCollectionHolder__S], typing.Generic[_Mappers__FlatMapSourceCollectionHolder__S]):
        """
        Java class 'cern.accsoft.commons.util.Mappers$FlatMapSourceCollectionHolder'
        
            Extends:
                cern.accsoft.commons.util.Mappers$SourceCollectionHolder
        
        """
        _to__D = typing.TypeVar('_to__D')  # <D>
        _to__C = typing.TypeVar('_to__C', bound=java.util.Collection)  # <C>
        def to(self, c: _to__C) -> 'Mappers.FlatMapSourceAndDestCollectionHolder'[_Mappers__FlatMapSourceCollectionHolder__S, _to__D, _to__C]: ...
        _toListOf__D = typing.TypeVar('_toListOf__D')  # <D>
        def toListOf(self, mapper: 'Mappers.Mapper'[_Mappers__FlatMapSourceCollectionHolder__S, typing.Union[java.util.Collection[_toListOf__D], typing.Sequence[_toListOf__D]]]) -> java.util.List[_toListOf__D]: ...
        _toSetOf__D = typing.TypeVar('_toSetOf__D')  # <D>
        def toSetOf(self, mapper: 'Mappers.Mapper'[_Mappers__FlatMapSourceCollectionHolder__S, typing.Union[java.util.Collection[_toSetOf__D], typing.Sequence[_toSetOf__D]]]) -> java.util.Set[_toSetOf__D]: ...
    class GroupSourceCollectionHolder(typing.Generic[_Mappers__GroupSourceCollectionHolder__S, _Mappers__GroupSourceCollectionHolder__C]):
        """
        Java class 'cern.accsoft.commons.util.Mappers$GroupSourceCollectionHolder'
        
            Extends:
                java.lang.Object
        
        """
        _by__D = typing.TypeVar('_by__D')  # <D>
        def by(self, mapper: 'Mappers.Mapper'[_Mappers__GroupSourceCollectionHolder__S, _by__D]) -> java.util.Map[_by__D, _Mappers__GroupSourceCollectionHolder__C]: ...
    class MapBySourceAndDestCollectionHolder(cern.accsoft.commons.util.Mappers.SourceCollectionHolder[_Mappers__MapBySourceAndDestCollectionHolder__S], typing.Generic[_Mappers__MapBySourceAndDestCollectionHolder__S, _Mappers__MapBySourceAndDestCollectionHolder__D, _Mappers__MapBySourceAndDestCollectionHolder__M]):
        """
        Java class 'cern.accsoft.commons.util.Mappers$MapBySourceAndDestCollectionHolder'
        
            Extends:
                cern.accsoft.commons.util.Mappers$SourceCollectionHolder
        
        """
        def by(self, mapper: 'Mappers.Mapper'[_Mappers__MapBySourceAndDestCollectionHolder__S, _Mappers__MapBySourceAndDestCollectionHolder__D]) -> _Mappers__MapBySourceAndDestCollectionHolder__M: ...
    class MapSourceCollectionHolder(cern.accsoft.commons.util.Mappers.SourceCollectionHolder[_Mappers__MapSourceCollectionHolder__S], typing.Generic[_Mappers__MapSourceCollectionHolder__S]):
        """
        Java class 'cern.accsoft.commons.util.Mappers$MapSourceCollectionHolder'
        
            Extends:
                cern.accsoft.commons.util.Mappers$SourceCollectionHolder
        
        """
        _by__D = typing.TypeVar('_by__D')  # <D>
        def by(self, mapper: 'Mappers.Mapper'[_Mappers__MapSourceCollectionHolder__S, _by__D]) -> java.util.Map[_by__D, _Mappers__MapSourceCollectionHolder__S]: ...
        _to_0__D = typing.TypeVar('_to_0__D')  # <D>
        _to_0__M = typing.TypeVar('_to_0__M', bound=java.util.Map)  # <M>
        _to_1__D = typing.TypeVar('_to_1__D')  # <D>
        _to_1__C = typing.TypeVar('_to_1__C', bound=java.util.Collection)  # <C>
        @typing.overload
        def to(self, m: _to_0__M) -> 'Mappers.MapBySourceAndDestCollectionHolder'[_Mappers__MapSourceCollectionHolder__S, _to_0__D, _to_0__M]: ...
        @typing.overload
        def to(self, c: _to_1__C) -> 'Mappers.MapToSourceAndDestCollectionHolder'[_Mappers__MapSourceCollectionHolder__S, _to_1__D, _to_1__C]: ...
        _toListOf__D = typing.TypeVar('_toListOf__D')  # <D>
        def toListOf(self, mapper: 'Mappers.Mapper'[_Mappers__MapSourceCollectionHolder__S, _toListOf__D]) -> java.util.List[_toListOf__D]: ...
        _toSetOf__D = typing.TypeVar('_toSetOf__D')  # <D>
        def toSetOf(self, mapper: 'Mappers.Mapper'[_Mappers__MapSourceCollectionHolder__S, _toSetOf__D]) -> java.util.Set[_toSetOf__D]: ...
    class MapToSourceAndDestCollectionHolder(cern.accsoft.commons.util.Mappers.SourceCollectionHolder[_Mappers__MapToSourceAndDestCollectionHolder__S], typing.Generic[_Mappers__MapToSourceAndDestCollectionHolder__S, _Mappers__MapToSourceAndDestCollectionHolder__D, _Mappers__MapToSourceAndDestCollectionHolder__C]):
        """
        Java class 'cern.accsoft.commons.util.Mappers$MapToSourceAndDestCollectionHolder'
        
            Extends:
                cern.accsoft.commons.util.Mappers$SourceCollectionHolder
        
        """
        def of(self, mapper: 'Mappers.Mapper'[_Mappers__MapToSourceAndDestCollectionHolder__S, _Mappers__MapToSourceAndDestCollectionHolder__D]) -> _Mappers__MapToSourceAndDestCollectionHolder__C: ...
    class Mapper(typing.Generic[_Mappers__Mapper__S, _Mappers__Mapper__D]):
        """
        Java class 'cern.accsoft.commons.util.Mappers$Mapper'
        
        """
        def map(self, s2: _Mappers__Mapper__S) -> _Mappers__Mapper__D: ...
    class SourceCollectionHolder: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util")``.

    AbstractImmutableNamed: typing.Type[AbstractImmutableNamed]
    AbstractImmutableNamedSerializable: typing.Type[AbstractImmutableNamedSerializable]
    AbstractNamed: typing.Type[AbstractNamed]
    AbstractNamedSerializable: typing.Type[AbstractNamedSerializable]
    AppLauncher: typing.Type[AppLauncher]
    ArrayUtils: typing.Type[ArrayUtils]
    Assert: typing.Type[Assert]
    BeanSupport: typing.Type[BeanSupport]
    BeanUtils: typing.Type[BeanUtils]
    ClassLoaderJarInfo: typing.Type[ClassLoaderJarInfo]
    ClassLoaderUtils: typing.Type[ClassLoaderUtils]
    ClassUtils: typing.Type[ClassUtils]
    ClasspathUtils: typing.Type[ClasspathUtils]
    Cleanable: typing.Type[Cleanable]
    CleanableUtil: typing.Type[CleanableUtil]
    CollectionUtils: typing.Type[CollectionUtils]
    ExceptionUtils: typing.Type[ExceptionUtils]
    FileCopyUtils: typing.Type[FileCopyUtils]
    FileUtils: typing.Type[FileUtils]
    Filters: typing.Type[Filters]
    JarInfo: typing.Type[JarInfo]
    JdkUtils: typing.Type[JdkUtils]
    MapUtils: typing.Type[MapUtils]
    Mappers: typing.Type[Mappers]
    MockitoUtil: typing.Type[MockitoUtil]
    Named: typing.Type[Named]
    Nameds: typing.Type[Nameds]
    NumberUtils: typing.Type[NumberUtils]
    OSUtils: typing.Type[OSUtils]
    ObjectUtils: typing.Type[ObjectUtils]
    PcropsRepositoryDownloader: typing.Type[PcropsRepositoryDownloader]
    PcropsRepositoryJnlpSearcher: typing.Type[PcropsRepositoryJnlpSearcher]
    PcropsRepositoryProductUsageSearcher: typing.Type[PcropsRepositoryProductUsageSearcher]
    ProcessUtils: typing.Type[ProcessUtils]
    ReflectionUtils: typing.Type[ReflectionUtils]
    ResourceUtils: typing.Type[ResourceUtils]
    SerializationObjectCloner: typing.Type[SerializationObjectCloner]
    StringUtils: typing.Type[StringUtils]
    SystemPropertyUtils: typing.Type[SystemPropertyUtils]
    Trace: typing.Type[Trace]
    UnitExponents: typing.Type[UnitExponents]
    annotation: cern.accsoft.commons.util.annotation.__module_protocol__
    collections: cern.accsoft.commons.util.collections.__module_protocol__
    concurrent: cern.accsoft.commons.util.concurrent.__module_protocol__
    enums: cern.accsoft.commons.util.enums.__module_protocol__
    event: cern.accsoft.commons.util.event.__module_protocol__
    executor: cern.accsoft.commons.util.executor.__module_protocol__
    format: cern.accsoft.commons.util.format.__module_protocol__
    jmx: cern.accsoft.commons.util.jmx.__module_protocol__
    mail: cern.accsoft.commons.util.mail.__module_protocol__
    marker: cern.accsoft.commons.util.marker.__module_protocol__
    metric: cern.accsoft.commons.util.metric.__module_protocol__
    proc: cern.accsoft.commons.util.proc.__module_protocol__
    rba: cern.accsoft.commons.util.rba.__module_protocol__
    reflect: cern.accsoft.commons.util.reflect.__module_protocol__
    regexp: cern.accsoft.commons.util.regexp.__module_protocol__
    remoting: cern.accsoft.commons.util.remoting.__module_protocol__
    traceid: cern.accsoft.commons.util.traceid.__module_protocol__
    trigger: cern.accsoft.commons.util.trigger.__module_protocol__
    userctx: cern.accsoft.commons.util.userctx.__module_protocol__
    userinfo: cern.accsoft.commons.util.userinfo.__module_protocol__
    value: cern.accsoft.commons.util.value.__module_protocol__
    xml: cern.accsoft.commons.util.xml.__module_protocol__
