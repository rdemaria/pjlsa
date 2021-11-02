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
    @Configuration public abstract class AbstractCacheConfig extends org.springframework.cache.annotation.CachingConfigurerSupport
    """
    def __init__(self): ...
    def keyGenerator(self) -> org.springframework.cache.interceptor.KeyGenerator: ...

class CacheKeyGenerator(org.springframework.cache.interceptor.KeyGenerator):
    """
    public class CacheKeyGenerator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements org.springframework.cache.interceptor.KeyGenerator
    
        Client side key generator which uses toString methods of method's parameters to compose key.
    """
    def __init__(self): ...
    def generate(self, object: typing.Any, method: java.lang.reflect.Method, objectArray: typing.List[typing.Any]) -> typing.Any: ...

class ClientCache(org.springframework.cache.Cache, org.springframework.beans.factory.BeanNameAware):
    """
    public class ClientCache extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements org.springframework.cache.Cache, org.springframework.beans.factory.BeanNameAware
    
        Simple cache based on ConcurrentHashMap with possibility to set time to live. Used in 3tier client to avoid depending on
        fat jar with full feature cache.
    """
    def clear(self) -> None:
        """
        
            Specified by:
                :code:`clear` in interface :code:`org.springframework.cache.Cache`
        
        
        """
        ...
    def destroy(self) -> None:
        """
            This method is called to stop the scheduler, it can be registered in Spring as a bean destroyMethod e.g.
            Bean(destroyMethod = "destroy")
        
        """
        ...
    def evict(self, object: typing.Any) -> None:
        """
        
            Specified by:
                :code:`evict` in interface :code:`org.springframework.cache.Cache`
        
        
        """
        ...
    _get_0__T = typing.TypeVar('_get_0__T')  # <T>
    _get_1__T = typing.TypeVar('_get_1__T')  # <T>
    @typing.overload
    def get(self, object: typing.Any, class_: typing.Type[_get_0__T]) -> _get_0__T: ...
    @typing.overload
    def get(self, object: typing.Any, callable: typing.Union[java.util.concurrent.Callable[_get_1__T], typing.Callable[[], _get_1__T]]) -> _get_1__T: ...
    @typing.overload
    def get(self, object: typing.Any) -> org.springframework.cache.Cache.ValueWrapper:
        """
        
            Specified by:
                :code:`get` in interface :code:`org.springframework.cache.Cache`
        
        public <T> T get (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` key, `Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`<T> clazz)
        
        
            Specified by:
                :code:`get` in interface :code:`org.springframework.cache.Cache`
        
        public <T> T get (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` key, `Callable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/concurrent/Callable.html?is-external=true>`<T> valueLoader)
        
        
            Specified by:
                :code:`get` in interface :code:`org.springframework.cache.Cache`
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'ClientCache': ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`org.springframework.cache.Cache`
        
        
        """
        ...
    def getNativeCache(self) -> typing.Any:
        """
        
            Specified by:
                :code:`getNativeCache` in interface :code:`org.springframework.cache.Cache`
        
        
        """
        ...
    def put(self, object: typing.Any, object2: typing.Any) -> None:
        """
        
            Specified by:
                :code:`put` in interface :code:`org.springframework.cache.Cache`
        
        
        """
        ...
    def putIfAbsent(self, object: typing.Any, object2: typing.Any) -> org.springframework.cache.Cache.ValueWrapper:
        """
        
            Specified by:
                :code:`putIfAbsent` in interface :code:`org.springframework.cache.Cache`
        
        
        """
        ...
    def setBeanName(self, string: str) -> None:
        """
        
            Specified by:
                :code:`setBeanName` in interface :code:`org.springframework.beans.factory.BeanNameAware`
        
        
        """
        ...

class ClientCacheManagerConfig:
    """
    @Configuration public class ClientCacheManagerConfig extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    def __init__(self): ...
    def clientCacheManager(self) -> org.springframework.cache.support.SimpleCacheManager: ...

class ClientCacheConfig(AbstractCacheConfig):
    """
    @EnableCaching(order=1) @Configuration @Import(:class:`~cern.lsa.client.common.cache.ClientCacheManagerConfig`) public class ClientCacheConfig extends :class:`~cern.lsa.client.common.cache.AbstractCacheConfig`
    
        This configuration is for 3-tier client applications only, which only use the client caches.
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
