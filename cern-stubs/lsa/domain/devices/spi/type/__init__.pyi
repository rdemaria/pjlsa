import cern.accsoft.commons.util
import cern.accsoft.commons.value
import cern.lsa.domain.commons.spi
import cern.lsa.domain.devices
import cern.lsa.domain.devices.type
import java.lang
import java.util
import typing



class PropertyBuilder:
    """
    public final class PropertyBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self): ...
    def addField(self, propertyFieldInfo: 'PropertyBuilder.PropertyFieldInfo') -> 'PropertyBuilder': ...
    def build(self) -> cern.lsa.domain.devices.type.PropertyVersion: ...
    def hasFieldWithName(self, string: str) -> bool: ...
    def setAddedInLsa(self, boolean: bool) -> 'PropertyBuilder': ...
    def setCycleBound(self, boolean: bool) -> 'PropertyBuilder': ...
    def setDescription(self, string: str) -> 'PropertyBuilder': ...
    def setDeviceTypeVersion(self, deviceTypeVersion: cern.lsa.domain.devices.DeviceTypeVersion) -> 'PropertyBuilder': ...
    def setMonitorable(self, boolean: bool) -> 'PropertyBuilder': ...
    def setMultiplexed(self, boolean: bool) -> 'PropertyBuilder': ...
    def setName(self, string: str) -> 'PropertyBuilder': ...
    def setPropertyVisibility(self, propertyVisibility: cern.lsa.domain.devices.type.PropertyVersion.PropertyVisibility) -> 'PropertyBuilder': ...
    def setReadable(self, boolean: bool) -> 'PropertyBuilder': ...
    def setSupportingPartialSet(self, boolean: bool) -> 'PropertyBuilder': ...
    def setWritable(self, boolean: bool) -> 'PropertyBuilder': ...
    class PropertyFieldInfo(cern.accsoft.commons.util.Named):
        def __init__(self, string: str, type: cern.accsoft.commons.value.Type, string2: str, valueDescriptor: cern.accsoft.commons.value.ValueDescriptor, string3: str, propertyField: cern.lsa.domain.devices.type.PropertyField): ...
        def getName(self) -> str: ...

class PropertyFieldAccess(java.lang.Enum['PropertyFieldAccess']):
    """
    public enum PropertyFieldAccess extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.devices.spi.type.PropertyFieldAccess`>
    
        Characteristic of the field. It corresponds to FESA IN, OUT, INOUT values but our enum is easier to read and understand
        its meaning.
    """
    READ_ONLY: typing.ClassVar['PropertyFieldAccess'] = ...
    WRITE_ONLY: typing.ClassVar['PropertyFieldAccess'] = ...
    READ_WRITE: typing.ClassVar['PropertyFieldAccess'] = ...
    @staticmethod
    def getFromString(string: str) -> 'PropertyFieldAccess': ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PropertyFieldAccess':
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
    def values() -> typing.List['PropertyFieldAccess']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (PropertyFieldAccess c : PropertyFieldAccess.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PropertyVersionsRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.devices.type.PropertyVersionsRequest):
    """
    public class PropertyVersionsRequestImpl extends :class:`~cern.lsa.domain.commons.spi.AbstractPropertiesHolder` implements :class:`~cern.lsa.domain.devices.type.PropertyVersionsRequest`
    
        Default implementation of the :class:`~cern.lsa.domain.devices.type.PropertyVersionsRequest` interface.
    
        Also see:
            :meth:`~serialized`
    """
    PROPERTY_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPERTY_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.type.PropertyVersionsRequestImpl.getPropertyNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_TYPE_NAMES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_TYPE_NAMES
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.type.PropertyVersionsRequestImpl.getDeviceTypeNames`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEVICE_TYPE_VERSIONS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEVICE_TYPE_VERSIONS
    
        Attribute name for :meth:`~cern.lsa.domain.devices.spi.type.PropertyVersionsRequestImpl.getDeviceTypeVersions`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getDeviceTypeNames(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersions(self) -> java.util.Set[cern.lsa.domain.devices.DeviceTypeVersion]: ...
    def getPropertyNames(self) -> java.util.Set[str]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.devices.spi.type")``.

    PropertyBuilder: typing.Type[PropertyBuilder]
    PropertyFieldAccess: typing.Type[PropertyFieldAccess]
    PropertyVersionsRequestImpl: typing.Type[PropertyVersionsRequestImpl]
