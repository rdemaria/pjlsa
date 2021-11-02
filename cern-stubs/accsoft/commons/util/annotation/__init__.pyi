import java.lang.annotation
import typing



class EverythingIsNonnullByDefault(java.lang.annotation.Annotation):
    """
    `@Nonnull <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/annotation/Nonnull.html?is-external=true>` @TypeQualifierDefault({`PARAMETER <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/annotation/ElementType.html?is-external=true#PARAMETER>`,`METHOD <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/annotation/ElementType.html?is-external=true#METHOD>`}) `@Retention <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/annotation/Retention.html?is-external=true>`(`RUNTIME <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/annotation/RetentionPolicy.html?is-external=true#RUNTIME>`) public @interface EverythingIsNonnullByDefault
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.annotation")``.

    EverythingIsNonnullByDefault: typing.Type[EverythingIsNonnullByDefault]
