import cern.accsoft.commons.util
import java.lang
import typing



class LhcExperiment(cern.accsoft.commons.util.AbstractImmutableNamedSerializable['LhcExperiment']):
    """
    public class LhcExperiment extends cern.accsoft.commons.util.AbstractImmutableNamedSerializable<:class:`~cern.accsoft.commons.domain.lhc.LhcExperiment`>
    
        LHC experiments.
    
        Also see:
            :meth:`~serialized`
    """
    ATLAS: typing.ClassVar['LhcExperiment'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.lhc.LhcExperiment` ATLAS
    
        ATLAS
    
    """
    ALICE: typing.ClassVar['LhcExperiment'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.lhc.LhcExperiment` ALICE
    
        ALICE
    
    """
    CMS: typing.ClassVar['LhcExperiment'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.lhc.LhcExperiment` CMS
    
        CMS
    
    """
    LHCB: typing.ClassVar['LhcExperiment'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.lhc.LhcExperiment` LHCB
    
        LHCB
    
    """
    LHCF: typing.ClassVar['LhcExperiment'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.lhc.LhcExperiment` LHCF
    
        LHCF
    
    """
    TOTEM: typing.ClassVar['LhcExperiment'] = ...
    """
    public static final :class:`~cern.accsoft.commons.domain.lhc.LhcExperiment` TOTEM
    
        TOTEM
    
    """
    @staticmethod
    def valueOf(string: str) -> 'LhcExperiment': ...
    @staticmethod
    def values() -> typing.List['LhcExperiment']: ...

class LhcInteractionPoint(java.lang.Enum['LhcInteractionPoint'], cern.accsoft.commons.util.Named):
    """
    public enum LhcInteractionPoint extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.lhc.LhcInteractionPoint`> implements cern.accsoft.commons.util.Named
    
        LHC interaction points.
    """
    LHC_IP1: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP2: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP3: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP4: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP5: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP6: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP7: typing.ClassVar['LhcInteractionPoint'] = ...
    LHC_IP8: typing.ClassVar['LhcInteractionPoint'] = ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LhcInteractionPoint':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['LhcInteractionPoint']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LhcInteractionPoint c : LhcInteractionPoint.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LhcSector(java.lang.Enum['LhcSector'], cern.accsoft.commons.util.Named):
    """
    public enum LhcSector extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.lhc.LhcSector`> implements cern.accsoft.commons.util.Named
    
        LHC sectors.
    """
    SECTOR_12: typing.ClassVar['LhcSector'] = ...
    SECTOR_23: typing.ClassVar['LhcSector'] = ...
    SECTOR_34: typing.ClassVar['LhcSector'] = ...
    SECTOR_45: typing.ClassVar['LhcSector'] = ...
    SECTOR_56: typing.ClassVar['LhcSector'] = ...
    SECTOR_67: typing.ClassVar['LhcSector'] = ...
    SECTOR_78: typing.ClassVar['LhcSector'] = ...
    SECTOR_81: typing.ClassVar['LhcSector'] = ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LhcSector':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['LhcSector']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LhcSector c : LhcSector.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.domain.lhc")``.

    LhcExperiment: typing.Type[LhcExperiment]
    LhcInteractionPoint: typing.Type[LhcInteractionPoint]
    LhcSector: typing.Type[LhcSector]
