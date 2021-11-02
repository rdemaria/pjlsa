import typing



class FloatingPointComparator:
    """
    public class FloatingPointComparator extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Helper class which allows to compare floating point values with non-infinite accuracy. 2 floats are considered equal if
        the difference is 5 orders less than the greatest float. 2 doubles are considered equal if the difference is 10 orders
        less than the greatest double.
    """
    DOUBLE_TOLERANCE: typing.ClassVar[float] = ...
    """
    public static final double DOUBLE_TOLERANCE
    
        Tolerance to compare doubles
    
        Also see:
            :meth:`~constant`
    
    
    """
    FLOAT_TOLERANCE: typing.ClassVar[float] = ...
    """
    public static final float FLOAT_TOLERANCE
    
        Tolerance to compare floats
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def compare(double: float, double2: float) -> int:
        """
            This methods compares 2 doubles. It returns 0 if doubles are equal, -1 if first double is less, and +1 if first double
            is greater.
        
            Parameters:
                d1 (double): first double
                d2 (double): second double
        
            Returns:
                0 if doubles are equal, -1 if first double is less, and +1 if first double is greater
        
            This methods compares 2 floats. It returns 0 if floats are equal, -1 if first float is less, and +1 if first float is
            greater.
        
            Parameters:
                f1 (float): first float
                f2 (float): second float
        
            Returns:
                0 if floats are equal, -1 if first float is less, and +1 if first float is greater
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def compare(float: float, float2: float) -> int: ...
    @typing.overload
    @staticmethod
    def equal(double: float, double2: float) -> bool:
        """
            This method checks if 2 doubles are equal.
        
            Parameters:
                number1 (double): first double
                number2 (double): second double
        
            Returns:
                true if arguments are equal and false otherwise.
        
            This method checks if 2 floats are equal.
        
            Parameters:
                number1 (float): first float
                number2 (float): second float
        
            Returns:
                true if arguments are equal and false otherwise.
        
            This method checks if 2 double arrays are equal.
        
            Parameters:
                da1 (double[]): first double array
                da2 (double[]): second double array
        
            Returns:
                true if arguments are equal and false otherwise.
        
            This method checks if 2 float arrays are equal.
        
            Parameters:
                fa1 (float[]): first float array
                fa2 (float[]): second float array
        
            Returns:
                true if arguments are equal and false otherwise.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def equal(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> bool: ...
    @typing.overload
    @staticmethod
    def equal(float: float, float2: float) -> bool: ...
    @typing.overload
    @staticmethod
    def equal(floatArray: typing.List[float], floatArray2: typing.List[float]) -> bool: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.value.spi.util")``.

    FloatingPointComparator: typing.Type[FloatingPointComparator]
