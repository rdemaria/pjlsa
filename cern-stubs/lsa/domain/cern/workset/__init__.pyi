import cern.accsoft.commons.util
import cern.lsa.domain.cern.workset.spi
import cern.lsa.domain.commons
import cern.lsa.domain.devices
import cern.lsa.domain.settings
import java.util
import typing



class Cell:
    """
    Java class 'cern.lsa.domain.cern.workset.Cell'
    
    """
    def isEmpty(self) -> bool: ...

_Knob__P = typing.TypeVar('_Knob__P', bound='KnobPage')  # <P>
class Knob(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named, typing.Generic[_Knob__P]):
    """
    Java class 'cern.lsa.domain.cern.workset.Knob'
    
        Interfaces:
            cern.lsa.domain.commons.IdentifiedEntity,
            cern.accsoft.commons.util.Named
    
    """
    def getPages(self) -> java.util.List[_Knob__P]: ...

_KnobPage__C = typing.TypeVar('_KnobPage__C', bound=Cell)  # <C>
class KnobPage(typing.Generic[_KnobPage__C]):
    """
    Java class 'cern.lsa.domain.cern.workset.KnobPage'
    
    """
    def getCell(self, int: int, int2: int) -> _KnobPage__C: ...
    def getColumnCount(self) -> int: ...
    def getRowCount(self) -> int: ...

class WorkingSetDeviceGroups:
    """
    Java class 'cern.lsa.domain.cern.workset.WorkingSetDeviceGroups'
    
    """
    def getChildGroups(self) -> java.util.List[cern.lsa.domain.devices.DeviceGroup]: ...
    def getGroupsWithDevices(self) -> java.util.Map[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]]: ...
    def getWorkingSetGroup(self) -> cern.lsa.domain.devices.DeviceGroup: ...
    def getWorkingSetLayoutName(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup) -> str: ...

class WorkingSetInstance(cern.accsoft.commons.util.Named):
    """
    Java class 'cern.lsa.domain.cern.workset.WorkingSetInstance'
    
        Interfaces:
            cern.accsoft.commons.util.Named
    
    """
    def getTables(self) -> java.util.List['WorkingSetTableInstance']: ...

_WorkingSetTable__C = typing.TypeVar('_WorkingSetTable__C', bound='WorkingSetTableCell')  # <C>
class WorkingSetTable(typing.Generic[_WorkingSetTable__C]):
    """
    Java class 'cern.lsa.domain.cern.workset.WorkingSetTable'
    
    """
    def getCell(self, int: int, int2: int) -> _WorkingSetTable__C: ...
    def getColumnCount(self) -> int: ...
    def getColumnHeader(self, int: int) -> str: ...
    def getRowCount(self) -> int: ...

class KnobInstance(Knob['KnobPageInstance']):
    """
    Java class 'cern.lsa.domain.cern.workset.KnobInstance'
    
        Interfaces:
            cern.lsa.domain.cern.workset.Knob
    
    """
    def getDevice(self) -> cern.lsa.domain.devices.Device: ...

class KnobLayout(Knob['KnobPageLayout']):
    """
    Java class 'cern.lsa.domain.cern.workset.KnobLayout'
    
        Interfaces:
            cern.lsa.domain.cern.workset.Knob
    
    """
    def putCell(self, int: int, int2: int, int3: int, parameterTypeCell: 'ParameterTypeCell') -> 'KnobLayout': ...
    def removeCell(self, int: int, int2: int, int3: int) -> 'KnobLayout': ...

class KnobPageInstance(KnobPage['ParameterCell']): ...

class KnobPageLayout(KnobPage['ParameterTypeCell']):
    """
    Java class 'cern.lsa.domain.cern.workset.KnobPageLayout'
    
        Interfaces:
            cern.lsa.domain.cern.workset.KnobPage
    
    """
    def putCell(self, int: int, int2: int, parameterTypeCell: 'ParameterTypeCell') -> 'KnobPageLayout': ...
    def removeCell(self, int: int, int2: int) -> 'KnobPageLayout': ...

class ParameterCell(Cell):
    """
    Java class 'cern.lsa.domain.cern.workset.ParameterCell'
    
        Interfaces:
            cern.lsa.domain.cern.workset.Cell
    
    """
    def getParameter(self) -> cern.lsa.domain.settings.Parameter: ...

class ParameterTypeCell(Cell):
    """
    Java class 'cern.lsa.domain.cern.workset.ParameterTypeCell'
    
        Interfaces:
            cern.lsa.domain.cern.workset.Cell
    
    """
    def getParameterTypeName(self) -> str: ...

class WorkingSetTableCell(Cell):
    """
    Java class 'cern.lsa.domain.cern.workset.WorkingSetTableCell'
    
        Interfaces:
            cern.lsa.domain.cern.workset.Cell
    
    """
    def getDisplayPattern(self) -> str: ...

class WorkingSetTableInstance(WorkingSetTable['WorkingSetTableInstanceCell']):
    """
    Java class 'cern.lsa.domain.cern.workset.WorkingSetTableInstance'
    
        Interfaces:
            cern.lsa.domain.cern.workset.WorkingSetTable
    
    """
    def getDescription(self) -> str: ...

class WorkingSetTableLayout(WorkingSetTable['WorkingSetTableLayoutCell']): ...

class WorkingSetTableInstanceCell(WorkingSetTableCell, ParameterCell):
    """
    Java class 'cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell'
    
        Interfaces:
            cern.lsa.domain.cern.workset.WorkingSetTableCell,
            cern.lsa.domain.cern.workset.ParameterCell
    
    """
    def getDevice(self) -> cern.lsa.domain.devices.Device: ...

class WorkingSetTableLayoutCell(WorkingSetTableCell, ParameterTypeCell):
    """
    Java class 'cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell'
    
        Interfaces:
            cern.lsa.domain.cern.workset.WorkingSetTableCell,
            cern.lsa.domain.cern.workset.ParameterTypeCell
    
      Attributes:
        MACRO_DEVICE_NAME (java.lang.String): final static field
    
    """
    MACRO_DEVICE_NAME: typing.ClassVar[str] = ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.workset")``.

    Cell: typing.Type[Cell]
    Knob: typing.Type[Knob]
    KnobInstance: typing.Type[KnobInstance]
    KnobLayout: typing.Type[KnobLayout]
    KnobPage: typing.Type[KnobPage]
    KnobPageInstance: typing.Type[KnobPageInstance]
    KnobPageLayout: typing.Type[KnobPageLayout]
    ParameterCell: typing.Type[ParameterCell]
    ParameterTypeCell: typing.Type[ParameterTypeCell]
    WorkingSetDeviceGroups: typing.Type[WorkingSetDeviceGroups]
    WorkingSetInstance: typing.Type[WorkingSetInstance]
    WorkingSetTable: typing.Type[WorkingSetTable]
    WorkingSetTableCell: typing.Type[WorkingSetTableCell]
    WorkingSetTableInstance: typing.Type[WorkingSetTableInstance]
    WorkingSetTableInstanceCell: typing.Type[WorkingSetTableInstanceCell]
    WorkingSetTableLayout: typing.Type[WorkingSetTableLayout]
    WorkingSetTableLayoutCell: typing.Type[WorkingSetTableLayoutCell]
    spi: cern.lsa.domain.cern.workset.spi.__module_protocol__
