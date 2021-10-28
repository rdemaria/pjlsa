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
    Java class 'cern.lsa.domain.devices.spi.type.PropertyBuilder'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PropertyBuilder()
    
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
        """
        Java class 'cern.lsa.domain.devices.spi.type.PropertyBuilder$PropertyFieldInfo'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                cern.accsoft.commons.util.Named
        
          Constructors:
            * PropertyFieldInfo(java.lang.String, cern.accsoft.commons.value.Type, java.lang.String, cern.accsoft.commons.value.ValueDescriptor, java.lang.String, cern.lsa.domain.devices.type.PropertyField)
        
        """
        def __init__(self, string: str, type: cern.accsoft.commons.value.Type, string2: str, valueDescriptor: cern.accsoft.commons.value.ValueDescriptor, string3: str, propertyField: cern.lsa.domain.devices.type.PropertyField): ...
        def getName(self) -> str: ...

class PropertyFieldAccess(java.lang.Enum['PropertyFieldAccess']):
    """
    Java class 'cern.lsa.domain.devices.spi.type.PropertyFieldAccess'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        READ_ONLY (cern.lsa.domain.devices.spi.type.PropertyFieldAccess): final static enum constant
        WRITE_ONLY (cern.lsa.domain.devices.spi.type.PropertyFieldAccess): final static enum constant
        READ_WRITE (cern.lsa.domain.devices.spi.type.PropertyFieldAccess): final static enum constant
    
    """
    READ_ONLY: typing.ClassVar['PropertyFieldAccess'] = ...
    WRITE_ONLY: typing.ClassVar['PropertyFieldAccess'] = ...
    READ_WRITE: typing.ClassVar['PropertyFieldAccess'] = ...
    @staticmethod
    def getFromString(string: str) -> 'PropertyFieldAccess': ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'PropertyFieldAccess': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['PropertyFieldAccess']: ...

class PropertyVersionsRequestImpl(cern.lsa.domain.commons.spi.AbstractPropertiesHolder, cern.lsa.domain.devices.type.PropertyVersionsRequest):
    """
    Java class 'cern.lsa.domain.devices.spi.type.PropertyVersionsRequestImpl'
    
        Extends:
            cern.lsa.domain.commons.spi.AbstractPropertiesHolder
    
        Interfaces:
            cern.lsa.domain.devices.type.PropertyVersionsRequest
    
      Constructors:
        * PropertyVersionsRequestImpl(java.util.Map)
    
      Attributes:
        PROPERTY_NAMES (java.lang.String): final static field
        DEVICE_TYPE_NAMES (java.lang.String): final static field
        DEVICE_TYPE_VERSIONS (java.lang.String): final static field
    
    """
    PROPERTY_NAMES: typing.ClassVar[str] = ...
    DEVICE_TYPE_NAMES: typing.ClassVar[str] = ...
    DEVICE_TYPE_VERSIONS: typing.ClassVar[str] = ...
    def __init__(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]): ...
    def getDeviceTypeNames(self) -> java.util.Set[str]: ...
    def getDeviceTypeVersions(self) -> java.util.Set[cern.lsa.domain.devices.DeviceTypeVersion]: ...
    def getPropertyNames(self) -> java.util.Set[str]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.devices.spi.type")``.

    PropertyBuilder: typing.Type[PropertyBuilder]
    PropertyFieldAccess: typing.Type[PropertyFieldAccess]
    PropertyVersionsRequestImpl: typing.Type[PropertyVersionsRequestImpl]
