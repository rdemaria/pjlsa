import cern.lsa.client.rest.api.v1.dto.commons
import cern.lsa.client.rest.api.v1.dto.trim.tag
import com.fasterxml.jackson.databind
import java.util
import typing



class FeignService:
    """
    public interface FeignService
    """
    ...

class FeignServiceLocator:
    """
    public class FeignServiceLocator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def createObjectMapper() -> com.fasterxml.jackson.databind.ObjectMapper: ...
    @staticmethod
    def forHostAndPort(string: str, int: int) -> 'FeignServiceLocator': ...
    _getFeignService__T = typing.TypeVar('_getFeignService__T', bound=FeignService)  # <T>
    def getFeignService(self, class_: typing.Type[_getFeignService__T]) -> _getFeignService__T: ...

class TrimTagFeignService(FeignService):
    """
    public interface TrimTagFeignService extends :class:`~cern.lsa.client.rest.api.v1.feign.FeignService`
    """
    def findTrimTagAttributeDefinitions(self, string: str) -> java.util.Set[cern.lsa.client.rest.api.v1.dto.commons.AttributeDefinitionDto]: ...
    def findTrimTags(self, trimTagsRequestDto: cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagsRequestDto) -> java.util.List[cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto]: ...
    def tagSettings(self, trimTagCreationRequestDto: cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagCreationRequestDto) -> cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto: ...
    def updateTrimTag(self, trimTagDto: cern.lsa.client.rest.api.v1.dto.trim.tag.TrimTagDto) -> None: ...
    class Urls:
        TAG_SETTINGS: typing.ClassVar[str] = ...
        UPDATE_TRIM_TAG: typing.ClassVar[str] = ...
        FIND_TRIM_TAGS: typing.ClassVar[str] = ...
        FIND_TRIM_TAG_ATTRIBUTE_DEFINITIONS: typing.ClassVar[str] = ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1.feign")``.

    FeignService: typing.Type[FeignService]
    FeignServiceLocator: typing.Type[FeignServiceLocator]
    TrimTagFeignService: typing.Type[TrimTagFeignService]
