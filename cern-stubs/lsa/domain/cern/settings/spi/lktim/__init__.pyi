import cern.accsoft.commons.util
import cern.lsa.domain.cern.settings.lktim
import cern.lsa.domain.commons.spi
import cern.lsa.domain.settings
import java.io
import java.util
import typing



class AbstractLktimDevice(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.settings.lktim.LktimDevice], cern.lsa.domain.cern.settings.lktim.LktimDevice):
    """
    public abstract class AbstractLktimDevice extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.cern.settings.lktim.LktimDevice`> implements :class:`~cern.lsa.domain.cern.settings.lktim.LktimDevice`
    
        Abstract implementation of :class:`~cern.lsa.domain.cern.settings.lktim.LktimDevice` with common attributes and methods.
    
        Also see:
            :meth:`~serialized`
    """
    PROPERTY_ACTIVE_TREE_ID: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPERTY_ACTIVE_TREE_ID
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getActiveTreeId(self, contextSettings: cern.lsa.domain.settings.ContextSettings) -> int:
        """
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.getActiveTreeId`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimDevice`
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeSettings.getActiveTreeId`
        
        
        """
        ...
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def isValid(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.isValid`
            Indicates whether the device wrapper is in a valid state i.e. it is properly configured in the database. It might be
            invalid (the method returns :code:`false`) e.g. if there are some parameters missing for the device in LSA database. If
            the method returns :code:`false`, then the method
            :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.getErrorMessages` returns details about the problem.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.isValid`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimDevice`
        
            Returns:
                :code:`true` if the device is valid and all necessary parameters exist, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.getErrorMessages`
        
        
        """
        ...
    def setActiveTreeId(self, contextSettings: cern.lsa.domain.settings.ContextSettings, long: int) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.setActiveTreeId`
            Sets value of 'ActiveTreeId' parameter to the specified value. The method is used when a tree is activated (IN_USE) to
            mark all devices that belong to this active tree.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.setActiveTreeId`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimDevice`
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeSettings.setActive`
        
        
        """
        ...

class LktimTreeImpl(cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity[cern.lsa.domain.cern.settings.lktim.LktimTree], cern.lsa.domain.cern.settings.lktim.LktimTree):
    """
    public final class LktimTreeImpl extends cern.lsa.domain.commons.spi.AbstractIdentifiedNamedEntity<:class:`~cern.lsa.domain.cern.settings.lktim.LktimTree`> implements :class:`~cern.lsa.domain.cern.settings.lktim.LktimTree`
    
        Implementation of the LKTIM :class:`~cern.lsa.domain.cern.settings.lktim.LktimTree` interface.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, long: int, string: str, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode): ...
    @typing.overload
    def __init__(self, long: int, string: str, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode, parameter: cern.lsa.domain.settings.Parameter, date: java.util.Date): ...
    def addErrorMessage(self, string: str) -> None: ...
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def getNode(self, string: str) -> cern.lsa.domain.cern.settings.lktim.LktimTreeNode:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getNode`
            Returns node with specified name belonging to this tree.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getNode`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTree`
        
            Parameters:
                deviceName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): name of the timing device for which node should be returned
        
            Returns:
                the node or :code:`null` if node with given name does not belong to this tree
        
        
        """
        ...
    def getRoot(self) -> cern.lsa.domain.cern.settings.lktim.LktimTreeNode:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getRoot`
            Returns root node of this tree. Note that root node is shared among all trees. The root node should not be trimmed and
            when settings are loaded for the whole tree - the root node settings are not touched.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getRoot`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTree`
        
            Returns:
                root node
        
        
        """
        ...
    def getStatusParameter(self) -> cern.lsa.domain.settings.Parameter:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getStatusParameter`
            Returns the LSA parameter that keeps the status of the tree. The parameter is created out of property:
            LKTIMTree/Status#value.
        
            The value type of this parameter is boolean and its setting indicates whether the tree is active (
            :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeStatus.IN_USE`) or not active
            ((:meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeStatus.NOT_IN_USE` or
            :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeStatus.NOT_USABLE`). Whether it is NOT_IN_USE or NOT_USABLE is
            determined when settings of the tree are loaded from the database and compared with all other overlapping trees.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getStatusParameter`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTree`
        
            Returns:
                LSA parameter representing 'activity' of the tree
        
            Also see:
                :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeStatus`
        
        
        """
        ...
    def getTime(self) -> java.util.Date:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getTime`
            Indicates time (in the past) for which the tree was loaded. If the method returns :code:`null`, it means that this is
            current tree (as defined currently in the database).
        
            It is a time in trim history when the tree structure was saved.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getTime`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTree`
        
            Returns:
                time for which the tree was loaded
        
        
        """
        ...
    def isValid(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.isValid`
            Indicates whether the tree is valid i.e. it is properly configured in the database. It might be invalid (the method
            returns :code:`false`) e.g. if there are some parameters missing for the tree in LSA database, if the setting describing
            structure of the tree is missing or corrupted or if any of the node devices does not exist any more. If the method
            returns :code:`false`, then the method :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getErrorMessages` returns
            more detailed information about the problem.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.isValid`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTree`
        
            Returns:
                :code:`true` if the tree is valid and all necessary devices, parameters and settings exist, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTree.getErrorMessages`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.cern.settings.lktim.LktimTree`
        
        
        """
        ...

class LktimTreeNodeImpl(cern.accsoft.commons.util.AbstractNamedSerializable[cern.lsa.domain.cern.settings.lktim.LktimTreeNode], cern.lsa.domain.cern.settings.lktim.LktimTreeNode):
    """
    public final class LktimTreeNodeImpl extends cern.accsoft.commons.util.AbstractNamedSerializable<:class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`> implements :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
    
        Implementation of the :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode` interface.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, long: int, lktimDevice: cern.lsa.domain.cern.settings.lktim.LktimDevice, string: str): ...
    @typing.overload
    def addChild(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.addChild`
            Adds child node to this node.
        
            After calling this method, this node becomes :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getParent` of the
            :code:`childNode`.
        
            Note that by calling this method, this node is not automatically persisted. This should be done separately using
            dedicated controller's method.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.addChild`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
            Parameters:
                node (:class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`): the child node to be added
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.addChild`
        
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.addChild`
            Inserts the specified child node at the specified position. Shifts the element currently at that position (if any) and
            any subsequent elements to the right.
        
            After calling this method, this node becomes :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getParent` of the
            :code:`childNode`.
        
            Note that by calling this method, this node is not automatically persisted. This should be done separately using
            dedicated controller's method.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.addChild`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
            Parameters:
                index (int): index at which the specified child is to be inserted
                node (:class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`): the child node to be inserted
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.addChild`
        
        
        """
        ...
    @typing.overload
    def addChild(self, int: int, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> None: ...
    def compareTo(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> int:
        """
        
            Specified by:
                 in interface 
        
            Overrides:
                :code:`compareTo` in class :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
        
        """
        ...
    def getChildCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getChildCount`
            Returns number of direct child nodes. This method is equivalent of calling
            :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getChildren`.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getChildCount`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
            Returns:
                returns number of direct child nodes
        
        
        """
        ...
    def getChildren(self) -> java.util.List[cern.lsa.domain.cern.settings.lktim.LktimTreeNode]: ...
    def getDescendants(self, boolean: bool) -> java.util.List[cern.lsa.domain.cern.settings.lktim.LktimTreeNode]: ...
    def getDescription(self) -> str:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getDescription`
            Returns descriptive text for the node that may indicate the nature and/or the function of the node in the tree.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
            Returns:
                description of the node in the tree
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.setDescription`
        
        
        """
        ...
    def getDeviceId(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getDeviceId`
            Returns database ID of the timing device representing this node.
        
            This method is there in case the underlying device has been deleted from the database, in which case the
            :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getLktimDevice` method returns :code:`null`.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getDeviceId`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
        
        """
        ...
    def getErrorMessages(self) -> java.util.Set[str]: ...
    def getLevel(self) -> int:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getLevel`
            Returns level of the node within the tree. Level for the root node is -1, level for root's children is 0, level for
            children of root's children is 1, etc..
        
            In the GUI application, effective roots of a tree are actually direct children of the ultimate root. And for these nodes
            users of the application expect the level to be 0. That's why the ultimate root's level is -1.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getLevel`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
            Returns:
                level of this node in the tree
        
        
        """
        ...
    def getLktimDevice(self) -> cern.lsa.domain.cern.settings.lktim.LktimDevice:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getLktimDevice`
            Returns associated wrapper over the timing device that translates settings of the node into appropriate properties of
            the underlying device.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getLktimDevice`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
            Returns:
                the associated :class:`~cern.lsa.domain.cern.settings.lktim.LktimDevice`
        
        
        """
        ...
    def getParent(self) -> cern.lsa.domain.cern.settings.lktim.LktimTreeNode:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getParent`
            Returns parent node or :code:`null` if this node is root in the tree
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getParent`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
            Returns:
                parent node or :code:`null`
        
        
        """
        ...
    def isValid(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.isValid`
            Indicates whether the node is valid i.e. it is properly configured in the database. It might be invalid (the method
            returns :code:`false`) e.g. if there are some parameters missing for the node in LSA database or if the device doesn't
            exist at all (was deleted). If the method returns :code:`false`, then the method
            :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getErrorMessages` returns more detailed information about the
            problem.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.isValid`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
            Returns:
                :code:`true` if the node is valid and the necessary device and parameters exist, :code:`false` otherwise
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getErrorMessages`
        
        
        """
        ...
    def removeChild(self, lktimTreeNode: cern.lsa.domain.cern.settings.lktim.LktimTreeNode) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.removeChild`
            Removes child node from this node.
        
            After calling this method, the :code:`childNode` is detached from this node i.e. this node is no more
            :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getParent` of the :code:`childNode`.
        
            Note that by calling this method, this node is not automatically persisted. This should be done separately using
            dedicated controller's method.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.removeChild`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
            Parameters:
                node (:class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`): child node to be removed
        
        
        """
        ...
    def setDescription(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.setDescription`
            Changes description of this node to the specified one.
        
            Specified by:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.setDescription`Â in
                interfaceÂ :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
            Parameters:
                desc (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): description of the node
        
            Also see:
                :meth:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode.getDescription`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :code:`toString` in class :class:`~cern.lsa.domain.cern.settings.lktim.LktimTreeNode`
        
        
        """
        ...

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
    """
    public final class LtimDevice extends :class:`~cern.lsa.domain.cern.settings.spi.lktim.AbstractLktimDevice`
    
        Implementation of the :class:`~cern.lsa.domain.cern.settings.lktim.LktimDevice` interface dedicated for LTIM class
        (FESA).
    
        Also see:
            :meth:`~serialized`
    """
    PROPERTY_DELAY: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPERTY_DELAY
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROPERTY_PAYLOAD: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPERTY_PAYLOAD
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROPERTY_ENABLE_STATUS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPERTY_ENABLE_STATUS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROPERTY_PERMIT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPERTY_PERMIT
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    PROPERTY_CLOCK: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PROPERTY_CLOCK
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str, list: java.util.List[cern.lsa.domain.settings.Parameter]): ...
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
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.setTime`
            Sets the absolute time when the device should pulse with the respect to the start of cycle.
        
        """
        ...

class RootNodeDevice(AbstractLktimDevice):
    """
    public final class RootNodeDevice extends :class:`~cern.lsa.domain.cern.settings.spi.lktim.AbstractLktimDevice`
    
        An implementation of :class:`~cern.lsa.domain.cern.settings.lktim.LktimDevice` dedicated for the root device which is
        treated separately as we don't fetch/trim its settings.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...
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
            Description copied from interface: :meth:`~cern.lsa.domain.cern.settings.lktim.LktimDevice.setTime`
            Sets the absolute time when the device should pulse with the respect to the start of cycle.
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.settings.spi.lktim")``.

    AbstractLktimDevice: typing.Type[AbstractLktimDevice]
    LktimTreeImpl: typing.Type[LktimTreeImpl]
    LktimTreeNodeImpl: typing.Type[LktimTreeNodeImpl]
    LktimTreeSettingsImpl: typing.Type[LktimTreeSettingsImpl]
    LtimDevice: typing.Type[LtimDevice]
    RootNodeDevice: typing.Type[RootNodeDevice]
