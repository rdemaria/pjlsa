import cern.rbac.common
import typing



class SerializedTokenFields:
    """
    public interface SerializedTokenFields
    
        This structure represents all the serialized token fields.
    """
    def getApplicationName(self) -> str:
        """
        
            Returns:
                the applicationName
        
        
        """
        ...
    def getApplicationTimeout(self) -> int:
        """
        
            Returns:
                the applicationTimeout
        
        
        """
        ...
    def getAuthenticationTime(self) -> int:
        """
        
            Returns:
                the authenticationTime
        
        
        """
        ...
    def getBody(self) -> typing.List[int]:
        """
        
            Returns:
                the bodySize
        
        
        """
        ...
    def getExpirationTime(self) -> int:
        """
        
            Returns:
                the expirationTime
        
        
        """
        ...
    def getExtraFields(self) -> cern.rbac.common.ExtraFields:
        """
        
            Returns:
                the extraFields
        
        
        """
        ...
    def getLocationAddress(self) -> typing.List[int]:
        """
        
            Returns:
                the locationAddress
        
        
        """
        ...
    def getLocationName(self) -> str:
        """
        
            Returns:
                the locationName
        
        
        """
        ...
    def getRoles(self) -> typing.List[cern.rbac.common.Role]:
        """
        
            Returns:
                the roles
        
        
        """
        ...
    def getSerialId(self) -> int:
        """
        
            Returns:
                the serialId
        
        
        """
        ...
    def getSignature(self) -> typing.List[int]:
        """
        
            Returns:
                the signature
        
        
        """
        ...
    def getUserAccountType(self) -> cern.rbac.common.UserPrincipal.AccountType:
        """
        
            Returns:
                the userAccountType
        
        
        """
        ...
    def getUserEmail(self) -> str:
        """
        
            Returns:
                the userEmail
        
        
        """
        ...
    def getUserFullName(self) -> str:
        """
        
            Returns:
                the userFullName
        
        
        """
        ...
    def getUserName(self) -> str:
        """
        
            Returns:
                the userName
        
        
        """
        ...
    def isApplicationCritical(self) -> bool:
        """
        
            Returns:
                the applicationCritical
        
        
        """
        ...
    def isLocationAuthReq(self) -> bool:
        """
        
            Returns:
                the locationAuthReq
        
        
        """
        ...

class TokenDecoder:
    """
    public interface TokenDecoder
    
        Interface for the token decoder.
    """
    def decode(self, byteArray: typing.List[int]) -> SerializedTokenFields:
        """
            Decode byte array into :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields` object
        
            Parameters:
                encoded (byte[]): Encoded byte array
        
            Returns:
                Newly created :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields` object
        
            Raises:
                : if unable to decode or verify encoded object
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl.serialization.decode")``.

    SerializedTokenFields: typing.Type[SerializedTokenFields]
    TokenDecoder: typing.Type[TokenDecoder]
