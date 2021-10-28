import typing



class FloatingPointComparator:
    """
    Java class 'cern.japc.value.spi.util.FloatingPointComparator'
    
        Extends:
            java.lang.Object
    
      Constructors:
        * FloatingPointComparator()
    
      Attributes:
        DOUBLE_TOLERANCE (double): final static field
        FLOAT_TOLERANCE (float): final static field
    
    """
    DOUBLE_TOLERANCE: typing.ClassVar[float] = ...
    FLOAT_TOLERANCE: typing.ClassVar[float] = ...
    def __init__(self): ...
    @typing.overload
    @staticmethod
    def compare(double: float, double2: float) -> int: ...
    @typing.overload
    @staticmethod
    def compare(float: float, float2: float) -> int: ...
    @typing.overload
    @staticmethod
    def equal(double: float, double2: float) -> bool: ...
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
