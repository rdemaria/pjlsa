import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.modes
import cern.accsoft.commons.util
import java.lang
import java.util
import typing



class Beam(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.accsoft.commons.domain.beams.Beam'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator: ...
    def getBeamNumber(self) -> int: ...

class AdBeam(java.lang.Enum['AdBeam'], Beam):
    """
    Java class 'cern.accsoft.commons.domain.beams.AdBeam'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.domain.beams.Beam
    
      Attributes:
        BEAM1 (cern.accsoft.commons.domain.beams.AdBeam): final static enum constant
    
    """
    BEAM1: typing.ClassVar['AdBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'AdBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def getBeamNumber(self) -> int: ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AdBeam': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['AdBeam']: ...

class AwakeBeam(java.lang.Enum['AwakeBeam'], Beam):
    """
    Java class 'cern.accsoft.commons.domain.beams.AwakeBeam'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.domain.beams.Beam
    
      Attributes:
        BEAM1 (cern.accsoft.commons.domain.beams.AwakeBeam): final static enum constant
    
    """
    BEAM1: typing.ClassVar['AwakeBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'AwakeBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def getBeamNumber(self) -> int: ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AwakeBeam': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['AwakeBeam']: ...

class ElenaBeam(java.lang.Enum['ElenaBeam'], Beam):
    """
    Java class 'cern.accsoft.commons.domain.beams.ElenaBeam'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.domain.beams.Beam
    
      Attributes:
        BEAM1 (cern.accsoft.commons.domain.beams.ElenaBeam): final static enum constant
    
    """
    BEAM1: typing.ClassVar['ElenaBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'ElenaBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def getBeamNumber(self) -> int: ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ElenaBeam': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['ElenaBeam']: ...

class IsoldeBeam(java.lang.Enum['IsoldeBeam'], Beam):
    """
    Java class 'cern.accsoft.commons.domain.beams.IsoldeBeam'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.domain.beams.Beam
    
      Attributes:
        BEAM1 (cern.accsoft.commons.domain.beams.IsoldeBeam): final static enum constant
    
    """
    BEAM1: typing.ClassVar['IsoldeBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'IsoldeBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def getBeamNumber(self) -> int: ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'IsoldeBeam': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['IsoldeBeam']: ...

class LeirBeam(java.lang.Enum['LeirBeam'], Beam):
    """
    Java class 'cern.accsoft.commons.domain.beams.LeirBeam'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.domain.beams.Beam
    
      Attributes:
        BEAM1 (cern.accsoft.commons.domain.beams.LeirBeam): final static enum constant
    
    """
    BEAM1: typing.ClassVar['LeirBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'LeirBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def getBeamNumber(self) -> int: ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LeirBeam': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['LeirBeam']: ...

class LhcBeam(java.lang.Enum['LhcBeam'], Beam):
    """
    Java class 'cern.accsoft.commons.domain.beams.LhcBeam'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.domain.beams.Beam
    
      Attributes:
        BEAM1 (cern.accsoft.commons.domain.beams.LhcBeam): final static enum constant
        BEAM2 (cern.accsoft.commons.domain.beams.LhcBeam): final static enum constant
    
    """
    BEAM1: typing.ClassVar['LhcBeam'] = ...
    BEAM2: typing.ClassVar['LhcBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'LhcBeam': ...
    @staticmethod
    def fromNonStandardName(string: str) -> 'LhcBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def getBeamModes(self) -> java.util.Set[cern.accsoft.commons.domain.modes.LhcBeamMode]: ...
    def getBeamNumber(self) -> int: ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LhcBeam': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['LhcBeam']: ...

class PsBeam(java.lang.Enum['PsBeam'], Beam):
    """
    Java class 'cern.accsoft.commons.domain.beams.PsBeam'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.domain.beams.Beam
    
      Attributes:
        BEAM1 (cern.accsoft.commons.domain.beams.PsBeam): final static enum constant
    
    """
    BEAM1: typing.ClassVar['PsBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'PsBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def getBeamNumber(self) -> int: ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PsBeam': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['PsBeam']: ...

class PsbBeam(java.lang.Enum['PsbBeam'], Beam):
    """
    Java class 'cern.accsoft.commons.domain.beams.PsbBeam'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.domain.beams.Beam
    
      Attributes:
        BEAM1 (cern.accsoft.commons.domain.beams.PsbBeam): final static enum constant
        BEAM2 (cern.accsoft.commons.domain.beams.PsbBeam): final static enum constant
        BEAM3 (cern.accsoft.commons.domain.beams.PsbBeam): final static enum constant
        BEAM4 (cern.accsoft.commons.domain.beams.PsbBeam): final static enum constant
    
    """
    BEAM1: typing.ClassVar['PsbBeam'] = ...
    BEAM2: typing.ClassVar['PsbBeam'] = ...
    BEAM3: typing.ClassVar['PsbBeam'] = ...
    BEAM4: typing.ClassVar['PsbBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'PsbBeam': ...
    @staticmethod
    def fromNonStandardName(string: str) -> 'PsbBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def getBeamNumber(self) -> int: ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PsbBeam': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['PsbBeam']: ...

class SpsBeam(java.lang.Enum['SpsBeam'], Beam):
    """
    Java class 'cern.accsoft.commons.domain.beams.SpsBeam'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.domain.beams.Beam
    
      Attributes:
        BEAM1 (cern.accsoft.commons.domain.beams.SpsBeam): final static enum constant
    
    """
    BEAM1: typing.ClassVar['SpsBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'SpsBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator: ...
    def getBeamNumber(self) -> int: ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SpsBeam': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['SpsBeam']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.beams")``.

    AdBeam: typing.Type[AdBeam]
    AwakeBeam: typing.Type[AwakeBeam]
    Beam: typing.Type[Beam]
    ElenaBeam: typing.Type[ElenaBeam]
    IsoldeBeam: typing.Type[IsoldeBeam]
    LeirBeam: typing.Type[LeirBeam]
    LhcBeam: typing.Type[LhcBeam]
    PsBeam: typing.Type[PsBeam]
    PsbBeam: typing.Type[PsbBeam]
    SpsBeam: typing.Type[SpsBeam]
