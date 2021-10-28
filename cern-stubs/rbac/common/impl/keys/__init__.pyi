import cern.rbac.common
import java.security
import java.util
import typing



class KeyStoreLoader:
    """
    Java class 'cern.rbac.common.impl.keys.KeyStoreLoader'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def loadKeyStore(string: str, string2: str) -> java.security.KeyStore: ...
    @staticmethod
    def loadTokenKeyStore(environment: cern.rbac.common.RbacConfiguration.Environment) -> java.security.KeyStore: ...

class RbaKeyStore:
    """
    Java class 'cern.rbac.common.impl.keys.RbaKeyStore'
    
        Extends:
            java.lang.Object
    
      Attributes:
        KEYSTORE_TYPE (java.lang.String): final static field
    
    """
    KEYSTORE_TYPE: typing.ClassVar[str] = ...
    @staticmethod
    def getPublicKeys(environment: cern.rbac.common.RbacConfiguration.Environment) -> java.util.Collection[java.security.PublicKey]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl.keys")``.

    KeyStoreLoader: typing.Type[KeyStoreLoader]
    RbaKeyStore: typing.Type[RbaKeyStore]
