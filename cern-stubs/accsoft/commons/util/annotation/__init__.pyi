import java.lang.annotation
import typing



class EverythingIsNonnullByDefault(java.lang.annotation.Annotation):
    """
    Java class 'cern.accsoft.commons.util.annotation.EverythingIsNonnullByDefault'
    
        Interfaces:
            java.lang.annotation.Annotation
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.annotation")``.

    EverythingIsNonnullByDefault: typing.Type[EverythingIsNonnullByDefault]
