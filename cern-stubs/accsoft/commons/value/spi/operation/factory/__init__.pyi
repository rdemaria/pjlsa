import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.operation.factory
import typing



class BinaryOperationProvider(cern.accsoft.commons.value.operation.factory.AbstractOperationProvider[cern.accsoft.commons.value.operation.BinaryOperation]):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.factory.BinaryOperationProvider'
    
        Extends:
            cern.accsoft.commons.value.operation.factory.AbstractOperationProvider
    
      Constructors:
        * BinaryOperationProvider()
    
      Attributes:
        MAX (java.lang.String): final static field
        MIN (java.lang.String): final static field
        IEEEREMAINDER (java.lang.String): final static field
        POW (java.lang.String): final static field
    
    """
    MAX: typing.ClassVar[str] = ...
    MIN: typing.ClassVar[str] = ...
    IEEEREMAINDER: typing.ClassVar[str] = ...
    POW: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType: ...

class CoreOperationProvider(cern.accsoft.commons.value.operation.factory.AbstractOperationProvider[cern.accsoft.commons.value.operation.BinaryOperation]):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.factory.CoreOperationProvider'
    
        Extends:
            cern.accsoft.commons.value.operation.factory.AbstractOperationProvider
    
      Constructors:
        * CoreOperationProvider()
    
    """
    def __init__(self): ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType: ...

class MathFunctionOperationProvider(cern.accsoft.commons.value.operation.factory.AbstractOperationProvider[cern.accsoft.commons.value.operation.MathFunctionOperation]):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.factory.MathFunctionOperationProvider'
    
        Extends:
            cern.accsoft.commons.value.operation.factory.AbstractOperationProvider
    
      Constructors:
        * MathFunctionOperationProvider()
    
      Attributes:
        ABS (java.lang.String): final static field
        ACOS (java.lang.String): final static field
        ASIN (java.lang.String): final static field
        ATAN (java.lang.String): final static field
        CEIL (java.lang.String): final static field
        COS (java.lang.String): final static field
        EXP (java.lang.String): final static field
        FLOOR (java.lang.String): final static field
        LOG (java.lang.String): final static field
        LOG10 (java.lang.String): final static field
        POW2 (java.lang.String): final static field
        RINT (java.lang.String): final static field
        ROUND (java.lang.String): final static field
        SIN (java.lang.String): final static field
        SQRT (java.lang.String): final static field
        TAN (java.lang.String): final static field
        TODEGREES (java.lang.String): final static field
        TORADIANS (java.lang.String): final static field
    
    """
    ABS: typing.ClassVar[str] = ...
    ACOS: typing.ClassVar[str] = ...
    ASIN: typing.ClassVar[str] = ...
    ATAN: typing.ClassVar[str] = ...
    CEIL: typing.ClassVar[str] = ...
    COS: typing.ClassVar[str] = ...
    EXP: typing.ClassVar[str] = ...
    FLOOR: typing.ClassVar[str] = ...
    LOG: typing.ClassVar[str] = ...
    LOG10: typing.ClassVar[str] = ...
    POW2: typing.ClassVar[str] = ...
    RINT: typing.ClassVar[str] = ...
    ROUND: typing.ClassVar[str] = ...
    SIN: typing.ClassVar[str] = ...
    SQRT: typing.ClassVar[str] = ...
    TAN: typing.ClassVar[str] = ...
    TODEGREES: typing.ClassVar[str] = ...
    TORADIANS: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType: ...

class UnaryOperationProvider(cern.accsoft.commons.value.operation.factory.AbstractOperationProvider[cern.accsoft.commons.value.operation.UnaryOperation]):
    """
    Java class 'cern.accsoft.commons.value.spi.operation.factory.UnaryOperationProvider'
    
        Extends:
            cern.accsoft.commons.value.operation.factory.AbstractOperationProvider
    
      Constructors:
        * UnaryOperationProvider()
    
    """
    def __init__(self): ...
    def getType(self) -> cern.accsoft.commons.value.operation.OperationType: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.value.spi.operation.factory")``.

    BinaryOperationProvider: typing.Type[BinaryOperationProvider]
    CoreOperationProvider: typing.Type[CoreOperationProvider]
    MathFunctionOperationProvider: typing.Type[MathFunctionOperationProvider]
    UnaryOperationProvider: typing.Type[UnaryOperationProvider]
