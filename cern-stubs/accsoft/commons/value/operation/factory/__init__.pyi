import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.spi.operation
import java.lang
import typing



class OperationFactory:
    """
    Java class 'cern.accsoft.commons.value.operation.factory.OperationFactory'
    
    """
    def createIndexing(self, integer: int) -> cern.accsoft.commons.value.spi.operation.Indexing: ...
    def createUnaryMinus(self) -> cern.accsoft.commons.value.spi.operation.UnaryMinus: ...
    def findBinaryOperation(self, string: str) -> cern.accsoft.commons.value.operation.BinaryOperation: ...
    def findFunctionOperation(self, string: str) -> cern.accsoft.commons.value.operation.MultiOperation: ...
    def findUnaryOperation(self, string: str) -> cern.accsoft.commons.value.operation.UnaryOperation: ...
    def getCoreOperation(self, coreOperation: 'OperationFactory.CoreOperation') -> cern.accsoft.commons.value.operation.BinaryOperation: ...
    def init(self) -> None: ...
    def registerProvider(self, operationProvider: 'OperationProvider'[cern.accsoft.commons.value.operation.Operation]) -> None: ...
    class CoreOperation(java.lang.Enum['OperationFactory.CoreOperation']):
        """
        Java class 'cern.accsoft.commons.value.operation.factory.OperationFactory$CoreOperation'
        
            Extends:
                java.lang.Enum
        
          Attributes:
            ADDITION (cern.accsoft.commons.value.operation.factory.OperationFactory$CoreOperation): final static enum constant
            SUBTRACTION (cern.accsoft.commons.value.operation.factory.OperationFactory$CoreOperation): final static enum constant
            MULTIPLICATION (cern.accsoft.commons.value.operation.factory.OperationFactory$CoreOperation): final static enum constant
            DIVISION (cern.accsoft.commons.value.operation.factory.OperationFactory$CoreOperation): final static enum constant
            EXPONENTIATION (cern.accsoft.commons.value.operation.factory.OperationFactory$CoreOperation): final static enum constant
        
        """
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
    Java class 'cern.accsoft.commons.value.operation.factory.OperationProvider'
    
    """
    def doProvide(self) -> None: ...
    def getInstance(self, string: str) -> _OperationProvider__T: ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType: ...

class AbstractOperationFactory(OperationFactory):
    """
    Java class 'cern.accsoft.commons.value.operation.factory.AbstractOperationFactory'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.operation.factory.OperationFactory
    
      Constructors:
        * AbstractOperationFactory()
    
    """
    def __init__(self): ...
    def createUnaryMinus(self) -> cern.accsoft.commons.value.spi.operation.UnaryMinus: ...
    def getCoreOperation(self, coreOperation: OperationFactory.CoreOperation) -> cern.accsoft.commons.value.operation.BinaryOperation: ...
    def init(self) -> None: ...
    def registerProvider(self, operationProvider: OperationProvider[cern.accsoft.commons.value.operation.Operation]) -> None: ...

_AbstractOperationProvider__T = typing.TypeVar('_AbstractOperationProvider__T', bound=cern.accsoft.commons.value.operation.Operation)  # <T>
class AbstractOperationProvider(OperationProvider[_AbstractOperationProvider__T], typing.Generic[_AbstractOperationProvider__T]):
    """
    Java class 'cern.accsoft.commons.value.operation.factory.AbstractOperationProvider'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.operation.factory.OperationProvider
    
      Constructors:
        * AbstractOperationProvider()
    
    """
    def __init__(self): ...
    def doProvide(self) -> None: ...
    def getInstance(self, string: str) -> _AbstractOperationProvider__T: ...

class DefaultOperationFactory(AbstractOperationFactory):
    """
    Java class 'cern.accsoft.commons.value.operation.factory.DefaultOperationFactory'
    
        Extends:
            cern.accsoft.commons.value.operation.factory.AbstractOperationFactory
    
      Constructors:
        * DefaultOperationFactory()
    
    """
    def __init__(self): ...
    def createIndexing(self, integer: int) -> cern.accsoft.commons.value.spi.operation.Indexing: ...
    def findBinaryOperation(self, string: str) -> cern.accsoft.commons.value.operation.BinaryOperation: ...
    def findFunctionOperation(self, string: str) -> cern.accsoft.commons.value.operation.MultiOperation: ...
    def findUnaryOperation(self, string: str) -> cern.accsoft.commons.value.operation.UnaryOperation: ...
    def init(self) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.value.operation.factory")``.

    AbstractOperationFactory: typing.Type[AbstractOperationFactory]
    AbstractOperationProvider: typing.Type[AbstractOperationProvider]
    DefaultOperationFactory: typing.Type[DefaultOperationFactory]
    OperationFactory: typing.Type[OperationFactory]
    OperationProvider: typing.Type[OperationProvider]
