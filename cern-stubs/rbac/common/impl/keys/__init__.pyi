import cern.rbac.common
import java.security
import java.util
import typing



class KeyStoreLoader:
    """
    public final class KeyStoreLoader extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def loadKeyStore(string: str, string2: str) -> java.security.KeyStore: ...
    @staticmethod
    def loadTokenKeyStore(environment: cern.rbac.common.RbacConfiguration.Environment) -> java.security.KeyStore: ...

class RbaKeyStore:
    """
    public final class RbaKeyStore extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class provides access to various keystores and passwords stored in local files.
    """
    KEYSTORE_TYPE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` KEYSTORE_TYPE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def getPublicKeys(environment: cern.rbac.common.RbacConfiguration.Environment) -> java.util.Collection[java.security.PublicKey]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl.keys")``.

    KeyStoreLoader: typing.Type[KeyStoreLoader]
    RbaKeyStore: typing.Type[RbaKeyStore]
