import java.io
import java.util
import typing



_TreeNode__T = typing.TypeVar('_TreeNode__T')  # <T>
class TreeNode(typing.Generic[_TreeNode__T]):
    """
    Java class 'cern.accsoft.commons.util.collections.tree.TreeNode'
    
    """
    def getChildNodes(self) -> java.util.Collection['TreeNode'[_TreeNode__T]]: ...
    def getNodeValue(self) -> _TreeNode__T: ...
    def getParentNode(self) -> 'TreeNode'[_TreeNode__T]: ...

class Trees:
    """
    Java class 'cern.accsoft.commons.util.collections.tree.Trees'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Trees()
    
    """
    def __init__(self): ...
    _newHashMapTree__T = typing.TypeVar('_newHashMapTree__T')  # <T>
    @staticmethod
    def newHashMapTree() -> 'EditableTreeNode'[_newHashMapTree__T]: ...
    _newLinkedHashMapTree__T = typing.TypeVar('_newLinkedHashMapTree__T')  # <T>
    @staticmethod
    def newLinkedHashMapTree() -> 'EditableTreeNode'[_newLinkedHashMapTree__T]: ...
    _newTreeMapTree__T = typing.TypeVar('_newTreeMapTree__T')  # <T>
    @staticmethod
    def newTreeMapTree(comparator: typing.Union[java.util.Comparator[_newTreeMapTree__T], typing.Callable[[_newTreeMapTree__T, _newTreeMapTree__T], int]]) -> 'EditableTreeNode'[_newTreeMapTree__T]: ...

_EditableTreeNode__T = typing.TypeVar('_EditableTreeNode__T')  # <T>
class EditableTreeNode(TreeNode[_EditableTreeNode__T], typing.Generic[_EditableTreeNode__T]):
    """
    Java class 'cern.accsoft.commons.util.collections.tree.EditableTreeNode'
    
        Interfaces:
            cern.accsoft.commons.util.collections.tree.TreeNode
    
    """
    def addChild(self, t: _EditableTreeNode__T) -> 'EditableTreeNode'[_EditableTreeNode__T]: ...
    def getChildNodes(self) -> java.util.Collection['EditableTreeNode'[_EditableTreeNode__T]]: ...
    def getParentNode(self) -> 'EditableTreeNode'[_EditableTreeNode__T]: ...
    def removeChild(self, t: _EditableTreeNode__T) -> 'EditableTreeNode'[_EditableTreeNode__T]: ...
    def setNodeValue(self, t: _EditableTreeNode__T) -> None: ...

_AbstractMapTreeNode__T = typing.TypeVar('_AbstractMapTreeNode__T')  # <T>
_AbstractMapTreeNode__N = typing.TypeVar('_AbstractMapTreeNode__N', bound='AbstractMapTreeNode')  # <N>
class AbstractMapTreeNode(EditableTreeNode[_AbstractMapTreeNode__T], java.io.Serializable, typing.Generic[_AbstractMapTreeNode__T, _AbstractMapTreeNode__N]):
    """
    Java class 'cern.accsoft.commons.util.collections.tree.AbstractMapTreeNode'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.util.collections.tree.EditableTreeNode,
            java.io.Serializable
    
    """
    def addChild(self, t: _AbstractMapTreeNode__T) -> _AbstractMapTreeNode__N: ...
    def getChildNodes(self) -> java.util.Collection[_AbstractMapTreeNode__N]: ...
    def getNodeValue(self) -> _AbstractMapTreeNode__T: ...
    def getParentNode(self) -> _AbstractMapTreeNode__N: ...
    def removeChild(self, t: _AbstractMapTreeNode__T) -> _AbstractMapTreeNode__N: ...
    def setNodeValue(self, t: _AbstractMapTreeNode__T) -> None: ...

_HashMapTreeNode__T = typing.TypeVar('_HashMapTreeNode__T')  # <T>
class HashMapTreeNode(AbstractMapTreeNode[_HashMapTreeNode__T, 'HashMapTreeNode'[_HashMapTreeNode__T]], typing.Generic[_HashMapTreeNode__T]): ...

_LinkedHashMapTreeNode__T = typing.TypeVar('_LinkedHashMapTreeNode__T')  # <T>
class LinkedHashMapTreeNode(AbstractMapTreeNode[_LinkedHashMapTreeNode__T, 'LinkedHashMapTreeNode'[_LinkedHashMapTreeNode__T]], typing.Generic[_LinkedHashMapTreeNode__T]): ...

_TreeMapTreeNode__T = typing.TypeVar('_TreeMapTreeNode__T')  # <T>
class TreeMapTreeNode(AbstractMapTreeNode[_TreeMapTreeNode__T, 'TreeMapTreeNode'[_TreeMapTreeNode__T]], typing.Generic[_TreeMapTreeNode__T]): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.collections.tree")``.

    AbstractMapTreeNode: typing.Type[AbstractMapTreeNode]
    EditableTreeNode: typing.Type[EditableTreeNode]
    HashMapTreeNode: typing.Type[HashMapTreeNode]
    LinkedHashMapTreeNode: typing.Type[LinkedHashMapTreeNode]
    TreeMapTreeNode: typing.Type[TreeMapTreeNode]
    TreeNode: typing.Type[TreeNode]
    Trees: typing.Type[Trees]
