import cern.lsa.client.rest.api.v1.dto
import com.fasterxml.jackson.databind
import feign
import feign.codec
import java.lang
import typing



class DefaultErrorDecoder(feign.codec.ErrorDecoder.Default):
    """
    public class DefaultErrorDecoder extends feign.codec.ErrorDecoder.Default
    """
    def __init__(self, objectMapper: com.fasterxml.jackson.databind.ObjectMapper): ...
    def decode(self, string: str, response: feign.Response) -> java.lang.Exception:
        """
        
            Specified by:
                :code:`decode` in interface :code:`feign.codec.ErrorDecoder`
        
            Overrides:
                :code:`decode` in class :code:`feign.codec.ErrorDecoder.Default`
        
        
        """
        ...

class RestResponseException(java.lang.RuntimeException):
    """
    public class RestResponseException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, errorDto: cern.lsa.client.rest.api.v1.dto.ErrorDto): ...
    def getErrorDto(self) -> cern.lsa.client.rest.api.v1.dto.ErrorDto: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1.error")``.

    DefaultErrorDecoder: typing.Type[DefaultErrorDecoder]
    RestResponseException: typing.Type[RestResponseException]
