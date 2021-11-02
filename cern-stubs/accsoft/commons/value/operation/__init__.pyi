import cern.accsoft.commons.value
import cern.accsoft.commons.value.expression
import cern.accsoft.commons.value.operation.factory
import java.lang
import java.util
import typing



class BoundedPolynomialOperations:
    """
    public final class BoundedPolynomialOperations extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def differentiate(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial) -> cern.accsoft.commons.value.BoundedPolynomial:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.PolynomialOperations.differentiate`
        
        
        """
        ...
    @staticmethod
    def integrate(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, double: float) -> cern.accsoft.commons.value.BoundedPolynomial:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.PolynomialOperations.integrate`
        
        
        """
        ...
    @staticmethod
    def neg(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial) -> cern.accsoft.commons.value.BoundedPolynomial:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.PolynomialOperations.neg`
        
        
        """
        ...
    @staticmethod
    def scale(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, double: float) -> cern.accsoft.commons.value.BoundedPolynomial:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.PolynomialOperations.scale`
        
        
        """
        ...
    @staticmethod
    def scaleArg(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, double: float) -> cern.accsoft.commons.value.BoundedPolynomial:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.PolynomialOperations.scaleArg`
        
        
        """
        ...
    @staticmethod
    def shift(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, double: float) -> cern.accsoft.commons.value.BoundedPolynomial:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.PolynomialOperations.shift`
        
        
        """
        ...
    @staticmethod
    def shiftArg(boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, double: float) -> cern.accsoft.commons.value.BoundedPolynomial:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.PolynomialOperations.shiftArg`
        
        
        """
        ...

class BoundedPolynomialSequenceBinaryOperations:
    """
    public final class BoundedPolynomialSequenceBinaryOperations extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Binary operations for polynomial sequences. The operations are permitted only if both sequences have equal boundaries.
        Otherwise, an exception is thrown.
    """
    @staticmethod
    def add(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, boundedPolynomialSequence2: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.PolynomialBinaryOperations.add`
        
        
        """
        ...
    @staticmethod
    def concat(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, boundedPolynomialSequence2: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
            Concats two :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`s into one.
        
        
            The upper bound of p1 has to be less or equal to the lower bound of p2.
        
        """
        ...
    @staticmethod
    def multiply(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, boundedPolynomialSequence2: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.PolynomialBinaryOperations.multiply`
        
        
        """
        ...
    @staticmethod
    def subtract(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, boundedPolynomialSequence2: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.PolynomialBinaryOperations.subtract`
        
        
        """
        ...

class BoundedPolynomialSequenceOperations:
    """
    public final class BoundedPolynomialSequenceOperations extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def differentiate(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.BoundedPolynomialOperations.differentiate`
        
        
        """
        ...
    @staticmethod
    def integrate(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, double: float) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.BoundedPolynomialOperations.integrate`
        
        
        """
        ...
    @staticmethod
    def neg(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.BoundedPolynomialOperations.neg`
        
        
        """
        ...
    @staticmethod
    def scale(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, double: float) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.BoundedPolynomialOperations.scale`
        
        
        """
        ...
    @staticmethod
    def scaleArg(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, double: float) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.BoundedPolynomialOperations.scaleArg`
        
        
        """
        ...
    @staticmethod
    def shift(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, double: float) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.BoundedPolynomialOperations.shift`
        
        
        """
        ...
    @staticmethod
    def shiftArg(boundedPolynomialSequence: cern.accsoft.commons.value.BoundedPolynomialSequence, double: float) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Also see:
                :meth:`~cern.accsoft.commons.value.operation.BoundedPolynomialOperations.shiftArg`
        
        
        """
        ...

class Operation:
    """
    public interface Operation
    
        Defines the concept of Operation.
    """
    def getType(self) -> 'OperationType':
        """
        
            Returns:
        
        
        """
        ...

class OperationException(java.lang.RuntimeException):
    """
    public class OperationException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class OperationType(java.lang.Enum['OperationType']):
    """
    public enum OperationType extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.value.operation.OperationType`>
    
        helper enum which defines all the type of supported operations
    """
    BINARY: typing.ClassVar['OperationType'] = ...
    UNARY: typing.ClassVar['OperationType'] = ...
    INDEXING: typing.ClassVar['OperationType'] = ...
    FUNCTION: typing.ClassVar['OperationType'] = ...
    CUSTOM: typing.ClassVar['OperationType'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'OperationType':
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
    def values() -> typing.List['OperationType']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (OperationType c : OperationType.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PolynomialBinaryOperations:
    """
    public final class PolynomialBinaryOperations extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Binary operations on polynomials (i.e. operations of the polynomial ring).
    """
    @staticmethod
    def add(polynomial: cern.accsoft.commons.value.Polynomial, polynomial2: cern.accsoft.commons.value.Polynomial) -> cern.accsoft.commons.value.Polynomial:
        """
            Add two polynomials.
        
        """
        ...
    @staticmethod
    def multiply(polynomial: cern.accsoft.commons.value.Polynomial, polynomial2: cern.accsoft.commons.value.Polynomial) -> cern.accsoft.commons.value.Polynomial:
        """
            Multiply two polynomials.
        
        """
        ...
    @staticmethod
    def subtract(polynomial: cern.accsoft.commons.value.Polynomial, polynomial2: cern.accsoft.commons.value.Polynomial) -> cern.accsoft.commons.value.Polynomial:
        """
            Subtract two polynomials.
        
        """
        ...

class PolynomialOperations:
    """
    public final class PolynomialOperations extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def differentiate(polynomial: cern.accsoft.commons.value.Polynomial) -> cern.accsoft.commons.value.Polynomial:
        """
            Return the derivative :class:`~cern.accsoft.commons.value.Polynomial`.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
        
            Returns:
                differentiated polynomial
        
        
        """
        ...
    @staticmethod
    def integrate(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> cern.accsoft.commons.value.Polynomial:
        """
            Return the :class:`~cern.accsoft.commons.value.Polynomial` defining the integral from a given lower bound.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                c (double): the lower bound of integration
        
            Returns:
                integrated polynomial
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def invert(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> float:
        """
            Invert the given :class:`~cern.accsoft.commons.value.Polynomial` numerically using Newton's algorithm.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                y (double): point to calculate the inverse at
        
            Returns:
                a value :code:`x` such that :code:`Math.abs(p.interpolate(x) - y) < 1e-8`
        
            Invert the given :class:`~cern.accsoft.commons.value.Polynomial` numerically using Newton's algorithm.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                x0 (double): start value for Newton's algorithm
                y (double): point to calculate the inverse at
        
            Returns:
                a value :code:`x` such that :code:`Math.abs(p.interpolate(x) - y) < 1e-8`
        
            Invert the given :class:`~cern.accsoft.commons.value.Polynomial` numerically using Newton's algorithm.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                tolerance (double): desired tolerance
                x0 (double): start value for Newton's algorithm
                y (double): point to calculate the inverse at
        
            Returns:
                a value :code:`x` such that :code:`Math.abs(p.interpolate(x) - y) < tolerance`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def invert(polynomial: cern.accsoft.commons.value.Polynomial, double: float, double2: float) -> float: ...
    @typing.overload
    @staticmethod
    def invert(polynomial: cern.accsoft.commons.value.Polynomial, double: float, double2: float, double3: float) -> float: ...
    @staticmethod
    def neg(polynomial: cern.accsoft.commons.value.Polynomial) -> cern.accsoft.commons.value.Polynomial:
        """
            Return the negative :class:`~cern.accsoft.commons.value.Polynomial`.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
        
            Returns:
                polynomial with inverted sign
        
        
        """
        ...
    @staticmethod
    def scale(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> cern.accsoft.commons.value.Polynomial:
        """
            Return a :class:`~cern.accsoft.commons.value.Polynomial` with scaled y value.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                c (double): the magnitude of the scaling
        
            Returns:
                scaled polynomial
        
        
        """
        ...
    @staticmethod
    def scaleArg(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> cern.accsoft.commons.value.Polynomial:
        """
            Return a :class:`~cern.accsoft.commons.value.Polynomial` with scaled argument such that
            :code:`p.scaleArg(c).interpolate(c * x) = p.interpolate(x)`.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                c (double): the magnitude of the scaling
        
            Returns:
                polynomial with rescaled argument
        
        
        """
        ...
    @staticmethod
    def shift(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> cern.accsoft.commons.value.Polynomial:
        """
            Return a :class:`~cern.accsoft.commons.value.Polynomial` with shifted y value.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                c (double): the magnitude of the shift
        
            Returns:
                shifted polynomial
        
        
        """
        ...
    @staticmethod
    def shiftArg(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> cern.accsoft.commons.value.Polynomial:
        """
            Return a :class:`~cern.accsoft.commons.value.Polynomial` with shifted argument such that
            :code:`p.shiftArg(c).interpolate(x + c) = p.interpolate(x)`.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                c (double): the magnitude of the shift
        
            Returns:
                polynomial with shifted argument
        
        
        """
        ...
    @staticmethod
    def taylorsExpansion(polynomial: cern.accsoft.commons.value.Polynomial, double: float) -> typing.List[float]:
        """
            Return the coefficients of Taylor's expansion with respect to the argument.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                c (double): the origin of Taylor's expansion
        
            Returns:
                array of coefficients defining Taylor's expansion
        
        
        """
        ...

class BinaryOperation(Operation):
    """
    public interface BinaryOperation extends :class:`~cern.accsoft.commons.value.operation.Operation`
    
        Defines a binary operation working on values (scalars, scalars array or function). The BinaryOperation is a visitor
        passed on value that call back the execute method is this operation, passing itself as the first argument.
    """
    NOT_SAME_LENGTH_MSG: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` NOT_SAME_LENGTH_MSG
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def execute(self, discreteFunction: cern.accsoft.commons.value.DiscreteFunction, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None:
        """
            Executes the operation on the first operand using the second. The first operand is altered by the operation.
        
            Parameters:
                scalars (:class:`~cern.accsoft.commons.value.Scalar`): the first operand of the operation
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Executes the operation on the first operand using the second. The first operand is altered by the operation.
        
            Parameters:
                scalarsArray (:class:`~cern.accsoft.commons.value.ScalarArray`): the first operand of the operation
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Executes the operation on the first operand using the second. The first operand is altered by the operation.
        
            Parameters:
                scalarsArray2d (:class:`~cern.accsoft.commons.value.ScalarArray2D`): the first operand of the operation
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Executes the operation on the first operand using the second. The first operand is altered by the operation.
        
            Parameters:
                function (:class:`~cern.accsoft.commons.value.DiscreteFunction`): the first operand of the operation
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Executes the operation on the first operand using the second. Internally, the operation is applied to each single
            function. The first operand is altered by the operation.
        
            Parameters:
                functionsArray (:class:`~cern.accsoft.commons.value.DiscreteFunctionsArray`): the first operand of the operation
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
        
        """
        ...
    @typing.overload
    def execute(self, discreteFunctionsArray: cern.accsoft.commons.value.DiscreteFunctionsArray, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalar: cern.accsoft.commons.value.Scalar, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    def isSymmetric(self) -> bool:
        """
            determines if this operation is type symmetric, e.g. the operands might have different types
        
            Returns:
        
        
        """
        ...

class MultiOperation(Operation):
    """
    public interface MultiOperation extends :class:`~cern.accsoft.commons.value.operation.Operation`
    """
    _execute__T = typing.TypeVar('_execute__T', bound=cern.accsoft.commons.value.Value)  # <T>
    def execute(self, valueMap: cern.accsoft.commons.value.expression.ValueMap, list: java.util.List[_execute__T]) -> _execute__T: ...

class TypeReducingOperation(Operation):
    """
    public interface TypeReducingOperation extends :class:`~cern.accsoft.commons.value.operation.Operation`
    
        represents a specialized type of operation when the resulting type is "reduced", e.g. a matrix is reduced to a
        single-column array when indexed
    """
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray) -> cern.accsoft.commons.value.Scalar:
        """
            reduces an array to scalar
        
            Parameters:
                arr (:class:`~cern.accsoft.commons.value.ScalarArray`): 
            Returns:
        
            reduces a matrix to vector
        
            Parameters:
                arr (:class:`~cern.accsoft.commons.value.ScalarArray2D`): 
            Returns:
        
        
        """
        ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D) -> cern.accsoft.commons.value.ScalarArray: ...

class UnaryOperation(Operation):
    """
    public interface UnaryOperation extends :class:`~cern.accsoft.commons.value.operation.Operation`
    
        Defines a unary operation working on functions and scalars
    """
    @typing.overload
    def execute(self, discreteFunction: cern.accsoft.commons.value.DiscreteFunction) -> None:
        """
            Execute this unary operation on the given operande. The operande is altered by the operation.
        
            Parameters:
                function (:class:`~cern.accsoft.commons.value.DiscreteFunction`): the operand of the operation
        
            Execute this unary operation on the given functions array. Internally, the operation is applied to each single function.
        
            Parameters:
                functionsArray (:class:`~cern.accsoft.commons.value.DiscreteFunctionsArray`): the operand of the operation
        
            Performs the operation on the scalars. The scalars is altered by the operation.
        
            Parameters:
                scalars (:class:`~cern.accsoft.commons.value.Scalar`): the operand of the operation
        
            Performs the operation on the ConstantArray. The scalars is altered by the operation.
        
            Parameters:
                scalarsArray (:class:`~cern.accsoft.commons.value.ScalarArray`): the operand of the operation
        
            Performs the operation on the ConstantArray. The scalars is altered by the operation.
        
            Parameters:
                scalarsArray2d (:class:`~cern.accsoft.commons.value.ScalarArray2D`): the operand of the operation
        
        
        """
        ...
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
    public abstract class AbstractBinaryOperation extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.operation.BinaryOperation`
    
        Template that implements the methods needed by BinaryOperation. Subclasses just need to implement few abstract methods
        to implement fully the BinaryOperation interface.
    """
    def __init__(self): ...
    @typing.overload
    def execute(self, discreteFunction: cern.accsoft.commons.value.DiscreteFunction, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.execute`
            Executes the operation on the first operand using the second. The first operand is altered by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.BinaryOperation`
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Scalar`): the first operand of the operation
                immutableValue (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.execute`
            Executes the operation on the first operand using the second. The first operand is altered by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.BinaryOperation`
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.DiscreteFunction`): the first operand of the operation
                immutableValue (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.execute`
            Executes the operation on the first operand using the second. Internally, the operation is applied to each single
            function. The first operand is altered by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.BinaryOperation`
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.DiscreteFunctionsArray`): the first operand of the operation
                immutableValue (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.execute`
            Executes the operation on the first operand using the second. The first operand is altered by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.BinaryOperation`
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ScalarArray`): the first operand of the operation
                immutableValue (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.execute`
            Executes the operation on the first operand using the second. The first operand is altered by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.BinaryOperation`
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ScalarArray2D`): the first operand of the operation
                immutableValue (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
        
        """
        ...
    @typing.overload
    def execute(self, discreteFunctionsArray: cern.accsoft.commons.value.DiscreteFunctionsArray, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalar: cern.accsoft.commons.value.Scalar, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    def getType(self) -> OperationType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.Operation.getType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.Operation`
        
            Returns:
        
        
        """
        ...
    def isSymmetric(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.isSymmetric`
            determines if this operation is type symmetric, e.g. the operands might have different types
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.isSymmetric`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.BinaryOperation`
        
            Returns:
        
        
        """
        ...

class FunctionBasedOperation(MultiOperation):
    """
    public class FunctionBasedOperation extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.operation.MultiOperation`
    
        operation to wrap over an ExpressionBasedFunction
    """
    def __init__(self, continuousFunction: cern.accsoft.commons.value.ContinuousFunction): ...
    _execute__T = typing.TypeVar('_execute__T', bound=cern.accsoft.commons.value.Value)  # <T>
    def execute(self, valueMap: cern.accsoft.commons.value.expression.ValueMap, list: java.util.List[_execute__T]) -> _execute__T: ...
    def getType(self) -> OperationType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.Operation.getType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.Operation`
        
            Returns:
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class MathFunctionOperation(UnaryOperation):
    """
    public class MathFunctionOperation extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.operation.UnaryOperation`
    
        support operation class to wrap math functions
    """
    def __init__(self, mathFunction: cern.accsoft.commons.value.MathFunction): ...
    @typing.overload
    def execute(self, discreteFunction: cern.accsoft.commons.value.DiscreteFunction) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.UnaryOperation.execute`
            Performs the operation on the scalars. The scalars is altered by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.UnaryOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.UnaryOperation`
        
            Parameters:
                c (:class:`~cern.accsoft.commons.value.Scalar`): the operand of the operation
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.UnaryOperation.execute`
            Performs the operation on the ConstantArray. The scalars is altered by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.UnaryOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.UnaryOperation`
        
            Parameters:
                c (:class:`~cern.accsoft.commons.value.ScalarArray`): the operand of the operation
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.UnaryOperation.execute`
            Performs the operation on the ConstantArray. The scalars is altered by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.UnaryOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.UnaryOperation`
        
            Parameters:
                c (:class:`~cern.accsoft.commons.value.ScalarArray2D`): the operand of the operation
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.UnaryOperation.execute`
            Execute this unary operation on the given operande. The operande is altered by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.UnaryOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.UnaryOperation`
        
            Parameters:
                f (:class:`~cern.accsoft.commons.value.DiscreteFunction`): the operand of the operation
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.UnaryOperation.execute`
            Execute this unary operation on the given functions array. Internally, the operation is applied to each single function.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.UnaryOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.UnaryOperation`
        
            Parameters:
                functionsArray (:class:`~cern.accsoft.commons.value.DiscreteFunctionsArray`): the operand of the operation
        
        
        """
        ...
    @typing.overload
    def execute(self, discreteFunctionsArray: cern.accsoft.commons.value.DiscreteFunctionsArray) -> None: ...
    @typing.overload
    def execute(self, scalar: cern.accsoft.commons.value.Scalar) -> None: ...
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray) -> None: ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D) -> None: ...
    def getType(self) -> OperationType:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.Operation.getType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.Operation`
        
            Returns:
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...


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
