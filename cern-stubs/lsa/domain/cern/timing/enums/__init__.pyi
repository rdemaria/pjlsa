import java.lang
import typing



class BEAM_TYPE(java.lang.Enum['BEAM_TYPE']):
    """
    public enum BEAM_TYPE extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.enums.BEAM_TYPE`>
    """
    INTERMEDIATE: typing.ClassVar['BEAM_TYPE'] = ...
    NOMINAL: typing.ClassVar['BEAM_TYPE'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'BEAM_TYPE':
        """
            Returns the BEAM_TYPE enumeration value corresponding to integer FESA value
        
            Parameters:
                fesaValue (int): an integer FESA value
        
            Returns:
                the corresponding BEAM_TYPE enumeration value
        
        
        """
        ...
    def getFesaValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'BEAM_TYPE':
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
    def values() -> typing.List['BEAM_TYPE']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (BEAM_TYPE c : BEAM_TYPE.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class INJECTION_STATUS(java.lang.Enum['INJECTION_STATUS']):
    """
    public enum INJECTION_STATUS extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.enums.INJECTION_STATUS`>
    """
    NO_REQUEST: typing.ClassVar['INJECTION_STATUS'] = ...
    PENDING: typing.ClassVar['INJECTION_STATUS'] = ...
    FAILED: typing.ClassVar['INJECTION_STATUS'] = ...
    SUCCEDED: typing.ClassVar['INJECTION_STATUS'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'INJECTION_STATUS':
        """
            Returns the INJECTION_STATUS enumeration value corresponding to integer FESA value
        
            Parameters:
                fesaValue (int): an integer FESA value
        
            Returns:
                the corresponding INJECTION_STATUS enumeration value
        
        
        """
        ...
    def getFesaValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'INJECTION_STATUS':
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
    def values() -> typing.List['INJECTION_STATUS']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (INJECTION_STATUS c : INJECTION_STATUS.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class MASTER_STATUS(java.lang.Enum['MASTER_STATUS']):
    """
    public enum MASTER_STATUS extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.enums.MASTER_STATUS`>
    """
    NO: typing.ClassVar['MASTER_STATUS'] = ...
    PENDING: typing.ClassVar['MASTER_STATUS'] = ...
    YES: typing.ClassVar['MASTER_STATUS'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'MASTER_STATUS':
        """
            Returns the MASTER_STATUS enumeration value corresponding to integer FESA value
        
            Parameters:
                fesaValue (int): an integer FESA value
        
            Returns:
                the corresponding MASTER_STATUS enumeration value
        
        
        """
        ...
    def getFesaValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'MASTER_STATUS':
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
    def values() -> typing.List['MASTER_STATUS']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (MASTER_STATUS c : MASTER_STATUS.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PARTICLE_TYPE(java.lang.Enum['PARTICLE_TYPE']):
    """
    public enum PARTICLE_TYPE extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.enums.PARTICLE_TYPE`>
    
        Enum defines the possible particle types.
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
    def valueOf(string: str) -> 'PARTICLE_TYPE':
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
    def values() -> typing.List['PARTICLE_TYPE']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (PARTICLE_TYPE c : PARTICLE_TYPE.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class RNGI(java.lang.Enum['RNGI']):
    """
    public enum RNGI extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.enums.RNGI`>
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
    def valueOf(string: str) -> 'RNGI':
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
    def values() -> typing.List['RNGI']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (RNGI c : RNGI.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TABLE_STATUS_HW(java.lang.Enum['TABLE_STATUS_HW']):
    """
    public enum TABLE_STATUS_HW extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.enums.TABLE_STATUS_HW`>
    """
    INVALID: typing.ClassVar['TABLE_STATUS_HW'] = ...
    ILLEGAL_OP_CODE: typing.ClassVar['TABLE_STATUS_HW'] = ...
    ILLEGAL_VALUE: typing.ClassVar['TABLE_STATUS_HW'] = ...
    ILLEGAL_REGISTER: typing.ClassVar['TABLE_STATUS_HW'] = ...
    WAITING: typing.ClassVar['TABLE_STATUS_HW'] = ...
    STOPPED: typing.ClassVar['TABLE_STATUS_HW'] = ...
    RUNNING: typing.ClassVar['TABLE_STATUS_HW'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'TABLE_STATUS_HW':
        """
            Returns the TABLE_STATUS_HW enumeration value corresponding to integer FESA value
        
            Parameters:
                fesaValue (int): an integer FESA value
        
            Returns:
                the corresponding TABLE_STATUS_HW enumeration value
        
        
        """
        ...
    def getFesaValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TABLE_STATUS_HW':
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
    def values() -> typing.List['TABLE_STATUS_HW']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (TABLE_STATUS_HW c : TABLE_STATUS_HW.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class TABLE_STATUS_SW(java.lang.Enum['TABLE_STATUS_SW']):
    """
    public enum TABLE_STATUS_SW extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.timing.enums.TABLE_STATUS_SW`>
    """
    INVALID: typing.ClassVar['TABLE_STATUS_SW'] = ...
    CRASHED: typing.ClassVar['TABLE_STATUS_SW'] = ...
    WAIT_PARA: typing.ClassVar['TABLE_STATUS_SW'] = ...
    WAIT_TRIG: typing.ClassVar['TABLE_STATUS_SW'] = ...
    RUNNING: typing.ClassVar['TABLE_STATUS_SW'] = ...
    @staticmethod
    def getEnumValue(int: int) -> 'TABLE_STATUS_SW':
        """
            Returns the TABLE_STATUS_SW enumeration value corresponding to integer FESA value
        
            Parameters:
                fesaValue (int): an integer FESA value
        
            Returns:
                the corresponding TABLE_STATUS_SW enumeration value
        
        
        """
        ...
    def getFesaValue(self) -> int: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'TABLE_STATUS_SW':
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
    def values() -> typing.List['TABLE_STATUS_SW']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (TABLE_STATUS_SW c : TABLE_STATUS_SW.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.timing.enums")``.

    BEAM_TYPE: typing.Type[BEAM_TYPE]
    INJECTION_STATUS: typing.Type[INJECTION_STATUS]
    MASTER_STATUS: typing.Type[MASTER_STATUS]
    PARTICLE_TYPE: typing.Type[PARTICLE_TYPE]
    RNGI: typing.Type[RNGI]
    TABLE_STATUS_HW: typing.Type[TABLE_STATUS_HW]
    TABLE_STATUS_SW: typing.Type[TABLE_STATUS_SW]
