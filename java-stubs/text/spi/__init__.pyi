import java.text
import java.util
import java.util.spi
import typing



class BreakIteratorProvider(java.util.spi.LocaleServiceProvider):
    """
    Java class 'java.text.spi.BreakIteratorProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getCharacterInstance(self, locale: java.util.Locale) -> java.text.BreakIterator: ...
    def getLineInstance(self, locale: java.util.Locale) -> java.text.BreakIterator: ...
    def getSentenceInstance(self, locale: java.util.Locale) -> java.text.BreakIterator: ...
    def getWordInstance(self, locale: java.util.Locale) -> java.text.BreakIterator: ...

class CollatorProvider(java.util.spi.LocaleServiceProvider):
    """
    Java class 'java.text.spi.CollatorProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getInstance(self, locale: java.util.Locale) -> java.text.Collator: ...

class DateFormatProvider(java.util.spi.LocaleServiceProvider):
    """
    Java class 'java.text.spi.DateFormatProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getDateInstance(self, int: int, locale: java.util.Locale) -> java.text.DateFormat: ...
    def getDateTimeInstance(self, int: int, int2: int, locale: java.util.Locale) -> java.text.DateFormat: ...
    def getTimeInstance(self, int: int, locale: java.util.Locale) -> java.text.DateFormat: ...

class DateFormatSymbolsProvider(java.util.spi.LocaleServiceProvider):
    """
    Java class 'java.text.spi.DateFormatSymbolsProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getInstance(self, locale: java.util.Locale) -> java.text.DateFormatSymbols: ...

class DecimalFormatSymbolsProvider(java.util.spi.LocaleServiceProvider):
    """
    Java class 'java.text.spi.DecimalFormatSymbolsProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getInstance(self, locale: java.util.Locale) -> java.text.DecimalFormatSymbols: ...

class NumberFormatProvider(java.util.spi.LocaleServiceProvider):
    """
    Java class 'java.text.spi.NumberFormatProvider'
    
        Extends:
            java.util.spi.LocaleServiceProvider
    
    """
    def getCurrencyInstance(self, locale: java.util.Locale) -> java.text.NumberFormat: ...
    def getIntegerInstance(self, locale: java.util.Locale) -> java.text.NumberFormat: ...
    def getNumberInstance(self, locale: java.util.Locale) -> java.text.NumberFormat: ...
    def getPercentInstance(self, locale: java.util.Locale) -> java.text.NumberFormat: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.text.spi")``.

    BreakIteratorProvider: typing.Type[BreakIteratorProvider]
    CollatorProvider: typing.Type[CollatorProvider]
    DateFormatProvider: typing.Type[DateFormatProvider]
    DateFormatSymbolsProvider: typing.Type[DateFormatSymbolsProvider]
    DecimalFormatSymbolsProvider: typing.Type[DecimalFormatSymbolsProvider]
    NumberFormatProvider: typing.Type[NumberFormatProvider]
