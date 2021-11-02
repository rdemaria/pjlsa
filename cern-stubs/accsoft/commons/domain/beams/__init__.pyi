import cern.accsoft.commons.domain
import cern.accsoft.commons.domain.modes
import cern.accsoft.commons.util
import java.lang
import java.util
import typing



class Beam(cern.accsoft.commons.util.Named):
    """
    public interface Beam extends cern.accsoft.commons.util.Named
    
        Accelerator beam.
    """
    def getAccelerator(self) -> cern.accsoft.commons.domain.Accelerator:
        """
        
            Returns:
                the accelerator this beam belongs to (never :code:`null`)
        
        
        """
        ...
    def getBeamNumber(self) -> int:
        """
        
            Returns:
                the beam number
        
        
        """
        ...

class AdBeam(java.lang.Enum['AdBeam'], Beam):
    """
    public enum AdBeam extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.beams.AdBeam`> implements :class:`~cern.accsoft.commons.domain.beams.Beam`
    
        AD beam.
    """
    BEAM1: typing.ClassVar['AdBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'AdBeam':
        """
            Returns the :class:`~cern.accsoft.commons.domain.beams.AdBeam` for the beam number
        
            Parameters:
                beamNumber (int): the beam number
        
            Returns:
                the enum value corresponding to the beam number
        
            Raises:
                : for wrong beam numbers
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the accelerator this beam belongs to (never :code:`null`)
        
        
        """
        ...
    def getBeamNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getBeamNumber`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the beam number
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AdBeam':
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
    def values() -> typing.List['AdBeam']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AdBeam c : AdBeam.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class AwakeBeam(java.lang.Enum['AwakeBeam'], Beam):
    """
    public enum AwakeBeam extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.beams.AwakeBeam`> implements :class:`~cern.accsoft.commons.domain.beams.Beam`
    
        AWAKE beam.
    """
    BEAM1: typing.ClassVar['AwakeBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'AwakeBeam':
        """
            Returns the :class:`~cern.accsoft.commons.domain.beams.AwakeBeam` for the beam number
        
            Parameters:
                beamNumber (int): the beam number
        
            Returns:
                the enum value corresponding to the beam number
        
            Raises:
                : for wrong beam numbers
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the accelerator this beam belongs to (never :code:`null`)
        
        
        """
        ...
    def getBeamNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getBeamNumber`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the beam number
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AwakeBeam':
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
    def values() -> typing.List['AwakeBeam']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AwakeBeam c : AwakeBeam.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ElenaBeam(java.lang.Enum['ElenaBeam'], Beam):
    """
    public enum ElenaBeam extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.beams.ElenaBeam`> implements :class:`~cern.accsoft.commons.domain.beams.Beam`
    
        ELENA beam.
    """
    BEAM1: typing.ClassVar['ElenaBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'ElenaBeam':
        """
            Returns the :class:`~cern.accsoft.commons.domain.beams.ElenaBeam` for the beam number
        
            Parameters:
                beamNumber (int): the beam number
        
            Returns:
                the enum value corresponding to the beam number
        
            Raises:
                : for wrong beam numbers
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the accelerator this beam belongs to (never :code:`null`)
        
        
        """
        ...
    def getBeamNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getBeamNumber`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the beam number
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ElenaBeam':
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
    def values() -> typing.List['ElenaBeam']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (ElenaBeam c : ElenaBeam.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class IsoldeBeam(java.lang.Enum['IsoldeBeam'], Beam):
    """
    public enum IsoldeBeam extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.beams.IsoldeBeam`> implements :class:`~cern.accsoft.commons.domain.beams.Beam`
    
        ISOLDE beam.
    """
    BEAM1: typing.ClassVar['IsoldeBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'IsoldeBeam':
        """
            Returns the :class:`~cern.accsoft.commons.domain.beams.IsoldeBeam` for the beam number
        
            Parameters:
                beamNumber (int): the beam number
        
            Returns:
                the enum value corresponding to the beam number
        
            Raises:
                : for wrong beam numbers
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the accelerator this beam belongs to (never :code:`null`)
        
        
        """
        ...
    def getBeamNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getBeamNumber`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the beam number
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'IsoldeBeam':
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
    def values() -> typing.List['IsoldeBeam']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (IsoldeBeam c : IsoldeBeam.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LeirBeam(java.lang.Enum['LeirBeam'], Beam):
    """
    public enum LeirBeam extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.beams.LeirBeam`> implements :class:`~cern.accsoft.commons.domain.beams.Beam`
    
        LEIR beam.
    """
    BEAM1: typing.ClassVar['LeirBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'LeirBeam':
        """
            Returns the :class:`~cern.accsoft.commons.domain.beams.LeirBeam` for the beam number
        
            Parameters:
                beamNumber (int): the beam number
        
            Returns:
                the enum value corresponding to the beam number
        
            Raises:
                : for wrong beam numbers
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the accelerator this beam belongs to (never :code:`null`)
        
        
        """
        ...
    def getBeamNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getBeamNumber`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the beam number
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LeirBeam':
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
    def values() -> typing.List['LeirBeam']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LeirBeam c : LeirBeam.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LhcBeam(java.lang.Enum['LhcBeam'], Beam):
    """
    public enum LhcBeam extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.beams.LhcBeam`> implements :class:`~cern.accsoft.commons.domain.beams.Beam`
    
        LHC beams.
    """
    BEAM1: typing.ClassVar['LhcBeam'] = ...
    BEAM2: typing.ClassVar['LhcBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'LhcBeam':
        """
            Returns the :class:`~cern.accsoft.commons.domain.beams.LhcBeam` for the beam number.
        
            Parameters:
                beamNumber (int): the beam number
        
            Returns:
                the enum value corresponding to the beam number
        
            Raises:
                : for wrong beam numbers
        
        
        """
        ...
    @staticmethod
    def fromNonStandardName(string: str) -> 'LhcBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the accelerator this beam belongs to (never :code:`null`)
        
        
        """
        ...
    def getBeamModes(self) -> java.util.Set[cern.accsoft.commons.domain.modes.LhcBeamMode]: ...
    def getBeamNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getBeamNumber`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the beam number
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LhcBeam':
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
    def values() -> typing.List['LhcBeam']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LhcBeam c : LhcBeam.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PsBeam(java.lang.Enum['PsBeam'], Beam):
    """
    public enum PsBeam extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.beams.PsBeam`> implements :class:`~cern.accsoft.commons.domain.beams.Beam`
    
        PS beam.
    """
    BEAM1: typing.ClassVar['PsBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'PsBeam':
        """
            Returns the :class:`~cern.accsoft.commons.domain.beams.PsBeam` for the beam number
        
            Parameters:
                beamNumber (int): the beam number
        
            Returns:
                the enum value corresponding to the beam number
        
            Raises:
                : for wrong beam numbers
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the accelerator this beam belongs to (never :code:`null`)
        
        
        """
        ...
    def getBeamNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getBeamNumber`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the beam number
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PsBeam':
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
    def values() -> typing.List['PsBeam']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (PsBeam c : PsBeam.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PsbBeam(java.lang.Enum['PsbBeam'], Beam):
    """
    public enum PsbBeam extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.beams.PsbBeam`> implements :class:`~cern.accsoft.commons.domain.beams.Beam`
    
        PSB beams.
    """
    BEAM1: typing.ClassVar['PsbBeam'] = ...
    BEAM2: typing.ClassVar['PsbBeam'] = ...
    BEAM3: typing.ClassVar['PsbBeam'] = ...
    BEAM4: typing.ClassVar['PsbBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'PsbBeam':
        """
            Returns the :class:`~cern.accsoft.commons.domain.beams.PsbBeam` for the beam number.
        
            Parameters:
                beamNumber (int): the beam number
        
            Returns:
                the enum value corresponding to the beam number
        
            Raises:
                : for wrong beam numbers
        
        
        """
        ...
    @staticmethod
    def fromNonStandardName(string: str) -> 'PsbBeam': ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the accelerator this beam belongs to (never :code:`null`)
        
        
        """
        ...
    def getBeamNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getBeamNumber`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the beam number
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PsbBeam':
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
    def values() -> typing.List['PsbBeam']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (PsbBeam c : PsbBeam.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SpsBeam(java.lang.Enum['SpsBeam'], Beam):
    """
    public enum SpsBeam extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.domain.beams.SpsBeam`> implements :class:`~cern.accsoft.commons.domain.beams.Beam`
    
        SPS beam.
    """
    BEAM1: typing.ClassVar['SpsBeam'] = ...
    @staticmethod
    def fromBeamNumber(int: int) -> 'SpsBeam':
        """
            Returns the :class:`~cern.accsoft.commons.domain.beams.SpsBeam` for the beam number
        
            Parameters:
                beamNumber (int): the beam number
        
            Returns:
                the enum value corresponding to the beam number
        
            Raises:
                : for wrong beam numbers
        
        
        """
        ...
    def getAccelerator(self) -> cern.accsoft.commons.domain.CernAccelerator:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getAccelerator`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the accelerator this beam belongs to (never :code:`null`)
        
        
        """
        ...
    def getBeamNumber(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.domain.beams.Beam.getBeamNumber`Â in
                interfaceÂ :class:`~cern.accsoft.commons.domain.beams.Beam`
        
            Returns:
                the beam number
        
        
        """
        ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SpsBeam':
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
    def values() -> typing.List['SpsBeam']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SpsBeam c : SpsBeam.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


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
