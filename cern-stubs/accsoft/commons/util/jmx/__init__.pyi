import cern.accsoft.commons.util.jmx.servlet
import cern.accsoft.commons.util.jmx.spring
import java.util
import javax.management
import org.slf4j
import typing



class MBeanRegistry:
    """
    Java class 'cern.accsoft.commons.util.jmx.MBeanRegistry'
    
        Extends:
            java.lang.Object
    
    """
    @typing.overload
    def createObjectName(self, string: str) -> javax.management.ObjectName: ...
    @typing.overload
    @staticmethod
    def createObjectName(string: str, string2: str) -> javax.management.ObjectName: ...
    @staticmethod
    def get() -> 'MBeanRegistry': ...
    def registerMBean(self, string: str, object: typing.Any, logger: org.slf4j.Logger) -> javax.management.ObjectInstance: ...
    def setJmxAppName(self, string: str) -> None: ...
    def unregisterAll(self, logger: org.slf4j.Logger) -> None: ...
    def unregisterMBean(self, string: str, logger: org.slf4j.Logger) -> None: ...

class NameParser:
    """
    Java class 'cern.accsoft.commons.util.jmx.NameParser'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * NameParser()
    
    """
    def __init__(self): ...
    @staticmethod
    def parseName(string: str) -> 'NameParser.Name': ...
    class Name:
        """
        Java class 'cern.accsoft.commons.util.jmx.NameParser$Name'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * Name(java.lang.String, java.util.Map, boolean)
        
        """
        def __init__(self, string: str, map: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]], boolean: bool): ...
        def getDomainName(self) -> str: ...
        def getProperties(self) -> java.util.Map[str, str]: ...
        def isPropertyListPattern(self) -> bool: ...
        def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.jmx")``.

    MBeanRegistry: typing.Type[MBeanRegistry]
    NameParser: typing.Type[NameParser]
    servlet: cern.accsoft.commons.util.jmx.servlet.__module_protocol__
    spring: cern.accsoft.commons.util.jmx.spring.__module_protocol__
