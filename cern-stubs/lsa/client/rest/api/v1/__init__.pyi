import cern.accsoft.commons.domain
import cern.lsa.client
import cern.lsa.client.rest.api.v1.dto
import cern.lsa.client.rest.api.v1.error
import cern.lsa.client.rest.api.v1.feign
import cern.lsa.client.rest.api.v1.interceptor
import cern.lsa.client.rest.api.v1.mapper
import cern.lsa.domain.commons
import cern.lsa.domain.trim.tag
import java.lang
import java.util
import org.springframework.context
import typing



class AbstractClientRestConfig:
    """
    @Configuration @PropertySource(value="classpath:${lsa.server.properties}", ignoreResourceNotFound=true) public abstract class AbstractClientRestConfig extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self): ...

class ClientRestTrimTagService(cern.lsa.client.TrimTagService, org.springframework.context.ApplicationContextAware):
    """
    public class ClientRestTrimTagService extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements cern.lsa.client.TrimTagService, org.springframework.context.ApplicationContextAware
    """
    def __init__(self, trimTagFeignService: cern.lsa.client.rest.api.v1.feign.TrimTagFeignService, toDto: cern.lsa.client.rest.api.v1.mapper.ToDto, fromDto: cern.lsa.client.rest.api.v1.mapper.FromDto): ...
    def findTrimTagAttributeDefinitions(self, accelerator: cern.accsoft.commons.domain.Accelerator) -> java.util.Set[cern.lsa.domain.commons.AttributeDefinition]: ...
    def findTrimTags(self, trimTagsRequest: cern.lsa.domain.trim.tag.TrimTagsRequest) -> java.util.List[cern.lsa.domain.trim.tag.TrimTag]: ...
    def setApplicationContext(self, applicationContext: org.springframework.context.ApplicationContext) -> None:
        """
        
            Specified by:
                :code:`setApplicationContext` in interface :code:`org.springframework.context.ApplicationContextAware`
        
        
        """
        ...
    def tagSettings(self, trimTagCreationRequest: cern.lsa.domain.trim.tag.TrimTagCreationRequest) -> cern.lsa.domain.trim.tag.TrimTag:
        """
        
            Specified by:
                :code:`tagSettings` in interface :code:`cern.lsa.client.TrimTagService`
        
        
        """
        ...
    def updateTrimTag(self, trimTag: cern.lsa.domain.trim.tag.TrimTag) -> None:
        """
        
            Specified by:
                :code:`updateTrimTag` in interface :code:`cern.lsa.client.TrimTagService`
        
        
        """
        ...

class HttpHeaders(java.lang.Enum['HttpHeaders']):
    """
    public enum HttpHeaders extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.lsa.client.rest.api.v1.HttpHeaders`>
    """
    X_CLIENT_ID: typing.ClassVar['HttpHeaders'] = ...
    def getValue(self) -> str: ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'HttpHeaders':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['HttpHeaders']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (HttpHeaders c : HttpHeaders.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1")``.

    AbstractClientRestConfig: typing.Type[AbstractClientRestConfig]
    ClientRestTrimTagService: typing.Type[ClientRestTrimTagService]
    HttpHeaders: typing.Type[HttpHeaders]
    dto: cern.lsa.client.rest.api.v1.dto.__module_protocol__
    error: cern.lsa.client.rest.api.v1.error.__module_protocol__
    feign: cern.lsa.client.rest.api.v1.feign.__module_protocol__
    interceptor: cern.lsa.client.rest.api.v1.interceptor.__module_protocol__
    mapper: cern.lsa.client.rest.api.v1.mapper.__module_protocol__
