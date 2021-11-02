import java.lang
import typing



class JapcCache:
    """
    public interface JapcCache
    
        Interface to be implemented by all the JAPC components which implement any kind of caching which should be managed via
        central JAPC Cache API.
    """
    def clearAll(self) -> None: ...

class JapcCacheException(java.lang.Exception):
    """
    public class JapcCacheException extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`
    
        This exception is thrown in case of problems with JAPC cache management
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class JapcCacheType(java.lang.Enum['JapcCacheType']):
    """
    public enum JapcCacheType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.japc.core.spi.cache.JapcCacheType`>
    
        All the possible types of JAPC cached information.
    
        Different components of JAPC can cache the JAPC parameters, JAPC descriptors, JAPC services configurations, enumeration
        definitions, etc.
    """
    DEVICE_TYPE: typing.ClassVar['JapcCacheType'] = ...
    DEVICE: typing.ClassVar['JapcCacheType'] = ...
    PARAMETER: typing.ClassVar['JapcCacheType'] = ...
    DEVICE_DESCRIPTOR: typing.ClassVar['JapcCacheType'] = ...
    PARAMETER_DESCRIPTOR: typing.ClassVar['JapcCacheType'] = ...
    VALUE_DESCRIPTOR: typing.ClassVar['JapcCacheType'] = ...
    SERVICE_CONFIG: typing.ClassVar['JapcCacheType'] = ...
    ENUM: typing.ClassVar['JapcCacheType'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'JapcCacheType':
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
    def values() -> typing.List['JapcCacheType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (JapcCacheType c : JapcCacheType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class JapcCacheController(JapcCache):
    """
    public class JapcCacheController extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.cache.JapcCache`
    
        The JAPC controller to handle the cached information.
    """
    def __init__(self): ...
    def clearAll(self) -> None: ...
    @staticmethod
    def getInstance() -> 'JapcCacheController':
        """
            Getter for the singleton of :class:`~cern.japc.core.spi.cache.JapcCacheController`.
        
            Returns:
                the singleton of :class:`~cern.japc.core.spi.cache.JapcCacheController`
        
        
        """
        ...
    def registerCache(self, japcCache: JapcCache) -> None:
        """
            Registers a new JAPC cache
        
            Parameters:
                cache (:class:`~cern.japc.core.spi.cache.JapcCache`): JAPC cache
        
        
        """
        ...
    def unregisterCache(self, japcCache: JapcCache) -> None:
        """
            Unregisters a JAPC cache
        
            Parameters:
                cache (:class:`~cern.japc.core.spi.cache.JapcCache`): JAPC cache
        
        
        """
        ...
    class JmxMBean:
        def clearAll(self) -> None: ...
        def getRegisteredCaches(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.cache")``.

    JapcCache: typing.Type[JapcCache]
    JapcCacheController: typing.Type[JapcCacheController]
    JapcCacheException: typing.Type[JapcCacheException]
    JapcCacheType: typing.Type[JapcCacheType]
