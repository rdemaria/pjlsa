import cern.japc.core
import cern.japc.value
import cern.lsa.client.common.japc
import cern.lsa.domain.settings
import java.io
import typing



class LsaSelectorImpl(cern.lsa.client.common.japc.LsaSelector, java.io.Serializable):
    """
    public class LsaSelectorImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.common.japc.LsaSelector`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Implementation of the JAPC selector that contains, in addition to the usual JAPC information, attributes for the LSA
        TrimRequest.
    
    
        This is an internal class. Instantiation must be done using the :class:`~cern.lsa.client.common.japc.LsaSelectorBuilder`
        and never directly with :code:`new`.
    
    
        Using this selector outside of LSA is meaningless
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, selector: cern.japc.core.Selector, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum, string: str): ...
    def getDataFilter(self) -> cern.japc.value.ParameterValue:
        """
        
            Specified by:
                :code:`getDataFilter` in interface :code:`cern.japc.core.Selector`
        
        
        """
        ...
    def getId(self) -> str:
        """
        
            Specified by:
                :code:`getId` in interface :code:`cern.japc.core.Selector`
        
        
        """
        ...
    def getPeriod(self) -> int:
        """
        
            Specified by:
                :code:`getPeriod` in interface :code:`cern.japc.core.Selector`
        
        
        """
        ...
    def getSettingPart(self) -> cern.lsa.domain.settings.SettingPartEnum:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.common.japc.LsaSelector.getSettingPart`Â in
                interfaceÂ :class:`~cern.lsa.client.common.japc.LsaSelector`
        
            Also see:
                :code:`TrimRequest.getSettingPart()`
        
        
        """
        ...
    def getTrimDescription(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.lsa.client.common.japc.LsaSelector.getTrimDescription`Â in
                interfaceÂ :class:`~cern.lsa.client.common.japc.LsaSelector`
        
            Also see:
                :code:`TrimRequest.getDescription()`
        
        
        """
        ...
    def isPeriodic(self) -> bool:
        """
        
            Specified by:
                :code:`isPeriodic` in interface :code:`cern.japc.core.Selector`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.common.spi.japc")``.

    LsaSelectorImpl: typing.Type[LsaSelectorImpl]
