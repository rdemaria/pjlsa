import feign


class RbacInterceptor(feign.RequestInterceptor):
    def __init__(self): ...
    def apply(self, requestTemplate: feign.RequestTemplate) -> None: ...
