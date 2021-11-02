import cern.japc.value
import java.io
import typing



class ValueBean:
    """
    public interface ValueBean
    
        A interface defining a bean used to read and edit values. Concrete implementations of the bean should provide specific
        type safe method to get and set the value associated to this bean. The bean can be mutable, which means that the setters
        can be used, or non mutable, which means that only the getter are available. It is possible to make the bean mutable be
        calling the :meth:`~cern.japc.core.spi.beans.ValueBean.makeMutable` method. Making the bean mutable when the bean is
        immutable will make sure that the original immutable value the bean is based on will remain untouched. Making the bean
        mutable when it is already mutable will make no change.
    """
    NON_MUTABLE_MESSAGE: typing.ClassVar[str] = ...
    """
    static final `String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>` NON_MUTABLE_MESSAGE
    
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getParameterValue(self) -> cern.japc.value.ParameterValue:
        """
            Returns the parameter value this bean is based on.
        
            Returns:
                the parameter value this bean is based on.
        
        
        """
        ...
    def isMutable(self) -> bool:
        """
            Returns true if this bean is mutable. If the bean is not mutable it can be made mutable be calling the method
            :meth:`~cern.japc.core.spi.beans.ValueBean.makeMutable`.
        
            Returns:
                true if this bean is mutable
        
        
        """
        ...
    def makeMutable(self) -> None:
        """
            Makes this bean a mutable object that can be set using the setters. The original value is untouched by this operation, a
            copy is obtained to be modified. If the bean is already mutable this method has no effect. Care must be taken about
            references on the parameter value obtained using the getParameterValue() method. After the call to this method those
            references will be stalled. A new parameter value will be created by the makeMutable if the bean is not already mutable.
        
        """
        ...

class ValueBeanImpl(ValueBean, java.io.Serializable):
    """
    public class ValueBeanImpl extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.beans.ValueBean`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        An implementation of the :class:`~cern.japc.core.spi.beans.ValueBean` interface that holds the value and provides
        support for the mutable / immutable nature of the :class:`~cern.japc.core.spi.beans.ValueBean`. Beans tailored for a
        specific type of value should subclass this class and provide additional methods tailored for the specific type of value
        they are for.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, parameterValue: cern.japc.value.ParameterValue): ...
    def getParameterValue(self) -> cern.japc.value.ParameterValue:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.beans.ValueBean.getParameterValue`
            Returns the parameter value this bean is based on.
        
            Specified by:
                :meth:`~cern.japc.core.spi.beans.ValueBean.getParameterValue` in interface :class:`~cern.japc.core.spi.beans.ValueBean`
        
            Returns:
                the parameter value this bean is based on.
        
        
        """
        ...
    def isMutable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.beans.ValueBean.isMutable`
            Returns true if this bean is mutable. If the bean is not mutable it can be made mutable be calling the method
            :meth:`~cern.japc.core.spi.beans.ValueBean.makeMutable`.
        
            Specified by:
                :meth:`~cern.japc.core.spi.beans.ValueBean.isMutable` in interface :class:`~cern.japc.core.spi.beans.ValueBean`
        
            Returns:
                true if this bean is mutable
        
        
        """
        ...
    def makeMutable(self) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.beans.ValueBean.makeMutable`
            Makes this bean a mutable object that can be set using the setters. The original value is untouched by this operation, a
            copy is obtained to be modified. If the bean is already mutable this method has no effect. Care must be taken about
            references on the parameter value obtained using the getParameterValue() method. After the call to this method those
            references will be stalled. A new parameter value will be created by the makeMutable if the bean is not already mutable.
        
            Specified by:
                :meth:`~cern.japc.core.spi.beans.ValueBean.makeMutable` in interface :class:`~cern.japc.core.spi.beans.ValueBean`
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class MapValueBean(ValueBeanImpl):
    """
    public class MapValueBean extends :class:`~cern.japc.core.spi.beans.ValueBeanImpl`
    
        This class gives the basic functionalities of a java bean backed by a MapValue.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, mapDescriptor: cern.japc.value.MapDescriptor): ...
    @typing.overload
    def __init__(self, mapParameterValue: cern.japc.value.MapParameterValue): ...
    @typing.overload
    def __init__(self, mapParameterValue: cern.japc.value.MapParameterValue, mapDescriptor: cern.japc.value.MapDescriptor): ...
    def setParameterValue(self, mapParameterValue: cern.japc.value.MapParameterValue) -> None:
        """
            Sets a new value for this bean. If the bean was mutable before the call, it remains mutable after. If the bean was not
            mutable before the call, it inherits from the mutable state of the new given value.
        
            Parameters:
                value (cern.japc.value.MapParameterValue): the new value for this bean
        
        
        """
        ...

class SimpleValueBean(ValueBeanImpl):
    """
    public class SimpleValueBean extends :class:`~cern.japc.core.spi.beans.ValueBeanImpl`
    
        This class gives the basic functionalities of a java bean backed by a SimpleValue.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, simpleDescriptor: cern.japc.value.SimpleDescriptor): ...
    @typing.overload
    def __init__(self, simpleParameterValue: cern.japc.value.SimpleParameterValue): ...
    @typing.overload
    def __init__(self, simpleParameterValue: cern.japc.value.SimpleParameterValue, simpleDescriptor: cern.japc.value.SimpleDescriptor): ...
    def setParameterValue(self, simpleParameterValue: cern.japc.value.SimpleParameterValue) -> None:
        """
            Sets a new value for this bean. If the bean was mutable before the call, it remains mutable after. If the bean was not
            mutable before the call, it inherits from the mutable state of the new given value.
        
            Parameters:
                value (cern.japc.value.SimpleParameterValue): the new reader for this bean
        
        
        """
        ...
    @staticmethod
    def validateReader(simpleParameterValue: cern.japc.value.SimpleParameterValue, simpleDescriptor: cern.japc.value.SimpleDescriptor) -> None:
        """
            Validate the reader against the given descriptor. If the validation fails a ParameterRuntimeException is thrown.
        
            Parameters:
                value (cern.japc.value.SimpleParameterValue): the reader to validate
                descriptor (cern.japc.value.SimpleDescriptor): the descriptor to use for the validation
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.beans")``.

    MapValueBean: typing.Type[MapValueBean]
    SimpleValueBean: typing.Type[SimpleValueBean]
    ValueBean: typing.Type[ValueBean]
    ValueBeanImpl: typing.Type[ValueBeanImpl]
