import cern
import cern.accsoft.commons.util.userinfo
import java.io
import java.util
import typing



class ProcUtils:
    """
    public class ProcUtils extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A class with Process-related utilities, e.g. to obtain information about the current process.
    
        Clients can either call direct methods such as :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getPid`,
        :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getApplicationName` or
        :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getOfficialApplicationId` (aka ClientID) or obtain complete information
        using the call :code:`ProcUtils.get().getProcessInfo()`.
    
        For use with dependency injection in Spring, please use :class:`~cern.accsoft.commons.util.proc.ProcUtilsBean`.
    """
    SYSPROP_APP_NAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_APP_NAME
    
        The system property used to specify the application name
    
        Also see:
            :meth:`~constant`
    
    
    """
    SYSPROP_APP_VERSION: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SYSPROP_APP_VERSION
    
        The system property used to specify the application version
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNKNOWN_PROCNAME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` UNKNOWN_PROCNAME
    
        The String used as last resort if the process name could not be determined
    
        Also see:
            :meth:`~constant`
    
    
    """
    INVALID_PID: typing.ClassVar[int] = ...
    """
    public static final int INVALID_PID
    
        The integer used to represent an invalid PID, e.g. if the PID cannot be determined
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def createClientInformation(string: str) -> cern.accsoft.commons.util.userinfo.ClientInformation: ...
    @staticmethod
    def get() -> 'ProcUtils':
        """
            Get the singleton instance of this class
        
            Returns:
                the singleton
        
        
        """
        ...
    @staticmethod
    def getApplicationName() -> str:
        """
            Tries to return a meaningful and valid application name else returns the pid; never returns :code:`null` or an empty
            string This method is guaranteed not to throw any Exception.
        
            Returns:
                a meaningful and valid process name or the pid; never returns :code:`null` or an empty string
        
            Also see:
                :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.getApplicationName`
        
        
        """
        ...
    @staticmethod
    def getClientInformation() -> cern.accsoft.commons.util.userinfo.ClientInformation: ...
    @staticmethod
    def getNoJmxInit() -> 'ProcUtils':
        """
            If JMX is already initialized: Get the singleton instance of this class Otherwise: create a new instance of ProcUtils
            without initializing JMX
        
        """
        ...
    @staticmethod
    def getOfficialApplicationId() -> str:
        """
            Returns a standard String (aka ClientID) containing in a condensed format all information useful for a controls expert
            to identify a process.
        
            This method is guaranteed not to throw any Exception.
        
            The information is formatted as :code:`"app=ApplicationName;ver=version;uid=user;host=hostname;pid=pid;jmx=jmxPort"`
            :code:`"app=SequencerGui;ver=2.5.1;uid=copera;host=cs-ccr-seq1;pid=11902;jmx=1234"`
        
            Not all the fields are guaranteed to be present; if information is missing, the corresponding field is omitted.
        
            Returns:
                the official Application ID, aka ClientID
        
        
        """
        ...
    @staticmethod
    def getPid() -> int:
        """
            Returns the Process ID of this process or :meth:`~cern.accsoft.commons.util.proc.ProcUtils.INVALID_PID` if it cannot be
            determined.
        
            This method is guaranteed not to throw any Exception.
        
            Returns:
                the Process ID of this process or :meth:`~cern.accsoft.commons.util.proc.ProcUtils.INVALID_PID` if it cannot be
                determined.
        
        
        """
        ...
    @typing.overload
    def getProcessInfo(self) -> 'ProcessInfo':
        """
            Returns the :class:`~cern.accsoft.commons.util.proc.ProcessInfo` object.
        
            For efficiency reasons, only the first call to this method will create a new instance, subsequent calls will just return
            the same object. Use :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getProcessInfo` to create a new object.
        
            Returns:
                the :class:`~cern.accsoft.commons.util.proc.ProcessInfo` object
        
        """
        ...
    @typing.overload
    def getProcessInfo(self, boolean: bool) -> 'ProcessInfo':
        """
            Same as :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getProcessInfo`, but with the option to create a new instance
            of :class:`~cern.accsoft.commons.util.proc.ProcessInfo`.
        
            Creating a new ProcessInfo object has a certain overhead, so this method should only be called with :code:`refresh=true`
            when something might have changed, e.g. if a new RBAC token has been assigned, or the Window Title has changed. TODO:
            reduce overhead: only refresh the things that can change, keep static information.
        
            Parameters:
                refresh (boolean): if true, a new ProcessInfo will be created
        
            Returns:
                the ProcessInfo object
        
        
        """
        ...
    class PUMBean:
        def geMainClassName(self) -> str: ...
        def getApplicationName(self) -> str: ...
        def getApplicationOsName(self) -> str: ...
        def getApplicationVersion(self) -> str: ...
        def getOfficialApplicationId(self) -> str: ...

class ProcUtilsBean:
    """
    public class ProcUtilsBean extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Wrapper around :class:`~cern.accsoft.commons.util.proc.ProcUtils` to make it usable in Spring, with possibility to
        specify appName and appVersion
    """
    def __init__(self): ...
    def getAppName(self) -> str:
        """
            Getter for :meth:`~cern.accsoft.commons.util.proc.ProcUtilsBean.setAppName`
        
            Returns:
        
        
        """
        ...
    def getAppVersion(self) -> str:
        """
            Getter for :meth:`~cern.accsoft.commons.util.proc.ProcUtilsBean.setAppVersion`
        
            Returns:
        
        
        """
        ...
    @typing.overload
    def getProcessInfo(self) -> 'ProcessInfo':
        """
            Delegates to :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getProcessInfo`
        
            Returns:
                same as :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getProcessInfo`
        
        """
        ...
    @typing.overload
    def getProcessInfo(self, boolean: bool) -> 'ProcessInfo':
        """
            Delegates to :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getProcessInfo`
        
            Parameters:
                refresh (boolean): see :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getProcessInfo`
        
            Returns:
                same as :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getProcessInfo`
        
        
        """
        ...
    def setAppName(self, string: str) -> None:
        """
            Setter, to set the application name. Careful - this sets the application name in a static variable, i.e. for the whole
            JVM.
        
            Parameters:
                appName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the application name, same effect as setting system property
        
        
        """
        ...
    def setAppVersion(self, string: str) -> None:
        """
            Setter, to set the application version. Careful - this sets the application version in a static variable, i.e. for the
            whole JVM.
        
            Parameters:
                appVersion (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the application version, same effect as setting system property
        
        
        """
        ...

class ProcessInfo(java.io.Serializable):
    """
    public class ProcessInfo extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        A class holding information about a process (e.g. a GUI application or a server process).
    
        It is intended to be sent over the network in client-server interactions, and to be written in logfiles.
    
    
          - Some pieces of information are useful for troubleshooting, e.g. to identify client applications that connect to a
            server. :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.getHostName`,
            :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.getPid` and
            :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.getJmxPort` provide means to further investigate on the client
            process.
          - Other information is useful to clearly determine or at least collect statistics on who uses what service, e.g. who
            accesses deprecated server APIs or FESA devices
    
    
        Instances of this class are typically created by a call to
        :meth:`~cern.accsoft.commons.util.proc.ProcUtils.getProcessInfo`. Not all the data in ProcessInfo objects will be filled
        with values; :code:`null` is returned for empty fields.
    
        The :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.toString` method returns a String composed of
        :code:`"tag=value;"` elements. This is intended for use e.g. as a Client Identifier, as it should not be too long, it
        does not contain all the values will be represented there.
    
        If you need all values, use :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.getAsMap` or the getter methods.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getApplicationName(self) -> str:
        """
            Returns a meaningful and valid application name that best enables a controls expert to identify the process, never
            :code:`null` or an empty String.
        
            By default this is taken in order of preference from
        
              - which is either the value of the system property :meth:`~cern.accsoft.commons.util.proc.ProcUtils.SYSPROP_APP_NAME` if
                set
              - the last part of the JNLP url (e.g. SequencerGui.jnlp), if available
              - the wreboot name (e.g. PM-XPOC-PRO), if available
              - the window title, if available
              - the fully qualified name of the main (the one that contains the main() method)
              - the :meth:`~cern.accsoft.commons.util.proc.ProcUtils.UNKNOWN_PROCNAME` as last resort valid String.
        
            If :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.setApplicationName` was externally invoked with a more meaningful
            name, the new application name will be returned.
        
            Returns:
                the process name for controls experts (guaranteed to be non-null and non-empty)
        
        
        """
        ...
    def getAsMap(self) -> java.util.Map[str, typing.Any]: ...
    def getHostName(self) -> str:
        """
            Returns the hostname on which this ProcessInfo object was created; for CERN hosts, the domain (".cern.ch") is removed,
            other domains are kept.
        
            Returns:
                the hostname on which this ProcessInfo object was created
        
        
        """
        ...
    def getJmxPort(self) -> int:
        """
            Returns the JMX port to which a remote JMX client such as JVisualVm can connect.
        
            This is derived from the system property com.sun Note that JMX should be configured that with password protection.
        
            Returns:
                the JMX port to which a remote JMX client such as JVisualVm can connect
        
        
        """
        ...
    def getJnlpUrl(self) -> str:
        """
            Returns the JNLP URL or :code:`null` if it cannot be determined.
        
        
            Returns:
                the JNLP URL or :code:`null`
        
        
        """
        ...
    def getMainClassName(self) -> str:
        """
            Returns the fully qualified name of the main class (the one containing the main() method) or :code:`null` if it cannot
            be determined.
        
            e.g. cern.seq.lhc.SeqServerStarter
        
            Returns:
                the fully qualified name of the main class or :code:`null`
        
        
        """
        ...
    def getOfficialApplicationId(self) -> str:
        """
            Aka "Client ID" - Returns a standard String containing in a condensed format all information useful for a controls
            expert to identify a process.
        
            It is formatted as :code:`"app=ApplicationName;ver=version;uid=user;host=hostname;pid=pid;jmx=jmxPort"`
            :code:`"app=SequencerGui;ver=2.5.1;uid=copera;host=cs-ccr-seq1;pid=11902;jmx=1234"`
        
            Not all the fields are guaranteed to be present; if information is missing, the corresponding field is omitted.
        
            Returns:
                a standard string with combined process information
        
        
        """
        ...
    def getOsProcessName(self) -> str:
        """
            Returns the process name running the process, which often is just "java" and thus pretty useless.
        
            Returns:
                the process name running the process
        
        
        """
        ...
    def getPid(self) -> int:
        """
            Returns the process id or :code:`null` if it cannot be determined.
        
            Returns:
                the process id or :code:`null`
        
        
        """
        ...
    def getSystemProperties(self) -> java.util.Properties:
        """
            Returns the system properties.
        
            This variable is marked as transitive, i.e. the system properties won't be serialized and sent over a remote connection.
        
            Returns:
                the system properties
        
        
        """
        ...
    def getUserId(self) -> str:
        """
            Returns by default the operating system user ID (e.g. spsop) A more meaningful user id can be set using
            :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.setUserId`
        
            Returns:
                the user ID
        
        
        """
        ...
    def getVersion(self) -> str:
        """
            Returns the application version as defined with the system property
            :meth:`~cern.accsoft.commons.util.proc.ProcUtils.SYSPROP_APP_VERSION` or :code:`null` if it cannot be determined.
        
            Returns:
                the application version or :code:`null`
        
        
        """
        ...
    def getWindowTitle(self) -> str:
        """
            Returns the main window title or :code:`null` if none can be found.
        
        
              - First all windows are inspected to see if any of them implements ExternalFrame (from accsoft-commons-gui), the title is
                returned
              - Otherwise, all JFrames are inspected to see if they have a title. If exactly one JFrame has a title this is used.
                Otherwise :code:`null` is returned
              - If no title is found :code:`null` is returned
        
        
            Returns:
                the title of the window according to the algorithm specified above
        
        
        """
        ...
    def isJnlp(self) -> bool:
        """
            Returns true if this process was launched using JNLP.
        
            This is determined by checking for system properties that are needed for JNLP.
        
            Returns:
                true if this process was launched using JNLP
        
        
        """
        ...
    def reComposeOfficialApplicationId(self) -> None:
        """
            Recomposes the official application id.
        
        """
        ...
    def restoreFromMap(self, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]) -> None: ...
    def setApplicationName(self, string: str) -> None:
        """
            By default this method is internally invoked via ProcUtils where the application name is taken in order of preference
            from
        
              - which is either the value of the system property :meth:`~cern.accsoft.commons.util.proc.ProcUtils.SYSPROP_APP_NAME` if
                set
              - the last part of the JNLP url (e.g. SequencerGui.jnlp), if available
              - the wreboot name (e.g. PM-XPOC-PRO), if available
              - the window title, if available
              - the fully qualified name of the main (the one that contains the main() method)
              - the :meth:`~cern.accsoft.commons.util.proc.ProcUtils.UNKNOWN_PROCNAME` as last resort valid String. If a more meaningful
                name can be provided by an external package, the application name can be optionally overwritten. Note that
                :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.reComposeOfficialApplicationId` must be called after an external
                invocation in order to regenerate the official application id with the new application name.
        
        
            Parameters:
              :code:`applicationName` - The application name
        
        
        """
        ...
    def setUserId(self, string: str) -> None:
        """
            By default this method is internally invoked via ProcUtils where the user id represents the OS user. If the client
            application provides an authentication facility (example: a GUI with a login button), this method can be externally
            invoked to set the user id with a more meaningful name provided during the authentication instead of the default
            operating system. Note that :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.reComposeOfficialApplicationId` must be
            called in order to regenerate the official application id with the new user id.
        
            Parameters:
                userId (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The user
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns :meth:`~cern.accsoft.commons.util.proc.ProcessInfo.getOfficialApplicationId`
        
            Overrides:
                 in class 
        
        
        """
        ...

class JpsImpl(cern.accsoft.commons.util.proc.Jps):
    """
    public class JpsImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def findMainClassName(self, int: int) -> str: ...
    @staticmethod
    def get() -> 'Jps':
        """
            Getter method, returns the singleton
        
            Returns:
                the singleton
        
        
        """
        ...

class Jps: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.proc")``.

    Jps: typing.Type[Jps]
    JpsImpl: typing.Type[JpsImpl]
    ProcUtils: typing.Type[ProcUtils]
    ProcUtilsBean: typing.Type[ProcUtilsBean]
    ProcessInfo: typing.Type[ProcessInfo]
