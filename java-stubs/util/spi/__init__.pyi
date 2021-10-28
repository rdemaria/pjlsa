import java.io
import java.util
import typing



class LocaleServiceProvider:
    """
    Java class 'java.util.spi.LocaleServiceProvider'
    
        Extends:
            java.lang.Object
    
    """
    def getAvailableLocales(self) -> typing.List[java.util.Locale]: ...
    def isSupportedLocale(self, locale: java.util.Locale) -> bool: ...

class ResourceBundleControlProvider:
    """
    Java class 'java.util.spi.ResourceBundleControlProvider'
    
    """
    def getControl(self, string: str) -> java.util.ResourceBundle.Control: ...

class ResourceBundleProvider:
    """
    Java class 'java.util.spi.ResourceBundleProvider'
    
    """
    def getBundle(self, string: str, locale: java.util.Locale) -> java.util.ResourceBundle: ...

class ToolProvider:
    """
    Java class 'java.util.spi.ToolProvider'
    
    """
    @staticmethod
    def findFirst(string: str) -> java.util.Optional['ToolProvider']: ...
    def name(self) -> str: ...
    @typing.overload
    def run(self, printWriter: java.io.PrintWriter, printWriter2: java.io.PrintWriter, stringArray: typing.List[str]) -> int: ...
    @typing.overload
    def run(self, printStream: java.io.PrintStream, printStream2: java.io.PrintStream, stringArray: typing.List[str]) -> int: ...

class AbstractResourceBundleProvider(ResourceBundleProvider):
    """
    Java class 'java.util.spi.AbstractResourceBundleProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.util.spi.ResourceBundleProvider
    
    """
    def getBundle(self, string: str, locale: java.util.Locale) -> java.util.ResourceBundle: ...

class CalendarDataProvider(LocaleServiceProvider):
    """
    Java class 'java.util.spi.CalendarDataProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getFirstDayOfWeek(self, locale: java.util.Locale) -> int: ...
    def getMinimalDaysInFirstWeek(self, locale: java.util.Locale) -> int: ...

class CalendarNameProvider(LocaleServiceProvider):
    """
    Java class 'java.util.spi.CalendarNameProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getDisplayName(self, string: str, int: int, int2: int, int3: int, locale: java.util.Locale) -> str: ...
    def getDisplayNames(self, string: str, int: int, int2: int, locale: java.util.Locale) -> java.util.Map[str, int]: ...

class CurrencyNameProvider(LocaleServiceProvider):
    """
    Java class 'java.util.spi.CurrencyNameProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getDisplayName(self, string: str, locale: java.util.Locale) -> str: ...
    def getSymbol(self, string: str, locale: java.util.Locale) -> str: ...

class LocaleNameProvider(LocaleServiceProvider):
    """
    Java class 'java.util.spi.LocaleNameProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getDisplayCountry(self, string: str, locale: java.util.Locale) -> str: ...
    def getDisplayLanguage(self, string: str, locale: java.util.Locale) -> str: ...
    def getDisplayScript(self, string: str, locale: java.util.Locale) -> str: ...
    def getDisplayUnicodeExtensionKey(self, string: str, locale: java.util.Locale) -> str: ...
    def getDisplayUnicodeExtensionType(self, string: str, string2: str, locale: java.util.Locale) -> str: ...
    def getDisplayVariant(self, string: str, locale: java.util.Locale) -> str: ...

class TimeZoneNameProvider(LocaleServiceProvider):
    """
    Java class 'java.util.spi.TimeZoneNameProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getDisplayName(self, string: str, boolean: bool, int: int, locale: java.util.Locale) -> str: ...
    def getGenericDisplayName(self, string: str, int: int, locale: java.util.Locale) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.util.spi")``.

    AbstractResourceBundleProvider: typing.Type[AbstractResourceBundleProvider]
    CalendarDataProvider: typing.Type[CalendarDataProvider]
    CalendarNameProvider: typing.Type[CalendarNameProvider]
    CurrencyNameProvider: typing.Type[CurrencyNameProvider]
    LocaleNameProvider: typing.Type[LocaleNameProvider]
    LocaleServiceProvider: typing.Type[LocaleServiceProvider]
    ResourceBundleControlProvider: typing.Type[ResourceBundleControlProvider]
    ResourceBundleProvider: typing.Type[ResourceBundleProvider]
    TimeZoneNameProvider: typing.Type[TimeZoneNameProvider]
    ToolProvider: typing.Type[ToolProvider]
