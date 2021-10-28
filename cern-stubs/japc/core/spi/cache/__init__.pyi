import java.lang
import typing



class JapcCache:
    """
    Java class 'cern.japc.core.spi.cache.JapcCache'
    
    """
    def clearAll(self) -> None: ...

class JapcCacheException(java.lang.Exception):
    """
    Java class 'cern.japc.core.spi.cache.JapcCacheException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * JapcCacheException(java.lang.String)
        * JapcCacheException(java.lang.Throwable)
        * JapcCacheException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class JapcCacheType(java.lang.Enum['JapcCacheType']):
    """
    Java class 'cern.japc.core.spi.cache.JapcCacheType'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        DEVICE_TYPE (cern.japc.core.spi.cache.JapcCacheType): final static enum constant
        DEVICE (cern.japc.core.spi.cache.JapcCacheType): final static enum constant
        PARAMETER (cern.japc.core.spi.cache.JapcCacheType): final static enum constant
        DEVICE_DESCRIPTOR (cern.japc.core.spi.cache.JapcCacheType): final static enum constant
        PARAMETER_DESCRIPTOR (cern.japc.core.spi.cache.JapcCacheType): final static enum constant
        VALUE_DESCRIPTOR (cern.japc.core.spi.cache.JapcCacheType): final static enum constant
        SERVICE_CONFIG (cern.japc.core.spi.cache.JapcCacheType): final static enum constant
        ENUM (cern.japc.core.spi.cache.JapcCacheType): final static enum constant
    
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
    def valueOf(string: str) -> 'JapcCacheType': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['JapcCacheType']: ...

class JapcCacheController(JapcCache):
    """
    Java class 'cern.japc.core.spi.cache.JapcCacheController'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.japc.core.spi.cache.JapcCache
    
      Constructors:
        * JapcCacheController()
    
    """
    def __init__(self): ...
    def clearAll(self) -> None: ...
    @staticmethod
    def getInstance() -> 'JapcCacheController': ...
    def registerCache(self, japcCache: JapcCache) -> None: ...
    def unregisterCache(self, japcCache: JapcCache) -> None: ...
    class JmxMBean:
        """
        Java class 'cern.japc.core.spi.cache.JapcCacheController$JmxMBean'
        
        """
        def clearAll(self) -> None: ...
        def getRegisteredCaches(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.cache")``.

    JapcCache: typing.Type[JapcCache]
    JapcCacheController: typing.Type[JapcCacheController]
    JapcCacheException: typing.Type[JapcCacheException]
    JapcCacheType: typing.Type[JapcCacheType]
