import cern.accsoft.commons.value
import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.spi.operation.factory
import typing



class Addition(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    public class Addition extends :class:`~cern.accsoft.commons.value.operation.AbstractBinaryOperation`
    
        Defines the addition operation working on Value or Function
    """
    def __init__(self): ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class Division(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    public class Division extends :class:`~cern.accsoft.commons.value.operation.AbstractBinaryOperation`
    
        Defines the division operation working on Value or Function
    """
    def __init__(self): ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class Exponentiation(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    public class Exponentiation extends :class:`~cern.accsoft.commons.value.operation.AbstractBinaryOperation`
    
        Defines the exponentiation operation working on Value or Function
    """
    def __init__(self): ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class IEEEremainder(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    public class IEEEremainder extends :class:`~cern.accsoft.commons.value.operation.AbstractBinaryOperation`
    
        Defines the minimun operation working on any Value
    """
    def __init__(self): ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class Indexing(cern.accsoft.commons.value.operation.TypeReducingOperation):
    """
    public class Indexing extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.operation.TypeReducingOperation`
    
        Defines the indexing operation on the arrays, e.g. "x[i]". specifying null index would make the operation return the
        scalar length of the underlying array, e.g. evaluating "{3,4}[]" would return "5".
    """
    def __init__(self, integer: int): ...
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray) -> cern.accsoft.commons.value.Scalar:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.TypeReducingOperation.execute`
            reduces an array to scalar
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.TypeReducingOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.TypeReducingOperation`
        
            Returns:
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.TypeReducingOperation.execute`
            reduces a matrix to vector
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.TypeReducingOperation.execute`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.TypeReducingOperation`
        
            Returns:
        
        
        """
        ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D) -> cern.accsoft.commons.value.ScalarArray: ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType:
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

class Max(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    public class Max extends :class:`~cern.accsoft.commons.value.operation.AbstractBinaryOperation`
    
        Defines the maximun operation working on any Value
    """
    def __init__(self): ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class Min(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    public class Min extends :class:`~cern.accsoft.commons.value.operation.AbstractBinaryOperation`
    
        Defines the minimun operation working on any Value
    """
    def __init__(self): ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class Multiplication(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    public class Multiplication extends :class:`~cern.accsoft.commons.value.operation.AbstractBinaryOperation`
    
        Defines the multiplication operation working on Value or Function
    """
    def __init__(self): ...
    def isAllowTypeConversion(self) -> bool: ...
    def isSymmetric(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.isSymmetric`
            determines if this operation is type symmetric, e.g. the operands might have different types
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.operation.BinaryOperation.isSymmetric`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.operation.BinaryOperation`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.operation.AbstractBinaryOperation.isSymmetric`Â in
                classÂ :class:`~cern.accsoft.commons.value.operation.AbstractBinaryOperation`
        
            Returns:
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class Subtraction(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    public class Subtraction extends :class:`~cern.accsoft.commons.value.operation.AbstractBinaryOperation`
    
        Defines the subtraction operation working on Value or Function
    """
    def __init__(self): ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class UnaryMinus(cern.accsoft.commons.value.operation.UnaryOperation):
    """
    public class UnaryMinus extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.operation.UnaryOperation`
    
        Defines the unary minus operation working on Value or Function
    """
    def __init__(self): ...
    @typing.overload
    def execute(self, discreteFunction: cern.accsoft.commons.value.DiscreteFunction) -> None:
        """
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
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType:
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

class Power(Exponentiation):
    """
    public class Power extends :class:`~cern.accsoft.commons.value.spi.operation.Exponentiation`
    
        Defines the exponentiation operation working on Value or Function
    """
    def __init__(self): ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.operation.Exponentiation.toString`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.operation.Exponentiation`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.value.spi.operation")``.

    Addition: typing.Type[Addition]
    Division: typing.Type[Division]
    Exponentiation: typing.Type[Exponentiation]
    IEEEremainder: typing.Type[IEEEremainder]
    Indexing: typing.Type[Indexing]
    Max: typing.Type[Max]
    Min: typing.Type[Min]
    Multiplication: typing.Type[Multiplication]
    Power: typing.Type[Power]
    Subtraction: typing.Type[Subtraction]
    UnaryMinus: typing.Type[UnaryMinus]
    factory: cern.accsoft.commons.value.spi.operation.factory.__module_protocol__
