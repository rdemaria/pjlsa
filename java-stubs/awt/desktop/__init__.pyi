import java.io
import java.lang
import java.net
import java.util
import jpype.protocol
import typing



class AboutHandler:
    """
    Java class 'java.awt.desktop.AboutHandler'
    
    """
    def handleAbout(self, aboutEvent: 'AboutEvent') -> None: ...

class AppEvent(java.util.EventObject): ...

class OpenFilesHandler:
    """
    Java class 'java.awt.desktop.OpenFilesHandler'
    
    """
    def openFiles(self, openFilesEvent: 'OpenFilesEvent') -> None: ...

class OpenURIHandler:
    """
    Java class 'java.awt.desktop.OpenURIHandler'
    
    """
    def openURI(self, openURIEvent: 'OpenURIEvent') -> None: ...

class PreferencesHandler:
    """
    Java class 'java.awt.desktop.PreferencesHandler'
    
    """
    def handlePreferences(self, preferencesEvent: 'PreferencesEvent') -> None: ...

class PrintFilesHandler:
    """
    Java class 'java.awt.desktop.PrintFilesHandler'
    
    """
    def printFiles(self, printFilesEvent: 'PrintFilesEvent') -> None: ...

class QuitHandler:
    """
    Java class 'java.awt.desktop.QuitHandler'
    
    """
    def handleQuitRequestWith(self, quitEvent: 'QuitEvent', quitResponse: 'QuitResponse') -> None: ...

class QuitResponse:
    """
    Java class 'java.awt.desktop.QuitResponse'
    
    """
    def cancelQuit(self) -> None: ...
    def performQuit(self) -> None: ...

class QuitStrategy(java.lang.Enum['QuitStrategy']):
    """
    Java class 'java.awt.desktop.QuitStrategy'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        NORMAL_EXIT (java.awt.desktop.QuitStrategy): final static enum constant
        CLOSE_ALL_WINDOWS (java.awt.desktop.QuitStrategy): final static enum constant
    
    """
    NORMAL_EXIT: typing.ClassVar['QuitStrategy'] = ...
    CLOSE_ALL_WINDOWS: typing.ClassVar['QuitStrategy'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'QuitStrategy': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['QuitStrategy']: ...

class SystemEventListener(java.util.EventListener): ...

class AboutEvent(AppEvent):
    """
    Java class 'java.awt.desktop.AboutEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
      Constructors:
        * AboutEvent()
    
    """
    def __init__(self): ...

class AppForegroundEvent(AppEvent):
    """
    Java class 'java.awt.desktop.AppForegroundEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
      Constructors:
        * AppForegroundEvent()
    
    """
    def __init__(self): ...

class AppForegroundListener(SystemEventListener):
    """
    Java class 'java.awt.desktop.AppForegroundListener'
    
        Interfaces:
            java.awt.desktop.SystemEventListener
    
    """
    def appMovedToBackground(self, appForegroundEvent: AppForegroundEvent) -> None: ...
    def appRaisedToForeground(self, appForegroundEvent: AppForegroundEvent) -> None: ...

class AppHiddenEvent(AppEvent):
    """
    Java class 'java.awt.desktop.AppHiddenEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
      Constructors:
        * AppHiddenEvent()
    
    """
    def __init__(self): ...

class AppHiddenListener(SystemEventListener):
    """
    Java class 'java.awt.desktop.AppHiddenListener'
    
        Interfaces:
            java.awt.desktop.SystemEventListener
    
    """
    def appHidden(self, appHiddenEvent: AppHiddenEvent) -> None: ...
    def appUnhidden(self, appHiddenEvent: AppHiddenEvent) -> None: ...

class AppReopenedEvent(AppEvent):
    """
    Java class 'java.awt.desktop.AppReopenedEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
      Constructors:
        * AppReopenedEvent()
    
    """
    def __init__(self): ...

class AppReopenedListener(SystemEventListener):
    """
    Java class 'java.awt.desktop.AppReopenedListener'
    
        Interfaces:
            java.awt.desktop.SystemEventListener
    
    """
    def appReopened(self, appReopenedEvent: AppReopenedEvent) -> None: ...

class FilesEvent(AppEvent):
    """
    Java class 'java.awt.desktop.FilesEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
    """
    def getFiles(self) -> java.util.List[java.io.File]: ...

class OpenURIEvent(AppEvent):
    """
    Java class 'java.awt.desktop.OpenURIEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
      Constructors:
        * OpenURIEvent(java.net.URI)
    
    """
    def __init__(self, uRI: java.net.URI): ...
    def getURI(self) -> java.net.URI: ...

class PreferencesEvent(AppEvent):
    """
    Java class 'java.awt.desktop.PreferencesEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
      Constructors:
        * PreferencesEvent()
    
    """
    def __init__(self): ...

class QuitEvent(AppEvent):
    """
    Java class 'java.awt.desktop.QuitEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
      Constructors:
        * QuitEvent()
    
    """
    def __init__(self): ...

class ScreenSleepEvent(AppEvent):
    """
    Java class 'java.awt.desktop.ScreenSleepEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
      Constructors:
        * ScreenSleepEvent()
    
    """
    def __init__(self): ...

class ScreenSleepListener(SystemEventListener):
    """
    Java class 'java.awt.desktop.ScreenSleepListener'
    
        Interfaces:
            java.awt.desktop.SystemEventListener
    
    """
    def screenAboutToSleep(self, screenSleepEvent: ScreenSleepEvent) -> None: ...
    def screenAwoke(self, screenSleepEvent: ScreenSleepEvent) -> None: ...

class SystemSleepEvent(AppEvent):
    """
    Java class 'java.awt.desktop.SystemSleepEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
      Constructors:
        * SystemSleepEvent()
    
    """
    def __init__(self): ...

class SystemSleepListener(SystemEventListener):
    """
    Java class 'java.awt.desktop.SystemSleepListener'
    
        Interfaces:
            java.awt.desktop.SystemEventListener
    
    """
    def systemAboutToSleep(self, systemSleepEvent: SystemSleepEvent) -> None: ...
    def systemAwoke(self, systemSleepEvent: SystemSleepEvent) -> None: ...

class UserSessionEvent(AppEvent):
    """
    Java class 'java.awt.desktop.UserSessionEvent'
    
        Extends:
            java.awt.desktop.AppEvent
    
      Constructors:
        * UserSessionEvent(java.awt.desktop.UserSessionEvent.Reason)
    
    """
    def __init__(self, reason: 'UserSessionEvent.Reason'): ...
    def getReason(self) -> 'UserSessionEvent.Reason': ...
    class Reason(java.lang.Enum['UserSessionEvent.Reason']):
        """
        Java class 'java.awt.desktop.UserSessionEvent$Reason'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            UNSPECIFIED (java.awt.desktop.UserSessionEvent$Reason): final static enum constant
            CONSOLE (java.awt.desktop.UserSessionEvent$Reason): final static enum constant
            REMOTE (java.awt.desktop.UserSessionEvent$Reason): final static enum constant
            LOCK (java.awt.desktop.UserSessionEvent$Reason): final static enum constant
        
        """
        UNSPECIFIED: typing.ClassVar['UserSessionEvent.Reason'] = ...
        CONSOLE: typing.ClassVar['UserSessionEvent.Reason'] = ...
        REMOTE: typing.ClassVar['UserSessionEvent.Reason'] = ...
        LOCK: typing.ClassVar['UserSessionEvent.Reason'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'UserSessionEvent.Reason': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['UserSessionEvent.Reason']: ...

class UserSessionListener(SystemEventListener):
    """
    Java class 'java.awt.desktop.UserSessionListener'
    
        Interfaces:
            java.awt.desktop.SystemEventListener
    
    """
    def userSessionActivated(self, userSessionEvent: UserSessionEvent) -> None: ...
    def userSessionDeactivated(self, userSessionEvent: UserSessionEvent) -> None: ...

class OpenFilesEvent(FilesEvent):
    """
    Java class 'java.awt.desktop.OpenFilesEvent'
    
        Extends:
            java.awt.desktop.FilesEvent
    
      Constructors:
        * OpenFilesEvent(java.util.List, java.lang.String)
    
    """
    def __init__(self, list: java.util.List[typing.Union[java.io.File, jpype.protocol.SupportsPath]], string: str): ...
    def getSearchTerm(self) -> str: ...

class PrintFilesEvent(FilesEvent):
    """
    Java class 'java.awt.desktop.PrintFilesEvent'
    
        Extends:
            java.awt.desktop.FilesEvent
    
      Constructors:
        * PrintFilesEvent(java.util.List)
    
    """
    def __init__(self, list: java.util.List[typing.Union[java.io.File, jpype.protocol.SupportsPath]]): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.awt.desktop")``.

    AboutEvent: typing.Type[AboutEvent]
    AboutHandler: typing.Type[AboutHandler]
    AppEvent: typing.Type[AppEvent]
    AppForegroundEvent: typing.Type[AppForegroundEvent]
    AppForegroundListener: typing.Type[AppForegroundListener]
    AppHiddenEvent: typing.Type[AppHiddenEvent]
    AppHiddenListener: typing.Type[AppHiddenListener]
    AppReopenedEvent: typing.Type[AppReopenedEvent]
    AppReopenedListener: typing.Type[AppReopenedListener]
    FilesEvent: typing.Type[FilesEvent]
    OpenFilesEvent: typing.Type[OpenFilesEvent]
    OpenFilesHandler: typing.Type[OpenFilesHandler]
    OpenURIEvent: typing.Type[OpenURIEvent]
    OpenURIHandler: typing.Type[OpenURIHandler]
    PreferencesEvent: typing.Type[PreferencesEvent]
    PreferencesHandler: typing.Type[PreferencesHandler]
    PrintFilesEvent: typing.Type[PrintFilesEvent]
    PrintFilesHandler: typing.Type[PrintFilesHandler]
    QuitEvent: typing.Type[QuitEvent]
    QuitHandler: typing.Type[QuitHandler]
    QuitResponse: typing.Type[QuitResponse]
    QuitStrategy: typing.Type[QuitStrategy]
    ScreenSleepEvent: typing.Type[ScreenSleepEvent]
    ScreenSleepListener: typing.Type[ScreenSleepListener]
    SystemEventListener: typing.Type[SystemEventListener]
    SystemSleepEvent: typing.Type[SystemSleepEvent]
    SystemSleepListener: typing.Type[SystemSleepListener]
    UserSessionEvent: typing.Type[UserSessionEvent]
    UserSessionListener: typing.Type[UserSessionListener]
