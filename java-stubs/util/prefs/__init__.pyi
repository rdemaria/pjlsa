from typing import Any as _py_Any
from typing import List as _py_List
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.io
import java.lang
import java.util


class BackingStoreException(java.lang.Exception):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, throwable: java.lang.Throwable): ...

class Base64:
    @classmethod
    def main(cls, stringArray: _py_List[str]) -> None: ...

class InvalidPreferencesFormatException(java.lang.Exception):
    @overload
    def __init__(self, string: str): ...
    @overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @overload
    def __init__(self, throwable: java.lang.Throwable): ...

class NodeChangeEvent(java.util.EventObject):
    def __init__(self, preferences: 'Preferences', preferences2: 'Preferences'): ...
    def getChild(self) -> 'Preferences': ...
    def getParent(self) -> 'Preferences': ...

class NodeChangeListener(java.util.EventListener):
    def childAdded(self, nodeChangeEvent: NodeChangeEvent) -> None: ...
    def childRemoved(self, nodeChangeEvent: NodeChangeEvent) -> None: ...

class PreferenceChangeEvent(java.util.EventObject):
    def __init__(self, preferences: 'Preferences', string: str, string2: str): ...
    def getKey(self) -> str: ...
    def getNewValue(self) -> str: ...
    def getNode(self) -> 'Preferences': ...

class PreferenceChangeListener(java.util.EventListener):
    def preferenceChange(self, preferenceChangeEvent: PreferenceChangeEvent) -> None: ...

class Preferences:
    MAX_KEY_LENGTH: _py_ClassVar[int] = ...
    MAX_VALUE_LENGTH: _py_ClassVar[int] = ...
    MAX_NAME_LENGTH: _py_ClassVar[int] = ...
    def absolutePath(self) -> str: ...
    def addNodeChangeListener(self, nodeChangeListener: NodeChangeListener) -> None: ...
    def addPreferenceChangeListener(self, preferenceChangeListener: PreferenceChangeListener) -> None: ...
    def childrenNames(self) -> _py_List[str]: ...
    def clear(self) -> None: ...
    def exportNode(self, outputStream: java.io.OutputStream) -> None: ...
    def exportSubtree(self, outputStream: java.io.OutputStream) -> None: ...
    def flush(self) -> None: ...
    def get(self, string: str, string2: str) -> str: ...
    def getBoolean(self, string: str, boolean: bool) -> bool: ...
    def getByteArray(self, string: str, byteArray: _py_List[int]) -> _py_List[int]: ...
    def getDouble(self, string: str, double: float) -> float: ...
    def getFloat(self, string: str, float: float) -> float: ...
    def getInt(self, string: str, int: int) -> int: ...
    def getLong(self, string: str, long: int) -> int: ...
    @classmethod
    def importPreferences(cls, inputStream: java.io.InputStream) -> None: ...
    def isUserNode(self) -> bool: ...
    def keys(self) -> _py_List[str]: ...
    def name(self) -> str: ...
    def node(self, string: str) -> 'Preferences': ...
    def nodeExists(self, string: str) -> bool: ...
    def parent(self) -> 'Preferences': ...
    def put(self, string: str, string2: str) -> None: ...
    def putBoolean(self, string: str, boolean: bool) -> None: ...
    def putByteArray(self, string: str, byteArray: _py_List[int]) -> None: ...
    def putDouble(self, string: str, double: float) -> None: ...
    def putFloat(self, string: str, float: float) -> None: ...
    def putInt(self, string: str, int: int) -> None: ...
    def putLong(self, string: str, long: int) -> None: ...
    def remove(self, string: str) -> None: ...
    def removeNode(self) -> None: ...
    def removeNodeChangeListener(self, nodeChangeListener: NodeChangeListener) -> None: ...
    def removePreferenceChangeListener(self, preferenceChangeListener: PreferenceChangeListener) -> None: ...
    def sync(self) -> None: ...
    @classmethod
    def systemNodeForPackage(cls, class_: _py_Type[_py_Any]) -> 'Preferences': ...
    @classmethod
    def systemRoot(cls) -> 'Preferences': ...
    def toString(self) -> str: ...
    @classmethod
    def userNodeForPackage(cls, class_: _py_Type[_py_Any]) -> 'Preferences': ...
    @classmethod
    def userRoot(cls) -> 'Preferences': ...

class PreferencesFactory:
    def systemRoot(self) -> Preferences: ...
    def userRoot(self) -> Preferences: ...

class XmlSupport: ...

class AbstractPreferences(Preferences):
    def absolutePath(self) -> str: ...
    def addNodeChangeListener(self, nodeChangeListener: NodeChangeListener) -> None: ...
    def addPreferenceChangeListener(self, preferenceChangeListener: PreferenceChangeListener) -> None: ...
    def childrenNames(self) -> _py_List[str]: ...
    def clear(self) -> None: ...
    def exportNode(self, outputStream: java.io.OutputStream) -> None: ...
    def exportSubtree(self, outputStream: java.io.OutputStream) -> None: ...
    def flush(self) -> None: ...
    def get(self, string: str, string2: str) -> str: ...
    def getBoolean(self, string: str, boolean: bool) -> bool: ...
    def getByteArray(self, string: str, byteArray: _py_List[int]) -> _py_List[int]: ...
    def getDouble(self, string: str, double: float) -> float: ...
    def getFloat(self, string: str, float: float) -> float: ...
    def getInt(self, string: str, int: int) -> int: ...
    def getLong(self, string: str, long: int) -> int: ...
    def isUserNode(self) -> bool: ...
    def keys(self) -> _py_List[str]: ...
    def name(self) -> str: ...
    def node(self, string: str) -> Preferences: ...
    def nodeExists(self, string: str) -> bool: ...
    def parent(self) -> Preferences: ...
    def put(self, string: str, string2: str) -> None: ...
    def putBoolean(self, string: str, boolean: bool) -> None: ...
    def putByteArray(self, string: str, byteArray: _py_List[int]) -> None: ...
    def putDouble(self, string: str, double: float) -> None: ...
    def putFloat(self, string: str, float: float) -> None: ...
    def putInt(self, string: str, int: int) -> None: ...
    def putLong(self, string: str, long: int) -> None: ...
    def remove(self, string: str) -> None: ...
    def removeNode(self) -> None: ...
    def removeNodeChangeListener(self, nodeChangeListener: NodeChangeListener) -> None: ...
    def removePreferenceChangeListener(self, preferenceChangeListener: PreferenceChangeListener) -> None: ...
    def sync(self) -> None: ...
    def toString(self) -> str: ...

class WindowsPreferencesFactory(PreferencesFactory):
    def systemRoot(self) -> Preferences: ...
    def userRoot(self) -> Preferences: ...

class WindowsPreferences(AbstractPreferences):
    def flush(self) -> None: ...
    def removeNodeSpi(self) -> None: ...
    def sync(self) -> None: ...