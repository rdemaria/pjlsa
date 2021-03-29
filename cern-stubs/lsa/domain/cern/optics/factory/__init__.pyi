import cern.accsoft.commons.domain
import cern.lsa.domain.cern.optics
import java.util


class MasterControllerTimingEventFactory:
    def getEventsByAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.List[cern.lsa.domain.cern.optics.MasterControllerTimingEvent]: ...
    @staticmethod
    def getInstance() -> 'MasterControllerTimingEventFactory': ...
