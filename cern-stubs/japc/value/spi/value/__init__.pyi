import cern.japc.value
import cern.japc.value.spi.value.core
import cern.japc.value.spi.value.simple
import java.io
import java.lang
import java.util
import typing



class BooleanItemData:
    """
    public class BooleanItemData extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Class containing the data of a single boolean item.
    """
    def __init__(self, boolean: bool, simpleValueStandardMeaning: cern.japc.value.SimpleValueStandardMeaning): ...
    def getStandardMeaning(self) -> cern.japc.value.SimpleValueStandardMeaning:
        """
            Returns the meaning of a boolean item.
        
            Returns:
                the meaning of a boolean item
        
        
        """
        ...
    def getValue(self) -> bool:
        """
            Returns the boolean value of a boolean item.
        
            Returns:
                the boolean value of a boolean item
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class BooleanTypeRegistry:
    """
    public class BooleanTypeRegistry extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory for creating JAPC boolean types and values.
    
        This factory takes care that the boolean types are created only once.
    """
    @staticmethod
    def clearAll() -> None:
        """
            Cleans the information about registered boolean types.
        
        """
        ...
    @typing.overload
    @staticmethod
    def createBooleanTypeName(string: str, string2: str) -> str:
        """
            Creates the unique boolean type name.
        
            The name is unique if it includes device class name, the version of the device design and boolean identifier unique
            within the class design (ex. property with field).
        
            The "default version" is used in this method.
        
            Parameters:
                deviceType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the device type name
                booleanIdentifier (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the boolean identifier
        
            Returns:
                the unique name for a boolean type
        
        """
        ...
    @typing.overload
    @staticmethod
    def createBooleanTypeName(string: str, string2: str, string3: str) -> str:
        """
            Creates the unique boolean type name.
        
            The name is unique if it includes device class name, the version of the device design and boolean identifier unique
            within the class design (ex. property with field).
        
            Parameters:
                deviceType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the device type name
                booleanIdentifier (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the boolean identifier
                version (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the device design version
        
            Returns:
                the unique name for a boolean type
        
        
        """
        ...
    @staticmethod
    def getBooleanType(string: str) -> cern.japc.value.BooleanType:
        """
            Returns a registered boolean type or :code:`null` if such boolean type is not known.
        
            Parameters:
                booleanTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): boolean type name
        
            Returns:
                a registered boolean type or :code:`null` if such boolean type is not known
        
        
        """
        ...
    @staticmethod
    def getBooleanTypeNotNull(string: str) -> cern.japc.value.BooleanType:
        """
            Returns a registered boolean type or throws an exception if such boolean type is not known.
        
            Parameters:
                booleanTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): boolean type name
        
            Returns:
                a registered boolean type
        
            Raises:
                : if boolean type is not known
        
        
        """
        ...
    @staticmethod
    def isRegistered(string: str) -> bool:
        """
            Checks whether an boolean type is registered.
        
            Parameters:
                booleanTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): boolean type name
        
            Returns:
                :code:`true` if the boolean type is registered and :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def registerBooleanType(string: str, booleanItemData: BooleanItemData, booleanItemData2: BooleanItemData) -> cern.japc.value.BooleanType:
        """
            Registers a new boolean type.
        
            Parameters:
                booleanTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): boolean type name
                firstItemData (:class:`~cern.japc.value.spi.value.BooleanItemData`): first :class:`~cern.japc.value.spi.value.BooleanItemData` to build boolean items from (true or false)
                secondItemData (:class:`~cern.japc.value.spi.value.BooleanItemData`): second :class:`~cern.japc.value.spi.value.BooleanItemData` to build boolean items from (true or false)
        
            Returns:
                a created and registered boolean type
        
            Raises:
                : if there is already an boolean type with the same name
        
        
        """
        ...
    @staticmethod
    def registerBooleanTypeIfUnknown(string: str, booleanItemData: BooleanItemData, booleanItemData2: BooleanItemData) -> cern.japc.value.BooleanType:
        """
            Registers a new boolean type only if there is no yet a boolean type with the same name registered.
        
            Parameters:
                booleanTypeName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): boolean type name
                firstItemData (:class:`~cern.japc.value.spi.value.BooleanItemData`): first :class:`~cern.japc.value.spi.value.BooleanItemData` to build boolean items from (true or false)
                secondItemData (:class:`~cern.japc.value.spi.value.BooleanItemData`): second :class:`~cern.japc.value.spi.value.BooleanItemData` to build boolean items from (true or false)
        
            Returns:
                a created and registered or existing boolean type
        
        
        """
        ...

class EnumItemData:
    """
    public class EnumItemData extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Class containing the data of a single enumeration item.
    """
    @typing.overload
    def __init__(self, long: int, string: str): ...
    @typing.overload
    def __init__(self, long: int, string: str, simpleValueStandardMeaning: cern.japc.value.SimpleValueStandardMeaning, boolean: bool): ...
    def getCode(self) -> int:
        """
            Returns an integer code of this enumeration item
        
            Returns:
                an integer code of this enumeration item
        
        
        """
        ...
    def getStandardMeaning(self) -> cern.japc.value.SimpleValueStandardMeaning:
        """
            Returns the meaning of this enumeration item.
        
            Returns:
                the meaning of this enumeration item
        
        
        """
        ...
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
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class EnumItemSetImpl(java.util.AbstractSet[cern.japc.value.EnumItem], cern.japc.value.EnumItemSet, java.io.Serializable):
    """
    public class EnumItemSetImpl extends `AbstractSet <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/AbstractSet.html?is-external=true>`<:class:`~cern.japc.value.EnumItem`> implements :class:`~cern.japc.value.EnumItemSet`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Default implementation of the enumeration item set.
    
        The implementation idea is taken from `null
        <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/EnumSet.html?is-external=true>` implementation and its
        subclass RegularEnumSet.
    
        This implementation doesn't accept :code:`null:code:`values.``
    
        See Also:
          :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, enumItem: cern.japc.value.EnumItem, enumItemArray: typing.List[cern.japc.value.EnumItem]): ...
    @typing.overload
    def __init__(self, enumType: cern.japc.value.EnumType, enumItemArray: typing.List[cern.japc.value.EnumItem]): ...
    @typing.overload
    def __init__(self, enumType: cern.japc.value.EnumType, long: int): ...
    def add(self, enumItem: cern.japc.value.EnumItem) -> bool:
        """
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def addAll(self, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.value.EnumItemSet.addAll`
            Syntactical sugar around `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true#addAll(java.util.Collection)>`
            method.
        
            Specified by:
                :meth:`~cern.japc.value.EnumItemSet.addAll` in interface :class:`~cern.japc.value.EnumItemSet`
        
            Parameters:
                enumItems (:class:`~cern.japc.value.EnumItem`...): enumeration items to add
        
            Returns:
                ``true`` if this set changed as a result of the call
        
        public boolean addAll (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<? extends :class:`~cern.japc.value.EnumItem`> c)
        
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def addAll(self, collection: typing.Union[java.util.Collection[cern.japc.value.EnumItem], typing.Sequence[cern.japc.value.EnumItem]]) -> bool: ...
    def asLong(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.EnumItemSet.asLong`
            Returns the set encoded into a long.
        
            Specified by:
                :meth:`~cern.japc.value.EnumItemSet.asLong` in interface :class:`~cern.japc.value.EnumItemSet`
        
            Returns:
                a long corresponding to the set
        
        
        """
        ...
    def clear(self) -> None:
        """
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    def clone(self) -> cern.japc.value.EnumItemSet:
        """
            Description copied from interface: :meth:`~cern.japc.value.EnumItemSet.clone`
            Returns a deep copy of this set. The copy is guarantee to be deep.
        
            Specified by:
                :meth:`~cern.japc.value.EnumItemSet.clone` in interface :class:`~cern.japc.value.EnumItemSet`
        
            Overrides:
                 in class 
        
            Returns:
                a deep copy of this set.
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def contains(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def containsAll(self, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.value.EnumItemSet.containsAll`
            Syntactical sugar around `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true#containsAll(java.util.Collection)>`
            method.
        
            Specified by:
                :meth:`~cern.japc.value.EnumItemSet.containsAll` in interface :class:`~cern.japc.value.EnumItemSet`
        
            Parameters:
                enumItems (:class:`~cern.japc.value.EnumItem`...): enumeration items to check for
        
            Returns:
                ``true`` if this set contains all of the elements
        
        public boolean containsAll (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<?> c)
        
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def containsAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def getEnumType(self) -> cern.japc.value.EnumType:
        """
            Description copied from interface: :meth:`~cern.japc.value.EnumItemSet.getEnumType`
            Returns the enumeration type of this set.
        
            Specified by:
                :meth:`~cern.japc.value.EnumItemSet.getEnumType` in interface :class:`~cern.japc.value.EnumItemSet`
        
            Returns:
                the enumeration type of this set
        
        
        """
        ...
    def isEmpty(self) -> bool:
        """
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator[cern.japc.value.EnumItem]: ...
    def remove(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def removeAll(self, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.value.EnumItemSet.removeAll`
            Syntactical sugar around `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true#removeAll(java.util.Collection)>`
            method.
        
            Specified by:
                :meth:`~cern.japc.value.EnumItemSet.removeAll` in interface :class:`~cern.japc.value.EnumItemSet`
        
            Parameters:
                enumItems (:class:`~cern.japc.value.EnumItem`...): enumeration items to add
        
            Returns:
                ``true`` if this set changed as a result of the call
        
        public boolean removeAll (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<?> c)
        
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def removeAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    @typing.overload
    def retainAll(self, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.value.EnumItemSet.retainAll`
            Syntactical sugar around `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true#retainAll(java.util.Collection)>`
            method.
        
            Specified by:
                :meth:`~cern.japc.value.EnumItemSet.retainAll` in interface :class:`~cern.japc.value.EnumItemSet`
        
            Parameters:
                enumItems (:class:`~cern.japc.value.EnumItem`...): enumeration items to add
        
            Returns:
                ``true`` if this set changed as a result of the call
        
        public boolean retainAll (`Collection <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/util/Collection.html?is-external=true>`<?> c)
        
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def retainAll(self, collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any]]) -> bool: ...
    def size(self) -> int:
        """
        
            Specified by:
                 in interface 
        
            Specified by:
                 in interface 
        
            Specified by:
                 in class 
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class EnumerationRegistry:
    """
    public class EnumerationRegistry extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Factory for creating JAPC enumeration types and values.
    
        This factory takes care that the enumeration types are created only once.
    """
    @staticmethod
    def clearAll() -> None:
        """
            Cleans the information about registered enumerations.
        
        """
        ...
    @typing.overload
    @staticmethod
    def createEnumTypeName(string: str, string2: str) -> str:
        """
            Creates the unique enumeration type name.
        
            The name is unique if it includes device class name, the version of the device design and enum identifier unique within
            the class design (ex. property with field).
        
            The "default version" is used in this method.
        
            Parameters:
                deviceType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the device type name
                enumName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the enumeration name
        
            Returns:
                the unique name for an enumeration type
        
        """
        ...
    @typing.overload
    @staticmethod
    def createEnumTypeName(string: str, string2: str, string3: str) -> str:
        """
            Creates the unique enumeration type name.
        
            The name is unique if it includes device class name, the version of the device design and enum identifier unique within
            the class design (ex. property with field).
        
            Parameters:
                deviceType (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the device type name
                enumName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the enumeration name
                version (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the device design version
        
            Returns:
                the unique name for an enumeration type
        
        
        """
        ...
    @staticmethod
    def getEnumType(string: str) -> cern.japc.value.EnumType:
        """
            Returns a registered enumeration type or :code:`null` if such enumeration type is not known.
        
            Parameters:
                enumName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): enumeration type name
        
            Returns:
                a registered enumeration type or :code:`null` if such enumeration type is not known
        
        
        """
        ...
    @staticmethod
    def getEnumTypeNotNull(string: str) -> cern.japc.value.EnumType:
        """
            Returns a registered enumeration type or throws an exception if such enumeration type is not known.
        
            Parameters:
                enumName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): enumeration type name
        
            Returns:
                a registered enumeration type
        
            Raises:
                : if enumeration type is not known
        
        
        """
        ...
    @staticmethod
    def isRegistered(string: str) -> bool:
        """
            Checks whether an enumeration type is registered.
        
            Parameters:
                enumName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): enumeration type name
        
            Returns:
                :code:`true` if the enumeration type is registered and :code:`false` otherwise
        
        
        """
        ...
    @staticmethod
    def registerEnumType(string: str, enumTypeBitSize: cern.japc.value.EnumTypeBitSize, set: java.util.Set[EnumItemData]) -> cern.japc.value.EnumType: ...
    @staticmethod
    def registerEnumTypeIfUnknown(string: str, enumTypeBitSize: cern.japc.value.EnumTypeBitSize, set: java.util.Set[EnumItemData]) -> cern.japc.value.EnumType: ...

class InternalDiscreteFunctionFactory:
    """
    public class InternalDiscreteFunctionFactory extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        This factory is used to produce :class:`~cern.japc.value.DiscreteFunction` and
        :class:`~cern.japc.value.DiscreteFunctionList` implementations.
    
        This factory is supposed to be used internally. If you need a public factory for
        :class:`~cern.japc.value.DiscreteFunction` and :class:`~cern.japc.value.DiscreteFunctionList` implementations please use
        :class:`~cern.japc.value.factory.DomainValueFactory`.
    """
    def __init__(self): ...
    @staticmethod
    def newDiscreteFunction(doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> cern.japc.value.DiscreteFunction:
        """
            Creates a new :class:`~cern.japc.value.DiscreteFunction`.
        
            Parameters:
                xArray (double[]): an array of X coordinates
                yArray (double[]): an array of Y coordinates
        
            Returns:
                constructed :class:`~cern.japc.value.DiscreteFunction`
        
        
        """
        ...
    @staticmethod
    def newDiscreteFunctionList(discreteFunctionArray: typing.List[cern.japc.value.DiscreteFunction]) -> cern.japc.value.DiscreteFunctionList:
        """
            Creates a new :class:`~cern.japc.value.DiscreteFunctionList`.
        
            Parameters:
                functions (:class:`~cern.japc.value.DiscreteFunction`...): discrete function which should compose the list
        
            Returns:
                constructed :class:`~cern.japc.value.DiscreteFunctionList`
        
        
        """
        ...

class SimpleParameterValueImpl(cern.japc.value.spi.value.simple.AbstractMapSimpleValue, java.lang.Cloneable, java.io.Serializable):
    """
    public class SimpleParameterValueImpl extends :class:`~cern.japc.value.spi.value.simple.AbstractMapSimpleValue` implements `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        This class provides methods to edit a simple type value (scalars, strings, array of scalars, array of strings).
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, simpleParameterValue: cern.japc.value.SimpleParameterValue): ...
    def clone(self) -> typing.Any:
        """
            Description copied from interface: :meth:`~cern.japc.value.ParameterValue.clone`
            Returns a deep copy of this ParameterValue. The copy is guarantee to be deep.
        
            Specified by:
                :meth:`~cern.japc.value.ParameterValue.clone` in interface :class:`~cern.japc.value.ParameterValue`
        
            Overrides:
                :meth:`~cern.japc.value.spi.value.core.ParameterValueImpl.clone`Â in
                classÂ :class:`~cern.japc.value.spi.value.core.ParameterValueImpl`
        
            Returns:
                a deep copy of this ParameterValue.
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def getArray2D(self) -> cern.japc.value.Array2D:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getArray2D`
            Returns a wrapper around the value being interpreted as a 2d array. If the value is a 1d array it is encapsulated in an
            array of size 1xn. If the value is not an array it is encapsulated in an array of size 1x1. IMPORTANT: if the value is
            mutable and is changed after the wrapper is got the wrapper becomes invalide and can return wrong values or even throw
            OutOfBoundException.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getArray2D` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a boolean 2d array.
        
        
        """
        ...
    @typing.overload
    def getArray2D(self, string: str) -> cern.japc.value.Array2D: ...
    @typing.overload
    def getBoolean(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getBoolean`
            Returns the value being interpreted as a boolean. If the value is an array only the first value of the array is
            returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getBoolean` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a boolean.
        
        """
        ...
    @typing.overload
    def getBoolean(self, int: int) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getBoolean`
            Returns the value being interpreted as a boolean. The value returned is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getBoolean` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getBoolean(self, string: str) -> bool: ...
    @typing.overload
    def getBoolean(self, string: str, int: int) -> bool: ...
    @typing.overload
    def getBooleans(self) -> typing.List[bool]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getBooleans`
            Returns the value being interpreted as a boolean array. The array returned is not linked to the underlying array stored
            in this value. Only in the case this value is of type boolean array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getBooleans` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a boolean array.
        
        """
        ...
    @typing.overload
    def getBooleans(self, int: int, int2: int) -> typing.List[bool]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getBooleans`
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getBooleans` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a boolean array.
        
        
        """
        ...
    @typing.overload
    def getBooleans(self, string: str) -> typing.List[bool]: ...
    @typing.overload
    def getBooleans(self, string: str, int: int, int2: int) -> typing.List[bool]: ...
    @typing.overload
    def getByte(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getByte`
            Returns the value being interpreted as a byte. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getByte` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a byte.
        
        """
        ...
    @typing.overload
    def getByte(self, int: int) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getByte`
            Returns the value being interpreted as a byte. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getByte` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getByte(self, string: str) -> int: ...
    @typing.overload
    def getByte(self, string: str, int: int) -> int: ...
    @typing.overload
    def getBytes(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getBytes`
            Returns the value being interpreted as a byte array. The array returned is not linked to the underlying array stored in
            this value. Only in the case this value is of type byte array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getBytes` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a byte array.
        
        """
        ...
    @typing.overload
    def getBytes(self, int: int, int2: int) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getBytes`
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getBytes` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a byte array.
        
        
        """
        ...
    @typing.overload
    def getBytes(self, string: str) -> typing.List[int]: ...
    @typing.overload
    def getBytes(self, string: str, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getColumnCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getColumnCount`
            Returns the number of columns for the case when the value is represented as 2-dimensional array. For scalar which are
            not bit-pattern will always return 1.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getColumnCount`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the number of columns for the case when the value is represented as 2-dimensional array
        
        
        """
        ...
    @typing.overload
    def getColumnCount(self, string: str) -> int: ...
    @typing.overload
    def getDiscreteFunction(self) -> cern.japc.value.DiscreteFunction:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getDiscreteFunction`
            Returns the value being interpreted as a discrete function. If the value can't be represented as a discrete function a
            ValueConversionException is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getDiscreteFunction`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a discrete function.
        
        
        """
        ...
    @typing.overload
    def getDiscreteFunction(self, string: str) -> cern.japc.value.DiscreteFunction: ...
    @typing.overload
    def getDiscreteFunctionList(self) -> cern.japc.value.DiscreteFunctionList:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getDiscreteFunctionList`
            Returns the value being interpreted as a discrete function list. If the value can't be represented as a discrete
            function list a ValueConversionException is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getDiscreteFunctionList`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a discrete function list.
        
        
        """
        ...
    @typing.overload
    def getDiscreteFunctionList(self, string: str) -> cern.japc.value.DiscreteFunctionList: ...
    @typing.overload
    def getDouble(self) -> float:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getDouble`
            Returns the value being interpreted as a double. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getDouble` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a double.
        
        """
        ...
    @typing.overload
    def getDouble(self, int: int) -> float:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getDouble`
            Returns the value being interpreted as a double. The value returned is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getDouble` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getDouble(self, string: str) -> float: ...
    @typing.overload
    def getDouble(self, string: str, int: int) -> float: ...
    @typing.overload
    def getDoubles(self) -> typing.List[float]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getDoubles`
            Returns the value being interpreted as a double array. The array returned is not linked to the underlying array stored
            in this value. Only in the case this value is of type double array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getDoubles` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a double array.
        
        """
        ...
    @typing.overload
    def getDoubles(self, int: int, int2: int) -> typing.List[float]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getDoubles`
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getDoubles` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a double array.
        
        
        """
        ...
    @typing.overload
    def getDoubles(self, string: str) -> typing.List[float]: ...
    @typing.overload
    def getDoubles(self, string: str, int: int, int2: int) -> typing.List[float]: ...
    @typing.overload
    def getEnumItem(self) -> cern.japc.value.EnumItem:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getEnumItem`
            Returns the value being interpreted as an enumeration item. If the value can't be represented as an enumeration item
            (value is boolean, array or there is no information about enumeration type, etc) an ValueConversionException is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getEnumItem` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as an enumeration item.
        
        """
        ...
    @typing.overload
    def getEnumItem(self, int: int) -> cern.japc.value.EnumItem:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getEnumItem`
            Returns the value being interpreted as an enumeration. The value returned is the nth one from the array where n is given
            by the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getEnumItem` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getEnumItem(self, string: str) -> cern.japc.value.EnumItem: ...
    @typing.overload
    def getEnumItemSet(self) -> cern.japc.value.EnumItemSet:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getEnumItemSet`
            Returns the value being interpreted as an enumeration item set. If the value can't be represented as an enumeration item
            set (value is boolean, array or there is no information about enumeration type, etc) an ValueConversionException is
            thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getEnumItemSet`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as an enumeration item set.
        
        """
        ...
    @typing.overload
    def getEnumItemSet(self, int: int) -> cern.japc.value.EnumItemSet:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getEnumItemSet`
            Returns the value being interpreted as an enumeration set. The value returned is the nth one from the array where n is
            given by the index. If the underlying value is not an array the index is ignored the the value is returned. If the value
            is an array the nth value will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getEnumItemSet`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getEnumItemSet(self, string: str) -> cern.japc.value.EnumItemSet: ...
    @typing.overload
    def getEnumItemSets(self) -> typing.List[cern.japc.value.EnumItemSet]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getEnumItemSets`
            Returns the value being interpreted as an array of enumeration item sets. If the value can't be represented as an array
            of enumeration item sets, ValueConversionException is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getEnumItemSets`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as an array of enumeration item sets.
        
        """
        ...
    @typing.overload
    def getEnumItemSets(self, int: int, int2: int) -> typing.List[cern.japc.value.EnumItemSet]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getEnumItemSets`
            Returns a sub array of the value being interpreted as an array of enumeration item sets. The subarray starts at
            startIndex and contains the number of element given by length. If startIndex+length is greater than the number of values
            in the underlying array an exception is thrown. If the value is not an array, the value is returned encapsulated in an
            array of size 1, ignoring the arguments.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getEnumItemSets`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as an array of enumeration items.
        
        
        """
        ...
    @typing.overload
    def getEnumItemSets(self, string: str) -> typing.List[cern.japc.value.EnumItemSet]: ...
    @typing.overload
    def getEnumItems(self) -> typing.List[cern.japc.value.EnumItem]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getEnumItems`
            Returns the value being interpreted as an array of enumeration items. If the value can't be represented as an array of
            enumeration items, ValueConversionException is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getEnumItems` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as an array of enumeration items.
        
        """
        ...
    @typing.overload
    def getEnumItems(self, int: int, int2: int) -> typing.List[cern.japc.value.EnumItem]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getEnumItems`
            Returns a sub array of the value being interpreted as an array of enumeration items. The subarray starts at startIndex
            and contains the number of element given by length. If startIndex+length is greater than the number of values in the
            underlying array an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of
            size 1, ignoring the arguments.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getEnumItems` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as an array of enumeration items.
        
        
        """
        ...
    @typing.overload
    def getEnumItems(self, string: str) -> typing.List[cern.japc.value.EnumItem]: ...
    @typing.overload
    def getFloat(self) -> float:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getFloat`
            Returns the value being interpreted as a float. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getFloat` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a float.
        
        """
        ...
    @typing.overload
    def getFloat(self, int: int) -> float:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getFloat`
            Returns the value being interpreted as a float. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getFloat` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getFloat(self, string: str) -> float: ...
    @typing.overload
    def getFloat(self, string: str, int: int) -> float: ...
    @typing.overload
    def getFloats(self) -> typing.List[float]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getFloats`
            Returns the value being interpreted as a float array. The array returned is not linked to the underlying array stored in
            this value. Only in the case this value is of type float array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getFloats` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a float array.
        
        """
        ...
    @typing.overload
    def getFloats(self, int: int, int2: int) -> typing.List[float]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getFloats`
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getFloats` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a float array.
        
        
        """
        ...
    @typing.overload
    def getFloats(self, string: str) -> typing.List[float]: ...
    @typing.overload
    def getFloats(self, string: str, int: int, int2: int) -> typing.List[float]: ...
    @typing.overload
    def getInt(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getInt`
            Returns the value being interpreted as a int. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getInt` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a int.
        
        """
        ...
    @typing.overload
    def getInt(self, int: int) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getInt`
            Returns the value being interpreted as a int. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getInt` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getInt(self, string: str) -> int: ...
    @typing.overload
    def getInt(self, string: str, int: int) -> int: ...
    @typing.overload
    def getInts(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getInts`
            Returns the value being interpreted as a int array. The array returned is not linked to the underlying array stored in
            this value. Only in the case this value is of type int array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getInts` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a int array.
        
        """
        ...
    @typing.overload
    def getInts(self, int: int, int2: int) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getInts`
            Returns the value being interpreted as a int array. If the value is not an array it is encapsulated in an array of size
            1
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getInts` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a int array.
        
        
        """
        ...
    @typing.overload
    def getInts(self, string: str) -> typing.List[int]: ...
    @typing.overload
    def getInts(self, string: str, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getLength(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getLength`
            Returns the length of the array if the value is an array. In case the value is not an array the value returned is 1.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getLength` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the length of the array or 1 in case of a scalar.
        
        
        """
        ...
    @typing.overload
    def getLength(self, string: str) -> int: ...
    @typing.overload
    def getLong(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getLong`
            Returns the value being interpreted as a long. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getLong` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a long.
        
        """
        ...
    @typing.overload
    def getLong(self, int: int) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getLong`
            Returns the value being interpreted as a long. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getLong` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getLong(self, string: str) -> int: ...
    @typing.overload
    def getLong(self, string: str, int: int) -> int: ...
    @typing.overload
    def getLongs(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getLongs`
            Returns the value being interpreted as a long array. The array returned is not linked to the underlying array stored in
            this value. Only in the case this value is of type long array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getLongs` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a long array.
        
        """
        ...
    @typing.overload
    def getLongs(self, int: int, int2: int) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getLongs`
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getLongs` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a long array.
        
        
        """
        ...
    @typing.overload
    def getLongs(self, string: str) -> typing.List[int]: ...
    @typing.overload
    def getLongs(self, string: str, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getMaxValue(self) -> float:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getMaxValue`
            Returns the allowed maximum of this value. The maximum is usually the same as the one given by the descriptor. If the
            maximum is dynamic, the one from the descriptor cannot be defined and this method returns the correct value. If no
            maximum is defined the :code:`Double.NaN` is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getMaxValue` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the allowed maximum of this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getMaxValue(self, string: str) -> float: ...
    @typing.overload
    def getMinValue(self) -> float:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getMinValue`
            Returns the allowed minimum of this value. The minimum is usually the same as the one given by the descriptor. If the
            minimum is dynamic, the one from the descriptor cannot be defined and this method returns the correct value. If no
            minimum is defined the :code:`Double.NaN` is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getMinValue` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the allowed minimum of this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getMinValue(self, string: str) -> float: ...
    @typing.overload
    def getObject(self) -> typing.Any:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getObject`
            Returns the value as an object. This method returns the scalar type in their wrapping Object type, arrays and string
            without change and 2D-arrays as :class:`~cern.japc.value.Array2D`.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getObject` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value as an object.
        
        """
        ...
    @typing.overload
    def getObject(self, int: int) -> typing.Any:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getObject`
            Returns the value as an Object. The value returned is the nth one from the array where n is given by the index. If the
            underlying value is not an array the index is ignored the the value is returned. If the value is an array the nth value
            will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getObject` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getObject(self, string: str) -> typing.Any: ...
    @typing.overload
    def getObject(self, string: str, int: int) -> typing.Any: ...
    @typing.overload
    def getRowCount(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getRowCount`
            Returns the number of rows for the case when the value is represented as 2-dimensional array. For scalar and
            1-dimensional arrays will always return 1.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getRowCount` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the number of rows for the case when the value is represented as 2-dimensional array
        
        
        """
        ...
    @typing.overload
    def getRowCount(self, string: str) -> int: ...
    @typing.overload
    def getShort(self) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getShort`
            Returns the value being interpreted as a short. If the value is an array only the first value of the array is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getShort` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a short.
        
        """
        ...
    @typing.overload
    def getShort(self, int: int) -> int:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getShort`
            Returns the value being interpreted as a short. The value returned is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an array
            the nth value will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getShort` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getShort(self, string: str) -> int: ...
    @typing.overload
    def getShort(self, string: str, int: int) -> int: ...
    @typing.overload
    def getShorts(self) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getShorts`
            Returns the value being interpreted as a short array. The array returned is not linked to the underlying array stored in
            this value. Only in the case this value is of type short array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getShorts` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a short array.
        
        """
        ...
    @typing.overload
    def getShorts(self, int: int, int2: int) -> typing.List[int]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getShorts`
            Returns a sub array of the value being interpreted as a boolean array. The subarray starts at startIndex and contains
            the number of element given by length. If startIndex+length is greater than the number of values in the underlying array
            an exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getShorts` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a short array.
        
        
        """
        ...
    @typing.overload
    def getShorts(self, string: str) -> typing.List[int]: ...
    @typing.overload
    def getShorts(self, string: str, int: int, int2: int) -> typing.List[int]: ...
    @typing.overload
    def getString(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.value.ParameterValue.getString`
            Returns the value as a string. This method should be specially useful for client that just want to display the value
            without any interpretation. The string returned should be as useful as possible for the clients.
        
            Specified by:
                :meth:`~cern.japc.value.ParameterValue.getString` in interface :class:`~cern.japc.value.ParameterValue`
        
            Returns:
                a string representing the value as a string.
        
        """
        ...
    @typing.overload
    def getString(self, int: int) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getString`
            Returns the value being interpreted as a String. The value returned is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored the the value is returned. If the value is an
            array the nth value will be returned where n is given by index.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getString` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index in the array at which to get the value
        
            Returns:
                the nth value of the array
        
        
        """
        ...
    @typing.overload
    def getString(self, string: str) -> str: ...
    @typing.overload
    def getString(self, string: str, int: int) -> str: ...
    @typing.overload
    def getStrings(self) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getStrings`
            Returns the value being interpreted as a String array. The array returned is not linked to the underlying array stored
            in this value. Only in the case this value is of type String array and is mutable, the array returned is actually the
            underlying one. In that last case, changes in the returned array directly affect this value. If the value is not an
            array it is encapsulated in an array of size 1
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getStrings` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value being interpreted as a String array.
        
        """
        ...
    @typing.overload
    def getStrings(self, int: int, int2: int) -> typing.List[str]:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getStrings`
            Returns a sub array of the value being interpreted as a string array. The subarray starts at startIndex and contains the
            number of element given by length. If startIndex+length is greater than the number of values in the underlying array an
            exception is thrown. If the value is not an array, the value is returned encapsulated in an array of size 1, ignoring
            the arguments.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getStrings` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                startIndex (int): the index of the first element of the array to return
                length (int): the number of elements in the array to return (starting from startIndex)
        
            Returns:
                the value being interpreted as a String array.
        
        
        """
        ...
    @typing.overload
    def getStrings(self, string: str) -> typing.List[str]: ...
    @typing.overload
    def getStrings(self, string: str, int: int, int2: int) -> typing.List[str]: ...
    @typing.overload
    def getUnit(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getUnit`
            Returns the unit of this value. The unit is usually the same as the one given by the descriptor. If the unit is dynamic,
            the one from the descriptor cannot be defined and this method returns the correct value. If no unit is defined an empty
            string is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getUnit` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the unit of this value or an empty string
        
        
        """
        ...
    @typing.overload
    def getUnit(self, string: str) -> str: ...
    def getValueStatus(self) -> cern.japc.value.SimpleValueStatus:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getValueStatus`
            Returns the :class:`~cern.japc.value.SimpleValueStatus` object of this value. It represents additional information about
            value acquisition.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getValueStatus`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the :class:`~cern.japc.value.SimpleValueStatus` object of this value.
        
        
        """
        ...
    @typing.overload
    def getValueType(self) -> cern.japc.value.ValueType:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getValueType`
            Returns the value type of the value interpreted by this reader
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getValueType` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the value type of the value interpreted by this reader
        
        
        """
        ...
    @typing.overload
    def getValueType(self, string: str) -> cern.japc.value.ValueType: ...
    @typing.overload
    def getXMaxValue(self) -> float:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getXMaxValue`
            If the value is a function, this method returns the allowed maximum of X axis. The maximum is usually the same as the
            one given by the descriptor. If the maximum is dynamic, the one from the descriptor cannot be defined and this method
            returns the correct value. If the value is not a function or no maximum is defined the :code:`Double.NaN` is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getXMaxValue` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the allowed maximum of X axis for this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getXMaxValue(self, string: str) -> float: ...
    @typing.overload
    def getXMinValue(self) -> float:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getXMinValue`
            If the value is a function, this method returns the allowed minimum of X axis. The minimum is usually the same as the
            one given by the descriptor. If the minimum is dynamic, the one from the descriptor cannot be defined and this method
            returns the correct value. If the value is not a function or no minimum is defined the :code:`Double.NaN` is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getXMinValue` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the allowed minimum of X axis for this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getXMinValue(self, string: str) -> float: ...
    @typing.overload
    def getXUnit(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getXUnit`
            If the value is a function, this method returns the unit of X axis. The unit is usually the same as the one given by the
            descriptor. If the unit is dynamic, the one from the descriptor cannot be defined and this method returns the correct
            value. If the value is not a function or no unit is defined an empty string is returned.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getXUnit` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the unit of X axis or an empty string
        
        
        """
        ...
    @typing.overload
    def getXUnit(self, string: str) -> str: ...
    @typing.overload
    def getYMaxValue(self) -> float:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getYMaxValue`
            If the value is a function, this method returns the allowed maximum of Y axis. The maximum is usually the same as the
            one given by the descriptor. If the maximum is dynamic, the one from the descriptor cannot be defined and this method
            returns the correct value. If no maximum is defined the :code:`Double.NaN` is returned. If the value is not a function
            this method returns the same result as :meth:`~cern.japc.value.SimpleParameterValue.getMaxValue`.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getYMaxValue` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the allowed maximum of Y axis for this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getYMaxValue(self, string: str) -> float: ...
    @typing.overload
    def getYMinValue(self) -> float:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getYMinValue`
            If the value is a function, this method returns the allowed minimum of Y axis. The minimum is usually the same as the
            one given by the descriptor. If the minimum is dynamic, the one from the descriptor cannot be defined and this method
            returns the correct value. If no minimum is defined the :code:`Double.NaN` is returned. If the value is not a function
            this method returns the same result as :meth:`~cern.japc.value.SimpleParameterValue.getMinValue`.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getYMinValue` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the allowed minimum of Y axis for this value or :code:`Double.NaN`
        
        
        """
        ...
    @typing.overload
    def getYMinValue(self, string: str) -> float: ...
    @typing.overload
    def getYUnit(self) -> str:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.getYUnit`
            If the value is a function, this method returns the unit of Y axis. The unit is usually the same as the one given by the
            descriptor. If the unit is dynamic, the one from the descriptor cannot be defined and this method returns the correct
            value. If no unit is defined an empty string is returned. If the value is not a function this method returns the same
            result as :meth:`~cern.japc.value.SimpleParameterValue.getUnit`.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.getYUnit` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Returns:
                the unit of Y axis or an empty string
        
        
        """
        ...
    @typing.overload
    def getYUnit(self, string: str) -> str: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def setBoolean(self, boolean: bool) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setBoolean`
            Sets the value being a boolean. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setBoolean` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (boolean): the boolean value.
        
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setBoolean`
            Sets the value at the given index to the given boolean. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setBoolean` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index where to set the value in the array
                value (boolean): the boolean value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setBoolean(self, int: int, boolean: bool) -> None: ...
    @typing.overload
    def setBoolean(self, string: str, boolean: bool) -> None: ...
    @typing.overload
    def setBoolean(self, string: str, int: int, boolean: bool) -> None: ...
    @typing.overload
    def setBooleans(self, booleanArray: typing.List[bool]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setBooleans`
            Sets the value being a boolean array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setBooleans` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (boolean[]): the boolean array value.
        
        
        """
        ...
    @typing.overload
    def setBooleans(self, string: str, booleanArray: typing.List[bool]) -> None: ...
    @typing.overload
    def setBooleans2D(self, booleanArray: typing.List[bool], intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setBooleans2D`
            Sets the value being a 2-dimensional boolean array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setBooleans2D` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (boolean[]): the boolean array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setBooleans2D(self, string: str, booleanArray: typing.List[bool], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setByte(self, byte: int) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setByte`
            Sets the value being a byte. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setByte` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (byte): the byte value.
        
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setByte`
            Sets the value at the given index to the given byte. The value set is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored and the value is set. If this value is not mutable
            an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setByte` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index where to set the value in the array
                value (byte): the byte value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setByte(self, int: int, byte: int) -> None: ...
    @typing.overload
    def setByte(self, string: str, byte: int) -> None: ...
    @typing.overload
    def setByte(self, string: str, int: int, byte: int) -> None: ...
    @typing.overload
    def setBytes(self, byteArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setBytes`
            Sets the value being a byte array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setBytes` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (byte[]): the byte array value.
        
        
        """
        ...
    @typing.overload
    def setBytes(self, string: str, byteArray: typing.List[int]) -> None: ...
    @typing.overload
    def setBytes2D(self, byteArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setBytes2D`
            Sets the value being a 2-dimensional byte array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setBytes2D` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (byte[]): the byte array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setBytes2D(self, string: str, byteArray: typing.List[int], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setDiscreteFunction(self, discreteFunction: cern.japc.value.DiscreteFunction) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setDiscreteFunction`
            Sets the value being an :class:`~cern.japc.value.DiscreteFunction`.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setDiscreteFunction`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (:class:`~cern.japc.value.DiscreteFunction`): the DiscreteFunction value.
        
        
        """
        ...
    @typing.overload
    def setDiscreteFunction(self, string: str, discreteFunction: cern.japc.value.DiscreteFunction) -> None: ...
    @typing.overload
    def setDiscreteFunctionList(self, discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setDiscreteFunctionList`
            Sets the value being an :class:`~cern.japc.value.DiscreteFunctionList`.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setDiscreteFunctionList`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (:class:`~cern.japc.value.DiscreteFunctionList`): the DiscreteFunctionList value.
        
        
        """
        ...
    @typing.overload
    def setDiscreteFunctionList(self, string: str, discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> None: ...
    @typing.overload
    def setDouble(self, double: float) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setDouble`
            Sets the value being a double. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setDouble` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (double): the double value.
        
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setDouble`
            Sets the value at the given index to the given double. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setDouble` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index where to set the value in the array
                value (double): the double value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setDouble(self, int: int, double: float) -> None: ...
    @typing.overload
    def setDouble(self, string: str, double: float) -> None: ...
    @typing.overload
    def setDouble(self, string: str, int: int, double: float) -> None: ...
    @typing.overload
    def setDoubles(self, doubleArray: typing.List[float]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setDoubles`
            Sets the value being a double array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setDoubles` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (double[]): the double array value.
        
        
        """
        ...
    @typing.overload
    def setDoubles(self, string: str, doubleArray: typing.List[float]) -> None: ...
    @typing.overload
    def setDoubles2D(self, doubleArray: typing.List[float], intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setDoubles2D`
            Sets the value being a 2-dimensional double array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setDoubles2D` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (double[]): the double array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setDoubles2D(self, string: str, doubleArray: typing.List[float], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setEnumItem(self, enumItem: cern.japc.value.EnumItem) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setEnumItem`
            Sets the value being an :class:`~cern.japc.value.EnumItem`.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setEnumItem` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItem`): the EnumItem value.
        
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setEnumItem`
            Sets the value at the given index to the given enumeration item. The value set is the nth one from the array where n is
            given by the index. If the underlying value is not an array the index is ignored and the value is set. If this value is
            not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setEnumItem` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index where to set the value in the array
                value (:class:`~cern.japc.value.EnumItem`): the enumeration item to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setEnumItem(self, int: int, enumItem: cern.japc.value.EnumItem) -> None: ...
    @typing.overload
    def setEnumItem(self, string: str, enumItem: cern.japc.value.EnumItem) -> None: ...
    @typing.overload
    def setEnumItemSet(self, enumItemSet: cern.japc.value.EnumItemSet) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setEnumItemSet`
            Sets the value being an :class:`~cern.japc.value.EnumItemSet`.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setEnumItemSet`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItemSet`): the EnumItemSet value.
        
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setEnumItemSet`
            Sets the value at the given index to the given enumeration items set. The value set is the nth one from the array where
            n is given by the index. If the underlying value is not an array the index is ignored and the value is set. If this
            value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setEnumItemSet`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index where to set the value in the array
                value (:class:`~cern.japc.value.EnumItemSet`): the enumeration items set to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setEnumItemSet(self, int: int, enumItemSet: cern.japc.value.EnumItemSet) -> None: ...
    @typing.overload
    def setEnumItemSet(self, string: str, enumItemSet: cern.japc.value.EnumItemSet) -> None: ...
    @typing.overload
    def setEnumItemSets(self, enumItemSetArray: typing.List[cern.japc.value.EnumItemSet]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setEnumItemSets`
            Sets the value being a EnumItemSet array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setEnumItemSets`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItemSet`[]): the EnumItemSet array value.
        
        
        """
        ...
    @typing.overload
    def setEnumItemSets(self, string: str, enumItemSetArray: typing.List[cern.japc.value.EnumItemSet]) -> None: ...
    @typing.overload
    def setEnumItemSets2D(self, enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setEnumItemSets2D`
            Sets the value being a 2-dimensional enumeration set array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setEnumItemSets2D`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItemSet`[]): the enumeration set array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setEnumItemSets2D(self, string: str, enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setEnumItems(self, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setEnumItems`
            Sets the value being a EnumItem array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setEnumItems` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItem`[]): the EnumItem array value.
        
        
        """
        ...
    @typing.overload
    def setEnumItems(self, string: str, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> None: ...
    @typing.overload
    def setEnumItems2D(self, enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setEnumItems2D`
            Sets the value being a 2-dimensional enumeration array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setEnumItems2D`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (:class:`~cern.japc.value.EnumItem`[]): the enumeration array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setEnumItems2D(self, string: str, enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setFloat(self, float: float) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setFloat`
            Sets the value being a float. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setFloat` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (float): the float value.
        
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setFloat`
            Sets the value at the given index to the given float. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setFloat` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index where to set the value in the array
                value (float): the float value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setFloat(self, int: int, float: float) -> None: ...
    @typing.overload
    def setFloat(self, string: str, float: float) -> None: ...
    @typing.overload
    def setFloat(self, string: str, int: int, float: float) -> None: ...
    @typing.overload
    def setFloats(self, floatArray: typing.List[float]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setFloats`
            Sets the value being a float array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setFloats` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (float[]): the float array value.
        
        
        """
        ...
    @typing.overload
    def setFloats(self, string: str, floatArray: typing.List[float]) -> None: ...
    @typing.overload
    def setFloats2D(self, floatArray: typing.List[float], intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setFloats2D`
            Sets the value being a 2-dimensional float array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setFloats2D` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (float[]): the float array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setFloats2D(self, string: str, floatArray: typing.List[float], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setInt(self, int: int) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setInt`
            Sets the value being a int. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setInt` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (int): the int value.
        
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setInt`
            Sets the value at the given index to the given int. The value set is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored and the value is set. If this value is not mutable
            an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setInt` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index where to set the value in the array
                value (int): the int value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setInt(self, int: int, int2: int) -> None: ...
    @typing.overload
    def setInt(self, string: str, int: int) -> None: ...
    @typing.overload
    def setInt(self, string: str, int: int, int2: int) -> None: ...
    @typing.overload
    def setInts(self, intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setInts`
            Sets the value being a int array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setInts` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (int[]): the int array value.
        
        
        """
        ...
    @typing.overload
    def setInts(self, string: str, intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setInts2D(self, intArray: typing.List[int], intArray2: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setInts2D`
            Sets the value being a 2-dimensional int array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setInts2D` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (int[]): the int array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setInts2D(self, string: str, intArray: typing.List[int], intArray2: typing.List[int]) -> None: ...
    @typing.overload
    def setLong(self, int: int, long: int) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setLong`
            Sets the value at the given index to the given long. The value set is the nth one from the array where n is given by the
            index. If the underlying value is not an array the index is ignored and the value is set. If this value is not mutable
            an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setLong` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index where to set the value in the array
                value (long): the long value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setLong(self, long: int) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setLong`
            Sets the value being a long. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setLong` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (long): the long value.
        
        """
        ...
    @typing.overload
    def setLong(self, string: str, int: int, long: int) -> None: ...
    @typing.overload
    def setLong(self, string: str, long: int) -> None: ...
    @typing.overload
    def setLongs(self, longArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setLongs`
            Sets the value being a long array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setLongs` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (long[]): the long array value.
        
        
        """
        ...
    @typing.overload
    def setLongs(self, string: str, longArray: typing.List[int]) -> None: ...
    @typing.overload
    def setLongs2D(self, longArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setLongs2D`
            Sets the value being a 2-dimensional long array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setLongs2D` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (long[]): the long array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setLongs2D(self, string: str, longArray: typing.List[int], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setObject(self, object: typing.Any) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setObject`
            Sets the value as an object. This method can handle any scalar wrapping Object type as well as arrays and string. If
            other type was passed a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` will be
            thrown. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setObject` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                o (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value as an object.
        
        
        """
        ...
    @typing.overload
    def setObject(self, string: str, object: typing.Any) -> None: ...
    @typing.overload
    def setObjects2D(self, object: typing.Any, intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setObjects2D`
            Sets the value as a 2d array of objects. This method can handle any array of primitives and Strings, which will be used
            as a source for 2D array. If other type was passed a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/IllegalArgumentException.html?is-external=true>` will be
            thrown. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setObjects2D` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                o (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the value as an object.
                dimensions (int[]): the dimensions of the 2D array
        
        
        """
        ...
    @typing.overload
    def setObjects2D(self, string: str, object: typing.Any, intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setShort(self, int: int, short: int) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setShort`
            Sets the value at the given index to the given short. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setShort` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index where to set the value in the array
                value (short): the short value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setShort(self, short: int) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setShort`
            Sets the value being a short. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setShort` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (short): the short value.
        
        """
        ...
    @typing.overload
    def setShort(self, string: str, int: int, short: int) -> None: ...
    @typing.overload
    def setShort(self, string: str, short: int) -> None: ...
    @typing.overload
    def setShorts(self, shortArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setShorts`
            Sets the value being a short array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setShorts` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (short[]): the short array value.
        
        
        """
        ...
    @typing.overload
    def setShorts(self, string: str, shortArray: typing.List[int]) -> None: ...
    @typing.overload
    def setShorts2D(self, shortArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setShorts2D`
            Sets the value being a 2-dimensional short array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setShorts2D` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (short[]): the short array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setShorts2D(self, string: str, shortArray: typing.List[int], intArray: typing.List[int]) -> None: ...
    @typing.overload
    def setString(self, int: int, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setString`
            Sets the value at the given index to the given String. The value set is the nth one from the array where n is given by
            the index. If the underlying value is not an array the index is ignored and the value is set. If this value is not
            mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setString` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                index (int): the index where to set the value in the array
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the String value to set at the given index.
        
        
        """
        ...
    @typing.overload
    def setString(self, string: str) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setString`
            Sets the value being a String. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setString` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the String value.
        
        """
        ...
    @typing.overload
    def setString(self, string: str, int: int, string2: str) -> None: ...
    @typing.overload
    def setString(self, string: str, string2: str) -> None: ...
    @typing.overload
    def setStrings(self, stringArray: typing.List[str]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setStrings`
            Sets the value being a String array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setStrings` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the String array value.
        
        
        """
        ...
    @typing.overload
    def setStrings(self, string: str, stringArray: typing.List[str]) -> None: ...
    @typing.overload
    def setStrings2D(self, stringArray: typing.List[str], intArray: typing.List[int]) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setStrings2D`
            Sets the value being a 2-dimensional String array. If this value is not mutable an exception is thrown.
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setStrings2D` in interface :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`[]): the String array value.
                dimensions (int[]): the dimensions of the array
        
        
        """
        ...
    @typing.overload
    def setStrings2D(self, string: str, stringArray: typing.List[str], intArray: typing.List[int]) -> None: ...
    def setValueStatus(self, simpleValueStatus: cern.japc.value.SimpleValueStatus) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.SimpleParameterValue.setValueStatus`
            Sets the value status.
        
            If the value is immutable a `null
            <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/RuntimeException.html?is-external=true>` will be thrown.
        
        
            Specified by:
                :meth:`~cern.japc.value.SimpleParameterValue.setValueStatus`Â in
                interfaceÂ :class:`~cern.japc.value.SimpleParameterValue`
        
            Parameters:
                svs (:class:`~cern.japc.value.SimpleValueStatus`): new valueStatus
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.value.spi.value")``.

    BooleanItemData: typing.Type[BooleanItemData]
    BooleanTypeRegistry: typing.Type[BooleanTypeRegistry]
    EnumItemData: typing.Type[EnumItemData]
    EnumItemSetImpl: typing.Type[EnumItemSetImpl]
    EnumerationRegistry: typing.Type[EnumerationRegistry]
    InternalDiscreteFunctionFactory: typing.Type[InternalDiscreteFunctionFactory]
    SimpleParameterValueImpl: typing.Type[SimpleParameterValueImpl]
    core: cern.japc.value.spi.value.core.__module_protocol__
    simple: cern.japc.value.spi.value.simple.__module_protocol__
