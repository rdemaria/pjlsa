import cern.rbac.common
import java.security
import java.util
import typing


class KeyStoreLoader:
    @staticmethod
    def loadKeyStore(string: str, string2: str) -> java.security.KeyStore: ...
    @staticmethod
    def loadTokenKeyStore(environment: cern.rbac.common.RbacConfiguration.Environment) -> java.security.KeyStore: ...

class RbaKeyStore:
    KEYSTORE_TYPE: typing.ClassVar[str] = ...
    @staticmethod
    def getPublicKeys(environment: cern.rbac.common.RbacConfiguration.Environment) -> java.util.Collection[java.security.PublicKey]: ...
