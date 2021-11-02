import cern.accsoft.commons.domain
import cern.lsa.domain.cern.optics
import java.util
import typing



class MasterControllerTimingEventFactory:
    """
    public final class MasterControllerTimingEventFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A factory class that provides information about Master Controller timing events for PS and PSB machines.
    
        Also see:
            :class:`~cern.lsa.domain.cern.optics.MasterControllerTimingEvent`
    """
    def getEventsByAccelerator(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.List[cern.lsa.domain.cern.optics.MasterControllerTimingEvent]: ...
    @staticmethod
    def getInstance() -> 'MasterControllerTimingEventFactory':
        """
            Returns the singleton instance of this factory.
        
            Returns:
                singleton instance of this factory.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.cern.optics.factory")``.

    MasterControllerTimingEventFactory: typing.Type[MasterControllerTimingEventFactory]
