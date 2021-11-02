import cern.lsa.client.common.spi.japc
import cern.lsa.client.common.spi.remoting
import typing



class EnvironmentResolver:
    """
    public final class EnvironmentResolver extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Helper to identify what environment the application is running i.e.: PRO, NEXT, DEV
    """
    @staticmethod
    def isDev() -> bool:
        """
            Indicates if the application runs with DEV server (in 3-tier mode) or with DEV database (in 2-tier mode).
        
        """
        ...
    @staticmethod
    def isNext() -> bool:
        """
            Indicates if the application runs with NEXT server (in 3-tier mode) or with NEXT database (in 2-tier mode).
        
        """
        ...
    @staticmethod
    def isPro() -> bool:
        """
            Indicates if the application runs in production environment i.e. on the production database and/or with LSA production
            server.
        
        """
        ...
    @staticmethod
    def isTest() -> bool:
        """
            Indicates if the application runs with TEST database (in 2-tier mode).
        
        """
        ...
    @staticmethod
    def isTestbed() -> bool:
        """
            Indicates if the application runs with TESTBED server (in 3-tier mode) or with TESTBED database (in 2-tier mode).
        
        """
        ...
    @staticmethod
    def isTwoTier() -> bool:
        """
            Indicates if the application runs in 2-tier mode.
        
            Also see:
                :meth:`~cern.lsa.client.common.CommonServiceLocator.isTwoTier`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.common.spi")``.

    EnvironmentResolver: typing.Type[EnvironmentResolver]
    japc: cern.lsa.client.common.spi.japc.__module_protocol__
    remoting: cern.lsa.client.common.spi.remoting.__module_protocol__
