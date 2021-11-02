import java.io
import typing



class ClientInformation(java.io.Serializable):
    """
    public class ClientInformation extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    @staticmethod
    def builder() -> 'ClientInformation.ClientInformationBuilder': ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getApplication(self) -> str: ...
    def getHostname(self) -> str: ...
    def getUser(self) -> str: ...
    def getVersion(self) -> str: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def prettyPrint(self) -> str: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def withApplication(self, string: str) -> 'ClientInformation': ...
    def withUser(self, string: str) -> 'ClientInformation': ...
    class ClientInformationBuilder:
        def application(self, string: str) -> 'ClientInformation.ClientInformationBuilder': ...
        def build(self) -> 'ClientInformation': ...
        def hostname(self, string: str) -> 'ClientInformation.ClientInformationBuilder': ...
        def user(self, string: str) -> 'ClientInformation.ClientInformationBuilder': ...
        def version(self, string: str) -> 'ClientInformation.ClientInformationBuilder': ...

class ClientInformationHolder:
    """
    public interface ClientInformationHolder
    """
    def getClientInformationOrDefault(self) -> ClientInformation: ...
    @staticmethod
    def getInstance() -> 'ClientInformationHolder': ...
    def isClientInformationPresent(self) -> bool: ...
    def setClientInformation(self, clientInformation: ClientInformation) -> None: ...

class Constants:
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface Constants
    
        Deprecated.
        use instead accsoft-commons-directoryservice
        Library constants.
    """
    OUT_ENCODING: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` OUT_ENCODING
    
        Deprecated.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRUST_PASSWD: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TRUST_PASSWD
    
        Deprecated.
        Keystore file password (ca.key)
    
        Also see:
            :meth:`~constant`
    
    
    """
    TRUSTSTORE_TYPE: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TRUSTSTORE_TYPE
    
        Deprecated.
        Keystore type (Java Key Store)
    
        Also see:
            :meth:`~constant`
    
    
    """
    IS_WINDOWS: typing.ClassVar[bool] = ...
    """
    static final boolean IS_WINDOWS
    
        Deprecated.
        True if the current platform is MS WINDOWS, false otherwise.
    
    """
    DATA_PATH: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DATA_PATH
    
        Deprecated.
        This PATH string is pointing to the PS java development DATA directory.
    
    
        This constant is platform independent.
    
    
        i.e.:
    
    
        If your application is in the package cern.ps.ade.my_app_package, you may get data files related to this application via
        the URL path: DATA_PATH + FS + "ade" + FS + "my_app_package"+ FS
    
    """
    DATA_URL: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DATA_URL
    
        Deprecated.
        This URL string is pointing to the PS java development DATA directory.(/acc/java/data)
    
    
        Should be use only for READING data file. If you need to WRITE data file, please use the
        :meth:`~cern.accsoft.commons.util.userinfo.Constants.DATA_PATH` constant.
    
    
        This constant is platform independent.
    
    
        i.e.:
    
    
        If your application is in the package cern.ps.ade.my_app_package, you may get data files related to this application via
        the URL path: DATA_URL + FS + "ade" + FS + "my_app_package"+ FS
    
        Also see:
            :meth:`~constant`
    
    
    """
    CONNECT_TIMEOUT: typing.ClassVar[int] = ...
    """
    static final int CONNECT_TIMEOUT
    
        Deprecated.
        Connection timeout
    
        Also see:
            :meth:`~constant`
    
    
    """

class NiceUser:
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public class NiceUser extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Deprecated.
        use instead accsoft-commons-directoryservice
        This class contains all information about a user extracted from db
    """
    def __init__(self, int: int, int2: int, string: str, string2: str, string3: str, string4: str, string5: str, string6: str, string7: str, string8: str): ...
    def equals(self, object: typing.Any) -> bool:
        """
            Deprecated.
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getCCID(self) -> int:
        """
            Deprecated.
            Gets user ccid
        
            Returns:
                user ccid
        
        
        """
        ...
    def getCompany(self) -> str:
        """
            Deprecated.
            Gets user company
        
            Returns:
                user company
        
        
        """
        ...
    def getDepartment(self) -> str:
        """
            Deprecated.
            Gets user department
        
            Returns:
                user department
        
        
        """
        ...
    def getEmail(self) -> str:
        """
            Deprecated.
            Gets user email
        
            Returns:
                user email
        
        
        """
        ...
    def getFirstName(self) -> str:
        """
            Deprecated.
            Gets user first name
        
            Returns:
                user first name
        
        
        """
        ...
    def getFullName(self) -> str:
        """
            Deprecated.
            Gets user full name
        
            Returns:
                user full name
        
        
        """
        ...
    def getLastName(self) -> str:
        """
            Deprecated.
            Gets user last name
        
            Returns:
                user last name
        
        
        """
        ...
    def getLogin(self) -> str:
        """
            Deprecated.
            Gets user login
        
            Returns:
                user login
        
        
        """
        ...
    def getPhone(self) -> str:
        """
            Deprecated.
            Gets user phone
        
            Returns:
                user phone
        
        
        """
        ...
    def getRespCCID(self) -> int:
        """
            Deprecated.
            Gets ccid of the person responsible for this external
        
            Returns:
                ccid of the person responsible for this external
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Deprecated.
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
            Deprecated.
        
            Overrides:
                 in class 
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.userinfo")``.

    ClientInformation: typing.Type[ClientInformation]
    ClientInformationHolder: typing.Type[ClientInformationHolder]
    Constants: typing.Type[Constants]
    NiceUser: typing.Type[NiceUser]
