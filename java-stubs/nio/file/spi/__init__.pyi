from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import overload
import java.io
import java.net
import java.nio.channels
import java.nio.file
import java.nio.file.attribute
import java.util
import java.util.concurrent


class FileSystemProvider:
    def checkAccess(self, path: java.nio.file.Path, accessModeArray: _py_List[java.nio.file.AccessMode]) -> None: ...
    def copy(self, path: java.nio.file.Path, path2: java.nio.file.Path, copyOptionArray: _py_List[java.nio.file.CopyOption]) -> None: ...
    def createDirectory(self, path: java.nio.file.Path, fileAttributeArray: _py_List[java.nio.file.attribute.FileAttribute[_py_Any]]) -> None: ...
    def createLink(self, path: java.nio.file.Path, path2: java.nio.file.Path) -> None: ...
    def createSymbolicLink(self, path: java.nio.file.Path, path2: java.nio.file.Path, fileAttributeArray: _py_List[java.nio.file.attribute.FileAttribute[_py_Any]]) -> None: ...
    def delete(self, path: java.nio.file.Path) -> None: ...
    def deleteIfExists(self, path: java.nio.file.Path) -> bool: ...
    _getFileAttributeView__V = _py_TypeVar('_getFileAttributeView__V', bound=java.nio.file.attribute.FileAttributeView)  # <V>
    def getFileAttributeView(self, path: java.nio.file.Path, class_: _py_Type[_getFileAttributeView__V], linkOptionArray: _py_List[java.nio.file.LinkOption]) -> _getFileAttributeView__V: ...
    def getFileStore(self, path: java.nio.file.Path) -> java.nio.file.FileStore: ...
    def getFileSystem(self, uRI: java.net.URI) -> java.nio.file.FileSystem: ...
    def getPath(self, uRI: java.net.URI) -> java.nio.file.Path: ...
    def getScheme(self) -> str: ...
    @classmethod
    def installedProviders(cls) -> java.util.List['FileSystemProvider']: ...
    def isHidden(self, path: java.nio.file.Path) -> bool: ...
    def isSameFile(self, path: java.nio.file.Path, path2: java.nio.file.Path) -> bool: ...
    def move(self, path: java.nio.file.Path, path2: java.nio.file.Path, copyOptionArray: _py_List[java.nio.file.CopyOption]) -> None: ...
    def newAsynchronousFileChannel(self, path: java.nio.file.Path, set: java.util.Set[java.nio.file.OpenOption], executorService: java.util.concurrent.ExecutorService, fileAttributeArray: _py_List[java.nio.file.attribute.FileAttribute[_py_Any]]) -> java.nio.channels.AsynchronousFileChannel: ...
    def newByteChannel(self, path: java.nio.file.Path, set: java.util.Set[java.nio.file.OpenOption], fileAttributeArray: _py_List[java.nio.file.attribute.FileAttribute[_py_Any]]) -> java.nio.channels.SeekableByteChannel: ...
    def newDirectoryStream(self, path: java.nio.file.Path, filter: java.nio.file.DirectoryStream.Filter[java.nio.file.Path]) -> java.nio.file.DirectoryStream[java.nio.file.Path]: ...
    def newFileChannel(self, path: java.nio.file.Path, set: java.util.Set[java.nio.file.OpenOption], fileAttributeArray: _py_List[java.nio.file.attribute.FileAttribute[_py_Any]]) -> java.nio.channels.FileChannel: ...
    @overload
    def newFileSystem(self, uRI: java.net.URI, map: java.util.Map[str, _py_Any]) -> java.nio.file.FileSystem: ...
    @overload
    def newFileSystem(self, path: java.nio.file.Path, map: java.util.Map[str, _py_Any]) -> java.nio.file.FileSystem: ...
    def newInputStream(self, path: java.nio.file.Path, openOptionArray: _py_List[java.nio.file.OpenOption]) -> java.io.InputStream: ...
    def newOutputStream(self, path: java.nio.file.Path, openOptionArray: _py_List[java.nio.file.OpenOption]) -> java.io.OutputStream: ...
    _readAttributes_0__A = _py_TypeVar('_readAttributes_0__A', bound=java.nio.file.attribute.BasicFileAttributes)  # <A>
    @overload
    def readAttributes(self, path: java.nio.file.Path, class_: _py_Type[_readAttributes_0__A], linkOptionArray: _py_List[java.nio.file.LinkOption]) -> _readAttributes_0__A: ...
    @overload
    def readAttributes(self, path: java.nio.file.Path, string: str, linkOptionArray: _py_List[java.nio.file.LinkOption]) -> java.util.Map[str, _py_Any]: ...
    def readSymbolicLink(self, path: java.nio.file.Path) -> java.nio.file.Path: ...
    def setAttribute(self, path: java.nio.file.Path, string: str, object: _py_Any, linkOptionArray: _py_List[java.nio.file.LinkOption]) -> None: ...

class FileTypeDetector:
    def probeContentType(self, path: java.nio.file.Path) -> str: ...
