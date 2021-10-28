import java
import java.io
import java.lang
import java.net
import java.nio
import java.security.acl
import java.security.cert
import java.security.interfaces
import java.security.spec
import java.util
import java.util.function
import java.util.stream
import javax.crypto
import javax.security.auth
import javax.security.auth.callback
import javax.security.auth.login
import jpype.protocol
import typing



class AccessControlContext:
    """
    Java class 'java.security.AccessControlContext'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AccessControlContext(java.security.AccessControlContext, java.security.DomainCombiner)
        * AccessControlContext(java.security.ProtectionDomain[])
    
    """
    @typing.overload
    def __init__(self, accessControlContext: 'AccessControlContext', domainCombiner: 'DomainCombiner'): ...
    @typing.overload
    def __init__(self, protectionDomainArray: typing.List['ProtectionDomain']): ...
    def checkPermission(self, permission: 'Permission') -> None: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDomainCombiner(self) -> 'DomainCombiner': ...
    def hashCode(self) -> int: ...

class AccessControlException(java.lang.SecurityException):
    """
    Java class 'java.security.AccessControlException'
    
        Extends:
            java.lang.SecurityException
    
      Constructors:
        * AccessControlException(java.lang.String)
        * AccessControlException(java.lang.String, java.security.Permission)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, permission: 'Permission'): ...
    def getPermission(self) -> 'Permission': ...

class AccessController:
    """
    Java class 'java.security.AccessController'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def checkPermission(permission: 'Permission') -> None: ...
    _doPrivileged_0__T = typing.TypeVar('_doPrivileged_0__T')  # <T>
    _doPrivileged_1__T = typing.TypeVar('_doPrivileged_1__T')  # <T>
    _doPrivileged_2__T = typing.TypeVar('_doPrivileged_2__T')  # <T>
    _doPrivileged_3__T = typing.TypeVar('_doPrivileged_3__T')  # <T>
    _doPrivileged_4__T = typing.TypeVar('_doPrivileged_4__T')  # <T>
    _doPrivileged_5__T = typing.TypeVar('_doPrivileged_5__T')  # <T>
    @typing.overload
    @staticmethod
    def doPrivileged(privilegedAction: 'PrivilegedAction'[_doPrivileged_0__T], accessControlContext: AccessControlContext, permissionArray: typing.List['Permission']) -> _doPrivileged_0__T: ...
    @typing.overload
    @staticmethod
    def doPrivileged(privilegedExceptionAction: 'PrivilegedExceptionAction'[_doPrivileged_1__T], accessControlContext: AccessControlContext, permissionArray: typing.List['Permission']) -> _doPrivileged_1__T: ...
    @typing.overload
    @staticmethod
    def doPrivileged(privilegedAction: 'PrivilegedAction'[_doPrivileged_2__T]) -> _doPrivileged_2__T: ...
    @typing.overload
    @staticmethod
    def doPrivileged(privilegedAction: 'PrivilegedAction'[_doPrivileged_3__T], accessControlContext: AccessControlContext) -> _doPrivileged_3__T: ...
    @typing.overload
    @staticmethod
    def doPrivileged(privilegedExceptionAction: 'PrivilegedExceptionAction'[_doPrivileged_4__T]) -> _doPrivileged_4__T: ...
    @typing.overload
    @staticmethod
    def doPrivileged(privilegedExceptionAction: 'PrivilegedExceptionAction'[_doPrivileged_5__T], accessControlContext: AccessControlContext) -> _doPrivileged_5__T: ...
    _doPrivilegedWithCombiner_0__T = typing.TypeVar('_doPrivilegedWithCombiner_0__T')  # <T>
    _doPrivilegedWithCombiner_1__T = typing.TypeVar('_doPrivilegedWithCombiner_1__T')  # <T>
    _doPrivilegedWithCombiner_2__T = typing.TypeVar('_doPrivilegedWithCombiner_2__T')  # <T>
    _doPrivilegedWithCombiner_3__T = typing.TypeVar('_doPrivilegedWithCombiner_3__T')  # <T>
    @typing.overload
    @staticmethod
    def doPrivilegedWithCombiner(privilegedAction: 'PrivilegedAction'[_doPrivilegedWithCombiner_0__T]) -> _doPrivilegedWithCombiner_0__T: ...
    @typing.overload
    @staticmethod
    def doPrivilegedWithCombiner(privilegedAction: 'PrivilegedAction'[_doPrivilegedWithCombiner_1__T], accessControlContext: AccessControlContext, permissionArray: typing.List['Permission']) -> _doPrivilegedWithCombiner_1__T: ...
    @typing.overload
    @staticmethod
    def doPrivilegedWithCombiner(privilegedExceptionAction: 'PrivilegedExceptionAction'[_doPrivilegedWithCombiner_2__T]) -> _doPrivilegedWithCombiner_2__T: ...
    @typing.overload
    @staticmethod
    def doPrivilegedWithCombiner(privilegedExceptionAction: 'PrivilegedExceptionAction'[_doPrivilegedWithCombiner_3__T], accessControlContext: AccessControlContext, permissionArray: typing.List['Permission']) -> _doPrivilegedWithCombiner_3__T: ...
    @staticmethod
    def getContext() -> AccessControlContext: ...

class AlgorithmConstraints:
    """
    Java class 'java.security.AlgorithmConstraints'
    
    """
    @typing.overload
    def permits(self, set: java.util.Set['CryptoPrimitive'], string: str, algorithmParameters: 'AlgorithmParameters') -> bool: ...
    @typing.overload
    def permits(self, set: java.util.Set['CryptoPrimitive'], string: str, key: 'Key', algorithmParameters: 'AlgorithmParameters') -> bool: ...
    @typing.overload
    def permits(self, set: java.util.Set['CryptoPrimitive'], key: 'Key') -> bool: ...

class AlgorithmParameterGenerator:
    """
    Java class 'java.security.AlgorithmParameterGenerator'
    
        Extends:
            java.lang.Object
    
    """
    def generateParameters(self) -> 'AlgorithmParameters': ...
    def getAlgorithm(self) -> str: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'AlgorithmParameterGenerator': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'AlgorithmParameterGenerator': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: 'Provider') -> 'AlgorithmParameterGenerator': ...
    def getProvider(self) -> 'Provider': ...
    @typing.overload
    def init(self, int: int) -> None: ...
    @typing.overload
    def init(self, int: int, secureRandom: 'SecureRandom') -> None: ...
    @typing.overload
    def init(self, algorithmParameterSpec: java.security.spec.AlgorithmParameterSpec) -> None: ...
    @typing.overload
    def init(self, algorithmParameterSpec: java.security.spec.AlgorithmParameterSpec, secureRandom: 'SecureRandom') -> None: ...

class AlgorithmParameterGeneratorSpi:
    """
    Java class 'java.security.AlgorithmParameterGeneratorSpi'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AlgorithmParameterGeneratorSpi()
    
    """
    def __init__(self): ...

class AlgorithmParameters:
    """
    Java class 'java.security.AlgorithmParameters'
    
        Extends:
            java.lang.Object
    
    """
    def getAlgorithm(self) -> str: ...
    @typing.overload
    def getEncoded(self) -> typing.List[int]: ...
    @typing.overload
    def getEncoded(self, string: str) -> typing.List[int]: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'AlgorithmParameters': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'AlgorithmParameters': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: 'Provider') -> 'AlgorithmParameters': ...
    _getParameterSpec__T = typing.TypeVar('_getParameterSpec__T', bound=java.security.spec.AlgorithmParameterSpec)  # <T>
    def getParameterSpec(self, class_: typing.Type[_getParameterSpec__T]) -> _getParameterSpec__T: ...
    def getProvider(self) -> 'Provider': ...
    @typing.overload
    def init(self, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def init(self, byteArray: typing.List[int], string: str) -> None: ...
    @typing.overload
    def init(self, algorithmParameterSpec: java.security.spec.AlgorithmParameterSpec) -> None: ...
    def toString(self) -> str: ...

class AlgorithmParametersSpi:
    """
    Java class 'java.security.AlgorithmParametersSpi'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * AlgorithmParametersSpi()
    
    """
    def __init__(self): ...

class Certificate:
    """
    Java class 'java.security.Certificate'
    
    """
    def decode(self, inputStream: java.io.InputStream) -> None: ...
    def encode(self, outputStream: java.io.OutputStream) -> None: ...
    def getFormat(self) -> str: ...
    def getGuarantor(self) -> 'Principal': ...
    def getPrincipal(self) -> 'Principal': ...
    def getPublicKey(self) -> 'PublicKey': ...
    def toString(self, boolean: bool) -> str: ...

class CodeSigner(java.io.Serializable):
    """
    Java class 'java.security.CodeSigner'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * CodeSigner(java.security.cert.CertPath, java.security.Timestamp)
    
    """
    def __init__(self, certPath: java.security.cert.CertPath, timestamp: 'Timestamp'): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getSignerCertPath(self) -> java.security.cert.CertPath: ...
    def getTimestamp(self) -> 'Timestamp': ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class CodeSource(java.io.Serializable):
    """
    Java class 'java.security.CodeSource'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * CodeSource(java.net.URL, java.security.cert.Certificate[])
        * CodeSource(java.net.URL, java.security.CodeSigner[])
    
    """
    @typing.overload
    def __init__(self, uRL: java.net.URL, codeSignerArray: typing.List[CodeSigner]): ...
    @typing.overload
    def __init__(self, uRL: java.net.URL, certificateArray: typing.List[java.security.cert.Certificate]): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getCertificates(self) -> typing.List[java.security.cert.Certificate]: ...
    def getCodeSigners(self) -> typing.List[CodeSigner]: ...
    def getLocation(self) -> java.net.URL: ...
    def hashCode(self) -> int: ...
    def implies(self, codeSource: 'CodeSource') -> bool: ...
    def toString(self) -> str: ...

class CryptoPrimitive(java.lang.Enum['CryptoPrimitive']):
    """
    Java class 'java.security.CryptoPrimitive'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        MESSAGE_DIGEST (java.security.CryptoPrimitive): final static enum constant
        SECURE_RANDOM (java.security.CryptoPrimitive): final static enum constant
        BLOCK_CIPHER (java.security.CryptoPrimitive): final static enum constant
        STREAM_CIPHER (java.security.CryptoPrimitive): final static enum constant
        MAC (java.security.CryptoPrimitive): final static enum constant
        KEY_WRAP (java.security.CryptoPrimitive): final static enum constant
        PUBLIC_KEY_ENCRYPTION (java.security.CryptoPrimitive): final static enum constant
        SIGNATURE (java.security.CryptoPrimitive): final static enum constant
        KEY_ENCAPSULATION (java.security.CryptoPrimitive): final static enum constant
        KEY_AGREEMENT (java.security.CryptoPrimitive): final static enum constant
    
    """
    MESSAGE_DIGEST: typing.ClassVar['CryptoPrimitive'] = ...
    SECURE_RANDOM: typing.ClassVar['CryptoPrimitive'] = ...
    BLOCK_CIPHER: typing.ClassVar['CryptoPrimitive'] = ...
    STREAM_CIPHER: typing.ClassVar['CryptoPrimitive'] = ...
    MAC: typing.ClassVar['CryptoPrimitive'] = ...
    KEY_WRAP: typing.ClassVar['CryptoPrimitive'] = ...
    PUBLIC_KEY_ENCRYPTION: typing.ClassVar['CryptoPrimitive'] = ...
    SIGNATURE: typing.ClassVar['CryptoPrimitive'] = ...
    KEY_ENCAPSULATION: typing.ClassVar['CryptoPrimitive'] = ...
    KEY_AGREEMENT: typing.ClassVar['CryptoPrimitive'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'CryptoPrimitive': ...
    @staticmethod
    def values() -> typing.List['CryptoPrimitive']: ...

class DigestInputStream(java.io.FilterInputStream):
    """
    Java class 'java.security.DigestInputStream'
    
        Extends:
            java.io.FilterInputStream
    
      Constructors:
        * DigestInputStream(java.io.InputStream, java.security.MessageDigest)
    
    """
    def __init__(self, inputStream: java.io.InputStream, messageDigest: 'MessageDigest'): ...
    def getMessageDigest(self) -> 'MessageDigest': ...
    def on(self, boolean: bool) -> None: ...
    @typing.overload
    def read(self, byteArray: typing.List[int]) -> int: ...
    @typing.overload
    def read(self) -> int: ...
    @typing.overload
    def read(self, byteArray: typing.List[int], int: int, int2: int) -> int: ...
    def setMessageDigest(self, messageDigest: 'MessageDigest') -> None: ...
    def toString(self) -> str: ...

class DigestOutputStream(java.io.FilterOutputStream):
    """
    Java class 'java.security.DigestOutputStream'
    
        Extends:
            java.io.FilterOutputStream
    
      Constructors:
        * DigestOutputStream(java.io.OutputStream, java.security.MessageDigest)
    
    """
    def __init__(self, outputStream: java.io.OutputStream, messageDigest: 'MessageDigest'): ...
    def getMessageDigest(self) -> 'MessageDigest': ...
    def on(self, boolean: bool) -> None: ...
    def setMessageDigest(self, messageDigest: 'MessageDigest') -> None: ...
    def toString(self) -> str: ...
    @typing.overload
    def write(self, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def write(self, byteArray: typing.List[int], int: int, int2: int) -> None: ...
    @typing.overload
    def write(self, int: int) -> None: ...

class DomainCombiner:
    """
    Java class 'java.security.DomainCombiner'
    
    """
    def combine(self, protectionDomainArray: typing.List['ProtectionDomain'], protectionDomainArray2: typing.List['ProtectionDomain']) -> typing.List['ProtectionDomain']: ...

class GeneralSecurityException(java.lang.Exception):
    """
    Java class 'java.security.GeneralSecurityException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * GeneralSecurityException(java.lang.Throwable)
        * GeneralSecurityException(java.lang.String, java.lang.Throwable)
        * GeneralSecurityException(java.lang.String)
        * GeneralSecurityException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class Guard:
    """
    Java class 'java.security.Guard'
    
    """
    def checkGuard(self, object: typing.Any) -> None: ...

class GuardedObject(java.io.Serializable):
    """
    Java class 'java.security.GuardedObject'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * GuardedObject(java.lang.Object, java.security.Guard)
    
    """
    def __init__(self, object: typing.Any, guard: Guard): ...
    def getObject(self) -> typing.Any: ...

class InvalidParameterException(java.lang.IllegalArgumentException):
    """
    Java class 'java.security.InvalidParameterException'
    
        Extends:
            java.lang.IllegalArgumentException
    
      Constructors:
        * InvalidParameterException()
        * InvalidParameterException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class Key(java.io.Serializable):
    """
    Java class 'java.security.Key'
    
        Interfaces:
            java.io.Serializable
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    def getAlgorithm(self) -> str: ...
    def getEncoded(self) -> typing.List[int]: ...
    def getFormat(self) -> str: ...

class KeyFactory:
    """
    Java class 'java.security.KeyFactory'
    
        Extends:
            java.lang.Object
    
    """
    def generatePrivate(self, keySpec: java.security.spec.KeySpec) -> 'PrivateKey': ...
    def generatePublic(self, keySpec: java.security.spec.KeySpec) -> 'PublicKey': ...
    def getAlgorithm(self) -> str: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'KeyFactory': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'KeyFactory': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: 'Provider') -> 'KeyFactory': ...
    _getKeySpec__T = typing.TypeVar('_getKeySpec__T', bound=java.security.spec.KeySpec)  # <T>
    def getKeySpec(self, key: Key, class_: typing.Type[_getKeySpec__T]) -> _getKeySpec__T: ...
    def getProvider(self) -> 'Provider': ...
    def translateKey(self, key: Key) -> Key: ...

class KeyFactorySpi:
    """
    Java class 'java.security.KeyFactorySpi'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * KeyFactorySpi()
    
    """
    def __init__(self): ...

class KeyPair(java.io.Serializable):
    """
    Java class 'java.security.KeyPair'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * KeyPair(java.security.PublicKey, java.security.PrivateKey)
    
    """
    def __init__(self, publicKey: 'PublicKey', privateKey: 'PrivateKey'): ...
    def getPrivate(self) -> 'PrivateKey': ...
    def getPublic(self) -> 'PublicKey': ...

class KeyPairGeneratorSpi:
    """
    Java class 'java.security.KeyPairGeneratorSpi'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * KeyPairGeneratorSpi()
    
    """
    def __init__(self): ...
    def generateKeyPair(self) -> KeyPair: ...
    @typing.overload
    def initialize(self, int: int, secureRandom: 'SecureRandom') -> None: ...
    @typing.overload
    def initialize(self, algorithmParameterSpec: java.security.spec.AlgorithmParameterSpec, secureRandom: 'SecureRandom') -> None: ...

class KeyRep(java.io.Serializable):
    """
    Java class 'java.security.KeyRep'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * KeyRep(java.security.KeyRep.Type, java.lang.String, java.lang.String, byte[])
    
    """
    def __init__(self, type: 'KeyRep.Type', string: str, string2: str, byteArray: typing.List[int]): ...
    class Type(java.lang.Enum['KeyRep.Type']):
        """
        Java class 'java.security.KeyRep$Type'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            SECRET (java.security.KeyRep$Type): final static enum constant
            PUBLIC (java.security.KeyRep$Type): final static enum constant
            PRIVATE (java.security.KeyRep$Type): final static enum constant
        
        """
        SECRET: typing.ClassVar['KeyRep.Type'] = ...
        PUBLIC: typing.ClassVar['KeyRep.Type'] = ...
        PRIVATE: typing.ClassVar['KeyRep.Type'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'KeyRep.Type': ...
        @staticmethod
        def values() -> typing.List['KeyRep.Type']: ...

class KeyStoreSpi:
    """
    Java class 'java.security.KeyStoreSpi'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * KeyStoreSpi()
    
    """
    def __init__(self): ...
    def engineAliases(self) -> java.util.Enumeration[str]: ...
    def engineContainsAlias(self, string: str) -> bool: ...
    def engineDeleteEntry(self, string: str) -> None: ...
    def engineEntryInstanceOf(self, string: str, class_: typing.Type['KeyStore.Entry']) -> bool: ...
    def engineGetCertificate(self, string: str) -> java.security.cert.Certificate: ...
    def engineGetCertificateAlias(self, certificate: java.security.cert.Certificate) -> str: ...
    def engineGetCertificateChain(self, string: str) -> typing.List[java.security.cert.Certificate]: ...
    def engineGetCreationDate(self, string: str) -> java.util.Date: ...
    def engineGetEntry(self, string: str, protectionParameter: 'KeyStore.ProtectionParameter') -> 'KeyStore.Entry': ...
    def engineGetKey(self, string: str, charArray: typing.List[str]) -> Key: ...
    def engineIsCertificateEntry(self, string: str) -> bool: ...
    def engineIsKeyEntry(self, string: str) -> bool: ...
    @typing.overload
    def engineLoad(self, inputStream: java.io.InputStream, charArray: typing.List[str]) -> None: ...
    @typing.overload
    def engineLoad(self, loadStoreParameter: 'KeyStore.LoadStoreParameter') -> None: ...
    def engineProbe(self, inputStream: java.io.InputStream) -> bool: ...
    def engineSetCertificateEntry(self, string: str, certificate: java.security.cert.Certificate) -> None: ...
    def engineSetEntry(self, string: str, entry: 'KeyStore.Entry', protectionParameter: 'KeyStore.ProtectionParameter') -> None: ...
    @typing.overload
    def engineSetKeyEntry(self, string: str, byteArray: typing.List[int], certificateArray: typing.List[java.security.cert.Certificate]) -> None: ...
    @typing.overload
    def engineSetKeyEntry(self, string: str, key: Key, charArray: typing.List[str], certificateArray: typing.List[java.security.cert.Certificate]) -> None: ...
    def engineSize(self) -> int: ...
    @typing.overload
    def engineStore(self, outputStream: java.io.OutputStream, charArray: typing.List[str]) -> None: ...
    @typing.overload
    def engineStore(self, loadStoreParameter: 'KeyStore.LoadStoreParameter') -> None: ...

class MessageDigestSpi:
    """
    Java class 'java.security.MessageDigestSpi'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * MessageDigestSpi()
    
    """
    def __init__(self): ...
    def clone(self) -> typing.Any: ...

class PermissionCollection(java.io.Serializable):
    """
    Java class 'java.security.PermissionCollection'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * PermissionCollection()
    
    """
    def __init__(self): ...
    def add(self, permission: 'Permission') -> None: ...
    def elements(self) -> java.util.Enumeration['Permission']: ...
    def elementsAsStream(self) -> java.util.stream.Stream['Permission']: ...
    def implies(self, permission: 'Permission') -> bool: ...
    def isReadOnly(self) -> bool: ...
    def setReadOnly(self) -> None: ...
    def toString(self) -> str: ...

class Policy:
    """
    Java class 'java.security.Policy'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * Policy()
    
      Attributes:
        UNSUPPORTED_EMPTY_COLLECTION (java.security.PermissionCollection): final static field
    
    """
    UNSUPPORTED_EMPTY_COLLECTION: typing.ClassVar[PermissionCollection] = ...
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, parameters: 'Policy.Parameters') -> 'Policy': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, parameters: 'Policy.Parameters', string2: str) -> 'Policy': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, parameters: 'Policy.Parameters', provider: 'Provider') -> 'Policy': ...
    def getParameters(self) -> 'Policy.Parameters': ...
    @typing.overload
    def getPermissions(self, codeSource: CodeSource) -> PermissionCollection: ...
    @typing.overload
    def getPermissions(self, protectionDomain: 'ProtectionDomain') -> PermissionCollection: ...
    @staticmethod
    def getPolicy() -> 'Policy': ...
    def getProvider(self) -> 'Provider': ...
    def getType(self) -> str: ...
    def implies(self, protectionDomain: 'ProtectionDomain', permission: 'Permission') -> bool: ...
    def refresh(self) -> None: ...
    @staticmethod
    def setPolicy(policy: 'Policy') -> None: ...
    class Parameters: ...

class PolicySpi:
    """
    Java class 'java.security.PolicySpi'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * PolicySpi()
    
    """
    def __init__(self): ...

class Principal:
    """
    Java class 'java.security.Principal'
    
    """
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def implies(self, subject: javax.security.auth.Subject) -> bool: ...
    def toString(self) -> str: ...

_PrivilegedAction__T = typing.TypeVar('_PrivilegedAction__T')  # <T>
class PrivilegedAction(typing.Generic[_PrivilegedAction__T]):
    """
    Java class 'java.security.PrivilegedAction'
    
    """
    def run(self) -> _PrivilegedAction__T: ...

class PrivilegedActionException(java.lang.Exception):
    """
    Java class 'java.security.PrivilegedActionException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * PrivilegedActionException(java.lang.Exception)
    
    """
    def __init__(self, exception: java.lang.Exception): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getException(self) -> java.lang.Exception: ...
    def toString(self) -> str: ...

_PrivilegedExceptionAction__T = typing.TypeVar('_PrivilegedExceptionAction__T')  # <T>
class PrivilegedExceptionAction(typing.Generic[_PrivilegedExceptionAction__T]):
    """
    Java class 'java.security.PrivilegedExceptionAction'
    
    """
    def run(self) -> _PrivilegedExceptionAction__T: ...

class ProtectionDomain:
    """
    Java class 'java.security.ProtectionDomain'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ProtectionDomain(java.security.CodeSource, java.security.PermissionCollection)
        * ProtectionDomain(java.security.CodeSource, java.security.PermissionCollection, java.lang.ClassLoader, java.security.Principal[])
    
    """
    @typing.overload
    def __init__(self, codeSource: CodeSource, permissionCollection: PermissionCollection): ...
    @typing.overload
    def __init__(self, codeSource: CodeSource, permissionCollection: PermissionCollection, classLoader: java.lang.ClassLoader, principalArray: typing.List[Principal]): ...
    def getClassLoader(self) -> java.lang.ClassLoader: ...
    def getCodeSource(self) -> CodeSource: ...
    def getPermissions(self) -> PermissionCollection: ...
    def getPrincipals(self) -> typing.List[Principal]: ...
    def implies(self, permission: 'Permission') -> bool: ...
    def staticPermissionsOnly(self) -> bool: ...
    def toString(self) -> str: ...

class Provider(java.util.Properties):
    """
    Java class 'java.security.Provider'
    
        Extends:
            java.util.Properties
    
    """
    def clear(self) -> None: ...
    def compute(self, object: typing.Any, biFunction: typing.Union[java.util.function.BiFunction[typing.Any, typing.Any, typing.Any], typing.Callable[[typing.Any, typing.Any], typing.Any]]) -> typing.Any: ...
    def computeIfAbsent(self, object: typing.Any, function: typing.Union[java.util.function.Function[typing.Any, typing.Any], typing.Callable[[typing.Any], typing.Any]]) -> typing.Any: ...
    def computeIfPresent(self, object: typing.Any, biFunction: typing.Union[java.util.function.BiFunction[typing.Any, typing.Any, typing.Any], typing.Callable[[typing.Any, typing.Any], typing.Any]]) -> typing.Any: ...
    def configure(self, string: str) -> 'Provider': ...
    def elements(self) -> java.util.Enumeration[typing.Any]: ...
    def entrySet(self) -> java.util.Set[java.util.Map.Entry[typing.Any, typing.Any]]: ...
    def forEach(self, biConsumer: typing.Union[java.util.function.BiConsumer[typing.Any, typing.Any], typing.Callable[[typing.Any, typing.Any], None]]) -> None: ...
    def get(self, object: typing.Any) -> typing.Any: ...
    def getInfo(self) -> str: ...
    def getName(self) -> str: ...
    def getOrDefault(self, object: typing.Any, object2: typing.Any) -> typing.Any: ...
    @typing.overload
    def getProperty(self, string: str) -> str: ...
    @typing.overload
    def getProperty(self, string: str, string2: str) -> str: ...
    def getService(self, string: str, string2: str) -> 'Provider.Service': ...
    def getServices(self) -> java.util.Set['Provider.Service']: ...
    def getVersion(self) -> float: ...
    def getVersionStr(self) -> str: ...
    def isConfigured(self) -> bool: ...
    def keySet(self) -> java.util.Set[typing.Any]: ...
    def keys(self) -> java.util.Enumeration[typing.Any]: ...
    @typing.overload
    def load(self, inputStream: java.io.InputStream) -> None: ...
    @typing.overload
    def load(self, reader: java.io.Reader) -> None: ...
    def merge(self, object: typing.Any, object2: typing.Any, biFunction: typing.Union[java.util.function.BiFunction[typing.Any, typing.Any, typing.Any], typing.Callable[[typing.Any, typing.Any], typing.Any]]) -> typing.Any: ...
    def put(self, object: typing.Any, object2: typing.Any) -> typing.Any: ...
    def putAll(self, map: typing.Union[java.util.Map[typing.Any, typing.Any], typing.Mapping[typing.Any, typing.Any]]) -> None: ...
    def putIfAbsent(self, object: typing.Any, object2: typing.Any) -> typing.Any: ...
    @typing.overload
    def remove(self, object: typing.Any, object2: typing.Any) -> bool: ...
    @typing.overload
    def remove(self, object: typing.Any) -> typing.Any: ...
    @typing.overload
    def replace(self, object: typing.Any, object2: typing.Any, object3: typing.Any) -> bool: ...
    @typing.overload
    def replace(self, object: typing.Any, object2: typing.Any) -> typing.Any: ...
    def replaceAll(self, biFunction: typing.Union[java.util.function.BiFunction[typing.Any, typing.Any, typing.Any], typing.Callable[[typing.Any, typing.Any], typing.Any]]) -> None: ...
    def toString(self) -> str: ...
    def values(self) -> java.util.Collection[typing.Any]: ...
    class Service:
        """
        Java class 'java.security.Provider$Service'
        
            Extends:
                java.lang.Object
        
          Constructors:
            * Service(java.security.Provider, java.lang.String, java.lang.String, java.lang.String, java.util.List, java.util.Map)
        
        """
        def __init__(self, provider: 'Provider', string: str, string2: str, string3: str, list: java.util.List[str], map: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]]): ...
        def getAlgorithm(self) -> str: ...
        def getAttribute(self, string: str) -> str: ...
        def getClassName(self) -> str: ...
        def getProvider(self) -> 'Provider': ...
        def getType(self) -> str: ...
        def newInstance(self, object: typing.Any) -> typing.Any: ...
        def supportsParameter(self, object: typing.Any) -> bool: ...
        def toString(self) -> str: ...

class ProviderException(java.lang.RuntimeException):
    """
    Java class 'java.security.ProviderException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * ProviderException(java.lang.Throwable)
        * ProviderException(java.lang.String, java.lang.Throwable)
        * ProviderException(java.lang.String)
        * ProviderException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class SecureClassLoader(java.lang.ClassLoader): ...

class SecureRandom(java.util.Random):
    """
    Java class 'java.security.SecureRandom'
    
        Extends:
            java.util.Random
    
      Constructors:
        * SecureRandom(byte[])
        * SecureRandom()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, byteArray: typing.List[int]): ...
    def generateSeed(self, int: int) -> typing.List[int]: ...
    def getAlgorithm(self) -> str: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'SecureRandom': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'SecureRandom': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: Provider) -> 'SecureRandom': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, secureRandomParameters: 'SecureRandomParameters') -> 'SecureRandom': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, secureRandomParameters: 'SecureRandomParameters', string2: str) -> 'SecureRandom': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, secureRandomParameters: 'SecureRandomParameters', provider: Provider) -> 'SecureRandom': ...
    @staticmethod
    def getInstanceStrong() -> 'SecureRandom': ...
    def getParameters(self) -> 'SecureRandomParameters': ...
    def getProvider(self) -> Provider: ...
    @staticmethod
    def getSeed(int: int) -> typing.List[int]: ...
    @typing.overload
    def nextBytes(self, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def nextBytes(self, byteArray: typing.List[int], secureRandomParameters: 'SecureRandomParameters') -> None: ...
    @typing.overload
    def reseed(self) -> None: ...
    @typing.overload
    def reseed(self, secureRandomParameters: 'SecureRandomParameters') -> None: ...
    @typing.overload
    def setSeed(self, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def setSeed(self, long: int) -> None: ...
    def toString(self) -> str: ...

class SecureRandomParameters: ...

class SecureRandomSpi(java.io.Serializable):
    """
    Java class 'java.security.SecureRandomSpi'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * SecureRandomSpi()
    
    """
    def __init__(self): ...
    def toString(self) -> str: ...

class Security:
    """
    Java class 'java.security.Security'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def addProvider(provider: Provider) -> int: ...
    @staticmethod
    def getAlgorithmProperty(string: str, string2: str) -> str: ...
    @staticmethod
    def getAlgorithms(string: str) -> java.util.Set[str]: ...
    @staticmethod
    def getProperty(string: str) -> str: ...
    @staticmethod
    def getProvider(string: str) -> Provider: ...
    @typing.overload
    @staticmethod
    def getProviders() -> typing.List[Provider]: ...
    @typing.overload
    @staticmethod
    def getProviders(string: str) -> typing.List[Provider]: ...
    @typing.overload
    @staticmethod
    def getProviders(map: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]]) -> typing.List[Provider]: ...
    @staticmethod
    def insertProviderAt(provider: Provider, int: int) -> int: ...
    @staticmethod
    def removeProvider(string: str) -> None: ...
    @staticmethod
    def setProperty(string: str, string2: str) -> None: ...

class SignatureSpi:
    """
    Java class 'java.security.SignatureSpi'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * SignatureSpi()
    
    """
    def __init__(self): ...
    def clone(self) -> typing.Any: ...

class SignedObject(java.io.Serializable):
    """
    Java class 'java.security.SignedObject'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * SignedObject(java.io.Serializable, java.security.PrivateKey, java.security.Signature)
    
      Raises:
        java.io.IOException: from java
        java.security.SignatureException: from java
        java.security.InvalidKeyException: from java
    
    """
    def __init__(self, serializable: java.io.Serializable, privateKey: 'PrivateKey', signature: 'Signature'): ...
    def getAlgorithm(self) -> str: ...
    def getObject(self) -> typing.Any: ...
    def getSignature(self) -> typing.List[int]: ...
    def verify(self, publicKey: 'PublicKey', signature: 'Signature') -> bool: ...

class Timestamp(java.io.Serializable):
    """
    Java class 'java.security.Timestamp'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * Timestamp(java.util.Date, java.security.cert.CertPath)
    
    """
    def __init__(self, date: java.util.Date, certPath: java.security.cert.CertPath): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getSignerCertPath(self) -> java.security.cert.CertPath: ...
    def getTimestamp(self) -> java.util.Date: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

class AuthProvider(Provider):
    """
    Java class 'java.security.AuthProvider'
    
        Extends:
            java.security.Provider
    
    """
    def login(self, subject: javax.security.auth.Subject, callbackHandler: javax.security.auth.callback.CallbackHandler) -> None: ...
    def logout(self) -> None: ...
    def setCallbackHandler(self, callbackHandler: javax.security.auth.callback.CallbackHandler) -> None: ...

class DigestException(GeneralSecurityException):
    """
    Java class 'java.security.DigestException'
    
        Extends:
            java.security.GeneralSecurityException
    
      Constructors:
        * DigestException(java.lang.Throwable)
        * DigestException(java.lang.String, java.lang.Throwable)
        * DigestException(java.lang.String)
        * DigestException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class DrbgParameters:
    """
    Java class 'java.security.DrbgParameters'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def instantiation(int: int, capability: 'DrbgParameters.Capability', byteArray: typing.List[int]) -> 'DrbgParameters.Instantiation': ...
    @staticmethod
    def nextBytes(int: int, boolean: bool, byteArray: typing.List[int]) -> 'DrbgParameters.NextBytes': ...
    @staticmethod
    def reseed(boolean: bool, byteArray: typing.List[int]) -> 'DrbgParameters.Reseed': ...
    class Capability(java.lang.Enum['DrbgParameters.Capability']):
        """
        Java class 'java.security.DrbgParameters$Capability'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            PR_AND_RESEED (java.security.DrbgParameters$Capability): final static enum constant
            RESEED_ONLY (java.security.DrbgParameters$Capability): final static enum constant
            NONE (java.security.DrbgParameters$Capability): final static enum constant
        
        """
        PR_AND_RESEED: typing.ClassVar['DrbgParameters.Capability'] = ...
        RESEED_ONLY: typing.ClassVar['DrbgParameters.Capability'] = ...
        NONE: typing.ClassVar['DrbgParameters.Capability'] = ...
        def supportsPredictionResistance(self) -> bool: ...
        def supportsReseeding(self) -> bool: ...
        def toString(self) -> str: ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'DrbgParameters.Capability': ...
        @staticmethod
        def values() -> typing.List['DrbgParameters.Capability']: ...
    class Instantiation(SecureRandomParameters):
        """
        Java class 'java.security.DrbgParameters$Instantiation'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.security.SecureRandomParameters
        
        """
        def getCapability(self) -> 'DrbgParameters.Capability': ...
        def getPersonalizationString(self) -> typing.List[int]: ...
        def getStrength(self) -> int: ...
        def toString(self) -> str: ...
    class NextBytes(SecureRandomParameters):
        """
        Java class 'java.security.DrbgParameters$NextBytes'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.security.SecureRandomParameters
        
        """
        def getAdditionalInput(self) -> typing.List[int]: ...
        def getPredictionResistance(self) -> bool: ...
        def getStrength(self) -> int: ...
    class Reseed(SecureRandomParameters):
        """
        Java class 'java.security.DrbgParameters$Reseed'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.security.SecureRandomParameters
        
        """
        def getAdditionalInput(self) -> typing.List[int]: ...
        def getPredictionResistance(self) -> bool: ...

class Identity(Principal, java.io.Serializable):
    """
    Java class 'java.security.Identity'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.Principal, java.io.Serializable
    
      Constructors:
        * Identity(java.lang.String)
        * Identity(java.lang.String, java.security.IdentityScope)
    
      Raises:
        java.security.KeyManagementException: from java
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, identityScope: 'IdentityScope'): ...
    def addCertificate(self, certificate: Certificate) -> None: ...
    def certificates(self) -> typing.List[Certificate]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getInfo(self) -> str: ...
    def getName(self) -> str: ...
    def getPublicKey(self) -> 'PublicKey': ...
    def getScope(self) -> 'IdentityScope': ...
    def hashCode(self) -> int: ...
    def removeCertificate(self, certificate: Certificate) -> None: ...
    def setInfo(self, string: str) -> None: ...
    def setPublicKey(self, publicKey: 'PublicKey') -> None: ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    def toString(self, boolean: bool) -> str: ...

class InvalidAlgorithmParameterException(GeneralSecurityException):
    """
    Java class 'java.security.InvalidAlgorithmParameterException'
    
        Extends:
            java.security.GeneralSecurityException
    
      Constructors:
        * InvalidAlgorithmParameterException(java.lang.Throwable)
        * InvalidAlgorithmParameterException(java.lang.String, java.lang.Throwable)
        * InvalidAlgorithmParameterException(java.lang.String)
        * InvalidAlgorithmParameterException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class KeyException(GeneralSecurityException):
    """
    Java class 'java.security.KeyException'
    
        Extends:
            java.security.GeneralSecurityException
    
      Constructors:
        * KeyException(java.lang.Throwable)
        * KeyException(java.lang.String, java.lang.Throwable)
        * KeyException(java.lang.String)
        * KeyException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class KeyPairGenerator(KeyPairGeneratorSpi):
    """
    Java class 'java.security.KeyPairGenerator'
    
        Extends:
            java.security.KeyPairGeneratorSpi
    
    """
    def genKeyPair(self) -> KeyPair: ...
    def generateKeyPair(self) -> KeyPair: ...
    def getAlgorithm(self) -> str: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'KeyPairGenerator': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'KeyPairGenerator': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: Provider) -> 'KeyPairGenerator': ...
    def getProvider(self) -> Provider: ...
    @typing.overload
    def initialize(self, int: int) -> None: ...
    @typing.overload
    def initialize(self, int: int, secureRandom: SecureRandom) -> None: ...
    @typing.overload
    def initialize(self, algorithmParameterSpec: java.security.spec.AlgorithmParameterSpec) -> None: ...
    @typing.overload
    def initialize(self, algorithmParameterSpec: java.security.spec.AlgorithmParameterSpec, secureRandom: SecureRandom) -> None: ...

class KeyStoreException(GeneralSecurityException):
    """
    Java class 'java.security.KeyStoreException'
    
        Extends:
            java.security.GeneralSecurityException
    
      Constructors:
        * KeyStoreException(java.lang.Throwable)
        * KeyStoreException(java.lang.String, java.lang.Throwable)
        * KeyStoreException(java.lang.String)
        * KeyStoreException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class MessageDigest(MessageDigestSpi):
    """
    Java class 'java.security.MessageDigest'
    
        Extends:
            java.security.MessageDigestSpi
    
    """
    def clone(self) -> typing.Any: ...
    @typing.overload
    def digest(self) -> typing.List[int]: ...
    @typing.overload
    def digest(self, byteArray: typing.List[int]) -> typing.List[int]: ...
    @typing.overload
    def digest(self, byteArray: typing.List[int], int: int, int2: int) -> int: ...
    def getAlgorithm(self) -> str: ...
    def getDigestLength(self) -> int: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'MessageDigest': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'MessageDigest': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: Provider) -> 'MessageDigest': ...
    def getProvider(self) -> Provider: ...
    @staticmethod
    def isEqual(byteArray: typing.List[int], byteArray2: typing.List[int]) -> bool: ...
    def reset(self) -> None: ...
    def toString(self) -> str: ...
    @typing.overload
    def update(self, byteBuffer: java.nio.ByteBuffer) -> None: ...
    @typing.overload
    def update(self, byte: int) -> None: ...
    @typing.overload
    def update(self, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def update(self, byteArray: typing.List[int], int: int, int2: int) -> None: ...

class NoSuchAlgorithmException(GeneralSecurityException):
    """
    Java class 'java.security.NoSuchAlgorithmException'
    
        Extends:
            java.security.GeneralSecurityException
    
      Constructors:
        * NoSuchAlgorithmException(java.lang.Throwable)
        * NoSuchAlgorithmException(java.lang.String, java.lang.Throwable)
        * NoSuchAlgorithmException(java.lang.String)
        * NoSuchAlgorithmException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class NoSuchProviderException(GeneralSecurityException):
    """
    Java class 'java.security.NoSuchProviderException'
    
        Extends:
            java.security.GeneralSecurityException
    
      Constructors:
        * NoSuchProviderException()
        * NoSuchProviderException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class Permission(Guard, java.io.Serializable):
    """
    Java class 'java.security.Permission'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.Guard, java.io.Serializable
    
      Constructors:
        * Permission(java.lang.String)
    
    """
    def __init__(self, string: str): ...
    def checkGuard(self, object: typing.Any) -> None: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getActions(self) -> str: ...
    def getName(self) -> str: ...
    def hashCode(self) -> int: ...
    def implies(self, permission: 'Permission') -> bool: ...
    def newPermissionCollection(self) -> PermissionCollection: ...
    def toString(self) -> str: ...

class Permissions(PermissionCollection, java.io.Serializable):
    """
    Java class 'java.security.Permissions'
    
        Extends:
            java.security.PermissionCollection
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * Permissions()
    
    """
    def __init__(self): ...
    def add(self, permission: Permission) -> None: ...
    def elements(self) -> java.util.Enumeration[Permission]: ...
    def implies(self, permission: Permission) -> bool: ...

class PrivateKey(Key, javax.security.auth.Destroyable):
    """
    Java class 'java.security.PrivateKey'
    
        Interfaces:
            java.security.Key, javax.security.auth.Destroyable
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...

class PublicKey(Key):
    """
    Java class 'java.security.PublicKey'
    
        Interfaces:
            java.security.Key
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...

class Signature(SignatureSpi):
    """
    Java class 'java.security.Signature'
    
        Extends:
            java.security.SignatureSpi
    
    """
    def clone(self) -> typing.Any: ...
    def getAlgorithm(self) -> str: ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'Signature': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'Signature': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: Provider) -> 'Signature': ...
    def getParameter(self, string: str) -> typing.Any: ...
    def getParameters(self) -> AlgorithmParameters: ...
    def getProvider(self) -> Provider: ...
    @typing.overload
    def initSign(self, privateKey: PrivateKey) -> None: ...
    @typing.overload
    def initSign(self, privateKey: PrivateKey, secureRandom: SecureRandom) -> None: ...
    @typing.overload
    def initVerify(self, publicKey: PublicKey) -> None: ...
    @typing.overload
    def initVerify(self, certificate: java.security.cert.Certificate) -> None: ...
    @typing.overload
    def setParameter(self, string: str, object: typing.Any) -> None: ...
    @typing.overload
    def setParameter(self, algorithmParameterSpec: java.security.spec.AlgorithmParameterSpec) -> None: ...
    @typing.overload
    def sign(self) -> typing.List[int]: ...
    @typing.overload
    def sign(self, byteArray: typing.List[int], int: int, int2: int) -> int: ...
    def toString(self) -> str: ...
    @typing.overload
    def update(self, byte: int) -> None: ...
    @typing.overload
    def update(self, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def update(self, byteArray: typing.List[int], int: int, int2: int) -> None: ...
    @typing.overload
    def update(self, byteBuffer: java.nio.ByteBuffer) -> None: ...
    @typing.overload
    def verify(self, byteArray: typing.List[int]) -> bool: ...
    @typing.overload
    def verify(self, byteArray: typing.List[int], int: int, int2: int) -> bool: ...

class SignatureException(GeneralSecurityException):
    """
    Java class 'java.security.SignatureException'
    
        Extends:
            java.security.GeneralSecurityException
    
      Constructors:
        * SignatureException(java.lang.Throwable)
        * SignatureException(java.lang.String, java.lang.Throwable)
        * SignatureException(java.lang.String)
        * SignatureException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class URIParameter(Policy.Parameters, javax.security.auth.login.Configuration.Parameters):
    """
    Java class 'java.security.URIParameter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.Policy.Parameters,
            javax.security.auth.login.Configuration.Parameters
    
      Constructors:
        * URIParameter(java.net.URI)
    
    """
    def __init__(self, uRI: java.net.URI): ...
    def getURI(self) -> java.net.URI: ...

class UnrecoverableEntryException(GeneralSecurityException):
    """
    Java class 'java.security.UnrecoverableEntryException'
    
        Extends:
            java.security.GeneralSecurityException
    
      Constructors:
        * UnrecoverableEntryException()
        * UnrecoverableEntryException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class AllPermission(Permission):
    """
    Java class 'java.security.AllPermission'
    
        Extends:
            java.security.Permission
    
      Constructors:
        * AllPermission()
        * AllPermission(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getActions(self) -> str: ...
    def hashCode(self) -> int: ...
    def implies(self, permission: Permission) -> bool: ...
    def newPermissionCollection(self) -> PermissionCollection: ...

class BasicPermission(Permission, java.io.Serializable):
    """
    Java class 'java.security.BasicPermission'
    
        Extends:
            java.security.Permission
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * BasicPermission(java.lang.String, java.lang.String)
        * BasicPermission(java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getActions(self) -> str: ...
    def hashCode(self) -> int: ...
    def implies(self, permission: Permission) -> bool: ...
    def newPermissionCollection(self) -> PermissionCollection: ...

class IdentityScope(Identity):
    """
    Java class 'java.security.IdentityScope'
    
        Extends:
            java.security.Identity
    
      Constructors:
        * IdentityScope(java.lang.String)
        * IdentityScope(java.lang.String, java.security.IdentityScope)
    
      Raises:
        java.security.KeyManagementException: from java
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, identityScope: 'IdentityScope'): ...
    def addIdentity(self, identity: Identity) -> None: ...
    @typing.overload
    def getIdentity(self, string: str) -> Identity: ...
    @typing.overload
    def getIdentity(self, publicKey: PublicKey) -> Identity: ...
    @typing.overload
    def getIdentity(self, principal: Principal) -> Identity: ...
    @staticmethod
    def getSystemScope() -> 'IdentityScope': ...
    def identities(self) -> java.util.Enumeration[Identity]: ...
    def removeIdentity(self, identity: Identity) -> None: ...
    def size(self) -> int: ...
    @typing.overload
    def toString(self, boolean: bool) -> str: ...
    @typing.overload
    def toString(self) -> str: ...

class InvalidKeyException(KeyException):
    """
    Java class 'java.security.InvalidKeyException'
    
        Extends:
            java.security.KeyException
    
      Constructors:
        * InvalidKeyException(java.lang.Throwable)
        * InvalidKeyException(java.lang.String, java.lang.Throwable)
        * InvalidKeyException(java.lang.String)
        * InvalidKeyException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class KeyManagementException(KeyException):
    """
    Java class 'java.security.KeyManagementException'
    
        Extends:
            java.security.KeyException
    
      Constructors:
        * KeyManagementException(java.lang.Throwable)
        * KeyManagementException(java.lang.String, java.lang.Throwable)
        * KeyManagementException(java.lang.String)
        * KeyManagementException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class Signer(Identity):
    """
    Java class 'java.security.Signer'
    
        Extends:
            java.security.Identity
    
      Constructors:
        * Signer(java.lang.String, java.security.IdentityScope)
        * Signer(java.lang.String)
    
      Raises:
        java.security.KeyManagementException: from java
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, identityScope: IdentityScope): ...
    def getPrivateKey(self) -> PrivateKey: ...
    def setKeyPair(self, keyPair: KeyPair) -> None: ...
    @typing.overload
    def toString(self, boolean: bool) -> str: ...
    @typing.overload
    def toString(self) -> str: ...

class UnrecoverableKeyException(UnrecoverableEntryException):
    """
    Java class 'java.security.UnrecoverableKeyException'
    
        Extends:
            java.security.UnrecoverableEntryException
    
      Constructors:
        * UnrecoverableKeyException()
        * UnrecoverableKeyException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class UnresolvedPermission(Permission, java.io.Serializable):
    """
    Java class 'java.security.UnresolvedPermission'
    
        Extends:
            java.security.Permission
    
        Interfaces:
            java.io.Serializable
    
      Constructors:
        * UnresolvedPermission(java.lang.String, java.lang.String, java.lang.String, java.security.cert.Certificate[])
    
    """
    def __init__(self, string: str, string2: str, string3: str, certificateArray: typing.List[java.security.cert.Certificate]): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getActions(self) -> str: ...
    def getUnresolvedActions(self) -> str: ...
    def getUnresolvedCerts(self) -> typing.List[java.security.cert.Certificate]: ...
    def getUnresolvedName(self) -> str: ...
    def getUnresolvedType(self) -> str: ...
    def hashCode(self) -> int: ...
    def implies(self, permission: Permission) -> bool: ...
    def newPermissionCollection(self) -> PermissionCollection: ...
    def toString(self) -> str: ...

class SecurityPermission(BasicPermission):
    """
    Java class 'java.security.SecurityPermission'
    
        Extends:
            java.security.BasicPermission
    
      Constructors:
        * SecurityPermission(java.lang.String)
        * SecurityPermission(java.lang.String, java.lang.String)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...

class DomainLoadStoreParameter(java.security.KeyStore.LoadStoreParameter):
    """
    Java class 'java.security.DomainLoadStoreParameter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.KeyStore.LoadStoreParameter
    
      Constructors:
        * DomainLoadStoreParameter(java.net.URI, java.util.Map)
    
    """
    def __init__(self, uRI: java.net.URI, map: typing.Union[java.util.Map[str, 'KeyStore.ProtectionParameter'], typing.Mapping[str, 'KeyStore.ProtectionParameter']]): ...
    def getConfiguration(self) -> java.net.URI: ...
    def getProtectionParameter(self) -> 'KeyStore.ProtectionParameter': ...
    def getProtectionParams(self) -> java.util.Map[str, 'KeyStore.ProtectionParameter']: ...

class KeyStore:
    """
    Java class 'java.security.KeyStore'
    
        Extends:
            java.lang.Object
    
    """
    def aliases(self) -> java.util.Enumeration[str]: ...
    def containsAlias(self, string: str) -> bool: ...
    def deleteEntry(self, string: str) -> None: ...
    def entryInstanceOf(self, string: str, class_: typing.Type['KeyStore.Entry']) -> bool: ...
    def getCertificate(self, string: str) -> java.security.cert.Certificate: ...
    def getCertificateAlias(self, certificate: java.security.cert.Certificate) -> str: ...
    def getCertificateChain(self, string: str) -> typing.List[java.security.cert.Certificate]: ...
    def getCreationDate(self, string: str) -> java.util.Date: ...
    @staticmethod
    def getDefaultType() -> str: ...
    def getEntry(self, string: str, protectionParameter: 'KeyStore.ProtectionParameter') -> 'KeyStore.Entry': ...
    @typing.overload
    @staticmethod
    def getInstance(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], charArray: typing.List[str]) -> 'KeyStore': ...
    @typing.overload
    @staticmethod
    def getInstance(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], loadStoreParameter: 'KeyStore.LoadStoreParameter') -> 'KeyStore': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str) -> 'KeyStore': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, string2: str) -> 'KeyStore': ...
    @typing.overload
    @staticmethod
    def getInstance(string: str, provider: Provider) -> 'KeyStore': ...
    def getKey(self, string: str, charArray: typing.List[str]) -> Key: ...
    def getProvider(self) -> Provider: ...
    def getType(self) -> str: ...
    def isCertificateEntry(self, string: str) -> bool: ...
    def isKeyEntry(self, string: str) -> bool: ...
    @typing.overload
    def load(self, inputStream: java.io.InputStream, charArray: typing.List[str]) -> None: ...
    @typing.overload
    def load(self, loadStoreParameter: 'KeyStore.LoadStoreParameter') -> None: ...
    def setCertificateEntry(self, string: str, certificate: java.security.cert.Certificate) -> None: ...
    def setEntry(self, string: str, entry: 'KeyStore.Entry', protectionParameter: 'KeyStore.ProtectionParameter') -> None: ...
    @typing.overload
    def setKeyEntry(self, string: str, byteArray: typing.List[int], certificateArray: typing.List[java.security.cert.Certificate]) -> None: ...
    @typing.overload
    def setKeyEntry(self, string: str, key: Key, charArray: typing.List[str], certificateArray: typing.List[java.security.cert.Certificate]) -> None: ...
    def size(self) -> int: ...
    @typing.overload
    def store(self, outputStream: java.io.OutputStream, charArray: typing.List[str]) -> None: ...
    @typing.overload
    def store(self, loadStoreParameter: 'KeyStore.LoadStoreParameter') -> None: ...
    class Builder:
        """
        Java class 'java.security.KeyStore$Builder'
        
            Extends:
                java.lang.Object
        
        """
        def getKeyStore(self) -> 'KeyStore': ...
        def getProtectionParameter(self, string: str) -> 'KeyStore.ProtectionParameter': ...
        @typing.overload
        @staticmethod
        def newInstance(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], protectionParameter: 'KeyStore.ProtectionParameter') -> 'KeyStore.Builder': ...
        @typing.overload
        @staticmethod
        def newInstance(string: str, provider: Provider, file: typing.Union[java.io.File, jpype.protocol.SupportsPath], protectionParameter: 'KeyStore.ProtectionParameter') -> 'KeyStore.Builder': ...
        @typing.overload
        @staticmethod
        def newInstance(string: str, provider: Provider, protectionParameter: 'KeyStore.ProtectionParameter') -> 'KeyStore.Builder': ...
        @typing.overload
        @staticmethod
        def newInstance(keyStore: 'KeyStore', protectionParameter: 'KeyStore.ProtectionParameter') -> 'KeyStore.Builder': ...
    class CallbackHandlerProtection(java.security.KeyStore.ProtectionParameter):
        """
        Java class 'java.security.KeyStore$CallbackHandlerProtection'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.security.KeyStore.ProtectionParameter
        
          Constructors:
            * CallbackHandlerProtection(javax.security.auth.callback.CallbackHandler)
        
        """
        def __init__(self, callbackHandler: javax.security.auth.callback.CallbackHandler): ...
        def getCallbackHandler(self) -> javax.security.auth.callback.CallbackHandler: ...
    class Entry:
        """
        Java class 'java.security.KeyStore$Entry'
        
        """
        def getAttributes(self) -> java.util.Set['KeyStore.Entry.Attribute']: ...
        class Attribute:
            """
            Java class 'java.security.KeyStore$Entry$Attribute'
            
            """
            def getName(self) -> str: ...
            def getValue(self) -> str: ...
    class LoadStoreParameter:
        """
        Java class 'java.security.KeyStore$LoadStoreParameter'
        
        """
        def getProtectionParameter(self) -> 'KeyStore.ProtectionParameter': ...
    class PasswordProtection(java.security.KeyStore.ProtectionParameter, javax.security.auth.Destroyable):
        """
        Java class 'java.security.KeyStore$PasswordProtection'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.security.KeyStore.ProtectionParameter,
                javax.security.auth.Destroyable
        
          Constructors:
            * PasswordProtection(char[])
            * PasswordProtection(char[], java.lang.String, java.security.spec.AlgorithmParameterSpec)
        
        """
        @typing.overload
        def __init__(self, charArray: typing.List[str]): ...
        @typing.overload
        def __init__(self, charArray: typing.List[str], string: str, algorithmParameterSpec: java.security.spec.AlgorithmParameterSpec): ...
        def destroy(self) -> None: ...
        def getPassword(self) -> typing.List[str]: ...
        def getProtectionAlgorithm(self) -> str: ...
        def getProtectionParameters(self) -> java.security.spec.AlgorithmParameterSpec: ...
        def isDestroyed(self) -> bool: ...
    class PrivateKeyEntry(java.security.KeyStore.Entry):
        """
        Java class 'java.security.KeyStore$PrivateKeyEntry'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.security.KeyStore.Entry
        
          Constructors:
            * PrivateKeyEntry(java.security.PrivateKey, java.security.cert.Certificate[])
            * PrivateKeyEntry(java.security.PrivateKey, java.security.cert.Certificate[], java.util.Set)
        
        """
        @typing.overload
        def __init__(self, privateKey: PrivateKey, certificateArray: typing.List[java.security.cert.Certificate]): ...
        @typing.overload
        def __init__(self, privateKey: PrivateKey, certificateArray: typing.List[java.security.cert.Certificate], set: java.util.Set['KeyStore.Entry.Attribute']): ...
        def getAttributes(self) -> java.util.Set['KeyStore.Entry.Attribute']: ...
        def getCertificate(self) -> java.security.cert.Certificate: ...
        def getCertificateChain(self) -> typing.List[java.security.cert.Certificate]: ...
        def getPrivateKey(self) -> PrivateKey: ...
        def toString(self) -> str: ...
    class ProtectionParameter: ...
    class SecretKeyEntry(java.security.KeyStore.Entry):
        """
        Java class 'java.security.KeyStore$SecretKeyEntry'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.security.KeyStore.Entry
        
          Constructors:
            * SecretKeyEntry(javax.crypto.SecretKey)
            * SecretKeyEntry(javax.crypto.SecretKey, java.util.Set)
        
        """
        @typing.overload
        def __init__(self, secretKey: javax.crypto.SecretKey): ...
        @typing.overload
        def __init__(self, secretKey: javax.crypto.SecretKey, set: java.util.Set['KeyStore.Entry.Attribute']): ...
        def getAttributes(self) -> java.util.Set['KeyStore.Entry.Attribute']: ...
        def getSecretKey(self) -> javax.crypto.SecretKey: ...
        def toString(self) -> str: ...
    class TrustedCertificateEntry(java.security.KeyStore.Entry):
        """
        Java class 'java.security.KeyStore$TrustedCertificateEntry'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.security.KeyStore.Entry
        
          Constructors:
            * TrustedCertificateEntry(java.security.cert.Certificate)
            * TrustedCertificateEntry(java.security.cert.Certificate, java.util.Set)
        
        """
        @typing.overload
        def __init__(self, certificate: java.security.cert.Certificate): ...
        @typing.overload
        def __init__(self, certificate: java.security.cert.Certificate, set: java.util.Set['KeyStore.Entry.Attribute']): ...
        def getAttributes(self) -> java.util.Set['KeyStore.Entry.Attribute']: ...
        def getTrustedCertificate(self) -> java.security.cert.Certificate: ...
        def toString(self) -> str: ...

class PKCS12Attribute(KeyStore.Entry.Attribute):
    """
    Java class 'java.security.PKCS12Attribute'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.KeyStore.Entry.Attribute
    
      Constructors:
        * PKCS12Attribute(java.lang.String, java.lang.String)
        * PKCS12Attribute(byte[])
    
    """
    @typing.overload
    def __init__(self, byteArray: typing.List[int]): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getEncoded(self) -> typing.List[int]: ...
    def getName(self) -> str: ...
    def getValue(self) -> str: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.security")``.

    AccessControlContext: typing.Type[AccessControlContext]
    AccessControlException: typing.Type[AccessControlException]
    AccessController: typing.Type[AccessController]
    AlgorithmConstraints: typing.Type[AlgorithmConstraints]
    AlgorithmParameterGenerator: typing.Type[AlgorithmParameterGenerator]
    AlgorithmParameterGeneratorSpi: typing.Type[AlgorithmParameterGeneratorSpi]
    AlgorithmParameters: typing.Type[AlgorithmParameters]
    AlgorithmParametersSpi: typing.Type[AlgorithmParametersSpi]
    AllPermission: typing.Type[AllPermission]
    AuthProvider: typing.Type[AuthProvider]
    BasicPermission: typing.Type[BasicPermission]
    Certificate: typing.Type[Certificate]
    CodeSigner: typing.Type[CodeSigner]
    CodeSource: typing.Type[CodeSource]
    CryptoPrimitive: typing.Type[CryptoPrimitive]
    DigestException: typing.Type[DigestException]
    DigestInputStream: typing.Type[DigestInputStream]
    DigestOutputStream: typing.Type[DigestOutputStream]
    DomainCombiner: typing.Type[DomainCombiner]
    DomainLoadStoreParameter: typing.Type[DomainLoadStoreParameter]
    DrbgParameters: typing.Type[DrbgParameters]
    GeneralSecurityException: typing.Type[GeneralSecurityException]
    Guard: typing.Type[Guard]
    GuardedObject: typing.Type[GuardedObject]
    Identity: typing.Type[Identity]
    IdentityScope: typing.Type[IdentityScope]
    InvalidAlgorithmParameterException: typing.Type[InvalidAlgorithmParameterException]
    InvalidKeyException: typing.Type[InvalidKeyException]
    InvalidParameterException: typing.Type[InvalidParameterException]
    Key: typing.Type[Key]
    KeyException: typing.Type[KeyException]
    KeyFactory: typing.Type[KeyFactory]
    KeyFactorySpi: typing.Type[KeyFactorySpi]
    KeyManagementException: typing.Type[KeyManagementException]
    KeyPair: typing.Type[KeyPair]
    KeyPairGenerator: typing.Type[KeyPairGenerator]
    KeyPairGeneratorSpi: typing.Type[KeyPairGeneratorSpi]
    KeyRep: typing.Type[KeyRep]
    KeyStore: typing.Type[KeyStore]
    KeyStoreException: typing.Type[KeyStoreException]
    KeyStoreSpi: typing.Type[KeyStoreSpi]
    MessageDigest: typing.Type[MessageDigest]
    MessageDigestSpi: typing.Type[MessageDigestSpi]
    NoSuchAlgorithmException: typing.Type[NoSuchAlgorithmException]
    NoSuchProviderException: typing.Type[NoSuchProviderException]
    PKCS12Attribute: typing.Type[PKCS12Attribute]
    Permission: typing.Type[Permission]
    PermissionCollection: typing.Type[PermissionCollection]
    Permissions: typing.Type[Permissions]
    Policy: typing.Type[Policy]
    PolicySpi: typing.Type[PolicySpi]
    Principal: typing.Type[Principal]
    PrivateKey: typing.Type[PrivateKey]
    PrivilegedAction: typing.Type[PrivilegedAction]
    PrivilegedActionException: typing.Type[PrivilegedActionException]
    PrivilegedExceptionAction: typing.Type[PrivilegedExceptionAction]
    ProtectionDomain: typing.Type[ProtectionDomain]
    Provider: typing.Type[Provider]
    ProviderException: typing.Type[ProviderException]
    PublicKey: typing.Type[PublicKey]
    SecureClassLoader: typing.Type[SecureClassLoader]
    SecureRandom: typing.Type[SecureRandom]
    SecureRandomParameters: typing.Type[SecureRandomParameters]
    SecureRandomSpi: typing.Type[SecureRandomSpi]
    Security: typing.Type[Security]
    SecurityPermission: typing.Type[SecurityPermission]
    Signature: typing.Type[Signature]
    SignatureException: typing.Type[SignatureException]
    SignatureSpi: typing.Type[SignatureSpi]
    SignedObject: typing.Type[SignedObject]
    Signer: typing.Type[Signer]
    Timestamp: typing.Type[Timestamp]
    URIParameter: typing.Type[URIParameter]
    UnrecoverableEntryException: typing.Type[UnrecoverableEntryException]
    UnrecoverableKeyException: typing.Type[UnrecoverableKeyException]
    UnresolvedPermission: typing.Type[UnresolvedPermission]
    acl: java.security.acl.__module_protocol__
    cert: java.security.cert.__module_protocol__
    interfaces: java.security.interfaces.__module_protocol__
    spec: java.security.spec.__module_protocol__
