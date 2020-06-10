from typing import Any as _py_Any
from typing import ClassVar as _py_ClassVar
from typing import overload
import cern.accsoft.commons.util
import cern.lsa.domain.cern.settings.lktim
import cern.lsa.domain.commons.spi
import cern.lsa.domain.settings
import java.io
import java.util


class AbstractLktimDevice(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.settings.lktim.LktimDevice], cern.lsa.domain.cern.settings.lktim.LktimDevice):
    PROPERTY_ACTIVE_TREE_ID: _py_ClassVar[str] = ...
    def getActiveTreeId(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> int: ...
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def isValid(self) -> bool: ...
    def setActiveTreeId(self, contextSettings: cern.lsa.domain.settings.ContextSettings, long: int) -> None: ...

class LktimSettingsUtils: ...

class LktimTreeImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.cern.settings.lktim.LktimTree], cern.lsa.domain.cern.settings.lktim.LktimTree):
    @overload
    def __init__(self, long: int, string: str, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode): ...
    @overload
    def __init__(self, long: int, string: str, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode, parameter: cern.lsa.domain.settings.Parameter, date: java.util.Date): ...
    def addErrorMessage(self, string: str) -> None: ...
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def getNode(self, string: str) -> cern.lsa.domain.cern.settings.lktim.LktimTreeNode: ...
    def getRoot(self) -> cern.lsa.domain.cern.settings.lktim.LktimTreeNode: ...
    def getStatusParameter(self) -> cern.lsa.domain.settings.Parameter: ...
    def getTime(self) -> java.util.Date: ...
    def isValid(self) -> bool: ...
    def toString(self) -> str: ...

class LktimTreeNodeImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.settings.lktim.LktimTreeNode], cern.lsa.domain.cern.settings.lktim.LktimTreeNode):
    def __init__(self, long: int, lktimDevice: cern.lsa.domain.cern.settings.lktim.LktimDevice, string: str): ...
    @overload
    def addChild(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> None: ...
    @overload
    def addChild(self, int: int, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> None: ...
    @overload
    def compareTo(self, named: cern.accsoft.commons.util.Named) -> int: ...
    @overload
    def compareTo(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> int: ...
    @overload
    def compareTo(self, object: _py_Any) -> int: ...
    def getChildCount(self) -> int: ...
    def getChildren(self) -> java.util.List[cern.lsa.domain.cern.settings.lktim.LktimTreeNode]: ...
    def getDescendants(self, boolean: bool) -> java.util.List[cern.lsa.domain.cern.settings.lktim.LktimTreeNode]: ...
    def getDescription(self) -> str: ...
    def getDeviceId(self) -> int: ...
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def getLevel(self) -> int: ...
    def getLktimDevice(self) -> cern.lsa.domain.cern.settings.lktim.LktimDevice: ...
    def getParent(self) -> cern.lsa.domain.cern.settings.lktim.LktimTreeNode: ...
    def isValid(self) -> bool: ...
    def removeChild(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> None: ...
    def setDescription(self, string: str) -> None: ...
    def toString(self) -> str: ...

class LktimTreeSettingsImpl(cern.lsa.domain.cern.settings.lktim.LktimTreeSettings, java.io.Serializable):
    def __init__(self, lktimTree: cern.lsa.domain.cern.settings.lktim.LktimTree, lktimTreeStatus: cern.lsa.domain.cern.settings.lktim.LktimTreeStatus, contextSettings: cern.lsa.domain.settings.ContextSettings): ...
    def getActiveTreeId(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> int: ...
    def getContext(self) -> cern.lsa.domain.settings.StandAloneCycle: ...
    def getContextSettings(self) -> cern.lsa.domain.settings.ContextSettings: ...
    def getDelay(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> float: ...
    def getStatus(self) -> cern.lsa.domain.cern.settings.lktim.LktimTreeStatus: ...
    def getTime(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> float: ...
    def getTree(self) -> cern.lsa.domain.cern.settings.lktim.LktimTree: ...
    def isEnabled(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> bool: ...
    def isPermitted(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> bool: ...
    def setActive(self, boolean: bool) -> None: ...
    def setDelay(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode, double: float) -> None: ...
    def setEnabled(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode, boolean: bool) -> None: ...
    def setPermitted(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode, boolean: bool) -> None: ...
    def statusHasChanged(self) -> bool: ...
    def toString(self) -> str: ...

class LtimDevice(AbstractLktimDevice):
    PROPERTY_DELAY: _py_ClassVar[str] = ...
    PROPERTY_PAYLOAD: _py_ClassVar[str] = ...
    PROPERTY_ENABLE_STATUS: _py_ClassVar[str] = ...
    PROPERTY_PERMIT: _py_ClassVar[str] = ...
    PROPERTY_CLOCK: _py_ClassVar[str] = ...
    def __init__(self, string: str, list: java.util.List[cern.lsa.domain.settings.Parameter]): ...
    def getParameters(self) -> java.util.List[cern.lsa.domain.settings.Parameter]: ...
    def getTime(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> float: ...
    def isEnabled(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool: ...
    def isPermitted(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool: ...
    def setEnabled(self, contextSettings: cern.lsa.domain.settings.ContextSettings, boolean: bool) -> None: ...
    def setPermitted(self, contextSettings: cern.lsa.domain.settings.ContextSettings, boolean: bool) -> None: ...
    def setTime(self, contextSettings: cern.lsa.domain.settings.ContextSettings, double: float) -> None: ...

class RootNodeDevice(AbstractLktimDevice):
    def __init__(self, string: str): ...
    def getParameters(self) -> java.util.List[cern.lsa.domain.settings.Parameter]: ...
    def getTime(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> float: ...
    def isEnabled(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool: ...
    def isPermitted(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool: ...
    def setEnabled(self, contextSettings: cern.lsa.domain.settings.ContextSettings, boolean: bool) -> None: ...
    def setPermitted(self, contextSettings: cern.lsa.domain.settings.ContextSettings, boolean: bool) -> None: ...
    def setTime(self, contextSettings: cern.lsa.domain.settings.ContextSettings, double: float) -> None: ...
