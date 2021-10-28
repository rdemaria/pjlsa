import cern.accsoft.commons.util.userctx
import cern.lsa.client.common.spi.remoting
import cern.lsa.client.spi.japc
import cern.lsa.client.spi.rba
import typing



class ClientRmiConfig:
    """
    Java class 'cern.lsa.client.spi.ClientRmiConfig'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ClientRmiConfig()
    
    """
    def __init__(self): ...
    def acceleratorServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def adServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def archiveReferenceServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def cacheServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def contextServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def deviceServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def elenaServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def exploitationServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def fidelServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def generationServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def hyperCycleServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def incaServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def invocationIdProvider(self) -> cern.lsa.client.common.spi.remoting.InvocationIdProvider: ...
    def japcServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def knobServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def lhcServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def lktimServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def opticServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def parameterServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def remoteInvocationFactory(self) -> cern.accsoft.commons.util.userctx.ContextAwareRemoteInvocationFactory: ...
    def settingServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def spsServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def timingServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def transactionServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...
    def trimServiceProxy(self) -> cern.lsa.client.common.spi.remoting.LSAServiceAwareRmiProxyFactoryBean: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.spi")``.

    ClientRmiConfig: typing.Type[ClientRmiConfig]
    japc: cern.lsa.client.spi.japc.__module_protocol__
    rba: cern.lsa.client.spi.rba.__module_protocol__
