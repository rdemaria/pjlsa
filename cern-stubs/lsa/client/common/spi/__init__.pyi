import cern.lsa.client.common.spi.japc
import cern.lsa.client.common.spi.remoting
import typing



class EnvironmentResolver:
    """
    Java class 'cern.lsa.client.common.spi.EnvironmentResolver'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def isDev() -> bool: ...
    @staticmethod
    def isNext() -> bool: ...
    @staticmethod
    def isPro() -> bool: ...
    @staticmethod
    def isTest() -> bool: ...
    @staticmethod
    def isTestbed() -> bool: ...
    @staticmethod
    def isTwoTier() -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.common.spi")``.

    EnvironmentResolver: typing.Type[EnvironmentResolver]
    japc: cern.lsa.client.common.spi.japc.__module_protocol__
    remoting: cern.lsa.client.common.spi.remoting.__module_protocol__
