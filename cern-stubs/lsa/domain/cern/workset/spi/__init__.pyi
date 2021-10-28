import cern
import cern.lsa.domain.cern.workset
import cern.lsa.domain.commons.spi
import cern.lsa.domain.devices
import cern.lsa.domain.settings
import java.io
import java.util
import typing



class KnobInstanceImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.cern.workset.KnobLayout], cern.lsa.domain.cern.workset.KnobInstance):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.KnobInstanceImpl'
    
        Extends:
            cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity
    
        Interfaces:
            cern.lsa.domain.cern.workset.KnobInstance
    
      Constructors:
        * KnobInstanceImpl(cern.lsa.domain.devices.Device, java.util.List)
    
    """
    def __init__(self, device: cern.lsa.domain.devices.Device, list: java.util.List[cern.lsa.domain.cern.workset.KnobPageInstance]): ...
    def getDevice(self) -> cern.lsa.domain.devices.Device: ...
    def getPages(self) -> java.util.List[cern.lsa.domain.cern.workset.KnobPageInstance]: ...
    def toString(self) -> str: ...

class KnobLayoutImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.cern.workset.KnobLayout], cern.lsa.domain.cern.workset.KnobLayout):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.KnobLayoutImpl'
    
        Extends:
            cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity
    
        Interfaces:
            cern.lsa.domain.cern.workset.KnobLayout
    
      Constructors:
        * KnobLayoutImpl(java.util.List)
    
    """
    def __init__(self, list: java.util.List[cern.lsa.domain.cern.workset.KnobPageLayout]): ...
    def getPages(self) -> java.util.List[cern.lsa.domain.cern.workset.KnobPageLayout]: ...
    def putCell(self, int: int, int2: int, int3: int, parameterTypeCell: cern.lsa.domain.cern.workset.ParameterTypeCell) -> cern.lsa.domain.cern.workset.KnobLayout: ...
    def removeCell(self, int: int, int2: int, int3: int) -> cern.lsa.domain.cern.workset.KnobLayout: ...
    def toString(self) -> str: ...

class ParameterCellImpl(cern.lsa.domain.cern.workset.ParameterCell, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.ParameterCellImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.workset.ParameterCell,
            java.io.Serializable
    
      Constructors:
        * ParameterCellImpl(cern.lsa.domain.settings.Parameter)
    
      Attributes:
        EMPTY_CELL (cern.lsa.domain.cern.workset.ParameterCell): final static field
    
    """
    EMPTY_CELL: typing.ClassVar[cern.lsa.domain.cern.workset.ParameterCell] = ...
    def __init__(self, parameter: cern.lsa.domain.settings.Parameter): ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def isEmpty(self) -> bool: ...

class ParameterTypeCellImpl(cern.lsa.domain.cern.workset.ParameterTypeCell, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.ParameterTypeCellImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.workset.ParameterTypeCell,
            java.io.Serializable
    
      Constructors:
        * ParameterTypeCellImpl(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    def getParameterTypeName(self) -> str: ...
    def isEmpty(self) -> bool: ...
    def toString(self) -> str: ...

class WorkingSetDeviceGroupsImpl(cern.lsa.domain.cern.workset.WorkingSetDeviceGroups, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.WorkingSetDeviceGroupsImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.workset.WorkingSetDeviceGroups,
            java.io.Serializable
    
      Constructors:
        * WorkingSetDeviceGroupsImpl(cern.lsa.domain.devices.DeviceGroup)
    
    """
    def __init__(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup): ...
    def getChildGroups(self) -> java.util.List[cern.lsa.domain.devices.DeviceGroup]: ...
    def getGroupsWithDevices(self) -> java.util.Map[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]]: ...
    def getWorkingSetGroup(self) -> cern.lsa.domain.devices.DeviceGroup: ...
    def getWorkingSetLayoutName(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup) -> str: ...
    def setDeviceGroupDevices(self, map: typing.Union[java.util.Map[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]], typing.Mapping[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]]]) -> None: ...
    def setDeviceGroupLayouts(self, map: typing.Union[java.util.Map[cern.lsa.domain.devices.DeviceGroup, str], typing.Mapping[cern.lsa.domain.devices.DeviceGroup, str]]) -> None: ...

class WorkingSetInstanceImpl(cern.lsa.domain.cern.workset.WorkingSetInstance, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.WorkingSetInstanceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.workset.WorkingSetInstance,
            java.io.Serializable
    
      Constructors:
        * WorkingSetInstanceImpl(java.lang.String, java.util.List)
    
    """
    def __init__(self, string: str, list: java.util.List[cern.lsa.domain.cern.workset.WorkingSetTableInstance]): ...
    def getName(self) -> str: ...
    def getTables(self) -> java.util.List[cern.lsa.domain.cern.workset.WorkingSetTableInstance]: ...
    def toString(self) -> str: ...

class WorkingSetTableInstanceCellImpl(cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.WorkingSetTableInstanceCellImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell,
            java.io.Serializable
    
      Constructors:
        * WorkingSetTableInstanceCellImpl(java.lang.String, cern.lsa.domain.settings.Parameter, cern.lsa.domain.devices.Device)
    
    """
    def __init__(self, string: str, parameter: cern.lsa.domain.settings.Parameter, device: cern.lsa.domain.devices.Device): ...
    def getDevice(self) -> cern.lsa.domain.devices.Device: ...
    def getDisplayPattern(self) -> str: ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def isEmpty(self) -> bool: ...
    def toString(self) -> str: ...

class WorkingSetTableInstanceImpl(cern.lsa.domain.cern.workset.WorkingSetTableInstance, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.WorkingSetTableInstanceImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.workset.WorkingSetTableInstance,
            java.io.Serializable
    
      Constructors:
        * WorkingSetTableInstanceImpl(java.lang.String, java.util.Map, java.util.Map)
    
    """
    def __init__(self, string: str, map: typing.Union[java.util.Map[int, str], typing.Mapping[int, str]], map2: typing.Union[java.util.Map[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell], typing.Mapping[int, cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell]]], typing.Mapping[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell], typing.Mapping[int, cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell]]]]): ...
    def getCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell: ...
    def getColumnCount(self) -> int: ...
    def getColumnHeader(self, int: int) -> str: ...
    def getDescription(self) -> str: ...
    def getRowCount(self) -> int: ...
    def toString(self) -> str: ...

class WorkingSetTableLayoutCellImpl(cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.WorkingSetTableLayoutCellImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell,
            java.io.Serializable
    
      Constructors:
        * WorkingSetTableLayoutCellImpl(java.lang.String, java.lang.String)
    
      Attributes:
        EMPTY_CELL (cern.lsa.domain.cern.workset.spi.WorkingSetTableLayoutCellImpl): final static field
        LAYOUT_CELL_WITHOUT_CONFIGURATION (cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell): final static field
    
    """
    EMPTY_CELL: typing.ClassVar['WorkingSetTableLayoutCellImpl'] = ...
    LAYOUT_CELL_WITHOUT_CONFIGURATION: typing.ClassVar[cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell] = ...
    def __init__(self, string: str, string2: str): ...
    def getDisplayPattern(self) -> str: ...
    def getParameterTypeName(self) -> str: ...
    def isEmpty(self) -> bool: ...
    def toString(self) -> str: ...

class WorkingSetTableLayoutImpl(cern.lsa.domain.cern.workset.WorkingSetTableLayout, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.WorkingSetTableLayoutImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.cern.workset.WorkingSetTableLayout,
            java.io.Serializable
    
      Constructors:
        * WorkingSetTableLayoutImpl(java.util.Map, java.util.Map, java.lang.String)
    
    """
    def __init__(self, map: typing.Union[java.util.Map[int, str], typing.Mapping[int, str]], map2: typing.Union[java.util.Map[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell], typing.Mapping[int, cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell]]], typing.Mapping[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell], typing.Mapping[int, cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell]]]], string: str): ...
    def getCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell: ...
    def getColumnCount(self) -> int: ...
    def getColumnHeader(self, int: int) -> str: ...
    def getRowCount(self) -> int: ...
    def toString(self) -> str: ...

class KnobPageInstanceImpl(cern.lsa.domain.cern.workset.spi.KnobPageImpl[cern.lsa.domain.cern.workset.ParameterCell], cern.lsa.domain.cern.workset.KnobPageInstance, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.KnobPageInstanceImpl'
    
        Extends:
            cern.lsa.domain.cern.workset.spi.KnobPageImpl
    
        Interfaces:
            cern.lsa.domain.cern.workset.KnobPageInstance,
            java.io.Serializable
    
      Constructors:
        * KnobPageInstanceImpl(java.util.Map)
    
    """
    def __init__(self, map: typing.Union[java.util.Map[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.ParameterCell], typing.Mapping[int, cern.lsa.domain.cern.workset.ParameterCell]]], typing.Mapping[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.ParameterCell], typing.Mapping[int, cern.lsa.domain.cern.workset.ParameterCell]]]]): ...

class KnobPageLayoutImpl(cern.lsa.domain.cern.workset.spi.KnobPageImpl[cern.lsa.domain.cern.workset.ParameterTypeCell], cern.lsa.domain.cern.workset.KnobPageLayout, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.cern.workset.spi.KnobPageLayoutImpl'
    
        Extends:
            cern.lsa.domain.cern.workset.spi.KnobPageImpl
    
        Interfaces:
            cern.lsa.domain.cern.workset.KnobPageLayout,
            java.io.Serializable
    
      Constructors:
        * KnobPageLayoutImpl(java.util.Map)
    
    """
    def __init__(self, map: typing.Union[java.util.Map[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.ParameterTypeCell], typing.Mapping[int, cern.lsa.domain.cern.workset.ParameterTypeCell]]], typing.Mapping[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.ParameterTypeCell], typing.Mapping[int, cern.lsa.domain.cern.workset.ParameterTypeCell]]]]): ...
    def putCell(self, int: int, int2: int, parameterTypeCell: cern.lsa.domain.cern.workset.ParameterTypeCell) -> cern.lsa.domain.cern.workset.KnobPageLayout: ...
    def removeCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.KnobPageLayout: ...

class KnobPageImpl: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.workset.spi")``.

    KnobInstanceImpl: typing.Type[KnobInstanceImpl]
    KnobLayoutImpl: typing.Type[KnobLayoutImpl]
    KnobPageImpl: typing.Type[KnobPageImpl]
    KnobPageInstanceImpl: typing.Type[KnobPageInstanceImpl]
    KnobPageLayoutImpl: typing.Type[KnobPageLayoutImpl]
    ParameterCellImpl: typing.Type[ParameterCellImpl]
    ParameterTypeCellImpl: typing.Type[ParameterTypeCellImpl]
    WorkingSetDeviceGroupsImpl: typing.Type[WorkingSetDeviceGroupsImpl]
    WorkingSetInstanceImpl: typing.Type[WorkingSetInstanceImpl]
    WorkingSetTableInstanceCellImpl: typing.Type[WorkingSetTableInstanceCellImpl]
    WorkingSetTableInstanceImpl: typing.Type[WorkingSetTableInstanceImpl]
    WorkingSetTableLayoutCellImpl: typing.Type[WorkingSetTableLayoutCellImpl]
    WorkingSetTableLayoutImpl: typing.Type[WorkingSetTableLayoutImpl]
