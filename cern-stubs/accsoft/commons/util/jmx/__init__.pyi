import cern.accsoft.commons.util.jmx.servlet
import cern.accsoft.commons.util.jmx.spring
import java.util
import javax.management
import org.slf4j
import typing



class MBeanRegistry:
    """
    public class MBeanRegistry extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Helper class to facilitate the (un)registration of JMX MBeans.
    """
    @typing.overload
    def createObjectName(self, string: str) -> javax.management.ObjectName: ...
    @typing.overload
    @staticmethod
    def createObjectName(string: str, string2: str) -> javax.management.ObjectName: ...
    @staticmethod
    def get() -> 'MBeanRegistry':
        """
            Getter for the singleton.
        
            Returns:
                the singleton
        
        
        """
        ...
    def registerMBean(self, string: str, object: typing.Any, logger: org.slf4j.Logger) -> javax.management.ObjectInstance:
        """
            Registers an MBean.
        
            This method never throws an exception in order to not prevent application from working. It logs the problem instead.
        
            Parameters:
                mBeanName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): valid MBean name, ex. "cern.japc:type=core,name=updateDelivery"
                mBean (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): MBean implementation to register
                logger (org.slf4j.Logger): logger to use (can be :code:`null`)
        
            Returns:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/management/ObjectInstance.html?is-external=true>`
                corresponding to the registered bean or :code:`null` if registration failed.
        
        
        """
        ...
    def setJmxAppName(self, string: str) -> None:
        """
            Setter for the application name to be used by JMX in order to distinguish applications running in the same JVM (the case
            of application servers) but loaded with different classloaders.
        
            Parameters:
                jmxAppName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): JMX application name
        
        
        """
        ...
    def unregisterAll(self, logger: org.slf4j.Logger) -> None:
        """
            Unregisters all the registered MBeans.
        
            Parameters:
                logger (org.slf4j.Logger): logger to use
        
        
        """
        ...
    def unregisterMBean(self, string: str, logger: org.slf4j.Logger) -> None:
        """
            Unregisters an MBean.
        
            This method never throws an exception in order to not prevent application from working. It logs the problem instead.
        
            Parameters:
                mBeanName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): valid MBean name, ex. "cern.japc:type=core,name=updateDelivery", which was previously registered with
                    :meth:`~cern.accsoft.commons.util.jmx.MBeanRegistry.registerMBean`
                logger (org.slf4j.Logger): logger to use (can be :code:`null`)
        
        
        """
        ...

class NameParser:
    """
    public class NameParser extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Parses JMX bean name. Most of the code was taken from `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/management/ObjectName.html?is-external=true>` class. It was
        not possible to simply use `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/management/ObjectName.html?is-external=true>` class itself as
        it does not expose enough information about parsed name.
    """
    def __init__(self): ...
    @staticmethod
    def parseName(string: str) -> 'NameParser.Name': ...
    class Name:
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
