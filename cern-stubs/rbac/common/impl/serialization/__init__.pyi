import cern.rbac.common
import cern.rbac.common.impl.serialization.decode
import java.security
import typing



class TokenSerialization:
    """
    public final class TokenSerialization extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class contains several methods for :class:`~cern.rbac.common.RbaToken` serialization purposes. Those methods are
        used by client and server side.
    """
    SIGNATURE_LENGTH_SIZE: typing.ClassVar[int] = ...
    """
    public static final int SIGNATURE_LENGTH_SIZE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    TOKEN_LENGTH_SIZE: typing.ClassVar[int] = ...
    """
    public static final int TOKEN_LENGTH_SIZE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    SERIAL_ID: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SERIAL_ID
    
        Field names for TEXT token format
    
        Also see:
            :meth:`~constant`
    
    
    """
    AUTHENTICATION_TIME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` AUTHENTICATION_TIME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    EXPIRATION_TIME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` EXPIRATION_TIME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    APPLICATION_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` APPLICATION_NAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    APPLICATION_CRITICAL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` APPLICATION_CRITICAL
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    APPLICATION_TIMEOUT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` APPLICATION_TIMEOUT
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    LOCATION_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` LOCATION_NAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    LOCATION_ADDRESS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` LOCATION_ADDRESS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    LOCATION_AUTH_REQ: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` LOCATION_AUTH_REQ
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    USER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` USER_NAME
    
        User principal
    
        Also see:
            :meth:`~constant`
    
    
    """
    USER_FULLNAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` USER_FULLNAME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    USER_EMAIL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` USER_EMAIL
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    USER_ACCOUNT_TYPE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` USER_ACCOUNT_TYPE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    USER_ROLES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` USER_ROLES
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    USER_ROLES_LIFETIME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` USER_ROLES_LIFETIME
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    EXTRA_FIELDS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` EXTRA_FIELDS
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    TOKEN_TYPE: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TOKEN_TYPE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROLES_HINT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ROLES_HINT
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROLES_EXPIRATION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ROLES_EXPIRATION
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def extractBody(byteArray: typing.List[int]) -> typing.List[int]:
        """
            Extracts body from the given token byte array
        
            Parameters:
                encodedToken (byte[]): token byte array
        
            Returns:
                body bytes
        
        
        """
        ...
    @staticmethod
    def extractSignature(byteArray: typing.List[int]) -> typing.List[int]:
        """
            Extracts signature from the given token byte array
        
            Parameters:
                encodedToken (byte[]): token byte array
        
            Returns:
                signature bytes
        
        
        """
        ...
    @staticmethod
    def extractSignatureSize(byteArray: typing.List[int]) -> int:
        """
            Extracts signature size from the given token byte array
        
            Parameters:
                encodedToken (byte[]): token byte array
        
            Returns:
                signature size
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getBytes(int: int) -> typing.List[int]:
        """
            Converts `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` into byte
            array with default encoding
        
            Parameters:
                input (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): String to encode
        
            Returns:
                byte array with default encoding for the given string
        
            Converts integer into byte array with default encoding
        
            Parameters:
                input (int): Integer to encode
        
            Returns:
                byte array with default encoding for the given int
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getBytes(string: str) -> typing.List[int]: ...
    @staticmethod
    def sign(privateKey: java.security.PrivateKey, byteArray: typing.List[int]) -> typing.List[int]:
        """
            Signs message with specified private key and returns signature
        
            Parameters:
                privateKey (`PrivateKey <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/security/PrivateKey.html?is-external=true>`): Private key for signature
                body (byte[]): Body of the message to sign
        
            Returns:
                Signature byte array
        
        
        """
        ...
    @staticmethod
    def toInt(byteArray: typing.List[int]) -> int:
        """
            Converts byte array into integer
        
            Parameters:
                encoded (byte[]): byte array representing integer
        
            Returns:
                Converted integer value
        
        
        """
        ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    @staticmethod
    def toString(byteArray: typing.List[int]) -> str:
        """
            Converts encoded token byte array into `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` representation
        
            Parameters:
                encoded (byte[]): token byte array
        
            Returns:
                String for the given array
        
        
        """
        ...
    @staticmethod
    def verifySignature(byteArray: typing.List[int], byteArray2: typing.List[int], rbacConfiguration: cern.rbac.common.RbacConfiguration) -> bool:
        """
            Default implementation of the verification process.
        
            Parameters:
                body (byte[]): Message body
                signature (byte[]): Signature to verify
                configuration (:class:`~cern.rbac.common.RbacConfiguration`): RBAC runtime configuration
        
            Returns:
                :code:`true` if signature is verified, or :code:`false` otherwise
        
            Raises:
                : if verification fails
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl.serialization")``.

    TokenSerialization: typing.Type[TokenSerialization]
    decode: cern.rbac.common.impl.serialization.decode.__module_protocol__
