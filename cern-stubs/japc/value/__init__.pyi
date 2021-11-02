import cern.accsoft.commons.util
import cern.japc.value.factory
import cern.japc.value.spi
import java.io
import java.lang
import java.util
import typing



class Array2D:
    """
    public interface Array2D
    
        Interface describing a JAPC 2-dimentional array
    """
    def getArray1D(self) -> typing.Any:
        """
            Returns a flat array representing the 2D array as an Object.
        
            The return value is an array of elements of corresponding type (boolean[], byte[], double[], float[], int[], long[],
            short[] or String[])
        
            Returns:
                a flat array representing the 2D array.
        
        
        """
        ...
    def getBoolean(self, int: int, int2: int) -> bool:
        """
            Returns the value specified with the 2 indexes.
        
            Parameters:
                rowNumber (int): first index
                columnNumber (int): second index
        
            Returns:
                the value specified with the 2 indexes.
        
        
        """
        ...
    def getBooleanArray2D(self) -> typing.List[typing.List[bool]]:
        """
            Returns the 2-dimensional array
        
            Returns:
                the 2-dimensional array
        
        
        """
        ...
    def getBooleanRow(self, int: int) -> typing.List[bool]:
        """
            Returns the row specified with the index
        
            Parameters:
                rowNumber (int): the index of the row
        
            Returns:
                the row specified with the index
        
        
        """
        ...
    def getBooleans(self) -> typing.List[bool]:
        """
            Returns a flat array of booleans representing the 2D array.
        
        
            Returns:
                a flat array of booleans representing the 2D array.
        
        
        """
        ...
    def getByte(self, int: int, int2: int) -> int:
        """
            Returns the value specified with the 2 indexes.
        
            Parameters:
                rowNumber (int): first index
                columnNumber (int): second index
        
            Returns:
                the value specified with the 2 indexes.
        
        
        """
        ...
    def getByteArray2D(self) -> typing.List[typing.List[int]]:
        """
            Returns the 2-dimensional array
        
            Returns:
                the 2-dimensional array
        
        
        """
        ...
    def getByteRow(self, int: int) -> typing.List[int]:
        """
            Returns the row specified with the index
        
            Parameters:
                rowNumber (int): the index of the row
        
            Returns:
                the row specified with the index
        
        
        """
        ...
    def getBytes(self) -> typing.List[int]:
        """
            Returns a flat array of bytes representing the 2D array.
        
        
            Returns:
                a flat array of bytes representing the 2D array.
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
            Returns the number of columns.
        
            Returns:
                the number of columns.
        
        
        """
        ...
    def getDouble(self, int: int, int2: int) -> float:
        """
            Returns the value specified with the 2 indexes.
        
            Parameters:
                rowNumber (int): first index
                columnNumber (int): second index
        
            Returns:
                the value specified with the 2 indexes.
        
        
        """
        ...
    def getDoubleArray2D(self) -> typing.List[typing.List[float]]:
        """
            Returns the 2-dimensional array
        
            Returns:
                the 2-dimensional array
        
        
        """
        ...
    def getDoubleRow(self, int: int) -> typing.List[float]:
        """
            Returns the row specified with the index
        
            Parameters:
                rowNumber (int): the index of the row
        
            Returns:
                the row specified with the index
        
        
        """
        ...
    def getDoubles(self) -> typing.List[float]:
        """
            Returns a flat array of doubles representing the 2D array.
        
        
            Returns:
                a flat array of doubles representing the 2D array.
        
        
        """
        ...
    def getEnumItem(self, int: int, int2: int) -> 'EnumItem':
        """
            Returns the value specified with the 2 indexes.
        
            Parameters:
                rowNumber (int): first index
                columnNumber (int): second index
        
            Returns:
                the value specified with the 2 indexes.
        
        
        """
        ...
    def getEnumItemArray2D(self) -> typing.List[typing.List['EnumItem']]:
        """
            Returns the 2-dimensional array
        
            Returns:
                the 2-dimensional array
        
        
        """
        ...
    def getEnumItemRow(self, int: int) -> typing.List['EnumItem']:
        """
            Returns the row specified with the index
        
            Parameters:
                rowNumber (int): the index of the row
        
            Returns:
                the row specified with the index
        
        
        """
        ...
    def getEnumItemSet(self, int: int, int2: int) -> 'EnumItemSet':
        """
            Returns the value specified with the 2 indexes.
        
            Parameters:
                rowNumber (int): first index
                columnNumber (int): second index
        
            Returns:
                the value specified with the 2 indexes.
        
        
        """
        ...
    def getEnumItemSetArray2D(self) -> typing.List[typing.List['EnumItemSet']]:
        """
            Returns the 2-dimensional array
        
            Returns:
                the 2-dimensional array
        
        
        """
        ...
    def getEnumItemSetRow(self, int: int) -> typing.List['EnumItemSet']:
        """
            Returns the row specified with the index
        
            Parameters:
                rowNumber (int): the index of the row
        
            Returns:
                the row specified with the index
        
        
        """
        ...
    def getEnumItemSets(self) -> typing.List['EnumItemSet']:
        """
            Returns a flat array of enumeration sets representing the 2D array.
        
        
            Returns:
                a flat array of enumeration sets representing the 2D array.
        
        
        """
        ...
    def getEnumItems(self) -> typing.List['EnumItem']:
        """
            Returns a flat array of enumerations representing the 2D array.
        
        
            Returns:
                a flat array of enumerations representing the 2D array.
        
        
        """
        ...
    def getFloat(self, int: int, int2: int) -> float:
        """
            Returns the value specified with the 2 indexes.
        
            Parameters:
                rowNumber (int): first index
                columnNumber (int): second index
        
            Returns:
                the value specified with the 2 indexes.
        
        
        """
        ...
    def getFloatArray2D(self) -> typing.List[typing.List[float]]:
        """
            Returns the 2-dimensional array
        
            Returns:
                the 2-dimensional array
        
        
        """
        ...
    def getFloatRow(self, int: int) -> typing.List[float]:
        """
            Returns the row specified with the index
        
            Parameters:
                rowNumber (int): the index of the row
        
            Returns:
                the row specified with the index
        
        
        """
        ...
    def getFloats(self) -> typing.List[float]:
        """
            Returns a flat array of floats representing the 2D array.
        
        
            Returns:
                a flat array of floats representing the 2D array.
        
        
        """
        ...
    def getInt(self, int: int, int2: int) -> int:
        """
            Returns the value specified with the 2 indexes.
        
            Parameters:
                rowNumber (int): first index
                columnNumber (int): second index
        
            Returns:
                the value specified with the 2 indexes.
        
        
        """
        ...
    def getIntArray2D(self) -> typing.List[typing.List[int]]:
        """
            Returns the 2-dimensional array
        
            Returns:
                the 2-dimensional array
        
        
        """
        ...
    def getIntRow(self, int: int) -> typing.List[int]:
        """
            Returns the row specified with the index
        
            Parameters:
                rowNumber (int): the index of the row
        
            Returns:
                the row specified with the index
        
        
        """
        ...
    def getInternalComponentType(self) -> 'ValueType':
        """
            Returns the internal component type of the 2D array.
        
            This method returns the JAPC type of the elements in the array.
        
        
            Returns:
                the internal component type of the 2D array
        
        
        """
        ...
    def getInts(self) -> typing.List[int]:
        """
            Returns a flat array of integers representing the 2D array.
        
        
            Returns:
                a flat array of integers representing the 2D array.
        
        
        """
        ...
    def getLong(self, int: int, int2: int) -> int:
        """
            Returns the value specified with the 2 indexes.
        
            Parameters:
                rowNumber (int): first index
                columnNumber (int): second index
        
            Returns:
                the value specified with the 2 indexes.
        
        
        """
        ...
    def getLongArray2D(self) -> typing.List[typing.List[int]]:
        """
            Returns the 2-dimensional array
        
            Returns:
                the 2-dimensional array
        
        
        """
        ...
    def getLongRow(self, int: int) -> typing.List[int]:
        """
            Returns the row specified with the index
        
            Parameters:
                rowNumber (int): the index of the row
        
            Returns:
                the row specified with the index
        
        
        """
        ...
    def getLongs(self) -> typing.List[int]:
        """
            Returns a flat array of longs representing the 2D array.
        
        
            Returns:
                a flat array of longs representing the 2D array.
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
            Returns the number of rows.
        
            Returns:
                the number of rows.
        
        
        """
        ...
    def getShort(self, int: int, int2: int) -> int:
        """
            Returns the value specified with the 2 indexes.
        
            Parameters:
                rowNumber (int): first index
                columnNumber (int): second index
        
            Returns:
                the value specified with the 2 indexes.
        
        
        """
        ...
    def getShortArray2D(self) -> typing.List[typing.List[int]]:
        """
            Returns the 2-dimensional array
        
            Returns:
                the 2-dimensional array
        
        
        """
        ...
    def getShortRow(self, int: int) -> typing.List[int]:
        """
            Returns the row specified with the index
        
            Parameters:
                rowNumber (int): the index of the row
        
            Returns:
                the row specified with the index
        
        
        """
        ...
    def getShorts(self) -> typing.List[int]:
        """
            Returns a flat array of shorts representing the 2D array.
        
        
            Returns:
                a flat array of shorts representing the 2D array.
        
        
        """
        ...
    def getString(self, int: int, int2: int) -> str:
        """
            Returns the value specified with the 2 indexes.
        
            Parameters:
                rowNumber (int): first index
                columnNumber (int): second index
        
            Returns:
                the value specified with the 2 indexes.
        
        
        """
        ...
    def getStringArray2D(self) -> typing.List[typing.List[str]]:
        """
            Returns the 2-dimensional array
        
            Returns:
                the 2-dimensional array
        
        
        """
        ...
    def getStringRow(self, int: int) -> typing.List[str]:
        """
            Returns the row specified with the index
        
            Parameters:
                rowNumber (int): the index of the row
        
            Returns:
                the row specified with the index
        
        
        """
        ...
    def getStrings(self) -> typing.List[str]:
        """
            Returns a flat array of strings representing the 2D array.
        
        
            Returns:
                a flat array of strings representing the 2D array.
        
        
        """
        ...

class Array2DBuilder:
    """
    public class Array2DBuilder extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        A builder for 2D array values.
    """
    @typing.overload
    def __init__(self, array2D: Array2D): ...
    @typing.overload
    def __init__(self, valueType: 'ValueType', intArray: typing.List[int]): ...
    def build(self) -> Array2D:
        """
            Builds an :class:`~cern.japc.value.Array2D` instance.
        
            Returns:
                an :class:`~cern.japc.value.Array2D` instance
        
        
        """
        ...
    def setBoolean(self, boolean: bool, int: int, int2: int) -> 'Array2DBuilder':
        """
            Sets a boolean.
        
            Parameters:
                value (boolean): boolean value
                rowIndex (int): row index, 0-based
                columnIndex (int): column index, 0-based
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def setByte(self, byte: int, int: int, int2: int) -> 'Array2DBuilder':
        """
            Sets a byte.
        
            Parameters:
                value (byte): byte value
                rowIndex (int): row index, 0-based
                columnIndex (int): column index, 0-based
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def setDouble(self, double: float, int: int, int2: int) -> 'Array2DBuilder':
        """
            Sets a double.
        
            Parameters:
                value (double): double value
                rowIndex (int): row index, 0-based
                columnIndex (int): column index, 0-based
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def setEnumItem(self, enumItem: 'EnumItem', int: int, int2: int) -> 'Array2DBuilder':
        """
            Sets an enumeration item.
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItem`): enumeration item value
                rowIndex (int): row index, 0-based
                columnIndex (int): column index, 0-based
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def setEnumItemSet(self, enumItemSet: 'EnumItemSet', int: int, int2: int) -> 'Array2DBuilder':
        """
            Sets an enumeration items set.
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItemSet`): enumeration items set value
                rowIndex (int): row index, 0-based
                columnIndex (int): column index, 0-based
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def setFloat(self, float: float, int: int, int2: int) -> 'Array2DBuilder':
        """
            Sets a float.
        
            Parameters:
                value (float): float value
                rowIndex (int): row index, 0-based
                columnIndex (int): column index, 0-based
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def setInt(self, int: int, int2: int, int3: int) -> 'Array2DBuilder':
        """
            Sets a integer.
        
            Parameters:
                value (int): integer value
                rowIndex (int): row index, 0-based
                columnIndex (int): column index, 0-based
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def setLong(self, long: int, int: int, int2: int) -> 'Array2DBuilder':
        """
            Sets a long.
        
            Parameters:
                value (long): long value
                rowIndex (int): row index, 0-based
                columnIndex (int): column index, 0-based
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def setShort(self, short: int, int: int, int2: int) -> 'Array2DBuilder':
        """
            Sets a short.
        
            Parameters:
                value (short): short value
                rowIndex (int): row index, 0-based
                columnIndex (int): column index, 0-based
        
            Returns:
                this builder for chaining
        
        
        """
        ...
    def setString(self, string: str, int: int, int2: int) -> 'Array2DBuilder':
        """
            Sets a string.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): string value
                rowIndex (int): row index, 0-based
                columnIndex (int): column index, 0-based
        
            Returns:
                this builder for chaining
        
        
        """
        ...

class BooleanItem:
    """
    public interface BooleanItem
    
        This interface represents a generic boolean item.
    
        Generally speaking a boolean item has a boolean value associated with
        :class:`~cern.japc.value.SimpleValueStandardMeaning`.
    """
    def getStandardMeaning(self) -> 'SimpleValueStandardMeaning':
        """
            Returns the meaning of this boolean item
        
            Returns:
                the meaning of this boolean item
        
        
        """
        ...
    def getValue(self) -> bool:
        """
            Returns the boolean value of this boolean item
        
            Returns:
                the boolean value of this boolean item
        
        
        """
        ...

class BooleanType(cern.accsoft.commons.util.Named):
    """
    public interface BooleanType extends cern.accsoft.commons.util.Named
    
        This interface represents a boolean type. Each boolean type has a unique name and is comprised of two
        :class:`~cern.japc.value.BooleanItem`'s (true/false).
    """
    def getName(self) -> str:
        """
            Returns the name of the boolean type.
        
            **The name must be unique**.
        
            Specified by:
                :code:`getName` in interface :code:`cern.accsoft.commons.util.Named`
        
            Returns:
                the name of the boolean type
        
        
        """
        ...
    def valueOf(self, boolean: bool) -> BooleanItem:
        """
            Returns the :class:`~cern.japc.value.BooleanItem` corresponding to the boolean value.
        
            Parameters:
                value (boolean): a boolean value
        
            Returns:
                the :class:`~cern.japc.value.BooleanItem` corresponding to the boolean value
        
        
        """
        ...
    def values(self) -> java.util.Set[BooleanItem]: ...

class DiscreteFunction(java.lang.Cloneable):
    """
    public interface DiscreteFunction extends `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Defines a discrete function. A discrete function is a list of points strictly ordered by their x-coordinates.
    
        A discrete function can support gap. A gap is an undefined part in the discrete function with no value. A gap is created
        by having an y value equals to Double.NaN. For instance, if p1(x1, y1), p2(x2, Double.NaN) and p3(x3, y3) are 3
        successive points, the part between x1 and x3 is undefined.
    """
    def clone(self) -> 'DiscreteFunction':
        """
            Returns a deep copy of this discrete function. The copy is guarantee to be deep.
        
            Returns:
                a deep copy of this discrete function.
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def getX(self, int: int) -> float:
        """
            Returns the x-coordinate of the point defined with the :code:`index` argument (the index goes from 0 to size-1).
        
            Parameters:
                index (int): the index of the point
        
            Returns:
                the x-coordinate of the point
        
        
        """
        ...
    def getY(self, int: int) -> float:
        """
            Returns the y-coordinate of the point defined with the :code:`index` argument (the index goes from 0 to size-1).
        
            Parameters:
                index (int): the index of the point
        
            Returns:
                the y-coordinate of the point
        
        
        """
        ...
    def size(self) -> int:
        """
            Returns the number of points that defines this function.
        
            Returns:
                the number of points defining this function.
        
        
        """
        ...
    def toXArray(self) -> typing.List[float]:
        """
            Returns all x-coordinates of this function (the index goes from 0 to size-1). The array returned is a copy of the
            internal representation. Any modification of this array does not affect this function.
        
            Returns:
                all x-coordinates of this function
        
        
        """
        ...
    def toYArray(self) -> typing.List[float]:
        """
            Returns all y-coordinates of this function (the index goes from 0 to size-1). The array returned is a copy of the
            internal representation. Any modification of this array does not affect this function.
        
            Returns:
                all y-coordinates of this function
        
        
        """
        ...

class DiscreteFunctionList(java.lang.Cloneable):
    """
    public interface DiscreteFunctionList extends `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Interface for a list of discrete functions.
    """
    def clone(self) -> 'DiscreteFunctionList':
        """
            Returns a deep copy of this discrete function list. The copy is guarantee to be deep.
        
            Returns:
                a deep copy of this discrete function list.
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def getFunction(self, int: int) -> DiscreteFunction:
        """
            Returns a function specified with its index in the list
        
            Parameters:
                index (int): the index of the function
        
            Returns:
                a function corresponding to the index
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator[DiscreteFunction]: ...
    def size(self) -> int:
        """
            Returns the number of functions in the list.
        
            Returns:
                the number of functions in the list
        
        
        """
        ...

class EnumItem(java.lang.Comparable['EnumItem']):
    """
    public interface EnumItem extends `Comparable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Comparable.html?is-external=true>`<:class:`~cern.japc.value.EnumItem`>
    
        This interface represents a generic item of an enumeration.
    
        Generally speaking an enumeration item has an integer value and a symbol associated with it.
    
        Such enumeration items are used for the property fields which values:
    
          - can be one value of a predefined set in a time
          - can be several (including 0) values of a predefined set in a time
    """
    def getCode(self) -> int:
        """
            Returns an integer code of this enumeration item
        
            Returns:
                an integer code of this enumeration item
        
        
        """
        ...
    def getEnumType(self) -> 'EnumType':
        """
            Returns the enumeration type this item belongs to.
        
            Returns:
                the enumeration type this item belongs to
        
        
        """
        ...
    def getStandardMeaning(self) -> 'SimpleValueStandardMeaning':
        """
            Returns the meaning of this enumeration item
        
            Returns:
                the meaning of this enumeration item
        
        
        """
        ...
    def getString(self) -> str: ...
    def getSymbol(self) -> str:
        """
            Returns a symbol of this enumeration item
        
            Returns:
                a symbol of this enumeration item
        
        
        """
        ...
    def isSettable(self) -> bool:
        """
            Returns :code:`true` if this enumeration item is settable.
        
            Returns:
                :code:`true` if this enumeration item is settable
        
        
        """
        ...

class EnumItemSet(java.util.Set[EnumItem], java.lang.Cloneable):
    """
    public interface EnumItemSet extends `Set <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Set.html?is-external=true>`<:class:`~cern.japc.value.EnumItem`>, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        This interface represents a set of :class:`~cern.japc.value.EnumItem`'s.
    
        Such a set corresponds to a field value which is called "bit-enum" in FESA world.
    """
    @typing.overload
    def addAll(self, enumItemArray: typing.List[EnumItem]) -> bool:
        """
            Syntactical sugar around `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true#addAll(java.util.Collection)>`
            method.
        
            Parameters:
                enumItems (:class:`~cern.japc.value.EnumItem`...): enumeration items to add
        
            Returns:
                ``true`` if this set changed as a result of the call
        
        
        """
        ...
    @typing.overload
    def addAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def asLong(self) -> int:
        """
            Returns the set encoded into a long.
        
            Returns:
                a long corresponding to the set
        
        
        """
        ...
    def clone(self) -> 'EnumItemSet':
        """
            Returns a deep copy of this set. The copy is guarantee to be deep.
        
            Returns:
                a deep copy of this set.
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    @typing.overload
    def containsAll(self, enumItemArray: typing.List[EnumItem]) -> bool:
        """
            Syntactical sugar around `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true#containsAll(java.util.Collection)>`
            method.
        
            Parameters:
                enumItems (:class:`~cern.japc.value.EnumItem`...): enumeration items to check for
        
            Returns:
                ``true`` if this set contains all of the elements
        
        
        """
        ...
    @typing.overload
    def containsAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getEnumType(self) -> 'EnumType':
        """
            Returns the enumeration type of this set.
        
            Returns:
                the enumeration type of this set
        
        
        """
        ...
    def hashCode(self) -> int: ...
    @typing.overload
    def removeAll(self, enumItemArray: typing.List[EnumItem]) -> bool:
        """
            Syntactical sugar around `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true#removeAll(java.util.Collection)>`
            method.
        
            Parameters:
                enumItems (:class:`~cern.japc.value.EnumItem`...): enumeration items to add
        
            Returns:
                ``true`` if this set changed as a result of the call
        
        
        """
        ...
    @typing.overload
    def removeAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    @typing.overload
    def retainAll(self, enumItemArray: typing.List[EnumItem]) -> bool:
        """
            Syntactical sugar around `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true#retainAll(java.util.Collection)>`
            method.
        
            Parameters:
                enumItems (:class:`~cern.japc.value.EnumItem`...): enumeration items to add
        
            Returns:
                ``true`` if this set changed as a result of the call
        
        
        """
        ...
    @typing.overload
    def retainAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...

class EnumType:
    """
    public interface EnumType
    
        This interface represents an enumeration type. Each enumeration type has a unique name and is comprised of a set of
        :class:`~cern.japc.value.EnumItem`'s.
    """
    def getBitSize(self) -> 'EnumTypeBitSize':
        """
            Returns the form of low-level representation of values: byte, short, int or long.
        
            Returns:
                the form of low-level representation of values
        
        
        """
        ...
    def getName(self) -> str:
        """
            Returns the name of the enumeration.
        
            **The name must be unique**. So it must follow the naming convention: <device type>/<enum name>.
        
            Returns:
                the name of the enumeration
        
        
        """
        ...
    def isApplicableToEnumItemSet(self) -> bool:
        """
            Returns true if this enumeration type can be used for an enum item set and false otherwise.
        
            Only those enum types can be used in an enum item sets which items has only powers of 2 as their codes.
        
            Returns:
                true if this enumeration type can be used for an enum item set and false otherwise
        
        
        """
        ...
    def symbols(self) -> java.util.Collection[str]: ...
    @typing.overload
    def valueOf(self, string: str) -> EnumItem:
        """
            Returns the :class:`~cern.japc.value.EnumItem` corresponding to the symbol.
        
            Parameters:
                symbol (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): symbol
        
            Returns:
                the :class:`~cern.japc.value.EnumItem` corresponding to the symbol
        
            Returns the :class:`~cern.japc.value.EnumItem` corresponding to the code.
        
            Parameters:
                code (long): a code
        
            Returns:
                the :class:`~cern.japc.value.EnumItem` corresponding to the code
        
        
        """
        ...
    @typing.overload
    def valueOf(self, long: int) -> EnumItem: ...
    def valueStrings(self) -> java.util.Collection[str]: ...
    def values(self) -> java.util.Set[EnumItem]: ...

class EnumTypeBitSize(java.lang.Enum['EnumTypeBitSize']):
    """
    public enum EnumTypeBitSize extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.japc.value.EnumTypeBitSize`>
    
        The low level representation of the values of an enumeration type.
    """
    BYTE: typing.ClassVar['EnumTypeBitSize'] = ...
    SHORT: typing.ClassVar['EnumTypeBitSize'] = ...
    INT: typing.ClassVar['EnumTypeBitSize'] = ...
    LONG: typing.ClassVar['EnumTypeBitSize'] = ...
    STRING: typing.ClassVar['EnumTypeBitSize'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'EnumTypeBitSize':
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
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['EnumTypeBitSize']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (EnumTypeBitSize c : EnumTypeBitSize.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class ParameterValue(java.lang.Cloneable):
    """
    public interface ParameterValue extends `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        A class implementing this interface holds the value of a parameter. Concrete implementation of the interface should
        provide specific methods that can be used to read the value.
    
        A parameter value can be mutable, it can be modified, or immutable when it cannot be modified. The producer of the value
        can decide whether the value is mutable or not depending on the way the value is shared by clients.
    """
    def castAsMap(self) -> 'MapParameterValue':
        """
            Returns this value casted as a :class:`~cern.japc.value.MapParameterValue`
        
            Returns:
                this value casted as a :class:`~cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def castAsSimple(self) -> 'SimpleParameterValue':
        """
            Returns this value casted as a :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                this value casted as a :class:`~cern.japc.value.SimpleParameterValue`
        
        
        """
        ...
    def clone(self) -> typing.Any:
        """
            Returns a deep copy of this ParameterValue. The copy is guarantee to be deep.
        
            Returns:
                a deep copy of this ParameterValue.
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def getString(self) -> str:
        """
            Returns the value as a string. This method should be specially useful for client that just want to display the value
            without any interpretation. The string returned should be as useful as possible for the clients.
        
            Returns:
                a string representing the value as a string.
        
        
        """
        ...
    def getType(self) -> 'Type':
        """
            Returns the type of this value
        
            Returns:
                the type of this value
        
        
        """
        ...
    def isMutable(self) -> bool:
        """
            Returns true is this ParameterValue is mutable. If the ParameterValue is not mutable, a mutable version can be by
            calling the method :code:`makeMutable:code:`. Any attempt to change this ParameterValue if is is mutable will result in
            an exception being thrown by the method attempting the modification (such as a setter).``
        
            Returns:
              whether this parameter value is mutable or not
        
        
        """
        ...
    def makeImmutable(self) -> None:
        """
            Makes this ParameterValue immutable. The original values are untouched by this operation. If this ParameterValue is
            already immutable this method has no effect. Once a parameter value has been made immutable it cannot be made mutable
            anymore unless a copy is created using the method :code:`makeMutable`. Any call to a method attempting to modify an
            immutable parameter will result into an exception.
        
        """
        ...
    def makeMutable(self) -> 'ParameterValue':
        """
            Creates a mutable version of this ParameterValue that can be set using the setters. The original values are untouched by
            this operation. If this ParameterValue is already mutable this method returns the same instance.
        
            Returns:
                A new mutable copy of this parameter value or this parameter value itself if it is already mutable.
        
        
        """
        ...

class SimpleValueControlStatus(java.lang.Enum['SimpleValueControlStatus']):
    """
    public enum SimpleValueControlStatus extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.japc.value.SimpleValueControlStatus`>
    
        Control status of a simple value (field of a map value).
    
        It is introduced to fulfill general purpose requirements coming from INCA project.
    """
    OK: typing.ClassVar['SimpleValueControlStatus'] = ...
    WARNING: typing.ClassVar['SimpleValueControlStatus'] = ...
    ERROR: typing.ClassVar['SimpleValueControlStatus'] = ...
    NONE: typing.ClassVar['SimpleValueControlStatus'] = ...
    INACTIVE: typing.ClassVar['SimpleValueControlStatus'] = ...
    OFF: typing.ClassVar['SimpleValueControlStatus'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SimpleValueControlStatus':
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
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['SimpleValueControlStatus']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SimpleValueControlStatus c : SimpleValueControlStatus.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SimpleValueStandardMeaning(java.lang.Enum['SimpleValueStandardMeaning']):
    """
    public enum SimpleValueStandardMeaning extends `Enum <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Enum.html?is-external=true>`<:class:`~cern.japc.value.SimpleValueStandardMeaning`>
    
        Standard meanings of simple parameter values.
    
        It is introduced to fulfill general purpose requirements coming from INCA project.
    """
    ON: typing.ClassVar['SimpleValueStandardMeaning'] = ...
    OFF: typing.ClassVar['SimpleValueStandardMeaning'] = ...
    WARNING: typing.ClassVar['SimpleValueStandardMeaning'] = ...
    ERROR: typing.ClassVar['SimpleValueStandardMeaning'] = ...
    NONE: typing.ClassVar['SimpleValueStandardMeaning'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SimpleValueStandardMeaning':
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
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.List['SimpleValueStandardMeaning']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (SimpleValueStandardMeaning c : SimpleValueStandardMeaning.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SimpleValueStatus(java.io.Serializable, java.lang.Cloneable):
    """
    public class SimpleValueStatus extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        This class represents the information associated with the status of an acquired value. It is taken from middleware
        through the field fieldName_status. It represents the AQN_STATUS bit enum type described in chapter 5.3.1 of "GUIDELINES
        AND CONVENTIONS FOR DEFINING INTERFACES OF EQUIPMENT DEVELOPED USING FESA"
    
        Also see:
            "https://edms.cern.ch/file/581892/1.1/LeirPropertyGuildelines-final-1.0.1.pdf", :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, long: int): ...
    @typing.overload
    def __init__(self, long: int, simpleValueControlStatus: SimpleValueControlStatus): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getAqnStatus(self) -> int:
        """
            Returns the ACN_STATUS bit-pattern.
        
            Returns:
                the ACN_STATUS bit-pattern
        
        
        """
        ...
    def getControlStatus(self) -> SimpleValueControlStatus:
        """
            Returns the control status for the simple value.
        
            Returns:
                the control status for the simple value
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isBadQuality(self) -> bool:
        """
            Returns the value of BAD_QUALITY flag.
        
            Returns:
                the value of BAD_QUALITY flag
        
        
        """
        ...
    def isBusy(self) -> bool:
        """
            Returns the value of BUSY flag.
        
            Returns:
                the value of BUSY flag
        
        
        """
        ...
    def isDifferentFromSetting(self) -> bool:
        """
            Returns the value of DIFFERENT_FROM_SETTING flag.
        
            Returns:
                the value of DIFFERENT_FROM_SETTING flag
        
        
        """
        ...
    def isNotOk(self) -> bool:
        """
            Returns the value of NOT_OK flag.
        
            Returns:
                the value of NOT_OK flag
        
        
        """
        ...
    def isOutOfRange(self) -> bool:
        """
            Returns the value of OUT_OF_RANGE flag.
        
            Returns:
                the value of OUT_OF_RANGE flag
        
        
        """
        ...
    def isTimeout(self) -> bool:
        """
            Returns the value of TIMEOUT flag.
        
            Returns:
                the value of TIMEOUT flag
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class Type(java.io.Serializable):
    """
    public class Type extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        A class implementing this interface represents an entity linked to the type of a value. A limited number of types are
        standardized. The value interval from 0 to 100 is reserved. Sub interfaces or implementations may return a non standard
        type providing that the client support that specific type.
    
        Also see:
            :meth:`~serialized`
    """
    SIMPLE: typing.ClassVar['Type'] = ...
    """
    public static final :class:`~cern.japc.value.Type` SIMPLE
    
        The value holds a simple type (not composite) that is a scalar, an array of scalars, a String or an array of Strings
    
    """
    MAP: typing.ClassVar['Type'] = ...
    """
    public static final :class:`~cern.japc.value.Type` MAP
    
        The value holds a map of named simple values (as defined above).
    
    """
    OBJECT: typing.ClassVar['Type'] = ...
    """
    public static final :class:`~cern.japc.value.Type` OBJECT
    
        The value holds an arbitrary
    
    """
    def getName(self) -> str:
        """
        
            Returns:
                type name
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns the type as a String. The type can be one of the enumerated values defined in this class.
        
            Overrides:
                 in class 
        
            Returns:
                A string corresponding to the type
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(int: int) -> 'Type':
        """
            Returns the type from its name. The id can be one of the legal value of the type names.
        
            Parameters:
                typeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the type to return
        
            Returns:
                the type identified by the name
        
            Returns the type from its id. The id can be one of the legal value of the type ids.
        
            Parameters:
                id (int): the id of the type to return
        
            Returns:
                the type identified by the id
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Type': ...

class ValueConversionException(java.lang.RuntimeException):
    """
    public class ValueConversionException extends `RuntimeException <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>`
    
        Thrown when a problem occurs with a convertion of value with a reader.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, exception: java.lang.Exception): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ValueDescriptor:
    """
    public interface ValueDescriptor
    
        A class implementing this interface provides a description of a value. The description provides meta information that
        can be used to interpret the value.
    """
    def castAsMap(self) -> 'MapDescriptor':
        """
            Returns this descriptor casted as a :class:`~cern.japc.value.MapDescriptor`
        
            Returns:
                this descriptor casted as a :class:`~cern.japc.value.MapDescriptor`
        
        
        """
        ...
    def castAsSimple(self) -> 'SimpleDescriptor':
        """
            Returns this descriptor casted as a :class:`~cern.japc.value.SimpleDescriptor`
        
            Returns:
                this descriptor casted as a :class:`~cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getType(self) -> Type:
        """
            Returns the type of this value
        
            Returns:
                the type of this value
        
        
        """
        ...
    def isConstant(self) -> bool:
        """
            Returns true if the value described by this descriptor is constant and never change during the life of this parameter.
            The default value is false.
        
            Returns:
                true if the value described by this descriptor is constant.
        
        
        """
        ...

class ValueStatus(java.io.Serializable):
    """
    public class ValueStatus extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class represents the information associated with the status of a value.
    
        Also see:
            :meth:`~serialized`
    """
    NONE: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` NONE
    
        Enumerated status value : NONE
    
    """
    UNDEFINED: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` UNDEFINED
    
        Enumerated status value : UNDEFINED
    
    """
    WARNING: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` WARNING
    
        Enumerated status value : WARNING
    
    """
    ERROR: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` ERROR
    
        Enumerated status value : ERROR
    
    """
    ON: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` ON
    
        Enumerated status value : ON
    
    """
    STAND_BY: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` STAND_BY
    
        Enumerated status value : STAND BY
    
    """
    OFF: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` OFF
    
        Enumerated status value : OFF
    
    """
    DIFFERS_FROM_CONTROL: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` DIFFERS_FROM_CONTROL
    
        Enumerated status value : NOT EQUALS TO CONTROL
    
    """
    OUT_OF_TOLERANCE: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` OUT_OF_TOLERANCE
    
        Enumerated status value : OUT OF TOLERANCE
    
    """
    ILLEGAL: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` ILLEGAL
    
        Enumerated status value : ILLEGAL
    
    """
    COM_ERROR: typing.ClassVar['ValueStatus'] = ...
    """
    public static final :class:`~cern.japc.value.ValueStatus` COM_ERROR
    
        Enumerated status value : COM_ERROR
    
    """
    @staticmethod
    def convertToValueStatus(int: int) -> 'ValueStatus':
        """
            Returns a ValueStatus object representation of the int error code passed in parameter.
        
            Parameters:
                status (int): The hardware status to be converted in ValueStatus.
        
            Returns:
                A ValueStatus object representation of the int error code passed in parameter.
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @staticmethod
    def mergeValueStatus(valueStatus: 'ValueStatus', valueStatus2: 'ValueStatus') -> 'ValueStatus':
        """
            Merges two status into one based on their level of importance. The most critical status is the one kept by this method.
        
            Parameters:
                valueStatus1 (:class:`~cern.japc.value.ValueStatus`): the first value status
                valueStatus2 (:class:`~cern.japc.value.ValueStatus`): the second value status
        
            Returns:
                the resulting most critical status
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns the value's status as a String. The status value can be one of the enumerated values defined in this interface.
        
            Overrides:
                 in class 
        
            Returns:
                A string corresponding to the status value
        
        
        """
        ...

class ValueType(java.io.Serializable):
    """
    public class ValueType extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class provides an enumeration of the supported simple value types
    
        Also see:
            :meth:`~serialized`
    """
    UNDEFINED: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` UNDEFINED
    
        value type when a problem occurs
    
    """
    BOOLEAN: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` BOOLEAN
    
        value type for boolean
    
    """
    BYTE: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` BYTE
    
        value type for byte
    
    """
    DOUBLE: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` DOUBLE
    
        value type for double
    
    """
    FLOAT: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` FLOAT
    
        value type for float
    
    """
    INT: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` INT
    
        value type for int
    
    """
    LONG: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` LONG
    
        value type for long
    
    """
    SHORT: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` SHORT
    
        value type for short
    
    """
    STRING: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` STRING
    
        value type for string
    
    """
    BOOLEAN_ARRAY: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` BOOLEAN_ARRAY
    
        value type for boolean array
    
    """
    BYTE_ARRAY: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` BYTE_ARRAY
    
        value type for byte array
    
    """
    DOUBLE_ARRAY: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` DOUBLE_ARRAY
    
        value type for double array
    
    """
    FLOAT_ARRAY: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` FLOAT_ARRAY
    
        value type for float array
    
    """
    INT_ARRAY: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` INT_ARRAY
    
        value type for int array
    
    """
    LONG_ARRAY: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` LONG_ARRAY
    
        value type for long array
    
    """
    SHORT_ARRAY: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` SHORT_ARRAY
    
        value type for short array
    
    """
    STRING_ARRAY: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` STRING_ARRAY
    
        value type for string array
    
    """
    BOOLEAN_ARRAY_2D: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` BOOLEAN_ARRAY_2D
    
        value type for boolean 2d array
    
    """
    BYTE_ARRAY_2D: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` BYTE_ARRAY_2D
    
        value type for byte 2d array
    
    """
    DOUBLE_ARRAY_2D: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` DOUBLE_ARRAY_2D
    
        value type for double 2d array
    
    """
    FLOAT_ARRAY_2D: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` FLOAT_ARRAY_2D
    
        value type for float 2d array
    
    """
    INT_ARRAY_2D: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` INT_ARRAY_2D
    
        value type for int 2d array
    
    """
    LONG_ARRAY_2D: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` LONG_ARRAY_2D
    
        value type for long 2d array
    
    """
    SHORT_ARRAY_2D: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` SHORT_ARRAY_2D
    
        value type for short 2d array
    
    """
    STRING_ARRAY_2D: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` STRING_ARRAY_2D
    
        value type for string 2d array
    
    """
    ENUM: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` ENUM
    
        value type for enumeration
    
    """
    ENUM_SET: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` ENUM_SET
    
        value type for enumeration set
    
    """
    DISCRETE_FUNCTION: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` DISCRETE_FUNCTION
    
        value type for discrete function
    
    """
    DISCRETE_FUNCTION_LIST: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` DISCRETE_FUNCTION_LIST
    
        value type for discrete function list
    
    """
    ENUM_ARRAY: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` ENUM_ARRAY
    
        value type for enumeration array
    
    """
    ENUM_SET_ARRAY: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` ENUM_SET_ARRAY
    
        value type for enumeration set array
    
    """
    ENUM_ARRAY_2D: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` ENUM_ARRAY_2D
    
        value type for enumeration 2d array
    
    """
    ENUM_SET_ARRAY_2D: typing.ClassVar['ValueType'] = ...
    """
    public static final :class:`~cern.japc.value.ValueType` ENUM_SET_ARRAY_2D
    
        value type for enumeration set 2d array
    
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getComponentType(self) -> 'ValueType':
        """
            Returns the internal component value type.
        
            If the value type is array then corresponding component type is returned. If the value type is scalar then itself is
            returned.
        
            Returns:
                the internal component value type
        
        
        """
        ...
    @staticmethod
    def getInternalComponentType(valueType: 'ValueType') -> 'ValueType':
        """
            Returns the internal component value type.
        
            If the value type is array then corresponding component type is returned. If the value type is scalar then itself is
            returned.
        
            Parameters:
                valueType (:class:`~cern.japc.value.ValueType`): the value type t analyze
        
            Returns:
                the internal component value type
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def isArray(self) -> bool:
        """
            Returns true if this value type is an array (an array 2D is an array)
        
            Returns:
                true if this value type is an array
        
        
        """
        ...
    def isArray2d(self) -> bool:
        """
            Returns true if this value type is a 2-dimensional array
        
            Returns:
                true if this value type is a 2-dimensional array
        
        
        """
        ...
    @staticmethod
    def isArray2dType(valueType: 'ValueType') -> bool:
        """
            Returns true if the value type is array 2D.
        
            Parameters:
                valueType (:class:`~cern.japc.value.ValueType`): value type
        
            Returns:
                true if the value type is array 2D
        
        
        """
        ...
    @staticmethod
    def isArrayType(valueType: 'ValueType') -> bool:
        """
            Returns true if the value type is array or array 2D.
        
            Parameters:
                valueType (:class:`~cern.japc.value.ValueType`): value type
        
            Returns:
                true if the value type is array or array 2D
        
        
        """
        ...
    def isBoolean(self) -> bool:
        """
            Returns :code:`true` if the value type is a :meth:`~cern.japc.value.ValueType.BOOLEAN` or array of those.
        
            Returns:
                :code:`true` if the value type is a :meth:`~cern.japc.value.ValueType.BOOLEAN` or array of those
        
        
        """
        ...
    @staticmethod
    def isBooleanType(valueType: 'ValueType') -> bool:
        """
            Returns :code:`true` if the value type is a :meth:`~cern.japc.value.ValueType.BOOLEAN` or array of those.
        
            Parameters:
                valueType (:class:`~cern.japc.value.ValueType`): value type
        
            Returns:
                :code:`true` if the value type is a :meth:`~cern.japc.value.ValueType.BOOLEAN` or array of those
        
        
        """
        ...
    def isEnumeric(self) -> bool:
        """
            Returns :code:`true` if the value type is an :meth:`~cern.japc.value.ValueType.ENUM`,
            :meth:`~cern.japc.value.ValueType.ENUM_SET` or array of those.
        
            Returns:
                :code:`true` if the value type is an :meth:`~cern.japc.value.ValueType.ENUM`,
                :meth:`~cern.japc.value.ValueType.ENUM_SET` or array of those
        
        
        """
        ...
    @staticmethod
    def isEnumericType(valueType: 'ValueType') -> bool:
        """
            Returns :code:`true` if the value type is an :meth:`~cern.japc.value.ValueType.ENUM`,
            :meth:`~cern.japc.value.ValueType.ENUM_SET` or array of those.
        
            Parameters:
                valueType (:class:`~cern.japc.value.ValueType`): value type
        
            Returns:
                :code:`true` if the value type is an :meth:`~cern.japc.value.ValueType.ENUM`,
                :meth:`~cern.japc.value.ValueType.ENUM_SET` or array of those
        
        
        """
        ...
    def isNumeric(self) -> bool:
        """
            Returns true if this value type is numeric and false otherwise
        
            Returns:
                true if this value type is numeric and false otherwise
        
        
        """
        ...
    @staticmethod
    def isNumericType(valueType: 'ValueType') -> bool:
        """
            Returns true if type is numeric and false otherwise
        
            Parameters:
                valueType (:class:`~cern.japc.value.ValueType`): type to test
        
            Returns:
                true if type is numeric and false otherwise
        
        
        """
        ...
    def isScalar(self) -> bool:
        """
            Returns true if this value type is an scalar type
        
            Returns:
                true if this value type is an scalar type
        
        
        """
        ...
    @staticmethod
    def isScalarType(valueType: 'ValueType') -> bool:
        """
            Returns true if the value type is scalar.
        
            Parameters:
                valueType (:class:`~cern.japc.value.ValueType`): value type
        
            Returns:
                true if the value type is scalar
        
        
        """
        ...
    def toString(self) -> str:
        """
            Returns the value type as a String. The value type can be one of the enumerated values defined in this class.
        
            Overrides:
                 in class 
        
            Returns:
                A string corresponding to the value type
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(int: int) -> 'ValueType':
        """
            Returns the value type from its name. The name can be one of the legal value of the value type names.
        
            Parameters:
                valueTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value type to return
        
            Returns:
                the value type identified by the name
        
            Returns the value type from its id. The id can be one of the legal value of the value type ids.
        
            Parameters:
                id (int): the id of the value type to return
        
            Returns:
                the value type identified by the id
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ValueType': ...

class ImmutableMapParameterValue(ParameterValue):
    """
    public interface ImmutableMapParameterValue extends :class:`~cern.japc.value.ParameterValue`
    
        A class implementing this interface provides method to interpret a set of named simple values.
    
        This interface represents an immutable set of names simple values.
    
        A call to any of the method of this interface with a name that does not exist will throw an
        :class:`~cern.japc.value.ValueConversionException`.
    """
    def get(self, string: str) -> 'SimpleParameterValue':
        """
            Returns the matching value for the given name
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
        
            Returns:
                the matching value for the given name or null if no match
        
        
        """
        ...
    def getArray2D(self, string: str) -> Array2D:
        """
            Returns a wrapper around the the value being interpreted as a 2d array. If the value is a 1d array it is encapsulated in
            an array of size 1xn. If the value is not an array it is encapsulated in an array of size 1x1. If the name does not
            match any value an :class:`~cern.japc.value.ValueConversionException` is thrown. IMPORTANT: if the value is mutable and
            is changed after the wrapper is got the wrapper becomes invalide and can return wrong values or even throw
            OutOfBoundException.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a boolean 2d array.
        
        
        """
        ...
    @typing.overload
    def getBoolean(self, string: str) -> bool:
        """
            Returns the value being interpreted as a boolean. If the value is an array only the first value of the array is
            returned. If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as a boolean.
        
        """
        ...
    @typing.overload
    def getBoolean(self, string: str, int: int) -> bool:
        """
            Returns the value being interpreted as a boolean. The value returned is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getBooleans(self, string: str) -> typing.List[bool]:
        """
            Returns the value being interpreted as a boolean array. If the value is not an array it is encapsulated in an array of
            size 1. If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a boolean array.
        
        """
        ...
    @typing.overload
    def getBooleans(self, string: str, int: int, int2: int) -> typing.List[bool]:
        """
            Returns a sub array of the value translated as a boolean array. The subarray starts at startIndex and contains the
            number of element given by length. If startIndex+length is greater than the number of values in the underlying array an
            exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value translated as a boolean array.
        
        
        """
        ...
    @typing.overload
    def getByte(self, string: str) -> int:
        """
            Returns the value being interpreted as a byte. If the value is an array only the first value of the array is returned.
            If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as a byte.
        
        """
        ...
    @typing.overload
    def getByte(self, string: str, int: int) -> int:
        """
            Returns the value being interpreted as a byte. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getBytes(self, string: str) -> typing.List[int]:
        """
            Returns the value translated as a byte array. If the value is not an array it is encapsulated in an array of size 1. If
            the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a byte array.
        
        """
        ...
    @typing.overload
    def getBytes(self, string: str, int: int, int2: int) -> typing.List[int]:
        """
            Returns a sub array of the value translated as a boolean array. The subarray starts at startIndex and contains the
            number of element given by length. If startIndex+length is greater than the number of values in the underlying array an
            exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value translated as a byte array.
        
        
        """
        ...
    def getColumnCount(self, string: str) -> int:
        """
            Returns the number of columns for the case when the value is represented as 2-dimensional array. For scalar which are
            not bit-pattern will always return 1.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the number of columns for the case when the value is represented as 2-dimensional array
        
        
        """
        ...
    def getDiscreteFunction(self, string: str) -> DiscreteFunction:
        """
            Returns the value being interpreted as a discrete function. If the name does not match any value or the value can't be
            represented as a discrete function a :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as a discrete function.
        
        
        """
        ...
    def getDiscreteFunctionList(self, string: str) -> DiscreteFunctionList:
        """
            Returns the value being interpreted as a discrete function list. If the name does not match any value or the value can't
            be represented as a discrete function list a :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as a discrete function list.
        
        
        """
        ...
    @typing.overload
    def getDouble(self, string: str) -> float:
        """
            Returns the value being interpreted as a double. If the value is an array only the first value of the array is returned.
            If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as a double.
        
        """
        ...
    @typing.overload
    def getDouble(self, string: str, int: int) -> float:
        """
            Returns the value being interpreted as a double. The value returned is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getDoubles(self, string: str) -> typing.List[float]:
        """
            Returns the value translated as a double array. If the value is not an array it is encapsulated in an array of size 1.
            If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a double array.
        
        """
        ...
    @typing.overload
    def getDoubles(self, string: str, int: int, int2: int) -> typing.List[float]:
        """
            Returns a sub array of the value translated as a boolean array. The subarray starts at startIndex and contains the
            number of element given by length. If startIndex+length is greater than the number of values in the underlying array an
            exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value translated as a double array.
        
        
        """
        ...
    def getEnumItem(self, string: str) -> EnumItem:
        """
            Returns the value being interpreted as an enumeration item. If the name does not match any value or the value can't be
            represented as an enumeration item (value is boolean, array or there is no information about enumeration type, etc) an
            :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as an enumeration item.
        
        
        """
        ...
    def getEnumItemSet(self, string: str) -> EnumItemSet:
        """
            Returns the value being interpreted as an enumeration item set. If the name does not match any value or the value can't
            be represented as an enumeration item set (value is boolean, array or there is no information about enumeration type,
            etc) an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as an enumeration item set.
        
        
        """
        ...
    def getEnumItemSets(self, string: str) -> typing.List[EnumItemSet]:
        """
            Returns the value translated as a :class:`~cern.japc.value.EnumItemSet` array. If the value is not an array it is
            encapsulated in an array of size 1. If the name does not match any value an
            :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a String array.
        
        
        """
        ...
    def getEnumItems(self, string: str) -> typing.List[EnumItem]:
        """
            Returns the value translated as a :class:`~cern.japc.value.EnumItem` array. If the value is not an array it is
            encapsulated in an array of size 1. If the name does not match any value an
            :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a String array.
        
        
        """
        ...
    @typing.overload
    def getFloat(self, string: str) -> float:
        """
            Returns the value being interpreted as a float. If the value is an array only the first value of the array is returned.
            If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as a float.
        
        """
        ...
    @typing.overload
    def getFloat(self, string: str, int: int) -> float:
        """
            Returns the value being interpreted as a float. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getFloats(self, string: str) -> typing.List[float]:
        """
            Returns the value translated as a float array. If the value is not an array it is encapsulated in an array of size 1. If
            the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a float array.
        
        """
        ...
    @typing.overload
    def getFloats(self, string: str, int: int, int2: int) -> typing.List[float]:
        """
            Returns a sub array of the value translated as a boolean array. The subarray starts at startIndex and contains the
            number of element given by length. If startIndex+length is greater than the number of values in the underlying array an
            exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value translated as a float array.
        
        
        """
        ...
    @typing.overload
    def getInt(self, string: str) -> int:
        """
            Returns the value being interpreted as a int. If the value is an array only the first value of the array is returned. If
            the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as a int.
        
        """
        ...
    @typing.overload
    def getInt(self, string: str, int: int) -> int:
        """
            Returns the value being interpreted as a int. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getInts(self, string: str) -> typing.List[int]:
        """
            Returns the value translated as a int array. If the value is not an array it is encapsulated in an array of size 1. If
            the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a int array.
        
        """
        ...
    @typing.overload
    def getInts(self, string: str, int: int, int2: int) -> typing.List[int]:
        """
            Returns the value translated as a int array. If the value is not an array it is encapsulated in an array of size 1
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value translated as a int array.
        
        
        """
        ...
    def getLength(self, string: str) -> int:
        """
            Returns the length of the array represented by the value of given name. In case the value is not an array the value
            returned is 1. If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get the length for
        
            Returns:
                the length of the array or 1 in case of a scalar.
        
        
        """
        ...
    @typing.overload
    def getLong(self, string: str) -> int:
        """
            Returns the value being interpreted as a long. If the value is an array only the first value of the array is returned.
            If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as a long.
        
        """
        ...
    @typing.overload
    def getLong(self, string: str, int: int) -> int:
        """
            Returns the value being interpreted as a long. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getLongs(self, string: str) -> typing.List[int]:
        """
            Returns the value translated as a long array. If the value is not an array it is encapsulated in an array of size 1. If
            the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a long array.
        
        """
        ...
    @typing.overload
    def getLongs(self, string: str, int: int, int2: int) -> typing.List[int]:
        """
            Returns a sub array of the value translated as a boolean array. The subarray starts at startIndex and contains the
            number of element given by length. If startIndex+length is greater than the number of values in the underlying array an
            exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value translated as a long array.
        
        
        """
        ...
    def getMaxValue(self, string: str) -> float:
        """
            Returns the allowed maximum of the value with a given name. The maximum is usually the same as the one given by the
            descriptor. If the maximum is dynamic, the one from the descriptor cannot be defined and this method returns the correct
            value. If no maximum is defined the :code:`Double.NaN` is returned.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value name
        
            Returns:
                the allowed maximum of the value with a given name or :code:`Double.NaN`
        
        
        """
        ...
    def getMinValue(self, string: str) -> float:
        """
            Returns the allowed minimum of the value with a given name. The minimum is usually the same as the one given by the
            descriptor. If the minimum is dynamic, the one from the descriptor cannot be defined and this method returns the correct
            value. If no minimum is defined the :code:`Double.NaN` is returned.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value name
        
            Returns:
                the allowed minimum of the value with a given name or :code:`Double.NaN`
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
            Returns the names of all entries in this map. The array returned is a copy. Any modification on the returned array has
            no effect on this value.
        
            Returns:
                the names of all entries in this map
        
        
        """
        ...
    @typing.overload
    def getObject(self, string: str) -> typing.Any:
        """
            Returns the value as an object. This method returns the scalar type in their wrapping Object type and arrays and string
            without change.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value as an object.
        
        """
        ...
    @typing.overload
    def getObject(self, string: str, int: int) -> typing.Any:
        """
            Returns the value as an Object. The value returned is the nth one from the array where n is given by the index. If the
            underlying value is not an array the index is ignored the the value is returned. If the value is an array the nth value
            will be returned where n is given by index.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    def getRowCount(self, string: str) -> int:
        """
            Returns the number of rows for the case when the value is represented as 2-dimensional array. For scalar and
            1-dimensional arrays will always return 1.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the number of rows for the case when the value is represented as 2-dimensional array
        
        
        """
        ...
    @typing.overload
    def getShort(self, string: str) -> int:
        """
            Returns the value being interpreted as a short. If the value is an array only the first value of the array is returned.
            If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as a short.
        
        """
        ...
    @typing.overload
    def getShort(self, string: str, int: int) -> int:
        """
            Returns the value being interpreted as a short. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getShorts(self, string: str) -> typing.List[int]:
        """
            Returns the value translated as a short array. If the value is not an array it is encapsulated in an array of size 1. If
            the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a short array.
        
        """
        ...
    @typing.overload
    def getShorts(self, string: str, int: int, int2: int) -> typing.List[int]:
        """
            Returns a sub array of the value translated as a boolean array. The subarray starts at startIndex and contains the
            number of element given by length. If startIndex+length is greater than the number of values in the underlying array an
            exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value translated as a short array.
        
        
        """
        ...
    @typing.overload
    def getString(self, string: str) -> str:
        """
            Returns the value being interpreted as a String. If the value is an array only the first value of the array is returned.
            If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value being interpreted as a String.
        
        """
        ...
    @typing.overload
    def getString(self, string: str, int: int) -> str:
        """
            Returns the value being interpreted as a String. The value returned is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getString(self) -> str: ...
    @typing.overload
    def getStrings(self, string: str) -> typing.List[str]:
        """
            Returns the value translated as a String array. If the value is not an array it is encapsulated in an array of size 1.
            If the name does not match any value an :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
        
            Returns:
                the value translated as a String array.
        
        """
        ...
    @typing.overload
    def getStrings(self, string: str, int: int, int2: int) -> typing.List[str]:
        """
            Returns a sub array of the value translated as a boolean array. The subarray starts at startIndex and contains the
            number of element given by length. If startIndex+length is greater than the number of values in the underlying array an
            exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value translated as a String array.
        
        
        """
        ...
    def getUnit(self, string: str) -> str:
        """
            Returns the unit of the value with a given name. The unit is usually the same as the one given by the descriptor. If the
            unit is dynamic, the one from the descriptor cannot be defined and this method returns the correct value. If no unit is
            defined an empty string is returned.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value name
        
            Returns:
                the unit of the value with a given name or an empty string
        
        
        """
        ...
    def getValueType(self, string: str) -> ValueType:
        """
            Returns the value type of the value of given name If the name does not match any value an
            :class:`~cern.japc.value.ValueConversionException` is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value to get the type for
        
            Returns:
                the value type of the value interpreted by this reader
        
        
        """
        ...
    def getXMaxValue(self, string: str) -> float:
        """
            If the value with a given name is a function, this method returns the allowed maximum of X axis. The maximum is usually
            the same as the one given by the descriptor. If the maximum is dynamic, the one from the descriptor cannot be defined
            and this method returns the correct value. If the value is not a function or no maximum is defined the
            :code:`Double.NaN` is returned.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value name
        
            Returns:
                the allowed maximum of X axis for the value with a given name or :code:`Double.NaN`
        
        
        """
        ...
    def getXMinValue(self, string: str) -> float:
        """
            If the value with a given name is a function, this method returns the allowed minimum of X axis. The minimum is usually
            the same as the one given by the descriptor. If the minimum is dynamic, the one from the descriptor cannot be defined
            and this method returns the correct value. If the value is not a function or no minimum is defined the
            :code:`Double.NaN` is returned.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value name
        
            Returns:
                the allowed minimum of X axis for the value with a given name or :code:`Double.NaN`
        
        
        """
        ...
    def getXUnit(self, string: str) -> str:
        """
            If the value with a given name is a function, this method returns the unit of X axis. The unit is usually the same as
            the one given by the descriptor. If the unit is dynamic, the one from the descriptor cannot be defined and this method
            returns the correct value. If the value is not a function or no unit is defined an empty string is returned.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value name
        
            Returns:
                the unit of X axis for the value with a given name or an empty string
        
        
        """
        ...
    def getYMaxValue(self, string: str) -> float:
        """
            If the value with a given name is a function, this method returns the allowed maximum of Y axis. The maximum is usually
            the same as the one given by the descriptor. If the maximum is dynamic, the one from the descriptor cannot be defined
            and this method returns the correct value. If no maximum is defined the :code:`Double.NaN` is returned. If the value is
            not a function this method returns the same result as :meth:`~cern.japc.value.ImmutableMapParameterValue.getMinValue`.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value name
        
            Returns:
                the allowed maximum of Y axis for the value with a given name or :code:`Double.NaN`
        
        
        """
        ...
    def getYMinValue(self, string: str) -> float:
        """
            If the value with a given name is a function, this method returns the allowed minimum of Y axis. The minimum is usually
            the same as the one given by the descriptor. If the minimum is dynamic, the one from the descriptor cannot be defined
            and this method returns the correct value. If no minimum is defined the :code:`Double.NaN` is returned. If the value is
            not a function this method returns the same result as :meth:`~cern.japc.value.ImmutableMapParameterValue.getMinValue`.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value name
        
            Returns:
                the allowed minimum of Y axis for the value with a given name or :code:`Double.NaN`
        
        
        """
        ...
    def getYUnit(self, string: str) -> str:
        """
            If the value with a given name is a function, this method returns the unit of Y axis. The unit is usually the same as
            the one given by the descriptor. If the unit is dynamic, the one from the descriptor cannot be defined and this method
            returns the correct value. If no unit is defined an empty string is returned. If the value is not a function this method
            returns the same result as :meth:`~cern.japc.value.ImmutableMapParameterValue.getUnit`.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): value name
        
            Returns:
                the unit of Y axis for the value with a given name or an empty string
        
        
        """
        ...
    def size(self) -> int:
        """
            Returns the number of entries in this map
        
            Returns:
                the number of entries in this map
        
        
        """
        ...

class MapDescriptor(ValueDescriptor):
    """
    public interface MapDescriptor extends :class:`~cern.japc.value.ValueDescriptor`
    
        A class implementing this interface provides a description of an named set of simple values.
    
        Examples of such a type would be :
    
          - A value having named fields, each of them being a simple value
    """
    def get(self, string: str) -> 'SimpleDescriptor':
        """
            Returns the matching descriptor for the given named value
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the property fields
        
            Returns:
                the matching descriptor for the given named value or null if no match
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
            Returns the name of all available property fields
        
            Returns:
                the name of all available property fields
        
        
        """
        ...
    def size(self) -> int:
        """
            Returns the number of entries in this map if constant or the maximum number if not constant. -1 can be returned to
            signal that no information is know.
        
            Returns:
                the number of entries in this map
        
        
        """
        ...

class MapParameterValue(ImmutableMapParameterValue):
    """
    public interface MapParameterValue extends :class:`~cern.japc.value.ImmutableMapParameterValue`
    
        A class implementing this interface provides method to interpret a set of named simple values. A call to any of the
        method of this interface with a name that does not exist will throw an ValueConversionException.
    """
    def makeMutable(self) -> 'MapParameterValue':
        """
            Description copied from interface: :meth:`~cern.japc.value.ParameterValue.makeMutable`
            Creates a mutable version of this ParameterValue that can be set using the setters. The original values are untouched by
            this operation. If this ParameterValue is already mutable this method returns the same instance.
        
            Specified by:
                :meth:`~cern.japc.value.ParameterValue.makeMutable` in interface :class:`~cern.japc.value.ParameterValue`
        
            Returns:
                A new mutable copy of this parameter value or this parameter value itself if it is already mutable.
        
        
        """
        ...
    def put(self, string: str, simpleParameterValue: 'SimpleParameterValue') -> None:
        """
            Sets the matching reader for the given named value
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                valueReader (:class:`~cern.japc.value.SimpleParameterValue`): the non null matching reader for the given named value
        
        
        """
        ...
    def remove(self, string: str) -> 'SimpleParameterValue':
        """
            Removes the matching reader from this map
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the reader
        
            Returns:
                the reader removed or null if none was removed
        
        
        """
        ...
    @typing.overload
    def setBoolean(self, string: str, boolean: bool) -> None:
        """
            Sets the value being a boolean. The scale is left unchanged from what it was before or set to 0 is the value of that
            name has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (boolean): the boolean value.
        
            Sets the value at the given index to the given boolean. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                index (int): the index where to set the value in the array
                value (boolean): the boolean value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setBoolean(self, string: str, int: int, boolean: bool) -> None: ...
    def setBooleans(self, string: str, booleanArray: typing.List[bool]) -> None:
        """
            Sets the value being a boolean array. The scale is left unchanged from what it was before or set to 0 is the value of
            that name has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (boolean[]): the boolean array value.
        
        
        """
        ...
    def setBooleans2D(self, string: str, booleanArray: typing.List[bool], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional boolean array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (boolean[]): the boolean array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setByte(self, string: str, byte: int) -> None:
        """
            Sets the value being a byte. The scale is left unchanged from what it was before or set to 0 is the value of that name
            has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (byte): the byte value.
        
            Sets the value at the given index to the given byte. The value set is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored and the value is set. If this value is not mutable
            an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                index (int): the index where to set the value in the array
                value (byte): the byte value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setByte(self, string: str, int: int, byte: int) -> None: ...
    def setBytes(self, string: str, byteArray: typing.List[int]) -> None:
        """
            Sets the value being a byte array. The scale is left unchanged from what it was before or set to 0 is the value of that
            name has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (byte[]): the byte array value.
        
        
        """
        ...
    def setBytes2D(self, string: str, byteArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional byte array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (byte[]): the byte array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    def setDiscreteFunction(self, string: str, discreteFunction: DiscreteFunction) -> None:
        """
            Sets the value being a :class:`~cern.japc.value.DiscreteFunction`.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (:class:`~cern.japc.value.DiscreteFunction`): the DiscreteFunction value.
        
        
        """
        ...
    def setDiscreteFunctionList(self, string: str, discreteFunctionList: DiscreteFunctionList) -> None:
        """
            Sets the value being a :class:`~cern.japc.value.DiscreteFunctionList`.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (:class:`~cern.japc.value.DiscreteFunctionList`): the DiscreteFunctionList value.
        
        
        """
        ...
    @typing.overload
    def setDouble(self, string: str, double: float) -> None:
        """
            Sets the value being a double. The scale is left unchanged from what it was before or set to 0 is the value of that name
            has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (double): the double value.
        
            Sets the value at the given index to the given double. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                index (int): the index where to set the value in the array
                value (double): the double value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setDouble(self, string: str, int: int, double: float) -> None: ...
    def setDoubles(self, string: str, doubleArray: typing.List[float]) -> None:
        """
            Sets the value being a double array. The scale is left unchanged from what it was before or set to 0 is the value of
            that name has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (double[]): the double array value.
        
        
        """
        ...
    def setDoubles2D(self, string: str, doubleArray: typing.List[float], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional double array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (double[]): the double array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    def setEnumItem(self, string: str, enumItem: EnumItem) -> None:
        """
            Sets the value being an :class:`~cern.japc.value.EnumItem`.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (:class:`~cern.japc.value.EnumItem`): the EnumItem value.
        
        
        """
        ...
    def setEnumItemSet(self, string: str, enumItemSet: EnumItemSet) -> None:
        """
            Sets the value being an :class:`~cern.japc.value.EnumItemSet`.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (:class:`~cern.japc.value.EnumItemSet`): the EnumItemSet value.
        
        
        """
        ...
    def setEnumItemSets(self, string: str, enumItemSetArray: typing.List[EnumItemSet]) -> None:
        """
            Sets the value being a EnumItemSet array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (:class:`~cern.japc.value.EnumItemSet`[]): the EnumItemSet array value.
        
        
        """
        ...
    def setEnumItemSets2D(self, string: str, enumItemSetArray: typing.List[EnumItemSet], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional EnumItemSet array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (:class:`~cern.japc.value.EnumItemSet`[]): the EnumItemSet array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    def setEnumItems(self, string: str, enumItemArray: typing.List[EnumItem]) -> None:
        """
            Sets the value being a EnumItem array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (:class:`~cern.japc.value.EnumItem`[]): the EnumItem array value.
        
        
        """
        ...
    def setEnumItems2D(self, string: str, enumItemArray: typing.List[EnumItem], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional EnumItem array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (:class:`~cern.japc.value.EnumItem`[]): the EnumItem array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setFloat(self, string: str, float: float) -> None:
        """
            Sets the value being a float. The scale is left unchanged from what it was before or set to 0 is the value of that name
            has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (float): the float value.
        
            Sets the value at the given index to the given float. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                index (int): the index where to set the value in the array
                value (float): the float value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setFloat(self, string: str, int: int, float: float) -> None: ...
    def setFloats(self, string: str, floatArray: typing.List[float]) -> None:
        """
            Sets the value being a float array. The scale is left unchanged from what it was before or set to 0 is the value of that
            name has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (float[]): the float array value.
        
        
        """
        ...
    def setFloats2D(self, string: str, floatArray: typing.List[float], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional float array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (float[]): the float array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setInt(self, string: str, int: int) -> None:
        """
            Sets the value being a int. The scale is left unchanged from what it was before or set to 0 is the value of that name
            has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (int): the int value.
        
            Sets the value at the given index to the given int. The value set is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored and the value is set. If this value is not mutable
            an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                index (int): the index where to set the value in the array
                value (int): the int value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setInt(self, string: str, int: int, int2: int) -> None: ...
    def setInts(self, string: str, intArray: typing.List[int]) -> None:
        """
            Sets the value being a int array. The scale is left unchanged from what it was before or set to 0 is the value of that
            name has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (int[]): the int array value.
        
        
        """
        ...
    def setInts2D(self, string: str, intArray: typing.List[int], intArray2: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional int array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (int[]): the int array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setLong(self, string: str, int: int, long: int) -> None:
        """
            Sets the value at the given index to the given long. The value set is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored and the value is set. If this value is not mutable
            an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                index (int): the index where to set the value in the array
                value (long): the long value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setLong(self, string: str, long: int) -> None:
        """
            Sets the value being a long. The scale is left unchanged from what it was before or set to 0 is the value of that name
            has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (long): the long value.
        
        """
        ...
    def setLongs(self, string: str, longArray: typing.List[int]) -> None:
        """
            Sets the value being a long array. The scale is left unchanged from what it was before or set to 0 is the value of that
            name has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (long[]): the long array value.
        
        
        """
        ...
    def setLongs2D(self, string: str, longArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional long array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (long[]): the long array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    def setObject(self, string: str, object: typing.Any) -> None:
        """
            Sets the value as an object. This method can handle any scalar wrapping Object type as well as arrays and string. If
            other type was passed a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` will be
            thrown. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                o (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value as an object.
        
        
        """
        ...
    def setObjects2D(self, string: str, object: typing.Any, intArray: typing.List[int]) -> None:
        """
            Sets the value as a 2d array of objects. This method can handle any array of primitives and Strings, which will be used
            as a source for 2D array. If other type was passed a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` will be
            thrown. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                o (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value as an object.
                dimensions (int[]): the dimensions of the 2D array
        
        
        """
        ...
    @typing.overload
    def setShort(self, string: str, int: int, short: int) -> None:
        """
            Sets the value at the given index to the given short. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                index (int): the index where to set the value in the array
                value (short): the short value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setShort(self, string: str, short: int) -> None:
        """
            Sets the value being a short. The scale is left unchanged from what it was before or set to 0 is the value of that name
            has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (short): the short value.
        
        """
        ...
    def setShorts(self, string: str, shortArray: typing.List[int]) -> None:
        """
            Sets the value being a short array. The scale is left unchanged from what it was before or set to 0 is the value of that
            name has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (short[]): the short array value.
        
        
        """
        ...
    def setShorts2D(self, string: str, shortArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional short array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (short[]): the short array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setString(self, string: str, int: int, string2: str) -> None:
        """
            Sets the value at the given index to the given String. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                index (int): the index where to set the value in the array
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the String value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setString(self, string: str, string2: str) -> None:
        """
            Sets the value being a String. The scale is left unchanged from what it was before or set to 0 is the value of that name
            has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the String value.
        
        """
        ...
    def setStrings(self, string: str, stringArray: typing.List[str]) -> None:
        """
            Sets the value being a String array. The scale is left unchanged from what it was before or set to 0 is the value of
            that name has not been set before.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the String array value.
        
        
        """
        ...
    def setStrings2D(self, string: str, stringArray: typing.List[str], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional String array. If this value is not mutable an exception is thrown.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the value
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the String array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...

class SimpleDescriptor(MapDescriptor):
    """
    public interface SimpleDescriptor extends :class:`~cern.japc.value.MapDescriptor`
    
        A class implementing this interface provides a description of a simple value that is not a composite value. The
        supported types are scalar types, array of scalar types, strings and array of strings.
    
        Examples of such a type would be :
    
          - an int
          - a double
          - an array of doubles
    """
    DEFAULT_DECIMAL_FORMAT: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_DECIMAL_FORMAT
    
        This is the default format used for decimal values if none is defined.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_FORMAT: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DEFAULT_FORMAT
    
        This is the default format used for non-decimal values if none is defined.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DATE_FORMAT_PREFIX: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` DATE_FORMAT_PREFIX
    
        This is the date format prefix.
    
        Also see:
            :meth:`~constant`
    
    
    """
    HEXADECIMAL_FORMAT_PREFIX: typing.ClassVar[str] = ...
    """
    `@Deprecated <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Deprecated.html?is-external=true>` static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` HEXADECIMAL_FORMAT_PREFIX
    
        Deprecated.
        Please use :code:`NumberUtils.HEXADECIMAL_FORMAT_PREFIX` instead.
        This is the hexadecimal format prefix.
    
        Also see:
            :meth:`~constant`
    
    
    """
    UNDEFINED_DIMENSION: typing.ClassVar[int] = ...
    """
    static final int UNDEFINED_DIMENSION
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getBooleanType(self) -> BooleanType:
        """
            Returns the boolean type for :meth:`~cern.japc.value.ValueType.BOOLEAN` values. Otherwise returns :code:`null`.
        
            Returns:
                the enumeration type for :meth:`~cern.japc.value.ValueType.BOOLEAN` values, :code:`null` otherwise
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
            Returns the number of columns if the value will be represented as 2d array. For a scalar, this returns 1.
        
            It will return :meth:`~cern.japc.value.SimpleDescriptor.UNDEFINED_DIMENSION` for dynamically sized array parameters.
        
            PER-TYPE: Same for all instances of the described value.
        
            Returns:
                the number of columns if the value will be represented as 2d array.
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Returns an optional description of this value. If no description is defined, null is returned.
        
            PER-TYPE: Same for all instances of the described value.
        
            Returns:
                an optional description of this value or null
        
        
        """
        ...
    def getEnumType(self) -> EnumType:
        """
            Returns the enumeration type for :meth:`~cern.japc.value.ValueType.ENUM` and :meth:`~cern.japc.value.ValueType.ENUM_SET`
            values. Otherwise returns :code:`null`.
        
            Returns:
                the enumeration type for :meth:`~cern.japc.value.ValueType.ENUM` and :meth:`~cern.japc.value.ValueType.ENUM_SET` values.
                Otherwise returns :code:`null`.
        
        
        """
        ...
    def getExtraCharacteristic(self, string: str) -> str:
        """
            Returns the value of the characteristic of the parameter defined by the given name. If no characteristic of that name is
            defined for this parameter the value returned is null.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the extra characteristic to get
        
            Returns:
                the value of the characteristic of the parameter defined by the given name.
        
        
        """
        ...
    def getExtraCharacteristicNames(self) -> typing.List[str]:
        """
            Returns the names of the possible extra characteristics of the parameter. The returned value is guaranteed to be non
            null. It is an array that is possibly empty.
        
            Returns:
                the names of the possible extra characteristic of the parameter.
        
        
        """
        ...
    def getFormatPattern(self) -> str:
        """
            Returns the Parameter data format in java style. Cannot be null.
        
            PER-TYPE: Same for all instances of the described value. Used mainly in GUIs.
        
            Returns:
                the Parameter data format in java style.
        
        
        """
        ...
    def getLength(self) -> int:
        """
            Returns the length of the array if the array is always of the same size. In case the array is of variable size (possibly
            changing for each value read) the method returns its maximal size. In case the value is not an array the value returned
            is 1. The default value for the value of type array is Integer.
        
            It will return :meth:`~cern.japc.value.SimpleDescriptor.UNDEFINED_DIMENSION` for dynamically sized array parameters.
        
            This value is used by JAPC to transform the received value into one that has the expected length. For example, if the
            length=1 and the received value is an array, JAPC will only return the first element of the array.
        
            PER-TYPE: Same for all instances of the described value.
        
            Returns:
                the length of the array if fixed or the maximal size or 1 in case of a scalar, or -1 if N/A
        
        
        """
        ...
    def getMaxValue(self) -> float:
        """
            Returns the allowed maximum of the value described by this descriptor. If no maximum is defined the :code:`Double.NaN`
            is returned.
        
            PER-INSTANCE: Can be different for different instances of the described value.
        
            Returns:
                the allowed maximum of the value described by this descriptor or :code:`Double.NaN`
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
            Returns the allowed minimum of the value described by this descriptor. If no minimum is defined the :code:`Double.NaN`
            is returned.
        
            PER-INSTANCE: Can be different for different instances of the described value.
        
            Returns:
                the allowed minimum of the value described by this descriptor or :code:`Double.NaN`
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
            Returns the number of rows if the value will be represented as 2d array. For a scalar, this returns 1.
        
            It will return :meth:`~cern.japc.value.SimpleDescriptor.UNDEFINED_DIMENSION` for dynamically sized array parameters.
        
            PER-TYPE: Same for all instances of the described value.
        
            Returns:
                the number of rows if the value will be represented as 2d array.
        
        
        """
        ...
    def getStandardMeaning(self, object: typing.Any) -> SimpleValueStandardMeaning:
        """
            Returns the standard meaning defined for a value.
        
            This method never returns :code:`null`. If nothing is defined then
            :meth:`~cern.japc.value.SimpleValueStandardMeaning.NONE` is returned.
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): a value
        
            Returns:
                the standard meaning defined for a value
        
        
        """
        ...
    def getTitle(self) -> str:
        """
            Returns an optional title of this value. If no title is defined null is returned. Used mainly in GUIs.
        
            Returns:
                an optional title of this value or null
        
        
        """
        ...
    def getUnit(self) -> str:
        """
            Returns the unit of the value described by this descriptor. If no unit is defined an empty string is returned.
        
            PER-INSTANCE: Can be different for different instances of the described value.
        
            Returns:
                the unit of the value described by this descriptor or an empty string
        
        
        """
        ...
    def getValueType(self) -> ValueType:
        """
            Returns the simple value type (with information about the underlying real Java type) of the value described by this
            descriptor
        
            PER-TYPE: Same for all instances of the described value.
        
            Returns:
                the simple value type of the value described by this descriptor
        
        
        """
        ...
    def getXMaxValue(self) -> float:
        """
            Returns the allowed maximum of the X axis of the value described by this descriptor. If the value is not a function or
            no maximum is defined the :code:`Double.NaN` is returned.
        
            PER-INSTANCE: Can be different for different instances of the described value.
        
            Returns:
                the allowed maximum of the X axis of the value described by this descriptor or :code:`Double.NaN`
        
        
        """
        ...
    def getXMinValue(self) -> float:
        """
            Returns the allowed minimum of the X axis of the value described by this descriptor. If the value is not a function or
            no minimum is defined the :code:`Double.NaN` is returned.
        
            PER-INSTANCE: Can be different for different instances of the described value.
        
            Returns:
                the allowed minimum of the X axis of the value described by this descriptor or :code:`Double.NaN`
        
        
        """
        ...
    def getXUnit(self) -> str:
        """
            Returns the unit of the X axis of the value described by this descriptor. If the value is not a function or no unit is
            defined an empty string is returned.
        
            PER-INSTANCE: Can be different for different instances of the described value.
        
            Returns:
                the unit of the X axis of the value described by this descriptor or an empty string
        
        
        """
        ...
    def getYMaxValue(self) -> float:
        """
            Returns the allowed maximum of the Y axis of the value described by this descriptor. If the value is not a function or
            no maximum is defined the :code:`Double.NaN` is returned.
        
            PER-INSTANCE: Can be different for different instances of the described value.
        
            Returns:
                the allowed maximum of the Y axis of the value described by this descriptor or :code:`Double.NaN`
        
        
        """
        ...
    def getYMinValue(self) -> float:
        """
            Returns the allowed minimum of the Y axis of the value described by this descriptor. If the value is not a function or
            no minimum is defined the :code:`Double.NaN` is returned.
        
            PER-INSTANCE: Can be different for different instances of the described value.
        
            Returns:
                the allowed minimum of the Y axis of the value described by this descriptor or :code:`Double.NaN`
        
        
        """
        ...
    def getYUnit(self) -> str:
        """
            Returns the unit of the Y axis of the value described by this descriptor. If no unit is defined an empty string is
            returned. If the value is not a function this method returns the same result as
            :meth:`~cern.japc.value.SimpleDescriptor.getUnit`.
        
            PER-INSTANCE: Can be different for different instances of the described value.
        
            Returns:
                the unit of the Y axis of the value described by this descriptor or an empty string
        
        
        """
        ...
    def isDiscrete(self) -> bool: ...
    def isFilterable(self) -> bool: ...
    def isSettable(self, object: typing.Any) -> bool:
        """
            Checks whether it is possible to set a value.
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): value to check
        
            Returns:
                :code:`true` if it is possible to set the value and :code:`false` otherwise
        
        
        """
        ...

class SimpleParameterValue(MapParameterValue):
    """
    public interface SimpleParameterValue extends :class:`~cern.japc.value.MapParameterValue`
    
        Representation of a a value of simple type:
    
    
        - scalars: see :class:`~cern.japc.value.ValueType` including strings, enums, enumsets, functions and function-lists
    
    
        - arrays of scalar types
    
    
        - 2D arrays of scalar types
    """
    NO_UNIT: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` NO_UNIT
    
        String used when no unit is defined
    
        Also see:
            :meth:`~constant`
    
    
    """
    NO_MIN_MAX_VALUE: typing.ClassVar[float] = ...
    """
    static final `Double <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Double.html?is-external=true>` NO_MIN_MAX_VALUE
    
        Double value used when no min or no max is defined
    
    """
    @typing.overload
    def getArray2D(self, string: str) -> Array2D: ...
    @typing.overload
    def getArray2D(self) -> Array2D:
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
    def getBoolean(self, string: str) -> bool:
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
    def getBoolean(self, string: str, int: int) -> bool: ...
    @typing.overload
    def getBoolean(self) -> bool:
        """
            Returns the value being interpreted as a boolean. If the value is an array only the first value of the array is
            returned.
        
            Returns:
                the value being interpreted as a boolean.
        
        """
        ...
    @typing.overload
    def getBoolean(self, int: int) -> bool: ...
    @typing.overload
    def getBooleans(self, string: str) -> typing.List[bool]:
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
    def getBooleans(self, string: str, int: int, int2: int) -> typing.List[bool]: ...
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
    def getBooleans(self, int: int, int2: int) -> typing.List[bool]: ...
    @typing.overload
    def getByte(self, string: str) -> int:
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
    def getByte(self, string: str, int: int) -> int: ...
    @typing.overload
    def getByte(self) -> int:
        """
            Returns the value being interpreted as a byte. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a byte.
        
        """
        ...
    @typing.overload
    def getByte(self, int: int) -> int: ...
    @typing.overload
    def getBytes(self, string: str) -> typing.List[int]:
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
    def getBytes(self, string: str, int: int, int2: int) -> typing.List[int]: ...
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
    def getBytes(self, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getColumnCount(self, string: str) -> int: ...
    @typing.overload
    def getColumnCount(self) -> int:
        """
            Returns the number of columns for the case when the value is represented as 2-dimensional array. For scalar which are
            not bit-pattern will always return 1.
        
            Returns:
                the number of columns for the case when the value is represented as 2-dimensional array
        
        
        """
        ...
    @typing.overload
    def getDiscreteFunction(self, string: str) -> DiscreteFunction: ...
    @typing.overload
    def getDiscreteFunction(self) -> DiscreteFunction:
        """
            Returns the value being interpreted as a discrete function. If the value can't be represented as a discrete function a
            ValueConversionException is thrown.
        
            Returns:
                the value being interpreted as a discrete function.
        
        
        """
        ...
    @typing.overload
    def getDiscreteFunctionList(self, string: str) -> DiscreteFunctionList: ...
    @typing.overload
    def getDiscreteFunctionList(self) -> DiscreteFunctionList:
        """
            Returns the value being interpreted as a discrete function list. If the value can't be represented as a discrete
            function list a ValueConversionException is thrown.
        
            Returns:
                the value being interpreted as a discrete function list.
        
        
        """
        ...
    @typing.overload
    def getDouble(self, string: str) -> float:
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
    def getDouble(self, string: str, int: int) -> float: ...
    @typing.overload
    def getDouble(self) -> float:
        """
            Returns the value being interpreted as a double. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a double.
        
        """
        ...
    @typing.overload
    def getDouble(self, int: int) -> float: ...
    @typing.overload
    def getDoubles(self, string: str) -> typing.List[float]:
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
    def getDoubles(self, string: str, int: int, int2: int) -> typing.List[float]: ...
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
    def getDoubles(self, int: int, int2: int) -> typing.List[float]: ...
    @typing.overload
    def getEnumItem(self, string: str) -> EnumItem:
        """
            Returns the value being interpreted as an enumeration. The value returned is the nth one from the array where n is given
            by the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getEnumItem(self) -> EnumItem:
        """
            Returns the value being interpreted as an enumeration item. If the value can't be represented as an enumeration item
            (value is boolean, array or there is no information about enumeration type, etc) an ValueConversionException is thrown.
        
            Returns:
                the value being interpreted as an enumeration item.
        
        """
        ...
    @typing.overload
    def getEnumItem(self, int: int) -> EnumItem: ...
    @typing.overload
    def getEnumItemSet(self, string: str) -> EnumItemSet:
        """
            Returns the value being interpreted as an enumeration set. The value returned is the nth one from the array where n is
            given by the index. If the underlying value is not an array the index is ignored the the value is returned. If the value
            is an array the nth value will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getEnumItemSet(self) -> EnumItemSet:
        """
            Returns the value being interpreted as an enumeration item set. If the value can't be represented as an enumeration item
            set (value is boolean, array or there is no information about enumeration type, etc) an ValueConversionException is
            thrown.
        
            Returns:
                the value being interpreted as an enumeration item set.
        
        """
        ...
    @typing.overload
    def getEnumItemSet(self, int: int) -> EnumItemSet: ...
    @typing.overload
    def getEnumItemSets(self, string: str) -> typing.List[EnumItemSet]:
        """
            Returns a sub array of the value being interpreted as an array of enumeration item sets. The subarray starts at
            startIndex and contains the number of element given by length. If startIndex+length is greater than the number of values
            in the underlying array an exception is thrown. If the value is not an array, the value is returned encapsulated in an
            array of size 1, ignoring the arguments.
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as an array of enumeration items.
        
        
        """
        ...
    @typing.overload
    def getEnumItemSets(self) -> typing.List[EnumItemSet]:
        """
            Returns the value being interpreted as an array of enumeration item sets. If the value can't be represented as an array
            of enumeration item sets, ValueConversionException is thrown.
        
            Returns:
                the value being interpreted as an array of enumeration item sets.
        
        """
        ...
    @typing.overload
    def getEnumItemSets(self, int: int, int2: int) -> typing.List[EnumItemSet]: ...
    @typing.overload
    def getEnumItems(self, string: str) -> typing.List[EnumItem]:
        """
            Returns a sub array of the value being interpreted as an array of enumeration items. The subarray starts at startIndex
            and contains the number of element given by length. If startIndex+length is greater than the number of values in the
            underlying array an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of
            size 1, ignoring the arguments.
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as an array of enumeration items.
        
        
        """
        ...
    @typing.overload
    def getEnumItems(self) -> typing.List[EnumItem]:
        """
            Returns the value being interpreted as an array of enumeration items. If the value can't be represented as an array of
            enumeration items, ValueConversionException is thrown.
        
            Returns:
                the value being interpreted as an array of enumeration items.
        
        """
        ...
    @typing.overload
    def getEnumItems(self, int: int, int2: int) -> typing.List[EnumItem]: ...
    @typing.overload
    def getFloat(self, string: str) -> float:
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
    def getFloat(self, string: str, int: int) -> float: ...
    @typing.overload
    def getFloat(self) -> float:
        """
            Returns the value being interpreted as a float. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a float.
        
        """
        ...
    @typing.overload
    def getFloat(self, int: int) -> float: ...
    @typing.overload
    def getFloats(self, string: str) -> typing.List[float]:
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
    def getFloats(self, string: str, int: int, int2: int) -> typing.List[float]: ...
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
    def getFloats(self, int: int, int2: int) -> typing.List[float]: ...
    @typing.overload
    def getInt(self, string: str) -> int:
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
    def getInt(self, string: str, int: int) -> int: ...
    @typing.overload
    def getInt(self) -> int:
        """
            Returns the value being interpreted as a int. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a int.
        
        """
        ...
    @typing.overload
    def getInt(self, int: int) -> int: ...
    @typing.overload
    def getInts(self, string: str) -> typing.List[int]:
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
    @typing.overload
    def getInts(self, string: str, int: int, int2: int) -> typing.List[int]: ...
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
    def getInts(self, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getLength(self, string: str) -> int: ...
    @typing.overload
    def getLength(self) -> int:
        """
            Returns the length of the array if the value is an array. In case the value is not an array the value returned is 1.
        
            Returns:
                the length of the array or 1 in case of a scalar.
        
        
        """
        ...
    @typing.overload
    def getLong(self, string: str) -> int:
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
    def getLong(self, string: str, int: int) -> int: ...
    @typing.overload
    def getLong(self) -> int:
        """
            Returns the value being interpreted as a long. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a long.
        
        """
        ...
    @typing.overload
    def getLong(self, int: int) -> int: ...
    @typing.overload
    def getLongs(self, string: str) -> typing.List[int]:
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
    def getLongs(self, string: str, int: int, int2: int) -> typing.List[int]: ...
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
    def getLongs(self, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getMaxValue(self, string: str) -> float: ...
    @typing.overload
    def getMaxValue(self) -> float:
        """
            Returns the allowed maximum of this value. The maximum is usually the same as the one given by the descriptor. If the
            maximum is dynamic, the one from the descriptor cannot be defined and this method returns the correct value. If no
            maximum is defined the :code:`Double.NaN` is returned.
        
            Returns:
                the allowed maximum of this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getMinValue(self, string: str) -> float: ...
    @typing.overload
    def getMinValue(self) -> float:
        """
            Returns the allowed minimum of this value. The minimum is usually the same as the one given by the descriptor. If the
            minimum is dynamic, the one from the descriptor cannot be defined and this method returns the correct value. If no
            minimum is defined the :code:`Double.NaN` is returned.
        
            Returns:
                the allowed minimum of this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getObject(self, string: str) -> typing.Any:
        """
            Returns the value as an Object. The value returned is the nth one from the array where n is given by the index. If the
            underlying value is not an array the index is ignored the the value is returned. If the value is an array the nth value
            will be returned where n is given by index.
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getObject(self, string: str, int: int) -> typing.Any: ...
    @typing.overload
    def getObject(self) -> typing.Any:
        """
            Returns the value as an object. This method returns the scalar type in their wrapping Object type, arrays and string
            without change and 2D-arrays as :class:`~cern.japc.value.Array2D`.
        
            Returns:
                the value as an object.
        
        """
        ...
    @typing.overload
    def getObject(self, int: int) -> typing.Any: ...
    @typing.overload
    def getRowCount(self, string: str) -> int: ...
    @typing.overload
    def getRowCount(self) -> int:
        """
            Returns the number of rows for the case when the value is represented as 2-dimensional array. For scalar and
            1-dimensional arrays will always return 1.
        
            Returns:
                the number of rows for the case when the value is represented as 2-dimensional array
        
        
        """
        ...
    @typing.overload
    def getShort(self, string: str) -> int:
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
    def getShort(self, string: str, int: int) -> int: ...
    @typing.overload
    def getShort(self) -> int:
        """
            Returns the value being interpreted as a short. If the value is an array only the first value of the array is returned.
        
            Returns:
                the value being interpreted as a short.
        
        """
        ...
    @typing.overload
    def getShort(self, int: int) -> int: ...
    @typing.overload
    def getShorts(self, string: str) -> typing.List[int]:
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
    def getShorts(self, string: str, int: int, int2: int) -> typing.List[int]: ...
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
    def getShorts(self, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getString(self, string: str) -> str:
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
    def getString(self, string: str, int: int) -> str: ...
    @typing.overload
    def getString(self) -> str: ...
    @typing.overload
    def getString(self, int: int) -> str: ...
    @typing.overload
    def getStrings(self, string: str) -> typing.List[str]:
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
    @typing.overload
    def getStrings(self, string: str, int: int, int2: int) -> typing.List[str]: ...
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
    def getStrings(self, int: int, int2: int) -> typing.List[str]: ...
    @typing.overload
    def getUnit(self, string: str) -> str: ...
    @typing.overload
    def getUnit(self) -> str:
        """
            Returns the unit of this value. The unit is usually the same as the one given by the descriptor. If the unit is dynamic,
            the one from the descriptor cannot be defined and this method returns the correct value. If no unit is defined an empty
            string is returned.
        
            Returns:
                the unit of this value or an empty string
        
        
        """
        ...
    def getValueStatus(self) -> SimpleValueStatus:
        """
            Returns the :class:`~cern.japc.value.SimpleValueStatus` object of this value. It represents additional information about
            value acquisition.
        
            Returns:
                the :class:`~cern.japc.value.SimpleValueStatus` object of this value.
        
        
        """
        ...
    @typing.overload
    def getValueType(self, string: str) -> ValueType: ...
    @typing.overload
    def getValueType(self) -> ValueType:
        """
            Returns the value type of the value interpreted by this reader
        
            Returns:
                the value type of the value interpreted by this reader
        
        
        """
        ...
    @typing.overload
    def getXMaxValue(self, string: str) -> float: ...
    @typing.overload
    def getXMaxValue(self) -> float:
        """
            If the value is a function, this method returns the allowed maximum of X axis. The maximum is usually the same as the
            one given by the descriptor. If the maximum is dynamic, the one from the descriptor cannot be defined and this method
            returns the correct value. If the value is not a function or no maximum is defined the :code:`Double.NaN` is returned.
        
            Returns:
                the allowed maximum of X axis for this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getXMinValue(self, string: str) -> float: ...
    @typing.overload
    def getXMinValue(self) -> float:
        """
            If the value is a function, this method returns the allowed minimum of X axis. The minimum is usually the same as the
            one given by the descriptor. If the minimum is dynamic, the one from the descriptor cannot be defined and this method
            returns the correct value. If the value is not a function or no minimum is defined the :code:`Double.NaN` is returned.
        
            Returns:
                the allowed minimum of X axis for this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getXUnit(self, string: str) -> str: ...
    @typing.overload
    def getXUnit(self) -> str:
        """
            If the value is a function, this method returns the unit of X axis. The unit is usually the same as the one given by the
            descriptor. If the unit is dynamic, the one from the descriptor cannot be defined and this method returns the correct
            value. If the value is not a function or no unit is defined an empty string is returned.
        
            Returns:
                the unit of X axis or an empty string
        
        
        """
        ...
    @typing.overload
    def getYMaxValue(self, string: str) -> float: ...
    @typing.overload
    def getYMaxValue(self) -> float:
        """
            If the value is a function, this method returns the allowed maximum of Y axis. The maximum is usually the same as the
            one given by the descriptor. If the maximum is dynamic, the one from the descriptor cannot be defined and this method
            returns the correct value. If no maximum is defined the :code:`Double.NaN` is returned. If the value is not a function
            this method returns the same result as :meth:`~cern.japc.value.SimpleParameterValue.getMaxValue`.
        
            Returns:
                the allowed maximum of Y axis for this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getYMinValue(self, string: str) -> float: ...
    @typing.overload
    def getYMinValue(self) -> float:
        """
            If the value is a function, this method returns the allowed minimum of Y axis. The minimum is usually the same as the
            one given by the descriptor. If the minimum is dynamic, the one from the descriptor cannot be defined and this method
            returns the correct value. If no minimum is defined the :code:`Double.NaN` is returned. If the value is not a function
            this method returns the same result as :meth:`~cern.japc.value.SimpleParameterValue.getMinValue`.
        
            Returns:
                the allowed minimum of Y axis for this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getYUnit(self, string: str) -> str: ...
    @typing.overload
    def getYUnit(self) -> str:
        """
            If the value is a function, this method returns the unit of Y axis. The unit is usually the same as the one given by the
            descriptor. If the unit is dynamic, the one from the descriptor cannot be defined and this method returns the correct
            value. If no unit is defined an empty string is returned. If the value is not a function this method returns the same
            result as :meth:`~cern.japc.value.SimpleParameterValue.getUnit`.
        
            Returns:
                the unit of Y axis or an empty string
        
        
        """
        ...
    def makeMutable(self) -> 'SimpleParameterValue':
        """
            Description copied from interface: :meth:`~cern.japc.value.ParameterValue.makeMutable`
            Creates a mutable version of this ParameterValue that can be set using the setters. The original values are untouched by
            this operation. If this ParameterValue is already mutable this method returns the same instance.
        
            Specified by:
                :meth:`~cern.japc.value.MapParameterValue.makeMutable` in interface :class:`~cern.japc.value.MapParameterValue`
        
            Specified by:
                :meth:`~cern.japc.value.ParameterValue.makeMutable` in interface :class:`~cern.japc.value.ParameterValue`
        
            Returns:
                A new mutable copy of this parameter value or this parameter value itself if it is already mutable.
        
        
        """
        ...
    @typing.overload
    def setBoolean(self, string: str, boolean: bool) -> None:
        """
            Sets the value at the given index to the given boolean. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Parameters:
                index (int): the index where to set the value in the array
                value (boolean): the boolean value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setBoolean(self, string: str, int: int, boolean: bool) -> None: ...
    @typing.overload
    def setBoolean(self, boolean: bool) -> None:
        """
            Sets the value being a boolean. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (boolean): the boolean value.
        
        """
        ...
    @typing.overload
    def setBoolean(self, int: int, boolean: bool) -> None: ...
    @typing.overload
    def setBooleans(self, string: str, booleanArray: typing.List[bool]) -> None: ...
    @typing.overload
    def setBooleans(self, booleanArray: typing.List[bool]) -> None:
        """
            Sets the value being a boolean array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (boolean[]): the boolean array value.
        
        
        """
        ...
    @typing.overload
    def setBooleans2D(self, string: str, booleanArray: typing.List[bool], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setBooleans2D(self, booleanArray: typing.List[bool], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional boolean array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (boolean[]): the boolean array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setByte(self, string: str, byte: int) -> None:
        """
            Sets the value at the given index to the given byte. The value set is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored and the value is set. If this value is not mutable
            an exception is thrown.
        
            Parameters:
                index (int): the index where to set the value in the array
                value (byte): the byte value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setByte(self, string: str, int: int, byte: int) -> None: ...
    @typing.overload
    def setByte(self, byte: int) -> None:
        """
            Sets the value being a byte. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (byte): the byte value.
        
        """
        ...
    @typing.overload
    def setByte(self, int: int, byte: int) -> None: ...
    @typing.overload
    def setBytes(self, string: str, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def setBytes(self, byteArray: typing.List[int]) -> None:
        """
            Sets the value being a byte array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (byte[]): the byte array value.
        
        
        """
        ...
    @typing.overload
    def setBytes2D(self, string: str, byteArray: typing.List[int], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setBytes2D(self, byteArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional byte array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (byte[]): the byte array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setDiscreteFunction(self, string: str, discreteFunction: DiscreteFunction) -> None: ...
    @typing.overload
    def setDiscreteFunction(self, discreteFunction: DiscreteFunction) -> None:
        """
            Sets the value being an :class:`~cern.japc.value.DiscreteFunction`.
        
            Parameters:
                value (:class:`~cern.japc.value.DiscreteFunction`): the DiscreteFunction value.
        
        
        """
        ...
    @typing.overload
    def setDiscreteFunctionList(self, string: str, discreteFunctionList: DiscreteFunctionList) -> None: ...
    @typing.overload
    def setDiscreteFunctionList(self, discreteFunctionList: DiscreteFunctionList) -> None:
        """
            Sets the value being an :class:`~cern.japc.value.DiscreteFunctionList`.
        
            Parameters:
                value (:class:`~cern.japc.value.DiscreteFunctionList`): the DiscreteFunctionList value.
        
        
        """
        ...
    @typing.overload
    def setDouble(self, string: str, double: float) -> None:
        """
            Sets the value at the given index to the given double. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Parameters:
                index (int): the index where to set the value in the array
                value (double): the double value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setDouble(self, string: str, int: int, double: float) -> None: ...
    @typing.overload
    def setDouble(self, double: float) -> None:
        """
            Sets the value being a double. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (double): the double value.
        
        """
        ...
    @typing.overload
    def setDouble(self, int: int, double: float) -> None: ...
    @typing.overload
    def setDoubles(self, string: str, doubleArray: typing.List[float]) -> None: ...
    @typing.overload
    def setDoubles(self, doubleArray: typing.List[float]) -> None:
        """
            Sets the value being a double array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (double[]): the double array value.
        
        
        """
        ...
    @typing.overload
    def setDoubles2D(self, string: str, doubleArray: typing.List[float], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setDoubles2D(self, doubleArray: typing.List[float], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional double array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (double[]): the double array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setEnumItem(self, string: str, enumItem: EnumItem) -> None:
        """
            Sets the value at the given index to the given enumeration item. The value set is the nth one from the array where n is
            given by the index. If the underlying value is not an array the index is ignored and the value is set. If this value is
            not mutable an exception is thrown.
        
            Parameters:
                index (int): the index where to set the value in the array
                value (:class:`~cern.japc.value.EnumItem`): the enumeration item to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setEnumItem(self, enumItem: EnumItem) -> None:
        """
            Sets the value being an :class:`~cern.japc.value.EnumItem`.
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItem`): the EnumItem value.
        
        """
        ...
    @typing.overload
    def setEnumItem(self, int: int, enumItem: EnumItem) -> None: ...
    @typing.overload
    def setEnumItemSet(self, string: str, enumItemSet: EnumItemSet) -> None:
        """
            Sets the value at the given index to the given enumeration items set. The value set is the nth one from the array where
            n is given by the index. If the underlying value is not an array the index is ignored and the value is set. If this
            value is not mutable an exception is thrown.
        
            Parameters:
                index (int): the index where to set the value in the array
                value (:class:`~cern.japc.value.EnumItemSet`): the enumeration items set to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setEnumItemSet(self, enumItemSet: EnumItemSet) -> None:
        """
            Sets the value being an :class:`~cern.japc.value.EnumItemSet`.
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItemSet`): the EnumItemSet value.
        
        """
        ...
    @typing.overload
    def setEnumItemSet(self, int: int, enumItemSet: EnumItemSet) -> None: ...
    @typing.overload
    def setEnumItemSets(self, string: str, enumItemSetArray: typing.List[EnumItemSet]) -> None: ...
    @typing.overload
    def setEnumItemSets(self, enumItemSetArray: typing.List[EnumItemSet]) -> None:
        """
            Sets the value being a EnumItemSet array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItemSet`[]): the EnumItemSet array value.
        
        
        """
        ...
    @typing.overload
    def setEnumItemSets2D(self, string: str, enumItemSetArray: typing.List[EnumItemSet], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setEnumItemSets2D(self, enumItemSetArray: typing.List[EnumItemSet], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional enumeration set array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItemSet`[]): the enumeration set array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setEnumItems(self, string: str, enumItemArray: typing.List[EnumItem]) -> None: ...
    @typing.overload
    def setEnumItems(self, enumItemArray: typing.List[EnumItem]) -> None:
        """
            Sets the value being a EnumItem array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItem`[]): the EnumItem array value.
        
        
        """
        ...
    @typing.overload
    def setEnumItems2D(self, string: str, enumItemArray: typing.List[EnumItem], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setEnumItems2D(self, enumItemArray: typing.List[EnumItem], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional enumeration array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItem`[]): the enumeration array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setFloat(self, string: str, float: float) -> None:
        """
            Sets the value at the given index to the given float. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Parameters:
                index (int): the index where to set the value in the array
                value (float): the float value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setFloat(self, string: str, int: int, float: float) -> None: ...
    @typing.overload
    def setFloat(self, float: float) -> None:
        """
            Sets the value being a float. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (float): the float value.
        
        """
        ...
    @typing.overload
    def setFloat(self, int: int, float: float) -> None: ...
    @typing.overload
    def setFloats(self, string: str, floatArray: typing.List[float]) -> None: ...
    @typing.overload
    def setFloats(self, floatArray: typing.List[float]) -> None:
        """
            Sets the value being a float array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (float[]): the float array value.
        
        
        """
        ...
    @typing.overload
    def setFloats2D(self, string: str, floatArray: typing.List[float], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setFloats2D(self, floatArray: typing.List[float], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional float array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (float[]): the float array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setInt(self, string: str, int: int) -> None:
        """
            Sets the value at the given index to the given int. The value set is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored and the value is set. If this value is not mutable
            an exception is thrown.
        
            Parameters:
                index (int): the index where to set the value in the array
                value (int): the int value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setInt(self, string: str, int: int, int2: int) -> None: ...
    @typing.overload
    def setInt(self, int: int) -> None:
        """
            Sets the value being a int. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (int): the int value.
        
        """
        ...
    @typing.overload
    def setInt(self, int: int, int2: int) -> None: ...
    @typing.overload
    def setInts(self, string: str, intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setInts(self, intArray: typing.List[int]) -> None:
        """
            Sets the value being a int array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (int[]): the int array value.
        
        
        """
        ...
    @typing.overload
    def setInts2D(self, string: str, intArray: typing.List[int], intArray2: typing.List[int]) -> None: ...
    @typing.overload
    def setInts2D(self, intArray: typing.List[int], intArray2: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional int array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (int[]): the int array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setLong(self, string: str, int: int, long: int) -> None: ...
    @typing.overload
    def setLong(self, string: str, long: int) -> None:
        """
            Sets the value at the given index to the given long. The value set is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored and the value is set. If this value is not mutable
            an exception is thrown.
        
            Parameters:
                index (int): the index where to set the value in the array
                value (long): the long value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setLong(self, int: int, long: int) -> None: ...
    @typing.overload
    def setLong(self, long: int) -> None:
        """
            Sets the value being a long. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (long): the long value.
        
        """
        ...
    @typing.overload
    def setLongs(self, string: str, longArray: typing.List[int]) -> None: ...
    @typing.overload
    def setLongs(self, longArray: typing.List[int]) -> None:
        """
            Sets the value being a long array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (long[]): the long array value.
        
        
        """
        ...
    @typing.overload
    def setLongs2D(self, string: str, longArray: typing.List[int], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setLongs2D(self, longArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional long array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (long[]): the long array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setObject(self, string: str, object: typing.Any) -> None: ...
    @typing.overload
    def setObject(self, object: typing.Any) -> None:
        """
            Sets the value as an object. This method can handle any scalar wrapping Object type as well as arrays and string. If
            other type was passed a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` will be
            thrown. If this value is not mutable an exception is thrown.
        
            Parameters:
                o (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value as an object.
        
        
        """
        ...
    @typing.overload
    def setObjects2D(self, string: str, object: typing.Any, intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setObjects2D(self, object: typing.Any, intArray: typing.List[int]) -> None:
        """
            Sets the value as a 2d array of objects. This method can handle any array of primitives and Strings, which will be used
            as a source for 2D array. If other type was passed a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` will be
            thrown. If this value is not mutable an exception is thrown.
        
            Parameters:
                o (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value as an object.
                dimensions (int[]): the dimensions of the 2D array
        
        
        """
        ...
    @typing.overload
    def setShort(self, string: str, int: int, short: int) -> None: ...
    @typing.overload
    def setShort(self, string: str, short: int) -> None:
        """
            Sets the value at the given index to the given short. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Parameters:
                index (int): the index where to set the value in the array
                value (short): the short value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setShort(self, int: int, short: int) -> None: ...
    @typing.overload
    def setShort(self, short: int) -> None:
        """
            Sets the value being a short. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (short): the short value.
        
        """
        ...
    @typing.overload
    def setShorts(self, string: str, shortArray: typing.List[int]) -> None: ...
    @typing.overload
    def setShorts(self, shortArray: typing.List[int]) -> None:
        """
            Sets the value being a short array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (short[]): the short array value.
        
        
        """
        ...
    @typing.overload
    def setShorts2D(self, string: str, shortArray: typing.List[int], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setShorts2D(self, shortArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional short array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (short[]): the short array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setString(self, string: str, int: int, string2: str) -> None: ...
    @typing.overload
    def setString(self, string: str, string2: str) -> None:
        """
            Sets the value at the given index to the given String. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Parameters:
                index (int): the index where to set the value in the array
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the String value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setString(self, int: int, string: str) -> None: ...
    @typing.overload
    def setString(self, string: str) -> None:
        """
            Sets the value being a String. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the String value.
        
        """
        ...
    @typing.overload
    def setStrings(self, string: str, stringArray: typing.List[str]) -> None: ...
    @typing.overload
    def setStrings(self, stringArray: typing.List[str]) -> None:
        """
            Sets the value being a String array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the String array value.
        
        
        """
        ...
    @typing.overload
    def setStrings2D(self, string: str, stringArray: typing.List[str], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setStrings2D(self, stringArray: typing.List[str], intArray: typing.List[int]) -> None:
        """
            Sets the value being a 2-dimensional String array. If this value is not mutable an exception is thrown.
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the String array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    def setValueStatus(self, simpleValueStatus: SimpleValueStatus) -> None:
        """
            Sets the value status.
        
            If the value is immutable a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>` will be thrown.
        
        
            Parameters:
                valueStatus (:class:`~cern.japc.value.SimpleValueStatus`): new valueStatus
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.value")``.

    Array2D: typing.Type[Array2D]
    Array2DBuilder: typing.Type[Array2DBuilder]
    BooleanItem: typing.Type[BooleanItem]
    BooleanType: typing.Type[BooleanType]
    DiscreteFunction: typing.Type[DiscreteFunction]
    DiscreteFunctionList: typing.Type[DiscreteFunctionList]
    EnumItem: typing.Type[EnumItem]
    EnumItemSet: typing.Type[EnumItemSet]
    EnumType: typing.Type[EnumType]
    EnumTypeBitSize: typing.Type[EnumTypeBitSize]
    ImmutableMapParameterValue: typing.Type[ImmutableMapParameterValue]
    MapDescriptor: typing.Type[MapDescriptor]
    MapParameterValue: typing.Type[MapParameterValue]
    ParameterValue: typing.Type[ParameterValue]
    SimpleDescriptor: typing.Type[SimpleDescriptor]
    SimpleParameterValue: typing.Type[SimpleParameterValue]
    SimpleValueControlStatus: typing.Type[SimpleValueControlStatus]
    SimpleValueStandardMeaning: typing.Type[SimpleValueStandardMeaning]
    SimpleValueStatus: typing.Type[SimpleValueStatus]
    Type: typing.Type[Type]
    ValueConversionException: typing.Type[ValueConversionException]
    ValueDescriptor: typing.Type[ValueDescriptor]
    ValueStatus: typing.Type[ValueStatus]
    ValueType: typing.Type[ValueType]
    factory: cern.japc.value.factory.__module_protocol__
    spi: cern.japc.value.spi.__module_protocol__
