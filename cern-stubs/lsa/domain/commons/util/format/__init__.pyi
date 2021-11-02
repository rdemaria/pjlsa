import java.util
import typing



class DefaultDateFormatter:
    """
    public final class DefaultDateFormatter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A synchronized formatter that formats and parses date using most common pattern defined in
        :meth:`~cern.lsa.domain.commons.util.format.DefaultDateFormatter.FORMAT`.
    
        Also see:
            `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/text/SimpleDateFormat.html?is-external=true>`
    """
    FORMAT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` FORMAT
    
        Format used by this formatter: :code:`dd-MM-yyyy HH:mm:ss`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @staticmethod
    def format(date: java.util.Date) -> str:
        """
            Formats the date using :meth:`~cern.lsa.domain.commons.util.format.DefaultDateFormatter.FORMAT` pattern.
        
            Parameters:
                date (`Date <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Date.html?is-external=true>`): date to be formatted
        
            Returns:
                string representation
        
            Also see:
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/text/DateFormat.html?is-external=true#format(java.util.Date)>`
        
        
        """
        ...
    @staticmethod
    def parse(string: str) -> java.util.Date:
        """
            Parses given string that is expected to be in this
            :meth:`~cern.lsa.domain.commons.util.format.DefaultDateFormatter.FORMAT`.
        
            Parameters:
                formattedDate (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the string to be parsed
        
            Returns:
                date
        
            Raises:
                : if the string can't be parsed to date using the default
                    :meth:`~cern.lsa.domain.commons.util.format.DefaultDateFormatter.FORMAT`
        
            Also see:
                `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/text/DateFormat.html?is-external=true#parse(java.lang.String)>`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.domain.commons.util.format")``.

    DefaultDateFormatter: typing.Type[DefaultDateFormatter]
