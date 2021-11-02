import java.io
import java.lang
import java.net
import java.nio.channels
import java.nio.charset
import java.nio.file.attribute
import java.nio.file.spi
import java.security
import java.util
import java.util.concurrent
import java.util.function
import java.util.stream
import jpype.protocol
import typing



class AccessMode(java.lang.Enum['AccessMode']):
    READ: typing.ClassVar['AccessMode'] = ...
    WRITE: typing.ClassVar['AccessMode'] = ...
    EXECUTE: typing.ClassVar['AccessMode'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AccessMode': ...
    @staticmethod
    def values() -> typing.List['AccessMode']: ...

class ClosedDirectoryStreamException(java.lang.IllegalStateException):
    def __init__(self): ...

class ClosedFileSystemException(java.lang.IllegalStateException):
    def __init__(self): ...

class ClosedWatchServiceException(java.lang.IllegalStateException):
    def __init__(self): ...

class CopyOption: ...

class DirectoryIteratorException(java.util.ConcurrentModificationException):
    def __init__(self, iOException: java.io.IOException): ...
    def getCause(self) -> java.io.IOException: ...

_DirectoryStream__Filter__T = typing.TypeVar('_DirectoryStream__Filter__T')  # <T>
_DirectoryStream__T = typing.TypeVar('_DirectoryStream__T')  # <T>
class DirectoryStream(java.io.Closeable, java.lang.Iterable[_DirectoryStream__T], typing.Generic[_DirectoryStream__T]):
    def iterator(self) -> java.util.Iterator[_DirectoryStream__T]: ...
    class Filter(typing.Generic[_DirectoryStream__Filter__T]):
        def accept(self, t: _DirectoryStream__Filter__T) -> bool: ...

class FileStore:
    def getAttribute(self, string: str) -> typing.Any: ...
    def getBlockSize(self) -> int: ...
    _getFileStoreAttributeView__V = typing.TypeVar('_getFileStoreAttributeView__V', bound=java.nio.file.attribute.FileStoreAttributeView)  # <V>
    def getFileStoreAttributeView(self, class_: typing.Type[_getFileStoreAttributeView__V]) -> _getFileStoreAttributeView__V: ...
    def getTotalSpace(self) -> int: ...
    def getUnallocatedSpace(self) -> int: ...
    def getUsableSpace(self) -> int: ...
    def isReadOnly(self) -> bool: ...
    def name(self) -> str: ...
    @typing.overload
    def supportsFileAttributeView(self, class_: typing.Type[java.nio.file.attribute.FileAttributeView]) -> bool: ...
    @typing.overload
    def supportsFileAttributeView(self, string: str) -> bool: ...
    def type(self) -> str: ...

class FileSystem(java.io.Closeable):
    def close(self) -> None: ...
    def getFileStores(self) -> java.lang.Iterable[FileStore]: ...
    def getPath(self, string: str, stringArray: typing.List[str]) -> 'Path': ...
    def getPathMatcher(self, string: str) -> 'PathMatcher': ...
    def getRootDirectories(self) -> java.lang.Iterable['Path']: ...
    def getSeparator(self) -> str: ...
    def getUserPrincipalLookupService(self) -> java.nio.file.attribute.UserPrincipalLookupService: ...
    def isOpen(self) -> bool: ...
    def isReadOnly(self) -> bool: ...
    def newWatchService(self) -> 'WatchService': ...
    def provider(self) -> java.nio.file.spi.FileSystemProvider: ...
    def supportedFileAttributeViews(self) -> java.util.Set[str]: ...

class FileSystemAlreadyExistsException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class FileSystemException(java.io.IOException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...
    def getFile(self) -> str: ...
    def getMessage(self) -> str: ...
    def getOtherFile(self) -> str: ...
    def getReason(self) -> str: ...

class FileSystemNotFoundException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class FileSystems:
    @staticmethod
    def getDefault() -> FileSystem: ...
    @staticmethod
    def getFileSystem(uRI: java.net.URI) -> FileSystem: ...
    @typing.overload
    @staticmethod
    def newFileSystem(uRI: java.net.URI, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]) -> FileSystem: ...
    @typing.overload
    @staticmethod
    def newFileSystem(uRI: java.net.URI, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]], classLoader: java.lang.ClassLoader) -> FileSystem: ...
    @typing.overload
    @staticmethod
    def newFileSystem(path: typing.Union['Path', jpype.protocol.SupportsPath], classLoader: java.lang.ClassLoader) -> FileSystem: ...

class FileVisitOption(java.lang.Enum['FileVisitOption']):
    FOLLOW_LINKS: typing.ClassVar['FileVisitOption'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'FileVisitOption': ...
    @staticmethod
    def values() -> typing.List['FileVisitOption']: ...

class FileVisitResult(java.lang.Enum['FileVisitResult']):
    CONTINUE: typing.ClassVar['FileVisitResult'] = ...
    TERMINATE: typing.ClassVar['FileVisitResult'] = ...
    SKIP_SUBTREE: typing.ClassVar['FileVisitResult'] = ...
    SKIP_SIBLINGS: typing.ClassVar['FileVisitResult'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'FileVisitResult': ...
    @staticmethod
    def values() -> typing.List['FileVisitResult']: ...

_FileVisitor__T = typing.TypeVar('_FileVisitor__T')  # <T>
class FileVisitor(typing.Generic[_FileVisitor__T]):
    def postVisitDirectory(self, t: _FileVisitor__T, iOException: java.io.IOException) -> FileVisitResult: ...
    def preVisitDirectory(self, t: _FileVisitor__T, basicFileAttributes: java.nio.file.attribute.BasicFileAttributes) -> FileVisitResult: ...
    def visitFile(self, t: _FileVisitor__T, basicFileAttributes: java.nio.file.attribute.BasicFileAttributes) -> FileVisitResult: ...
    def visitFileFailed(self, t: _FileVisitor__T, iOException: java.io.IOException) -> FileVisitResult: ...

class Files:
    @typing.overload
    @staticmethod
    def copy(path: typing.Union['Path', jpype.protocol.SupportsPath], path2: typing.Union['Path', jpype.protocol.SupportsPath], copyOptionArray: typing.List[CopyOption]) -> 'Path': ...
    @typing.overload
    @staticmethod
    def copy(inputStream: java.io.InputStream, path: typing.Union['Path', jpype.protocol.SupportsPath], copyOptionArray: typing.List[CopyOption]) -> int: ...
    @typing.overload
    @staticmethod
    def copy(path: typing.Union['Path', jpype.protocol.SupportsPath], outputStream: java.io.OutputStream) -> int: ...
    @staticmethod
    def createDirectories(path: typing.Union['Path', jpype.protocol.SupportsPath], fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @staticmethod
    def createDirectory(path: typing.Union['Path', jpype.protocol.SupportsPath], fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @staticmethod
    def createFile(path: typing.Union['Path', jpype.protocol.SupportsPath], fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @staticmethod
    def createLink(path: typing.Union['Path', jpype.protocol.SupportsPath], path2: typing.Union['Path', jpype.protocol.SupportsPath]) -> 'Path': ...
    @staticmethod
    def createSymbolicLink(path: typing.Union['Path', jpype.protocol.SupportsPath], path2: typing.Union['Path', jpype.protocol.SupportsPath], fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @typing.overload
    @staticmethod
    def createTempDirectory(string: str, fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @typing.overload
    @staticmethod
    def createTempDirectory(path: typing.Union['Path', jpype.protocol.SupportsPath], string: str, fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @typing.overload
    @staticmethod
    def createTempFile(string: str, string2: str, fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @typing.overload
    @staticmethod
    def createTempFile(path: typing.Union['Path', jpype.protocol.SupportsPath], string: str, string2: str, fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'Path': ...
    @staticmethod
    def delete(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> None: ...
    @staticmethod
    def deleteIfExists(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> bool: ...
    @staticmethod
    def exists(path: typing.Union['Path', jpype.protocol.SupportsPath], linkOptionArray: typing.List['LinkOption']) -> bool: ...
    @staticmethod
    def find(path: typing.Union['Path', jpype.protocol.SupportsPath], int: int, biPredicate: typing.Union[java.util.function.BiPredicate[typing.Union['Path', jpype.protocol.SupportsPath], java.nio.file.attribute.BasicFileAttributes], typing.Callable[[typing.Union['Path', jpype.protocol.SupportsPath], java.nio.file.attribute.BasicFileAttributes], bool]], fileVisitOptionArray: typing.List[FileVisitOption]) -> java.util.stream.Stream['Path']: ...
    @staticmethod
    def getAttribute(path: typing.Union['Path', jpype.protocol.SupportsPath], string: str, linkOptionArray: typing.List['LinkOption']) -> typing.Any: ...
    _getFileAttributeView__V = typing.TypeVar('_getFileAttributeView__V', bound=java.nio.file.attribute.FileAttributeView)  # <V>
    @staticmethod
    def getFileAttributeView(path: typing.Union['Path', jpype.protocol.SupportsPath], class_: typing.Type[_getFileAttributeView__V], linkOptionArray: typing.List['LinkOption']) -> _getFileAttributeView__V: ...
    @staticmethod
    def getFileStore(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> FileStore: ...
    @staticmethod
    def getLastModifiedTime(path: typing.Union['Path', jpype.protocol.SupportsPath], linkOptionArray: typing.List['LinkOption']) -> java.nio.file.attribute.FileTime: ...
    @staticmethod
    def getOwner(path: typing.Union['Path', jpype.protocol.SupportsPath], linkOptionArray: typing.List['LinkOption']) -> java.nio.file.attribute.UserPrincipal: ...
    @staticmethod
    def getPosixFilePermissions(path: typing.Union['Path', jpype.protocol.SupportsPath], linkOptionArray: typing.List['LinkOption']) -> java.util.Set[java.nio.file.attribute.PosixFilePermission]: ...
    @staticmethod
    def isDirectory(path: typing.Union['Path', jpype.protocol.SupportsPath], linkOptionArray: typing.List['LinkOption']) -> bool: ...
    @staticmethod
    def isExecutable(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> bool: ...
    @staticmethod
    def isHidden(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> bool: ...
    @staticmethod
    def isReadable(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> bool: ...
    @staticmethod
    def isRegularFile(path: typing.Union['Path', jpype.protocol.SupportsPath], linkOptionArray: typing.List['LinkOption']) -> bool: ...
    @staticmethod
    def isSameFile(path: typing.Union['Path', jpype.protocol.SupportsPath], path2: typing.Union['Path', jpype.protocol.SupportsPath]) -> bool: ...
    @staticmethod
    def isSymbolicLink(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> bool: ...
    @staticmethod
    def isWritable(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> bool: ...
    @typing.overload
    @staticmethod
    def lines(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> java.util.stream.Stream[str]: ...
    @typing.overload
    @staticmethod
    def lines(path: typing.Union['Path', jpype.protocol.SupportsPath], charset: java.nio.charset.Charset) -> java.util.stream.Stream[str]: ...
    @staticmethod
    def list(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> java.util.stream.Stream['Path']: ...
    @staticmethod
    def move(path: typing.Union['Path', jpype.protocol.SupportsPath], path2: typing.Union['Path', jpype.protocol.SupportsPath], copyOptionArray: typing.List[CopyOption]) -> 'Path': ...
    @typing.overload
    @staticmethod
    def newBufferedReader(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> java.io.BufferedReader: ...
    @typing.overload
    @staticmethod
    def newBufferedReader(path: typing.Union['Path', jpype.protocol.SupportsPath], charset: java.nio.charset.Charset) -> java.io.BufferedReader: ...
    @typing.overload
    @staticmethod
    def newBufferedWriter(path: typing.Union['Path', jpype.protocol.SupportsPath], charset: java.nio.charset.Charset, openOptionArray: typing.List['OpenOption']) -> java.io.BufferedWriter: ...
    @typing.overload
    @staticmethod
    def newBufferedWriter(path: typing.Union['Path', jpype.protocol.SupportsPath], openOptionArray: typing.List['OpenOption']) -> java.io.BufferedWriter: ...
    @typing.overload
    @staticmethod
    def newByteChannel(path: typing.Union['Path', jpype.protocol.SupportsPath], openOptionArray: typing.List['OpenOption']) -> java.nio.channels.SeekableByteChannel: ...
    @typing.overload
    @staticmethod
    def newByteChannel(path: typing.Union['Path', jpype.protocol.SupportsPath], set: java.util.Set['OpenOption'], fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> java.nio.channels.SeekableByteChannel: ...
    @typing.overload
    @staticmethod
    def newDirectoryStream(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> DirectoryStream['Path']: ...
    @typing.overload
    @staticmethod
    def newDirectoryStream(path: typing.Union['Path', jpype.protocol.SupportsPath], string: str) -> DirectoryStream['Path']: ...
    @typing.overload
    @staticmethod
    def newDirectoryStream(path: typing.Union['Path', jpype.protocol.SupportsPath], filter: typing.Union[DirectoryStream.Filter['Path'], typing.Callable[['Path'], bool]]) -> DirectoryStream['Path']: ...
    @staticmethod
    def newInputStream(path: typing.Union['Path', jpype.protocol.SupportsPath], openOptionArray: typing.List['OpenOption']) -> java.io.InputStream: ...
    @staticmethod
    def newOutputStream(path: typing.Union['Path', jpype.protocol.SupportsPath], openOptionArray: typing.List['OpenOption']) -> java.io.OutputStream: ...
    @staticmethod
    def notExists(path: typing.Union['Path', jpype.protocol.SupportsPath], linkOptionArray: typing.List['LinkOption']) -> bool: ...
    @staticmethod
    def probeContentType(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> str: ...
    @staticmethod
    def readAllBytes(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> typing.List[int]: ...
    @typing.overload
    @staticmethod
    def readAllLines(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> java.util.List[str]: ...
    @typing.overload
    @staticmethod
    def readAllLines(path: typing.Union['Path', jpype.protocol.SupportsPath], charset: java.nio.charset.Charset) -> java.util.List[str]: ...
    _readAttributes_0__A = typing.TypeVar('_readAttributes_0__A', bound=java.nio.file.attribute.BasicFileAttributes)  # <A>
    @typing.overload
    @staticmethod
    def readAttributes(path: typing.Union['Path', jpype.protocol.SupportsPath], class_: typing.Type[_readAttributes_0__A], linkOptionArray: typing.List['LinkOption']) -> _readAttributes_0__A: ...
    @typing.overload
    @staticmethod
    def readAttributes(path: typing.Union['Path', jpype.protocol.SupportsPath], string: str, linkOptionArray: typing.List['LinkOption']) -> java.util.Map[str, typing.Any]: ...
    @typing.overload
    @staticmethod
    def readString(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> str: ...
    @typing.overload
    @staticmethod
    def readString(path: typing.Union['Path', jpype.protocol.SupportsPath], charset: java.nio.charset.Charset) -> str: ...
    @staticmethod
    def readSymbolicLink(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> 'Path': ...
    @staticmethod
    def setAttribute(path: typing.Union['Path', jpype.protocol.SupportsPath], string: str, object: typing.Any, linkOptionArray: typing.List['LinkOption']) -> 'Path': ...
    @staticmethod
    def setLastModifiedTime(path: typing.Union['Path', jpype.protocol.SupportsPath], fileTime: java.nio.file.attribute.FileTime) -> 'Path': ...
    @staticmethod
    def setOwner(path: typing.Union['Path', jpype.protocol.SupportsPath], userPrincipal: java.nio.file.attribute.UserPrincipal) -> 'Path': ...
    @staticmethod
    def setPosixFilePermissions(path: typing.Union['Path', jpype.protocol.SupportsPath], set: java.util.Set[java.nio.file.attribute.PosixFilePermission]) -> 'Path': ...
    @staticmethod
    def size(path: typing.Union['Path', jpype.protocol.SupportsPath]) -> int: ...
    @typing.overload
    @staticmethod
    def walk(path: typing.Union['Path', jpype.protocol.SupportsPath], int: int, fileVisitOptionArray: typing.List[FileVisitOption]) -> java.util.stream.Stream['Path']: ...
    @typing.overload
    @staticmethod
    def walk(path: typing.Union['Path', jpype.protocol.SupportsPath], fileVisitOptionArray: typing.List[FileVisitOption]) -> java.util.stream.Stream['Path']: ...
    @typing.overload
    @staticmethod
    def walkFileTree(path: typing.Union['Path', jpype.protocol.SupportsPath], fileVisitor: FileVisitor['Path']) -> 'Path': ...
    @typing.overload
    @staticmethod
    def walkFileTree(path: typing.Union['Path', jpype.protocol.SupportsPath], set: java.util.Set[FileVisitOption], int: int, fileVisitor: FileVisitor['Path']) -> 'Path': ...
    @typing.overload
    @staticmethod
    def write(path: typing.Union['Path', jpype.protocol.SupportsPath], byteArray: typing.List[int], openOptionArray: typing.List['OpenOption']) -> 'Path': ...
    @typing.overload
    @staticmethod
    def write(path: typing.Union['Path', jpype.protocol.SupportsPath], iterable: java.lang.Iterable[java.lang.CharSequence], charset: java.nio.charset.Charset, openOptionArray: typing.List['OpenOption']) -> 'Path': ...
    @typing.overload
    @staticmethod
    def write(path: typing.Union['Path', jpype.protocol.SupportsPath], iterable: java.lang.Iterable[java.lang.CharSequence], openOptionArray: typing.List['OpenOption']) -> 'Path': ...
    @typing.overload
    @staticmethod
    def writeString(path: typing.Union['Path', jpype.protocol.SupportsPath], charSequence: typing.Union[java.lang.CharSequence, str], charset: java.nio.charset.Charset, openOptionArray: typing.List['OpenOption']) -> 'Path': ...
    @typing.overload
    @staticmethod
    def writeString(path: typing.Union['Path', jpype.protocol.SupportsPath], charSequence: typing.Union[java.lang.CharSequence, str], openOptionArray: typing.List['OpenOption']) -> 'Path': ...

class InvalidPathException(java.lang.IllegalArgumentException):
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, int: int): ...
    def getIndex(self) -> int: ...
    def getInput(self) -> str: ...
    def getMessage(self) -> str: ...
    def getReason(self) -> str: ...

class LinkPermission(java.security.BasicPermission):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...

class OpenOption: ...

class PathMatcher:
    def matches(self, path: typing.Union['Path', jpype.protocol.SupportsPath]) -> bool: ...

class Paths:
    @typing.overload
    @staticmethod
    def get(string: str, stringArray: typing.List[str]) -> 'Path': ...
    @typing.overload
    @staticmethod
    def get(uRI: java.net.URI) -> 'Path': ...

class ProviderMismatchException(java.lang.IllegalArgumentException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class ProviderNotFoundException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class ReadOnlyFileSystemException(java.lang.UnsupportedOperationException):
    def __init__(self): ...

class StandardWatchEventKinds:
    OVERFLOW: typing.ClassVar['WatchEvent.Kind'] = ...
    ENTRY_CREATE: typing.ClassVar['WatchEvent.Kind'] = ...
    ENTRY_DELETE: typing.ClassVar['WatchEvent.Kind'] = ...
    ENTRY_MODIFY: typing.ClassVar['WatchEvent.Kind'] = ...

_WatchEvent__Kind__T = typing.TypeVar('_WatchEvent__Kind__T')  # <T>
_WatchEvent__T = typing.TypeVar('_WatchEvent__T')  # <T>
class WatchEvent(typing.Generic[_WatchEvent__T]):
    def context(self) -> _WatchEvent__T: ...
    def count(self) -> int: ...
    def kind(self) -> 'WatchEvent.Kind'[_WatchEvent__T]: ...
    class Kind(typing.Generic[_WatchEvent__Kind__T]):
        def name(self) -> str: ...
        def type(self) -> typing.Type[_WatchEvent__Kind__T]: ...
    class Modifier:
        def name(self) -> str: ...

class WatchKey:
    def cancel(self) -> None: ...
    def isValid(self) -> bool: ...
    def pollEvents(self) -> java.util.List[WatchEvent[typing.Any]]: ...
    def reset(self) -> bool: ...
    def watchable(self) -> 'Watchable': ...

class WatchService(java.io.Closeable):
    def close(self) -> None: ...
    @typing.overload
    def poll(self) -> WatchKey: ...
    @typing.overload
    def poll(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> WatchKey: ...
    def take(self) -> WatchKey: ...

class Watchable:
    @typing.overload
    def register(self, watchService: WatchService, kindArray: typing.List[WatchEvent.Kind[typing.Any]]) -> WatchKey: ...
    @typing.overload
    def register(self, watchService: WatchService, kindArray: typing.List[WatchEvent.Kind[typing.Any]], modifierArray: typing.List[WatchEvent.Modifier]) -> WatchKey: ...

class AccessDeniedException(FileSystemException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...

class AtomicMoveNotSupportedException(FileSystemException):
    def __init__(self, string: str, string2: str, string3: str): ...

class DirectoryNotEmptyException(FileSystemException):
    def __init__(self, string: str): ...

class FileAlreadyExistsException(FileSystemException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...

class FileSystemLoopException(FileSystemException):
    def __init__(self, string: str): ...

class LinkOption(java.lang.Enum['LinkOption'], OpenOption, CopyOption):
    NOFOLLOW_LINKS: typing.ClassVar['LinkOption'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LinkOption': ...
    @staticmethod
    def values() -> typing.List['LinkOption']: ...

class NoSuchFileException(FileSystemException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...

class NotDirectoryException(FileSystemException):
    def __init__(self, string: str): ...

class NotLinkException(FileSystemException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...

class Path(java.lang.Comparable['Path'], java.lang.Iterable['Path'], Watchable):
    def compareTo(self, path: typing.Union['Path', jpype.protocol.SupportsPath]) -> int: ...
    @typing.overload
    def endsWith(self, path: typing.Union['Path', jpype.protocol.SupportsPath]) -> bool: ...
    @typing.overload
    def endsWith(self, string: str) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getFileName(self) -> 'Path': ...
    def getFileSystem(self) -> FileSystem: ...
    def getName(self, int: int) -> 'Path': ...
    def getNameCount(self) -> int: ...
    def getParent(self) -> 'Path': ...
    def getRoot(self) -> 'Path': ...
    def hashCode(self) -> int: ...
    def isAbsolute(self) -> bool: ...
    def iterator(self) -> java.util.Iterator['Path']: ...
    def normalize(self) -> 'Path': ...
    @typing.overload
    @staticmethod
    def of(string: str, stringArray: typing.List[str]) -> 'Path': ...
    @typing.overload
    @staticmethod
    def of(uRI: java.net.URI) -> 'Path': ...
    @typing.overload
    def register(self, watchService: WatchService, kindArray: typing.List[WatchEvent.Kind[typing.Any]], modifierArray: typing.List[WatchEvent.Modifier]) -> WatchKey: ...
    @typing.overload
    def register(self, watchService: WatchService, kindArray: typing.List[WatchEvent.Kind[typing.Any]]) -> WatchKey: ...
    def relativize(self, path: typing.Union['Path', jpype.protocol.SupportsPath]) -> 'Path': ...
    @typing.overload
    def resolve(self, path: typing.Union['Path', jpype.protocol.SupportsPath]) -> 'Path': ...
    @typing.overload
    def resolve(self, string: str) -> 'Path': ...
    @typing.overload
    def resolveSibling(self, string: str) -> 'Path': ...
    @typing.overload
    def resolveSibling(self, path: typing.Union['Path', jpype.protocol.SupportsPath]) -> 'Path': ...
    @typing.overload
    def startsWith(self, path: typing.Union['Path', jpype.protocol.SupportsPath]) -> bool: ...
    @typing.overload
    def startsWith(self, string: str) -> bool: ...
    def subpath(self, int: int, int2: int) -> 'Path': ...
    def toAbsolutePath(self) -> 'Path': ...
    def toFile(self) -> java.io.File: ...
    def toRealPath(self, linkOptionArray: typing.List[LinkOption]) -> 'Path': ...
    def toString(self) -> str: ...
    def toUri(self) -> java.net.URI: ...

_SecureDirectoryStream__T = typing.TypeVar('_SecureDirectoryStream__T')  # <T>
class SecureDirectoryStream(DirectoryStream[_SecureDirectoryStream__T], typing.Generic[_SecureDirectoryStream__T]):
    def deleteDirectory(self, t: _SecureDirectoryStream__T) -> None: ...
    def deleteFile(self, t: _SecureDirectoryStream__T) -> None: ...
    _getFileAttributeView_0__V = typing.TypeVar('_getFileAttributeView_0__V', bound=java.nio.file.attribute.FileAttributeView)  # <V>
    _getFileAttributeView_1__V = typing.TypeVar('_getFileAttributeView_1__V', bound=java.nio.file.attribute.FileAttributeView)  # <V>
    @typing.overload
    def getFileAttributeView(self, class_: typing.Type[_getFileAttributeView_0__V]) -> _getFileAttributeView_0__V: ...
    @typing.overload
    def getFileAttributeView(self, t: _SecureDirectoryStream__T, class_: typing.Type[_getFileAttributeView_1__V], linkOptionArray: typing.List[LinkOption]) -> _getFileAttributeView_1__V: ...
    def move(self, t: _SecureDirectoryStream__T, secureDirectoryStream: 'SecureDirectoryStream'[_SecureDirectoryStream__T], t2: _SecureDirectoryStream__T) -> None: ...
    def newByteChannel(self, t: _SecureDirectoryStream__T, set: java.util.Set[OpenOption], fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> java.nio.channels.SeekableByteChannel: ...
    def newDirectoryStream(self, t: _SecureDirectoryStream__T, linkOptionArray: typing.List[LinkOption]) -> 'SecureDirectoryStream'[_SecureDirectoryStream__T]: ...

_SimpleFileVisitor__T = typing.TypeVar('_SimpleFileVisitor__T')  # <T>
class SimpleFileVisitor(FileVisitor[_SimpleFileVisitor__T], typing.Generic[_SimpleFileVisitor__T]):
    def postVisitDirectory(self, t: _SimpleFileVisitor__T, iOException: java.io.IOException) -> FileVisitResult: ...
    def preVisitDirectory(self, t: _SimpleFileVisitor__T, basicFileAttributes: java.nio.file.attribute.BasicFileAttributes) -> FileVisitResult: ...
    def visitFile(self, t: _SimpleFileVisitor__T, basicFileAttributes: java.nio.file.attribute.BasicFileAttributes) -> FileVisitResult: ...
    def visitFileFailed(self, t: _SimpleFileVisitor__T, iOException: java.io.IOException) -> FileVisitResult: ...

class StandardCopyOption(java.lang.Enum['StandardCopyOption'], CopyOption):
    REPLACE_EXISTING: typing.ClassVar['StandardCopyOption'] = ...
    COPY_ATTRIBUTES: typing.ClassVar['StandardCopyOption'] = ...
    ATOMIC_MOVE: typing.ClassVar['StandardCopyOption'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'StandardCopyOption': ...
    @staticmethod
    def values() -> typing.List['StandardCopyOption']: ...

class StandardOpenOption(java.lang.Enum['StandardOpenOption'], OpenOption):
    READ: typing.ClassVar['StandardOpenOption'] = ...
    WRITE: typing.ClassVar['StandardOpenOption'] = ...
    APPEND: typing.ClassVar['StandardOpenOption'] = ...
    TRUNCATE_EXISTING: typing.ClassVar['StandardOpenOption'] = ...
    CREATE: typing.ClassVar['StandardOpenOption'] = ...
    CREATE_NEW: typing.ClassVar['StandardOpenOption'] = ...
    DELETE_ON_CLOSE: typing.ClassVar['StandardOpenOption'] = ...
    SPARSE: typing.ClassVar['StandardOpenOption'] = ...
    SYNC: typing.ClassVar['StandardOpenOption'] = ...
    DSYNC: typing.ClassVar['StandardOpenOption'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'StandardOpenOption': ...
    @staticmethod
    def values() -> typing.List['StandardOpenOption']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.nio.file")``.

    AccessDeniedException: typing.Type[AccessDeniedException]
    AccessMode: typing.Type[AccessMode]
    AtomicMoveNotSupportedException: typing.Type[AtomicMoveNotSupportedException]
    ClosedDirectoryStreamException: typing.Type[ClosedDirectoryStreamException]
    ClosedFileSystemException: typing.Type[ClosedFileSystemException]
    ClosedWatchServiceException: typing.Type[ClosedWatchServiceException]
    CopyOption: typing.Type[CopyOption]
    DirectoryIteratorException: typing.Type[DirectoryIteratorException]
    DirectoryNotEmptyException: typing.Type[DirectoryNotEmptyException]
    DirectoryStream: typing.Type[DirectoryStream]
    FileAlreadyExistsException: typing.Type[FileAlreadyExistsException]
    FileStore: typing.Type[FileStore]
    FileSystem: typing.Type[FileSystem]
    FileSystemAlreadyExistsException: typing.Type[FileSystemAlreadyExistsException]
    FileSystemException: typing.Type[FileSystemException]
    FileSystemLoopException: typing.Type[FileSystemLoopException]
    FileSystemNotFoundException: typing.Type[FileSystemNotFoundException]
    FileSystems: typing.Type[FileSystems]
    FileVisitOption: typing.Type[FileVisitOption]
    FileVisitResult: typing.Type[FileVisitResult]
    FileVisitor: typing.Type[FileVisitor]
    Files: typing.Type[Files]
    InvalidPathException: typing.Type[InvalidPathException]
    LinkOption: typing.Type[LinkOption]
    LinkPermission: typing.Type[LinkPermission]
    NoSuchFileException: typing.Type[NoSuchFileException]
    NotDirectoryException: typing.Type[NotDirectoryException]
    NotLinkException: typing.Type[NotLinkException]
    OpenOption: typing.Type[OpenOption]
    Path: typing.Type[Path]
    PathMatcher: typing.Type[PathMatcher]
    Paths: typing.Type[Paths]
    ProviderMismatchException: typing.Type[ProviderMismatchException]
    ProviderNotFoundException: typing.Type[ProviderNotFoundException]
    ReadOnlyFileSystemException: typing.Type[ReadOnlyFileSystemException]
    SecureDirectoryStream: typing.Type[SecureDirectoryStream]
    SimpleFileVisitor: typing.Type[SimpleFileVisitor]
    StandardCopyOption: typing.Type[StandardCopyOption]
    StandardOpenOption: typing.Type[StandardOpenOption]
    StandardWatchEventKinds: typing.Type[StandardWatchEventKinds]
    WatchEvent: typing.Type[WatchEvent]
    WatchKey: typing.Type[WatchKey]
    WatchService: typing.Type[WatchService]
    Watchable: typing.Type[Watchable]
    attribute: java.nio.file.attribute.__module_protocol__
    spi: java.nio.file.spi.__module_protocol__
