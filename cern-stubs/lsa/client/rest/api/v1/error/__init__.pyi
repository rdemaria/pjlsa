import cern.lsa.client.rest.api.v1.dto
import com.fasterxml.jackson.databind
import feign
import feign.codec
import java.lang
import typing



class DefaultErrorDecoder(feign.codec.ErrorDecoder.Default):
    """
    Java class 'cern.lsa.client.rest.api.v1.error.DefaultErrorDecoder'
    
        Extends:
            feign.codec.ErrorDecoder$Default
    
      Constructors:
        * DefaultErrorDecoder(com.fasterxml.jackson.databind.ObjectMapper)
    
    """
    def __init__(self, objectMapper: com.fasterxml.jackson.databind.ObjectMapper): ...
    def decode(self, string: str, response: feign.Response) -> java.lang.Exception: ...

class RestResponseException(java.lang.RuntimeException):
    """
    Java class 'cern.lsa.client.rest.api.v1.error.RestResponseException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * RestResponseException(cern.lsa.client.rest.api.v1.dto.ErrorDto)
    
    """
    def __init__(self, errorDto: cern.lsa.client.rest.api.v1.dto.ErrorDto): ...
    def getErrorDto(self) -> cern.lsa.client.rest.api.v1.dto.ErrorDto: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1.error")``.

    DefaultErrorDecoder: typing.Type[DefaultErrorDecoder]
    RestResponseException: typing.Type[RestResponseException]
