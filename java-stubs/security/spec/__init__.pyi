import java.lang
import java.math
import java.security
import java.security.interfaces
import typing



class AlgorithmParameterSpec: ...

class ECField:
    """
    Java class 'java.security.spec.ECField'
    
    """
    def getFieldSize(self) -> int: ...

class ECPoint:
    """
    Java class 'java.security.spec.ECPoint'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ECPoint(java.math.BigInteger, java.math.BigInteger)
    
      Attributes:
        POINT_INFINITY (java.security.spec.ECPoint): final static field
    
    """
    POINT_INFINITY: typing.ClassVar['ECPoint'] = ...
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAffineX(self) -> java.math.BigInteger: ...
    def getAffineY(self) -> java.math.BigInteger: ...
    def hashCode(self) -> int: ...

class EllipticCurve:
    """
    Java class 'java.security.spec.EllipticCurve'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * EllipticCurve(java.security.spec.ECField, java.math.BigInteger, java.math.BigInteger, byte[])
        * EllipticCurve(java.security.spec.ECField, java.math.BigInteger, java.math.BigInteger)
    
    """
    @typing.overload
    def __init__(self, eCField: ECField, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger): ...
    @typing.overload
    def __init__(self, eCField: ECField, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, byteArray: typing.List[int]): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getA(self) -> java.math.BigInteger: ...
    def getB(self) -> java.math.BigInteger: ...
    def getField(self) -> ECField: ...
    def getSeed(self) -> typing.List[int]: ...
    def hashCode(self) -> int: ...

class InvalidKeySpecException(java.security.GeneralSecurityException):
    """
    Java class 'java.security.spec.InvalidKeySpecException'
    
        Extends:
            java.security.GeneralSecurityException
    
      Constructors:
        * InvalidKeySpecException(java.lang.Throwable)
        * InvalidKeySpecException(java.lang.String, java.lang.Throwable)
        * InvalidKeySpecException(java.lang.String)
        * InvalidKeySpecException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class InvalidParameterSpecException(java.security.GeneralSecurityException):
    """
    Java class 'java.security.spec.InvalidParameterSpecException'
    
        Extends:
            java.security.GeneralSecurityException
    
      Constructors:
        * InvalidParameterSpecException()
        * InvalidParameterSpecException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class KeySpec: ...

class RSAOtherPrimeInfo:
    """
    Java class 'java.security.spec.RSAOtherPrimeInfo'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * RSAOtherPrimeInfo(java.math.BigInteger, java.math.BigInteger, java.math.BigInteger)
    
    """
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, bigInteger3: java.math.BigInteger): ...
    def getCrtCoefficient(self) -> java.math.BigInteger: ...
    def getExponent(self) -> java.math.BigInteger: ...
    def getPrime(self) -> java.math.BigInteger: ...

class DSAGenParameterSpec(AlgorithmParameterSpec):
    """
    Java class 'java.security.spec.DSAGenParameterSpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.AlgorithmParameterSpec
    
      Constructors:
        * DSAGenParameterSpec(int, int)
        * DSAGenParameterSpec(int, int, int)
    
    """
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, int3: int): ...
    def getPrimePLength(self) -> int: ...
    def getSeedLength(self) -> int: ...
    def getSubprimeQLength(self) -> int: ...

class DSAParameterSpec(AlgorithmParameterSpec, java.security.interfaces.DSAParams):
    """
    Java class 'java.security.spec.DSAParameterSpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.AlgorithmParameterSpec,
            java.security.interfaces.DSAParams
    
      Constructors:
        * DSAParameterSpec(java.math.BigInteger, java.math.BigInteger, java.math.BigInteger)
    
    """
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, bigInteger3: java.math.BigInteger): ...
    def getG(self) -> java.math.BigInteger: ...
    def getP(self) -> java.math.BigInteger: ...
    def getQ(self) -> java.math.BigInteger: ...

class DSAPrivateKeySpec(KeySpec):
    """
    Java class 'java.security.spec.DSAPrivateKeySpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.KeySpec
    
      Constructors:
        * DSAPrivateKeySpec(java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger)
    
    """
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, bigInteger3: java.math.BigInteger, bigInteger4: java.math.BigInteger): ...
    def getG(self) -> java.math.BigInteger: ...
    def getP(self) -> java.math.BigInteger: ...
    def getQ(self) -> java.math.BigInteger: ...
    def getX(self) -> java.math.BigInteger: ...

class DSAPublicKeySpec(KeySpec):
    """
    Java class 'java.security.spec.DSAPublicKeySpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.KeySpec
    
      Constructors:
        * DSAPublicKeySpec(java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger)
    
    """
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, bigInteger3: java.math.BigInteger, bigInteger4: java.math.BigInteger): ...
    def getG(self) -> java.math.BigInteger: ...
    def getP(self) -> java.math.BigInteger: ...
    def getQ(self) -> java.math.BigInteger: ...
    def getY(self) -> java.math.BigInteger: ...

class ECFieldF2m(ECField):
    """
    Java class 'java.security.spec.ECFieldF2m'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.ECField
    
      Constructors:
        * ECFieldF2m(int, int[])
        * ECFieldF2m(int, java.math.BigInteger)
        * ECFieldF2m(int)
    
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, intArray: typing.List[int]): ...
    @typing.overload
    def __init__(self, int: int, bigInteger: java.math.BigInteger): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getFieldSize(self) -> int: ...
    def getM(self) -> int: ...
    def getMidTermsOfReductionPolynomial(self) -> typing.List[int]: ...
    def getReductionPolynomial(self) -> java.math.BigInteger: ...
    def hashCode(self) -> int: ...

class ECFieldFp(ECField):
    """
    Java class 'java.security.spec.ECFieldFp'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.ECField
    
      Constructors:
        * ECFieldFp(java.math.BigInteger)
    
    """
    def __init__(self, bigInteger: java.math.BigInteger): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getFieldSize(self) -> int: ...
    def getP(self) -> java.math.BigInteger: ...
    def hashCode(self) -> int: ...

class ECParameterSpec(AlgorithmParameterSpec):
    """
    Java class 'java.security.spec.ECParameterSpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.AlgorithmParameterSpec
    
      Constructors:
        * ECParameterSpec(java.security.spec.EllipticCurve, java.security.spec.ECPoint, java.math.BigInteger, int)
    
    """
    def __init__(self, ellipticCurve: EllipticCurve, eCPoint: ECPoint, bigInteger: java.math.BigInteger, int: int): ...
    def getCofactor(self) -> int: ...
    def getCurve(self) -> EllipticCurve: ...
    def getGenerator(self) -> ECPoint: ...
    def getOrder(self) -> java.math.BigInteger: ...

class ECPrivateKeySpec(KeySpec):
    """
    Java class 'java.security.spec.ECPrivateKeySpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.KeySpec
    
      Constructors:
        * ECPrivateKeySpec(java.math.BigInteger, java.security.spec.ECParameterSpec)
    
    """
    def __init__(self, bigInteger: java.math.BigInteger, eCParameterSpec: ECParameterSpec): ...
    def getParams(self) -> ECParameterSpec: ...
    def getS(self) -> java.math.BigInteger: ...

class ECPublicKeySpec(KeySpec):
    """
    Java class 'java.security.spec.ECPublicKeySpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.KeySpec
    
      Constructors:
        * ECPublicKeySpec(java.security.spec.ECPoint, java.security.spec.ECParameterSpec)
    
    """
    def __init__(self, eCPoint: ECPoint, eCParameterSpec: ECParameterSpec): ...
    def getParams(self) -> ECParameterSpec: ...
    def getW(self) -> ECPoint: ...

class EncodedKeySpec(KeySpec):
    """
    Java class 'java.security.spec.EncodedKeySpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.KeySpec
    
      Constructors:
        * EncodedKeySpec(byte[])
    
    """
    def __init__(self, byteArray: typing.List[int]): ...
    def getAlgorithm(self) -> str: ...
    def getEncoded(self) -> typing.List[int]: ...
    def getFormat(self) -> str: ...

class MGF1ParameterSpec(AlgorithmParameterSpec):
    """
    Java class 'java.security.spec.MGF1ParameterSpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.AlgorithmParameterSpec
    
      Constructors:
        * MGF1ParameterSpec(java.lang.String)
    
      Attributes:
        SHA1 (java.security.spec.MGF1ParameterSpec): final static field
        SHA224 (java.security.spec.MGF1ParameterSpec): final static field
        SHA256 (java.security.spec.MGF1ParameterSpec): final static field
        SHA384 (java.security.spec.MGF1ParameterSpec): final static field
        SHA512 (java.security.spec.MGF1ParameterSpec): final static field
        SHA512_224 (java.security.spec.MGF1ParameterSpec): final static field
        SHA512_256 (java.security.spec.MGF1ParameterSpec): final static field
    
    """
    SHA1: typing.ClassVar['MGF1ParameterSpec'] = ...
    SHA224: typing.ClassVar['MGF1ParameterSpec'] = ...
    SHA256: typing.ClassVar['MGF1ParameterSpec'] = ...
    SHA384: typing.ClassVar['MGF1ParameterSpec'] = ...
    SHA512: typing.ClassVar['MGF1ParameterSpec'] = ...
    SHA512_224: typing.ClassVar['MGF1ParameterSpec'] = ...
    SHA512_256: typing.ClassVar['MGF1ParameterSpec'] = ...
    def __init__(self, string: str): ...
    def getDigestAlgorithm(self) -> str: ...

class NamedParameterSpec(AlgorithmParameterSpec):
    """
    Java class 'java.security.spec.NamedParameterSpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.AlgorithmParameterSpec
    
      Constructors:
        * NamedParameterSpec(java.lang.String)
    
      Attributes:
        X25519 (java.security.spec.NamedParameterSpec): final static field
        X448 (java.security.spec.NamedParameterSpec): final static field
    
    """
    X25519: typing.ClassVar['NamedParameterSpec'] = ...
    X448: typing.ClassVar['NamedParameterSpec'] = ...
    def __init__(self, string: str): ...
    def getName(self) -> str: ...

class PSSParameterSpec(AlgorithmParameterSpec):
    """
    Java class 'java.security.spec.PSSParameterSpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.AlgorithmParameterSpec
    
      Constructors:
        * PSSParameterSpec(int)
        * PSSParameterSpec(java.lang.String, java.lang.String, java.security.spec.AlgorithmParameterSpec, int, int)
    
      Attributes:
        TRAILER_FIELD_BC (int): final static field
        DEFAULT (java.security.spec.PSSParameterSpec): final static field
    
    """
    TRAILER_FIELD_BC: typing.ClassVar[int] = ...
    DEFAULT: typing.ClassVar['PSSParameterSpec'] = ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, string: str, string2: str, algorithmParameterSpec: AlgorithmParameterSpec, int: int, int2: int): ...
    def getDigestAlgorithm(self) -> str: ...
    def getMGFAlgorithm(self) -> str: ...
    def getMGFParameters(self) -> AlgorithmParameterSpec: ...
    def getSaltLength(self) -> int: ...
    def getTrailerField(self) -> int: ...

class RSAKeyGenParameterSpec(AlgorithmParameterSpec):
    """
    Java class 'java.security.spec.RSAKeyGenParameterSpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.AlgorithmParameterSpec
    
      Constructors:
        * RSAKeyGenParameterSpec(int, java.math.BigInteger)
        * RSAKeyGenParameterSpec(int, java.math.BigInteger, java.security.spec.AlgorithmParameterSpec)
    
      Attributes:
        F0 (java.math.BigInteger): final static field
        F4 (java.math.BigInteger): final static field
    
    """
    F0: typing.ClassVar[java.math.BigInteger] = ...
    F4: typing.ClassVar[java.math.BigInteger] = ...
    @typing.overload
    def __init__(self, int: int, bigInteger: java.math.BigInteger): ...
    @typing.overload
    def __init__(self, int: int, bigInteger: java.math.BigInteger, algorithmParameterSpec: AlgorithmParameterSpec): ...
    def getKeyParams(self) -> AlgorithmParameterSpec: ...
    def getKeysize(self) -> int: ...
    def getPublicExponent(self) -> java.math.BigInteger: ...

class RSAPrivateKeySpec(KeySpec):
    """
    Java class 'java.security.spec.RSAPrivateKeySpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.KeySpec
    
      Constructors:
        * RSAPrivateKeySpec(java.math.BigInteger, java.math.BigInteger)
        * RSAPrivateKeySpec(java.math.BigInteger, java.math.BigInteger, java.security.spec.AlgorithmParameterSpec)
    
    """
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, algorithmParameterSpec: AlgorithmParameterSpec): ...
    def getModulus(self) -> java.math.BigInteger: ...
    def getParams(self) -> AlgorithmParameterSpec: ...
    def getPrivateExponent(self) -> java.math.BigInteger: ...

class RSAPublicKeySpec(KeySpec):
    """
    Java class 'java.security.spec.RSAPublicKeySpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.KeySpec
    
      Constructors:
        * RSAPublicKeySpec(java.math.BigInteger, java.math.BigInteger)
        * RSAPublicKeySpec(java.math.BigInteger, java.math.BigInteger, java.security.spec.AlgorithmParameterSpec)
    
    """
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, algorithmParameterSpec: AlgorithmParameterSpec): ...
    def getModulus(self) -> java.math.BigInteger: ...
    def getParams(self) -> AlgorithmParameterSpec: ...
    def getPublicExponent(self) -> java.math.BigInteger: ...

class XECPrivateKeySpec(KeySpec):
    """
    Java class 'java.security.spec.XECPrivateKeySpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.KeySpec
    
      Constructors:
        * XECPrivateKeySpec(java.security.spec.AlgorithmParameterSpec, byte[])
    
    """
    def __init__(self, algorithmParameterSpec: AlgorithmParameterSpec, byteArray: typing.List[int]): ...
    def getParams(self) -> AlgorithmParameterSpec: ...
    def getScalar(self) -> typing.List[int]: ...

class XECPublicKeySpec(KeySpec):
    """
    Java class 'java.security.spec.XECPublicKeySpec'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.security.spec.KeySpec
    
      Constructors:
        * XECPublicKeySpec(java.security.spec.AlgorithmParameterSpec, java.math.BigInteger)
    
    """
    def __init__(self, algorithmParameterSpec: AlgorithmParameterSpec, bigInteger: java.math.BigInteger): ...
    def getParams(self) -> AlgorithmParameterSpec: ...
    def getU(self) -> java.math.BigInteger: ...

class ECGenParameterSpec(NamedParameterSpec):
    """
    Java class 'java.security.spec.ECGenParameterSpec'
    
        Extends:
            java.security.spec.NamedParameterSpec
    
      Constructors:
        * ECGenParameterSpec(java.lang.String)
    
    """
    def __init__(self, string: str): ...

class PKCS8EncodedKeySpec(EncodedKeySpec):
    """
    Java class 'java.security.spec.PKCS8EncodedKeySpec'
    
        Extends:
            java.security.spec.EncodedKeySpec
    
      Constructors:
        * PKCS8EncodedKeySpec(byte[])
        * PKCS8EncodedKeySpec(byte[], java.lang.String)
    
    """
    @typing.overload
    def __init__(self, byteArray: typing.List[int]): ...
    @typing.overload
    def __init__(self, byteArray: typing.List[int], string: str): ...
    def getEncoded(self) -> typing.List[int]: ...
    def getFormat(self) -> str: ...

class RSAMultiPrimePrivateCrtKeySpec(RSAPrivateKeySpec):
    """
    Java class 'java.security.spec.RSAMultiPrimePrivateCrtKeySpec'
    
        Extends:
            java.security.spec.RSAPrivateKeySpec
    
      Constructors:
        * RSAMultiPrimePrivateCrtKeySpec(java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.security.spec.RSAOtherPrimeInfo[])
        * RSAMultiPrimePrivateCrtKeySpec(java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.security.spec.RSAOtherPrimeInfo[], java.security.spec.AlgorithmParameterSpec)
    
    """
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, bigInteger3: java.math.BigInteger, bigInteger4: java.math.BigInteger, bigInteger5: java.math.BigInteger, bigInteger6: java.math.BigInteger, bigInteger7: java.math.BigInteger, bigInteger8: java.math.BigInteger, rSAOtherPrimeInfoArray: typing.List[RSAOtherPrimeInfo]): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, bigInteger3: java.math.BigInteger, bigInteger4: java.math.BigInteger, bigInteger5: java.math.BigInteger, bigInteger6: java.math.BigInteger, bigInteger7: java.math.BigInteger, bigInteger8: java.math.BigInteger, rSAOtherPrimeInfoArray: typing.List[RSAOtherPrimeInfo], algorithmParameterSpec: AlgorithmParameterSpec): ...
    def getCrtCoefficient(self) -> java.math.BigInteger: ...
    def getOtherPrimeInfo(self) -> typing.List[RSAOtherPrimeInfo]: ...
    def getPrimeExponentP(self) -> java.math.BigInteger: ...
    def getPrimeExponentQ(self) -> java.math.BigInteger: ...
    def getPrimeP(self) -> java.math.BigInteger: ...
    def getPrimeQ(self) -> java.math.BigInteger: ...
    def getPublicExponent(self) -> java.math.BigInteger: ...

class RSAPrivateCrtKeySpec(RSAPrivateKeySpec):
    """
    Java class 'java.security.spec.RSAPrivateCrtKeySpec'
    
        Extends:
            java.security.spec.RSAPrivateKeySpec
    
      Constructors:
        * RSAPrivateCrtKeySpec(java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger)
        * RSAPrivateCrtKeySpec(java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.math.BigInteger, java.security.spec.AlgorithmParameterSpec)
    
    """
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, bigInteger3: java.math.BigInteger, bigInteger4: java.math.BigInteger, bigInteger5: java.math.BigInteger, bigInteger6: java.math.BigInteger, bigInteger7: java.math.BigInteger, bigInteger8: java.math.BigInteger): ...
    @typing.overload
    def __init__(self, bigInteger: java.math.BigInteger, bigInteger2: java.math.BigInteger, bigInteger3: java.math.BigInteger, bigInteger4: java.math.BigInteger, bigInteger5: java.math.BigInteger, bigInteger6: java.math.BigInteger, bigInteger7: java.math.BigInteger, bigInteger8: java.math.BigInteger, algorithmParameterSpec: AlgorithmParameterSpec): ...
    def getCrtCoefficient(self) -> java.math.BigInteger: ...
    def getPrimeExponentP(self) -> java.math.BigInteger: ...
    def getPrimeExponentQ(self) -> java.math.BigInteger: ...
    def getPrimeP(self) -> java.math.BigInteger: ...
    def getPrimeQ(self) -> java.math.BigInteger: ...
    def getPublicExponent(self) -> java.math.BigInteger: ...

class X509EncodedKeySpec(EncodedKeySpec):
    """
    Java class 'java.security.spec.X509EncodedKeySpec'
    
        Extends:
            java.security.spec.EncodedKeySpec
    
      Constructors:
        * X509EncodedKeySpec(byte[])
        * X509EncodedKeySpec(byte[], java.lang.String)
    
    """
    @typing.overload
    def __init__(self, byteArray: typing.List[int]): ...
    @typing.overload
    def __init__(self, byteArray: typing.List[int], string: str): ...
    def getEncoded(self) -> typing.List[int]: ...
    def getFormat(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.security.spec")``.

    AlgorithmParameterSpec: typing.Type[AlgorithmParameterSpec]
    DSAGenParameterSpec: typing.Type[DSAGenParameterSpec]
    DSAParameterSpec: typing.Type[DSAParameterSpec]
    DSAPrivateKeySpec: typing.Type[DSAPrivateKeySpec]
    DSAPublicKeySpec: typing.Type[DSAPublicKeySpec]
    ECField: typing.Type[ECField]
    ECFieldF2m: typing.Type[ECFieldF2m]
    ECFieldFp: typing.Type[ECFieldFp]
    ECGenParameterSpec: typing.Type[ECGenParameterSpec]
    ECParameterSpec: typing.Type[ECParameterSpec]
    ECPoint: typing.Type[ECPoint]
    ECPrivateKeySpec: typing.Type[ECPrivateKeySpec]
    ECPublicKeySpec: typing.Type[ECPublicKeySpec]
    EllipticCurve: typing.Type[EllipticCurve]
    EncodedKeySpec: typing.Type[EncodedKeySpec]
    InvalidKeySpecException: typing.Type[InvalidKeySpecException]
    InvalidParameterSpecException: typing.Type[InvalidParameterSpecException]
    KeySpec: typing.Type[KeySpec]
    MGF1ParameterSpec: typing.Type[MGF1ParameterSpec]
    NamedParameterSpec: typing.Type[NamedParameterSpec]
    PKCS8EncodedKeySpec: typing.Type[PKCS8EncodedKeySpec]
    PSSParameterSpec: typing.Type[PSSParameterSpec]
    RSAKeyGenParameterSpec: typing.Type[RSAKeyGenParameterSpec]
    RSAMultiPrimePrivateCrtKeySpec: typing.Type[RSAMultiPrimePrivateCrtKeySpec]
    RSAOtherPrimeInfo: typing.Type[RSAOtherPrimeInfo]
    RSAPrivateCrtKeySpec: typing.Type[RSAPrivateCrtKeySpec]
    RSAPrivateKeySpec: typing.Type[RSAPrivateKeySpec]
    RSAPublicKeySpec: typing.Type[RSAPublicKeySpec]
    X509EncodedKeySpec: typing.Type[X509EncodedKeySpec]
    XECPrivateKeySpec: typing.Type[XECPrivateKeySpec]
    XECPublicKeySpec: typing.Type[XECPublicKeySpec]
