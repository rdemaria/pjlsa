from typing import List as _py_List
from typing import ClassVar as _py_ClassVar
from typing import overload
import cern.rbac.common
import java.security


class TokenSerialization:
    SIGNATURE_LENGTH_SIZE: _py_ClassVar[int] = ...
    TOKEN_LENGTH_SIZE: _py_ClassVar[int] = ...
    SERIAL_ID: _py_ClassVar[str] = ...
    AUTHENTICATION_TIME: _py_ClassVar[str] = ...
    EXPIRATION_TIME: _py_ClassVar[str] = ...
    APPLICATION_NAME: _py_ClassVar[str] = ...
    APPLICATION_CRITICAL: _py_ClassVar[str] = ...
    APPLICATION_TIMEOUT: _py_ClassVar[str] = ...
    LOCATION_NAME: _py_ClassVar[str] = ...
    LOCATION_ADDRESS: _py_ClassVar[str] = ...
    LOCATION_AUTH_REQ: _py_ClassVar[str] = ...
    USER_NAME: _py_ClassVar[str] = ...
    USER_FULLNAME: _py_ClassVar[str] = ...
    USER_EMAIL: _py_ClassVar[str] = ...
    USER_ACCOUNT_TYPE: _py_ClassVar[str] = ...
    USER_ROLES: _py_ClassVar[str] = ...
    USER_ROLES_LIFETIME: _py_ClassVar[str] = ...
    EXTRA_FIELDS: _py_ClassVar[str] = ...
    TOKEN_TYPE: _py_ClassVar[str] = ...
    ROLES_HINT: _py_ClassVar[str] = ...
    ROLES_EXPIRATION: _py_ClassVar[str] = ...
    RENEW_TILL: _py_ClassVar[str] = ...
    @classmethod
    def extractBody(cls, byteArray: _py_List[int]) -> _py_List[int]: ...
    @classmethod
    def extractSignature(cls, byteArray: _py_List[int]) -> _py_List[int]: ...
    @classmethod
    def extractSignatureSize(cls, byteArray: _py_List[int]) -> int: ...
    @classmethod
    @overload
    def getBytes(cls, int: int) -> _py_List[int]: ...
    @classmethod
    @overload
    def getBytes(cls, string: str) -> _py_List[int]: ...
    @classmethod
    def sign(cls, privateKey: java.security.PrivateKey, byteArray: _py_List[int]) -> _py_List[int]: ...
    @classmethod
    def toInt(cls, byteArray: _py_List[int]) -> int: ...
    @overload
    def toString(self) -> str: ...
    @classmethod
    @overload
    def toString(cls, byteArray: _py_List[int]) -> str: ...
    @classmethod
    def verifySignature(cls, byteArray: _py_List[int], byteArray2: _py_List[int], rbacConfiguration: cern.rbac.common.RbacConfiguration) -> bool: ...
