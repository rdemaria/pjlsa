import java.lang
import typing



class BEAM_TYPE(java.lang.Enum['BEAM_TYPE']):
    """
    Java class 'cern.lsa.domain.cern.timing.enums.BEAM_TYPE'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        INTERMEDIATE (cern.lsa.domain.cern.timing.enums.BEAM_TYPE): final static enum constant
        NOMINAL (cern.lsa.domain.cern.timing.enums.BEAM_TYPE): final static enum constant
    
    """
    INTERMEDIATE: typing.ClassVar['BEAM_TYPE'] = ...
    NOMINAL: typing.ClassVar['BEAM_TYPE'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'BEAM_TYPE': ...
    def getFesaValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'BEAM_TYPE': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['BEAM_TYPE']: ...

class INJECTION_STATUS(java.lang.Enum['INJECTION_STATUS']):
    """
    Java class 'cern.lsa.domain.cern.timing.enums.INJECTION_STATUS'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        NO_REQUEST (cern.lsa.domain.cern.timing.enums.INJECTION_STATUS): final static enum constant
        PENDING (cern.lsa.domain.cern.timing.enums.INJECTION_STATUS): final static enum constant
        FAILED (cern.lsa.domain.cern.timing.enums.INJECTION_STATUS): final static enum constant
        SUCCEDED (cern.lsa.domain.cern.timing.enums.INJECTION_STATUS): final static enum constant
    
    """
    NO_REQUEST: typing.ClassVar['INJECTION_STATUS'] = ...
    PENDING: typing.ClassVar['INJECTION_STATUS'] = ...
    FAILED: typing.ClassVar['INJECTION_STATUS'] = ...
    SUCCEDED: typing.ClassVar['INJECTION_STATUS'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'INJECTION_STATUS': ...
    def getFesaValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'INJECTION_STATUS': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['INJECTION_STATUS']: ...

class MASTER_STATUS(java.lang.Enum['MASTER_STATUS']):
    """
    Java class 'cern.lsa.domain.cern.timing.enums.MASTER_STATUS'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        NO (cern.lsa.domain.cern.timing.enums.MASTER_STATUS): final static enum constant
        PENDING (cern.lsa.domain.cern.timing.enums.MASTER_STATUS): final static enum constant
        YES (cern.lsa.domain.cern.timing.enums.MASTER_STATUS): final static enum constant
    
    """
    NO: typing.ClassVar['MASTER_STATUS'] = ...
    PENDING: typing.ClassVar['MASTER_STATUS'] = ...
    YES: typing.ClassVar['MASTER_STATUS'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'MASTER_STATUS': ...
    def getFesaValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'MASTER_STATUS': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['MASTER_STATUS']: ...

class PARTICLE_TYPE(java.lang.Enum['PARTICLE_TYPE']):
    """
    Java class 'cern.lsa.domain.cern.timing.enums.PARTICLE_TYPE'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        PROTON (cern.lsa.domain.cern.timing.enums.PARTICLE_TYPE): final static enum constant
        PB82 (cern.lsa.domain.cern.timing.enums.PARTICLE_TYPE): final static enum constant
        AR18 (cern.lsa.domain.cern.timing.enums.PARTICLE_TYPE): final static enum constant
        D (cern.lsa.domain.cern.timing.enums.PARTICLE_TYPE): final static enum constant
        XE54 (cern.lsa.domain.cern.timing.enums.PARTICLE_TYPE): final static enum constant
    
    """
    PROTON: typing.ClassVar['PARTICLE_TYPE'] = ...
    PB82: typing.ClassVar['PARTICLE_TYPE'] = ...
    AR18: typing.ClassVar['PARTICLE_TYPE'] = ...
    D: typing.ClassVar['PARTICLE_TYPE'] = ...
    XE54: typing.ClassVar['PARTICLE_TYPE'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'PARTICLE_TYPE': ...
    def getValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PARTICLE_TYPE': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['PARTICLE_TYPE']: ...

class RNGI(java.lang.Enum['RNGI']):
    """
    Java class 'cern.lsa.domain.cern.timing.enums.RNGI'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        NORING (cern.lsa.domain.cern.timing.enums.RNGI): final static enum constant
        RING_1 (cern.lsa.domain.cern.timing.enums.RNGI): final static enum constant
        RING_2 (cern.lsa.domain.cern.timing.enums.RNGI): final static enum constant
    
    """
    NORING: typing.ClassVar['RNGI'] = ...
    RING_1: typing.ClassVar['RNGI'] = ...
    RING_2: typing.ClassVar['RNGI'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'RNGI': ...
    def getValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'RNGI': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['RNGI']: ...

class TABLE_STATUS_HW(java.lang.Enum['TABLE_STATUS_HW']):
    """
    Java class 'cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        INVALID (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW): final static enum constant
        ILLEGAL_OP_CODE (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW): final static enum constant
        ILLEGAL_VALUE (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW): final static enum constant
        ILLEGAL_REGISTER (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW): final static enum constant
        WAITING (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW): final static enum constant
        STOPPED (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW): final static enum constant
        RUNNING (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW): final static enum constant
    
    """
    INVALID: typing.ClassVar['TABLE_STATUS_HW'] = ...
    ILLEGAL_OP_CODE: typing.ClassVar['TABLE_STATUS_HW'] = ...
    ILLEGAL_VALUE: typing.ClassVar['TABLE_STATUS_HW'] = ...
    ILLEGAL_REGISTER: typing.ClassVar['TABLE_STATUS_HW'] = ...
    WAITING: typing.ClassVar['TABLE_STATUS_HW'] = ...
    STOPPED: typing.ClassVar['TABLE_STATUS_HW'] = ...
    RUNNING: typing.ClassVar['TABLE_STATUS_HW'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'TABLE_STATUS_HW': ...
    def getFesaValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TABLE_STATUS_HW': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['TABLE_STATUS_HW']: ...

class TABLE_STATUS_SW(java.lang.Enum['TABLE_STATUS_SW']):
    """
    Java class 'cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        INVALID (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW): final static enum constant
        CRASHED (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW): final static enum constant
        WAIT_PARA (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW): final static enum constant
        WAIT_TRIG (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW): final static enum constant
        RUNNING (cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW): final static enum constant
    
    """
    INVALID: typing.ClassVar['TABLE_STATUS_SW'] = ...
    CRASHED: typing.ClassVar['TABLE_STATUS_SW'] = ...
    WAIT_PARA: typing.ClassVar['TABLE_STATUS_SW'] = ...
    WAIT_TRIG: typing.ClassVar['TABLE_STATUS_SW'] = ...
    RUNNING: typing.ClassVar['TABLE_STATUS_SW'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'TABLE_STATUS_SW': ...
    def getFesaValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TABLE_STATUS_SW': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['TABLE_STATUS_SW']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.timing.enums")``.

    BEAM_TYPE: typing.Type[BEAM_TYPE]
    INJECTION_STATUS: typing.Type[INJECTION_STATUS]
    MASTER_STATUS: typing.Type[MASTER_STATUS]
    PARTICLE_TYPE: typing.Type[PARTICLE_TYPE]
    RNGI: typing.Type[RNGI]
    TABLE_STATUS_HW: typing.Type[TABLE_STATUS_HW]
    TABLE_STATUS_SW: typing.Type[TABLE_STATUS_SW]
