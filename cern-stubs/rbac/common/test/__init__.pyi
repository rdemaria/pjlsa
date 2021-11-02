import cern.rbac.common
import typing



class TestTokenBuilder:
    """
    public final class TestTokenBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Builder facilitates creation of test (fake) RBAC tokens (see :class:`~cern.rbac.common.RbaToken`) using the requested
        configuration i.e. user, set of roles, location, etc.
    
        Token instances created by this builder can be only used for the testing purposes i.e. unit tests verifying business
        logic with different user credentials. Moreover, the test (fake) tokens are not valid for performing any operation on a
        protected device property.
    
        Note: Use :code:`setLifetime(0)` for creating an expired token
    
        *Example code which builds a new test RBAC token*:
    
    
    
    
        :code:`TestTokenBuilder builder = TestTokenBuilder.newInstance();
        builder.setApplication("TestApplication").setLocation("MyTestLocation");
        builder.setUsername("rbaguest").setRoles("Role1", "Role2"); RbaToken testToken = builder.build();`
    """
    DEFAULT_USER_ACCOUNT_TYPE: typing.ClassVar[cern.rbac.common.UserPrincipal.AccountType] = ...
    """
    public static final :class:`~cern.rbac.common.UserPrincipal.AccountType` DEFAULT_USER_ACCOUNT_TYPE
    
    
    """
    def application(self, string: str) -> 'TestTokenBuilder':
        """
            Sets requested application name. The default name is "TestTokenFactory".
        
            Parameters:
                application (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): requested application name
        
            Returns:
                this token builder
        
        
        """
        ...
    def authenticationTime(self, int: int) -> 'TestTokenBuilder':
        """
            Sets requested token authentication time in seconds. The default is current time.
        
            Parameters:
                authenticationTime (int): requested token authentication time
        
            Returns:
                this token builder
        
        
        """
        ...
    def build(self) -> cern.rbac.common.RbaToken:
        """
            Builds and returns a new, test (fake) token, an instance of :class:`~cern.rbac.common.RbaToken`.
        
        
            Returned token is configured using the provided attributes.
        
            Returns:
                new, test token, an instance of :class:`~cern.rbac.common.RbaToken`
        
        
        """
        ...
    def lifeTime(self, int: int) -> 'TestTokenBuilder':
        """
            Sets requested token lifetime in minutes. The default lifetime is 8 hours. For obtaining an expired token, set lifetime
            to 0 (zero).
        
            Parameters:
                lifeTime (int): requested token lifetime
        
            Returns:
                this token builder
        
        
        """
        ...
    def location(self, string: str) -> 'TestTokenBuilder':
        """
            Sets requested logical location name. The default location is "TestLocation".
        
            Parameters:
                location (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): requested logical location name
        
            Returns:
                this token builder
        
        
        """
        ...
    @staticmethod
    def newInstance() -> 'TestTokenBuilder':
        """
            Creates a new instance of the builder.
        
            Returns:
                new instance of the builder
        
        
        """
        ...
    def reset(self) -> 'TestTokenBuilder':
        """
            Resets the set of configuration attributes to it's default values.
        
            Returns:
                this token builder
        
        
        """
        ...
    def roles(self, stringArray: typing.List[str]) -> 'TestTokenBuilder': ...
    def rolesExpirations(self, intArray: typing.List[int]) -> 'TestTokenBuilder':
        """
            Sets roles expiration times. By default nothing is set.
        
            Parameters:
                rolesExpirations (int...): requested user roles expirations for a token
        
            Returns:
                this token builder
        
        
        """
        ...
    def rolesHints(self, stringArray: typing.List[str]) -> 'TestTokenBuilder': ...
    def tokenType(self, tokenType: cern.rbac.common.TokenType) -> 'TestTokenBuilder':
        """
            Sets requested type of token. The default type is Application.
        
            Parameters:
                tokenType (:class:`~cern.rbac.common.TokenType`): requested type of token
        
            Returns:
                this token builder
        
        
        """
        ...
    def userAccountType(self, accountType: cern.rbac.common.UserPrincipal.AccountType) -> 'TestTokenBuilder':
        """
            Sets the requested user account type. The default value is AccountType.SERVICE
        
            Parameters:
                userAccountType (:class:`~cern.rbac.common.UserPrincipal.AccountType`): the account type
        
            Returns:
                this token builder
        
        
        """
        ...
    def userEmail(self, string: str) -> 'TestTokenBuilder':
        """
            Set the requested user email. The default value is "rba.guest@cern.ch"
        
            Parameters:
                userEmail (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the email of the user
        
            Returns:
                this token builder
        
        
        """
        ...
    def userFullName(self, string: str) -> 'TestTokenBuilder':
        """
            Sets requested user full name. The default value is "RBAC GUEST"
        
            Parameters:
                userFullName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the full name of the user
        
            Returns:
                this token builder
        
        
        """
        ...
    def username(self, string: str) -> 'TestTokenBuilder':
        """
            Sets requested token username. The default username is "rbaguest".
        
            Parameters:
                username (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): requested token username
        
            Returns:
                this token builder
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.rbac.common.test")``.

    TestTokenBuilder: typing.Type[TestTokenBuilder]
