import java.nio.charset
import java.util


class CharsetProvider:
    def charsetForName(self, string: str) -> java.nio.charset.Charset: ...
    def charsets(self) -> java.util.Iterator[java.nio.charset.Charset]: ...
