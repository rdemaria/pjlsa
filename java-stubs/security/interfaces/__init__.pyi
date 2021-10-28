import java.math
import java.security
import java.security.spec
import java.util
import typing



class DSAKey:
    """
    Java class 'java.security.interfaces.DSAKey'
    
    """
    def getParams(self) -> 'DSAParams': ...

class DSAKeyPairGenerator:
    """
    Java class 'java.security.interfaces.DSAKeyPairGenerator'
    
    """
    @typing.overload
    def initialize(self, int: int, boolean: bool, secureRandom: java.security.SecureRandom) -> None: ...
    @typing.overload
    def initialize(self, dSAParams: 'DSAParams', secureRandom: java.security.SecureRandom) -> None: ...

class DSAParams:
    """
    Java class 'java.security.interfaces.DSAParams'
    
    """
    def getG(self) -> java.math.BigInteger: ...
    def getP(self) -> java.math.BigInteger: ...
    def getQ(self) -> java.math.BigInteger: ...

class ECKey:
    """
    Java class 'java.security.interfaces.ECKey'
    
    """
    def getParams(self) -> java.security.spec.ECParameterSpec: ...

class RSAKey:
    """
    Java class 'java.security.interfaces.RSAKey'
    
    """
    def getModulus(self) -> java.math.BigInteger: ...
    def getParams(self) -> java.security.spec.AlgorithmParameterSpec: ...

class XECKey:
    """
    Java class 'java.security.interfaces.XECKey'
    
    """
    def getParams(self) -> java.security.spec.AlgorithmParameterSpec: ...

class DSAPrivateKey(DSAKey, java.security.PrivateKey):
    """
    Java class 'java.security.interfaces.DSAPrivateKey'
    
        Interfaces:
            java.security.interfaces.DSAKey, java.security.PrivateKey
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    def getX(self) -> java.math.BigInteger: ...

class DSAPublicKey(DSAKey, java.security.PublicKey):
    """
    Java class 'java.security.interfaces.DSAPublicKey'
    
        Interfaces:
            java.security.interfaces.DSAKey, java.security.PublicKey
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    def getY(self) -> java.math.BigInteger: ...

class ECPrivateKey(java.security.PrivateKey, ECKey):
    """
    Java class 'java.security.interfaces.ECPrivateKey'
    
        Interfaces:
            java.security.PrivateKey, java.security.interfaces.ECKey
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    def getS(self) -> java.math.BigInteger: ...

class ECPublicKey(java.security.PublicKey, ECKey):
    """
    Java class 'java.security.interfaces.ECPublicKey'
    
        Interfaces:
            java.security.PublicKey, java.security.interfaces.ECKey
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    def getW(self) -> java.security.spec.ECPoint: ...

class RSAPrivateKey(java.security.PrivateKey, RSAKey):
    """
    Java class 'java.security.interfaces.RSAPrivateKey'
    
        Interfaces:
            java.security.PrivateKey, java.security.interfaces.RSAKey
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    def getPrivateExponent(self) -> java.math.BigInteger: ...

class RSAPublicKey(java.security.PublicKey, RSAKey):
    """
    Java class 'java.security.interfaces.RSAPublicKey'
    
        Interfaces:
            java.security.PublicKey, java.security.interfaces.RSAKey
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    def getPublicExponent(self) -> java.math.BigInteger: ...

class XECPrivateKey(XECKey, java.security.PrivateKey):
    """
    Java class 'java.security.interfaces.XECPrivateKey'
    
        Interfaces:
            java.security.interfaces.XECKey, java.security.PrivateKey
    
    """
    def getScalar(self) -> java.util.Optional[typing.List[int]]: ...

class XECPublicKey(XECKey, java.security.PublicKey):
    """
    Java class 'java.security.interfaces.XECPublicKey'
    
        Interfaces:
            java.security.interfaces.XECKey, java.security.PublicKey
    
    """
    def getU(self) -> java.math.BigInteger: ...

class RSAMultiPrimePrivateCrtKey(RSAPrivateKey):
    """
    Java class 'java.security.interfaces.RSAMultiPrimePrivateCrtKey'
    
        Interfaces:
            java.security.interfaces.RSAPrivateKey
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    def getCrtCoefficient(self) -> java.math.BigInteger: ...
    def getOtherPrimeInfo(self) -> typing.List[java.security.spec.RSAOtherPrimeInfo]: ...
    def getPrimeExponentP(self) -> java.math.BigInteger: ...
    def getPrimeExponentQ(self) -> java.math.BigInteger: ...
    def getPrimeP(self) -> java.math.BigInteger: ...
    def getPrimeQ(self) -> java.math.BigInteger: ...
    def getPublicExponent(self) -> java.math.BigInteger: ...

class RSAPrivateCrtKey(RSAPrivateKey):
    """
    Java class 'java.security.interfaces.RSAPrivateCrtKey'
    
        Interfaces:
            java.security.interfaces.RSAPrivateKey
    
      Attributes:
        serialVersionUID (long): final static field
    
    """
    serialVersionUID: typing.ClassVar[int] = ...
    def getCrtCoefficient(self) -> java.math.BigInteger: ...
    def getPrimeExponentP(self) -> java.math.BigInteger: ...
    def getPrimeExponentQ(self) -> java.math.BigInteger: ...
    def getPrimeP(self) -> java.math.BigInteger: ...
    def getPrimeQ(self) -> java.math.BigInteger: ...
    def getPublicExponent(self) -> java.math.BigInteger: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.security.interfaces")``.

    DSAKey: typing.Type[DSAKey]
    DSAKeyPairGenerator: typing.Type[DSAKeyPairGenerator]
    DSAParams: typing.Type[DSAParams]
    DSAPrivateKey: typing.Type[DSAPrivateKey]
    DSAPublicKey: typing.Type[DSAPublicKey]
    ECKey: typing.Type[ECKey]
    ECPrivateKey: typing.Type[ECPrivateKey]
    ECPublicKey: typing.Type[ECPublicKey]
    RSAKey: typing.Type[RSAKey]
    RSAMultiPrimePrivateCrtKey: typing.Type[RSAMultiPrimePrivateCrtKey]
    RSAPrivateCrtKey: typing.Type[RSAPrivateCrtKey]
    RSAPrivateKey: typing.Type[RSAPrivateKey]
    RSAPublicKey: typing.Type[RSAPublicKey]
    XECKey: typing.Type[XECKey]
    XECPrivateKey: typing.Type[XECPrivateKey]
    XECPublicKey: typing.Type[XECPublicKey]
