import java.io
import java.util
import typing



_TreeNode__T = typing.TypeVar('_TreeNode__T')  # <T>
class TreeNode(typing.Generic[_TreeNode__T]):
    """
    public interface TreeNode<T>
    
        Generic tree-node.
    """
    def getChildNodes(self) -> java.util.Collection['TreeNode'[_TreeNode__T]]: ...
    def getNodeValue(self) -> _TreeNode__T:
        """
            Returns the value of this node.
        
            Returns:
                the value of this node
        
        
        """
        ...
    def getParentNode(self) -> 'TreeNode'[_TreeNode__T]: ...

class Trees:
    """
    public class Trees extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory class for trees.
    """
    def __init__(self): ...
    _newHashMapTree__T = typing.TypeVar('_newHashMapTree__T')  # <T>
    @staticmethod
    def newHashMapTree() -> 'EditableTreeNode'[_newHashMapTree__T]:
        """
            Creates new empty tree to use when the node values implement `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#hashCode()>` and `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#equals(java.lang.Object)>`
            and the order of the children nodes is not important.
        
            Returns:
                the root node of the new tree
        
        
        """
        ...
    _newLinkedHashMapTree__T = typing.TypeVar('_newLinkedHashMapTree__T')  # <T>
    @staticmethod
    def newLinkedHashMapTree() -> 'EditableTreeNode'[_newLinkedHashMapTree__T]:
        """
            Creates new empty tree to use when the values implement `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#hashCode()>` and `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#equals(java.lang.Object)>`
            and the insertion order of the children nodes should be kept.
        
            Returns:
                the root node of the new tree
        
        
        """
        ...
    _newTreeMapTree__T = typing.TypeVar('_newTreeMapTree__T')  # <T>
    @staticmethod
    def newTreeMapTree(comparator: typing.Union[java.util.Comparator[_newTreeMapTree__T], typing.Callable[[_newTreeMapTree__T, _newTreeMapTree__T], int]]) -> 'EditableTreeNode'[_newTreeMapTree__T]: ...

_EditableTreeNode__T = typing.TypeVar('_EditableTreeNode__T')  # <T>
class EditableTreeNode(TreeNode[_EditableTreeNode__T], typing.Generic[_EditableTreeNode__T]):
    """
    public interface EditableTreeNode<T> extends :class:`~cern.accsoft.commons.util.collections.tree.TreeNode`<T>
    
        A tree node which can be modified.
    """
    def addChild(self, t: _EditableTreeNode__T) -> 'EditableTreeNode'[_EditableTreeNode__T]: ...
    def getChildNodes(self) -> java.util.Collection['EditableTreeNode'[_EditableTreeNode__T]]: ...
    def getParentNode(self) -> 'EditableTreeNode'[_EditableTreeNode__T]: ...
    def removeChild(self, t: _EditableTreeNode__T) -> 'EditableTreeNode'[_EditableTreeNode__T]: ...
    def setNodeValue(self, t: _EditableTreeNode__T) -> None:
        """
            Sets the value for the node.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode`): the value for the node
        
        
        """
        ...

_AbstractMapTreeNode__T = typing.TypeVar('_AbstractMapTreeNode__T')  # <T>
_AbstractMapTreeNode__N = typing.TypeVar('_AbstractMapTreeNode__N', bound='AbstractMapTreeNode')  # <N>
class AbstractMapTreeNode(EditableTreeNode[_AbstractMapTreeNode__T], java.io.Serializable, typing.Generic[_AbstractMapTreeNode__T, _AbstractMapTreeNode__N]):
    """
    public abstract class AbstractMapTreeNode<T, N extends AbstractMapTreeNode<T, N>> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode`<T>, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of an :class:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode`.
    
        Internally this implementation is backed up by a map, so this node doesn't allow duplicated children.
    
        Not thread-safe.
    
        Also see:
            :meth:`~serialized`
    """
    def addChild(self, t: _AbstractMapTreeNode__T) -> _AbstractMapTreeNode__N:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode.addChild`
            Adds and returns a child node initialized with the :code:`childValue`.
        
            If the tree doesn't allow duplicated children and there is already a child with the same value then the existing node is
            returned and no new node is created.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode.addChild`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode`
        
            Parameters:
                childValue (:class:`~cern.accsoft.commons.util.collections.tree.AbstractMapTreeNode`): a child value
        
            Returns:
                the newly created child node
        
        
        """
        ...
    def getChildNodes(self) -> java.util.Collection[_AbstractMapTreeNode__N]: ...
    def getNodeValue(self) -> _AbstractMapTreeNode__T:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.collections.tree.TreeNode.getNodeValue`
            Returns the value of this node.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.collections.tree.TreeNode.getNodeValue`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.collections.tree.TreeNode`
        
            Returns:
                the value of this node
        
        
        """
        ...
    def getParentNode(self) -> _AbstractMapTreeNode__N:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.collections.tree.TreeNode.getParentNode`
            Returns the parent of the node. Returns :code:`null` for the root node.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode.getParentNode`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode`
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.collections.tree.TreeNode.getParentNode`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.collections.tree.TreeNode`
        
            Returns:
                the parent of the node
        
        
        """
        ...
    def removeChild(self, t: _AbstractMapTreeNode__T) -> _AbstractMapTreeNode__N:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode.removeChild`
            Removes and returns a child node containing the :code:`childValue`.
        
            If there are multiple nodes with the same value one of them is removed.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode.removeChild`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode`
        
            Parameters:
                childValue (:class:`~cern.accsoft.commons.util.collections.tree.AbstractMapTreeNode`): a child value
        
            Returns:
                the removed child node
        
        
        """
        ...
    def setNodeValue(self, t: _AbstractMapTreeNode__T) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode.setNodeValue`
            Sets the value for the node.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode.setNodeValue`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.collections.tree.EditableTreeNode`
        
            Parameters:
                value (:class:`~cern.accsoft.commons.util.collections.tree.AbstractMapTreeNode`): the value for the node
        
        
        """
        ...

_HashMapTreeNode__T = typing.TypeVar('_HashMapTreeNode__T')  # <T>
class HashMapTreeNode(AbstractMapTreeNode[_HashMapTreeNode__T, 'HashMapTreeNode'[_HashMapTreeNode__T]], typing.Generic[_HashMapTreeNode__T]):
    """
    public class HashMapTreeNode<T> extends :class:`~cern.accsoft.commons.util.collections.tree.AbstractMapTreeNode`<T, :class:`~cern.accsoft.commons.util.collections.tree.HashMapTreeNode`<T>>
    
        An implementation of :class:`~cern.accsoft.commons.util.collections.tree.AbstractMapTreeNode` to use when the values
        implement `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#hashCode()>`
        and `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#equals(java.lang.Object)>`
        and the order of the children nodes is not important.
    
        Not thread-safe.
    
        Also see:
            :meth:`~serialized`
    """
    ...

_LinkedHashMapTreeNode__T = typing.TypeVar('_LinkedHashMapTreeNode__T')  # <T>
class LinkedHashMapTreeNode(AbstractMapTreeNode[_LinkedHashMapTreeNode__T, 'LinkedHashMapTreeNode'[_LinkedHashMapTreeNode__T]], typing.Generic[_LinkedHashMapTreeNode__T]):
    """
    public class LinkedHashMapTreeNode<T> extends :class:`~cern.accsoft.commons.util.collections.tree.AbstractMapTreeNode`<T, :class:`~cern.accsoft.commons.util.collections.tree.LinkedHashMapTreeNode`<T>>
    
        An implementation of :class:`~cern.accsoft.commons.util.collections.tree.AbstractMapTreeNode` to use when the values
        implement `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#hashCode()>`
        and `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#equals(java.lang.Object)>`
        and the insertion order of the children nodes should be kept.
    
        Not thread-safe.
    
        Also see:
            :meth:`~serialized`
    """
    ...

_TreeMapTreeNode__T = typing.TypeVar('_TreeMapTreeNode__T')  # <T>
class TreeMapTreeNode(AbstractMapTreeNode[_TreeMapTreeNode__T, 'TreeMapTreeNode'[_TreeMapTreeNode__T]], typing.Generic[_TreeMapTreeNode__T]):
    """
    public class TreeMapTreeNode<T> extends :class:`~cern.accsoft.commons.util.collections.tree.AbstractMapTreeNode`<T, :class:`~cern.accsoft.commons.util.collections.tree.TreeMapTreeNode`<T>>
    
        An implementation of :class:`~cern.accsoft.commons.util.collections.tree.AbstractMapTreeNode` to use when the node
        values don't implement `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#hashCode()>` and `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#equals(java.lang.Object)>`
        and/or the children nodes should be sorted according to the natural ordering of their values or by a `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Comparator.html?is-external=true>` provided at the node
        creation time.
    
        Not thread-safe.
    
        Also see:
            :meth:`~serialized`
    """
    ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.collections.tree")``.

    AbstractMapTreeNode: typing.Type[AbstractMapTreeNode]
    EditableTreeNode: typing.Type[EditableTreeNode]
    HashMapTreeNode: typing.Type[HashMapTreeNode]
    LinkedHashMapTreeNode: typing.Type[LinkedHashMapTreeNode]
    TreeMapTreeNode: typing.Type[TreeMapTreeNode]
    TreeNode: typing.Type[TreeNode]
    Trees: typing.Type[Trees]
