from typing import overload
import cern.accsoft.commons.value
import cern.accsoft.commons.value.operation


class Addition(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    def __init__(self): ...
    def toString(self) -> str: ...

class Division(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    def __init__(self): ...
    def toString(self) -> str: ...

class Exponentiation(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    def __init__(self): ...
    def toString(self) -> str: ...

class IEEEremainder(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    def __init__(self): ...
    def toString(self) -> str: ...

class Indexing(cern.accsoft.commons.value.operation.TypeReducingOperation):
    def __init__(self, integer: int): ...
    @overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray) -> cern.accsoft.commons.value.Scalar: ...
    @overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D) -> cern.accsoft.commons.value.ScalarArray: ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType: ...
    def toString(self) -> str: ...

class Max(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    def __init__(self): ...
    def toString(self) -> str: ...

class Min(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    def __init__(self): ...
    def toString(self) -> str: ...

class Multiplication(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    def __init__(self): ...
    def isAllowTypeConversion(self) -> bool: ...
    def isSymmetric(self) -> bool: ...
    def toString(self) -> str: ...

class Subtraction(cern.accsoft.commons.value.operation.AbstractBinaryOperation):
    def __init__(self): ...
    def toString(self) -> str: ...

class UnaryMinus(cern.accsoft.commons.value.operation.UnaryOperation):
    def __init__(self): ...
    @overload
    def execute(self, discreteFunction: cern.accsoft.commons.value.DiscreteFunction) -> None: ...
    @overload
    def execute(self, discreteFunctionsArray: cern.accsoft.commons.value.DiscreteFunctionsArray) -> None: ...
    @overload
    def execute(self, scalar: cern.accsoft.commons.value.Scalar) -> None: ...
    @overload
    def execute(self, scalarArray: cern.accsoft.commons.value.ScalarArray) -> None: ...
    @overload
    def execute(self, scalarArray2D: cern.accsoft.commons.value.ScalarArray2D) -> None: ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType: ...
    def toString(self) -> str: ...

class Power(Exponentiation):
    def __init__(self): ...
    def toString(self) -> str: ...
