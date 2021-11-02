import cern.accsoft.commons.util
import cern.lsa.domain.commons
import cern.lsa.domain.settings
import java.lang
import java.util
import typing



class LktimDevice(cern.accsoft.commons.util.Named):
    """
    public interface LktimDevice extends cern.accsoft.commons.util.Named
    
        A wrapper interface that handles trims of **enable, permit and time** properties depending on the underlying device
        class.
    
        At the moment in an LKTIM tree we have only LTIM devices (before LS1 we had also PTIM-V devices).
    """
    def getActiveTreeId(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> int:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeSettings.getActiveTreeId`
        
        
        """
        ...
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def getParameters(self) -> java.util.List[cern.lsa.domain.settings.Parameter]: ...
    def getTime(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> float:
        """
        
            Also see:
                :code:`LktimTreeSettings#getTime(TreeNode)`
        
        
        """
        ...
    def isEnabled(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool:
        """
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeSettings.isEnabled`
        
        
        """
        ...
    def isPermitted(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> bool:
        """
        
            Also see:
                :code:`LktimTreeSettings#isPermitted(TreeNode)`
        
        
        """
        ...
    def isValid(self) -> bool:
        """
            Indicates whether the device wrapper is in a valid state i.e. it is properly configured in the database. It might be
            invalid (the method returns :code:`false`) e.g. if there are some parameters missing for the device in LSA database. If
            the method returns :code:`false`, then the method
            :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.getErrorMessages` returns details about the problem.
        
            Returns:
                :code:`true` if the device is valid and all necessary parameters exist, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.getErrorMessages`
        
        
        """
        ...
    def setActiveTreeId(self, contextSettings: cern.lsa.domain.settings.ContextSettings, long: int) -> None:
        """
            Sets value of 'ActiveTreeId' parameter to the specified value. The method is used when a tree is activated (IN_USE) to
            mark all devices that belong to this active tree.
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeSettings.setActive`
        
        
        """
        ...
    def setEnabled(self, contextSettings: cern.lsa.domain.settings.ContextSettings, boolean: bool) -> None:
        """
        
            Also see:
                :code:`LktimTreeSettings#setEnabled(TreeNode, boolean)`
        
        
        """
        ...
    def setPermitted(self, contextSettings: cern.lsa.domain.settings.ContextSettings, boolean: bool) -> None:
        """
        
            Also see:
                :code:`LktimTreeSettings#setPermitted(TreeNode, boolean)`
        
        
        """
        ...
    def setTime(self, contextSettings: cern.lsa.domain.settings.ContextSettings, double: float) -> None:
        """
            Sets the absolute time when the device should pulse with the respect to the start of cycle.
        
        """
        ...

class LktimTree(cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named):
    """
    public interface LktimTree extends cern.lsa.domain.commons.IdentifiedEntity, cern.accsoft.commons.util.Named
    
        Represents a Timing Tree structure i.e. the root node (device) of the tree and information about all the child nodes in
        the tree. The tree structure does not depend on the context (cycle). Any context-dependent information like status or
        settings of all nodes are stored in :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeSettings`.
    
        Also see:
            :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeSettings`
    """
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def getName(self) -> str:
        """
            Returns name of this tree.
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                name of this tree
        
        
        """
        ...
    def getNode(self, string: str) -> 'LktimTreeNode':
        """
            Returns node with specified name belonging to this tree.
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the timing device for which node should be returned
        
            Returns:
                the node or :code:`null` if node with given name does not belong to this tree
        
        
        """
        ...
    def getRoot(self) -> 'LktimTreeNode':
        """
            Returns root node of this tree. Note that root node is shared among all trees. The root node should not be trimmed and
            when settings are loaded for the whole tree - the root node settings are not touched.
        
            Returns:
                root node
        
        
        """
        ...
    def getStatusParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
            Returns the LSA parameter that keeps the status of the tree. The parameter is created out of property:
            LKTIMTree/Status#value.
        
            The value type of this parameter is boolean and its setting indicates whether the tree is active (
            :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeStatus.IN_USE`) or not active
            ((:meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeStatus.NOT_IN_USE` or
            :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeStatus.NOT_USABLE`). Whether it is NOT_IN_USE or NOT_USABLE is
            determined when settings of the tree are loaded from the database and compared with all other overlapping trees.
        
            Returns:
                LSA parameter representing 'activity' of the tree
        
            Also see:
                :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeStatus`
        
        
        """
        ...
    def getTime(self) -> java.util.Date:
        """
            Indicates time (in the past) for which the tree was loaded. If the method returns :code:`null`, it means that this is
            current tree (as defined currently in the database).
        
            It is a time in trim history when the tree structure was saved.
        
            Returns:
                time for which the tree was loaded
        
        
        """
        ...
    def isValid(self) -> bool:
        """
            Indicates whether the tree is valid i.e. it is properly configured in the database. It might be invalid (the method
            returns :code:`false`) e.g. if there are some parameters missing for the tree in LSA database, if the setting describing
            structure of the tree is missing or corrupted or if any of the node devices does not exist any more. If the method
            returns :code:`false`, then the method :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getErrorMessages` returns
            more detailed information about the problem.
        
            Returns:
                :code:`true` if the tree is valid and all necessary devices, parameters and settings exist, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getErrorMessages`
        
        
        """
        ...

class LktimTreeNode(cern.accsoft.commons.util.Named, java.lang.Comparable['LktimTreeNode']):
    @typing.overload
    def addChild(self, lktimTreeNode: 'LktimTreeNode') -> None: ...
    @typing.overload
    def addChild(self, int: int, lktimTreeNode: 'LktimTreeNode') -> None: ...
    def getChildCount(self) -> int: ...
    def getChildren(self) -> java.util.List['LktimTreeNode']: ...
    def getDescendants(self, boolean: bool) -> java.util.List['LktimTreeNode']: ...
    def getDescription(self) -> str: ...
    def getDeviceId(self) -> int: ...
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def getLevel(self) -> int: ...
    def getLktimDevice(self) -> LktimDevice: ...
    def getName(self) -> str: ...
    def getParent(self) -> 'LktimTreeNode': ...
    def isValid(self) -> bool: ...
    def removeChild(self, lktimTreeNode: 'LktimTreeNode') -> None: ...
    def setDescription(self, string: str) -> None: ...

class LktimTreeSettings:
    def getActiveTreeId(self, lktimTreeNode: LktimTreeNode) -> int: ...
    def getContext(self) -> cern.lsa.domain.settings.StandAloneCycle: ...
    def getContextSettings(self) -> cern.lsa.domain.settings.ContextSettings: ...
    def getDelay(self, lktimTreeNode: LktimTreeNode) -> float: ...
    def getStatus(self) -> 'LktimTreeStatus': ...
    def getTime(self, lktimTreeNode: LktimTreeNode) -> float: ...
    def getTree(self) -> LktimTree: ...
    def isEnabled(self, lktimTreeNode: LktimTreeNode) -> bool: ...
    def isPermitted(self, lktimTreeNode: LktimTreeNode) -> bool: ...
    def setActive(self, boolean: bool) -> None: ...
    def setDelay(self, lktimTreeNode: LktimTreeNode, double: float) -> None: ...
    def setEnabled(self, lktimTreeNode: LktimTreeNode, boolean: bool) -> None: ...
    def setPermitted(self, lktimTreeNode: LktimTreeNode, boolean: bool) -> None: ...
    def statusHasChanged(self) -> bool: ...

class LktimTreeStatus(java.lang.Enum['LktimTreeStatus']):
    """
    public enum LktimTreeStatus extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeStatus`>
    
        Possible status of an LKTIM tree.
    """
    IN_USE: typing.ClassVar['LktimTreeStatus'] = ...
    NOT_IN_USE: typing.ClassVar['LktimTreeStatus'] = ...
    NOT_USABLE: typing.ClassVar['LktimTreeStatus'] = ...
    ERROR: typing.ClassVar['LktimTreeStatus'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LktimTreeStatus':
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
    def values() -> typing.List['LktimTreeStatus']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LktimTreeStatus c : LktimTreeStatus.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class NodeAdditionCheckResult(java.lang.Enum['NodeAdditionCheckResult']):
    """
    public enum NodeAdditionCheckResult extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.domain.cern.settings.lktim.NodeAdditionCheckResult`>
    
        Result of a check that verifies if a device can be added to a given timing tree.
    """
    OK: typing.ClassVar['NodeAdditionCheckResult'] = ...
    DEVICE_ALREADY_IN_THE_TREE: typing.ClassVar['NodeAdditionCheckResult'] = ...
    CANNOT_ADD_TO_HISTORICAL_TREE: typing.ClassVar['NodeAdditionCheckResult'] = ...
    UNSUPPORTED_DEVICE: typing.ClassVar['NodeAdditionCheckResult'] = ...
    DEVICE_BELONGS_TO_ACTIVE_TREE: typing.ClassVar['NodeAdditionCheckResult'] = ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'NodeAdditionCheckResult':
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
    def values() -> typing.List['NodeAdditionCheckResult']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (NodeAdditionCheckResult c : NodeAdditionCheckResult.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.settings.lktim")``.

    LktimDevice: typing.Type[LktimDevice]
    LktimTree: typing.Type[LktimTree]
    LktimTreeNode: typing.Type[LktimTreeNode]
    LktimTreeSettings: typing.Type[LktimTreeSettings]
    LktimTreeStatus: typing.Type[LktimTreeStatus]
    NodeAdditionCheckResult: typing.Type[NodeAdditionCheckResult]
