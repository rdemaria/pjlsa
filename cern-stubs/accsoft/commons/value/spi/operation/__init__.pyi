import cern.accsoft.commons.value
import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.spi.operation.factory
import typing



class Addition(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.Addition'
    
        Extends:
            cern.accsoft.commons.value.operation.AbstractBinaryOperation
    
      Constructors:
        * Addition()
    
    """
    def __init__(self): ...
    def toString(self) -> str: ...

class Division(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.Division'
    
        Extends:
            cern.accsoft.commons.value.operation.AbstractBinaryOperation
    
      Constructors:
        * Division()
    
    """
    def __init__(self): ...
    def toString(self) -> str: ...

class Exponentiation(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.Exponentiation'
    
        Extends:
            cern.accsoft.commons.value.operation.AbstractBinaryOperation
    
      Constructors:
        * Exponentiation()
    
    """
    def __init__(self): ...
    def toString(self) -> str: ...

class IEEEremainder(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.IEEEremainder'
    
        Extends:
            cern.accsoft.commons.value.operation.AbstractBinaryOperation
    
      Constructors:
        * IEEEremainder()
    
    """
    def __init__(self): ...
    def toString(self) -> str: ...

class Indexing(cern.accsoft.commons.value.operation.TypeReducingOperation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.Indexing'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.operation.TypeReducingOperation
    
      Constructors:
        * Indexing(java.lang.Integer)
    
    """
    def __init__(self, integer: int): ...
    @typing.overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray) -> cern.accsoft.commons.value.Scalar: ...
    @typing.overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D) -> cern.accsoft.commons.value.ScalarArray: ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType: ...
    def toString(self) -> str: ...

class Max(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.Max'
    
        Extends:
            cern.accsoft.commons.value.operation.AbstractBinaryOperation
    
      Constructors:
        * Max()
    
    """
    def __init__(self): ...
    def toString(self) -> str: ...

class Min(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.Min'
    
        Extends:
            cern.accsoft.commons.value.operation.AbstractBinaryOperation
    
      Constructors:
        * Min()
    
    """
    def __init__(self): ...
    def toString(self) -> str: ...

class Multiplication(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.Multiplication'
    
        Extends:
            cern.accsoft.commons.value.operation.AbstractBinaryOperation
    
      Constructors:
        * Multiplication()
    
    """
    def __init__(self): ...
    def isAllowTypeConversion(self) -> bool: ...
    def isSymmetric(self) -> bool: ...
    def toString(self) -> str: ...

class Subtraction(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.Subtraction'
    
        Extends:
            cern.accsoft.commons.value.operation.AbstractBinaryOperation
    
      Constructors:
        * Subtraction()
    
    """
    def __init__(self): ...
    def toString(self) -> str: ...

class UnaryMinus(cern.accsoft.commons.value.operation.UnaryOperation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.UnaryMinus'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.operation.UnaryOperation
    
      Constructors:
        * UnaryMinus()
    
    """
    def __init__(self): ...
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
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType: ...
    def toString(self) -> str: ...

class Power(Exponentiation):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.Power'
    
        Extends:
            cern.accsoft.commons.value.spi.operation.Exponentiation
    
      Constructors:
        * Power()
    
    """
    def __init__(self): ...
    def toString(self) -> str: ...


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
