import cern.accsoft.commons.util
import cern.accsoft.commons.util.value
import cern.accsoft.commons.value.expression
import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.spi
import cern.accsoft.commons.value.spi.function
import cern.accsoft.commons.value.spi.operation
import cern.japc.value
import java.io
import java.lang
import java.util
import typing



class BoundedPolynomials:
    """
    public final class BoundedPolynomials extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility class to transform or manipulate :class:`~cern.accsoft.commons.value.BoundedPolynomial`.
    """
    @typing.overload
    @staticmethod
    def createBoundedPolynomialSequence(boundedPolynomialArray: typing.List['BoundedPolynomial']) -> 'BoundedPolynomialSequence':
        """
            Creates a :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`, where the coefficients are defined with
            respect to lower boundaries of the interval, i.e. the polynomial :code:`p[n]` should be evaluated as
            :code:`p[n].interpolate(x - b)`, where :code:`b` is the lower bound.
        
            Parameters:
                boundedPolynomials (:class:`~cern.accsoft.commons.value.BoundedPolynomial`[]): an array of :class:`~cern.accsoft.commons.value.BoundedPolynomial`s
        
            Returns:
                a :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createBoundedPolynomialSequence(collection: typing.Union[java.util.Collection['BoundedPolynomial'], typing.Sequence['BoundedPolynomial']]) -> 'BoundedPolynomialSequence': ...
    @staticmethod
    def createLinearBoundedPolynomialSequence(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> 'BoundedPolynomialSequence':
        """
            Creates a :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence` containing linear
            :class:`~cern.accsoft.commons.value.Polynomial` (degree 1) between every neighboring interpolation from two arrays of x
            and y values.
        
            Parameters:
                xValues (double[]): array of x coordinates (with at least two values)
                yValues (double[]): array of corresponding y coordinates (with at least two values)
        
            Returns:
                a :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def forAbsoluteBoundedPolynomial(polynomial: 'Polynomial', interval: 'Interval') -> 'BoundedPolynomial':
        """
            Creates a :class:`~cern.accsoft.commons.value.BoundedPolynomial`, where the coefficients are defined with respect to
            zero, i.e. the polynomial :code:`p[n]` should be evaluated as :code:`p[n].interpolate(x)` independent of the boundaries.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                lowerBound (double): the lower bound of the :class:`~cern.accsoft.commons.value.Polynomial`
                upperBound (double): the upper bound of the :class:`~cern.accsoft.commons.value.Polynomial`
        
            Returns:
                a :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
            Creates a :class:`~cern.accsoft.commons.value.BoundedPolynomial`, where the coefficients are defined with respect to
            zero, i.e. the polynomial :code:`p[n]` should be evaluated as :code:`p[n].interpolate(x)` independent of the boundaries.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                interval (:class:`~cern.accsoft.commons.value.Interval`): the interval of the :class:`~cern.accsoft.commons.value.Polynomial`
        
            Returns:
                a :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def forAbsoluteBoundedPolynomial(polynomial: 'Polynomial', double: float, double2: float) -> 'BoundedPolynomial': ...
    @typing.overload
    @staticmethod
    def forRelativeBoundedPolynomial(polynomial: 'Polynomial', interval: 'Interval') -> 'BoundedPolynomial':
        """
            Creates a :class:`~cern.accsoft.commons.value.BoundedPolynomial`, where the coefficients are defined with respect to the
            lower bound, i.e. the polynomial :code:`p[n]` should be evaluated as :code:`p[n].interpolate(x - lowerBound)`.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                lowerBound (double): the lower bound of the :class:`~cern.accsoft.commons.value.Polynomial`
                upperBound (double): the upper bound of the :class:`~cern.accsoft.commons.value.Polynomial`
        
            Returns:
                a :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
            Creates a :class:`~cern.accsoft.commons.value.BoundedPolynomial`, where the coefficients are defined with respect to the
            lower bound of the interval, i.e. the polynomial :code:`p[n]` should be evaluated as :code:`p[n].interpolate(x - b)`,
            where :code:`b` is the lower bound.
        
            Parameters:
                p (:class:`~cern.accsoft.commons.value.Polynomial`): the :class:`~cern.accsoft.commons.value.Polynomial`
                interval (:class:`~cern.accsoft.commons.value.Interval`): the interval of the :class:`~cern.accsoft.commons.value.Polynomial`
        
            Returns:
                a :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def forRelativeBoundedPolynomial(polynomial: 'Polynomial', double: float, double2: float) -> 'BoundedPolynomial': ...
    @typing.overload
    @staticmethod
    def getIntervals(boundedPolynomialSequence: 'BoundedPolynomialSequence') -> typing.List['Interval']:
        """
            Extracts intervals from the given :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`.
        
            Parameters:
                bps (:class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`): non-null :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
            Returns:
                array of :class:`~cern.accsoft.commons.value.Interval`
        
            Extracts intervals from the given :class:`~cern.accsoft.commons.value.BoundedPolynomial`.
        
            Parameters:
                bps (:class:`~cern.accsoft.commons.value.BoundedPolynomial`[]): non-null array of :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
            Returns:
                array of intervals
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getIntervals(boundedPolynomialArray: typing.List['BoundedPolynomial']) -> typing.List['Interval']: ...
    @typing.overload
    @staticmethod
    def getLength(boundedPolynomial: 'BoundedPolynomial') -> float:
        """
            This method behaves equal to :meth:`~cern.accsoft.commons.value.Interval.getLength`.
        
            Parameters:
                bp (:class:`~cern.accsoft.commons.value.BoundedPolynomial`): the bounded polynomial
        
            Returns:
                the length of this :class:`~cern.accsoft.commons.value.BoundedPolynomial` :class:`~cern.accsoft.commons.value.Interval`
        
            This method behaves equal to :meth:`~cern.accsoft.commons.value.Interval.getLength`.
        
            Parameters:
                bps (:class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`): the bounded polynomial sequence
        
            Returns:
                the length of the lowest lowerBound to the highest upper bound of all
                :class:`~cern.accsoft.commons.value.BoundedPolynomial` in this
                :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getLength(boundedPolynomialSequence: 'BoundedPolynomialSequence') -> float: ...
    @staticmethod
    def isContinue(boundedPolynomialSequence: 'BoundedPolynomialSequence', boundedPolynomialSequence2: 'BoundedPolynomialSequence') -> bool:
        """
        
            Parameters:
                bps1 (:class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`): the first :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
                bps2 (:class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`): the next :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
            Returns:
                true, if the upperBound of the last :class:`~cern.accsoft.commons.value.BoundedPolynomial` of bps1 value is equal to the
                lowerBound value of the first :class:`~cern.accsoft.commons.value.BoundedPolynomial` of bps2
        
        
        """
        ...
    @staticmethod
    def isContinueWith(boundedPolynomialSequence: 'BoundedPolynomialSequence', boundedPolynomialSequence2: 'BoundedPolynomialSequence', double: float) -> bool:
        """
        
            Parameters:
                bps1 (:class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`): the first :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
                bps2 (:class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`): the next :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
                precision (double): the precision applied for the comparison operation (precision is needed as smallest value of the given amount of decimal
                    places)
        
            Returns:
                true, if the upperBound of the last :class:`~cern.accsoft.commons.value.BoundedPolynomial` of bps1 value is equal to the
                lowerBound value of the first :class:`~cern.accsoft.commons.value.BoundedPolynomial` of bps2
        
        
        """
        ...
    @staticmethod
    def toAbsolutePolynomial(boundedPolynomial: 'BoundedPolynomial') -> 'Polynomial':
        """
            Returns a :class:`~cern.accsoft.commons.value.Polynomial`, where the coefficients are defined with respect to zero, i.e.
            the polynomial :code:`p[n]` should be evaluated as :code:`p[n].interpolate(x)` independent of the boundaries.
        
            Parameters:
                bp (:class:`~cern.accsoft.commons.value.BoundedPolynomial`): the given :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
            Returns:
                :class:`~cern.accsoft.commons.value.Polynomial` relative to zero
        
        
        """
        ...
    @staticmethod
    def toAbsolutePolynomials(boundedPolynomialSequence: 'BoundedPolynomialSequence') -> typing.List['Polynomial']:
        """
            Return the :class:`~cern.accsoft.commons.value.Polynomial` defining the function as an array, where the coefficients are
            defined with respect to zero, i.e. the :class:`~cern.accsoft.commons.value.Polynomial` :code:`p[n]` should be evaluated
            as :code:`p[n].interpolate(x)` independent of the boundaries.
        
            Parameters:
                bps (:class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`): the given :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
            Returns:
                array of :class:`~cern.accsoft.commons.value.Polynomial` relative to zero
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def toDiscreteFunction(boundedPolynomialSequence: 'BoundedPolynomialSequence') -> 'DiscreteFunction':
        """
            This returns the same as calling #toImmutableDiscreteFunction(BoundedPolynomialSequence, double) with stepSize =
            interval.getLength() / 50.
        
            Parameters:
                bps (:class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`): the :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
            Returns:
                an DiscreteFunction from a :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
            Also see:
                :meth:`~cern.accsoft.commons.value.BoundedPolynomials.toDiscreteFunction`
        
        
            Parameters:
                bps (:class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`): the :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
                stepSize (double): the size of the step between two x-values (e.g. stepSize = 0.5 and interval [0;2] -> steps are [0; 0.5; 1; 1.5; 2] or if
                    stepSize = 2 and interval [0;4] -> steps are [0; 2; 4] Also if the degree of the Polynomial is less than 2 only the
                    first and the last values are stored regardless of the stepSize.
        
            Returns:
                a :class:`~cern.accsoft.commons.value.DiscreteFunction` from a
                :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def toDiscreteFunction(boundedPolynomialSequence: 'BoundedPolynomialSequence', double: float) -> 'DiscreteFunction': ...
    @staticmethod
    def toRelativePolynomial(boundedPolynomial: 'BoundedPolynomial') -> 'Polynomial':
        """
            Returns a :class:`~cern.accsoft.commons.value.Polynomial`, where the coefficients are defined with respect to the lower
            boundaries of the interval, i.e. the polynomial :code:`p[n]` should be evaluated as :code:`p[n].interpolate(x - b)`,
            where :code:`b` is the lower bound.
        
            Parameters:
                bp (:class:`~cern.accsoft.commons.value.BoundedPolynomial`): the given :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
            Returns:
                :class:`~cern.accsoft.commons.value.Polynomial` relative to lower boundary
        
        
        """
        ...
    @staticmethod
    def toRelativePolynomials(boundedPolynomialSequence: 'BoundedPolynomialSequence') -> typing.List['Polynomial']:
        """
            Return the :class:`~cern.accsoft.commons.value.Polynomial` defining the function as an array, where the coefficients are
            defined with respect to the lower boundaries of the intervals, i.e. the :class:`~cern.accsoft.commons.value.Polynomial`
            :code:`p[n]` should be evaluated as :code:`p[n].interpolate(x - b[n])`, where :code:`b[n]` is the lower bound.
        
            Parameters:
                bps (:class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`): the given :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
            Returns:
                array of :class:`~cern.accsoft.commons.value.Polynomial` relative to lower boundary
        
        
        """
        ...

class DiscreteFunctionCompressor:
    """
    public class DiscreteFunctionCompressor extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Implements a compression on discrete functions, using Genetic Algorithm.
    """
    @typing.overload
    def __init__(self, discreteFunction: 'DiscreteFunction', int: int): ...
    @typing.overload
    def __init__(self, discreteFunction: 'DiscreteFunction', int: int, int2: int, int3: int, int4: int, float: float): ...
    def compressFunction(self) -> 'DiscreteFunction': ...

class DiscreteFunctions:
    DEFAULT_SHIFT_COMPENSATION_FACTOR: typing.ClassVar[float] = ...
    @staticmethod
    def align(discreteFunction: 'DiscreteFunction', int: int, int2: int) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def buildDiscreteFunctionList(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> cern.japc.value.DiscreteFunctionList: ...
    @typing.overload
    @staticmethod
    def buildDiscreteFunctionList(doubleArray: typing.List[float], doubleArray2: typing.List[float], intArray: typing.List[int]) -> cern.japc.value.DiscreteFunctionList: ...
    @typing.overload
    @staticmethod
    def compare(immutableDiscreteFunction: 'ImmutableDiscreteFunction', immutableDiscreteFunction2: 'ImmutableDiscreteFunction') -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def compare(immutableDiscreteFunction: 'ImmutableDiscreteFunction', immutableDiscreteFunction2: 'ImmutableDiscreteFunction', double: float) -> 'DiscreteFunction': ...
    @staticmethod
    def computeDerivative(immutableDiscreteFunction: 'ImmutableDiscreteFunction', approximationMode: 'DiscreteFunctions.ApproximationMode') -> 'DiscreteFunction': ...
    @staticmethod
    def computeIntegral(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> float: ...
    @staticmethod
    def computeTotalSize(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> int: ...
    @staticmethod
    def concat(immutableDiscreteFunction: 'ImmutableDiscreteFunction', immutableDiscreteFunction2: 'ImmutableDiscreteFunction') -> 'DiscreteFunction': ...
    @staticmethod
    def containsNaN(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> bool: ...
    @staticmethod
    def convertFromJAPCFunction(discreteFunction: cern.japc.value.DiscreteFunction) -> 'ImmutableDiscreteFunction': ...
    @staticmethod
    def convertFromJAPCFunctionList(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> 'ImmutableDiscreteFunctionList': ...
    @staticmethod
    def convertToJAPCFunction(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> cern.japc.value.DiscreteFunction: ...
    @staticmethod
    def convertToJAPCFunctionList(immutableDiscreteFunctionList: 'ImmutableDiscreteFunctionList') -> cern.japc.value.DiscreteFunctionList: ...
    @staticmethod
    def createConstantDiscreteFunction(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def dx(immutableDiscreteFunction: 'ImmutableDiscreteFunction', int: int) -> float: ...
    @typing.overload
    @staticmethod
    def dx(immutableDiscreteFunction: 'ImmutableDiscreteFunction', int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def dy(immutableDiscreteFunction: 'ImmutableDiscreteFunction', int: int) -> float: ...
    @typing.overload
    @staticmethod
    def dy(immutableDiscreteFunction: 'ImmutableDiscreteFunction', int: int, int2: int) -> float: ...
    @typing.overload
    @staticmethod
    def extractXArray(immutableDiscreteFunctionList: 'ImmutableDiscreteFunctionList') -> typing.List[float]: ...
    @typing.overload
    @staticmethod
    def extractXArray(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> typing.List[float]: ...
    @typing.overload
    @staticmethod
    def extractYArray(immutableDiscreteFunctionList: 'ImmutableDiscreteFunctionList') -> typing.List[float]: ...
    @typing.overload
    @staticmethod
    def extractYArray(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> typing.List[float]: ...
    @typing.overload
    @staticmethod
    def filter(discreteFunction: 'DiscreteFunction', double: float) -> 'DiscreteFunctions.FilterResult': ...
    @typing.overload
    @staticmethod
    def filter(discreteFunction: 'DiscreteFunction', double: float, interval: 'Interval') -> 'DiscreteFunctions.FilterResult': ...
    @typing.overload
    @staticmethod
    def filterByXCoordinate(discreteFunction: 'DiscreteFunction', double: float) -> None: ...
    @typing.overload
    @staticmethod
    def filterByXCoordinate(discreteFunction: 'DiscreteFunction', double: float, double2: float) -> None: ...
    @staticmethod
    def filterFractionalXCoordinates(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> 'ImmutableDiscreteFunction': ...
    @typing.overload
    @staticmethod
    def filterRamerDouglasPeucker(discreteFunction: 'DiscreteFunction', double: float) -> 'DiscreteFunctions.FilterResult': ...
    @typing.overload
    @staticmethod
    def filterRamerDouglasPeucker(discreteFunction: 'DiscreteFunction', double: float, interval: 'Interval') -> 'DiscreteFunctions.FilterResult': ...
    @staticmethod
    def getAbsoluteFunction(discreteFunctionList: cern.japc.value.DiscreteFunctionList, int: int) -> cern.japc.value.DiscreteFunction: ...
    @staticmethod
    def getAllXforY(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> java.util.SortedSet[float]: ...
    @typing.overload
    @staticmethod
    def getAvailableConstantSpaceAtBeginning(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> float: ...
    @typing.overload
    @staticmethod
    def getAvailableConstantSpaceAtBeginning(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> float: ...
    @typing.overload
    @staticmethod
    def getAvailableConstantSpaceAtEnd(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> float: ...
    @typing.overload
    @staticmethod
    def getAvailableConstantSpaceAtEnd(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> float: ...
    @staticmethod
    def getSplitIndices(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> typing.List[int]: ...
    @staticmethod
    def getXforY(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> float: ...
    @typing.overload
    @staticmethod
    def hasSameLength(immutableDiscreteFunction: 'ImmutableDiscreteFunction', int: int) -> bool: ...
    @typing.overload
    @staticmethod
    def hasSameLength(immutableDiscreteFunctionsArray: 'ImmutableDiscreteFunctionsArray', int: int) -> bool: ...
    @staticmethod
    def inRange(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> bool: ...
    @staticmethod
    def indexOf(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float, double2: float) -> int: ...
    @staticmethod
    def integrate(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> 'DiscreteFunction': ...
    @staticmethod
    def interpolate(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> float: ...
    @typing.overload
    @staticmethod
    def isConstant(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> bool: ...
    @typing.overload
    @staticmethod
    def isConstant(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def isConstant(immutableDiscreteFunctionsArray: 'ImmutableDiscreteFunctionsArray') -> bool: ...
    @typing.overload
    @staticmethod
    def isConstant(immutableDiscreteFunctionsArray: 'ImmutableDiscreteFunctionsArray', double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def isContinue(immutableDiscreteFunction: 'ImmutableDiscreteFunction', immutableDiscreteFunction2: 'ImmutableDiscreteFunction') -> bool: ...
    @typing.overload
    @staticmethod
    def isContinue(immutableDiscreteFunctionsArray: 'ImmutableDiscreteFunctionsArray', immutableDiscreteFunctionsArray2: 'ImmutableDiscreteFunctionsArray') -> bool: ...
    @typing.overload
    @staticmethod
    def isContinueWith(immutableDiscreteFunction: 'ImmutableDiscreteFunction', immutableDiscreteFunction2: 'ImmutableDiscreteFunction', double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def isContinueWith(immutableDiscreteFunction: 'ImmutableDiscreteFunction', immutableDiscreteFunction2: 'ImmutableDiscreteFunction', double: float, double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def isEmpty(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> bool: ...
    @typing.overload
    @staticmethod
    def isEmpty(immutableDiscreteFunctionsArray: 'ImmutableDiscreteFunctionsArray') -> bool: ...
    @staticmethod
    def isMonotonic(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> bool: ...
    @staticmethod
    def isStriclyAscending(doubleArray: typing.List[float]) -> bool: ...
    @staticmethod
    def isStrictlyMonotonic(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> bool: ...
    @typing.overload
    @staticmethod
    def isZero(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> bool: ...
    @typing.overload
    @staticmethod
    def isZero(immutableDiscreteFunctionsArray: 'ImmutableDiscreteFunctionsArray') -> bool: ...
    @staticmethod
    def max(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> float: ...
    @staticmethod
    def maxCoordinates(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> cern.accsoft.commons.util.value.Pair[float, java.util.SortedSet[float]]: ...
    @staticmethod
    def min(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> float: ...
    @staticmethod
    def minCoordinates(immutableDiscreteFunction: 'ImmutableDiscreteFunction') -> cern.accsoft.commons.util.value.Pair[float, java.util.SortedSet[float]]: ...
    @staticmethod
    def normalizeByXCoordinates(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float, double2: float) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def reduceFunctionPoints(immutableDiscreteFunction: 'ImmutableDiscreteFunction', int: int) -> 'ImmutableDiscreteFunction': ...
    @typing.overload
    @staticmethod
    def reduceFunctionPoints(immutableDiscreteFunction: 'ImmutableDiscreteFunction', int: int, functionPointReductionOptions: 'FunctionPointReductionOptions') -> 'ImmutableDiscreteFunction': ...
    @typing.overload
    @staticmethod
    def reduceFunctionPoints(immutableDiscreteFunction: 'ImmutableDiscreteFunction', int: int, double: float) -> 'ImmutableDiscreteFunction': ...
    @typing.overload
    @staticmethod
    def shift(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> 'ImmutableDiscreteFunction': ...
    @typing.overload
    @staticmethod
    def shift(immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float, double2: float) -> 'ImmutableDiscreteFunction': ...
    @staticmethod
    def toArray(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> typing.List[cern.japc.value.DiscreteFunction]: ...
    @staticmethod
    def toXArray(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> typing.List[float]: ...
    @staticmethod
    def toYArray(discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> typing.List[float]: ...
    class ApproximationMode(java.lang.Enum['DiscreteFunctions.ApproximationMode']):
        FORWARD: typing.ClassVar['DiscreteFunctions.ApproximationMode'] = ...
        BACKWARD: typing.ClassVar['DiscreteFunctions.ApproximationMode'] = ...
        CENTERED: typing.ClassVar['DiscreteFunctions.ApproximationMode'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'DiscreteFunctions.ApproximationMode': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['DiscreteFunctions.ApproximationMode']: ...
    class FilterResult(java.lang.Enum['DiscreteFunctions.FilterResult']):
        FILTERED: typing.ClassVar['DiscreteFunctions.FilterResult'] = ...
        NOT_FILTERED: typing.ClassVar['DiscreteFunctions.FilterResult'] = ...
        ONLY_FLAT_TOPS: typing.ClassVar['DiscreteFunctions.FilterResult'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'DiscreteFunctions.FilterResult': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['DiscreteFunctions.FilterResult']: ...

class FunctionOperationException(java.lang.RuntimeException):
    """
    public class FunctionOperationException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
        Thrown when a mathematical operation or manipulation on a function has failed or it was not possible to perform it.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, string: str): ...

class FunctionPointReductionOptions:
    """
    public class FunctionPointReductionOptions extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def defaults() -> 'FunctionPointReductionOptions': ...
    def getInitialTolerance(self) -> float: ...
    def getMaxRounds(self) -> int: ...
    def getToleranceIncrementMultiplier(self) -> float: ...
    def withInitialTolerance(self, double: float) -> 'FunctionPointReductionOptions': ...
    def withMaxRounds(self, int: int) -> 'FunctionPointReductionOptions': ...
    def withToleranceIncrementMultiplier(self, double: float) -> 'FunctionPointReductionOptions': ...

class Indexed:
    """
    public interface Indexed
    """
    def execute(self, indexing: cern.accsoft.commons.value.spi.operation.Indexing) -> 'Scalar':
        """
            this method returns because the ValueType changes during execution
        
            Parameters:
                oper (:class:`~cern.accsoft.commons.value.spi.operation.Indexing`): 
            Returns:
                Scalar
        
        
        """
        ...

class Interpolable:
    """
    public interface Interpolable
    """
    def interpolate(self, double: float) -> float:
        """
            Interpolates a new point at the given x-coordinate. If no point can be interpolated NaN is returned.
        
            Interpolates linearly the point at the x-coordinate x using this discrete function. If this function is defined at that
            x-coordinate, the y-coordinate at this point is returned. Else the linear interpolation is performed with the adjacent
            points.
        
            Note that we consider this function is only defined from x1 to x2 where x1 is the x-coordinate of the first point and x2
            is the x-coordinate of the last point. If x1 <= x <= x2 the interpolation can be performed. If x < x1 or x > x2 the
            interpolation cannot be performed and Double.NaN is returned.
        
            Parameters:
                x (double): the x-coordinate of the point to interpolate
        
            Returns:
                the new interpolated y-coordinate or NaN
        
        
        """
        ...

class Interval(java.io.Serializable):
    INFINITY: typing.ClassVar['Interval'] = ...
    BOUNDS_COMPARATOR: typing.ClassVar[java.util.Comparator] = ...
    def __init__(self, double: float, double2: float): ...
    def compareByBoundsTo(self, interval: 'Interval') -> int: ...
    def compareTo(self, interval: 'Interval') -> int: ...
    def contains(self, double: float) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    @staticmethod
    def gapIntervals(intervalArray: typing.List['Interval']) -> typing.List['Interval']: ...
    def getLength(self) -> float: ...
    def getLowerBound(self) -> float: ...
    def getUpperBound(self) -> float: ...
    def hashCode(self) -> int: ...
    def intersects(self, interval: 'Interval') -> bool: ...
    def isAdjacentTo(self, interval: 'Interval') -> bool: ...
    @staticmethod
    def of(double: float, double2: float) -> 'Interval': ...
    def overlaps(self, interval: 'Interval') -> bool: ...
    @staticmethod
    def span(intervalArray: typing.List['Interval']) -> 'Interval': ...
    def toString(self) -> str: ...

class Operations:
    """
    public final class Operations extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Provides all needed methods to performs all supported operations on any value.
    """
    @staticmethod
    def abs(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function abs on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def absNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function abs on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @staticmethod
    def acos(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function acos on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def acosNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function acos on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def add(immutableValue: 'ImmutableValue', immutableValue2: 'ImmutableValue') -> 'Value':
        """
            Performs the addition of value1 by value2 and returns the result of the operation. The two value value1 and value2 are
            untouched by this operation.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the first operand of the operation
                value2 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Returns:
                the result of the addition of value1 by value2
        
            Performs the addition of value1 by value2 and returns the result of the operation. The two value value1 and value2 are
            untouched by this operation.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the first operand of the operation
                value2 (double): the second operand of the operation
        
            Returns:
                the result of the addition of value1 by value2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def add(immutableValue: 'ImmutableValue', double: float) -> 'Value': ...
    @typing.overload
    @staticmethod
    def addNoCopy(value: 'Value', immutableValue: 'ImmutableValue') -> None:
        """
            Adds value1 by value2. The value value1 is the result of the operation. The value value1 is modified by the operation
            while value2 remained untouched.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.Value`): the first operand of the operation that is modified by the operation
                value2 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation that is untouched by the operation
        
            Adds value1 by value2. The value value1 is the result of the operation. The value value1 is modified by the operation
            while value2 remained untouched.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.Value`): the first operand of the operation that is modified by the operation
                value2 (double): the second operand of the operation that is untouched by the operation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def addNoCopy(value: 'Value', double: float) -> None: ...
    @staticmethod
    def asin(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function asin on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def asinNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function asin on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @staticmethod
    def atan(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function atan on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def atanNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function atan on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @staticmethod
    def ceil(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function ceil on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def ceilNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function ceil on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @staticmethod
    def cos(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function cos on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def cosNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function cos on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def divide(immutableValue: 'ImmutableValue', immutableValue2: 'ImmutableValue') -> 'Value':
        """
            Performs the division of value1 by value2 and returns the result of the operation. The two value value1 and value2 are
            untouched by this operation.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the first operand of the operation
                value2 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Returns:
                the result of the division of value1 by value2
        
            Performs the division of value1 by value2 and returns the result of the operation. The two value value1 and value2 are
            untouched by this operation.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the first operand of the operation
                value2 (double): the second operand of the operation
        
            Returns:
                the result of the division of value1 by value2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def divide(immutableValue: 'ImmutableValue', double: float) -> 'Value': ...
    @typing.overload
    @staticmethod
    def divideNoCopy(value: 'Value', immutableValue: 'ImmutableValue') -> None:
        """
            Divides value1 by value2. The value value1 is the result of the operation. The value value1 is modified by the operation
            while value2 remained untouched.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.Value`): the first operand of the operation that is modified by the operation
                value2 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation that is untouched by the operation
        
            Divides value1 by value2. The value value1 is the result of the operation. The value value1 is modified by the operation
            while value2 remained untouched.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.Value`): the first operand of the operation that is modified by the operation
                value2 (double): the second operand of the operation that is untouched by the operation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def divideNoCopy(value: 'Value', double: float) -> None: ...
    @staticmethod
    def floor(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function floor on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def floorNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function floor on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @staticmethod
    def log(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function log on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def log10(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function log base 10 on the given value value1 and returns the result of the operation. The
            value value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def log10NoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function log base 10 on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @staticmethod
    def logNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function log on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @staticmethod
    def mathNoCopy(value: 'Value', string: str) -> None: ...
    @typing.overload
    @staticmethod
    def multiply(immutableValue: 'ImmutableValue', immutableValue2: 'ImmutableValue') -> 'Value':
        """
            Performs the multiplication of value1 by value2 and returns the result of the operation. The two value value1 and value2
            are untouched by this operation.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the first operand of the operation
                value2 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Returns:
                the result of the multiplication of value1 by value2
        
            Performs the multiplication of value1 by value2 and returns the result of the operation. The two value value1 and value2
            are untouched by this operation.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the first operand of the operation
                value2 (double): the second operand of the operation
        
            Returns:
                the result of the multiplication of value1 by value2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def multiply(immutableValue: 'ImmutableValue', double: float) -> 'Value': ...
    @typing.overload
    @staticmethod
    def multiplyNoCopy(value: 'Value', immutableValue: 'ImmutableValue') -> None:
        """
            Multiplies value1 by value2. The value value1 is the result of the operation. The value value1 is modified by the
            operation while value2 remained untouched.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.Value`): the first operand of the operation that is modified by the operation
                value2 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation that is untouched by the operation
        
            Multiplies value1 by value2. The value value1 is the result of the operation. The value value1 is modified by the
            operation while value2 remained untouched.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.Value`): the first operand of the operation that is modified by the operation
                value2 (double): the second operand of the operation that is untouched by the operation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def multiplyNoCopy(value: 'Value', double: float) -> None: ...
    @staticmethod
    def pow2(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function pow2 on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def pow2NoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function pow2 on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def power(immutableValue: 'ImmutableValue', immutableValue2: 'ImmutableValue') -> 'Value':
        """
            Performs the exponentiation of value1 by value2 and returns the result of the operation. The two value value1 and value2
            are untouched by this operation.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the first operand of the operation
                value2 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Returns:
                the result of the exponentiation of value1 by value2
        
            Performs the exponentiation of value1 by value2 and returns the result of the operation. The two value value1 and value2
            are untouched by this operation.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the first operand of the operation
                value2 (double): the second operand of the operation
        
            Returns:
                the result of the exponentiation of value1 by value2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def power(immutableValue: 'ImmutableValue', double: float) -> 'Value': ...
    @typing.overload
    @staticmethod
    def powerNoCopy(value: 'Value', immutableValue: 'ImmutableValue') -> None:
        """
            Exponentiates value1 by value2. The value value1 is the result of the operation. The value value1 is modified by the
            operation while value2 remained untouched.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.Value`): the first operand of the operation that is modified by the operation
                value2 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation that is untouched by the operation
        
            Exponentiates value1 by value2. The value value1 is the result of the operation. The value value1 is modified by the
            operation while value2 remained untouched.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.Value`): the first operand of the operation that is modified by the operation
                value2 (double): the second operand of the operation that is untouched by the operation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def powerNoCopy(value: 'Value', double: float) -> None: ...
    @staticmethod
    def rint(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function rint on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def rintNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function rint on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @staticmethod
    def round(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function round on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def roundNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function round on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @staticmethod
    def sin(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function sin on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def sinNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function sin on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @staticmethod
    def sqrt(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function sqrt on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def sqrtNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function sqrt on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def subtract(immutableValue: 'ImmutableValue', immutableValue2: 'ImmutableValue') -> 'Value':
        """
            Performs the subtraction of value1 by value2 and returns the result of the operation. The two value value1 and value2
            are untouched by this operation.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the first operand of the operation
                value2 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation
        
            Returns:
                the result of the subtraction of value1 by value2
        
            Performs the subtraction of value1 by value2 and returns the result of the operation. The two value value1 and value2
            are untouched by this operation.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the first operand of the operation
                value2 (double): the second operand of the operation
        
            Returns:
                the result of the subtraction of value1 by value2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def subtract(immutableValue: 'ImmutableValue', double: float) -> 'Value': ...
    @typing.overload
    @staticmethod
    def subtractNoCopy(value: 'Value', immutableValue: 'ImmutableValue') -> None:
        """
            Subtracts value1 by value2. The value value1 is the result of the operation. The value value1 is modified by the
            operation while value2 remained untouched.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.Value`): the first operand of the operation that is modified by the operation
                value2 (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand of the operation that is untouched by the operation
        
            Subtracts value1 by value2. The value value1 is the result of the operation. The value value1 is modified by the
            operation while value2 remained untouched.
        
            Parameters:
                value1 (:class:`~cern.accsoft.commons.value.Value`): the first operand of the operation that is modified by the operation
                value2 (double): the second operand of the operation that is untouched by the operation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def subtractNoCopy(value: 'Value', double: float) -> None: ...
    @staticmethod
    def tan(immutableValue: 'ImmutableValue') -> 'Value':
        """
            Applies the mathematical function tan on the given value value1 and returns the result of the operation. The value
            value1 is untouched by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the operand of the operation
        
            Returns:
                the result of the application of the math function on the value
        
        
        """
        ...
    @staticmethod
    def tanNoCopy(value: 'Value') -> None:
        """
            Applies the mathematical function tan on the given value. The value is modified by this operation.
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): the value on which to apply the mathematical function.
        
        
        """
        ...

class ParabolicSplineFunction(cern.accsoft.commons.value.spi.function.AbstractMathFunction):
    """
    public class ParabolicSplineFunction extends :class:`~cern.accsoft.commons.value.spi.function.AbstractMathFunction`
    
        Spline function that connects every pair of points using two parabolas rather than a cubic function. The function uses
        certain assumptions when calculating coefficients of these parabolas:
    
          - Gradient of the first and last point is 0
          - Gradient of a local extremum point is 0
          - Gradient of a flat part of the function is 0
    """
    def __init__(self, immutableDiscreteFunction: 'ImmutableDiscreteFunction'): ...
    def getFunction(self) -> 'ImmutableDiscreteFunction':
        """
            Returns the function for which the spline is calculated
        
            Returns:
                function passed to the constructor: :meth:`~cern.accsoft.commons.value.ParabolicSplineFunction.%3Cinit%3E`
        
        
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

class ScalarArrays:
    """
    public final class ScalarArrays extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    """
    @staticmethod
    def isContinueWith(immutableScalarArray: 'ImmutableScalarArray', immutableScalarArray2: 'ImmutableScalarArray', double: float) -> bool:
        """
            Returns true if the first array is continue with the second one taken into account the offset. To be continue means that
            the first value of the second array, shifted with the offset is the same as the last value of the first array. Note that
            equal is defined relative to a given precision defined in :code:`Values`.
        
            Parameters:
                scalarArray1 (:class:`~cern.accsoft.commons.value.ImmutableScalarArray`): the first array to test for continuity
                scalarArray2 (:class:`~cern.accsoft.commons.value.ImmutableScalarArray`): the second array to test for continuity with the first one
                offset (double): the offset of the given array
        
            Returns:
                true if this functino is continue with the given function.
        
        
        """
        ...

class Type(java.lang.Enum['Type'], cern.accsoft.commons.util.Named):
    """
    public enum Type extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.accsoft.commons.value.Type`> implements cern.accsoft.commons.util.Named
    
        A class implementing this interface represents an entity linked to the type of a value. A limited number of types are
        standardized.
    """
    FUNCTION: typing.ClassVar['Type'] = ...
    POINT: typing.ClassVar['Type'] = ...
    EXPRESSION_BASED_FUNCTION: typing.ClassVar['Type'] = ...
    FUNCTION_LIST: typing.ClassVar['Type'] = ...
    FUNCTIONS_ARRAY: typing.ClassVar['Type'] = ...
    POLYNOMIAL: typing.ClassVar['Type'] = ...
    BOUNDED_POLYNOMIAL: typing.ClassVar['Type'] = ...
    BOUNDED_POLYNOMIAL_SEQUENCE: typing.ClassVar['Type'] = ...
    BOOLEAN: typing.ClassVar['Type'] = ...
    BYTE: typing.ClassVar['Type'] = ...
    DOUBLE: typing.ClassVar['Type'] = ...
    FLOAT: typing.ClassVar['Type'] = ...
    LONG: typing.ClassVar['Type'] = ...
    INT: typing.ClassVar['Type'] = ...
    SHORT: typing.ClassVar['Type'] = ...
    STRING: typing.ClassVar['Type'] = ...
    TEXT_DOCUMENT: typing.ClassVar['Type'] = ...
    BOOLEAN_ARRAY: typing.ClassVar['Type'] = ...
    BYTE_ARRAY: typing.ClassVar['Type'] = ...
    DOUBLE_ARRAY: typing.ClassVar['Type'] = ...
    FLOAT_ARRAY: typing.ClassVar['Type'] = ...
    INT_ARRAY: typing.ClassVar['Type'] = ...
    LONG_ARRAY: typing.ClassVar['Type'] = ...
    SHORT_ARRAY: typing.ClassVar['Type'] = ...
    STRING_ARRAY: typing.ClassVar['Type'] = ...
    BOOLEAN_ARRAY_2D: typing.ClassVar['Type'] = ...
    BYTE_ARRAY_2D: typing.ClassVar['Type'] = ...
    DOUBLE_ARRAY_2D: typing.ClassVar['Type'] = ...
    FLOAT_ARRAY_2D: typing.ClassVar['Type'] = ...
    INT_ARRAY_2D: typing.ClassVar['Type'] = ...
    LONG_ARRAY_2D: typing.ClassVar['Type'] = ...
    SHORT_ARRAY_2D: typing.ClassVar['Type'] = ...
    STRING_ARRAY_2D: typing.ClassVar['Type'] = ...
    ENUM: typing.ClassVar['Type'] = ...
    ENUM_ARRAY: typing.ClassVar['Type'] = ...
    ENUM_ARRAY_2D: typing.ClassVar['Type'] = ...
    ENUM_SET: typing.ClassVar['Type'] = ...
    ENUM_SET_ARRAY: typing.ClassVar['Type'] = ...
    ENUM_SET_ARRAY_2D: typing.ClassVar['Type'] = ...
    UNDEFINED: typing.ClassVar['Type'] = ...
    @staticmethod
    def convertEnumTypeToPrimitiveType(type: 'Type', enumType: cern.japc.value.EnumType) -> 'Type':
        """
            Converts specified :meth:`~cern.accsoft.commons.value.Type.isEnumeric` into the corresponding primitive type. For
            :meth:`~cern.accsoft.commons.value.Type.ENUM` and :meth:`~cern.accsoft.commons.value.Type.ENUM_SET` the method returns
            scalar type, for :meth:`~cern.accsoft.commons.value.Type.ENUM_ARRAY` and
            :meth:`~cern.accsoft.commons.value.Type.ENUM_SET_ARRAY` the method returns scalar array type and for
            :meth:`~cern.accsoft.commons.value.Type.ENUM_ARRAY_2D` and :meth:`~cern.accsoft.commons.value.Type.ENUM_SET_ARRAY_2D` -
            the method returns scalar array 2D type. The actual value type (byte, short, int, long) is determined by the :code:`bit
            size` of the enum type.
        
            For example for :meth:`~cern.accsoft.commons.value.Type.ENUM` type that has :code:`EnumTypeBitSize.SHORT` bit size - the
            method returns :meth:`~cern.accsoft.commons.value.Type.SHORT`. For
            :meth:`~cern.accsoft.commons.value.Type.ENUM_SET_ARRAY` type that has :code:`EnumTypeBitSize.LONG` bit size - the method
            returns :meth:`~cern.accsoft.commons.value.Type.LONG_ARRAY`, etc..
        
            If the specified type is not :meth:`~cern.accsoft.commons.value.Type.isEnumeric` - the method returns directly the type
            without any conversion.
        
            Parameters:
                type (:class:`~cern.accsoft.commons.value.Type`): the enumeric type to be converted
                enumType (cern.japc.value.EnumType): enumeration type that is necessary to determine :code:`bit size`. If the :code:`type` is not enumeric - this argument is
                    ignored (can be :code:`null`).
        
            Returns:
                corresponding primitive type
        
        
        """
        ...
    @staticmethod
    def convertToArray2DType(type: 'Type') -> 'Type':
        """
            Returns corresponding ARRAY_2D type for the given scalar type e.g. Type.DOUBLE_ARRAY_2D for Type.DOUBLE
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): the scalar type
        
            Returns:
                corresponding ARRAY_2D type
        
            Raises:
                : if the specified type is not a scalar type
        
        
        """
        ...
    @staticmethod
    def convertToArrayType(type: 'Type') -> 'Type':
        """
            Returns corresponding array type for the given scalar type e.g. Type.DOUBLE_ARRAY for Type.DOUBLE
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): the scalar type
        
            Returns:
                corresponding array type
        
            Raises:
                : if the specified type is not a scalar type
        
        
        """
        ...
    @staticmethod
    def convertToScalarType(type: 'Type') -> 'Type': ...
    def getName(self) -> str:
        """
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
        
        """
        ...
    @staticmethod
    def getObjectType(object: typing.Any) -> 'Type': ...
    def isArray(self) -> bool: ...
    def isArray2D(self) -> bool: ...
    @staticmethod
    def isBooleanType(type: 'Type') -> bool:
        """
            Return :code:`true` if Type is one of the supported boolean types.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): Type to be verified
        
            Returns:
                :code:`true` if Type is one of the supported boolean types e.g. BOOLEAN, BOOLEAN_ARRAY or BOOLEAN_ARRAY_2D
        
        
        """
        ...
    def isDiscrete(self) -> bool:
        """
            Returns :code:`true` if this Type represents a discrete type - scalar, scalar array or scalar array 2D.
        
        """
        ...
    @staticmethod
    def isDiscreteType(type: 'Type') -> bool:
        """
            Returns :code:`true` if Type represents a discrete type - scalar, scalar array or scalar array 2D.
        
        """
        ...
    def isEnum(self) -> bool:
        """
            Returns :code:`true` if this type is one of: ENUM, ENUM_ARRAY, ENUM_ARRAY_2D.
        
        """
        ...
    def isEnumSet(self) -> bool:
        """
            Returns :code:`true` if this type is one of: ENUM_SET, ENUM_SET_ARRAY, ENUM_SET_ARRAY_2D.
        
        """
        ...
    @staticmethod
    def isEnumSetType(type: 'Type') -> bool:
        """
            Returns :code:`true` if this type is one of: ENUM_SET, ENUM_SET_ARRAY, ENUM_SET_ARRAY_2D.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): Type to be verified
        
            Also see:
                :meth:`~cern.accsoft.commons.value.Type.isEnumType`
        
        
        """
        ...
    @staticmethod
    def isEnumType(type: 'Type') -> bool:
        """
            Return :code:`true` if the specified type is one of: ENUM, ENUM_ARRAY, ENUM_ARRAY_2D
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): Type to be verified
        
            Also see:
                :meth:`~cern.accsoft.commons.value.Type.isEnumSetType`
        
        
        """
        ...
    def isEnumeric(self) -> bool:
        """
            Returns :code:`true` if this type is any of: ENUM, ENUM_ARRAY, ENUM_ARRAY_2D, ENUM_SET, ENUM_SET_ARRAY,
            ENUM_SET_ARRAY_2D
        
        """
        ...
    @staticmethod
    def isEnumericType(type: 'Type') -> bool:
        """
            Returns :code:`true` if the specified type is any of: ENUM, ENUM_ARRAY, ENUM_ARRAY_2D, ENUM_SET, ENUM_SET_ARRAY,
            ENUM_SET_ARRAY_2D.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): type to be verified
        
        
        """
        ...
    @staticmethod
    def isFloatingType(type: 'Type') -> bool:
        """
            Returns :code:`true` if the given type is one of: :meth:`~cern.accsoft.commons.value.Type.DOUBLE`,
            :meth:`~cern.accsoft.commons.value.Type.DOUBLE_ARRAY`, :meth:`~cern.accsoft.commons.value.Type.DOUBLE_ARRAY_2D`,
            :meth:`~cern.accsoft.commons.value.Type.FLOAT`, :meth:`~cern.accsoft.commons.value.Type.FLOAT_ARRAY`,
            :meth:`~cern.accsoft.commons.value.Type.FLOAT_ARRAY_2D`, :meth:`~cern.accsoft.commons.value.Type.FUNCTION` or
            :meth:`~cern.accsoft.commons.value.Type.FUNCTION_LIST`.
        
            Note that :code:`FUNCTION` and :code:`FUNCTION_LIST` and :code:`FUNCTIONS_ARRAY` are also considered as floating type
            since both X and Y coordinates are of type :code:`DOUBLE`.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): type to be checked
        
            Returns:
                :code:`true` if the given type represents a floating point type
        
        
        """
        ...
    def isFunction(self) -> bool:
        """
            Returns :code:`true` if this Type represents a function type - function, function list, point or expression based
            function.
        
        """
        ...
    def isFunctionList(self) -> bool:
        """
            Returns :code:`true` if this Type represents a function list type. based function.
        
        """
        ...
    @staticmethod
    def isFunctionListType(type: 'Type') -> bool:
        """
            Return :code:`true` if Type is one of the supported function list types.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): Type to be verified
        
            Returns:
                :code:`true` if Type is one of the supported function types e.g. FUNCTION_LIST
        
        
        """
        ...
    @staticmethod
    def isFunctionType(type: 'Type') -> bool:
        """
            Return :code:`true` if Type is one of the supported function types.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): Type to be verified
        
            Returns:
                :code:`true` if Type is one of the supported function types e.g. FUNCTION, FUNCTION_LIST, POINT or
                EXPRESSION_BASED_FUNCTION
        
        
        """
        ...
    def isFunctionsArray(self) -> bool:
        """
            Returns :code:`true` if this Type represents a function array type.
        
        """
        ...
    @staticmethod
    def isFunctionsArrayType(type: 'Type') -> bool:
        """
            Return :code:`true` if Type is one of the supported functions array type.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): Type to be verified
        
            Returns:
                :code:`true` if Type is one of the supported function types e.g. FUNCTIONS_ARRAY
        
        
        """
        ...
    @staticmethod
    def isNumberArray2DType(type: 'Type') -> bool:
        """
            Returns true if the given type is a number array 2d type, e.g. DOUBLE_ARRAY_2D, FLOAT_ARRAY_2D, INT_ARRAY_2D,
            LONG_ARRAY_2D, SHORT_ARRAY_2D or BYTE_ARRAY_2D
        
            Parameters:
                valueType (:class:`~cern.accsoft.commons.value.Type`): the type to be checked
        
            Returns:
                :code:`true` if the given type is a number array 2d array type. If the parameter is :code:`null` it returns
                :code:`false`.
        
        
        """
        ...
    @staticmethod
    def isNumberArrayType(type: 'Type') -> bool:
        """
            Returns true if the given type is a number array type, e.g. DOUBLE_ARRAY, FLOAT_ARRAY, INT_ARRAY, LONG_ARRAY,
            SHORT_ARRAY or BYTE_ARRAY
        
            Parameters:
                valueType (:class:`~cern.accsoft.commons.value.Type`): the type to be checked
        
            Returns:
                :code:`true` if the given type is a number array type. If the parameter is :code:`null` it returns :code:`false`.
        
        
        """
        ...
    @staticmethod
    def isNumberType(type: 'Type') -> bool:
        """
            Returns :code:`true` if the given type is a number type, e.g. DOUBLE, FLOAT, INT, LONG, SHORT or BYTE
        
            Parameters:
                valueType (:class:`~cern.accsoft.commons.value.Type`): the type to be checked
        
            Returns:
                :code:`true` if the given type is a number type. If the parameter is :code:`null` it returns :code:`false`.
        
        
        """
        ...
    def isScalar(self) -> bool:
        """
            Returns :code:`true` if this Type represents a scalar type i.e. DOUBLE, FLOAT, LONG, SHORT, INT, BYTE, BOOLEAN, STRING,
            ENUM or ENUM_SET.
        
        """
        ...
    @staticmethod
    def isScalarArray2DType(type: 'Type') -> bool:
        """
            Return :code:`true` if Type is one of the supported scalar array 2d types.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): Type to be verified
        
            Returns:
                :code:`true` if Type is one of the supported scalar array 2d types e.g. DOUBLE_ARRAY_2D, FLOAT_ARRAY_2D, LONG_ARRAY_2D,
                etc.
        
        
        """
        ...
    @staticmethod
    def isScalarArrayType(type: 'Type') -> bool:
        """
            Return :code:`true` if Type is one of the supported scalar array types.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): Type to be verified
        
            Returns:
                :code:`true` if Type is one of the supported scalar array types e.g. DOUBLE_ARRAY, FLOAT_ARRAY, LONG_ARRAY, etc.
        
        
        """
        ...
    @staticmethod
    def isScalarType(type: 'Type') -> bool:
        """
            Return :code:`true` if Type is one of the supported scalar types.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): Type to be verified
        
            Returns:
                :code:`true` if Type is one of the supported scalar types e.g. DOUBLE, FLOAT, LONG, SHORT, INT, BYTE, BOOLEAN, STRING,
                ENUM, ENUM_SET
        
        
        """
        ...
    @staticmethod
    def isStringType(type: 'Type') -> bool:
        """
            Return :code:`true` if Type is one of the supported string types.
        
            Parameters:
                t (:class:`~cern.accsoft.commons.value.Type`): Type to be verified
        
            Returns:
                :code:`true` if Type is one of the supported string types e.g. STRING, STRING_ARRAY or STRING_ARRAY_2D
        
        
        """
        ...
    _valueOf_2__T = typing.TypeVar('_valueOf_2__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(valueType: cern.japc.value.ValueType) -> 'Type':
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
        
            Converts JAPC :code:`ValueType` into the accsoft-commons-value :code:`Type` enum.
        
            Parameters:
                valueType (cern.japc.value.ValueType): type to be converted
        
            Returns:
                corresponding :code:`Type`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Type': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_2__T], string: str) -> _valueOf_2__T: ...
    @staticmethod
    def values() -> typing.List['Type']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (Type c : Type.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Typed:
    """
    public interface Typed
    """
    def getType(self) -> Type:
        """
            Returns the type of this value
        
            Returns:
                the type of this value
        
        
        """
        ...

class ValueDescriptor(java.io.Serializable, java.lang.Cloneable):
    """
    public interface ValueDescriptor extends `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Provides additional (meta) information about the associated value like min and max value, precision or enumeration
        definition.
    """
    def clone(self) -> 'ValueDescriptor':
        """
            Publicly available clone method
        
            Returns:
                a cloned copy of this instance
        
        
        """
        ...
    def containsMeanings(self) -> bool:
        """
            Returns :code:`true` if at least one meaning is defined.
        
        """
        ...
    def getAbsoluteTolerance(self) -> float:
        """
        
            Returns:
                absolute tolerance used when comparing value
        
        
        """
        ...
    def getBooleanType(self) -> cern.japc.value.BooleanType:
        """
            Returns corresponding :code:`BooleanType` if the associated value represents a boolean.
        
            Returns:
                :code:`BooleanType` or :code:`null` if the associated value doesn't represent a boolean
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
            Information about dimensions of array for 1d arrays this returns the number of elements for 2d arrays this returns the
            number of columns If value is not an array null is returned This method was formerly named getDim1()
        
        """
        ...
    def getEnumType(self) -> cern.japc.value.EnumType:
        """
            Returns corresponding :code:`EnumType` if the associated value represents an enumeration.
        
            Returns:
                :code:`EnumType` or :code:`null` if the associated value doesn't represent an enumeration
        
        
        """
        ...
    def getMax(self) -> float:
        """
            Returns the maximal possible value, if it is not set returns null
        
            Returns:
                maximal possible value
        
        
        """
        ...
    def getMeaning(self, object: typing.Any) -> cern.japc.value.SimpleValueStandardMeaning:
        """
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value of the parameter (ex. int, String[] , :code:`EnumItem`, etc.)
        
            Returns:
                the meaning of the value of :code:`null` if the meaning is not defined
        
            Raises:
                : if the value is not compatible with the parameter
        
        
        """
        ...
    def getMin(self) -> float:
        """
            Returns the minimal possible value, if it is not set returns null
        
            Returns:
                minimal possible value
        
        
        """
        ...
    def getRelativeTolerance(self) -> float:
        """
        
            Returns:
                relative tolerance used when comparing value
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
            Information about dimensions of array for 1d arrays this returns null for 2d arrays this returns the number of rows If
            value is not an array null is returned This method was formerly named getDim2()
        
        """
        ...
    def getUnit(self) -> str:
        """
            Returns the unit of the values (if available) or empty string if not set.
        
            Returns:
                The unit as a string or empty string if not set.
        
        
        """
        ...
    def getXPrecision(self) -> int:
        """
            Defines precision of X coordinates if the associated parameter is a function.
        
            Returns:
                precision of function X coordinates (if defined), or :code:`null`
        
        
        """
        ...
    def getXUnit(self) -> str:
        """
            Returns the unit of the x values (if available) or empty string if not set.
        
            Returns:
                The unit as a string or empty string if not set.
        
        
        """
        ...
    def getYPrecision(self) -> int:
        """
            Returns precision of Y coordinates if the associated value represents a function. The Y precision is also used for
            scalars and arrays of scalars.
        
            Returns:
                precision of Y coordinates (if defined) or :code:`null`
        
        
        """
        ...
    def getYUnit(self) -> str:
        """
            Returns the unit of the y values (if available) or empty string if not set.
        
            Returns:
                The unit as a string or empty string if not set.
        
        
        """
        ...
    def isSettable(self, object: typing.Any) -> bool:
        """
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value of the parameter (ex. int, String[] , :code:`EnumItem`, etc.)
        
            Returns:
                :code:`true` if this value is settable
        
            Raises:
                : if the value is not compatible with the parameter
        
        
        """
        ...
    class ValueCompareType(java.lang.Enum['ValueDescriptor.ValueCompareType']):
        EXACT_MEANING: typing.ClassVar['ValueDescriptor.ValueCompareType'] = ...
        TOL_REL: typing.ClassVar['ValueDescriptor.ValueCompareType'] = ...
        TOL_ABS: typing.ClassVar['ValueDescriptor.ValueCompareType'] = ...
        EXACT_WITH_RES: typing.ClassVar['ValueDescriptor.ValueCompareType'] = ...
        EXACT: typing.ClassVar['ValueDescriptor.ValueCompareType'] = ...
        TOL_ABS_REL: typing.ClassVar['ValueDescriptor.ValueCompareType'] = ...
        TOL_ABS_MOD360: typing.ClassVar['ValueDescriptor.ValueCompareType'] = ...
        NONE: typing.ClassVar['ValueDescriptor.ValueCompareType'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ValueDescriptor.ValueCompareType': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.List['ValueDescriptor.ValueCompareType']: ...

class ValueFactory:
    @staticmethod
    def convertToDiscreteFunction(immutableScalarArray: 'ImmutableScalarArray') -> 'DiscreteFunction': ...
    @staticmethod
    def createConstantFunction(double: float, double2: float) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createDiscreteFunctionList() -> 'DiscreteFunctionList': ...
    @typing.overload
    @staticmethod
    def createDiscreteFunctionList(immutableDiscreteFunctionArray: typing.List['ImmutableDiscreteFunction']) -> 'DiscreteFunctionList': ...
    @typing.overload
    @staticmethod
    def createDiscreteFunctionList(doubleArray: typing.List[float], doubleArray2: typing.List[float], intArray: typing.List[int]) -> 'DiscreteFunctionList': ...
    @typing.overload
    @staticmethod
    def createDiscreteFunctionsArray() -> 'DiscreteFunctionsArray': ...
    @typing.overload
    @staticmethod
    def createDiscreteFunctionsArray(immutableDiscreteFunctionArray: typing.List['ImmutableDiscreteFunction']) -> 'DiscreteFunctionsArray': ...
    @typing.overload
    @staticmethod
    def createFunction(immutablePointArray: typing.List['ImmutablePoint']) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createFunction(immutableValue: 'ImmutableValue') -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createFunction(interpolable: Interpolable, double: float, int2: int, double2: float, double3: float) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createFunction(interpolable: Interpolable, doubleArray: typing.List[float]) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createFunction(interpolable: Interpolable, int2: int, double: float, double2: float) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createFunction(interpolable: Interpolable, double: float, int2: int, double2: float, double3: float, integer: int, double4: float, double5: float) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createFunction(pointArray: typing.List['Point']) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createFunction(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createFunction(doubleArray: typing.List[float], doubleArray2: typing.List[float], boolean: bool) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createFunction(intArray: typing.List[int], doubleArray: typing.List[float]) -> 'DiscreteFunction': ...
    @typing.overload
    @staticmethod
    def createFunction(string: str) -> cern.accsoft.commons.value.spi.function.ExpressionBasedFunction: ...
    @staticmethod
    def createLinearBoundedPolynomialSequence(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> 'BoundedPolynomialSequence': ...
    @typing.overload
    @staticmethod
    def createMonomial(int: int) -> 'Polynomial': ...
    @typing.overload
    @staticmethod
    def createMonomial(int: int, double: float) -> 'Polynomial': ...
    @typing.overload
    @staticmethod
    def createPoint(immutableValue: 'ImmutableValue') -> 'Point': ...
    @typing.overload
    @staticmethod
    def createPoint(double: float, double2: float) -> 'Point': ...
    @typing.overload
    @staticmethod
    def createPolynomial(doubleArray: typing.List[float]) -> 'Polynomial': ...
    @typing.overload
    @staticmethod
    def createPolynomial(collection: typing.Union[java.util.Collection[float], typing.Sequence[float]]) -> 'Polynomial': ...
    @typing.overload
    @staticmethod
    def createPolynomial(sortedMap: java.util.SortedMap[int, float]) -> 'Polynomial': ...
    @typing.overload
    @staticmethod
    def createScalar(boolean: bool) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(byte: int) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(type: Type) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(type: Type, valueDescriptor: ValueDescriptor, object: typing.Any) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(type: Type, object: typing.Any) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(valueDescriptor: ValueDescriptor, object: typing.Any) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(double: float) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(double: float, type: Type) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(float: float) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(int: int) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(object: typing.Any) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(string: str) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(long: int) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(long: int, type: Type) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalar(short: int) -> 'Scalar': ...
    @typing.overload
    @staticmethod
    def createScalarArray(immutableValue: 'ImmutableValue') -> 'ScalarArray': ...
    @typing.overload
    @staticmethod
    def createScalarArray(valueArray: typing.List['Value']) -> 'ScalarArray': ...
    @typing.overload
    @staticmethod
    def createScalarArray(object: typing.Any) -> 'ScalarArray': ...
    @typing.overload
    @staticmethod
    def createScalarArray(object: typing.Any, type: Type) -> 'ScalarArray': ...
    @typing.overload
    @staticmethod
    def createScalarArray2D(immutableValue: 'ImmutableValue') -> 'ScalarArray2D': ...
    @typing.overload
    @staticmethod
    def createScalarArray2D(object: typing.Any, int: int, int2: int) -> 'ScalarArray2D': ...
    @typing.overload
    @staticmethod
    def createScalarArray2D(object: typing.Any, int: int, int2: int, type: Type) -> 'ScalarArray2D': ...
    @staticmethod
    def createScalarFunction(double: float) -> 'DiscreteFunction': ...
    @staticmethod
    def createZeroFunction(double: float) -> 'DiscreteFunction': ...

class Values:
    DEFAULT_DOUBLE_PRECISION: typing.ClassVar[float] = ...
    INFINITE_PRECISION: typing.ClassVar[float] = ...
    doublePrecision: typing.ClassVar[float] = ...
    @typing.overload
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(immutableValue: 'ImmutableValue', immutableValue2: 'ImmutableValue') -> bool: ...
    @typing.overload
    @staticmethod
    def equals(double: float, double2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equals(double: float, double2: float, double3: float) -> bool: ...
    @staticmethod
    def getDisplayValue(immutableValue: 'ImmutableValue') -> str: ...
    @staticmethod
    def getPrecision() -> float: ...
    @staticmethod
    def hasAllowedValue(immutableScalar: 'ImmutableScalar') -> bool: ...
    @staticmethod
    def isInLimits(immutableValue: 'ImmutableValue') -> bool: ...
    @staticmethod
    def isZero(double: float) -> bool: ...
    @typing.overload
    @staticmethod
    def round(double: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def round(doubleArray: typing.List[float], int: int) -> typing.List[float]: ...
    @typing.overload
    @staticmethod
    def round(float: float, int: int) -> float: ...
    @typing.overload
    @staticmethod
    def round(floatArray: typing.List[float], int: int) -> typing.List[float]: ...
    @staticmethod
    def roundArray(immutableScalarArray: 'ImmutableScalarArray', int: int) -> 'ImmutableScalarArray': ...
    @staticmethod
    def roundFunction(immutableDiscreteFunction: 'ImmutableDiscreteFunction', integer: int, integer2: int) -> 'ImmutableDiscreteFunction': ...
    @staticmethod
    def roundFunctionList(immutableDiscreteFunctionList: 'ImmutableDiscreteFunctionList', integer: int, integer2: int) -> 'ImmutableValue': ...
    @staticmethod
    def roundFunctionsArray(immutableDiscreteFunctionsArray: 'ImmutableDiscreteFunctionsArray', integer: int, integer2: int) -> 'ImmutableValue': ...
    @staticmethod
    def roundScalar(immutableScalar: 'ImmutableScalar', int: int) -> 'ImmutableScalar': ...
    @staticmethod
    def roundValue(immutableValue: 'ImmutableValue') -> 'ImmutableValue': ...
    @staticmethod
    def setPrecision(double: float) -> None: ...

class Function(Typed):
    """
    public interface Function extends :class:`~cern.accsoft.commons.value.Typed`
    
        Defines an immutable function that is discrete or continue.
    """
    def isDiscrete(self) -> bool:
        """
            Returns true is this function is a discrete function defined with a list of points. If false one can assume that this
            function is defined with a mathematical formula and does not hold any particular point.
        
            Returns:
                true is this function is a discrete function.
        
        
        """
        ...

class ImmutableValue(java.lang.Cloneable, java.io.Serializable, Typed):
    """
    public interface ImmutableValue extends `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, :class:`~cern.accsoft.commons.value.Typed`
    
        Defines the concept of ImmutableValue that is a cloneable and serializable entity.
    """
    def clone(self) -> typing.Any:
        """
            Performs a deep copy of this value
        
            Returns:
                a deep copy of this value
        
        
        """
        ...
    def getString(self) -> str: ...
    def getValueDescriptor(self) -> ValueDescriptor:
        """
            Get descriptor for this value. Descriptor describes specific properties of value such as minimal, maximal value,
            precision and possible values represented by enumeration.
        
            Returns:
                value descriptor
        
        
        """
        ...
    def isDefined(self) -> bool:
        """
            If in moment of creation (retrieving from data base) the value for ImmutableValue cannot be specified this flag is set
            to false. This flag is set by default to true.
        
            Returns:
                :code:`true` by default or :code:`false` when value is not defined
        
        
        """
        ...
    def makeMutable(self) -> 'Value':
        """
            Returns a mutable version of this immutable value. The mutable version is made by performing a deep copy of this value.
            The runtime type of the value is preserved by this operation. The resulting value can be cast in the mutable type
            corresponding to the immutable type of this value.
        
            Returns:
                a mutable deep copy of this value
        
        
        """
        ...

class ContinuousFunction(Function):
    """
    public interface ContinuousFunction extends :class:`~cern.accsoft.commons.value.Function`
    
        interface to define a function of many arguments. currently only real arguments are supported :(, no mixing between
        booleans, arrays and that kind of things, only algebraic functions which operate on doubles
    """
    _evaluate__T = typing.TypeVar('_evaluate__T', bound='Value')  # <T>
    def evaluate(self, valueMap: cern.accsoft.commons.value.expression.ValueMap, list: java.util.List[_evaluate__T]) -> _evaluate__T: ...

class ImmutableDiscreteFunctionsArray(ImmutableValue):
    """
    public interface ImmutableDiscreteFunctionsArray extends :class:`~cern.accsoft.commons.value.ImmutableValue`
    
        Defines an immutable array of functions (:class:`~cern.accsoft.commons.value.ImmutableDiscreteFunction`). All functions
        are expected to have the same length.
    """
    def getFunction(self, int: int) -> 'ImmutableDiscreteFunction':
        """
            Return the function of the given index or null, if the index is out of the range of the function array.
        
            Parameters:
                index (int): the function index
        
            Returns:
                the function at the given index
        
        
        """
        ...
    def getFunctions(self) -> typing.List['ImmutableDiscreteFunction']:
        """
            Return the function array
        
            Returns:
                the array of functions
        
        
        """
        ...
    def getFunctionsCount(self) -> int:
        """
            Size of the functions array.
        
            Returns:
                the length of the array
        
        
        """
        ...
    def getYs(self, double: float) -> typing.List[float]:
        """
            Returns an array of the y-coordinates at the given x value.
        
            Parameters:
                x (double): the x-coordinate of the y-coordinates to return
        
            Returns:
                the y-coordinates at the given x-coordinate
        
        
        """
        ...
    def makeMutable(self) -> 'DiscreteFunctionsArray':
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
    def subView(self, double: float, double2: float) -> 'ImmutableDiscreteFunctionsArray':
        """
            Returns a sub view of the whole functions array.
        
            Parameters:
                fromX (double): the first x-coordinate of the view to return (inclusive)
                toX (double): the last x-coordinate of the view to return (inclusive)
        
            Returns:
                the view on the discrete function as defined by fromX and toX and the above rules.
        
        
        """
        ...
    def toXArray(self) -> typing.List[float]:
        """
            Returns all union of all x-coordinates for all functions (the index goes from 0 to length-1). The array returned is a
            copy of the internal representation. Any modification of this array does not affect this function.
        
            Returns:
                the union of all x-coordinates of all functions
        
        
        """
        ...

class ImmutableScalar(ImmutableValue):
    """
    public interface ImmutableScalar extends :class:`~cern.accsoft.commons.value.ImmutableValue`
    
        Defines a Value that is an immutable scalars.
    """
    def getBoolean(self) -> bool:
        """
            Returns the value being interpreted as a boolean. If the value is an array only the first value of the array is
            returned.
        
            Returns:
                the value being interpreted as a boolean.
        
        
        """
        ...
    def getByte(self) -> int:
        """
            Returns the value being interpreted as a byte. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a byte.
        
        
        """
        ...
    def getDouble(self) -> float:
        """
            Returns the value being interpreted as a double. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a double.
        
        
        """
        ...
    def getFloat(self) -> float:
        """
            Returns the value being interpreted as a float. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a float.
        
        
        """
        ...
    def getInt(self) -> int:
        """
            Returns the value being interpreted as a int. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a int.
        
        
        """
        ...
    def getLong(self) -> int:
        """
            Returns the value being interpreted as a long. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a long.
        
        
        """
        ...
    def getObject(self) -> typing.Any:
        """
            Returns the value as an object. This method returns the scalar type in their wrapping Object type and arrays and string
            without change.
        
            Returns:
                the value as an object.
        
        
        """
        ...
    def getShort(self) -> int:
        """
            Returns the value being interpreted as a short. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a short.
        
        
        """
        ...
    def makeMutable(self) -> 'Scalar':
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
    def toSimpleParameterValue(self) -> cern.japc.value.SimpleParameterValue:
        """
            Converts this scalar into a JAPC SimpleParameterValue.
        
            Returns:
                JAPC simple parameter value
        
        
        """
        ...

class MathFunction(Function, Interpolable):
    """
    public interface MathFunction extends :class:`~cern.accsoft.commons.value.Function`, :class:`~cern.accsoft.commons.value.Interpolable`
    
        Represents a mathematical function.
    """
    ...

class Value(ImmutableValue):
    """
    public interface Value extends :class:`~cern.accsoft.commons.value.ImmutableValue`
    
        Defines the concept of Value that is a cloneable entity on which one can apply operations.
    """
    @typing.overload
    def execute(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, immutableValue: ImmutableValue) -> None:
        """
            Performs the operation on this value with the given value as second operand. This value is changed by the operation.
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.BinaryOperation`): the operation to perform
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand for the binary operation
        
        
        """
        ...
    @typing.overload
    def execute(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation) -> None:
        """
            Performs the given operation on this value. This value is changed by the operation.
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.UnaryOperation`): the operation to perform
        
        """
        ...
    def setDefined(self, boolean: bool) -> None: ...
    def setValueDescriptor(self, valueDescriptor: ValueDescriptor) -> None: ...

class BoundedPolynomialSequence(MathFunction, Value):
    """
    public interface BoundedPolynomialSequence extends :class:`~cern.accsoft.commons.value.MathFunction`, :class:`~cern.accsoft.commons.value.Value`
    
        Stores always relative :class:`~cern.accsoft.commons.value.Polynomial`, where the coefficients are defined with respect
        to the lower boundaries of the interval, i.e. the polynomial :code:`p[n]` should be evaluated as
        :code:`p[n].interpolate(x - b)`, where :code:`b` is the lower bound.
    """
    def getBoundedPolynomials(self) -> typing.List['BoundedPolynomial']:
        """
        
            Returns:
                all :class:`~cern.accsoft.commons.value.BoundedPolynomial` contained in this
                :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence`
        
        
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
                the interpolated value of the :class:`~cern.accsoft.commons.value.BoundedPolynomialSequence` if one of the
                :class:`~cern.accsoft.commons.value.Interval` of the :class:`~cern.accsoft.commons.value.BoundedPolynomial` contains
                :code:`x` or `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Double.html?is-external=true#NaN>` if
                no :class:`~cern.accsoft.commons.value.Interval` contains :code:`x`.
        
            Also see:
                :meth:`~cern.accsoft.commons.value.BoundedPolynomial.interpolate`,
                :meth:`~cern.accsoft.commons.value.Interpolable.interpolate`
        
        
        """
        ...

class DiscreteFunctionsArray(ImmutableDiscreteFunctionsArray, Value):
    def getFunction(self, int: int) -> 'DiscreteFunction': ...
    def getFunctions(self) -> typing.List['DiscreteFunction']: ...
    @typing.overload
    def insert(self, double: float) -> bool: ...
    @typing.overload
    def insert(self, int: int, double: float) -> bool: ...
    @typing.overload
    def insert(self, int: int, double: float, double2: float) -> bool: ...
    @typing.overload
    def insertAll(self, doubleArray: typing.List[float]) -> int: ...
    @typing.overload
    def insertAll(self, int: int, immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> int: ...
    @typing.overload
    def insertAll(self, int: int, doubleArray: typing.List[float]) -> int: ...
    @typing.overload
    def remove(self, double: float) -> bool: ...
    @typing.overload
    def remove(self, int: int, double: float) -> bool: ...
    @typing.overload
    def removeAll(self, doubleArray: typing.List[float]) -> int: ...
    @typing.overload
    def removeAll(self, int: int, doubleArray: typing.List[float]) -> int: ...
    def retainAll(self, int: int, immutableDiscreteFunction: 'ImmutableDiscreteFunction', double: float) -> int: ...
    def setY(self, int: int, int2: int, double: float) -> None: ...
    @typing.overload
    def subView(self, int: int, double: float, double2: float) -> 'DiscreteFunction': ...
    @typing.overload
    def subView(self, double: float, double2: float) -> 'DiscreteFunctionsArray': ...
    @typing.overload
    def translate(self, double: float) -> None: ...
    @typing.overload
    def translate(self, int: int, double: float) -> None: ...

class ImmutableDiscreteFunction(Function, ImmutableScalar, Interpolable):
    def getLength(self) -> float: ...
    def getX(self, int: int) -> float: ...
    def getY(self, int: int) -> float: ...
    def indexOf(self, double: float) -> int: ...
    def makeMutable(self) -> 'DiscreteFunction': ...
    def size(self) -> int: ...
    def subFunction(self, double: float, double2: float) -> 'DiscreteFunction': ...
    @typing.overload
    def toPointArray(self) -> typing.List['ImmutablePoint']: ...
    @typing.overload
    def toPointArray(self, immutablePointArray: typing.List['ImmutablePoint']) -> typing.List['ImmutablePoint']: ...
    def toScalarArray2D(self) -> 'ScalarArray2D': ...
    def toXArray(self) -> typing.List[float]: ...
    def toYArray(self) -> typing.List[float]: ...

class ImmutablePoint(ImmutableScalar):
    """
    public interface ImmutablePoint extends :class:`~cern.accsoft.commons.value.ImmutableScalar`
    
        A ImmutablePoint is a ImmutableConstant where the value is the y-coordinate. The x-coordinate is an additional
        information.
    """
    def getX(self) -> float:
        """
            Returns the x-coordinates of the point.
        
            Returns:
                the x-coordinates of the point.
        
        
        """
        ...
    def getY(self) -> float:
        """
            Returns the y-coordinates of the point that matched the value of the scalars.
        
            Returns:
                the y-coordinates of the point that matched the value of the scalars.
        
            Also see:
                :code:`ImmutableScalar#get()`
        
        
        """
        ...
    def makeMutable(self) -> 'Point':
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`
            Returns a mutable version of this immutable value. The mutable version is made by performing a deep copy of this value.
            The runtime type of the value is preserved by this operation. The resulting value can be cast in the mutable type
            corresponding to the immutable type of this value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Returns:
                a mutable deep copy of this value
        
        
        """
        ...

class ImmutableScalarArray(ImmutableScalar):
    """
    public interface ImmutableScalarArray extends :class:`~cern.accsoft.commons.value.ImmutableScalar`
    
        Define an immutable array of scalars
    
        Note that a scalar array is a scalar. That means that is it possible by extension, to use a scalar array where a scalar
        would be used. In this case, the value of a scalar array taken as a scalar is its first value. If the scalar array is
        empty, the value is Double.NaN.
    """
    def getArray2D(self) -> cern.japc.value.Array2D:
        """
            Returns a wrapper around the value being interpreted as a 2d array. If the value is a 1d array it is encapsulated in an
            array of size 1xn. If the value is not an array it is encapsulated in an array of size 1x1. IMPORTANT: if the value is
            mutable and is changed after the wrapper is got the wrapper becomes invalide and can return wrong values or even throw
            OutOfBoundException.
        
            Returns:
                the value being interpreted as a boolean 2d array.
        
        
        """
        ...
    @typing.overload
    def getBoolean(self) -> bool: ...
    @typing.overload
    def getBoolean(self, int: int) -> bool:
        """
            Returns the value being interpreted as a boolean. The value returned is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getBooleans(self) -> typing.List[bool]:
        """
            Returns the value being interpreted as a boolean array. The array returned is not linked to the underlying array stored
            in this value. Only in the case this value is of type boolean array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Returns:
                the value being interpreted as a boolean array.
        
        """
        ...
    @typing.overload
    def getBooleans(self, int: int, int2: int) -> typing.List[bool]:
        """
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a boolean array.
        
        
        """
        ...
    @typing.overload
    def getByte(self) -> int: ...
    @typing.overload
    def getByte(self, int: int) -> int:
        """
            Returns the value being interpreted as a byte. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getBytes(self) -> typing.List[int]:
        """
            Returns the value being interpreted as a byte array. The array returned is not linked to the underlying array stored in
            this value. Only in the case this value is of type byte array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Returns:
                the value being interpreted as a byte array.
        
        """
        ...
    @typing.overload
    def getBytes(self, int: int, int2: int) -> typing.List[int]:
        """
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a byte array.
        
        
        """
        ...
    @typing.overload
    def getDouble(self) -> float: ...
    @typing.overload
    def getDouble(self, int: int) -> float:
        """
            Returns the value being interpreted as a double. The value returned is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getDoubles(self) -> typing.List[float]:
        """
            Returns the value being interpreted as a double array. The array returned is not linked to the underlying array stored
            in this value. Only in the case this value is of type double array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Returns:
                the value being interpreted as a double array.
        
        """
        ...
    @typing.overload
    def getDoubles(self, int: int, int2: int) -> typing.List[float]:
        """
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a double array.
        
        
        """
        ...
    @typing.overload
    def getFloat(self) -> float: ...
    @typing.overload
    def getFloat(self, int: int) -> float:
        """
            Returns the value being interpreted as a float. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getFloats(self) -> typing.List[float]:
        """
            Returns the value being interpreted as a float array. The array returned is not linked to the underlying array stored in
            this value. Only in the case this value is of type float array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Returns:
                the value being interpreted as a float array.
        
        """
        ...
    @typing.overload
    def getFloats(self, int: int, int2: int) -> typing.List[float]:
        """
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a float array.
        
        
        """
        ...
    @typing.overload
    def getInt(self) -> int: ...
    @typing.overload
    def getInt(self, int: int) -> int:
        """
            Returns the value being interpreted as a int. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getInts(self) -> typing.List[int]:
        """
            Returns the value being interpreted as a int array. The array returned is not linked to the underlying array stored in
            this value. Only in the case this value is of type int array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Returns:
                the value being interpreted as a int array.
        
        """
        ...
    @typing.overload
    def getInts(self, int: int, int2: int) -> typing.List[int]:
        """
            Returns the value being interpreted as a int array. If the value is not an array it is encapsulated in an array of size
            1
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a int array.
        
        
        """
        ...
    def getLength(self) -> int:
        """
            Returns the length of the array if the value is an array. In case the value is not an array the value returned is 1.
        
            Returns:
                the length of the array or 1 in case of a scalar.
        
        
        """
        ...
    @typing.overload
    def getLong(self) -> int: ...
    @typing.overload
    def getLong(self, int: int) -> int:
        """
            Returns the value being interpreted as a long. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getLongs(self) -> typing.List[int]:
        """
            Returns the value being interpreted as a long array. The array returned is not linked to the underlying array stored in
            this value. Only in the case this value is of type long array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Returns:
                the value being interpreted as a long array.
        
        """
        ...
    @typing.overload
    def getLongs(self, int: int, int2: int) -> typing.List[int]:
        """
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a long array.
        
        
        """
        ...
    @typing.overload
    def getObject(self) -> typing.Any: ...
    @typing.overload
    def getObject(self, int: int) -> typing.Any: ...
    def getScalar(self, int: int) -> ImmutableScalar:
        """
            Returns ImmutableScalar at a specified index. The method creates and returns always a new instance of ImmutableScalar
        
            Parameters:
                index (int): index of a scalar to be returned.
        
        
        """
        ...
    def getScalars(self) -> typing.List[ImmutableScalar]:
        """
            Transforms this object into an array of scalars.
        
            Returns:
                array of immutable scalars.
        
        
        """
        ...
    @typing.overload
    def getShort(self) -> int: ...
    @typing.overload
    def getShort(self, int: int) -> int:
        """
            Returns the value being interpreted as a short. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getShorts(self) -> typing.List[int]:
        """
            Returns the value being interpreted as a short array. The array returned is not linked to the underlying array stored in
            this value. Only in the case this value is of type short array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Returns:
                the value being interpreted as a short array.
        
        """
        ...
    @typing.overload
    def getShorts(self, int: int, int2: int) -> typing.List[int]:
        """
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a short array.
        
        
        """
        ...
    @typing.overload
    def getString(self, int: int) -> str:
        """
            Returns the value being interpreted as a String. The value returned is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getString(self) -> str: ...
    @typing.overload
    def getStrings(self) -> typing.List[str]:
        """
            Returns the value being interpreted as a String array. The array returned is not linked to the underlying array stored
            in this value. Only in the case this value is of type String array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Returns:
                the value being interpreted as a String array.
        
        """
        ...
    @typing.overload
    def getStrings(self, int: int, int2: int) -> typing.List[str]:
        """
            Returns a sub array of the value being interpreted as a string array. The subarray starts at startIndex and contains the
            number of element given by length. If startIndex+length is greater than the number of values in the underlying array an
            exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a String array.
        
        
        """
        ...
    def indexOf(self, object: typing.Any) -> int:
        """
            Finds the index of the value inside the array. If it is not sorted, the results are undefined. If the array contains
            multiple elements with the specified value, there is no guarantee which one will be found. This method considers all NaN
            values to be equivalent and equal.
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value to find the index for
        
            Returns:
                index of the value, if it is contained in the list; otherwise, it returns (-(insertion point) - 1). The insertion point
                is defined as the point at which the value would be inserted into the list: the index of the first element greater than
                the value, or list.size(), if all elements in the list are less than the specified key. Note that this guarantees that
                the return value will be >= 0 if and only if the key is found.
        
        
        """
        ...
    def makeMutable(self) -> 'ScalarArray':
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`
            Returns a mutable version of this immutable value. The mutable version is made by performing a deep copy of this value.
            The runtime type of the value is preserved by this operation. The resulting value can be cast in the mutable type
            corresponding to the immutable type of this value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Returns:
                a mutable deep copy of this value
        
        
        """
        ...
    def subArray(self, int: int, int2: int) -> 'ScalarArray':
        """
            Returns a sub part of this array defined by the 2 indexes. The 2 indexes must be in the range of this scalars array and
            index1 must be less then or equals to index2.
        
            Parameters:
                index1 (int): the index of the first value to return in the sub array
                index2 (int): the index of the last value to return in the sub array
        
            Returns:
                the sub-function as defined by index1 and index2 with the above rules.
        
        
        """
        ...

class Polynomial(MathFunction, Value):
    """
    public interface Polynomial extends :class:`~cern.accsoft.commons.value.MathFunction`, :class:`~cern.accsoft.commons.value.Value`
    
        Defines a polynomial type based on :class:`~cern.accsoft.commons.value.MathFunction`.
    """
    def getCoefficients(self) -> typing.List[float]:
        """
            Example: You have polynomial p(x) = a + b*x + c*x^2 the resulting coefficients array would be [a, b, c].
        
            Returns:
                the coefficients of the polynomial as an array.
        
        
        """
        ...
    def getDegree(self) -> int:
        """
        
            Returns:
                the maximum degree of the polynomial.
        
        
        """
        ...

class Scalar(Value, ImmutableScalar):
    """
    public interface Scalar extends :class:`~cern.accsoft.commons.value.Value`, :class:`~cern.accsoft.commons.value.ImmutableScalar`
    
        Defines a Value that is a scalar that can be changed
    """
    def setBoolean(self, boolean: bool) -> None:
        """
            Sets the value being a boolean. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (boolean): the boolean value.
        
        
        """
        ...
    def setByte(self, byte: int) -> None:
        """
            Sets the value being a byte. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (byte): the byte value.
        
        
        """
        ...
    def setDouble(self, double: float) -> None:
        """
            Sets the value being a double. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (double): the double value.
        
        
        """
        ...
    def setFloat(self, float: float) -> None:
        """
            Sets the value being a float. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (float): the float value.
        
        
        """
        ...
    def setInt(self, int: int) -> None:
        """
            Sets the value being a int. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (int): the int value.
        
        
        """
        ...
    def setLong(self, long: int) -> None:
        """
            Sets the value being a long. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (long): the long value.
        
        
        """
        ...
    def setObject(self, object: typing.Any) -> None: ...
    def setShort(self, short: int) -> None:
        """
            Sets the value being a short. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (short): the short value.
        
        
        """
        ...
    def setString(self, string: str) -> None:
        """
            Sets the value being a String. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the String value.
        
        
        """
        ...

class BoundedPolynomial(Polynomial):
    """
    public interface BoundedPolynomial extends :class:`~cern.accsoft.commons.value.Polynomial`
    
        Stores always a relative :class:`~cern.accsoft.commons.value.Polynomial`, where the coefficients are defined with
        respect to the lower boundaries of the interval, i.e. the polynomial :code:`p[n]` should be evaluated as
        :code:`p[n].interpolate(x - b)`, where :code:`b` is the lower bound.
    """
    def getInterval(self) -> Interval:
        """
        
            Returns:
                the :class:`~cern.accsoft.commons.value.Interval` of this :class:`~cern.accsoft.commons.value.BoundedPolynomial`
        
        
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
                the interpolated value of the :class:`~cern.accsoft.commons.value.BoundedPolynomial` if the
                :class:`~cern.accsoft.commons.value.Interval` contains :code:`x` or `null
                <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Double.html?is-external=true#NaN>` if the
                :class:`~cern.accsoft.commons.value.Interval` doesn't contain :code:`x`.
        
            Also see:
                :meth:`~cern.accsoft.commons.value.spi.function.AbstractMathFunction.interpolate`
        
        
        """
        ...

class DiscreteFunction(Scalar, ImmutableDiscreteFunction):
    @typing.overload
    def insert(self, double: float) -> bool: ...
    @typing.overload
    def insert(self, double: float, double2: float) -> bool: ...
    @typing.overload
    def insertAll(self, immutableDiscreteFunction: ImmutableDiscreteFunction, double: float) -> int: ...
    @typing.overload
    def insertAll(self, doubleArray: typing.List[float]) -> int: ...
    def remove(self, double: float) -> bool: ...
    def removeAll(self, doubleArray: typing.List[float]) -> int: ...
    def retainAll(self, immutableDiscreteFunction: ImmutableDiscreteFunction, double: float) -> int: ...
    def setY(self, int: int, double: float) -> None: ...
    def subView(self, double: float, double2: float) -> 'DiscreteFunction': ...
    def translate(self, double: float) -> None: ...

class ImmutableDiscreteFunctionList(ImmutableDiscreteFunction):
    """
    public interface ImmutableDiscreteFunctionList extends :class:`~cern.accsoft.commons.value.ImmutableDiscreteFunction`
    """
    def getAbsoluteFunction(self, int: int) -> ImmutableDiscreteFunction:
        """
            Returns function at specified index with absolute coordinates
        
            Parameters:
                index (int): 
            Returns:
                function at specified index with absolute coordinates
        
        
        """
        ...
    def getFunction(self, int: int) -> ImmutableDiscreteFunction: ...
    def getFunctions(self) -> typing.List[ImmutableDiscreteFunction]: ...
    def getFunctionsCount(self) -> int: ...
    def getSizeIncludingStopPoints(self) -> int:
        """
            Returns sum of number of points of each function in function list
        
            Returns:
                sum of number of points of each function in function list
        
        
        """
        ...
    def getStopPointsIndices(self) -> typing.List[int]:
        """
            Returns indices of stop points of this function. If this function doesn't have any stop points - the method returns an
            empty array.
        
            Returns:
                indices of stop points of this function or empty array
        
        
        """
        ...
    def makeMutable(self) -> 'DiscreteFunctionList':
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`
            Returns a mutable version of this immutable value. The mutable version is made by performing a deep copy of this value.
            The runtime type of the value is preserved by this operation. The resulting value can be cast in the mutable type
            corresponding to the immutable type of this value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableDiscreteFunction.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableDiscreteFunction`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Returns:
                a mutable deep copy of this value
        
        
        """
        ...

class ImmutableScalarArray2D(ImmutableScalarArray):
    """
    public interface ImmutableScalarArray2D extends :class:`~cern.accsoft.commons.value.ImmutableScalarArray`
    
        Define an immutable array2d of scalars
    
        Note that a scalars array2d is a scalar array. That means that the scalar array2d is a scalar array with additional
        information on dimension. If rownum is the number of rows of the scalar array2d and colnum the number of columns, all
        methods of the scalar array will apply on this scalar 2d as if it was an array of size colnum*rownum. An access on index
        i would access the corresponding cell defined by (i / colnum) + (i % colnum).
    """
    def getArray2D(self) -> cern.japc.value.Array2D:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalarArray.getArray2D`
            Returns a wrapper around the value being interpreted as a 2d array. If the value is a 1d array it is encapsulated in an
            array of size 1xn. If the value is not an array it is encapsulated in an array of size 1x1. IMPORTANT: if the value is
            mutable and is changed after the wrapper is got the wrapper becomes invalide and can return wrong values or even throw
            OutOfBoundException.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalarArray.getArray2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalarArray`
        
            Returns:
                the value being interpreted as a boolean 2d array.
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
            Returns the number of columns in this array 2d
        
            Returns:
                the number of columns in this array 2d
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
            Returns the number of rows in this array 2d
        
            Returns:
                the number of rows in this array 2d
        
        
        """
        ...
    def makeMutable(self) -> 'ScalarArray2D':
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`
            Returns a mutable version of this immutable value. The mutable version is made by performing a deep copy of this value.
            The runtime type of the value is preserved by this operation. The resulting value can be cast in the mutable type
            corresponding to the immutable type of this value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalarArray.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalarArray`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Returns:
                a mutable deep copy of this value
        
        
        """
        ...

class Point(Scalar, ImmutablePoint):
    """
    public interface Point extends :class:`~cern.accsoft.commons.value.Scalar`, :class:`~cern.accsoft.commons.value.ImmutablePoint`
    
        A point is a scalars where the value is the y-coordinate. The x-coordinate is an additional information.
    """
    def setX(self, double: float) -> None:
        """
            Sets the x-coordinates of the point.
        
            Parameters:
                x (double): the x-coordinates of the point.
        
        
        """
        ...
    def setY(self, double: float) -> None:
        """
            Sets the y-coordinates of the point
        
            Parameters:
                y (double): the y-coordinates of the point
        
        
        """
        ...

class ScalarArray(Scalar, ImmutableScalarArray, Indexed):
    def insert(self, int: int, double: float) -> None: ...
    def insertAll(self, intArray: typing.List[int], doubleArray: typing.List[float]) -> None: ...
    def remove(self, int: int) -> None: ...
    def removeAll(self, intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setBoolean(self, boolean: bool) -> None: ...
    @typing.overload
    def setBoolean(self, int: int, boolean: bool) -> None: ...
    def setBooleans(self, booleanArray: typing.List[bool]) -> None: ...
    @typing.overload
    def setByte(self, byte: int) -> None: ...
    @typing.overload
    def setByte(self, int: int, byte: int) -> None: ...
    def setBytes(self, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def setDouble(self, double: float) -> None: ...
    @typing.overload
    def setDouble(self, int: int, double: float) -> None: ...
    def setDoubles(self, doubleArray: typing.List[float]) -> None: ...
    @typing.overload
    def setFloat(self, float: float) -> None: ...
    @typing.overload
    def setFloat(self, int: int, float: float) -> None: ...
    def setFloats(self, floatArray: typing.List[float]) -> None: ...
    @typing.overload
    def setInt(self, int: int) -> None: ...
    @typing.overload
    def setInt(self, int: int, int2: int) -> None: ...
    def setInts(self, intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setLong(self, long: int) -> None: ...
    @typing.overload
    def setLong(self, int: int, long: int) -> None: ...
    def setLongs(self, longArray: typing.List[int]) -> None: ...
    def setObject(self, object: typing.Any) -> None: ...
    def setScalar(self, int: int, immutableScalar: ImmutableScalar) -> None: ...
    def setScalars(self, immutableScalarArray: typing.List[ImmutableScalar]) -> None: ...
    @typing.overload
    def setShort(self, short: int) -> None: ...
    @typing.overload
    def setShort(self, int: int, short: int) -> None: ...
    def setShorts(self, shortArray: typing.List[int]) -> None: ...
    @typing.overload
    def setString(self, string: str) -> None: ...
    @typing.overload
    def setString(self, int: int, string: str) -> None: ...
    def setStrings(self, stringArray: typing.List[str]) -> None: ...

class DiscreteFunctionList(DiscreteFunction, ImmutableDiscreteFunctionList):
    """
    public interface DiscreteFunctionList extends :class:`~cern.accsoft.commons.value.DiscreteFunction`, :class:`~cern.accsoft.commons.value.ImmutableDiscreteFunctionList`
    
        Defines a discrete function with optional stop points which split the initial function into sub-functions.
    """
    def merge(self, int: int) -> None:
        """
            Merge specified and next after specified functions. Merge means removing the stop point.
        
            Parameters:
                functionNumber (int): number of function to be merged with the next one
        
            Raises:
                : if function number is greater then (functionsCount - 2)
        
        
        """
        ...
    def setStopPoints(self, intArray: typing.List[int]) -> None:
        """
            Sets function stop points on specified indices.
        
            Parameters:
                stopPointIndices (int[]): array of indices of stop points
        
            Raises:
                : if the given array contains indices of non-existing points
        
        
        """
        ...
    def split(self, double: float) -> None:
        """
            Split function at specified x-coordinate. Split means adding the stop point.
        
            Parameters:
                x (double): coordinate of stop point
        
            Raises:
                : if x is out of bounds
        
        
        """
        ...
    def subView(self, double: float, double2: float) -> DiscreteFunction:
        """
            Not supported for DiscreteFunctionList - throws :code:`UnsupportedOperationException`.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.DiscreteFunction.subView`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.DiscreteFunction`
        
            Parameters:
                fromX (double): the first x-coordinate of the view to return (inclusive)
                toX (double): the last x-coordinate of the view to return (inclusive)
        
            Returns:
                the view on the discrete function as defined by fromX and toX and the above rules.
        
        
        """
        ...

class ScalarArray2D(ImmutableScalarArray2D, ScalarArray):
    """
    public interface ScalarArray2D extends :class:`~cern.accsoft.commons.value.ImmutableScalarArray2D`, :class:`~cern.accsoft.commons.value.ScalarArray`
    
        Define an array of scalars
    
        Note that a scalar array is a scalar. That means that is it possible by extension, to use a scalar array where a scalar
        would be used. In this case, the value of a scalar array taken as a scalar is its first value. If the scalar array is
        empty, the value is Double.NaN.
    """
    def setBooleans2D(self, booleanArray: typing.List[bool], int: int, int2: int) -> None:
        """
            Sets the value being a 2-dimetional boolean array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (boolean[]): the boolean array value.
                dimensions (int): the dimensions of the array
        
        
        """
        ...
    def setBytes2D(self, byteArray: typing.List[int], int: int, int2: int) -> None:
        """
            Sets the value being a 2-dimetional byte array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (byte[]): the byte array value.
                dimensions (int): the dimensions of the array
        
        
        """
        ...
    def setDoubles2D(self, doubleArray: typing.List[float], int: int, int2: int) -> None:
        """
            Sets the value being a 2-dimetional double array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (double[]): the double array value.
                dimensions (int): the dimensions of the array
        
        
        """
        ...
    def setFloats2D(self, floatArray: typing.List[float], int: int, int2: int) -> None:
        """
            Sets the value being a 2-dimetional float array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (float[]): the float array value.
                dimensions (int): the dimensions of the array
        
        
        """
        ...
    def setInts2D(self, intArray: typing.List[int], int2: int, int3: int) -> None:
        """
            Sets the value being a 2-dimetional int array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (int[]): the int array value.
                dimensions (int): the dimensions of the array
        
        
        """
        ...
    def setLongs2D(self, longArray: typing.List[int], int: int, int2: int) -> None:
        """
            Sets the value being a 2-dimetional long array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (long[]): the long array value.
                dimensions (int): the dimensions of the array
        
        
        """
        ...
    def setObjects2D(self, object: typing.Any, int: int, int2: int) -> None:
        """
            Sets the value as a 2d array of objects. This method can handle any array of primitives and Strings, which will be used
            as a source for 2D array. If other type was passed a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` will be
            thrown. If this value is not mutable an exception is thrown.
        
            Parameters:
                o (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value as an object.
        
        
        """
        ...
    def setShorts2D(self, shortArray: typing.List[int], int: int, int2: int) -> None:
        """
            Sets the value being a 2-dimetional short array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (short[]): the short array value.
                dimensions (int): the dimensions of the array
        
        
        """
        ...
    def setStrings2D(self, stringArray: typing.List[str], int: int, int2: int) -> None:
        """
            Sets the value being a 2-dimetional String array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the String array value.
                dimensions (int): the dimensions of the array
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.value")``.

    BoundedPolynomial: typing.Type[BoundedPolynomial]
    BoundedPolynomialSequence: typing.Type[BoundedPolynomialSequence]
    BoundedPolynomials: typing.Type[BoundedPolynomials]
    ContinuousFunction: typing.Type[ContinuousFunction]
    DiscreteFunction: typing.Type[DiscreteFunction]
    DiscreteFunctionCompressor: typing.Type[DiscreteFunctionCompressor]
    DiscreteFunctionList: typing.Type[DiscreteFunctionList]
    DiscreteFunctions: typing.Type[DiscreteFunctions]
    DiscreteFunctionsArray: typing.Type[DiscreteFunctionsArray]
    Function: typing.Type[Function]
    FunctionOperationException: typing.Type[FunctionOperationException]
    FunctionPointReductionOptions: typing.Type[FunctionPointReductionOptions]
    ImmutableDiscreteFunction: typing.Type[ImmutableDiscreteFunction]
    ImmutableDiscreteFunctionList: typing.Type[ImmutableDiscreteFunctionList]
    ImmutableDiscreteFunctionsArray: typing.Type[ImmutableDiscreteFunctionsArray]
    ImmutablePoint: typing.Type[ImmutablePoint]
    ImmutableScalar: typing.Type[ImmutableScalar]
    ImmutableScalarArray: typing.Type[ImmutableScalarArray]
    ImmutableScalarArray2D: typing.Type[ImmutableScalarArray2D]
    ImmutableValue: typing.Type[ImmutableValue]
    Indexed: typing.Type[Indexed]
    Interpolable: typing.Type[Interpolable]
    Interval: typing.Type[Interval]
    MathFunction: typing.Type[MathFunction]
    Operations: typing.Type[Operations]
    ParabolicSplineFunction: typing.Type[ParabolicSplineFunction]
    Point: typing.Type[Point]
    Polynomial: typing.Type[Polynomial]
    Scalar: typing.Type[Scalar]
    ScalarArray: typing.Type[ScalarArray]
    ScalarArray2D: typing.Type[ScalarArray2D]
    ScalarArrays: typing.Type[ScalarArrays]
    Type: typing.Type[Type]
    Typed: typing.Type[Typed]
    Value: typing.Type[Value]
    ValueDescriptor: typing.Type[ValueDescriptor]
    ValueFactory: typing.Type[ValueFactory]
    Values: typing.Type[Values]
    expression: cern.accsoft.commons.value.expression.__module_protocol__
    operation: cern.accsoft.commons.value.operation.__module_protocol__
    spi: cern.accsoft.commons.value.spi.__module_protocol__
