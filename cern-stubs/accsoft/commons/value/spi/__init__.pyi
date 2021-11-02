import cern.accsoft.commons.value
import cern.accsoft.commons.value.operation
import cern.accsoft.commons.value.spi.function
import cern.accsoft.commons.value.spi.operation
import cern.japc.value
import cern.japc.value.spi.value.simple
import java.io
import java.util
import jpype.protocol
import typing



class AbstractValue(cern.accsoft.commons.value.Value):
    """
    public abstract class AbstractValue extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.Value`
    
    
        Give a first implementation of Value that support the int operations using the double version of them.
    
        Also see:
            :meth:`~serialized`
    """
    def clone(self) -> typing.Any:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.clone`
            Performs a deep copy of this value
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.clone`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Overrides:
                 in class 
        
            Returns:
                a deep copy of this value
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createValue(type: cern.accsoft.commons.value.Type) -> cern.japc.value.spi.value.simple.AbstractSimpleValue:
        """
        public static cern.japc.value.spi.value.simple.AbstractSimpleValue createValue (:class:`~cern.accsoft.commons.value.Type` type, `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` value)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createValue(type: cern.accsoft.commons.value.Type, object: typing.Any) -> cern.japc.value.spi.value.simple.AbstractSimpleValue: ...
    @typing.overload
    @staticmethod
    def createValue(object: typing.Any) -> cern.japc.value.spi.value.simple.AbstractSimpleValue: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
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
    def getValueDescriptor(self) -> cern.accsoft.commons.value.ValueDescriptor:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.getValueDescriptor`
            Get descriptor for this value. Descriptor describes specific properties of value such as minimal, maximal value,
            precision and possible values represented by enumeration.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.getValueDescriptor`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Returns:
                value descriptor
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isDefined(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.isDefined`
            If in moment of creation (retrieving from data base) the value for ImmutableValue cannot be specified this flag is set
            to false. This flag is set by default to true.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.isDefined`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Returns:
                :code:`true` by default or :code:`false` when value is not defined
        
        
        """
        ...
    def setDefined(self, boolean: bool) -> None:
        """
            Sets defined property.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.setDefined` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Parameters:
                defined (boolean): the defined to set
        
        
        """
        ...
    def setValueDescriptor(self, valueDescriptor: cern.accsoft.commons.value.ValueDescriptor) -> None:
        """
            Sets descriptor property.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.setValueDescriptor` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Parameters:
                descriptor (:class:`~cern.accsoft.commons.value.ValueDescriptor`): the descriptor to set
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class IOUtils:
    def __init__(self): ...
    @staticmethod
    def parseCSV(file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> java.util.Map[str, cern.accsoft.commons.value.ImmutableValue]: ...
    @staticmethod
    def toCSV(file: typing.Union[java.io.File, jpype.protocol.SupportsPath], map: typing.Union[java.util.Map[str, cern.accsoft.commons.value.ImmutableValue], typing.Mapping[str, cern.accsoft.commons.value.ImmutableValue]]) -> None: ...

class ValueDescriptorImpl(cern.accsoft.commons.value.ValueDescriptor):
    """
    public class ValueDescriptorImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.accsoft.commons.value.ValueDescriptor`
    
        The default implementation of the :code:`ValueDescriptor` interface.
    
        Enumerations are stored as :code:`EnumType`, as given by japc-value.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def clone(self) -> 'ValueDescriptorImpl':
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.clone`
            Publicly available clone method
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.clone`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Overrides:
                 in class 
        
            Returns:
                a cloned copy of this instance
        
        
        """
        ...
    def containsMeanings(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.containsMeanings`
            Returns :code:`true` if at least one meaning is defined.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.containsMeanings`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
        
        """
        ...
    def getAbsoluteTolerance(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getAbsoluteTolerance`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Returns:
                absolute tolerance used when comparing value
        
        
        """
        ...
    def getBooleanType(self) -> cern.japc.value.BooleanType:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.getBooleanType`
            Returns corresponding :code:`BooleanType` if the associated value represents a boolean.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getBooleanType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Returns:
                :code:`BooleanType` or :code:`null` if the associated value doesn't represent a boolean
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.getColumnCount`
            Information about dimensions of array for 1d arrays this returns the number of elements for 2d arrays this returns the
            number of columns If value is not an array null is returned This method was formerly named getDim1()
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getColumnCount`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
        
        """
        ...
    def getEnumType(self) -> cern.japc.value.EnumType:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.getEnumType`
            Returns corresponding :code:`EnumType` if the associated value represents an enumeration.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getEnumType`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Returns:
                :code:`EnumType` or :code:`null` if the associated value doesn't represent an enumeration
        
        
        """
        ...
    def getMax(self) -> float:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.getMax`
            Returns the maximal possible value, if it is not set returns null
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getMax`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Returns:
                maximal possible value
        
        
        """
        ...
    def getMeaning(self, object: typing.Any) -> cern.japc.value.SimpleValueStandardMeaning:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getMeaning`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value of the parameter (ex. int, String[] , :code:`EnumItem`, etc.)
        
            Returns:
                the meaning of the value of :code:`null` if the meaning is not defined
        
        
        """
        ...
    def getMin(self) -> float:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.getMin`
            Returns the minimal possible value, if it is not set returns null
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getMin`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Returns:
                minimal possible value
        
        
        """
        ...
    def getRelativeTolerance(self) -> float:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getRelativeTolerance`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Returns:
                relative tolerance used when comparing value
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.getRowCount`
            Information about dimensions of array for 1d arrays this returns null for 2d arrays this returns the number of rows If
            value is not an array null is returned This method was formerly named getDim2()
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getRowCount`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
        
        """
        ...
    def getXPrecision(self) -> int:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.getXPrecision`
            Defines precision of X coordinates if the associated parameter is a function.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getXPrecision`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Returns:
                precision of function X coordinates (if defined), or :code:`null`
        
        
        """
        ...
    def getXUnit(self) -> str:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.getXUnit`
            Returns the unit of the x values (if available) or empty string if not set.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getXUnit`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Returns:
                the xUnit
        
        
        """
        ...
    def getYPrecision(self) -> int:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.getYPrecision`
            Returns precision of Y coordinates if the associated value represents a function. The Y precision is also used for
            scalars and arrays of scalars.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getYPrecision`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Returns:
                precision of Y coordinates (if defined) or :code:`null`
        
        
        """
        ...
    def getYUnit(self) -> str:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ValueDescriptor.getYUnit`
            Returns the unit of the y values (if available) or empty string if not set.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.getYUnit`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Returns:
                the yUnit
        
        
        """
        ...
    def isSettable(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ValueDescriptor.isSettable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ValueDescriptor`
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value of the parameter (ex. int, String[] , :code:`EnumItem`, etc.)
        
            Returns:
                :code:`true` if this value is settable
        
        
        """
        ...
    def setAbsoluteTolerance(self, double: float) -> None: ...
    def setBooleanType(self, booleanType: cern.japc.value.BooleanType) -> None:
        """
            Sets boolean type related data to this value descriptor.
        
            Parameters:
                booleanType (cern.japc.value.BooleanType): see :meth:`~cern.accsoft.commons.value.spi.ValueDescriptorImpl.getBooleanType`
        
        
        """
        ...
    def setColumnCount(self, integer: int) -> None: ...
    def setEnumType(self, enumType: cern.japc.value.EnumType) -> None:
        """
            Sets :code:`EnumType` related data to this value descriptor.
        
            Parameters:
                enumType (cern.japc.value.EnumType): see :meth:`~cern.accsoft.commons.value.spi.ValueDescriptorImpl.getEnumType`
        
        
        """
        ...
    def setMax(self, double: float) -> None: ...
    def setMin(self, double: float) -> None: ...
    def setPrecision(self, integer: int) -> None:
        """
            Method to set precision for scalar values and arrays. Calls
            :meth:`~cern.accsoft.commons.value.spi.ValueDescriptorImpl.setYPrecision`.
        
            Parameters:
                precision (`Integer <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Integer.html?is-external=true>`): precision
        
            Also see:
                :meth:`~cern.accsoft.commons.value.spi.ValueDescriptorImpl.getYPrecision`
        
        
        """
        ...
    def setRelativeTolerance(self, double: float) -> None: ...
    def setRowCount(self, integer: int) -> None: ...
    def setXPrecision(self, integer: int) -> None: ...
    def setXUnit(self, string: str) -> None:
        """
        
            Parameters:
                unit (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the xUnit to set
        
        
        """
        ...
    def setYPrecision(self, integer: int) -> None: ...
    def setYUnit(self, string: str) -> None:
        """
        
            Parameters:
                unit (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the yUnit to set
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ScalarArrayView(AbstractValue, cern.accsoft.commons.value.ScalarArray, java.io.Serializable):
    def __init__(self, scalarArray: cern.accsoft.commons.value.ScalarArray, int: int, int2: int): ...
    def clone(self) -> typing.Any: ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def execute(self, indexing: cern.accsoft.commons.value.spi.operation.Indexing) -> cern.accsoft.commons.value.Scalar: ...
    @typing.overload
    def execute(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation) -> None: ...
    def getArray2D(self) -> cern.japc.value.Array2D: ...
    @typing.overload
    def getBoolean(self) -> bool: ...
    @typing.overload
    def getBoolean(self, int: int) -> bool: ...
    @typing.overload
    def getBooleans(self) -> typing.List[bool]: ...
    @typing.overload
    def getBooleans(self, int: int, int2: int) -> typing.List[bool]: ...
    @typing.overload
    def getByte(self) -> int: ...
    @typing.overload
    def getByte(self, int: int) -> int: ...
    @typing.overload
    def getBytes(self) -> typing.List[int]: ...
    @typing.overload
    def getBytes(self, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getDouble(self) -> float: ...
    @typing.overload
    def getDouble(self, int: int) -> float: ...
    @typing.overload
    def getDoubles(self) -> typing.List[float]: ...
    @typing.overload
    def getDoubles(self, int: int, int2: int) -> typing.List[float]: ...
    @typing.overload
    def getFloat(self) -> float: ...
    @typing.overload
    def getFloat(self, int: int) -> float: ...
    @typing.overload
    def getFloats(self) -> typing.List[float]: ...
    @typing.overload
    def getFloats(self, int: int, int2: int) -> typing.List[float]: ...
    @typing.overload
    def getInt(self) -> int: ...
    @typing.overload
    def getInt(self, int: int) -> int: ...
    @typing.overload
    def getInts(self) -> typing.List[int]: ...
    @typing.overload
    def getInts(self, int: int, int2: int) -> typing.List[int]: ...
    def getLength(self) -> int: ...
    @typing.overload
    def getLong(self) -> int: ...
    @typing.overload
    def getLong(self, int: int) -> int: ...
    @typing.overload
    def getLongs(self) -> typing.List[int]: ...
    @typing.overload
    def getLongs(self, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getObject(self) -> typing.Any: ...
    @typing.overload
    def getObject(self, int: int) -> typing.Any: ...
    def getScalar(self, int: int) -> cern.accsoft.commons.value.ImmutableScalar: ...
    def getScalars(self) -> typing.List[cern.accsoft.commons.value.ImmutableScalar]: ...
    @typing.overload
    def getShort(self) -> int: ...
    @typing.overload
    def getShort(self, int: int) -> int: ...
    @typing.overload
    def getShorts(self) -> typing.List[int]: ...
    @typing.overload
    def getShorts(self, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getString(self) -> str: ...
    @typing.overload
    def getString(self, int: int) -> str: ...
    @typing.overload
    def getStrings(self) -> typing.List[str]: ...
    @typing.overload
    def getStrings(self, int: int, int2: int) -> typing.List[str]: ...
    def getType(self) -> cern.accsoft.commons.value.Type: ...
    def getValueDescriptor(self) -> cern.accsoft.commons.value.ValueDescriptor: ...
    def hashCode(self) -> int: ...
    def indexOf(self, object: typing.Any) -> int: ...
    def insert(self, int: int, double: float) -> None: ...
    def insertAll(self, intArray: typing.List[int], doubleArray: typing.List[float]) -> None: ...
    def isDefined(self) -> bool: ...
    def makeMutable(self) -> cern.accsoft.commons.value.ScalarArray: ...
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
    def setLong(self, int: int, long: int) -> None: ...
    @typing.overload
    def setLong(self, long: int) -> None: ...
    def setLongs(self, longArray: typing.List[int]) -> None: ...
    def setObject(self, object: typing.Any) -> None: ...
    def setScalar(self, int: int, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None: ...
    def setScalars(self, immutableScalarArray: typing.List[cern.accsoft.commons.value.ImmutableScalar]) -> None: ...
    @typing.overload
    def setShort(self, int: int, short: int) -> None: ...
    @typing.overload
    def setShort(self, short: int) -> None: ...
    def setShorts(self, shortArray: typing.List[int]) -> None: ...
    @typing.overload
    def setString(self, int: int, string: str) -> None: ...
    @typing.overload
    def setString(self, string: str) -> None: ...
    def setStrings(self, stringArray: typing.List[str]) -> None: ...
    def subArray(self, int: int, int2: int) -> cern.accsoft.commons.value.ScalarArray: ...
    def toSimpleParameterValue(self) -> cern.japc.value.SimpleParameterValue: ...
    def toString(self) -> str: ...

class ScalarImpl(AbstractValue, cern.accsoft.commons.value.Scalar):
    """
    public class ScalarImpl extends :class:`~cern.accsoft.commons.value.spi.AbstractValue` implements :class:`~cern.accsoft.commons.value.Scalar`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, type: cern.accsoft.commons.value.Type, simpleParameterValue: cern.japc.value.SimpleParameterValue): ...
    def asMatrix(self, intArray: typing.List[int]) -> cern.accsoft.commons.value.ScalarArray2D: ...
    def asVector(self, int: int) -> cern.accsoft.commons.value.ScalarArray: ...
    def clone(self) -> typing.Any:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.clone`
            Performs a deep copy of this value
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.clone`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.AbstractValue.clone`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.AbstractValue`
        
            Returns:
                a deep copy of this value
        
        
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
    def makeMutable(self) -> cern.accsoft.commons.value.Scalar:
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

class PointImpl(ScalarImpl, cern.accsoft.commons.value.Point):
    """
    public class PointImpl extends :class:`~cern.accsoft.commons.value.spi.ScalarImpl` implements :class:`~cern.accsoft.commons.value.Point`
    
        Defines a point in a plan. The x-coordinate can be of type int or double. The y-coordinate is a double. A Point is a
        Constant whose value is the y-coordinate. A point can be seen as a scalars with a x-coordinate associated to it.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, immutablePoint: cern.accsoft.commons.value.ImmutablePoint): ...
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarImpl.equals` in class :class:`~cern.accsoft.commons.value.spi.ScalarImpl`
        
        
        """
        ...
    def getX(self) -> float:
        """
            getter method for x
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutablePoint.getX`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutablePoint`
        
            Returns:
                the value of the x of this point
        
        
        """
        ...
    def getY(self) -> float:
        """
            getter method for y
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutablePoint.getY`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutablePoint`
        
            Returns:
                the value of the y of this point
        
            Also see:
                :code:`ImmutableScalar#get()`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarImpl.hashCode`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarImpl`
        
        
        """
        ...
    @staticmethod
    def interpolate(pointImpl: 'PointImpl', pointImpl2: 'PointImpl', double: float) -> cern.accsoft.commons.value.Point:
        """
            Computes a new point at x-coordinate x on the line defined by p1 and p2
        
            Parameters:
                p1 (:class:`~cern.accsoft.commons.value.spi.PointImpl`): the first point of the ilne
                p2 (:class:`~cern.accsoft.commons.value.spi.PointImpl`): the second point of the line
                x (double): the x-coordinate of the new point to calculate
        
            Returns:
                the resulting point interpolated from the two given points at the given x-coordinate
        
        
        """
        ...
    def isContinueWith(self, value: cern.accsoft.commons.value.Value) -> bool:
        """
            Returns true if the given value is a point and if the x-coordinate and the y-coordinate of the given point are equal to
            the ones of this point. Note that equal is defined relative to a given precision defined in :code:`Values`
        
            Parameters:
                value (:class:`~cern.accsoft.commons.value.Value`): a value to test the continuity with
        
            Returns:
                true if the given valus if a point whose coordinates are equals to this one
        
        
        """
        ...
    def makeMutable(self) -> cern.accsoft.commons.value.Point:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`
            Returns a mutable version of this immutable value. The mutable version is made by performing a deep copy of this value.
            The runtime type of the value is preserved by this operation. The resulting value can be cast in the mutable type
            corresponding to the immutable type of this value.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutablePoint.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutablePoint`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalar.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalar`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarImpl.makeMutable`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarImpl`
        
            Returns:
                a mutable deep copy of this value
        
        
        """
        ...
    def setX(self, double: float) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Point.setX`
            Sets the x-coordinates of the point.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Point.setX` in interface :class:`~cern.accsoft.commons.value.Point`
        
            Parameters:
                x (double): the x-coordinates of the point.
        
        
        """
        ...
    def setY(self, double: float) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Point.setY`
            Sets the y-coordinates of the point
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Point.setY` in interface :class:`~cern.accsoft.commons.value.Point`
        
            Parameters:
                y (double): the y-coordinates of the point
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarImpl.toString`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarImpl`
        
        
        """
        ...

class ScalarArrayImpl(ScalarImpl, cern.accsoft.commons.value.ScalarArray):
    def __init__(self, type: cern.accsoft.commons.value.Type, simpleParameterValue: cern.japc.value.SimpleParameterValue): ...
    def asMatrix(self, intArray: typing.List[int]) -> cern.accsoft.commons.value.ScalarArray2D: ...
    def asVector(self, int: int) -> cern.accsoft.commons.value.ScalarArray: ...
    def equals(self, object: typing.Any) -> bool: ...
    @typing.overload
    def execute(self, indexing: cern.accsoft.commons.value.spi.operation.Indexing) -> cern.accsoft.commons.value.Scalar: ...
    @typing.overload
    def execute(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation) -> None: ...
    def getArray2D(self) -> cern.japc.value.Array2D: ...
    @typing.overload
    def getBoolean(self, int: int) -> bool: ...
    @typing.overload
    def getBoolean(self) -> bool: ...
    @typing.overload
    def getBooleans(self) -> typing.List[bool]: ...
    @typing.overload
    def getBooleans(self, int: int, int2: int) -> typing.List[bool]: ...
    @typing.overload
    def getByte(self, int: int) -> int: ...
    @typing.overload
    def getByte(self) -> int: ...
    @typing.overload
    def getBytes(self) -> typing.List[int]: ...
    @typing.overload
    def getBytes(self, int: int, int2: int) -> typing.List[int]: ...
    def getColumnCount(self) -> int: ...
    @typing.overload
    def getDouble(self, int: int) -> float: ...
    @typing.overload
    def getDouble(self) -> float: ...
    @typing.overload
    def getDoubles(self) -> typing.List[float]: ...
    @typing.overload
    def getDoubles(self, int: int, int2: int) -> typing.List[float]: ...
    @typing.overload
    def getFloat(self, int: int) -> float: ...
    @typing.overload
    def getFloat(self) -> float: ...
    @typing.overload
    def getFloats(self) -> typing.List[float]: ...
    @typing.overload
    def getFloats(self, int: int, int2: int) -> typing.List[float]: ...
    @typing.overload
    def getInt(self, int: int) -> int: ...
    @typing.overload
    def getInt(self) -> int: ...
    @typing.overload
    def getInts(self) -> typing.List[int]: ...
    @typing.overload
    def getInts(self, int: int, int2: int) -> typing.List[int]: ...
    def getLength(self) -> int: ...
    @typing.overload
    def getLong(self, int: int) -> int: ...
    @typing.overload
    def getLong(self) -> int: ...
    @typing.overload
    def getLongs(self) -> typing.List[int]: ...
    @typing.overload
    def getLongs(self, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getObject(self, int: int) -> typing.Any: ...
    @typing.overload
    def getObject(self) -> typing.Any: ...
    def getRowCount(self) -> int: ...
    def getScalar(self, int: int) -> cern.accsoft.commons.value.ImmutableScalar: ...
    def getScalars(self) -> typing.List[cern.accsoft.commons.value.ImmutableScalar]: ...
    @typing.overload
    def getShort(self, int: int) -> int: ...
    @typing.overload
    def getShort(self) -> int: ...
    @typing.overload
    def getShorts(self) -> typing.List[int]: ...
    @typing.overload
    def getShorts(self, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getString(self, int: int) -> str: ...
    @typing.overload
    def getString(self) -> str: ...
    @typing.overload
    def getStrings(self) -> typing.List[str]: ...
    @typing.overload
    def getStrings(self, int: int, int2: int) -> typing.List[str]: ...
    def hashCode(self) -> int: ...
    def indexOf(self, object: typing.Any) -> int: ...
    def insert(self, int: int, double: float) -> None: ...
    def insertAll(self, intArray: typing.List[int], doubleArray: typing.List[float]) -> None: ...
    def makeMutable(self) -> cern.accsoft.commons.value.ScalarArray: ...
    def remove(self, int: int) -> None: ...
    def removeAll(self, intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setBoolean(self, int: int, boolean: bool) -> None: ...
    @typing.overload
    def setBoolean(self, boolean: bool) -> None: ...
    def setBooleans(self, booleanArray: typing.List[bool]) -> None: ...
    @typing.overload
    def setByte(self, int: int, byte: int) -> None: ...
    @typing.overload
    def setByte(self, byte: int) -> None: ...
    def setBytes(self, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def setDouble(self, int: int, double: float) -> None: ...
    @typing.overload
    def setDouble(self, double: float) -> None: ...
    def setDoubles(self, doubleArray: typing.List[float]) -> None: ...
    @typing.overload
    def setFloat(self, int: int, float: float) -> None: ...
    @typing.overload
    def setFloat(self, float: float) -> None: ...
    def setFloats(self, floatArray: typing.List[float]) -> None: ...
    @typing.overload
    def setInt(self, int: int, int2: int) -> None: ...
    @typing.overload
    def setInt(self, int: int) -> None: ...
    def setInts(self, intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setLong(self, int: int, long: int) -> None: ...
    @typing.overload
    def setLong(self, long: int) -> None: ...
    def setLongs(self, longArray: typing.List[int]) -> None: ...
    def setObject(self, object: typing.Any) -> None: ...
    def setScalar(self, int: int, immutableScalar: cern.accsoft.commons.value.ImmutableScalar) -> None: ...
    def setScalars(self, immutableScalarArray: typing.List[cern.accsoft.commons.value.ImmutableScalar]) -> None: ...
    @typing.overload
    def setShort(self, int: int, short: int) -> None: ...
    @typing.overload
    def setShort(self, short: int) -> None: ...
    def setShorts(self, shortArray: typing.List[int]) -> None: ...
    @typing.overload
    def setString(self, int: int, string: str) -> None: ...
    @typing.overload
    def setString(self, string: str) -> None: ...
    def setStrings(self, stringArray: typing.List[str]) -> None: ...
    def subArray(self, int: int, int2: int) -> cern.accsoft.commons.value.ScalarArray: ...

class ScalarArray2DImpl(ScalarArrayImpl, cern.accsoft.commons.value.ScalarArray2D):
    """
    public class ScalarArray2DImpl extends :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl` implements :class:`~cern.accsoft.commons.value.ScalarArray2D`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, type: cern.accsoft.commons.value.Type, simpleParameterValue: cern.japc.value.SimpleParameterValue): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarArrayImpl.equals`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl`
        
        
        """
        ...
    @typing.overload
    def execute(self, indexing: cern.accsoft.commons.value.spi.operation.Indexing) -> cern.accsoft.commons.value.ScalarArray:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Value.execute`
            Performs the operation on this value with the given value as second operand. This value is changed by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.execute` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarArrayImpl.execute`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl`
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.BinaryOperation`): the operation to perform
                value (:class:`~cern.accsoft.commons.value.ImmutableValue`): the second operand for the binary operation
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Value.execute`
            Performs the given operation on this value. This value is changed by the operation.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Value.execute` in interface :class:`~cern.accsoft.commons.value.Value`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarArrayImpl.execute`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl`
        
            Parameters:
                operation (:class:`~cern.accsoft.commons.value.operation.UnaryOperation`): the operation to perform
        
            Description copied from interface: :meth:`~cern.accsoft.commons.value.Indexed.execute`
            this method returns because the ValueType changes during execution
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Indexed.execute` in interface :class:`~cern.accsoft.commons.value.Indexed`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarArrayImpl.execute`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl`
        
            Returns:
                Scalar
        
        
        """
        ...
    @typing.overload
    def execute(self, binaryOperation: cern.accsoft.commons.value.operation.BinaryOperation, immutableValue: cern.accsoft.commons.value.ImmutableValue) -> None: ...
    @typing.overload
    def execute(self, unaryOperation: cern.accsoft.commons.value.operation.UnaryOperation) -> None: ...
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
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalarArray2D.getArray2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalarArray2D`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarArrayImpl.getArray2D`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl`
        
            Returns:
                the value being interpreted as a boolean 2d array.
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalarArray2D.getColumnCount`
            Returns the number of columns in this array 2d
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalarArray2D.getColumnCount`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalarArray2D`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarArrayImpl.getColumnCount`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl`
        
            Returns:
                the number of columns in this array 2d
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ImmutableScalarArray2D.getRowCount`
            Returns the number of rows in this array 2d
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableScalarArray2D.getRowCount`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalarArray2D`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarArrayImpl.getRowCount`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl`
        
            Returns:
                the number of rows in this array 2d
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarArrayImpl.hashCode`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl`
        
        
        """
        ...
    def makeMutable(self) -> cern.accsoft.commons.value.ScalarArray2D:
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
                :meth:`~cern.accsoft.commons.value.ImmutableScalarArray2D.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableScalarArray2D`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ImmutableValue.makeMutable`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ImmutableValue`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarArrayImpl.makeMutable`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl`
        
            Returns:
                a mutable deep copy of this value
        
        
        """
        ...
    def setBooleans2D(self, booleanArray: typing.List[bool], int: int, int2: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ScalarArray2D.setBooleans2D`
            Sets the value being a 2-dimetional boolean array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ScalarArray2D.setBooleans2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ScalarArray2D`
        
            Parameters:
                value (boolean[]): the boolean array value.
        
        
        """
        ...
    def setBytes2D(self, byteArray: typing.List[int], int: int, int2: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ScalarArray2D.setBytes2D`
            Sets the value being a 2-dimetional byte array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ScalarArray2D.setBytes2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ScalarArray2D`
        
            Parameters:
                value (byte[]): the byte array value.
        
        
        """
        ...
    def setDoubles2D(self, doubleArray: typing.List[float], int: int, int2: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ScalarArray2D.setDoubles2D`
            Sets the value being a 2-dimetional double array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ScalarArray2D.setDoubles2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ScalarArray2D`
        
            Parameters:
                value (double[]): the double array value.
        
        
        """
        ...
    def setFloats2D(self, floatArray: typing.List[float], int: int, int2: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ScalarArray2D.setFloats2D`
            Sets the value being a 2-dimetional float array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ScalarArray2D.setFloats2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ScalarArray2D`
        
            Parameters:
                value (float[]): the float array value.
        
        
        """
        ...
    def setInts2D(self, intArray: typing.List[int], int2: int, int3: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ScalarArray2D.setInts2D`
            Sets the value being a 2-dimetional int array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ScalarArray2D.setInts2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ScalarArray2D`
        
            Parameters:
                value (int[]): the int array value.
        
        
        """
        ...
    def setLongs2D(self, longArray: typing.List[int], int: int, int2: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ScalarArray2D.setLongs2D`
            Sets the value being a 2-dimetional long array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ScalarArray2D.setLongs2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ScalarArray2D`
        
            Parameters:
                value (long[]): the long array value.
        
        
        """
        ...
    def setObject(self, object: typing.Any) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ScalarArray.setObject`
            Sets the value as an object. This method can handle any scalar wrapping Object type as well as arrays and string. If
            other type was passed a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` will be
            thrown. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.Scalar.setObject` in interface :class:`~cern.accsoft.commons.value.Scalar`
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ScalarArray.setObject` in interface :class:`~cern.accsoft.commons.value.ScalarArray`
        
            Overrides:
                :meth:`~cern.accsoft.commons.value.spi.ScalarArrayImpl.setObject`Â in
                classÂ :class:`~cern.accsoft.commons.value.spi.ScalarArrayImpl`
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value as an object.
        
        
        """
        ...
    def setObjects2D(self, object: typing.Any, int: int, int2: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ScalarArray2D.setObjects2D`
            Sets the value as a 2d array of objects. This method can handle any array of primitives and Strings, which will be used
            as a source for 2D array. If other type was passed a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` will be
            thrown. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ScalarArray2D.setObjects2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ScalarArray2D`
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value as an object.
        
        
        """
        ...
    def setShorts2D(self, shortArray: typing.List[int], int: int, int2: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ScalarArray2D.setShorts2D`
            Sets the value being a 2-dimetional short array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ScalarArray2D.setShorts2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ScalarArray2D`
        
            Parameters:
                value (short[]): the short array value.
        
        
        """
        ...
    def setStrings2D(self, stringArray: typing.List[str], int: int, int2: int) -> None:
        """
            Description copied from interface: :meth:`~cern.accsoft.commons.value.ScalarArray2D.setStrings2D`
            Sets the value being a 2-dimetional String array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.accsoft.commons.value.ScalarArray2D.setStrings2D`Â in
                interfaceÂ :class:`~cern.accsoft.commons.value.ScalarArray2D`
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the String array value.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.accsoft.commons.value.spi")``.

    AbstractValue: typing.Type[AbstractValue]
    IOUtils: typing.Type[IOUtils]
    PointImpl: typing.Type[PointImpl]
    ScalarArray2DImpl: typing.Type[ScalarArray2DImpl]
    ScalarArrayImpl: typing.Type[ScalarArrayImpl]
    ScalarArrayView: typing.Type[ScalarArrayView]
    ScalarImpl: typing.Type[ScalarImpl]
    ValueDescriptorImpl: typing.Type[ValueDescriptorImpl]
    function: cern.accsoft.commons.value.spi.function.__module_protocol__
    operation: cern.accsoft.commons.value.spi.operation.__module_protocol__
