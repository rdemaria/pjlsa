from typing import List as _py_List
import cern.rbac.common


class SerializedTokenFields:
    def getApplicationName(self) -> str: ...
    def getApplicationTimeout(self) -> int: ...
    def getAuthenticationTime(self) -> int: ...
    def getBody(self) -> _py_List[int]: ...
    def getExpirationTime(self) -> int: ...
    def getExtraFields(self) -> cern.rbac.common.ExtraFields: ...
    def getLocationAddress(self) -> _py_List[int]: ...
    def getLocationName(self) -> str: ...
    def getRoles(self) -> _py_List[cern.rbac.common.Role]: ...
    def getSerialId(self) -> int: ...
    def getSignature(self) -> _py_List[int]: ...
    def getUserAccountType(self) -> cern.rbac.common.UserPrincipal.AccountType: ...
    def getUserEmail(self) -> str: ...
    def getUserFullName(self) -> str: ...
    def getUserName(self) -> str: ...
    def isApplicationCritical(self) -> bool: ...
    def isLocationAuthReq(self) -> bool: ...

class TokenDecoder:
    def decode(self, byteArray: _py_List[int]) -> SerializedTokenFields: ...