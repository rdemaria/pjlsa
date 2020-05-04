from typing import Any as _py_Any
from typing import List as _py_List
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.io
import java.lang
import java.nio
import java.nio.charset
import java.nio.file.attribute
import java.util
import java.util.stream


class CheckedInputStream(java.io.FilterInputStream):
    def __init__(self, inputStream: java.io.InputStream, checksum: 'Checksum'): ...
    def getChecksum(self) -> 'Checksum': ...
    @overload
    def read(self) -> int: ...
    @overload
    def read(self, byteArray: _py_List[int], int: int, int2: int) -> int: ...
    @overload
    def read(self, byteArray: _py_List[int]) -> int: ...
    def skip(self, long: int) -> int: ...

class CheckedOutputStream(java.io.FilterOutputStream):
    def __init__(self, outputStream: java.io.OutputStream, checksum: 'Checksum'): ...
    def getChecksum(self) -> 'Checksum': ...
    @overload
    def write(self, int: int) -> None: ...
    @overload
    def write(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...
    @overload
    def write(self, byteArray: _py_List[int]) -> None: ...

class Checksum:
    def getValue(self) -> int: ...
    def reset(self) -> None: ...
    @overload
    def update(self, int: int) -> None: ...
    @overload
    def update(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...

class DataFormatException(java.lang.Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, string: str): ...

class Deflater:
    DEFLATED: _py_ClassVar[int] = ...
    NO_COMPRESSION: _py_ClassVar[int] = ...
    BEST_SPEED: _py_ClassVar[int] = ...
    BEST_COMPRESSION: _py_ClassVar[int] = ...
    DEFAULT_COMPRESSION: _py_ClassVar[int] = ...
    FILTERED: _py_ClassVar[int] = ...
    HUFFMAN_ONLY: _py_ClassVar[int] = ...
    DEFAULT_STRATEGY: _py_ClassVar[int] = ...
    NO_FLUSH: _py_ClassVar[int] = ...
    SYNC_FLUSH: _py_ClassVar[int] = ...
    FULL_FLUSH: _py_ClassVar[int] = ...
    @overload
    def __init__(self, int: int): ...
    @overload
    def __init__(self, int: int, boolean: bool): ...
    @overload
    def __init__(self): ...
    @overload
    def deflate(self, byteArray: _py_List[int], int: int, int2: int, int3: int) -> int: ...
    @overload
    def deflate(self, byteArray: _py_List[int]) -> int: ...
    @overload
    def deflate(self, byteArray: _py_List[int], int: int, int2: int) -> int: ...
    def end(self) -> None: ...
    def finish(self) -> None: ...
    def finished(self) -> bool: ...
    def getAdler(self) -> int: ...
    def getBytesRead(self) -> int: ...
    def getBytesWritten(self) -> int: ...
    def getTotalIn(self) -> int: ...
    def getTotalOut(self) -> int: ...
    def needsInput(self) -> bool: ...
    def reset(self) -> None: ...
    @overload
    def setDictionary(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...
    @overload
    def setDictionary(self, byteArray: _py_List[int]) -> None: ...
    @overload
    def setInput(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...
    @overload
    def setInput(self, byteArray: _py_List[int]) -> None: ...
    def setLevel(self, int: int) -> None: ...
    def setStrategy(self, int: int) -> None: ...

class DeflaterInputStream(java.io.FilterInputStream):
    @overload
    def __init__(self, inputStream: java.io.InputStream, deflater: Deflater, int: int): ...
    @overload
    def __init__(self, inputStream: java.io.InputStream): ...
    @overload
    def __init__(self, inputStream: java.io.InputStream, deflater: Deflater): ...
    def available(self) -> int: ...
    def close(self) -> None: ...
    def mark(self, int: int) -> None: ...
    def markSupported(self) -> bool: ...
    @overload
    def read(self) -> int: ...
    @overload
    def read(self, byteArray: _py_List[int], int: int, int2: int) -> int: ...
    @overload
    def read(self, byteArray: _py_List[int]) -> int: ...
    def reset(self) -> None: ...
    def skip(self, long: int) -> int: ...

class DeflaterOutputStream(java.io.FilterOutputStream):
    @overload
    def __init__(self, outputStream: java.io.OutputStream, deflater: Deflater, int: int, boolean: bool): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream, boolean: bool): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream, deflater: Deflater): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream, deflater: Deflater, boolean: bool): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream, deflater: Deflater, int: int): ...
    def close(self) -> None: ...
    def finish(self) -> None: ...
    def flush(self) -> None: ...
    @overload
    def write(self, int: int) -> None: ...
    @overload
    def write(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...
    @overload
    def write(self, byteArray: _py_List[int]) -> None: ...

class Inflater:
    @overload
    def __init__(self, boolean: bool): ...
    @overload
    def __init__(self): ...
    def end(self) -> None: ...
    def finished(self) -> bool: ...
    def getAdler(self) -> int: ...
    def getBytesRead(self) -> int: ...
    def getBytesWritten(self) -> int: ...
    def getRemaining(self) -> int: ...
    def getTotalIn(self) -> int: ...
    def getTotalOut(self) -> int: ...
    @overload
    def inflate(self, byteArray: _py_List[int]) -> int: ...
    @overload
    def inflate(self, byteArray: _py_List[int], int: int, int2: int) -> int: ...
    def needsDictionary(self) -> bool: ...
    def needsInput(self) -> bool: ...
    def reset(self) -> None: ...
    @overload
    def setDictionary(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...
    @overload
    def setDictionary(self, byteArray: _py_List[int]) -> None: ...
    @overload
    def setInput(self, byteArray: _py_List[int]) -> None: ...
    @overload
    def setInput(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...

class InflaterInputStream(java.io.FilterInputStream):
    @overload
    def __init__(self, inputStream: java.io.InputStream, inflater: Inflater): ...
    @overload
    def __init__(self, inputStream: java.io.InputStream, inflater: Inflater, int: int): ...
    @overload
    def __init__(self, inputStream: java.io.InputStream): ...
    def available(self) -> int: ...
    def close(self) -> None: ...
    def mark(self, int: int) -> None: ...
    def markSupported(self) -> bool: ...
    @overload
    def read(self) -> int: ...
    @overload
    def read(self, byteArray: _py_List[int], int: int, int2: int) -> int: ...
    @overload
    def read(self, byteArray: _py_List[int]) -> int: ...
    def reset(self) -> None: ...
    def skip(self, long: int) -> int: ...

class InflaterOutputStream(java.io.FilterOutputStream):
    @overload
    def __init__(self, outputStream: java.io.OutputStream, inflater: Inflater, int: int): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream, inflater: Inflater): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream): ...
    def close(self) -> None: ...
    def finish(self) -> None: ...
    def flush(self) -> None: ...
    @overload
    def write(self, int: int) -> None: ...
    @overload
    def write(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...
    @overload
    def write(self, byteArray: _py_List[int]) -> None: ...

class ZStreamRef: ...

class ZipCoder: ...

class ZipConstants:
    LOCSIG: _py_ClassVar[int] = ...
    EXTSIG: _py_ClassVar[int] = ...
    CENSIG: _py_ClassVar[int] = ...
    ENDSIG: _py_ClassVar[int] = ...
    LOCHDR: _py_ClassVar[int] = ...
    EXTHDR: _py_ClassVar[int] = ...
    CENHDR: _py_ClassVar[int] = ...
    ENDHDR: _py_ClassVar[int] = ...
    LOCVER: _py_ClassVar[int] = ...
    LOCFLG: _py_ClassVar[int] = ...
    LOCHOW: _py_ClassVar[int] = ...
    LOCTIM: _py_ClassVar[int] = ...
    LOCCRC: _py_ClassVar[int] = ...
    LOCSIZ: _py_ClassVar[int] = ...
    LOCLEN: _py_ClassVar[int] = ...
    LOCNAM: _py_ClassVar[int] = ...
    LOCEXT: _py_ClassVar[int] = ...
    EXTCRC: _py_ClassVar[int] = ...
    EXTSIZ: _py_ClassVar[int] = ...
    EXTLEN: _py_ClassVar[int] = ...
    CENVEM: _py_ClassVar[int] = ...
    CENVER: _py_ClassVar[int] = ...
    CENFLG: _py_ClassVar[int] = ...
    CENHOW: _py_ClassVar[int] = ...
    CENTIM: _py_ClassVar[int] = ...
    CENCRC: _py_ClassVar[int] = ...
    CENSIZ: _py_ClassVar[int] = ...
    CENLEN: _py_ClassVar[int] = ...
    CENNAM: _py_ClassVar[int] = ...
    CENEXT: _py_ClassVar[int] = ...
    CENCOM: _py_ClassVar[int] = ...
    CENDSK: _py_ClassVar[int] = ...
    CENATT: _py_ClassVar[int] = ...
    CENATX: _py_ClassVar[int] = ...
    CENOFF: _py_ClassVar[int] = ...
    ENDSUB: _py_ClassVar[int] = ...
    ENDTOT: _py_ClassVar[int] = ...
    ENDSIZ: _py_ClassVar[int] = ...
    ENDOFF: _py_ClassVar[int] = ...
    ENDCOM: _py_ClassVar[int] = ...

class ZipConstants64: ...

class ZipError(java.lang.InternalError):
    def __init__(self, string: str): ...

class ZipException(java.io.IOException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, string: str): ...

class ZipUtils:
    @classmethod
    def extendedDosToJavaTime(cls, long: int) -> int: ...
    @classmethod
    def fileTimeToUnixTime(cls, fileTime: java.nio.file.attribute.FileTime) -> int: ...
    @classmethod
    def fileTimeToWinTime(cls, fileTime: java.nio.file.attribute.FileTime) -> int: ...
    @classmethod
    def get16(cls, byteArray: _py_List[int], int: int) -> int: ...
    @classmethod
    def get32(cls, byteArray: _py_List[int], int: int) -> int: ...
    @classmethod
    def get64(cls, byteArray: _py_List[int], int: int) -> int: ...
    @classmethod
    def javaToExtendedDosTime(cls, long: int) -> int: ...
    @classmethod
    def unixTimeToFileTime(cls, long: int) -> java.nio.file.attribute.FileTime: ...
    @classmethod
    def winTimeToFileTime(cls, long: int) -> java.nio.file.attribute.FileTime: ...

class Adler32(Checksum):
    def __init__(self): ...
    def getValue(self) -> int: ...
    def reset(self) -> None: ...
    @overload
    def update(self, int: int) -> None: ...
    @overload
    def update(self, byteBuffer: java.nio.ByteBuffer) -> None: ...
    @overload
    def update(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...
    @overload
    def update(self, byteArray: _py_List[int]) -> None: ...

class CRC32(Checksum):
    def __init__(self): ...
    def getValue(self) -> int: ...
    def reset(self) -> None: ...
    @overload
    def update(self, int: int) -> None: ...
    @overload
    def update(self, byteBuffer: java.nio.ByteBuffer) -> None: ...
    @overload
    def update(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...
    @overload
    def update(self, byteArray: _py_List[int]) -> None: ...

class GZIPInputStream(InflaterInputStream):
    GZIP_MAGIC: _py_ClassVar[int] = ...
    @overload
    def __init__(self, inputStream: java.io.InputStream): ...
    @overload
    def __init__(self, inputStream: java.io.InputStream, int: int): ...
    def close(self) -> None: ...
    @overload
    def read(self, byteArray: _py_List[int], int: int, int2: int) -> int: ...
    @overload
    def read(self) -> int: ...
    @overload
    def read(self, byteArray: _py_List[int]) -> int: ...

class GZIPOutputStream(DeflaterOutputStream):
    @overload
    def __init__(self, outputStream: java.io.OutputStream, int: int): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream, boolean: bool): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream, int: int, boolean: bool): ...
    def finish(self) -> None: ...
    @overload
    def write(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...
    @overload
    def write(self, int: int) -> None: ...
    @overload
    def write(self, byteArray: _py_List[int]) -> None: ...

class ZipEntry(ZipConstants, java.lang.Cloneable):
    STORED: _py_ClassVar[int] = ...
    DEFLATED: _py_ClassVar[int] = ...
    @overload
    def __init__(self, zipEntry: 'ZipEntry'): ...
    @overload
    def __init__(self, string: str): ...
    def clone(self) -> _py_Any: ...
    def getComment(self) -> str: ...
    def getCompressedSize(self) -> int: ...
    def getCrc(self) -> int: ...
    def getCreationTime(self) -> java.nio.file.attribute.FileTime: ...
    def getExtra(self) -> _py_List[int]: ...
    def getLastAccessTime(self) -> java.nio.file.attribute.FileTime: ...
    def getLastModifiedTime(self) -> java.nio.file.attribute.FileTime: ...
    def getMethod(self) -> int: ...
    def getName(self) -> str: ...
    def getSize(self) -> int: ...
    def getTime(self) -> int: ...
    def hashCode(self) -> int: ...
    def isDirectory(self) -> bool: ...
    def setComment(self, string: str) -> None: ...
    def setCompressedSize(self, long: int) -> None: ...
    def setCrc(self, long: int) -> None: ...
    def setCreationTime(self, fileTime: java.nio.file.attribute.FileTime) -> 'ZipEntry': ...
    def setExtra(self, byteArray: _py_List[int]) -> None: ...
    def setLastAccessTime(self, fileTime: java.nio.file.attribute.FileTime) -> 'ZipEntry': ...
    def setLastModifiedTime(self, fileTime: java.nio.file.attribute.FileTime) -> 'ZipEntry': ...
    def setMethod(self, int: int) -> None: ...
    def setSize(self, long: int) -> None: ...
    def setTime(self, long: int) -> None: ...
    def toString(self) -> str: ...

class ZipFile(ZipConstants, java.io.Closeable):
    OPEN_READ: _py_ClassVar[int] = ...
    OPEN_DELETE: _py_ClassVar[int] = ...
    @overload
    def __init__(self, string: str, charset: java.nio.charset.Charset): ...
    @overload
    def __init__(self, file: java.io.File, int: int, charset: java.nio.charset.Charset): ...
    @overload
    def __init__(self, file: java.io.File): ...
    @overload
    def __init__(self, file: java.io.File, charset: java.nio.charset.Charset): ...
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, file: java.io.File, int: int): ...
    def close(self) -> None: ...
    def entries(self) -> java.util.Enumeration[ZipEntry]: ...
    def getComment(self) -> str: ...
    def getEntry(self, string: str) -> ZipEntry: ...
    def getInputStream(self, zipEntry: ZipEntry) -> java.io.InputStream: ...
    def getName(self) -> str: ...
    def size(self) -> int: ...
    def stream(self) -> java.util.stream.Stream[ZipEntry]: ...

class ZipInputStream(InflaterInputStream, ZipConstants):
    @overload
    def __init__(self, inputStream: java.io.InputStream, charset: java.nio.charset.Charset): ...
    @overload
    def __init__(self, inputStream: java.io.InputStream): ...
    def available(self) -> int: ...
    def close(self) -> None: ...
    def closeEntry(self) -> None: ...
    def getNextEntry(self) -> ZipEntry: ...
    @overload
    def read(self, byteArray: _py_List[int], int: int, int2: int) -> int: ...
    @overload
    def read(self) -> int: ...
    @overload
    def read(self, byteArray: _py_List[int]) -> int: ...
    def skip(self, long: int) -> int: ...

class ZipOutputStream(DeflaterOutputStream, ZipConstants):
    STORED: _py_ClassVar[int] = ...
    DEFLATED: _py_ClassVar[int] = ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream): ...
    @overload
    def __init__(self, outputStream: java.io.OutputStream, charset: java.nio.charset.Charset): ...
    def close(self) -> None: ...
    def closeEntry(self) -> None: ...
    def finish(self) -> None: ...
    def putNextEntry(self, zipEntry: ZipEntry) -> None: ...
    def setComment(self, string: str) -> None: ...
    def setLevel(self, int: int) -> None: ...
    def setMethod(self, int: int) -> None: ...
    @overload
    def write(self, byteArray: _py_List[int], int: int, int2: int) -> None: ...
    @overload
    def write(self, int: int) -> None: ...
    @overload
    def write(self, byteArray: _py_List[int]) -> None: ...
