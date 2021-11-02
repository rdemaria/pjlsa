import cern.accsoft.commons.util
import cern.lsa.domain.cern.workset.spi
import cern.lsa.domain.commons
import cern.lsa.domain.devices
import cern.lsa.domain.settings
import java.util
import typing



class Cell:
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface Cell
    
        Deprecated.
        Use workingset-configuration-client library
        Representation of a basic working set / knob cell
    """
    def isEmpty(self) -> bool:
        """
            Deprecated.
        
            Returns:
                true if the cell is empty
        
        
        """
        ...

_Knob__P = typing.TypeVar('_Knob__P', bound='KnobPage')  # <P>
class Knob(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named, typing.Generic[_Knob__P]):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface Knob<P extends :class:`~cern.lsa.domain.cern.workset.KnobPage`<? extends :class:`~cern.lsa.domain.cern.workset.Cell`>> extends cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named
    
        Deprecated.
        Use workingset-configuration-client library
        Represents a Knob.
    """
    def getPages(self) -> java.util.List[_Knob__P]: ...

_KnobPage__C = typing.TypeVar('_KnobPage__C', bound=Cell)  # <C>
class KnobPage(typing.Generic[_KnobPage__C]):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface KnobPage<C extends :class:`~cern.lsa.domain.cern.workset.Cell`>
    
        Deprecated.
        Use workingset-configuration-client library
        Represents a generic KnobPage.
    """
    def getCell(self, int: int, int2: int) -> _KnobPage__C:
        """
            Deprecated.
            Get a specific cell, throws `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` if the
            indexes are out of bound
        
            Parameters:
                row (int): index of the cell's row. Starting from 0.
                column (int): index of the cell's column. Starting from 0.
        
            Returns:
                the cell or a default empty cell
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
            Deprecated.
        
            Returns:
                number of the column of the page
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
            Deprecated.
        
            Returns:
                the number of rows of the page
        
        
        """
        ...

class WorkingSetDeviceGroups:
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface WorkingSetDeviceGroups
    
        Deprecated.
        Use workingset-configuration-client library
        Represents working set device groups together with associated layouts.
    """
    def getChildGroups(self) -> java.util.List[cern.lsa.domain.devices.DeviceGroup]: ...
    def getGroupsWithDevices(self) -> java.util.Map[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]]: ...
    def getWorkingSetGroup(self) -> cern.lsa.domain.devices.DeviceGroup:
        """
            Deprecated.
        
            Returns:
                device group representing the working set
        
        
        """
        ...
    def getWorkingSetLayoutName(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup) -> str:
        """
            Deprecated.
        
            Parameters:
                group (cern.lsa.domain.devices.DeviceGroup): 
            Returns:
                name of layout associated with the given working set device group
        
        
        """
        ...

class WorkingSetInstance(cern.accsoft.commons.util.Named):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface WorkingSetInstance extends cern.accsoft.commons.util.Named
    
        Deprecated.
        Use workingset-configuration-client library
        Represents a working set instance.
    """
    def getTables(self) -> java.util.List['WorkingSetTableInstance']: ...

_WorkingSetTable__C = typing.TypeVar('_WorkingSetTable__C', bound='WorkingSetTableCell')  # <C>
class WorkingSetTable(typing.Generic[_WorkingSetTable__C]):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface WorkingSetTable<C extends :class:`~cern.lsa.domain.cern.workset.WorkingSetTableCell`>
    
        Deprecated.
        Use workingset-configuration-client library
        Represents a single working set table (list of devices)
    """
    def getCell(self, int: int, int2: int) -> _WorkingSetTable__C:
        """
            Deprecated.
            Get a specific cell, throws `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` if the
            indexes are out of bound
        
            Parameters:
                row (int): index of the cell's row. Starting from 0.
                column (int): index of the cell's column. Starting from 0.
        
            Returns:
                the cell or a default empty cell
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
            Deprecated.
        
            Returns:
                the number of columns
        
        
        """
        ...
    def getColumnHeader(self, int: int) -> str:
        """
            Deprecated.
            Return the column header for a specific column. Throws `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` if the
            index is out of bound.
        
            Parameters:
                columnIndex (int): the index of the column
        
            Returns:
                the column header, not null (enforced by DB)
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
            Deprecated.
        
            Returns:
                the number of rows
        
        
        """
        ...

class KnobInstance(Knob['KnobPageInstance']):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface KnobInstance extends :class:`~cern.lsa.domain.cern.workset.Knob`<:class:`~cern.lsa.domain.cern.workset.KnobPageInstance`>
    
        Deprecated.
        Use workingset-configuration-client library
        Represents a KnobInstance.
    """
    def getDevice(self) -> cern.lsa.domain.devices.Device:
        """
            Deprecated.
            Get the device associated with the knob
        
            Returns:
                the associated device, not null
        
        
        """
        ...

class KnobLayout(Knob['KnobPageLayout']):
    def putCell(self, int: int, int2: int, int3: int, parameterTypeCell: 'ParameterTypeCell') -> 'KnobLayout': ...
    def removeCell(self, int: int, int2: int, int3: int) -> 'KnobLayout': ...

class KnobPageInstance(KnobPage['ParameterCell']):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface KnobPageInstance extends :class:`~cern.lsa.domain.cern.workset.KnobPage`<:class:`~cern.lsa.domain.cern.workset.ParameterCell`>
    
        Deprecated.
        Use workingset-configuration-client library
        Represents an instance of a Knob Page
    """
    ...

class KnobPageLayout(KnobPage['ParameterTypeCell']):
    def putCell(self, int: int, int2: int, parameterTypeCell: 'ParameterTypeCell') -> 'KnobPageLayout': ...
    def removeCell(self, int: int, int2: int) -> 'KnobPageLayout': ...

class ParameterCell(Cell):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface ParameterCell extends :class:`~cern.lsa.domain.cern.workset.Cell`
    
        Deprecated.
        Use workingset-configuration-client library
        Represent a :class:`~cern.lsa.domain.cern.workset.Cell` containing a :code:`Parameter`
    """
    def getParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
            Deprecated.
            Get the :code:`Parameter` contained by the cell
        
            Returns:
                the :code:`Parameter`, may be null
        
        
        """
        ...

class ParameterTypeCell(Cell):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface ParameterTypeCell extends :class:`~cern.lsa.domain.cern.workset.Cell`
    
        Deprecated.
        Use workingset-configuration-client library
        Represent a :class:`~cern.lsa.domain.cern.workset.Cell` containing a parameter type name
    """
    def getParameterTypeName(self) -> str:
        """
            Deprecated.
        
            Returns:
                parameter type name associated with this cell or :code:`null`
        
        
        """
        ...

class WorkingSetTableCell(Cell):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface WorkingSetTableCell extends :class:`~cern.lsa.domain.cern.workset.Cell`
    
        Deprecated.
        Use workingset-configuration-client library
        Represents a cell for a :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`
    """
    def getDisplayPattern(self) -> str:
        """
            Deprecated.
            Get the display pattern
        
            Returns:
                custom text to be displayed in the cell, may be null
        
        
        """
        ...

class WorkingSetTableInstance(WorkingSetTable['WorkingSetTableInstanceCell']):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface WorkingSetTableInstance extends :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`<:class:`~cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell`>
    
        Deprecated.
        Use workingset-configuration-client library
        Represents a single table (device group) in a working set.
    """
    def getDescription(self) -> str:
        """
            Deprecated.
        
            Returns:
                the description of the table, may be null
        
        
        """
        ...

class WorkingSetTableLayout(WorkingSetTable['WorkingSetTableLayoutCell']):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface WorkingSetTableLayout extends :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`<:class:`~cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell`>
    
        Deprecated.
        Use workingset-configuration-client library
        Represents a Working Set table layout
    """
    ...

class WorkingSetTableInstanceCell(WorkingSetTableCell, ParameterCell):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface WorkingSetTableInstanceCell extends :class:`~cern.lsa.domain.cern.workset.WorkingSetTableCell`, :class:`~cern.lsa.domain.cern.workset.ParameterCell`
    
        Deprecated.
        Use workingset-configuration-client library
    """
    def getDevice(self) -> cern.lsa.domain.devices.Device:
        """
            Deprecated.
            Returns device associated with this cell, may be null
        
        """
        ...

class WorkingSetTableLayoutCell(WorkingSetTableCell, ParameterTypeCell):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface WorkingSetTableLayoutCell extends :class:`~cern.lsa.domain.cern.workset.WorkingSetTableCell`, :class:`~cern.lsa.domain.cern.workset.ParameterTypeCell`
    
        Deprecated.
        Use workingset-configuration-client library
        Represents a cell contained in a :class:`~cern.lsa.domain.cern.workset.WorkingSetTableLayout`
    """
    MACRO_DEVICE_NAME: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MACRO_DEVICE_NAME
    
        Deprecated.
        Pattern to put in display pattern, in order to display the device's name
    
        Also see:
            :meth:`~constant`
    
    
    """


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
