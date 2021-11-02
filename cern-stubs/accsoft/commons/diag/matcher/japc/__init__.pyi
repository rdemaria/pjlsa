import cern.accsoft.commons.diag
import cern.accsoft.commons.diag.matcher
import java.lang
import typing



class AbstractJapcThrowableMatcher(cern.accsoft.commons.diag.matcher.StringThrowableMatcher):
    """
    public abstract class AbstractJapcThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.StringThrowableMatcher`
    
        Basic JAPC exception string-based matcher.
    """
    JAPC_PROBLEM_DOMAIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAPC_PROBLEM_DOMAIN
    
        JAPC problem domain
    
        Also see:
            :meth:`~constant`
    
    
    """

class JapcParamExExceptionThrowableMatcher(cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher):
    """
    public class JapcParamExExceptionThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.ExceptionClassThrowableMatcher`
    """
    JAPC_PE_EX_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAPC_PE_EX_MATCHER_NAME
    
        JAPC parameter exception matcher name (working with exception class)
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class JapcParamExProxyThrowableMatcher(cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher):
    """
    public class JapcParamExProxyThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.ProxyThrowableMatcher`
    """
    def __init__(self): ...

class JapcThrowableMessageComposer(cern.accsoft.commons.diag.DefaultThrowableMessageComposer):
    """
    public class JapcThrowableMessageComposer extends :class:`~cern.accsoft.commons.diag.DefaultThrowableMessageComposer`
    
        :class:`~cern.accsoft.commons.diag.ThrowableMessageComposer` for JAPC :code:`ParameterException`'s.
    """
    def __init__(self): ...
    def composeMessage(self, throwable: java.lang.Throwable) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.diag.ThrowableMessageComposer.composeMessage`Â in
                interfaceÂ :class:`~cern.accsoft.commons.diag.ThrowableMessageComposer`
        
            Overrides:
                :meth:`~cern.accsoft.commons.diag.DefaultThrowableMessageComposer.composeMessage`Â in
                classÂ :class:`~cern.accsoft.commons.diag.DefaultThrowableMessageComposer`
        
            Returns:
                message describing a `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Throwable.html?is-external=true>`
        
        
        """
        ...

class JapcCmwDisconnectedStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    public class JapcCmwDisconnectedStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher`
    """
    CMW_DISCONNECTED_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_DISCONNECTED_MATCHER_NAME
    
        CMW no connection matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class JapcCmwRdaParameterCreatorExceptionThrowableMatcher(JapcParamExExceptionThrowableMatcher):
    """
    public class JapcCmwRdaParameterCreatorExceptionThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.japc.JapcParamExExceptionThrowableMatcher`
    
        **DO NOT DELETE PLEASE**
    
    
        Duplicate implementation of the
        :class:`~cern.accsoft.commons.diag.matcher.japc.JapcCmwRdaParameterCreatorStringThrowableMatcher` to be kept for
        documentation purpose since it is used in :class:`~cern.accsoft.commons.diag.matcher.japc`.
    """
    def __init__(self): ...

class JapcCmwRdaParameterCreatorStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    public class JapcCmwRdaParameterCreatorStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher`
    
        **DO NOT DELETE PLEASE**
    
    
        Duplicate implementation of the
        :class:`~cern.accsoft.commons.diag.matcher.japc.JapcCmwRdaParameterCreatorExceptionThrowableMatcher` to be kept for
        documentation purpose since it is used in :class:`~cern.accsoft.commons.diag.matcher.japc`.
    """
    CMW_RDA_PARAMETER_CREATOR_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CMW_RDA_PARAMETER_CREATOR_MATCHER_NAME
    
        CMW no connection matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class JapcNoValueStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    public class JapcNoValueStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher`
    """
    JAPC_NO_VALUE_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAPC_NO_VALUE_MATCHER_NAME
    
        JAPC "no value" exception matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class JapcParamExFgcErrorStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    public class JapcParamExFgcErrorStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher`
    """
    JAPC_FGC_ERROR_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAPC_FGC_ERROR_MATCHER_NAME
    
        JAPC subscription failure matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class JapcParamExMonitoringNotSupportedStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    public class JapcParamExMonitoringNotSupportedStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher`
    """
    JAPC_MONITORING_NOT_SUPORTED_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAPC_MONITORING_NOT_SUPORTED_MATCHER_NAME
    
        JAPC subscription failure matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class JapcParamExNoSubscriptionStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    public class JapcParamExNoSubscriptionStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher`
    """
    JAPC_PE_SUB_FAIL_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAPC_PE_SUB_FAIL_MATCHER_NAME
    
        JAPC subscription failure matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class JapcParamExStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    public class JapcParamExStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher`
    """
    JAPC_PE_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAPC_PE_MATCHER_NAME
    
        JAPC parameter exception matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class JapcParamRuntimeExStringThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    public class JapcParamRuntimeExStringThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher`
    """
    JAPC_RUNTIME_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAPC_RUNTIME_MATCHER_NAME
    
        JAPC runtime exception matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...

class JapcThrowableMatcher(AbstractJapcThrowableMatcher):
    """
    public class JapcThrowableMatcher extends :class:`~cern.accsoft.commons.diag.matcher.japc.AbstractJapcThrowableMatcher`
    
        JAPC exception general string-based matcher.
    """
    JAPC_MATCHER_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` JAPC_MATCHER_NAME
    
        JAPC exception matcher name
    
        Also see:
            :meth:`~constant`
    
    
    """
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
