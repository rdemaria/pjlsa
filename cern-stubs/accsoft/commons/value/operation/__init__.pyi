import cern.accsoft.commons.value
import cern.accsoft.commons.value.expression
import cern.accsoft.commons.value.operation.factory
import java.lang
import java.util
import typing



class BoundedPolynomialOperations:
    """
    Java class 'cern.accsoft.commons.value.operation.BoundedPolynomialOperations'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def differentiate(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial) -> cern.accsoft.commons.value.BoundedPolynomial: ...
    @staticmethod
    def integrate(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, double: float) -> cern.accsoft.commons.value.BoundedPolynomial: ...
    @staticmethod
    def neg(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial) -> cern.accsoft.commons.value.BoundedPolynomial: ...
    @staticmethod
    def scale(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, double: float) -> cern.accsoft.commons.value.BoundedPolynomial: ...
    @staticmethod
    def scaleArg(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, double: float) -> cern.accsoft.commons.value.BoundedPolynomial: ...
    @staticmethod
    def shift(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, double: float) -> cern.accsoft.commons.value.BoundedPolynomial: ...
    @staticmethod
    def shiftArg(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, double: float) -> cern.accsoft.commons.value.BoundedPolynomial: ...

class BoundedPolynomialSequenceBinaryOperations:
    """
    Java class 'cern.accsoft.commons.value.operation.BoundedPolynomialSequenceBinaryOperations'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def add(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, boundedPolynomialSequence2: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...
    @staticmethod
    def concat(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, boundedPolynomialSequence2: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...
    @staticmethod
    def multiply(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, boundedPolynomialSequence2: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...
    @staticmethod
    def subtract(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, boundedPolynomialSequence2: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...

class BoundedPolynomialSequenceOperations:
    """
    Java class 'cern.accsoft.commons.value.operation.BoundedPolynomialSequenceOperations'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def differentiate(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...
    @staticmethod
    def integrate(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, double: float) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...
    @staticmethod
    def neg(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...
    @staticmethod
    def scale(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, double: float) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...
    @staticmethod
    def scaleArg(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, double: float) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...
    @staticmethod
    def shift(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, double: float) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...
    @staticmethod
    def shiftArg(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, double: float) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...

class Operation:
    """
    Java class 'cern.accsoft.commons.value.operation.Operation'
    
    """
    def getType(self) -> 'OperationType': ...

class OperationException(java.lang.RuntimeException):
    """
    Java class 'cern.accsoft.commons.value.operation.OperationException'
    
        Extends:
            java.lang.RuntimeException
    
      Constructors:
        * OperationException(java.lang.String)
        * OperationException(java.lang.Throwable)
        * OperationException(java.lang.String, java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class OperationType(java.lang.Enum['OperationType']):
    """
    Java class 'cern.accsoft.commons.value.operation.OperationType'
    
        Extends:
            java.lang.Enum
    
      Attributes:
        BINARY (cern.accsoft.commons.value.operation.OperationType): final static enum constant
        UNARY (cern.accsoft.commons.value.operation.OperationType): final static enum constant
        INDEXING (cern.accsoft.commons.value.operation.OperationType): final static enum constant
        FUNCTION (cern.accsoft.commons.value.operation.OperationType): final static enum constant
        CUSTOM (cern.accsoft.commons.value.operation.OperationType): final static enum constant
    
    """
    BINARY: typing.ClassVar['OperationType'] = ...
    UNARY: typing.ClassVar['OperationType'] = ...
    INDEXING: typing.ClassVar['OperationType'] = ...
    FUNCTION: typing.ClassVar['OperationType'] = ...
    CUSTOM: typing.ClassVar['OperationType'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OperationType': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['OperationType']: ...

class PolynomialBinaryOperations:
    """
    Java class 'cern.accsoft.commons.value.operation.PolynomialBinaryOperations'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def add(polynomial: cern.accsoft.commons.value.Polynomial, polynomial2: cern.accsoft.commons.value.Polynomial) -> cern.accsoft.commons.value.Polynomial: ...
    @staticmethod
    def multiply(polynomial: cern.accsoft.commons.value.Polynomial, polynomial2: cern.accsoft.commons.value.Polynomial) -> cern.accsoft.commons.value.Polynomial: ...
    @staticmethod
    def subtract(polynomial: cern.accsoft.commons.value.Polynomial, polynomial2: cern.accsoft.commons.value.Polynomial) -> cern.accsoft.commons.value.Polynomial: ...

class PolynomialOperations:
    """
    Java class 'cern.accsoft.commons.value.operation.PolynomialOperations'
    
        Extends:
            java.lang.Object
    
    """
    @staticmethod
    def differentiate(polynomial: cern.accsoft.commons.value.Polynomial) -> cern.accsoft.commons.value.Polynomial: ...
    @staticmethod
    def integrate(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> cern.accsoft.commons.value.Polynomial: ...
    @typing.overload
    @staticmethod
    def invert(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> float: ...
    @typing.overload
    @staticmethod
    def invert(polynomial: cern.accsoft.commons.value.Polynomial, double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def invert(polynomial: cern.accsoft.commons.value.Polynomial, double: float, double2: float, double3: float) -> float: ...
    @staticmethod
    def neg(polynomial: cern.accsoft.commons.value.Polynomial) -> cern.accsoft.commons.value.Polynomial: ...
    @staticmethod
    def scale(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> cern.accsoft.commons.value.Polynomial: ...
    @staticmethod
    def scaleArg(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> cern.accsoft.commons.value.Polynomial: ...
    @staticmethod
    def shift(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> cern.accsoft.commons.value.Polynomial: ...
    @staticmethod
    def shiftArg(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> cern.accsoft.commons.value.Polynomial: ...
    @staticmethod
    def taylorsExpansion(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> typing.List[float]: ...

class BinaryOperation(Operation):
    """
    Java class 'cern.accsoft.commons.value.operation.BinaryOperation'
    
        Interfaces:
            cern.accsoft.commons.value.operation.Operation
    
      Attributes:
        NOT_SAME_LENGTH_MSG (java.lang.String): final static field
    
    """
    NOT_SAME_LENGTH_MSG: typing.ClassVar[str] = ...
    @typing.overload
    def execute(self, discreteFunction: cern.accsoft.commons.value.DiscreteFunction, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, discreteFunctionsArray: cern.accsoft.commons.value.DiscreteFunctionsArray, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalar: cern.accsoft.commons.value.Scalar, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    def isSymmetric(self) -> bool: ...

class MultiOperation(Operation):
    """
    Java class 'cern.accsoft.commons.value.operation.MultiOperation'
    
        Interfaces:
            cern.accsoft.commons.value.operation.Operation
    
    """
    _execute__T = typing.TypeVar('_execute__T', bound=cern.accsoft.commons.value.Value)  # <T>
    def execute(self, valueMap: cern.accsoft.commons.value.expression.ValueMap, list: java.util.List[_execute__T]) -> _execute__T: ...

class TypeReducingOperation(Operation):
    """
    Java class 'cern.accsoft.commons.value.operation.TypeReducingOperation'
    
        Interfaces:
            cern.accsoft.commons.value.operation.Operation
    
    """
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray) -> cern.accsoft.commons.value.Scalar: ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D) -> cern.accsoft.commons.value.ScalarArray: ...

class UnaryOperation(Operation):
    """
    Java class 'cern.accsoft.commons.value.operation.UnaryOperation'
    
        Interfaces:
            cern.accsoft.commons.value.operation.Operation
    
    """
    @typing.overload
    def execute(self, discreteFunction: cern.accsoft.commons.value.DiscreteFunction) -> None: ...
    @typing.overload
    def execute(self, discreteFunctionsArray: cern.accsoft.commons.value.DiscreteFunctionsArray) -> None: ...
    @typing.overload
    def execute(self, scalar: cern.accsoft.commons.value.Scalar) -> None: ...
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray) -> None: ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D) -> None: ...

class AbstractBinaryOperation(BinaryOperation):
    """
    Java class 'cern.accsoft.commons.value.operation.AbstractBinaryOperation'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.operation.BinaryOperation
    
      Constructors:
        * AbstractBinaryOperation()
    
    """
    def __init__(self): ...
    @typing.overload
    def execute(self, discreteFunction: cern.accsoft.commons.value.DiscreteFunction, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, discreteFunctionsArray: cern.accsoft.commons.value.DiscreteFunctionsArray, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalar: cern.accsoft.commons.value.Scalar, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    def getType(self) -> OperationType: ...
    def isSymmetric(self) -> bool: ...

class FunctionBasedOperation(MultiOperation):
    """
    Java class 'cern.accsoft.commons.value.operation.FunctionBasedOperation'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.operation.MultiOperation
    
      Constructors:
        * FunctionBasedOperation(cern.accsoft.commons.value.ContinuousFunction)
    
    """
    def __init__(self, continuousFunction: cern.accsoft.commons.value.ContinuousFunction): ...
    _execute__T = typing.TypeVar('_execute__T', bound=cern.accsoft.commons.value.Value)  # <T>
    def execute(self, valueMap: cern.accsoft.commons.value.expression.ValueMap, list: java.util.List[_execute__T]) -> _execute__T: ...
    def getType(self) -> OperationType: ...
    def toString(self) -> str: ...

class MathFunctionOperation(UnaryOperation):
    """
    Java class 'cern.accsoft.commons.value.operation.MathFunctionOperation'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.operation.UnaryOperation
    
      Constructors:
        * MathFunctionOperation(cern.accsoft.commons.value.MathFunction)
    
    """
    def __init__(self, mathFunction: cern.accsoft.commons.value.MathFunction): ...
    @typing.overload
    def execute(self, discreteFunction: cern.accsoft.commons.value.DiscreteFunction) -> None: ...
    @typing.overload
    def execute(self, discreteFunctionsArray: cern.accsoft.commons.value.DiscreteFunctionsArray) -> None: ...
    @typing.overload
    def execute(self, scalar: cern.accsoft.commons.value.Scalar) -> None: ...
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray) -> None: ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D) -> None: ...
    def getType(self) -> OperationType: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.value.operation")``.

    AbstractBinaryOperation: typing.Type[AbstractBinaryOperation]
    BinaryOperation: typing.Type[BinaryOperation]
    BoundedPolynomialOperations: typing.Type[BoundedPolynomialOperations]
    BoundedPolynomialSequenceBinaryOperations: typing.Type[BoundedPolynomialSequenceBinaryOperations]
    BoundedPolynomialSequenceOperations: typing.Type[BoundedPolynomialSequenceOperations]
    FunctionBasedOperation: typing.Type[FunctionBasedOperation]
    MathFunctionOperation: typing.Type[MathFunctionOperation]
    MultiOperation: typing.Type[MultiOperation]
    Operation: typing.Type[Operation]
    OperationException: typing.Type[OperationException]
    OperationType: typing.Type[OperationType]
    PolynomialBinaryOperations: typing.Type[PolynomialBinaryOperations]
    PolynomialOperations: typing.Type[PolynomialOperations]
    TypeReducingOperation: typing.Type[TypeReducingOperation]
    UnaryOperation: typing.Type[UnaryOperation]
    factory: cern.accsoft.commons.value.operation.factory.__module_protocol__
