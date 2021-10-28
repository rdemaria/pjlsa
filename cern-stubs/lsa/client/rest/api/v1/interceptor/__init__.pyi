import feign
import typing



class RbacInterceptor(feign.RequestInterceptor):
    """
    Java class 'cern.lsa.client.rest.api.v1.interceptor.RbacInterceptor'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            feign.RequestInterceptor
    
      Constructors:
        * RbacInterceptor()
    
    """
    def __init__(self): ...
    def apply(self, requestTemplate: feign.RequestTemplate) -> None: ...

class TracingInterceptor(feign.RequestInterceptor):
    """
    Java class 'cern.lsa.client.rest.api.v1.interceptor.TracingInterceptor'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            feign.RequestInterceptor
    
      Constructors:
        * TracingInterceptor()
    
    """
    def __init__(self): ...
    def apply(self, requestTemplate: feign.RequestTemplate) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.rest.api.v1.interceptor")``.

    RbacInterceptor: typing.Type[RbacInterceptor]
    TracingInterceptor: typing.Type[TracingInterceptor]
