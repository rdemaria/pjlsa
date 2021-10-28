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
    Java class 'cern.lsa.client.reference.impl.ContextResolver'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ContextResolver(cern.lsa.client.ParameterService, cern.lsa.client.ContextService)
    
    """
    def __init__(self, parameterService: cern.lsa.client.ParameterService, contextService: cern.lsa.client.ContextService): ...
    def getDrivableContextByUser(self, string: str) -> cern.lsa.domain.settings.DrivableContext: ...
    def getNonMuxDrivableContext(self, set: java.util.Set[str]) -> cern.lsa.domain.settings.DrivableContext: ...
    def getNonMuxDrivableContextForDeviceProperty(self, string: str) -> cern.lsa.domain.settings.DrivableContext: ...

class InternalReferenceController:
    """
    Java class 'cern.lsa.client.reference.impl.InternalReferenceController'
    
    """
    def getReference(self, string: str, drivableContext: cern.lsa.domain.settings.DrivableContext) -> cern.japc.value.SimpleParameterValue: ...
    def getReferences(self, set: java.util.Set[str], drivableContext: cern.lsa.domain.settings.DrivableContext) -> java.util.Map[str, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]: ...

class LsaReferenceUpdateListener:
    """
    Java class 'cern.lsa.client.reference.impl.LsaReferenceUpdateListener'
    
    """
    def onReferenceChanged(self, lsaReferenceUpdate: 'LsaReferenceUpdate') -> None: ...

class LsaReferenceUpdate: ...

class ReferenceControllerImpl(cern.lsa.client.reference.ReferenceController, InternalReferenceController):
    """
    Java class 'cern.lsa.client.reference.impl.ReferenceControllerImpl'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.client.reference.ReferenceController,
            cern.lsa.client.reference.impl.InternalReferenceController
    
      Constructors:
        * ReferenceControllerImpl()
    
    """
    def __init__(self): ...
    def addReferenceListener(self, string: str, selector: cern.japc.core.Selector, referenceListener: cern.lsa.client.reference.ReferenceListener) -> None: ...
    @typing.overload
    def getReference(self, string: str, selector: cern.japc.core.Selector) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    def getReference(self, string: str, drivableContext: cern.lsa.domain.settings.DrivableContext) -> cern.japc.value.SimpleParameterValue: ...
    @typing.overload
    def getReferences(self, string: str, collection: typing.Union[java.util.Collection[cern.japc.core.Selector], typing.Sequence[cern.japc.core.Selector]]) -> cern.lsa.client.reference.ParameterReferences: ...
    @typing.overload
    def getReferences(self, collection: typing.Union[java.util.Collection[str], typing.Sequence[str]], selector: cern.japc.core.Selector) -> java.util.Map[str, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]: ...
    @typing.overload
    def getReferences(self, set: java.util.Set[str], drivableContext: cern.lsa.domain.settings.DrivableContext) -> java.util.Map[str, cern.accsoft.commons.util.value.FailSafeValue[cern.japc.value.SimpleParameterValue]]: ...
    def initialize(self) -> None: ...
    def removeReferenceListener(self, string: str, selector: cern.japc.core.Selector) -> None: ...
    def setAccelerator(self, cernAccelerator: cern.accsoft.commons.domain.CernAccelerator) -> None: ...
    def setArchiveReferenceService(self, archiveReferenceService: cern.lsa.client.ArchiveReferenceService) -> None: ...
    def setContextService(self, contextService: cern.lsa.client.ContextService) -> None: ...
    def setDescriptorProvider(self, descriptorProvider: cern.japc.core.spi.provider.DescriptorProvider) -> None: ...
    def setParameterFactory(self, parameterFactory: cern.japc.core.factory.ParameterFactory) -> None: ...
    def setParameterService(self, parameterService: cern.lsa.client.ParameterService) -> None: ...

class ReferenceWatcher(LsaReferenceUpdateListener, cern.lsa.client.reference.impl.LsaMappingUpdateListener):
    """
    Java class 'cern.lsa.client.reference.impl.ReferenceWatcher'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.lsa.client.reference.impl.LsaReferenceUpdateListener,
            cern.lsa.client.reference.impl.LsaMappingUpdateListener
    
      Constructors:
        * ReferenceWatcher(cern.lsa.client.reference.impl.InternalReferenceController, cern.japc.core.factory.ParameterFactory, cern.lsa.client.ContextService, java.util.Set)
        * ReferenceWatcher(cern.lsa.client.reference.impl.InternalReferenceController, cern.japc.core.factory.ParameterFactory, cern.lsa.client.ContextService)
    
    """
    @typing.overload
    def __init__(self, internalReferenceController: InternalReferenceController, parameterFactory: cern.japc.core.factory.ParameterFactory, contextService: cern.lsa.client.ContextService): ...
    @typing.overload
    def __init__(self, internalReferenceController: InternalReferenceController, parameterFactory: cern.japc.core.factory.ParameterFactory, contextService: cern.lsa.client.ContextService, set: java.util.Set[cern.accsoft.commons.domain.Accelerator]): ...
    def onLsaMappingChanged(self, lsaMappingUpdate: 'LsaMappingUpdate') -> None: ...
    def onReferenceChanged(self, lsaReferenceUpdate: LsaReferenceUpdate) -> None: ...

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
