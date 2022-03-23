import cern
import cern.accsoft.commons.domain
import cern.accsoft.commons.util.value
import cern.japc.core
import cern.japc.core.factory
import cern.japc.core.spi.provider
import cern.japc.value
import cern.lsa.client
import cern.lsa.client.reference
import cern.lsa.domain.settings
import java.util
import typing



class ContextResolver:
    """
    public class ContextResolver extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class which provides the means of retrieving :code:`DrivableContext`s for different inputs.
    """
    def __init__(self, parameterService: cern.lsa.client.ParameterService, contextService: cern.lsa.client.ContextService): ...
    def getDrivableContextByUser(self, string: str) -> cern.lsa.domain.settings.DrivableContext:
        """
            Gets a drivable context mapped to the given user.
        
            Parameters:
                selectorId (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a selector id specifying a timing user.
        
            Returns:
                a drivable context mapped to the user.
        
        
        """
        ...
    def getNonMuxDrivableContext(self, set: java.util.Set[str]) -> cern.lsa.domain.settings.DrivableContext: ...
    def getNonMuxDrivableContextForDeviceProperty(self, string: str) -> cern.lsa.domain.settings.DrivableContext:
        """
            Gets non-mux drivable context based on the provided device property.
        
            Parameters:
                deviceAndProperty (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
                a drivable context
        
        
        """
        ...

class InternalReferenceController:
    """
    public interface InternalReferenceController
    
        The controller provides read-only access to LSA references.
    """
    def getReference(self, string: str, drivableContext: cern.lsa.domain.settings.DrivableContext) -> cern.japc.value.SimpleParameterValue:
        """
            Gets the reference value for the given parameter and context.
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a parameter name
                drivableContext (cern.lsa.domain.settings.DrivableContext): a drivable context to use
        
            Returns:
                :code:`SimpleParameterValue` or :code:`null` if the reference doesn't exist
        
            Raises:
                : if:
        
                      - PPM parameter and non-PPM context is specified
                      - non-PPM parameter and PPM context is specified
        
                :class:`~cern.lsa.client.reference.ReferenceException`: if there was a problem with data retrieving
        
        
        """
        ...
    def getReferences(self, set: java.util.Set[str], drivableContext: cern.lsa.domain.settings.DrivableContext) -> java.util.Map[str, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]: ...

class LsaReferenceUpdateListener:
    """
    public interface LsaReferenceUpdateListener
    
        Listener for LSA parameter reference change events.
    """
    def onReferenceChanged(self, lsaReferenceUpdate: 'LsaReferenceUpdate') -> None:
        """
            Callback notifying about LSA parameter reference change.
        
            Parameters:
                referenceUpdate (cern.lsa.client.reference.impl.LsaReferenceUpdate): LSA parameter reference update (never :code:`null`)
        
        
        """
        ...

class LsaReferenceUpdate: ...

class ReferenceControllerImpl(cern.lsa.client.reference.ReferenceController, InternalReferenceController):
    """
    public class ReferenceControllerImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.reference.ReferenceController`, :class:`~cern.lsa.client.reference.impl.InternalReferenceController`
    
        A thread-safe implementation of :class:`~cern.lsa.client.reference.ReferenceController` interface.
    """
    def __init__(self): ...
    def addReferenceListener(self, string: str, selector: cern.japc.core.Selector, referenceListener: cern.lsa.client.reference.ReferenceListener) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.client.reference.ReferenceController.addReferenceListener`
            Adds a :class:`~cern.lsa.client.reference.ReferenceListener`.
        
            Specified by:
                :meth:`~cern.lsa.client.reference.ReferenceController.addReferenceListener`Â in
                interfaceÂ :class:`~cern.lsa.client.reference.ReferenceController`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                selector (cern.japc.core.Selector): selector specifying the timing user
                listener (:class:`~cern.lsa.client.reference.ReferenceListener`): listener
        
        
        """
        ...
    @typing.overload
    def getReference(self, string: str, selector: cern.japc.core.Selector) -> cern.japc.value.SimpleParameterValue:
        """
            Description copied from interface: :meth:`~cern.lsa.client.reference.ReferenceController.getReference`
            Gets the reference value for the given parameter and selector.
        
            Specified by:
                :meth:`~cern.lsa.client.reference.ReferenceController.getReference`Â in
                interfaceÂ :class:`~cern.lsa.client.reference.ReferenceController`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a parameter name
                selector (cern.japc.core.Selector): selector specifying the timing user
        
            Returns:
                :code:`ParameterValue` or :code:`null` if the reference doesn't exist or no context is mapped to the timing user
        
            Description copied from interface: :meth:`~cern.lsa.client.reference.impl.InternalReferenceController.getReference`
            Gets the reference value for the given parameter and context.
        
            Specified by:
                :meth:`~cern.lsa.client.reference.impl.InternalReferenceController.getReference`Â in
                interfaceÂ :class:`~cern.lsa.client.reference.impl.InternalReferenceController`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): a parameter name
                drivableContext (cern.lsa.domain.settings.DrivableContext): a drivable context to use
        
            Returns:
                :code:`SimpleParameterValue` or :code:`null` if the reference doesn't exist
        
        
        """
        ...
    @typing.overload
    def getReference(self, string: str, drivableContext: cern.lsa.domain.settings.DrivableContext) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    def getReferences(self, string: str, collection: typing.Union[java.util.Collection[cern.japc.core.Selector], typing.Sequence[cern.japc.core.Selector]]) -> cern.lsa.client.reference.ParameterReferences: ...
    @typing.overload
    def getReferences(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]], selector: cern.japc.core.Selector) -> java.util.Map[str, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]: ...
    @typing.overload
    def getReferences(self, set: java.util.Set[str], drivableContext: cern.lsa.domain.settings.DrivableContext) -> java.util.Map[str, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]: ...
    def initialize(self) -> None:
        """
            Initializes the controller.
        
            To be called after all the necessary components are injected.
        
        """
        ...
    def removeReferenceListener(self, string: str, selector: cern.japc.core.Selector) -> None:
        """
            Description copied from interface: :meth:`~cern.lsa.client.reference.ReferenceController.removeReferenceListener`
            Removes a :class:`~cern.lsa.client.reference.ReferenceListener`.
        
            Specified by:
                :meth:`~cern.lsa.client.reference.ReferenceController.removeReferenceListener`Â in
                interfaceÂ :class:`~cern.lsa.client.reference.ReferenceController`
        
            Parameters:
                parameterName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): parameter name
                selector (cern.japc.core.Selector): selector specifying the timing user
        
        
        """
        ...
    def setAccelerator(self, cernAccelerator: cern.accsoft.commons.domain.CernAccelerator) -> None: ...
    def setArchiveReferenceService(self, archiveReferenceService: cern.lsa.client.ArchiveReferenceService) -> None:
        """
        
            Parameters:
                archiveReferenceService (cern.lsa.client.ArchiveReferenceService): 
        
        """
        ...
    def setContextService(self, contextService: cern.lsa.client.ContextService) -> None:
        """
        
            Parameters:
                contextService (cern.lsa.client.ContextService): 
        
        """
        ...
    def setDescriptorProvider(self, descriptorProvider: cern.japc.core.spi.provider.DescriptorProvider) -> None:
        """
        
            Parameters:
                descriptorProvider (cern.japc.core.spi.provider.DescriptorProvider): 
        
        """
        ...
    def setParameterFactory(self, parameterFactory: cern.japc.core.factory.ParameterFactory) -> None:
        """
        
            Parameters:
                parameterFactory (cern.japc.core.factory.ParameterFactory): 
        
        """
        ...
    def setParameterService(self, parameterService: cern.lsa.client.ParameterService) -> None:
        """
        
            Parameters:
                parameterService (cern.lsa.client.ParameterService): 
        
        """
        ...

class ReferenceWatcher(LsaReferenceUpdateListener, cern.lsa.client.reference.impl.LsaMappingUpdateListener):
    """
    public class ReferenceWatcher extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.lsa.client.reference.impl.LsaReferenceUpdateListener`
    
        Monitors the changes of LSA parameter references. Supports 2 cases:
    
          - Direct reference modification
          - Reference modification due to the change of the mapping between timing user and LSA context
    """
    @typing.overload
    def __init__(self, internalReferenceController: InternalReferenceController, parameterFactory: cern.japc.core.factory.ParameterFactory, contextService: cern.lsa.client.ContextService): ...
    @typing.overload
    def __init__(self, internalReferenceController: InternalReferenceController, parameterFactory: cern.japc.core.factory.ParameterFactory, contextService: cern.lsa.client.ContextService, set: java.util.Set[cern.accsoft.commons.domain.Accelerator]): ...
    def onLsaMappingChanged(self, lsaMappingUpdate: 'LsaMappingUpdate') -> None: ...
    def onReferenceChanged(self, lsaReferenceUpdate: LsaReferenceUpdate) -> None:
        """
            Description copied from
            interface:Â :meth:`~cern.lsa.client.reference.impl.LsaReferenceUpdateListener.onReferenceChanged`
            Callback notifying about LSA parameter reference change.
        
            Specified by:
                :meth:`~cern.lsa.client.reference.impl.LsaReferenceUpdateListener.onReferenceChanged`Â in
                interfaceÂ :class:`~cern.lsa.client.reference.impl.LsaReferenceUpdateListener`
        
            Parameters:
                referenceUpdate (cern.lsa.client.reference.impl.LsaReferenceUpdate): LSA parameter reference update (never :code:`null`)
        
        
        """
        ...

class LsaMappingUpdate: ...

class LsaMappingUpdateListener: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.reference.impl")``.

    ContextResolver: typing.Type[ContextResolver]
    InternalReferenceController: typing.Type[InternalReferenceController]
    LsaMappingUpdate: typing.Type[LsaMappingUpdate]
    LsaMappingUpdateListener: typing.Type[LsaMappingUpdateListener]
    LsaReferenceUpdate: typing.Type[LsaReferenceUpdate]
    LsaReferenceUpdateListener: typing.Type[LsaReferenceUpdateListener]
    ReferenceControllerImpl: typing.Type[ReferenceControllerImpl]
    ReferenceWatcher: typing.Type[ReferenceWatcher]
