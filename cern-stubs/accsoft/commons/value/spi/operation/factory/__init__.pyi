import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.operation.factory
import typing



class BinaryOperationProvider(cern.accsoft.commons.value.operation.factory.AbstractOperationProvider[cern.accsoft.commons.value.operation.BinaryOperation]):
    """
    public class BinaryOperationProvider extends :class:`~cern.accsoft.commons.value.operation.factory.AbstractOperationProvider`<:class:`~cern.accsoft.commons.value.operation.BinaryOperation`>
    """
    MAX: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MAX
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    MIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` MIN
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    IEEEREMAINDER: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` IEEEREMAINDER
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    POW: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` POW
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.factory.OperationProvider.getType`
            method to specify which type of operation is provided
        
            Returns:
        
        
        """
        ...

class CoreOperationProvider(cern.accsoft.commons.value.operation.factory.AbstractOperationProvider[cern.accsoft.commons.value.operation.BinaryOperation]):
    """
    public class CoreOperationProvider extends :class:`~cern.accsoft.commons.value.operation.factory.AbstractOperationProvider`<:class:`~cern.accsoft.commons.value.operation.BinaryOperation`>
    
        provides core operations for the parser
    """
    def __init__(self): ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.factory.OperationProvider.getType`
            method to specify which type of operation is provided
        
            Returns:
        
        
        """
        ...

class MathFunctionOperationProvider(cern.accsoft.commons.value.operation.factory.AbstractOperationProvider[cern.accsoft.commons.value.operation.MathFunctionOperation]):
    """
    public class MathFunctionOperationProvider extends :class:`~cern.accsoft.commons.value.operation.factory.AbstractOperationProvider`<:class:`~cern.accsoft.commons.value.operation.MathFunctionOperation`>
    
        Basic operation provider for Math functions.
    """
    ABS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ABS
    
        perform the absolute value of a double value
    
        Also see:
            :meth:`~constant`
    
    
    """
    ACOS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ACOS
    
        perform the arc cosine of an angle, in the range of 0.0 through pi
    
        Also see:
            :meth:`~constant`
    
    
    """
    ASIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ASIN
    
        perform the arc sine of an angle, in the range of -pi/2 through pi/2
    
        Also see:
            :meth:`~constant`
    
    
    """
    ATAN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ATAN
    
        perform the arc tangent of an angle, in the range of -pi/2 through pi/2
    
        Also see:
            :meth:`~constant`
    
    
    """
    CEIL: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` CEIL
    
        perform the smallest (closest to negative infinity) double value that is not less than the argument and is equal to a
        mathematical integer
    
        Also see:
            :meth:`~constant`
    
    
    """
    COS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` COS
    
        perform the trigonometric cosine of an angle
    
        Also see:
            :meth:`~constant`
    
    
    """
    EXP: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` EXP
    
        Returns Euler's number e raised to the power of a double value.
    
        Also see:
            :meth:`~constant`
    
    
    """
    FLOOR: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` FLOOR
    
        the largest (closest to positive infinity) double value that is not greater than the argument and is equal to a
        mathematical integer
    
        Also see:
            :meth:`~constant`
    
    
    """
    LOG: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` LOG
    
        perform the natural logarithm (base e) of a double value
    
        Also see:
            :meth:`~constant`
    
    
    """
    LOG10: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` LOG10
    
        perform the logarithm (base 10) of a double value
    
        Also see:
            :meth:`~constant`
    
    
    """
    POW2: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` POW2
    
        compute the first argument raised to the power of 2
    
        Also see:
            :meth:`~constant`
    
    
    """
    RINT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` RINT
    
        compute the double value that is closest in value to the argument and is equal to mathematical integer
    
        Also see:
            :meth:`~constant`
    
    
    """
    ROUND: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` ROUND
    
        compute the closest long to the argument
    
        Also see:
            :meth:`~constant`
    
    
    """
    SIN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SIN
    
        perform the correctly rounded positive square root of a double value
    
        Also see:
            :meth:`~constant`
    
    
    """
    SQRT: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` SQRT
    
        perform the correctly rounded positive square root of a double value
    
        Also see:
            :meth:`~constant`
    
    
    """
    TAN: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TAN
    
        compute the trigonometric tangent of an angle
    
        Also see:
            :meth:`~constant`
    
    
    """
    TODEGREES: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TODEGREES
    
        Converts an angle measured in radians to an approximately equivalent angle measured in degrees.
    
        Also see:
            :meth:`~constant`
    
    
    """
    TORADIANS: typing.ClassVar[str] = ...
    """
    public static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` TORADIANS
    
        Converts an angle measured in degrees to an approximately equivalent angle measured in radians.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.factory.OperationProvider.getType`
            method to specify which type of operation is provided
        
            Returns:
        
        
        """
        ...

class UnaryOperationProvider(cern.accsoft.commons.value.operation.factory.AbstractOperationProvider[cern.accsoft.commons.value.operation.UnaryOperation]):
    """
    public class UnaryOperationProvider extends :class:`~cern.accsoft.commons.value.operation.factory.AbstractOperationProvider`<:class:`~cern.accsoft.commons.value.operation.UnaryOperation`>
    
        Currently no special unary operations are implemented.
    """
    def __init__(self): ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.operation.factory.OperationProvider.getType`
            method to specify which type of operation is provided
        
            Returns:
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.value.spi.operation.factory")``.

    BinaryOperationProvider: typing.Type[BinaryOperationProvider]
    CoreOperationProvider: typing.Type[CoreOperationProvider]
    MathFunctionOperationProvider: typing.Type[MathFunctionOperationProvider]
    UnaryOperationProvider: typing.Type[UnaryOperationProvider]
