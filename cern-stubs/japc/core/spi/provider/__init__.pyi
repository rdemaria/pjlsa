import cern.japc.core
import cern.japc.core.spi.cache
import cern.japc.value
import java.util
import typing



class CompositeParameterExplorer(cern.japc.core.ParameterExplorer):
    """
    Java class 'cern.japc.core.spi.provider.CompositeParameterExplorer'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.ParameterExplorer
    
      Constructors:
        * CompositeParameterExplorer(cern.japc.core.ParameterExplorer[])
    
    """
    def __init__(self, parameterExplorerArray: typing.List[cern.japc.core.ParameterExplorer]): ...
    def getAcceleratorNames(self, boolean: bool) -> typing.List[str]: ...
    def getDependentParameterNames(self, string: str) -> typing.List[str]: ...
    def getDeviceNamesForAccelerator(self, string: str, filter: cern.japc.core.ParameterExplorer.Filter) -> typing.List[str]: ...
    def getDeviceNamesForHost(self, string: str, filter: cern.japc.core.ParameterExplorer.Filter) -> typing.List[str]: ...
    def getFamilyNamesForAccelerator(self, string: str, filter: cern.japc.core.ParameterExplorer.Filter) -> typing.List[str]: ...
    def getFamilyNamesForHost(self, string: str, filter: cern.japc.core.ParameterExplorer.Filter) -> typing.List[str]: ...
    def getHostNamesForAccelerator(self, string: str, filter: cern.japc.core.ParameterExplorer.Filter) -> typing.List[str]: ...
    def getPropertyNameDescriptions(self, string: str) -> typing.List[cern.japc.core.ParameterExplorer.NameDescription]: ...
    def getRootParameterNames(self) -> typing.List[str]: ...
    def getSourceParameterNames(self, string: str) -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def mergeResults(nameDescriptionArray: typing.List[typing.List[cern.japc.core.ParameterExplorer.NameDescription]], int: int) -> typing.List[cern.japc.core.ParameterExplorer.NameDescription]: ...
    @typing.overload
    @staticmethod
    def mergeResults(stringArray: typing.List[typing.List[str]], int: int) -> typing.List[str]: ...

class DescriptorContainer:
    """
    Java class 'cern.japc.core.spi.provider.DescriptorContainer'
    
    """
    def getDeviceDescriptors(self) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    def getParameterDescriptors(self) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def getValueDescriptors(self) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...

class DescriptorProvider:
    """
    Java class 'cern.japc.core.spi.provider.DescriptorProvider'
    
      Attributes:
        SYSPROP_CDP_DATA_CONTAINERS (java.lang.String): final static field
    
    """
    SYSPROP_CDP_DATA_CONTAINERS: typing.ClassVar[str] = ...
    def findDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor: ...
    def findDeviceDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    def findParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def findParameterDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def findValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def findValueDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...

class CachingDescriptorProvider(DescriptorProvider, cern.japc.core.spi.cache.JapcCache):
    """
    Java class 'cern.japc.core.spi.provider.CachingDescriptorProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.provider.DescriptorProvider,
            cern.japc.core.spi.cache.JapcCache
    
      Constructors:
        * CachingDescriptorProvider(cern.japc.core.spi.provider.DescriptorProvider)
    
    """
    def __init__(self, descriptorProvider: DescriptorProvider): ...
    def clearAll(self) -> None: ...
    def findDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor: ...
    def findDeviceDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    def findParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def findParameterDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def findValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def findValueDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...

class CompositeDescriptorProvider(DescriptorProvider):
    """
    Java class 'cern.japc.core.spi.provider.CompositeDescriptorProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.provider.DescriptorProvider
    
      Constructors:
        * CompositeDescriptorProvider(cern.japc.core.spi.provider.DescriptorProvider[])
    
    """
    def __init__(self, descriptorProviderArray: typing.List[DescriptorProvider]): ...
    def createParameterExplorer(self) -> cern.japc.core.ParameterExplorer: ...
    def findDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor: ...
    def findDeviceDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    def findParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def findParameterDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def findValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def findValueDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...

class DefaultDescriptorProvider(DescriptorProvider):
    """
    Java class 'cern.japc.core.spi.provider.DefaultDescriptorProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.provider.DescriptorProvider
    
      Constructors:
        * DefaultDescriptorProvider()
    
    """
    def __init__(self): ...
    @staticmethod
    def createDefaultParameterDescriptor(string: str) -> cern.japc.core.ParameterDescriptor: ...
    def createParameterExplorer(self) -> cern.japc.core.ParameterExplorer: ...
    def findDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor: ...
    def findDeviceDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.DeviceDescriptor]: ...
    def findParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def findParameterDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.core.ParameterDescriptor]: ...
    def findValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    def findValueDescriptors(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> java.util.Map[str, cern.japc.value.ValueDescriptor]: ...

class CustomizableDescriptorProvider(DefaultDescriptorProvider):
    """
    Java class 'cern.japc.core.spi.provider.CustomizableDescriptorProvider'
    
        Extends:
            cern.japc.core.spi.provider.DefaultDescriptorProvider
    
      Constructors:
        * CustomizableDescriptorProvider()
    
      Attributes:
        DATA_CONTAINER_SEPARATOR (java.lang.String): static field
    
    """
    DATA_CONTAINER_SEPARATOR: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def addAllDescriptors(string: str, deviceDescriptor: cern.japc.core.DeviceDescriptor, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor) -> None: ...
    @staticmethod
    def addDeviceDescriptor(string: str, deviceDescriptor: cern.japc.core.DeviceDescriptor) -> None: ...
    @staticmethod
    def addParameterAndValueDescriptor(string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor, valueDescriptor: cern.japc.value.ValueDescriptor) -> None: ...
    @staticmethod
    def addParameterDescriptor(string: str, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> None: ...
    @staticmethod
    def addValueDescriptor(string: str, valueDescriptor: cern.japc.value.ValueDescriptor) -> None: ...
    def findDeviceDescriptor(self, string: str) -> cern.japc.core.DeviceDescriptor: ...
    def findParameterDescriptor(self, string: str) -> cern.japc.core.ParameterDescriptor: ...
    def findValueDescriptor(self, string: str) -> cern.japc.value.ValueDescriptor: ...
    @staticmethod
    def getDeviceInstanceSeparator() -> str: ...
    @staticmethod
    def setDeviceInstanceSeparator(string: str) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.provider")``.

    CachingDescriptorProvider: typing.Type[CachingDescriptorProvider]
    CompositeDescriptorProvider: typing.Type[CompositeDescriptorProvider]
    CompositeParameterExplorer: typing.Type[CompositeParameterExplorer]
    CustomizableDescriptorProvider: typing.Type[CustomizableDescriptorProvider]
    DefaultDescriptorProvider: typing.Type[DefaultDescriptorProvider]
    DescriptorContainer: typing.Type[DescriptorContainer]
    DescriptorProvider: typing.Type[DescriptorProvider]
