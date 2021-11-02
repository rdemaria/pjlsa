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
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class KnobInstanceImpl extends cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity<:class:`~cern.lsa.domain.cern.workset.KnobLayout`> implements :class:`~cern.lsa.domain.cern.workset.KnobInstance`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation for an instance of :class:`~cern.lsa.domain.cern.workset.KnobLayout`
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, device: cern.lsa.domain.devices.Device, list: java.util.List[cern.lsa.domain.cern.workset.KnobPageInstance]): ...
    def getDevice(self) -> cern.lsa.domain.devices.Device:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.KnobInstance.getDevice`
            Get the device associated with the knob
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.KnobInstance.getDevice`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.KnobInstance`
        
            Returns:
                the associated device, not null
        
        
        """
        ...
    def getPages(self) -> java.util.List[cern.lsa.domain.cern.workset.KnobPageInstance]: ...
    def toString(self) -> str:
        """
            Deprecated.
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.cern.workset.KnobLayout`
        
        
        """
        ...

class KnobLayoutImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.cern.workset.KnobLayout], cern.lsa.domain.cern.workset.KnobLayout):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class KnobLayoutImpl extends cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity<:class:`~cern.lsa.domain.cern.workset.KnobLayout`> implements :class:`~cern.lsa.domain.cern.workset.KnobLayout`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation of :class:`~cern.lsa.domain.cern.workset.KnobLayout`
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, list: java.util.List[cern.lsa.domain.cern.workset.KnobPageLayout]): ...
    def getPages(self) -> java.util.List[cern.lsa.domain.cern.workset.KnobPageLayout]: ...
    def putCell(self, int: int, int2: int, int3: int, parameterTypeCell: cern.lsa.domain.cern.workset.ParameterTypeCell) -> cern.lsa.domain.cern.workset.KnobLayout:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.KnobLayout.putCell`
            Add a new cell to the layout
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.KnobLayout.putCell` in interface :class:`~cern.lsa.domain.cern.workset.KnobLayout`
        
            Parameters:
                pageIndex (int): index of the page to modify
                rowIndex (int): index of the row where the newCell should be put
                columnIndex (int): index of the column where the newCell should be put
                newCell (:class:`~cern.lsa.domain.cern.workset.ParameterTypeCell`): the new cell to insert
        
            Returns:
                the modified KnobLayout, not null
        
        
        """
        ...
    def removeCell(self, int: int, int2: int, int3: int) -> cern.lsa.domain.cern.workset.KnobLayout:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.KnobLayout.removeCell`
            Remove a cell from the layout
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.KnobLayout.removeCell`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.KnobLayout`
        
            Parameters:
                pageIndex (int): index of the page to modify
                rowIndex (int): index of the row where the cell will be deleted
                columnIndex (int): index of the column where the cell will be deleted
        
            Returns:
                the modified knobLayout, not null
        
        
        """
        ...
    def toString(self) -> str:
        """
            Deprecated.
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.cern.workset.KnobLayout`
        
        
        """
        ...

class ParameterCellImpl(cern.lsa.domain.cern.workset.ParameterCell, java.io.Serializable):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class ParameterCellImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.workset.ParameterCell`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation of :class:`~cern.lsa.domain.cern.workset.spi.ParameterCellImpl`
    
        Also see:
            :meth:`~serialized`
    """
    EMPTY_CELL: typing.ClassVar[cern.lsa.domain.cern.workset.ParameterCell] = ...
    """
    public static final :class:`~cern.lsa.domain.cern.workset.ParameterCell` EMPTY_CELL
    
        Deprecated.
    
    """
    def __init__(self, parameter: cern.lsa.domain.settings.Parameter): ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.ParameterCell.getParameter`
            Get the :code:`Parameter` contained by the cell
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.ParameterCell.getParameter`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.ParameterCell`
        
            Returns:
                the :code:`Parameter`, may be null
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.Cell.isEmpty` in interface :class:`~cern.lsa.domain.cern.workset.Cell`
        
            Returns:
                true if the cell is empty
        
        
        """
        ...

class ParameterTypeCellImpl(cern.lsa.domain.cern.workset.ParameterTypeCell, java.io.Serializable):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class ParameterTypeCellImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.workset.ParameterTypeCell`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation of :class:`~cern.lsa.domain.cern.workset.ParameterTypeCell`
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...
    def getParameterTypeName(self) -> str:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.ParameterTypeCell.getParameterTypeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.ParameterTypeCell`
        
            Returns:
                parameter type name associated with this cell or :code:`null`
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.Cell.isEmpty` in interface :class:`~cern.lsa.domain.cern.workset.Cell`
        
            Returns:
                true if the cell is empty
        
        
        """
        ...
    def toString(self) -> str:
        """
            Deprecated.
        
            Overrides:
                 in class 
        
        
        """
        ...

class WorkingSetDeviceGroupsImpl(cern.lsa.domain.cern.workset.WorkingSetDeviceGroups, java.io.Serializable):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class WorkingSetDeviceGroupsImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.workset.WorkingSetDeviceGroups`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use workingset-configuration-client library
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup): ...
    def getChildGroups(self) -> java.util.List[cern.lsa.domain.devices.DeviceGroup]: ...
    def getGroupsWithDevices(self) -> java.util.Map[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]]: ...
    def getWorkingSetGroup(self) -> cern.lsa.domain.devices.DeviceGroup:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetDeviceGroups.getWorkingSetGroup`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetDeviceGroups`
        
            Returns:
                device group representing the working set
        
        
        """
        ...
    def getWorkingSetLayoutName(self, deviceGroup: cern.lsa.domain.devices.DeviceGroup) -> str:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetDeviceGroups.getWorkingSetLayoutName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetDeviceGroups`
        
            Returns:
                name of layout associated with the given working set device group
        
        
        """
        ...
    def setDeviceGroupDevices(self, map: typing.Union[java.util.Map[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]], typing.Mapping[cern.lsa.domain.devices.DeviceGroup, java.util.List[cern.lsa.domain.devices.Device]]]) -> None: ...
    def setDeviceGroupLayouts(self, map: typing.Union[java.util.Map[cern.lsa.domain.devices.DeviceGroup, str], typing.Mapping[cern.lsa.domain.devices.DeviceGroup, str]]) -> None: ...

class WorkingSetInstanceImpl(cern.lsa.domain.cern.workset.WorkingSetInstance, java.io.Serializable):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class WorkingSetInstanceImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.workset.WorkingSetInstance`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation of :class:`~cern.lsa.domain.cern.workset.WorkingSetInstance`
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, list: java.util.List[cern.lsa.domain.cern.workset.WorkingSetTableInstance]): ...
    def getName(self) -> str:
        """
            Deprecated.
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    def getTables(self) -> java.util.List[cern.lsa.domain.cern.workset.WorkingSetTableInstance]: ...
    def toString(self) -> str:
        """
            Deprecated.
        
            Overrides:
                 in class 
        
        
        """
        ...

class WorkingSetTableInstanceCellImpl(cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell, java.io.Serializable):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class WorkingSetTableInstanceCellImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation of :class:`~cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell`
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, parameter: cern.lsa.domain.settings.Parameter, device: cern.lsa.domain.devices.Device): ...
    def getDevice(self) -> cern.lsa.domain.devices.Device:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell.getDevice`
            Returns device associated with this cell, may be null
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell.getDevice`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell`
        
        
        """
        ...
    def getDisplayPattern(self) -> str:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.WorkingSetTableCell.getDisplayPattern`
            Get the display pattern
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTableCell.getDisplayPattern`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTableCell`
        
            Returns:
                custom text to be displayed in the cell, may be null
        
        
        """
        ...
    def getParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.ParameterCell.getParameter`
            Get the :code:`Parameter` contained by the cell
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.ParameterCell.getParameter`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.ParameterCell`
        
            Returns:
                the :code:`Parameter`, may be null
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.Cell.isEmpty` in interface :class:`~cern.lsa.domain.cern.workset.Cell`
        
            Returns:
                true if the cell is empty
        
        
        """
        ...
    def toString(self) -> str:
        """
            Deprecated.
        
            Overrides:
                 in class 
        
        
        """
        ...

class WorkingSetTableInstanceImpl(cern.lsa.domain.cern.workset.WorkingSetTableInstance, java.io.Serializable):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class WorkingSetTableInstanceImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.workset.WorkingSetTableInstance`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation of :class:`~cern.lsa.domain.cern.workset.WorkingSetTableInstance`
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str, map: typing.Union[java.util.Map[int, str], typing.Mapping[int, str]], map2: typing.Union[java.util.Map[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell], typing.Mapping[int, cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell]]], typing.Mapping[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell], typing.Mapping[int, cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell]]]]): ...
    def getCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.WorkingSetTableInstanceCell:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getCell`
            Get a specific cell, throws `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` if the
            indexes are out of bound
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getCell`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`
        
            Returns:
                the cell or a default empty cell
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getColumnCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`
        
            Returns:
                the number of columns
        
        
        """
        ...
    def getColumnHeader(self, int: int) -> str:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getColumnHeader`
            Return the column header for a specific column. Throws `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` if the
            index is out of bound.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getColumnHeader`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`
        
            Parameters:
                columnIndex (int): the index of the column
        
            Returns:
                the column header, not null (enforced by DB)
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTableInstance.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTableInstance`
        
            Returns:
                the description of the table, may be null
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getRowCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`
        
            Returns:
                the number of rows
        
        
        """
        ...
    def toString(self) -> str:
        """
            Deprecated.
        
            Overrides:
                 in class 
        
        
        """
        ...

class WorkingSetTableLayoutCellImpl(cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell, java.io.Serializable):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class WorkingSetTableLayoutCellImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation of :class:`~cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell`
    
        Also see:
            :meth:`~serialized`
    """
    EMPTY_CELL: typing.ClassVar['WorkingSetTableLayoutCellImpl'] = ...
    """
    public static final :class:`~cern.lsa.domain.cern.workset.spi.WorkingSetTableLayoutCellImpl` EMPTY_CELL
    
        Deprecated.
    
    """
    LAYOUT_CELL_WITHOUT_CONFIGURATION: typing.ClassVar[cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell] = ...
    """
    public static final :class:`~cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell` LAYOUT_CELL_WITHOUT_CONFIGURATION
    
        Deprecated.
    
    """
    def __init__(self, string: str, string2: str): ...
    def getDisplayPattern(self) -> str:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.WorkingSetTableCell.getDisplayPattern`
            Get the display pattern
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTableCell.getDisplayPattern`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTableCell`
        
            Returns:
                custom text to be displayed in the cell, may be null
        
        
        """
        ...
    def getParameterTypeName(self) -> str:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.ParameterTypeCell.getParameterTypeName`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.ParameterTypeCell`
        
            Returns:
                parameter type name associated with this cell or :code:`null`
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.Cell.isEmpty` in interface :class:`~cern.lsa.domain.cern.workset.Cell`
        
            Returns:
                true if the cell is empty
        
        
        """
        ...
    def toString(self) -> str:
        """
            Deprecated.
        
            Overrides:
                 in class 
        
        
        """
        ...

class WorkingSetTableLayoutImpl(cern.lsa.domain.cern.workset.WorkingSetTableLayout, java.io.Serializable):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class WorkingSetTableLayoutImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.workset.WorkingSetTableLayout`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation of :class:`~cern.lsa.domain.cern.workset.WorkingSetTableLayout`
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, map: typing.Union[java.util.Map[int, str], typing.Mapping[int, str]], map2: typing.Union[java.util.Map[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell], typing.Mapping[int, cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell]]], typing.Mapping[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell], typing.Mapping[int, cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell]]]], string: str): ...
    def getCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.WorkingSetTableLayoutCell:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getCell`
            Get a specific cell, throws `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` if the
            indexes are out of bound
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getCell`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`
        
            Returns:
                the cell or a default empty cell
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getColumnCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`
        
            Returns:
                the number of columns
        
        
        """
        ...
    def getColumnHeader(self, int: int) -> str:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getColumnHeader`
            Return the column header for a specific column. Throws `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` if the
            index is out of bound.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getColumnHeader`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`
        
            Parameters:
                columnIndex (int): the index of the column
        
            Returns:
                the column header, not null (enforced by DB)
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
            Deprecated.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.WorkingSetTable.getRowCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.WorkingSetTable`
        
            Returns:
                the number of rows
        
        
        """
        ...
    def toString(self) -> str:
        """
            Deprecated.
        
            Overrides:
                 in class 
        
        
        """
        ...

class KnobPageInstanceImpl(cern.lsa.domain.cern.workset.spi.KnobPageImpl[cern.lsa.domain.cern.workset.ParameterCell], cern.lsa.domain.cern.workset.KnobPageInstance, java.io.Serializable):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class KnobPageInstanceImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.workset.KnobPageInstance`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation of :class:`~cern.lsa.domain.cern.workset.KnobPageInstance`
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, map: typing.Union[java.util.Map[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.ParameterCell], typing.Mapping[int, cern.lsa.domain.cern.workset.ParameterCell]]], typing.Mapping[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.ParameterCell], typing.Mapping[int, cern.lsa.domain.cern.workset.ParameterCell]]]]): ...

class KnobPageLayoutImpl(cern.lsa.domain.cern.workset.spi.KnobPageImpl[cern.lsa.domain.cern.workset.ParameterTypeCell], cern.lsa.domain.cern.workset.KnobPageLayout, java.io.Serializable):
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class KnobPageLayoutImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.domain.cern.workset.KnobPageLayout`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Deprecated.
        Use workingset-configuration-client library
        Implementation of :class:`~cern.lsa.domain.cern.workset.KnobPageLayout`
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, map: typing.Union[java.util.Map[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.ParameterTypeCell], typing.Mapping[int, cern.lsa.domain.cern.workset.ParameterTypeCell]]], typing.Mapping[int, typing.Union[java.util.Map[int, cern.lsa.domain.cern.workset.ParameterTypeCell], typing.Mapping[int, cern.lsa.domain.cern.workset.ParameterTypeCell]]]]): ...
    def putCell(self, int: int, int2: int, parameterTypeCell: cern.lsa.domain.cern.workset.ParameterTypeCell) -> cern.lsa.domain.cern.workset.KnobPageLayout:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.KnobPageLayout.putCell`
            Add a new cell to the layout
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.KnobPageLayout.putCell`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.KnobPageLayout`
        
            Parameters:
                newRowIndex (int): index of the row where the newCell should be put
                newColumnIndex (int): index of the column where the newCell should be put
                newCell (:class:`~cern.lsa.domain.cern.workset.ParameterTypeCell`): the new cell to insert
        
            Returns:
                the modified KnobLayout, not null
        
        
        """
        ...
    def removeCell(self, int: int, int2: int) -> cern.lsa.domain.cern.workset.KnobPageLayout:
        """
            Deprecated.
            Description copied from interface: :meth:`~cern.lsa.domain.cern.workset.KnobPageLayout.removeCell`
            Remove a cell from the layout
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.workset.KnobPageLayout.removeCell`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.workset.KnobPageLayout`
        
            Parameters:
                rowIndex (int): index of the row where the cell will be deleted
                columnIndex (int): index of the column where the cell will be deleted
        
            Returns:
                the modified knobLayout, not null
        
        
        """
        ...

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
