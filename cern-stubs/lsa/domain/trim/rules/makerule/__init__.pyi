import java.io
import java.lang
import java.util
import typing



class MakeRuleClassInfo:
    """
    Java class 'cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo'
    
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleClassInfo.Builder': ...
    def getClassName(self) -> str: ...
    def getProductName(self) -> str: ...
    def getVersion(self) -> str: ...

class MakeRuleConfigInfo:
    """
    Java class 'cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo'
    
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigInfo.Builder': ...
    def getMakeRuleConfigStatus(self) -> 'MakeRuleConfigInfo.MakeRuleConfigStatus': ...
    def getMakeRuleInfo(self) -> java.util.Optional['MakeRuleInfo']: ...
    class MakeRuleConfigStatus(java.lang.Enum['MakeRuleConfigInfo.MakeRuleConfigStatus']):
        """
        Java class 'cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo$MakeRuleConfigStatus'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            FULLY_CONFIGURED (cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo$MakeRuleConfigStatus): final static enum constant
            NOT_CONFIGURED (cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo$MakeRuleConfigStatus): final static enum constant
            BEAN_MISSING (cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo$MakeRuleConfigStatus): final static enum constant
        
        """
        FULLY_CONFIGURED: typing.ClassVar['MakeRuleConfigInfo.MakeRuleConfigStatus'] = ...
        NOT_CONFIGURED: typing.ClassVar['MakeRuleConfigInfo.MakeRuleConfigStatus'] = ...
        BEAN_MISSING: typing.ClassVar['MakeRuleConfigInfo.MakeRuleConfigStatus'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'MakeRuleConfigInfo.MakeRuleConfigStatus': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['MakeRuleConfigInfo.MakeRuleConfigStatus']: ...

class MakeRuleInfo:
    """
    Java class 'cern.lsa.domain.trim.rules.makerule.MakeRuleInfo'
    
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleInfo.Builder': ...
    def getMakeRuleClassInfo(self) -> java.util.Optional[MakeRuleClassInfo]: ...
    def getMakeRuleName(self) -> str: ...

class DefaultMakeRuleClassInfo(MakeRuleClassInfo, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleClassInfo'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.trim.rules.makerule.MakeRuleClassInfo,
            java.io.Serializable
    
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleClassInfo.Builder': ...
    @staticmethod
    def copyOf(makeRuleClassInfo: MakeRuleClassInfo) -> 'DefaultMakeRuleClassInfo': ...
    def equals(self, object: typing.Any) -> bool: ...
    def getClassName(self) -> str: ...
    def getProductName(self) -> str: ...
    def getVersion(self) -> str: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def withClassName(self, string: str) -> 'DefaultMakeRuleClassInfo': ...
    def withProductName(self, string: str) -> 'DefaultMakeRuleClassInfo': ...
    def withVersion(self, string: str) -> 'DefaultMakeRuleClassInfo': ...
    class Builder:
        """
        Java class 'cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleClassInfo$Builder'
        
            Extends:
                java.lang.Object
        
        """
        def build(self) -> 'DefaultMakeRuleClassInfo': ...
        def className(self, string: str) -> 'DefaultMakeRuleClassInfo.Builder': ...
        def productName(self, string: str) -> 'DefaultMakeRuleClassInfo.Builder': ...
        def version(self, string: str) -> 'DefaultMakeRuleClassInfo.Builder': ...

class DefaultMakeRuleConfigInfo(MakeRuleConfigInfo, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleConfigInfo'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.trim.rules.makerule.MakeRuleConfigInfo,
            java.io.Serializable
    
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleConfigInfo.Builder': ...
    @staticmethod
    def copyOf(makeRuleConfigInfo: MakeRuleConfigInfo) -> 'DefaultMakeRuleConfigInfo': ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMakeRuleConfigStatus(self) -> MakeRuleConfigInfo.MakeRuleConfigStatus: ...
    def getMakeRuleInfo(self) -> java.util.Optional[MakeRuleInfo]: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...
    def withMakeRuleConfigStatus(self, makeRuleConfigStatus: MakeRuleConfigInfo.MakeRuleConfigStatus) -> 'DefaultMakeRuleConfigInfo': ...
    @typing.overload
    def withMakeRuleInfo(self, makeRuleInfo: MakeRuleInfo) -> 'DefaultMakeRuleConfigInfo': ...
    @typing.overload
    def withMakeRuleInfo(self, optional: java.util.Optional[MakeRuleInfo]) -> 'DefaultMakeRuleConfigInfo': ...
    class Builder:
        """
        Java class 'cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleConfigInfo$Builder'
        
            Extends:
                java.lang.Object
        
        """
        def build(self) -> 'DefaultMakeRuleConfigInfo': ...
        def makeRuleConfigStatus(self, makeRuleConfigStatus: MakeRuleConfigInfo.MakeRuleConfigStatus) -> 'DefaultMakeRuleConfigInfo.Builder': ...
        @typing.overload
        def makeRuleInfo(self, makeRuleInfo: MakeRuleInfo) -> 'DefaultMakeRuleConfigInfo.Builder': ...
        @typing.overload
        def makeRuleInfo(self, optional: java.util.Optional[MakeRuleInfo]) -> 'DefaultMakeRuleConfigInfo.Builder': ...

class DefaultMakeRuleInfo(MakeRuleInfo, java.io.Serializable):
    """
    Java class 'cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleInfo'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.domain.trim.rules.makerule.MakeRuleInfo,
            java.io.Serializable
    
    """
    @staticmethod
    def builder() -> 'DefaultMakeRuleInfo.Builder': ...
    @staticmethod
    def copyOf(makeRuleInfo: MakeRuleInfo) -> 'DefaultMakeRuleInfo': ...
    def equals(self, object: typing.Any) -> bool: ...
    def getMakeRuleClassInfo(self) -> java.util.Optional[MakeRuleClassInfo]: ...
    def getMakeRuleName(self) -> str: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def of(string: str) -> 'DefaultMakeRuleInfo': ...
    def toString(self) -> str: ...
    @typing.overload
    def withMakeRuleClassInfo(self, makeRuleClassInfo: MakeRuleClassInfo) -> 'DefaultMakeRuleInfo': ...
    @typing.overload
    def withMakeRuleClassInfo(self, optional: java.util.Optional[MakeRuleClassInfo]) -> 'DefaultMakeRuleInfo': ...
    def withMakeRuleName(self, string: str) -> 'DefaultMakeRuleInfo': ...
    class Builder:
        """
        Java class 'cern.lsa.domain.trim.rules.makerule.DefaultMakeRuleInfo$Builder'
        
            Extends:
                java.lang.Object
        
        """
        def build(self) -> 'DefaultMakeRuleInfo': ...
        @typing.overload
        def makeRuleClassInfo(self, makeRuleClassInfo: MakeRuleClassInfo) -> 'DefaultMakeRuleInfo.Builder': ...
        @typing.overload
        def makeRuleClassInfo(self, optional: java.util.Optional[MakeRuleClassInfo]) -> 'DefaultMakeRuleInfo.Builder': ...
        def makeRuleName(self, string: str) -> 'DefaultMakeRuleInfo.Builder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.trim.rules.makerule")``.

    DefaultMakeRuleClassInfo: typing.Type[DefaultMakeRuleClassInfo]
    DefaultMakeRuleConfigInfo: typing.Type[DefaultMakeRuleConfigInfo]
    DefaultMakeRuleInfo: typing.Type[DefaultMakeRuleInfo]
    MakeRuleClassInfo: typing.Type[MakeRuleClassInfo]
    MakeRuleConfigInfo: typing.Type[MakeRuleConfigInfo]
    MakeRuleInfo: typing.Type[MakeRuleInfo]
