import cern.japc.core
import cern.japc.core.spi.provider
import cern.japc.core.spi.transaction
import cern.japc.core.transaction
import cern.japc.value
import typing



class AcquiredParameterValueAdapter:
    """
    public interface AcquiredParameterValueAdapter
    
        This interface defines method to adapt a :class:`~cern.japc.core.AcquiredParameterValue` received from an adapted
        parameter. It only takes care of the adaptation for receiving value.
    
        This is useful in the case a Parameter A (the parameter adapter) is defined as an adapter of a Parameter B (the adapted
        parameter). A delegates everything to B while adapting the values received. Any value received from B has to be adapted
        before being given to A (method adaptValueReceived).
    """
    def adaptValueReceived(self, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> cern.japc.core.AcquiredParameterValue: ...

class ConstantParameter(cern.japc.core.spi.transaction.AbstractTransactionalParameter):
    """
    public class ConstantParameter extends :class:`~cern.japc.core.spi.transaction.AbstractTransactionalParameter`
    
        A Parameter that has always the same value given at construction time. If the descriptor support the write, the set will
        be supported by modifying the constant value. This parameter does not connect to any underlying hardware.
    """
    def __init__(self, string: str, parameterValue: cern.japc.value.ParameterValue): ...
    @typing.overload
    def setParameterDescriptor(self, parameterDescriptor: cern.japc.core.ParameterDescriptor, descriptorProvider: cern.japc.core.spi.provider.DescriptorProvider) -> None: ...
    @typing.overload
    def setParameterDescriptor(self, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> None:
        """
            Description copied from class: :meth:`~cern.japc.core.spi.AbstractImmutableParameter.setParameterDescriptor`
            Sets the descriptor of this parameter. This method must be called by the creator of this parameter in order to set a
            proper descriptor that enables get, set, monitor based on what is possible on the specific parameter.
        
            Such a descriptor becomes fixed, so it is not possible to refresh it later.
        
            Overrides:
                :meth:`~cern.japc.core.spi.AbstractImmutableParameter.setParameterDescriptor`Â in
                classÂ :class:`~cern.japc.core.spi.AbstractImmutableParameter`
        
            Parameters:
                parameterDescriptor (:class:`~cern.japc.core.ParameterDescriptor`): the parameter descriptor (can't be :code:`null`)
        
        
        """
        ...
    @typing.overload
    def setValueDescriptor(self, valueDescriptor: cern.japc.value.ValueDescriptor, descriptorProvider: cern.japc.core.spi.provider.DescriptorProvider) -> None: ...
    @typing.overload
    def setValueDescriptor(self, valueDescriptor: cern.japc.value.ValueDescriptor) -> None:
        """
            Description copied from class: :meth:`~cern.japc.core.spi.AbstractImmutableParameter.setValueDescriptor`
            Sets the value descriptor of this parameter. This method must be called by the creator of this parameter in order to set
            a proper value descriptor that describes the value the parameter can take. By default, at the creation of the parameter,
            the value descriptor is :code:`null`.
        
            Such a descriptor becomes fixed, so it is not possible to refresh it later.
        
            Overrides:
                :meth:`~cern.japc.core.spi.AbstractImmutableParameter.setValueDescriptor`Â in
                classÂ :class:`~cern.japc.core.spi.AbstractImmutableParameter`
        
            Parameters:
                valueDescriptor (cern.japc.value.ValueDescriptor): the value descriptor (can be :code:`null`)
        
        
        """
        ...

class ParameterValueSentAdapter:
    """
    public interface ParameterValueSentAdapter
    
        This interface defines methods to adapt ParameterValue sent to an adapted parameter. It only takes care of the
        adaptation for sending value.
    
        This is useful in the case a Parameter A (the parameter adapter) is defined as an adapter of a Parameter B (the adapted
        parameter). A delegates everything to B while adapting the values sent or received. Any value set on A has to be adapted
        before to be given to B (method adaptValueSent).
    """
    def adaptValueSent(self, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.value.ParameterValue:
        """
            Adapts the :code:`ParameterValue` sent to the adapter parameter to make the :code:`ParameterValue` sent to the adapted
            parameter.
        
            Parameters:
                valueSent (cern.japc.value.ParameterValue): the :code:`ParameterValue` sent to the adapter parameter
        
            Returns:
                the :code:`ParameterValue` sent to the adapted parameter
        
        
        """
        ...

class ViewParameter(cern.japc.core.spi.transaction.TransactionalParameterDecorator):
    def __init__(self, string: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, acquiredParameterValueAdapter: AcquiredParameterValueAdapter): ...
    def createSubscription(self, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> cern.japc.core.SubscriptionHandle: ...
    def getAdaptedParameter(self) -> cern.japc.core.transaction.TransactionalParameter: ...
    def getDeviceName(self) -> str: ...
    def getName(self) -> str: ...
    def getParameterDescriptor(self) -> cern.japc.core.ParameterDescriptor: ...
    def getPropertyName(self) -> str: ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector) -> cern.japc.core.AcquiredParameterValue: ...
    @typing.overload
    def getValue(self, selector: cern.japc.core.Selector, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def getValueDescriptor(self) -> cern.japc.value.ValueDescriptor: ...
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, compositeTransaction: cern.japc.core.transaction.CompositeTransaction) -> None: ...
    def setParameterDescriptor(self, parameterDescriptor: cern.japc.core.ParameterDescriptor) -> None: ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue) -> None: ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...
    def setValueDescriptor(self, valueDescriptor: cern.japc.value.ValueDescriptor) -> None: ...
    def toString(self) -> str: ...

class VirtualParameterUtil:
    """
    public class VirtualParameterUtil extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>`
    
        Utility methods for creating Virtual parameters, e.g. View and AdapterParameters
    """
    def __init__(self): ...
    @staticmethod
    def createAdapterParameter(string: str, string2: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, class_: typing.Type, transactionalParameter2: cern.japc.core.transaction.TransactionalParameter, class2: typing.Type) -> 'AdapterParameter':
        """
            Creates an Adapter parameter. The parameter name will be composed of the groupName and the propertyName
        
            Parameters:
                groupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enclosing parameter group, must be non-null
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the property name of this ViewParameter, must be non-null
                receivePar (:class:`~cern.japc.core.transaction.TransactionalParameter`): the parameter used to read (receive) values, must be non-null
                receiveAdapter (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the adapter that transforms values in read (get) direction if null, an
                    :class:`~cern.japc.core.spi.adaptation.IdentityValueAdapter`will be used
                sendPar (:class:`~cern.japc.core.transaction.TransactionalParameter`): the parameter used to set (send) values, must be non-null
                sendAdapter (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the adapter that transforms values in send (set) direction if null, an
                    :class:`~cern.japc.core.spi.adaptation.IdentityValueAdapter`will be used
        
            Returns:
                the new AdapterParameter based on the given information
        
            Also see:
                :meth:`~cern.japc.core.spi.adaptation.AdapterParameter.%3Cinit%3E`
        
        
        """
        ...
    @staticmethod
    def createAdapterParameterWithAdapterInstances(string: str, string2: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, acquiredParameterValueAdapter: AcquiredParameterValueAdapter, transactionalParameter2: cern.japc.core.transaction.TransactionalParameter, parameterValueSentAdapter: ParameterValueSentAdapter) -> 'AdapterParameter':
        """
            Creates an Adapter parameter. The parameter name will be composed of the groupName and the propertyName
        
            Parameters:
                groupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enclosing parameter group, must be non-null
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the property name of this ViewParameter, must be non-null
                receivePar (:class:`~cern.japc.core.transaction.TransactionalParameter`): the parameter used to read (receive) values, must be non-null
                receiveAdapter (:class:`~cern.japc.core.spi.adaptation.AcquiredParameterValueAdapter`): the adapter that transforms values in read (get) direction if null, an
                    :class:`~cern.japc.core.spi.adaptation.IdentityValueAdapter`will be used
                sendPar (:class:`~cern.japc.core.transaction.TransactionalParameter`): the parameter used to set (send) values, must be non-null
                sendAdapter (:class:`~cern.japc.core.spi.adaptation.ParameterValueSentAdapter`): the adapter that transforms values in send (set) direction if null, an
                    :class:`~cern.japc.core.spi.adaptation.IdentityValueAdapter`will be used
        
            Returns:
                the new AdapterParameter based on the given information
        
            Also see:
                :meth:`~cern.japc.core.spi.adaptation.AdapterParameter.%3Cinit%3E`
        
        
        """
        ...
    @staticmethod
    def createInstance(class_: typing.Type, string: str) -> typing.Any:
        """
            helper method, creates an instance of an adapter class for a given view parameter name
        
            Parameters:
                adapterClass (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): the class to be instantiated
                viewParName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the parameter name (to be passed in the constructor)
        
            Returns:
                the new parameter
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createViewParameter(string: str, string2: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter) -> ViewParameter:
        """
            create a ViewParameter that does not change the property value, just its name This uses a
            :class:`~cern.japc.core.spi.adaptation.IdentityValueAdapter`
        
            Parameters:
                groupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enclosing parameter group
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the property name of this ViewParameter
                par (:class:`~cern.japc.core.transaction.TransactionalParameter`): parameter to build the view on
        
            Returns:
                the new ViewParameter based on the given information
        
            Creates a View parameter with a ParameterName composed of groupName and propertyName, and with the given readAdapter
        
            Parameters:
                groupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enclosing parameter group, must be non-null
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the property name of this ViewParameter, must be non-null
                par (:class:`~cern.japc.core.transaction.TransactionalParameter`): parameter to build the view on, must be non-null
                readAdapter (`Class <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Class.html?is-external=true>`): 
            Returns:
                the new ViewParameter based on the given information
        
            Creates a View parameter with a ParameterName composed of groupName and propertyName. ViewParameters created by this
            method are needed to change the name of the parameter.
        
            Parameters:
                groupName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the name of the enclosing parameter group, must be non-null
                propertyName (`String <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/String.html?is-external=true>`): the property name of this ViewParameter, must be non-null
                par (:class:`~cern.japc.core.transaction.TransactionalParameter`): parameter to build the view on, must be non-null
                adapter (:class:`~cern.japc.core.spi.adaptation.AcquiredParameterValueAdapter`): the adapter to be used, must be non-null
        
            Returns:
                the new ViewParameter based on the given information
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createViewParameter(string: str, string2: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, acquiredParameterValueAdapter: AcquiredParameterValueAdapter) -> ViewParameter: ...
    @typing.overload
    @staticmethod
    def createViewParameter(string: str, string2: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, class_: typing.Type) -> ViewParameter: ...

class AbstractAcquiredParameterValueAdapter(AcquiredParameterValueAdapter):
    """
    public abstract class AbstractAcquiredParameterValueAdapter extends `Object <http://bewww.cern.ch/ap/dist/java/jdk/1.8/docs/api/java/lang/Object.html?is-external=true>` implements :class:`~cern.japc.core.spi.adaptation.AcquiredParameterValueAdapter`
    
        Helper class for the implementation of a :class:`~cern.japc.core.spi.adaptation.AcquiredParameterValueAdapter`. This
        adapter allows to adapt a given parameter called the adapted parameter.
    
        If we take two parameters A and B. We make A an adapter of B. A is the adapter parameter, B is the adapted parameter.
        For this adapter, the name of A will be passed to the constructor.
    
        The method :meth:`~cern.japc.core.spi.adaptation.AbstractAcquiredParameterValueAdapter.adaptValueReceived` will take the
        value received from B and adapt it to be returned as a value received from A.
    """
    def __init__(self, string: str): ...
    def adaptValueReceived(self, acquiredParameterValue: cern.japc.core.AcquiredParameterValue) -> cern.japc.core.AcquiredParameterValue: ...

class AdapterParameter(ViewParameter):
    def __init__(self, string: str, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, acquiredParameterValueAdapter: AcquiredParameterValueAdapter, transactionalParameter2: cern.japc.core.transaction.TransactionalParameter, parameterValueSentAdapter: ParameterValueSentAdapter): ...
    def prepareValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, compositeTransaction: cern.japc.core.transaction.CompositeTransaction) -> None: ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue) -> None: ...
    @typing.overload
    def setValue(self, selector: cern.japc.core.Selector, parameterValue: cern.japc.value.ParameterValue, parameterValueListener: cern.japc.core.ParameterValueListener) -> None: ...

class FieldFilteringParameterAdapter(AdapterParameter):
    """
    public class FieldFilteringParameterAdapter extends :class:`~cern.japc.core.spi.adaptation.AdapterParameter`
    
        A Decorator that allows Parameters to be created for parameter names including a field, e.g.
        "MyDevice/myProperty#myField".
    
        The ParameterFactory intercepts the creation of such a parameter with fieldName and creates a parameter without
        fieldName instead. The wrapped parameter works with MapParameterValues, whereas the created FieldParameter uses
        SimpleParameterValues. This Adapter translates between the two.
    """
    def __init__(self, transactionalParameter: cern.japc.core.transaction.TransactionalParameter, string: str, string2: str): ...
    def getParameterDescriptor(self) -> cern.japc.core.ParameterDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getParameterDescriptor`
            Returns a descriptor of this parameter. The descriptor provides information that describes the parameter.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getParameterDescriptor`Â in
                interfaceÂ :class:`~cern.japc.core.ImmutableParameter`
        
            Overrides:
                :meth:`~cern.japc.core.spi.adaptation.ViewParameter.getParameterDescriptor`Â in
                classÂ :class:`~cern.japc.core.spi.adaptation.ViewParameter`
        
            Returns:
                a descriptor of this parameter
        
        
        """
        ...
    def getValueDescriptor(self) -> cern.japc.value.ValueDescriptor:
        """
            Description copied from interface: :meth:`~cern.japc.core.ImmutableParameter.getValueDescriptor`
            Returns a descriptor of the value returned by this parameter. The descriptor provides meta information that describes
            the value.
        
            Specified by:
                :meth:`~cern.japc.core.ImmutableParameter.getValueDescriptor` in interface :class:`~cern.japc.core.ImmutableParameter`
        
            Overrides:
                :meth:`~cern.japc.core.spi.adaptation.ViewParameter.getValueDescriptor`Â in
                classÂ :class:`~cern.japc.core.spi.adaptation.ViewParameter`
        
            Returns:
                a descriptor of this value.
        
        
        """
        ...

class IdentityValueAdapter(AbstractAcquiredParameterValueAdapter, ParameterValueSentAdapter):
    """
    public class IdentityValueAdapter extends :class:`~cern.japc.core.spi.adaptation.AbstractAcquiredParameterValueAdapter` implements :class:`~cern.japc.core.spi.adaptation.ParameterValueSentAdapter`
    
        A ValueAdapter that does not modify the value, useful for Adapters that only change the property name.
    """
    def __init__(self, string: str): ...
    def adaptValueSent(self, parameterValue: cern.japc.value.ParameterValue) -> cern.japc.value.ParameterValue:
        """
            Description copied from interface: :meth:`~cern.japc.core.spi.adaptation.ParameterValueSentAdapter.adaptValueSent`
            Adapts the :code:`ParameterValue` sent to the adapter parameter to make the :code:`ParameterValue` sent to the adapted
            parameter.
        
            Specified by:
                :meth:`~cern.japc.core.spi.adaptation.ParameterValueSentAdapter.adaptValueSent`Â in
                interfaceÂ :class:`~cern.japc.core.spi.adaptation.ParameterValueSentAdapter`
        
            Parameters:
                valueSent (cern.japc.value.ParameterValue): the :code:`ParameterValue` sent to the adapter parameter
        
            Returns:
                the :code:`ParameterValue` sent to the adapted parameter
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("cern.japc.core.spi.adaptation")``.

    AbstractAcquiredParameterValueAdapter: typing.Type[AbstractAcquiredParameterValueAdapter]
    AcquiredParameterValueAdapter: typing.Type[AcquiredParameterValueAdapter]
    AdapterParameter: typing.Type[AdapterParameter]
    ConstantParameter: typing.Type[ConstantParameter]
    FieldFilteringParameterAdapter: typing.Type[FieldFilteringParameterAdapter]
    IdentityValueAdapter: typing.Type[IdentityValueAdapter]
    ParameterValueSentAdapter: typing.Type[ParameterValueSentAdapter]
    ViewParameter: typing.Type[ViewParameter]
    VirtualParameterUtil: typing.Type[VirtualParameterUtil]
