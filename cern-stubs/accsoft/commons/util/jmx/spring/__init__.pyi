import javax.management
import org.springframework.jmx.export


class ApplicationMBeanExporter(org.springframework.jmx.export.MBeanExporter):
    def __init__(self): ...
    def setServer(self, mBeanServer: javax.management.MBeanServer) -> None: ...
