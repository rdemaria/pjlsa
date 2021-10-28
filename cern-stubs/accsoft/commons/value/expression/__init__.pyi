import cern.accsoft.commons.value
import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.operation.factory
import java.lang
import java.util
import typing



class Expression:
    """
    Java class 'cern.accsoft.commons.value.expression.Expression'
    
    """
    def evaluate(self, valueMap: 'ValueMap') -> cern.accsoft.commons.value.Value: ...
    def getVariableNames(self) -> java.util.List[str]: ...

class ExpressionParser:
    """
    Java class 'cern.accsoft.commons.value.expression.ExpressionParser'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * ExpressionParser(java.lang.String)
        * ExpressionParser(java.lang.String, cern.accsoft.commons.value.operation.factory.OperationFactory)
    
      Attributes:
        ADDITION_OPERATOR (char): final static field
        SUBTRACTION_OPERATOR (char): final static field
        MULTIPLICATION_OPERATOR (char): final static field
        DIVISION_OPERATOR (char): final static field
        EXPONENTIATION_OPERATOR (char): final static field
        UNARY_NEGATION_OPERATOR (char): final static field
    
    """
    ADDITION_OPERATOR: typing.ClassVar[str] = ...
    SUBTRACTION_OPERATOR: typing.ClassVar[str] = ...
    MULTIPLICATION_OPERATOR: typing.ClassVar[str] = ...
    DIVISION_OPERATOR: typing.ClassVar[str] = ...
    EXPONENTIATION_OPERATOR: typing.ClassVar[str] = ...
    UNARY_NEGATION_OPERATOR: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, operationFactory: cern.accsoft.commons.value.operation.factory.OperationFactory): ...
    @typing.overload
    def parse(self) -> Expression: ...
    @typing.overload
    @staticmethod
    def parse(string: str) -> Expression: ...

class ExpressionSyntaxException(java.lang.Exception):
    """
    Java class 'cern.accsoft.commons.value.expression.ExpressionSyntaxException'
    
        Extends:
            java.lang.Exception
    
      Constructors:
        * ExpressionSyntaxException(java.lang.String)
        * ExpressionSyntaxException(java.lang.String, java.lang.Throwable)
        * ExpressionSyntaxException(java.lang.Throwable)
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class ValueMap:
    """
    Java class 'cern.accsoft.commons.value.expression.ValueMap'
    
    """
    @typing.overload
    def get(self, string: str) -> cern.accsoft.commons.value.ImmutableValue: ...
    @typing.overload
    def get(self, string: str, int: int) -> cern.accsoft.commons.value.ImmutableValue: ...

class BinaryOperationExpression(Expression):
    """
    Java class 'cern.accsoft.commons.value.expression.BinaryOperationExpression'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.expression.Expression
    
      Constructors:
        * BinaryOperationExpression(cern.accsoft.commons.value.operation.BinaryOperation, cern.accsoft.commons.value.expression.Expression, cern.accsoft.commons.value.expression.Expression)
    
    """
    def __init__(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, expression: Expression, expression2: Expression): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value: ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str: ...

class BooleanConstantExpression(Expression):
    """
    Java class 'cern.accsoft.commons.value.expression.BooleanConstantExpression'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.expression.Expression
    
      Constructors:
        * BooleanConstantExpression(java.lang.String)
        * BooleanConstantExpression(boolean)
    
    """
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value: ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str: ...

class ConstantExpression(Expression):
    """
    Java class 'cern.accsoft.commons.value.expression.ConstantExpression'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.expression.Expression
    
      Constructors:
        * ConstantExpression(double)
    
    """
    def __init__(self, double: float): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value: ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str: ...

class FunctionBasedOperationExpression(Expression):
    """
    Java class 'cern.accsoft.commons.value.expression.FunctionBasedOperationExpression'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.expression.Expression
    
      Constructors:
        * FunctionBasedOperationExpression(cern.accsoft.commons.value.operation.MultiOperation, java.util.List)
    
    """
    def __init__(self, multiOperation: cern.accsoft.commons.value.operation.MultiOperation, list: java.util.List[Expression]): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value: ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str: ...

class UnaryOperationExpression(Expression):
    """
    Java class 'cern.accsoft.commons.value.expression.UnaryOperationExpression'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.expression.Expression
    
      Constructors:
        * UnaryOperationExpression(cern.accsoft.commons.value.operation.UnaryOperation, cern.accsoft.commons.value.expression.Expression)
        * UnaryOperationExpression(cern.accsoft.commons.value.MathFunction, cern.accsoft.commons.value.expression.Expression)
    
    """
    @typing.overload
    def __init__(self, mathFunction: cern.accsoft.commons.value.MathFunction, expression: Expression): ...
    @typing.overload
    def __init__(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation, expression: Expression): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value: ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str: ...

class ValueMapAdapter(ValueMap):
    """
    Java class 'cern.accsoft.commons.value.expression.ValueMapAdapter'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.expression.ValueMap
    
      Constructors:
        * ValueMapAdapter()
    
    """
    def __init__(self): ...
    @typing.overload
    def get(self, string: str) -> cern.accsoft.commons.value.ImmutableValue: ...
    @typing.overload
    def get(self, string: str, int: int) -> cern.accsoft.commons.value.ImmutableValue: ...

class VectorExpression(Expression):
    """
    Java class 'cern.accsoft.commons.value.expression.VectorExpression'
    
        Extends:
            java.lang.Object
    
        Interfaces:
            cern.accsoft.commons.value.expression.Expression
    
      Constructors:
        * VectorExpression(java.util.List)
    
    """
    def __init__(self, list: java.util.List[Expression]): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value: ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.value.expression")``.

    BinaryOperationExpression: typing.Type[BinaryOperationExpression]
    BooleanConstantExpression: typing.Type[BooleanConstantExpression]
    ConstantExpression: typing.Type[ConstantExpression]
    Expression: typing.Type[Expression]
    ExpressionParser: typing.Type[ExpressionParser]
    ExpressionSyntaxException: typing.Type[ExpressionSyntaxException]
    FunctionBasedOperationExpression: typing.Type[FunctionBasedOperationExpression]
    UnaryOperationExpression: typing.Type[UnaryOperationExpression]
    ValueMap: typing.Type[ValueMap]
    ValueMapAdapter: typing.Type[ValueMapAdapter]
    VectorExpression: typing.Type[VectorExpression]
