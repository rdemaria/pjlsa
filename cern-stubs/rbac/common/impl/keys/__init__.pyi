from typing import ClassVar as _py_ClassVar
import cern.rbac.common
import java.security
import java.util


class KeyStoreLoader:
    @classmethod
    def loadKeyStore(cls, string: str, string2: str) -> java.security.KeyStore: ...
    @classmethod
    def loadTokenKeyStore(cls, environment: cern.rbac.common.RbacConfiguration.Environment) -> java.security.KeyStore: ...

class RbaKeyStore:
    KEYSTORE_TYPE: _py_ClassVar[str] = ...
    @classmethod
    def getPublicKeys(cls, environment: cern.rbac.common.RbacConfiguration.Environment) -> java.util.Collection[java.security.PublicKey]: ...
