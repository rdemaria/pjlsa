import java.io
import java.lang
import java.nio
import java.nio.charset.spi
import java.util
import typing



class CharacterCodingException(java.io.IOException):
    def __init__(self): ...

class Charset(java.lang.Comparable['Charset']):
    def aliases(self) -> java.util.Set[str]: ...
    @staticmethod
    def availableCharsets() -> java.util.SortedMap[str, 'Charset']: ...
    def canEncode(self) -> bool: ...
    def compareTo(self, charset: 'Charset') -> int: ...
    def contains(self, charset: 'Charset') -> bool: ...
    def decode(self, byteBuffer: java.nio.ByteBuffer) -> java.nio.CharBuffer: ...
    @staticmethod
    def defaultCharset() -> 'Charset': ...
    @typing.overload
    def displayName(self) -> str: ...
    @typing.overload
    def displayName(self, locale: java.util.Locale) -> str: ...
    @typing.overload
    def encode(self, string: str) -> java.nio.ByteBuffer: ...
    @typing.overload
    def encode(self, charBuffer: java.nio.CharBuffer) -> java.nio.ByteBuffer: ...
    def equals(self, object: typing.Any) -> bool: ...
    @staticmethod
    def forName(string: str) -> 'Charset': ...
    def hashCode(self) -> int: ...
    def isRegistered(self) -> bool: ...
    @staticmethod
    def isSupported(string: str) -> bool: ...
    def name(self) -> str: ...
    def newDecoder(self) -> 'CharsetDecoder': ...
    def newEncoder(self) -> 'CharsetEncoder': ...
    def toString(self) -> str: ...

class CharsetDecoder:
    def averageCharsPerByte(self) -> float: ...
    def charset(self) -> Charset: ...
    @typing.overload
    def decode(self, byteBuffer: java.nio.ByteBuffer) -> java.nio.CharBuffer: ...
    @typing.overload
    def decode(self, byteBuffer: java.nio.ByteBuffer, charBuffer: java.nio.CharBuffer, boolean: bool) -> 'CoderResult': ...
    def detectedCharset(self) -> Charset: ...
    def flush(self, charBuffer: java.nio.CharBuffer) -> 'CoderResult': ...
    def isAutoDetecting(self) -> bool: ...
    def isCharsetDetected(self) -> bool: ...
    def malformedInputAction(self) -> 'CodingErrorAction': ...
    def maxCharsPerByte(self) -> float: ...
    def onMalformedInput(self, codingErrorAction: 'CodingErrorAction') -> 'CharsetDecoder': ...
    def onUnmappableCharacter(self, codingErrorAction: 'CodingErrorAction') -> 'CharsetDecoder': ...
    def replaceWith(self, string: str) -> 'CharsetDecoder': ...
    def replacement(self) -> str: ...
    def reset(self) -> 'CharsetDecoder': ...
    def unmappableCharacterAction(self) -> 'CodingErrorAction': ...

class CharsetEncoder:
    def averageBytesPerChar(self) -> float: ...
    @typing.overload
    def canEncode(self, char: str) -> bool: ...
    @typing.overload
    def canEncode(self, charSequence: typing.Union[java.lang.CharSequence, str]) -> bool: ...
    def charset(self) -> Charset: ...
    @typing.overload
    def encode(self, charBuffer: java.nio.CharBuffer) -> java.nio.ByteBuffer: ...
    @typing.overload
    def encode(self, charBuffer: java.nio.CharBuffer, byteBuffer: java.nio.ByteBuffer, boolean: bool) -> 'CoderResult': ...
    def flush(self, byteBuffer: java.nio.ByteBuffer) -> 'CoderResult': ...
    def isLegalReplacement(self, byteArray: typing.List[int]) -> bool: ...
    def malformedInputAction(self) -> 'CodingErrorAction': ...
    def maxBytesPerChar(self) -> float: ...
    def onMalformedInput(self, codingErrorAction: 'CodingErrorAction') -> 'CharsetEncoder': ...
    def onUnmappableCharacter(self, codingErrorAction: 'CodingErrorAction') -> 'CharsetEncoder': ...
    def replaceWith(self, byteArray: typing.List[int]) -> 'CharsetEncoder': ...
    def replacement(self) -> typing.List[int]: ...
    def reset(self) -> 'CharsetEncoder': ...
    def unmappableCharacterAction(self) -> 'CodingErrorAction': ...

class CoderMalfunctionError(java.lang.Error):
    def __init__(self, exception: java.lang.Exception): ...

class CoderResult:
    UNDERFLOW: typing.ClassVar['CoderResult'] = ...
    OVERFLOW: typing.ClassVar['CoderResult'] = ...
    def isError(self) -> bool: ...
    def isMalformed(self) -> bool: ...
    def isOverflow(self) -> bool: ...
    def isUnderflow(self) -> bool: ...
    def isUnmappable(self) -> bool: ...
    def length(self) -> int: ...
    @staticmethod
    def malformedForLength(int: int) -> 'CoderResult': ...
    def throwException(self) -> None: ...
    def toString(self) -> str: ...
    @staticmethod
    def unmappableForLength(int: int) -> 'CoderResult': ...

class CodingErrorAction:
    IGNORE: typing.ClassVar['CodingErrorAction'] = ...
    REPLACE: typing.ClassVar['CodingErrorAction'] = ...
    REPORT: typing.ClassVar['CodingErrorAction'] = ...
    def toString(self) -> str: ...

class IllegalCharsetNameException(java.lang.IllegalArgumentException):
    def __init__(self, string: str): ...
    def getCharsetName(self) -> str: ...

class StandardCharsets:
    US_ASCII: typing.ClassVar[Charset] = ...
    ISO_8859_1: typing.ClassVar[Charset] = ...
    UTF_8: typing.ClassVar[Charset] = ...
    UTF_16BE: typing.ClassVar[Charset] = ...
    UTF_16LE: typing.ClassVar[Charset] = ...
    UTF_16: typing.ClassVar[Charset] = ...

class UnsupportedCharsetException(java.lang.IllegalArgumentException):
    def __init__(self, string: str): ...
    def getCharsetName(self) -> str: ...

class MalformedInputException(CharacterCodingException):
    def __init__(self, int: int): ...
    def getInputLength(self) -> int: ...
    def getMessage(self) -> str: ...

class UnmappableCharacterException(CharacterCodingException):
    def __init__(self, int: int): ...
    def getInputLength(self) -> int: ...
    def getMessage(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.nio.charset")``.

    CharacterCodingException: typing.Type[CharacterCodingException]
    Charset: typing.Type[Charset]
    CharsetDecoder: typing.Type[CharsetDecoder]
    CharsetEncoder: typing.Type[CharsetEncoder]
    CoderMalfunctionError: typing.Type[CoderMalfunctionError]
    CoderResult: typing.Type[CoderResult]
    CodingErrorAction: typing.Type[CodingErrorAction]
    IllegalCharsetNameException: typing.Type[IllegalCharsetNameException]
    MalformedInputException: typing.Type[MalformedInputException]
    StandardCharsets: typing.Type[StandardCharsets]
    UnmappableCharacterException: typing.Type[UnmappableCharacterException]
    UnsupportedCharsetException: typing.Type[UnsupportedCharsetException]
    spi: java.nio.charset.spi.__module_protocol__
