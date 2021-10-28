import cern.japc.core
import cern.japc.value
import cern.lsa.client.common.japc
import cern.lsa.domain.settings
import java.io
import typing



class LsaSelectorImpl(cern.lsa.client.common.japc.LsaSelector, java.io.Serializable):
    """
    Java class 'cern.lsa.client.common.spi.japc.LsaSelectorImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.client.common.japc.LsaSelector, java.io.Serializable
    
      Constructors:
        * LsaSelectorImpl(cern.japc.core.Selector, cern.lsa.domain.settings.SettingPartEnum, java.lang.String)
    
    """
    def __init__(self, selector: cern.japc.core.Selector, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum, string: str): ...
    def getDataFilter(self) -> cern.japc.value.ParameterValue: ...
    def getId(self) -> str: ...
    def getPeriod(self) -> int: ...
    def getSettingPart(self) -> cern.lsa.domain.settings.SettingPartEnum: ...
    def getTrimDescription(self) -> str: ...
    def isPeriodic(self) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.common.spi.japc")``.

    LsaSelectorImpl: typing.Type[LsaSelectorImpl]
