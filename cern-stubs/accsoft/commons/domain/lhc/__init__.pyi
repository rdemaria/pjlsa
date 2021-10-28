import cern.accsoft.commons.util
import java.lang
import typing



class LhcExperiment(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LhcExperiment']):
    """
    Java class 'cern.accsoft.commons.domain.lhc.LhcExperiment'
    
        Extends:
            cern.accsoft.commons.util.AbstractImmutableNamedSerializable
    
      Attributes:
        ATLAS (cern.accsoft.commons.domain.lhc.LhcExperiment): final static field
        ALICE (cern.accsoft.commons.domain.lhc.LhcExperiment): final static field
        CMS (cern.accsoft.commons.domain.lhc.LhcExperiment): final static field
        LHCB (cern.accsoft.commons.domain.lhc.LhcExperiment): final static field
        LHCF (cern.accsoft.commons.domain.lhc.LhcExperiment): final static field
        TOTEM (cern.accsoft.commons.domain.lhc.LhcExperiment): final static field
    
    """
    ATLAS: typing.ClassVar['LhcExperiment'] = ...
    ALICE: typing.ClassVar['LhcExperiment'] = ...
    CMS: typing.ClassVar['LhcExperiment'] = ...
    LHCB: typing.ClassVar['LhcExperiment'] = ...
    LHCF: typing.ClassVar['LhcExperiment'] = ...
    TOTEM: typing.ClassVar['LhcExperiment'] = ...
    @staticmethod
    def valueOf(string: str) -> 'LhcExperiment': ...
    @staticmethod
    def values() -> typing.List['LhcExperiment']: ...

class LhcInteractionPoint(java.lang.Enum['LhcInteractionPoint'], cern.accsoft.commons.util.Named):
    """
    Java class 'cern.accsoft.commons.domain.lhc.LhcInteractionPoint'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
      Attributes:
        LHC_IP1 (cern.accsoft.commons.domain.lhc.LhcInteractionPoint): final static enum constant
        LHC_IP2 (cern.accsoft.commons.domain.lhc.LhcInteractionPoint): final static enum constant
        LHC_IP3 (cern.accsoft.commons.domain.lhc.LhcInteractionPoint): final static enum constant
        LHC_IP4 (cern.accsoft.commons.domain.lhc.LhcInteractionPoint): final static enum constant
        LHC_IP5 (cern.accsoft.commons.domain.lhc.LhcInteractionPoint): final static enum constant
        LHC_IP6 (cern.accsoft.commons.domain.lhc.LhcInteractionPoint): final static enum constant
        LHC_IP7 (cern.accsoft.commons.domain.lhc.LhcInteractionPoint): final static enum constant
        LHC_IP8 (cern.accsoft.commons.domain.lhc.LhcInteractionPoint): final static enum constant
    
    """
    LHC_IP1: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP2: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP3: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP4: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP5: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP6: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP7: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP8: typing.ClassVar['LhcInteractionPoint'] = ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LhcInteractionPoint': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['LhcInteractionPoint']: ...

class LhcSector(java.lang.Enum['LhcSector'], cern.accsoft.commons.util.Named):
    """
    Java class 'cern.accsoft.commons.domain.lhc.LhcSector'
    
        Extends:
            java.lang.Enum
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
      Attributes:
        SECTOR_12 (cern.accsoft.commons.domain.lhc.LhcSector): final static enum constant
        SECTOR_23 (cern.accsoft.commons.domain.lhc.LhcSector): final static enum constant
        SECTOR_34 (cern.accsoft.commons.domain.lhc.LhcSector): final static enum constant
        SECTOR_45 (cern.accsoft.commons.domain.lhc.LhcSector): final static enum constant
        SECTOR_56 (cern.accsoft.commons.domain.lhc.LhcSector): final static enum constant
        SECTOR_67 (cern.accsoft.commons.domain.lhc.LhcSector): final static enum constant
        SECTOR_78 (cern.accsoft.commons.domain.lhc.LhcSector): final static enum constant
        SECTOR_81 (cern.accsoft.commons.domain.lhc.LhcSector): final static enum constant
    
    """
    SECTOR_12: typing.ClassVar['LhcSector'] = ...
    SECTOR_23: typing.ClassVar['LhcSector'] = ...
    SECTOR_34: typing.ClassVar['LhcSector'] = ...
    SECTOR_45: typing.ClassVar['LhcSector'] = ...
    SECTOR_56: typing.ClassVar['LhcSector'] = ...
    SECTOR_67: typing.ClassVar['LhcSector'] = ...
    SECTOR_78: typing.ClassVar['LhcSector'] = ...
    SECTOR_81: typing.ClassVar['LhcSector'] = ...
    def getName(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LhcSector': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['LhcSector']: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.lhc")``.

    LhcExperiment: typing.Type[LhcExperiment]
    LhcInteractionPoint: typing.Type[LhcInteractionPoint]
    LhcSector: typing.Type[LhcSector]
