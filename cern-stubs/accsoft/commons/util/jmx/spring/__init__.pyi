import javax.management
import org.springframework.jmx.export
import typing



class ApplicationMBeanExporter(org.springframework.jmx.export.MBeanExporter):
    """
    Java class 'cern.accsoft.commons.util.jmx.spring.ApplicationMBeanExporter'
    
        Extends:
            org.springframework.jmx.export.MBeanExporter
    
      Constructors:
        * ApplicationMBeanExporter()
    
    """
    def __init__(self): ...
    def setServer(self, mBeanServer: javax.management.MBeanServer) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.jmx.spring")``.

    ApplicationMBeanExporter: typing.Type[ApplicationMBeanExporter]
