import org.slf4j
import typing



class MBean:
    """
    public interface MBean
    
        General purpose JMX MBean.
    """
    def getDescription(self) -> str:
        """
            Returns MBean description, ex. "JAPC Executor JMX interface".
        
            Returns:
                MBean description
        
        
        """
        ...

class MBeanRegistry:
    """
    public class MBeanRegistry extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Helper class which facilitates the registration of JMX MBeans.
    """
    def __init__(self): ...
    @staticmethod
    def get() -> 'MBeanRegistry':
        """
            Getter for the singleton.
        
            Returns:
                the singleton
        
        
        """
        ...
    def getMBean(self, string: str) -> MBean:
        """
            Get an MBean by name.
        
            Parameters:
                mBeanName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): valid MBean name, ex. "cern.japc:type=core,name=updateDelivery", which was previously registered with
                    :meth:`~cern.japc.core.spi.jmx.MBeanRegistry.registerMBean`
        
        
        """
        ...
    def registerMBean(self, string: str, mBean: MBean, logger: org.slf4j.Logger) -> None:
        """
            Registers an MBean.
        
            Parameters:
                mBeanName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): valid MBean name, ex. "cern.japc:type=core,name=updateDelivery"
                mBean (:class:`~cern.japc.core.spi.jmx.MBean`): MBean implementation to register
                log (org.slf4j.Logger): logger to use
        
        
        """
        ...
    def setJmxAppName(self, string: str) -> None:
        """
            Setter for the application name to be used by JMX in order to distinguish applications running in the same JVM (the case
            of application servers).
        
            Parameters:
                jmxAppName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): JMX application name
        
        
        """
        ...
    def unregisterAll(self, logger: org.slf4j.Logger) -> None:
        """
            Unregisters all the registered MBeans.
        
            Parameters:
                log (org.slf4j.Logger): logger to use
        
        
        """
        ...
    def unregisterMBean(self, string: str, logger: org.slf4j.Logger) -> None:
        """
            Unregisters an MBean.
        
            Parameters:
                mBeanName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): valid MBean name, ex. "cern.japc:type=core,name=updateDelivery", which was previously registered with
                    :meth:`~cern.japc.core.spi.jmx.MBeanRegistry.registerMBean`
                log (org.slf4j.Logger): logger to use
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.jmx")``.

    MBean: typing.Type[MBean]
    MBeanRegistry: typing.Type[MBeanRegistry]
