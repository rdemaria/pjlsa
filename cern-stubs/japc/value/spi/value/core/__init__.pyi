import cern.japc.value
import java.io
import typing



class TypedObject(java.io.Serializable):
    """
    public class TypedObject extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Implements support for a Typed object that holds a reference on its type.
    
        Also see:
            :meth:`~serialized`
    """
    def getType(self) -> cern.japc.value.Type:
        """
            Returns the type of this object amongst the ones defined in the :code:`Type` class.
        
            Returns:
                the type of this object amongst the ones defined in the :code:`Type` class.
        
        
        """
        ...

class AbstractValueDescriptor(TypedObject, cern.japc.value.ValueDescriptor, java.io.Serializable):
    """
    public class AbstractValueDescriptor extends :class:`~cern.japc.value.spi.value.core.TypedObject` implements :class:`~cern.japc.value.ValueDescriptor`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Basic class for all the value descriptors.
    
        Also see:
            :meth:`~serialized`
    """
    def getName(self) -> str:
        """
            Getter for the parameter name.
        
            Returns:
                the name
        
        
        """
        ...
    def isConstant(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.value.ValueDescriptor.isConstant`
            Returns true if the value described by this descriptor is constant and never change during the life of this parameter.
            The default value is false.
        
            Specified by:
                :meth:`~cern.japc.value.ValueDescriptor.isConstant` in interface :class:`~cern.japc.value.ValueDescriptor`
        
            Returns:
                true if the value described by this descriptor is constant.
        
        
        """
        ...
    def setConstant(self, boolean: bool) -> None:
        """
            Sets the isConstant.
        
            Parameters:
                isConstant (boolean): The isConstant to set
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Setter for the parameter name.
        
            Parameters:
                name (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name to set
        
        
        """
        ...

class ParameterValueImpl(TypedObject, cern.japc.value.ParameterValue, java.io.Serializable):
    """
    public abstract class ParameterValueImpl extends :class:`~cern.japc.value.spi.value.core.TypedObject` implements :class:`~cern.japc.value.ParameterValue`, `Serializable <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/io/Serializable.html?is-external=true>`
    
        Implementation of ParameterValue. When the parameter value is created it is always mutable until it is made explicitly
        immutable.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, type: cern.japc.value.Type): ...
    @typing.overload
    def __init__(self, type: cern.japc.value.Type, valueDescriptor: cern.japc.value.ValueDescriptor): ...
    def clone(self) -> typing.Any:
        """
            Description copied from interface: :meth:`~cern.japc.value.ParameterValue.clone`
            Returns a deep copy of this ParameterValue. The copy is guarantee to be deep.
        
            Specified by:
                :meth:`~cern.japc.value.ParameterValue.clone` in interface :class:`~cern.japc.value.ParameterValue`
        
            Overrides:
                 in class 
        
            Returns:
                a deep copy of this ParameterValue.
        
            Also see:
                `null <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true#clone()>`
        
        
        """
        ...
    def getDescriptor(self) -> cern.japc.value.ValueDescriptor:
        """
            Returns the value descriptor for this ParameterValue if it has been set. Else null is returned.
        
            Returns:
                the value descriptor for this ParameterValue or null.
        
        
        """
        ...
    def isMutable(self) -> bool:
        """
            Description copied from interface: :meth:`~cern.japc.value.ParameterValue.isMutable`
            Returns true is this ParameterValue is mutable. If the ParameterValue is not mutable, a mutable version can be by
            calling the method :code:`makeMutable:code:`. Any attempt to change this ParameterValue if is is mutable will result in
            an exception being thrown by the method attempting the modification (such as a setter).``
        
            Specified by:
              :meth:`~cern.japc.value.ParameterValue.isMutable` in interface :class:`~cern.japc.value.ParameterValue`
        
            Returns:
              whether this parameter value is mutable or not
        
        
        """
        ...
    def makeImmutable(self) -> None:
        """
            Description copied from interface: :meth:`~cern.japc.value.ParameterValue.makeImmutable`
            Makes this ParameterValue immutable. The original values are untouched by this operation. If this ParameterValue is
            already immutable this method has no effect. Once a parameter value has been made immutable it cannot be made mutable
            anymore unless a copy is created using the method :code:`makeMutable`. Any call to a method attempting to modify an
            immutable parameter will result into an exception.
        
            Specified by:
                :meth:`~cern.japc.value.ParameterValue.makeImmutable` in interface :class:`~cern.japc.value.ParameterValue`
        
        
        """
        ...
    def makeMutable(self) -> cern.japc.value.ParameterValue:
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
    def setDescriptor(self, valueDescriptor: cern.japc.value.ValueDescriptor) -> None:
        """
            Sets the value descriptor for this parameter value.
        
            Parameters:
                valueDescriptor (:class:`~cern.japc.value.ValueDescriptor`): the value descriptor for this value
        
        
        """
        ...
    def setMutable(self, boolean: bool) -> None:
        """
            Sets this value to be mutable or not. This only set the boolean and does not touch this value in any other way.
        
            Parameters:
                mutable (boolean): whether the value is mutable or not.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.value.spi.value.core")``.

    AbstractValueDescriptor: typing.Type[AbstractValueDescriptor]
    ParameterValueImpl: typing.Type[ParameterValueImpl]
    TypedObject: typing.Type[TypedObject]
