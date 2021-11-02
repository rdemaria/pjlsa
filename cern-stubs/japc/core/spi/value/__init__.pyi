import cern.japc.core
import cern.japc.value
import cern.japc.value.spi.value.core
import java.io
import java.lang
import java.util
import typing



class AbstractMapParameterValue(cern.japc.value.spi.value.core.ParameterValueImpl, cern.japc.value.MapParameterValue):
    """
    public abstract class AbstractMapParameterValue extends cern.japc.value.spi.value.core.ParameterValueImpl implements cern.japc.value.MapParameterValue
    
        Basic implementation of a :code:`MapParameterValue`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, mapDescriptor: cern.japc.value.MapDescriptor): ...
    @typing.overload
    def __init__(self, stringArray: typing.List[str], simpleParameterValueArray: typing.List[cern.japc.value.SimpleParameterValue]): ...
    @typing.overload
    def __init__(self, map: typing.Union[java.util.Map[str, cern.japc.value.SimpleParameterValue], typing.Mapping[str, cern.japc.value.SimpleParameterValue]]): ...
    def clone(self) -> typing.Any:
        """
        
            Specified by:
                :code:`clone` in interface :code:`cern.japc.value.ParameterValue`
        
            Overrides:
                :code:`clone` in class :code:`cern.japc.value.spi.value.core.ParameterValueImpl`
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def get(self, string: str) -> cern.japc.value.SimpleParameterValue:
        """
        
            Specified by:
                :code:`get` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
        
            Specified by:
                :code:`getNames` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getString(self, string: str) -> str: ...
    @typing.overload
    def getString(self, string: str, int: int) -> str: ...
    @typing.overload
    def getString(self) -> str:
        """
        
            Specified by:
                :code:`getString` in interface :code:`cern.japc.value.ParameterValue`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def makeMutable(self) -> 'AbstractMapParameterValue':
        """
        
            Specified by:
                :code:`makeMutable` in interface :code:`cern.japc.value.MapParameterValue`
        
            Specified by:
                :code:`makeMutable` in interface :code:`cern.japc.value.ParameterValue`
        
            Overrides:
                :code:`makeMutable` in class :code:`cern.japc.value.spi.value.core.ParameterValueImpl`
        
        
        """
        ...
    def put(self, string: str, simpleParameterValue: cern.japc.value.SimpleParameterValue) -> None:
        """
        
            Specified by:
                :code:`put` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def remove(self, string: str) -> cern.japc.value.SimpleParameterValue:
        """
        
            Specified by:
                :code:`remove` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setMutable(self, boolean: bool) -> None:
        """
        
            Overrides:
                :code:`setMutable` in class :code:`cern.japc.value.spi.value.core.ParameterValueImpl`
        
        
        """
        ...
    def size(self) -> int:
        """
        
            Specified by:
                :code:`size` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class MapDescriptorImpl(cern.japc.value.spi.value.core.AbstractValueDescriptor, cern.japc.value.MapDescriptor, java.io.Serializable):
    """
    public class MapDescriptorImpl extends cern.japc.value.spi.value.core.AbstractValueDescriptor implements cern.japc.value.MapDescriptor, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, stringArray: typing.List[str], simpleDescriptorArray: typing.List[cern.japc.value.SimpleDescriptor]): ...
    @typing.overload
    def __init__(self, map: typing.Union[java.util.Map[str, cern.japc.value.SimpleDescriptor], typing.Mapping[str, cern.japc.value.SimpleDescriptor]]): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def get(self, string: str) -> cern.japc.value.SimpleDescriptor:
        """
        
            Specified by:
                :code:`get` in interface :code:`cern.japc.value.MapDescriptor`
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
        
            Specified by:
                :code:`getNames` in interface :code:`cern.japc.value.MapDescriptor`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def put(self, string: str, simpleDescriptor: cern.japc.value.SimpleDescriptor) -> None:
        """
            Adds a value descriptor for a field.
        
            Parameters:
                fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): field name
                descriptor (cern.japc.value.SimpleDescriptor): descriptor
        
        
        """
        ...
    def remove(self, string: str) -> cern.japc.value.SimpleDescriptor:
        """
            Removes a descriptor of a field
        
            Parameters:
                fieldName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): field name
        
            Returns:
                the removed descriptor
        
        
        """
        ...
    def size(self) -> int:
        """
        
            Specified by:
                :code:`size` in interface :code:`cern.japc.value.MapDescriptor`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class ObjectParameterValueImpl(cern.japc.value.spi.value.core.ParameterValueImpl, cern.japc.core.ObjectParameterValue):
    """
    public class ObjectParameterValueImpl extends cern.japc.value.spi.value.core.ParameterValueImpl implements :class:`~cern.japc.core.ObjectParameterValue`
    
        This class implements a ParameterValue holding an arbitrary object.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, object: typing.Any): ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getString(self) -> str:
        """
        
            Specified by:
                :code:`getString` in interface :code:`cern.japc.value.ParameterValue`
        
        
        """
        ...
    def getValue(self) -> typing.Any:
        """
            Description copied from interface: :meth:`~cern.japc.core.ObjectParameterValue.getValue`
            Returns the value hold by this ParameterValue. The value returned can be null.
        
            Specified by:
                :meth:`~cern.japc.core.ObjectParameterValue.getValue` in interface :class:`~cern.japc.core.ObjectParameterValue`
        
            Returns:
                the possibly null value hold by this ParameterValue
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def makeMutable(self) -> 'ObjectParameterValueImpl':
        """
        
            Specified by:
                :meth:`~cern.japc.core.ObjectParameterValue.makeMutable` in interface :class:`~cern.japc.core.ObjectParameterValue`
        
            Specified by:
                :code:`makeMutable` in interface :code:`cern.japc.value.ParameterValue`
        
            Overrides:
                :code:`makeMutable` in class :code:`cern.japc.value.spi.value.core.ParameterValueImpl`
        
        
        """
        ...
    def setValue(self, object: typing.Any) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.ObjectParameterValue.setValue`
            Sets the value of this ParameterValue. The given value can bu null.
        
            Specified by:
                :meth:`~cern.japc.core.ObjectParameterValue.setValue` in interface :class:`~cern.japc.core.ObjectParameterValue`
        
            Parameters:
                value (`Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`): the possibly null value of this parameter value.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class SimpleDescriptorImpl(cern.japc.value.spi.value.core.AbstractValueDescriptor, cern.japc.value.SimpleDescriptor, java.io.Serializable):
    """
    public class SimpleDescriptorImpl extends cern.japc.value.spi.value.core.AbstractValueDescriptor implements cern.japc.value.SimpleDescriptor, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Implements a SimpleDescriptor
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, valueType: cern.japc.value.ValueType): ...
    @typing.overload
    def __init__(self, valueType: cern.japc.value.ValueType, booleanType: cern.japc.value.BooleanType): ...
    @typing.overload
    def __init__(self, valueType: cern.japc.value.ValueType, enumType: cern.japc.value.EnumType): ...
    def addExtraCharacteristic(self, string: str, string2: str) -> None:
        """
            Add an extra characteristic of the parameter associated with this descriptor. If the same name is entered twice the
            value is overwritten.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The name of the extra parameter characteristic
                value (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The value of the extra parameter characteristic
        
        
        """
        ...
    def get(self, string: str) -> cern.japc.value.SimpleDescriptor:
        """
        
            Specified by:
                :code:`get` in interface :code:`cern.japc.value.MapDescriptor`
        
        
        """
        ...
    def getBooleanType(self) -> cern.japc.value.BooleanType:
        """
        
            Specified by:
                :code:`getBooleanType` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
        
            Specified by:
                :code:`getColumnCount` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getDescription(self) -> str:
        """
        
            Specified by:
                :code:`getDescription` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getEnumType(self) -> cern.japc.value.EnumType:
        """
        
            Specified by:
                :code:`getEnumType` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getExtraCharacteristic(self, string: str) -> str:
        """
        
            Specified by:
                :code:`getExtraCharacteristic` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getExtraCharacteristicNames(self) -> typing.List[str]:
        """
        
            Specified by:
                :code:`getExtraCharacteristicNames` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getFormatPattern(self) -> str:
        """
            Default implementation that returns a default format if none is defined. The format pattern is in java format style
        
            Specified by:
                :code:`getFormatPattern` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Also see:
                :code:`SimpleDescriptor.getFormatPattern()`
        
        
        """
        ...
    def getLength(self) -> int:
        """
        
            Specified by:
                :code:`getLength` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getMaxValue(self) -> float:
        """
        
            Specified by:
                :code:`getMaxValue` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
        
            Specified by:
                :code:`getMinValue` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
        
            Specified by:
                :code:`getNames` in interface :code:`cern.japc.value.MapDescriptor`
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
        
            Specified by:
                :code:`getRowCount` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getStandardMeaning(self, object: typing.Any) -> cern.japc.value.SimpleValueStandardMeaning:
        """
        
            Specified by:
                :code:`getStandardMeaning` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getTitle(self) -> str:
        """
        
            Specified by:
                :code:`getTitle` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getUnit(self) -> str:
        """
        
            Specified by:
                :code:`getUnit` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getValueType(self) -> cern.japc.value.ValueType:
        """
        
            Specified by:
                :code:`getValueType` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getXMaxValue(self) -> float:
        """
        
            Specified by:
                :code:`getXMaxValue` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getXMinValue(self) -> float:
        """
        
            Specified by:
                :code:`getXMinValue` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getXUnit(self) -> str:
        """
        
            Specified by:
                :code:`getXUnit` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getYMaxValue(self) -> float:
        """
        
            Specified by:
                :code:`getYMaxValue` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getYMinValue(self) -> float:
        """
        
            Specified by:
                :code:`getYMinValue` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getYUnit(self) -> str:
        """
        
            Specified by:
                :code:`getYUnit` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def isDiscrete(self) -> bool: ...
    def isFilterable(self) -> bool: ...
    def isSettable(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                :code:`isSettable` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def setColumnCount(self, int: int) -> None:
        """
            Sets the columnCount.
        
            Parameters:
                columnCount (int): The columnCount to set.
        
        
        """
        ...
    def setDescription(self, string: str) -> None:
        """
            Sets the description.
        
            Parameters:
                description (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The description to set
        
        
        """
        ...
    def setFilterable(self, boolean: bool) -> None: ...
    def setFormatPattern(self, string: str) -> None:
        """
            Sets the format pattern in java format style.
        
            Parameters:
                formatPattern (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The format to set.
        
        
        """
        ...
    def setLength(self, int: int) -> None:
        """
            Sets the length.
        
            Parameters:
                length (int): The length to set
        
        
        """
        ...
    def setMaxValue(self, double: float) -> None:
        """
        
            Parameters:
                maxValue (double): maximum to set
        
        
        """
        ...
    def setMinValue(self, double: float) -> None:
        """
        
            Parameters:
                minValue (double): minimum to set
        
        
        """
        ...
    def setRowCount(self, int: int) -> None:
        """
            Sets the rowCount.
        
            Parameters:
                rowCount (int): The rowCount to set.
        
        
        """
        ...
    def setTitle(self, string: str) -> None:
        """
            Sets the title.
        
            Parameters:
                title (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The title to set
        
        
        """
        ...
    def setUnit(self, string: str) -> None:
        """
        
            Parameters:
                unit (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): unit to set
        
        
        """
        ...
    def setXMaxValue(self, double: float) -> None:
        """
        
            Parameters:
                xMaxValue (double): maximum of X axis to set (makes sense for function values only)
        
        
        """
        ...
    def setXMinValue(self, double: float) -> None:
        """
        
            Parameters:
                xMinValue (double): minimum of X axis to set (makes sense for function values only)
        
        
        """
        ...
    def setXUnit(self, string: str) -> None:
        """
        
            Parameters:
                xUnit (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): unit of X axis set (makes sense for function values only)
        
        
        """
        ...
    def setYMaxValue(self, double: float) -> None:
        """
        
            Parameters:
                yMaxValue (double): maximum of Y axis to set (makes sense for function values only)
        
        
        """
        ...
    def setYMinValue(self, double: float) -> None:
        """
        
            Parameters:
                yMinValue (double): minimum of Y axis to set (makes sense for function values only)
        
        
        """
        ...
    def setYUnit(self, string: str) -> None:
        """
        
            Parameters:
                yUnit (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): unit of Y axis to set (makes sense for function values only)
        
        
        """
        ...
    def size(self) -> int:
        """
        
            Specified by:
                :code:`size` in interface :code:`cern.japc.value.MapDescriptor`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class SimpleDescriptorSupport(cern.japc.value.spi.value.core.TypedObject, cern.japc.value.SimpleDescriptor, java.io.Serializable):
    """
    public abstract class SimpleDescriptorSupport extends cern.japc.value.spi.value.core.TypedObject implements cern.japc.value.SimpleDescriptor, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Support class for implementing the SimpleDescriptor interface that returns default values.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def get(self, string: str) -> cern.japc.value.SimpleDescriptor:
        """
        
            Specified by:
                :code:`get` in interface :code:`cern.japc.value.MapDescriptor`
        
        
        """
        ...
    def getBooleanType(self) -> cern.japc.value.BooleanType:
        """
        
            Specified by:
                :code:`getBooleanType` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getColumnCount(self) -> int:
        """
        
            Specified by:
                :code:`getColumnCount` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getDescription(self) -> str:
        """
            Default implementation that returns :code:`null`. Override to return proper value.
        
            Specified by:
                :code:`getDescription` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Also see:
                :code:`SimpleDescriptor.getDescription()`
        
        
        """
        ...
    def getEnumType(self) -> cern.japc.value.EnumType:
        """
        
            Specified by:
                :code:`getEnumType` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getExtraCharacteristic(self, string: str) -> str:
        """
            By default no Extra Characteristic are provided by default and this method returns null.
        
            Specified by:
                :code:`getExtraCharacteristic` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Returns:
                null as no Extra Characteristic are provided by default
        
            Also see:
                :meth:`~cern.japc.core.ParameterDescriptor.getExtraCharacteristic`
        
        
        """
        ...
    def getExtraCharacteristicNames(self) -> typing.List[str]:
        """
            By default no Extra Characteristic Names are provided by default and this method returns an empty String array.
        
            Specified by:
                :code:`getExtraCharacteristicNames` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Returns:
                an empty String array as no Extra Characteristic Names are provided by default
        
            Also see:
                :meth:`~cern.japc.core.ParameterDescriptor.getExtraCharacteristicNames`
        
        
        """
        ...
    def getFormatPattern(self) -> str:
        """
            Default implementation that returns :code:`null`. Override to return proper value.
        
            Specified by:
                :code:`getFormatPattern` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Also see:
                :code:`SimpleDescriptor.getFormatPattern()`
        
        
        """
        ...
    def getLength(self) -> int:
        """
        
            Specified by:
                :code:`getLength` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getMaxValue(self) -> float:
        """
            Default implementation that returns Double.NaN. Override to return proper value.
        
            Specified by:
                :code:`getMaxValue` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Also see:
                :code:`SimpleDescriptor.getMaxValue()`
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
            Default implementation that returns Double.NaN. Override to return proper value.
        
            Specified by:
                :code:`getMinValue` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Also see:
                :code:`SimpleDescriptor.getMinValue()`
        
        
        """
        ...
    def getNames(self) -> typing.List[str]:
        """
        
            Specified by:
                :code:`getNames` in interface :code:`cern.japc.value.MapDescriptor`
        
        
        """
        ...
    def getRowCount(self) -> int:
        """
        
            Specified by:
                :code:`getRowCount` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getStandardMeaning(self, object: typing.Any) -> cern.japc.value.SimpleValueStandardMeaning:
        """
        
            Specified by:
                :code:`getStandardMeaning` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def getTitle(self) -> str:
        """
            Default implementation that returns :code:`null`. Override to return proper value.
        
            Specified by:
                :code:`getTitle` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Also see:
                :code:`SimpleDescriptor.getTitle()`
        
        
        """
        ...
    def getUnit(self) -> str:
        """
            Default implementation that returns :code:`null`. Override to return proper value.
        
            Specified by:
                :code:`getUnit` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Also see:
                :code:`SimpleDescriptor.getUnit()`
        
        
        """
        ...
    def isConstant(self) -> bool:
        """
            Default implementation that returns false. Override to return proper value.
        
            Specified by:
                :code:`isConstant` in interface :code:`cern.japc.value.ValueDescriptor`
        
            Also see:
                :code:`ValueDescriptor.isConstant()`
        
        
        """
        ...
    def isDiscrete(self) -> bool: ...
    def isFilterable(self) -> bool: ...
    def isSettable(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                :code:`isSettable` in interface :code:`cern.japc.value.SimpleDescriptor`
        
        
        """
        ...
    def size(self) -> int:
        """
        
            Specified by:
                :code:`size` in interface :code:`cern.japc.value.MapDescriptor`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class SimpleDescriptorToStringHelper:
    """
    public class SimpleDescriptorToStringHelper extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Helper class for SimpleDescriptor.toString() shared by SimpleDescriptor implementations.
    """
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    @staticmethod
    def toString(simpleDescriptor: cern.japc.value.SimpleDescriptor) -> str:
        """
        
            Parameters:
                simpleDescriptor (cern.japc.value.SimpleDescriptor): The SimpleDescriptor to convert to String.
        
            Returns:
                A string representation of the given SimpleDescriptor.
        
        
            Parameters:
                simpleDescriptor (cern.japc.value.SimpleDescriptor): The SimpleDescriptor to convert to String.
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): The SimpleDescriptor (parameter) name
        
            Returns:
                A string representation of the given SimpleDescriptor.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def toString(simpleDescriptor: cern.japc.value.SimpleDescriptor, string: str) -> str: ...

class EnumValueDescriptor(SimpleDescriptorImpl):
    """
    public class EnumValueDescriptor extends :class:`~cern.japc.core.spi.value.SimpleDescriptorImpl`
    
        Value descriptor for :code:`ValueType.ENUM` values.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, valueType: cern.japc.value.ValueType, enumType: cern.japc.value.EnumType, map: typing.Union[java.util.Map[cern.japc.value.EnumItem, cern.japc.value.SimpleValueStandardMeaning], typing.Mapping[cern.japc.value.EnumItem, cern.japc.value.SimpleValueStandardMeaning]], set: java.util.Set[cern.japc.value.EnumItem]): ...
    def getStandardMeaning(self, object: typing.Any) -> cern.japc.value.SimpleValueStandardMeaning:
        """
        
            Specified by:
                :code:`getStandardMeaning` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Overrides:
                :meth:`~cern.japc.core.spi.value.SimpleDescriptorImpl.getStandardMeaning`Â in
                classÂ :class:`~cern.japc.core.spi.value.SimpleDescriptorImpl`
        
        
        """
        ...
    def isDiscrete(self) -> bool:
        """
        
            Specified by:
                :code:`isDiscrete` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Overrides:
                :meth:`~cern.japc.core.spi.value.SimpleDescriptorImpl.isDiscrete`Â in
                classÂ :class:`~cern.japc.core.spi.value.SimpleDescriptorImpl`
        
        
        """
        ...
    def isSettable(self, object: typing.Any) -> bool:
        """
        
            Specified by:
                :code:`isSettable` in interface :code:`cern.japc.value.SimpleDescriptor`
        
            Overrides:
                :meth:`~cern.japc.core.spi.value.SimpleDescriptorImpl.isSettable`Â in
                classÂ :class:`~cern.japc.core.spi.value.SimpleDescriptorImpl`
        
        
        """
        ...

class MapParameterValueImpl(AbstractMapParameterValue, cern.japc.value.MapParameterValue, java.io.Serializable, java.lang.Cloneable):
    """
    public class MapParameterValueImpl extends :class:`~cern.japc.core.spi.value.AbstractMapParameterValue` implements cern.japc.value.MapParameterValue, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`, `Cloneable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Cloneable.html?is-external=true>`
    
        Implementation of :code:`MapParameterValue`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, immutableMapParameterValue: cern.japc.value.ImmutableMapParameterValue): ...
    @typing.overload
    def __init__(self, mapDescriptor: cern.japc.value.MapDescriptor): ...
    @typing.overload
    def __init__(self, stringArray: typing.List[str], simpleParameterValueArray: typing.List[cern.japc.value.SimpleParameterValue]): ...
    @typing.overload
    def __init__(self, map: typing.Union[java.util.Map[str, cern.japc.value.SimpleParameterValue], typing.Mapping[str, cern.japc.value.SimpleParameterValue]]): ...
    def getArray2D(self, string: str) -> cern.japc.value.Array2D:
        """
        
            Specified by:
                :code:`getArray2D` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getBoolean(self, string: str) -> bool:
        """
        
            Specified by:
                :code:`getBoolean` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getBoolean(self, string: str, int: int) -> bool:
        """
        
            Specified by:
                :code:`getBoolean` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getBooleans(self, string: str) -> typing.List[bool]:
        """
        
            Specified by:
                :code:`getBooleans` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getBooleans(self, string: str, int: int, int2: int) -> typing.List[bool]:
        """
        
            Specified by:
                :code:`getBooleans` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getByte(self, string: str) -> int:
        """
        
            Specified by:
                :code:`getByte` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getByte(self, string: str, int: int) -> int:
        """
        
            Specified by:
                :code:`getByte` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getBytes(self, string: str) -> typing.List[int]:
        """
        
            Specified by:
                :code:`getBytes` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getBytes(self, string: str, int: int, int2: int) -> typing.List[int]:
        """
        
            Specified by:
                :code:`getBytes` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getColumnCount(self, string: str) -> int:
        """
        
            Specified by:
                :code:`getColumnCount` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getDiscreteFunction(self, string: str) -> cern.japc.value.DiscreteFunction:
        """
        
            Specified by:
                :code:`getDiscreteFunction` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getDiscreteFunctionList(self, string: str) -> cern.japc.value.DiscreteFunctionList:
        """
        
            Specified by:
                :code:`getDiscreteFunctionList` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getDouble(self, string: str) -> float:
        """
        
            Specified by:
                :code:`getDouble` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getDouble(self, string: str, int: int) -> float:
        """
        
            Specified by:
                :code:`getDouble` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getDoubles(self, string: str) -> typing.List[float]:
        """
        
            Specified by:
                :code:`getDoubles` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getDoubles(self, string: str, int: int, int2: int) -> typing.List[float]:
        """
        
            Specified by:
                :code:`getDoubles` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getEnumItem(self, string: str) -> cern.japc.value.EnumItem:
        """
        
            Specified by:
                :code:`getEnumItem` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getEnumItemSet(self, string: str) -> cern.japc.value.EnumItemSet:
        """
        
            Specified by:
                :code:`getEnumItemSet` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getEnumItemSets(self, string: str) -> typing.List[cern.japc.value.EnumItemSet]:
        """
        
            Specified by:
                :code:`getEnumItemSets` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getEnumItems(self, string: str) -> typing.List[cern.japc.value.EnumItem]:
        """
        
            Specified by:
                :code:`getEnumItems` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getFloat(self, string: str) -> float:
        """
        
            Specified by:
                :code:`getFloat` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getFloat(self, string: str, int: int) -> float:
        """
        
            Specified by:
                :code:`getFloat` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getFloats(self, string: str) -> typing.List[float]:
        """
        
            Specified by:
                :code:`getFloats` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getFloats(self, string: str, int: int, int2: int) -> typing.List[float]:
        """
        
            Specified by:
                :code:`getFloats` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getInt(self, string: str) -> int:
        """
        
            Specified by:
                :code:`getInt` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getInt(self, string: str, int: int) -> int:
        """
        
            Specified by:
                :code:`getInt` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getInts(self, string: str) -> typing.List[int]:
        """
        
            Specified by:
                :code:`getInts` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getInts(self, string: str, int: int, int2: int) -> typing.List[int]:
        """
        
            Specified by:
                :code:`getInts` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getLength(self, string: str) -> int:
        """
        
            Specified by:
                :code:`getLength` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getLong(self, string: str) -> int:
        """
        
            Specified by:
                :code:`getLong` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getLong(self, string: str, int: int) -> int:
        """
        
            Specified by:
                :code:`getLong` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getLongs(self, string: str) -> typing.List[int]:
        """
        
            Specified by:
                :code:`getLongs` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getLongs(self, string: str, int: int, int2: int) -> typing.List[int]:
        """
        
            Specified by:
                :code:`getLongs` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getMaxValue(self, string: str) -> float:
        """
        
            Specified by:
                :code:`getMaxValue` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getMinValue(self, string: str) -> float:
        """
        
            Specified by:
                :code:`getMinValue` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getObject(self, string: str) -> typing.Any:
        """
        
            Specified by:
                :code:`getObject` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getObject(self, string: str, int: int) -> typing.Any:
        """
        
            Specified by:
                :code:`getObject` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getRowCount(self, string: str) -> int:
        """
        
            Specified by:
                :code:`getRowCount` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getScale(self, string: str) -> int: ...
    @typing.overload
    def getShort(self, string: str) -> int:
        """
        
            Specified by:
                :code:`getShort` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getShort(self, string: str, int: int) -> int:
        """
        
            Specified by:
                :code:`getShort` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getShorts(self, string: str) -> typing.List[int]:
        """
        
            Specified by:
                :code:`getShorts` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getShorts(self, string: str, int: int, int2: int) -> typing.List[int]:
        """
        
            Specified by:
                :code:`getShorts` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getString(self) -> str: ...
    @typing.overload
    def getString(self, string: str) -> str:
        """
        
            Specified by:
                :code:`getString` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getString(self, string: str, int: int) -> str:
        """
        
            Specified by:
                :code:`getString` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def getStrings(self, string: str) -> typing.List[str]:
        """
        
            Specified by:
                :code:`getStrings` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        """
        ...
    @typing.overload
    def getStrings(self, string: str, int: int, int2: int) -> typing.List[str]:
        """
        
            Specified by:
                :code:`getStrings` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getUnit(self, string: str) -> str:
        """
        
            Specified by:
                :code:`getUnit` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getValueType(self, string: str) -> cern.japc.value.ValueType:
        """
        
            Specified by:
                :code:`getValueType` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getXMaxValue(self, string: str) -> float:
        """
        
            Specified by:
                :code:`getXMaxValue` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getXMinValue(self, string: str) -> float:
        """
        
            Specified by:
                :code:`getXMinValue` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getXUnit(self, string: str) -> str:
        """
        
            Specified by:
                :code:`getXUnit` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getYMaxValue(self, string: str) -> float:
        """
        
            Specified by:
                :code:`getYMaxValue` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getYMinValue(self, string: str) -> float:
        """
        
            Specified by:
                :code:`getYMinValue` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    def getYUnit(self, string: str) -> str:
        """
        
            Specified by:
                :code:`getYUnit` in interface :code:`cern.japc.value.ImmutableMapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setBoolean(self, string: str, boolean: bool) -> None:
        """
        
            Specified by:
                :code:`setBoolean` in interface :code:`cern.japc.value.MapParameterValue`
        
        
            Specified by:
                :code:`setBoolean` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setBoolean(self, string: str, int: int, boolean: bool) -> None: ...
    def setBooleans(self, string: str, booleanArray: typing.List[bool]) -> None:
        """
        
            Specified by:
                :code:`setBooleans` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setBooleans2D(self, string: str, booleanArray: typing.List[bool], intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setBooleans2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setByte(self, string: str, byte: int) -> None:
        """
        
            Specified by:
                :code:`setByte` in interface :code:`cern.japc.value.MapParameterValue`
        
        
            Specified by:
                :code:`setByte` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setByte(self, string: str, int: int, byte: int) -> None: ...
    def setBytes(self, string: str, byteArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setBytes` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setBytes2D(self, string: str, byteArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setBytes2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setDiscreteFunction(self, string: str, discreteFunction: cern.japc.value.DiscreteFunction) -> None:
        """
        
            Specified by:
                :code:`setDiscreteFunction` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setDiscreteFunctionList(self, string: str, discreteFunctionList: cern.japc.value.DiscreteFunctionList) -> None:
        """
        
            Specified by:
                :code:`setDiscreteFunctionList` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setDouble(self, string: str, double: float) -> None:
        """
        
            Specified by:
                :code:`setDouble` in interface :code:`cern.japc.value.MapParameterValue`
        
        
            Specified by:
                :code:`setDouble` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setDouble(self, string: str, int: int, double: float) -> None: ...
    def setDoubles(self, string: str, doubleArray: typing.List[float]) -> None:
        """
        
            Specified by:
                :code:`setDoubles` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setDoubles2D(self, string: str, doubleArray: typing.List[float], intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setDoubles2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setEnumItem(self, string: str, enumItem: cern.japc.value.EnumItem) -> None:
        """
        
            Specified by:
                :code:`setEnumItem` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setEnumItemSet(self, string: str, enumItemSet: cern.japc.value.EnumItemSet) -> None:
        """
        
            Specified by:
                :code:`setEnumItemSet` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setEnumItemSets(self, string: str, enumItemSetArray: typing.List[cern.japc.value.EnumItemSet]) -> None:
        """
        
            Specified by:
                :code:`setEnumItemSets` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setEnumItemSets2D(self, string: str, enumItemSetArray: typing.List[cern.japc.value.EnumItemSet], intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setEnumItemSets2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setEnumItems(self, string: str, enumItemArray: typing.List[cern.japc.value.EnumItem]) -> None:
        """
        
            Specified by:
                :code:`setEnumItems` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setEnumItems2D(self, string: str, enumItemArray: typing.List[cern.japc.value.EnumItem], intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setEnumItems2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setFloat(self, string: str, float: float) -> None:
        """
        
            Specified by:
                :code:`setFloat` in interface :code:`cern.japc.value.MapParameterValue`
        
        
            Specified by:
                :code:`setFloat` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setFloat(self, string: str, int: int, float: float) -> None: ...
    def setFloats(self, string: str, floatArray: typing.List[float]) -> None:
        """
        
            Specified by:
                :code:`setFloats` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setFloats2D(self, string: str, floatArray: typing.List[float], intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setFloats2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setInt(self, string: str, int: int) -> None:
        """
        
            Specified by:
                :code:`setInt` in interface :code:`cern.japc.value.MapParameterValue`
        
        
            Specified by:
                :code:`setInt` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setInt(self, string: str, int: int, int2: int) -> None: ...
    def setInts(self, string: str, intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setInts` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setInts2D(self, string: str, intArray: typing.List[int], intArray2: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setInts2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setLong(self, string: str, int: int, long: int) -> None:
        """
        
            Specified by:
                :code:`setLong` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setLong(self, string: str, long: int) -> None:
        """
        
            Specified by:
                :code:`setLong` in interface :code:`cern.japc.value.MapParameterValue`
        
        """
        ...
    def setLongs(self, string: str, longArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setLongs` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setLongs2D(self, string: str, longArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setLongs2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setObject(self, string: str, object: typing.Any) -> None:
        """
        
            Specified by:
                :code:`setObject` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setObjects2D(self, string: str, object: typing.Any, intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setObjects2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setShort(self, string: str, int: int, short: int) -> None:
        """
        
            Specified by:
                :code:`setShort` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setShort(self, string: str, short: int) -> None:
        """
        
            Specified by:
                :code:`setShort` in interface :code:`cern.japc.value.MapParameterValue`
        
        """
        ...
    def setShorts(self, string: str, shortArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setShorts` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setShorts2D(self, string: str, shortArray: typing.List[int], intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setShorts2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setString(self, string: str, int: int, string2: str) -> None:
        """
        
            Specified by:
                :code:`setString` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    @typing.overload
    def setString(self, string: str, string2: str) -> None:
        """
        
            Specified by:
                :code:`setString` in interface :code:`cern.japc.value.MapParameterValue`
        
        """
        ...
    def setStrings(self, string: str, stringArray: typing.List[str]) -> None:
        """
        
            Specified by:
                :code:`setStrings` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...
    def setStrings2D(self, string: str, stringArray: typing.List[str], intArray: typing.List[int]) -> None:
        """
        
            Specified by:
                :code:`setStrings2D` in interface :code:`cern.japc.value.MapParameterValue`
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.value")``.

    AbstractMapParameterValue: typing.Type[AbstractMapParameterValue]
    EnumValueDescriptor: typing.Type[EnumValueDescriptor]
    MapDescriptorImpl: typing.Type[MapDescriptorImpl]
    MapParameterValueImpl: typing.Type[MapParameterValueImpl]
    ObjectParameterValueImpl: typing.Type[ObjectParameterValueImpl]
    SimpleDescriptorImpl: typing.Type[SimpleDescriptorImpl]
    SimpleDescriptorSupport: typing.Type[SimpleDescriptorSupport]
    SimpleDescriptorToStringHelper: typing.Type[SimpleDescriptorToStringHelper]
