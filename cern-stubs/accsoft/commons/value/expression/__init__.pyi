import cern.accsoft.commons.value
import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.operation.factory
import java.lang
import java.util
import typing



class Expression:
    """
    public interface Expression
    
        A class implementing this interface is an mathematical Expression that combines Values and that can be evaluated in a
        given context. The given context allow to resolve variable names and to associate them with a Value.
    """
    def evaluate(self, valueMap: 'ValueMap') -> cern.accsoft.commons.value.Value:
        """
            Evaluates this expression in the given context and return the resulting value.
        
            Parameters:
                variableNamesMap (:class:`~cern.accsoft.commons.value.expression.ValueMap`): the context in which the expression should be evaluated
        
            Returns:
                the resulting value
        
            Raises:
                :class:`~cern.accsoft.commons.value.operation.OperationException`: if the expression cannot be evaluated
        
        
        """
        ...
    def getVariableNames(self) -> java.util.List[str]: ...

class ExpressionParser:
    """
    public class ExpressionParser extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This class implements a simple recursive-descent parser for the expression grammar defined below. This class has been
        designed from Aho and Ullman's compiler design text book.
    
        This grammar is defined with some nonterminals that allow us to embed the precedence relationship of operators into the
        grammar. The grammar is defined as follows:
    
        .. code-block: java
        
          ELEMENT ::= id 
                   | scalars 
                   | "(" EXPRESSION ")" 
                   | function "("EXPRESSION ")"  
                   | function "("EXPRESSION "," EXPRESSION ")" 
          PRIMARY ::= "-" ELEMENT 
                   | ELEMENT 
          FACTOR  ::= PRIMARY "&circ;" FACTOR 
                   | PRIMARY 
          TERM    ::= TERM "*" FACTOR 
                   | TERM "/" FACTOR | FACTOR 
          SUM     ::= SUM "+" TERM 
                   | SUM "-" TERM 
                   | TERM EXPRESSION ::= SUM
          
           Precidence rules from lowest to highest : 1. +, - 2. *, / 3. ˆ 4. unary -
    """
    ADDITION_OPERATOR: typing.ClassVar[str] = ...
    """
    public static final char ADDITION_OPERATOR
    
        Addition '+'
    
        Also see:
            :meth:`~constant`
    
    
    """
    SUBTRACTION_OPERATOR: typing.ClassVar[str] = ...
    """
    public static final char SUBTRACTION_OPERATOR
    
        Subtraction '-'
    
        Also see:
            :meth:`~constant`
    
    
    """
    MULTIPLICATION_OPERATOR: typing.ClassVar[str] = ...
    """
    public static final char MULTIPLICATION_OPERATOR
    
        Multiplication '*'
    
        Also see:
            :meth:`~constant`
    
    
    """
    DIVISION_OPERATOR: typing.ClassVar[str] = ...
    """
    public static final char DIVISION_OPERATOR
    
        Division '/'
    
        Also see:
            :meth:`~constant`
    
    
    """
    EXPONENTIATION_OPERATOR: typing.ClassVar[str] = ...
    """
    public static final char EXPONENTIATION_OPERATOR
    
        Exponentiation '^'
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNARY_NEGATION_OPERATOR: typing.ClassVar[str] = ...
    """
    public static final char UNARY_NEGATION_OPERATOR
    
        Unary minus '-'
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, operationFactory: cern.accsoft.commons.value.operation.factory.OperationFactory): ...
    @typing.overload
    def parse(self) -> Expression: ...
    @typing.overload
    @staticmethod
    def parse(string: str) -> Expression:
        """
            Parses the mathematical expression given by the parameter and returns a tree of Expressions that represents it. The
            expression returned can be evaluated in a given context.
        
            Parameters:
                expression (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the String representing the expression to evaluate
        
            Returns:
                the tree of expression representing the parsed expression or null if the expression cannot be evaluated
        
        public :class:`~cern.accsoft.commons.value.expression.Expression` parse() throws :class:`~cern.accsoft.commons.value.expression.ExpressionSyntaxException`
        
            Parses the mathematical expression of this ExpressionParser and returns a tree of Expressions that represents the
            original expression. The expression returned can be evaluated in a given context.
        
            Returns:
                the tree of expression representing the parsed expression
        
            Raises:
                :class:`~cern.accsoft.commons.value.expression.ExpressionSyntaxException`: if the expression cannot be parsed
        
        
        """
        ...

class ExpressionSyntaxException(java.lang.Exception):
    """
    public class ExpressionSyntaxException extends `Exception <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Exception.html?is-external=true>`
    
        When an error occurs while parsing the expression we throw a SyntaxError.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...

class ValueMap:
    """
    public interface ValueMap
    
        A simple Map a named values
    """
    @typing.overload
    def get(self, string: str) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Returns the value of name :code:`valueName`
        
            Parameters:
                valueName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value of matching name or null if a value of that name does not exist.
        
        """
        ...
    @typing.overload
    def get(self, string: str, int: int) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Returns the value of name :code:`valueName`
        
            Parameters:
                valueName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index of the value
        
            Returns:
                the value of matching name and index or null if a value of that name does not exist.
        
        
        """
        ...

class BinaryOperationExpression(Expression):
    """
    public class BinaryOperationExpression extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.expression.Expression`
    
        This class implements the composition of two expressions with a BinaryOperation
    """
    def __init__(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, expression: Expression, expression2: Expression): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`
            Evaluates this expression in the given context and return the resulting value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.expression.Expression`
        
            Parameters:
                variableNamesMap (:class:`~cern.accsoft.commons.value.expression.ValueMap`): the context in which the expression should be evaluated
        
            Returns:
                the resulting value
        
        
        """
        ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class BooleanConstantExpression(Expression):
    """
    public class BooleanConstantExpression extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.expression.Expression`
    """
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def __init__(self, string: str): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`
            Evaluates this expression in the given context and return the resulting value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.expression.Expression`
        
            Parameters:
                variableNamesMap (:class:`~cern.accsoft.commons.value.expression.ValueMap`): the context in which the expression should be evaluated
        
            Returns:
                the resulting value
        
        
        """
        ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ConstantExpression(Expression):
    """
    public class ConstantExpression extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.expression.Expression`
    
        This class is an Expression that represents a simple constant value
    """
    def __init__(self, double: float): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`
            Evaluates this expression in the given context and return the resulting value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.expression.Expression`
        
            Parameters:
                variableNamesMap (:class:`~cern.accsoft.commons.value.expression.ValueMap`): the context in which the expression should be evaluated
        
            Returns:
                the resulting value
        
        
        """
        ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class FunctionBasedOperationExpression(Expression):
    """
    public class FunctionBasedOperationExpression extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.expression.Expression`
    
        expression to hold a function of many arguments
    """
    def __init__(self, multiOperation: cern.accsoft.commons.value.operation.MultiOperation, list: java.util.List[Expression]): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`
            Evaluates this expression in the given context and return the resulting value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.expression.Expression`
        
            Parameters:
                variableNamesMap (:class:`~cern.accsoft.commons.value.expression.ValueMap`): the context in which the expression should be evaluated
        
            Returns:
                the resulting value
        
        
        """
        ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class UnaryOperationExpression(Expression):
    """
    public class UnaryOperationExpression extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.expression.Expression`
    
        This class implements the application of an UnaryOperation on an expression
    """
    @typing.overload
    def __init__(self, mathFunction: cern.accsoft.commons.value.MathFunction, expression: Expression): ...
    @typing.overload
    def __init__(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation, expression: Expression): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`
            Evaluates this expression in the given context and return the resulting value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.expression.Expression`
        
            Parameters:
                variableNamesMap (:class:`~cern.accsoft.commons.value.expression.ValueMap`): the context in which the expression should be evaluated
        
            Returns:
                the resulting value
        
        
        """
        ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ValueMapAdapter(ValueMap):
    """
    public class ValueMapAdapter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.expression.ValueMap`
    
        The method get for name and index is delegated to get for name. get for name returns null.
    """
    def __init__(self): ...
    @typing.overload
    def get(self, string: str) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.expression.ValueMap.get`
            Returns the value of name :code:`valueName`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.expression.ValueMap.get`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.expression.ValueMap`
        
            Parameters:
                valueName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value of matching name or null if a value of that name does not exist.
        
        """
        ...
    @typing.overload
    def get(self, string: str, int: int) -> cern.accsoft.commons.value.ImmutableValue:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.expression.ValueMap.get`
            Returns the value of name :code:`valueName`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.expression.ValueMap.get`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.expression.ValueMap`
        
            Parameters:
                valueName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index of the value
        
            Returns:
                the value of matching name and index or null if a value of that name does not exist.
        
        
        """
        ...

class VectorExpression(Expression):
    """
    public class VectorExpression extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.expression.Expression`
    
        a dedicated expression to represent vectors. use it with the following notation: {expr1, expr2, ... , exprN}
    """
    def __init__(self, list: java.util.List[Expression]): ...
    def evaluate(self, valueMap: ValueMap) -> cern.accsoft.commons.value.Value:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`
            Evaluates this expression in the given context and return the resulting value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.expression.Expression.evaluate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.expression.Expression`
        
            Parameters:
                variableNamesMap (:class:`~cern.accsoft.commons.value.expression.ValueMap`): the context in which the expression should be evaluated
        
            Returns:
                the resulting value
        
        
        """
        ...
    def getVariableNames(self) -> java.util.List[str]: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...


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
