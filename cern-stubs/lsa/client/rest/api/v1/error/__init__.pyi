import cern.lsa.client.rest.api.v1.dto
import com.fasterxml.jackson.databind
import feign
import feign.codec
import java.lang


class DefaultErrorDecoder(feign.codec.ErrorDecoder.Default):
    def __init__(self, objectMapper: com.fasterxml.jackson.databind.ObjectMapper): ...
    def decode(self, string: str, response: feign.Response) -> java.lang.Exception: ...

class RestResponseException(java.lang.RuntimeException):
    def __init__(self, errorDto: cern.lsa.client.rest.api.v1.dto.ErrorDto): ...
    def getErrorDto(self) -> cern.lsa.client.rest.api.v1.dto.ErrorDto: ...
