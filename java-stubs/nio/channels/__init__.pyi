import java.io
import java.lang
import java.net
import java.nio
import java.nio.channels.spi
import java.nio.charset
import java.nio.file
import java.nio.file.attribute
import java.util
import java.util.concurrent
import java.util.function
import jpype.protocol
import typing



class AcceptPendingException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.AcceptPendingException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * AcceptPendingException()
    
    """
    def __init__(self): ...

class AlreadyBoundException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.AlreadyBoundException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * AlreadyBoundException()
    
    """
    def __init__(self): ...

class AlreadyConnectedException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.AlreadyConnectedException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * AlreadyConnectedException()
    
    """
    def __init__(self): ...

class AsynchronousChannelGroup:
    """
    Java class 'java.nio.channels.AsynchronousChannelGroup'
    
        Extends:
            java.lang.Object
    
    """
    def awaitTermination(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> bool: ...
    def isShutdown(self) -> bool: ...
    def isTerminated(self) -> bool: ...
    def provider(self) -> java.nio.channels.spi.AsynchronousChannelProvider: ...
    def shutdown(self) -> None: ...
    def shutdownNow(self) -> None: ...
    @staticmethod
    def withCachedThreadPool(executorService: java.util.concurrent.ExecutorService, int: int) -> 'AsynchronousChannelGroup': ...
    @staticmethod
    def withFixedThreadPool(int: int, threadFactory: java.util.concurrent.ThreadFactory) -> 'AsynchronousChannelGroup': ...
    @staticmethod
    def withThreadPool(executorService: java.util.concurrent.ExecutorService) -> 'AsynchronousChannelGroup': ...

class CancelledKeyException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.CancelledKeyException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * CancelledKeyException()
    
    """
    def __init__(self): ...

class Channel(java.io.Closeable):
    """
    Java class 'java.nio.channels.Channel'
    
        Interfaces:
            java.io.Closeable
    
    """
    def close(self) -> None: ...
    def isOpen(self) -> bool: ...

class Channels:
    """
    Java class 'java.nio.channels.Channels'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    @staticmethod
    def newChannel(inputStream: java.io.InputStream) -> 'ReadableByteChannel': ...
    @typing.overload
    @staticmethod
    def newChannel(outputStream: java.io.OutputStream) -> 'WritableByteChannel': ...
    @typing.overload
    @staticmethod
    def newInputStream(asynchronousByteChannel: 'AsynchronousByteChannel') -> java.io.InputStream: ...
    @typing.overload
    @staticmethod
    def newInputStream(readableByteChannel: 'ReadableByteChannel') -> java.io.InputStream: ...
    @typing.overload
    @staticmethod
    def newOutputStream(asynchronousByteChannel: 'AsynchronousByteChannel') -> java.io.OutputStream: ...
    @typing.overload
    @staticmethod
    def newOutputStream(writableByteChannel: 'WritableByteChannel') -> java.io.OutputStream: ...
    @typing.overload
    @staticmethod
    def newReader(readableByteChannel: 'ReadableByteChannel', string: str) -> java.io.Reader: ...
    @typing.overload
    @staticmethod
    def newReader(readableByteChannel: 'ReadableByteChannel', charset: java.nio.charset.Charset) -> java.io.Reader: ...
    @typing.overload
    @staticmethod
    def newReader(readableByteChannel: 'ReadableByteChannel', charsetDecoder: java.nio.charset.CharsetDecoder, int: int) -> java.io.Reader: ...
    @typing.overload
    @staticmethod
    def newWriter(writableByteChannel: 'WritableByteChannel', string: str) -> java.io.Writer: ...
    @typing.overload
    @staticmethod
    def newWriter(writableByteChannel: 'WritableByteChannel', charset: java.nio.charset.Charset) -> java.io.Writer: ...
    @typing.overload
    @staticmethod
    def newWriter(writableByteChannel: 'WritableByteChannel', charsetEncoder: java.nio.charset.CharsetEncoder, int: int) -> java.io.Writer: ...

class ClosedChannelException(java.io.IOException):
    """
    Java class 'java.nio.channels.ClosedChannelException'
    
        Extends:
            java.io.IOException
    
      Constructors:
        * ClosedChannelException()
    
    """
    def __init__(self): ...

class ClosedSelectorException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.ClosedSelectorException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * ClosedSelectorException()
    
    """
    def __init__(self): ...

_CompletionHandler__V = typing.TypeVar('_CompletionHandler__V')  # <V>
_CompletionHandler__A = typing.TypeVar('_CompletionHandler__A')  # <A>
class CompletionHandler(typing.Generic[_CompletionHandler__V, _CompletionHandler__A]):
    """
    Java class 'java.nio.channels.CompletionHandler'
    
    """
    def completed(self, v: _CompletionHandler__V, a: _CompletionHandler__A) -> None: ...
    def failed(self, throwable: java.lang.Throwable, a: _CompletionHandler__A) -> None: ...

class ConnectionPendingException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.ConnectionPendingException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * ConnectionPendingException()
    
    """
    def __init__(self): ...

class FileLock(java.lang.AutoCloseable):
    """
    Java class 'java.nio.channels.FileLock'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.lang.AutoCloseable
    
    """
    def acquiredBy(self) -> Channel: ...
    def channel(self) -> 'FileChannel': ...
    def close(self) -> None: ...
    def isShared(self) -> bool: ...
    def isValid(self) -> bool: ...
    def overlaps(self, long: int, long2: int) -> bool: ...
    def position(self) -> int: ...
    def release(self) -> None: ...
    def size(self) -> int: ...
    def toString(self) -> str: ...

class FileLockInterruptionException(java.io.IOException):
    """
    Java class 'java.nio.channels.FileLockInterruptionException'
    
        Extends:
            java.io.IOException
    
      Constructors:
        * FileLockInterruptionException()
    
    """
    def __init__(self): ...

class IllegalBlockingModeException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.IllegalBlockingModeException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * IllegalBlockingModeException()
    
    """
    def __init__(self): ...

class IllegalChannelGroupException(java.lang.IllegalArgumentException):
    """
    Java class 'java.nio.channels.IllegalChannelGroupException'
    
        Extends:
            java.lang.IllegalArgumentException
    
      Constructors:
        * IllegalChannelGroupException()
    
    """
    def __init__(self): ...

class IllegalSelectorException(java.lang.IllegalArgumentException):
    """
    Java class 'java.nio.channels.IllegalSelectorException'
    
        Extends:
            java.lang.IllegalArgumentException
    
      Constructors:
        * IllegalSelectorException()
    
    """
    def __init__(self): ...

class InterruptedByTimeoutException(java.io.IOException):
    """
    Java class 'java.nio.channels.InterruptedByTimeoutException'
    
        Extends:
            java.io.IOException
    
      Constructors:
        * InterruptedByTimeoutException()
    
    """
    def __init__(self): ...

class MembershipKey:
    """
    Java class 'java.nio.channels.MembershipKey'
    
        Extends:
            java.lang.Object
    
    """
    def block(self, inetAddress: java.net.InetAddress) -> 'MembershipKey': ...
    def channel(self) -> 'MulticastChannel': ...
    def drop(self) -> None: ...
    def group(self) -> java.net.InetAddress: ...
    def isValid(self) -> bool: ...
    def networkInterface(self) -> java.net.NetworkInterface: ...
    def sourceAddress(self) -> java.net.InetAddress: ...
    def unblock(self, inetAddress: java.net.InetAddress) -> 'MembershipKey': ...

class NoConnectionPendingException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.NoConnectionPendingException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * NoConnectionPendingException()
    
    """
    def __init__(self): ...

class NonReadableChannelException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.NonReadableChannelException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * NonReadableChannelException()
    
    """
    def __init__(self): ...

class NonWritableChannelException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.NonWritableChannelException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * NonWritableChannelException()
    
    """
    def __init__(self): ...

class NotYetBoundException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.NotYetBoundException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * NotYetBoundException()
    
    """
    def __init__(self): ...

class NotYetConnectedException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.NotYetConnectedException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * NotYetConnectedException()
    
    """
    def __init__(self): ...

class OverlappingFileLockException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.OverlappingFileLockException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * OverlappingFileLockException()
    
    """
    def __init__(self): ...

class ReadPendingException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.ReadPendingException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * ReadPendingException()
    
    """
    def __init__(self): ...

class SelectionKey:
    """
    Java class 'java.nio.channels.SelectionKey'
    
        Extends:
            java.lang.Object
    
      Attributes:
        OP_READ (int): final static field
        OP_WRITE (int): final static field
        OP_CONNECT (int): final static field
        OP_ACCEPT (int): final static field
    
    """
    OP_READ: typing.ClassVar[int] = ...
    OP_WRITE: typing.ClassVar[int] = ...
    OP_CONNECT: typing.ClassVar[int] = ...
    OP_ACCEPT: typing.ClassVar[int] = ...
    def attach(self, object: typing.Any) -> typing.Any: ...
    def attachment(self) -> typing.Any: ...
    def cancel(self) -> None: ...
    def channel(self) -> 'SelectableChannel': ...
    @typing.overload
    def interestOps(self) -> int: ...
    @typing.overload
    def interestOps(self, int: int) -> 'SelectionKey': ...
    def interestOpsAnd(self, int: int) -> int: ...
    def interestOpsOr(self, int: int) -> int: ...
    def isAcceptable(self) -> bool: ...
    def isConnectable(self) -> bool: ...
    def isReadable(self) -> bool: ...
    def isValid(self) -> bool: ...
    def isWritable(self) -> bool: ...
    def readyOps(self) -> int: ...
    def selector(self) -> 'Selector': ...

class Selector(java.io.Closeable):
    """
    Java class 'java.nio.channels.Selector'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Closeable
    
    """
    def close(self) -> None: ...
    def isOpen(self) -> bool: ...
    def keys(self) -> java.util.Set[SelectionKey]: ...
    @staticmethod
    def open() -> 'Selector': ...
    def provider(self) -> java.nio.channels.spi.SelectorProvider: ...
    @typing.overload
    def select(self) -> int: ...
    @typing.overload
    def select(self, long: int) -> int: ...
    @typing.overload
    def select(self, consumer: typing.Union[java.util.function.Consumer[SelectionKey], typing.Callable[[SelectionKey], None]]) -> int: ...
    @typing.overload
    def select(self, consumer: typing.Union[java.util.function.Consumer[SelectionKey], typing.Callable[[SelectionKey], None]], long: int) -> int: ...
    @typing.overload
    def selectNow(self) -> int: ...
    @typing.overload
    def selectNow(self, consumer: typing.Union[java.util.function.Consumer[SelectionKey], typing.Callable[[SelectionKey], None]]) -> int: ...
    def selectedKeys(self) -> java.util.Set[SelectionKey]: ...
    def wakeup(self) -> 'Selector': ...

class ShutdownChannelGroupException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.ShutdownChannelGroupException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * ShutdownChannelGroupException()
    
    """
    def __init__(self): ...

class UnresolvedAddressException(java.lang.IllegalArgumentException):
    """
    Java class 'java.nio.channels.UnresolvedAddressException'
    
        Extends:
            java.lang.IllegalArgumentException
    
      Constructors:
        * UnresolvedAddressException()
    
    """
    def __init__(self): ...

class UnsupportedAddressTypeException(java.lang.IllegalArgumentException):
    """
    Java class 'java.nio.channels.UnsupportedAddressTypeException'
    
        Extends:
            java.lang.IllegalArgumentException
    
      Constructors:
        * UnsupportedAddressTypeException()
    
    """
    def __init__(self): ...

class WritePendingException(java.lang.IllegalStateException):
    """
    Java class 'java.nio.channels.WritePendingException'
    
        Extends:
            java.lang.IllegalStateException
    
      Constructors:
        * WritePendingException()
    
    """
    def __init__(self): ...

class AsynchronousChannel(Channel):
    """
    Java class 'java.nio.channels.AsynchronousChannel'
    
        Interfaces:
            java.nio.channels.Channel
    
    """
    def close(self) -> None: ...

class AsynchronousCloseException(ClosedChannelException):
    """
    Java class 'java.nio.channels.AsynchronousCloseException'
    
        Extends:
            java.nio.channels.ClosedChannelException
    
      Constructors:
        * AsynchronousCloseException()
    
    """
    def __init__(self): ...

class InterruptibleChannel(Channel):
    """
    Java class 'java.nio.channels.InterruptibleChannel'
    
        Interfaces:
            java.nio.channels.Channel
    
    """
    def close(self) -> None: ...

class NetworkChannel(Channel):
    """
    Java class 'java.nio.channels.NetworkChannel'
    
        Interfaces:
            java.nio.channels.Channel
    
    """
    def bind(self, socketAddress: java.net.SocketAddress) -> 'NetworkChannel': ...
    def getLocalAddress(self) -> java.net.SocketAddress: ...
    _getOption__T = typing.TypeVar('_getOption__T')  # <T>
    def getOption(self, socketOption: java.net.SocketOption[_getOption__T]) -> _getOption__T: ...
    _setOption__T = typing.TypeVar('_setOption__T')  # <T>
    def setOption(self, socketOption: java.net.SocketOption[_setOption__T], t: _setOption__T) -> 'NetworkChannel': ...
    def supportedOptions(self) -> java.util.Set[java.net.SocketOption[typing.Any]]: ...

class ReadableByteChannel(Channel):
    """
    Java class 'java.nio.channels.ReadableByteChannel'
    
        Interfaces:
            java.nio.channels.Channel
    
    """
    def read(self, byteBuffer: java.nio.ByteBuffer) -> int: ...

class SelectableChannel(java.nio.channels.spi.AbstractInterruptibleChannel, Channel):
    """
    Java class 'java.nio.channels.SelectableChannel'
    
        Extends:
            java.nio.channels.spi.AbstractInterruptibleChannel
    
        Interfaces:
            java.nio.channels.Channel
    
    """
    def blockingLock(self) -> typing.Any: ...
    def configureBlocking(self, boolean: bool) -> 'SelectableChannel': ...
    def isBlocking(self) -> bool: ...
    def isRegistered(self) -> bool: ...
    def keyFor(self, selector: Selector) -> SelectionKey: ...
    def provider(self) -> java.nio.channels.spi.SelectorProvider: ...
    @typing.overload
    def register(self, selector: Selector, int: int, object: typing.Any) -> SelectionKey: ...
    @typing.overload
    def register(self, selector: Selector, int: int) -> SelectionKey: ...
    def validOps(self) -> int: ...

class WritableByteChannel(Channel):
    """
    Java class 'java.nio.channels.WritableByteChannel'
    
        Interfaces:
            java.nio.channels.Channel
    
    """
    def write(self, byteBuffer: java.nio.ByteBuffer) -> int: ...

class AsynchronousByteChannel(AsynchronousChannel):
    """
    Java class 'java.nio.channels.AsynchronousByteChannel'
    
        Interfaces:
            java.nio.channels.AsynchronousChannel
    
    """
    _read_1__A = typing.TypeVar('_read_1__A')  # <A>
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer) -> java.util.concurrent.Future[int]: ...
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer, a: _read_1__A, completionHandler: CompletionHandler[int, _read_1__A]) -> None: ...
    _write_1__A = typing.TypeVar('_write_1__A')  # <A>
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer) -> java.util.concurrent.Future[int]: ...
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer, a: _write_1__A, completionHandler: CompletionHandler[int, _write_1__A]) -> None: ...

class AsynchronousFileChannel(AsynchronousChannel):
    """
    Java class 'java.nio.channels.AsynchronousFileChannel'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.nio.channels.AsynchronousChannel
    
    """
    def force(self, boolean: bool) -> None: ...
    _lock_1__A = typing.TypeVar('_lock_1__A')  # <A>
    _lock_3__A = typing.TypeVar('_lock_3__A')  # <A>
    @typing.overload
    def lock(self, long: int, long2: int, boolean: bool) -> java.util.concurrent.Future[FileLock]: ...
    @typing.overload
    def lock(self, long: int, long2: int, boolean: bool, a: _lock_1__A, completionHandler: CompletionHandler[FileLock, _lock_1__A]) -> None: ...
    @typing.overload
    def lock(self) -> java.util.concurrent.Future[FileLock]: ...
    @typing.overload
    def lock(self, a: _lock_3__A, completionHandler: CompletionHandler[FileLock, _lock_3__A]) -> None: ...
    @typing.overload
    @staticmethod
    def open(path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], openOptionArray: typing.List[java.nio.file.OpenOption]) -> 'AsynchronousFileChannel': ...
    @typing.overload
    @staticmethod
    def open(path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], set: java.util.Set[java.nio.file.OpenOption], executorService: java.util.concurrent.ExecutorService, fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'AsynchronousFileChannel': ...
    _read_1__A = typing.TypeVar('_read_1__A')  # <A>
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer, long: int) -> java.util.concurrent.Future[int]: ...
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer, long: int, a: _read_1__A, completionHandler: CompletionHandler[int, _read_1__A]) -> None: ...
    def size(self) -> int: ...
    def truncate(self, long: int) -> 'AsynchronousFileChannel': ...
    @typing.overload
    def tryLock(self, long: int, long2: int, boolean: bool) -> FileLock: ...
    @typing.overload
    def tryLock(self) -> FileLock: ...
    _write_1__A = typing.TypeVar('_write_1__A')  # <A>
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer, long: int) -> java.util.concurrent.Future[int]: ...
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer, long: int, a: _write_1__A, completionHandler: CompletionHandler[int, _write_1__A]) -> None: ...

class AsynchronousServerSocketChannel(AsynchronousChannel, NetworkChannel):
    """
    Java class 'java.nio.channels.AsynchronousServerSocketChannel'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.nio.channels.AsynchronousChannel,
            java.nio.channels.NetworkChannel
    
    """
    _accept_1__A = typing.TypeVar('_accept_1__A')  # <A>
    @typing.overload
    def accept(self) -> java.util.concurrent.Future['AsynchronousSocketChannel']: ...
    @typing.overload
    def accept(self, a: _accept_1__A, completionHandler: CompletionHandler['AsynchronousSocketChannel', _accept_1__A]) -> None: ...
    @typing.overload
    def bind(self, socketAddress: java.net.SocketAddress, int: int) -> 'AsynchronousServerSocketChannel': ...
    @typing.overload
    def bind(self, socketAddress: java.net.SocketAddress) -> 'AsynchronousServerSocketChannel': ...
    def getLocalAddress(self) -> java.net.SocketAddress: ...
    @typing.overload
    @staticmethod
    def open() -> 'AsynchronousServerSocketChannel': ...
    @typing.overload
    @staticmethod
    def open(asynchronousChannelGroup: AsynchronousChannelGroup) -> 'AsynchronousServerSocketChannel': ...
    def provider(self) -> java.nio.channels.spi.AsynchronousChannelProvider: ...
    _setOption__T = typing.TypeVar('_setOption__T')  # <T>
    def setOption(self, socketOption: java.net.SocketOption[_setOption__T], t: _setOption__T) -> 'AsynchronousServerSocketChannel': ...

class ByteChannel(ReadableByteChannel, WritableByteChannel): ...

class ClosedByInterruptException(AsynchronousCloseException):
    """
    Java class 'java.nio.channels.ClosedByInterruptException'
    
        Extends:
            java.nio.channels.AsynchronousCloseException
    
      Constructors:
        * ClosedByInterruptException()
    
    """
    def __init__(self): ...

class GatheringByteChannel(WritableByteChannel):
    """
    Java class 'java.nio.channels.GatheringByteChannel'
    
        Interfaces:
            java.nio.channels.WritableByteChannel
    
    """
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer) -> int: ...
    @typing.overload
    def write(self, byteBufferArray: typing.List[java.nio.ByteBuffer]) -> int: ...
    @typing.overload
    def write(self, byteBufferArray: typing.List[java.nio.ByteBuffer], int: int, int2: int) -> int: ...

class MulticastChannel(NetworkChannel):
    """
    Java class 'java.nio.channels.MulticastChannel'
    
        Interfaces:
            java.nio.channels.NetworkChannel
    
    """
    def close(self) -> None: ...
    @typing.overload
    def join(self, inetAddress: java.net.InetAddress, networkInterface: java.net.NetworkInterface) -> MembershipKey: ...
    @typing.overload
    def join(self, inetAddress: java.net.InetAddress, networkInterface: java.net.NetworkInterface, inetAddress2: java.net.InetAddress) -> MembershipKey: ...

class ScatteringByteChannel(ReadableByteChannel):
    """
    Java class 'java.nio.channels.ScatteringByteChannel'
    
        Interfaces:
            java.nio.channels.ReadableByteChannel
    
    """
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer) -> int: ...
    @typing.overload
    def read(self, byteBufferArray: typing.List[java.nio.ByteBuffer]) -> int: ...
    @typing.overload
    def read(self, byteBufferArray: typing.List[java.nio.ByteBuffer], int: int, int2: int) -> int: ...

class ServerSocketChannel(java.nio.channels.spi.AbstractSelectableChannel, NetworkChannel):
    """
    Java class 'java.nio.channels.ServerSocketChannel'
    
        Extends:
            java.nio.channels.spi.AbstractSelectableChannel
    
        Interfaces:
            java.nio.channels.NetworkChannel
    
    """
    def accept(self) -> 'SocketChannel': ...
    @typing.overload
    def bind(self, socketAddress: java.net.SocketAddress, int: int) -> 'ServerSocketChannel': ...
    @typing.overload
    def bind(self, socketAddress: java.net.SocketAddress) -> 'ServerSocketChannel': ...
    def getLocalAddress(self) -> java.net.SocketAddress: ...
    @staticmethod
    def open() -> 'ServerSocketChannel': ...
    _setOption__T = typing.TypeVar('_setOption__T')  # <T>
    def setOption(self, socketOption: java.net.SocketOption[_setOption__T], t: _setOption__T) -> 'ServerSocketChannel': ...
    def socket(self) -> java.net.ServerSocket: ...
    def validOps(self) -> int: ...

class AsynchronousSocketChannel(AsynchronousByteChannel, NetworkChannel):
    """
    Java class 'java.nio.channels.AsynchronousSocketChannel'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.nio.channels.AsynchronousByteChannel,
            java.nio.channels.NetworkChannel
    
    """
    def bind(self, socketAddress: java.net.SocketAddress) -> 'AsynchronousSocketChannel': ...
    _connect_1__A = typing.TypeVar('_connect_1__A')  # <A>
    @typing.overload
    def connect(self, socketAddress: java.net.SocketAddress) -> java.util.concurrent.Future[None]: ...
    @typing.overload
    def connect(self, socketAddress: java.net.SocketAddress, a: _connect_1__A, completionHandler: CompletionHandler[None, _connect_1__A]) -> None: ...
    def getLocalAddress(self) -> java.net.SocketAddress: ...
    def getRemoteAddress(self) -> java.net.SocketAddress: ...
    @typing.overload
    @staticmethod
    def open() -> 'AsynchronousSocketChannel': ...
    @typing.overload
    @staticmethod
    def open(asynchronousChannelGroup: AsynchronousChannelGroup) -> 'AsynchronousSocketChannel': ...
    def provider(self) -> java.nio.channels.spi.AsynchronousChannelProvider: ...
    _read_1__A = typing.TypeVar('_read_1__A')  # <A>
    _read_2__A = typing.TypeVar('_read_2__A')  # <A>
    _read_3__A = typing.TypeVar('_read_3__A')  # <A>
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer) -> java.util.concurrent.Future[int]: ...
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer, long: int, timeUnit: java.util.concurrent.TimeUnit, a: _read_1__A, completionHandler: CompletionHandler[int, _read_1__A]) -> None: ...
    @typing.overload
    def read(self, byteBufferArray: typing.List[java.nio.ByteBuffer], int: int, int2: int, long: int, timeUnit: java.util.concurrent.TimeUnit, a: _read_2__A, completionHandler: CompletionHandler[int, _read_2__A]) -> None: ...
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer, a: _read_3__A, completionHandler: CompletionHandler[int, _read_3__A]) -> None: ...
    _setOption__T = typing.TypeVar('_setOption__T')  # <T>
    def setOption(self, socketOption: java.net.SocketOption[_setOption__T], t: _setOption__T) -> 'AsynchronousSocketChannel': ...
    def shutdownInput(self) -> 'AsynchronousSocketChannel': ...
    def shutdownOutput(self) -> 'AsynchronousSocketChannel': ...
    _write_1__A = typing.TypeVar('_write_1__A')  # <A>
    _write_2__A = typing.TypeVar('_write_2__A')  # <A>
    _write_3__A = typing.TypeVar('_write_3__A')  # <A>
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer) -> java.util.concurrent.Future[int]: ...
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer, long: int, timeUnit: java.util.concurrent.TimeUnit, a: _write_1__A, completionHandler: CompletionHandler[int, _write_1__A]) -> None: ...
    @typing.overload
    def write(self, byteBufferArray: typing.List[java.nio.ByteBuffer], int: int, int2: int, long: int, timeUnit: java.util.concurrent.TimeUnit, a: _write_2__A, completionHandler: CompletionHandler[int, _write_2__A]) -> None: ...
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer, a: _write_3__A, completionHandler: CompletionHandler[int, _write_3__A]) -> None: ...

class DatagramChannel(java.nio.channels.spi.AbstractSelectableChannel, ByteChannel, ScatteringByteChannel, GatheringByteChannel, MulticastChannel):
    """
    Java class 'java.nio.channels.DatagramChannel'
    
        Extends:
            java.nio.channels.spi.AbstractSelectableChannel
    
        Interfaces:
            java.nio.channels.ByteChannel,
            java.nio.channels.ScatteringByteChannel,
            java.nio.channels.GatheringByteChannel,
            java.nio.channels.MulticastChannel
    
    """
    def bind(self, socketAddress: java.net.SocketAddress) -> 'DatagramChannel': ...
    def connect(self, socketAddress: java.net.SocketAddress) -> 'DatagramChannel': ...
    def disconnect(self) -> 'DatagramChannel': ...
    def getLocalAddress(self) -> java.net.SocketAddress: ...
    def getRemoteAddress(self) -> java.net.SocketAddress: ...
    def isConnected(self) -> bool: ...
    @typing.overload
    @staticmethod
    def open() -> 'DatagramChannel': ...
    @typing.overload
    @staticmethod
    def open(protocolFamily: java.net.ProtocolFamily) -> 'DatagramChannel': ...
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer) -> int: ...
    @typing.overload
    def read(self, byteBufferArray: typing.List[java.nio.ByteBuffer], int: int, int2: int) -> int: ...
    @typing.overload
    def read(self, byteBufferArray: typing.List[java.nio.ByteBuffer]) -> int: ...
    def receive(self, byteBuffer: java.nio.ByteBuffer) -> java.net.SocketAddress: ...
    def send(self, byteBuffer: java.nio.ByteBuffer, socketAddress: java.net.SocketAddress) -> int: ...
    _setOption__T = typing.TypeVar('_setOption__T')  # <T>
    def setOption(self, socketOption: java.net.SocketOption[_setOption__T], t: _setOption__T) -> 'DatagramChannel': ...
    def socket(self) -> java.net.DatagramSocket: ...
    def validOps(self) -> int: ...
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer) -> int: ...
    @typing.overload
    def write(self, byteBufferArray: typing.List[java.nio.ByteBuffer], int: int, int2: int) -> int: ...
    @typing.overload
    def write(self, byteBufferArray: typing.List[java.nio.ByteBuffer]) -> int: ...

class Pipe:
    """
    Java class 'java.nio.channels.Pipe'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def open() -> 'Pipe': ...
    def sink(self) -> 'Pipe.SinkChannel': ...
    def source(self) -> 'Pipe.SourceChannel': ...
    class SinkChannel(java.nio.channels.spi.AbstractSelectableChannel, WritableByteChannel, GatheringByteChannel):
        """
        Java class 'java.nio.channels.Pipe$SinkChannel'
        
            Extends:
                java.nio.channels.spi.AbstractSelectableChannel
        
            Interfaces:
                java.nio.channels.WritableByteChannel,
                java.nio.channels.GatheringByteChannel
        
        """
        def validOps(self) -> int: ...
    class SourceChannel(java.nio.channels.spi.AbstractSelectableChannel, ReadableByteChannel, ScatteringByteChannel):
        """
        Java class 'java.nio.channels.Pipe$SourceChannel'
        
            Extends:
                java.nio.channels.spi.AbstractSelectableChannel
        
            Interfaces:
                java.nio.channels.ReadableByteChannel,
                java.nio.channels.ScatteringByteChannel
        
        """
        def validOps(self) -> int: ...

class SeekableByteChannel(ByteChannel):
    """
    Java class 'java.nio.channels.SeekableByteChannel'
    
        Interfaces:
            java.nio.channels.ByteChannel
    
    """
    @typing.overload
    def position(self, long: int) -> 'SeekableByteChannel': ...
    @typing.overload
    def position(self) -> int: ...
    def read(self, byteBuffer: java.nio.ByteBuffer) -> int: ...
    def size(self) -> int: ...
    def truncate(self, long: int) -> 'SeekableByteChannel': ...
    def write(self, byteBuffer: java.nio.ByteBuffer) -> int: ...

class SocketChannel(java.nio.channels.spi.AbstractSelectableChannel, ByteChannel, ScatteringByteChannel, GatheringByteChannel, NetworkChannel):
    """
    Java class 'java.nio.channels.SocketChannel'
    
        Extends:
            java.nio.channels.spi.AbstractSelectableChannel
    
        Interfaces:
            java.nio.channels.ByteChannel,
            java.nio.channels.ScatteringByteChannel,
            java.nio.channels.GatheringByteChannel,
            java.nio.channels.NetworkChannel
    
    """
    def bind(self, socketAddress: java.net.SocketAddress) -> 'SocketChannel': ...
    def connect(self, socketAddress: java.net.SocketAddress) -> bool: ...
    def finishConnect(self) -> bool: ...
    def getLocalAddress(self) -> java.net.SocketAddress: ...
    def getRemoteAddress(self) -> java.net.SocketAddress: ...
    def isConnected(self) -> bool: ...
    def isConnectionPending(self) -> bool: ...
    @typing.overload
    @staticmethod
    def open() -> 'SocketChannel': ...
    @typing.overload
    @staticmethod
    def open(socketAddress: java.net.SocketAddress) -> 'SocketChannel': ...
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer) -> int: ...
    @typing.overload
    def read(self, byteBufferArray: typing.List[java.nio.ByteBuffer], int: int, int2: int) -> int: ...
    @typing.overload
    def read(self, byteBufferArray: typing.List[java.nio.ByteBuffer]) -> int: ...
    _setOption__T = typing.TypeVar('_setOption__T')  # <T>
    def setOption(self, socketOption: java.net.SocketOption[_setOption__T], t: _setOption__T) -> 'SocketChannel': ...
    def shutdownInput(self) -> 'SocketChannel': ...
    def shutdownOutput(self) -> 'SocketChannel': ...
    def socket(self) -> java.net.Socket: ...
    def validOps(self) -> int: ...
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer) -> int: ...
    @typing.overload
    def write(self, byteBufferArray: typing.List[java.nio.ByteBuffer], int: int, int2: int) -> int: ...
    @typing.overload
    def write(self, byteBufferArray: typing.List[java.nio.ByteBuffer]) -> int: ...

class FileChannel(java.nio.channels.spi.AbstractInterruptibleChannel, SeekableByteChannel, GatheringByteChannel, ScatteringByteChannel):
    """
    Java class 'java.nio.channels.FileChannel'
    
        Extends:
            java.nio.channels.spi.AbstractInterruptibleChannel
    
        Interfaces:
            java.nio.channels.SeekableByteChannel,
            java.nio.channels.GatheringByteChannel,
            java.nio.channels.ScatteringByteChannel
    
    """
    def force(self, boolean: bool) -> None: ...
    @typing.overload
    def lock(self, long: int, long2: int, boolean: bool) -> FileLock: ...
    @typing.overload
    def lock(self) -> FileLock: ...
    def map(self, mapMode: 'FileChannel.MapMode', long: int, long2: int) -> java.nio.MappedByteBuffer: ...
    @typing.overload
    @staticmethod
    def open(path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], openOptionArray: typing.List[java.nio.file.OpenOption]) -> 'FileChannel': ...
    @typing.overload
    @staticmethod
    def open(path: typing.Union[java.nio.file.Path, jpype.protocol.SupportsPath], set: java.util.Set[java.nio.file.OpenOption], fileAttributeArray: typing.List[java.nio.file.attribute.FileAttribute[typing.Any]]) -> 'FileChannel': ...
    @typing.overload
    def position(self, long: int) -> 'FileChannel': ...
    @typing.overload
    def position(self) -> int: ...
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer) -> int: ...
    @typing.overload
    def read(self, byteBuffer: java.nio.ByteBuffer, long: int) -> int: ...
    @typing.overload
    def read(self, byteBufferArray: typing.List[java.nio.ByteBuffer], int: int, int2: int) -> int: ...
    @typing.overload
    def read(self, byteBufferArray: typing.List[java.nio.ByteBuffer]) -> int: ...
    def size(self) -> int: ...
    def transferFrom(self, readableByteChannel: ReadableByteChannel, long: int, long2: int) -> int: ...
    def transferTo(self, long: int, long2: int, writableByteChannel: WritableByteChannel) -> int: ...
    def truncate(self, long: int) -> 'FileChannel': ...
    @typing.overload
    def tryLock(self, long: int, long2: int, boolean: bool) -> FileLock: ...
    @typing.overload
    def tryLock(self) -> FileLock: ...
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer) -> int: ...
    @typing.overload
    def write(self, byteBuffer: java.nio.ByteBuffer, long: int) -> int: ...
    @typing.overload
    def write(self, byteBufferArray: typing.List[java.nio.ByteBuffer], int: int, int2: int) -> int: ...
    @typing.overload
    def write(self, byteBufferArray: typing.List[java.nio.ByteBuffer]) -> int: ...
    class MapMode:
        """
        Java class 'java.nio.channels.FileChannel$MapMode'
        
            Extends:
                java.lang.Object
        
          Attributes:
            READ_ONLY (java.nio.channels.FileChannel$MapMode): final static field
            READ_WRITE (java.nio.channels.FileChannel$MapMode): final static field
            PRIVATE (java.nio.channels.FileChannel$MapMode): final static field
        
        """
        READ_ONLY: typing.ClassVar['FileChannel.MapMode'] = ...
        READ_WRITE: typing.ClassVar['FileChannel.MapMode'] = ...
        PRIVATE: typing.ClassVar['FileChannel.MapMode'] = ...
        def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.nio.channels")``.

    AcceptPendingException: typing.Type[AcceptPendingException]
    AlreadyBoundException: typing.Type[AlreadyBoundException]
    AlreadyConnectedException: typing.Type[AlreadyConnectedException]
    AsynchronousByteChannel: typing.Type[AsynchronousByteChannel]
    AsynchronousChannel: typing.Type[AsynchronousChannel]
    AsynchronousChannelGroup: typing.Type[AsynchronousChannelGroup]
    AsynchronousCloseException: typing.Type[AsynchronousCloseException]
    AsynchronousFileChannel: typing.Type[AsynchronousFileChannel]
    AsynchronousServerSocketChannel: typing.Type[AsynchronousServerSocketChannel]
    AsynchronousSocketChannel: typing.Type[AsynchronousSocketChannel]
    ByteChannel: typing.Type[ByteChannel]
    CancelledKeyException: typing.Type[CancelledKeyException]
    Channel: typing.Type[Channel]
    Channels: typing.Type[Channels]
    ClosedByInterruptException: typing.Type[ClosedByInterruptException]
    ClosedChannelException: typing.Type[ClosedChannelException]
    ClosedSelectorException: typing.Type[ClosedSelectorException]
    CompletionHandler: typing.Type[CompletionHandler]
    ConnectionPendingException: typing.Type[ConnectionPendingException]
    DatagramChannel: typing.Type[DatagramChannel]
    FileChannel: typing.Type[FileChannel]
    FileLock: typing.Type[FileLock]
    FileLockInterruptionException: typing.Type[FileLockInterruptionException]
    GatheringByteChannel: typing.Type[GatheringByteChannel]
    IllegalBlockingModeException: typing.Type[IllegalBlockingModeException]
    IllegalChannelGroupException: typing.Type[IllegalChannelGroupException]
    IllegalSelectorException: typing.Type[IllegalSelectorException]
    InterruptedByTimeoutException: typing.Type[InterruptedByTimeoutException]
    InterruptibleChannel: typing.Type[InterruptibleChannel]
    MembershipKey: typing.Type[MembershipKey]
    MulticastChannel: typing.Type[MulticastChannel]
    NetworkChannel: typing.Type[NetworkChannel]
    NoConnectionPendingException: typing.Type[NoConnectionPendingException]
    NonReadableChannelException: typing.Type[NonReadableChannelException]
    NonWritableChannelException: typing.Type[NonWritableChannelException]
    NotYetBoundException: typing.Type[NotYetBoundException]
    NotYetConnectedException: typing.Type[NotYetConnectedException]
    OverlappingFileLockException: typing.Type[OverlappingFileLockException]
    Pipe: typing.Type[Pipe]
    ReadPendingException: typing.Type[ReadPendingException]
    ReadableByteChannel: typing.Type[ReadableByteChannel]
    ScatteringByteChannel: typing.Type[ScatteringByteChannel]
    SeekableByteChannel: typing.Type[SeekableByteChannel]
    SelectableChannel: typing.Type[SelectableChannel]
    SelectionKey: typing.Type[SelectionKey]
    Selector: typing.Type[Selector]
    ServerSocketChannel: typing.Type[ServerSocketChannel]
    ShutdownChannelGroupException: typing.Type[ShutdownChannelGroupException]
    SocketChannel: typing.Type[SocketChannel]
    UnresolvedAddressException: typing.Type[UnresolvedAddressException]
    UnsupportedAddressTypeException: typing.Type[UnsupportedAddressTypeException]
    WritableByteChannel: typing.Type[WritableByteChannel]
    WritePendingException: typing.Type[WritePendingException]
    spi: java.nio.channels.spi.__module_protocol__
