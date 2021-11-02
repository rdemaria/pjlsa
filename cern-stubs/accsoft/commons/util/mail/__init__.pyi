import java.io
import typing



class MailSender:
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` public interface MailSender
    
        Deprecated.
        This interface has been moved to accsoft-commons-io package. Please use it from there.
        Mail sender.
    
        Also see:
            :class:`~cern.accsoft.commons.util.mail.MailSenderFactory`
    """
    @typing.overload
    def send(self, stringArray: typing.List[str], string2: str, string3: str) -> None:
        """
            Deprecated.
            Sends an email.
        
            Parameters:
                to (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): 'To' email addresses. Can be :code:`null`
                subject (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): email subject
                body (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): email body (can be HTML text).
        
        """
        ...
    @typing.overload
    def send(self, stringArray: typing.List[str], stringArray2: typing.List[str], stringArray3: typing.List[str], string4: str, string5: str) -> None:
        """
            Deprecated.
            Sends an email. Note that at least one of :code:`to`, :code:`cc` and :code:`bcc` arguments must be specified.
        
            Parameters:
                to (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): 'To' email addresses. Can be :code:`null`
                cc (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): 'Cc' email addresses. Can be :code:`null`
                bcc (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): 'Bcc' email addresses. Can be :code:`null`
                subject (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): email subject
                body (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): email body (can be HTML text).
        
        """
        ...
    @typing.overload
    def send(self, stringArray: typing.List[str], stringArray2: typing.List[str], stringArray3: typing.List[str], string4: str, string5: str, fileArray: typing.List[java.io.File]) -> None:
        """
            Deprecated.
            Sends an email. Note that at least one of :code:`to`, :code:`cc` and :code:`bcc` arguments must be specified.
        
            Parameters:
                to (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): 'To' email addresses. Can be :code:`null`
                cc (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): 'Cc' email addresses. Can be :code:`null`
                bcc (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): 'Bcc' email addresses. Can be :code:`null`
                subject (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): email subject
                body (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): email body (can be HTML text).
                attachments (`File <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/File.html?is-external=true>`[]): optional array with files to be attached. Can be :code:`null`
        
        
        """
        ...

class MailSenderFactory:
    def __init__(self): ...
    def getFrom(self) -> str: ...
    def getSmtpHost(self) -> str: ...
    def getSmtpPort(self) -> int: ...
    def getUserName(self) -> str: ...
    def isTLSConnection(self) -> bool: ...
    @staticmethod
    def newInstance() -> 'MailSenderFactory': ...
    @typing.overload
    def newMailSender(self) -> MailSender: ...
    @typing.overload
    def newMailSender(self, string: str) -> MailSender: ...
    def setFrom(self, string: str) -> None: ...
    def setPassword(self, string: str) -> None: ...
    def setSmtpHost(self, string: str) -> None: ...
    def setSmtpPort(self, int: int) -> None: ...
    def setTLSConnection(self, boolean: bool) -> None: ...
    def setUserName(self, string: str) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.util.mail")``.

    MailSender: typing.Type[MailSender]
    MailSenderFactory: typing.Type[MailSenderFactory]
