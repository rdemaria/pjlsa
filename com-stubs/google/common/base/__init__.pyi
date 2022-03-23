import com
import com.google.common.base.internal
import java.io
import java.lang
import java.lang.ref
import java.lang.reflect
import java.nio.charset
import java.time
import java.util
import java.util.concurrent
import java.util.function
import java.util.regex
import java.util.stream
import typing



class Ascii:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Static methods pertaining to ASCII characters (those in the range of values :code:`0x00` through :code:`0x7F`), and to
        strings containing such characters.
    
        ASCII utilities also exist in other classes of this package:
    
          - :meth:`~com.google.common.base.Charsets.US_ASCII` specifies the :code:`Charset` of ASCII characters.
          - :meth:`~com.google.common.base.CharMatcher.ascii` matches ASCII characters and provides text processing methods which
            operate only on the ASCII characters of a string.
    
    
        Since:
            7.0
    """
    NUL: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Null ('\0'): The all-zeros character which may serve to accomplish time fill and media fill. Normally used as a C string
        terminator.
    
        Although RFC 20 names this as "Null", note that it is distinct from the C/C++ "NULL" pointer.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    SOH: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Start of Heading: A communication control character used at the beginning of a sequence of characters which constitute a
        machine-sensible address or routing information. Such a sequence is referred to as the "heading." An STX character has
        the effect of terminating a heading.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    STX: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Start of Text: A communication control character which precedes a sequence of characters that is to be treated as an
        entity and entirely transmitted through to the ultimate destination. Such a sequence is referred to as "text." STX may
        be used to terminate a sequence of characters started by SOH.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    ETX: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        End of Text: A communication control character used to terminate a sequence of characters started with STX and
        transmitted as an entity.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    EOT: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        End of Transmission: A communication control character used to indicate the conclusion of a transmission, which may have
        contained one or more texts and any associated headings.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    ENQ: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Enquiry: A communication control character used in data communication systems as a request for a response from a remote
        station. It may be used as a "Who Are You" (WRU) to obtain identification, or may be used to obtain station status, or
        both.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    ACK: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Acknowledge: A communication control character transmitted by a receiver as an affirmative response to a sender.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    BEL: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Bell ('\a'): A character for use when there is a need to call for human attention. It may control alarm or attention
        devices.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    BS: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Backspace ('\b'): A format effector which controls the movement of the printing position one printing space backward on
        the same printing line. (Applicable also to display devices.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    HT: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Horizontal Tabulation ('\t'): A format effector which controls the movement of the printing position to the next in a
        series of predetermined positions along the printing line. (Applicable also to display devices and the skip function on
        punched cards.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    LF: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Line Feed ('\n'): A format effector which controls the movement of the printing position to the next printing line.
        (Applicable also to display devices.) Where appropriate, this character may have the meaning "New Line" (NL), a format
        effector which controls the movement of the printing point to the first printing position on the next printing line. Use
        of this convention requires agreement between sender and recipient of data.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    NL: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Alternate name for :meth:`~com.google.common.base.Ascii.LF`. (:code:`LF` is preferred.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    VT: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Vertical Tabulation ('\v'): A format effector which controls the movement of the printing position to the next in a
        series of predetermined printing lines. (Applicable also to display devices.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    FF: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Form Feed ('\f'): A format effector which controls the movement of the printing position to the first pre-determined
        printing line on the next form or page. (Applicable also to display devices.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    CR: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Carriage Return ('\r'): A format effector which controls the movement of the printing position to the first printing
        position on the same printing line. (Applicable also to display devices.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    SO: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Shift Out: A control character indicating that the code combinations which follow shall be interpreted as outside of the
        character set of the standard code table until a Shift In character is reached.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    SI: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Shift In: A control character indicating that the code combinations which follow shall be interpreted according to the
        standard code table.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DLE: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Data Link Escape: A communication control character which will change the meaning of a limited number of contiguously
        following characters. It is used exclusively to provide supplementary controls in data communication networks.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DC1: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Device Control 1. Characters for the control of ancillary devices associated with data processing or telecommunication
        systems, more especially switching devices "on" or "off." (If a single "stop" control is required to interrupt or turn
        off ancillary devices, DC4 is the preferred assignment.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    XON: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Transmission On: Although originally defined as DC1, this ASCII control character is now better known as the XON code
        used for software flow control in serial communications. The main use is restarting the transmission after the
        communication has been stopped by the XOFF control code.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DC2: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Device Control 2. Characters for the control of ancillary devices associated with data processing or telecommunication
        systems, more especially switching devices "on" or "off." (If a single "stop" control is required to interrupt or turn
        off ancillary devices, DC4 is the preferred assignment.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DC3: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Device Control 3. Characters for the control of ancillary devices associated with data processing or telecommunication
        systems, more especially switching devices "on" or "off." (If a single "stop" control is required to interrupt or turn
        off ancillary devices, DC4 is the preferred assignment.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    XOFF: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Transmission off. See :meth:`~com.google.common.base.Ascii.XON` for explanation.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DC4: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Device Control 4. Characters for the control of ancillary devices associated with data processing or telecommunication
        systems, more especially switching devices "on" or "off." (If a single "stop" control is required to interrupt or turn
        off ancillary devices, DC4 is the preferred assignment.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    NAK: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Negative Acknowledge: A communication control character transmitted by a receiver as a negative response to the sender.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYN: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Synchronous Idle: A communication control character used by a synchronous transmission system in the absence of any
        other character to provide a signal from which synchronism may be achieved or retained.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    ETB: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        End of Transmission Block: A communication control character used to indicate the end of a block of data for
        communication purposes. ETB is used for blocking data where the block structure is not necessarily related to the
        processing format.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    CAN: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Cancel: A control character used to indicate that the data with which it is sent is in error or is to be disregarded.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    EM: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        End of Medium: A control character associated with the sent data which may be used to identify the physical end of the
        medium, or the end of the used, or wanted, portion of information recorded on a medium. (The position of this character
        does not necessarily correspond to the physical end of the medium.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    SUB: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Substitute: A character that may be substituted for a character which is determined to be invalid or in error.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    ESC: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Escape: A control character intended to provide code extension (supplementary characters) in general information
        interchange. The Escape character itself is a prefix affecting the interpretation of a limited number of contiguously
        following characters.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    FS: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        File Separator: These four information separators may be used within data in optional fashion, except that their
        hierarchical relationship shall be: FS is the most inclusive, then GS, then RS, and US is least inclusive. (The content
        and length of a File, Group, Record, or Unit are not specified.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    GS: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Group Separator: These four information separators may be used within data in optional fashion, except that their
        hierarchical relationship shall be: FS is the most inclusive, then GS, then RS, and US is least inclusive. (The content
        and length of a File, Group, Record, or Unit are not specified.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    RS: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Record Separator: These four information separators may be used within data in optional fashion, except that their
        hierarchical relationship shall be: FS is the most inclusive, then GS, then RS, and US is least inclusive. (The content
        and length of a File, Group, Record, or Unit are not specified.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    US: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Unit Separator: These four information separators may be used within data in optional fashion, except that their
        hierarchical relationship shall be: FS is the most inclusive, then GS, then RS, and US is least inclusive. (The content
        and length of a File, Group, Record, or Unit are not specified.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    SP: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Space: A normally non-printing graphic character used to separate words. It is also a format effector which controls the
        movement of the printing position, one printing position forward. (Applicable also to display devices.)
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    SPACE: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Alternate name for :meth:`~com.google.common.base.Ascii.SP`.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEL: typing.ClassVar[int] = ...
    """
    public static final byte :meth:`~src`
    
        Delete: This character is used primarily to "erase" or "obliterate" erroneous or unwanted characters in perforated tape.
    
        Since:
            8.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN: typing.ClassVar[str] = ...
    """
    public static final char :meth:`~src`
    
        The minimum value of an ASCII character.
    
        Since:
            9.0 (was type :code:`int` before 12.0)
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX: typing.ClassVar[str] = ...
    """
    public static final char :meth:`~src`
    
        The maximum value of an ASCII character.
    
        Since:
            9.0 (was type :code:`int` before 12.0)
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def equalsIgnoreCase(charSequence: typing.Union[java.lang.CharSequence, str], charSequence2: typing.Union[java.lang.CharSequence, str]) -> bool: ...
    @staticmethod
    def isLowerCase(char: str) -> bool: ...
    @staticmethod
    def isUpperCase(char: str) -> bool: ...
    @typing.overload
    @staticmethod
    def toLowerCase(char: str) -> str: ...
    @typing.overload
    @staticmethod
    def toLowerCase(charSequence: typing.Union[java.lang.CharSequence, str]) -> str: ...
    @typing.overload
    @staticmethod
    def toLowerCase(string: str) -> str: ...
    @typing.overload
    @staticmethod
    def toUpperCase(char: str) -> str: ...
    @typing.overload
    @staticmethod
    def toUpperCase(charSequence: typing.Union[java.lang.CharSequence, str]) -> str: ...
    @typing.overload
    @staticmethod
    def toUpperCase(string: str) -> str: ...
    @staticmethod
    def truncate(charSequence: typing.Union[java.lang.CharSequence, str], int: int, string: str) -> str: ...

class CaseFormat(java.lang.Enum['CaseFormat']):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public enum :meth:`~src` extends Enum<:class:`~com.google.common.base.CaseFormat`>
    
        Utility class for converting between various ASCII case formats. Behavior is undefined for non-ASCII input.
    
        Since:
            1.0
    """
    LOWER_HYPHEN: typing.ClassVar['CaseFormat'] = ...
    LOWER_UNDERSCORE: typing.ClassVar['CaseFormat'] = ...
    LOWER_CAMEL: typing.ClassVar['CaseFormat'] = ...
    UPPER_CAMEL: typing.ClassVar['CaseFormat'] = ...
    UPPER_UNDERSCORE: typing.ClassVar['CaseFormat'] = ...
    def converterTo(self, caseFormat: 'CaseFormat') -> 'Converter'[str, str]: ...
    def to(self, caseFormat: 'CaseFormat', string: str) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CaseFormat': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['CaseFormat']: ...

class Charsets:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Contains constant definitions for the six standard null instances, which are guaranteed to be supported by all Java
        platform implementations.
    
        Assuming you're free to choose, note that **:meth:`~com.google.common.base.Charsets.UTF_8` is widely preferred**.
    
        See the Guava User Guide article on null.
    
        Since:
            1.0
    """
    US_ASCII: typing.ClassVar[java.nio.charset.Charset] = ...
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public static final Charset :meth:`~src`
    
        US-ASCII: seven-bit ASCII, the Basic Latin block of the Unicode character set (ISO646-US).
    
        **Note for Java 7 and later:** this constant should be treated as deprecated; use null instead.
    
    """
    ISO_8859_1: typing.ClassVar[java.nio.charset.Charset] = ...
    """
    public static final Charset :meth:`~src`
    
        ISO-8859-1: ISO Latin Alphabet Number 1 (ISO-LATIN-1).
    
        **Note for Java 7 and later:** this constant should be treated as deprecated; use null instead.
    
    """
    UTF_8: typing.ClassVar[java.nio.charset.Charset] = ...
    """
    public static final Charset :meth:`~src`
    
        UTF-8: eight-bit UCS Transformation Format.
    
        **Note for Java 7 and later:** this constant should be treated as deprecated; use null instead.
    
    """
    UTF_16BE: typing.ClassVar[java.nio.charset.Charset] = ...
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public static final Charset :meth:`~src`
    
        UTF-16BE: sixteen-bit UCS Transformation Format, big-endian byte order.
    
        **Note for Java 7 and later:** this constant should be treated as deprecated; use null instead.
    
    """
    UTF_16LE: typing.ClassVar[java.nio.charset.Charset] = ...
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public static final Charset :meth:`~src`
    
        UTF-16LE: sixteen-bit UCS Transformation Format, little-endian byte order.
    
        **Note for Java 7 and later:** this constant should be treated as deprecated; use null instead.
    
    """
    UTF_16: typing.ClassVar[java.nio.charset.Charset] = ...
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public static final Charset :meth:`~src`
    
        UTF-16: sixteen-bit UCS Transformation Format, byte order identified by an optional byte-order mark.
    
        **Note for Java 7 and later:** this constant should be treated as deprecated; use null instead.
    
    """

class Defaults:
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public final class :meth:`~src` extends Object
    
        This class provides default values for all Java types, as defined by the JLS.
    
        Since:
            1.0
    """
    _defaultValue__T = typing.TypeVar('_defaultValue__T')  # <T>
    @staticmethod
    def defaultValue(class_: typing.Type[_defaultValue__T]) -> _defaultValue__T: ...

class Enums:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Utility methods for working with null instances.
    
        Since:
            9.0
    """
    @staticmethod
    def getField(enum: java.lang.Enum[typing.Any]) -> java.lang.reflect.Field: ...
    _getIfPresent__T = typing.TypeVar('_getIfPresent__T', bound=java.lang.Enum)  # <T>
    @staticmethod
    def getIfPresent(class_: typing.Type[_getIfPresent__T], string: str) -> 'Optional'[_getIfPresent__T]: ...
    _stringConverter__T = typing.TypeVar('_stringConverter__T', bound=java.lang.Enum)  # <T>
    @staticmethod
    def stringConverter(class_: typing.Type[_stringConverter__T]) -> 'Converter'[str, _stringConverter__T]: ...

_Equivalence__Wrapper__T = typing.TypeVar('_Equivalence__Wrapper__T')  # <T>
_Equivalence__T = typing.TypeVar('_Equivalence__T')  # <T>
class Equivalence(java.util.function.BiPredicate[_Equivalence__T, _Equivalence__T], typing.Generic[_Equivalence__T]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<T> extends Object implements BiPredicate<T, T>
    
        A strategy for determining whether two instances are considered equivalent, and for computing hash codes in a manner
        consistent with that equivalence. Two examples of equivalences are the
        :meth:`~com.google.common.base.Equivalence.identity` and the :meth:`~com.google.common.base.Equivalence.equals`.
    
        Since:
            10.0 (mostly source-compatible since 4.0)
    """
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def equals() -> 'Equivalence'[typing.Any]: ...
    def equivalent(self, t: _Equivalence__T, t2: _Equivalence__T) -> bool: ...
    def equivalentTo(self, t: _Equivalence__T) -> 'Predicate'[_Equivalence__T]: ...
    def hash(self, t: _Equivalence__T) -> int: ...
    @staticmethod
    def identity() -> 'Equivalence'[typing.Any]: ...
    _onResultOf__F = typing.TypeVar('_onResultOf__F')  # <F>
    def onResultOf(self, function: typing.Union['Function'[_onResultOf__F, _Equivalence__T], typing.Callable[[_onResultOf__F], _Equivalence__T]]) -> 'Equivalence'[_onResultOf__F]: ...
    _pairwise__S = typing.TypeVar('_pairwise__S')  # <S>
    def pairwise(self) -> 'Equivalence'[java.lang.Iterable[_pairwise__S]]: ...
    def test(self, t: _Equivalence__T, t2: _Equivalence__T) -> bool: ...
    _wrap__S = typing.TypeVar('_wrap__S')  # <S>
    def wrap(self, s2: _wrap__S) -> 'Equivalence.Wrapper'[_wrap__S]: ...
    class Wrapper(java.io.Serializable, typing.Generic[_Equivalence__Wrapper__T]):
        def equals(self, object: typing.Any) -> bool: ...
        def get(self) -> _Equivalence__Wrapper__T: ...
        def hashCode(self) -> int: ...
        def toString(self) -> str: ...

class FinalizableReference:
    """
    @DoNotMock("Use an instance of one of the Finalizable*Reference classes") :class:`~com.google.common.annotations.GwtIncompatible` public interface :meth:`~src`
    
        Implemented by references that have code to run after garbage collection of their referents.
    
        Since:
            2.0
    
        Also see:
            :class:`~com.google.common.base.FinalizableReferenceQueue`
    """
    def finalizeReferent(self) -> None: ...

class FinalizableReferenceQueue(java.io.Closeable):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public class :meth:`~src` extends Object implements Closeable
    
        A reference queue with an associated background thread that dequeues references and invokes
        :meth:`~com.google.common.base.FinalizableReference.finalizeReferent` on them.
    
        Keep a strong reference to this object until all of the associated referents have been finalized. If this object is
        garbage collected earlier, the backing thread will not invoke :code:`finalizeReferent()` on the remaining references.
    
        As an example of how this is used, imagine you have a class :code:`MyServer` that creates a a null, and you would like
        to ensure that the :code:`ServerSocket` is closed even if the :code:`MyServer` object is garbage-collected without
        calling its :code:`close` method. You *could* use a finalizer to accomplish this, but that has a number of well-known
        problems. Here is how you might use this class instead:
    
        .. code-block: java
        
         public class MyServer implements Closeable {
           private static final FinalizableReferenceQueue frq = new FinalizableReferenceQueue();
           // You might also share this between several objects.
        
           private static final Set<Reference<?>> references = Sets.newConcurrentHashSet();
           // This ensures that the FinalizablePhantomReference itself is not garbage-collected.
        
           private final ServerSocket serverSocket;
        
           private MyServer(...) {
             ...
             this.serverSocket = new ServerSocket(...);
             ...
           }
        
           public static MyServer create(...) {
             MyServer myServer = new MyServer(...);
             final ServerSocket serverSocket = myServer.serverSocket;
             Reference<?> reference = new FinalizablePhantomReference<MyServer>(myServer, frq) {
               public void finalizeReferent() {
                 references.remove(this):
                 if (!serverSocket.isClosed()) {
                   ...log a message about how nobody called close()...
                   try {
                     serverSocket.close();
                   } catch (IOException e) {
                     ...
                   }
                 }
               }
             };
             references.add(reference);
             return myServer;
           }
        
           public void close() {
             serverSocket.close();
           }
         }
         
    
        Since:
            2.0
    """
    def __init__(self): ...
    def close(self) -> None: ...

_Function__F = typing.TypeVar('_Function__F')  # <F>
_Function__T = typing.TypeVar('_Function__T')  # <T>
class Function(java.util.function.Function[_Function__F, _Function__T], typing.Generic[_Function__F, _Function__T]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` @FunctionalInterface public interface :meth:`~src`<F, T> extends Function<F, T>
    
        Legacy version of null.
    
        The :class:`~com.google.common.base.Functions` class provides common functions and related utilities.
    
        As this interface extends :code:`java.util.function.Function`, an instance of this type can be used as a
        :code:`java.util.function.Function` directly. To use a :code:`java.util.function.Function` in a context where a
        :code:`com.google.common.base.Function` is needed, use :code:`function::apply`.
    
        This interface is now a legacy type. Use :code:`java.util.function.Function` (or the appropriate primitive
        specialization such as :code:`ToIntFunction`) instead whenever possible. Otherwise, at least reduce *explicit*
        dependencies on this type by using lambda expressions or method references instead of classes, leaving your code easier
        to migrate in the future.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    def apply(self, f: _Function__F) -> _Function__T: ...
    def equals(self, object: typing.Any) -> bool: ...

class Functions:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Static utility methods pertaining to :code:`com.google.common.base.Function` instances; see that class for information
        about migrating to :code:`java.util.function`.
    
        All methods return serializable functions as long as they're given serializable parameters.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    _compose__A = typing.TypeVar('_compose__A')  # <A>
    _compose__B = typing.TypeVar('_compose__B')  # <B>
    _compose__C = typing.TypeVar('_compose__C')  # <C>
    @staticmethod
    def compose(function: typing.Union[Function[_compose__B, _compose__C], typing.Callable[[_compose__B], _compose__C]], function2: typing.Union[Function[_compose__A, _compose__B], typing.Callable[[_compose__A], _compose__B]]) -> Function[_compose__A, _compose__C]: ...
    _constant__E = typing.TypeVar('_constant__E')  # <E>
    @staticmethod
    def constant(e: _constant__E) -> Function[typing.Any, _constant__E]: ...
    _forMap_0__K = typing.TypeVar('_forMap_0__K')  # <K>
    _forMap_0__V = typing.TypeVar('_forMap_0__V')  # <V>
    _forMap_1__K = typing.TypeVar('_forMap_1__K')  # <K>
    _forMap_1__V = typing.TypeVar('_forMap_1__V')  # <V>
    @typing.overload
    @staticmethod
    def forMap(map: typing.Union[java.util.Map[_forMap_0__K, _forMap_0__V], typing.Mapping[_forMap_0__K, _forMap_0__V]]) -> Function[_forMap_0__K, _forMap_0__V]: ...
    @typing.overload
    @staticmethod
    def forMap(map: typing.Union[java.util.Map[_forMap_1__K, _forMap_1__V], typing.Mapping[_forMap_1__K, _forMap_1__V]], v: _forMap_1__V) -> Function[_forMap_1__K, _forMap_1__V]: ...
    _forPredicate__T = typing.TypeVar('_forPredicate__T')  # <T>
    @staticmethod
    def forPredicate(predicate: typing.Union['Predicate'[_forPredicate__T], typing.Callable[[_forPredicate__T], bool]]) -> Function[_forPredicate__T, bool]: ...
    _forSupplier__T = typing.TypeVar('_forSupplier__T')  # <T>
    @staticmethod
    def forSupplier(supplier: typing.Union['Supplier'[_forSupplier__T], typing.Callable[[], _forSupplier__T]]) -> Function[typing.Any, _forSupplier__T]: ...
    _identity__E = typing.TypeVar('_identity__E')  # <E>
    @staticmethod
    def identity() -> Function[_identity__E, _identity__E]: ...
    @staticmethod
    def toStringFunction() -> Function[typing.Any, str]: ...

class Joiner:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public class :meth:`~src` extends Object
    
        An object which joins pieces of text (specified as an array, null, varargs or even a null) with a separator. It either
        appends the results to an null or returns them as a null. Example:
    
        .. code-block: java
        
         Joiner joiner = Joiner.on("; ").skipNulls();
          . . .
         return joiner.join("Harry", null, "Ron", "Hermione");
         
    
        This returns the string :code:`"Harry; Ron; Hermione"`. Note that all input elements are converted to strings using null
        before being appended.
    
        If neither :meth:`~com.google.common.base.Joiner.skipNulls` nor :meth:`~com.google.common.base.Joiner.useForNull` is
        specified, the joining methods will throw null if any given element is null.
    
        **Warning: joiner instances are always immutable**; a configuration method such as :code:`useForNull` has no effect on
        the instance it is invoked on! You must store and use the new joiner instance returned by the method. This makes joiners
        thread-safe, and safe to store as :code:`static final` constants.
    
        .. code-block: java
        
         // Bad! Do not do this!
         Joiner joiner = Joiner.on(',');
         joiner.skipNulls(); // does nothing!
         return joiner.join("wrong", null, "wrong");
         
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    _appendTo_0__A = typing.TypeVar('_appendTo_0__A', bound=java.lang.Appendable)  # <A>
    _appendTo_1__A = typing.TypeVar('_appendTo_1__A', bound=java.lang.Appendable)  # <A>
    _appendTo_6__A = typing.TypeVar('_appendTo_6__A', bound=java.lang.Appendable)  # <A>
    _appendTo_7__A = typing.TypeVar('_appendTo_7__A', bound=java.lang.Appendable)  # <A>
    @typing.overload
    def appendTo(self, a: _appendTo_0__A, object: typing.Any, object2: typing.Any, objectArray: typing.List[typing.Any]) -> _appendTo_0__A: ...
    @typing.overload
    def appendTo(self, a: _appendTo_1__A, objectArray: typing.List[typing.Any]) -> _appendTo_1__A: ...
    @typing.overload
    def appendTo(self, stringBuilder: java.lang.StringBuilder, iterable: java.lang.Iterable[typing.Any]) -> java.lang.StringBuilder: ...
    @typing.overload
    def appendTo(self, stringBuilder: java.lang.StringBuilder, object: typing.Any, object2: typing.Any, objectArray: typing.List[typing.Any]) -> java.lang.StringBuilder: ...
    @typing.overload
    def appendTo(self, stringBuilder: java.lang.StringBuilder, objectArray: typing.List[typing.Any]) -> java.lang.StringBuilder: ...
    @typing.overload
    def appendTo(self, stringBuilder: java.lang.StringBuilder, iterator: java.util.Iterator[typing.Any]) -> java.lang.StringBuilder: ...
    @typing.overload
    def appendTo(self, a: _appendTo_6__A, iterable: java.lang.Iterable[typing.Any]) -> _appendTo_6__A: ...
    @typing.overload
    def appendTo(self, a: _appendTo_7__A, iterator: java.util.Iterator[typing.Any]) -> _appendTo_7__A: ...
    @typing.overload
    def join(self, iterable: java.lang.Iterable[typing.Any]) -> str: ...
    @typing.overload
    def join(self, object: typing.Any, object2: typing.Any, objectArray: typing.List[typing.Any]) -> str: ...
    @typing.overload
    def join(self, objectArray: typing.List[typing.Any]) -> str: ...
    @typing.overload
    def join(self, iterator: java.util.Iterator[typing.Any]) -> str: ...
    @typing.overload
    @staticmethod
    def on(char: str) -> 'Joiner': ...
    @typing.overload
    @staticmethod
    def on(string: str) -> 'Joiner': ...
    def skipNulls(self) -> 'Joiner': ...
    def useForNull(self, string: str) -> 'Joiner': ...
    @typing.overload
    def withKeyValueSeparator(self, char: str) -> 'Joiner.MapJoiner': ...
    @typing.overload
    def withKeyValueSeparator(self, string: str) -> 'Joiner.MapJoiner': ...
    class MapJoiner:
        _appendTo_0__A = typing.TypeVar('_appendTo_0__A', bound=java.lang.Appendable)  # <A>
        _appendTo_1__A = typing.TypeVar('_appendTo_1__A', bound=java.lang.Appendable)  # <A>
        _appendTo_2__A = typing.TypeVar('_appendTo_2__A', bound=java.lang.Appendable)  # <A>
        @typing.overload
        def appendTo(self, a: _appendTo_0__A, iterable: java.lang.Iterable[java.util.Map.Entry[typing.Any, typing.Any]]) -> _appendTo_0__A: ...
        @typing.overload
        def appendTo(self, a: _appendTo_1__A, iterator: java.util.Iterator[java.util.Map.Entry[typing.Any, typing.Any]]) -> _appendTo_1__A: ...
        @typing.overload
        def appendTo(self, a: _appendTo_2__A, map: typing.Union[java.util.Map[typing.Any, typing.Any], typing.Mapping[typing.Any, typing.Any]]) -> _appendTo_2__A: ...
        @typing.overload
        def appendTo(self, stringBuilder: java.lang.StringBuilder, iterable: java.lang.Iterable[java.util.Map.Entry[typing.Any, typing.Any]]) -> java.lang.StringBuilder: ...
        @typing.overload
        def appendTo(self, stringBuilder: java.lang.StringBuilder, iterator: java.util.Iterator[java.util.Map.Entry[typing.Any, typing.Any]]) -> java.lang.StringBuilder: ...
        @typing.overload
        def appendTo(self, stringBuilder: java.lang.StringBuilder, map: typing.Union[java.util.Map[typing.Any, typing.Any], typing.Mapping[typing.Any, typing.Any]]) -> java.lang.StringBuilder: ...
        @typing.overload
        def join(self, iterable: java.lang.Iterable[java.util.Map.Entry[typing.Any, typing.Any]]) -> str: ...
        @typing.overload
        def join(self, iterator: java.util.Iterator[java.util.Map.Entry[typing.Any, typing.Any]]) -> str: ...
        @typing.overload
        def join(self, map: typing.Union[java.util.Map[typing.Any, typing.Any], typing.Mapping[typing.Any, typing.Any]]) -> str: ...
        def useForNull(self, string: str) -> 'Joiner.MapJoiner': ...

class MoreObjects:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Helper functions that operate on any :code:`Object`, and are not already provided in null.
    
        See the Guava User Guide on null.
    
        Since:
            18.0 (since 2.0 as :code:`Objects`)
    """
    _firstNonNull__T = typing.TypeVar('_firstNonNull__T')  # <T>
    @staticmethod
    def firstNonNull(t: _firstNonNull__T, t2: _firstNonNull__T) -> _firstNonNull__T: ...
    @typing.overload
    @staticmethod
    def toStringHelper(class_: typing.Type[typing.Any]) -> 'MoreObjects.ToStringHelper': ...
    @typing.overload
    @staticmethod
    def toStringHelper(object: typing.Any) -> 'MoreObjects.ToStringHelper': ...
    @typing.overload
    @staticmethod
    def toStringHelper(string: str) -> 'MoreObjects.ToStringHelper': ...
    class ToStringHelper:
        @typing.overload
        def add(self, string: str, boolean: bool) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def add(self, string: str, char: str) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def add(self, string: str, double: float) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def add(self, string: str, float: float) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def add(self, string: str, int: int) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def add(self, string: str, object: typing.Any) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def add(self, string: str, long: int) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def addValue(self, boolean: bool) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def addValue(self, char: str) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def addValue(self, double: float) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def addValue(self, float: float) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def addValue(self, int: int) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def addValue(self, object: typing.Any) -> 'MoreObjects.ToStringHelper': ...
        @typing.overload
        def addValue(self, long: int) -> 'MoreObjects.ToStringHelper': ...
        def omitNullValues(self) -> 'MoreObjects.ToStringHelper': ...
        def toString(self) -> str: ...

_Optional__T = typing.TypeVar('_Optional__T')  # <T>
class Optional(java.io.Serializable, typing.Generic[_Optional__T]):
    """
    @DoNotMock("Use Optional.of(value) or Optional.absent()") :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.serializable`=true) public abstract class :meth:`~src`<T> extends Object implements Serializable
    
        An immutable object that may contain a non-null reference to another object. Each instance of this type either contains
        a non-null reference, or contains nothing (in which case we say that the reference is "absent"); it is never said to
        "contain :code:`null`".
    
        A non-null :code:`Optional<T>` reference can be used as a replacement for a nullable :code:`T` reference. It allows you
        to represent "a :code:`T` that must be present" and a "a :code:`T` that might be absent" as two distinct types in your
        program, which can aid clarity.
    
        Some uses of this class include
    
          - As a method return type, as an alternative to returning :code:`null` to indicate that no value was available
          - To distinguish between "unknown" (for example, not present in a map) and "known to have no value" (present in the map,
            with value :code:`Optional.absent()`)
          - To wrap nullable references for storage in a collection that does not support :code:`null` (though there are several
            other approaches to this that should be considered first)
    
    
        A common alternative to using this class is to find or create a suitable `null object
        <http://en.wikipedia.org/wiki/Null_Object_pattern>` for the type in question.
    
        This class is not intended as a direct analogue of any existing "option" or "maybe" construct from other programming
        environments, though it may bear some similarities.
    
        **Comparison to :code:`java.util.Optional` (JDK 8 and higher):** A new :code:`Optional` class was added for Java 8. The
        two classes are extremely similar, but incompatible (they cannot share a common supertype). *All* known differences are
        listed either here or with the relevant methods below.
    
          - This class is serializable; :code:`java.util.Optional` is not.
          - :code:`java.util.Optional` has the additional methods :code:`ifPresent`, :code:`filter`, :code:`flatMap`, and
            :code:`orElseThrow`.
          - :code:`java.util` offers the primitive-specialized versions :code:`OptionalInt`, :code:`OptionalLong` and
            :code:`OptionalDouble`, the use of which is recommended; Guava does not have these.
    
    
        **There are no plans to deprecate this class in the foreseeable future.** However, we do gently recommend that you
        prefer the new, standard Java class whenever possible.
    
        See the Guava User Guide article on null.
    
        Since:
            10.0
    
        Also see:
            :meth:`~serialized`
    """
    _absent__T = typing.TypeVar('_absent__T')  # <T>
    @staticmethod
    def absent() -> 'Optional'[_absent__T]: ...
    def asSet(self) -> java.util.Set[_Optional__T]: ...
    def equals(self, object: typing.Any) -> bool: ...
    _fromJavaUtil__T = typing.TypeVar('_fromJavaUtil__T')  # <T>
    @staticmethod
    def fromJavaUtil(optional: java.util.Optional[_fromJavaUtil__T]) -> 'Optional'[_fromJavaUtil__T]: ...
    _fromNullable__T = typing.TypeVar('_fromNullable__T')  # <T>
    @staticmethod
    def fromNullable(t: _fromNullable__T) -> 'Optional'[_fromNullable__T]: ...
    def get(self) -> _Optional__T: ...
    def hashCode(self) -> int: ...
    def isPresent(self) -> bool: ...
    _of__T = typing.TypeVar('_of__T')  # <T>
    @staticmethod
    def of(t: _of__T) -> 'Optional'[_of__T]: ...
    def orNull(self) -> _Optional__T: ...
    _presentInstances__T = typing.TypeVar('_presentInstances__T')  # <T>
    @staticmethod
    def presentInstances(iterable: java.lang.Iterable['Optional'[_presentInstances__T]]) -> java.lang.Iterable[_presentInstances__T]: ...
    _toJavaUtil_1__T = typing.TypeVar('_toJavaUtil_1__T')  # <T>
    @typing.overload
    def toJavaUtil(self) -> java.util.Optional[_Optional__T]: ...
    @typing.overload
    @staticmethod
    def toJavaUtil(optional: 'Optional'[_toJavaUtil_1__T]) -> java.util.Optional[_toJavaUtil_1__T]: ...
    def toString(self) -> str: ...
    _transform__V = typing.TypeVar('_transform__V')  # <V>
    def transform(self, function: typing.Union[Function[_Optional__T, _transform__V], typing.Callable[[_Optional__T], _transform__V]]) -> 'Optional'[_transform__V]: ...

class Preconditions:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Static convenience methods that help a method or constructor check whether it was invoked correctly (that is, whether
        its *preconditions* were met).
    
        If the precondition is not met, the :code:`Preconditions` method throws an unchecked exception of a specified type,
        which helps the method in which the exception was thrown communicate that its caller has made a mistake. This allows
        constructs such as
    
        .. code-block: java
        
         public static double sqrt(double value) {
           if (value < 0) {
             throw new IllegalArgumentException("input is negative: " + value);
           }
           // calculate square root
         }
         
    
        to be replaced with the more compact
    
        .. code-block: java
        
         public static double sqrt(double value) {
           checkArgument(value >= 0, "input is negative: %s", value);
           // calculate square root
         }
         
    
        so that a hypothetical bad caller of this method, such as:
    
        .. code-block: java
        
         void exampleBadCaller() {
           double d = sqrt(-1.0);
         }
         
    
        would be flagged as having called :code:`sqrt()` with an illegal argument.
    
        Performance
    -----------
    
    
        Avoid passing message arguments that are expensive to compute; your code will always compute them, even though they
        usually won't be needed. If you have such arguments, use the conventional if/throw idiom instead.
    
        Depending on your message arguments, memory may be allocated for boxing and varargs array creation. However, the methods
        of this class have a large number of overloads that prevent such allocations in many common cases.
    
        The message string is not formatted unless the exception will be thrown, so the cost of the string formatting itself
        should not be a concern.
    
        As with any performance concerns, you should consider profiling your code (in a production environment if possible)
        before spending a lot of effort on tweaking a particular element.
    
        Other types of preconditions
    ----------------------------
    
    
        Not every type of precondition failure is supported by these methods. Continue to throw standard JDK exceptions such as
        null or null in the situations they are intended for.
    
        Non-preconditions
    -----------------
    
    
        It is of course possible to use the methods of this class to check for invalid conditions which are *not the caller's
        fault*. Doing so is **not recommended** because it is misleading to future readers of the code and of stack traces. See
        Conditional failures explained in the Guava User Guide for more advice. Notably, :class:`~com.google.common.base.Verify`
        offers assertions similar to those in this class for non-precondition checks.
    
        :code:`java.util.Objects.requireNonNull()`
    ------------------------------------------
    
    
        Projects which use :code:`com.google.common` should generally avoid the use of null. Instead, use whichever of
        :meth:`~com.google.common.base.Preconditions.checkNotNull` or :meth:`~com.google.common.base.Verify.verifyNotNull` is
        appropriate to the situation. (The same goes for the message-accepting overloads.)
    
        Only :code:`%s` is supported
    ----------------------------
    
    
        :code:`Preconditions` uses :meth:`~com.google.common.base.Strings.lenientFormat` to format error message template
        strings. This only supports the :code:`"%s"` specifier, not the full range of null specifiers. However, note that if the
        number of arguments does not match the number of occurrences of :code:`"%s"` in the format string, :code:`Preconditions`
        will still behave as expected, and will still include all argument values in the error message; the message will simply
        not be formatted exactly as intended.
    
        More information
    ----------------
    
    
        See the Guava User Guide on null.
    
        Since:
            2.0
    """
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, char: str, char2: str) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, char: str, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, char: str, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, char: str, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, int: int, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, int: int, int2: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, int: int, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, int: int, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, object: typing.Any, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, object: typing.Any, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, object: typing.Any, object2: typing.Any, object3: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, object: typing.Any, object2: typing.Any, object3: typing.Any, object4: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, object: typing.Any, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, long: int, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, long: int, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, long: int, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkArgument(boolean: bool, string: str, long: int, long2: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkElementIndex(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def checkElementIndex(int: int, int2: int, string: str) -> int: ...
    _checkNotNull_0__T = typing.TypeVar('_checkNotNull_0__T')  # <T>
    _checkNotNull_1__T = typing.TypeVar('_checkNotNull_1__T')  # <T>
    _checkNotNull_2__T = typing.TypeVar('_checkNotNull_2__T')  # <T>
    _checkNotNull_3__T = typing.TypeVar('_checkNotNull_3__T')  # <T>
    _checkNotNull_4__T = typing.TypeVar('_checkNotNull_4__T')  # <T>
    _checkNotNull_5__T = typing.TypeVar('_checkNotNull_5__T')  # <T>
    _checkNotNull_6__T = typing.TypeVar('_checkNotNull_6__T')  # <T>
    _checkNotNull_7__T = typing.TypeVar('_checkNotNull_7__T')  # <T>
    _checkNotNull_8__T = typing.TypeVar('_checkNotNull_8__T')  # <T>
    _checkNotNull_9__T = typing.TypeVar('_checkNotNull_9__T')  # <T>
    _checkNotNull_10__T = typing.TypeVar('_checkNotNull_10__T')  # <T>
    _checkNotNull_11__T = typing.TypeVar('_checkNotNull_11__T')  # <T>
    _checkNotNull_12__T = typing.TypeVar('_checkNotNull_12__T')  # <T>
    _checkNotNull_13__T = typing.TypeVar('_checkNotNull_13__T')  # <T>
    _checkNotNull_14__T = typing.TypeVar('_checkNotNull_14__T')  # <T>
    _checkNotNull_15__T = typing.TypeVar('_checkNotNull_15__T')  # <T>
    _checkNotNull_16__T = typing.TypeVar('_checkNotNull_16__T')  # <T>
    _checkNotNull_17__T = typing.TypeVar('_checkNotNull_17__T')  # <T>
    _checkNotNull_18__T = typing.TypeVar('_checkNotNull_18__T')  # <T>
    _checkNotNull_19__T = typing.TypeVar('_checkNotNull_19__T')  # <T>
    _checkNotNull_20__T = typing.TypeVar('_checkNotNull_20__T')  # <T>
    _checkNotNull_21__T = typing.TypeVar('_checkNotNull_21__T')  # <T>
    _checkNotNull_22__T = typing.TypeVar('_checkNotNull_22__T')  # <T>
    _checkNotNull_23__T = typing.TypeVar('_checkNotNull_23__T')  # <T>
    _checkNotNull_24__T = typing.TypeVar('_checkNotNull_24__T')  # <T>
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_0__T) -> _checkNotNull_0__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_1__T, object: typing.Any) -> _checkNotNull_1__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_2__T, string: str, char: str) -> _checkNotNull_2__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_3__T, string: str, char: str, char2: str) -> _checkNotNull_3__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_4__T, string: str, char: str, int: int) -> _checkNotNull_4__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_5__T, string: str, char: str, object: typing.Any) -> _checkNotNull_5__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_6__T, string: str, char: str, long: int) -> _checkNotNull_6__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_7__T, string: str, int: int) -> _checkNotNull_7__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_8__T, string: str, int: int, char: str) -> _checkNotNull_8__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_9__T, string: str, int: int, int2: int) -> _checkNotNull_9__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_10__T, string: str, int: int, object: typing.Any) -> _checkNotNull_10__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_11__T, string: str, int: int, long: int) -> _checkNotNull_11__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_12__T, string: str, object: typing.Any) -> _checkNotNull_12__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_13__T, string: str, object: typing.Any, char: str) -> _checkNotNull_13__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_14__T, string: str, object: typing.Any, int: int) -> _checkNotNull_14__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_15__T, string: str, object: typing.Any, object2: typing.Any) -> _checkNotNull_15__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_16__T, string: str, object: typing.Any, object2: typing.Any, object3: typing.Any) -> _checkNotNull_16__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_17__T, string: str, object: typing.Any, object2: typing.Any, object3: typing.Any, object4: typing.Any) -> _checkNotNull_17__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_18__T, string: str, object: typing.Any, long: int) -> _checkNotNull_18__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_19__T, string: str, objectArray: typing.List[typing.Any]) -> _checkNotNull_19__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_20__T, string: str, long: int) -> _checkNotNull_20__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_21__T, string: str, long: int, char: str) -> _checkNotNull_21__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_22__T, string: str, long: int, int: int) -> _checkNotNull_22__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_23__T, string: str, long: int, object: typing.Any) -> _checkNotNull_23__T: ...
    @typing.overload
    @staticmethod
    def checkNotNull(t: _checkNotNull_24__T, string: str, long: int, long2: int) -> _checkNotNull_24__T: ...
    @typing.overload
    @staticmethod
    def checkPositionIndex(int: int, int2: int) -> int: ...
    @typing.overload
    @staticmethod
    def checkPositionIndex(int: int, int2: int, string: str) -> int: ...
    @staticmethod
    def checkPositionIndexes(int: int, int2: int, int3: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, char: str, char2: str) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, char: str, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, char: str, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, char: str, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, int: int, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, int: int, int2: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, int: int, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, int: int, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, object: typing.Any, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, object: typing.Any, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, object: typing.Any, object2: typing.Any, object3: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, object: typing.Any, object2: typing.Any, object3: typing.Any, object4: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, object: typing.Any, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, long: int, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, long: int, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, long: int, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def checkState(boolean: bool, string: str, long: int, long2: int) -> None: ...

_Predicate__T = typing.TypeVar('_Predicate__T')  # <T>
class Predicate(java.util.function.Predicate[_Predicate__T], typing.Generic[_Predicate__T]):
    """
    @FunctionalInterface :class:`~com.google.common.annotations.GwtCompatible` public interface :meth:`~src`<T> extends Predicate<T>
    
        Legacy version of null. Determines a true or false value for a given input.
    
        As this interface extends :code:`java.util.function.Predicate`, an instance of this type may be used as a
        :code:`Predicate` directly. To use a :code:`java.util.function.Predicate` where a
        :code:`com.google.common.base.Predicate` is expected, use the method reference :code:`predicate::test`.
    
        This interface is now a legacy type. Use :code:`java.util.function.Predicate` (or the appropriate primitive
        specialization such as :code:`IntPredicate`) instead whenever possible. Otherwise, at least reduce *explicit*
        dependencies on this type by using lambda expressions or method references instead of classes, leaving your code easier
        to migrate in the future.
    
        The :class:`~com.google.common.base.Predicates` class provides common predicates and related utilities.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    def apply(self, t: _Predicate__T) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def test(self, t: _Predicate__T) -> bool: ...

class Predicates:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Static utility methods pertaining to :code:`Predicate` instances.
    
        All methods return serializable predicates as long as they're given serializable parameters.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    _alwaysFalse__T = typing.TypeVar('_alwaysFalse__T')  # <T>
    @staticmethod
    def alwaysFalse() -> Predicate[_alwaysFalse__T]: ...
    _alwaysTrue__T = typing.TypeVar('_alwaysTrue__T')  # <T>
    @staticmethod
    def alwaysTrue() -> Predicate[_alwaysTrue__T]: ...
    _compose__A = typing.TypeVar('_compose__A')  # <A>
    _compose__B = typing.TypeVar('_compose__B')  # <B>
    @staticmethod
    def compose(predicate: typing.Union[Predicate[_compose__B], typing.Callable[[_compose__B], bool]], function: typing.Union[Function[_compose__A, _compose__B], typing.Callable[[_compose__A], _compose__B]]) -> Predicate[_compose__A]: ...
    @staticmethod
    def contains(pattern: java.util.regex.Pattern) -> Predicate[java.lang.CharSequence]: ...
    @staticmethod
    def containsPattern(string: str) -> Predicate[java.lang.CharSequence]: ...
    _equalTo__T = typing.TypeVar('_equalTo__T')  # <T>
    @staticmethod
    def equalTo(t: _equalTo__T) -> Predicate[_equalTo__T]: ...
    @staticmethod
    def instanceOf(class_: typing.Type[typing.Any]) -> Predicate[typing.Any]: ...
    _isNull__T = typing.TypeVar('_isNull__T')  # <T>
    @staticmethod
    def isNull() -> Predicate[_isNull__T]: ...
    _notNull__T = typing.TypeVar('_notNull__T')  # <T>
    @staticmethod
    def notNull() -> Predicate[_notNull__T]: ...
    @staticmethod
    def subtypeOf(class_: typing.Type[typing.Any]) -> Predicate[typing.Type[typing.Any]]: ...

class Splitter:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Extracts non-overlapping substrings from an input string, typically by recognizing appearances of a *separator*
        sequence. This separator can be specified as a single :meth:`~com.google.common.base.Splitter.on`, fixed
        :meth:`~com.google.common.base.Splitter.on`, :meth:`~com.google.common.base.Splitter.onPattern` or
        :meth:`~com.google.common.base.Splitter.on` instance. Or, instead of using a separator at all, a splitter can extract
        adjacent substrings of a given :meth:`~com.google.common.base.Splitter.fixedLength`.
    
        For example, this expression:
    
        .. code-block: java
        
         Splitter.on(',').split("foo,bar,qux")
         
        ... produces an :code:`Iterable` containing :code:`"foo"`, :code:`"bar"` and :code:`"qux"`, in that order.
    
        By default, :code:`Splitter`'s behavior is simplistic and unassuming. The following expression:
    
        .. code-block: java
        
         Splitter.on(',').split(" foo,,,  bar ,")
         
        ... yields the substrings :code:`[" foo", "", "", " bar ", ""]`. If this is not the desired behavior, use configuration
        methods to obtain a *new* splitter instance with modified behavior:
    
        .. code-block: java
        
         private static final Splitter MY_SPLITTER = Splitter.on(',')
             .trimResults()
             .omitEmptyStrings();
         
    
        Now :code:`MY_SPLITTER.split("foo,,, bar ,")` returns just :code:`["foo", "bar"]`. Note that the order in which these
        configuration methods are called is never significant.
    
        **Warning:** Splitter instances are immutable. Invoking a configuration method has no effect on the receiving instance;
        you must store and use the new splitter instance it returns instead.
    
        .. code-block: java
        
         // Do NOT do this
         Splitter splitter = Splitter.on('/');
         splitter.trimResults(); // does nothing!
         return splitter.split("wrong / wrong / wrong");
         
    
        For separator-based splitters that do not use :code:`omitEmptyStrings`, an input string containing :code:`n` occurrences
        of the separator naturally yields an iterable of size :code:`n + 1`. So if the separator does not occur anywhere in the
        input, a single substring is returned containing the entire input. Consequently, all splitters split the empty string to
        :code:`[""]` (note: even fixed-length splitters).
    
        Splitter instances are thread-safe immutable, and are therefore safe to store as :code:`static final` constants.
    
        The :class:`~com.google.common.base.Joiner` class provides the inverse operation to splitting, but note that a
        round-trip between the two should be assumed to be lossy.
    
        See the Guava User Guide article on null.
    
        Since:
            1.0
    """
    @staticmethod
    def fixedLength(int: int) -> 'Splitter': ...
    def limit(self, int: int) -> 'Splitter': ...
    def omitEmptyStrings(self) -> 'Splitter': ...
    @typing.overload
    @staticmethod
    def on(char: str) -> 'Splitter': ...
    @typing.overload
    @staticmethod
    def on(charMatcher: 'CharMatcher') -> 'Splitter': ...
    @typing.overload
    @staticmethod
    def on(string: str) -> 'Splitter': ...
    @typing.overload
    @staticmethod
    def on(pattern: java.util.regex.Pattern) -> 'Splitter': ...
    @staticmethod
    def onPattern(string: str) -> 'Splitter': ...
    def split(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> java.lang.Iterable[str]: ...
    def splitToList(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> java.util.List[str]: ...
    def splitToStream(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> java.util.stream.Stream[str]: ...
    @typing.overload
    def trimResults(self) -> 'Splitter': ...
    @typing.overload
    def trimResults(self, charMatcher: 'CharMatcher') -> 'Splitter': ...
    @typing.overload
    def withKeyValueSeparator(self, char: str) -> 'Splitter.MapSplitter': ...
    @typing.overload
    def withKeyValueSeparator(self, splitter: 'Splitter') -> 'Splitter.MapSplitter': ...
    @typing.overload
    def withKeyValueSeparator(self, string: str) -> 'Splitter.MapSplitter': ...
    class MapSplitter:
        def split(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> java.util.Map[str, str]: ...

class StandardSystemProperty(java.lang.Enum['StandardSystemProperty']):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public enum :meth:`~src` extends Enum<:class:`~com.google.common.base.StandardSystemProperty`>
    
        Represents a standard system property.
    
        Since:
            15.0
    """
    JAVA_VERSION: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_VENDOR: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_VENDOR_URL: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_HOME: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_VM_SPECIFICATION_VERSION: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_VM_SPECIFICATION_VENDOR: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_VM_SPECIFICATION_NAME: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_VM_VERSION: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_VM_VENDOR: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_VM_NAME: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_SPECIFICATION_VERSION: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_SPECIFICATION_VENDOR: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_SPECIFICATION_NAME: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_CLASS_VERSION: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_CLASS_PATH: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_LIBRARY_PATH: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_IO_TMPDIR: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_COMPILER: typing.ClassVar['StandardSystemProperty'] = ...
    JAVA_EXT_DIRS: typing.ClassVar['StandardSystemProperty'] = ...
    OS_NAME: typing.ClassVar['StandardSystemProperty'] = ...
    OS_ARCH: typing.ClassVar['StandardSystemProperty'] = ...
    OS_VERSION: typing.ClassVar['StandardSystemProperty'] = ...
    FILE_SEPARATOR: typing.ClassVar['StandardSystemProperty'] = ...
    PATH_SEPARATOR: typing.ClassVar['StandardSystemProperty'] = ...
    LINE_SEPARATOR: typing.ClassVar['StandardSystemProperty'] = ...
    USER_NAME: typing.ClassVar['StandardSystemProperty'] = ...
    USER_HOME: typing.ClassVar['StandardSystemProperty'] = ...
    USER_DIR: typing.ClassVar['StandardSystemProperty'] = ...
    def key(self) -> str: ...
    def toString(self) -> str: ...
    def value(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'StandardSystemProperty': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['StandardSystemProperty']: ...

class Stopwatch:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        An object that accurately measures *elapsed time*: the measured duration between two successive readings of "now" in the
        same process.
    
        In contrast, *wall time* is a reading of "now" as given by a method like null, best represented as an :code:`Instant`.
        Such values *can* be subtracted to obtain a :code:`Duration` (such as by :code:`Duration.between`), but doing so does
        *not* give a reliable measurement of elapsed time, because wall time readings are inherently approximate, routinely
        affected by periodic clock corrections. Because this class (by default) uses null, it is unaffected by these changes.
    
        Use this class instead of direct calls to null for two reasons:
    
          - The raw :code:`long` values returned by :code:`nanoTime` are meaningless and unsafe to use in any other way than how
            :code:`Stopwatch` uses them.
          - An alternative source of nanosecond ticks can be substituted, for example for testing or performance reasons, without
            affecting most of your code.
    
    
        Basic usage:
    
        .. code-block: java
        
         Stopwatch stopwatch = Stopwatch.createStarted();
         doSomething();
         stopwatch.stop(); // optional
        
         Duration duration = stopwatch.elapsed();
        
         log.info("time: " + stopwatch); // formatted string like "12.3 ms"
         
    
        The state-changing methods are not idempotent; it is an error to start or stop a stopwatch that is already in the
        desired state.
    
        When testing code that uses this class, use :meth:`~com.google.common.base.Stopwatch.createUnstarted` or
        :meth:`~com.google.common.base.Stopwatch.createStarted` to supply a fake or mock ticker. This allows you to simulate any
        valid behavior of the stopwatch.
    
        **Note:** This class is not thread-safe.
    
        **Warning for Android users:** a stopwatch with default behavior may not continue to keep time while the device is
        asleep. Instead, create one like this:
    
        .. code-block: java
        
         Stopwatch.createStarted(
              new Ticker() {
                public long read() {
                  return android.os.SystemClock.elapsedRealtimeNanos();
                }
              });
         
    
        Since:
            10.0
    """
    @typing.overload
    @staticmethod
    def createStarted() -> 'Stopwatch': ...
    @typing.overload
    @staticmethod
    def createStarted(ticker: 'Ticker') -> 'Stopwatch': ...
    @typing.overload
    @staticmethod
    def createUnstarted() -> 'Stopwatch': ...
    @typing.overload
    @staticmethod
    def createUnstarted(ticker: 'Ticker') -> 'Stopwatch': ...
    @typing.overload
    def elapsed(self) -> java.time.Duration: ...
    @typing.overload
    def elapsed(self, timeUnit: java.util.concurrent.TimeUnit) -> int: ...
    def isRunning(self) -> bool: ...
    def reset(self) -> 'Stopwatch': ...
    def start(self) -> 'Stopwatch': ...
    def stop(self) -> 'Stopwatch': ...
    def toString(self) -> str: ...

class Strings:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Static utility methods pertaining to :code:`String` or :code:`CharSequence` instances.
    
        Since:
            3.0
    """
    @staticmethod
    def commonPrefix(charSequence: typing.Union[java.lang.CharSequence, str], charSequence2: typing.Union[java.lang.CharSequence, str]) -> str: ...
    @staticmethod
    def commonSuffix(charSequence: typing.Union[java.lang.CharSequence, str], charSequence2: typing.Union[java.lang.CharSequence, str]) -> str: ...
    @staticmethod
    def emptyToNull(string: str) -> str: ...
    @staticmethod
    def isNullOrEmpty(string: str) -> bool: ...
    @staticmethod
    def lenientFormat(string: str, objectArray: typing.List[typing.Any]) -> str: ...
    @staticmethod
    def nullToEmpty(string: str) -> str: ...
    @staticmethod
    def padEnd(string: str, int: int, char: str) -> str: ...
    @staticmethod
    def padStart(string: str, int: int, char: str) -> str: ...
    @staticmethod
    def repeat(string: str, int: int) -> str: ...

_Supplier__T = typing.TypeVar('_Supplier__T')  # <T>
class Supplier(java.util.function.Supplier[_Supplier__T], typing.Generic[_Supplier__T]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` @FunctionalInterface public interface :meth:`~src`<T> extends Supplier<T>
    
        Legacy version of null. Semantically, this could be a factory, generator, builder, closure, or something else entirely.
        No guarantees are implied by this interface.
    
        The :class:`~com.google.common.base.Suppliers` class provides common suppliers and related utilities.
    
        As this interface extends :code:`java.util.function.Supplier`, an instance of this type can be used as a
        :code:`java.util.function.Supplier` directly. To use a :code:`java.util.function.Supplier` in a context where a
        :code:`com.google.common.base.Supplier` is needed, use :code:`supplier::get`.
    
        See the Guava User Guide article on null.
    
        Since:
            2.0
    """
    def get(self) -> _Supplier__T: ...

class Suppliers:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Useful suppliers.
    
        All methods return serializable suppliers as long as they're given serializable parameters.
    
        Since:
            2.0
    """
    _compose__F = typing.TypeVar('_compose__F')  # <F>
    _compose__T = typing.TypeVar('_compose__T')  # <T>
    @staticmethod
    def compose(function: typing.Union[Function[_compose__F, _compose__T], typing.Callable[[_compose__F], _compose__T]], supplier: typing.Union[Supplier[_compose__F], typing.Callable[[], _compose__F]]) -> Supplier[_compose__T]: ...
    _memoize__T = typing.TypeVar('_memoize__T')  # <T>
    @staticmethod
    def memoize(supplier: typing.Union[Supplier[_memoize__T], typing.Callable[[], _memoize__T]]) -> Supplier[_memoize__T]: ...
    _memoizeWithExpiration__T = typing.TypeVar('_memoizeWithExpiration__T')  # <T>
    @staticmethod
    def memoizeWithExpiration(supplier: typing.Union[Supplier[_memoizeWithExpiration__T], typing.Callable[[], _memoizeWithExpiration__T]], long: int, timeUnit: java.util.concurrent.TimeUnit) -> Supplier[_memoizeWithExpiration__T]: ...
    _ofInstance__T = typing.TypeVar('_ofInstance__T')  # <T>
    @staticmethod
    def ofInstance(t: _ofInstance__T) -> Supplier[_ofInstance__T]: ...
    _supplierFunction__T = typing.TypeVar('_supplierFunction__T')  # <T>
    @staticmethod
    def supplierFunction() -> Function[Supplier[_supplierFunction__T], _supplierFunction__T]: ...
    _synchronizedSupplier__T = typing.TypeVar('_synchronizedSupplier__T')  # <T>
    @staticmethod
    def synchronizedSupplier(supplier: typing.Union[Supplier[_synchronizedSupplier__T], typing.Callable[[], _synchronizedSupplier__T]]) -> Supplier[_synchronizedSupplier__T]: ...

class Throwables:
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Static utility methods pertaining to instances of null.
    
        See the Guava User Guide entry on Throwables.
    
        Since:
            1.0
    """
    @staticmethod
    def getCausalChain(throwable: java.lang.Throwable) -> java.util.List[java.lang.Throwable]: ...
    _getCauseAs__X = typing.TypeVar('_getCauseAs__X', bound=java.lang.Throwable)  # <X>
    @staticmethod
    def getCauseAs(throwable: java.lang.Throwable, class_: typing.Type[_getCauseAs__X]) -> _getCauseAs__X: ...
    @staticmethod
    def getRootCause(throwable: java.lang.Throwable) -> java.lang.Throwable: ...
    @staticmethod
    def getStackTraceAsString(throwable: java.lang.Throwable) -> str: ...
    @staticmethod
    def lazyStackTrace(throwable: java.lang.Throwable) -> java.util.List[java.lang.StackTraceElement]: ...
    @staticmethod
    def lazyStackTraceIsLazy() -> bool: ...
    @staticmethod
    def propagate(throwable: java.lang.Throwable) -> java.lang.RuntimeException: ...
    _propagateIfInstanceOf__X = typing.TypeVar('_propagateIfInstanceOf__X', bound=java.lang.Throwable)  # <X>
    @staticmethod
    def propagateIfInstanceOf(throwable: java.lang.Throwable, class_: typing.Type[_propagateIfInstanceOf__X]) -> None: ...
    _propagateIfPossible_1__X = typing.TypeVar('_propagateIfPossible_1__X', bound=java.lang.Throwable)  # <X>
    _propagateIfPossible_2__X1 = typing.TypeVar('_propagateIfPossible_2__X1', bound=java.lang.Throwable)  # <X1>
    _propagateIfPossible_2__X2 = typing.TypeVar('_propagateIfPossible_2__X2', bound=java.lang.Throwable)  # <X2>
    @typing.overload
    @staticmethod
    def propagateIfPossible(throwable: java.lang.Throwable) -> None: ...
    @typing.overload
    @staticmethod
    def propagateIfPossible(throwable: java.lang.Throwable, class_: typing.Type[_propagateIfPossible_1__X]) -> None: ...
    @typing.overload
    @staticmethod
    def propagateIfPossible(throwable: java.lang.Throwable, class_: typing.Type[_propagateIfPossible_2__X1], class2: typing.Type[_propagateIfPossible_2__X2]) -> None: ...
    _throwIfInstanceOf__X = typing.TypeVar('_throwIfInstanceOf__X', bound=java.lang.Throwable)  # <X>
    @staticmethod
    def throwIfInstanceOf(throwable: java.lang.Throwable, class_: typing.Type[_throwIfInstanceOf__X]) -> None: ...
    @staticmethod
    def throwIfUnchecked(throwable: java.lang.Throwable) -> None: ...

class Ticker:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src` extends Object
    
        A time source; returns a time value representing the number of nanoseconds elapsed since some fixed but arbitrary point
        in time. Note that most users should use :class:`~com.google.common.base.Stopwatch` instead of interacting with this
        class directly.
    
        **Warning:** this interface can only be used to measure elapsed time, not wall time.
    
        Since:
            10.0 (mostly source-compatible since 9.0)
    """
    def read(self) -> int: ...
    @staticmethod
    def systemTicker() -> 'Ticker': ...

class Utf8:
    """
    :class:`~com.google.common.annotations.Beta` :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public final class :meth:`~src` extends Object
    
        Low-level, high-performance utility methods related to the :meth:`~com.google.common.base.Charsets.UTF_8` character
        encoding. UTF-8 is defined in section D92 of `The Unicode Standard Core Specification, Chapter 3
        <http://www.unicode.org/versions/Unicode6.2.0/ch03.pdf>`.
    
        The variant of UTF-8 implemented by this class is the restricted definition of UTF-8 introduced in Unicode 3.1. One
        implication of this is that it rejects `"non-shortest form" <http://www.unicode.org/versions/corrigendum1.html>` byte
        sequences, even though the JDK decoder may accept them.
    
        Since:
            16.0
    """
    @staticmethod
    def encodedLength(charSequence: typing.Union[java.lang.CharSequence, str]) -> int: ...
    @typing.overload
    @staticmethod
    def isWellFormed(byteArray: typing.List[int]) -> bool: ...
    @typing.overload
    @staticmethod
    def isWellFormed(byteArray: typing.List[int], int: int, int2: int) -> bool: ...

class Verify:
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Static convenience methods that serve the same purpose as Java language assertions, except that they are always enabled.
        These methods should be used instead of Java assertions whenever there is a chance the check may fail "in real life".
        Example:
    
        .. code-block: java
        
         Bill bill = remoteService.getLastUnpaidBill();
        
         // In case bug 12345 happens again we'd rather just die
         Verify.verify(bill.status() == Status.UNPAID,
             "Unexpected bill status: %s", bill.status());
         
    
        Comparison to alternatives
    --------------------------
    
    
        **Note:** In some cases the differences explained below can be subtle. When it's unclear which approach to use, **don't
        worry** too much about it; just pick something that seems reasonable and it will be fine.
    
          - If checking whether the *caller* has violated your method or constructor's contract (such as by passing an invalid
            argument), use the utilities of the :class:`~com.google.common.base.Preconditions` class instead.
          - If checking an *impossible* condition (which *cannot* happen unless your own class or its *trusted* dependencies is
            badly broken), this is what ordinary Java assertions are for. Note that assertions are not enabled by default; they are
            essentially considered "compiled comments."
          - An explicit :code:`if/throw` (as illustrated below) is always acceptable; we still recommend using our
            :class:`~com.google.common.base.VerifyException` exception type. Throwing a plain null is frowned upon.
          - Use of null is generally discouraged, since :meth:`~com.google.common.base.Verify.verifyNotNull` and
            :meth:`~com.google.common.base.Preconditions.checkNotNull` perform the same function with more clarity.
    
    
        Warning about performance
    -------------------------
    
    
        Remember that parameter values for message construction must all be computed eagerly, and autoboxing and varargs array
        creation may happen as well, even when the verification succeeds and the message ends up unneeded. Performance-sensitive
        verification checks should continue to use usual form:
    
        .. code-block: java
        
         Bill bill = remoteService.getLastUnpaidBill();
         if (bill.status() != Status.UNPAID) {
           throw new VerifyException("Unexpected bill status: " + bill.status());
         }
         
    
        Only :code:`%s` is supported
    ----------------------------
    
    
        As with :class:`~com.google.common.base.Preconditions`, :code:`Verify` uses
        :meth:`~com.google.common.base.Strings.lenientFormat` to format error message template strings. This only supports the
        :code:`"%s"` specifier, not the full range of null specifiers. However, note that if the number of arguments does not
        match the number of occurrences of :code:`"%s"` in the format string, :code:`Verify` will still behave as expected, and
        will still include all argument values in the error message; the message will simply not be formatted exactly as
        intended.
    
        More information
    ----------------
    
        See Conditional failures explained in the Guava User Guide for advice on when this class should be used.
    
        Since:
            17.0
    """
    @typing.overload
    @staticmethod
    def verify(boolean: bool) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, char: str, char2: str) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, char: str, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, char: str, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, char: str, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, int: int, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, int: int, int2: int) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, int: int, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, int: int, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, object: typing.Any, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, object: typing.Any, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, object: typing.Any, object2: typing.Any, object3: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, object: typing.Any, object2: typing.Any, object3: typing.Any, object4: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, object: typing.Any, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, objectArray: typing.List[typing.Any]) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, long: int) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, long: int, char: str) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, long: int, int: int) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, long: int, object: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def verify(boolean: bool, string: str, long: int, long2: int) -> None: ...
    _verifyNotNull_0__T = typing.TypeVar('_verifyNotNull_0__T')  # <T>
    _verifyNotNull_1__T = typing.TypeVar('_verifyNotNull_1__T')  # <T>
    @typing.overload
    @staticmethod
    def verifyNotNull(t: _verifyNotNull_0__T) -> _verifyNotNull_0__T: ...
    @typing.overload
    @staticmethod
    def verifyNotNull(t: _verifyNotNull_1__T, string: str, objectArray: typing.List[typing.Any]) -> _verifyNotNull_1__T: ...

class VerifyException(java.lang.RuntimeException):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public class :meth:`~src` extends RuntimeException
    
        Exception thrown upon the failure of a verification check, including those performed by the convenience methods of the
        :class:`~com.google.common.base.Verify` class.
    
        Since:
            17.0
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class CharMatcher(Predicate[str]):
    """
    :class:`~com.google.common.annotations.GwtCompatible`(:meth:`~com.google.common.annotations.GwtCompatible.emulated`=true) public abstract class :meth:`~src` extends Object implements :class:`~com.google.common.base.Predicate`<Character>
    
        Determines a true or false value for any Java :code:`char` value, just as :class:`~com.google.common.base.Predicate`
        does for any null. Also offers basic text processing methods based on this function. Implementations are strongly
        encouraged to be side-effect-free and immutable.
    
        Throughout the documentation of this class, the phrase "matching character" is used to mean "any :code:`char` value
        :code:`c` for which :code:`this.matches(c)` returns :code:`true`".
    
        **Warning:** This class deals only with :code:`char` values, that is, `BMP characters
        <http://www.unicode.org/glossary/#BMP_character>`. It does not understand `supplementary Unicode code points
        <http://www.unicode.org/glossary/#supplementary_code_point>` in the range :code:`0x10000` to :code:`0x10FFFF` which
        includes the majority of assigned characters, including important CJK characters and emoji.
    
        Supplementary characters are null, and a :code:`CharMatcher` treats these just as two separate characters.
        :meth:`~com.google.common.base.CharMatcher.countIn` counts each supplementary character as 2 :code:`char`s.
    
        For up-to-date Unicode character properties (digit, letter, etc.) and support for supplementary code points, use ICU4J
        UCharacter and UnicodeSet (freeze() after building). For basic text processing based on UnicodeSet use the ICU4J
        UnicodeSetSpanner.
    
        Example usages:
    
        .. code-block: java
        
           String trimmed = :meth:`~com.google.common.base.CharMatcher.whitespace`.:meth:`~com.google.common.base.CharMatcher.trimFrom`(userInput);
           if (:meth:`~com.google.common.base.CharMatcher.ascii`.:meth:`~com.google.common.base.CharMatcher.matchesAllOf`(s)) { ... }
    
        See the Guava User Guide article on null.
    
        Since:
            1.0
    """
    @staticmethod
    def any() -> 'CharMatcher': ...
    @staticmethod
    def anyOf(charSequence: typing.Union[java.lang.CharSequence, str]) -> 'CharMatcher': ...
    def apply(self, character: str) -> bool: ...
    @staticmethod
    def ascii() -> 'CharMatcher': ...
    @staticmethod
    def breakingWhitespace() -> 'CharMatcher': ...
    def collapseFrom(self, charSequence: typing.Union[java.lang.CharSequence, str], char2: str) -> str: ...
    def countIn(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> int: ...
    @staticmethod
    def digit() -> 'CharMatcher': ...
    @staticmethod
    def forPredicate(predicate: typing.Union[Predicate[str], typing.Callable[[str], bool]]) -> 'CharMatcher': ...
    @staticmethod
    def inRange(char: str, char2: str) -> 'CharMatcher': ...
    @typing.overload
    def indexIn(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> int: ...
    @typing.overload
    def indexIn(self, charSequence: typing.Union[java.lang.CharSequence, str], int: int) -> int: ...
    @staticmethod
    def invisible() -> 'CharMatcher': ...
    @staticmethod
    def isNot(char: str) -> 'CharMatcher': ...
    @staticmethod
    def javaDigit() -> 'CharMatcher': ...
    @staticmethod
    def javaIsoControl() -> 'CharMatcher': ...
    @staticmethod
    def javaLetter() -> 'CharMatcher': ...
    @staticmethod
    def javaLetterOrDigit() -> 'CharMatcher': ...
    @staticmethod
    def javaLowerCase() -> 'CharMatcher': ...
    @staticmethod
    def javaUpperCase() -> 'CharMatcher': ...
    def lastIndexIn(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> int: ...
    def matches(self, char: str) -> bool: ...
    def matchesAllOf(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> bool: ...
    def matchesAnyOf(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> bool: ...
    def matchesNoneOf(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> bool: ...
    def negate(self) -> 'CharMatcher': ...
    @staticmethod
    def none() -> 'CharMatcher': ...
    @staticmethod
    def noneOf(charSequence: typing.Union[java.lang.CharSequence, str]) -> 'CharMatcher': ...
    def precomputed(self) -> 'CharMatcher': ...
    def removeFrom(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> str: ...
    @typing.overload
    def replaceFrom(self, charSequence: typing.Union[java.lang.CharSequence, str], char2: str) -> str: ...
    @typing.overload
    def replaceFrom(self, charSequence: typing.Union[java.lang.CharSequence, str], charSequence2: typing.Union[java.lang.CharSequence, str]) -> str: ...
    def retainFrom(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> str: ...
    @staticmethod
    def singleWidth() -> 'CharMatcher': ...
    def toString(self) -> str: ...
    def trimAndCollapseFrom(self, charSequence: typing.Union[java.lang.CharSequence, str], char2: str) -> str: ...
    def trimFrom(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> str: ...
    def trimLeadingFrom(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> str: ...
    def trimTrailingFrom(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> str: ...
    @staticmethod
    def whitespace() -> 'CharMatcher': ...

_Converter__A = typing.TypeVar('_Converter__A')  # <A>
_Converter__B = typing.TypeVar('_Converter__B')  # <B>
class Converter(Function[_Converter__A, _Converter__B], typing.Generic[_Converter__A, _Converter__B]):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public abstract class :meth:`~src`<A, B> extends Object implements :class:`~com.google.common.base.Function`<A, B>
    
        A function from :code:`A` to :code:`B` with an associated *reverse* function from :code:`B` to :code:`A`; used for
        converting back and forth between *different representations of the same information*.
    
        Invertibility
    -------------
    
    
        The reverse operation **may** be a strict *inverse* (meaning that
        :code:`converter.reverse().convert(converter.convert(a)).equals(a)` is always true). However, it is very common (perhaps
        *more* common) for round-trip conversion to be *lossy*. Consider an example round-trip using
        :meth:`~com.google.common.primitives.Doubles.stringConverter`:
    
          1.  :code:`stringConverter().convert("1.00")` returns the :code:`Double` value :code:`1.0`
          2.  :code:`stringConverter().reverse().convert(1.0)` returns the string :code:`"1.0"` -- *not* the same string
            (:code:`"1.00"`) we started with
    
    
        Note that it should still be the case that the round-tripped and original objects are *similar*.
    
        Nullability
    -----------
    
    
        A converter always converts :code:`null` to :code:`null` and non-null references to non-null references. It would not
        make sense to consider :code:`null` and a non-null reference to be "different representations of the same information",
        since one is distinguishable from *missing* information and the other is not. The
        :meth:`~com.google.common.base.Converter.convert` method handles this null behavior for all converters; implementations
        of :meth:`~com.google.common.base.Converter.doForward` and :meth:`~com.google.common.base.Converter.doBackward` are
        guaranteed to never be passed :code:`null`, and must never return :code:`null`.
    
        Common ways to use
    ------------------
    
    
        Getting a converter:
    
          - Use a provided converter implementation, such as :meth:`~com.google.common.base.Enums.stringConverter`,
            :meth:`~com.google.common.primitives.Ints.stringConverter` or the :meth:`~com.google.common.base.Converter.reverse`
            views of these.
          - Convert between specific preset values using :meth:`~com.google.common.collect.Maps.asConverter`. For example, use this
            to create a "fake" converter for a unit test. It is unnecessary (and confusing) to *mock* the :code:`Converter` type
            using a mocking framework.
          - Extend this class and implement its :meth:`~com.google.common.base.Converter.doForward` and
            :meth:`~com.google.common.base.Converter.doBackward` methods.
          - **Java 8 users:** you may prefer to pass two lambda expressions or method references to the
            :meth:`~com.google.common.base.Converter.from` factory method.
    
    
        Using a converter:
    
          - Convert one instance in the "forward" direction using :code:`converter.convert(a)`.
          - Convert multiple instances "forward" using :code:`converter.convertAll(as)`.
          - Convert in the "backward" direction using :code:`converter.reverse().convert(b)` or
            :code:`converter.reverse().convertAll(bs)`.
          - Use :code:`converter` or :code:`converter.reverse()` anywhere a null is accepted (for example null).
          - **Do not** call :meth:`~com.google.common.base.Converter.doForward` or
            :meth:`~com.google.common.base.Converter.doBackward` directly; these exist only to be overridden.
    
    
        Example
    -------
    
    
        .. code-block: java
        
           return new Converter<Integer, String>() {
             protected String doForward(Integer i) {
               return Integer.toHexString(i);
             }
        
             protected Integer doBackward(String s) {
               return parseUnsignedInt(s, 16);
             }
           };
    
        An alternative using Java 8:
    
        .. code-block: java
        
         return Converter.from(
             Integer::toHexString,
             s -> parseUnsignedInt(s, 16));
         
    
        Since:
            16.0
    """
    _andThen_0__V = typing.TypeVar('_andThen_0__V')  # <V>
    _andThen_1__C = typing.TypeVar('_andThen_1__C')  # <C>
    @typing.overload
    def andThen(self, function: typing.Union[java.util.function.Function[typing.Any, _andThen_0__V], typing.Callable[[typing.Any], _andThen_0__V]]) -> java.util.function.Function[typing.Any, _andThen_0__V]: ...
    @typing.overload
    def andThen(self, converter: 'Converter'[_Converter__B, _andThen_1__C]) -> 'Converter'[_Converter__A, _andThen_1__C]: ...
    def apply(self, a: _Converter__A) -> _Converter__B: ...
    def convert(self, a: _Converter__A) -> _Converter__B: ...
    def convertAll(self, iterable: java.lang.Iterable[_Converter__A]) -> java.lang.Iterable[_Converter__B]: ...
    def equals(self, object: typing.Any) -> bool: ...
    _identity__T = typing.TypeVar('_identity__T')  # <T>
    @staticmethod
    def identity() -> 'Converter'[_identity__T, _identity__T]: ...
    def reverse(self) -> 'Converter'[_Converter__B, _Converter__A]: ...

_FinalizablePhantomReference__T = typing.TypeVar('_FinalizablePhantomReference__T')  # <T>
class FinalizablePhantomReference(java.lang.ref.PhantomReference[_FinalizablePhantomReference__T], FinalizableReference, typing.Generic[_FinalizablePhantomReference__T]):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public abstract class :meth:`~src`<T> extends PhantomReference<T> implements :class:`~com.google.common.base.FinalizableReference`
    
        Phantom reference with a :code:`finalizeReferent()` method which a background thread invokes after the garbage collector
        reclaims the referent. This is a simpler alternative to using a null.
    
        Unlike a normal phantom reference, this reference will be cleared automatically.
    
        Since:
            2.0
    """
    ...

_FinalizableSoftReference__T = typing.TypeVar('_FinalizableSoftReference__T')  # <T>
class FinalizableSoftReference(java.lang.ref.SoftReference[_FinalizableSoftReference__T], FinalizableReference, typing.Generic[_FinalizableSoftReference__T]):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public abstract class :meth:`~src`<T> extends SoftReference<T> implements :class:`~com.google.common.base.FinalizableReference`
    
        Soft reference with a :code:`finalizeReferent()` method which a background thread invokes after the garbage collector
        reclaims the referent. This is a simpler alternative to using a null.
    
        Since:
            2.0
    """
    ...

_FinalizableWeakReference__T = typing.TypeVar('_FinalizableWeakReference__T')  # <T>
class FinalizableWeakReference(java.lang.ref.WeakReference[_FinalizableWeakReference__T], FinalizableReference, typing.Generic[_FinalizableWeakReference__T]):
    """
    :class:`~com.google.common.annotations.GwtIncompatible` public abstract class :meth:`~src`<T> extends WeakReference<T> implements :class:`~com.google.common.base.FinalizableReference`
    
        Weak reference with a :code:`finalizeReferent()` method which a background thread invokes after the garbage collector
        reclaims the referent. This is a simpler alternative to using a null.
    
        Since:
            2.0
    """
    ...

class Objects(com.google.common.base.ExtraObjectsMethodsForWeb):
    """
    :class:`~com.google.common.annotations.GwtCompatible` public final class :meth:`~src` extends Object
    
        Helper functions that can operate on any :code:`Object`.
    
        See the Guava User Guide on null.
    
        Since:
            2.0
    """
    @staticmethod
    def equal(object: typing.Any, object2: typing.Any) -> bool: ...
    @typing.overload
    def hashCode(self) -> int: ...
    @typing.overload
    @staticmethod
    def hashCode(objectArray: typing.List[typing.Any]) -> int: ...

class ExtraObjectsMethodsForWeb: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("com.google.common.base")``.

    Ascii: typing.Type[Ascii]
    CaseFormat: typing.Type[CaseFormat]
    CharMatcher: typing.Type[CharMatcher]
    Charsets: typing.Type[Charsets]
    Converter: typing.Type[Converter]
    Defaults: typing.Type[Defaults]
    Enums: typing.Type[Enums]
    Equivalence: typing.Type[Equivalence]
    ExtraObjectsMethodsForWeb: typing.Type[ExtraObjectsMethodsForWeb]
    FinalizablePhantomReference: typing.Type[FinalizablePhantomReference]
    FinalizableReference: typing.Type[FinalizableReference]
    FinalizableReferenceQueue: typing.Type[FinalizableReferenceQueue]
    FinalizableSoftReference: typing.Type[FinalizableSoftReference]
    FinalizableWeakReference: typing.Type[FinalizableWeakReference]
    Function: typing.Type[Function]
    Functions: typing.Type[Functions]
    Joiner: typing.Type[Joiner]
    MoreObjects: typing.Type[MoreObjects]
    Objects: typing.Type[Objects]
    Optional: typing.Type[Optional]
    Preconditions: typing.Type[Preconditions]
    Predicate: typing.Type[Predicate]
    Predicates: typing.Type[Predicates]
    Splitter: typing.Type[Splitter]
    StandardSystemProperty: typing.Type[StandardSystemProperty]
    Stopwatch: typing.Type[Stopwatch]
    Strings: typing.Type[Strings]
    Supplier: typing.Type[Supplier]
    Suppliers: typing.Type[Suppliers]
    Throwables: typing.Type[Throwables]
    Ticker: typing.Type[Ticker]
    Utf8: typing.Type[Utf8]
    Verify: typing.Type[Verify]
    VerifyException: typing.Type[VerifyException]
    internal: com.google.common.base.internal.__module_protocol__
