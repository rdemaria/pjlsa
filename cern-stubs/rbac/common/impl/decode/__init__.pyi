import cern.rbac.common
import cern.rbac.common.impl.serialization.decode
import typing



class AbstractTokenDecoder(cern.rbac.common.impl.serialization.decode.TokenDecoder):
    """
    public abstract class AbstractTokenDecoder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.rbac.common.impl.serialization.decode.TokenDecoder`
    
        This class implements functionality of the abstract token decoder. It allows to chain several decoders.
    """
    def __init__(self, rbacConfiguration: cern.rbac.common.RbacConfiguration): ...
    def decode(self, byteArray: typing.List[int]) -> cern.rbac.common.impl.serialization.decode.SerializedTokenFields:
        """
            Description copied from interface: :meth:`~cern.rbac.common.impl.serialization.decode.TokenDecoder.decode`
            Decode byte array into :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields` object
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.TokenDecoder.decode`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.TokenDecoder`
        
            Parameters:
                encoded (byte[]): Encoded byte array
        
            Returns:
                Newly created :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields` object
        
        
        """
        ...

class SerializedTokenFieldsImpl(cern.rbac.common.impl.serialization.decode.SerializedTokenFields):
    """
    public class SerializedTokenFieldsImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
    
        This structure represents all the serialized token fields.
    """
    def __init__(self): ...
    def getApplicationName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getApplicationName`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the applicationName
        
        
        """
        ...
    def getApplicationTimeout(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getApplicationTimeout`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the applicationTimeout
        
        
        """
        ...
    def getAuthenticationTime(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getAuthenticationTime`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the authenticationTime
        
        
        """
        ...
    def getBody(self) -> typing.List[int]:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getBody`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the bodySize
        
        
        """
        ...
    def getExpirationTime(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getExpirationTime`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the expirationTime
        
        
        """
        ...
    def getExtraFields(self) -> cern.rbac.common.ExtraFields:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getExtraFields`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the extraFields
        
        
        """
        ...
    def getLocationAddress(self) -> typing.List[int]:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getLocationAddress`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the locationAddress
        
        
        """
        ...
    def getLocationName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getLocationName`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the locationName
        
        
        """
        ...
    def getRoles(self) -> typing.List[cern.rbac.common.Role]:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getRoles`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the roles
        
        
        """
        ...
    def getSerialId(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getSerialId`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the serialId
        
        
        """
        ...
    def getSignature(self) -> typing.List[int]:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getSignature`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the signature
        
        
        """
        ...
    def getUserAccountType(self) -> cern.rbac.common.UserPrincipal.AccountType:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getUserAccountType`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the userAccountType
        
        
        """
        ...
    def getUserEmail(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getUserEmail`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the userEmail
        
        
        """
        ...
    def getUserFullName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getUserFullName`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the userFullName
        
        
        """
        ...
    def getUserName(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.getUserName`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the userName
        
        
        """
        ...
    def isApplicationCritical(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.isApplicationCritical`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the applicationCritical
        
        
        """
        ...
    def isLocationAuthReq(self) -> bool:
        """
        
            Specified by:
                :meth:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields.isLocationAuthReq`Â in
                interfaceÂ :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields`
        
            Returns:
                the locationAuthReq
        
        
        """
        ...
    def setApplicationCritical(self, boolean: bool) -> None:
        """
        
            Parameters:
                applicationCritical (boolean): the applicationCritical to set
        
        
        """
        ...
    def setApplicationName(self, string: str) -> None:
        """
        
            Parameters:
                applicationName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the applicationName to set
        
        
        """
        ...
    def setApplicationTimeout(self, int: int) -> None:
        """
        
            Parameters:
                applicationTimeout (int): the applicationTimeout to set
        
        
        """
        ...
    def setAuthenticationTime(self, int: int) -> None:
        """
        
            Parameters:
                authenticationTime (int): the authenticationTime to set
        
        
        """
        ...
    def setBody(self, byteArray: typing.List[int]) -> None:
        """
        
            Parameters:
                body (byte[]): the body to set
        
        
        """
        ...
    def setExpirationTime(self, int: int) -> None:
        """
        
            Parameters:
                expirationTime (int): the expirationTime to set
        
        
        """
        ...
    def setExtraFields(self, extraFields: cern.rbac.common.ExtraFields) -> None:
        """
        
            Parameters:
                extraFields (:class:`~cern.rbac.common.ExtraFields`): the extraFields to set
        
        
        """
        ...
    def setLocationAddress(self, byteArray: typing.List[int]) -> None:
        """
        
            Parameters:
                locationAddress (byte[]): the locationAddress to set
        
        
        """
        ...
    def setLocationAuthReq(self, boolean: bool) -> None:
        """
        
            Parameters:
                locationAuthReq (boolean): the locationAuthReq to set
        
        
        """
        ...
    def setLocationName(self, string: str) -> None:
        """
        
            Parameters:
                locationName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the locationName to set
        
        
        """
        ...
    def setRoles(self, roleArray: typing.List[cern.rbac.common.Role]) -> None:
        """
        
            Parameters:
                roles (:class:`~cern.rbac.common.Role`[]): the roles to set
        
        
        """
        ...
    def setSerialId(self, int: int) -> None:
        """
        
            Parameters:
                serialId (int): the serialId to set
        
        
        """
        ...
    def setSignature(self, byteArray: typing.List[int]) -> None:
        """
        
            Parameters:
                signature (byte[]): the signature to set
        
        
        """
        ...
    def setUserAccountType(self, accountType: cern.rbac.common.UserPrincipal.AccountType) -> None:
        """
        
            Parameters:
                userAccountType (:class:`~cern.rbac.common.UserPrincipal.AccountType`): the accountType to set.
        
        
        """
        ...
    def setUserEmail(self, string: str) -> None:
        """
        
            Parameters:
                userEmail (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the userEmail to set
        
        
        """
        ...
    def setUserFullName(self, string: str) -> None:
        """
        
            Parameters:
                userFullName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the userFullName to set
        
        
        """
        ...
    def setUserName(self, string: str) -> None:
        """
        
            Parameters:
                userName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the userName to set
        
        
        """
        ...

class TestTokenDecoderDecorator(AbstractTokenDecoder):
    """
    public class TestTokenDecoderDecorator extends :class:`~cern.rbac.common.impl.decode.AbstractTokenDecoder`
    
        Decorator for the test tokens. The idea to have this decorator is to skip signature verification process for test
        tokens. The actual deserialization is performed by underlying delegate.
    """
    def __init__(self, abstractTokenDecoder: AbstractTokenDecoder): ...

class TextTokenDecoder(AbstractTokenDecoder):
    """
    public class TextTokenDecoder extends :class:`~cern.rbac.common.impl.decode.AbstractTokenDecoder`
    
        Performs decoding from cmw-serialized byte array (TEXT format) into
        :class:`~cern.rbac.common.impl.serialization.decode.SerializedTokenFields` object that is used to reconstruct the token
        on the client side.
    """
    def __init__(self, rbacConfiguration: cern.rbac.common.RbacConfiguration): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.impl.decode")``.

    AbstractTokenDecoder: typing.Type[AbstractTokenDecoder]
    SerializedTokenFieldsImpl: typing.Type[SerializedTokenFieldsImpl]
    TestTokenDecoderDecorator: typing.Type[TestTokenDecoderDecorator]
    TextTokenDecoder: typing.Type[TextTokenDecoder]
