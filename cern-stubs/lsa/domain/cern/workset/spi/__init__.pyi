from typing import TypeVar as _py_TypeVar
from typing import ClassVar as _py_ClassVar
from typing import Generic as _py_Generic
from typing import overload
import cern.lsa.domain.cern.workset
import cern.lsa.domain.commons.spi
import cern.lsa.domain.devices
import cern.lsa.domain.settings
import java.io
import java.util


class CellsContainerHelper: ...

class KnobInstanceImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.cern.workset.KnobLayout], cern.lsa.domain.cern.workset.KnobInstance):
    def __init__(self, device: cern.lsa.domain.devices.Device, list: java.util.List[cern.lsa.domain.cern.workset.KnobPageInstance]): ...
    def getDevice(self) -> cern.lsa.domain.devices.Device: ...
    def getPages(self) -> java.util.List[cern.lsa.domain.cern.workset.KnobPageInstance]: ...
    def toString(self) -> str: ...

class KnobLayoutImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.cern.workset.KnobLayout], cern.lsa.domain.cern.workset.KnobLayout):
    def __init__(self, list: java.util.List[cern.lsa.domain.cern.workset.KnobPageLayout]): ...
    def getPages(self) -> java.util.List[cern.lsa.domain.cern.workset.KnobPageLayout]: ...
    def putCell(self, int: int, int2: int, int3: int, parameterTypeCell: cern.lsa.domain.cern.workset.ParameterTypeCell) -> cern.lsa.domain.cern.workset.KnobLayout: ...
    def removeCell(self, int: int, int2: int, int3: int) -> cern.lsa.domain.cern.workset.KnobLayout: ...
    def toString(self) -> str: ...

_KnobPageImpl__C = _py_TypeVar('_KnobPageImpl__C', bound=cern.lsa.domain.cern.workset.Cell)  # <C>
class KnobPageImpl(cern.lsa.domain.cern.workset.KnobPage[_KnobPageImpl__C], java.io.Serializable, _py_Generic[_KnobPageImpl__C]):
    def getCell(self, int: int, int2: int) -> _KnobPageImpl__C: ...
    def getColumnCount(self) -> int: ...
    def getRowCount(self) -> int: ...
    def toString(self) -> str: ...

class ParameterCellImpl(cern.lsa.domain.cern.workset.ParameterCell, java.io.Serializable):
    EMPTY_CELL: _py_ClassVar[cern.lsa.domain.cern.workset.ParameterCell] = ...
    def __init__(self, parameter: cern.lsa.domain.settings.Parameter): ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def isEmpty(self) -> bool: ...

class ParameterTypeCellImpl(cern.lsa.domain.cern.workset.ParameterTypeCell, java.io.Serializable):
    def __init__(self, string: str): ...
    def getParameterTypeName(self) -> str: ...
    def isEmpty(self) -> bool: ...
    def toString(self) -> str: ...

class WorkingSetDeviceGroupsImpl(cern.lsa.domain.cern.workset.WorkingSetDeviceGroups, java.io.Serializable):
    def __init__(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup): ...
    def getChildGroups(self) -> java.util.List[cern.lsa.domain.devices.DeviceGroup]: ...
    def getGroupsWithDevices(self) -> java.util.Map[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]]: ...
    def getWorkingSetGroup(self) -> cern.lsa.domain.devices.DeviceGroup: ...
    def getWorkingSetLayoutName(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup) -> str: ...
    def setDeviceGroupDevices(self, map: java.util.Map[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]]) -> None: ...
    def setDeviceGroupLayouts(self, map: java.util.Map[cern.lsa.domain.devices.DeviceGroup, str]) -> None: ...

class WorkingSetInstanceImpl(cern.lsa.domain.cern.workset.WorkingSetInstance, java.io.Serializable):
    def __init__(self, string: str, list: java.util.List[cern.lsa.domain.cern.workset.WorkingSetTableInstance]): ...
    def getName(self) -> str: ...
    def getTables(self) -> java.util.List[cern.lsa.domain.cern.workset.WorkingSetTableInstance]: ...
    def toString(self) -> str: ...

class WorkingSetTableInstanceCellImpl(cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell, java.io.Serializable):
    def __init__(self, string: str, parameter: cern.lsa.domain.settings.Parameter, device: cern.lsa.domain.devices.Device): ...
    def getDevice(self) -> cern.lsa.domain.devices.Device: ...
    def getDisplayPattern(self) -> str: ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def isEmpty(self) -> bool: ...
    def toString(self) -> str: ...

class WorkingSetTableInstanceImpl(cern.lsa.domain.cern.workset.WorkingSetTableInstance, java.io.Serializable):
    def __init__(self, string: str, map: java.util.Map[int, str], map2: java.util.Map[int, java.util.Map[int, cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell]]): ...
    @overload
    def getCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell: ...
    @overload
    def getCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.WorkingSetTableCell: ...
    def getColumnCount(self) -> int: ...
    def getColumnHeader(self, int: int) -> str: ...
    def getDescription(self) -> str: ...
    def getRowCount(self) -> int: ...
    def toString(self) -> str: ...

class WorkingSetTableLayoutCellImpl(cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell, java.io.Serializable):
    EMPTY_CELL: _py_ClassVar['WorkingSetTableLayoutCellImpl'] = ...
    LAYOUT_CELL_WITHOUT_CONFIGURATION: _py_ClassVar[cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell] = ...
    def __init__(self, string: str, string2: str): ...
    def getDisplayPattern(self) -> str: ...
    def getParameterTypeName(self) -> str: ...
    def isEmpty(self) -> bool: ...
    def toString(self) -> str: ...

class WorkingSetTableLayoutImpl(cern.lsa.domain.cern.workset.WorkingSetTableLayout, java.io.Serializable):
    def __init__(self, map: java.util.Map[int, str], map2: java.util.Map[int, java.util.Map[int, cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell]], string: str): ...
    @overload
    def getCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell: ...
    @overload
    def getCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.WorkingSetTableCell: ...
    def getColumnCount(self) -> int: ...
    def getColumnHeader(self, int: int) -> str: ...
    def getRowCount(self) -> int: ...
    def toString(self) -> str: ...

class KnobPageInstanceImpl(KnobPageImpl[cern.lsa.domain.cern.workset.ParameterCell], cern.lsa.domain.cern.workset.KnobPageInstance, java.io.Serializable):
    def __init__(self, map: java.util.Map[int, java.util.Map[int, cern.lsa.domain.cern.workset.ParameterCell]]): ...
    def getColumnCount(self) -> int: ...
    def getRowCount(self) -> int: ...
    def toString(self) -> str: ...

class KnobPageLayoutImpl(KnobPageImpl[cern.lsa.domain.cern.workset.ParameterTypeCell], cern.lsa.domain.cern.workset.KnobPageLayout, java.io.Serializable):
    def __init__(self, map: java.util.Map[int, java.util.Map[int, cern.lsa.domain.cern.workset.ParameterTypeCell]]): ...
    def getColumnCount(self) -> int: ...
    def getRowCount(self) -> int: ...
    def putCell(self, int: int, int2: int, parameterTypeCell: cern.lsa.domain.cern.workset.ParameterTypeCell) -> cern.lsa.domain.cern.workset.KnobPageLayout: ...
    def removeCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.KnobPageLayout: ...
    def toString(self) -> str: ...
