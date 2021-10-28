import java.lang.reflect
import java.util.concurrent
import org.springframework.beans.factory
import org.springframework.cache
import org.springframework.cache.annotation
import org.springframework.cache.interceptor
import org.springframework.cache.support
import typing



class AbstractCacheConfig(org.springframework.cache.annotation.CachingConfigurerSupport):
    """
    Java class 'cern.lsa.client.common.cache.AbstractCacheConfig'
    
        Extends:
            org.springframework.cache.annotation.CachingConfigurerSupport
    
      Constructors:
        * AbstractCacheConfig()
    
    """
    def __init__(self): ...
    def keyGenerator(self) -> org.springframework.cache.interceptor.KeyGenerator: ...

class CacheKeyGenerator(org.springframework.cache.interceptor.KeyGenerator):
    """
    Java class 'cern.lsa.client.common.cache.CacheKeyGenerator'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.springframework.cache.interceptor.KeyGenerator
    
      Constructors:
        * CacheKeyGenerator()
    
    """
    def __init__(self): ...
    def generate(self, object: typing.Any, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any]) -> typing.Any: ...

class ClientCache(org.springframework.cache.Cache, org.springframework.beans.factory.BeanNameAware):
    """
    Java class 'cern.lsa.client.common.cache.ClientCache'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            org.springframework.cache.Cache,
            org.springframework.beans.factory.BeanNameAware
    
    """
    def clear(self) -> None: ...
    def destroy(self) -> None: ...
    def evict(self, object: typing.Any) -> None: ...
    _get_0__T = typing.TypeVar('_get_0__T')  # <T>
    _get_1__T = typing.TypeVar('_get_1__T')  # <T>
    @typing.overload
    def get(self, object: typing.Any, class_: typing.Type[_get_0__T]) -> _get_0__T: ...
    @typing.overload
    def get(self, object: typing.Any, callable: typing.Union[java.util.concurrent.Callable[_get_1__T], typing.Callable[[], _get_1__T]]) -> _get_1__T: ...
    @typing.overload
    def get(self, object: typing.Any) -> org.springframework.cache.Cache.ValueWrapper: ...
    @staticmethod
    def getInstance() -> 'ClientCache': ...
    def getName(self) -> str: ...
    def getNativeCache(self) -> typing.Any: ...
    def put(self, object: typing.Any, object2: typing.Any) -> None: ...
    def putIfAbsent(self, object: typing.Any, object2: typing.Any) -> org.springframework.cache.Cache.ValueWrapper: ...
    def setBeanName(self, string: str) -> None: ...

class ClientCacheManagerConfig:
    """
    Java class 'cern.lsa.client.common.cache.ClientCacheManagerConfig'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ClientCacheManagerConfig()
    
    """
    def __init__(self): ...
    def clientCacheManager(self) -> org.springframework.cache.support.SimpleCacheManager: ...

class ClientCacheConfig(AbstractCacheConfig):
    """
    Java class 'cern.lsa.client.common.cache.ClientCacheConfig'
    
        Extends:
            cern.lsa.client.common.cache.AbstractCacheConfig
    
      Constructors:
        * ClientCacheConfig()
    
    """
    def __init__(self): ...
    def cacheManager(self) -> org.springframework.cache.CacheManager: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.lsa.client.common.cache")``.

    AbstractCacheConfig: typing.Type[AbstractCacheConfig]
    CacheKeyGenerator: typing.Type[CacheKeyGenerator]
    ClientCache: typing.Type[ClientCache]
    ClientCacheConfig: typing.Type[ClientCacheConfig]
    ClientCacheManagerConfig: typing.Type[ClientCacheManagerConfig]
