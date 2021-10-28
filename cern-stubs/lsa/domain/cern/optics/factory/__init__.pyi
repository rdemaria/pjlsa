import cern.accsoft.commons.domain
import cern.lsa.domain.cern.optics
import java.util
import typing



class MasterControllerTimingEventFactory:
    """
    Java class 'cern.lsa.domain.cern.optics.factory.MasterControllerTimingEventFactory'
    
        Extends:
            java.lang.Object
    
    """
    def getEventsByAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.List[cern.lsa.domain.cern.optics.MasterControllerTimingEvent]: ...
    @staticmethod
    def getInstance() -> 'MasterControllerTimingEventFactory': ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.optics.factory")``.

    MasterControllerTimingEventFactory: typing.Type[MasterControllerTimingEventFactory]
