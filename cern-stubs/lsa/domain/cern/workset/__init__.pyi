import cern.accsoft.commons.util
import cern.lsa.domain.commons
import cern.lsa.domain.devices
import cern.lsa.domain.settings
import java.util
import typing


class Cell:
    def isEmpty(self) -> bool: ...

_Knob__P = typing.TypeVar('_Knob__P', bound='KnobPage')  # <P>
class Knob(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named, typing.Generic[_Knob__P]):
    def getPages(self) -> java.util.List[_Knob__P]: ...

_KnobPage__C = typing.TypeVar('_KnobPage__C', bound=Cell)  # <C>
class KnobPage(typing.Generic[_KnobPage__C]):
    def getCell(self, int: int, int2: int) -> _KnobPage__C: ...
    def getColumnCount(self) -> int: ...
    def getRowCount(self) -> int: ...

class WorkingSetDeviceGroups:
    def getChildGroups(self) -> java.util.List[cern.lsa.domain.devices.DeviceGroup]: ...
    def getGroupsWithDevices(self) -> java.util.Map[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]]: ...
    def getWorkingSetGroup(self) -> cern.lsa.domain.devices.DeviceGroup: ...
    def getWorkingSetLayoutName(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup) -> str: ...

class WorkingSetInstance(cern.accsoft.commons.util.Named):
    def getTables(self) -> java.util.List['WorkingSetTableInstance']: ...

_WorkingSetTable__C = typing.TypeVar('_WorkingSetTable__C', bound='WorkingSetTableCell')  # <C>
class WorkingSetTable(typing.Generic[_WorkingSetTable__C]):
    def getCell(self, int: int, int2: int) -> _WorkingSetTable__C: ...
    def getColumnCount(self) -> int: ...
    def getColumnHeader(self, int: int) -> str: ...
    def getRowCount(self) -> int: ...

class KnobInstance(Knob['KnobPageInstance']):
    def getDevice(self) -> cern.lsa.domain.devices.Device: ...

class KnobLayout(Knob['KnobPageLayout']):
    def putCell(self, int: int, int2: int, int3: int, parameterTypeCell: 'ParameterTypeCell') -> 'KnobLayout': ...
    def removeCell(self, int: int, int2: int, int3: int) -> 'KnobLayout': ...

class KnobPageInstance(KnobPage['ParameterCell']): ...

class KnobPageLayout(KnobPage['ParameterTypeCell']):
    def putCell(self, int: int, int2: int, parameterTypeCell: 'ParameterTypeCell') -> 'KnobPageLayout': ...
    def removeCell(self, int: int, int2: int) -> 'KnobPageLayout': ...

class ParameterCell(Cell):
    def getParameter(self) -> cern.lsa.domain.settings.Parameter: ...

class ParameterTypeCell(Cell):
    def getParameterTypeName(self) -> str: ...

class WorkingSetTableCell(Cell):
    def getDisplayPattern(self) -> str: ...

class WorkingSetTableInstance(WorkingSetTable['WorkingSetTableInstanceCell']):
    def getDescription(self) -> str: ...

class WorkingSetTableLayout(WorkingSetTable['WorkingSetTableLayoutCell']): ...

class WorkingSetTableInstanceCell(WorkingSetTableCell, ParameterCell):
    def getDevice(self) -> cern.lsa.domain.devices.Device: ...

class WorkingSetTableLayoutCell(WorkingSetTableCell, ParameterTypeCell):
    MACRO_DEVICE_NAME: typing.ClassVar[str] = ...
