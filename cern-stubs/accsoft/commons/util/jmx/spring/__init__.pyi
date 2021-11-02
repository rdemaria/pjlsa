import javax.management
import org.springframework.jmx.export
import typing



class ApplicationMBeanExporter(org.springframework.jmx.export.MBeanExporter):
    """
    public class ApplicationMBeanExporter extends org.springframework.jmx.export.MBeanExporter
    
        Custom implementation of :code:`MBeanExporter` provided by Spring. It redirects registration and name creation to
        :class:`~cern.accsoft.commons.util.jmx.MBeanRegistry`.
    """
    def __init__(self): ...
    def setServer(self, mBeanServer: javax.management.MBeanServer) -> None:
        """
            Wraps given `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/management/MBeanServer.html?is-external=true>` into `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/reflect/Proxy.html?is-external=true>` to intercept
            registration and unregistration requests.
        
            Given `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/javax/management/MBeanServer.html?is-external=true>` is
            discarded in favour of `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/management/ManagementFactory.html?is-external=true#getPlatformMBeanServer()>`.
        
            Overrides:
                :code:`setServer` in class :code:`org.springframework.jmx.support.MBeanRegistrationSupport`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.jmx.spring")``.

    ApplicationMBeanExporter: typing.Type[ApplicationMBeanExporter]
