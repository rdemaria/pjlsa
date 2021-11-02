import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.spi.operation
import java.lang
import typing



class OperationFactory:
    """
    public interface OperationFactory
    
        main interface for the operation factory. extend it if you for some reason want to provide your own implementation
    """
    def createIndexing(self, integer: int) -> cern.accsoft.commons.value.spi.operation.Indexing:
        """
            provides an indexing operation is a separate operation as the parser doesn't support type changing during parsing
        
            Parameters:
                index (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): an index of the array
        
            Returns:
                Indexing
        
        
        """
        ...
    def createUnaryMinus(self) -> cern.accsoft.commons.value.spi.operation.UnaryMinus:
        """
            provides an instance of UnaryMinus operation
        
            Returns:
        
        
        """
        ...
    def findBinaryOperation(self, string: str) -> cern.accsoft.commons.value.operation.BinaryOperation:
        """
            Returns the binary operation of the given name. If the no binary operation of that name can be found null is returned.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the binary operation to find
        
            Returns:
                the operation of that name or null if it cannot be found
        
        
        """
        ...
    def findFunctionOperation(self, string: str) -> cern.accsoft.commons.value.operation.MultiOperation:
        """
            method to find registered functions
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): 
            Returns:
        
        
        """
        ...
    def findUnaryOperation(self, string: str) -> cern.accsoft.commons.value.operation.UnaryOperation:
        """
            Returns the unary operation of the given name. If the no unary operation of that name can be found null is returned.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the unary operation to find
        
            Returns:
                the operation of that name or null if it cannot be found
        
        
        """
        ...
    def getCoreOperation(self, coreOperation: 'OperationFactory.CoreOperation') -> cern.accsoft.commons.value.operation.BinaryOperation:
        """
            method to get a core operation.
        
            Parameters:
                co (:class:`~cern.accsoft.commons.value.operation.factory.OperationFactory.CoreOperation`): 
            Returns:
        
        
        """
        ...
    def init(self) -> None:
        """
            init method for the factory
        
        """
        ...
    def registerProvider(self, operationProvider: 'OperationProvider'[cern.accsoft.commons.value.operation.Operation]) -> None: ...
    class CoreOperation(java.lang.Enum['OperationFactory.CoreOperation']):
        ADDITION: typing.ClassVar['OperationFactory.CoreOperation'] = ...
        SUBTRACTION: typing.ClassVar['OperationFactory.CoreOperation'] = ...
        MULTIPLICATION: typing.ClassVar['OperationFactory.CoreOperation'] = ...
        DIVISION: typing.ClassVar['OperationFactory.CoreOperation'] = ...
        EXPONENTIATION: typing.ClassVar['OperationFactory.CoreOperation'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'OperationFactory.CoreOperation': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['OperationFactory.CoreOperation']: ...

_OperationProvider__T = typing.TypeVar('_OperationProvider__T')  # <T>
class OperationProvider(typing.Generic[_OperationProvider__T]):
    """
    public interface OperationProvider<T>
    
        interface that defines a custom operation module and provides operations of a certain type
    """
    def doProvide(self) -> None:
        """
            init method, which is usually called from OperationFactory instance to prepare the provider
        
        """
        ...
    def getInstance(self, string: str) -> _OperationProvider__T: ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType:
        """
            method to specify which type of operation is provided
        
            Returns:
        
        
        """
        ...

class AbstractOperationFactory(OperationFactory):
    """
    public abstract class AbstractOperationFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.operation.factory.OperationFactory`
    
        an abstract "all-that-should-be-there" operation factory
    """
    def __init__(self): ...
    def createUnaryMinus(self) -> cern.accsoft.commons.value.spi.operation.UnaryMinus:
        """
            Description copied from
            interface:Â :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.createUnaryMinus`
            provides an instance of UnaryMinus operation
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.createUnaryMinus`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.factory.OperationFactory`
        
            Returns:
        
        
        """
        ...
    def getCoreOperation(self, coreOperation: OperationFactory.CoreOperation) -> cern.accsoft.commons.value.operation.BinaryOperation:
        """
            Description copied from
            interface:Â :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.getCoreOperation`
            method to get a core operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.getCoreOperation`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.factory.OperationFactory`
        
            Returns:
        
        
        """
        ...
    def init(self) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.init`
            init method for the factory
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.init`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.factory.OperationFactory`
        
        
        """
        ...
    def registerProvider(self, operationProvider: OperationProvider[cern.accsoft.commons.value.operation.Operation]) -> None: ...

_AbstractOperationProvider__T = typing.TypeVar('_AbstractOperationProvider__T', bound=cern.accsoft.commons.value.operation.Operation)  # <T>
class AbstractOperationProvider(OperationProvider[_AbstractOperationProvider__T], typing.Generic[_AbstractOperationProvider__T]):
    """
    public abstract class AbstractOperationProvider<T extends :class:`~cern.accsoft.commons.value.operation.Operation`> extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.operation.factory.OperationProvider`<T>
    """
    def __init__(self): ...
    def doProvide(self) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.factory.OperationProvider.doProvide`
            init method, which is usually called from OperationFactory instance to prepare the provider
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.factory.OperationProvider.doProvide`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.factory.OperationProvider`
        
        
        """
        ...
    def getInstance(self, string: str) -> _AbstractOperationProvider__T:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.factory.OperationProvider.getInstance`
            method to ask this provider of an operation instance
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.factory.OperationProvider.getInstance`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.factory.OperationProvider`
        
            Returns:
        
        
        """
        ...

class DefaultOperationFactory(AbstractOperationFactory):
    """
    public class DefaultOperationFactory extends :class:`~cern.accsoft.commons.value.operation.factory.AbstractOperationFactory`
    
        default factory for available binary and unary operations
    """
    def __init__(self): ...
    def createIndexing(self, integer: int) -> cern.accsoft.commons.value.spi.operation.Indexing:
        """
            Description copied from
            interface:Â :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.createIndexing`
            provides an indexing operation is a separate operation as the parser doesn't support type changing during parsing
        
            Parameters:
                index (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): an index of the array
        
            Returns:
                Indexing
        
        
        """
        ...
    def findBinaryOperation(self, string: str) -> cern.accsoft.commons.value.operation.BinaryOperation:
        """
            Description copied from
            interface:Â :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.findBinaryOperation`
            Returns the binary operation of the given name. If the no binary operation of that name can be found null is returned.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the binary operation to find
        
            Returns:
                the operation of that name or null if it cannot be found
        
        
        """
        ...
    def findFunctionOperation(self, string: str) -> cern.accsoft.commons.value.operation.MultiOperation:
        """
            Description copied from
            interface:Â :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.findFunctionOperation`
            method to find registered functions
        
            Returns:
        
        
        """
        ...
    def findUnaryOperation(self, string: str) -> cern.accsoft.commons.value.operation.UnaryOperation:
        """
            Description copied from
            interface:Â :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.findUnaryOperation`
            Returns the unary operation of the given name. If the no unary operation of that name can be found null is returned.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the unary operation to find
        
            Returns:
                the operation of that name or null if it cannot be found
        
        
        """
        ...
    def init(self) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.init`
            init method for the factory
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.factory.OperationFactory.init`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.factory.OperationFactory`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.operation.factory.AbstractOperationFactory.init`Â in
                classÂ :class:`~cern.accsoft.commons.value.operation.factory.AbstractOperationFactory`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.value.operation.factory")``.

    AbstractOperationFactory: typing.Type[AbstractOperationFactory]
    AbstractOperationProvider: typing.Type[AbstractOperationProvider]
    DefaultOperationFactory: typing.Type[DefaultOperationFactory]
    OperationFactory: typing.Type[OperationFactory]
    OperationProvider: typing.Type[OperationProvider]
