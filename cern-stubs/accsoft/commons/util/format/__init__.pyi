import java.util.concurrent
import typing



class TimeFormat:
    """
    public interface TimeFormat
    
        An interface for a time period formatter.
    
        The main purpose of implementations is to represent a time period expressed with milliseconds, nanoseconds, etc. in a
        human-readable format (ex. "5 min, 20 sec").
    """
    def format(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> str:
        """
            Returns a string representation of a time period expressed in certain units.
        
            Parameters:
                time (long): time period
                unit (`TimeUnit <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/TimeUnit.html?is-external=true>`): the time unit of time argument
        
            Returns:
                a string representation of a time period
        
        
        """
        ...

class DefaultTimeFormat(TimeFormat):
    """
    public class DefaultTimeFormat extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.util.format.TimeFormat`
    
        Default implementation of :class:`~cern.accsoft.commons.util.format.TimeFormat`.
    
        This time format is based on 7 patterns for the time components and the separator between them. The time components are:
        days, hours, minutes, seconds, milliseconds, microseconds and nanoseconds. In each pattern the placeholder
        :meth:`~cern.accsoft.commons.util.format.DefaultTimeFormat.PLACEHOLDER` stands for the actual number in the resulting
        string.
    
        This class can either skip the zero values (which are between two significant values) or include them into the resulting
        string. In the first case an example of the result would be "2 hrs, 45 sec", while in the second case "2 hrs, 0 min, 45
        sec". The zero values which are not between two significant values are never included into resulting string. That means
        that the result will never be "0 days, 2 hrs, 0 min, 45 sec, 0 ms, 0 mcs, 0 ns" but "2 hrs, 0 min, 45 sec" or "2 hrs, 45
        sec".
    """
    PLACEHOLDER: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` PLACEHOLDER
    
        A placeholder used to specify the place of the value in the format template
    
        Also see:
            :meth:`~constant`
    
    
    """
    NO_TIME: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` NO_TIME
    
        A string for the total time of 0 nanoseconds
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def format(self, long: int, timeUnit: java.util.concurrent.TimeUnit) -> str:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.util.format.TimeFormat.format`
            Returns a string representation of a time period expressed in certain units.
        
            Specified by:
                :meth:`~cern.accsoft.commons.util.format.TimeFormat.format`Â in
                interfaceÂ :class:`~cern.accsoft.commons.util.format.TimeFormat`
        
            Parameters:
                time (long): time period
                unit (`TimeUnit <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/TimeUnit.html?is-external=true>`): the time unit of time argument
        
            Returns:
                a string representation of a time period
        
        
        """
        ...
    def getDayFormat(self) -> str:
        """
            Getter for the day format
        
            Returns:
                the day format
        
        
        """
        ...
    def getHourFormat(self) -> str:
        """
            Getter for the hour format
        
            Returns:
                the hour format
        
        
        """
        ...
    def getMicrosecFormat(self) -> str:
        """
            Getter for the microsecond format
        
            Returns:
                the microsecond format
        
        
        """
        ...
    def getMillisecFormat(self) -> str:
        """
            Getter for the millisecond format
        
            Returns:
                the millisecond format
        
        
        """
        ...
    def getMinFormat(self) -> str:
        """
            Getter for the minute format
        
            Returns:
                the minute format
        
        
        """
        ...
    def getNanosecFormat(self) -> str:
        """
            Getter for the nanosecond format
        
            Returns:
                the nanosecond format
        
        
        """
        ...
    def getSecFormat(self) -> str:
        """
            Getter for the second format
        
            Returns:
                the second format
        
        
        """
        ...
    def getSeparator(self) -> str:
        """
            Getter for the separator between components of the time
        
            Returns:
                the separator between components of the time
        
        
        """
        ...
    def isSkipZeroValues(self) -> bool:
        """
            Returns true if the zero values should be skipped and false otherwise
        
            Returns:
                true if the zero values should be skipped and false otherwise
        
        
        """
        ...
    def setDayFormat(self, string: str) -> None:
        """
            Setter for the day format
        
            Parameters:
                dayFormat (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the day format
        
        
        """
        ...
    def setHourFormat(self, string: str) -> None:
        """
            Setter for the hour format
        
            Parameters:
                hourFormat (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the hour format
        
        
        """
        ...
    def setMicrosecFormat(self, string: str) -> None:
        """
            Setter for the microsecond format
        
            Parameters:
                microsecFormat (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the microsecond format
        
        
        """
        ...
    def setMillisecFormat(self, string: str) -> None:
        """
            Setter for the millisecond format
        
            Parameters:
                millisecFormat (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the millisecond format
        
        
        """
        ...
    def setMinFormat(self, string: str) -> None:
        """
            Setter for the minute format
        
            Parameters:
                minFormat (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the minute format
        
        
        """
        ...
    def setNanosecFormat(self, string: str) -> None:
        """
            Setter for the nanosecond format
        
            Parameters:
                nanosecFormat (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the nanosecond format
        
        
        """
        ...
    def setSecFormat(self, string: str) -> None:
        """
            Setter for the second format
        
            Parameters:
                secFormat (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the second format
        
        
        """
        ...
    def setSeparator(self, string: str) -> None:
        """
            Setter for the separator between components of the time
        
            Parameters:
                separator (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the separator between components of the time
        
        
        """
        ...
    def setSkipZeroValues(self, boolean: bool) -> None:
        """
            Setter for the "skip-zero-values" flag. True means that the zero-value will be skipped in the result string. For
            example, "2 hrs, 45 sec" instead of "2 hrs, 0 min, 45 sec". False means that zero-values will be left in the result
            string.
        
            Parameters:
                skipZeroValues (boolean): true to skip zero-values in the result string
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.format")``.

    DefaultTimeFormat: typing.Type[DefaultTimeFormat]
    TimeFormat: typing.Type[TimeFormat]
