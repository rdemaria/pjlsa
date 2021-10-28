import cern.accsoft.commons.diag
import cern.accsoft.commons.diag.matcher
import java.lang
import typing



class AbstractJapcThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.StringThrowableMatcher
    
      Attributes:
        JAPC_PROBLEM_DOMAIN (java.lang.String): final static field
    
    """
    JAPC_PROBLEM_DOMAIN: typing.ClassVar[str] = ...

class JapcParamExExceptionThrowableMatcher(cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcParamExExceptionThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher
    
      Constructors:
        * JapcParamExExceptionThrowableMatcher()
    
      Attributes:
        JAPC_PE_EX_MATCHER_NAME (java.lang.String): final static field
    
    """
    JAPC_PE_EX_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class JapcParamExProxyThrowableMatcher(cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcParamExProxyThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher
    
      Constructors:
        * JapcParamExProxyThrowableMatcher()
    
    """
    def __init__(self): ...

class JapcThrowableMessageComposer(cern.accsoft.commons.diag.DefaultThrowableMessageComposer):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcThrowableMessageComposer'
    
        Extends:
            cern.accsoft.commons.diag.DefaultThrowableMessageComposer
    
      Constructors:
        * JapcThrowableMessageComposer()
    
    """
    def __init__(self): ...
    def composeMessage(self, throwable: java.lang.Throwable) -> str: ...

class JapcCmwDisconnectedStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcCmwDisconnectedStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher
    
      Constructors:
        * JapcCmwDisconnectedStringThrowableMatcher()
    
      Attributes:
        CMW_DISCONNECTED_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_DISCONNECTED_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class JapcCmwRdaParameterCreatorExceptionThrowableMatcher(JapcParamExExceptionThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcCmwRdaParameterCreatorExceptionThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.japc.JapcParamExExceptionThrowableMatcher
    
      Constructors:
        * JapcCmwRdaParameterCreatorExceptionThrowableMatcher()
    
    """
    def __init__(self): ...

class JapcCmwRdaParameterCreatorStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcCmwRdaParameterCreatorStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher
    
      Constructors:
        * JapcCmwRdaParameterCreatorStringThrowableMatcher()
    
      Attributes:
        CMW_RDA_PARAMETER_CREATOR_MATCHER_NAME (java.lang.String): final static field
    
    """
    CMW_RDA_PARAMETER_CREATOR_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class JapcNoValueStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcNoValueStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher
    
      Constructors:
        * JapcNoValueStringThrowableMatcher()
    
      Attributes:
        JAPC_NO_VALUE_MATCHER_NAME (java.lang.String): final static field
    
    """
    JAPC_NO_VALUE_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class JapcParamExFgcErrorStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcParamExFgcErrorStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher
    
      Constructors:
        * JapcParamExFgcErrorStringThrowableMatcher()
    
      Attributes:
        JAPC_FGC_ERROR_MATCHER_NAME (java.lang.String): final static field
    
    """
    JAPC_FGC_ERROR_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class JapcParamExMonitoringNotSupportedStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcParamExMonitoringNotSupportedStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher
    
      Constructors:
        * JapcParamExMonitoringNotSupportedStringThrowableMatcher()
    
      Attributes:
        JAPC_MONITORING_NOT_SUPORTED_MATCHER_NAME (java.lang.String): final static field
    
    """
    JAPC_MONITORING_NOT_SUPORTED_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class JapcParamExNoSubscriptionStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcParamExNoSubscriptionStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher
    
      Constructors:
        * JapcParamExNoSubscriptionStringThrowableMatcher()
    
      Attributes:
        JAPC_PE_SUB_FAIL_MATCHER_NAME (java.lang.String): final static field
    
    """
    JAPC_PE_SUB_FAIL_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class JapcParamExStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcParamExStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher
    
      Constructors:
        * JapcParamExStringThrowableMatcher()
    
      Attributes:
        JAPC_PE_MATCHER_NAME (java.lang.String): final static field
    
    """
    JAPC_PE_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class JapcParamRuntimeExStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcParamRuntimeExStringThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher
    
      Constructors:
        * JapcParamRuntimeExStringThrowableMatcher()
    
      Attributes:
        JAPC_RUNTIME_MATCHER_NAME (java.lang.String): final static field
    
    """
    JAPC_RUNTIME_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...

class JapcThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    Java class 'cern.accsoft.commons.diag.matcher.japc.JapcThrowableMatcher'
    
        Extends:
            cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher
    
      Constructors:
        * JapcThrowableMatcher()
    
      Attributes:
        JAPC_MATCHER_NAME (java.lang.String): final static field
    
    """
    JAPC_MATCHER_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.diag.matcher.japc")``.

    AbstractJapcThrowableMatcher: typing.Type[AbstractJapcThrowableMatcher]
    JapcCmwDisconnectedStringThrowableMatcher: typing.Type[JapcCmwDisconnectedStringThrowableMatcher]
    JapcCmwRdaParameterCreatorExceptionThrowableMatcher: typing.Type[JapcCmwRdaParameterCreatorExceptionThrowableMatcher]
    JapcCmwRdaParameterCreatorStringThrowableMatcher: typing.Type[JapcCmwRdaParameterCreatorStringThrowableMatcher]
    JapcNoValueStringThrowableMatcher: typing.Type[JapcNoValueStringThrowableMatcher]
    JapcParamExExceptionThrowableMatcher: typing.Type[JapcParamExExceptionThrowableMatcher]
    JapcParamExFgcErrorStringThrowableMatcher: typing.Type[JapcParamExFgcErrorStringThrowableMatcher]
    JapcParamExMonitoringNotSupportedStringThrowableMatcher: typing.Type[JapcParamExMonitoringNotSupportedStringThrowableMatcher]
    JapcParamExNoSubscriptionStringThrowableMatcher: typing.Type[JapcParamExNoSubscriptionStringThrowableMatcher]
    JapcParamExProxyThrowableMatcher: typing.Type[JapcParamExProxyThrowableMatcher]
    JapcParamExStringThrowableMatcher: typing.Type[JapcParamExStringThrowableMatcher]
    JapcParamRuntimeExStringThrowableMatcher: typing.Type[JapcParamRuntimeExStringThrowableMatcher]
    JapcThrowableMatcher: typing.Type[JapcThrowableMatcher]
    JapcThrowableMessageComposer: typing.Type[JapcThrowableMessageComposer]
