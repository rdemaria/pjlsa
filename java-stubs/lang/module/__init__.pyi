import java.io
import java.lang
import java.net
import java.nio
import java.nio.file
import java.util
import java.util.function
import java.util.stream
import typing



class Configuration:
    """
    Java class 'java.lang.module.Configuration'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def empty() -> 'Configuration': ...
    def findModule(self, string: str) -> java.util.Optional['ResolvedModule']: ...
    def modules(self) -> java.util.Set['ResolvedModule']: ...
    def parents(self) -> java.util.List['Configuration']: ...
    @typing.overload
    def resolve(self, moduleFinder: 'ModuleFinder', moduleFinder2: 'ModuleFinder', collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'Configuration': ...
    @typing.overload
    @staticmethod
    def resolve(moduleFinder: 'ModuleFinder', list: java.util.List['Configuration'], moduleFinder2: 'ModuleFinder', collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'Configuration': ...
    @typing.overload
    def resolveAndBind(self, moduleFinder: 'ModuleFinder', moduleFinder2: 'ModuleFinder', collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'Configuration': ...
    @typing.overload
    @staticmethod
    def resolveAndBind(moduleFinder: 'ModuleFinder', list: java.util.List['Configuration'], moduleFinder2: 'ModuleFinder', collection: typing.Union[java.util.Collection[str], typing.Sequence[str]]) -> 'Configuration': ...
    def toString(self) -> str: ...

class FindException(java.lang.RuntimeException):
    """
    Java class 'java.lang.module.FindException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * FindException(java.lang.String, java.lang.Throwable)
        * FindException(java.lang.Throwable)
        * FindException(java.lang.String)
        * FindException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class InvalidModuleDescriptorException(java.lang.RuntimeException):
    """
    Java class 'java.lang.module.InvalidModuleDescriptorException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * InvalidModuleDescriptorException()
        * InvalidModuleDescriptorException(java.lang.String)
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class ModuleDescriptor(java.lang.Comparable['ModuleDescriptor']):
    """
    Java class 'java.lang.module.ModuleDescriptor'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            java.lang.Comparable
    
    """
    def compareTo(self, moduleDescriptor: 'ModuleDescriptor') -> int: ...
    def equals(self, object: typing.Any) -> bool: ...
    def exports(self) -> java.util.Set['ModuleDescriptor.Exports']: ...
    def hashCode(self) -> int: ...
    def isAutomatic(self) -> bool: ...
    def isOpen(self) -> bool: ...
    def mainClass(self) -> java.util.Optional[str]: ...
    def modifiers(self) -> java.util.Set['ModuleDescriptor.Modifier']: ...
    def name(self) -> str: ...
    @staticmethod
    def newAutomaticModule(string: str) -> 'ModuleDescriptor.Builder': ...
    @typing.overload
    @staticmethod
    def newModule(string: str) -> 'ModuleDescriptor.Builder': ...
    @typing.overload
    @staticmethod
    def newModule(string: str, set: java.util.Set['ModuleDescriptor.Modifier']) -> 'ModuleDescriptor.Builder': ...
    @staticmethod
    def newOpenModule(string: str) -> 'ModuleDescriptor.Builder': ...
    def opens(self) -> java.util.Set['ModuleDescriptor.Opens']: ...
    def packages(self) -> java.util.Set[str]: ...
    def provides(self) -> java.util.Set['ModuleDescriptor.Provides']: ...
    def rawVersion(self) -> java.util.Optional[str]: ...
    @typing.overload
    @staticmethod
    def read(inputStream: java.io.InputStream) -> 'ModuleDescriptor': ...
    @typing.overload
    @staticmethod
    def read(inputStream: java.io.InputStream, supplier: typing.Union[java.util.function.Supplier[java.util.Set[str]], typing.Callable[[], java.util.Set[str]]]) -> 'ModuleDescriptor': ...
    @typing.overload
    @staticmethod
    def read(byteBuffer: java.nio.ByteBuffer) -> 'ModuleDescriptor': ...
    @typing.overload
    @staticmethod
    def read(byteBuffer: java.nio.ByteBuffer, supplier: typing.Union[java.util.function.Supplier[java.util.Set[str]], typing.Callable[[], java.util.Set[str]]]) -> 'ModuleDescriptor': ...
    def requires(self) -> java.util.Set['ModuleDescriptor.Requires']: ...
    def toNameAndVersion(self) -> str: ...
    def toString(self) -> str: ...
    def uses(self) -> java.util.Set[str]: ...
    def version(self) -> java.util.Optional['ModuleDescriptor.Version']: ...
    class Builder:
        """
        Java class 'java.lang.module.ModuleDescriptor$Builder'
        
            Extends:
                java.lang.Object
        
        """
        def build(self) -> 'ModuleDescriptor': ...
        @typing.overload
        def exports(self, string: str) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def exports(self, string: str, set: java.util.Set[str]) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def exports(self, exports: 'ModuleDescriptor.Exports') -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def exports(self, set: java.util.Set['ModuleDescriptor.Exports.Modifier'], string: str) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def exports(self, set: java.util.Set['ModuleDescriptor.Exports.Modifier'], string: str, set2: java.util.Set[str]) -> 'ModuleDescriptor.Builder': ...
        def mainClass(self, string: str) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def opens(self, string: str) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def opens(self, string: str, set: java.util.Set[str]) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def opens(self, opens: 'ModuleDescriptor.Opens') -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def opens(self, set: java.util.Set['ModuleDescriptor.Opens.Modifier'], string: str) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def opens(self, set: java.util.Set['ModuleDescriptor.Opens.Modifier'], string: str, set2: java.util.Set[str]) -> 'ModuleDescriptor.Builder': ...
        def packages(self, set: java.util.Set[str]) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def provides(self, string: str, list: java.util.List[str]) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def provides(self, provides: 'ModuleDescriptor.Provides') -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def requires(self, string: str) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def requires(self, requires: 'ModuleDescriptor.Requires') -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def requires(self, set: java.util.Set['ModuleDescriptor.Requires.Modifier'], string: str) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def requires(self, set: java.util.Set['ModuleDescriptor.Requires.Modifier'], string: str, version: 'ModuleDescriptor.Version') -> 'ModuleDescriptor.Builder': ...
        def uses(self, string: str) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def version(self, string: str) -> 'ModuleDescriptor.Builder': ...
        @typing.overload
        def version(self, version: 'ModuleDescriptor.Version') -> 'ModuleDescriptor.Builder': ...
    class Exports(java.lang.Comparable['ModuleDescriptor.Exports']):
        """
        Java class 'java.lang.module.ModuleDescriptor$Exports'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.lang.Comparable
        
        """
        def compareTo(self, exports: 'ModuleDescriptor.Exports') -> int: ...
        def equals(self, object: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def isQualified(self) -> bool: ...
        def modifiers(self) -> java.util.Set['ModuleDescriptor.Exports.Modifier']: ...
        def source(self) -> str: ...
        def targets(self) -> java.util.Set[str]: ...
        def toString(self) -> str: ...
        class Modifier(java.lang.Enum['ModuleDescriptor.Exports.Modifier']):
            """
            Java class 'java.lang.module.ModuleDescriptor$Exports$Modifier'
            
                Extends:
                    java.lang.Enum
            
              Attributes:
                SYNTHETIC (java.lang.module.ModuleDescriptor$Exports$Modifier): final static enum constant
                MANDATED (java.lang.module.ModuleDescriptor$Exports$Modifier): final static enum constant
            
            """
            SYNTHETIC: typing.ClassVar['ModuleDescriptor.Exports.Modifier'] = ...
            MANDATED: typing.ClassVar['ModuleDescriptor.Exports.Modifier'] = ...
            _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
            @typing.overload
            @staticmethod
            def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
            @typing.overload
            @staticmethod
            def valueOf(string: str) -> 'ModuleDescriptor.Exports.Modifier': ...
            @staticmethod
            def values() -> typing.List['ModuleDescriptor.Exports.Modifier']: ...
    class Modifier(java.lang.Enum['ModuleDescriptor.Modifier']):
        """
        Java class 'java.lang.module.ModuleDescriptor$Modifier'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            OPEN (java.lang.module.ModuleDescriptor$Modifier): final static enum constant
            AUTOMATIC (java.lang.module.ModuleDescriptor$Modifier): final static enum constant
            SYNTHETIC (java.lang.module.ModuleDescriptor$Modifier): final static enum constant
            MANDATED (java.lang.module.ModuleDescriptor$Modifier): final static enum constant
        
        """
        OPEN: typing.ClassVar['ModuleDescriptor.Modifier'] = ...
        AUTOMATIC: typing.ClassVar['ModuleDescriptor.Modifier'] = ...
        SYNTHETIC: typing.ClassVar['ModuleDescriptor.Modifier'] = ...
        MANDATED: typing.ClassVar['ModuleDescriptor.Modifier'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ModuleDescriptor.Modifier': ...
        @staticmethod
        def values() -> typing.List['ModuleDescriptor.Modifier']: ...
    class Opens(java.lang.Comparable['ModuleDescriptor.Opens']):
        """
        Java class 'java.lang.module.ModuleDescriptor$Opens'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.lang.Comparable
        
        """
        def compareTo(self, opens: 'ModuleDescriptor.Opens') -> int: ...
        def equals(self, object: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def isQualified(self) -> bool: ...
        def modifiers(self) -> java.util.Set['ModuleDescriptor.Opens.Modifier']: ...
        def source(self) -> str: ...
        def targets(self) -> java.util.Set[str]: ...
        def toString(self) -> str: ...
        class Modifier(java.lang.Enum['ModuleDescriptor.Opens.Modifier']):
            """
            Java class 'java.lang.module.ModuleDescriptor$Opens$Modifier'
            
                Extends:
                    java.lang.Enum
            
              Attributes:
                SYNTHETIC (java.lang.module.ModuleDescriptor$Opens$Modifier): final static enum constant
                MANDATED (java.lang.module.ModuleDescriptor$Opens$Modifier): final static enum constant
            
            """
            SYNTHETIC: typing.ClassVar['ModuleDescriptor.Opens.Modifier'] = ...
            MANDATED: typing.ClassVar['ModuleDescriptor.Opens.Modifier'] = ...
            _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
            @typing.overload
            @staticmethod
            def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
            @typing.overload
            @staticmethod
            def valueOf(string: str) -> 'ModuleDescriptor.Opens.Modifier': ...
            @staticmethod
            def values() -> typing.List['ModuleDescriptor.Opens.Modifier']: ...
    class Provides(java.lang.Comparable['ModuleDescriptor.Provides']):
        """
        Java class 'java.lang.module.ModuleDescriptor$Provides'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.lang.Comparable
        
        """
        def compareTo(self, provides: 'ModuleDescriptor.Provides') -> int: ...
        def equals(self, object: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def providers(self) -> java.util.List[str]: ...
        def service(self) -> str: ...
        def toString(self) -> str: ...
    class Requires(java.lang.Comparable['ModuleDescriptor.Requires']):
        """
        Java class 'java.lang.module.ModuleDescriptor$Requires'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.lang.Comparable
        
        """
        def compareTo(self, requires: 'ModuleDescriptor.Requires') -> int: ...
        def compiledVersion(self) -> java.util.Optional['ModuleDescriptor.Version']: ...
        def equals(self, object: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        def modifiers(self) -> java.util.Set['ModuleDescriptor.Requires.Modifier']: ...
        def name(self) -> str: ...
        def rawCompiledVersion(self) -> java.util.Optional[str]: ...
        def toString(self) -> str: ...
        class Modifier(java.lang.Enum['ModuleDescriptor.Requires.Modifier']):
            """
            Java class 'java.lang.module.ModuleDescriptor$Requires$Modifier'
            
                Extends:
                    java.lang.Enum
            
              Attributes:
                TRANSITIVE (java.lang.module.ModuleDescriptor$Requires$Modifier): final static enum constant
                STATIC (java.lang.module.ModuleDescriptor$Requires$Modifier): final static enum constant
                SYNTHETIC (java.lang.module.ModuleDescriptor$Requires$Modifier): final static enum constant
                MANDATED (java.lang.module.ModuleDescriptor$Requires$Modifier): final static enum constant
            
            """
            TRANSITIVE: typing.ClassVar['ModuleDescriptor.Requires.Modifier'] = ...
            STATIC: typing.ClassVar['ModuleDescriptor.Requires.Modifier'] = ...
            SYNTHETIC: typing.ClassVar['ModuleDescriptor.Requires.Modifier'] = ...
            MANDATED: typing.ClassVar['ModuleDescriptor.Requires.Modifier'] = ...
            _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
            @typing.overload
            @staticmethod
            def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
            @typing.overload
            @staticmethod
            def valueOf(string: str) -> 'ModuleDescriptor.Requires.Modifier': ...
            @staticmethod
            def values() -> typing.List['ModuleDescriptor.Requires.Modifier']: ...
    class Version(java.lang.Comparable['ModuleDescriptor.Version']):
        """
        Java class 'java.lang.module.ModuleDescriptor$Version'
        
            Extends:
                java.lang.Object
        
            Interfaces:
                java.lang.Comparable
        
        """
        def compareTo(self, version: 'ModuleDescriptor.Version') -> int: ...
        def equals(self, object: typing.Any) -> bool: ...
        def hashCode(self) -> int: ...
        @staticmethod
        def parse(string: str) -> 'ModuleDescriptor.Version': ...
        def toString(self) -> str: ...

class ModuleFinder:
    """
    Java class 'java.lang.module.ModuleFinder'
    
    """
    @staticmethod
    def compose(moduleFinderArray: typing.List['ModuleFinder']) -> 'ModuleFinder': ...
    def find(self, string: str) -> java.util.Optional['ModuleReference']: ...
    def findAll(self) -> java.util.Set['ModuleReference']: ...
    @staticmethod
    def of(pathArray: typing.List[java.nio.file.Path]) -> 'ModuleFinder': ...
    @staticmethod
    def ofSystem() -> 'ModuleFinder': ...

class ModuleReader(java.io.Closeable):
    """
    Java class 'java.lang.module.ModuleReader'
    
        Interfaces:
            java.io.Closeable
    
    """
    def close(self) -> None: ...
    def find(self, string: str) -> java.util.Optional[java.net.URI]: ...
    def list(self) -> java.util.stream.Stream[str]: ...
    def open(self, string: str) -> java.util.Optional[java.io.InputStream]: ...
    def read(self, string: str) -> java.util.Optional[java.nio.ByteBuffer]: ...
    def release(self, byteBuffer: java.nio.ByteBuffer) -> None: ...

class ModuleReference:
    """
    Java class 'java.lang.module.ModuleReference'
    
        Extends:
            java.lang.Object
    
    """
    def descriptor(self) -> ModuleDescriptor: ...
    def location(self) -> java.util.Optional[java.net.URI]: ...
    def open(self) -> ModuleReader: ...

class ResolutionException(java.lang.RuntimeException):
    """
    Java class 'java.lang.module.ResolutionException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * ResolutionException(java.lang.String, java.lang.Throwable)
        * ResolutionException(java.lang.Throwable)
        * ResolutionException(java.lang.String)
        * ResolutionException()
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class ResolvedModule:
    """
    Java class 'java.lang.module.ResolvedModule'
    
        Extends:
            java.lang.Object
    
    """
    def configuration(self) -> Configuration: ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def name(self) -> str: ...
    def reads(self) -> java.util.Set['ResolvedModule']: ...
    def reference(self) -> ModuleReference: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.lang.module")``.

    Configuration: typing.Type[Configuration]
    FindException: typing.Type[FindException]
    InvalidModuleDescriptorException: typing.Type[InvalidModuleDescriptorException]
    ModuleDescriptor: typing.Type[ModuleDescriptor]
    ModuleFinder: typing.Type[ModuleFinder]
    ModuleReader: typing.Type[ModuleReader]
    ModuleReference: typing.Type[ModuleReference]
    ResolutionException: typing.Type[ResolutionException]
    ResolvedModule: typing.Type[ResolvedModule]
