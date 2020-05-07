from typing import Any as _py_Any
from typing import List as _py_List
from typing import TypeVar as _py_TypeVar
from typing import Type as _py_Type
from typing import ClassVar as _py_ClassVar
from typing import overload
import java.io
import java.lang
import java.util


class MakeRuleClassInfo:
    @classmethod
    def builder(cls) -> 'DefaultMakeRuleClassInfo.Builder': ...
    def getClassName(self) -> str: ...
    def getProductName(self) -> str: ...
    def getVersion(self) -> str: ...

class MakeRuleConfigInfo:
    @classmethod
    def builder(cls) -> 'DefaultMakeRuleConfigInfo.Builder': ...
    def getMakeRuleConfigStatus(self) -> 'MakeRuleConfigInfo.MakeRuleConfigStatus': ...
    def getMakeRuleInfo(self) -> java.util.Optional['MakeRuleInfo']: ...
    class MakeRuleConfigStatus(java.lang.Enum['MakeRuleConfigInfo.MakeRuleConfigStatus']):
        FULLY_CONFIGURED: _py_ClassVar['MakeRuleConfigInfo.MakeRuleConfigStatus'] = ...
        NOT_CONFIGURED: _py_ClassVar['MakeRuleConfigInfo.MakeRuleConfigStatus'] = ...
        BEAN_MISSING: _py_ClassVar['MakeRuleConfigInfo.MakeRuleConfigStatus'] = ...
        @classmethod
        @overload
        def valueOf(cls, string: str) -> 'MakeRuleConfigInfo.MakeRuleConfigStatus': ...
        _valueOf_1__T = _py_TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @classmethod
        @overload
        def valueOf(cls, class_: _py_Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @classmethod
        def values(cls) -> _py_List['MakeRuleConfigInfo.MakeRuleConfigStatus']: ...

class MakeRuleInfo:
    @classmethod
    def builder(cls) -> 'DefaultMakeRuleInfo.Builder': ...
    def getMakeRuleClassInfo(self) -> java.util.Optional[MakeRuleClassInfo]: ...
    def getMakeRuleName(self) -> str: ...

class DefaultMakeRuleClassInfo(MakeRuleClassInfo, java.io.Serializable):
    @classmethod
    def builder(cls) -> 'DefaultMakeRuleClassInfo.Builder': ...
    @classmethod
    def copyOf(cls, makeRuleClassInfo: MakeRuleClassInfo) -> 'DefaultMakeRuleClassInfo': ...
    def equals(self, object: _py_Any) -> bool: ...
    def getClassName(self) -> str: ...
    def getProductName(self) -> str: ...
    def getVersion(self) -> str: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def withClassName(self, string: str) -> 'DefaultMakeRuleClassInfo': ...
    def withProductName(self, string: str) -> 'DefaultMakeRuleClassInfo': ...
    def withVersion(self, string: str) -> 'DefaultMakeRuleClassInfo': ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleClassInfo': ...
        def className(self, string: str) -> 'DefaultMakeRuleClassInfo.Builder': ...
        def productName(self, string: str) -> 'DefaultMakeRuleClassInfo.Builder': ...
        def version(self, string: str) -> 'DefaultMakeRuleClassInfo.Builder': ...

class DefaultMakeRuleConfigInfo(MakeRuleConfigInfo, java.io.Serializable):
    @classmethod
    def builder(cls) -> 'DefaultMakeRuleConfigInfo.Builder': ...
    @classmethod
    def copyOf(cls, makeRuleConfigInfo: MakeRuleConfigInfo) -> 'DefaultMakeRuleConfigInfo': ...
    def equals(self, object: _py_Any) -> bool: ...
    def getMakeRuleConfigStatus(self) -> MakeRuleConfigInfo.MakeRuleConfigStatus: ...
    def getMakeRuleInfo(self) -> java.util.Optional[MakeRuleInfo]: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def withMakeRuleConfigStatus(self, makeRuleConfigStatus: MakeRuleConfigInfo.MakeRuleConfigStatus) -> 'DefaultMakeRuleConfigInfo': ...
    @overload
    def withMakeRuleInfo(self, makeRuleInfo: MakeRuleInfo) -> 'DefaultMakeRuleConfigInfo': ...
    @overload
    def withMakeRuleInfo(self, optional: java.util.Optional[MakeRuleInfo]) -> 'DefaultMakeRuleConfigInfo': ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleConfigInfo': ...
        def makeRuleConfigStatus(self, makeRuleConfigStatus: MakeRuleConfigInfo.MakeRuleConfigStatus) -> 'DefaultMakeRuleConfigInfo.Builder': ...
        @overload
        def makeRuleInfo(self, makeRuleInfo: MakeRuleInfo) -> 'DefaultMakeRuleConfigInfo.Builder': ...
        @overload
        def makeRuleInfo(self, optional: java.util.Optional[MakeRuleInfo]) -> 'DefaultMakeRuleConfigInfo.Builder': ...

class DefaultMakeRuleInfo(MakeRuleInfo, java.io.Serializable):
    @classmethod
    def builder(cls) -> 'DefaultMakeRuleInfo.Builder': ...
    @classmethod
    def copyOf(cls, makeRuleInfo: MakeRuleInfo) -> 'DefaultMakeRuleInfo': ...
    def equals(self, object: _py_Any) -> bool: ...
    def getMakeRuleClassInfo(self) -> java.util.Optional[MakeRuleClassInfo]: ...
    def getMakeRuleName(self) -> str: ...
    def hashCode(self) -> int: ...
    @classmethod
    def of(cls, string: str) -> 'DefaultMakeRuleInfo': ...
    def toString(self) -> str: ...
    @overload
    def withMakeRuleClassInfo(self, makeRuleClassInfo: MakeRuleClassInfo) -> 'DefaultMakeRuleInfo': ...
    @overload
    def withMakeRuleClassInfo(self, optional: java.util.Optional[MakeRuleClassInfo]) -> 'DefaultMakeRuleInfo': ...
    def withMakeRuleName(self, string: str) -> 'DefaultMakeRuleInfo': ...
    class Builder:
        def build(self) -> 'DefaultMakeRuleInfo': ...
        @overload
        def makeRuleClassInfo(self, makeRuleClassInfo: MakeRuleClassInfo) -> 'DefaultMakeRuleInfo.Builder': ...
        @overload
        def makeRuleClassInfo(self, optional: java.util.Optional[MakeRuleClassInfo]) -> 'DefaultMakeRuleInfo.Builder': ...
        def makeRuleName(self, string: str) -> 'DefaultMakeRuleInfo.Builder': ...
