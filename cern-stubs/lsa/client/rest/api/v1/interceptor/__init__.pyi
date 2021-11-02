import feign
import typing



class RbacInterceptor(feign.RequestInterceptor):
    """
    public class RbacInterceptor extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements feign.RequestInterceptor
    """
    def __init__(self): ...
    def apply(self, requestTemplate: feign.RequestTemplate) -> None:
        """
        
            Specified by:
                :code:`apply` in interface :code:`feign.RequestInterceptor`
        
        
        """
        ...

class TracingInterceptor(feign.RequestInterceptor):
    """
    public class TracingInterceptor extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements feign.RequestInterceptor
    """
    def __init__(self): ...
    def apply(self, requestTemplate: feign.RequestTemplate) -> None:
        """
        
            Specified by:
                :code:`apply` in interface :code:`feign.RequestInterceptor`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1.interceptor")``.

    RbacInterceptor: typing.Type[RbacInterceptor]
    TracingInterceptor: typing.Type[TracingInterceptor]
