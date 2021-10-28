import cern.japc.core
import cern.lsa.domain.settings
import typing



class LsaSelector(cern.japc.core.Selector):
    """
    Java class 'cern.lsa.client.common.japc.LsaSelector'
    
        Interfaces:
            cern.japc.core.Selector
    
    """
    def getSettingPart(self) -> cern.lsa.domain.settings.SettingPartEnum: ...
    def getTrimDescription(self) -> str: ...

class LsaSelectorBuilder:
    """
    Java class 'cern.lsa.client.common.japc.LsaSelectorBuilder'
    
        Extends:
            java.lang.Object
    
    """
    def build(self) -> LsaSelector: ...
    @staticmethod
    def newInstance() -> 'LsaSelectorBuilder': ...
    def setLsaContext(self, drivableContext: cern.lsa.domain.settings.DrivableContext) -> 'LsaSelectorBuilder': ...
    def setSelector(self, selector: cern.japc.core.Selector) -> 'LsaSelectorBuilder': ...
    def setSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'LsaSelectorBuilder': ...
    def setTrimDescription(self, string: str) -> 'LsaSelectorBuilder': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.common.japc")``.

    LsaSelector: typing.Type[LsaSelector]
    LsaSelectorBuilder: typing.Type[LsaSelectorBuilder]
