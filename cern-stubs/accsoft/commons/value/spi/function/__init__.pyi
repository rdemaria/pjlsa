import cern.accsoft.commons.value
import cern.accsoft.commons.value.expression
import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.spi
import cern.japc.value
import java.io
import java.util
import typing



class AbstractMathFunction(cern.accsoft.commons.value.MathFunction):
    """
    public abstract class AbstractMathFunction extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.MathFunction`
    """
    def __init__(self): ...
    def getType(self) -> cern.accsoft.commons.value.Type:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Typed.getType`
            Returns the type of this value
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Typed.getType` in interface :class:`~cern.accsoft.commons.value.Typed`
        
            Returns:
                the type of this value
        
        
        """
        ...
    def interpolate(self, double: float) -> float:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`
            Interpolates a new point at the given x-coordinate. If no point can be interpolated NaN is returned.
        
            Interpolates linearly the point at the x-coordinate x using this discrete function. If this function is defined at that
            x-coordinate, the y-coordinate at this point is returned. Else the linear interpolation is performed with the adjacent
            points.
        
            Note that we consider this function is only defined from x1 to x2 where x1 is the x-coordinate of the first point and x2
            is the x-coordinate of the last point. If x1 <= x <= x2 the interpolation can be performed. If x < x1 or x > x2 the
            interpolation cannot be performed and Double.NaN is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.Interpolable`
        
            Parameters:
                x (double): the x-coordinate of the point to interpolate
        
            Returns:
                the new interpolated y-coordinate or NaN
        
        
        """
        ...
    def isDiscrete(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Function.isDiscrete`
            Returns true is this function is a discrete function defined with a list of points. If false one can assume that this
            function is defined with a mathematical formula and does not hold any particular point.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Function.isDiscrete` in interface :class:`~cern.accsoft.commons.value.Function`
        
            Returns:
                true is this function is a discrete function.
        
        
        """
        ...

class BoundedPolynomialIntervalComparator(java.util.Comparator[cern.accsoft.commons.value.BoundedPolynomial]):
    """
    public final class BoundedPolynomialIntervalComparator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Comparator <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Comparator.html?is-external=true>`<:class:`~cern.accsoft.commons.value.BoundedPolynomial`>
    
        Compares intervals of the given :class:`~cern.accsoft.commons.value.BoundedPolynomial`s.
    
        Also see:
            :meth:`~cern.accsoft.commons.value.Interval.compareByBoundsTo`
    """
    def compare(self, boundedPolynomial: cern.accsoft.commons.value.BoundedPolynomial, boundedPolynomial2: cern.accsoft.commons.value.BoundedPolynomial) -> int:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'BoundedPolynomialIntervalComparator':
        """
        
            Returns:
                the singleton instance of the comparator
        
        
        """
        ...

class BoundedPolynomialSequenceImpl(cern.accsoft.commons.value.spi.AbstractValue, cern.accsoft.commons.value.BoundedPolynomialSequence):
    """
    public class BoundedPolynomialSequenceImpl extends :class:`~cern.accsoft.commons.value.spi.AbstractValue` implements :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, boundedPolynomialArray: typing.List[cern.accsoft.commons.value.BoundedPolynomial]): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[cern.accsoft.commons.value.BoundedPolynomial], typing.Sequence[cern.accsoft.commons.value.BoundedPolynomial]]): ...
    @staticmethod
    def createOfAbsoluteBoundedPolynomials(doubleArray: typing.List[typing.List[float]]) -> cern.accsoft.commons.value.BoundedPolynomialSequence: ...
    @staticmethod
    def createOfRelativeBoundedPolynomials(doubleArray: typing.List[typing.List[float]]) -> cern.accsoft.commons.value.BoundedPolynomialSequence:
        """
        
            Parameters:
                boundedPolynomials (double[][]): a 2d array containing lower bound, upper bound and then the coefficients in increasing order for each
                    :class:`~cern.accsoft.commons.value.BoundedPolynomial`.
        
            Returns:
                a BoundedPolynomialSequence
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.AbstractValue.equals`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.AbstractValue`
        
        
        """
        ...
    @typing.overload
    def execute(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Value.execute`
            Performs the operation on this value with the given value as second operand. This value is changed by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.execute` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.BinaryOperation`): the operation to perform
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand for the binary operation
        
        
        """
        ...
    @typing.overload
    def execute(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Value.execute`
            Performs the given operation on this value. This value is changed by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.execute` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.UnaryOperation`): the operation to perform
        
        """
        ...
    def getBoundedPolynomials(self) -> typing.List[cern.accsoft.commons.value.BoundedPolynomial]:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.BoundedPolynomialSequence.getBoundedPolynomials`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
            Returns:
                all :class:`~cern.accsoft.commons.value.BoundedPolynomial` contained in this
                :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
        
        """
        ...
    def getString(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.getString`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.AbstractValue.hashCode`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.AbstractValue`
        
        
        """
        ...
    def interpolate(self, double: float) -> float:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`
            Interpolates a new point at the given x-coordinate. If no point can be interpolated NaN is returned.
        
            Interpolates linearly the point at the x-coordinate x using this discrete function. If this function is defined at that
            x-coordinate, the y-coordinate at this point is returned. Else the linear interpolation is performed with the adjacent
            points.
        
            Note that we consider this function is only defined from x1 to x2 where x1 is the x-coordinate of the first point and x2
            is the x-coordinate of the last point. If x1 <= x <= x2 the interpolation can be performed. If x < x1 or x > x2 the
            interpolation cannot be performed and Double.NaN is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.BoundedPolynomialSequence.interpolate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.Interpolable`
        
            Parameters:
                x (double): the x-coordinate of the point to interpolate
        
            Returns:
                the interpolated value of the :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence` if one of the
                :class:`~cern.accsoft.commons.value.Interval` of the :class:`~cern.accsoft.commons.value.BoundedPolynomial` contains
                :code:`x` or `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Double.html?is-external=true#NaN>` if
                no :class:`~cern.accsoft.commons.value.Interval` contains :code:`x`.
        
            Also see:
                :meth:`~cern.accsoft.commons.value.BoundedPolynomial.interpolate`,
                :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`
        
        
        """
        ...
    def isDiscrete(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Function.isDiscrete`
            Returns true is this function is a discrete function defined with a list of points. If false one can assume that this
            function is defined with a mathematical formula and does not hold any particular point.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Function.isDiscrete` in interface :class:`~cern.accsoft.commons.value.Function`
        
            Returns:
                true is this function is a discrete function.
        
        
        """
        ...
    def makeMutable(self) -> cern.accsoft.commons.value.Value:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`
            Returns a mutable version of this immutable value. The mutable version is made by performing a deep copy of this value.
            The runtime type of the value is preserved by this operation. The resulting value can be cast in the mutable type
            corresponding to the immutable type of this value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Returns:
                a mutable deep copy of this value
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.AbstractValue.toString`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.AbstractValue`
        
        
        """
        ...

class DiscreteFunctionImpl(cern.accsoft.commons.value.spi.AbstractValue, cern.accsoft.commons.value.DiscreteFunction, java.io.Serializable):
    """
    public abstract class DiscreteFunctionImpl extends :class:`~cern.accsoft.commons.value.spi.AbstractValue` implements :class:`~cern.accsoft.commons.value.DiscreteFunction`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Implement a discrete function defined by a list of Points.
    
        Also see:
            :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.AbstractValue.equals`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.AbstractValue`
        
        
        """
        ...
    @typing.overload
    def execute(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Value.execute`
            Performs the operation on this value with the given value as second operand. This value is changed by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.execute` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.BinaryOperation`): the operation to perform
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand for the binary operation
        
        
        """
        ...
    @typing.overload
    def execute(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Value.execute`
            Performs the given operation on this value. This value is changed by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.execute` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.UnaryOperation`): the operation to perform
        
        """
        ...
    def getBoolean(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalar.getBoolean`
            Returns the value being interpreted as a boolean. If the value is an array only the first value of the array is
            returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.getBoolean`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Returns:
                the value being interpreted as a boolean.
        
        
        """
        ...
    def getByte(self) -> int:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalar.getByte`
            Returns the value being interpreted as a byte. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.getByte`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Returns:
                the value being interpreted as a byte.
        
        
        """
        ...
    def getDouble(self) -> float:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalar.getDouble`
            Returns the value being interpreted as a double. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.getDouble`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Returns:
                the value being interpreted as a double.
        
        
        """
        ...
    def getFloat(self) -> float:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalar.getFloat`
            Returns the value being interpreted as a float. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.getFloat`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Returns:
                the value being interpreted as a float.
        
        
        """
        ...
    def getInt(self) -> int:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalar.getInt`
            Returns the value being interpreted as a int. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.getInt`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Returns:
                the value being interpreted as a int.
        
        
        """
        ...
    def getLength(self) -> float:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableDiscreteFunction.getLength`
            Returns length of this function i.e. difference between last X coordinate and first X coordinate. If the function is
            empty - NaN value is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableDiscreteFunction.getLength`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableDiscreteFunction`
        
        
        """
        ...
    def getLong(self) -> int:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalar.getLong`
            Returns the value being interpreted as a long. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.getLong`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Returns:
                the value being interpreted as a long.
        
        
        """
        ...
    def getObject(self) -> typing.Any:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalar.getObject`
            Returns the value as an object. This method returns the scalar type in their wrapping Object type and arrays and string
            without change.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.getObject`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Returns:
                the value as an object.
        
        
        """
        ...
    def getShort(self) -> int:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalar.getShort`
            Returns the value being interpreted as a short. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.getShort`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Returns:
                the value being interpreted as a short.
        
        
        """
        ...
    def getString(self) -> str:
        """
            Returns string representation of this function in the following format: [x1 y1, x2 y2, x3 y3, ...]. Only first 10 points
            of the function are displayed. If the function has more points than that - the string contains only first 10 elements
            and information about number of remaining points (that are not included in the string).
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.getString`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Returns:
                string representation of this discrete function
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.AbstractValue.hashCode`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.AbstractValue`
        
        
        """
        ...
    def interpolate(self, double: float) -> float:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`
            Interpolates a new point at the given x-coordinate. If no point can be interpolated NaN is returned.
        
            Interpolates linearly the point at the x-coordinate x using this discrete function. If this function is defined at that
            x-coordinate, the y-coordinate at this point is returned. Else the linear interpolation is performed with the adjacent
            points.
        
            Note that we consider this function is only defined from x1 to x2 where x1 is the x-coordinate of the first point and x2
            is the x-coordinate of the last point. If x1 <= x <= x2 the interpolation can be performed. If x < x1 or x > x2 the
            interpolation cannot be performed and Double.NaN is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.Interpolable`
        
            Parameters:
                x (double): the x-coordinate of the point to interpolate
        
            Returns:
                the new interpolated y-coordinate or NaN
        
        
        """
        ...
    def isDiscrete(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Function.isDiscrete`
            Returns true is this function is a discrete function defined with a list of points. If false one can assume that this
            function is defined with a mathematical formula and does not hold any particular point.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Function.isDiscrete` in interface :class:`~cern.accsoft.commons.value.Function`
        
            Returns:
                true is this function is a discrete function.
        
        
        """
        ...
    def setBoolean(self, boolean: bool) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Scalar.setBoolean`
            Sets the value being a boolean. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Scalar.setBoolean` in interface :class:`~cern.accsoft.commons.value.Scalar`
        
            Parameters:
                value (boolean): the boolean value.
        
        
        """
        ...
    def setByte(self, byte: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Scalar.setByte`
            Sets the value being a byte. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Scalar.setByte` in interface :class:`~cern.accsoft.commons.value.Scalar`
        
            Parameters:
                value (byte): the byte value.
        
        
        """
        ...
    def setDouble(self, double: float) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Scalar.setDouble`
            Sets the value being a double. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Scalar.setDouble` in interface :class:`~cern.accsoft.commons.value.Scalar`
        
            Parameters:
                value (double): the double value.
        
        
        """
        ...
    def setFloat(self, float: float) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Scalar.setFloat`
            Sets the value being a float. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Scalar.setFloat` in interface :class:`~cern.accsoft.commons.value.Scalar`
        
            Parameters:
                value (float): the float value.
        
        
        """
        ...
    def setInt(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Scalar.setInt`
            Sets the value being a int. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Scalar.setInt` in interface :class:`~cern.accsoft.commons.value.Scalar`
        
            Parameters:
                value (int): the int value.
        
        
        """
        ...
    def setLong(self, long: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Scalar.setLong`
            Sets the value being a long. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Scalar.setLong` in interface :class:`~cern.accsoft.commons.value.Scalar`
        
            Parameters:
                value (long): the long value.
        
        
        """
        ...
    def setObject(self, object: typing.Any) -> None:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Scalar.setObject` in interface :class:`~cern.accsoft.commons.value.Scalar`
        
        
        """
        ...
    def setShort(self, short: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Scalar.setShort`
            Sets the value being a short. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Scalar.setShort` in interface :class:`~cern.accsoft.commons.value.Scalar`
        
            Parameters:
                value (short): the short value.
        
        
        """
        ...
    def setString(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Scalar.setString`
            Sets the value being a String. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Scalar.setString` in interface :class:`~cern.accsoft.commons.value.Scalar`
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the String value.
        
        
        """
        ...
    def toScalarArray2D(self) -> cern.accsoft.commons.value.ScalarArray2D:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableDiscreteFunction.toScalarArray2D`
            Converts the function into a 2D array. The array consists of 2 rows First row are x-coordinates and second row are
            y-coordinates. Number of columns correspons to number of points in the function.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableDiscreteFunction.toScalarArray2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableDiscreteFunction`
        
            Returns:
                2D array
        
        
        """
        ...
    def toSimpleParameterValue(self) -> cern.japc.value.SimpleParameterValue:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalar.toSimpleParameterValue`
            Converts this scalar into a JAPC SimpleParameterValue.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.toSimpleParameterValue`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Returns:
                JAPC simple parameter value
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.AbstractValue.toString`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.AbstractValue`
        
        
        """
        ...

class DiscreteFunctionsArrayImpl(cern.accsoft.commons.value.spi.AbstractValue, cern.accsoft.commons.value.DiscreteFunctionsArray, java.io.Serializable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, immutableDiscreteFunctionArray: typing.List[cern.accsoft.commons.value.ImmutableDiscreteFunction]): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def execute(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation) -> None: ...
    def getFunction(self, int: int) -> cern.accsoft.commons.value.DiscreteFunction: ...
    def getFunctions(self) -> typing.List[cern.accsoft.commons.value.DiscreteFunction]: ...
    def getFunctionsCount(self) -> int: ...
    def getString(self) -> str: ...
    def getYs(self, double: float) -> typing.List[float]: ...
    def hashCode(self) -> int: ...
    @typing.overload
    def insert(self, double: float) -> bool: ...
    @typing.overload
    def insert(self, int: int, double: float) -> bool: ...
    @typing.overload
    def insert(self, int: int, double: float, double2: float) -> bool: ...
    @typing.overload
    def insertAll(self, doubleArray: typing.List[float]) -> int: ...
    @typing.overload
    def insertAll(self, int: int, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, double: float) -> int: ...
    @typing.overload
    def insertAll(self, int: int, doubleArray: typing.List[float]) -> int: ...
    def makeMutable(self) -> cern.accsoft.commons.value.DiscreteFunctionsArray: ...
    @typing.overload
    def remove(self, double: float) -> bool: ...
    @typing.overload
    def remove(self, int: int, double: float) -> bool: ...
    @typing.overload
    def removeAll(self, doubleArray: typing.List[float]) -> int: ...
    @typing.overload
    def removeAll(self, int: int, doubleArray: typing.List[float]) -> int: ...
    def retainAll(self, int: int, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, double: float) -> int: ...
    def setY(self, int: int, int2: int, double: float) -> None: ...
    @typing.overload
    def subView(self, int: int, double: float, double2: float) -> cern.accsoft.commons.value.DiscreteFunction: ...
    @typing.overload
    def subView(self, double: float, double2: float) -> cern.accsoft.commons.value.DiscreteFunctionsArray: ...
    def toXArray(self) -> typing.List[float]: ...
    @typing.overload
    def translate(self, double: float) -> None: ...
    @typing.overload
    def translate(self, int: int, double: float) -> None: ...

class Discretizer:
    """
    public final class Discretizer extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class with static methods for converting continuous functions of type
        :class:`~cern.accsoft.commons.value.Interpolable` into 2D arrays or values of type DiscreteFunction.
    """
    @typing.overload
    @staticmethod
    def createArray(int: int, double: float, double2: float) -> typing.List[float]:
        """
            Return an array of length :code:`nIntervals+1` defining the boundaries of :code:`nIntervals` intervals of length
            :code:`dx`, starting and ending at values :code:`xStart` and :code:`xEnd`, respectively. The boundaries are rounded with
            a precision of :code:`precision` decimal places using :meth:`~cern.accsoft.commons.value.Values.round`. At least one of
            :code:`dx` or :code:`nIntervals` must be specified. If both are given, they are left unchanged. :code:`dx` is always
            converted into a positive quantity internally by taking its absolute value.
        
            Parameters:
                dx (`Double <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Double.html?is-external=true>`): length of interval. If :code:`null`, calculate from :code:`nIntervals`.
                nIntervals (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): number of intervals. If :code:`null`, calculate from :code:`dx`.
                xStart (double): value of first boundary
                xEnd (double): value of last boundary
                precision (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): number of decimal places for rounding x values. If :code:`null`, don't round.
        
            Returns:
                array of interval boundaries
        
            Convenience function: Return an array of length :code:`nIntervals+1` defining the boundaries of :code:`nIntervals`,
            starting and ending at values :code:`xStart` and :code:`xEnd`, respectively.
        
            Parameters:
                nIntervals (int): number of intervals
                xStart (double): value of first boundary
                xEnd (double): value of last boundary
        
            Returns:
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createArray(double: float, integer: int, double2: float, double3: float, integer2: int) -> typing.List[float]: ...
    @typing.overload
    @staticmethod
    def createDiscreteFunction(interpolable: cern.accsoft.commons.value.Interpolable, double: float, int2: int, double2: float, double3: float) -> cern.accsoft.commons.value.DiscreteFunction:
        """
            Return a DiscreteFunction defined over :code:`nIntervals+1` points by evaluating the given function :code:`f` at the
            boundaries of :code:`nIntervals` intervals of length :code:`dx`, starting end ending at values :code:`xStart` and
            :code:`xEnd`, respectively.
        
            Parameters:
                f (:class:`~cern.accsoft.commons.value.Interpolable`): function to convert
                dx (double): length of interval
                nIntervals (int): number of intervals
                xStart (double): value of first boundary
                xEnd (double): value of last boundary
        
            Returns:
                DiscreteFunction
        
            Return a DiscreteFunction defined over :code:`nIntervals+1` points by evaluating the given function :code:`f` at the
            boundaries of :code:`nIntervals` intervals of length :code:`dx`, starting end ending at values :code:`xStart` and
            :code:`xEnd`, respectively. The x coordinates are rounded with a precision of :code:`precision` decimal places using
            :meth:`~cern.accsoft.commons.value.Values.round`. The first and last y coordinate are set to :code:`yStart` and
            :code:`yEnd`, respectively.
        
            Parameters:
                f (:class:`~cern.accsoft.commons.value.Interpolable`): function to convert
                dx (`Double <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Double.html?is-external=true>`): length of interval. If :code:`null`, calculate from :code:`nIntervals`.
                nIntervals (int): number of intervals
                xStart (double): value of first boundary
                xEnd (double): value of last boundary
                precision (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): number of decimal places for rounding x values. If :code:`null`, don't round.
                yStart (double): value of first y coordinate
                yEnd (double): value of last y coordinate
        
            Returns:
                2D array
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createDiscreteFunction(interpolable: cern.accsoft.commons.value.Interpolable, doubleArray: typing.List[float]) -> cern.accsoft.commons.value.DiscreteFunction:
        """
            Return a :class:`~cern.accsoft.commons.value.DiscreteFunction` by evaluating the given function :code:`f` on an array
            :code:`xCoordinates` of x values.
        
            Parameters:
                f (:class:`~cern.accsoft.commons.value.Interpolable`): function to convert
                xCoordinates (double[]): 
            Returns:
                2D array
        
            Return a DiscreteFunction defined over :code:`nIntervals+1` points by evaluating the given function :code:`f` at the
            boundaries of :code:`nIntervals` intervals, starting end ending at values :code:`xStart` and :code:`xEnd`, respectively.
            The length of an interval is calculated automatically.
        
            Parameters:
                f (:class:`~cern.accsoft.commons.value.Interpolable`): function to convert
                nIntervals (int): number of intervals
                xStart (double): value of first boundary
                xEnd (double): value of last boundary
        
            Returns:
                DiscreteFunction
        
        """
        ...
    @typing.overload
    @staticmethod
    def createDiscreteFunction(interpolable: cern.accsoft.commons.value.Interpolable, int2: int, double: float, double2: float) -> cern.accsoft.commons.value.DiscreteFunction: ...
    @typing.overload
    @staticmethod
    def createDiscreteFunction(interpolable: cern.accsoft.commons.value.Interpolable, double: float, int2: int, double2: float, double3: float, integer: int, double4: float, double5: float) -> cern.accsoft.commons.value.DiscreteFunction: ...

class ExpressionBasedFunction(cern.accsoft.commons.value.ContinuousFunction, java.io.Serializable):
    """
    public class ExpressionBasedFunction extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.ContinuousFunction`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Implement a function based on a mathematical expression of input variables. it's defined as F(x_1, x_2, .. x_N) where
        x_i (i >= 1) are the function's arguments. argument definitions are matched with the actual argument values using their
        index, e.g. x_1 would be resolved to the value number 0 and so forth.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, expression: cern.accsoft.commons.value.expression.Expression): ...
    @typing.overload
    def __init__(self, string: str): ...
    _evaluate__T = typing.TypeVar('_evaluate__T', bound=cern.accsoft.commons.value.Value)  # <T>
    def evaluate(self, valueMap: cern.accsoft.commons.value.expression.ValueMap, list: java.util.List[_evaluate__T]) -> _evaluate__T: ...
    def getFunctionExpression(self) -> cern.accsoft.commons.value.expression.Expression:
        """
            Returns the expression of the function represented by this ExpressionBasedFunction
        
            Returns:
                the expression of the function represented by this ExpressionBasedFunction
        
        
        """
        ...
    def getString(self) -> str: ...
    def getType(self) -> cern.accsoft.commons.value.Type:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Typed.getType`
            Returns the type of this value
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Typed.getType` in interface :class:`~cern.accsoft.commons.value.Typed`
        
            Returns:
                the type of this value
        
        
        """
        ...
    def isDiscrete(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Function.isDiscrete`
            Returns true is this function is a discrete function defined with a list of points. If false one can assume that this
            function is defined with a mathematical formula and does not hold any particular point.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Function.isDiscrete` in interface :class:`~cern.accsoft.commons.value.Function`
        
            Returns:
                true is this function is a discrete function.
        
        
        """
        ...
    @typing.overload
    def performOperation(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, expression: cern.accsoft.commons.value.expression.Expression) -> None:
        """
            performs a binary operation on this function using a specified function
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.BinaryOperation`):         f (:class:`~cern.accsoft.commons.value.spi.function.ExpressionBasedFunction`): 
            performs a binary operation on this function, using a specified expression
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.BinaryOperation`):         e (:class:`~cern.accsoft.commons.value.expression.Expression`): 
        """
        ...
    @typing.overload
    def performOperation(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, expressionBasedFunction: 'ExpressionBasedFunction') -> None: ...
    @typing.overload
    def performOperation(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation) -> None:
        """
            performs an unary operation with this function
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.UnaryOperation`): 
        
        """
        ...
    def setFunctionExpression(self, expression: cern.accsoft.commons.value.expression.Expression) -> None:
        """
        
            Parameters:
                expression (:class:`~cern.accsoft.commons.value.expression.Expression`): 
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class PolynomialImpl(cern.accsoft.commons.value.spi.AbstractValue, cern.accsoft.commons.value.Polynomial, cern.accsoft.commons.value.ImmutableValue):
    """
    public class PolynomialImpl extends :class:`~cern.accsoft.commons.value.spi.AbstractValue` implements :class:`~cern.accsoft.commons.value.Polynomial`, :class:`~cern.accsoft.commons.value.ImmutableValue`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[float], typing.Sequence[float]]): ...
    @typing.overload
    def __init__(self, sortedMap: java.util.SortedMap[int, float]): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.AbstractValue.equals`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.AbstractValue`
        
        
        """
        ...
    @typing.overload
    def execute(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Value.execute`
            Performs the operation on this value with the given value as second operand. This value is changed by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.execute` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.BinaryOperation`): the operation to perform
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand for the binary operation
        
        
        """
        ...
    @typing.overload
    def execute(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Value.execute`
            Performs the given operation on this value. This value is changed by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.execute` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.UnaryOperation`): the operation to perform
        
        """
        ...
    def getCoefficients(self) -> typing.List[float]:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Polynomial.getCoefficients`
            Example: You have polynomial p(x) = a + b*x + c*x^2 the resulting coefficients array would be [a, b, c].
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Polynomial.getCoefficients`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.Polynomial`
        
            Returns:
                the coefficients of the polynomial as an array.
        
        
        """
        ...
    def getDegree(self) -> int:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Polynomial.getDegree` in interface :class:`~cern.accsoft.commons.value.Polynomial`
        
            Returns:
                the maximum degree of the polynomial.
        
        
        """
        ...
    def getString(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.getString`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.AbstractValue.hashCode`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.AbstractValue`
        
        
        """
        ...
    def interpolate(self, double: float) -> float:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`
            Interpolates a new point at the given x-coordinate. If no point can be interpolated NaN is returned.
        
            Interpolates linearly the point at the x-coordinate x using this discrete function. If this function is defined at that
            x-coordinate, the y-coordinate at this point is returned. Else the linear interpolation is performed with the adjacent
            points.
        
            Note that we consider this function is only defined from x1 to x2 where x1 is the x-coordinate of the first point and x2
            is the x-coordinate of the last point. If x1 <= x <= x2 the interpolation can be performed. If x < x1 or x > x2 the
            interpolation cannot be performed and Double.NaN is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.Interpolable`
        
            Parameters:
                x (double): the x-coordinate of the point to interpolate
        
            Returns:
                the new interpolated y-coordinate or NaN
        
        
        """
        ...
    def isDiscrete(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Function.isDiscrete`
            Returns true is this function is a discrete function defined with a list of points. If false one can assume that this
            function is defined with a mathematical formula and does not hold any particular point.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Function.isDiscrete` in interface :class:`~cern.accsoft.commons.value.Function`
        
            Returns:
                true is this function is a discrete function.
        
        
        """
        ...
    def makeMutable(self) -> cern.accsoft.commons.value.Value:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`
            Returns a mutable version of this immutable value. The mutable version is made by performing a deep copy of this value.
            The runtime type of the value is preserved by this operation. The resulting value can be cast in the mutable type
            corresponding to the immutable type of this value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Returns:
                a mutable deep copy of this value
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.AbstractValue.toString`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.AbstractValue`
        
        
        """
        ...

class BoundedPolynomialImpl(PolynomialImpl, cern.accsoft.commons.value.BoundedPolynomial):
    """
    public class BoundedPolynomialImpl extends :class:`~cern.accsoft.commons.value.spi.function.PolynomialImpl` implements :class:`~cern.accsoft.commons.value.BoundedPolynomial`
    
        Stores always a relative :class:`~cern.accsoft.commons.value.Polynomial`, where the coefficients are defined with
        respect to the lower boundaries of the interval, i.e. the polynomial :code:`p[n]` should be evaluated as
        :code:`p[n].interpolate(x - b)`, where :code:`b` is the lower bound.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, polynomial: cern.accsoft.commons.value.Polynomial, interval: cern.accsoft.commons.value.Interval): ...
    @typing.overload
    def __init__(self, polynomial: cern.accsoft.commons.value.Polynomial, double: float, double2: float): ...
    @staticmethod
    def createRelativeBoundedPolynomial(doubleArray: typing.List[float]) -> cern.accsoft.commons.value.BoundedPolynomial:
        """
        
            Parameters:
                boundedPolynomialAsArray (double[]): an array containing lower bound, upper bound and then the coefficients in increasing order.
        
            Returns:
                a :class:`~cern.accsoft.commons.value.BoundedPolynomial`, where the coefficients are defined with respect to the lower
                boundaries of the interval, i.e. the polynomial :code:`p[n]` should be evaluated as :code:`p[n].interpolate(x - b)`,
                where :code:`b` is the lower bound.
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.function.PolynomialImpl.equals`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.function.PolynomialImpl`
        
        
        """
        ...
    @typing.overload
    def execute(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Value.execute`
            Performs the operation on this value with the given value as second operand. This value is changed by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.execute` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.function.PolynomialImpl.execute`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.function.PolynomialImpl`
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.BinaryOperation`): the operation to perform
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand for the binary operation
        
        
        """
        ...
    @typing.overload
    def execute(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Value.execute`
            Performs the given operation on this value. This value is changed by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.execute` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.function.PolynomialImpl.execute`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.function.PolynomialImpl`
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.UnaryOperation`): the operation to perform
        
        """
        ...
    def getInterval(self) -> cern.accsoft.commons.value.Interval:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.BoundedPolynomial.getInterval`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
            Returns:
                the :class:`~cern.accsoft.commons.value.Interval` of this :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
        
        """
        ...
    def getString(self) -> str:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.getString`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.function.PolynomialImpl.getString`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.function.PolynomialImpl`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.function.PolynomialImpl.hashCode`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.function.PolynomialImpl`
        
        
        """
        ...
    def interpolate(self, double: float) -> float:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`
            Interpolates a new point at the given x-coordinate. If no point can be interpolated NaN is returned.
        
            Interpolates linearly the point at the x-coordinate x using this discrete function. If this function is defined at that
            x-coordinate, the y-coordinate at this point is returned. Else the linear interpolation is performed with the adjacent
            points.
        
            Note that we consider this function is only defined from x1 to x2 where x1 is the x-coordinate of the first point and x2
            is the x-coordinate of the last point. If x1 <= x <= x2 the interpolation can be performed. If x < x1 or x > x2 the
            interpolation cannot be performed and Double.NaN is returned.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.BoundedPolynomial.interpolate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.Interpolable`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.function.PolynomialImpl.interpolate`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.function.PolynomialImpl`
        
            Parameters:
                x (double): the x-coordinate of the point to interpolate
        
            Returns:
                the new interpolated y-coordinate or NaN
        
            Also see:
                :meth:`~cern.accsoft.commons.value.spi.function.AbstractMathFunction.interpolate`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.function.PolynomialImpl.toString`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.function.PolynomialImpl`
        
        
        """
        ...

class ConstantFunction(ExpressionBasedFunction):
    """
    public class ConstantFunction extends :class:`~cern.accsoft.commons.value.spi.function.ExpressionBasedFunction`
    
        Implement a scalars function
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float): ...

class CubicSplineFunctionPrototype(AbstractMathFunction):
    """
    public class CubicSplineFunctionPrototype extends :class:`~cern.accsoft.commons.value.spi.function.AbstractMathFunction`
    
        Equivalent to :class:`~cern.accsoft.commons.value.ParabolicSplineFunction` but uses cubic spline to connect all points.
        This class was not really used and not tested. I put it in the spi.function package in case we want to use it in the
        future (didn't want to delete it as it's quite complicated).
    """
    def __init__(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction): ...
    def getAcceleration(self, double: float) -> float:
        """
        
            Parameters:
                x (double): 
            Returns:
        
        
        """
        ...
    def getFunction(self) -> cern.accsoft.commons.value.ImmutableDiscreteFunction:
        """
            Returns the function for which the spline is calculated
        
            Returns:
                function passed to the constructor: :code:`#ParabolicSplineFunction(ImmutableDiscreteFunction)`
        
        
        """
        ...
    def getSplineX(self, int: int) -> float:
        """
            Returns X coordinate of the spline point (point where two parabolas meet).
        
            Parameters:
                segmentIndex (int): index of the function segment. 1 corresponds to the segment between first and second point, 2, to the second and third
                    point etc..
        
            Returns:
                X coordinate of the spline point
        
        
        """
        ...
    @typing.overload
    def toDiscreteFunction(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, double: float, int: int) -> cern.accsoft.commons.value.DiscreteFunction:
        """
        public :class:`~cern.accsoft.commons.value.DiscreteFunction` toDiscreteFunction (:class:`~cern.accsoft.commons.value.ImmutableDiscreteFunction` toleranceFunction, double minXSpacing, int precision)
        
        
        """
        ...
    @typing.overload
    def toDiscreteFunction(self, double: float, double2: float, int: int) -> cern.accsoft.commons.value.DiscreteFunction: ...

class DiscreteFunctionArrayImpl(DiscreteFunctionImpl, java.io.Serializable):
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool): ...
    @typing.overload
    def __init__(self, intArray: typing.List[int], doubleArray: typing.List[float]): ...
    def clone(self) -> typing.Any: ...
    def getX(self, int: int) -> float: ...
    def getY(self, int: int) -> float: ...
    def indexOf(self, double: float) -> int: ...
    @typing.overload
    def insert(self, double: float) -> bool: ...
    @typing.overload
    def insert(self, double: float, double2: float) -> bool: ...
    @typing.overload
    def insertAll(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, double: float) -> int: ...
    @typing.overload
    def insertAll(self, doubleArray: typing.List[float]) -> int: ...
    def makeMutable(self) -> cern.accsoft.commons.value.DiscreteFunction: ...
    @staticmethod
    def newInstanceWithoutCoordinatesCheck(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> 'DiscreteFunctionArrayImpl': ...
    def remove(self, double: float) -> bool: ...
    def removeAll(self, doubleArray: typing.List[float]) -> int: ...
    def retainAll(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, double: float) -> int: ...
    def setX(self, int: int, double: float) -> None: ...
    def setY(self, int: int, double: float) -> None: ...
    def size(self) -> int: ...
    def stringValue(self) -> str: ...
    def subFunction(self, double: float, double2: float) -> cern.accsoft.commons.value.DiscreteFunction: ...
    def subView(self, double: float, double2: float) -> cern.accsoft.commons.value.DiscreteFunction: ...
    @typing.overload
    def toPointArray(self) -> typing.List[cern.accsoft.commons.value.ImmutablePoint]: ...
    @typing.overload
    def toPointArray(self, immutablePointArray: typing.List[cern.accsoft.commons.value.ImmutablePoint]) -> typing.List[cern.accsoft.commons.value.ImmutablePoint]: ...
    def toXArray(self) -> typing.List[float]: ...
    def toYArray(self) -> typing.List[float]: ...
    def translate(self, double: float) -> None: ...

class DiscreteFunctionListImpl(DiscreteFunctionImpl, cern.accsoft.commons.value.DiscreteFunctionList):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, immutableDiscreteFunctionArray: typing.List[cern.accsoft.commons.value.ImmutableDiscreteFunction]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], intArray: typing.List[int]): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getAbsoluteFunction(self, int: int) -> cern.accsoft.commons.value.ImmutableDiscreteFunction: ...
    def getFunction(self, int: int) -> cern.accsoft.commons.value.ImmutableDiscreteFunction: ...
    def getFunctions(self) -> typing.List[cern.accsoft.commons.value.ImmutableDiscreteFunction]: ...
    def getFunctionsCount(self) -> int: ...
    def getSizeIncludingStopPoints(self) -> int: ...
    def getStopPointsIndices(self) -> typing.List[int]: ...
    def getString(self) -> str: ...
    def getX(self, int: int) -> float: ...
    def getY(self, int: int) -> float: ...
    def hashCode(self) -> int: ...
    def indexOf(self, double: float) -> int: ...
    @typing.overload
    def insert(self, double: float) -> bool: ...
    @typing.overload
    def insert(self, double: float, double2: float) -> bool: ...
    @typing.overload
    def insertAll(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, double: float) -> int: ...
    @typing.overload
    def insertAll(self, doubleArray: typing.List[float]) -> int: ...
    def makeMutable(self) -> cern.accsoft.commons.value.DiscreteFunctionList: ...
    def merge(self, int: int) -> None: ...
    def remove(self, double: float) -> bool: ...
    def removeAll(self, doubleArray: typing.List[float]) -> int: ...
    def retainAll(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, double: float) -> int: ...
    def setStopPoints(self, intArray: typing.List[int]) -> None: ...
    def setY(self, int: int, double: float) -> None: ...
    def size(self) -> int: ...
    def split(self, double: float) -> None: ...
    def subFunction(self, double: float, double2: float) -> cern.accsoft.commons.value.DiscreteFunctionList: ...
    def subView(self, double: float, double2: float) -> cern.accsoft.commons.value.DiscreteFunction: ...
    @typing.overload
    def toPointArray(self) -> typing.List[cern.accsoft.commons.value.ImmutablePoint]: ...
    @typing.overload
    def toPointArray(self, immutablePointArray: typing.List[cern.accsoft.commons.value.ImmutablePoint]) -> typing.List[cern.accsoft.commons.value.ImmutablePoint]: ...
    def toSimpleParameterValue(self) -> cern.japc.value.SimpleParameterValue: ...
    def toXArray(self) -> typing.List[float]: ...
    def toYArray(self) -> typing.List[float]: ...
    def translate(self, double: float) -> None: ...

class DiscreteFunctionPointImpl(DiscreteFunctionImpl, cern.accsoft.commons.value.DiscreteFunction, java.io.Serializable):
    @typing.overload
    def __init__(self, immutablePointArray: typing.List[cern.accsoft.commons.value.ImmutablePoint]): ...
    @typing.overload
    def __init__(self, pointArray: typing.List[cern.accsoft.commons.value.Point]): ...
    def clone(self) -> typing.Any: ...
    def getX(self, int: int) -> float: ...
    def getY(self, int: int) -> float: ...
    def indexOf(self, double: float) -> int: ...
    @typing.overload
    def insert(self, double: float) -> bool: ...
    @typing.overload
    def insert(self, double: float, double2: float) -> bool: ...
    @typing.overload
    def insertAll(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, double: float) -> int: ...
    @typing.overload
    def insertAll(self, doubleArray: typing.List[float]) -> int: ...
    def makeMutable(self) -> cern.accsoft.commons.value.DiscreteFunction: ...
    def remove(self, double: float) -> bool: ...
    def removeAll(self, doubleArray: typing.List[float]) -> int: ...
    def retainAll(self, immutableDiscreteFunction: cern.accsoft.commons.value.ImmutableDiscreteFunction, double: float) -> int: ...
    def setX(self, int: int, double: float) -> None: ...
    def setY(self, int: int, double: float) -> None: ...
    def size(self) -> int: ...
    def stringValue(self) -> str: ...
    def subFunction(self, double: float, double2: float) -> cern.accsoft.commons.value.DiscreteFunction: ...
    def subView(self, double: float, double2: float) -> cern.accsoft.commons.value.DiscreteFunction: ...
    @typing.overload
    def toPointArray(self) -> typing.List[cern.accsoft.commons.value.ImmutablePoint]: ...
    @typing.overload
    def toPointArray(self, immutablePointArray: typing.List[cern.accsoft.commons.value.ImmutablePoint]) -> typing.List[cern.accsoft.commons.value.ImmutablePoint]: ...
    def toString(self) -> str: ...
    def toXArray(self) -> typing.List[float]: ...
    def toYArray(self) -> typing.List[float]: ...
    def translate(self, double: float) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.value.spi.function")``.

    AbstractMathFunction: typing.Type[AbstractMathFunction]
    BoundedPolynomialImpl: typing.Type[BoundedPolynomialImpl]
    BoundedPolynomialIntervalComparator: typing.Type[BoundedPolynomialIntervalComparator]
    BoundedPolynomialSequenceImpl: typing.Type[BoundedPolynomialSequenceImpl]
    ConstantFunction: typing.Type[ConstantFunction]
    CubicSplineFunctionPrototype: typing.Type[CubicSplineFunctionPrototype]
    DiscreteFunctionArrayImpl: typing.Type[DiscreteFunctionArrayImpl]
    DiscreteFunctionImpl: typing.Type[DiscreteFunctionImpl]
    DiscreteFunctionListImpl: typing.Type[DiscreteFunctionListImpl]
    DiscreteFunctionPointImpl: typing.Type[DiscreteFunctionPointImpl]
    DiscreteFunctionsArrayImpl: typing.Type[DiscreteFunctionsArrayImpl]
    Discretizer: typing.Type[Discretizer]
    ExpressionBasedFunction: typing.Type[ExpressionBasedFunction]
    PolynomialImpl: typing.Type[PolynomialImpl]
