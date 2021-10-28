import org.slf4j
import typing



class MBean:
    """
    Java class 'cern.japc.core.spi.jmx.MBean'
    
    """
    def getDescription(self) -> str: ...

class MBeanRegistry:
    """
    Java class 'cern.japc.core.spi.jmx.MBeanRegistry'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MBeanRegistry()
    
    """
    def __init__(self): ...
    @staticmethod
    def get() -> 'MBeanRegistry': ...
    def getMBean(self, string: str) -> MBean: ...
    def registerMBean(self, string: str, mBean: MBean, logger: org.slf4j.Logger) -> None: ...
    def setJmxAppName(self, string: str) -> None: ...
    def unregisterAll(self, logger: org.slf4j.Logger) -> None: ...
    def unregisterMBean(self, string: str, logger: org.slf4j.Logger) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.jmx")``.

    MBean: typing.Type[MBean]
    MBeanRegistry: typing.Type[MBeanRegistry]
