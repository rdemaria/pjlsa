import cern.japc.core
import cern.lsa.domain.settings
import typing



class LsaSelector(cern.japc.core.Selector):
    """
    public interface LsaSelector extends cern.japc.core.Selector
    
        Extension of the JAPC selector that contains, in addition to the usual JAPC information, attributes for the LSA
        :code:`TrimRequest`.
    
    
        Using this selector outside of LSA and/or for other operations than set is meaningless
    """
    def getSettingPart(self) -> cern.lsa.domain.settings.SettingPartEnum:
        """
        
            Also see:
                :code:`TrimRequest.getSettingPart()`
        
        
        """
        ...
    def getTrimDescription(self) -> str:
        """
        
            Also see:
                :code:`TrimRequest.getDescription()`
        
        
        """
        ...

class LsaSelectorBuilder:
    """
    public class LsaSelectorBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder for instances of the :code:`Selector` interface. The typical usage of the builder is following:
    
        .. code-block: java
        
         LsaSelectorBuilder builder = LsaSelectorBuilder.newInstance();
         builder.setContext(myCycle);
         builder.setDescription("A test trim"); // Trim comment
         Selector aSelector = builder.build();
         // Use JAPC...
         parameter.set(aSelector, 10.0);
         
        **Synchronization**
    
    
        This class is not synchronized. It is recommended to create separate instance for each thread. If multiple threads
        access one instance of this class concurrently, it must be synchronized externally.
    """
    def build(self) -> LsaSelector:
        """
            Builds a new instance of :code:`Selector` containing all the options set on the builder
        
            Returns:
                an instance of :code:`Selector`
        
        
        """
        ...
    @staticmethod
    def newInstance() -> 'LsaSelectorBuilder':
        """
            Creates and returns a new instance of the :code:`LsaSelectorBuilder`
        
            Returns:
                a :code:`LsaSelectorBuilder` instance
        
        
        """
        ...
    def setLsaContext(self, drivableContext: cern.lsa.domain.settings.DrivableContext) -> 'LsaSelectorBuilder':
        """
            Sets the LSA Context.
        
        """
        ...
    def setSelector(self, selector: cern.japc.core.Selector) -> 'LsaSelectorBuilder':
        """
            Sets the default JAPC selector.
        
        """
        ...
    def setSettingPart(self, settingPartEnum: cern.lsa.domain.settings.SettingPartEnum) -> 'LsaSelectorBuilder':
        """
        
            Also see:
                :code:`TrimRequest.getSettingPart()`
        
        
        """
        ...
    def setTrimDescription(self, string: str) -> 'LsaSelectorBuilder':
        """
        
            Also see:
                :code:`TrimRequest.getDescription()`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.common.japc")``.

    LsaSelector: typing.Type[LsaSelector]
    LsaSelectorBuilder: typing.Type[LsaSelectorBuilder]
